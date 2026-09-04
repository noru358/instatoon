# STYLE_LOCK.md

# INSTATOON_STYLE_v1.0 — AUTHORITATIVE VISUAL LOCK

**Status:** LOCKED  
**Effective:** 2026-09-04  
**Authority:** Highest visual authority in this repository.

This file defines the visual language for the project. Scene prompts, character prompts, tool defaults, model preferences, and future automation may not silently weaken these rules.

---

## 0. Target in one sentence

A warm Korean everyday anecdote-comic style using **thin softly imperfect charcoal-brown digital linework, simplified adult proportions, tiny understated facial features, broad near-black hair masses, warm muted pastel colors, almost-flat rendering, extremely restrained shading, quiet low-detail residential backgrounds, simple storytelling poses, and low visual density**.

This is deliberately **not** a polished romance-webtoon, anime, fashion illustration, 3D, or cinematic look.

---

## 1. Non-negotiable style DNA

The five highest-salience variables are:

1. **Face:** tiny eyes + minimal nose + tiny mouth + soft oval face.
2. **Line:** thin warm charcoal-brown, softly imperfect, never bold pure-black ink.
3. **Hair:** broad near-black graphic masses, almost no strand rendering or gloss.
4. **Palette:** warm ivory / peach / dusty wood / muted sage / warm gray / charcoal.
5. **Rendering density:** mostly flat color, nearly no shading, background quieter than character.

If any of these five drift, the generation is considered a style failure even if the image is otherwise attractive.

---

## 2. Linework lock

### Character line
- Thin, clean digital pen line with a slight hand-drawn irregularity.
- Dark warm charcoal-brown rather than #000000.
- Suggested visual range: approximately #3E3935–#554B45.
- Face/hair/outer contour: slightly stronger than clothing interiors.
- No dramatic pressure variation.
- No brush-ink character.
- No vector-perfect razor edges.

### Background line
- Noticeably lighter and thinner than character line.
- Warm beige-gray / taupe range.
- Suggested visual range: approximately #B8A897–#D0C1AF.
- Background line hierarchy must keep the person visually dominant.

### Forbidden
- thick black outlines
- manga ink
- heavy cel-animation contour
- comic-book brushwork
- highly variable calligraphic stroke width
- glossy/vector-polished contour

---

## 3. Face grammar lock

### Face shape
- Soft oval.
- Rounded jaw.
- Small rounded chin.
- No sharp V-line.
- No strong cheekbone modeling.
- Adult but gently simplified.

### Eyes
- Tiny simple dark ovals, dots, or short curved forms.
- No complex iris.
- No pupil/iris separation unless absolutely necessary.
- No glossy highlight.
- Almost no eyelashes.
- Eye size must remain small even in close-up.

### Brows
- Thin, short, understated.
- Emotion via angle, not detail.

### Nose
- Tiny mark, short minimal stroke, dot-like suggestion, or near omission.
- No bridge rendering.
- No realistic nostril structure.

### Mouth
- Very small curve, short line, tiny open oval, or simple smile.
- No detailed lips.
- No gloss.

### Blush
- Soft peach-pink cheek blush is allowed and often useful.
- Low opacity, diffused, small area.
- It should not become makeup rendering.

### Emotion
Emotion is conveyed primarily by:
- eyebrow angle
- mouth shape
- simple eye shape
- head tilt
- pose

Do not add facial rendering detail to increase emotion.

---

## 4. Hair lock

- Near-black charcoal, not blue-black anime gloss.
- Large clean silhouette masses.
- Minimal internal lines.
- Long hair falls in broad simple clumps.
- Softly tapered ends, not dozens of sharp strands.
- No luminous highlight band.
- No strand-by-strand rendering.
- No windswept or highly stylized anime motion unless required by the scene, and even then the silhouette remains simple.

---

## 5. Body proportion lock

Adult characters should read as approximately **6–6.5 heads tall**.

Typical female silhouette:
- slightly oversized head
- narrow/modest shoulders
- slim limbs
- small hands
- understated torso
- no exaggerated bust, waist, hips

Typical male silhouette:
- modestly broader shoulder than female
- simple straight torso
- no muscular rendering

Overall:
- human and adult
- simplified rather than chibi
- not fashion-model elongated
- not heroic/anime-proportioned

---

## 6. Hands and anatomy

- Hands are simplified storytelling shapes.
- Fingers may be grouped or minimally separated.
- Avoid hyper-realistic knuckle/nail/tendon detail.
- Anatomy should be readable and plausible, but not rendered for display.
- "Perfect anatomy" is not the target; clear, calm, low-detail storytelling is.

---

## 7. Clothing lock

- Flat simplified silhouette.
- Very few folds.
- Only lines needed to identify collar, sleeve, hem, waistband, or one major bend.
- No cloth texture.
- No material gloss.
- No fashion-illustration embellishment.
- White clothing should usually be warm off-white/cream, not pure digital white.

Typical dark pants: charcoal rather than absolute black.

---

## 8. Color palette lock

Primary family:
- creamy ivory
- warm off-white
- pale peach beige
- dusty salmon
- muted warm wood
- muted sage green
- pale desaturated blue
- warm gray
- charcoal

Approximate useful ranges from the reference analysis:
- background ivory: #F7EFE6
- warm cream: #F3E4D8
- peach interior tone: #ECCAB2
- warm taupe: #D0C2AF
- skin: #F1D9C7 / #F3DCCB
- wood: #D7B89C / #C7A68E
- muted sage: #909B79 / #A0A889
- dark clothing/hair accents: #292A29–#343331

