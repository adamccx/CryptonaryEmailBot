#!/usr/bin/env python3
"""
Cryptonary Email Generator Bot - V9
- Full feedback loop for emails and ads
- Split test aggregation for emails
- Video AIDA analytics + static ad analytics
- Pattern recognition and iteration suggestions
- New entry point: Email / Ads / Social
- Full ad creation flow with multi-select avatar + stage
- Static (3 variants) and Video (AIDA + 3 hooks)
- Logic breakdown per ad set
- Standalone social flow
- Subject line A/B testing
- Tone variants (Standard / Aggressive / Empathetic)
- Audience segmentation for Free email (Hot / Warm / Cold)
Clean flow with consistent Quick Edit / Enhance / Approve at every stage.
"""

import os, json, ssl, urllib.request, time, re, traceback

TELEGRAM_TOKEN = "8611455908:AAH2zTch0Nf5tM590-_ouPZO2at-sqDpj_Y"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_KEY", "YOUR_ANTHROPIC_KEY_HERE")
ssl._create_default_https_context = ssl._create_unverified_context

BOOK_KNOWLEDGE = """

=== EXPANDED COPYWRITING KNOWLEDGE BASE ===

--- EXISTING FOUNDATIONS ---

FROM HORMOZI ($100M OFFERS / $100M LEADS):
- Value Equation: Dream Outcome x Likelihood / Time x Effort = Value
- Grand Slam Offer: Stack so much value the price feels embarrassing
- Pain/Dream/Fix: Open on pain, paint the dream, position as mechanism
- Specificity sells: numbers, dates, exact levels beat vague claims
- Urgency must be real and tied to market events

FROM CASHVERTISING (WHITMAN):
- LF8 Life Force Desires: survival/enjoyment of life, enjoyment of food/drink, freedom from fear/pain/danger, sexual companionship, comfortable living, to be superior/win, care for loved ones, social approval
- Secondary Wants: information, curiosity, cleanliness, efficiency, convenience, dependability, expression of beauty/style, economy/profit, bargains
- Fear works when threat is real + reader vulnerable + solution clear
- Bucket brigade technique: keep them reading line by line

FROM CIALDINI (INFLUENCE / PRE-SUASION):
- Reciprocity: Give genuine value first, then the ask
- Commitment/Consistency: Anchor their identity as a serious investor
- Social Proof: Show what members DO not just what they have access to
- Authority: Track record with specific wins, not claims
- Scarcity: Information gap is most powerful for Cryptonary
- Liking: People buy from people they like and relate to
- Unity: Joining Pro = joining a group, not buying a product
- Pre-Suasion: What comes before the message primes the response

FROM OGILVY ON ADVERTISING:
- Headline is everything — 5x more people read the headline than the body
- Promise a benefit or provoke curiosity in the headline
- Specifics always outperform generalities
- P.S. is the second most-read element — use it for the sharpest proof point
- One CTA, one action, zero friction
- Long copy outperforms short copy when the reader is interested

--- NEW BOOKS ---

FROM 50 SCIENTIFICALLY PROVEN WAYS TO GET TO YES (CIALDINI / GOLDSTEIN / MARTIN):
- Social proof is most powerful when the group is similar to the reader ("investors like you")
- Defaults are powerful — frame the desired action as the natural/obvious choice
- Loss aversion: people work harder to avoid losing than to acquire gains — frame as "don't miss" not "get"
- Labelling: tell people what they are ("you're the kind of investor who...") and they live up to it
- Implementation intentions: "when X happens, I will do Y" — make the next step dead obvious
- Rhyme as reason: messages that rhyme are judged as more truthful
- Giving a reason increases compliance dramatically — always say why
- Scarcity + exclusivity: not just limited, but "only for people who qualify"
- Progress principle: showing partial progress increases motivation to complete ("you're 80% there")
- Reciprocity of disclosure: when you share something personal, they trust you more
- The "but you are free" technique: remind people they can say no — paradoxically increases yes rates
- Consistency through small commitments: get agreement on small points before the big ask

FROM EXPERT SECRETS (RUSSELL BRUNSON):
- The Big Domino: find the ONE belief that, if they had it, all other objections disappear
- The Epiphany Bridge: share the story of when YOU had the breakthrough they need to have
- The New Opportunity: don't improve their existing approach — offer a completely new vehicle
- Future pacing: help them vividly imagine life after the transformation
- Stack: present each element of the offer with its standalone value before revealing the price
- The origin story: people buy the founder's journey as much as the product
- Identity shift: the goal is not to sell a product but to create a new identity in the buyer
- Teach the "what" for free, sell the "how" — give the concept, sell the system
- Attractive character: flaws make you relatable, not weak
- Movement vs product: build a cause people want to belong to, not just a product they buy

FROM BUILDING A STORYBRAND (MILLER):
- The reader is ALWAYS the hero — the brand is the guide
- Guide characteristics: empathy (I understand your struggle) + authority (I can help)
- The 3 levels of problem: external (the market), internal (the fear/frustration), philosophical (it's not fair)
- A clear plan removes the risk of action — people don't act when confused
- Direct CTA + transitional CTA: "Buy now" AND "Learn more" — not everyone is ready
- Stakes must be clear: what do they gain if they act? What do they lose if they don't?
- Success should be painted explicitly — never assume they'll imagine it themselves
- One message, one call to action — confusion kills conversion
- Position the villain clearly — it's not a person, it's a force (market noise, bad information, complexity)

FROM ALCHEMY (SUTHERLAND):
- Logic is not what drives decisions — perceived value and meaning drive decisions
- Reframing changes everything: the same thing positioned differently creates different desire
- Psycho-logic over logic: people don't want the optimal solution, they want the one that feels right
- Signalling: expensive or inconvenient things signal quality and commitment (application-only = exclusive)
- The opposite of a good idea can also be a good idea — test counterintuitive angles
- Loss aversion framing is more powerful than gain framing in almost every context
- Context and environment change perception completely — same message, different result
- The threshold effect: small price changes near a threshold ($997 vs $1,000) matter more than large changes elsewhere
- Dare to be trivial: small, specific, seemingly irrelevant details make claims feel more credible
- People don't know why they want things — emotion precedes rationalisation
- Trust signals that are inefficient (e.g. a long sales page) paradoxically signal you have nothing to hide

FROM MADE TO STICK (HEATH & HEATH):
- SUCCESs framework: Simple, Unexpected, Concrete, Credible, Emotional, Story
- Simple: find the core idea and hammer it relentlessly — "the lead"
- Unexpected: break a pattern to get attention, then fill the gap with your message
- Concrete: abstract ideas don't stick — sensory, specific language does
- Credible: use details, statistics, and authorities — but also "testable credentials" (try it and see)
- Emotional: people don't care about information, they care about what it means for THEM
- Story: simulation (how to handle a situation) + inspiration (this is possible) = action
- The curse of knowledge: the more you know, the harder it is to remember what it's like not to know
- Ideas that stick violate expectations, then resolve the tension
- Use names and individuals not statistics — "a child named Rokia" beats "10 million in poverty"

FROM EVERYBODY WRITES (HANDLEY):
- Writing is a habit not a talent — clarity comes from rewriting
- The reader is always the most important person in the room — write for them, not for you
- Lead with what matters most — bury the lead and you lose the reader
- Use the word "you" more than any other word
- Short sentences accelerate pace — vary length intentionally
- Avoid weasel words: "very," "quite," "rather," "really" — delete them all
- Read it out loud — if you stumble, the reader will too
- Kill the passive voice — active voice is stronger, more direct, more credible
- The best writing is rewriting — first draft is just raw material
- Every piece of content should answer "so what?" and "what do I do next?"
- Empathy maps: know what your reader feels, fears, wants, and hears

FROM IDENTITY-BASED MARKETING / IDENTITY ECONOMICS:
- People buy to affirm who they are or who they want to become — identity is the deepest motivator
- "People like us do things like this" — Seth Godin's core identity principle
- Reference groups matter: show who is already in, so the prospect can see themselves in that group
- Status is a primary motivator — people want to move up in their reference group
- Belonging and exclusion are two sides of the same lever — use both
- Labels are self-fulfilling: "you're one of the serious investors" creates the behaviour
- Values-based messaging outlasts feature-based messaging
- Community signals identity: who else is in the room matters as much as what's in the room
- The product is often just the ticket to the identity — Inner Circle is not advice, it's membership

FROM BREAKTHROUGH ADVERTISING (SCHWARTZ):
- Market sophistication: match the message to where the market's awareness is — don't shout "new" to a saturated market
- The 5 levels of market awareness: unaware → problem aware → solution aware → product aware → most aware
- Breakthrough copy does not create desire — it channels desire that already exists
- The headline's job: stop the prospect, select the right prospect, pull them into the first line
- Mass desire: tap into a pre-existing desire already present in the market
- Mechanisms: "how it works" claims are more believable than "what it does" claims
- Spread: your product's claimed ability to fulfil desire across multiple situations creates breadth
- Fresh claims must feel NEW even if the product is not — reframe, repackage, rename
- The most powerful headline states the end result the prospect most desires
- Voice: write in the voice of the prospect's internal monologue, not your own

FROM THIS IS MARKETING (GODIN):
- Smallest viable market: don't try to reach everyone — reach the smallest group that matters most and make something specifically for them
- Find the people who are already looking — don't interrupt people who aren't
- People don't want what you make — they want how it will make them feel and who it will allow them to become
- Tension and release: create tension (the status quo is not acceptable) then offer the release (the solution)
- Permission marketing: earn the right to communicate, then use it carefully
- Status roles: people want to be seen, respected, and safe — and they want to give status to others
- Generous: show up with real value before asking for anything
- Tension is the engine of change — without it, people stay where they are
- The price is a signal — low price signals low value; pricing communicates positioning
- Marketing is not about persuasion — it's about finding the people who already want what you have and letting them know it exists

--- WRITING FRAMEWORKS ---

The bot is aware of these frameworks and can apply them when appropriate:

AIDA (Attention → Interest → Desire → Action)
- Classic direct response structure
- Attention: stop the scroll / open the email
- Interest: hold them with a relevant problem or story
- Desire: build the want through proof, benefits, transformation
- Action: one clear CTA
- Best for: ads, emails, landing pages

PAS (Problem → Agitate → Solution)
- Lean into the pain before offering the fix
- Problem: name the exact problem
- Agitate: make them feel how bad it is — the cost of inaction
- Solution: position the product as the relief
- Best for: short-form copy, ads, email openers

PASTOR (Problem → Amplify → Story → Transformation → Offer → Response)
- Extension of PAS with proof and story
- Amplify: stakes — what happens if they don't solve this
- Story: a real person who had the problem and fixed it
- Transformation: the before/after contrast
- Offer: the complete value stack
- Response: the CTA
- Best for: long-form sales pages, VSLs

4 Ps (Promise → Picture → Proof → Push)
- Promise: the headline benefit
- Picture: paint the vivid future state
- Proof: evidence it's real and achievable
- Push: urgency to act now
- Best for: landing page sections, email CTAs

BAB (Before → After → Bridge)
- Before: life with the problem
- After: life with the problem solved
- Bridge: how to get from before to after (the product)
- Best for: social ads, short email hooks, carousel slides

FAB (Features → Advantages → Benefits)
- Features: what it is
- Advantages: why that matters
- Benefits: what the reader gets as a result
- Best for: product descriptions, value stacks

The 4 Us (Urgent → Unique → Useful → Ultra-specific)
- Framework for evaluating headlines and hooks
- Best for: auditing subject lines and ad headlines

PPPP (Picture → Promise → Prove → Push)
- Similar to 4Ps, more narrative-led
- Best for: email sequences, story-led landing pages

QUEST (Qualify → Understand → Educate → Stimulate → Transition)
- Qualification-first approach — filter for the right reader
- Best for: Inner Circle copy, high-ticket offers

SLAP (Stop → Look → Act → Purchase)
- Attention-focused framework for visual/social content
- Best for: carousel slides, story sequences

The Storybrand 7-Part Framework:
1. Character (hero) who wants something
2. Encounters a problem (villain/obstacle)
3. Meets a guide (Cryptonary) who has empathy and authority
4. Who gives them a plan
5. And calls them to action
6. That results in success
7. And helps them avoid failure
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
    # Telegram max message length is 4096 chars - chunk if needed
    max_len = 4000
    if len(text) <= max_len:
        data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        if keyboard:
            data["reply_markup"] = {"inline_keyboard": keyboard}
        tg("sendMessage", data)
    else:
        # Send in chunks, keyboard only on last chunk
        chunks = []
        while len(text) > max_len:
            # Break at last newline before limit
            split_at = text.rfind("\n", 0, max_len)
            if split_at == -1: split_at = max_len
            chunks.append(text[:split_at])
            text = text[split_at:].lstrip("\n")
        chunks.append(text)
        for i, chunk in enumerate(chunks):
            is_last = (i == len(chunks) - 1)
            data = {"chat_id": chat_id, "text": chunk, "parse_mode": "Markdown"}
            if is_last and keyboard:
                data["reply_markup"] = {"inline_keyboard": keyboard}
            tg("sendMessage", data)
            if not is_last:
                time.sleep(0.3)  # avoid hitting rate limits

def send_plain(chat_id, text, keyboard=None):
    """Send without Markdown parsing - safe for raw Claude output."""
    max_len = 4000
    if len(text) <= max_len:
        data = {"chat_id": chat_id, "text": text}
        if keyboard:
            data["reply_markup"] = {"inline_keyboard": keyboard}
        tg("sendMessage", data)
    else:
        chunks = []
        while len(text) > max_len:
            split_at = text.rfind("\n", 0, max_len)
            if split_at == -1: split_at = max_len
            chunks.append(text[:split_at])
            text = text[split_at:].lstrip("\n")
        chunks.append(text)
        for i, chunk in enumerate(chunks):
            is_last = (i == len(chunks) - 1)
            data = {"chat_id": chat_id, "text": chunk}
            if is_last and keyboard:
                data["reply_markup"] = {"inline_keyboard": keyboard}
            tg("sendMessage", data)
            if not is_last:
                time.sleep(0.3)


def claude(prompt, max_tokens=900, system=None):
    payload = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": max_tokens,
        "system": system if system else VOICE_GUIDE,
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
        [{"text": "Length", "callback_data": "length_email"},
         {"text": "Critique", "callback_data": "critique_email"}]
    ]

def ad_action_keyboard():
    return [
        [{"text": "Quick Edit", "callback_data": "ad_quick_edit"},
         {"text": "Enhance", "callback_data": "ad_enhance"},
         {"text": "Critique", "callback_data": "critique_ad"}],
        [{"text": "Generate another set", "callback_data": "ads_again"},
         {"text": "Mark Complete", "callback_data": "mark_complete"}]
    ]

def format_action_keyboard(fmt_key, fmt_label):
    """Action keyboard for a specific format — encodes format in callback."""
    return [
        [{"text": "Quick Edit", "callback_data": "sfmt_edit_" + fmt_key},
         {"text": "Enhance", "callback_data": "sfmt_enhance_" + fmt_key},
         {"text": "Approve", "callback_data": "sfmt_approve_" + fmt_key}],
        [{"text": "Critique", "callback_data": "critique_social_" + fmt_key},
         {"text": "Length", "callback_data": "length_social"}]
    ]

def social_action_keyboard():
    return [
        [{"text": "Quick Edit", "callback_data": "social_quick_edit"},
         {"text": "Enhance", "callback_data": "social_enhance"},
         {"text": "Approve", "callback_data": "approve_social"}],
        [{"text": "Length", "callback_data": "length_social"},
         {"text": "Critique", "callback_data": "critique_social"}]
    ]

def mark_complete_keyboard():
    return [
        [{"text": "New session", "callback_data": "start_over"}],
        [{"text": "Log email", "callback_data": "log_email_start"},
         {"text": "Log ad", "callback_data": "log_ad_start"}],
        [{"text": "Email report", "callback_data": "run_email_report"},
         {"text": "Ad report", "callback_data": "run_ad_report"}]
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
        keyboard.append([{"text": "✏️ Write my own angle", "callback_data": "custom_angle"}])
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
        keyboard.append([{"text": "✏️ Write my own hook", "callback_data": "custom_hook"}])
        keyboard.append([{"text": "✏️ Write my own hook", "callback_data": "custom_hook"}])
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
    voice_examples = get_voice_corpus_context(chat_id)
    prompt = "Write BOTH a Free email and a Pro email for Cryptonary. Apply all copywriting principles.\n\n"
    if voice_examples:
        prompt += voice_examples + "\n\n"
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
        # Store for voice learning on approve
        state["current_emails"]["free_raw"] = emails.get("free", "")
        state["current_emails"]["pro_raw"] = emails.get("pro", "")
        state["email_record"] = {
            "subject": hook.get("subject", ""),
            "angle": angle,
            "date": time.strftime("%Y-%m-%d"),
            "timestamp": time.strftime("%Y-%m-%d %H:%M")
        }
        if "free" in emails:
            send_plain(chat_id, "FREE EMAIL\n\n" + extract_text(emails["free"]))
        if "pro" in emails:
            send_plain(chat_id, "PRO EMAIL\n\n" + extract_text(emails["pro"]))
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
            send_plain(chat_id, "*EDITED " + social_type.upper() + "*\n\n" + result)
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
                send_plain(chat_id, "EDITED FREE EMAIL\n\n" + extract_text(edited["free"]))
            if "pro" in edited:
                send_plain(chat_id, "EDITED PRO EMAIL\n\n" + extract_text(edited["pro"]))
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
            send_plain(chat_id, "*IMPROVED " + social_type.upper() + "*\n\n" + result)
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
                send_plain(chat_id, "IMPROVED FREE EMAIL\n\n" + extract_text(improved["free"]))
            if "pro" in improved:
                send_plain(chat_id, "IMPROVED PRO EMAIL\n\n" + extract_text(improved["pro"]))
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
    # If coming from standalone social with an angle but no hooks yet, generate hooks first
    if state.get("social_angle") and not state.get("social_hooks"):
        gen_social_hooks(chat_id)
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
    angle = state.get("selected_angle", "") or state.get("social_angle", "")
    reel_duration = state.get("reel_duration", 52)
    source_email = get_social_source_text(chat_id)[:500]
    hook = state.get("selected_social_hooks", {}).get("fmt_reel", "")
    word_count = int(reel_duration * 2.3)
    voice_examples = get_voice_corpus_context(chat_id)
    try:
        result = claude(
            (voice_examples + "\n\n" if voice_examples else "") +
            "Write a " + str(reel_duration) + "-second Instagram Reel voiceover script for Cryptonary.\n\n" +
            ("OPENING HOOK (use this as the first spoken line): " + hook + "\n\n" if hook else "") +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Approximately " + str(word_count) + " words (matches " + str(reel_duration) + "s at natural pace)\n- First 3 seconds must stop the scroll\n- Format: voiceover text | [B-roll instruction] for each line\n- CTA at end: follow Cryptonary\n- Adam's voice: punchy, direct, data-led\n\nReturn as plain string.",
            max_tokens=900
        )
        state["current_social"] = result
        state["current_social_type"] = "Reel Script"
        state["stage"] = "social_ready"
        send_plain(chat_id, "*REEL SCRIPT (" + str(reel_duration) + "s)*\n\n" + result)
        send(chat_id, "Reel script ready.", format_action_keyboard("fmt_reel", "Reel Script"))
    except Exception as e:
        send(chat_id, "Error generating reel: " + str(e))

def gen_carousel(chat_id):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "") or state.get("social_angle", "")
    slide_count = state.get("carousel_slides", 6)
    source_email = get_social_source_text(chat_id)[:500]
    hook = state.get("selected_social_hooks", {}).get("fmt_carousel", "")
    voice_examples = get_voice_corpus_context(chat_id)
    try:
        result = claude(
            (voice_examples + "\n\n" if voice_examples else "") +
            "Create a " + str(slide_count) + "-slide Instagram Carousel for Cryptonary.\n\n" +
            ("COVER SLIDE HEADLINE (use this): " + hook + "\n\n" if hook else "") +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Exactly " + str(slide_count) + " slides including cover and CTA final slide\n- Format: SLIDE N: [headline max 8 words] + [visual direction in brackets]\n- Mix bold text, data slides, list slides\n- Each slide earns the next swipe\n- Final slide: follow for more\n\nReturn as plain string.",
            max_tokens=900
        )
        state["current_social"] = result
        state["current_social_type"] = "Carousel"
        state["stage"] = "social_ready"
        send_plain(chat_id, "*CAROUSEL (" + str(slide_count) + " slides)*\n\n" + result)
        send(chat_id, "Carousel ready.", format_action_keyboard("fmt_carousel", "Carousel"))
    except Exception as e:
        send(chat_id, "Error generating carousel: " + str(e))

def gen_story(chat_id, multi=False):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    context = sanitise(state.get("context", ""))
    angle = state.get("selected_angle", "") or state.get("social_angle", "")
    story_slides = state.get("story_slides", 3) if multi else 1
    source_email = get_social_source_text(chat_id)[:500]
    fmt_key = "fmt_story_multi" if multi else "fmt_story_single"
    hook = state.get("selected_social_hooks", {}).get(fmt_key, "")
    slide_instruction = str(story_slides) + " slides" if multi else "1 single slide"
    voice_examples_story = get_voice_corpus_context(chat_id)
    try:
        result = claude(
            (voice_examples_story + "\n\n" if voice_examples_story else "") +
            "Create an Instagram Story for Cryptonary: " + slide_instruction + "\n\n" +
            ("OPENING SLIDE TEXT (use this as slide 1): " + hook + "\n\n" if hook else "") +
            "SOURCE:\nReport: " + report + ("\nContext: " + context if context else "") +
            "\nAngle: " + angle + "\nEmail reference: " + source_email +
            "\n\nRULES:\n- Format per slide: SLIDE N: [text max 15 words] + [visual/background direction] + [optional sticker]\n- Cliffhanger between slides if multi\n- Final slide: swipe up or link in bio\n- Urgent, direct tone\n\nReturn as plain string.",
            max_tokens=700
        )
        social_type = "Story (" + str(story_slides) + " slides)" if multi else "Story (single)"
        state["current_social"] = result
        state["current_social_type"] = social_type
        state["stage"] = "social_ready"
        send_plain(chat_id, "*" + social_type.upper() + "*\n\n" + result)
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
            send_plain(chat_id, social_type.upper() + " — " + direction.upper() + "ED\n\n" + result)
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
                send_plain(chat_id, "FREE EMAIL — " + direction.upper() + "ED\n\n" + extract_text(adjusted["free"]))
            if "pro" in adjusted:
                send_plain(chat_id, "PRO EMAIL — " + direction.upper() + "ED\n\n" + extract_text(adjusted["pro"]))
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
            save_all_data()
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
    label = ["B","C","D"][min(len(selected_ids)-1,2)] if selected_ids else "A"
    send(chat_id, str(count) + " subject line(s) applied.")
    # Show updated emails immediately
    if "free" in emails:
        send_plain(chat_id, "*FREE EMAIL (updated subjects)*\n\n" + extract_text(emails["free"]))
    if "pro" in emails:
        send_plain(chat_id, "*PRO EMAIL (updated subjects)*\n\n" + extract_text(emails["pro"]))
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
            send_plain(chat_id, "*FREE EMAIL — " + tone_label.upper() + "*\n\n" + extract_text(toned["free"]))
        if "pro" in toned:
            send_plain(chat_id, "*PRO EMAIL — " + tone_label.upper() + "*\n\n" + extract_text(toned["pro"]))
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
                send_plain(chat_id, "*FREE EMAIL — " + label.upper() + "*\n\n" + extract_text(segments[key]))
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
        send_plain(chat_id, "*EDITED — " + label.upper() + "*\n\n" + result)
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
        show_main_menu(chat_id)
        return
    if text == "/stats":
        show_stats(chat_id)
        return
    if text == "/logperformance":
        user_state.setdefault(chat_id, {})
        start_log_performance(chat_id)
        return
    if text == "/logemail":
        user_state.setdefault(chat_id, {})
        start_log_email(chat_id)
        return
    if text == "/logad":
        user_state.setdefault(chat_id, {})
        start_log_ad(chat_id)
        return
    if text == "/emailreport":
        run_email_analysis(chat_id)
        return
    if text == "/adreport":
        run_ad_analysis(chat_id)
        return
    if text == "/briefing":
        user_state.setdefault(chat_id, {})
        generate_briefing(chat_id)
        return

    if text == "/imageprompt" or text.startswith("/imageprompt "):
        user_state.setdefault(chat_id, {"stage": "idle"})
        brief = text.replace("/imageprompt", "").strip()
        if brief:
            generate_image_prompts(chat_id, brief)
        else:
            user_state[chat_id]["stage"] = "awaiting_image_brief"
            send(chat_id, "*Image Prompt Generator*\n\nDescribe what you need.\n\n_e.g. Hero image for Inner Circle landing page, premium dark crypto wealth theme_\n_e.g. Static ad for Passive Income avatar, warm lifestyle feel_\n_e.g. Carousel cover slide, Bitcoin price breakout energy_")
        return

    if text == "/help":
        send(chat_id, "*Cryptonary Content Studio V9*\n\nFrom /start choose: Emails, Ads, or Social\n\n*Email commands:*\n/logemail — log open rate + CTR\n/emailreport — analyse all logged emails\n\n*Ad commands:*\n/logad — log video or static ad results\n/adreport — analyse all logged ads\n\n*Legacy:*\n/logperformance — old performance log\n/stats — old stats summary\n\n/start — return to main menu")
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

    if stage == "logging_email":
        handle_email_log_step(chat_id, text)
        return

    if stage == "logging_ad":
        handle_ad_log_step(chat_id, text)
        return

    if stage == "awaiting_critique_apply":
        apply_critique_fix(chat_id, text.strip())
        return

    if stage == "awaiting_custom_angle":
        user_state[chat_id]["selected_angle"] = text
        user_state[chat_id]["stage"] = "pick_hook"
        gen_hooks(chat_id)
        return

    if stage == "awaiting_custom_hook":
        # Parse "subject | preview" or just subject
        parts = text.split("|")
        subject = parts[0].strip()
        preview = parts[1].strip() if len(parts) > 1 else ""
        hook = {"subject": subject, "preview": preview, "hook_a": "", "hook_b": "", "hook_c": ""}
        user_state[chat_id]["selected_hook"] = hook
        user_state[chat_id]["stage"] = "pick_free_cta"
        show_cta_menu(chat_id, "free")
        return

    if stage == "awaiting_custom_social_angle":
        user_state[chat_id]["social_angle"] = text
        user_state[chat_id]["stage"] = "pick_social_formats"
        user_state[chat_id]["selected_social_formats"] = []
        show_standalone_social_menu(chat_id)
        return

    if stage == "awaiting_ad_theme":
        user_state[chat_id]["ad_theme"] = text
        user_state[chat_id]["stage"] = "pick_ad_avatars"
        show_avatar_menu(chat_id)
        return

    if stage == "awaiting_image_brief":
        user_state[chat_id]["stage"] = "idle"
        generate_image_prompts(chat_id, text)
        return

    if stage.startswith("ie_awaiting_source_"):
        source_type = stage.replace("ie_awaiting_source_", "")
        sources = load_idea_sources()
        key_map = {"instagram": "instagram", "twitter": "twitter",
                   "facebook": "facebook_pages", "telegram": "telegram", "reddit": "reddit"}
        key = key_map.get(source_type)
        if key:
            if key not in sources: sources[key] = []
            val = text.strip().lstrip("@").lstrip("/")
            if val not in sources[key]:
                sources[key].append(val)
                save_idea_sources(sources)
                send(chat_id, "Added " + val + " to " + source_type + " sources.")
            else:
                send(chat_id, val + " is already in your sources.")
        user_state[chat_id]["stage"] = "idea_engine_idle"
        show_ie_manage_sources(chat_id)
        return

    if stage == "ie_awaiting_develop":
        idea_text = text
        last_ideas = user_state[chat_id].get("last_ideas", "")
        user_state[chat_id]["stage"] = "awaiting_social_report"
        user_state[chat_id]["report"] = "IDEA TO DEVELOP:\n" + idea_text + "\n\nFULL IDEAS CONTEXT:\n" + last_ideas[:500]
        user_state[chat_id]["social_angle"] = idea_text[:100]
        show_standalone_social_menu(chat_id)
        return

    if stage == "ie_awaiting_develop_ad":
        idea_text = text
        last_ideas = user_state[chat_id].get("last_ideas", "")
        user_state[chat_id]["stage"] = "pick_ad_avatars"
        user_state[chat_id]["ad_theme"] = idea_text
        user_state[chat_id]["report"] = last_ideas[:500]
        show_avatar_menu(chat_id)
        return

    if stage == "ds_awaiting_email_splitvar":
        user_state[chat_id]["ds_split_var"] = text
        user_state[chat_id]["stage"] = "ds_awaiting_email_split_data"
        user_state[chat_id]["ds_images"] = []
        keyboard = [[{"text": "Done — analyse now", "callback_data": "ds_analyse_emails_split"}]]
        send(chat_id, "Got it. Now upload your email performance screenshots or CSV.", keyboard)
        return

    if stage == "ds_awaiting_landing_splitvar":
        user_state[chat_id]["ds_split_var"] = text
        user_state[chat_id]["stage"] = "ds_awaiting_landing_split_data"
        user_state[chat_id]["ds_images"] = []
        keyboard = [[{"text": "Done — analyse now", "callback_data": "ds_analyse_landing_split"}]]
        send(chat_id, "Got it. Now upload your landing page screenshots or CSV.", keyboard)
        return

    if stage in ("ds_awaiting_followup", "ds_analysis_done") and user_state.get(chat_id, {}).get("last_ds_analysis"):
        last_analysis = user_state[chat_id].get("last_ds_analysis", "")
        user_state[chat_id]["stage"] = "ds_analysis_done"
        send(chat_id, "Working on it...")
        try:
            result = claude(
                "Previous analysis:\n" + last_analysis[:3000] +
                "\n\nFollow-up question: " + text +
                "\n\nAnswer specifically based on the data already analysed. Be direct and actionable.",
                max_tokens=1500,
                system=DATA_STUDIO_SYSTEM
            )
            send_plain(chat_id, result)
            keyboard = [
                [{"text": "Ask another follow-up", "callback_data": "ds_followup"}],
                [{"text": "Back to Data Studio", "callback_data": "open_data_studio"}]
            ]
            send(chat_id, "Done.", keyboard)
        except Exception as e:
            print("Followup error:", e, flush=True)
            print(traceback.format_exc(), flush=True)
            send(chat_id, "Error in follow-up: " + str(e))
        return

    if stage == "awaiting_lp_context_text":
        state["lp_context"] = text
        generate_landing_page(chat_id)
        return

    if stage == "awaiting_lp_quick_edit":
        instruction = text
        lp_content = state.get("current_lp", "")
        state["stage"] = "lp_ready"
        send(chat_id, "Applying edit...")
        try:
            result = claude(
                "Edit this Cryptonary landing page section. Instruction: " + instruction +
                "\n\nApply BrandScript framework and copywriting principles. Keep all other sections intact. Only change what the instruction specifies.\n\nFULL PAGE:\n" + lp_content[:3000] +
                "\n\nReturn only the edited section(s) as plain text.",
                max_tokens=1500,
                system=BRANDSCRIPT_PROMPT
            )
            send_plain(chat_id, result)
            keyboard = [
                [{"text": "Quick Edit", "callback_data": "lp_quick_edit"},
                 {"text": "Regenerate section", "callback_data": "lp_regen"}],
                [{"text": "Critique", "callback_data": "critique_lp"},
                 {"text": "Mark Complete", "callback_data": "mark_complete"}],
                [{"text": "Generate another page", "callback_data": "lp_again"}]
            ]
            send(chat_id, "Edit applied.", keyboard)
        except Exception as e:
            send(chat_id, "Error: " + str(e))
        return

    if stage == "awaiting_lp_regen_instruction":
        instruction = text.strip()
        section = state.get("lp_regen_section", "Hero")
        cta_key = state.get("lp_cta", "pro")
        cta = LP_CTA_DEFS.get(cta_key, LP_CTA_DEFS["pro"])
        avatar_keys = state.get("selected_avatars", [])
        avatar_descs = "\n".join([k + ": " + AVATARS_AD.get(k, ("",))[1] for k in avatar_keys])
        context = sanitise(state.get("lp_context", ""))
        state["stage"] = "lp_ready"
        send(chat_id, "Regenerating " + section + "...")
        try:
            prompt = BRANDSCRIPT_PROMPT
            prompt += "\n\nAVATAR(S): " + avatar_descs
            prompt += "\nCTA: " + cta["label"] + " — " + cta["price"]
            prompt += "\nPOSITIONING: " + cta["positioning"]
            if context: prompt += "\nCONTEXT: " + context
            if instruction: prompt += "\nSPECIFIC DIRECTION: " + instruction
            prompt += "\n\nREGENERATE ONLY: " + section.upper() + " SECTION. Return as plain text with graphic recommendations."
            result = claude(prompt, max_tokens=1200, system=BRANDSCRIPT_PROMPT)
            send_plain(chat_id, result)
            keyboard = [
                [{"text": "Quick Edit", "callback_data": "lp_quick_edit"},
                 {"text": "Regenerate section", "callback_data": "lp_regen"}],
                [{"text": "Critique", "callback_data": "critique_lp"},
                 {"text": "Mark Complete", "callback_data": "mark_complete"}],
                [{"text": "Generate another page", "callback_data": "lp_again"}]
            ]
            send(chat_id, "Section regenerated.", keyboard)
        except Exception as e:
            send(chat_id, "Error: " + str(e))
        return

    if stage == "awaiting_ad_quick_edit":
        instruction = text
        ad_content = state.get("current_ad", "")
        label = state.get("current_ad_label", "AD")
        state["stage"] = "ads_ready"
        send(chat_id, "Applying edit...")
        try:
            result = claude("Edit this ad copy. Instruction: " + instruction + "\n\nKeep the same structure and format. Only change what specified.\n\nAD:\n" + ad_content + "\n\nReturn as plain string.", max_tokens=1500)
            state["current_ad"] = result
            send_plain(chat_id, label + result, ad_action_keyboard())
        except Exception as e:
            send(chat_id, "Error: " + str(e), ad_action_keyboard())
        return

    if stage == "awaiting_social_report":
        user_state[chat_id]["report"] = text
        user_state[chat_id]["context"] = ""
        gen_social_angles(chat_id)
        return

    if len(text) > 100:
        current_stage = user_state.get(chat_id, {}).get("stage", "idle")
        # Buffer multi-message pastes
        if current_stage == "buffering_report":
            user_state[chat_id]["report_buffer"] += "\n" + text
            user_state[chat_id]["buffer_timer"] = time.time()
            return
        elif current_stage in ["idle", "awaiting_context_choice"] and user_state.get(chat_id, {}).get("buffer_timer"):
            return
        # Route based on what mode we're in
        elif current_stage == "awaiting_email_report":
            user_state[chat_id] = {"stage": "buffering_report", "report_buffer": text, "buffer_timer": time.time(), "mode": "email"}
            time.sleep(1.5)
            if user_state.get(chat_id, {}).get("stage") == "buffering_report":
                full_report = user_state[chat_id].get("report_buffer", text)
                user_state[chat_id] = {"stage": "awaiting_context_choice", "report": full_report, "mode": "email"}
                ask_context(chat_id)
        else:
            # Legacy: treat as email report
            user_state[chat_id] = {"stage": "buffering_report", "report_buffer": text, "buffer_timer": time.time(), "mode": "email"}
            time.sleep(1.5)
            if user_state.get(chat_id, {}).get("stage") == "buffering_report":
                full_report = user_state[chat_id].get("report_buffer", text)
                user_state[chat_id] = {"stage": "awaiting_context_choice", "report": full_report, "mode": "email"}
                ask_context(chat_id)
    else:
        stage = user_state.get(chat_id, {}).get("stage", "idle")
        if stage == "idle":
            show_main_menu(chat_id)
        # Silently ignore short text in active flows — don't reset or confuse the user

def handle_callback(cb):
    chat_id = cb["message"]["chat"]["id"]
    message_id = cb["message"]["message_id"]
    data = cb["data"]
    tg("answerCallbackQuery", {"callback_query_id": cb["id"]})
    state = user_state.get(chat_id, {})

    if data == "start_over":
        show_main_menu(chat_id)

    elif data == "open_content_studio":
        keyboard = [
            [{"text": "Emails", "callback_data": "mode_email"}],
            [{"text": "Ad Copy", "callback_data": "mode_ads"}],
            [{"text": "Social Content", "callback_data": "mode_social"}],
            [{"text": "Landing Page", "callback_data": "mode_landing"}]
        ]
        send(chat_id, "*Cryptonary Content Studio*\n\nWhat do you want to create?", keyboard)

    elif data == "open_data_studio":
        show_data_studio_menu(chat_id)

    elif data == "mode_email":
        user_state[chat_id] = {"stage": "awaiting_email_report"}
        send(chat_id, "Paste your report:")

    elif data == "mode_ads":
        user_state[chat_id] = {"stage": "awaiting_ad_theme", "selected_avatars": [], "selected_stages": []}
        send(chat_id, "*Ad Creation*\n\nPaste your campaign theme, report, or context:\n\n_Examples: Bitcoin halving setup, inner circle launch, market crash opportunity, weekly market update..._")

    elif data == "mode_social":
        user_state[chat_id] = {"stage": "awaiting_social_report", "selected_social_formats": []}
        send(chat_id, "Paste your report or content to base social posts on:")

    elif data == "mode_landing":
        user_state[chat_id] = {"stage": "pick_lp_avatars", "selected_avatars": []}
        show_lp_avatar_menu(chat_id)

    elif data.startswith("adavatar_"):
        avatar_key = data.replace("adavatar_", "")
        toggle_avatar(chat_id, avatar_key, message_id)

    elif data == "adavatars_done":
        selected = state.get("selected_avatars", [])
        if not selected:
            send(chat_id, "Please select at least one avatar.")
        else:
            state["selected_stages"] = []
            show_stage_menu(chat_id)

    elif data.startswith("adstage_"):
        stage_key = data.replace("adstage_", "")
        toggle_stage(chat_id, stage_key, message_id)

    elif data == "adstages_done":
        selected = state.get("selected_stages", [])
        if not selected:
            send(chat_id, "Please select at least one funnel stage.")
        else:
            show_adtype_menu(chat_id)

    elif data == "adtype_static":
        state["ad_type"] = "static"
        generate_all_ads(chat_id)

    elif data == "adtype_video":
        state["ad_type"] = "video"
        generate_all_ads(chat_id)

    elif data == "ad_quick_edit":
        state["stage"] = "awaiting_ad_quick_edit"
        send(chat_id, "*Quick Edit — Ad Copy*\n\nType your instruction:")

    elif data == "ad_enhance":
        ad_content = state.get("current_ad", "")
        if not ad_content:
            send(chat_id, "No ad content found.", ad_action_keyboard())
        else:
            send(chat_id, "Analysing ad copy...")
            try:
                prompt = "Analyse this Cryptonary ad copy and give 6 specific improvements. Apply Hormozi, Cashvertising LF8, Cialdini, Ogilvy principles.\n\nAD:\n" + ad_content + "\n\nFormat:\n1. PRINCIPLE: [name]\nISSUE: [what is weak]\nFIX: [specific fix]\n\nAnd so on for all 6."
                raw = claude(prompt, max_tokens=1000)
                send_plain(chat_id, "AD ENHANCEMENT SUGGESTIONS\n\n" + raw, ad_action_keyboard())
            except Exception as e:
                send(chat_id, "Error: " + str(e), ad_action_keyboard())

    elif data == "avatarpage_next":
        page = state.get("avatar_page", 0)
        show_avatar_menu(chat_id, page + 1)

    elif data == "avatarpage_prev":
        page = state.get("avatar_page", 0)
        show_avatar_menu(chat_id, max(0, page - 1))

    elif data == "ads_again":
        state["selected_avatars"] = []
        state["selected_stages"] = []
        show_avatar_menu(chat_id)

    elif data.startswith("lpavatar_"):
        avatar_key = data.replace("lpavatar_", "")
        toggle_lp_avatar(chat_id, avatar_key, message_id)

    elif data == "lpavatarpage_next":
        page = state.get("avatar_page", 0)
        show_lp_avatar_menu(chat_id, page + 1)

    elif data == "lpavatarpage_prev":
        page = state.get("avatar_page", 0)
        show_lp_avatar_menu(chat_id, max(0, page - 1))

    elif data == "lpavatars_done":
        selected = state.get("selected_avatars", [])
        if not selected:
            send(chat_id, "Please select at least one avatar.")
        else:
            show_lp_cta_menu(chat_id)

    elif data == "lpcta_pro":
        state["lp_cta"] = "pro"
        state["stage"] = "awaiting_lp_context"
        keyboard = [
            [{"text": "Yes — add context", "callback_data": "lp_context_yes"}],
            [{"text": "No — generate now", "callback_data": "lp_context_no"}]
        ]
        send(chat_id, "*Any extra context?*\n\nCurrent offer, promo, urgency mechanic, specific hook, seasonal angle...", keyboard)

    elif data == "lpcta_inner_circle":
        state["lp_cta"] = "inner_circle"
        state["stage"] = "awaiting_lp_context"
        keyboard = [
            [{"text": "Yes — add context", "callback_data": "lp_context_yes"}],
            [{"text": "No — generate now", "callback_data": "lp_context_no"}]
        ]
        send(chat_id, "*Any extra context?*\n\nCurrent offer, promo, urgency mechanic, specific hook, seasonal angle...", keyboard)

    elif data == "lp_context_yes":
        state["stage"] = "awaiting_lp_context_text"
        send(chat_id, "Type your extra context:")

    elif data == "lp_context_no":
        state["lp_context"] = ""
        generate_landing_page(chat_id)

    elif data == "lp_quick_edit":
        state["stage"] = "awaiting_lp_quick_edit"
        send(chat_id, "*Quick Edit — Landing Page*\n\nWhich section and what to change?\n_e.g. Rewrite the hero headline / Make the value stack more specific / Shorten the FAQ_")

    elif data == "lp_regen":
        state["stage"] = "awaiting_lp_regen"
        keyboard = []
        for name in ["Hero", "Problem", "Guide", "Plan", "Value Stack", "Social Proof", "CTA Block", "FAQ", "Footer CTA"]:
            keyboard.append([{"text": name, "callback_data": "lp_regen_" + name.lower().replace(" ", "_")}])
        send(chat_id, "Which section to regenerate?", keyboard)

    elif data == "lp_now_regen":
        section = state.get("lp_regen_section", "Hero")
        state["stage"] = "lp_ready"
        cta_key = state.get("lp_cta", "pro")
        cta = LP_CTA_DEFS.get(cta_key, LP_CTA_DEFS["pro"])
        avatar_keys = state.get("selected_avatars", [])
        avatar_descs = "\n".join([k + ": " + AVATARS_AD.get(k, ("",))[1] for k in avatar_keys])
        context = sanitise(state.get("lp_context", ""))
        send(chat_id, "Regenerating " + section + "...")
        try:
            user_prompt = "LANDING PAGE BRIEF:\nAVATAR(S): " + avatar_descs
            user_prompt += "\nCTA: " + cta["label"] + " — " + cta["price"]
            user_prompt += "\nPOSITIONING: " + cta["positioning"]
            if context: user_prompt += "\nCONTEXT: " + context
            user_prompt += "\n\nREGENERATE ONLY: " + section.upper() + " SECTION. Return as plain text with graphic recommendations."
            result = claude(user_prompt, max_tokens=1200, system=BRANDSCRIPT_PROMPT)
            send_plain(chat_id, result)
            keyboard = [
                [{"text": "Quick Edit", "callback_data": "lp_quick_edit"},
                 {"text": "Regenerate section", "callback_data": "lp_regen"}],
                [{"text": "Critique", "callback_data": "critique_lp"},
                 {"text": "Mark Complete", "callback_data": "mark_complete"}],
                [{"text": "Generate another page", "callback_data": "lp_again"}]
            ]
            send(chat_id, "Section regenerated.", keyboard)
        except Exception as e:
            send(chat_id, "Error: " + str(e))


    elif data.startswith("lp_regen_"):
        section = data.replace("lp_regen_", "").replace("_", " ").title()
        state["lp_regen_section"] = section
        state["stage"] = "awaiting_lp_regen_instruction"
        keyboard = [[{"text": "Regenerate as-is", "callback_data": "lp_now_regen"}]]
        send(chat_id, "*Regenerate: " + section + "*\n\nType a specific direction, or tap to regenerate as-is:", keyboard)


    elif data == "lp_again":
        state["selected_avatars"] = []
        state.pop("lp_cta", None)
        state.pop("lp_context", None)
        show_lp_avatar_menu(chat_id)

    elif data == "context_yes":
        user_state[chat_id]["stage"] = "awaiting_context_text"
        send(chat_id, "Type your extra context:")

    elif data == "context_no":
        user_state[chat_id]["context"] = ""
        user_state[chat_id]["stage"] = "pick_angle"
        gen_angles(chat_id)

    elif data == "custom_angle":
        user_state[chat_id]["stage"] = "awaiting_custom_angle"
        send(chat_id, "Type your angle:")

    elif data == "custom_hook":
        user_state[chat_id]["stage"] = "awaiting_custom_hook"
        send(chat_id, "Type your subject line:\n\n_Format: Subject line | Preview text_\n_Or just type the subject line_")

    elif data == "social_custom_angle":
        user_state[chat_id]["stage"] = "awaiting_custom_social_angle"
        send(chat_id, "Type your angle:")

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

    elif data.startswith("sfmt_edit_"):
        fmt_key = data.replace("sfmt_edit_", "")
        # Load the right format into current_social
        outputs = state.get("social_outputs", {})
        if fmt_key in outputs:
            state["current_social"] = outputs[fmt_key]["content"]
            state["current_social_type"] = outputs[fmt_key]["type"]
            state["current_social_format"] = fmt_key
        state["stage"] = "social_quick_edit"
        send(chat_id, "What would you like to change in the " + state.get("current_social_type","content") + "?")

    elif data.startswith("sfmt_enhance_"):
        fmt_key = data.replace("sfmt_enhance_", "")
        outputs = state.get("social_outputs", {})
        if fmt_key in outputs:
            state["current_social"] = outputs[fmt_key]["content"]
            state["current_social_type"] = outputs[fmt_key]["type"]
            state["current_social_format"] = fmt_key
        gen_enhance(chat_id, mode="social")

    elif data.startswith("sfmt_approve_"):
        fmt_key = data.replace("sfmt_approve_", "")
        outputs = state.get("social_outputs", {})
        if fmt_key in outputs:
            state["current_social"] = outputs[fmt_key]["content"]
            state["current_social_type"] = outputs[fmt_key]["type"]
            state["current_social_format"] = fmt_key
        # Save to voice corpus
        social_body = state.get("current_social", "")
        social_type = state.get("current_social_type", "social")
        if social_body:
            save_voice_example(chat_id, social_body[:600], "approved_" + social_type.lower().replace(" ", "_"))
        state["stage"] = "social_approved"
        keyboard = [
            [{"text": "Generate another format", "callback_data": "social_yes"}],
            [{"text": "Mark Complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, social_type + " approved.", keyboard)

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
        # Save content metadata + actual approved copy for voice learning
        free_body = state.get("current_emails", {}).get("free", "")
        pro_body = state.get("current_emails", {}).get("pro", "")
        save_content_metadata(chat_id, "email", {
            "angle": state.get("angle", state.get("selected_angle", "")),
            "hook_subject": state.get("selected_hook", {}).get("subject", ""),
            "hook_preview": state.get("selected_hook", {}).get("preview", ""),
            "free_cta": state.get("free_cta", ""),
            "pro_cta": state.get("pro_cta", ""),
            "tone": state.get("selected_tone", "standard"),
            "free_email_body": free_body[:600],
            "pro_email_body": pro_body[:600]
        })
        # Save to voice corpus for self-learning
        if free_body:
            save_voice_example(chat_id, free_body[:600], "approved_free_email")
        if pro_body:
            save_voice_example(chat_id, pro_body[:600], "approved_pro_email")
        keyboard = [
            [{"text": "Yes — create social content", "callback_data": "social_yes"}],
            [{"text": "No — mark complete", "callback_data": "mark_complete"}]
        ]
        send(chat_id, "Emails approved. Want to create social content?", keyboard)

    elif data == "social_yes":
        state["selected_social_formats"] = []
        show_social_source_menu(chat_id)

    elif data.startswith("social_angle_"):
        idx = int(data.replace("social_angle_", ""))
        angles = state.get("social_angles", [])
        if idx < len(angles):
            state["social_angle"] = angles[idx]
        state["stage"] = "pick_social_formats"
        state["selected_social_formats"] = []
        show_standalone_social_menu(chat_id)

    elif data == "social_regen_angles":
        state["stage"] = "awaiting_social_report"
        gen_social_angles(chat_id)

    elif data == "gen_social_confirmed":
        gen_social_selected(chat_id)

    elif data.startswith("social_hook_"):
        # Format: social_hook_{fmt_idx}_{hook_idx}
        parts = data.replace("social_hook_", "").split("_")
        if len(parts) == 2:
            fmt_idx = int(parts[0])
            hook_idx = int(parts[1])
            formats = state.get("selected_social_formats", [])
            if fmt_idx < len(formats):
                fmt = formats[fmt_idx]
                hooks = state.get("social_hooks", {}).get(fmt, [])
                if hook_idx < len(hooks):
                    if "selected_social_hooks" not in state:
                        state["selected_social_hooks"] = {}
                    state["selected_social_hooks"][fmt] = hooks[hook_idx]
            show_social_hook_picker(chat_id, fmt_idx + 1)

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
        # Save to voice corpus for self-learning
        social_body = state.get("current_social", "")
        social_type = state.get("current_social_type", "social")
        if social_body:
            save_voice_example(chat_id, social_body[:600], "approved_" + social_type.lower().replace(" ", "_"))
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

    elif data == "log_email_start":
        start_log_email(chat_id)

    elif data == "log_ad_start":
        start_log_ad(chat_id)

    elif data == "run_email_report":
        run_email_analysis(chat_id)

    elif data == "run_ad_report":
        run_ad_analysis(chat_id)

    elif data == "email_log_ab_yes":
        state["log_stage"] = "email_ab_variable"
        send(chat_id, "What is the variable being tested? (e.g. 'name in subject line', 'curiosity gap vs data hook', 'short vs long preview')")

    elif data == "email_log_ab_no":
        state.get("log_data", {}).update({"ab_variable": None, "ab_label": None})
        state["log_stage"] = "email_recipients"
        send(chat_id, "How many recipients received this email?")

    elif data.startswith("adlog_type_"):
        ad_type = data.replace("adlog_type_", "")
        state["log_data"] = {"ad_type": ad_type}
        state["log_stage"] = "adlog_headline"
        send(chat_id, "Enter the headline or first line of the ad:")

    elif data.startswith("adlog_avatar_"):
        avatar_key = data.replace("adlog_avatar_", "")
        avatar_name = AVATARS_AD.get(avatar_key, ("Unknown",))[0]
        if "log_data" not in state:
            state["log_data"] = {}
        state["log_data"]["avatar"] = avatar_name
        state["log_stage"] = "adlog_stage"
        keyboard = [[{"text": s.capitalize(), "callback_data": "adlog_stage_" + s}] for s in ["awareness","consideration","conversion"]]
        send(chat_id, "Which funnel stage was this ad?", keyboard)

    elif data.startswith("adlog_stage_"):
        stage_name = data.replace("adlog_stage_", "")
        if "log_data" not in state:
            state["log_data"] = {}
        state["log_data"]["stage"] = stage_name
        state["log_stage"] = "adlog_date"
        send(chat_id, "Date the ad ran? (e.g. 2026-03-22)")

    elif data == "ds_adverts":
        state["ds_images"] = []
        state.pop("ds_csv_text", None)
        start_ds_adverts(chat_id)

    elif data.startswith("ad_filter_"):
        ad_filter = data.replace("ad_filter_", "")
        state["ds_ad_filter"] = ad_filter
        state["stage"] = "ds_awaiting_ad_data"
        state["ds_images"] = []
        filter_label = {"all": "All ads", "video": "Video ads only", "static": "Static ads only"}.get(ad_filter, "All ads")
        keyboard = [[{"text": "Done — analyse now", "callback_data": "ds_analyse_ads"}]]
        send(chat_id, "*" + filter_label + "*\n\nUpload your Meta Ads Manager screenshots or CSV. Send all then tap Done.", keyboard)

    elif data == "ds_social":
        state["ds_images"] = []
        state.pop("ds_csv_text", None)
        start_ds_social(chat_id)

    elif data.startswith("social_filter_"):
        social_filter = data.replace("social_filter_", "")
        state["ds_social_filter"] = social_filter
        state["stage"] = "ds_awaiting_social_data"
        state["ds_images"] = []
        filter_label = {"all": "All formats", "reels": "Reels only", "statics": "Statics only", "carousels": "Carousels only"}.get(social_filter, "All formats")
        keyboard = [[{"text": "Done — analyse now", "callback_data": "ds_analyse_social"}]]
        send(chat_id, "*" + filter_label + "*\n\nUpload your Minter screenshots or CSV. Send all then tap Done.", keyboard)

    elif data == "ds_emails":
        state["ds_images"] = []
        state.pop("ds_csv_text", None)
        start_ds_emails(chat_id)

    elif data == "ds_landing":
        state["ds_images"] = []
        state.pop("ds_csv_text", None)
        start_ds_landing(chat_id)

    elif data == "ds_analyse_ads":
        analyse_ads(chat_id)

    elif data == "ds_analyse_social":
        analyse_social(chat_id)

    elif data == "ds_analyse_emails":
        analyse_emails(chat_id)

    elif data == "ds_analyse_landing":
        analyse_landing(chat_id)

    elif data == "ds_email_splittest":
        start_ds_email_splittest(chat_id)

    elif data == "ds_landing_splittest":
        start_ds_landing_splittest(chat_id)

    elif data == "ds_analyse_emails_split":
        analyse_emails(chat_id, split_var=state.get("ds_split_var"))

    elif data == "ds_analyse_landing_split":
        analyse_landing(chat_id, split_var=state.get("ds_split_var"))

    elif data.startswith("ds_add_more_"):
        # Keep current stage, just prompt for more
        send(chat_id, "Send your next screenshot:")

    elif data == "briefing_refresh":
        generate_briefing(chat_id)

    elif data == "open_idea_engine":
        show_idea_engine_menu(chat_id)

    elif data == "ie_generate_all":
        generate_ideas(chat_id, "both")

    elif data == "ie_generate_social":
        generate_ideas(chat_id, "social")

    elif data == "ie_generate_ads":
        generate_ideas(chat_id, "ads")

    elif data == "ie_manage_sources":
        show_ie_manage_sources(chat_id)

    elif data == "ie_develop":
        state["stage"] = "ie_awaiting_develop"
        send(chat_id, "Type the idea number or paste the idea you want to develop into social content:")

    elif data == "ie_develop_ad":
        state["stage"] = "ie_awaiting_develop_ad"
        send(chat_id, "Type the idea number or paste the idea you want to develop into an ad:")

    elif data == "ie_screenshot_ideas":
        state["stage"] = "ie_awaiting_screenshot_ideas"
        send(chat_id, "*Ideas from a Screenshot*\n\nSend an image — Instagram post, ad, competitor content, anything. I\'ll analyse it and generate ideas based on what\'s working in it.")

    elif data == "ie_screenshot_critique":
        state["stage"] = "ie_awaiting_screenshot_critique"
        send(chat_id, "*Critique a Screenshot*\n\nSend an image of any content — your own post, a competitor ad, a carousel. I\'ll critique it against our full knowledge base with specific, numbered fixes.")

    elif data == "ie_imageprompt_again":
        brief = state.get("last_image_brief", "")
        if brief:
            generate_image_prompts(chat_id, brief)
        else:
            send(chat_id, "Use /imageprompt [description] to generate new prompts.")

    elif data.startswith("ie_add_"):
        source_type = data.replace("ie_add_", "")
        state["stage"] = "ie_awaiting_source_" + source_type
        prompts = {
            "instagram": "Enter Instagram handle (without @):",
            "twitter": "Enter Twitter/X handle (without @):",
            "facebook": "Enter Facebook page name:",
            "telegram": "Enter Telegram channel name (without t.me/):",
            "reddit": "Enter subreddit name (without r/):"
        }
        send(chat_id, prompts.get(source_type, "Enter the source name:"))

    elif data == "ds_followup":
        state["stage"] = "ds_awaiting_followup"
        send(chat_id, "Ask your follow-up question:")

    elif data.startswith("critique_") and data != "critique_":
        content_type = data.replace("critique_", "")
        run_critique(chat_id, content_type)

    elif data.startswith("apply_critique_"):
        num = data.replace("apply_critique_", "")
        apply_critique_fix(chat_id, num)

    elif data == "ignore_critique":
        # Just dismiss and show content keyboard
        ctype = state.get("critique_content_type", "email")
        kb_map = {"email": email_action_keyboard, "ad": ad_action_keyboard,
                  "social": social_action_keyboard}
        kb_fn = kb_map.get(ctype, email_action_keyboard)
        send(chat_id, "Critique dismissed.", kb_fn())

    elif data == "mark_complete":
        send(chat_id, "Set complete. What would you like to do next?", mark_complete_keyboard())

    elif data == "log_perf_start":
        start_log_performance(chat_id)

# ── POLLING LOOP ──────────────────────────────────────────────────

def poll():
    offset = 0
    processed_updates = set()
    print("Cryptonary Bot V9 running.", flush=True)
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
                # Deduplication: skip if already processed (handles brief 409 overlaps)
                uid = update["update_id"]
                if uid in processed_updates:
                    continue
                processed_updates.add(uid)
                if len(processed_updates) > 500:
                    processed_updates.clear()
                try:
                    if "message" in update:
                        msg = update["message"]
                        chat_id = msg["chat"]["id"]
                        # Handle photo uploads
                        if "photo" in msg:
                            user_state.setdefault(chat_id, {"stage": "idle"})
                            stage = user_state[chat_id].get("stage", "idle")
                            content_stages = ["awaiting_report","buffering_report",
                                "awaiting_social_report","awaiting_ad_theme",
                                "awaiting_lp_context_text"]
                            ie_stages = ["ie_awaiting_screenshot_ideas",
                                "ie_awaiting_screenshot_critique"]
                            if stage in content_stages:
                                handle_content_file(chat_id, msg["photo"][-1], "image")
                            elif stage in ie_stages:
                                handle_ie_screenshot(chat_id, msg["photo"][-1], stage)
                            else:
                                handle_ds_file(chat_id, msg["photo"][-1], "image")
                        elif "document" in msg:
                            user_state.setdefault(chat_id, {"stage": "idle"})
                            stage = user_state[chat_id].get("stage", "idle")
                            doc = msg["document"]
                            mime = doc.get("mime_type", "")
                            content_stages = ["awaiting_report","buffering_report",
                                "awaiting_social_report","awaiting_ad_theme",
                                "awaiting_lp_context_text"]
                            ie_stages_doc = ["ie_awaiting_screenshot_ideas",
                                "ie_awaiting_screenshot_critique"]
                            if stage in content_stages:
                                handle_content_file(chat_id, doc, "pdf" if "pdf" in mime else "doc")
                            elif stage in ie_stages_doc:
                                handle_ie_screenshot(chat_id, doc, stage)
                            else:
                                ftype = "image" if mime.startswith("image/") else "csv"
                                handle_ds_file(chat_id, doc, ftype)
                        else:
                            handle_message(msg)
                    elif "callback_query" in update:
                        handle_callback(update["callback_query"])
                except Exception as e:
                    print("Handler error:", e, flush=True)
                    print(traceback.format_exc(), flush=True)
        except KeyboardInterrupt:
            print("Stopped.")
            break
        except Exception as e:
            print("Poll error:", e, flush=True)
            time.sleep(5)

# ── MAIN MENU ─────────────────────────────────────────────────────

def show_main_menu(chat_id):
    user_state[chat_id] = {"stage": "idle"}
    keyboard = [
        [{"text": "Cryptonary Content Studio", "callback_data": "open_content_studio"}],
        [{"text": "Cryptonary Data Studio", "callback_data": "open_data_studio"}],
        [{"text": "Cryptonary Idea Engine", "callback_data": "open_idea_engine"}]
    ]
    send(chat_id, "*Cryptonary OS*\n\nWhat would you like to do?", keyboard)


# ── AD CREATION FLOW ──────────────────────────────────────────────

AVATARS_AD = {
    "general":         ("General", "Broad appeal. Core fear: missing the move. Tone: direct, confident, data-led."),
    "trader":          ("Trader", "Active, needs an edge. Core fear: missing the setup. Tone: fast, sharp, alpha."),
    "investor":        ("Investor", "Long-term, wants conviction. Core fear: wrong long-term call. Tone: measured, premium."),
    "passive_income":  ("Passive Income Seeker", "Wants yield without complexity. Core fear: losing while trying to earn. Tone: calm, reassuring."),
    "portfolio":       ("Portfolio Builder", "Overwhelmed by token choices. Core fear: bad allocation. Tone: clear, structured."),
    "skeptic":         ("Skeptic", "Has been burned. Only buys on receipts. Core fear: being scammed again. Tone: proof-first."),
    "burned":          ("The Burned", "Lost money, wants redemption. Core fear: losing again. Tone: empathetic, offers a path."),
    "student":         ("College Student", "Smart, low funds, wants escape. Core fear: missing window while broke. Tone: energetic, aspirational."),
    "nine_to_five":    ("Burned-Out 9-5 Worker", "Wants an exit path. Core fear: trapped forever. Tone: emotional, freedom-focused."),
    "boomer":          ("Boomer Near Retirement", "Risk-averse, wants returns. Core fear: losing retirement savings. Tone: conservative, proof-heavy."),
    "side_hustle":     ("Side-Hustle Seeker", "Wants money now, clear steps. Core fear: wasting time. Tone: action-oriented, simple."),
    "beginner":        ("Complete Beginner", "Zero knowledge, overwhelmed. Core fear: getting it wrong. Tone: warm, zero jargon."),
    "chaser":          ("100X Chaser", "Degen, FOMO-driven. Core fear: missing the next 100X. Tone: high energy, exclusive access.")
}

FUNNEL_STAGES = {
    "awareness":      "AWARENESS: Problem/curiosity focus. No price mention. Stop the scroll. Make them feel the problem or the opportunity.",
    "consideration":  "CONSIDERATION: Education and proof. Build authority with track record. Use specific wins. Soft CTA.",
    "conversion":     "CONVERSION: Clear offer. Price $1,197/year. Urgency. Transformation CTA. Make the math obvious."
}

AD_LOGIC_PROMPT = """
CRYPTONARY TRACK RECORD (use these specifics):
- Called SOL at $10 (now $290+), WIF at $0.004 (1,200X), POPCAT (660X), SPX (227X), HYPE airdrop avg $28,500
- 7+ years, 3 full cycles since 2017
- 300,000+ subscribers, 12,000+ Pro members

