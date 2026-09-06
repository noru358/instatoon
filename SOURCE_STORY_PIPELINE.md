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
- L11 EPISODE-LOCAL IDENTITY / ASSET NEEDS → Character & Asset Planner
- L12 WHOLE-EPISODE VISUAL PLAN → Visual Director
- L12.5 ASSET RESOLUTION GATE → Asset Resolver
- L13 ASSET AUTHORING + QC → Asset Author / QC Reviewer
- L13.5 DETERMINISTIC ART COMPOSITION → Composition Runtime
- L14 EDITABLE LETTERING / UI → Lettering & Layout Designer
- L15 QC → QC Reviewer
- L16 PERFORMANCE FEEDBACK → Performance Analyst

After each meaningful stage completes, report:
STAGE / WORKER ROLE / EXECUTION ACTOR / INPUT / SOURCE-PROVENANCE / OUTPUT / STATUS / QC / NEXT.

Stage reporting is audit visibility, **not an approval gate**. User gates are attached to material content/taste decisions and to newly authored production assets, not to every slide.

For stochastic asset authoring, SOURCE-PROVENANCE must name the exact reference assets/media actually supplied. Deterministic composition must name the approved production asset IDs it consumes.

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

During the current learning phase, this is a mandatory pre-production human gate.

Before storyboard/cast planning or any production-asset authoring, present the user with the accepted L1-L7 package in a compact reviewable form:
- source/provenance;
- why the source passed the human-interest gate;
- normalized premise and important human details;
- story shape / ordered beats;
- dialogue and reaction text after humanization;
- any material adaptation/invention notes.

Then STOP and wait for explicit user approval.

Hard rule:
- do not continue to L10 STORYBOARD + CAST ROUTER, L11 identity/asset needs, L12 visual planning, L12.5 asset resolution, or L13 asset authoring until the user explicitly passes the package;
- terse approval such as “통과”, “ㄱ”, “좋음”, or equivalent is sufficient;
- terse rejection/edit feedback is sufficient and must route back to the relevant L3-L7 stage;
- never treat silence, prior general approval, or “make a new episode” as approval of the current episode package.

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

Only after story/dialogue is acceptable.

For every beat decide:
- which character(s) are actually needed;
- main-cast vs episode-only;
- location / background need;
- key prop or UI information;
- expression / body action;
- shot scale / framing role;
- text role;
- primary visual-information owner.

Story/context decides cast. Do not insert recurring leads merely to fill a composition.

### L11 — EPISODE-LOCAL IDENTITY / ASSET NEEDS

If a non-main character appears repeatedly:
1. derive a compact identity contract from story/social role;
2. keep the person distinct from recurring leads;
3. resolve whether approved reusable assets already cover the needed views/poses;
4. open ASSET_GAP only for missing visual capability.

This stage does not require a standalone character sheet by default.

### L12 — WHOLE-EPISODE VISUAL PLAN

Plan the entire sequence before final composition.

Decide:
- slide count from actual story density;
- ordered beat role;
- shot scale / focal owner / visual delta;
- pose/expression/background/prop requirements;
- text-safe regions;
- which requirements are already covered by approved assets.

Production slide count is story-driven. The separate renderer calibration fixture is four slides; that test number is not a content rule.

### L12.5 — ASSET RESOLUTION GATE

Before any stochastic visual call:
1. inspect `assets/production/registry.json`;
2. map each visible requirement to an approved asset where semantically valid;
3. use crop/scale/position/layering when existing assets can express the beat;
4. create explicit ASSET_GAP entries only for missing pose/expression/background/prop/interaction capability;
5. define each gap's category and scope.

Do not use free-form “generate slide N” as the default production action.

### L13 — ASSET AUTHORING + QC

For each ASSET_GAP:
- use current authoring references and MASTER_PROMPTS;
- generate/import the smallest missing asset;
- run GENERATION_PROTOCOL QC;
- user/authorized PASS binds to exact bytes;
- register approved hash/dimensions/scope in `assets/production/registry.json`.

Rejected output is not a reference or production asset.

A full-frame stochastic output is allowed only as an explicit EXCEPTION_OUTPUT under ASSET_COMPOSITION_PROTOCOL.

### L13.5 — DETERMINISTIC ART COMPOSITION

Use the shared AutoPipeline compositor to assemble each text-free art frame from approved asset IDs + transforms.

Requirements:
- one slide = one image file;
- no baked narration/dialogue;
- frame count/order must match the approved storyboard;
- composition variation comes from asset selection, crop, scale, x/y, layering and justified new pose assets;
- do not regenerate accepted identity just to change framing.

For the architecture pilot only, compose exactly four slides. Normal episodes remain variable-length.

### L14 — EDITABLE LETTERING / UI

Add title/hook, narration, dialogue bubbles, reaction text, SFX and meaning-bearing UI as editable deterministic layers.

The old AUTO_FINISH/LETTERING_PLAN implementation is retired. The new implementation must consume the current composed scene/art contract rather than revive the old per-render episode state machine.

### L15 — QC

Run:
1. hard output/asset identity checks;
2. style/identity coherence;
3. anatomy/geometry where relevant;
4. sequence-level framing redundancy and semantic-intent review;
5. text/UI legibility and occlusion review.

Repair the smallest invalid asset/scene/text layer.
Do not restart or regenerate unrelated accepted work.

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

## 6. Current execution pointers

CURRENT_STATE.md identifies whether production is in calibration or an active episode.
ASSET_COMPOSITION_PROTOCOL.md owns final-render routing.
GENERATION_PROTOCOL.md owns stochastic asset/exception authoring and QC.
AutoPipeline owns shared dispatch, asset evidence and deterministic composition.
Git history does not route current production.
