#!/usr/bin/env python3
"""
Cryptonary Email Generator Bot - V3
- Book knowledge layer (Hormozi, Cashvertising, Cialdini, Ogilvy)
- Enhance feature with multi-select improvement suggestions
- CTA type selector (Free + Pro variants)
- Context box for extra info beyond the report
"""

import os, json, ssl, urllib.request, urllib.error, time

TELEGRAM_TOKEN = "8611455908:AAH2zTch0Nf5tM590-_ouPZO2at-sqDpj_Y"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_KEY", "YOUR_ANTHROPIC_KEY_HERE")

ssl._create_default_https_context = ssl._create_unverified_context

BOOK_KNOWLEDGE = """
COPYWRITING PRINCIPLES (Applied to Crypto Email Marketing)

FROM HORMOZI ($100M OFFERS / $100M LEADS):
- Value Equation: Sell transformation not product. CTA = outcome: "Know What's Coming" not "Upgrade to Pro"
- Grand Slam: Stack specific concrete value bullets before the ask. Each bullet = its own mini-dream.
- Pain/Dream/Fix: Open on pain (confusion, fear, missing out), paint dream, position Pro as mechanism
- Urgency must be real and tied to actual market events. Never manufactured.
- Specificity sells: "Bitcoin hit $72,300. Almost to the dollar." beats vague claims.
- Hook-Retain-Reward: Subject stops scroll, body earns each next sentence, reader rewarded even from free email.

FROM CASHVERTISING (WHITMAN):
- LF8 Desires: Lead with the relevant one. Freedom from fear in downturns. Superiority/winning in rallies. Social approval = "370,000 who don't follow hype". Comfortable living = financial freedom dream.
- Fear works when threat is credible + reader is vulnerable + solution is clear. Always pair fear with immediate solution.
- Repeat core benefit 3 times in different forms throughout the email.
- Bucket brigade: "But here's the thing." "Here's what that means for you." Keep momentum.
- People buy better versions of themselves, not products.

FROM CIALDINI (INFLUENCE / PRE-SUASION):
- Reciprocity: Give genuine value first. "Here's your free breakdown. Use it." Then the ask.
- Consistency: "You've been reading these breakdowns every week. You know the quality."
- Social Proof: Show what Pro members are DOING: "Pro members are positioned. They knew where to take profits."
- Authority: Prove via track record. "We called $74K last week. It played out."
- Scarcity: Information scarcity — what Pro members know that free readers don't.
- Pre-Suasion: Subject primes emotional state before they read a word. Everything before CTA builds to one emotional state.
- Unity: Joining Pro = joining a group, not buying a product.

FROM OGILVY:
- Subject line is everything. Must promise benefit, provoke curiosity, or announce news. Specifics beat generalities.
- Every sentence earns the next — the reader on a slide.
- P.S. is second most-read element. Use it for the sharpest proof point or urgency.
- Facts tell. Stories sell. Put reader inside the story.
- One CTA, one action, zero friction.
- Honesty builds trust: admit uncertainty before the reader finds it.
- Long copy works when the reader is genuinely interested.
"""

CTA_OPTIONS = {
    "free": {
        "upgrade": {
            "label": "Upgrade to Pro",
            "instruction": "CTA pushes reader to upgrade to Pro membership. Frame it as the natural next step given what they just read. Use Hormozi value equation — sell the transformation, not the subscription."
        },
        "read_free": {
            "label": "Read for Free",
            "instruction": "CTA invites reader to read a specific piece of content for free. Low friction ask. Frame it as a gift — they get full access to this one report at no cost. Build curiosity about what's inside."
        },
        "discount": {
            "label": "Upgrade with Discount/Offer",
            "instruction": "CTA offers a specific discount or promotional deal on Pro. Create urgency around the offer expiring. Use Cialdini scarcity. Make the math obvious — what they save, what they get."
        }
    },
    "pro": {
        "read_report": {
            "label": "Read the Full Report",
            "instruction": "CTA directs Pro member to read the full report. Direct, no friction. They have access — just send them there. Frame it as time-sensitive given market conditions."
        },
        "check_levels": {
            "label": "Check the Levels",
            "instruction": "CTA sends Pro member to check updated market levels/analysis. Frame it as the specific numbers they need right now. Direct and urgent."
        },
        "upgrade_save": {
            "label": "Upgrade & Save",
            "instruction": "CTA offers Pro members an upsell or renewal with a saving. Could be an annual plan, a loyalty discount, or a limited offer. Make the saving concrete and the urgency real."
        }
    }
}

