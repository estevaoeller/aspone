"""Confere a projeção Markdown contra a tabela de mensagens preservada em PostgreSQL."""
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from server import connect, output_file

TZ = ZoneInfo("America/Sao_Paulo")
MARKER = re.compile(r"^Mensagem: `(.*)`$")
def main():
    expected = {}
    with connect() as db:
        with db.cursor() as cur:
            cur.execute("""SELECT session,conversation_id,message_id,sent_at,has_media
                          FROM messages ORDER BY session,conversation_id,sent_at""")
            records = cur.fetchall()
            cur.execute("SELECT event_type,count(*) FROM raw_events GROUP BY event_type")
            events = dict(cur.fetchall())

    for session,chat,mid,dt,_ in records:
        day = dt.astimezone(TZ).date().isoformat()
        path=output_file(session,chat,day)
        expected.setdefault(path,Counter())[(mid)] += 1

    missing,extra,missing_files = [],[],[]
    observed_md = list(Path("/data/markdown").rglob("*.md"))
    for path, counts in expected.items():
        if not path.is_file():
            missing_files.append(str(path.relative_to("/data/markdown")))
            continue
        found = Counter()
        for line in path.read_text(encoding="utf-8").splitlines():
            match = MARKER.match(line)
            if match:
                found[match.group(1)] += 1
        short = str(path.relative_to("/data/markdown"))
        for key, value in (counts-found).items():
            missing.append({"file":short,"id":key,"count":value})
        for key, value in (found-counts).items():
            extra.append({"file":short,"id":key,"count":value})

    unknown_files = [str(p.relative_to("/data/markdown")) for p in observed_md if p not in expected]
    ok = not (missing or extra or missing_files or unknown_files)
    print(json.dumps({
        "status": "OK" if ok else "ERROR",
        "messages_db": len(records),
        "conversations": len(set((x[0],x[1]) for x in records)),
        "markdown_expected_files": len(expected),
        "markdown_files_found": len(observed_md),
        "events": events,
        "missing_files": missing_files[:10],
        "missing_messages": missing[:10],
        "extra_messages": extra[:10],
        "unknown_md_files": unknown_files[:10],
    }, ensure_ascii=False, indent=2))
    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
