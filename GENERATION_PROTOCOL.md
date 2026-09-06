# GENERATION_PROTOCOL.md

# GENERATION / CONTINUITY / REPAIR / QC PROTOCOL — v2.4
Updated: 2026-09-06

## 0. Stage order

Production order:

1. approved source/premise;
2. story beats;
3. humanized dialogue;
4. USER VOICE GATE during learning phase;
5. whole-episode storyboard + cast router;
6. internally derive any required episode-local character identity digest;
7. whole-episode visual/text plan, including sequence-level shot direction and expression-amplitude plan;
8. text-free raster generation;
9. editable lettering/composition;
10. QC;
11. targeted repair from last-known-good asset;
12. export.

Do not skip directly from a premise to production frames.
Do not enter raster generation until the structured render-contract gate below passes.

### Mandatory visual preflight before L13

Before ANY raster generation — including ChatGPT/native image generation — restore and inspect the current visual authorities:
1. CURRENT_STATE.md;
2. MASTER_PROMPTS.md;
3. VISUAL_GRAMMAR.md;
4. GENERATION_PROTOCOL.md;
5. REFERENCE_SET.md;
6. active episode package;
7. the actual current style/main-cast/scene reference binaries required by that episode.

Do not generate from chat memory alone.

Native/direct image generation is a valid production renderer and is the default when it can satisfy the episode requirements. Do not invoke an external renderer merely because one exists.

Use an external renderer only when:
- the user explicitly requests it;
- native generation lacks a material capability required by the episode;
- a reproducibility/automation/provider test specifically requires it.

Reference handling:
- inspect the currently exposed tool parameters before judging capability;
- use an explicit prompt and explicit local-image inputs when the tool provides them;
- native/direct does not imply CONVERSATION_INFERRED; choose the mode from the actual interface;
- pass the canonical binaries as actual media. Inspection or text descriptions alone do not satisfy BINARY_REQUIRED;
- authority-only output is a prototype exception only when explicitly allowed by the episode, never the current v2 production fallback.

Never substitute obsolete/legacy refs.

## 0.5 Current operating mode — MANUAL_VALIDATION (canonical, 2026-09-06)

The current learning phase is manual, but **manual does not mean user approval after every slide**.

Default user-facing checkpoints are the major production gates:
1. pre-raster content/plan approval: source/story/dialogue/storyboard/structured contract as applicable; unchanged subpackages are not re-approved;
2. S01 anchor approval: the user checks the first real rendered frame for style, main identity and overall render direction;
3. complete text-free raster-set approval: after S01 PASS, the operator produces S02 through the final slide as separate files with internal QC, then presents the whole art set to the user;
4. lettering/final approval: only after the raster-set PASS are the approved text layers applied and the finished episode reviewed.

During the learning phase, L8 may remain an earlier explicit sub-gate before storyboard construction. That internal layer ordering does not change the post-S01 approval topology above.

Hard distinction:
- **one slide = one image file** remains mandatory;
- **one slide = one user approval gate** is NOT the default.

After S01 USER PASS:
- S02 through the final slide may be rendered sequentially without asking the user after each frame;
- each frame still receives operator/internal QC for contract, style/identity, anatomy and scene correctness;
- conversation-inferred rendering still proceeds one frame at a time so a bad frame cannot contaminate the next;
- machine-bound QC records distinguish S01 `inspector=USER` from later `inspector=OPERATOR_INTERNAL` or `AUTO_VISION`;
- once every raster has a current artifact-bound PASS, state moves to `RASTER_SET_QC_PENDING`;
- only a USER PASS on the complete raster set authorizes `LETTERING`.

User re-entry before the complete raster set is required only when the operator cannot resolve a material taste/contract decision internally, such as:
- changing story/cast/approved dialogue;
- changing the visual authority or S01 anchor direction;
- a systemic renderer failure that requires a plan/prompt/provider decision rather than ordinary repair.

