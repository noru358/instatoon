# GENERATION_PROTOCOL.md

# Generation & QC protocol — INSTATOON_STYLE_v1.0

This protocol exists to prevent style drift when scenes, tools, models, or automation change.

---

## 1. Required prompt architecture

For each panel/frame:

### A. Scene facts
Specify only:
- characters
- location
- action
- essential props
- expression
- camera

### B. Story clarity
State what the viewer must understand instantly.

### C. Reference / identity control
If references exist, attach:
- REFERENCE_OBEDIENCE_BLOCK
- IDENTITY_PRESERVATION_BLOCK

### D. Stable style
Append:
- MASTER_STYLE_PROMPT
- NEGATIVE_STYLE_PROMPT

Do not rewrite the full style from scratch for each panel.

---

## 2. Generation priority

Use this decision order:

1. recognizability of action / story beat
2. style-lock compliance
3. character identity consistency
4. scene continuity
5. anatomy plausibility
6. beauty / polish

Beauty is intentionally last. A more beautiful image that violates the style is worse.

---

## 3. First-pass QC

Immediately reject if:
- eyes are too large/detailed
- face is glamorous or sharp
- outline is thick/pure black
- hair is glossy/strand-heavy
- shading is conspicuous
- background competes with character
- image resembles generic romance webtoon/anime
- character identity is redesigned

Do not attempt to rescue a heavily drifted frame by stacking dozens of corrective clauses. Return to the canonical blocks and regenerate.

---

## 4. Second-pass QC

After style passes, check:
- hands and object contact
- limbs / occlusion
- feet / seating
- table/chair geometry
- door/window continuity
- object count
- clothing continuity
- hairstyle silhouette
- body scale
- panel-to-panel environment continuity

---

## 5. Repair strategy

### If style drift is global
Regenerate with the canonical style/reference blocks. Do not locally patch every symptom.

### If one object/anatomy detail is wrong
Use targeted edit while explicitly freezing all unmentioned areas.

### If identity drifts
Reassert the identity-preservation block and reduce decorative prompt language.

### If background overcomplicates
Delete rather than redesign. Low information density is a style requirement.

---

## 6. Minimal-change edit rule

When editing an accepted panel:

> Change only the explicitly named defect. Preserve all unmentioned composition, face, hair, clothing, palette, linework, and background geometry.

A successful correction must not introduce a new style interpretation.

---

## 7. Character-master workflow

Before high-volume production, each recurring character should receive:

1. canonical full-body neutral
2. canonical bust/face
3. front / 3/4 / side enough to stabilize silhouette
4. small expression set
5. outfit lock
6. hair lock
7. simplified identity notes
8. reference sheet approved against STYLE_LOCK

These become identity references, not new style authorities.

---

## 8. Environment-master workflow

For recurring locations:

1. canonical establishing panel
2. simplified object map
3. fixed high-salience anchors only
4. approved palette
5. optional alternate camera distances

Do not over-lock minor props if they are irrelevant to story continuity.

---

## 9. Automation rule

Future automation may generate:
- scripts
- panel beats
- scene descriptions
- shot lists
- prompt assembly
- QC checklists

But agents must treat STYLE_LOCK.md and MASTER_PROMPTS.md as read-only authoritative inputs unless explicitly instructed to propose a versioned style change.

No automatic performance-feedback loop may mutate the core style by itself.

---

## 10. Versioning

Any material style modification must:
- create a new style version
- update STYLE_LOCK.md
- update MASTER_PROMPTS.md
- update CURRENT_STATE.md
- record what changed and why

Never silently edit a locked prompt while keeping the same version.