COPYWRITING PRINCIPLES TO APPLY:
- Hormozi: Sell transformation not product. Stack specific value bullets.
- Cashvertising LF8: Lead with the avatar's dominant desire/fear.
- Cialdini: Social proof (show what members DO), Authority (track record), Scarcity (information gap).
- Ogilvy: Headline is everything. Specifics beat generalities. One CTA.
"""

def show_avatar_menu(chat_id, page=0):
    state = user_state[chat_id]
    selected = state.get("selected_avatars", [])
    state["avatar_page"] = page
    all_avatars = list(AVATARS_AD.items())
    page_size = 7
    start = page * page_size
    page_avatars = all_avatars[start:start + page_size]
    keyboard = []
    for key, (name, _) in page_avatars:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + name, "callback_data": "adavatar_" + key}])
    nav = []
    if page > 0:
        nav.append({"text": "Previous", "callback_data": "avatarpage_prev"})
    if start + page_size < len(all_avatars):
        nav.append({"text": "Next page", "callback_data": "avatarpage_next"})
    if nav:
        keyboard.append(nav)
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "adavatars_done"}])
    page_label = "(" + str(page+1) + "/2)" if len(all_avatars) > page_size else ""
    send(chat_id, "*Pick avatars:* " + page_label + "\n_(tap to select multiple)_", keyboard)

def show_stage_menu(chat_id):
    state = user_state[chat_id]
    selected = state.get("selected_stages", [])
    keyboard = []
    for key in ["awareness", "consideration", "conversion"]:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + key.capitalize(), "callback_data": "adstage_" + key}])
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "adstages_done"}])
    send(chat_id, "*Pick funnel stages:*\n_(tap to select multiple)_", keyboard)

def show_adtype_menu(chat_id):
    keyboard = [
        [{"text": "Static — 3 copy variants", "callback_data": "adtype_static"}],
        [{"text": "Video — AIDA script + 3 hook variants", "callback_data": "adtype_video"}]
    ]
    send(chat_id, "*Static or Video?*", keyboard)

def toggle_avatar(chat_id, avatar_key, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_avatars", [])
    if avatar_key in selected: selected.remove(avatar_key)
    else: selected.append(avatar_key)
    state["selected_avatars"] = selected
    page = state.get("avatar_page", 0)
    all_avatars = list(AVATARS_AD.items())
    page_size = 7
    start = page * page_size
    page_avatars = all_avatars[start:start + page_size]
    keyboard = []
    for key, (name, _) in page_avatars:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + name, "callback_data": "adavatar_" + key}])
    nav = []
    if page > 0:
        nav.append({"text": "Previous", "callback_data": "avatarpage_prev"})
    if start + page_size < len(all_avatars):
        nav.append({"text": "Next page", "callback_data": "avatarpage_next"})
    if nav:
        keyboard.append(nav)
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "adavatars_done"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def toggle_stage(chat_id, stage_key, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_stages", [])
    if stage_key in selected: selected.remove(stage_key)
    else: selected.append(stage_key)
    state["selected_stages"] = selected
    keyboard = []
    for key in ["awareness", "consideration", "conversion"]:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + key.capitalize(), "callback_data": "adstage_" + key}])
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "adstages_done"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def generate_all_ads(chat_id):
    state = user_state[chat_id]
    avatars = state.get("selected_avatars", [])
    stages = state.get("selected_stages", [])
    ad_type = state.get("ad_type", "static")
    theme = sanitise(state.get("ad_theme", ""))
    state["current_ad_output"] = ""  # Reset for fresh generation

    if not avatars or not stages:
        send(chat_id, "Please select at least one avatar and one funnel stage.")
        return

    total = len(avatars) * len(stages)
    send(chat_id, "Generating " + str(total) + " ad set(s)... This may take a moment.")

    for avatar_key in avatars:
        avatar_name, avatar_desc = AVATARS_AD.get(avatar_key, ("General", ""))
        for stage_key in stages:
            stage_instruction = FUNNEL_STAGES.get(stage_key, "")
            try:
                if ad_type == "static":
                    prompt = "Write 3 Meta static ad variants for Cryptonary Pro.\n\nAVATAR: " + avatar_name + "\n" + avatar_desc
                    if theme: prompt += "\n\nCAMPAIGN THEME/CONTEXT:\n" + theme
                    prompt += "\n\nFUNNEL STAGE: " + stage_instruction
                    prompt += "\n\n" + AD_LOGIC_PROMPT
                    prompt += "\n\nFor EACH of the 3 variants write:\nVARIANT N:\nHEADLINE: [max 10 words, scroll-stopping]\nPRIMARY TEXT: [150-200 words, leads with avatar emotion, builds to CTA]\nDESCRIPTION: [max 20 words, reinforces headline]\nCTA BUTTON: [e.g. Learn More / Get Started / Join Now]\n\nThen after all 3 variants:\nLOGIC:\nHook mechanism: [what stops the scroll]\nLF8 desire: [which life force desire and why]\nCialdini principle: [which one and why]\nFunnel logic: [why this stage approach]\n\nReturn as plain text."
                    voice_ex = get_voice_corpus_context(chat_id)
                    if voice_ex: prompt = voice_ex + "\n\n" + prompt
                    raw = claude(prompt, max_tokens=1800)
                    header = "*AD SET — " + avatar_name.upper() + " | " + stage_key.upper() + " | STATIC*\n\n"
                    send_plain(chat_id, header + raw)
                    # Accumulate output for critique/voice learning
                    state["current_ad_output"] = state.get("current_ad_output", "") + "\n\n" + header + raw[:600]
                else:
                    # Video: AIDA script + 3 hook variants
                    prompt = "Write a 30-45 second Meta video ad script for Cryptonary Pro using the AIDA formula.\n\nAVATAR: " + avatar_name + "\n" + avatar_desc
                    if theme: prompt += "\n\nCAMPAIGN THEME/CONTEXT:\n" + theme
                    prompt += "\n\nFUNNEL STAGE: " + stage_instruction
                    prompt += "\n\n" + AD_LOGIC_PROMPT
                    prompt += "\n\nSTRUCTURE:\n\nATTENTION (0-3 seconds): Pattern interrupt hook. Must stop the scroll.\n\nINTEREST (3-12 seconds): Agitate the problem or amplify the desire. Make them feel it.\n\nDESIRE (12-28 seconds): The solution. Specific proof points. Transformation.\n\nACTION (28-35 seconds): Clear CTA. What to do next.\n\nFormat each section as:\n[SECTION NAME]\nSPOKEN: [voiceover text]\nON SCREEN: [text overlays]\nVISUAL: [scene direction]\n\nThen write 3 ALTERNATIVE HOOKS (just the Attention section, different each time — pattern interrupt, question, bold claim):\n\nHOOK VARIANT 1:\nSPOKEN: ...\nON SCREEN: ...\nVISUAL: ...\n\nHOOK VARIANT 2: ...\nHOOK VARIANT 3: ...\n\nThen:\nLOGIC:\nHook mechanism: [what stops the scroll]\nLF8 desire: [which life force desire and why]\nCialdini principle: [which one and why]\nFunnel logic: [why this stage approach]\nAIDA breakdown: [one sentence per section on what it does psychologically]\n\nReturn as plain text."
                    raw = claude(prompt, max_tokens=2000)
                    header = "*AD SET — " + avatar_name.upper() + " | " + stage_key.upper() + " | VIDEO*\n\n"
                    send_plain(chat_id, header + raw)
                    # Accumulate output for critique/voice learning
                    state["current_ad_output"] = state.get("current_ad_output", "") + "\n\n" + header + raw[:600]
            except Exception as e:
                send(chat_id, "Error generating " + avatar_name + " / " + stage_key + ": " + str(e))

    state["stage"] = "ads_ready"
    # Silently save content metadata + copy for voice learning
    ad_output = state.get("current_ad_output", "")
    save_content_metadata(chat_id, "ad", {
        "avatars": state.get("selected_avatars", []),
        "stages": state.get("selected_stages", []),
        "ad_type": state.get("ad_type", "static"),
        "theme": state.get("ad_theme", "")[:200],
        "ad_body": ad_output[:600]
    })
    if ad_output:
        save_voice_example(chat_id, ad_output[:600], "approved_ad")
    send(chat_id, "All " + str(total) + " ad set(s) generated.", ad_action_keyboard())


# ── STANDALONE SOCIAL FLOW ────────────────────────────────────────

def gen_social_angles(chat_id):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    send(chat_id, "Finding angles...")
    try:
        raw = claude(
            "REPORT:\n" + report +
            "\n\nGenerate exactly 4 distinct social media content angles for this crypto market update. Each angle should be a different creative lens or emotional hook — not just rephrasing the same idea. Think: what makes someone stop scrolling?\n\nFormat:\n1. [angle]\n2. [angle]\n3. [angle]\n4. [angle]\nNothing else.",
            max_tokens=500
        )
        angles = parse_numbered_list(raw, 4)
        state["social_angles"] = angles
        state["stage"] = "pick_social_angle"
        text = "*Pick a content angle:*\n\n"
        keyboard = []
        for i, a in enumerate(angles):
            text += str(i+1) + ". " + a + "\n\n"
            keyboard.append([{"text": str(i+1) + ". " + a[:50], "callback_data": "social_angle_" + str(i)}])
        keyboard.append([{"text": "Write my own angle", "callback_data": "social_custom_angle"}])
        keyboard.append([{"text": "Regenerate angles", "callback_data": "social_regen_angles"}])
        send(chat_id, text, keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "idle"

def gen_social_hooks(chat_id):
    state = user_state[chat_id]
    report = sanitise(state.get("report", ""))
    angle = state.get("social_angle", "")
    formats = state.get("selected_social_formats", [])
    send(chat_id, "Writing hooks for your selected formats...")

    format_hook_instructions = {
        "fmt_reel": "REEL HOOK: Write 4 alternative opening spoken lines (first 3 seconds of a video). Must stop the scroll immediately. Punchy, direct, creates instant curiosity or tension. Max 15 words each.",
        "fmt_carousel": "CAROUSEL COVER: Write 4 alternative cover slide headlines. Bold statement that makes someone swipe. Max 8 words each. Think: headline of a magazine, not a sentence.",
        "fmt_story_single": "STORY HOOK: Write 4 alternative single-slide story text options. Immediate, bold, designed for someone who's already engaged. Max 12 words each.",
        "fmt_story_multi": "STORY OPENING: Write 4 alternative opening slide lines for a multi-slide story. Creates a cliffhanger that pulls to the next slide. Max 12 words each."
    }

    format_labels = {
        "fmt_reel": "Reel",
        "fmt_carousel": "Carousel",
        "fmt_story_single": "Story (single)",
        "fmt_story_multi": "Story (multi)"
    }

    state["social_hooks"] = {}
    state["selected_social_hooks"] = {}
    state["stage"] = "pick_social_hooks"

    for fmt in formats:
        if fmt not in format_hook_instructions:
            continue
        instruction = format_hook_instructions[fmt]
        label = format_labels.get(fmt, fmt)
        try:
            raw = claude(
                "REPORT:\n" + report[:500] +
                "\nANGLE: " + angle +
                "\n\n" + instruction +
                "\n\nFormat:\n1. [hook]\n2. [hook]\n3. [hook]\n4. [hook]\nNothing else.",
                max_tokens=400
            )
            hooks = parse_numbered_list(raw, 4)
            state["social_hooks"][fmt] = hooks
        except Exception as e:
            state["social_hooks"][fmt] = ["Hook option 1", "Hook option 2", "Hook option 3", "Hook option 4"]

    # Show hook picker for first format
    show_social_hook_picker(chat_id, 0)

def show_social_hook_picker(chat_id, fmt_idx):
    state = user_state[chat_id]
    formats = state.get("selected_social_formats", [])
    if fmt_idx >= len(formats):
        # All hooks selected - show format menu confirmation and generate
        show_standalone_social_menu_confirm(chat_id)
        return

    fmt = formats[fmt_idx]
    state["current_hook_fmt_idx"] = fmt_idx
    format_labels = {
        "fmt_reel": "Reel",
        "fmt_carousel": "Carousel",
        "fmt_story_single": "Story (single)",
        "fmt_story_multi": "Story (multi)"
    }
    label = format_labels.get(fmt, fmt)
    hooks = state.get("social_hooks", {}).get(fmt, [])
    remaining = len(formats) - fmt_idx

    text = "*Pick a hook for " + label + ":*"
    if remaining > 1:
        text += " (" + str(remaining - 1) + " more after this)"
    text += "\n\n"
    keyboard = []
    for i, h in enumerate(hooks):
        text += str(i+1) + ". " + h + "\n\n"
        keyboard.append([{"text": str(i+1) + ". " + h[:50], "callback_data": "social_hook_" + str(fmt_idx) + "_" + str(i)}])
    send(chat_id, text, keyboard)

def show_standalone_social_menu_confirm(chat_id):
    state = user_state[chat_id]
    formats = state.get("selected_social_formats", [])
    selected_hooks = state.get("selected_social_hooks", {})
    format_labels = {
        "fmt_reel": "Reel Script",
        "fmt_carousel": "Carousel",
        "fmt_story_single": "Story (single)",
        "fmt_story_multi": "Story (multi)"
    }
    summary = "*Ready to generate:*\n\n"
    for fmt in formats:
        hook = selected_hooks.get(fmt, "")
        summary += format_labels.get(fmt, fmt) + "\n"
        if hook:
            summary += "_Hook: " + hook[:60] + "_\n"
        summary += "\n"
    keyboard = [[{"text": "Generate all", "callback_data": "gen_social_confirmed"}]]
    send(chat_id, summary, keyboard)

def show_standalone_social_menu(chat_id):
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
    send(chat_id, "*Select formats to generate:*\n_(tap to select multiple)_", keyboard)



# ── FEEDBACK LOOP DATA STORE ──────────────────────────────────────
# email_log: {chat_id: [{subject, preview, angle, cta, email_type, date, open_rate, ctr, ab_variable, ab_label}]}
# ad_log:    {chat_id: [{ad_type, avatar, stage, headline, date, ...metrics}]}

email_log = {}
ad_log = {}


# ── EMAIL LOGGING ─────────────────────────────────────────────────

def start_log_email(chat_id):
    user_state[chat_id]["log_stage"] = "email_subject"
    user_state[chat_id]["stage"] = "logging_email"
    user_state[chat_id]["log_data"] = {}
    send(chat_id, "*Log Email Performance*\n\nEnter the subject line of the email:")

def handle_email_log_step(chat_id, text):
    state = user_state[chat_id]
    log = state.get("log_data", {})
    step = state.get("log_stage", "")

    if step == "email_subject":
        log["subject"] = text
        state["log_stage"] = "email_date"
        send(chat_id, "Date sent? (e.g. 2026-03-22)")

    elif step == "email_date":
        log["date"] = text
        state["log_stage"] = "email_open"
        send(chat_id, "Open rate? (enter number, e.g. 28.4)")

    elif step == "email_open":
        try:
            log["open_rate"] = float(text)
            state["log_stage"] = "email_ctr"
            send(chat_id, "Click-through rate? (enter number, e.g. 3.2)")
        except:
            send(chat_id, "Please enter a number, e.g. 28.4")

    elif step == "email_ctr":
        try:
            log["ctr"] = float(text)
            state["log_stage"] = "email_ab"
            keyboard = [
                [{"text": "Yes — part of a split test", "callback_data": "email_log_ab_yes"}],
                [{"text": "No — standalone email", "callback_data": "email_log_ab_no"}]
            ]
            send(chat_id, "Was this part of a split test?", keyboard)
        except:
            send(chat_id, "Please enter a number, e.g. 3.2")

    elif step == "email_ab_variable":
        log["ab_variable"] = text
        state["log_stage"] = "email_ab_label"
        send(chat_id, "What variant is this? (e.g. 'name in subject' or 'no name in subject')")

    elif step == "email_ab_label":
        log["ab_label"] = text
        state["log_stage"] = "email_recipients"
        send(chat_id, "How many recipients received this email? (enter number)")

    elif step == "email_recipients":
        try:
            log["recipients"] = int(text.replace(",",""))
            save_email_log(chat_id, log)
        except:
            send(chat_id, "Please enter a number, e.g. 12500")

def save_email_log(chat_id, log):
    if chat_id not in email_log:
        email_log[chat_id] = []
    email_log[chat_id].append(log)
    save_all_data()
    state = user_state[chat_id]
    state["stage"] = "idle"
    records = email_log[chat_id]
    opens = [r["open_rate"] for r in records if "open_rate" in r]
    ctrs = [r["ctr"] for r in records if "ctr" in r]
    avg_open = round(sum(opens)/len(opens), 1) if opens else 0
    avg_ctr = round(sum(ctrs)/len(ctrs), 1) if ctrs else 0
    msg = "*Email logged.*\n\n"
    msg += "Subject: _" + log.get("subject","") + "_\n"
    msg += "Open: " + str(log.get("open_rate","?")) + "% | CTR: " + str(log.get("ctr","?")) + "%\n\n"
    msg += "Your averages (" + str(len(records)) + " emails):\n"
    msg += "Open: " + str(avg_open) + "% | CTR: " + str(avg_ctr) + "%"
    if log.get("ab_variable"):
        msg += "\n\nTagged as split test: _" + log["ab_variable"] + "_ — variant: _" + log.get("ab_label","") + "_"
    keyboard = [[{"text": "Back to menu", "callback_data": "start_over"}]]
    send(chat_id, msg, keyboard)


# ── AD LOGGING ────────────────────────────────────────────────────

def start_log_ad(chat_id):
    state = user_state[chat_id]
    state["stage"] = "logging_ad"
    state["log_data"] = {}
    keyboard = [
        [{"text": "Video ad", "callback_data": "adlog_type_video"}],
        [{"text": "Static ad", "callback_data": "adlog_type_static"}]
    ]
    send(chat_id, "*Log Ad Performance*\n\nVideo or Static?", keyboard)

def handle_ad_log_step(chat_id, text):
    state = user_state[chat_id]
    log = state.get("log_data", {})
    step = state.get("log_stage", "")

    if step == "adlog_headline":
        log["headline"] = text
        state["log_stage"] = "adlog_avatar"
        keyboard = [[{"text": name, "callback_data": "adlog_avatar_" + key}] for key, (name, _) in AVATARS_AD.items()]
        send(chat_id, "Which avatar was this ad for?", keyboard)

    elif step == "adlog_date":
        log["date"] = text
        ad_type = log.get("ad_type", "static")
        if ad_type == "video":
            state["log_stage"] = "adlog_v_attention"
            send(chat_id, "3-second view rate? (Attention — 3s views / impressions as %, e.g. 12.5)")
        else:
            state["log_stage"] = "adlog_s_cpc"
            send(chat_id, "Cost per click? (CPC in GBP/USD, e.g. 0.85)")

    # VIDEO METRICS
    elif step == "adlog_v_attention":
        try:
            log["attention"] = float(text)
            state["log_stage"] = "adlog_v_interest"
            send(chat_id, "Average watch time in seconds? (Interest, e.g. 18)")
        except: send(chat_id, "Enter a number, e.g. 12.5")

    elif step == "adlog_v_interest":
        try:
            log["interest"] = float(text)
            state["log_stage"] = "adlog_v_desire"
            send(chat_id, "Outbound CTR? (Desire — %, e.g. 2.4)")
        except: send(chat_id, "Enter a number, e.g. 18")

    elif step == "adlog_v_desire":
        try:
            log["desire"] = float(text)
            state["log_stage"] = "adlog_v_purchases"
            send(chat_id, "Number of purchases (Action)? (e.g. 3)")
        except: send(chat_id, "Enter a number, e.g. 2.4")

    elif step == "adlog_v_purchases":
        try:
            log["purchases"] = int(text)
            state["log_stage"] = "adlog_v_cpp"
            send(chat_id, "Cost per purchase? (e.g. 45.00)")
        except: send(chat_id, "Enter a number, e.g. 3")

    elif step == "adlog_v_cpp":
        try:
            log["cost_per_purchase"] = float(text)
            save_ad_log(chat_id, log)
        except: send(chat_id, "Enter a number, e.g. 45.00")

    # STATIC METRICS
    elif step == "adlog_s_cpc":
        try:
            log["cpc"] = float(text)
            state["log_stage"] = "adlog_s_ctr"
            send(chat_id, "Outbound CTR? (%, e.g. 1.8)")
        except: send(chat_id, "Enter a number, e.g. 0.85")

    elif step == "adlog_s_ctr":
        try:
            log["outbound_ctr"] = float(text)
            state["log_stage"] = "adlog_s_purchases"
            send(chat_id, "Number of purchases? (e.g. 5)")
        except: send(chat_id, "Enter a number, e.g. 1.8")

    elif step == "adlog_s_purchases":
        try:
            log["purchases"] = int(text)
            state["log_stage"] = "adlog_s_cpp"
            send(chat_id, "Cost per purchase? (e.g. 38.50)")
        except: send(chat_id, "Enter a number, e.g. 5")

    elif step == "adlog_s_cpp":
        try:
            log["cost_per_purchase"] = float(text)
            save_ad_log(chat_id, log)
        except: send(chat_id, "Enter a number, e.g. 38.50")

def save_ad_log(chat_id, log):
    if chat_id not in ad_log:
        ad_log[chat_id] = []
    ad_log[chat_id].append(log)
    save_all_data()
    user_state[chat_id]["stage"] = "idle"
    msg = "*Ad logged.*\n\n"
    msg += "Headline: _" + log.get("headline","")[:60] + "_\n"
    msg += "Avatar: " + log.get("avatar","?") + " | Stage: " + log.get("stage","?") + "\n"
    if log.get("ad_type") == "video":
        msg += "Attention: " + str(log.get("attention","?")) + "% | Watch time: " + str(log.get("interest","?")) + "s | CTR: " + str(log.get("desire","?")) + "%\n"
    else:
        msg += "CPC: " + str(log.get("cpc","?")) + " | CTR: " + str(log.get("outbound_ctr","?")) + "%\n"
    msg += "Purchases: " + str(log.get("purchases","?")) + " | CPP: " + str(log.get("cost_per_purchase","?"))
    msg += "\n\nTotal ads logged: " + str(len(ad_log[chat_id]))
    keyboard = [[{"text": "Back to menu", "callback_data": "start_over"}]]
    send(chat_id, msg, keyboard)


# ── ANALYSIS ─────────────────────────────────────────────────────

def run_email_analysis(chat_id):
    records = email_log.get(chat_id, [])
    if len(records) < 2:
        send(chat_id, "Need at least 2 logged emails to analyse. Log more with /logemail")
        return
    send(chat_id, "Analysing " + str(len(records)) + " emails...")

    # Build summary for Claude
    summary = "EMAIL PERFORMANCE DATA:\n\n"
    for i, r in enumerate(records):
        summary += str(i+1) + ". Subject: " + r.get("subject","") + "\n"
        summary += "   Date: " + r.get("date","?") + " | Open: " + str(r.get("open_rate","?")) + "% | CTR: " + str(r.get("ctr","?")) + "%\n"
        if r.get("ab_variable"):
            summary += "   Split test: " + r["ab_variable"] + " — variant: " + r.get("ab_label","") + " | Recipients: " + str(r.get("recipients","?")) + "\n"
        summary += "\n"

    # Split test aggregation
    ab_groups = {}
    for r in records:
        if r.get("ab_variable") and r.get("ab_label") and r.get("recipients"):
            var = r["ab_variable"]
            label = r["ab_label"]
            if var not in ab_groups: ab_groups[var] = {}
            if label not in ab_groups[var]: ab_groups[var][label] = {"recipients": 0, "opens": 0, "clicks": 0, "count": 0}
            rec = r["recipients"]
            ab_groups[var][label]["recipients"] += rec
            ab_groups[var][label]["opens"] += int(rec * r.get("open_rate",0) / 100)
            ab_groups[var][label]["clicks"] += int(rec * r.get("ctr",0) / 100)
            ab_groups[var][label]["count"] += 1

    if ab_groups:
        summary += "\nSPLIT TEST AGGREGATED RESULTS:\n"
        for var, labels in ab_groups.items():
            summary += "\nVariable: " + var + "\n"
            for label, data in labels.items():
                agg_open = round(data["opens"] / data["recipients"] * 100, 1) if data["recipients"] else 0
                agg_ctr = round(data["clicks"] / data["recipients"] * 100, 1) if data["recipients"] else 0
                summary += "  " + label + ": " + str(agg_open) + "% open / " + str(agg_ctr) + "% CTR (" + str(data["count"]) + " emails, " + str(data["recipients"]) + " total recipients)\n"

    prompt = "Analyse this Cryptonary email performance data and provide:\n\n1. TOP PERFORMERS — top 3 emails and exactly what made them work (subject style, angle type, CTA)\n2. WORST PERFORMERS — bottom 3 and what likely caused underperformance\n3. PATTERN RECOGNITION — what patterns emerge across the data (which subject styles, angles, CTAs consistently outperform)\n4. SPLIT TEST RESULTS — if split test data exists, declare the winner with the aggregated numbers and statistical context\n5. ITERATION IDEAS — for the top performers, give 3 specific variations to test next\n6. IMPROVEMENT SUGGESTIONS — for underperformers, give specific fixes based on the copywriting principles you know\n\n" + summary + "\n\nBe specific and actionable. Reference actual subject lines and numbers."
    try:
        analysis = claude(prompt, max_tokens=2000)
        send_plain(chat_id, "EMAIL PERFORMANCE ANALYSIS\n\n" + analysis)
    except Exception as e:
        send(chat_id, "Error: " + str(e))

def run_ad_analysis(chat_id):
    records = ad_log.get(chat_id, [])
    if len(records) < 2:
        send(chat_id, "Need at least 2 logged ads to analyse. Log more with /logad")
        return
    send(chat_id, "Analysing " + str(len(records)) + " ads...")

    video_ads = [r for r in records if r.get("ad_type") == "video"]
    static_ads = [r for r in records if r.get("ad_type") == "static"]

    summary = "AD PERFORMANCE DATA:\n\n"

    if video_ads:
        summary += "VIDEO ADS (" + str(len(video_ads)) + "):\n"
        for i, r in enumerate(video_ads):
            summary += str(i+1) + ". Headline: " + r.get("headline","")[:60] + "\n"
            summary += "   Avatar: " + r.get("avatar","?") + " | Stage: " + r.get("stage","?") + " | Date: " + r.get("date","?") + "\n"
            summary += "   ATTENTION (3s view rate): " + str(r.get("attention","?")) + "%\n"
            summary += "   INTEREST (avg watch time): " + str(r.get("interest","?")) + "s\n"
            summary += "   DESIRE (outbound CTR): " + str(r.get("desire","?")) + "%\n"
            summary += "   ACTION: " + str(r.get("purchases","?")) + " purchases @ " + str(r.get("cost_per_purchase","?")) + " CPP\n\n"

    if static_ads:
        summary += "STATIC ADS (" + str(len(static_ads)) + "):\n"
        for i, r in enumerate(static_ads):
            summary += str(i+1) + ". Headline: " + r.get("headline","")[:60] + "\n"
            summary += "   Avatar: " + r.get("avatar","?") + " | Stage: " + r.get("stage","?") + " | Date: " + r.get("date","?") + "\n"
            summary += "   CPC: " + str(r.get("cpc","?")) + " | Outbound CTR: " + str(r.get("outbound_ctr","?")) + "%\n"
            summary += "   ACTION: " + str(r.get("purchases","?")) + " purchases @ " + str(r.get("cost_per_purchase","?")) + " CPP\n\n"

    prompt = "Analyse this Cryptonary Meta ad performance data and provide:\n\n1. TOP PERFORMERS — best 3 ads with exactly what made them work (avatar, stage, hook type, which metrics stood out)\n2. WORST PERFORMERS — bottom 3 and diagnose where they failed (for video: which AIDA stage had the biggest drop-off? for static: which metric was weakest?)\n3. PATTERN RECOGNITION — what patterns emerge? (which avatars convert best, which stages perform, which ad types win)\n4. VIDEO AIDA DIAGNOSIS — for video ads, map the drop-off: high attention but low interest = hook works but body fails. High desire but low action = landing page issue. Give specific diagnosis per video.\n5. ITERATION IDEAS FOR WINNERS — for top performers, give 3 specific variants to test next\n6. IMPROVEMENT SUGGESTIONS FOR LOSERS — specific creative fixes based on the AIDA failure point or static metric weakness\n\n" + summary + "\n\nBe specific. Reference actual headlines and numbers."
    try:
        analysis = claude(prompt, max_tokens=2000)
        send_plain(chat_id, "AD PERFORMANCE ANALYSIS\n\n" + analysis)
    except Exception as e:
        send(chat_id, "Error: " + str(e))


# ── PERSISTENCE ───────────────────────────────────────────────────

ANALYTICS_FILE = "analytics_data.json"

def save_all_data():
    try:
        data = {"email_log": {str(k): v for k, v in email_log.items()},
                "ad_log": {str(k): v for k, v in ad_log.items()},
                "performance_data": {str(k): v for k, v in performance_data.items()}}
        with open(ANALYTICS_FILE, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print("Analytics save error:", e)
    save_content_stores()

def load_all_data():
    global email_log, ad_log, performance_data
    try:
        with open(ANALYTICS_FILE, "r") as f:
            data = json.load(f)
        email_log = {int(k): v for k, v in data.get("email_log", {}).items()}
        ad_log = {int(k): v for k, v in data.get("ad_log", {}).items()}
        performance_data = {int(k): v for k, v in data.get("performance_data", {}).items()}
    except:
        pass

load_all_data()

BRANDSCRIPT_PROMPT = """
You are writing a Cryptonary landing page using the StoryBrand BrandScript framework.