A local hand, prop, extra, text-baking, wrong-scene or stochastic failure is normally an **operator repair/QC task**, not a new user gate.

AUTO_FINISH is separate: after a machine-bound S01 USER PASS it intentionally bypasses the STANDARD full-raster-set and later manual gates, using automatic QC/lettering/final QC instead. It is preserved as experimental infrastructure and is not the default MANUAL_VALIDATION path.

Chat/native generation may be used for temporary visual validation. A native result that is not persisted with an attempt/artifact hash can be a user-approved visual/taste anchor, but it must not be falsely recorded as a machine-authoritative anchor.

### Conversation-inferred renderer isolation rule

E007 demonstrated that a long conversational image context can reinterpret a single-slide request as "complete the whole comic page".

Therefore, for CONVERSATION_INFERRED/manual native generation:
- never treat the full episode conversation as reliable request isolation;
- if MULTI_PANEL, BAKED_TEXT, wrong-cast, or unrelated-scene hard failures repeat twice in the same context, stop retrying that path;
- use a clean dedicated render context for the next manual experiment, or remain blocked until the explicit API renderer is available;
- repeated hard-contract failures are renderer/context failures, not ordinary stochastic noise.

### Reference routing

Cast cardinality / role rule:
- determine cast from the approved premise and beat requirements, never from a recurring-character quota;
- a scene or episode may use 0–3 recurring leads;
- supporting/episode-only characters are first-class cast when the story role requires them;
- do not add Gaeun/Harin/Taemin merely to create a reaction shot or fill a three-person composition;
- if an episode-local character appears in 2+ cuts, give that character a persistent identity digest before raster generation;
- this routing policy is global pipeline behavior; episode packages store only the resolved cast/roles for that episode.

- recurring lead: canonical style media + that selected lead’s actual identity reference;
- episode-only person: canonical style media for drawing language only + the story-derived age, gender/presentation, body, hair, clothes and identity digest;
- mixed cast: assign the role per person; never apply a whole cast sheet indiscriminately;
- after a machine-valid visual acceptance: include the accepted episode image as actual secondary identity/style media in later calls;
- a native/chat image that was merely liked by the user but is not persisted/bound may inform taste, but must not be falsely recorded as a machine-valid anchor.

Separate what is fixed (drawing language) from what changes (age, gender, physique, clothing, location, action, expression).

Background-extra identity isolation:
- a shared main-cast sheet may contain multiple recurring identities, but only explicitly selected main-cast identities may be instantiated as those characters;
- unselected recurring identities are NOT templates for incidental coworkers, strangers, customers, guards, or other extras;
- incidental extras inherit drawing language only: line, eye/face grammar range, flat color, simplification, and background integration;
- when story constraints allow, vary extras across age band, face shape, eye size/shape within the approved style range, hair silhouette/texture, body build, and ordinary clothing;
- extras must be visibly distinguishable from every recurring lead and must not read as a near-copy of Gaeun, Harin, or Taemin;
- one-frame extras do not need a persistent identity digest unless reused later.


### Sequence-level shot planning — anti-hardcoding invariant

The visual director plans camera/framing across the episode before or during coordinated raster production.

This is NOT a direction-counting rule. Never hard-code "one left-facing frame," equal left/right counts, or a fixed camera-angle recipe.

For beats with multiple valid visual solutions:
- maintain a small candidate set or equivalent internal alternatives;
- describe alternatives by camera side/height, shot distance, body orientation, face orientation and gaze;
- choose the option that best serves the beat while reducing unnecessary similarity to nearby/earlier frames;
- if only one composition clearly serves the story, use it even if it repeats a direction.

The pass condition is that the completed sequence does not feel directionally or compositionally biased because of renderer defaults. Viewer perception outranks token counts.

A frontal camera is not automatically a neutral-direction frame; QC judges the actual apparent face orientation.

