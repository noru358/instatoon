# REFERENCE_ANALYSIS.md

# Detailed visual deconstruction underlying INSTATOON_STYLE_v1.2

This file explains **why** the lock is written the way it is. It is descriptive evidence, not a looser substitute for STYLE_LOCK.md.

---

## 1. Overall visual category

The reference is best described as a **warm, low-density Korean everyday anecdote illustration comic**.

It is not accurately captured by generic labels such as:
- "pastel webtoon"
- "Korean webtoon"
- "anime"
- "watercolor comic"

Those labels are too broad and usually cause model drift.

The reference deliberately trades spectacle for:
- readability
- familiarity
- warmth
- repeatability
- narrative clarity
- easy panel-to-panel consistency

---

## 2. Line anatomy

The character line is:
- thin
- dark warm gray/brown
- clean but not vector-perfect
- only mildly irregular
- relatively uniform

The background line is:
- lighter
- thinner
- lower contrast
- warmer

This creates a quiet depth hierarchy without cinematic blur or realistic lighting.

---

## 3. Face anatomy

The face is one of the strongest identifiers of the style.

### Shape
- short-to-medium soft oval
- rounded lower cheek
- rounded jaw/chin
- no strong V-line

### Eye
- tiny
- dark
- simple oval/dot/short curved form
- minimal internal anatomy

### Nose
- nearly absent

### Mouth
- very small and symbolic

### Blush
- soft peach/pink circles or diffused patches

The result is adult, friendly, and non-glamorous.

---

## 4. Hair anatomy

Hair is treated as graphic mass rather than texture:
- near-black
- broad silhouette
- few internal separations
- very limited highlights
- ends grouped into a few clumps

This matters because common generative defaults over-render hair and immediately shift the style toward anime or polished webtoon.

---

## 5. Human proportion

The figures are neither chibi nor fashion illustration.

Approximate reading:
- about 6–6.5 heads tall
- slightly enlarged head
- modest shoulder width
- slim limbs
- small hands
- minimal torso modeling

The style retains adult recognizability while removing anatomical spectacle.

---

## 6. Clothing

Clothing communicates category before fabric:
- blouse
- slacks
- jacket
- turtleneck
- etc.

Folds are few.
Material texture is nearly absent.
The eye reads silhouette and color first.

---

## 7. Color behavior

The palette is warm and desaturated.

Common visual families:
- cream
- ivory
- peach
- salmon
- dusty beige
- pale wood
- sage
- muted blue
- charcoal

White is normally warmed.
Black is normally softened toward charcoal.

The palette produces a calm domestic/social tone and prevents the character from reading as anime merchandise art.

---

## 8. Shading behavior

Shading is close to absent.

When present:
- broad
- soft
- faint
- one-step

The reference does not depend on light-source realism.
It depends on line + flat shape + sparse contact/shadow cues.

---

## 9. Background behavior

Backgrounds are narratively sufficient, not descriptively complete.

An interior may need only:
- a sofa
- a plant
- a window
- a table
- a shelf/books

An exterior may need only:
- a low-rise building
- door/window
- balcony
- bicycle
- a few plants

Props are icon-like.
Fine material and structural details are omitted.

---

## 10. Perspective

Perspective is plausible but gently flattened.

The hand-drawn feeling benefits from:
- simplified geometry
- minor non-mechanical irregularity
- no architectural obsession

Perfect 3D construction would make the result colder and stylistically wrong.

---

## 11. Acting

Expressions are graphic and economical.

Surprise:
- slightly enlarged/simple eyes
- tiny O mouth
- raised brows

Embarrassment:
- tilted brows
- blush
- slight head tilt

Smile:
- curved eyes or normal tiny eyes
- tiny upward mouth

Complex emotion is created by combining a few small symbolic shifts.

---

## 12. Composition

The reference uses conventional story-panel framing:
- eye level
- medium / medium-full
- occasional closer portrait
- generous empty space
- straightforward blocking

The camera is not a character.
Its job is to let the anecdote read immediately.

---

## 13. Intentional non-polish

The style should not be described to a model as merely "low quality."
That risks artifacts.

The useful concepts are:
- intentionally simple
- modest drawing quality
- restrained
- low visual density
- clean
- consistent
- no beautification

The target is **controlled simplicity**, not technical failure.

---

## 14. Common generative failure modes

### Failure A — generic GPT webtoon face
Symptoms:
- larger eyes
- more detailed nose/lips
- prettier face shape
- smooth glossy finish

### Failure B — anime hair
Symptoms:
- many strands
- bright highlight band
- spiky ends
- blue-black shine

### Failure C — over-rendered environment
Symptoms:
- texture-rich furniture
- lighting effects
- too many props
- exact architecture

### Failure D — over-shading
Symptoms:
- cheek/nose modeling
- multi-step cel shadow
- rim light
- realistic cast shadows

### Failure E — fashion illustration
Symptoms:
- longer legs
- tiny waist
- stylized pose
- elaborate folds

All five are hard style regressions.


---

## 15. Empirical reproduction test — 2026-09-04

A single supplied character was translated into the target style across five conditions:

1. character portrait;
2. full-body;
3. two-person interaction;
4. indoor seated scene;
5. outdoor full-body scene.

### Result

Tests 1–4 were visually accepted as one coherent style family.

The initial outdoor test showed a distinct drift:
- the face became more conventionally attractive / generic AI-webtoon-like;
- the eyes were reinterpreted for off-axis gaze;
- facial construction became more polished;
- hair/face styling became slightly more model-default;
- the environment carried more architectural/object detail.

### Root cause

The combination of:
- full-body camera distance,
- environment-heavy outdoor scene,
- and side gaze

reduced the influence of the tiny-face grammar and allowed the generator's generic "cute Korean woman illustration" prior to fill the small face.

This was not primarily a palette failure.

### Corrective hypothesis

Two independent controls were added:

1. **FACE LOCK** — preserve the same tiny solid-dark eye / rounded-face grammar at every distance and express gaze mainly with head orientation.
2. **BACKGROUND DENSITY LOCK** — simplify environment detail as scene complexity rises so the visual budget does not shift toward generic polished illustration.

### Validation

The outdoor scene was regenerated with those controls and the approved references. The corrected result was explicitly accepted.

Therefore this is now an empirical production rule:

> **Farther character = simpler face, never more generic/detail-rich face.**

and:

> **As environment complexity rises, incidental background density should fall.**

The five accepted outputs are the canonical reproduction-test set defined in `REFERENCE_SET.md`.
