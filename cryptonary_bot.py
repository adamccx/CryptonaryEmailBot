#!/usr/bin/env python3
"""
Cryptonary Email Generator - Telegram Bot
Deploy on Railway: https://railway.app
"""

import os
import json
import ssl
import urllib.request
import urllib.error
import urllib.parse
import time

TELEGRAM_TOKEN = "8611455908:AAH2zTch0Nf5tM590-_ouPZO2at-sqDpj_Y"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_KEY", "YOUR_ANTHROPIC_KEY_HERE")

ssl._create_default_https_context = ssl._create_unverified_context

VOICE_GUIDE = """You are writing emails for Adam, Co-Founder of Cryptonary, a crypto research and education platform with 300K+ newsletter subscribers. Follow Adam's exact voice rules:

- Open with "Gm [Name],"
- Short punchy sentences. Very short. Sometimes one word. Or two.
- Bold key phrases using *asterisks* notation
- Never use em dashes. Use full stops or line breaks instead.
- Bullets use the bullet symbol
- Free email sign off: Talk soon, / Adam / Co-Founder, Cryptonary
- Pro email sign off: Adam / Co-Founder, Cryptonary
- Always include a punchy P.S. line
- No fluff. Every line earns its place.
- Rhetorical questions work well.
- Numbers and specifics make it real.
- Write like talking to one person.
- 2-3 sentences max per paragraph.

FREE EMAIL: tease the content, give partial value, create curiosity gap, CTA to upgrade to Pro.
PRO EMAIL: full analysis, exact levels, complete strategy, clear directional view."""

# In-memory state per user
user_state = {}

def tg(method, data):
    url = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/" + method
    payload = json.dumps(data).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        print("Telegram error:", e)
        return None

def send(chat_id, text, keyboard=None):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if keyboard:
        data["reply_markup"] = {"inline_keyboard": keyboard}
    tg("sendMessage", data)

def claude(prompt, max_tokens=900):
    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": max_tokens,
        "system": VOICE_GUIDE,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read())
        return "".join(c.get("text", "") for c in data["content"])

def clean_json(s):
    return s.replace("```json", "").replace("```", "").strip()

def gen_angles(chat_id, report):
    send(chat_id, "Finding angles...")
    try:
        raw = claude("Here is a Cryptonary research report:\n\n" + report + "\n\nGenerate exactly 4 distinct email angles. Each should be a different emotional lens or hook strategy. Return ONLY a valid JSON array of 4 strings. No preamble, no markdown, just the raw JSON array.")
        angles = json.loads(clean_json(raw))
        user_state[chat_id]["angles"] = angles
        user_state[chat_id]["stage"] = "pick_angle"

        text = "*Pick an angle:*\n\n"
        keyboard = []
        for i, a in enumerate(angles):
            text += "*" + str(i+1) + ".* " + a + "\n\n"
            keyboard.append([{"text": str(i+1), "callback_data": "angle_" + str(i)}])
        keyboard.append([{"text": "Regenerate angles", "callback_data": "regen_angles"}])
        send(chat_id, text, keyboard)
    except Exception as e:
        send(chat_id, "Error generating angles: " + str(e))

def gen_hooks(chat_id, angle):
    send(chat_id, "Writing hooks...")
    report = user_state[chat_id]["report"]
    try:
        raw = claude("Report:\n" + report + "\n\nAngle: " + angle + "\n\nWrite exactly 4 distinct subject line + preview text combos. Make each feel different: data-driven, question-led, bold statement, curiosity gap. Return ONLY a valid JSON array of 4 objects with keys subject and preview. No markdown, just raw JSON.")
        hooks = json.loads(clean_json(raw))
        user_state[chat_id]["hooks"] = hooks
        user_state[chat_id]["stage"] = "pick_hook"

        text = "*Pick a hook:*\n\n"
        keyboard = []
        for i, h in enumerate(hooks):
            text += "*" + str(i+1) + ".* " + h["subject"] + "\n_" + h["preview"] + "_\n\n"
            keyboard.append([{"text": str(i+1), "callback_data": "hook_" + str(i)}])
        keyboard.append([{"text": "Regenerate hooks", "callback_data": "regen_hooks"}])
        send(chat_id, text, keyboard)
    except Exception as e:
        send(chat_id, "Error generating hooks: " + str(e))

