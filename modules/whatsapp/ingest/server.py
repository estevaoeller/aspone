import hashlib
import hmac
import json
import logging
import os
import re
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

import psycopg
from psycopg.types.json import Jsonb

DATABASE_URL = os.environ["DATABASE_URL"]
TOKEN = os.environ["INGEST_TOKEN"]
OUTPUT_ROOT = Path(os.environ.get("MARKDOWN_ROOT", "/data/markdown"))
TZ = ZoneInfo("America/Sao_Paulo")
MAX_BYTES = 16 * 1024 * 1024
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def connect():
    return psycopg.connect(DATABASE_URL)


def init_schema():
    with connect() as db:
        with db.cursor() as c:
            c.execute("""
                CREATE TABLE IF NOT EXISTS raw_events (
                    id BIGSERIAL PRIMARY KEY,
                    received_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                    source TEXT NOT NULL DEFAULT 'waha',
                    session TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    fingerprint TEXT NOT NULL UNIQUE,
                    payload JSONB NOT NULL
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    session TEXT NOT NULL,
                    message_id TEXT NOT NULL,
                    conversation_id TEXT NOT NULL,
                    sender_id TEXT,
                    sent_at TIMESTAMPTZ NOT NULL,
                    from_me BOOLEAN NOT NULL DEFAULT FALSE,
                    body TEXT NOT NULL DEFAULT '',
                    has_media BOOLEAN NOT NULL DEFAULT FALSE,
                    media JSONB,
                    revoked BOOLEAN NOT NULL DEFAULT FALSE,
                    edited BOOLEAN NOT NULL DEFAULT FALSE,
                    payload JSONB NOT NULL,
                    PRIMARY KEY (session, message_id)
                )
            """)
            c.execute("CREATE INDEX IF NOT EXISTS messages_conversation_time ON messages(session, conversation_id, sent_at)")
            c.execute("""
                CREATE TABLE IF NOT EXISTS contact_names (
                    session TEXT NOT NULL,
                    contact_id TEXT NOT NULL,
                    name TEXT NOT NULL DEFAULT '',
                    push_name TEXT NOT NULL DEFAULT '',
                    refreshed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                    PRIMARY KEY (session, contact_id)
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS chat_names (
                    session TEXT NOT NULL,
                    chat_id TEXT NOT NULL,
                    name TEXT NOT NULL DEFAULT '',
                    refreshed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
                    PRIMARY KEY (session, chat_id)
                )
            """)



def message_id(payload):
    mid = payload.get("id")
    if isinstance(mid, (dict, list)):
        return json.dumps(mid, sort_keys=True, ensure_ascii=False)
    return str(mid or "")


def short_id(mid):
    parts = str(mid or "").split("_")
    return parts[2] if len(parts) >= 3 and parts[0] in ("true", "false") else str(mid or "")


def mutation_target(kind, payload):
    field = "editedMessageId" if kind == "message.edited" else "revokedMessageId"
    value = payload.get(field)
    return value if isinstance(value, str) and value else ""


def mutation_context(payload):
    result = set()
    for obj in (payload, payload.get("before"), payload.get("after")):
        if isinstance(obj, dict):
            for key in ("chatId", "from", "to"):
                value = obj.get(key)
                if isinstance(value, str) and value:
                    result.add(value)
    return sorted(result)


def resolve_mutation(cur, session, kind, payload):
    target = mutation_target(kind, payload)
    contexts = mutation_context(payload)
    if not target or not contexts:
        return None
    cur.execute("""
        SELECT message_id, conversation_id, sent_at
        FROM messages
        WHERE session=%s AND conversation_id=ANY(%s)
          AND (message_id=%s OR
               (split_part(message_id, '_', 1) IN ('true','false')
                AND split_part(message_id, '_', 3)=%s))
        LIMIT 2
    """, (session, contexts, target, short_id(target)))
    rows = cur.fetchall()
    return rows[0] if len(rows) == 1 else None


