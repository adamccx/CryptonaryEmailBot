#!/usr/bin/env python3
"""
Cryptonary Email Generator Bot - V5
Clean flow with consistent Quick Edit / Enhance / Approve at every stage.
"""

import os, json, ssl, urllib.request, time

TELEGRAM_TOKEN = "8611455908:AAH2zTch0Nf5tM590-_ouPZO2at-sqDpj_Y"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_KEY", "YOUR_ANTHROPIC_KEY_HERE")
ssl._create_default_https_context = ssl._create_unverified_context

BOOK_KNOWLEDGE = """
COPYWRITING PRINCIPLES (Applied to Crypto Email Marketing)

FROM HORMOZI ($100M OFFERS / $100M LEADS):
- Value Equation: Sell transformation not product. CTA = outcome: "Know What's Coming" not "Upgrade to Pro"
- Grand Slam: Stack specific concrete value bullets before the ask. Each bullet = its own mini-dream.
- Pain/Dream/Fix: Open on pain, paint dream, position Pro as mechanism.
- Urgency must be real and tied to actual market events. Never manufactured.
- Specificity sells: numbers, dates, exact levels beat vague claims.
- Hook-Retain-Reward: Subject stops scroll, body earns each next sentence, reader rewarded even from free email.

FROM CASHVERTISING (WHITMAN):
- LF8 Desires: Freedom from fear in downturns. Superiority/winning in rallies. Social approval = community size. Comfortable living = financial freedom.
- Fear works when threat is credible + reader vulnerable + solution clear. Always pair with immediate solution.
- Repeat core benefit 3 times in different forms. Bucket brigade keeps momentum.
- People buy better versions of themselves, not products.

FROM CIALDINI (INFLUENCE / PRE-SUASION):
- Reciprocity: Give genuine value first, then the ask.
- Consistency: Anchor their identity as a serious investor.
- Social Proof: Show what Pro members are DOING, not just what they have access to.
- Authority: Track record proof, not claims.
- Scarcity: Information scarcity is most powerful.
- Pre-Suasion: Subject primes emotional state. Everything before CTA builds to one emotional state.
- Unity: Joining Pro = joining a group, not buying a product.

FROM OGILVY:
- Subject line is everything. Promise benefit, provoke curiosity, or announce news. Specifics beat generalities.
- Every sentence earns the next.
- P.S. is second most-read element. Use it for the sharpest proof point.
- Facts tell. Stories sell. Put reader inside the story.
- One CTA, one action, zero friction.
- Honesty builds trust.
"""

CTA_OPTIONS = {
    "free": {
        "upgrade": "Upgrade to Pro",
        "read_free": "Read for Free",
        "discount": "Upgrade with Discount/Offer"
    },
    "pro": {
        "read_report": "Read the Full Report",
        "check_levels": "Check the Levels",
        "upgrade_save": "Upgrade & Save"
    }
}

CTA_INSTRUCTIONS = {
    "free": {
        "upgrade": "CTA pushes reader to upgrade to Pro. Sell the transformation not the subscription. Use Hormozi value equation.",
        "read_free": "CTA invites reader to read specific content for free. Low friction. Frame as a gift.",
        "discount": "CTA offers a specific discount on Pro. Make the saving concrete. Use Cialdini scarcity and urgency."
    },
    "pro": {
        "read_report": "CTA directs Pro member to read the full report. Direct, no friction. Frame as time-sensitive.",
        "check_levels": "CTA sends Pro member to check updated market levels. Frame as the specific numbers they need right now.",
        "upgrade_save": "CTA offers a saving on Pro — annual plan, loyalty discount, or limited offer. Make the saving concrete."
    }
}

VOICE_GUIDE = """You are writing emails and social content for Adam, Co-Founder of Cryptonary, a crypto research and education platform with 300K+ newsletter subscribers.

ADAM'S VOICE RULES:
- Open emails with "Gm [Name],"
- Short punchy sentences. Very short. Sometimes one word. Or two.
- Bold key phrases using *asterisks* notation
- Never use em dashes. Use full stops or line breaks instead.
- Bullets use the bullet point symbol
- Free email sign off: Talk soon, / Adam / Co-Founder, Cryptonary
- Pro email sign off: Adam / Co-Founder, Cryptonary
- Always include a punchy P.S. line
- No fluff. Every line earns its place.
- Rhetorical questions work well.
- Numbers and specifics make it real.
- Write like talking to one person.
- 2-3 sentences max per paragraph.

""" + BOOK_KNOWLEDGE

