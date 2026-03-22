#!/usr/bin/env python3
"""
Cryptonary Email Generator Bot - V7
- Subject line A/B testing
- Tone variants (Standard / Aggressive / Empathetic)
- Audience segmentation for Free email (Hot / Warm / Cold)
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

def sanitise(text):
    if not text: return ""
    pairs = [
        (u"\u2018", "'"), (u"\u2019", "'"), (u"\u201a", "'"),
        (u"\u201c", '"'), (u"\u201d", '"'), (u"\u201e", '"'),
        (u"\u2013", "-"), (u"\u2014", "-"), (u"\u2015", "-"),
        (u"\u2026", "..."), (u"\u2022", "-"), (u"\u00b7", "-"),
    ]
    for a, b in pairs:
        text = text.replace(a, b)
    out = []
    for ch in text:
        cp = ord(ch)
        if cp == 10 or cp == 9 or cp == 13:
            out.append(ch)
        elif cp < 32:
            continue
        elif 127 <= cp <= 159:
            continue
        else:
            out.append(ch)
    return "".join(out)


def parse_numbered_list(text, count):
    """Parse a numbered list response into a list of strings."""
    lines = text.strip().split("\n")
    results = []
    current = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Check if line starts with a number
        import re
        m = re.match(r"^\d+\.\s*(.+)", line)
        if m:
            if current:
                results.append(current.strip())
            current = m.group(1)
        else:
            if current:
                current += " " + line
    if current:
        results.append(current.strip())
    # Pad or trim to expected count
    while len(results) < count:
        results.append("Alternative angle " + str(len(results)+1))
    return results[:count]

def parse_hooks(text):
    """Parse numbered SUBJECT/PREVIEW format into list of dicts."""
    import re
    hooks = []
    # Split by numbered entries
    blocks = re.split(r"(?m)^\d+\.\s*", text.strip())
    for block in blocks:
        if not block.strip():
            continue
        subject = ""
        preview = ""
        for line in block.strip().split("\n"):
            line = line.strip()
            if line.upper().startswith("SUBJECT:"):
                subject = line[8:].strip()
            elif line.upper().startswith("PREVIEW:"):
                preview = line[8:].strip()
        if subject:
            hooks.append({"subject": subject, "preview": preview or ""})
    if not hooks:
        # Fallback: try to parse as plain lines
        lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
        for i in range(0, len(lines)-1, 2):
            hooks.append({"subject": lines[i], "preview": lines[i+1] if i+1 < len(lines) else ""})
    while len(hooks) < 4:
        hooks.append({"subject": "Alternative hook " + str(len(hooks)+1), "preview": ""})
    return hooks[:4]

def parse_subject_alternatives(text):
    """Parse numbered PRINCIPLE/SUBJECT/PREVIEW/REASON format."""
    import re
    alts = []
    blocks = re.split(r"(?m)^\d+\.\s*", text.strip())
    for block in blocks:
        if not block.strip():
            continue
        principle = ""
        subject = ""
        preview = ""
        reason = ""
        for line in block.strip().split("\n"):
            line = line.strip()
            if line.upper().startswith("PRINCIPLE:"):
                principle = line[10:].strip()
            elif line.upper().startswith("SUBJECT:"):
                subject = line[8:].strip()
            elif line.upper().startswith("PREVIEW:"):
                preview = line[8:].strip()
            elif line.upper().startswith("REASON:"):
                reason = line[7:].strip()
        if subject:
            alts.append({"principle": principle, "subject": subject, "preview": preview, "reason": reason})
    while len(alts) < 3:
        alts.append({"principle": "Alternative", "subject": "Alternative subject " + str(len(alts)+1), "preview": "", "reason": ""})
    return alts[:3]

def parse_enhance_suggestions(text):
    import re
    suggestions = []
    idx = 1
    current = {"principle": "", "issue": "", "fix": ""}
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        num_match = re.match(r"^(\d+)\.\s*(.*)", line)
        if num_match:
            if current.get("issue") or current.get("fix"):
                suggestions.append({"id": idx, "principle": current["principle"] or "Copywriting", "issue": current["issue"] or current["fix"][:50], "fix": current["fix"] or current["issue"]})
                idx += 1
            current = {"principle": "", "issue": "", "fix": ""}
            rest = num_match.group(2)
            if rest.upper().startswith("PRINCIPLE:"):
                current["principle"] = rest[10:].strip()
        elif line.upper().startswith("PRINCIPLE:"):
            current["principle"] = line[10:].strip()
        elif line.upper().startswith("ISSUE:"):
            current["issue"] = line[6:].strip()
        elif line.upper().startswith("FIX:"):
            current["fix"] = line[4:].strip()
    if current.get("issue") or current.get("fix"):
        suggestions.append({"id": idx, "principle": current["principle"] or "Copywriting", "issue": current["issue"] or current["fix"][:50], "fix": current["fix"] or current["issue"]})
    if not suggestions:
        suggestions = [{"id": 1, "principle": "General", "issue": "Could not parse", "fix": "Please try again"}]
    return suggestions


def parse_delimited_emails(text):
    """Parse FREE/PRO email delimiter format into dict."""
    emails = {}
    if "===FREE EMAIL START===" in text and "===FREE EMAIL END===" in text:
        start = text.find("===FREE EMAIL START===") + len("===FREE EMAIL START===")
        end = text.find("===FREE EMAIL END===")
        emails["free"] = text[start:end].strip()
    if "===PRO EMAIL START===" in text and "===PRO EMAIL END===" in text:
        start = text.find("===PRO EMAIL START===") + len("===PRO EMAIL START===")
        end = text.find("===PRO EMAIL END===")
        emails["pro"] = text[start:end].strip()
    # Fallback: if delimiters not found, try JSON
    if not emails:
        try:
            emails = json.loads(clean_json(text))
        except:
            emails = {"free": text, "pro": text}
    return emails

def parse_delimited_segments(text):
    """Parse HOT/WARM/COLD segment delimiter format into dict."""
    segments = {}
    for key in ["hot", "warm", "cold"]:
        start_tag = "===" + key.upper() + " EMAIL START==="
        end_tag = "===" + key.upper() + " EMAIL END==="
        if start_tag in text and end_tag in text:
            start = text.find(start_tag) + len(start_tag)
            end = text.find(end_tag)
            segments[key] = text[start:end].strip()
    if not segments:
        try:
            segments = json.loads(clean_json(text))
        except:
            segments = {"hot": text, "warm": text, "cold": text}
    return segments

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
         {"text": "Approve", "callback_data": "approve_emails"}],
        [{"text": "Subject Lines", "callback_data": "subject_ab"},
         {"text": "Tone", "callback_data": "tone_menu"},
         {"text": "Segments", "callback_data": "segments"}],
        [{"text": "Length", "callback_data": "length_email"}]
    ]

def social_action_keyboard():
    return [
        [{"text": "Quick Edit", "callback_data": "social_quick_edit"},
         {"text": "Enhance", "callback_data": "social_enhance"},
         {"text": "Approve", "callback_data": "approve_social"}],
        [{"text": "Length", "callback_data": "length_social"}]
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
    report = sanitise(user_state[chat_id].get("report", ""))
    context = sanitise(user_state[chat_id].get("context", ""))
    perf = get_perf_context(chat_id)
    prompt = "REPORT:\n" + report
    if context: prompt += "\n\nEXTRA CONTEXT:\n" + context
    prompt += perf
    prompt += "\n\nGenerate exactly 4 distinct email angles. Different emotional lenses or hook strategies. Apply copywriting principles. If performance data exists, weight toward high-performing patterns. Format your response as a simple numbered list:\n1. [angle one]\n2. [angle two]\n3. [angle three]\n4. [angle four]\nNothing else. No JSON, no preamble."
    send(chat_id, "Finding angles...")
    try:
        raw = claude(prompt)
        angles = parse_numbered_list(raw, 4)
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
    report = sanitise(user_state[chat_id].get("report", ""))
    context = sanitise(user_state[chat_id].get("context", ""))
    perf = get_perf_context(chat_id)
    prompt = "REPORT:\n" + report
    if context: prompt += "\n\nEXTRA CONTEXT:\n" + context
    prompt += perf
    prompt += "\n\nAngle: " + angle + "\n\nWrite exactly 4 distinct subject line + preview text combos. Ogilvy: promise benefit, provoke curiosity, or announce news. Specific numbers where possible. Format each as:\n1. SUBJECT: [subject line]\nPREVIEW: [preview text]\n\n2. SUBJECT: [subject line]\nPREVIEW: [preview text]\n\nAnd so on for all 4. Nothing else."
    send(chat_id, "Writing hooks...")
    try:
        hooks = parse_hooks(claude(prompt))
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
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
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
    prompt += "\n\nWrite the two emails separated by this exact delimiter. Do not use JSON. IMPORTANT: Every email MUST begin with Subject Line: and Preview: on the first two lines.\n\n===FREE EMAIL START===\nSubject Line: [subject here]\nPreview: [preview here]\n\n[complete free email body here]\n===FREE EMAIL END===\n\n===PRO EMAIL START===\nSubject Line: [subject here]\nPreview: [preview here]\n\n[complete pro email body here]\n===PRO EMAIL END==="
    send(chat_id, "Writing your emails...")
    try:
        raw = claude(prompt, max_tokens=2500)
        emails = parse_delimited_emails(raw)
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
                "\n\nReturn the edited emails using this exact format. No JSON:\n\n===FREE EMAIL START===\n[edited free email]\n===FREE EMAIL END===\n\n===PRO EMAIL START===\n[edited pro email]\n===PRO EMAIL END===",
                max_tokens=2500
            )
            edited = parse_delimited_emails(raw)
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
                "\n\nFormat as a numbered list:\n1. PRINCIPLE: [name]\nISSUE: [what is weak]\nFIX: [specific improvement]\n\n2. PRINCIPLE: ...\nAnd so on for all 6. Nothing else.",
                max_tokens=900
            )
            suggestions = parse_enhance_suggestions(raw)
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
                "\n\nFormat as a numbered list:\n1. PRINCIPLE: [name]\nISSUE: [what is weak]\nFIX: [specific improvement]\n\n2. PRINCIPLE: ...\nAnd so on for all 8. Nothing else.",
                max_tokens=1200
            )
            suggestions = parse_enhance_suggestions(raw)
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
                "\n\nReturn the improved emails using this exact format. No JSON:\n\n===FREE EMAIL START===\n[improved free email]\n===FREE EMAIL END===\n\n===PRO EMAIL START===\n[improved pro email]\n===PRO EMAIL END===",
                max_tokens=2500
            )
            improved = parse_delimited_emails(raw)
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

def show_social_source_menu(chat_id):
    state = user_state[chat_id]
    emails = state.get("current_emails", {})
    segments = state.get("current_segments", {})
    keyboard = []
    if "free" in emails:
        keyboard.append([{"text": "Free email", "callback_data": "src_free"}])
    if "pro" in emails:
        keyboard.append([{"text": "Pro email", "callback_data": "src_pro"}])
    if "hot" in segments:
        keyboard.append([{"text": "Free — Hot segment", "callback_data": "src_hot"}])
    if "warm" in segments:
        keyboard.append([{"text": "Free — Warm segment", "callback_data": "src_warm"}])
    if "cold" in segments:
        keyboard.append([{"text": "Free — Cold segment", "callback_data": "src_cold"}])
    keyboard.append([{"text": "Cancel", "callback_data": "back_to_done"}])
    send(chat_id, "*Which email should social content be based on?*", keyboard)

def show_social_format_menu(chat_id):
    state = user_state[chat_id]
    selected = state.get("selected_social_formats", [])
    formats = [
        ("Reel Script (45-60s)", "fmt_reel"),
        ("Carousel (5-8 slides)", "fmt_carousel"),
        ("Story — Single slide", "fmt_story_single"),
        ("Story — Multi slide", "fmt_story_multi"),
    ]
    keyboard = []
    for label, cb in formats:
        is_sel = cb in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + label, "callback_data": cb}])
    keyboard.append([{"text": "Generate selected (" + str(len(selected)) + ")", "callback_data": "gen_social_selected"}])
    keyboard.append([{"text": "Back", "callback_data": "back_to_done"}])
    send(chat_id, "*Select formats to generate:*\n_(tap to select multiple)_", keyboard)

def toggle_social_format(chat_id, fmt_cb, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_social_formats", [])
    if fmt_cb in selected:
        selected.remove(fmt_cb)
    else:
        selected.append(fmt_cb)
    state["selected_social_formats"] = selected
    formats = [
        ("Reel Script (45-60s)", "fmt_reel"),
        ("Carousel (5-8 slides)", "fmt_carousel"),
        ("Story — Single slide", "fmt_story_single"),
        ("Story — Multi slide", "fmt_story_multi"),
    ]
    keyboard = []
    for label, cb in formats:
        is_sel = cb in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + label, "callback_data": cb}])
    keyboard.append([{"text": "Generate selected (" + str(len(selected)) + ")", "callback_data": "gen_social_selected"}])
    keyboard.append([{"text": "Back", "callback_data": "back_to_done"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def get_social_source_text(chat_id):
    state = user_state[chat_id]
    source = state.get("social_source", "free")
    emails = state.get("current_emails", {})
    segments = state.get("current_segments", {})
    if source == "free":
        return extract_text(emails.get("free", ""))
    elif source == "pro":
        return extract_text(emails.get("pro", ""))
    elif source in ["hot", "warm", "cold"]:
        return extract_text(segments.get(source, ""))
    return extract_text(emails.get("free", ""))

def gen_social_selected(chat_id):
    state = user_state[chat_id]
    selected = state.get("selected_social_formats", [])
    if not selected:
        send(chat_id, "No formats selected. Tap the format names to select them first.")
        return
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "")
    source_email = get_social_source_text(chat_id)[:600]
    source_label = state.get("social_source", "free")
    fmt_map = {
        "fmt_reel": ("Reel Script", gen_reel),
        "fmt_carousel": ("Carousel", gen_carousel),
        "fmt_story_single": ("Story (single)", lambda c: gen_story(c, multi=False)),
        "fmt_story_multi": ("Story (multi)", lambda c: gen_story(c, multi=True)),
    }
    send(chat_id, "Generating " + str(len(selected)) + " format(s) based on " + source_label + " email...")
    for fmt_cb in selected:
        if fmt_cb in fmt_map:
            label, fn = fmt_map[fmt_cb]
            fn(chat_id)
    state["selected_social_formats"] = []

def gen_reel(chat_id):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "")
    reel_duration = state.get("reel_duration", 52)
    source_email = get_social_source_text(chat_id)[:500]
    word_count = int(reel_duration * 2.3)
    try:
        result = claude(
            "Write a " + str(reel_duration) + "-second Instagram Reel voiceover script for Cryptonary.\n\n" +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Approximately " + str(word_count) + " words (matches " + str(reel_duration) + "s at natural pace)\n- First 3 seconds must stop the scroll\n- Format: voiceover text | [B-roll instruction] for each line\n- CTA at end: follow Cryptonary\n- Adam's voice: punchy, direct, data-led\n\nReturn as plain string.",
            max_tokens=900
        )
        state["current_social"] = result
        state["current_social_type"] = "Reel Script"
        state["stage"] = "social_ready"
        send(chat_id, "*REEL SCRIPT (" + str(reel_duration) + "s)*\n\n" + result)
        send(chat_id, "Done.", social_action_keyboard())
    except Exception as e:
        send(chat_id, "Error generating reel: " + str(e))

def gen_carousel(chat_id):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "")
    slide_count = state.get("carousel_slides", 6)
    source_email = get_social_source_text(chat_id)[:500]
    try:
        result = claude(
            "Create a " + str(slide_count) + "-slide Instagram Carousel for Cryptonary.\n\n" +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Exactly " + str(slide_count) + " slides including cover and CTA final slide\n- Format: SLIDE N: [headline max 8 words] + [visual direction in brackets]\n- Mix bold text, data slides, list slides\n- Each slide earns the next swipe\n- Final slide: follow for more\n\nReturn as plain string.",
            max_tokens=900
        )
        state["current_social"] = result
        state["current_social_type"] = "Carousel"
        state["stage"] = "social_ready"
        send(chat_id, "*CAROUSEL (" + str(slide_count) + " slides)*\n\n" + result)
        send(chat_id, "Done.", social_action_keyboard())
    except Exception as e:
        send(chat_id, "Error generating carousel: " + str(e))

def gen_story(chat_id, multi=False):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "")
    story_slides = state.get("story_slides", 3) if multi else 1
    source_email = get_social_source_text(chat_id)[:500]
    slide_instruction = str(story_slides) + " slides" if multi else "1 single slide"
    try:
        result = claude(
            "Create an Instagram Story for Cryptonary: " + slide_instruction + "\n\n" +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Format per slide: SLIDE N: [text max 15 words] + [visual/background direction] + [optional sticker]\n- Cliffhanger between slides if multi\n- Final slide: swipe up or link in bio\n- Urgent, direct tone\n\nReturn as plain string.",
            max_tokens=700
        )
        social_type = "Story (" + str(story_slides) + " slides)" if multi else "Story (single)"
        state["current_social"] = result
        state["current_social_type"] = social_type
        state["stage"] = "social_ready"
        send(chat_id, "*" + social_type.upper() + "*\n\n" + result)
        send(chat_id, "Done.", social_action_keyboard())
    except Exception as e:
        send(chat_id, "Error generating story: " + str(e))

# ── LENGTH CONTROL ─────────────────────────────────────────────────

def show_length_menu(chat_id, mode="email"):
    user_state[chat_id]["length_mode"] = mode
    if mode == "email":
        keyboard = [
            [{"text": "Extend (add more detail)", "callback_data": "length_extend"}],
            [{"text": "Shorten (tighten it up)", "callback_data": "length_shorten"}],
            [{"text": "Cancel", "callback_data": "cancel_length"}]
        ]
        send(chat_id, "*Adjust length:*", keyboard)
    else:
        social_type = user_state[chat_id].get("current_social_type", "content")
        is_reel = "Reel" in social_type
        is_carousel = "Carousel" in social_type
        is_story = "Story" in social_type
        keyboard = []
        if is_reel:
            current = user_state[chat_id].get("reel_duration", 52)
            keyboard.append([{"text": "Extend to " + str(current+15) + "s", "callback_data": "reel_extend"}])
            keyboard.append([{"text": "Shorten to " + str(max(20, current-15)) + "s", "callback_data": "reel_shorten"}])
        elif is_carousel:
            current = user_state[chat_id].get("carousel_slides", 6)
            keyboard.append([{"text": "Add 2 more slides (" + str(current+2) + " total)", "callback_data": "carousel_extend"}])
            keyboard.append([{"text": "Remove 2 slides (" + str(max(3, current-2)) + " total)", "callback_data": "carousel_shorten"}])
        elif is_story:
            current = user_state[chat_id].get("story_slides", 3)
            keyboard.append([{"text": "Add a slide (" + str(current+1) + " total)", "callback_data": "story_extend"}])
            keyboard.append([{"text": "Remove a slide (" + str(max(1, current-1)) + " total)", "callback_data": "story_shorten"}])
        else:
            keyboard.append([{"text": "Extend", "callback_data": "length_extend"}])
            keyboard.append([{"text": "Shorten", "callback_data": "length_shorten"}])
        keyboard.append([{"text": "Cancel", "callback_data": "cancel_length"}])
        send(chat_id, "*Adjust length:*", keyboard)

def apply_length(chat_id, direction):
    state = user_state[chat_id]
    mode = state.get("length_mode", "email")
    instruction = "Make this significantly longer. Add more detail, context, and depth. Keep Adam's voice." if direction == "extend" else "Make this significantly shorter. Cut anything that doesn't earn its place. Keep the core message and Adam's voice."
    if mode == "social":
        content = state.get("current_social", "")
        social_type = state.get("current_social_type", "content")
        send(chat_id, ("Extending" if direction == "extend" else "Shortening") + " " + social_type + "...")
        try:
            result = claude(instruction + "\n\nCONTENT:\n" + content + "\n\nReturn as plain string.", max_tokens=1200)
            state["current_social"] = result
            state["stage"] = "social_ready"
            send(chat_id, "*" + social_type.upper() + " — " + direction.upper() + "ED*\n\n" + result)
            send(chat_id, "Done.", social_action_keyboard())
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
        send(chat_id, ("Extending" if direction == "extend" else "Shortening") + " emails...")
        try:
            raw = claude(
                instruction + "\n\nEMAILS:\n" + email_text +
                "\n\nReturn using this format. No JSON:\n\n===FREE EMAIL START===\n[adjusted free email]\n===FREE EMAIL END===\n\n===PRO EMAIL START===\n[adjusted pro email]\n===PRO EMAIL END===",
                max_tokens=2500
            )
            adjusted = parse_delimited_emails(raw)
            state["current_emails"] = adjusted
            state["stage"] = "emails_ready"
            if "free" in adjusted:
                send(chat_id, "*FREE EMAIL — " + direction.upper() + "ED*\n\n" + extract_text(adjusted["free"]))
            if "pro" in adjusted:
                send(chat_id, "*PRO EMAIL — " + direction.upper() + "ED*\n\n" + extract_text(adjusted["pro"]))
            send(chat_id, "Done.", email_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e))
            state["stage"] = "emails_ready"


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


# ── SUBJECT LINE A/B (MULTI-SELECT) ─────────────────────────────

def gen_subject_ab(chat_id):
    state = user_state[chat_id]
    hook = state.get("selected_hook", {})
    current_subject = hook.get("subject", "")
    current_preview = hook.get("preview", "")
    report = sanitise(state.get("report", ""))
    angle = state.get("selected_angle", "")
    send(chat_id, "Generating subject line alternatives...")
    try:
        raw = claude(
            "Generate 3 alternative subject lines for this Cryptonary email. Each uses a different copywriting principle.\n\nReport: " + report[:600] +
            "\nAngle: " + angle +
            "\nCurrent subject: " + current_subject +
            "\n\nPrinciples to use (one each): curiosity gap, fear with specific data, contrarian/counterintuitive.\n\nFormat each option as:\n1. PRINCIPLE: [principle name]\nSUBJECT: [subject line]\nPREVIEW: [preview text]\nREASON: [one sentence]\n\n2. PRINCIPLE: ...\nAnd so on for all 3. Nothing else.",
            max_tokens=700
        )
        alternatives = parse_subject_alternatives(raw)
        state["subject_alternatives"] = alternatives
        state["selected_subjects"] = []
        state["stage"] = "subject_select"
        text = "*Select subject lines to include:*\n_(tap to select multiple, then tap Done)_\n\n"
        text += "*Original:* " + current_subject + "\n_" + current_preview + "_\n\n"
        keyboard = []
        for i, a in enumerate(alternatives):
            text += "*" + str(i+1) + ". [" + a.get("principle","") + "]*\n"
            text += a.get("subject","") + "\n"
            text += "_" + a.get("preview","") + "_\n"
            text += a.get("reason","") + "\n\n"
            keyboard.append([{"text": "[ ] " + str(i+1) + ". " + a.get("subject","")[:40], "callback_data": "sel_sub_" + str(i)}])
        keyboard.append([{"text": "Done — apply selected", "callback_data": "apply_subjects"}])
        keyboard.append([{"text": "Keep original only", "callback_data": "keep_subject"}])
        send(chat_id, text, keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "emails_ready"

def toggle_subject_select(chat_id, idx, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_subjects", [])
    alternatives = state.get("subject_alternatives", [])
    if idx in selected:
        selected.remove(idx)
    else:
        selected.append(idx)
    state["selected_subjects"] = selected
    keyboard = []
    for i, a in enumerate(alternatives):
        is_sel = i in selected
        label = ("[x] " if is_sel else "[ ] ") + str(i+1) + ". " + a.get("subject","")[:40]
        keyboard.append([{"text": label, "callback_data": "sel_sub_" + str(i)}])
    keyboard.append([{"text": "Done — apply selected (" + str(len(selected)) + ")", "callback_data": "apply_subjects"}])
    keyboard.append([{"text": "Keep original only", "callback_data": "keep_subject"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def apply_subjects(chat_id):
    state = user_state[chat_id]
    selected_ids = state.get("selected_subjects", [])
    alternatives = state.get("subject_alternatives", [])
    hook = state.get("selected_hook", {})
    original_subject = hook.get("subject", "")
    original_preview = hook.get("preview", "")
    emails = state.get("current_emails", {})

    # Build subject block with A/B/C labels
    subject_block = "Subject A: " + original_subject + "\nPreview A: " + original_preview
    labels = ["B", "C", "D"]
    for li, idx in enumerate(selected_ids):
        if idx < len(alternatives):
            a = alternatives[idx]
            label = labels[li] if li < len(labels) else str(li+2)
            subject_block += "\nSubject " + label + ": " + a.get("subject","")
            subject_block += "\nPreview " + label + ": " + a.get("preview","")

    # Update both emails to have the multi-subject block at the top
    for key in ["free", "pro"]:
        if key in emails:
            email_str = extract_text(emails[key])
            lines = email_str.split("\n")
            new_lines = []
            skip_next = False
            replaced = False
            for line in lines:
                if not replaced and (line.lower().startswith("subject") or line.lower().startswith("preview")):
                    if not replaced:
                        new_lines.append(subject_block)
                        replaced = True
                    if line.lower().startswith("preview"):
                        skip_next = False
                    continue
                new_lines.append(line)
            if not replaced:
                new_lines.insert(0, subject_block)
            emails[key] = "\n".join(new_lines)

    state["current_emails"] = emails
    state["stage"] = "emails_ready"
    count = len(selected_ids) + 1
    send(chat_id, str(count) + " subject lines applied (A through " + ["B","C","D"][min(len(selected_ids)-1,2)] + " + original).")
    send(chat_id, "What next?", email_action_keyboard())


# ── TONE VARIANTS ─────────────────────────────────────────────────

TONE_DEFS = {
    "standard": ("Standard", "Adam's default voice. Confident, direct, data-led. Short punchy sentences. Balanced urgency."),
    "aggressive": ("Aggressive", "Bull market mode. High urgency, FOMO-driven. The opportunity is NOW. Stronger social proof. Reader will regret missing this. Shorter sentences. More bold statements. Commands not invitations."),
    "empathetic": ("Empathetic", "Bear market mode. Reader is stressed, possibly down on portfolio. Adam is alongside them. Acknowledges the pain. Positions Cryptonary as steady hand in chaos. Calmer tone. Less urgency, more reassurance. CTA is a lifeline not a push.")
}

def show_tone_menu(chat_id):
    keyboard = [
        [{"text": "Standard", "callback_data": "tone_standard"}],
        [{"text": "Aggressive (bull / FOMO)", "callback_data": "tone_aggressive"}],
        [{"text": "Empathetic (bear / stressed reader)", "callback_data": "tone_empathetic"}],
        [{"text": "Cancel", "callback_data": "cancel_tone"}]
    ]
    send(chat_id, "*Choose tone:*\n\nRewrites both emails in the selected tone. Same content, different emotional delivery.", keyboard)

def apply_tone(chat_id, tone_key):
    state = user_state[chat_id]
    tone_label, tone_instruction = TONE_DEFS.get(tone_key, TONE_DEFS["standard"])
    emails = state.get("current_emails", {})
    free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
    pro_email = extract_text(emails.get("pro", "")) if "pro" in emails else ""
    email_text = ""
    if free_email: email_text += "FREE EMAIL:\n" + free_email + "\n\n"
    if pro_email: email_text += "PRO EMAIL:\n" + pro_email
    send(chat_id, "Rewriting in " + tone_label + " tone...")
    try:
        raw = claude(
            "Rewrite these Cryptonary emails in the following tone. Keep same content, facts, structure. Only change emotional delivery and language.\n\nTONE: " + tone_label +
            "\nINSTRUCTION: " + tone_instruction +
            "\n\nEMAILS:\n" + email_text +
            "\n\nRewrite and return the emails using this exact format. No JSON:\n\n===FREE EMAIL START===\n[rewritten free email]\n===FREE EMAIL END===\n\n===PRO EMAIL START===\n[rewritten pro email]\n===PRO EMAIL END===",
            max_tokens=2500
        )
        toned = parse_delimited_emails(raw)
        state["current_emails"] = toned
        state["stage"] = "emails_ready"
        if "free" in toned:
            send(chat_id, "*FREE EMAIL — " + tone_label.upper() + "*\n\n" + extract_text(toned["free"]))
        if "pro" in toned:
            send(chat_id, "*PRO EMAIL — " + tone_label.upper() + "*\n\n" + extract_text(toned["pro"]))
        send(chat_id, tone_label + " tone applied.", email_action_keyboard())
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "emails_ready"
        send(chat_id, "What next?", email_action_keyboard())

# ── AUDIENCE SEGMENTS ─────────────────────────────────────────────

SEG_DEFS = {
    "hot": ("Hot (last 30 days)", "This reader opens every email. Engaged, informed, trusts Cryptonary. Assume shared context. Reference recent calls briefly. Reward loyalty with insider-feeling language. Skip basic explanations. Treat as fellow serious investor. CTA feels like natural next step for someone already bought in."),
    "warm": ("Warm (31-90 days)", "This reader has drifted. Knows Cryptonary but hasn't engaged lately. Re-establish value without being preachy. Reference what they may have missed as opportunity cost not guilt. Make them feel the gap between where they are and where engaged members are. Stronger hook than usual to cut through inertia. CTA feels like re-engaging with something good."),
    "cold": ("Cold (90+ days / never opened)", "Almost a cold lead. May barely remember signing up. No assumed context or knowledge. Re-introduce Cryptonary value proposition clearly. Lead with strongest possible hook: a track record stat, specific win, market call that played out. Feels like a first impression. Lower assumed knowledge. CTA is low-friction and easy to say yes to.")
}

def gen_segments(chat_id):
    state = user_state[chat_id]
    emails = state.get("current_emails", {})
    free_email = extract_text(emails.get("free", "")) if "free" in emails else ""
    if not free_email:
        send(chat_id, "No free email found.", email_action_keyboard())
        return
    free_cta_key = state.get("free_cta", "upgrade")
    free_cta_instruction = CTA_INSTRUCTIONS["free"].get(free_cta_key, "")
    send(chat_id, "Writing 3 segment versions of the Free email...")
    try:
        raw = claude(
            "Rewrite this Cryptonary Free email for 3 different audience segments. Same core content and CTA. Different tone, assumed knowledge, emotional approach.\n\nORIGINAL FREE EMAIL:\n" + free_email +
            "\n\nCTA INSTRUCTION: " + free_cta_instruction +
            "\n\nSEGMENT HOT: " + SEG_DEFS["hot"][1] +
            "\n\nSEGMENT WARM: " + SEG_DEFS["warm"][1] +
            "\n\nSEGMENT COLD: " + SEG_DEFS["cold"][1] +
            "\n\nReturn the 3 segment emails using this exact format. No JSON:\n\n===HOT EMAIL START===\n[hot segment email]\n===HOT EMAIL END===\n\n===WARM EMAIL START===\n[warm segment email]\n===WARM EMAIL END===\n\n===COLD EMAIL START===\n[cold segment email]\n===COLD EMAIL END===",
            max_tokens=3000
        )
        segments = parse_delimited_segments(raw)
        state["current_segments"] = segments
        state["stage"] = "segments_ready"
        for key, (label, _) in SEG_DEFS.items():
            if key in segments:
                send(chat_id, "*FREE EMAIL — " + label.upper() + "*\n\n" + extract_text(segments[key]))
        keyboard = [
            [{"text": "Edit Hot", "callback_data": "seg_edit_hot"},
             {"text": "Edit Warm", "callback_data": "seg_edit_warm"},
             {"text": "Edit Cold", "callback_data": "seg_edit_cold"}],
            [{"text": "Approve segments", "callback_data": "approve_segments"},
             {"text": "Back to emails", "callback_data": "back_to_emails"}]
        ]
        send(chat_id, "3 segment versions ready.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "emails_ready"
        send(chat_id, "What next?", email_action_keyboard())

def ask_seg_edit(chat_id, segment):
    user_state[chat_id]["stage"] = "awaiting_seg_edit"
    user_state[chat_id]["seg_edit_target"] = segment
    label = SEG_DEFS.get(segment, ("",))[0]
    send(chat_id, "*Quick Edit — " + label + "*\n\nType your instruction:")

def apply_seg_edit(chat_id, instruction):
    state = user_state[chat_id]
    segment = state.get("seg_edit_target", "hot")
    segments = state.get("current_segments", {})
    content = extract_text(segments.get(segment, ""))
    label = SEG_DEFS.get(segment, ("",))[0]
    send(chat_id, "Applying edit...")
    try:
        result = claude(
            "Edit this Cryptonary Free email (" + label + " segment). Instruction: " + instruction +
            "\n\nKeep segment tone intact. Only change what instruction specifies.\n\nEMAIL:\n" + content +
            "\n\nReturn edited email as a plain string.",
            max_tokens=1200
        )
        segments[segment] = result
        state["current_segments"] = segments
        state["stage"] = "segments_ready"
        send(chat_id, "*EDITED — " + label.upper() + "*\n\n" + result)
        keyboard = [
            [{"text": "Edit Hot", "callback_data": "seg_edit_hot"},
             {"text": "Edit Warm", "callback_data": "seg_edit_warm"},
             {"text": "Edit Cold", "callback_data": "seg_edit_cold"}],
            [{"text": "Approve segments", "callback_data": "approve_segments"},
             {"text": "Back to emails", "callback_data": "back_to_emails"}]
        ]
        send(chat_id, "Edit applied.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "segments_ready"

# ── MESSAGE + CALLBACK HANDLERS ───────────────────────────────────

def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "").strip()
    if not text: return

    if text == "/start":
        user_state[chat_id] = {"stage": "idle"}
        send(chat_id, "*Cryptonary Email Generator V7*\n\nPaste your report to get started.\n\n/stats — view performance\n/logperformance — log email results\n/help — how to use")
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

    if stage == "awaiting_seg_edit":
        apply_seg_edit(chat_id, text)
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
        send(chat_id, "Emails approved. Want to create social content?", keyboard)

    elif data == "social_yes":
        state["selected_social_formats"] = []
        show_social_source_menu(chat_id)

    elif data == "src_free":
        state["social_source"] = "free"
        show_social_format_menu(chat_id)

    elif data == "src_pro":
        state["social_source"] = "pro"
        show_social_format_menu(chat_id)

    elif data == "src_hot":
        state["social_source"] = "hot"
        show_social_format_menu(chat_id)

    elif data == "src_warm":
        state["social_source"] = "warm"
        show_social_format_menu(chat_id)

    elif data == "src_cold":
        state["social_source"] = "cold"
        show_social_format_menu(chat_id)

    elif data.startswith("fmt_"):
        toggle_social_format(chat_id, data, message_id)

    elif data == "gen_social_selected":
        gen_social_selected(chat_id)



    elif data == "approve_social":
        state["stage"] = "social_approved"
        keyboard = [
            [{"text": "Generate another format", "callback_data": "social_yes"}],
            [{"text": "Mark Complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, "Social content approved. Generate another format or mark complete?", keyboard)

    elif data == "subject_ab":
        gen_subject_ab(chat_id)

    elif data.startswith("use_subject_"):
        idx = int(data.replace("use_subject_", ""))
        apply_subject(chat_id, idx)

    elif data == "keep_subject":
        state["stage"] = "emails_ready"
        send(chat_id, "Keeping current subject.", email_action_keyboard())

    elif data == "tone_menu":
        show_tone_menu(chat_id)

    elif data.startswith("tone_") and data != "tone_menu":
        tone_key = data.replace("tone_", "")
        if tone_key in ["standard", "aggressive", "empathetic"]:
            apply_tone(chat_id, tone_key)

    elif data == "cancel_tone":
        state["stage"] = "emails_ready"
        send(chat_id, "Tone change cancelled.", email_action_keyboard())

    elif data == "segments":
        gen_segments(chat_id)

    elif data == "seg_edit_hot":
        ask_seg_edit(chat_id, "hot")

    elif data == "seg_edit_warm":
        ask_seg_edit(chat_id, "warm")

    elif data == "seg_edit_cold":
        ask_seg_edit(chat_id, "cold")

    elif data == "approve_segments":
        state["stage"] = "emails_approved"
        keyboard = [
            [{"text": "Yes — create social content", "callback_data": "social_yes"}],
            [{"text": "No — mark complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, "Segments approved. Want to create social content?", keyboard)

    elif data == "back_to_emails":
        state["stage"] = "emails_ready"
        send(chat_id, "Back to emails.", email_action_keyboard())

    elif data.startswith("sel_sub_"):
        idx = int(data.replace("sel_sub_", ""))
        toggle_subject_select(chat_id, idx, message_id)

    elif data == "apply_subjects":
        apply_subjects(chat_id)

    elif data == "length_email":
        show_length_menu(chat_id, mode="email")

    elif data == "length_social":
        show_length_menu(chat_id, mode="social")

    elif data == "length_extend":
        apply_length(chat_id, "extend")

    elif data == "length_shorten":
        apply_length(chat_id, "shorten")

    elif data == "cancel_length":
        mode = state.get("length_mode", "email")
        if mode == "social":
            send(chat_id, "Cancelled.", social_action_keyboard())
        else:
            send(chat_id, "Cancelled.", email_action_keyboard())

    elif data == "back_to_done":
        state["stage"] = "emails_ready"
        send(chat_id, "Back to emails.", email_action_keyboard())

    elif data == "reel_extend":
        state["reel_duration"] = state.get("reel_duration", 52) + 15
        gen_reel(chat_id)

    elif data == "reel_shorten":
        state["reel_duration"] = max(20, state.get("reel_duration", 52) - 15)
        gen_reel(chat_id)

    elif data == "carousel_extend":
        state["carousel_slides"] = state.get("carousel_slides", 6) + 2
        gen_carousel(chat_id)

    elif data == "carousel_shorten":
        state["carousel_slides"] = max(3, state.get("carousel_slides", 6) - 2)
        gen_carousel(chat_id)

    elif data == "story_extend":
        state["story_slides"] = state.get("story_slides", 3) + 1
        gen_story(chat_id, multi=True)

    elif data == "story_shorten":
        state["story_slides"] = max(1, state.get("story_slides", 3) - 1)
        is_multi = state.get("story_slides", 1) > 1
        gen_story(chat_id, multi=is_multi)

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
