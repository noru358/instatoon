# SOURCE_STORY_PIPELINE.md

# CANONICAL CONTENT / DIALOGUE / CAST PIPELINE v2.2
Updated: 2026-09-05

This file replaces the overlapping story-system material previously split across multiple root documents.

## 0. Channel definition

FORMAT = omnibus.
SOURCE SUPPLY = internet/community/SNS anecdotes, comments, everyday incidents, user stories, observed situations, plus limited original invention when appropriate.

DEFAULT EDITORIAL PRINCIPLE = HUMAN-SOURCE-FIRST.
Even when the final episode is substantially recomposed or partly invented, prefer to begin from one or more real human-produced anecdotes, comments, reactions, behavioral details, or observed incidents. The human material is seed material for specificity, cadence, awkwardness, and social texture; it does not need to be copied literally or treated as a verified factual source for the final reconstructed episode.

Pure AI-originated premises are allowed only when:
- the user explicitly asks for original invention; or
- human-source discovery produces no usable seed after a reasonable search; or
- the concept is intentionally experimental.

When a human source is used as inspiration rather than literal adaptation, record it as BASE / INSPIRATION provenance and distinguish it from SOURCE FACTS that the final episode claims to reproduce.

The project does NOT require one fixed cast or one fixed location.

Main characters are reusable assets:
- Gaeun
- Harin
- Taemin

But every episode decides cast from its own story/context.
Do not use a main character merely because the script needs a person of the same gender.
Episode-specific characters are normal.

## 0.5 New-work routing

User commands such as "새 만화 만들어", "새 작품", "하나 만들어", or equivalent default to NEW_EPISODE.

NEW_EPISODE means:
1. start again at L1 SOURCE DISCOVERY / COLLECTION;
2. seek fresh human-produced seed material by default;
3. do not silently reuse the currently active episode premise;
4. create a new episode ID/package once the source/premise passes the editorial gate.

Continue an existing episode only when the user explicitly refers to that episode, says to continue/repair/retry it, or otherwise clearly anchors the request to existing work.

## 1. Layered working order

Run the following layers in order.
Expose intermediate outputs for QC when the user is actively reviewing the production process.

### Worker-role map and reporting

Current manual/chat execution may use one ChatGPT orchestrator operating through bounded roles; these role labels do not imply separate live agents unless the runtime actually instantiates them.

Default worker roles:
- L1 SOURCE DISCOVERY / COLLECTION → Source Researcher
- L2 HUMAN-INTEREST GATE → Editorial Screener
- L3 SOURCE NORMALIZATION → Source Editor
- L4 FORMAT / STORY-SHAPE ROUTER → Story Architect
- L5 STORY ROOM → Story Writer
- L6 DIALOGUE DRAFT → Dialogue Writer
- L7 DIALOGUE HUMANIZATION → Dialogue Editor
- L8 USER VOICE GATE → User / Human Editor
- L9 VOICE LEDGER → Voice Editor
- L10 STORYBOARD + CAST ROUTER → Storyboard & Cast Director
- L11 EPISODE-LOCAL CHARACTER DESIGN → Character Designer
- L12 WHOLE-EPISODE VISUAL PLAN → Visual Director
- L13 TEXT-FREE ART GENERATION → Raster Renderer
- L14 VECTOR LETTERING / COMPOSITION → Lettering & Layout Designer
- L15 QC → QC Reviewer
- L16 PERFORMANCE FEEDBACK → Performance Analyst

After each meaningful stage completes, report:
STAGE / WORKER ROLE / EXECUTION ACTOR / INPUT / SOURCE-PROVENANCE / OUTPUT / STATUS / QC / NEXT.

For visual generation, SOURCE-PROVENANCE must additionally name the exact style and character reference assets actually supplied to the renderer.

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

Collection priority:
1. direct human anecdotes/posts;
2. comment/reply threads with vivid human wording;
3. multiple similar human incidents that can be recomposed into one stronger premise;
4. observed/user-submitted incidents;
5. pure original invention only as a fallback or explicit creative choice.

Do not confuse "human-seeded" with "literal adaptation." The story room may restructure, merge, fictionalize, or invent connective tissue while retaining the specific human texture that made the source worth collecting.

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

### L11 — EPISODE-LOCAL CHARACTER DESIGN

Mandatory when a newly introduced non-main character appears in 2+ cuts.

Before assembling the production batch:
1. infer the character internally from the story, social role, and scene context;
2. make age, face, hair, clothing, and role fit the story;
3. ensure the design is visually distinct from main cast;
4. reject generic smooth AI-face design;
5. record one compact identity digest;
6. reuse that digest consistently across every frame in the episode batch.

This step is internal by default and does not produce a separate user-facing character sheet or approval gate.
Create a temporary internal anchor image only when direct batch continuity fails. Ask for user approval only when identity itself becomes a material taste decision.

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
4. episode-only character identity continuity;
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