performance_data = {}
user_state = {}

# ── HELPERS ───────────────────────────────────────────────────────

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
    s = s.replace("```json", "").replace("```", "").strip()
    start = next((i for i, c in enumerate(s) if c in ('[', '{')), -1)
    if start >= 0: s = s[start:]
    end = next((i for i in range(len(s)-1, -1, -1) if s[i] in (']', '}')), -1)
    if end >= 0: s = s[:end+1]
    return s

def extract_text(v):
    if isinstance(v, str): return v
    if isinstance(v, dict):
        for k in ["body", "content", "email"]:
            if k in v: return v[k]
        return "\n\n".join(str(x) for x in v.values())
    return str(v)

def email_action_keyboard():
    return [
        [{"text": "Quick Edit", "callback_data": "quick_edit"},
         {"text": "Enhance", "callback_data": "enhance"},
         {"text": "Approve", "callback_data": "approve_emails"}]
    ]

def social_action_keyboard():
    return [
        [{"text": "Quick Edit", "callback_data": "social_quick_edit"},
         {"text": "Enhance", "callback_data": "social_enhance"},
         {"text": "Approve", "callback_data": "approve_social"}]
    ]

def mark_complete_keyboard():
    return [
        [{"text": "New email set", "callback_data": "start_over"},
         {"text": "Log performance", "callback_data": "log_perf_start"}]
    ]

def get_perf_context(chat_id):
    records = performance_data.get(chat_id, [])
    if not records: return ""
    ctx = "\n\nPERFORMANCE DATA FROM PAST EMAILS:\n"
    for r in records[-10:]:
        ctx += "- Subject: " + r.get("subject","") + " | Open: " + str(r.get("open_rate","?")) + "% | Click: " + str(r.get("click_rate","?")) + "%\n"
    high = [r for r in records if r.get("open_rate", 0) > 30]
    if high:
        ctx += "\nHIGH PERFORMERS (>30% open):\n"
        for r in high:
            ctx += "- " + r.get("subject","") + " (" + str(r.get("open_rate","?")) + "% open)\n"
    return ctx

# ── FLOW ──────────────────────────────────────────────────────────

def ask_context(chat_id):
    user_state[chat_id]["stage"] = "awaiting_context_choice"
    keyboard = [
        [{"text": "Yes — I have extra context", "callback_data": "context_yes"}],
        [{"text": "No — just the report", "callback_data": "context_no"}]
    ]
    send(chat_id, "*Any extra context to factor in?*\n\n_Promos, discounts, Inner Circle open, upcoming events, factoids, PSAs..._", keyboard)

def gen_angles(chat_id):
    report = user_state[chat_id].get("report", "")
    context = user_state[chat_id].get("context", "")
    perf = get_perf_context(chat_id)
    prompt = "REPORT:\n" + report
    if context: prompt += "\n\nEXTRA CONTEXT:\n" + context
    prompt += perf
    prompt += "\n\nGenerate exactly 4 distinct email angles. Different emotional lenses or hook strategies. Apply copywriting principles. If performance data exists, weight toward high-performing patterns. Return ONLY a valid JSON array of 4 strings. No preamble, no markdown."
    send(chat_id, "Finding angles...")
    try:
        angles = json.loads(clean_json(claude(prompt)))
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

def gen_hooks(chat_id):
    angle = user_state[chat_id].get("selected_angle", "")
    report = user_state[chat_id].get("report", "")
    context = user_state[chat_id].get("context", "")
    perf = get_perf_context(chat_id)
    prompt = "REPORT:\n" + report
    if context: prompt += "\n\nEXTRA CONTEXT:\n" + context
    prompt += perf
    prompt += "\n\nAngle: " + angle + "\n\nWrite exactly 4 distinct subject line + preview combos. Ogilvy: promise benefit, provoke curiosity, or announce news. Specific numbers where possible. If performance data exists, learn from high performers. Return ONLY a valid JSON array of 4 objects with keys subject and preview. No markdown."
    send(chat_id, "Writing hooks...")
    try:
        hooks = json.loads(clean_json(claude(prompt)))
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