VOICE_GUIDE = """You are writing emails for Adam, Co-Founder of Cryptonary, a crypto research and education platform with 300K+ newsletter subscribers.

ADAM'S VOICE RULES:
- Open with "Gm [Name],"
- Short punchy sentences. Very short. Sometimes one word. Or two.
- Bold key phrases using *asterisks* notation
- Never use em dashes. Use full stops or line breaks instead.
- Bullets use the bullet point symbol
- Free email sign off: Talk soon, / Adam / Co-Founder, Cryptonary
- Pro email sign off: Adam / Co-Founder, Cryptonary
- Always include a punchy P.S. line
- No fluff. Every line earns its place.
- Rhetorical questions work well.
- Numbers and specifics make it real. Use them.
- Write like talking to one person.
- 2-3 sentences max per paragraph.

FREE EMAIL: tease the content, give partial value, create curiosity gap, use the specified CTA type.
PRO EMAIL: full analysis, exact levels, complete strategy, clear directional view, use the specified CTA type.

""" + BOOK_KNOWLEDGE

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

def extract_text(v):
    if isinstance(v, str): return v
    if isinstance(v, dict):
        for k in ["body", "content", "email"]:
            if k in v: return v[k]
        return "\n\n".join(str(x) for x in v.values())
    return str(v)

def ask_context(chat_id):
    user_state[chat_id]["stage"] = "awaiting_context"
    keyboard = [[{"text": "Skip — no extra context", "callback_data": "skip_context"}]]
    send(chat_id,
        "*Anything else to factor in?*\n\nType any extra context here, or skip if not needed.\n\n_Examples: upcoming promo, discount offer, Inner Circle applications open, interesting factoid, PSA for the community, event happening this week..._",
        keyboard)

def ask_cta_type(chat_id):
    email_type = user_state[chat_id].get("email_type", "both")
    user_state[chat_id]["stage"] = "pick_cta"

    if email_type == "both":
        text = "*Choose your Free email CTA:*"
        options = CTA_OPTIONS["free"]
        prefix = "cta_free_"
    elif email_type == "free":
        text = "*Choose your Free email CTA:*"
        options = CTA_OPTIONS["free"]
        prefix = "cta_free_"
    else:
        text = "*Choose your Pro email CTA:*"
        options = CTA_OPTIONS["pro"]
        prefix = "cta_pro_"

    keyboard = []
    for key, val in options.items():
        keyboard.append([{"text": val["label"], "callback_data": prefix + key}])
    send(chat_id, text, keyboard)

def ask_pro_cta(chat_id):
    user_state[chat_id]["stage"] = "pick_pro_cta"
    text = "*Choose your Pro email CTA:*"
    keyboard = []
    for key, val in CTA_OPTIONS["pro"].items():
        keyboard.append([{"text": val["label"], "callback_data": "cta_pro_" + key}])
    send(chat_id, text, keyboard)

def gen_angles(chat_id):
    report = user_state[chat_id].get("report", "")
    context = user_state[chat_id].get("context", "")
    combined = "REPORT:\n" + report
    if context:
        combined += "\n\nEXTRA CONTEXT:\n" + context

    send(chat_id, "Finding angles...")
    try:
        raw = claude(combined + "\n\nGenerate exactly 4 distinct email angles. Each should be a different emotional lens or hook strategy. Apply copywriting principles — each angle should connect to a specific human desire or emotion. Consider the extra context if provided. Return ONLY a valid JSON array of 4 strings. No preamble, no markdown.")
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
        send(chat_id, "Error: " + str(e))

def gen_hooks(chat_id, angle):
    send(chat_id, "Writing hooks...")
    report = user_state[chat_id].get("report", "")
    context = user_state[chat_id].get("context", "")
    combined = "REPORT:\n" + report
    if context:
        combined += "\n\nEXTRA CONTEXT:\n" + context
    try:
        raw = claude(combined + "\n\nAngle: " + angle + "\n\nWrite exactly 4 distinct subject line + preview text combos. Apply Ogilvy: promise a benefit, provoke curiosity, or announce news. Use specific numbers where possible. Consider any extra context. Return ONLY a valid JSON array of 4 objects with keys subject and preview. No markdown.")
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
        send(chat_id, "Error: " + str(e))