def reconcile_message(cur, session, mid):
    """Apply known mutations in recorded order; revocation remains sticky."""
    cur.execute("""
        SELECT event_type, payload->'payload'
        FROM raw_events
        WHERE session=%s AND (
          (event_type='message.edited' AND payload->'payload'->>'editedMessageId' IN (%s,%s))
          OR (event_type='message.revoked' AND payload->'payload'->>'revokedMessageId' IN (%s,%s))
        )
        ORDER BY id
    """, (session, mid, short_id(mid), mid, short_id(mid)))
    events = cur.fetchall()
    for kind, payload in events:
        row = resolve_mutation(cur, session, kind, payload)
        if row is None or row[0] != mid:
            continue
        if kind == "message.revoked":
            cur.execute("UPDATE messages SET revoked=TRUE WHERE session=%s AND message_id=%s",
                        (session, mid))
        elif isinstance(payload.get("body"), str):
            cur.execute("UPDATE messages SET body=%s,edited=TRUE WHERE session=%s AND message_id=%s AND NOT revoked",
                        (payload["body"], session, mid))
    return len(events)


def timestamp_of(payload):
    value = payload.get("timestamp") or time.time()
    try:
        value = float(value)
        if value > 1e11:
            value /= 1000
        return datetime.fromtimestamp(value, timezone.utc)
    except (ValueError, TypeError, OverflowError):
        return datetime.now(timezone.utc)


def chat_of(payload, envelope):
    me = ((envelope.get("me") or {}).get("id") or "")
    chat = payload.get("chatId") or payload.get("from") or payload.get("to") or ""
    if payload.get("fromMe") and chat == me and payload.get("to"):
        chat = payload["to"]
    return str(chat)


def output_file(session, chat, day):
    key = hashlib.sha256((session + ":" + chat).encode()).hexdigest()[:14]
    return OUTPUT_ROOT / ("chat-" + key) / (day + ".md")


def clean_name(value):
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())[:160].replace("<", "&lt;").replace(">", "&gt;")


def render_day(db, session, chat, day):
    with db.cursor() as c:
        c.execute("""
            SELECT m.message_id, m.sender_id, m.sent_at, m.from_me, m.body,
                   m.has_media, m.media, m.revoked, m.edited,
                   COALESCE(NULLIF(cn.name, ''), NULLIF(cn.push_name, '')),
                   ch.name, m.payload
            FROM messages m
            LEFT JOIN contact_names cn
              ON (cn.session=m.session AND cn.contact_id=m.sender_id)
            LEFT JOIN chat_names ch
              ON (ch.session=m.session AND ch.chat_id=m.conversation_id)
            WHERE m.session=%s AND m.conversation_id=%s
              AND (m.sent_at AT TIME ZONE 'America/Sao_Paulo')::date = %s::date
            ORDER BY m.sent_at ASC, m.message_id ASC
        """, (session, chat, day))
        items = c.fetchall()

    destination = output_file(session, chat, day)
    if not items:
        return
    title = clean_name(items[0][10]) or "Conversa WhatsApp"
    destination.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---", "type: whatsapp_conversation",
        "source: waha",
        "session: " + json.dumps(session, ensure_ascii=False),
        "conversation_id: " + json.dumps(chat, ensure_ascii=False),
        "conversation_name: " + json.dumps(title if title != "Conversa WhatsApp" else "", ensure_ascii=False),
        "date: " + json.dumps(day),
        "---", "",
        "# " + title + " | " + day, "",
        "ID da conversa: `" + chat + "`", "",
    ]
    for mid, sender, sent_at, from_me, body, has_media, media, revoked, edited, resolved, _, payload in items:
        local = sent_at.astimezone(TZ).strftime("%Y-%m-%d %H:%M:%S %Z")
        extra = payload if isinstance(payload, dict) else {}
        nested = extra.get("_data") if isinstance(extra.get("_data"), dict) else {}
        fallback = (extra.get("pushName") or extra.get("notifyName") or
                    nested.get("pushName") or nested.get("notifyName"))
        if from_me:
            who = "Eu"
        else:
            who = clean_name(resolved) or clean_name(fallback) or clean_name(sender) or "Remetente não identificado"
        label = " (editada)" if edited else ""
        lines.extend(["### " + local + " | " + who + label,
                      "Mensagem: `" + mid + "`"])
        if sender:
            lines.append("ID do remetente: `" + str(sender) + "`")
        lines.append("")
        if revoked:
            lines.append("*Mensagem apagada*")
        elif body:
            fence = "`" * (max([len(x) for x in re.findall(r"`+", body)] + [2]) + 1)
            lines.extend([fence + "text", body, fence])
        if has_media:
            mimetype = (media or {}).get("mimetype") if isinstance(media, dict) else None
            lines.append("*Mídia presente" + (": " + str(mimetype) if mimetype else "") + ". Arquivo não extraído.*")
        if not body and not has_media and not revoked:
            lines.append("*Mensagem sem conteúdo textual extraído.*")
        lines.append("")
    pending = destination.with_name(destination.name + "." + os.urandom(8).hex() + ".tmp")
    pending.write_text("\n".join(lines) + "\n", encoding="utf-8")
    pending.replace(destination)