def ask_free_cta(chat_id):
    user_state[chat_id]["stage"] = "pick_free_cta"
    keyboard = [[{"text": v, "callback_data": "cta_free_" + k}] for k, v in CTA_OPTIONS["free"].items()]
    send(chat_id, "*Free email CTA:*", keyboard)

def ask_pro_cta(chat_id):
    user_state[chat_id]["stage"] = "pick_pro_cta"
    keyboard = [[{"text": v, "callback_data": "cta_pro_" + k}] for k, v in CTA_OPTIONS["pro"].items()]
    send(chat_id, "*Pro email CTA:*", keyboard)

def gen_emails(chat_id):
    state = user_state[chat_id]
    report = state.get("report", "")
    context = state.get("context", "")
    angle = state.get("selected_angle", "")
    hook = state.get("selected_hook", {})
    free_cta = state.get("free_cta", "upgrade")
    pro_cta = state.get("pro_cta", "read_report")
    prompt = "Write BOTH a Free email and a Pro email for Cryptonary. Apply all copywriting principles.\n\n"
    prompt += "REPORT:\n" + report
    if context: prompt += "\n\nEXTRA CONTEXT (weave in naturally):\n" + context
    prompt += "\n\nAngle: " + angle
    prompt += "\nSubject: " + hook.get("subject", "")
    prompt += "\nPreview: " + hook.get("preview", "")
    prompt += "\n\nFREE EMAIL CTA: " + CTA_INSTRUCTIONS["free"].get(free_cta, "")
    prompt += "\nPRO EMAIL CTA: " + CTA_INSTRUCTIONS["pro"].get(pro_cta, "")
    prompt += "\n\nReturn a JSON object with keys free and pro. Each value is the complete email as a plain string including Subject Line and Preview at top then full body. Return ONLY valid raw JSON."
    send(chat_id, "Writing your emails...")
    try:
        emails = json.loads(clean_json(claude(prompt, max_tokens=2500)))
        state["current_emails"] = emails
        state["stage"] = "emails_ready"
        state["email_record"] = {
            "subject": hook.get("subject", ""),
            "angle": angle,
            "date": time.strftime("%Y-%m-%d"),
            "timestamp": time.strftime("%Y-%m-%d %H:%M")
        }
        if "free" in emails:
            send(chat_id, "*FREE EMAIL*\n\n" + extract_text(emails["free"]))
        if "pro" in emails:
            send(chat_id, "*PRO EMAIL*\n\n" + extract_text(emails["pro"]))
        send(chat_id, "Emails ready. What would you like to do?", email_action_keyboard())
    except Exception as e:
        send(chat_id, "Error: " + str(e))

# ── QUICK EDIT ────────────────────────────────────────────────────

def ask_quick_edit(chat_id, mode="email"):
    user_state[chat_id]["stage"] = "awaiting_quick_edit"
    user_state[chat_id]["quick_edit_mode"] = mode
    send(chat_id, "*Quick Edit*\n\nType your instruction:\n\n_Examples: Make the opening more urgent / Shorten the P.S. / Make the CTA stronger / Add a specific number to paragraph 2_")