Expression planning follows the same principle: role and story beat determine amplitude. "Restrained," "not grotesque," or "not melodramatic" must not silently become a global low-energy acting lock.

### One frame / one file

- one generation request targets exactly one planned slide;
- supply only that slide’s scene/action contract when the interface allows explicit isolation;
- input reference sheets remain reference-only, never output layout examples;
- deliver separate `slide_01.png`, `slide_02.png`, etc., with one panel in each file;
- no comic strip, grid, collage or all-in-one episode image as a substitute;
- a combined review sheet is optional only when requested, and never replaces individual files;
- inspect panel count before style/anatomy QC. A merged multi-panel output is an immediate contract FAIL.

### QC order

QC is ordered so cheap hard-contract checks run before subjective visual checks.

**QC-0 contract**
- exactly one slide artifact;
- expected aspect / dimensions when machine-verifiable;
- one panel, not a grid/collage/page;
- no baked important readable dialogue/caption text;
- expected slide/cast semantics.

**QC-1 style / identity**
- approved drawing language;
- recurring identity / hair / clothing continuity;
- background density and finish;
- no generic AI-webtoon beautification drift.

**QC-2 anatomy / scene**
- face/hand integrity;
- occlusion;
- prop interaction;
- action/composition/story clarity.

**QC-3 sequence visual balance — after multiple/complete frames exist**
- inspect the set as a viewer, not only frame-by-frame;
- detect repeated apparent face orientation, gaze direction, body turn, camera side/height or shot distance that creates a perceptual bias without story reason;
- do NOT use fixed left/right/front quotas as the pass criterion. Compare visual redundancy against story-valid alternatives;
- check whether anti-exaggeration wording flattened comedy/reaction/reveal beats into uniformly small acting;
- check story-relevant mirrors/reflections for coherent face/torso/limb geometry;
- check supporting-character skin/local-color treatment for a different yellow/sepia cast from the main character without justification;
- when the set fails, identify the minimum subset of frames driving the problem and rerender/repair those frames only. Do not regenerate the whole episode by default.


High-risk anatomy cues raise scrutiny but do not forbid the pose:
hands near face, multiple exposed fingers, overlapping hands, phone/utensil grip, chopsticks, and physical contact.

A larger mouth during laughter or strong expression is NOT a defect by itself.
Fail only when the mouth treatment breaks the approved drawing language, identity, or facial proportions.

## 0.6 Renderer capability / reference-injection gate

Reference presence in the repository is NOT proof that a renderer received the reference.

Before authorization, the operator/runtime must declare:
- the renderer/tool;
- the actual reference-conditioning mode;
- the exact canonical reference paths actually supplied to the renderer as media inputs.

Machine rule:
- if EPISODE_PLAN.style.reference_conditioning_requirement = BINARY_REQUIRED, AUTHORITY_INFORMED_NON_BINARY_CONDITIONED is forbidden;
- every required canonical reference must be evidenced as actually supplied media;
- merely reading Markdown, inspecting a file, fetching its bytes, or mentioning its path in the prompt does not count as binary conditioning;
- if the current renderer cannot accept the required media, do not render with that renderer. Select a capable renderer/adapter or remain blocked at preflight;
- never perform a speculative raster call to “see if prompt-only is close enough” when BINARY_REQUIRED.

This gate exists because style fidelity is a renderer-input capability, not a prose-compliance problem.

### Mandatory structured render-contract gate

Before L13, the active episode must contain:
- `EPISODE_PLAN.json` conforming to `schemas/episode_plan.schema.json`;
- `RENDER_MANIFEST.json` conforming to `schemas/render_manifest.schema.json`.

The manifest is bound to the exact EPISODE_PLAN Git blob SHA. If the plan changes, the old manifest becomes stale and rendering is blocked.

Run:
`python pipeline/render_guard.py validate`