def process(envelope, raw):
    session = str(envelope.get("session") or "default")
    kind = str(envelope.get("event") or "unknown")
    payload = envelope.get("payload") or {}
    if not isinstance(payload, dict):
        payload = {}
    fingerprint = hashlib.sha256(raw).hexdigest()

    with connect() as db:
        with db.cursor() as cur:
            lock_id = short_id(message_id(payload)) if kind == "message.any" else (
                short_id(mutation_target(kind, payload)) if kind in ("message.edited", "message.revoked") else "")
            if lock_id:
                cur.execute("SELECT pg_advisory_xact_lock(hashtext(%s), hashtext(%s))", (session, lock_id))
            cur.execute("""
                INSERT INTO raw_events(session, event_type, fingerprint, payload)
                VALUES (%s, %s, %s, %s) ON CONFLICT(fingerprint) DO NOTHING
            """, (session, kind, fingerprint, Jsonb(envelope)))
            fresh = cur.rowcount > 0

            if kind == "message.any":
                mid = message_id(payload)
                chat = chat_of(payload, envelope)
                if mid and chat:
                    from_me = bool(payload.get("fromMe", False))
                    sender = payload.get("participant") or (
                        (envelope.get("me") or {}).get("id") if from_me else payload.get("from")
                    )
                    dt = timestamp_of(payload)
                    media = payload.get("media") if isinstance(payload.get("media"), dict) else {}
                    cur.execute("""
                        INSERT INTO messages
                          (session,message_id,conversation_id,sender_id,sent_at,from_me,body,has_media,media,payload)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT(session,message_id) DO UPDATE SET
                          conversation_id=EXCLUDED.conversation_id,
                          sender_id=EXCLUDED.sender_id,
                          body=CASE WHEN messages.edited OR messages.revoked THEN messages.body ELSE EXCLUDED.body END,
                          has_media=EXCLUDED.has_media,
                          media=EXCLUDED.media,
                          payload=EXCLUDED.payload
                    """, (session, mid, chat, sender, dt, from_me,
                          str(payload.get("body") or ""), bool(payload.get("hasMedia")), Jsonb(media),
                          Jsonb(payload)))
                    reconcile_message(cur, session, mid)
                    db.commit()
                    render_day(db, session, chat, dt.astimezone(TZ).date().isoformat())
                    return fresh
            elif kind in ("message.edited", "message.revoked"):
                result = resolve_mutation(cur, session, kind, payload)
                if result:
                    mid, chat, dt = result
                    reconcile_message(cur, session, mid)
                    db.commit()
                    render_day(db, session, chat, dt.astimezone(TZ).date().isoformat())
                    return fresh
    return fresh


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        logging.info("%s %s", self.address_string(), fmt % args)

    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        try:
            with connect() as db:
                db.execute("SELECT 1")
            self.respond(200, {"ok": True})
        except Exception:
            self.respond(503, {"ok": False})

    def respond(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/webhook":
            self.send_error(404)
            return
        provided = self.headers.get("X-Watchtower-Token", "")
        if not hmac.compare_digest(provided, TOKEN):
            self.respond(403, {"error": "forbidden"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_BYTES:
                self.respond(413, {"error": "invalid size"})
                return
            raw = self.rfile.read(length)
            envelope = json.loads(raw)
            if not isinstance(envelope, dict):
                raise ValueError("event must be object")
            fresh = process(envelope, raw)
            self.respond(200, {"ok": True, "new_event": fresh})
        except (json.JSONDecodeError, ValueError):
            self.respond(400, {"error": "invalid event"})
        except Exception:
            logging.exception("Failed to store webhook")
            self.respond(500, {"error": "storage failure"})


if __name__ == "__main__":
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for attempt in range(30):
        try:
            init_schema()
            break
        except Exception:
            logging.warning("Waiting for database")
            time.sleep(2)
    else:
        raise RuntimeError("Database unavailable")
    logging.info("Watchtower WhatsApp collector ready")
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