BRANDSCRIPT RULES:
- The READER is the hero, not Cryptonary
- Cryptonary is the GUIDE (wise, empathetic, has a plan)
- Lead with the reader's dominant problem/desire, not our features
- Every section earns the scroll to the next
- One CTA, repeated at key moments

COPY PRINCIPLES:
- Hormozi: Stack specific value bullets before the ask. Make the math obvious. Transformation not subscription.
- Cashvertising LF8: Lead with the avatar's dominant life force desire. Fear works when threat is real + solution is clear.
- Cialdini: Social proof = what members DO (not just what they get). Authority = track record with specific wins. Scarcity = information gap.
- Ogilvy: Headline is a promise. Subheads carry the narrative. Specifics beat generalities. One CTA, zero friction.

CRYPTONARY PROOF POINTS (use these):
- Called SOL at $10 (now $290+), WIF at $0.004 (1,200X), POPCAT (660X), SPX (227X)
- HYPE airdrop average $28,500 for members
- 300,000+ newsletter subscribers, 12,000+ Pro members
- 7+ years, 3 full crypto cycles since 2017
- Pro: $1,197/year | Inner Circle: $15K-$22K (portfolios $200K+)

GRAPHIC RECOMMENDATION FORMAT (for each section):
VISUAL DIRECTION: [What to show, why it works psychologically, where to place it]
AI IMAGE PROMPT: [Ready-to-use Midjourney/DALL-E prompt, photorealistic style]
"""

LP_CTA_DEFS = {
    "pro": {
        "label": "Join Cryptonary Pro",
        "price": "$1,197/year",
        "cta_text": "Get Pro Access Now",
        "alt_cta": "Start Making Better Trades",
        "audience": "crypto investors and traders wanting research-backed guidance",
        "positioning": "The research platform that puts you ahead of the market. Not a signal service — a complete intelligence layer.",
        "urgency": "Markets don't wait. Every day without this costs you positioning."
    },
    "inner_circle": {
        "label": "Apply for Inner Circle",
        "price": "$15,000-$22,000",
        "cta_text": "Apply for Inner Circle",
        "alt_cta": "Apply Now — Limited Spots",
        "audience": "high-net-worth crypto investors with $200K+ portfolios",
        "positioning": "Private advisory for serious capital. Personal access to Co-Founder Asad for portfolio-level guidance.",
        "urgency": "Inner Circle is application-only. Spots are strictly limited to maintain quality of service."
    }
}

def show_lp_avatar_menu(chat_id, page=0):
    state = user_state[chat_id]
    selected = state.get("selected_avatars", [])
    state["avatar_page"] = page
    all_avatars = list(AVATARS_AD.items())
    page_size = 7
    start = page * page_size
    page_avatars = all_avatars[start:start + page_size]
    keyboard = []
    for key, (name, _) in page_avatars:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + name, "callback_data": "lpavatar_" + key}])
    nav = []
    if page > 0:
        nav.append({"text": "Previous", "callback_data": "lpavatarpage_prev"})
    if start + page_size < len(all_avatars):
        nav.append({"text": "Next page", "callback_data": "lpavatarpage_next"})
    if nav:
        keyboard.append(nav)
    page_label = "(" + str(page+1) + "/2)"
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "lpavatars_done"}])
    send(chat_id, "*Who is this landing page targeting?* " + page_label + "\n_(Select one or more avatars)_", keyboard)

def toggle_lp_avatar(chat_id, avatar_key, message_id):
    state = user_state[chat_id]
    selected = state.get("selected_avatars", [])
    if avatar_key in selected: selected.remove(avatar_key)
    else: selected.append(avatar_key)
    state["selected_avatars"] = selected
    page = state.get("avatar_page", 0)
    all_avatars = list(AVATARS_AD.items())
    page_size = 7
    start = page * page_size
    page_avatars = all_avatars[start:start + page_size]
    keyboard = []
    for key, (name, _) in page_avatars:
        is_sel = key in selected
        keyboard.append([{"text": ("[x] " if is_sel else "[ ] ") + name, "callback_data": "lpavatar_" + key}])
    nav = []
    if page > 0:
        nav.append({"text": "Previous", "callback_data": "lpavatarpage_prev"})
    if start + page_size < len(all_avatars):
        nav.append({"text": "Next page", "callback_data": "lpavatarpage_next"})
    if nav:
        keyboard.append(nav)
    keyboard.append([{"text": "Done — " + str(len(selected)) + " selected", "callback_data": "lpavatars_done"}])
    tg("editMessageReplyMarkup", {"chat_id": chat_id, "message_id": message_id, "reply_markup": {"inline_keyboard": keyboard}})

def show_lp_cta_menu(chat_id):
    keyboard = [
        [{"text": "Join Cryptonary Pro ($1,197/year)", "callback_data": "lpcta_pro"}],
        [{"text": "Apply for Inner Circle ($15K-$22K)", "callback_data": "lpcta_inner_circle"}]
    ]
    send(chat_id, "*What is the CTA for this landing page?*", keyboard)

def generate_landing_page(chat_id):
    state = user_state[chat_id]
    avatar_keys = state.get("selected_avatars", [])
    cta_key = state.get("lp_cta", "pro")
    context = sanitise(state.get("lp_context", ""))
    cta = LP_CTA_DEFS.get(cta_key, LP_CTA_DEFS["pro"])

    # Build avatar descriptions
    avatar_names = []
    avatar_descs = []
    for key in avatar_keys:
        name, desc = AVATARS_AD.get(key, ("General", ""))
        avatar_names.append(name)
        avatar_descs.append(name + ": " + desc)

    avatar_summary = " / ".join(avatar_names) if avatar_names else "General"
    avatar_detail = "\n".join(avatar_descs) if avatar_descs else "General crypto investor"

    send(chat_id, "Writing landing page for " + avatar_summary + " — " + cta["label"] + "...")

    sections = [
        ("HERO SECTION", "Write the Hero section. This is above the fold. Include:\n- H1 headline (max 10 words — promise or provoke)\n- H2 subheadline (max 20 words — expand the promise)\n- Hero body copy (2-3 sentences — the reader's problem and Cryptonary as guide)\n- Primary CTA button text\n- Secondary soft CTA (e.g. 'See how it works')\n\nThen graphic recommendations."),
        ("PROBLEM / VILLAIN SECTION", "Write the Problem section. Name the external problem (market noise, bad info), internal problem (fear of making wrong moves), and philosophical problem (serious investors deserve serious research). Make the reader feel understood.\n\nThen graphic recommendations."),
        ("GUIDE SECTION", "Write the Guide section. Establish Cryptonary's empathy (we've been in the market since 2017, we've seen all of this before) and authority (specific track record wins). The guide doesn't brag — they demonstrate.\n\nThen graphic recommendations."),
        ("THE PLAN", "Write the Plan section. Show 3-4 simple steps the reader takes to get the result:\n1. Join/Apply\n2. Get access to research/guidance\n3. Make informed decisions\n4. Build/protect wealth\n\nKeep it dead simple. Remove friction.\n\nThen graphic recommendations."),
        ("VALUE STACK", "Write the Value Stack section. List everything included with specific bullet points. Each bullet answers 'so what?' Lead with outcomes not features. End with price reveal and value anchor (what this level of research normally costs).\n\nThen graphic recommendations."),
        ("SOCIAL PROOF", "Write the Social Proof section. Use track record specifics, member outcomes, and testimonial structure. Format as 2-3 featured wins + a wall of shorter proof points.\n\nThen graphic recommendations."),
        ("CTA BLOCK", "Write the primary CTA block. This should create urgency, restate the transformation, show the price, handle the last objection ('is this worth it'), and include the CTA button. Direct CTA and transitional CTA both.\n\nThen graphic recommendations."),
        ("FAQ / OBJECTIONS", "Write 5 FAQs that handle the real objections for this avatar and CTA type. Format as question + concise punchy answer.\n\nThen graphic recommendations."),
        ("FOOTER CTA", "Write the final footer CTA. Last chance. Restate the core promise in one line. CTA button. One final piece of social proof.\n\nThen graphic recommendations.")
    ]

    all_output = []
    for section_name, section_instruction in sections:
        try:
            user_prompt = "LANDING PAGE BRIEF:\nAVATAR(S): " + avatar_detail
            user_prompt += "\nCTA: " + cta["label"] + " — " + cta["price"]
            user_prompt += "\nCTA BUTTON TEXT: " + cta["cta_text"]
            user_prompt += "\nPOSITIONING: " + cta["positioning"]
            user_prompt += "\nURGENCY MECHANIC: " + cta["urgency"]
            if context:
                user_prompt += "\nEXTRA CONTEXT: " + context
            user_prompt += "\n\nNOW WRITE THIS SECTION:\n" + section_name
            user_prompt += "\n\n" + section_instruction
            user_prompt += "\n\nIMPORTANT: Return as plain text. Start with the section name in CAPS as a header. Write all copy first. Then at the end write GRAPHIC RECOMMENDATIONS: with visual direction and AI image prompt clearly labelled. Do NOT write emails. Write landing page copy only."

            raw = claude(user_prompt, max_tokens=1200, system=BRANDSCRIPT_PROMPT)
            send_plain(chat_id, raw)
            all_output.append(raw)
            time.sleep(0.5)
        except Exception as e:
            send(chat_id, "Error on " + section_name + ": " + str(e))

    state["current_lp"] = "\n\n---\n\n".join(all_output)
    state["stage"] = "lp_ready"

    keyboard = [
        [{"text": "Quick Edit", "callback_data": "lp_quick_edit"},
         {"text": "Regenerate section", "callback_data": "lp_regen"}],
        [{"text": "Generate another page", "callback_data": "lp_again"},
         {"text": "Mark Complete", "callback_data": "mark_complete"}]
    ]
    send(chat_id, "Landing page complete.", keyboard)

# ══════════════════════════════════════════════════════════════════
# CRYPTONARY DATA STUDIO
# ══════════════════════════════════════════════════════════════════

DATA_STUDIO_SYSTEM = """
You are a performance analyst for Cryptonary, a crypto research and education platform.
Your job is to analyse marketing performance data extracted from screenshots or CSV files.