The executable guard checks a subset of schema/business rules (it does not run full JSON Schema validation):
- CURRENT_STATE active episode == plan episode == manifest episode;
- continuous slide indices and exact slide count;
- text-free raster output;
- output ratio/dimensions;
- episode-only identity digest when the person recurs;
- required local media paths exist and SHA-256 matches their manifest;
- plan ↔ manifest scene contracts and required/forbidden entities are identical;
- manifest is not stale.

### Prompt-binding modes

Every renderer run records one prompt-binding mode:

`EXPLICIT_COMPILED_PAYLOAD`
- renderer receives the deterministic prompt compiled from MASTER_PROMPTS + EPISODE_PLAN/RENDER_MANIFEST;
- render first frame;
- continue remaining batch only after first-frame semantic QC PASS.

`CONVERSATION_INFERRED`
- renderer infers instructions from conversation/context rather than receiving an auditable explicit compiled payload;
- parallel/multi-frame batch is prohibited;
- render exactly one frame;
- semantic-QC that frame;
- only a PASS authorizes the next frame.

This stricter mode applies only when the current interface lacks an explicit auditable payload. Tool names and old session limitations do not establish its mode.

### Semantic hard-stop

If an output substitutes or introduces a materially different story/cast/concept — for example an unrelated mascot, animal, self-help/productivity scene, coding/Git scene, collage, poster, baked semantic text, or any episode-specific forbidden entity — then:
1. mark the image INVALID;
2. do not continue the batch;
3. do not repair from it;
4. do not promote it to LAST_KNOWN_GOOD or any reference;
5. inspect prompt binding / manifest / renderer path before retrying.

Renderer success means semantic contract compliance, not merely “an image was returned.”

## 1. Cast routing comes before character rendering

Story/context decides cast.

Main cast:
- Gaeun
- Harin
- Taemin

No main character is mandatory.
No main character is globally banned by default.

Never choose Taemin solely because a scene needs a man.
Never choose Harin solely because a scene needs a woman.

Record per episode:
- selected main cast;
- episode-only cast;
- why each is appropriate.

## 2. Episode-local character design — internal continuity rule

If a new non-main person appears in 2 or more cuts:

### A. Derive once
Before assembling the episode render batch:
1. infer one character design from the story, social role, and scene context;
2. verify age/presentation/social role;
3. verify hairstyle/face/clothing are coherent;
4. verify the design is distinct from main cast;
5. verify the face does not read as a generic smooth AI default;
6. record a compact identity digest.

### B. Carry through the batch
All later cuts preserve:
- face structure;
- hair silhouette;
- age;
- clothing unless the story explicitly changes it;
- salient identity details.

Only pose/expression/camera/action change by beat.

This is not a separate user-facing character-sheet or approval stage.
A temporary internal image anchor is an exception used only when direct multi-cut continuity fails.
One-frame incidental extras may skip the identity digest.

## 3. Reference roles

Keep these roles separate:

### STYLE REFERENCE
Controls:
- line;
- face grammar;
- color/rendering;
- background density;
- overall finish.

### MAIN CHARACTER REFERENCE
Controls identity of Gaeun/Harin/Taemin when selected.

### EPISODE-LOCAL IDENTITY DIGEST
An internal context-derived continuity record for a new multi-cut character. It is not a default deliverable.

### LAST-KNOWN-GOOD FRAME
Controls accepted composition/blocking/location during targeted repair.

A scene reference must not redefine style.
A failed/regressed retry must not become the new authority.

## 4. Prompt assembly

Free-form prompt rewriting at render time is prohibited.

The canonical compiler source is:
- `MASTER_PROMPTS.md` → `## 12. COMPILED PRODUCTION PROMPT`;
- active `EPISODE_PLAN.json`;
- bound `RENDER_MANIFEST.json`.

Use:
`python pipeline/render_guard.py compile --episode <ID> --slide <N>`

Per raster frame:

