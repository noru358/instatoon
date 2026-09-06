# VISUAL_GRAMMAR.md

# INSTATOON_VISUAL_GRAMMAR_v0.6 — SEQUENCE / COMPOSITION / LETTERING
Updated: 2026-09-07

STYLE authority: STYLE_LOCK.md / MASTER_PROMPTS.md
CONTENT authority: SOURCE_STORY_PIPELINE.md

## 0. Core principle

Plan the entire episode first.
Compose individual slides only after the sequence, cast, text roles, and visual rhythm are coherent.

A slide exists because it performs one story job.

### 0.1 Approved creative baseline — 2026-09-07

This is the project-level visual/storytelling baseline, not a fixed episode template.

- One slide should have one primary information or emotion beat. Supporting cues may exist, but the slide should have a clear owner of attention.
- Empty space is functional. Do not fill unused space merely to make the frame feel busier or more "finished."
- A face is not mandatory as the carrier of meaning. A phone, object, hand, posture, room distance, empty chair, or other scene element may carry the beat when that communicates the story better.
- Text and art divide labor. Do not narrate what the image already makes obvious, and do not force the raster to explain information better handled by editable text/UI.
- Reaction and silence are valid story jobs. A quiet reaction, pause, or object-only beat may earn a slide when it changes the reader's interpretation or emotional state.
- Dialogue-led, object-led, reaction-led, and scene-led episodes may use different proportions. Do not force a recurring visual recipe, fixed four-cut structure, or mandatory reversal.

This baseline governs composition decisions together with the episode-specific story contract. STYLE_LOCK still owns drawing language; this section does not redefine the art style.

## 1. Canvas / distribution

Primary feed/carousel master:
- 1080 × 1350
- 4:5 portrait

Vertical derivative:
- 1080 × 1920
- 9:16 Reels/Shorts

16:9 is not the default.

All slides within one carousel should share one ratio.

Current delivery requirement: ONE PANEL = ONE IMAGE FILE. Each planned slide is composed and delivered separately. A multi-panel page, strip, collage or review sheet cannot substitute for individual slide files. Optional combined previews require a user request and do not replace the masters.

## 2. Episode length

Typical:
- 5–9 slides;
- 6–8 common;
- shorter preferred when the story lands cleanly.

No padding to meet a quota.

Each slide has:
- one primary beat;
- at most one supporting reaction/cue;
- short text.

## 3. Cover / hook

Slide 1 is a hook, not a summary.

Preferred:
- short specific hook;
- one dominant scene or focal object;
- strong phone-size legibility;
- enough unanswered information to justify the next swipe.

Avoid:
- executive-summary text;
- long context;
- multiple claims;
- decorative title-card treatment.

The cover can be text-led, but it must still feel like part of a comic sequence.

## 4. Page archetypes

Choose one dominant archetype per slide:

- HERO_SCENE
- TWO_SHOT
- REACTION_CLOSEUP
- OBJECT_FOCUS
- TEXT_LED
- QUOTE_LED
- EMPTY_BEAT
- BEFORE_AFTER
- SPLIT_COMPARE
- SEQUENCE_WITHIN_SLIDE is inactive under the current one-panel-per-file requirement; do not create mini-panel strips.
- SCREEN_INFORMATION
- REACTION_WITH_UI_INSET

Current production requires one single-panel composition per file.
A UI inset/overlay is allowed when it is one informational layer inside a single composition, not a second comic panel.
Do not subdivide by habit.

## 5. Visual rhythm

Consistency does not mean identical camera/blocking.

Across a chronological anecdote, use deliberate variation such as:
- wide/medium → medium → detail → reaction;
- two-shot → hand/object focus → close reaction;
- normal spacing → compressed peak → quiet landing.

Avoid six nearly identical medium two-shots.

Do not vary camera merely for spectacle.
Variation should clarify the story.

### 5.1 Sequence-level directional balance — perceptual, not quota-based

Face direction and camera direction are judged across the whole episode as a viewer experiences it, not one frame at a time.