def gen_emails(chat_id):
    state = user_state[chat_id]
    report = state.get("report", "")
    context = state.get("context", "")
    angle = state.get("selected_angle", "")
    hook = state.get("selected_hook", {})
    email_type = state.get("email_type", "both")
    free_cta_key = state.get("free_cta", "upgrade")
    pro_cta_key = state.get("pro_cta", "read_report")

    free_cta = CTA_OPTIONS["free"].get(free_cta_key, CTA_OPTIONS["free"]["upgrade"])
    pro_cta = CTA_OPTIONS["pro"].get(pro_cta_key, CTA_OPTIONS["pro"]["read_report"])

    combined = "REPORT:\n" + report
    if context:
        combined += "\n\nEXTRA CONTEXT (weave this in naturally where relevant):\n" + context

    if email_type == "both":
        ti = "Write BOTH a Free email and a Pro email. Return a JSON object with keys free and pro."
        cta_instruction = "FREE EMAIL CTA: " + free_cta["instruction"] + "\n\nPRO EMAIL CTA: " + pro_cta["instruction"]
    elif email_type == "free":
        ti = "Write a Free email only. Return a JSON object with key free."
        cta_instruction = "FREE EMAIL CTA: " + free_cta["instruction"]
    else:
        ti = "Write a Pro email only. Return a JSON object with key pro."
        cta_instruction = "PRO EMAIL CTA: " + pro_cta["instruction"]

    send(chat_id, "Writing your emails...")
    try:
        raw = claude(
            "Write Cryptonary emails. Apply all copywriting principles — Hormozi value equation in the CTA, Cialdini reciprocity, Ogilvy subject lines and P.S., Cashvertising LF8, Pre-Suasion emotional priming.\n\n" +
            combined +
            "\n\nAngle: " + angle +
            "\nSubject: " + hook.get("subject", "") +
            "\nPreview: " + hook.get("preview", "") +
            "\n\nCTA INSTRUCTIONS:\n" + cta_instruction +
            "\n\n" + ti +
            "\n\nEach value is the complete email as a plain string including Subject Line and Preview at top then full body. Return ONLY valid raw JSON.",
            max_tokens=2500
        )
        emails = json.loads(clean_json(raw))
        state["current_emails"] = emails
        state["stage"] = "done"

        if "free" in emails:
            send(chat_id, "*FREE EMAIL*\n\n" + extract_text(emails["free"]))
        if "pro" in emails:
            send(chat_id, "*PRO EMAIL*\n\n" + extract_text(emails["pro"]))

        keyboard = [
            [{"text": "Enhance", "callback_data": "enhance"}],
            [{"text": "Regenerate", "callback_data": "regen_emails"}, {"text": "Start over", "callback_data": "start_over"}]
        ]
        send(chat_id, "Done. Tap *Enhance* to get improvement suggestions.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))

def gen_enhance_suggestions(chat_id):
    send(chat_id, "Analysing your emails against copywriting principles...")
    state = user_state[chat_id]
    emails = state.get("current_emails", {})
    free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
    pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
    email_text = ""
    if free_email:
        email_text += "FREE EMAIL:\n" + free_email + "\n\n"
    if pro_email:
        email_text += "PRO EMAIL:\n" + pro_email
    try:
        raw = claude(
            "Analyse these Cryptonary emails against the copywriting principles you know (Hormozi, Cashvertising LF8, Cialdini, Ogilvy). Generate exactly 8 specific, actionable improvement suggestions. Each must reference a specific principle, identify what is weak, and give a concrete fix.\n\nEmails:\n" + email_text +
            "\n\nReturn ONLY a valid JSON array of 8 objects with keys: id (1-8), principle (book/concept name), issue (what is weak), fix (specific improvement). No markdown.",
            max_tokens=1200
        )
        suggestions = json.loads(clean_json(raw))
        state["enhance_suggestions"] = suggestions
        state["selected_enhancements"] = []
        state["stage"] = "enhance_select"
        text = "*Choose improvements to apply:*\n_(tap to select, then Apply)_\n\n"
        keyboard = []
        for s in suggestions:
            label = "[ ] " + str(s["id"]) + ". [" + s["principle"] + "] " + s["issue"]
            keyboard.append([{"text": label, "callback_data": "enh_" + str(s["id"])}])
        keyboard.append([{"text": "Apply selected", "callback_data": "apply_enhancements"}])
        keyboard.append([{"text": "Cancel", "callback_data": "cancel_enhance"}])
        send(chat_id, text, keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))