1. scene facts;
2. story clarity;
3. output ratio;
4. text-free / planned negative-space instruction;
5. cast identity reference(s);
6. episode-local identity digest when applicable;
7. last-known-good preservation block for repair;
8. MASTER_PROMPTS stable visual blocks.

Do not rewrite the visual style from scratch per slide.

## 5. Text-free raster policy

Production raster should normally include:
- people;
- props;
- background;
- non-text expression/reaction marks.

Do not bake final:
- hook;
- narration;
- dialogue;
- speech bubbles;
- labels;
- source notes

into the canonical raster master.

Reason:
- better Korean text control;
- easy dialogue iteration;
- consistent font/size;
- less poster-like AI composition;
- lower repair cost.

Baked-in text is acceptable only for a quick prototype/taste check.

## 6. Output tracks

Feed/carousel:
- 4:5;
- 1080×1350.

Reels/Shorts:
- 9:16;
- 1080×1920.

16:9 only when explicitly required.

Do not stretch.
Recompose/crop using planned safe space.

## 7. First-pass visual QC

Check in this order:

1. correct story beat;
2. correct cast choice;
3. correct recurring identity or episode-only identity digest;
4. style lock;
5. scene blocking;
6. hands/object interaction;
7. spatial logic;
8. background simplicity;
9. planned text space;
10. ratio.

A pretty but incorrect character = fail.
A stylish frame in the wrong story order = fail.
An image from a different story/concept = semantic hard fail and immediate stop.

Continuation authorization:
- S01 must receive the user-facing anchor PASS before the remaining raster stage begins;
- explicit compiled payload: after the S01 user gate, remaining frames may be produced as an isolated batch, but each candidate still needs internal QC before the complete raster-set user gate;
- conversation-inferred: after the S01 user gate, render one frame at a time and require the previous frame's internal artifact-bound QC PASS before the next call. This is an operator QC gate, not a user approval gate.

## 8. Last-known-good rule

Every accepted:
- style test;
- episode-only identity digest or exceptional temporary anchor;
- episode frame;
- layout

may be marked LAST_KNOWN_GOOD.

When a subsequent retry is worse:
- reject the retry;
- revert to the last-known-good input;
- do not continue chaining from the regression.

This prevents repair drift.

## 9. Minimal-change repair rule

Before editing, classify the issue:

### LOCAL
Examples:
- wrong supporting character;
- typo/text placement;
- one hand;
- one prop;
- one expression;
- one accessory.

Action:
edit only the named defect.
Preserve:
- camera;
- composition;
- scene blocking;
- background;
- accepted character(s);
- palette;
- line style;
- all unmentioned objects.

### SYSTEMIC
Examples:
- entire batch uses wrong visual style;
- all new-character faces drift;
- all backgrounds get beige cinematic treatment;
- text layout system is fundamentally wrong.

Action:
repair the shared prompt/reference/layout system, then rerun only what depends on it.

Do not full-regenerate a good frame for a local defect.

## 10. Sequence-order QC

Before final carousel export, validate beat order explicitly.

For each adjacent pair:
- does slide N cause/enable/precede slide N+1?
- does REVEAL/PEAK occur before AFTERMATH/LANDING?
- was any generation/upload order accidentally mistaken for story order?

Final file naming must use explicit numeric prefixes:
- slide_01
- slide_02
- …
- slide_07

File creation time or tool-return order never defines narrative order.

## 11. Lettering QC

Final vector text check:
- phone-size readability;
- role-appropriate size;
- safe margins;
- bubble tail target;
- no text-face/hand/prop collisions;
- line breaks;
- reading order;
- contrast;
- no accidental duplicate narration;
- no tiny type used to save an overlong line.

See VISUAL_GRAMMAR.md for type scale.

## 12. Style QC current critical checks

Reject if:
- generic smooth AI face appears;
- a one-off male accidentally becomes Taemin;
- warm beige/sepia wash dominates;
- global texture/grain appears;
- background becomes polished lifestyle illustration;
- glossy/strand-heavy hair;
- modeled soft lighting/shading;
- environment looks more rendered than characters.