def apply_quick_edit(chat_id, instruction):
    state = user_state[chat_id]
    mode = state.get("quick_edit_mode", "email")
    if mode == "social":
        content = state.get("current_social", "")
        social_type = state.get("current_social_type", "social content")
        send(chat_id, "Applying edit to " + social_type + "...")
        try:
            result = claude(
                "Edit this Cryptonary " + social_type + " based on this instruction: " + instruction +
                "\n\nKeep Adam's voice intact. Only change what the instruction specifies.\n\nCONTENT:\n" + content +
                "\n\nReturn the edited content as a plain string, not JSON.",
                max_tokens=1500
            )
            state["current_social"] = result
            state["stage"] = "social_ready"
            send(chat_id, "*EDITED " + social_type.upper() + "*\n\n" + result)
            send(chat_id, "Edit applied.", social_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e))
            state["stage"] = "social_ready"
    else:
        emails = state.get("current_emails", {})
        free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
        pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
        email_text = ""
        if free_email: email_text += "FREE EMAIL:\n" + free_email + "\n\n"
        if pro_email: email_text += "PRO EMAIL:\n" + pro_email
        send(chat_id, "Applying edit...")
        try:
            raw = claude(
                "Edit these Cryptonary emails based on this instruction: " + instruction +
                "\n\nKeep Adam's voice intact. Only change what the instruction specifies.\n\nEMAILS:\n" + email_text +
                "\n\nReturn a JSON object with keys free and pro. Return ONLY valid raw JSON.",
                max_tokens=2500
            )
            edited = json.loads(clean_json(raw))
            state["current_emails"] = edited
            state["stage"] = "emails_ready"
            if "free" in edited:
                send(chat_id, "*EDITED FREE EMAIL*\n\n" + extract_text(edited["free"]))
            if "pro" in edited:
                send(chat_id, "*EDITED PRO EMAIL*\n\n" + extract_text(edited["pro"]))
            send(chat_id, "Edit applied.", email_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e))
            state["stage"] = "emails_ready"

# ── ENHANCE ───────────────────────────────────────────────────────

def gen_enhance(chat_id, mode="email"):
    state = user_state[chat_id]
    if mode == "social":
        content = state.get("current_social", "")
        social_type = state.get("current_social_type", "social content")
        send(chat_id, "Analysing " + social_type + "...")
        try:
            raw = claude(
                "Analyse this Cryptonary " + social_type + " and generate exactly 6 specific improvement suggestions. Each must reference a copywriting principle and give a concrete fix.\n\nCONTENT:\n" + content +
                "\n\nReturn ONLY a valid JSON array of 6 objects with keys: id (1-6), principle, issue, fix. No markdown.",
                max_tokens=900
            )
            suggestions = json.loads(clean_json(raw))
            state["enhance_suggestions"] = suggestions
            state["selected_enhancements"] = []
            state["enhance_mode"] = "social"
            state["stage"] = "enhance_select"
            text = "*Choose improvements:*\n_(tap to select, then Apply)_\n\n"
            keyboard = []
            for s in suggestions:
                keyboard.append([{"text": "[ ] " + str(s["id"]) + ". [" + s["principle"] + "] " + s["issue"], "callback_data": "enh_" + str(s["id"])}])
            keyboard.append([{"text": "Apply selected", "callback_data": "apply_enhancements"}])
            keyboard.append([{"text": "Skip", "callback_data": "skip_enhance"}])
            send(chat_id, text, keyboard)
        except Exception as e:
            send(chat_id, "Error: " + str(e))
    else:
        emails = state.get("current_emails", {})
        free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
        pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
        email_text = ""
        if free_email: email_text += "FREE EMAIL:\n" + free_email + "\n\n"
        if pro_email: email_text += "PRO EMAIL:\n" + pro_email
        send(chat_id, "Analysing emails against copywriting principles...")
        try:
            raw = claude(
                "Analyse these Cryptonary emails against copywriting principles (Hormozi, Cashvertising LF8, Cialdini, Ogilvy). Generate exactly 8 specific, actionable improvement suggestions.\n\nEmails:\n" + email_text +
                "\n\nReturn ONLY a valid JSON array of 8 objects with keys: id (1-8), principle, issue, fix. No markdown.",
                max_tokens=1200
            )
            suggestions = json.loads(clean_json(raw))
            state["enhance_suggestions"] = suggestions
            state["selected_enhancements"] = []
            state["enhance_mode"] = "email"
            state["stage"] = "enhance_select"
            text = "*Choose improvements:*\n_(tap to select, then Apply)_\n\n"
            keyboard = []
            for s in suggestions:
                keyboard.append([{"text": "[ ] " + str(s["id"]) + ". [" + s["principle"] + "] " + s["issue"], "callback_data": "enh_" + str(s["id"])}])
            keyboard.append([{"text": "Apply selected", "callback_data": "apply_enhancements"}])
            keyboard.append([{"text": "Skip", "callback_data": "skip_enhance"}])
            send(chat_id, text, keyboard)
        except Exception as e:
            send(chat_id, "Error: " + str(e))

