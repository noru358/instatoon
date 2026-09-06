# E007 — 결국 또 거기

Status: STORYBOARD APPROVED — MANUAL VALIDATION / STRUCTURED CONTRACT NEXT
Updated: 2026-09-06

## 1. Selected topic and provenance

Selected topic:
- office lunch decision fatigue;
- coworkers spend too long discussing what to eat;
- everyone says they are flexible, then rejects actual suggestions;
- after the debate, the group ends up at the familiar place they always visit.

Core comic engine:
**lengthy choice process → fake openness → rejection cascade → familiar default wins.**

Primary human-source seed:
- Reddit r/SideProject
- thread: "The 'where do you want to eat / I don't know where do YOU want to eat' conversation ends here"
- URL: https://www.reddit.com/r/SideProject/comments/1thxc9n/the_where_do_you_want_to_eat_i_dont_know_where_do/
- provenance class: HUMAN_SEEDED_INSPIRATION.

Source-faithfulness rule:
- preserve the recognizable decision loop and familiar-default ending;
- do not claim the source literally happened in a Korean office;
- Korean-localize setting, food, timing and dialogue;
- do not fabricate a named company, restaurant, or exact autobiographical incident.

## 2. L1-L7 — USER APPROVED 2026-09-06

### L1 SOURCE DISCOVERY
Selected because the source contains a compact, highly sceneable social loop:
people ask for preferences, refuse to choose, reject actual suggestions, then default to the usual place.

### L2 HUMAN-INTEREST GATE
PASS:
- near-universal "뭐 먹지?" recognition;
- low exposition burden;
- strong repetition/payoff structure;
- visually cheap;
- no moral lesson required.

### L3 SOURCE NORMALIZATION
Pattern:
- someone initiates lunch selection;
- nobody wants decision responsibility;
- "anything is fine" is not actually true;
- concrete suggestions reveal hidden preferences;
- time is wasted;
- familiarity beats choice.

Tone:
- light annoyance, not real conflict;
- nobody is the villain;
- understated ordinary coworker banter;
- no meta "직장인 공감" caption.

### L4 STORY SHAPE
DECISION_LOOP → REJECTION CASCADE → FAMILIAR DEFAULT.

### L5-L7
Final structure below supersedes the earlier draft.

## 3. Cast — USER APPROVED 2026-09-06

Three recurring leads are used because the three-way preference loop materially improves the comic rhythm.

- Harin: initiates / mediates the menu discussion.
- Gaeun: brighter reaction energy; says she is flexible but rejects at least one option.
- Taemin: deadpan / practical rejection role.

This is an episode-specific functional choice, not a project-wide three-person quota.

## 4. Six-slide storyboard — USER APPROVED 2026-09-06

### S01 — lunch question / openness
Location: ordinary office lunch area / meeting-table area, shortly before noon.

Dialogue intent:
- Harin: "오늘 점심 뭐 먹지?"
- Gaeun: "난 아무거나 좋아."
- Taemin: "나도."

Visual intent:
- all three still relaxed;
- clear three-person identity/style anchor opportunity;
- no baked text in production raster.

### S02 — first proposal rejected
- Harin: "그럼 제육?"
- Gaeun: "어제 먹었잖아…"
- Taemin listens.

Tone:
Gaeun is not angry; mildly apologetic / matter-of-fact rejection.

### S03 — second proposal rejected
- Harin: "그럼 냉면?"
- Taemin: "오늘은 좀 차갑지 않냐…"

Tone:
deadpan practical objection; discussion is starting to drag.

### S04 — third proposal rejected
- Gaeun: "돈까스는?"
- Taemin: "거기 점심때 줄 길걸."
- Harin: "그럼 대체 뭐 먹어…"

Tone:
visible fatigue increases.
If hands are near faces or multiple fingers are exposed, mark anatomy risk HIGH for QC.

### S05 — time / hunger realization
- Harin: "우리 이 얘기 몇 분째 하는 거야?"
- Taemin: "배고픈데 결정은 더 안 됨."
- Gaeun: "그냥 무난한 데 갈까…"

Visual:
phone or clock check is enough; do not let incidental text become baked semantic lettering.

### S06 — familiar-place payoff
Location: generic familiar Korean lunch restaurant, no real brand.

- Gaeun: "역시 여기가 제일 무난해."
- Taemin: "처음부터 여기 올 걸."
- Harin: "그러니까…"

Visual:
already seated and eating; unusually calm / routine.
The scene itself is the punchline.
Avoid decorative signage/menu text unless required by the final lettering plan.

## 5. Reference authority — USER CONFIRMED 2026-09-06

The user re-supplied the same current visual authorities during this session.

Canonical repository equivalents:
- REF_V2_D: assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
- REF_V2_E: assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg

Roles:
- REF_V2_D: character identity + face/line/color authority.
- REF_V2_E: multi-character scene drawing language + background density / character-environment integration.

Approved binaries outrank generalized prompt prose.

## 6. Native-chat S01 and failed continuation experiment

A ChatGPT/native S01 image was visually approved by the user in this session.
However:
- it was not produced by the repository render adapter;
- no repository attempt record / artifact hash is bound to it;
- therefore it is **visual taste evidence only**, not a machine-valid PRODUCTION_STATE episode_anchor.

Do not fabricate an attempt or anchor record for it.

After that S01 approval, several native-chat continuation attempts failed the production contract:
- outputs repeatedly collapsed S02-S06 into one six-panel page;
- Korean dialogue / labels were baked into the raster;
- at least one panel showed face/hand degradation, especially under small-panel + hand-near-face conditions.

All such multi-panel/baked-text outputs are INVALID and must not be used as anchors, repair bases, or final art.

Finding:
the long conversational context caused native image generation to optimize for "complete the episode/page" rather than the isolated requested slide.
This is a renderer/context isolation failure, not evidence that the supplied references are inadequate.

## 7. Current operating mode — MANUAL_VALIDATION

Until the image API/provider adapter is actually connected and measured:
- every production stage is user-reviewed manually;
- no automatic continuation after S01;
- each raster slide is generated and reviewed one at a time;
- lettering remains separate and is reviewed separately;
- final export is reviewed separately.

Chat/native image generation may be used temporarily for manual visual experiments, but it is not treated as a reproducible machine-bound production attempt unless the artifact is explicitly ingested through a future sanctioned ingest path.

If a conversation-inferred renderer repeats a hard contract failure such as MULTI_PANEL or BAKED_TEXT twice:
- stop retrying in the same contaminated context;
- use a clean dedicated render context or wait for the explicit API renderer;
- do not burn repeated attempts on the same failure mode.

## 8. Long-term target — API_PRODUCTION

Target user experience remains:
**storyboard approval → reference confirmation → S01 approval → finished episode**.

Internally, the long-term runner should use isolated requests:
- one request = exactly one slide;
- explicit canonical prompt + only that slide contract;
- actual reference binaries + approved S01 anchor as media inputs;
- image provider adapter, initially benchmarking GPT-Image-2;
- deterministic local contract QC first;
- low-cost vision QC provider adapter, initially benchmarking DeepSeek Flash Vision;
- deterministic Python lettering;
- cost / retry / first-pass-rate logging.

Model names are initial benchmark candidates, not permanent architecture constants.

## 9. Exact next action for the next session

1. restore this README + PRODUCTION_STATE + CURRENT_STATE;
2. create EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN from the already-approved six-slide package;
3. show the structured contracts / preflight result to the user for manual approval;
4. only after that approval, perform one-slide-at-a-time raster validation;
5. do not auto-finish while MANUAL_VALIDATION is active.