## 13. Cost / retry policy

Plan globally before paid generation.

Prefer:
- one first pass;
- targeted edit;
- bounded retries.

Do not “try again until good.”
If repeated failure is systemic, stop and repair the shared input.

## 13.5 Renderer selection / reporting

For each raster run record:
- execution actor;
- renderer/tool actually used;
- why that renderer was selected;
- exact Markdown authorities read;
- exact visual assets inspected;
- which assets were actually passed as renderer media inputs, if supported;
- whether the output is BINARY-CONDITIONED or AUTHORITY-INFORMED / NON-BINARY-CONDITIONED;
- generation attempt/result/cost when applicable.

A renderer failure is a local provider/tool failure unless all valid render paths are unavailable.
Do not mark the entire L13 stage blocked merely because one optional external provider has no credits.

## 14. Recordkeeping

For durable/paid production record:
- episode ID;
- slide index;
- exact story beat;
- selected identity references;
- selected style references;
- prompt/version;
- output ID/path;
- dimensions;
- QC verdict;
- whether LAST_KNOWN_GOOD;
- repair scope.

## 15. Automation boundary

Future automation can:
- route cast;
- detect episode-only continuity requirement;
- derive and persist internal one-off identity digests;
- assemble prompts;
- check sequence order;
- run deterministic text/layout QC;
- route targeted repair.

During the learning phase:
- USER VOICE GATE stays human;
- material visual-style changes stay human;
- final taste/publish remains human.


## 16. Short-term style-binding lock — CANONICAL

For the current production phase, style-sensitive raster generation is production-authorized only when the canonical style reference is bound to the renderer as ACTUAL IMAGE MEDIA.

A repository path, Markdown description, prompt paraphrase, filename, hash, or operator memory does NOT count as style-media binding.

Required per production render:
1. actual canonical style-sheet image media;
2. current slide contract from EPISODE_PLAN / RENDER_MANIFEST;
3. recurring-character identity media when that identity is present;
4. after the first accepted style pass, the accepted episode style/identity anchor as secondary actual image media on every later slide.

Current short-term hierarchy:
CANONICAL STYLE MEDIA → ACCEPTED EPISODE STYLE/IDENTITY ANCHOR → SLIDE SCENE CONTRACT → renderer.

If the runtime cannot actually attach the required image media:
- do not silently fall back to text-only style description;
- do not call the result production-ready;
- either use a renderer/runtime that can bind the media or stop at prototype status.

An accepted image may serve as an episode style/identity anchor even when its composition/story beat is not accepted, but that role must be recorded explicitly. It must not be mislabeled as a story-correct LAST_KNOWN_GOOD frame.

For conversation-inferred native rendering:
- actual reference images must be present in the current conversation and selected as the intended visual references;
- one frame only per call;
- visual QC before every next frame;
- attach/reuse both canonical style media and the accepted episode anchor after the style anchor exists.


## Generic media-requirement mapping

Instatoon is a child adapter of the AutoPipeline MEDIA_INPUT_CONTRACT.

RENDER_MANIFEST.media_requirements is the machine-facing authorization source.
Each item declares:
- requirement_id;
- role;
- media_type;
- source_id;
- conditioning;
- required;
- optional expected_hash.

Current style_refs remain a project-level compatibility field, but authorization does NOT hard-code or iterate special asset names from style_refs. Every style ref must map into media_requirements.

Future requirements such as:
- character_identity anchor;
- repair_base / LAST_KNOWN_GOOD image;
- location anchor;
- other image/audio/video conditioning

are added as new media_requirements entries. The authorization algorithm itself does not change.

AutoPipeline owns the generic declared/capability/supplied model; Instatoon adds story, slide-order, style, and episode-specific validation.

## 17. Implementation boundary