ANALYSIS PHILOSOPHY:
- Never just report numbers. Explain WHY something performed well or poorly.
- Look for patterns across the data — topic, format, hook style, avatar, funnel stage.
- Generate specific, actionable ideas based on what the patterns suggest.
- Use the A/B/C/D grading system (A=top 25%, B=above average, C=below average, D=bottom 25%).
- For metrics where lower is better (CPC, CPP), invert the grading.
- Always pool raw numbers for split tests — never average percentages.
- Compare like-for-like: ads vs ads of same avatar/stage, posts vs posts of same format.

GRADING SYSTEM:
A = Top 25% of cohort — Scale / Keep running
B = 26-50% — Above average, monitor
C = 51-75% — Below average, test changes
D = Bottom 25% — Kill or overhaul

OVERALL AD RATINGS:
Mostly A/B = SCALE
Mix A/B/C = KEEP AND MONITOR  
Mix B/C/D = TEST ONE CHANGE
Mostly C/D = KILL

VIDEO AIDA DIAGNOSIS:
- D on 3s view rate = Hook failing. Change opening 3 seconds.
- A on 3s, D on watch time = Hook works, body fails. Fix middle section.
- A/B on watch time, D on CTR = Watching but not clicking. Weak CTA or offer.
- A on CTR, D on CPP = Clicks but no purchase. Landing page problem not the ad.

