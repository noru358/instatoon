# GENERATION_PROTOCOL.md

# GENERATION / CONTINUITY / REPAIR / QC PROTOCOL — v2.2
Updated: 2026-09-05

## 0. Stage order

Production order:

1. approved source/premise;
2. story beats;
3. humanized dialogue;
4. USER VOICE GATE during learning phase;
5. whole-episode storyboard + cast router;
6. internally derive any required episode-local character identity digest;
7. whole-episode visual/text plan;
8. text-free raster generation;
9. editable lettering/composition;
10. QC;
11. targeted repair from last-known-good asset;
12. export.

Do not skip directly from a premise to production frames.

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
- if the renderer supports explicit reference-media inputs, supply the canonical binaries;
- if a native/direct renderer has no explicit repository-media slot, the operator must first inspect the canonical binaries and compile their observed identity/style constraints together with MASTER_PROMPTS into the generation instruction;
- in that second mode, report honestly that the output is authority-informed but not binary-conditioned;
- such an output may be QC'd and used as a prototype, but must not be promoted to a new canonical reference solely because the prompt said it matched.

Never substitute obsolete/legacy refs.

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