def toggle_enhancement(chat_id, enh_id, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_enhancements", [])
    suggestions = state.get("enhance_suggestions", [])
    if enh_id in selected:
        selected.remove(enh_id)
    else:
        selected.append(enh_id)
    state["selected_enhancements"] = selected
    keyboard = []
    for s in suggestions:
        is_sel = s["id"] in selected
        label = ("[x] " if is_sel else "[ ] ") + str(s["id"]) + ". [" + s["principle"] + "] " + s["issue"]
        keyboard.append([{"text": label, "callback_data": "enh_" + str(s["id"])}])
    keyboard.append([{"text": "Apply selected (" + str(len(selected)) + ")", "callback_data": "apply_enhancements"}])
    keyboard.append([{"text": "Cancel", "callback_data": "cancel_enhance"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def apply_enhancements(chat_id):
    state = user_state[chat_id]
    selected_ids = state.get("selected_enhancements", [])
    suggestions = state.get("enhance_suggestions", [])
    emails = state.get("current_emails", {})
    if not selected_ids:
        send(chat_id, "No improvements selected. Tap the numbered buttons to select first.")
        return
    selected_suggestions = [s for s in suggestions if s["id"] in selected_ids]
    improvements_text = "\n".join([str(s["id"]) + ". [" + s["principle"] + "] " + s["fix"] for s in selected_suggestions])
    free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
    pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
    email_text = ""
    if free_email:
        email_text += "FREE EMAIL:\n" + free_email + "\n\n"
    if pro_email:
        email_text += "PRO EMAIL:\n" + pro_email
    email_type = state.get("email_type", "both")
    if email_type == "both":
        ti = "Return both improved emails as JSON with keys free and pro."
    elif email_type == "free":
        ti = "Return the improved free email as JSON with key free."
    else:
        ti = "Return the improved pro email as JSON with key pro."
    send(chat_id, "Applying " + str(len(selected_ids)) + " improvements...")
    try:
        raw = claude(
            "Rewrite these Cryptonary emails applying the following improvements only. Keep Adam's voice intact. Only change what the improvements specify.\n\nIMPROVEMENTS:\n" + improvements_text +
            "\n\nORIGINAL EMAILS:\n" + email_text +
            "\n\n" + ti + "\n\nReturn ONLY valid raw JSON.",
            max_tokens=2500
        )
        improved = json.loads(clean_json(raw))
        state["current_emails"] = improved
        state["stage"] = "done"
        if "free" in improved:
            send(chat_id, "*IMPROVED FREE EMAIL*\n\n" + extract_text(improved["free"]))
        if "pro" in improved:
            send(chat_id, "*IMPROVED PRO EMAIL*\n\n" + extract_text(improved["pro"]))
        keyboard = [
            [{"text": "Enhance again", "callback_data": "enhance"}],
            [{"text": "Regenerate", "callback_data": "regen_emails"}, {"text": "Start over", "callback_data": "start_over"}]
        ]
        send(chat_id, str(len(selected_ids)) + " improvements applied.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))

def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "").strip()
    if not text: return

    if text == "/start":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "Cryptonary Email Generator V3\n\nPaste your report to get started.")
        return

    if text == "/help":
        send(chat_id, "*How to use:*\n\n1. Paste your report\n2. Add context (optional)\n3. Pick email type\n4. Pick angle\n5. Pick hook\n6. Pick CTA type\n7. Get emails\n8. Enhance with book principles\n\n/start to reset.")
        return

    stage = user_state.get(chat_id, {}).get("stage", "idle")

    if stage == "awaiting_context":
        user_state[chat_id]["context"] = text
        user_state[chat_id]["stage"] = "pick_email_type"
        send(chat_id, "Context added.")
        ask_email_type(chat_id)
        return

    if len(text) > 100:
        user_state[chat_id] = {"stage": "awaiting_context", "report": text}
        ask_context(chat_id)
    else:
        send(chat_id, "Paste your full report to get started, or use /start to reset.")

def ask_email_type(chat_id):
    keyboard = [
        [{"text": "Free + Pro", "callback_data": "etype_both"}],
        [{"text": "Free only", "callback_data": "etype_free"}],
        [{"text": "Pro only", "callback_data": "etype_pro"}]
    ]
    send(chat_id, "*Which emails do you need?*", keyboard)

def handle_callback(cb):
    chat_id = cb["message"]["chat"]["id"]
    message_id = cb["message"]["message_id"]
    data = cb["data"]
    tg("answerCallbackQuery", {"callback_query_id": cb["id"]})
    state = user_state.get(chat_id, {})

    if data == "start_over":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "Ready. Paste your next report.")

    elif data == "skip_context":
        user_state[chat_id]["context"] = ""
        user_state[chat_id]["stage"] = "pick_email_type"
        ask_email_type(chat_id)

    elif data.startswith("etype_"):
        etype = data.split("_")[1]
        user_state[chat_id]["email_type"] = etype
        gen_angles(chat_id)

    elif data == "regen_angles":
        gen_angles(chat_id)

    elif data.startswith("angle_"):
        idx = int(data.split("_")[1])
        angles = state.get("angles", [])
        if idx < len(angles):
            user_state[chat_id]["selected_angle"] = angles[idx]
            send(chat_id, "Angle: _" + angles[idx] + "_")
            gen_hooks(chat_id, angles[idx])

    elif data == "regen_hooks":
        angle = state.get("selected_angle", "")
        if angle: gen_hooks(chat_id, angle)

    elif data.startswith("hook_"):
        idx = int(data.split("_")[1])
        hooks = state.get("hooks", [])
        if idx < len(hooks):
            user_state[chat_id]["selected_hook"] = hooks[idx]
            send(chat_id, "Hook: _" + hooks[idx]["subject"] + "_")
            email_type = state.get("email_type", "both")
            if email_type in ["both", "free"]:
                ask_cta_type(chat_id)
            else:
                ask_pro_cta(chat_id)

    elif data.startswith("cta_free_"):
        cta_key = data.replace("cta_free_", "")
        user_state[chat_id]["free_cta"] = cta_key
        send(chat_id, "Free CTA: _" + CTA_OPTIONS["free"][cta_key]["label"] + "_")
        email_type = state.get("email_type", "both")
        if email_type == "both":
            ask_pro_cta(chat_id)
        else:
            gen_emails(chat_id)

    elif data.startswith("cta_pro_"):
        cta_key = data.replace("cta_pro_", "")
        user_state[chat_id]["pro_cta"] = cta_key
        send(chat_id, "Pro CTA: _" + CTA_OPTIONS["pro"][cta_key]["label"] + "_")
        gen_emails(chat_id)

    elif data == "regen_emails":
        gen_emails(chat_id)

    elif data == "enhance":
        gen_enhance_suggestions(chat_id)

    elif data.startswith("enh_"):
        enh_id = int(data.split("_")[1])
        toggle_enhancement(chat_id, enh_id, message_id)

    elif data == "apply_enhancements":
        apply_enhancements(chat_id)

    elif data == "cancel_enhance":
        state["stage"] = "done"
        keyboard = [
            [{"text": "Enhance", "callback_data": "enhance"}],
            [{"text": "Regenerate", "callback_data": "regen_emails"}, {"text": "Start over", "callback_data": "start_over"}]
        ]
        send(chat_id, "Enhancement cancelled.", keyboard)

def poll():
    offset = 0
    print("Cryptonary Bot V3 running.")
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
            print("Stopped.")
            break
        except Exception as e:
            print("Poll error:", e)
            time.sleep(5)

if __name__ == "__main__":
    if ANTHROPIC_KEY == "YOUR_ANTHROPIC_KEY_HERE":
        print("ERROR: Set ANTHROPIC_KEY environment variable.")
    else:
        poll()
