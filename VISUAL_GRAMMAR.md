# VISUAL_GRAMMAR.md

# INSTATOON_VISUAL_GRAMMAR_v0.1 — AUTHORITATIVE SEQUENTIAL / LAYOUT LOCK

**Status:** LOCKED BASELINE  
**Effective:** 2026-09-04  
**Scope:** episode-level visual grammar, slide/page grammar, lettering/layout behavior  
**Art-style authority:** `STYLE_LOCK.md`

This file defines **how an Instagram-toon episode reads**, while `STYLE_LOCK.md` defines **how the illustration looks**.

The project does **not** depend on recurring-character identity. The recurring identity is the **overall drawing language and page grammar**.

---

## 0. Core principle

> Plan the entire episode first. Render individual slides only after the full narrative and visual plan is coherent.

No slide is planned in isolation.

A slide exists because it has a specific cognitive/narrative job inside the full sequence.

---

## 1. Primary identity

The project identity is:

1. the locked illustration style in `STYLE_LOCK.md`;
2. the recurring page rhythm and layout language in this file;
3. the editorial voice / topic selection;
4. consistent vector lettering and graphic treatment.

Recurring characters may appear, but they are optional content elements rather than the main brand lock.

Episode-specific characters may be one-off, anonymous, symbolic, or omitted entirely.

---

## 2. Default canvas

Canonical feed master:
- 1080 × 1350 px
- 4:5 portrait

The renderer must keep important art and all vector text away from vulnerable outer edges.

A platform-specific export may be derived later, but the Instagram-toon project itself does not depend on a video workflow.

---

## 3. Episode grammar

Default episode length:
- 5–9 slides
- 6–8 is the normal target
- shorter is preferred when the idea lands cleanly

The system must not pad an idea to reach a slide count.

Each slide must have **one primary cognitive beat**.

Allowed secondary detail:
- one supporting reaction;
- one supporting visual cue;
- one short subordinate line.

If a slide carries two independent ideas, split it.

---

## 4. Cover grammar

Slide 1 is a **cover/hook**, not an executive summary.

It should:
- state or imply one tension, question, surprise, contradiction, or emotionally recognizable situation;
- leave a meaningful gap that slide 2 can answer or complicate;
- use one dominant visual focal point;
- remain readable at feed-thumbnail size.

Default:
- one short title/hook;
- one dominant illustration or graphic;
- minimal explanatory copy.

Avoid:
- full summary;
- dense context;
- multiple claims;
- decorative clutter;
- table-of-contents behavior.

---

## 5. Middle-slide grammar

Slides 2 through the penultimate slide form the body.

Every slide must perform one of these functions:

- `ESTABLISH` — situation / baseline
- `TRIGGER` — event that changes the state
- `DEVELOP` — one step of escalation or explanation
- `EXAMPLE` — concrete instance
- `COMPARE` — A/B or before/after
- `CAUSE` — mechanism / why
- `REACTION` — emotional or human consequence
- `TURN` — reframe / unexpected interpretation
- `METAPHOR` — visual analogy
- `PROOF` — source-derived fact, quote, number, or concrete evidence
- `BRIDGE` — minimal connection only when essential

A slide with no distinct function is filler and must be removed.

---

## 6. Landing grammar

The last slide must **land** the idea.

Possible landing types:
- punchline;
- reframe;
- emotional residue;
- concise takeaway;
- memorable quote;
- unresolved human question.

A generic CTA is optional and subordinate.

Do not force:
- “팔로우 해주세요”
- “저장해두세요”
- generic moral lesson
- AI-written inspirational summary

if it weakens the content.

---

## 7. v0.1 active narrative formats

v0.1 deliberately supports only two production formats.

Detailed editorial grammar is authoritative in `STORY_GRAMMAR.md`.

### A. STORY_ARC — anecdote / experience / incident

Use when temporal progression matters and the reader's main question is “what happened next?”

Every body slide must change the state.

### B. RELATABLE_SCENARIO — dramatized everyday recognition

Use when the payoff is “I do this too / I know this situation.”

The default is a mini-scenario, not a traits list or card-news collection.

### Future / dormant
- OBSERVATION_SET
- EXPLAINER_CAUSAL
- CONTRAST_REFRAME

Do not route v0.1 production into dormant formats merely because the source can be explained that way.

---

## 8. Source is orthogonal to format

Source type is metadata, not a narrative format.

Possible sources:
- personal observation
- community post / comments
- news / public data
- trend
- user-submitted story
- interview
- original idea

A community thread may route to any of the four narrative formats.

Therefore `COMMUNITY_REMIX` is an **ingestion/adaptation mode**, not a visual format.

---

## 9. Page archetypes

The Visual Director selects one primary page archetype per slide.

- `HERO_SCENE` — one large illustrative scene
- `REACTION_CLOSEUP` — expression / reaction dominates
- `TWO_SHOT` — simple interaction
- `OBJECT_FOCUS` — prop or detail carries the beat
- `SPLIT_COMPARE` — A/B comparison
- `BEFORE_AFTER` — temporal/state comparison
- `SEQUENCE_WITHIN_SLIDE` — 2–3 mini-beats only when needed
- `DIAGRAM` — simple causal/process relation
- `METAPHOR` — visual analogy
- `TEXT_LED` — typography is primary, art is secondary
- `QUOTE_LED` — one human/source line is primary
- `EMPTY_BEAT` — restrained pause / silence / minimal image

