# GENERATION_PROTOCOL.md

# Generation & QC protocol — INSTATOON_STYLE_v1.0 / VISUAL_GRAMMAR_v0.1

This protocol prevents style drift, page-grammar drift, and wasteful generation.

---

## 1. Whole-episode planning comes first

Before generating any slide, create the complete episode plan.

Required:
- topic;
- angle;
- narrative format;
- slide count;
- role/beat of every slide;
- whole-episode visual rhythm;
- page archetype per slide;
- render mode per slide;
- all planned text objects;
- negative-space requirements;
- continuity mode;
- provenance for factual/quoted material.

A slide may not be independently invented after rendering begins unless the whole plan is explicitly revised.

---

## 2. Required prompt architecture for raster slides

### A. Scene facts
Specify only:
- who/what is present;
- location;
- action;
- essential props;
- expression if relevant;
- camera/composition;
- required negative space.

### B. Story clarity
State the one beat the viewer must understand instantly.

### C. Episode-local continuity
Use only when the current episode requires the same person/object/location across slides.

This is not a recurring-character brand lock.

### D. Stable style
Append:
- REFERENCE_OBEDIENCE_BLOCK if applicable;
- IDENTITY_PRESERVATION_BLOCK only when a specific existing person/character must be preserved;
- MASTER_STYLE_PROMPT;
- NEGATIVE_STYLE_PROMPT.

Do not rewrite the full style from scratch for each slide.

---

## 3. Raster-art rule

Generated raster art should contain:
- illustration;
- subjects;
- props;
- background;
- non-text effects.

It should **not** contain:
- important readable dialogue;
- baked-in captions;
- critical labels;
- final speech bubbles;
- final SFX text.

Leave intentional space for the separate vector narrative layer.

---

## 4. Render-mode decision

Before each slide reaches the renderer, choose:

- `RASTER_FULL`
- `RASTER_PLUS_VECTOR`
- `VECTOR_PLUS_SPOT_ART`
- `VECTOR_ONLY`

Use the cheapest mode that communicates the beat clearly.

Do not create a full paid illustration merely for visual completeness.

---

## 5. Generation priority

Use this decision order:

1. story-beat recognizability;
2. style-lock compliance;
3. visual-grammar compliance;
4. planned negative space;
5. episode continuity when required;
6. anatomy / object plausibility;
7. beauty / polish.

Beauty remains last.

---

## 6. Two-slide render preflight

The entire episode is planned first.

Then, before bulk paid generation:

1. render the cover;
2. render one representative body slide with the highest visual risk;
3. QC both.

If they show the same systematic style/grammar failure:
- STOP;
- fix the common prompt/reference/system issue;
- do not spend on the rest of the episode.

This is a cost gate, not slide-by-slide planning.

---

## 7. First-pass render policy

After preflight passes:
- generate each planned raster slide once;
- compose vector text separately;
- do not auto-regenerate cosmetic differences.

Default regeneration budget:
- up to 2 additional paid generations per episode before human review.

Prefer targeted edit over full regeneration.

---

## 8. First-pass QC — style and grammar

Immediately reject or repair if:
- eyes are too large/detailed;
- face becomes glamorous or sharp;
- outline becomes thick/pure black;
- hair becomes glossy/strand-heavy;
- shading becomes conspicuous;
- background competes with the story subject;
- image resembles generic romance webtoon/anime;
- saturation/contrast rises materially;
- planned negative space disappears;
- page contains accidental generated text;
- the main beat is visually ambiguous;
- a slide is subdivided more than necessary;
- two visual focal points compete;
- the rendered composition no longer serves the planned slide role.

---

## 9. Second-pass QC — defects / continuity

After style and grammar pass, check:
- hands and object contact;
- limbs / occlusion;
- feet / seating if relevant;
- table/chair/object geometry;
- object count;
- episode-local clothing/hair continuity when required;
- body scale;
- spatial logic;
- location continuity in STRICT_EPISODE mode.

Do not enforce strict continuity when the format intentionally uses independent examples.

---

## 10. Vector-layer QC

Check deterministically where possible:
- text overflow;
- clipping;
- safe margins;
- line breaks;
- reading order;
- bubble-tail target;
- label association;
- title hierarchy;
- contrast;
- source-note placement.

All important wording must remain editable without regenerating art.

---

## 11. Repair strategy

### If global style drift appears
Stop the batch and fix canonical reference/prompt assembly.

### If one slide has a local defect
Target-edit that slide while freezing accepted areas.

### If a slide lacks text space
First consider vector/layout repositioning.
If impossible, targeted art edit/regeneration may be required.

### If the story itself is weak
Return to angle / swipe script / visual plan.

Do **not** ask an automated QC agent to “make it more engaging” by rewriting the whole episode.

---

## 12. Episode-local person continuity

Recurring character masters are optional, not required.

If a chronological story needs the same person across several slides:
- create a compact temporary continuity note;
- preserve hair silhouette, clothing, age/presentation, and one or two salient traits;
- reuse an accepted slide as a temporary reference if helpful;
- discard the requirement after the episode unless the character later becomes intentionally recurring.

The project identity remains the overall style and page grammar.

---

## 13. Environment continuity

For recurring locations within a chronological episode:
- preserve only story-relevant anchors;
- do not lock irrelevant props;
- keep backgrounds low-detail;
- prefer continuity of spatial logic over exact decorative replication.

---

## 14. Minimal-change edit rule

When editing an accepted slide:

> Change only the explicitly named defect. Preserve all unmentioned composition, style, palette, linework, narrative function, and accepted geometry.

A successful correction must not introduce a new style interpretation.

---

## 15. Automation rule

Automation may generate:
- source normalization;
- candidate angles;
- format routing;
- whole-episode swipe scripts;
- whole-episode visual plans;
- page specs;
- prompt assembly;
- vector layout;
- QC reports;
- render manifests.

Automation may not silently change:
- `STYLE_LOCK.md`;
- `VISUAL_GRAMMAR.md`;
- approved episode angle;
- approved whole-episode structure.

No performance-feedback loop may mutate the core style/grammar by itself.

---

## 16. Versioning

Material art-style changes:
- version `STYLE_LOCK.md`.

Material sequential/layout-grammar changes:
- version `VISUAL_GRAMMAR.md`.

Update:
- canonical prompts if needed;
- current state;
- rationale / test evidence.

Never silently mutate a locked standard.
