import argparse
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from psycopg.types.json import Jsonb
from server import connect, init_schema, render_day

ZONE = ZoneInfo("America/Sao_Paulo")
# Supports standard Android and iOS exports in Portuguese.
PATTERNS = [
    re.compile(r"^\[(\d{1,2}/\d{1,2}/\d{2,4}),?\s+(\d{1,2}:\d{2}(?::\d{2})?)\]\s*(.*)$"),
    re.compile(r"^(\d{1,2}/\d{1,2}/\d{2,4}),?\s+(\d{1,2}:\d{2}(?::\d{2})?)\s*[-–]\s*(.*)$"),
]


def parse_datetime(day, hour):
    for fmt in ("%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M",
                "%d/%m/%y %H:%M:%S", "%d/%m/%y %H:%M"):
        try:
            return datetime.strptime(day + " " + hour, fmt).replace(tzinfo=ZONE)
        except ValueError:
            pass
    return None


def parse_messages(content):
    records = []
    current = None
    for line in content.replace("\u200e", "").splitlines():
        found = None
        for pat in PATTERNS:
            found = pat.match(line)
            if found:
                break
        if found:
            dt = parse_datetime(found.group(1), found.group(2))
            if dt is None:
                if current:
                    current["body"] += "\n" + line
                continue
            rest = found.group(3)
            if ": " in rest:
                sender, body = rest.split(": ", 1)
            else:
                sender, body = "Sistema", rest
            current = {"sent_at": dt, "sender": sender, "body": body}
            records.append(current)
        elif current is not None:
            current["body"] += "\n" + line
    return records


def main():
    p = argparse.ArgumentParser(description="Importa exportação TXT do WhatsApp para Watchtower.")
    p.add_argument("file", type=Path)
    p.add_argument("--chat", help="Identificador/nome estável da conversa")
    args = p.parse_args()
    if not args.file.is_file():
        p.error("Arquivo .txt não encontrado")
    chat_name = args.chat or args.file.stem
    chat = "export:" + chat_name
    records = parse_messages(args.file.read_text(encoding="utf-8-sig"))
    if not records:
        raise SystemExit("Nenhuma mensagem identificada. Verifique o formato do TXT.")
    init_schema()
    changed_days = set()
    created = 0
    repeats = defaultdict(int)
    with connect() as db:
        with db.cursor() as cur:
            for record in records:
                dt, sender, body = record["sent_at"], record["sender"], record["body"]
                canonical = json.dumps([chat, dt.isoformat(), sender, body], ensure_ascii=False)
                repeats[canonical] += 1
                unique = canonical + "#" + str(repeats[canonical])
                mid = "export_" + hashlib.sha256(unique.encode()).hexdigest()
                raw = {"source_file": args.file.name, "timestamp": dt.isoformat(),
                       "sender": sender, "body": body, "chat": chat}
                cur.execute("""
                    INSERT INTO raw_events(source,session,event_type,fingerprint,payload)
                    VALUES ('whatsapp_export','export','export.message',%s,%s)
                    ON CONFLICT(fingerprint) DO NOTHING
                """, (mid, Jsonb(raw)))
                cur.execute("""
                    INSERT INTO messages
                    (session,message_id,conversation_id,sender_id,sent_at,from_me,body,has_media,media,payload)
                    VALUES ('export',%s,%s,%s,%s,false,%s,false,%s,%s)
                    ON CONFLICT(session,message_id) DO NOTHING
                """, (mid, chat, sender, dt, body, Jsonb({}), Jsonb(raw)))
                created += cur.rowcount
                changed_days.add(dt.date().isoformat())
        db.commit()
        for day in sorted(changed_days):
            render_day(db, "export", chat, day)
    print(json.dumps({"chat": chat, "parsed": len(records), "new": created,
                      "days": len(changed_days)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