The failure to avoid is **perceptual directional bias**: several frames repeatedly presenting the same apparent face orientation, gaze, body turn, camera side, height and distance until the set feels mechanically biased.

Do NOT solve this with a hard-coded quota such as "at least one left-facing face" or "equal numbers of left/right/front." Those counts are not the objective and can create artificial blocking.

Instead:
1. for each beat, identify more than one story-valid shot when alternatives naturally exist;
2. describe candidate shots using dimensions such as camera side, camera height, shot distance, body orientation, face orientation and gaze direction;
3. select the shot that best preserves story clarity and continuity while reducing redundant visual similarity with nearby/earlier frames;
4. allow front, either three-quarter direction, profile, over-shoulder, back view, high/low angle, upward/downward gaze, or other camera relationships only when they serve the beat;
5. after the raster set exists, inspect the whole sequence for repeated perceived orientation/framing and replace only the frames materially causing the bias.

The goal is **balanced visual experience**, not mathematically even direction counts.

A frontal camera does not automatically mean a neutral face direction. Judge the face as it is actually perceived in the output.

### 5.2 Role-adaptive expression amplitude

Expression should be strong enough to read at phone size.

Do not interpret anti-exaggeration rules as a requirement for uniformly small reactions. Quiet/setup beats may be restrained; comedy, surprise, reveal, embarrassment and reaction beats may use clearly amplified facial expression, gaze, shoulders, torso, hands and stance as long as the approved drawing language and identity remain intact.

A style-preserving expressive pose is preferred over a technically safe but emotionally flat pose.

### 5.3 Adjacent-beat visual-delta / merge preflight

Story beats and visual slides are not the same thing.

Before locking slide boundaries, compare every adjacent beat. If two beats keep the same actor, location, prop and basic action, and the meaningful change is mostly screen/UI state or a tiny reaction, mark them as a MERGE_CANDIDATE.

Prefer one stronger slide when:
- the second beat would otherwise become another near-identical person-looking-at-phone frame;
- the state change can be communicated by a UI inset/overlay, reaction change, or one clear prop action;
- splitting would force the renderer to invent an unnatural presentation pose merely to expose information.

Keep beats separate only when the new slide has a meaningful visual delta such as a new action, location, relationship, body state, information viewpoint, or emotional landing.

This is not a fixed slide-count reduction rule. It is a redundancy/clarity test.

### 5.4 Screen-bearing props / information ownership

Phones, tablets, laptops, monitors, TVs, kiosks and similar screen-bearing props require an explicit screen contract before raster generation.

For each screen-bearing slide, declare:
- one primary visual-information owner: CHARACTER_REACTION, SCREEN_INFORMATION, PHYSICAL_ACTION, ENVIRONMENT, RELATIONSHIP, or MIXED_WITH_DECLARED_PRIORITY;
- what side of the physical device the character is actually looking at;
- what side/edge the camera can physically see;
- whether UI is carried by the physical screen or by a separate UI inset/overlay;
- the UI/platform profile, when applicable.

Geometry invariant:
- readable screen content exists on the display face, never on the device back;
- character gaze, device orientation and camera view must be mutually possible;
- do not rotate a phone into an impossible "show the audience everything" pose;
- if reaction and screen information both matter, prefer either an over-shoulder/POV screen shot OR a reaction shot with a separate UI inset.

A character must not appear to be deliberately presenting a private screen to the audience unless the story actually calls for that action.

### 5.5 Reflection / mirror staging

Mirrors and reflective panels are geometry-sensitive story elements.

When a reflection matters:
- the reflected face, torso and limbs must correspond plausibly to the actual subject pose and mirror plane;
- avoid using a near-duplicate front-facing figure as a fake reflection when the camera/mirror relationship would not support it;
- when useful, prefer a camera position from the side or behind the subject so the real body and reflected face can be checked against each other clearly;
- reflection correctness outranks decorative symmetry.

## 6. Cast visibility

Story/context decides who appears.

Main cast may recur when appropriate.
Episode-only characters are valid and common.

If an episode-only character appears in 2+ cuts, GENERATION_PROTOCOL requires one internally derived identity digest to be carried across the coordinated batch. It does not require a separate visible character sheet.

