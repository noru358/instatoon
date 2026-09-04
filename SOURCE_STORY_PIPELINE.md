# SOURCE_STORY_PIPELINE.md

# CANONICAL CONTENT / DIALOGUE / CAST PIPELINE v2.1
Updated: 2026-09-04

This file replaces the overlapping story-system material previously split across multiple root documents.

## 0. Channel definition

FORMAT = omnibus.
SOURCE SUPPLY = internet/community/SNS anecdotes, comments, everyday incidents, user stories, observed situations, plus limited original invention when appropriate.

The project does NOT require one fixed cast or one fixed location.

Main characters are reusable assets:
- Gaeun
- Harin
- Taemin

But every episode decides cast from its own story/context.
Do not use a main character merely because the script needs a person of the same gender.
Episode-specific characters are normal.

## 1. Layered working order

Run the following layers in order.
Expose intermediate outputs for QC when the user is actively reviewing the production process.

### L1 — SOURCE DISCOVERY / COLLECTION

Collect candidate:
- anecdotes;
- incidents;
- awkward moments;
- social conflicts;
- funny comments;
- relatable routines;
- odd behavior;
- real-life observations;
- user-submitted premises.

Preserve provenance when applicable.

### L2 — HUMAN-INTEREST GATE

A candidate must have:
- sceneability;
- a real state change;
- enough specificity;
- a recognizable emotion;
- recognition/novelty;
- landing potential.

Hard-kill if:
- mostly explanation/no scenes;
- the “funny part” must be invented;
- long context is required before anything happens;
- all beats are generic;
- the ending only works after adding a neat moral;
- visualization would be mostly people standing and explaining.

### L3 — SOURCE NORMALIZATION

Separate:

SOURCE FACTS
- what actually happens;
- chronology;
- concrete objects/actions;
- uncertainty;
- what must not be invented.

SOURCE VOICE
- useful human wording;
- fragments;
- slang;
- odd phrasing;
- comments/replies;
- emotional rhythm.

Priority for later dialogue:
human source wording > lightly edited source wording > AI-invented wording.

Do not polish away the weird human details.

### L4 — FORMAT / STORY-SHAPE ROUTER

Active formats:

#### STORY_ARC
Main question: “그래서 무슨 일이 있었는데?”

Useful shapes:
- INCIDENT_ESCALATION
- MISUNDERSTANDING_REVEAL
- ERROR_SPIRAL
- EXPECTATION_REVERSAL
- ACCUMULATION_BREAK

Default 5–8-beat grammar:
HOOK → SETUP/BASELINE → TRIGGER → RESPONSE → ESCALATION → TURN/REVEAL → LANDING

Every body beat must change state.

#### RELATABLE_SCENARIO
Main reaction: “아 나도 이럼.”

Useful shapes:
- MICRO_SKIT
- INNER_OUTER_GAP
- RITUAL
- TINY_ANNOYANCE
- SOCIAL_CODE

The premise must be behavioral and specific, not merely categorical.

Bad:
“직장인은 월요일이 싫다.”

Better:
show the exact repeated behavior, object, sentence, timing, or social cue that makes it recognizable.

### L5 — STORY ROOM

Write story beats BEFORE polished dialogue.

Required:
- one-sentence premise;
- emotional engine;
- specific details to preserve;
- landing type;
- ordered beats;
- state delta after each beat;
- reader question after each non-final beat.

Useful landing types:
- PUNCH;
- AFTERSHOCK;
- HUMAN_RESIDUE;
- CALLBACK;
- DEADPAN;
- OPEN_RECOGNITION.

Do not force a clever closing line when the situation already carries the joke.

### L6 — DIALOGUE DRAFT

Write separately by register:

NARRATION / CAPTION
- concise;
- may use internet-storytelling rhythm;
- can omit subjects and use fragments when natural.

SPOKEN DIALOGUE
- what that person would actually say in the moment;
- role/age/context specific;
- not a narration disguised as dialogue.

REACTION / INNER THOUGHT
- short;
- often attached visually to expression;
- may be silence, “…”, “??”, etc.

COMMENTS / REPLIES
- preserve human internet cadence when source-derived.

### L7 — DIALOGUE HUMANIZATION

Repair AI-writing smell.

Reject/repair:
- overly complete sentences;
- neat emotional summaries;
- literary closure;
- artificial moral;
- clever wordplay added only to manufacture a punchline;
- symmetrical setup/payoff wording;
- generic reaction lines;
- every character speaking in the same polished grammar;
- captions explaining what the image already shows;
- excessive fake “ㅋㅋ” used merely to simulate humanity.

Preserve when useful:
- fragments;
- omissions;
- slang;
- hesitations;
- repetition;
- abrupt endings;
- mundane wording;
- intentionally plain landing.

Human texture > verbal smoothness.

### L8 — USER VOICE GATE