META AD NAMING CONVENTION:
Format: IMG (static) or VID (video)
Stage: AWA (awareness), CDR (consideration), CNV (conversion)
Avatars: UNIVERSAL, TRADER, INVESTOR, PASSIVE_INCOME, PORTFOLIO, SKEPTIC, BURNED, STUDENT, 9_5, BOOMER, SIDE_HUSTLE, BEGINNER, CHASER
Angle: after Msg_

INSTAGRAM ENGAGEMENT RATE:
Engagement Rate = (Likes + Comments + Saves + Shares) / Reach × 100
Grade engagement rate within format cohort (Reels vs Reels etc).
"""

def show_data_studio_menu(chat_id):
    user_state[chat_id] = {"stage": "data_studio_idle"}
    keyboard = [
        [{"text": "Adverts", "callback_data": "ds_adverts"}],
        [{"text": "Social (Instagram)", "callback_data": "ds_social"}],
        [{"text": "Emails", "callback_data": "ds_emails"}],
        [{"text": "Landing Pages", "callback_data": "ds_landing"}]
    ]
    send(chat_id, "*Cryptonary Data Studio*\n\nWhich data would you like to analyse?", keyboard)

# ── AD ANALYSIS ───────────────────────────────────────────────────

def start_ds_adverts(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_ad_format_filter"
    keyboard = [
        [{"text": "All ads", "callback_data": "ad_filter_all"}],
        [{"text": "Video ads only", "callback_data": "ad_filter_video"}],
        [{"text": "Static ads only", "callback_data": "ad_filter_static"}]
    ]
    send(chat_id, "*Ad Performance Analysis*\n\nWhich ad types do you want to analyse?", keyboard)

def analyse_ads(chat_id):
    state = user_state[chat_id]
    images = state.get("ds_images", [])
    csv_text = state.get("ds_csv_text", "")
    if not images and not csv_text:
        send(chat_id, "No data uploaded. Please send screenshots or a CSV file first.")
        return
    send(chat_id, "Analysing your ad data...")
    # Get content context and history
    ctx = get_content_context(chat_id)
    try:
        if images:
            content_blocks = []
            for img_data in images:
                content_blocks.append({"type": "image", "source": {"type": "base64", "media_type": img_data["type"], "data": img_data["data"]}})
            content_blocks.append({"type": "text", "text": """Extract and analyse all ad performance data from these screenshots.