These values are guides, not a mandatory indexed palette. The mandatory quality is **warm + muted + low saturation + low contrast**.

Avoid:
- neon
- jewel-tone saturation
- cool cyber palettes
- high-contrast complementary schemes
- pure white / pure black overuse

---

## 9. Rendering and light lock

Rendering should be:
- mostly flat
- matte
- restrained
- low-contrast

Per major form:
- zero or one faint soft shadow region is enough.

Faces:
- almost no modeled light.
- no nose shadow.
- at most a very faint chin/neck separation.

Objects:
- faint contact shadow is allowed.

Forbidden:
- cinematic lighting
- rim light
- volumetric light
- glossy highlight
- hard cel shadow
- dramatic directional lighting
- photorealistic ambient occlusion
- highly modeled skin

---

## 10. Skin lock

Skin is primarily a single warm peach plane.

Do not render:
- pores
- oily shine
- nose highlight
- realistic lip color
- tear duct
- detailed ear anatomy
- skin gradient modeling

The cheek blush may be the most visible tonal variation on the face.

---

## 11. Background lock

Target environments:
- everyday Korean residential or ordinary urban interiors/exteriors
- calm, familiar, low-stakes places
- home, alley, cafe, low-rise residential street, simple office, shop, park, etc.

Background object vocabulary is simplified:
- windows
- doors
- tables
- shelves
- sofas/chairs
- books
- potted plants
- bicycles
- simple kitchen or household items

Every prop should read quickly with minimal internal information.

Do not render:
- material micro-texture
- clutter for its own sake
- highly detailed decor
- photorealistic architecture
- complex signage unless story-critical

---

## 12. Perspective lock

- Eye-level by default.
- Straight-on or mild 3/4.
- Simplified hand-drawn perspective.
- Plausible, but not architectural/CAD-perfect.
- Slight flatness is desirable.
- No fisheye.
- No dramatic lens distortion.
- No extreme foreshortening unless narratively essential.

---

## 13. Composition lock

Preferred:
- medium shot
- medium-full shot
- chest-up
- occasional restrained close-up
- simple two-person or small-group staging
- comfortable negative space
- clean silhouette
- obvious action/readability

Avoid:
- cinematic framing for spectacle
- extreme Dutch angle
- dramatic low angle
- busy overlapping bodies
- composition whose primary goal is "coolness" rather than story clarity

---

## 14. Pose and acting lock

- Simple, readable storytelling gesture.
- Often only one or two limbs carry the action.
- Body can remain relatively calm.
- Facial and gestural clarity matter more than anatomical flourish.
- Do not request "dynamic anime pose."

The style can support surprise, discomfort, laughter, embarrassment, or frustration, but all are expressed using simple graphic changes rather than extra rendering.

---

## 15. Visual-density lock

The target is **consistent low-detail narrative illustration**, not "low quality."

Use:
- intentionally simple
- restrained
- modest
- low visual density
- clean
- readable

Do not optimize for:
- more detail
- more polish
- more realism
- more lighting
- more texture
- more decoration

A model-generated "upgrade" in those dimensions is usually a regression.

---

## 16. Absolute negative style set

Reject generations containing meaningful drift toward:

- anime
- manga rendering
- polished Korean romance-webtoon style
- glamorous character design
- large sparkling eyes
- detailed irises
- eye highlights
- long eyelashes
- sharp V-shaped jaw
- realistic nose/lips
- glossy skin
- detailed hair strands
- glossy anime hair
- photorealism
- semi-realistic rendering
- 3D / CGI
- painterly rendering
- strong watercolor texture
- thick black outlines
- brush-ink lines
- dramatic cel shading
- hard shadows
- cinematic lighting
- rim lighting
- volumetric light
- depth of field / bokeh
- high saturation
- high contrast
- hyper-detailed backgrounds
- complex furniture rendering
- detailed fabric texture
- excessive clothing folds
- fashion-illustration proportions
- muscular anatomy
- exaggerated body curves
- perfect architectural rendering
- visual clutter
- over-polishing

---

## 17. Hierarchy rule for generation

When composing a generation request:

**Content/scene may vary. Style may not.**

Scene-specific instructions may specify:
- person
- action
- object
- location
- composition
- expression

They may not silently redefine:
- line
- face grammar
- hair rendering
- palette
- shading
- anatomy style
- visual density

---

## 18. Identity-preservation rule

When adapting an existing character into this style:
- preserve hair silhouette, length, part
- preserve clothing design/color
- preserve age/gender presentation
- preserve characteristic eye shape within the tiny-eye grammar
- preserve recognizable silhouette
- simplify; do not redesign

"Style transfer" must not become "character redesign."

---

## 19. QC hard-fail conditions

A frame fails style QC if any major hard-fail is present:

1. Eyes visibly become anime/webtoon eyes.
2. Pure-black thick outline dominates.
3. Hair gains glossy strand-heavy rendering.
4. Face becomes sharp/V-line/glamorous.
5. Shading becomes multi-step/cinematic.
6. Background becomes more detailed or contrasty than the person.
7. Clothing develops fashion-rendered folds/materials.
8. Image reads as 3D, semi-realistic, romance-webtoon, or anime.
9. Saturation/contrast rises substantially.
10. Scene generation redesigns a locked character.

A "prettier" fail remains a fail.

---

## 20. Change-control rule

Do not edit the locked style based on one generation's convenience.

A style change requires:
1. explicit proposed change,
2. A/B examples,
3. evaluation against reference intent,
4. explicit approval,
5. version bump.

No silent mutation.