def toggle_enhancement(chat_id, enh_id, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_enhancements", [])
    suggestions = state.get("enhance_suggestions", [])
    if enh_id in selected: selected.remove(enh_id)
    else: selected.append(enh_id)
    state["selected_enhancements"] = selected
    keyboard = []
    for s in suggestions:
        is_sel = s["id"] in selected
        label = ("[x] " if is_sel else "[ ] ") + str(s["id"]) + ". [" + s["principle"] + "] " + s["issue"]
        keyboard.append([{"text": label, "callback_data": "enh_" + str(s["id"])}])
    keyboard.append([{"text": "Apply selected (" + str(len(selected)) + ")", "callback_data": "apply_enhancements"}])
    keyboard.append([{"text": "Skip", "callback_data": "skip_enhance"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def apply_enhancements(chat_id):
    state = user_state[chat_id]
    selected_ids = state.get("selected_enhancements", [])
    suggestions = state.get("enhance_suggestions", [])
    mode = state.get("enhance_mode", "email")
    if not selected_ids:
        send(chat_id, "No improvements selected. Tap numbers to select first.")
        return
    selected = [s for s in suggestions if s["id"] in selected_ids]
    improvements = "\n".join([str(s["id"]) + ". [" + s["principle"] + "] " + s["fix"] for s in selected])
    send(chat_id, "Applying " + str(len(selected_ids)) + " improvements...")
    if mode == "social":
        content = state.get("current_social", "")
        social_type = state.get("current_social_type", "social content")
        try:
            result = claude(
                "Rewrite this Cryptonary " + social_type + " applying these improvements only:\n\n" + improvements +
                "\n\nORIGINAL:\n" + content +
                "\n\nReturn the improved content as a plain string, not JSON.",
                max_tokens=1500
            )
            state["current_social"] = result
            state["stage"] = "social_ready"
            send(chat_id, "*IMPROVED " + social_type.upper() + "*\n\n" + result)
            send(chat_id, str(len(selected_ids)) + " improvements applied.", social_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e))
            state["stage"] = "social_ready"
    else:
        emails = state.get("current_emails", {})
        free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
        pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
        email_text = ""
        if free_email: email_text += "FREE EMAIL:\n" + free_email + "\n\n"
        if pro_email: email_text += "PRO EMAIL:\n" + pro_email
        try:
            raw = claude(
                "Rewrite these Cryptonary emails applying these improvements only. Keep Adam's voice intact.\n\nIMPROVEMENTS:\n" + improvements +
                "\n\nORIGINAL EMAILS:\n" + email_text +
                "\n\nReturn a JSON object with keys free and pro. Return ONLY valid raw JSON.",
                max_tokens=2500
            )
            improved = json.loads(clean_json(raw))
            state["current_emails"] = improved
            state["stage"] = "emails_ready"
            if "free" in improved:
                send(chat_id, "*IMPROVED FREE EMAIL*\n\n" + extract_text(improved["free"]))
            if "pro" in improved:
                send(chat_id, "*IMPROVED PRO EMAIL*\n\n" + extract_text(improved["pro"]))
            send(chat_id, str(len(selected_ids)) + " improvements applied.", email_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e))
            state["stage"] = "emails_ready"

# ── SOCIAL CONTENT ────────────────────────────────────────────────

def show_social_menu(chat_id):
    keyboard = [
        [{"text": "Reel Script (45-60s)", "callback_data": "social_reel"}],
        [{"text": "Carousel (5-8 slides)", "callback_data": "social_carousel"}],
        [{"text": "Story — Single slide", "callback_data": "social_story_single"}],
        [{"text": "Story — Multi slide", "callback_data": "social_story_multi"}],
        [{"text": "Mark Complete", "callback_data": "mark_complete"}]
    ]
    send(chat_id, "*Social Content*\n\nChoose a format:", keyboard)

def gen_social(chat_id, social_type):
    state = user_state[chat_id]
    report = state.get("report", "")
    context = state.get("context", "")
    angle = state.get("selected_angle", "")
    emails = state.get("current_emails", {})
    free_ref = extract_text(emails.get("free", ""))[:400] if "free" in emails else ""

    base = "SOURCE:\nReport: " + report
    if context: base += "\nContext: " + context
    base += "\nAngle: " + angle
    if free_ref: base += "\nFree email reference: " + free_ref

    send(chat_id, "Generating " + social_type + "...")
    try:
        if social_type == "Reel Script":
            prompt = "Write a 45-60 second Instagram Reel voiceover script for Cryptonary.\n\n" + base + "\n\nRULES:\n- 120-140 words total\n- First 3 seconds must stop the scroll — pattern interrupt hook\n- Format: voiceover text on left, [B-roll instruction] on right for each line\n- Build to a CTA: follow Cryptonary for more\n- Adam's voice: punchy, direct, data-led\n- No fluff\n\nReturn as plain string."
            max_tok = 800
        elif social_type == "Carousel":
            prompt = "Create an Instagram Carousel for Cryptonary. Mix of bold text and visual direction.\n\n" + base + "\n\nRULES:\n- 5-8 slides including cover and CTA final slide\n- Format: SLIDE N: [headline — max 8 words] + [visual direction in brackets]\n- Cover must stop the scroll\n- Mix bold text statements, data slides, and list slides\n- Each slide earns the next swipe\n- Final slide: follow for more / link in bio\n\nReturn as plain string."
            max_tok = 900
        elif social_type == "Story (single)":
            prompt = "Create a single Instagram Story slide for Cryptonary.\n\n" + base + "\n\nRULES:\n- Format: SLIDE 1: [main text — max 15 words] + [background/visual direction in brackets] + [optional poll or sticker suggestion]\n- Vertical full screen — text must be large and readable\n- Urgent, direct, makes reader act now\n- CTA: swipe up or link in bio\n\nReturn as plain string."
            max_tok = 400
        else:
            prompt = "Create a multi-slide Instagram Story for Cryptonary.\n\n" + base + "\n\nRULES:\n- 3-5 slides\n- Format per slide: SLIDE N: [main text — max 15 words] + [background/visual direction in brackets] + [optional poll or sticker]\n- Cliffhanger between each slide to drive tap-throughs\n- Final slide: swipe up or link in bio\n- Adam's voice: urgent, direct\n\nReturn as plain string."
            max_tok = 700

        result = claude(prompt, max_tokens=max_tok)
        state["current_social"] = result
        state["current_social_type"] = social_type
        state["stage"] = "social_ready"
        send(chat_id, "*" + social_type.upper() + "*\n\n" + result)
        send(chat_id, "Done. What would you like to do?", social_action_keyboard())
    except Exception as e:
        send(chat_id, "Error: " + str(e))

# ── PERFORMANCE TRACKING ──────────────────────────────────────────

def start_log_performance(chat_id):
    user_state[chat_id]["stage"] = "log_subject"
    send(chat_id, "*Log Performance*\n\nEnter the subject line of the email you want to log:")

def log_step(chat_id, text):
    state = user_state[chat_id]
    stage = state.get("stage")
    if stage == "log_subject":
        state["log_subject"] = text
        state["stage"] = "log_date"
        send(chat_id, "Date generated? (e.g. 2026-03-21)")
    elif stage == "log_date":
        state["log_date"] = text
        state["stage"] = "log_open"
        send(chat_id, "Open rate? (e.g. 28)")
    elif stage == "log_open":
        try:
            state["log_open"] = float(text)
            state["stage"] = "log_click"
            send(chat_id, "Click rate? (e.g. 4.2)")
        except:
            send(chat_id, "Please enter a number, e.g. 28")
    elif stage == "log_click":
        try:
            click = float(text)
            record = {
                "subject": state.get("log_subject", ""),
                "date": state.get("log_date", ""),
                "open_rate": state.get("log_open", 0),
                "click_rate": click
            }
            if chat_id not in performance_data:
                performance_data[chat_id] = []
            performance_data[chat_id].append(record)
            records = performance_data[chat_id]
            avg_open = sum(r.get("open_rate", 0) for r in records) / len(records)
            avg_click = sum(r.get("click_rate", 0) for r in records) / len(records)
            msg = "*Performance logged.*\n\n"
            msg += "Subject: _" + record["subject"] + "_\n"
            msg += "Open: " + str(record["open_rate"]) + "% | Click: " + str(click) + "%\n\n"
            msg += "Your averages (" + str(len(records)) + " emails tracked):\n"
            msg += "Open: " + str(round(avg_open, 1)) + "% | Click: " + str(round(avg_click, 1)) + "%"
            if len(records) >= 3:
                best = max(records, key=lambda r: r.get("open_rate", 0))
                msg += "\n\nBest subject: _" + best.get("subject", "") + "_\n(" + str(best.get("open_rate", 0)) + "% open)"
            state["stage"] = "idle"
            send(chat_id, msg, [[{"text": "New email set", "callback_data": "start_over"}]])
        except:
            send(chat_id, "Please enter a number, e.g. 4.2")

def show_stats(chat_id):
    records = performance_data.get(chat_id, [])
    if not records:
        send(chat_id, "No performance data yet. Use /logperformance after sending an email.")
        return
    avg_open = sum(r.get("open_rate", 0) for r in records) / len(records)
    avg_click = sum(r.get("click_rate", 0) for r in records) / len(records)
    best = max(records, key=lambda r: r.get("open_rate", 0))
    msg = "*Performance Summary*\n\n"
    msg += "Emails tracked: " + str(len(records)) + "\n"
    msg += "Avg open: " + str(round(avg_open, 1)) + "% | Avg click: " + str(round(avg_click, 1)) + "%\n\n"
    msg += "*Best subject:*\n_" + best.get("subject", "") + "_\n"
    msg += str(best.get("open_rate", 0)) + "% open / " + str(best.get("click_rate", 0)) + "% click\n\n"
    msg += "*Recent:*\n"
    for r in records[-5:]:
        msg += "- " + r.get("subject", "")[:45] + "\n  " + str(r.get("open_rate", "?")) + "% open / " + str(r.get("click_rate", "?")) + "% click\n"
    send(chat_id, msg)

# ── MESSAGE + CALLBACK HANDLERS ───────────────────────────────────

def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "").strip()
    if not text: return

    if text == "/start":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "*Cryptonary Email Generator V5*\n\nPaste your report to get started.\n\n/stats — view performance\n/logperformance — log email results\n/help — how to use")
        return
    if text == "/stats":
        show_stats(chat_id)
        return
    if text == "/logperformance":
        user_state.setdefault(chat_id, {})
        start_log_performance(chat_id)
        return
    if text == "/help":
        send(chat_id, "*How to use:*\n\n1. Paste your report\n2. Answer context question\n3. Pick angle\n4. Pick hook\n5. Pick Free CTA + Pro CTA\n6. Emails generated\n7. Quick Edit / Enhance / Approve\n8. Approve → social content option\n9. Quick Edit / Enhance / Approve on socials\n10. Approve → Mark Complete\n\n/logperformance — log results after sending\n/stats — performance summary")
        return

    stage = user_state.get(chat_id, {}).get("stage", "idle")

    if stage in ["log_subject", "log_date", "log_open", "log_click"]:
        log_step(chat_id, text)
        return

    if stage == "awaiting_context_text":
        user_state[chat_id]["context"] = text
        user_state[chat_id]["stage"] = "pick_angle"
        send(chat_id, "Context added.")
        gen_angles(chat_id)
        return

    if stage == "awaiting_quick_edit":
        user_state[chat_id]["stage"] = user_state[chat_id].get("pre_edit_stage", "emails_ready")
        apply_quick_edit(chat_id, text)
        return

    if len(text) > 100:
        user_state[chat_id] = {"stage": "awaiting_context_choice", "report": text}
        ask_context(chat_id)
    else:
        send(chat_id, "Paste your full report to get started, or /start to reset.")