META AD NAMING: IMG=static, VID=video | AWA/CDR/CNV=funnel stage | Avatar in name | Msg_=angle

FILTER: Only analyse """ + {"all": "all ad types", "video": "VIDEO (VID) ads only — ignore any IMG/static ads", "static": "STATIC (IMG) ads only — ignore any VID/video ads"}.get(state.get("ds_ad_filter","all"), "all ad types") + """

IMPORTANT: First count how many qualifying ads are visible. State total count.

STEP 1 — DATA EXTRACTION:
List every qualifying ad with: Ad Name, Type (IMG/VID), Stage, Avatar, Angle, all metrics visible.

STEP 2 — GRADING (A/B/C/D quartiles within cohort):
Grade each ad on every metric. For CPP/CPC lower=better so invert grading.
Give each ad an overall rating: SCALE / KEEP / TEST / KILL

STEP 3 — COHORT ANALYSIS:
Grade each ad against its own cohort (same avatar + stage) AND overall.

STEP 4 — VIDEO AIDA DIAGNOSIS (video ads only):
Map where each video's funnel breaks: Attention → Interest → Desire → Action.

STEP 5 — PATTERN RECOGNITION:
What patterns emerge across avatar, stage, angle, ad type? Be specific.

STEP 6 — IDEAS:
Generate 5 specific new ad ideas based on what the patterns suggest. Not generic — specific angles, avatars, hooks derived from the data.

Format clearly with headers for each step.
""" + ctx})
            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 3000,
                "system": DATA_STUDIO_SYSTEM,
                "messages": [{"role": "user", "content": content_blocks}]
            }).encode()
        else:
            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 3000,
                "system": DATA_STUDIO_SYSTEM,
                "messages": [{"role": "user", "content": "Analyse this Meta Ads Manager CSV data:\n\n" + csv_text + "\n\nApply full grading, cohort analysis, AIDA diagnosis for videos, pattern recognition, and generate 5 specific new ad ideas."}]
            }).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
            headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=90) as r:
            result = json.loads(r.read())["content"][0]["text"]
        state["last_ds_analysis"] = result
        state["stage"] = "ds_analysis_done"
        send_plain(chat_id, result)
        # Extract and save patterns for future sessions
        extract_and_save_insights(chat_id, result, "ads")
        keyboard = [
            [{"text": "Ask a follow-up", "callback_data": "ds_followup"}],
            [{"text": "Upload more data", "callback_data": "ds_adverts"}],
            [{"text": "Back to Data Studio", "callback_data": "open_data_studio"}]
        ]
        send(chat_id, "Analysis complete.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e), flush=True)
        state["stage"] = "ds_awaiting_ad_data"

# ── SOCIAL ANALYSIS ───────────────────────────────────────────────

def start_ds_social(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_social_format_filter"
    keyboard = [
        [{"text": "All formats", "callback_data": "social_filter_all"}],
        [{"text": "Reels only", "callback_data": "social_filter_reels"}],
        [{"text": "Statics only", "callback_data": "social_filter_statics"}],
        [{"text": "Carousels only", "callback_data": "social_filter_carousels"}]
    ]
    send(chat_id, "*Instagram Performance Analysis*\n\nWhich formats do you want to analyse?", keyboard)

def analyse_social(chat_id):
    state = user_state[chat_id]
    images = state.get("ds_images", [])
    csv_text = state.get("ds_csv_text", "")
    if not images and not csv_text:
        send(chat_id, "No data uploaded. Please send screenshots or a CSV first.")
        return
    send(chat_id, "Analysing your Instagram data...")
    try:
        analysis_prompt = """You are analysing Instagram performance data for Cryptonary.

FORMAT FILTER: Only analyse """ + {"all": "all formats (Reels, Statics, and Carousels)", "reels": "REELS only — ignore Statics and Carousels", "statics": "STATICS only — ignore Reels and Carousels", "carousels": "CAROUSELS only — ignore Reels and Statics"}.get(state.get("ds_social_filter","all"), "all formats") + """

FORMAT DETECTION — look for these visual cues in the screenshots:
- REELS: show a Views metric (in addition to likes/saves etc) — video posts
- STATICS: single image posts — thumbnail has NO overlay indicator
- CAROUSELS: multi-image posts — thumbnail has a small white square tile indicator in the corner

If Minter shows a post type column, use that. Otherwise use the visual cues above.

PRIMARY SUCCESS METRIC: Engagement Rate = (Likes + Comments + Saves + Shares) / Reach × 100
Metric priority: Engagement Rate > Saves > Reach > Follows gained > Comments > Likes > Shares
Views are Reels-only and graded separately.

STEP 1 — DATA EXTRACTION:
State total posts found across ALL images combined.
For each post extract: caption snippet, format (Reel/Static/Carousel), date if shown, Reach, Likes, Comments, Saves, Shares, Views (Reels only), Follows gained if shown.
Calculate Engagement Rate for each post.

STEP 2 — GRADING (A/B/C/D quartiles — higher ER = better):
Grade WITHIN format cohort: Reels vs Reels, Statics vs Statics, Carousels vs Carousels.
Then give an overall cross-format rank.
Per-post rating: SCALE (mostly A/B) | KEEP (B/C) | REVIEW (C/D) | LEARN FROM (D)
For Reels, also grade Views count separately.

STEP 3 — FORMAT BREAKDOWN:
For each format present:
- Count of posts
- Average engagement rate
- Average reach
- Average saves
- Best performer with ER%
- Worst performer with ER%
- What this format is best used for based on this data

STEP 4 — CROSS-FORMAT COMPARISON:
Which format wins on: Engagement Rate / Reach / Saves / Follows gained?
Overall format verdict: which delivers most value right now and for what goal?

STEP 5 — CONTENT PATTERN ANALYSIS:
From captions and topics, identify:
- Which topics drive most saves?
- Which drive most comments?
- Which drive most reach?
- Any pricing/data posts vs opinion posts difference?
- Any BTC vs altcoin vs airdrop vs general crypto difference?

STEP 6 — PATTERN RECOGNITION:
3 strongest patterns with specific post evidence.

STEP 7 — IDEAS:
5 specific content ideas. For each: format, topic, hook, why the data supports it.

STEP 8 — TOTALS SUMMARY:
- Total posts analysed: N
- Overall average engagement rate: X%
- Best format by ER: [format] at [avg ER%]
- Best format by reach: [format]
- Best single post: [caption] — [ER%]
- Worst single post: [caption] — [ER%]

Format clearly with headers."""

        if images:
            content_blocks = []
            for img_data in images:
                content_blocks.append({"type": "image", "source": {"type": "base64", "media_type": img_data["type"], "data": img_data["data"]}})
            content_blocks.append({"type": "text", "text": analysis_prompt})
            messages = [{"role": "user", "content": content_blocks}]
        else:
            messages = [{"role": "user", "content": "Analyse this Instagram CSV data:\n\n" + csv_text + "\n\n" + analysis_prompt}]

        payload = json.dumps({"model": "claude-sonnet-4-20250514", "max_tokens": 3000,
            "system": DATA_STUDIO_SYSTEM, "messages": messages}).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
            headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=90) as r:
            result = json.loads(r.read())["content"][0]["text"]
        state["last_ds_analysis"] = result
        state["stage"] = "ds_analysis_done"
        send_plain(chat_id, result)
        extract_and_save_insights(chat_id, result, "social")
        keyboard = [
            [{"text": "Ask a follow-up", "callback_data": "ds_followup"}],
            [{"text": "Upload more data", "callback_data": "ds_social"}],
            [{"text": "Back to Data Studio", "callback_data": "open_data_studio"}]
        ]
        send(chat_id, "Analysis complete.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "ds_awaiting_social_data"

# ── EMAIL ANALYSIS ────────────────────────────────────────────────

def start_ds_emails(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_awaiting_email_splitvar"
    state["ds_images"] = []
    send(chat_id, "*Email Split Test Analysis*\n\nWhat variable are you testing?\n\n_e.g. Image vs No Image, Name in subject vs No name, Short subject vs Long subject_")

def start_ds_email_splittest(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_awaiting_email_splitvar"
    send(chat_id, "*Split Test Analysis*\n\nWhat variable are you testing? (e.g. 'name in subject line', 'curiosity gap vs data hook', 'short vs long preview')")

def analyse_emails(chat_id, split_var=None):
    state = user_state[chat_id]
    images = state.get("ds_images", [])
    csv_text = state.get("ds_csv_text", "")
    if not images and not csv_text:
        send(chat_id, "No data uploaded. Please send screenshots or a CSV first.")
        return
    ctx = get_content_context(chat_id)
    send(chat_id, "Analysing your email data...")
    split_instruction = ""
    if split_var:
        split_instruction = """YOU ARE RUNNING A SPLIT TEST CALCULATION. DO NOT DO A FULL EMAIL ANALYSIS.
DO NOT grade emails. DO NOT identify top/bottom performers. DO NOT generate ideas.
ONLY do the following steps and nothing else.

VARIABLE TESTED: """ + split_var + """
Content A = Image version | Content B = No Image version

THESE ARE BREVO A/B TEST SCREENSHOTS. Each screenshot is one campaign.
The TIMELINE section at the bottom of each screenshot contains the real test data.

STEP 1 — FROM EACH CAMPAIGN TIMELINE, EXTRACT:
- Campaign name and audience segment
- Total A/B sample: the number X from "have been sent to X random subscribers"
- Winner: which version (A or B) won and how many openers it had
- Format: | Campaign | Segment | Total A/B Sample | Winner | Winner Openers |

STEP 2 — WEIGHTED AGGREGATION:
For Content A wins: sum their total A/B sample sizes = A weighted sample
For Content B wins: sum their total A/B sample sizes = B weighted sample
Content A evidence % = A weighted / (A + B weighted) × 100
Content B evidence % = B weighted / (A + B weighted) × 100

STEP 3 — POOLED TOTALS ACROSS ALL CAMPAIGNS:
Sum all delivered numbers. Sum all raw opens (delivered × open_rate / 100). Sum all raw clicks.
Combined open rate = total opens / total delivered × 100
Combined CTR = total clicks / total delivered × 100
Show as a TOTALS row.

STEP 4 — VERDICT (5 lines maximum):
WINNER: [A or B] — won campaigns representing [X]% of total test recipients
SEGMENT PATTERN: [one line — did winner hold across all segments?]
POOLED RATE: [combined open rate across all campaigns]
CONFIDENCE: [INCONCLUSIVE <5,000 / DIRECTIONAL 5,000-20,000 / SIGNIFICANT 20,000+]
RECOMMENDATION: [one sentence]

NOTHING ELSE. No performance grades. No insights sections. No suggestions. Just the table, the maths, and the verdict.
"""
    try:
        if split_var:
            # For split tests, skip standard analysis entirely - just run the split calculation
            analysis_prompt = split_instruction
        else:
            analysis_prompt = """Extract and analyse all email performance data.

METRICS TO EXTRACT per email:
- Subject line
- Send date
- Recipients
- Open rate (%) — convert to raw opens = recipients × open_rate / 100
- CTR (%) — convert to raw clicks = recipients × ctr / 100
- Email type if identifiable (Free/Pro)

STEP 1 — DATA EXTRACTION:
List every email with all metrics including calculated raw opens and clicks.

STEP 2 — GRADING (A/B/C/D quartiles):
Grade each email on open rate and CTR.
A = top 25%, B = 26-50%, C = 51-75%, D = bottom 25%.

STEP 3 — TOP AND BOTTOM PERFORMERS:
Top 3 emails — what made them work? (subject style, topic, length, hook type)
Bottom 3 — what likely caused underperformance?

STEP 4 — PATTERN RECOGNITION:
Look for patterns in subject lines:
- Curiosity gap vs data-led vs fear-based vs contrarian
- With name vs without name
- Short vs long subjects
- Question vs statement
- Specific numbers vs general claims
Which patterns correlate with higher open rates and CTR?

STEP 5 — IDEAS:
Generate 5 specific subject line and angle ideas based on what the patterns suggest.
""" + split_instruction

        if split_var:
            send_msg = "Running split test calculation..."
        else:
            send_msg = "Running full analysis..."

        if images:
            content_blocks = []
            for img_data in images:
                content_blocks.append({"type": "image", "source": {"type": "base64", "media_type": img_data["type"], "data": img_data["data"]}})
            content_blocks.append({"type": "text", "text": analysis_prompt})
            messages = [{"role": "user", "content": content_blocks}]
        else:
            messages = [{"role": "user", "content": "Analyse this email performance CSV:\n\n" + csv_text + "\n\n" + analysis_prompt}]

        payload = json.dumps({"model": "claude-sonnet-4-20250514", "max_tokens": 3000,
            "system": DATA_STUDIO_SYSTEM, "messages": messages}).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
            headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=90) as r:
            result = json.loads(r.read())["content"][0]["text"]
        state["last_ds_analysis"] = result
        state["stage"] = "ds_analysis_done"
        send_plain(chat_id, result)
        extract_and_save_insights(chat_id, result, "emails")
        keyboard = [
            [{"text": "Ask a follow-up", "callback_data": "ds_followup"}],
            [{"text": "Upload more data", "callback_data": "ds_emails"}],
            [{"text": "Back to Data Studio", "callback_data": "open_data_studio"}]
        ]
        send(chat_id, "Analysis complete.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "ds_awaiting_email_data"

# ── LANDING PAGE ANALYSIS ─────────────────────────────────────────

def start_ds_landing(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_awaiting_landing_splitvar"
    state["ds_images"] = []
    send(chat_id, "*Landing Page Split Test*\n\nWhat variable are you testing?\n\n_e.g. Hero headline A vs B, Pro vs Inner Circle CTA, With guarantee vs Without_")

def start_ds_landing_splittest(chat_id):
    state = user_state[chat_id]
    state["stage"] = "ds_awaiting_landing_splitvar"
    send(chat_id, "*Landing Page Split Test*\n\nWhat variable are you testing? (e.g. 'hero headline A vs B', 'Pro vs Inner Circle CTA', 'with guarantee vs without')")

def analyse_landing(chat_id, split_var=None):
    state = user_state[chat_id]
    images = state.get("ds_images", [])
    csv_text = state.get("ds_csv_text", "")
    if not images and not csv_text:
        send(chat_id, "No data uploaded. Please send screenshots or a CSV first.")
        return
    ctx = get_content_context(chat_id)
    send(chat_id, "Analysing your landing page data...")
    split_instruction = ""
    if split_var:
        split_instruction = f"""
SPLIT TEST ANALYSIS FOR: {split_var}

POOL RAW NUMBERS:
For each variant: total sessions, total conversions = sessions × CVR / 100
Pooled CVR = total conversions / total sessions × 100

Statistical confidence:
- Under 500 combined sessions = INCONCLUSIVE
- 500–2,000 = DIRECTIONAL
- 2,000+ = SIGNIFICANT

Declare winner with pooled numbers and confidence.
"""
    try:
        analysis_prompt = """Extract and analyse all landing page performance data.

METRICS TO EXTRACT:
- Page variant/name
- Traffic source (Meta/organic/email if available)
- Sessions
- CVR (%)
- Conversions (raw) = sessions × CVR / 100 if not provided
- Bounce rate if available
- Revenue/CPL if available

STEP 1 — DATA EXTRACTION with calculated conversions.

STEP 2 — GRADING on CVR (primary) and bounce rate.

STEP 3 — TOP AND BOTTOM PERFORMERS with diagnosis.

STEP 4 — TRAFFIC SOURCE BREAKDOWN: Does CVR vary by source?

STEP 5 — PATTERN RECOGNITION: What page variants, sections, or CTAs correlate with higher CVR?

