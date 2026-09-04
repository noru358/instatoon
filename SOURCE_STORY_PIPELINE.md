# SOURCE_STORY_PIPELINE.md

# Canonical content pipeline — v2.0
Updated: 2026-09-04

## 1. Channel definition

This project produces short omnibus anecdote/scenario comics and vertical short-form adaptations.

FORMAT = omnibus.
SOURCE SUPPLY = internet/community/SNS anecdotes, comments, everyday incidents, submitted stories, observed situations, plus limited original invention when needed.

Main characters may recur, but every episode may introduce one-off people appropriate to the story.

The system should not force every story into the Gaeun/Harin/Taemin trio.

## 2. Layered agent pipeline

Run stages in order and expose intermediate output for QC.

### Layer 1 — Source discovery / collection
Collect candidate anecdotes, incidents, conflicts, awkward moments, funny comments, and relatable situations.
Keep provenance when applicable.
Do not copy long source text into final output.

### Layer 2 — Selection / Human-interest Gate
Score:
- instant comprehensibility;
- emotional/social tension;
- visualizability;
- short-form compression potential;
- relatability or novelty;
- payoff / memorable beat.

Kill weak material early.

### Layer 3 — Source normalization
Separate:
A. SOURCE FACTS — what actually happens.
B. SOURCE VOICE — useful human wording, slang, fragments, reactions, rhythm, comments.

Example:
SOURCE FACTS:
- blind-date man borrows phone;
- opens Instagram;
- searches himself;
- follows himself from her account.

SOURCE VOICE:
- "폰 잠깐 빌려달라는 거임"
- "전화하나 했는데"
- "갑자기 인스타를 켜더라"
- "내 계정으로 지 팔로우함ㅋㅋ"
- "진심 뭐지 싶었음"

### Layer 4 — Story room
Build story beats without polishing dialogue.
Typical short anecdote grammar:
HOOK → SETUP → ODD SIGNAL → REVEAL/PAYOFF → AFTERMATH.
Do not invent a clever punchline if the situation already carries the joke.

### Layer 5 — Dialogue draft
Convert beats into speakable/readable lines.
Priority:
human source wording > lightly edited source wording > AI-invented wording.

Use different registers for:
- narrator/caption;
- spoken dialogue;
- comments/replies;
- internal reaction.

### Layer 6 — DIALOGUE HUMANIZATION AGENT
Remove AI-writing smell.

Avoid:
- overly complete sentences;
- neat emotional summaries;
- literary closure;
- artificial morals;
- symmetrical setup/payoff wording;
- generic reaction lines;
- clever wordplay added only to manufacture a punchline;
- every character speaking in the same polished grammar;
- explaining what the image already shows.

Preserve useful:
- fragments;
- slang;
- omitted subjects;
- hesitations;
- repetition;
- abrupt endings;
- casual internet rhythm;
- intentionally plain endings.

A scene may end without a joke line.

### Layer 7 — USER VOICE GATE
Mandatory during current manual/prototype phase.
Present humanized dialogue before final visual production whenever practical.
User may give terse edits such as:
- "2번 AI 같음"
- "더 툭툭"
- "마지막 펀치 삭제"
- "남자 말은 괜찮음"

Do not require a long rationale.

### Layer 8 — VOICE LEDGER
Convert useful recurring user edits into general rules.

Store pattern:
BAD:
WHY:
PREFERRED:
RULE LEARNED:

Do not overfit one isolated edit.
Promote a preference into a durable rule only when clearly intentional/repeated or explicitly approved.

### Layer 9 — Storyboard / visual plan
Only after story/dialogue approval.
Choose:
- slide count based on story, not a fixed 4-cut ideology;
- 4:5 carousel composition;
- 9:16 short-form adaptation if useful;
- characters required;
- one-off vs recurring identity;
- location per beat;
- props and reaction;
- shot distance.

### Layer 10 — Image / video production
Apply MASTER_PROMPTS.md and STYLE_LOCK.md.
Story chooses backgrounds.
No fixed-set requirement.

### Layer 11 — QC
Check:
- story clarity;
- human dialogue;
- style lock;
- identity continuity;
- spatial/anatomy defects;
- unnecessary detail;
- text/layout safety.

### Layer 12 — Performance feedback
Performance may influence topic/format experiments.
It may not silently average the voice, mutate the style, or force every episode into one winning template.

## 3. Current pilot

Approved pilot concept:
Blind-date phone self-follow anecdote.

Casting:
- female lead: Harin (recurring main character);
- male lead: episode-only one-off character.

Approved direction:
- 7-beat carousel is acceptable;
- 4:5 is primary;
- 9:16 derivative may follow;
- dialogue should remain casual and unpolished rather than AI-clever.

First-pass art has been generated and is awaiting visual/story/dialogue QC before publish status.