Default is one dominant composition per slide.

Do not subdivide a slide into many small panels by habit. Research on Instatoon visual direction found that excessive subdivision and too many characters reduce readability; simplicity and clarity are core platform strengths.

---

## 10. Render-mode grammar

The slide planner chooses the cheapest mode that serves the beat:

### `RASTER_FULL`
Full illustration generated as one flattened art scene.
Use for story scenes, interactions, locations, metaphor scenes.

### `RASTER_PLUS_VECTOR`
Generated illustration plus vector narration/dialogue/labels.
This is the default illustrated mode.

### `VECTOR_PLUS_SPOT_ART`
Mostly deterministic vector layout with one or two small illustrations/icons.
Use for explanatory or comparison pages.

### `VECTOR_ONLY`
No paid image generation.
Use for simple diagram, quote, list, number, or typographic impact when illustration adds little.

The system should not pay for a full illustration merely because every slide “should have a picture.”

---

## 11. Layer lock

Final page composition is separated into three logical layers.

### A. ART LAYER — raster
- generated scene
- character(s), if needed
- background
- props
- non-text visual effect
- NO readable dialogue
- NO baked-in speech bubbles
- NO baked-in captions
- NO critical labels

The art generator should intentionally leave required negative space.

### B. VECTOR NARRATIVE LAYER
- title
- narration
- dialogue
- speech bubbles and tails
- labels
- arrows
- dividers
- emphasis marks
- SFX
- source note / small attribution where required

All important text is deterministic and editable.

### C. LAYOUT / METADATA LAYER
- safe zones
- reading order
- bounding boxes
- focal point
- crop anchors
- source provenance
- semantic element IDs
- QC measurements

---

## 12. Text grammar

Text must be written for phone reading.

Rules:
- one dominant statement per slide;
- short lines;
- avoid long paragraph blocks;
- vector text must have a deliberate hierarchy: hook/title > spoken/narrative text > note/source;
- dialogue bubble count should stay low;
- narration may replace dialogue when that is clearer;
- do not manufacture dialogue merely to justify illustrated characters.

Text is a storytelling layer, not decoration.

---

## 13. Character policy

No recurring-character requirement.

For each episode, people may be:
- absent;
- one-off;
- generic;
- symbolic;
- repeated only within the current story;
- reused across episodes if editorially useful.

When one person must persist across multiple slides, create an **episode-local continuity anchor**:
- age/presentation;
- hair silhouette;
- clothing;
- one or two recognizable traits.

This anchor exists only to keep the current story readable. It is not a brand identity lock.

---

## 14. Background and continuity policy

Continuity level is selected at episode level:

- `NONE` — independent illustrative pages
- `LIGHT` — same broad person/object vocabulary, loose environment consistency
- `STRICT_EPISODE` — chronological story requiring same people, clothes, key props, and location logic

Do not enforce strict continuity on observation/explainer posts that benefit from varied examples.

---

## 15. Variety rule

Consistency does not mean identical composition.

Across an episode, avoid:
- 6 identical medium shots;
- repeated centered person + bubble;
- same camera distance on every slide;
- same left/right blocking on every slide.

Prefer deliberate rhythm:
- wide → medium → detail
- scene → graphic → scene
- calm → dense → calm
- literal → metaphor → landing

Variation serves comprehension, not spectacle.

---

## 16. Simplicity / clarity lock

External research on Instatoon visual direction repeatedly identifies simplicity and clarity as core strengths:
- simplified figures/backgrounds;
- restrained visual elements;
- regular readable layout;
- low clutter;
- clear typography;
- simple popular subjects.

This aligns with `STYLE_LOCK.md`.

Therefore:
- every decorative element must justify its existence;
- background is quieter than story action;
- typography must remain legible;
- avoid over-partitioning;
- reduce rather than add when uncertain.

---

## 17. Whole-episode preflight

Before the first paid image render, the full plan must pass:

1. one-sentence topic exists;
2. one-sentence angle exists;
3. format classification is justified;
4. every slide has exactly one primary job;
5. hook promises something the body actually delivers;
6. the landing resolves/reframes the same topic;
7. no filler slides;
8. visual archetypes vary intentionally;
9. render mode is cost-appropriate;
10. vector-text plan is complete;
11. episode continuity mode is explicit;
12. all factual/source claims have provenance when required.

Only after this gate may rendering begin.

---

## 18. Cost-aware render preflight

Even after a full plan is approved, do not immediately spend on every raster slide.

Default:
1. render the cover;
2. render one representative body slide with the highest style/scene risk;
3. check global style compatibility;
4. if both pass, render remaining raster slides.

This is a **render preflight**, not slide-by-slide planning.

The episode remains the planning unit.

---

## 19. Visual QC hard fails

Reject or repair if:
- `STYLE_LOCK.md` is violated;
- generated text appears in the raster art where vector text should go;
- a slide’s main beat is not instantly legible;
- art leaves no viable space for planned text;
- visual hierarchy has two competing focal points;
- background clutter competes with the subject;
- a multi-panel subdivision is harder to read than a single scene;
- continuity breaks in a `STRICT_EPISODE` sequence;
- the rendered page changes the planned narrative function.

---

## 20. Change control

This grammar is versioned.

Changes require:
1. explicit proposed rule;
2. prototype evidence;
3. comparison against existing grammar;
4. explicit approval;
5. version bump.

Performance data may inform experiments but may not silently mutate the grammar.