STEP 6 — IDEAS: 5 specific test hypotheses based on the patterns.
""" + ctx

        if images:
            content_blocks = []
            for img_data in images:
                content_blocks.append({"type": "image", "source": {"type": "base64", "media_type": img_data["type"], "data": img_data["data"]}})
            content_blocks.append({"type": "text", "text": analysis_prompt})
            messages = [{"role": "user", "content": content_blocks}]
        else:
            messages = [{"role": "user", "content": "Analyse this landing page CSV:\n\n" + csv_text + "\n\n" + analysis_prompt}]

        payload = json.dumps({"model": "claude-sonnet-4-20250514", "max_tokens": 3000,
            "system": DATA_STUDIO_SYSTEM, "messages": messages}).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
            headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
        with urllib.request.urlopen(req, timeout=90) as r:
            result = json.loads(r.read())["content"][0]["text"]
        state["last_ds_analysis"] = result
        state["stage"] = "ds_analysis_done"
        send_plain(chat_id, result)
        extract_and_save_insights(chat_id, result, "landing")
        keyboard = [
            [{"text": "Ask a follow-up", "callback_data": "ds_followup"}],
            [{"text": "Upload more data", "callback_data": "ds_landing"}],
            [{"text": "Back to Data Studio", "callback_data": "open_data_studio"}]
        ]
        send(chat_id, "Analysis complete.", keyboard)
    except Exception as e:
        send(chat_id, "Error: " + str(e))
        state["stage"] = "ds_awaiting_landing_data"

# ── IMAGE/CSV HANDLER ─────────────────────────────────────────────

def handle_ds_file(chat_id, file_info, file_type="image"):
    """Download and store uploaded file for analysis."""
    state = user_state.get(chat_id, {})
    stage = state.get("stage", "")
    if not stage.startswith("ds_awaiting"):
        return False
    try:
        file_id = file_info.get("file_id")
        # Get file path from Telegram
        path_data = tg("getFile", {"file_id": file_id})
        file_path = path_data.get("result", {}).get("file_path", "")
        if not file_path:
            return False
        url = "https://api.telegram.org/file/bot" + TELEGRAM_TOKEN + "/" + file_path
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as r:
            file_bytes = r.read()
        import base64
        if file_type == "image":
            # Detect image type
            mime = "image/jpeg"
            if file_path.endswith(".png"): mime = "image/png"
            elif file_path.endswith(".gif"): mime = "image/gif"
            elif file_path.endswith(".webp"): mime = "image/webp"
            encoded = base64.b64encode(file_bytes).decode()
            if "ds_images" not in state: state["ds_images"] = []
            state["ds_images"].append({"type": mime, "data": encoded})
            count = len(state["ds_images"])

            # Quick validation - ask Claude what it can see in this image
            stage = state.get("stage", "")
            context_hint = "Meta Ads Manager data" if "ad" in stage else "Instagram analytics data" if "social" in stage else "email performance data" if "email" in stage else "landing page analytics data"
            # For split test flows, skip preview to avoid partial data commentary
            is_split = "split" in stage
            if is_split:
                preview = "Screenshot received."
            else:
                try:
                    check_payload = json.dumps({
                        "model": "claude-sonnet-4-20250514",
                        "max_tokens": 150,
                        "messages": [{"role": "user", "content": [
                            {"type": "image", "source": {"type": "base64", "media_type": mime, "data": encoded}},
                            {"type": "text", "text": "This should contain " + context_hint + ". In one short sentence: what data can you see? If there are rows/ads/posts, how many? If the data is cut off or unclear, say so. Be specific and brief."}
                        ]}]
                    }).encode()
                    check_req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=check_payload,
                        headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
                    with urllib.request.urlopen(check_req, timeout=30) as r:
                        preview = json.loads(r.read())["content"][0]["text"].strip()
                except:
                    preview = "Image received."

            # Determine button label based on count
            ds_stage_map = {
                "ds_awaiting_ad_data": "ds_analyse_ads",
                "ds_awaiting_social_data": "ds_analyse_social",
                "ds_awaiting_email_data": "ds_analyse_emails",
                "ds_awaiting_email_split_data": "ds_analyse_emails_split",
                "ds_awaiting_landing_data": "ds_analyse_landing",
                "ds_awaiting_landing_split_data": "ds_analyse_landing_split"
            }
            analyse_cb = ds_stage_map.get(stage, "ds_analyse_ads")

            keyboard = [
                [{"text": "Analyse this", "callback_data": analyse_cb}],
                [{"text": "Add another screenshot", "callback_data": "ds_add_more_" + stage}]
            ]
            msg = "Got it. " + preview
            if count > 1:
                msg += "\n\n" + str(count) + " images queued."
            send(chat_id, msg, keyboard)
        else:
            # CSV or document — decode as text
            try:
                text = file_bytes.decode("utf-8")
            except:
                text = file_bytes.decode("latin-1")
            state["ds_csv_text"] = text[:15000]  # limit to 15k chars
            send(chat_id, "File received (" + str(len(text)) + " characters). Tap Done to analyse.")
        return True
    except Exception as e:
        send(chat_id, "Error reading file: " + str(e))
        return False

# ══════════════════════════════════════════════════════════════════
# CONTENT METADATA + PATTERN MEMORY ENGINE
# ══════════════════════════════════════════════════════════════════

import datetime as _dt

CONTENT_STORE_FILE = "content_metadata.json"
INSIGHTS_FILE = "pattern_insights.json"

# In-memory stores
content_metadata = {}   # {chat_id: [{type, date, metadata...}]}
pattern_insights = {}   # {chat_id: [{date, insight, source}]}

VOICE_CORPUS_FILE = "voice_corpus.json"
voice_corpus = {}  # {chat_id: [{date, text, source_type}]}

def load_content_stores():
    global content_metadata, pattern_insights, voice_corpus
    try:
        with open(CONTENT_STORE_FILE, "r") as f:
            raw = json.load(f)
        content_metadata = {int(k): v for k, v in raw.items()}
    except:
        pass
    try:
        with open(INSIGHTS_FILE, "r") as f:
            raw = json.load(f)
        pattern_insights = {int(k): v for k, v in raw.items()}
    except:
        pass
    try:
        with open(VOICE_CORPUS_FILE, "r") as f:
            raw = json.load(f)
        voice_corpus = {int(k): v for k, v in raw.items()}
    except:
        pass

def save_content_stores():
    try:
        with open(CONTENT_STORE_FILE, "w") as f:
            json.dump({str(k): v for k, v in content_metadata.items()}, f)
    except Exception as e:
        print("Content store save error:", e, flush=True)
    try:
        with open(INSIGHTS_FILE, "w") as f:
            json.dump({str(k): v for k, v in pattern_insights.items()}, f)
    except Exception as e:
        print("Insights save error:", e, flush=True)
    try:
        with open(VOICE_CORPUS_FILE, "w") as f:
            json.dump({str(k): v for k, v in voice_corpus.items()}, f)
    except Exception as e:
        print("Voice corpus save error:", e, flush=True)

def save_voice_example(chat_id, text, source_type="approved"):
    """Save approved copy to voice corpus for self-learning."""
    if not text or len(text.strip()) < 50:
        return
    if chat_id not in voice_corpus:
        voice_corpus[chat_id] = []
    voice_corpus[chat_id].append({
        "date": _dt.datetime.now().strftime("%Y-%m-%d"),
        "text": text.strip(),
        "source": source_type
    })
    # Keep last 100 examples
    if len(voice_corpus[chat_id]) > 100:
        voice_corpus[chat_id] = voice_corpus[chat_id][-100:]
    save_content_stores()

def get_voice_corpus_context(chat_id):
    """Return recent approved examples for injection into generation prompts."""
    examples = voice_corpus.get(chat_id, [])
    if not examples:
        return ""
    recent = examples[-5:]
    ctx = "\n\n=== APPROVED WRITING EXAMPLES (Adam's actual voice — match this style) ===\n"
    for ex in recent:
        ctx += "\n[" + ex.get("source","") + " — " + ex.get("date","") + "]\n"
        ctx += ex.get("text","") + "\n"
    return ctx

def save_content_metadata(chat_id, content_type, metadata):
    """Called silently when content is approved. Stores what was created."""
    if chat_id not in content_metadata:
        content_metadata[chat_id] = []
    record = {
        "type": content_type,
        "date": _dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        **metadata
    }
    content_metadata[chat_id].append(record)
    # Keep last 200 records per user
    if len(content_metadata[chat_id]) > 200:
        content_metadata[chat_id] = content_metadata[chat_id][-200:]
    save_content_stores()

def save_pattern_insight(chat_id, insight, source="analysis"):
    """Save a pattern discovered during analysis for future reference."""
    if chat_id not in pattern_insights:
        pattern_insights[chat_id] = []
    pattern_insights[chat_id].append({
        "date": _dt.datetime.now().strftime("%Y-%m-%d"),
        "insight": insight,
        "source": source
    })
    if len(pattern_insights[chat_id]) > 100:
        pattern_insights[chat_id] = pattern_insights[chat_id][-100:]
    save_content_stores()

def get_content_context(chat_id):
    """Build context string from stored metadata for use in analysis prompts."""
    records = content_metadata.get(chat_id, [])
    insights = pattern_insights.get(chat_id, [])
    if not records and not insights:
        return ""

    ctx = "\n\n=== CONTENT HISTORY & KNOWN PATTERNS ===\n"

    if records:
        ctx += "\nRECENT CONTENT CREATED (last 20):\n"
        for r in records[-20:]:
            line = "- [" + r.get("date","") + "] " + r.get("type","").upper()
            if r.get("angle"): line += " | Angle: " + r["angle"][:60]
            if r.get("hook_subject"): line += " | Subject: " + r["hook_subject"][:50]
            if r.get("free_cta"): line += " | CTA: " + r["free_cta"]
            if r.get("tone") and r["tone"] != "standard": line += " | Tone: " + r["tone"]
            if r.get("avatars"): line += " | Avatars: " + ", ".join(r["avatars"])
            if r.get("ad_type"): line += " | Type: " + r["ad_type"]
            ctx += line + "\n"

    if insights:
        ctx += "\nPREVIOUSLY DISCOVERED PATTERNS:\n"
        for ins in insights[-15:]:
            ctx += "- [" + ins.get("date","") + "] " + ins.get("insight","") + "\n"

    return ctx

def extract_and_save_insights(chat_id, analysis_text, source_type):
    """After analysis, extract key patterns and save them for future sessions."""
    try:
        raw = claude(
            "From this marketing analysis, extract 3-5 specific, memorable patterns or insights that should be remembered for future campaigns. Focus on what consistently works or fails.\n\nAnalysis:\n" + analysis_text[:3000] +
            "\n\nFormat each insight as one clear sentence starting with the content type and specific finding. Example: 'PASSIVE_INCOME ads consistently outperform at CDR stage with 50% lower CPP than average.' Return as a numbered list only.",
            max_tokens=400,
            system=DATA_STUDIO_SYSTEM
        )
        lines = [l.strip() for l in raw.split('\n') if l.strip() and l.strip()[0].isdigit()]
        for line in lines:
            import re as _re
            m = _re.match(r'^\d+\.\s*(.+)', line)
            if m:
                save_pattern_insight(chat_id, m.group(1), source_type)
    except Exception as e:
        print("Insight extraction error:", e, flush=True)

def get_preanalysis_checklist(data_type, item_count):
    """Returns warning if sample size is too small."""
    thresholds = {
        "ads": {"min": 5, "warn": 10},
        "emails": {"min": 3, "warn": 8},
        "social": {"min": 5, "warn": 10},
        "landing": {"min": 3, "warn": 6}
    }
    t = thresholds.get(data_type, {"min": 3, "warn": 5})
    if item_count < t["min"]:
        return ("TOO_SMALL", "Only " + str(item_count) + " items found. Minimum " + str(t["min"]) + " needed for meaningful analysis. Results may be misleading — consider gathering more data first.")
    elif item_count < t["warn"]:
        return ("SMALL", "Small sample (" + str(item_count) + " items). Analysis will run but treat conclusions as directional, not definitive.")
    return ("OK", "")

# Load on startup
load_content_stores()

# ══════════════════════════════════════════════════════════════════
# WEEKLY BRIEFING ENGINE
# ══════════════════════════════════════════════════════════════════

BRIEFING_CHAT_IDS_FILE = "briefing_subscribers.json"

def load_briefing_subscribers():
    try:
        with open(BRIEFING_CHAT_IDS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_briefing_subscribers(ids):
    try:
        with open(BRIEFING_CHAT_IDS_FILE, "w") as f:
            json.dump(ids, f)
    except Exception as e:
        print("Briefing subscriber save error:", e, flush=True)

def fetch_market_data():
    """Fetch BTC price, Fear & Greed index, and top crypto news."""
    results = {}
    try:
        # BTC price from CoinGecko public API
        req = urllib.request.Request(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true&include_7d_change=true",
            headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            btc = data.get("bitcoin", {})
            results["btc_price"] = btc.get("usd", 0)
            results["btc_24h"] = round(btc.get("usd_24h_change", 0), 1)
            results["btc_7d"] = round(btc.get("usd_7d_change", 0), 1)
    except Exception as e:
        results["btc_price"] = 0
        results["btc_24h"] = 0
        results["btc_7d"] = 0
        print("BTC price fetch error:", e, flush=True)

    try:
        # Fear & Greed from alternative.me
        req = urllib.request.Request(
            "https://api.alternative.me/fng/?limit=1",
            headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
            fng = data.get("data", [{}])[0]
            results["fng_value"] = fng.get("value", "N/A")
            results["fng_label"] = fng.get("value_classification", "N/A")
    except Exception as e:
        results["fng_value"] = "N/A"
        results["fng_label"] = "N/A"
        print("Fear & Greed fetch error:", e, flush=True)

    return results

def get_last_week_performance(chat_id):
    """Summarise last week's content and performance from stored data."""
    summary = []
    records = content_metadata.get(chat_id, [])
    insights = pattern_insights.get(chat_id, [])
    email_records = email_log.get(chat_id, [])
    ad_records = ad_log.get(chat_id, [])

    # Content created in last 7 days
    from datetime import datetime as _datetime, timedelta as _timedelta
    week_ago = (_datetime.now() - _timedelta(days=7)).strftime("%Y-%m-%d")
    recent = [r for r in records if r.get("date","") >= week_ago]
    if recent:
        email_count = len([r for r in recent if r.get("type") == "email"])
        ad_count = len([r for r in recent if r.get("type") == "ad"])
        summary.append(str(len(recent)) + " pieces created last week (" + str(email_count) + " emails, " + str(ad_count) + " ads)")

    # Best logged email
    if email_records:
        best = max(email_records, key=lambda r: r.get("open_rate", 0))
        summary.append("Best email: " + best.get("subject","")[:50] + " — " + str(best.get("open_rate","?")) + "% open / " + str(best.get("ctr","?")) + "% CTR")

    # Recent insights
    recent_insights = [i for i in insights if i.get("date","") >= week_ago]
    if recent_insights:
        summary.append("Recent pattern: " + recent_insights[-1].get("insight",""))

    return summary

def generate_briefing(chat_id):
    """Generate and send the full weekly briefing."""
    send(chat_id, "Generating your weekly briefing...")

    # Register this chat for auto-briefing
    subscribers = load_briefing_subscribers()
    if chat_id not in subscribers:
        subscribers.append(chat_id)
        save_briefing_subscribers(subscribers)

    # Fetch live data
    market = fetch_market_data()
    perf_summary = get_last_week_performance(chat_id)

    # Build context for Claude
    market_context = ""
    if market.get("btc_price"):
        price = "${:,.0f}".format(market["btc_price"])
        market_context += "BTC: " + price + " (" + str(market["btc_7d"]) + "% 7d, " + str(market["btc_24h"]) + "% 24h)\n"
    if market.get("fng_value") != "N/A":
        market_context += "Fear & Greed: " + str(market["fng_value"]) + " (" + market["fng_label"] + ")\n"

    perf_context = "\n".join(perf_summary) if perf_summary else "No performance data logged yet."

    try:
        # Use web search for news via Claude
        news_prompt = "Search for the top 3 most important crypto/Bitcoin news stories from the past 7 days. For each give: headline, one sentence summary, and why it matters for crypto investors and marketers. Be specific with dates and numbers."

        briefing_prompt = """You are the chief strategist for Cryptonary, a crypto research platform with 300K+ subscribers.

Generate a weekly Monday morning briefing for Adam (Co-Founder). Be direct, specific, and actionable.

MARKET DATA:
""" + market_context + """

LAST WEEK'S PERFORMANCE:
""" + perf_context + """

STRUCTURE THE BRIEFING EXACTLY AS:

MARKET PULSE
[BTC price, 7d change, Fear & Greed with one line on what it means for content tone this week]

TOP STORIES THIS WEEK
[3 most important crypto stories from the past 7 days with specific numbers and why each matters for Cryptonary's content]

LAST WEEK RECAP
[Summary of what was created and best performance metrics. If no data: note that logging performance in Data Studio will make this section more useful over time]

THIS WEEK'S CONTENT PLAN
[Specific recommendations based on market conditions and news:]
- Monday email angle: [specific suggestion based on market mood]
- Mid-week content: [social or email suggestion]
- Ad focus: [which avatar/stage to push given current market sentiment]
- Social: [1-2 specific post ideas tied to the week's news]

TONE RECOMMENDATION
[Based on Fear & Greed + price action: Standard / Aggressive / Empathetic and why]

Keep it tight. Every line should be actionable. No fluff."""

        result = claude(briefing_prompt, max_tokens=1500, system=DATA_STUDIO_SYSTEM)

        # Format header
        from datetime import datetime as _dt2
        date_str = _dt2.now().strftime("%A %d %B %Y")
        header = "CRYPTONARY WEEKLY BRIEFING\n" + date_str + "\n\n"

        send_plain(chat_id, header + result)

        keyboard = [
            [{"text": "Generate Monday email", "callback_data": "mode_email"},
             {"text": "Generate social content", "callback_data": "mode_social"}],
            [{"text": "Generate ads", "callback_data": "mode_ads"},
             {"text": "Refresh briefing", "callback_data": "briefing_refresh"}]
        ]
        send(chat_id, "Briefing complete. What do you want to create first?", keyboard)

    except Exception as e:
        print("Briefing error:", e, flush=True)
        send(chat_id, "Error generating briefing: " + str(e))


# ── AUTO BRIEFING SCHEDULER ───────────────────────────────────────
# Runs inside the poll loop - checks if it's Monday 7-8am GMT and sends briefing

_last_briefing_date = None

def check_and_send_briefing():
    """Called from poll loop. Sends briefing to all subscribers on Monday 7-8am GMT."""
    global _last_briefing_date
    from datetime import datetime as _dt3
    now = _dt3.utcnow()
    today = now.strftime("%Y-%m-%d")

    # Monday = 0, hour 7
    if now.weekday() == 0 and now.hour == 7 and _last_briefing_date != today:
        _last_briefing_date = today
        subscribers = load_briefing_subscribers()
        print("Sending weekly briefing to", len(subscribers), "subscribers", flush=True)
        for chat_id in subscribers:
            try:
                generate_briefing(chat_id)
                time.sleep(2)  # avoid rate limits between sends
            except Exception as e:
                print("Briefing send error for", chat_id, ":", e, flush=True)

# ══════════════════════════════════════════════════════════════════
# CRYPTONARY IDEA ENGINE
# ══════════════════════════════════════════════════════════════════

IDEA_ENGINE_SOURCES_FILE = "idea_sources.json"

# Cryptonary's source list
DEFAULT_SOURCES = {
    "instagram": [
        "cryptonary",
        "altcoinpost", "coinsauce", "algoresearch", "daytrading",
        "simplyougrow", "0x100x", "mange.marketing", "lukedavis.ig",
        "watcher.guru", "moonpay", "coinbase", "cryptocomofficial",
        "bitcoinmagazine"
    ],
    "twitter": [
        "watcherguru", "trendingbitcoin", "capitalflows", "coindesk",
        "bloomberg", "FT", "glxyresearch", "caprioleio",
        "lookonchain", "wublockchain", "documentingbtc"
    ],
    "twitter_ads_inspiration": ["the_adprofessor"],
    "facebook_pages": ["730238507162118"],
    "facebook_urls": [
        "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=GB&is_targeted_country=false&media_type=all&search_type=page&sort_data[direction]=desc&sort_data[mode]=total_impressions&view_all_page_id=730238507162118"
    ],
    "telegram": [],
    "reddit": ["cryptocurrency", "bitcoin", "ethfinance", "CryptoMarkets"],
    "own_accounts": {
        "instagram": "cryptonary",
        "twitter": "cryptonary",
        "facebook_page_id": "730238507162118"
    }
}

