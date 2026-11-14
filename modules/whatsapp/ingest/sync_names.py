"""Read-only enrichment of archived WhatsApp messages with WAHA contact/chat names.
Original messages and raw events remain unchanged.
"""
import json
import logging
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

from server import connect, render_day

URL = os.environ.get("WAHA_BASE_URL", "http://waha:3000").rstrip("/")
KEY_FILE = Path(os.environ.get("WAHA_API_KEY_FILE", "/run/secrets/waha_api_key"))
LOG = logging.getLogger("names")


def fetch(endpoint):
    key = KEY_FILE.read_text(encoding="utf-8").strip()
    request = urllib.request.Request(
        URL + endpoint,
        headers={"X-Api-Key": key, "Accept": "application/json"},
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=12) as response:
        return json.load(response)


def text_name(value):
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())[:160]


def sync():
    if not KEY_FILE.is_file():
        LOG.warning("WAHA name key unavailable, skipping")
        return {"contacts_updated": 0, "chats_updated": 0}

    with connect() as db:
        with db.cursor() as cur:
            cur.execute("""
                SELECT session, sender_id, MAX(from_me::int) = 1
                FROM messages
                WHERE sender_id IS NOT NULL AND session <> 'export'
                GROUP BY session, sender_id
            """)
            sender_rows = cur.fetchall()
            cur.execute("""
                SELECT DISTINCT session, conversation_id
                FROM messages WHERE session <> 'export'
            """)
            chat_rows = cur.fetchall()

    by_session = defaultdict(lambda: {"senders": set(), "chats": set()})
    for session, sender, is_me in sender_rows:
        if not is_me:
            by_session[session]["senders"].add(sender)
    for session, chat in chat_rows:
        by_session[session]["chats"].add(chat)

    contacts_changed = defaultdict(set)
    chats_changed = defaultdict(set)

    with connect() as db:
        for session, targets in by_session.items():
            for contact_id in sorted(targets["senders"]):
                params = urllib.parse.urlencode({"contactId": contact_id, "session": session})
                try:
                    contact = fetch("/api/contacts?" + params)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as ex:
                    LOG.warning("Contact lookup failed (%s): %s", type(ex).__name__, session)
                    continue
                if not isinstance(contact, dict):
                    continue
                name = text_name(contact.get("name"))
                push = text_name(contact.get("pushname") or contact.get("pushName"))
                if not name and not push:
                    continue
                with db.cursor() as cur:
                    cur.execute("""
                        INSERT INTO contact_names (session, contact_id, name, push_name, refreshed_at)
                        VALUES (%s, %s, %s, %s, now())
                        ON CONFLICT (session, contact_id) DO UPDATE SET
                            name=EXCLUDED.name, push_name=EXCLUDED.push_name,
                            refreshed_at=now()
                        WHERE (contact_names.name, contact_names.push_name)
                          IS DISTINCT FROM (EXCLUDED.name, EXCLUDED.push_name)
                        RETURNING contact_id
                    """, (session, contact_id, name, push))
                    if cur.fetchone():
                        contacts_changed[session].add(contact_id)
                db.commit()

            wanted = targets["chats"]
            if not wanted:
                continue
            matched = set()
            for offset in range(0, 5000, 100):
                params = urllib.parse.urlencode({"limit": 100, "offset": offset})
                try:
                    chats = fetch("/api/" + urllib.parse.quote(session, safe="") + "/chats?" + params)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as ex:
                    LOG.warning("Chat lookup failed (%s): %s", type(ex).__name__, session)
                    break
                if not isinstance(chats, list):
                    break
                for chat in chats:
                    if not isinstance(chat, dict):
                        continue
                    chat_id = chat.get("id")
                    if chat_id not in wanted:
                        continue
                    matched.add(chat_id)
                    display = text_name(chat.get("name"))
                    if not display:
                        continue
                    with db.cursor() as cur:
                        cur.execute("""
                            INSERT INTO chat_names (session, chat_id, name, refreshed_at)
                            VALUES (%s, %s, %s, now())
                            ON CONFLICT (session, chat_id) DO UPDATE SET
                                name=EXCLUDED.name, refreshed_at=now()
                            WHERE chat_names.name IS DISTINCT FROM EXCLUDED.name
                            RETURNING chat_id
                        """, (session, chat_id, display))
                        if cur.fetchone():
                            chats_changed[session].add(chat_id)
                    db.commit()
                if matched >= wanted or len(chats) < 100:
                    break

        updated_days = set()
        with db.cursor() as cur:
            for session in by_session:
                senders = list(contacts_changed[session])
                chats = list(chats_changed[session])
                if not senders and not chats:
                    continue
                cur.execute("""
                    SELECT DISTINCT conversation_id,
                        (sent_at AT TIME ZONE 'America/Sao_Paulo')::date
                    FROM messages
                    WHERE session=%s
                      AND (sender_id = ANY(%s::text[]) OR conversation_id = ANY(%s::text[]))
                """, (session, senders, chats))
                updated_days.update((session, chat, str(day)) for chat, day in cur.fetchall())
        for session, chat, day in updated_days:
            render_day(db, session, chat, day)

    counts = {
        "contacts_updated": sum(map(len, contacts_changed.values())),
        "chats_updated": sum(map(len, chats_changed.values())),
        "markdown_refreshed": len(updated_days),
    }
    LOG.info("Contact/chat name refresh: %s", counts)
    return counts


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(json.dumps(sync(), ensure_ascii=False))
