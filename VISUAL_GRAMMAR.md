# VISUAL_GRAMMAR.md

# INSTATOON_VISUAL_GRAMMAR_v0.2 — SEQUENCE / COMPOSITION / LETTERING
Updated: 2026-09-04

STYLE authority: STYLE_LOCK.md / MASTER_PROMPTS.md
CONTENT authority: SOURCE_STORY_PIPELINE.md

## 0. Core principle

Plan the entire episode first.
Render individual slides only after the sequence, cast, text roles, and visual rhythm are coherent.

A slide exists because it performs one story job.

## 1. Canvas / distribution

Primary feed/carousel master:
- 1080 × 1350
- 4:5 portrait

Vertical derivative:
- 1080 × 1920
- 9:16 Reels/Shorts

16:9 is not the default.

All slides within one carousel should share one ratio.

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
- SEQUENCE_WITHIN_SLIDE (only when 2–3 mini-beats truly belong together)

Default is one dominant composition.
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

## 6. Cast visibility

Story/context decides who appears.

Main cast may recur when appropriate.
Episode-only characters are valid and common.

If an episode-only character appears in 2+ cuts, GENERATION_PROTOCOL requires a character anchor before production frames.

Do not substitute a familiar main character just to solve continuity cheaply.

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

## 14. Whole-episode preflight

Before production art:
1. story premise exists;
2. beat order is locked;
3. each slide has one job;
4. final landing comes after the reveal/peak, not before;
5. cast routing is explicit;
6. new 2+ cut episode character anchor requirement is identified;
7. each slide has text role(s);
8. text safe area is planned;
9. camera rhythm is intentional;
10. output ratio is fixed.

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
- STYLE_LOCK is violated.

## 16. Change control

This grammar is versioned.
Material change requires prototype evidence + user approval.