def load_idea_sources():
    try:
        with open(IDEA_ENGINE_SOURCES_FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_SOURCES.copy()

def save_idea_sources(sources):
    try:
        with open(IDEA_ENGINE_SOURCES_FILE, "w") as f:
            json.dump(sources, f)
    except Exception as e:
        print("Sources save error:", e, flush=True)

def show_idea_engine_menu(chat_id):
    user_state[chat_id] = {"stage": "idea_engine_idle"}
    sources = load_idea_sources()
    source_count = (len(sources.get("instagram",[])) + len(sources.get("twitter",[])) +
                   len(sources.get("facebook_pages",[])) + len(sources.get("telegram",[])) +
                   len(sources.get("reddit",[])))
    keyboard = [
        [{"text": "Generate ideas now", "callback_data": "ie_generate_all"}],
        [{"text": "Social ideas only", "callback_data": "ie_generate_social"},
         {"text": "Ad ideas only", "callback_data": "ie_generate_ads"}],
        [{"text": "Ideas from a screenshot", "callback_data": "ie_screenshot_ideas"}],
        [{"text": "Critique a screenshot", "callback_data": "ie_screenshot_critique"}],
        [{"text": "Manage sources (" + str(source_count) + " saved)", "callback_data": "ie_manage_sources"}]
    ]
    send(chat_id, "*Cryptonary Idea Engine*\n\nPulls from live sources — competitor ads, trending crypto content, market narratives — and generates specific content and ad ideas with avatar, objective, and why it works.\n\nWhat do you want?", keyboard)

def show_ie_manage_sources(chat_id):
    sources = load_idea_sources()
    msg = "*Manage Sources*\n\n"
    if sources.get("instagram"):
        msg += "Instagram: " + ", ".join("@" + s for s in sources["instagram"]) + "\n"
    if sources.get("twitter"):
        msg += "Twitter: " + ", ".join("@" + s for s in sources["twitter"]) + "\n"
    if sources.get("facebook_pages"):
        msg += "Facebook: " + ", ".join(sources["facebook_pages"]) + "\n"
    if sources.get("telegram"):
        msg += "Telegram: " + ", ".join("t.me/" + s for s in sources["telegram"]) + "\n"
    if sources.get("reddit"):
        msg += "Reddit: " + ", ".join("r/" + s for s in sources["reddit"]) + "\n"
    keyboard = [
        [{"text": "Add Instagram account", "callback_data": "ie_add_instagram"}],
        [{"text": "Add Twitter account", "callback_data": "ie_add_twitter"}],
        [{"text": "Add Facebook page", "callback_data": "ie_add_facebook"}],
        [{"text": "Add Telegram channel", "callback_data": "ie_add_telegram"}],
        [{"text": "Add Reddit community", "callback_data": "ie_add_reddit"}],
        [{"text": "Back", "callback_data": "open_idea_engine"}]
    ]
    send(chat_id, msg, keyboard)

def fetch_source_content(sources):
    """Fetch live content from all saved sources using web search."""
    fetched = []

    # Reddit — most reliable
    for sub in sources.get("reddit", [])[:3]:
        try:
            url = "https://www.reddit.com/r/" + sub + "/hot.json?limit=5"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read())
                posts = data.get("data", {}).get("children", [])
                for p in posts[:3]:
                    post = p.get("data", {})
                    title = post.get("title", "")
                    score = post.get("score", 0)
                    if title:
                        fetched.append({"source": "r/" + sub, "type": "reddit", "content": title, "score": score})
        except Exception as e:
            print("Reddit fetch error " + sub + ":", e, flush=True)

    # Facebook Ad Library — use saved URL directly
    for fb_url in sources.get("facebook_urls", [])[:2]:
        try:
            req = urllib.request.Request(fb_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                html = r.read().decode("utf-8", errors="ignore")[:8000]
                fetched.append({"source": "Cryptonary FB Ads Library", "type": "facebook_ad", "content": html[:2000]})
        except Exception as e:
            print("FB Ad Library fetch error:", e, flush=True)

    # Telegram public channels
    for channel in sources.get("telegram", [])[:3]:
        try:
            url = "https://t.me/s/" + channel
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                html = r.read().decode("utf-8", errors="ignore")
                # Extract message text from HTML
                import re as _re
                msgs = _re.findall(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', html, _re.DOTALL)
                for msg in msgs[:3]:
                    clean = _re.sub(r'<[^>]+>', '', msg).strip()[:200]
                    if clean:
                        fetched.append({"source": "t.me/" + channel, "type": "telegram", "content": clean})
        except Exception as e:
            print("Telegram fetch error " + channel + ":", e, flush=True)

    # Twitter — fetch recent posts via search for each handle
    all_twitter = sources.get("twitter", [])[:6]
    ad_twitter = sources.get("twitter_ads_inspiration", [])
    for handle in all_twitter:
        try:
            search_url = "https://www.google.com/search?q=%40" + handle + "+site:twitter.com+OR+site:x.com&num=3&tbs=qdr:w"
            req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                html = r.read().decode("utf-8", errors="ignore")[:2000]
                fetched.append({"source": "@" + handle + " (X)", "type": "twitter", "content": html[:400]})
        except Exception as e:
            print("Twitter fetch error " + handle + ":", e, flush=True)

    # Ad inspiration accounts - flagged separately
    for handle in ad_twitter:
        try:
            search_url = "https://www.google.com/search?q=%40" + handle + "+site:twitter.com+OR+site:x.com&num=3&tbs=qdr:w"
            req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                html = r.read().decode("utf-8", errors="ignore")[:2000]
                fetched.append({"source": "@" + handle + " (Ad Inspiration)", "type": "twitter_ads", "content": html[:400]})
        except Exception as e:
            print("Ad Twitter fetch error " + handle + ":", e, flush=True)

    # Instagram — split into marketing inspiration vs crypto content
    marketing_handles = {"mange.marketing", "lukedavis.ig", "simplyougrow", "daytrading"}
    ig_handles = sources.get("instagram", [])
    for handle in ig_handles[:8]:
        try:
            search_url = "https://www.google.com/search?q=site:instagram.com%2F" + handle + "&num=3&tbs=qdr:w"
            req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                html = r.read().decode("utf-8", errors="ignore")[:2000]
                ig_type = "instagram_marketing" if handle in marketing_handles else ("instagram_own" if handle == "cryptonary" else "instagram")
                label = "@" + handle + (" (Marketing Inspo)" if handle in marketing_handles else (" (Our IG)" if handle == "cryptonary" else " (IG)"))
                fetched.append({"source": label, "type": ig_type, "content": html[:400]})
        except Exception as e:
            print("Instagram fetch error " + handle + ":", e, flush=True)

    return fetched

def generate_ideas(chat_id, idea_type="both"):
    """Generate ideas from all sources."""
    send(chat_id, "Scanning sources and generating ideas...")
    sources = load_idea_sources()
    ctx = get_content_context(chat_id)

    try:
        # Fetch live content
        fetched = fetch_source_content(sources)

        # Build source summary for Claude
        source_summary = ""
        if fetched:
            source_summary = "LIVE SOURCE DATA:\n"
            # Prioritise news sources and ad inspiration
            news_items = [i for i in fetched if i["type"] in ("twitter", "reddit")]
            ad_items = [i for i in fetched if i["type"] in ("twitter_ads", "facebook_ad", "instagram_marketing")]
            other_items = [i for i in fetched if i["type"] not in ("twitter", "reddit", "twitter_ads", "facebook_ad")]
            for item in (news_items[:6] + ad_items[:3] + other_items[:3]):
                source_summary += "- [" + item["source"] + "] " + item["content"][:150] + "\n"
            if ad_items:
                source_summary += "\nAD INSPIRATION SOURCES (use for ad hook/angle ideas):\n"
                for item in ad_items:
                    source_summary += "- [" + item["source"] + "] " + item["content"][:200] + "\n"
        else:
            source_summary = "Note: Live source fetching returned limited data. Generate ideas based on current crypto market context and trends.\n"

        # Also fetch trending crypto news
        market = fetch_market_data()
        market_line = ""
        if market.get("btc_price"):
            market_line = "Current BTC: ${:,.0f} | Fear & Greed: {} ({})".format(
                market["btc_price"], market.get("fng_value","?"), market.get("fng_label","?"))

        type_instruction = {
            "social": "Generate SOCIAL CONTENT ideas only (Reels, Carousels, Stories).",
            "ads": "Generate AD COPY ideas only (Meta static and video ads).",
            "both": "Generate a mix of SOCIAL CONTENT ideas and AD ideas."
        }.get(idea_type, "Generate a mix of social and ad ideas.")

        prompt = """You are the creative strategist for Cryptonary, a crypto research platform.

MARKET CONTEXT: """ + market_line + """

""" + source_summary + """

""" + ctx + """

""" + type_instruction + """

Generate exactly 8 specific, actionable content ideas. For each idea:

IDEA [N]: [Format] — [Hook/Concept in one punchy line]
AVATAR: [Which of these avatars: Trader / Investor / Passive Income / Portfolio Builder / 100X Chaser / Skeptic / Burned / Student / 9-5 Worker / Boomer / Side Hustle / Beginner / Universal]
OBJECTIVE: [Awareness / Consideration / Conversion] — [what action it drives]
INSPIRED BY: [which source or trend inspired this]
WHY IT WORKS: [one sentence — specific psychological principle or copywriting mechanic]
---

Rules:
- Ideas must be specific to Cryptonary's content — crypto research, market analysis, portfolio strategy, airdrops, passive income
- No generic ideas. Every idea should have a specific angle, hook, or narrative
- Mix formats: include Reels, Carousels, Static ads, and Video ads
- Ideas should reflect current market conditions (Fear & Greed: """ + str(market.get("fng_label","unknown")) + """)
- Draw from what's working in the source data above"""

        result = claude(prompt, max_tokens=2000, system=VOICE_GUIDE)

        # Parse into individual ideas and send with action buttons
        send_plain(chat_id, "*CRYPTONARY IDEA ENGINE*\n\n" + result)

        keyboard = [
            [{"text": "Generate more ideas", "callback_data": "ie_generate_all"}],
            [{"text": "Social ideas only", "callback_data": "ie_generate_social"},
             {"text": "Ad ideas only", "callback_data": "ie_generate_ads"}],
            [{"text": "Develop an idea → Content Studio", "callback_data": "ie_develop"}],
            [{"text": "Develop an idea → Ad Copy", "callback_data": "ie_develop_ad"}],
            [{"text": "Back to Idea Engine", "callback_data": "open_idea_engine"}]
        ]
        send(chat_id, "8 ideas generated. Tap Develop to take any idea straight into the Content Studio.", keyboard)

        # Save ideas to state for development
        user_state[chat_id]["last_ideas"] = result
        user_state[chat_id]["stage"] = "idea_engine_idle"

    except Exception as e:
        print("Idea generation error:", e, flush=True)
        send(chat_id, "Error generating ideas: " + str(e))

# ── IMAGE PROMPT GENERATOR ────────────────────────────────────────

def generate_image_prompts(chat_id, brief):
    """Generate Midjourney, DALL-E, and universal image prompts from a brief."""
    send(chat_id, "Generating image prompts...")
    try:
        prompt = """Generate 3 image prompt variants for this brief: """ + brief + """

You are creating prompts for Cryptonary — a premium crypto research brand. Dark, professional, aspirational aesthetic. The brand uses dark backgrounds, gold/amber accents, clean typography.

OUTPUT FORMAT:

MIDJOURNEY PROMPT:
[Full prompt optimised for Midjourney v6. Include: subject, lighting, mood, style reference, color palette, composition. End with: --ar 4:5 --v 6 --style raw --q 2]

DALL-E PROMPT:
[Plain English scene description optimised for DALL-E 3. Be explicit about style, what to include, what to avoid. No special syntax needed.]

RUNWAY / VIDEO THUMBNAIL:
[Opening frame description for video content. Include: subject position, background, lighting mood, any motion direction, emotional tone.]

DESIGN NOTES:
[2-3 specific notes for the designer: suggested text overlay placement, color hex codes that fit Cryptonary brand, any stock photo search terms as alternatives]

Keep each prompt specific and visual. Avoid abstract descriptions — describe exactly what should be in the frame."""

        result = claude(prompt, max_tokens=800)
        send_plain(chat_id, result)

        keyboard = [
            [{"text": "Generate another variation", "callback_data": "ie_imageprompt_again"}],
            [{"text": "Back to main menu", "callback_data": "start_over"}]
        ]
        user_state[chat_id]["last_image_brief"] = brief
        send(chat_id, "Prompts ready. Copy and paste into Midjourney, DALL-E, or Runway.", keyboard)

    except Exception as e:
        send(chat_id, "Error: " + str(e))

import urllib.parse as _urlparse

# ══════════════════════════════════════════════════════════════════
# CRITIQUE ENGINE
# ══════════════════════════════════════════════════════════════════

CRITIQUE_SYSTEM = """You are a senior copy editor for Cryptonary. Your job is to critique marketing content against Adam's voice rules, copywriting principles, and the full knowledge base.

ADAM'S VOICE NON-NEGOTIABLES:
- Opens with "Gm [Name]," for emails
- Short punchy sentences. No em dashes. Bullets use •
- No weasel words: very, quite, rather, really — delete them
- Bold key phrases with *asterisks*
- P.S. is mandatory on emails
- Sign off: "Talk soon, / Adam"
- Free emails: tease, curiosity gap, CTA to upgrade
- Pro emails: full analysis, exact levels, complete strategy
- No passive voice. Active, direct, confident.

COPYWRITING STANDARDS:
- Headline/subject must promise a benefit or provoke curiosity
- Every line must earn its place — cut anything that doesn't move the reader forward
- Specifics beat generalities — numbers, dates, names, exact levels
- CTA must be clear, single, and tied to a transformation not a feature
- Fear, curiosity, or desire must be present in the opening
- P.S. should contain the sharpest proof point or the most compelling hook

FORMAT YOUR CRITIQUE AS:
1. [Issue title] — [Specific problem identified]
   FIX: [Exact suggested change or replacement copy]

2. [Issue title] — [Specific problem identified]
   FIX: [Exact suggested change or replacement copy]

(continue for each issue found)

Maximum 6 issues. Order by severity — most important first.
Be specific. Don't say "improve the CTA" — say exactly what to change it to.
If the content is strong, say so briefly then give 2-3 refinements anyway."""

def run_critique(chat_id, content_type):
    """Run a critique on the current piece of content."""
    state = user_state[chat_id]
    state["critique_content_type"] = content_type

    # Get the right content from state
    if content_type == "email":
        free_email = state.get("current_emails", {}).get("free", "")
        pro_email = state.get("current_emails", {}).get("pro", "")
        content_to_critique = "FREE EMAIL:\n" + free_email[:800] + "\n\nPRO EMAIL:\n" + pro_email[:800]
        label = "emails"
    elif content_type == "ad":
        content_to_critique = state.get("current_ad_output", "")[:1500]
        label = "ad copy"
    elif content_type == "social":
        content_to_critique = state.get("current_social", "")[:1500]
        social_type = state.get("current_social_type", "social content")
        label = social_type
    elif content_type == "lp":
        content_to_critique = state.get("lp_content", "")[:1500]
        label = "landing page"
    else:
        content_to_critique = ""
        label = "content"

    if not content_to_critique or len(content_to_critique.strip()) < 50:
        send(chat_id, "Nothing to critique yet — generate content first.")
        return

    send(chat_id, "Critiquing your " + label + "...")

    try:
        result = claude(
            "Critique this " + label + ":\n\n" + content_to_critique,
            max_tokens=1200,
            system=CRITIQUE_SYSTEM
        )

        # Store critique and content for applying fixes
        state["current_critique"] = result
        state["critique_original"] = content_to_critique
        state["stage"] = "awaiting_critique_apply"

        send_plain(chat_id, "CRITIQUE\n\n" + result)

        # Build apply buttons for each numbered fix (up to 6)
        import re as _re
        nums = _re.findall(r'^\d+\.', result, _re.MULTILINE)
        keyboard = []
        row = []
        for i, _ in enumerate(nums[:6]):
            row.append({"text": "Apply " + str(i+1), "callback_data": "apply_critique_" + str(i+1)})
            if len(row) == 3:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
        keyboard.append([{"text": "Ignore all", "callback_data": "ignore_critique"}])

        send(chat_id, "Type a number to apply a fix, or tap a button:", keyboard)

    except Exception as e:
        send(chat_id, "Critique error: " + str(e))
        print("Critique error:", e, flush=True)

def apply_critique_fix(chat_id, fix_number):
    """Apply a specific critique fix to the content."""
    state = user_state[chat_id]
    critique = state.get("current_critique", "")
    original = state.get("critique_original", "")
    content_type = state.get("critique_content_type", "email")

    if not critique or not original:
        send(chat_id, "No active critique to apply.")
        return

    send(chat_id, "Applying fix " + str(fix_number) + "...")

    try:
        result = claude(
            "ORIGINAL CONTENT:\n" + original[:1500] +
            "\n\nCRITIQUE:\n" + critique[:1000] +
            "\n\nApply ONLY fix number " + str(fix_number) + " from the critique above. " +
            "Return the full revised content with that specific change applied. " +
            "Do not apply any other changes. Do not explain what you changed.",
            max_tokens=1500
        )

        # Update state with revised content
        if content_type == "email":
            # Re-parse and update
            emails = {"free": result[:len(result)//2], "pro": result[len(result)//2:]}
            state["current_emails"] = emails
        elif content_type == "ad":
            state["current_ad_output"] = result
        elif content_type == "social":
            state["current_social"] = result

        send_plain(chat_id, "Fix " + str(fix_number) + " applied:\n\n" + result)

        # Save as voice example since this is a refined, improved version
        save_voice_example(chat_id, result[:600], "critique_fix_" + content_type)

        # Show action keyboard
        kb_map = {"email": email_action_keyboard, "ad": ad_action_keyboard, "social": social_action_keyboard}
        kb_fn = kb_map.get(content_type, email_action_keyboard)

        # Offer to apply more fixes
        keyboard = kb_fn()
        keyboard.insert(0, [{"text": "Apply another fix", "callback_data": "critique_" + content_type}])
        state["stage"] = "awaiting_critique_apply"
        send(chat_id, "Fix applied. Apply another or proceed:", keyboard)

    except Exception as e:
        send(chat_id, "Error applying fix: " + str(e))
        print("Apply fix error:", e, flush=True)

# ══════════════════════════════════════════════════════════════════
# CONTENT STUDIO FILE HANDLER
# ══════════════════════════════════════════════════════════════════

def handle_content_file(chat_id, file_info, file_type="image"):
    """Handle file uploads in Content Studio flows (PDF, image, doc)."""
    state = user_state.get(chat_id, {})
    stage = state.get("stage", "idle")

    try:
        # Download the file
        file_id = file_info.get("file_id")
        path_data = tg("getFile", {"file_id": file_id})
        file_path = path_data.get("result", {}).get("file_path", "")
        if not file_path:
            send(chat_id, "Could not download file.")
            return

        url = "https://api.telegram.org/file/bot" + TELEGRAM_TOKEN + "/" + file_path
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as r:
            file_bytes = r.read()

        import base64
        send(chat_id, "Reading your file...")

        if file_type == "image":
            # Use Claude Vision to extract content
            mime = "image/jpeg"
            if file_path.endswith(".png"): mime = "image/png"
            elif file_path.endswith(".webp"): mime = "image/webp"
            encoded = base64.b64encode(file_bytes).decode()

            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 2000,
                "messages": [{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": mime, "data": encoded}},
                    {"type": "text", "text": "Extract all the text and data from this image. This is likely a research report, market analysis, or data table. Return everything you can read as plain text, preserving structure. Include all numbers, dates, percentages, and key points."}
                ]}]
            }).encode()

            req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
                headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
            with urllib.request.urlopen(req, timeout=60) as r:
                extracted = json.loads(r.read())["content"][0]["text"]

        elif file_type == "pdf":
            # Send PDF directly to Claude API as document
            encoded = base64.b64encode(file_bytes).decode()
            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 3000,
                "messages": [{"role": "user", "content": [
                    {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": encoded}},
                    {"type": "text", "text": "Extract all the content from this document. This is likely a research report, market analysis, newsletter, or data report. Return the full content as plain text preserving all key information, numbers, analysis, and structure."}
                ]}]
            }).encode()
            req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
                headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
            with urllib.request.urlopen(req, timeout=60) as r:
                extracted = json.loads(r.read())["content"][0]["text"]

        else:
            # Plain text / CSV / doc — decode directly
            try:
                extracted = file_bytes.decode("utf-8")[:8000]
            except:
                extracted = file_bytes.decode("latin-1")[:8000]

        if not extracted or len(extracted.strip()) < 20:
            send(chat_id, "Could not extract content from this file. Try pasting the text directly.")
            return

        # Show preview and proceed
        preview = extracted[:300] + ("..." if len(extracted) > 300 else "")
        send(chat_id, "Got it. Extracted " + str(len(extracted)) + " characters:\n\n_" + preview + "_")

        # Route based on current stage — same as if text was pasted
        if stage in ("awaiting_report", "buffering_report"):
            user_state[chat_id]["report"] = sanitise(extracted)
            user_state[chat_id]["stage"] = "awaiting_context_choice"
            keyboard = [
                [{"text": "Yes — I have extra context", "callback_data": "context_yes"}],
                [{"text": "No — just the report", "callback_data": "context_no"}]
            ]
            send(chat_id, "Any extra context to factor in?\n\n_Promos, discounts, Inner Circle open, upcoming events, factoids, PSAs..._", keyboard)

        elif stage == "awaiting_social_report":
            user_state[chat_id]["report"] = sanitise(extracted)
            user_state[chat_id]["context"] = ""
            gen_social_angles(chat_id)

        elif stage == "awaiting_ad_theme":
            user_state[chat_id]["ad_theme"] = sanitise(extracted[:500])
            user_state[chat_id]["stage"] = "pick_ad_avatars"
            show_avatar_menu(chat_id)

        elif stage == "awaiting_lp_context_text":
            user_state[chat_id]["lp_context"] = sanitise(extracted[:500])
            generate_landing_page(chat_id)

        else:
            send(chat_id, "File received but not sure where to use it. Try again from the right step.")

    except Exception as e:
        print("Content file handler error:", e, flush=True)
        send(chat_id, "Error reading file: " + str(e))

# ══════════════════════════════════════════════════════════════════
# IDEA ENGINE — SCREENSHOT ANALYSIS
# ══════════════════════════════════════════════════════════════════

def handle_ie_screenshot(chat_id, file_info, stage):
    """Handle screenshot uploads for Idea Engine — ideas or critique."""
    try:
        import base64
        file_id = file_info.get("file_id")
        path_data = tg("getFile", {"file_id": file_id})
        file_path = path_data.get("result", {}).get("file_path", "")
        if not file_path:
            send(chat_id, "Could not download the image.")
            return

        url = "https://api.telegram.org/file/bot" + TELEGRAM_TOKEN + "/" + file_path
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as r:
            file_bytes = r.read()

        mime = "image/jpeg"
        if file_path.endswith(".png"): mime = "image/png"
        elif file_path.endswith(".webp"): mime = "image/webp"
        encoded = base64.b64encode(file_bytes).decode()

        user_state[chat_id]["stage"] = "idea_engine_idle"

        if stage == "ie_awaiting_screenshot_ideas":
            send(chat_id, "Analysing and generating ideas...")
            prompt_text = """Look at this image carefully. It could be an Instagram post, a Facebook ad, a carousel, a reel thumbnail, or any piece of marketing content.

STEP 1 — READ THE CONTENT:
What format is it? What is the hook or opening line? What topic? What's the visual approach? Who is the target audience?

STEP 2 — IDENTIFY WHAT'S WORKING:
What copywriting or creative principles are at play? Why would this stop a scroll or drive engagement?

STEP 3 — GENERATE 6 CONTENT IDEAS INSPIRED BY THIS:
Use this as creative inspiration for Cryptonary content. Each idea should be in a different format or take a different angle — don't just replicate it.

For each idea:
IDEA [N]: [Format] — [Hook/Concept]
AVATAR: [which of Cryptonary's 13 avatars: Trader/Investor/Passive Income/Portfolio Builder/100X Chaser/Skeptic/Burned/Student/9-5 Worker/Boomer/Side Hustle/Beginner/Universal]
OBJECTIVE: [Awareness/Consideration/Conversion]
INSPIRED BY: [what specifically in the screenshot sparked this]
WHY IT WORKS: [one sentence — specific principle or mechanic]
---"""

            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1500,
                "system": VOICE_GUIDE,
                "messages": [{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": mime, "data": encoded}},
                    {"type": "text", "text": prompt_text}
                ]}]
            }).encode()

            req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
                headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
            with urllib.request.urlopen(req, timeout=60) as r:
                result = json.loads(r.read())["content"][0]["text"]

            user_state[chat_id]["last_ideas"] = result
            send_plain(chat_id, "*IDEAS FROM SCREENSHOT*\n\n" + result)
            keyboard = [
                [{"text": "Develop into social content", "callback_data": "ie_develop"}],
                [{"text": "Develop into ad", "callback_data": "ie_develop_ad"}],
                [{"text": "Generate more ideas", "callback_data": "ie_generate_all"}],
                [{"text": "Back to Idea Engine", "callback_data": "open_idea_engine"}]
            ]
            send(chat_id, "6 ideas generated from your screenshot.", keyboard)

        elif stage == "ie_awaiting_screenshot_critique":
            send(chat_id, "Critiquing...")
            prompt_text = """Critique this piece of content against professional copywriting and marketing standards.

This could be a Cryptonary post, a competitor's content, or any marketing material.

Apply these standards:
- Hook strength (does it stop the scroll in 3 seconds?)
- Clarity (is the message instantly understood?)
- Copy quality (voice, specificity, no weasel words, active not passive)
- Avatar targeting (is it speaking to one specific person or everyone and no one?)
- CTA effectiveness (is there a clear next action?)
- Visual/text balance (if visible)
- Copywriting principles from Ogilvy, Cashvertising, Cialdini, Hormozi, Made to Stick

FORMAT:
WHAT'S WORKING:
[1-2 things that are genuinely strong]

ISSUES:
1. [Issue title] — [Specific problem]
   FIX: [Exact suggested improvement]

2. [Issue title] — [Specific problem]
   FIX: [Exact suggested improvement]

(up to 6 issues, ordered by severity)

OVERALL RATING: [A/B/C/D] — [one sentence verdict]"""

            payload = json.dumps({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1200,
                "system": CRITIQUE_SYSTEM,
                "messages": [{"role": "user", "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": mime, "data": encoded}},
                    {"type": "text", "text": prompt_text}
                ]}]
            }).encode()

            req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
                headers={"Content-Type": "application/json", "x-api-key": ANTHROPIC_KEY, "anthropic-version": "2023-06-01"})
            with urllib.request.urlopen(req, timeout=60) as r:
                result = json.loads(r.read())["content"][0]["text"]

            send_plain(chat_id, "SCREENSHOT CRITIQUE\n\n" + result)
            keyboard = [
                [{"text": "Ideas from this screenshot", "callback_data": "ie_screenshot_ideas"}],
                [{"text": "Back to Idea Engine", "callback_data": "open_idea_engine"}]
            ]
            send(chat_id, "Critique complete.", keyboard)

    except Exception as e:
        print("IE screenshot error:", e, flush=True)
        send(chat_id, "Error analysing screenshot: " + str(e))
        user_state[chat_id]["stage"] = "idea_engine_idle"

if __name__ == "__main__":
    if ANTHROPIC_KEY == "YOUR_ANTHROPIC_KEY_HERE":
        print("ERROR: Set ANTHROPIC_KEY environment variable.", flush=True)
    else:
        poll()