def handle_callback(cb):
    chat_id = cb["message"]["chat"]["id"]
    message_id = cb["message"]["message_id"]
    data = cb["data"]
    tg("answerCallbackQuery", {"callback_query_id": cb["id"]})
    state = user_state.get(chat_id, {})

    if data == "start_over":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "Ready. Paste your next report.")

    elif data == "context_yes":
        user_state[chat_id]["stage"] = "awaiting_context_text"
        send(chat_id, "Type your extra context:")

    elif data == "context_no":
        user_state[chat_id]["context"] = ""
        user_state[chat_id]["stage"] = "pick_angle"
        gen_angles(chat_id)

    elif data == "regen_angles":
        gen_angles(chat_id)

    elif data.startswith("angle_"):
        idx = int(data.split("_")[1])
        angles = state.get("angles", [])
        if idx < len(angles):
            user_state[chat_id]["selected_angle"] = angles[idx]
            send(chat_id, "Angle: _" + angles[idx] + "_")
            gen_hooks(chat_id)

    elif data == "regen_hooks":
        gen_hooks(chat_id)

    elif data.startswith("hook_"):
        idx = int(data.split("_")[1])
        hooks = state.get("hooks", [])
        if idx < len(hooks):
            user_state[chat_id]["selected_hook"] = hooks[idx]
            send(chat_id, "Hook: _" + hooks[idx]["subject"] + "_")
            ask_free_cta(chat_id)

    elif data.startswith("cta_free_"):
        key = data.replace("cta_free_", "")
        user_state[chat_id]["free_cta"] = key
        send(chat_id, "Free CTA: _" + CTA_OPTIONS["free"][key] + "_")
        ask_pro_cta(chat_id)

    elif data.startswith("cta_pro_"):
        key = data.replace("cta_pro_", "")
        user_state[chat_id]["pro_cta"] = key
        send(chat_id, "Pro CTA: _" + CTA_OPTIONS["pro"][key] + "_")
        gen_emails(chat_id)

    elif data == "regen_emails":
        gen_emails(chat_id)

    elif data == "quick_edit":
        user_state[chat_id]["pre_edit_stage"] = "emails_ready"
        ask_quick_edit(chat_id, mode="email")

    elif data == "social_quick_edit":
        user_state[chat_id]["pre_edit_stage"] = "social_ready"
        ask_quick_edit(chat_id, mode="social")

    elif data == "enhance":
        gen_enhance(chat_id, mode="email")

    elif data == "social_enhance":
        gen_enhance(chat_id, mode="social")

    elif data.startswith("enh_"):
        enh_id = int(data.split("_")[1])
        toggle_enhancement(chat_id, enh_id, message_id)

    elif data == "apply_enhancements":
        apply_enhancements(chat_id)

    elif data == "skip_enhance":
        mode = state.get("enhance_mode", "email")
        if mode == "social":
            state["stage"] = "social_ready"
            send(chat_id, "Enhancement skipped.", social_action_keyboard())
        else:
            state["stage"] = "emails_ready"
            send(chat_id, "Enhancement skipped.", email_action_keyboard())

    elif data == "approve_emails":
        state["stage"] = "emails_approved"
        keyboard = [
            [{"text": "Yes — create social content", "callback_data": "social_yes"}],
            [{"text": "No — mark complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, "Emails approved. Want to create social content to accompany them?", keyboard)

    elif data == "social_yes":
        show_social_menu(chat_id)

    elif data.startswith("social_"):
        type_map = {
            "social_reel": "Reel Script",
            "social_carousel": "Carousel",
            "social_story_single": "Story (single)",
            "social_story_multi": "Story (multi)"
        }
        if data in type_map:
            gen_social(chat_id, type_map[data])

    elif data == "approve_social":
        state["stage"] = "social_approved"
        keyboard = [
            [{"text": "Generate another format", "callback_data": "social_yes"}],
            [{"text": "Mark Complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, "Social content approved. Generate another format or mark complete?", keyboard)

    elif data == "mark_complete":
        send(chat_id, "Set complete. What would you like to do next?", mark_complete_keyboard())

    elif data == "log_perf_start":
        start_log_performance(chat_id)

# ── POLLING LOOP ──────────────────────────────────────────────────

def poll():
    offset = 0
    print("Cryptonary Bot V5 running.")
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