During the current learning phase, this is a deliberate manual gate.

The user may give terse feedback:
- “2번 AI 같음”
- “더 툭툭”
- “마지막 펀치 삭제”
- “남자 말은 괜찮음”

Do not require an essay-length explanation.

### L9 — VOICE LEDGER

Convert recurring user corrections into general rules.

Store internally or episode-locally as:

BAD:
WHY:
PREFERRED:
RULE LEARNED:

Do not overfit one isolated edit.
Promote only explicit/repeated preferences.

### L10 — STORYBOARD + CAST ROUTER

Only after story/dialogue is acceptable:

For every beat decide:
- which character(s) are actually needed;
- main-cast vs episode-only;
- location;
- key prop;
- expression/reaction;
- camera distance;
- text role;
- output composition.

CAST PRINCIPLE:
Story/context decides.

Examples:
- Harin may lead a dating anecdote if it naturally fits.
- Taemin may appear in another episode if the story calls for him.
- A blind-date man is not automatically Taemin.
- A coworker, parent, stranger, boss, clerk, student, etc. may be episode-only.

### L11 — EPISODE-LOCAL CHARACTER ANCHOR

Mandatory when a newly introduced non-main character appears in 2+ cuts.

Before production frames:
1. create an internal anchor image or compact character sheet;
2. make age, face, hair, clothing, and role fit the story;
3. ensure the design is visually distinct from main cast;
4. reject generic smooth AI-face design;
5. accept one last-known-good anchor;
6. use it consistently across all subsequent frames.

This step is internal by default.
The user does not need to manually approve every anchor unless identity itself becomes a taste decision.

One-frame background extras may skip it.

### L12 — WHOLE-EPISODE VISUAL PLAN

Do not render slide 1 and invent slide 2 afterward.

Plan:
- slide count from actual story density;
- ordered beat role;
- page archetype;
- camera rhythm;
- text role;
- art-safe text area;
- render mode;
- continuity mode.

No fixed 4-cut ideology.
A 5, 6, 7, or 8-slide story is acceptable if every slide earns its place.

### L13 — TEXT-FREE ART GENERATION

Production art should normally contain:
- characters;
- props;
- environment;
- non-text reaction marks when useful.

It should normally NOT contain final readable:
- narration;
- dialogue;
- speech bubbles;
- labels;
- source notes.

This prevents typo risk and poster-like composition drift.

### L14 — VECTOR LETTERING / COMPOSITION

Add:
- title/hook;
- narration;
- dialogue bubbles;
- reaction text;
- SFX;
- source note

as editable layout elements.

See VISUAL_GRAMMAR.md for typography and placement rules.

### L15 — QC

QC order:
1. story causality/order;
2. dialogue naturalness;
3. correct cast choice;
4. new-character-anchor continuity;
5. visual style;
6. character identity;
7. scene/blocking/object logic;
8. text hierarchy/readability;
9. output ratio.

A beautiful frame with wrong story order fails.
A stylish frame with the wrong character fails.

### L16 — PERFORMANCE FEEDBACK

Performance may suggest:
- topic experiments;
- different hook forms;
- shorter/longer episode;
- different landing type;
- different distribution track.

It may NOT silently:
- average the voice into generic prose;
- force every episode into one winning template;
- mutate the visual style;
- force main characters into every story.

## 2. Anti-AI story rules

Default repair signals:
- every sentence is polished;
- every slide has explanatory narration;
- the ending summarizes the theme;
- “결국 / 어쩌면 / 우리 모두 / 소소하지만” style generic wisdom appears without need;
- writer invents a stronger humiliation/conflict/punchline than source warrants;
- source-specific odd detail disappears.

For sourced incidents:
allowed AI addition = connective wording / neutral staging.
not allowed = new conflict, accusation, humiliation, or materially stronger ending presented as fact.

## 3. State-delta test

For each slide after the first, answer:

“What changed from the previous slide?”

Valid:
- new action;
- new fact;
- new interpretation;
- new emotional level;
- new consequence;
- new social relation.

Invalid:
“same thing, different pose.”

Merge or delete invalid beats.

## 4. Swipe-question test

For each non-final slide, record the natural reader question.

Examples:
- “그래서 뭐라고 했는데?”
- “왜 저러지?”
- “설마?”
- “결국 어떻게 됐지?”

Do not manufacture fake cliffhangers.

## 5. Visual-story rule

SHOW when:
- action is obvious visually;
- object/reaction is the joke;
- spatial relation matters;
- facial timing matters.

NARRATE when:
- time jumps;
- one small context fact is needed;
- showing would add little.

Do not use a large caption to explain a scene the image already communicates.

## 6. Current pilot note

Active current pilot is E002.
See episodes/E002/README.md.

The current blind-date episode uses:
- Harin as the female lead;
- an episode-only blind-date man;
- no global rule banning Taemin from other episodes.