The standalone guard does not call the renderer or inspect generated pixels. `--previous-frame-qc PASS` and supplied-media arguments are caller declarations, not stored inspection records.
Manual production must check the actual request and output. Future runtime requirements are specified in AUTOMATION_TRANSITION.md: persist approval/QC bound to exact artifacts, build media evidence from the request and call the renderer through the same entry point.
Do not claim CI or input authorization proves story/style correctness.


## 18. Persisted production-state gate — ACTIVE

Every canonical episode that reaches render-contract stage must contain `episodes/<ID>/PRODUCTION_STATE.json`.

This file is the machine-facing execution authority for:
- current production stage;
- L8 full-package approval;
- durable partial decisions such as CAST_RESOLVED that are explicitly **not** full L8 approval;
- per-slide QC records bound to slide_id, attempt_id and artifact SHA-256.

Render authorization rules:
- `voice_gate.status=PASS` is insufficient by itself; `approved_scope` must be `L1_L7_FULL_PACKAGE` and approval_kind must be `USER_EXPLICIT`;
- a cast-only choice or other partial decision cannot authorize L10+ or L13;
- slide 1 requires a render-ready stage;
- slide 2+ in conversation-inferred mode requires a persisted PASS record for the immediately previous slide;
- a CLI/string `--previous-frame-qc PASS` is compatibility input only and is never evidence;
- explicit-payload continuation requires persisted first-frame QC.

This is a fail-closed bridge until the future runtime DB replaces the repository sidecar.


## 13. Experimental AUTO_FINISH approval topology — 2026-09-06

This section changes **approval frequency**, not the production-layer order.

Human checkpoints in AUTO_FINISH:
1. the existing L8/source-dialogue-storyboard package approval;
2. the first usable episode frame (S01) after the human actually inspects the rendered artifact.

After checkpoint 2, the runtime may finish the episode without further user approvals only when all of the following are true:
- S01 PASS is persisted against its exact attempt and artifact SHA-256;
- S01 is the fixed episode anchor;
- the episode's final copy and lettering placement are already locked in a current `LETTERING_PLAN.json`;
- remaining frames use EXPLICIT_COMPILED_PAYLOAD and the same binary style authorities;
- each remaining frame receives conservative automatic visual QC;
- deterministic separated lettering succeeds;
- final layout QC succeeds.

The raster/text separation remains mandatory:
`renders/*_art.png` → `lettering/*_overlay.png` → `exports/*_final.png`.
AUTO_FINISH must never ask the image renderer to bake final dialogue into raster art.

Automatic QC may authorize continuation only for an unambiguous PASS. Low confidence, semantic/style failure,
or a condition requiring prompt/plan changes is a hard stop for AUTO_FINISH, not permission to improvise.
Only stochastic generation failure is retryable automatically, with both per-slide and whole-episode render-attempt caps.

Rollback is a first-class transition, not an exception to the rules:
- raster/QC failure returns to STANDARD at `REMAINING_RENDER`;
- lettering/final-layout failure returns to STANDARD at `LETTERING`;
- accepted artifacts remain hash-bound and reusable;
- failed candidates never replace the human-approved episode anchor.

STANDARD mode remains supported indefinitely during the experiment. Removing the experiment therefore requires
no migration of episode assets or state; select STANDARD and continue from the persisted stage.


### Episode-local identity promotion during AUTO_FINISH

If a recurring episode-local character first appears after S01, a text digest alone is not sufficient for reliable visual continuity.
The first frame for that character may become a character-specific identity anchor only after that frame receives a valid human or AUTO_FINISH QC PASS.
That accepted artifact is then supplied on later slides where the same character appears.

This promotion is derived from `cast.episode_only[].appears_in`, never from hardcoded character names.
A failed candidate is never promoted. If the anchor slide is later invalidated with FAIL, its character-specific identity anchor is removed.
The global S01 episode anchor remains fixed and separate from these character-specific anchors.