Do not substitute a familiar main character just to solve continuity cheaply.

### Background / incidental extras

Incidental extras use the same drawing language but do not clone recurring-lead identities.

Default when the story does not require a specific demographic:
- distribute age and appearance rather than making every extra a same-age peer;
- vary face shape, eye scale/shape within the approved style range, hair silhouette, body build and ordinary clothing;
- keep extras visually subordinate to the focal character;
- do not let a shared main-cast reference sheet cause unselected Gaeun/Harin/Taemin identities to leak into background roles.

A background extra that reads as an unselected main character is a cast-routing QC failure, not harmless style similarity.


## 6.5 Interface / platform profiles

UI follows context, not a single hard-coded app.

Resolve an interface profile from story context before rendering. Domain defaults are allowed when they are natural and remain overrideable.

Current Korean everyday-messaging default:
- locale/context: contemporary Korea + ordinary personal/group messaging + no explicitly named service;
- visual profile: KakaoTalk-inspired messaging grammar;
- use familiar Korean chat hierarchy, bubble placement, group/private distinction and read/unread behavior;
- do not require copying logos, wordmarks, trademarks, exact branded chrome, or baked readable UI text.

If the story explicitly uses another service, workplace messenger, social DM, SMS, overseas setting, banking app, map app, delivery app, etc., that context overrides the Korean everyday-messaging default.

Meaning-bearing chat text, room names, read-count numerals and animated/decrementing read-status effects should normally be vector/layout elements. The raster supplies the device, shell, blank UI zones and spatially correct geometry.

## 7. Art / text separation

Final page has three logical layers:

### A. ART
- character;
- background;
- prop;
- non-text visual effect;
- intentional space for typography.

Normally NO final readable narration/dialogue inside the raster art.

### B. VECTOR NARRATIVE
- hook/title;
- narration;
- speech bubble;
- bubble tail;
- reaction/inner thought;
- SFX;
- source note.

### C. LAYOUT METADATA
- safe margins;
- reading order;
- text boxes;
- focal point;
- crop anchor;
- source refs;
- continuity refs.

## 8. Text roles

Do not treat all copy as one centered sentence at the top.

Use three main storytelling roles:

### NARRATION / CAPTION
Use for:
- setup;
- time jump;
- brief context;
- storyteller voice.

Typical position:
- upper region or a deliberately reserved side region;
- not necessarily centered;
- one or two short lines.

### SPOKEN DIALOGUE
Use speech bubbles attached to the speaker.
The bubble belongs spatially to the character and beat.

Rules:
- short;
- low bubble count;
- tail clearly targets speaker;
- do not cover the main face/hand/prop;
- avoid giant balloons when narration would be cleaner.

### REACTION / INNER TEXT
Examples:
- “…?”
- “설마”
- “아 집 가고 싶다”
- small SFX/reaction marks.

Place near the expression/action it belongs to.
Do not turn every reaction into a full top caption.

## 9. Mobile typography baseline

These are operational starting points for 1080×1350, not immutable font laws.
Always check on an actual phone-size preview.

Starting range:
- cover/hook: 72–96 px;
- strong narration: 48–64 px;
- normal narration: 42–56 px;
- speech-bubble dialogue: 44–60 px;
- reaction/inner text: 34–46 px;
- source/credit note: 24–30 px.

Default horizontal safe margin:
- roughly 64–80 px minimum for important text;
- more when a swipe edge or composition is visually busy.

Rules:
- do not shrink critical text just to fit;
- shorten/split the copy instead;
- use short line lengths;
- preserve high contrast;
- phone readability outranks desktop elegance.

## 10. No-poster rule

A comic page must not accidentally become a generic poster/card because text was requested.

Hard warning signs:
- top 30–40% becomes blank by default;
- all copy is centered above a static scene;
- every slide uses the same title-above-illustration template;
- character action is pushed too low merely to make room for text.

Instead:
1. decide text role first;
2. reserve only the space that role needs;
3. compose the art around that actual region;
4. let bubbles/reactions live near the acting when appropriate.