def gen_emails(chat_id, hook, email_type="both"):
    send(chat_id, "Writing your emails...")
    state = user_state[chat_id]
    report = state["report"]
    angle = state["selected_angle"]

    if email_type == "both":
        ti = "Write BOTH a Free email and a Pro email. Return a JSON object with keys free and pro."
    elif email_type == "free":
        ti = "Write a Free email only. Return a JSON object with key free."
    else:
        ti = "Write a Pro email only. Return a JSON object with key pro."

    try:
        raw = claude(
            "Write Cryptonary emails based on:\nReport: " + report +
            "\nAngle: " + angle +
            "\nSubject: " + hook["subject"] +
            "\nPreview: " + hook["preview"] +
            "\n\n" + ti +
            "\n\nEach value is the complete email as a plain string including Subject Line and Preview at top then full body. Return ONLY valid raw JSON.",
            max_tokens=2500
        )
        emails = json.loads(clean_json(raw))

        def extract(v):
            if isinstance(v, str): return v
            if isinstance(v, dict):
                for k in ["body", "content", "email"]:
                    if k in v: return v[k]
                return "\n\n".join(str(x) for x in v.values())
            return str(v)

        if "free" in emails:
            send(chat_id, "*FREE EMAIL*\n\n" + extract(emails["free"]))
        if "pro" in emails:
            send(chat_id, "*PRO EMAIL*\n\n" + extract(emails["pro"]))

        keyboard = [
            [{"text": "Regenerate emails", "callback_data": "regen_emails"}],
            [{"text": "Start over", "callback_data": "start_over"}]
        ]
        send(chat_id, "Done. Use the buttons below or paste a new report to start again.", keyboard)
        user_state[chat_id]["stage"] = "done"
        user_state[chat_id]["selected_hook"] = hook

    except Exception as e:
        send(chat_id, "Error generating emails: " + str(e))

def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "").strip()

    if not text:
        return

    if text == "/start":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "👋 *Cryptonary Email Generator*\n\nPaste your report and I'll write your Free + Pro emails in your voice.\n\nJust paste the report text to get started.")
        return

    if text == "/help":
        send(chat_id, "*How to use:*\n\n1. Paste your report\n2. Pick an angle\n3. Pick a hook\n4. Get your emails\n\nType /start to reset.")
        return

    # Any long message is treated as a report
    if len(text) > 100:
        user_state[chat_id] = {"stage": "generating_angles", "report": text}
        gen_angles(chat_id, text)
    else:
        if chat_id not in user_state or user_state[chat_id].get("stage") == "idle":
            send(chat_id, "Paste your report to get started. It should be the full text of your Cryptonary research update.")
        else:
            send(chat_id, "Paste your full report to begin, or use the buttons above.")

def handle_callback(cb):
    chat_id = cb["message"]["chat"]["id"]
    data = cb["data"]
    cb_id = cb["id"]

    tg("answerCallbackQuery", {"callback_query_id": cb_id})

    state = user_state.get(chat_id, {})

    if data == "start_over":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "Ready. Paste your next report.")

    elif data == "regen_angles":
        report = state.get("report", "")
        if report:
            gen_angles(chat_id, report)

    elif data.startswith("angle_"):
        idx = int(data.split("_")[1])
        angles = state.get("angles", [])
        if idx < len(angles):
            angle = angles[idx]
            user_state[chat_id]["selected_angle"] = angle
            user_state[chat_id]["stage"] = "generating_hooks"
            send(chat_id, "Angle selected: _" + angle + "_")
            gen_hooks(chat_id, angle)

    elif data == "regen_hooks":
        angle = state.get("selected_angle", "")
        if angle:
            gen_hooks(chat_id, angle)

    elif data.startswith("hook_"):
        idx = int(data.split("_")[1])
        hooks = state.get("hooks", [])
        if idx < len(hooks):
            hook = hooks[idx]
            user_state[chat_id]["stage"] = "generating_emails"
            send(chat_id, "Hook selected: _" + hook["subject"] + "_")
            gen_emails(chat_id, hook)

    elif data == "regen_emails":
        hook = state.get("selected_hook")
        if hook:
            gen_emails(chat_id, hook)

def get_updates(offset=0):
    try:
        raw = claude  # placeholder
        url = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/getUpdates?timeout=30&offset=" + str(offset)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=35) as r:
            return json.loads(r.read())
    except Exception as e:
        print("getUpdates error:", e)
        return {"ok": False, "result": []}

def poll():
    offset = 0
    print("Bot running. Send a message to @CryptonaryEmailGeneratorBot")
    while True:
        try:
            url = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/getUpdates?timeout=30&offset=" + str(offset)
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=35) as r:
                data = json.loads(r.read())

            if not data.get("ok"):
                time.sleep(5)
                continue

            for update in data.get("result", []):
                offset = update["update_id"] + 1
                if "message" in update:
                    handle_message(update["message"])
                elif "callback_query" in update:
                    handle_callback(update["callback_query"])

        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print("Poll error:", e)
            time.sleep(5)

if __name__ == "__main__":
    if ANTHROPIC_KEY == "YOUR_ANTHROPIC_KEY_HERE":
        print("ERROR: Set your ANTHROPIC_KEY environment variable.")
        print("On Railway: add ANTHROPIC_KEY in the Variables tab.")
    else:
        poll()