## 11. Text density

Prefer:
- one dominant statement;
- short lines;
- one or two text objects;
- strong hierarchy.

If the copy requires tiny type:
- cut;
- rephrase;
- or split the beat.

Do not use long paragraph blocks in the comic.

## 12. Background / composition

Background supports place and action.
It should not become a lifestyle illustration.

Use:
- story-essential anchors;
- open visual breathing room;
- lower detail than characters.

Avoid:
- decorative filler;
- complex café equipment unless story-critical;
- atmospheric lighting;
- realistic material rendering.

## 13. Continuity modes

### NONE
Independent illustrative examples.

### LIGHT
Loose identity/prop continuity.

### STRICT_EPISODE
Chronological sequence with the same people/clothes/key props/location logic.

For STRICT_EPISODE:
- recurring main character uses main identity anchor;
- episode-only important character uses episode-local anchor;
- accepted prior frame may support pose/location continuity but does not replace the canonical style reference.

## 13.5 Sequence visual-direction preflight

Before raster generation, the visual director reviews the episode as one sequence and confirms:
- camera/framing choices are story-first rather than model-default;
- no obvious repeated face/camera orientation is being selected simply because it is the safest generation pose;
- expression amplitude matches each beat's function;
- mirror/reflection beats have a plausible camera/reflection plan;
- skin/local-color treatment remains coherent across main and supporting cast;
- materially different adjacent beats do not read as the same safe portrait with only an expression swap when a story-valid visual delta exists;
- the planned body language carries the same semantic meaning as the facial expression, rather than defaulting to a prettier/cuter reaction.

This is an optimization pass, not a direction quota.

## 14. Whole-episode preflight

Before production art:
1. story premise exists;
2. beat order is locked;
3. each slide has one job;
4. final landing comes after the reveal/peak, not before;
5. cast routing is explicit;
6. new 2+ cut episode character continuity requirement is identified;
7. each slide has text role(s);
8. text safe area is planned;
9. camera rhythm is intentional;
10. adjacent beats were reviewed for meaningful visual delta / merge;
11. every screen-bearing prop has one information owner and a physically valid screen/camera contract;
12. context-sensitive UI/platform profile is resolved where relevant;
13. output ratio is fixed;
14. high-risk hand/face/torso or prop-contact poses have a readable anatomy/occlusion plan;
15. any information overlay has a concrete semantic job and a planned visual state change rather than decorative filler.

## 15. Visual hard fails

Repair/reject when:
- main beat is ambiguous;
- wrong character is used;
- episode-only character changes face between cuts;
- slide order breaks causality;
- text is too small on phone;
- all text is treated as detached top narration;
- giant blank title area posterizes the page;
- text covers the main action;
- composition changes dramatically during a local repair;
- background detail/polish competes with characters;
- STYLE_LOCK is violated;
- perceptual directional bias across the set is obvious and comes from repeated default-like face/camera orientation rather than story need;
- a reaction/peak is materially flattened because anti-exaggeration was misread as anti-expression;
- a story-relevant mirror/reflection has visibly inconsistent face/limb geometry;
- a supporting character receives a visibly different yellow/sepia skin-color treatment without story justification;
- a screen appears on the back/wrong face of a device;
- character gaze, device face and camera view are physically incompatible;
- a private device is held in an unnatural audience-presentation pose only to expose UI;
- adjacent low-delta beats were split into repetitive slides without a defensible visual reason;
- a contextually resolved UI profile is ignored without story reason;
- a meaningful beat change is rendered as a near-duplicate safe portrait even though a story-valid camera/body/gaze alternative exists;
- the intended emotion is semantically replaced by a beautified/cute/cheerful or melodramatic default (for example, hollow resignation reads as delighted laughter);
- shoulder/torso/arm/hand continuity is visibly broken or hidden by an implausible garment/occlusion solution;
- an information overlay that owns a concrete story fact reads only as generic floating icons/data decoration and fails to communicate the declared state.

## 16. Change control

This grammar is versioned.
Material change requires prototype evidence + user approval.
