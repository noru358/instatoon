# MASTER_PROMPTS.md

# Canonical prompt blocks — INSTATOON_STYLE_v1.2

These blocks implement [STYLE_LOCK.md](STYLE_LOCK.md).  
Do not rewrite them casually per scene. Prefer composition by appending scene content around stable blocks.

---

## 1. MASTER_STYLE_PROMPT

```text
Match the attached canonical INSTATOON style reference as the primary rendering authority.
Do not infer the style from generic category labels such as Korean webtoon, anime, slice-of-life illustration, editorial illustration, or cozy comic.

STYLE LOCK:
Use thin, softly imperfect hand-drawn digital linework, not bold ink.
Character outlines are dark warm charcoal-brown rather than pure black.
Background outlines are significantly thinner, lighter, and lower contrast.

Characters have simplified adult proportions, approximately 6 to 6.5 heads tall, with slightly oversized heads, narrow shoulders, slender limbs, small hands, and understated body shapes.
Do not exaggerate the chest, hips, muscles, or fashion-model proportions.

Faces are extremely simple and understated:
soft oval faces, rounded jawlines, small rounded chins,
tiny simple solid-dark oval/dot eyes,
ordinary eyes are NOT constructed as white sclera with separate black pupils,
no detailed irises,
no eye highlights,
almost no eyelashes,
thin short eyebrows,
a tiny minimal nose or nearly invisible nose,
and a very small curved mouth or small oval mouth.
Use subtle soft peach-pink blush on both cheeks.
Facial emotion should be communicated mainly through eyebrow angle, mouth shape, head tilt, and simple eye shape rather than facial detail.

Hair is rendered as a few large, clean, flat near-black charcoal shapes.
Minimal internal hair lines.
No hatch texture, pencil texture, scratch texture, or tonal scribbling in the hair.
No individual strand rendering.
No shiny anime highlights.
Long hair should fall in broad simple clumps with softly tapered ends.

Clothing is simplified into clean flat silhouettes.
Use very few fabric folds.
No textile texture.
No glossy material rendering.
Use only minimal lines necessary to identify collars, sleeves, hems and major folds.

COLOR:
Use a warm, muted pastel palette dominated by creamy ivory, warm off-white, pale peach beige, dusty salmon, light warm wood, muted sage green, pale desaturated blue and charcoal gray.
Avoid highly saturated colors.
White objects should usually be warm creamy off-white rather than pure white.

RENDERING:
Clean flat digital color fills.
No global paper/canvas texture.
No watercolor wash, pencil shading, crosshatching, stippling, or grain.
Mostly flat colors.
Extremely restrained shading.
At most one faint soft shadow region on each major form.
No dramatic shading.
No hard cel shadows.
No glossy highlights.
No realistic light simulation.
Skin is a clean flat warm peach tone with almost no texture.

BACKGROUND:
Quiet everyday Korean residential or ordinary urban environments.
Background objects are reduced to simple readable shapes: windows, tables, shelves, sofas, potted plants, books, doors and ordinary household objects.
Keep the environment low-detail and uncluttered.
In a shop/convenience-store scene, simplify merchandise into a few colored blocks; do not render rows of individual labels/packages.
Background lines and colors must be softer and lighter than the characters.
Use simplified hand-drawn perspective rather than mathematically perfect architectural perspective.

COMPOSITION:
Clear narrative storytelling composition.
Eye-level camera.
Mostly straight-on or mild three-quarter views.
Medium shots, medium-full shots, and occasional simple close-ups.
No dramatic lens distortion.
Leave comfortable negative space around the characters.
Use simple readable poses and gestures.

OVERALL FEEL:
gentle, ordinary, warm, understated, slightly naive but clean,
like a calm Korean everyday anecdote comic,
intentionally low visual density,
modest and restrained rather than polished or glamorous,
consistent simple illustration language across characters, props and backgrounds.
```

---

## 2. NEGATIVE_STYLE_PROMPT

```text
NO anime style,
NO manga rendering,
NO polished romance webtoon style,
NO glamorous character design,
NO large eyes,
NO sparkling eyes,
NO detailed irises,
NO eye highlights,
NO long eyelashes,
NO sharp V-line face,
NO detailed nose,
NO realistic lips,
NO glossy lips,
NO shiny skin,
NO detailed hair strands,
NO glossy anime hair,
NO elaborate hairstyles,
NO photorealism,
NO semi-realistic rendering,
NO 3D,
NO CGI,
NO painterly rendering,
NO oil painting,
NO watercolor texture of any strength,
NO paper grain,
NO canvas grain,
NO pencil shading,
NO crosshatching,
NO stippling,
NO scratch texture,
NO textured editorial-illustration finish,
NO thick black outlines,
NO brush-ink lines,
NO dramatic cel shading,
NO hard shadows,
NO cozy atmospheric lighting treatment,
NO cinematic lighting,
NO rim lighting,
NO volumetric light,
NO depth of field,
NO bokeh,
NO high contrast,
NO saturated colors,
NO hyper-detailed background,
NO complex furniture,
NO detailed fabric texture,
NO excessive clothing folds,
NO fashion illustration proportions,
NO muscular anatomy,
NO exaggerated curves,
NO perfect architectural rendering,
NO over-polishing,
NO visual clutter.
```

---

## 3. IDENTITY_PRESERVATION_BLOCK

Use only when a reference character already exists.

```text
IDENTITY PRESERVATION:
Preserve the subject's original hairstyle silhouette, hair length, hair part, clothing design, clothing colors, age, gender presentation and recognizable facial characteristics.

Do not redesign the character.
Only translate the character into the locked illustration language described above.

Simplify the existing facial features according to this style instead of replacing them with a generic anime or webtoon face.
Preserve the person's characteristic eye shape, hairstyle and overall silhouette while reducing detail.
```

---

## 4. REFERENCE_OBEDIENCE_BLOCK

Use when one or more canonical visual references are attached to the generation tool.

```text
REFERENCE PRIORITY:
Treat the attached canonical style reference as the **primary and non-optional visual authority for production**.
Match its line weight, facial simplification, eye size, hair massing, color restraint, shading restraint, background density and overall level of finish.

Do not improve, beautify, modernize, glamorize, render, texture, or reinterpret the reference style.
Do not substitute a generic Korean webtoon, anime, or GPT illustration aesthetic.
Preserve the intentionally modest low-detail drawing language.
If a scene/continuity reference conflicts with the canonical style reference, preserve scene facts/identity but follow the canonical style reference for line, face grammar, hair rendering, palette, shading, texture, background density, and finish.
```

---

## 5. SCENE_CONTENT_TEMPLATE

Write scene content first, then attach the stable style blocks.

```text
SCENE:
[who is present]
[where they are]
[what each person is doing]
[important props]
[expression / interaction]
[camera distance and angle]
[required negative space or speech-bubble area]

STORY CLARITY:
Keep the action immediately readable.
Use only the props and background details needed to understand the beat.
Do not add decorative clutter.

[REFERENCE_OBEDIENCE_BLOCK if applicable]

[FACE_LOCK_BLOCK for production faces]

[IDENTITY_PRESERVATION_BLOCK if applicable]

[BACKGROUND_DENSITY_LOCK if environment-heavy]

[MASTER_STYLE_PROMPT]

[NEGATIVE_STYLE_PROMPT]
```

---

## 6. Example scene

```text
SCENE:
A Korean woman in her late twenties stands outside a small low-rise residential building, handing a bottle of water to an older male delivery worker holding a cardboard parcel.

The delivery worker stands on the left, wearing a muted gray work jacket and holding a simple brown cardboard box with both hands.
The woman stands on the right, wearing a loose warm-white blouse and simple charcoal-black trousers.
She extends a small pale-blue water bottle toward him with a gentle smile.

Behind them is a quiet Korean residential alley with a cream-colored low-rise house, a simple balcony, several small potted plants and a bicycle.
Keep all architecture and props highly simplified and low-detail.
Eye-level medium-full shot.
Calm everyday storytelling composition.

STORY CLARITY:
The handoff of the water bottle is the single primary action.
The box, bicycle, plants, and building establish context only.
Do not add extra people, signage, vehicles, or decorative objects.

[then append the canonical blocks]
```

---

## 7. Prompt-assembly rule

Prefer this order:

1. scene facts
2. story-clarity constraint
3. reference-obedience block
4. face-lock block for production faces
5. identity-preservation block only when identity continuity is required
6. background-density lock for environment-heavy scenes
7. master style
8. negative style
9. anti-GPT-default block for production

Do not endlessly restate the same style rule in scene text. Repetition can cause tool-specific overcorrection. The stable master block is the authority.


---

## 8. ANTI_GPT_DEFAULT_BLOCK

Append for production renders, especially when the model tends to beautify or add texture.

```text
ANTI-GPT DEFAULT:
Do not substitute a generic AI illustration aesthetic.

The image must look flatter, simpler, quieter, and less rendered than a typical AI-generated webtoon/editorial illustration.

Eyes: tiny solid dark marks; no default white-eye + pupil construction.
Hair: broad flat near-black masses; no strand texture, hatching, scratch detail, or highlight bands.
Surface: clean flat digital fills; no paper grain, canvas grain, watercolor wash, pencil shading, stippling, or crosshatching.
Lighting: no cozy atmospheric glow, cinematic night lighting, rim light, or modeled ambient illumination.
Skin/clothes: no tonal rendering or texture beyond one extremely faint simple shadow if absolutely needed.
Background: only story-essential geometry; shop merchandise becomes simplified blocks with no label/detail rendering.

Do not make the picture prettier, richer, more atmospheric, or more finished than the canonical reference.
```

---

## 9. Production reference requirement

For production-grade raster generation:

```text
CANONICAL STYLE REFERENCE REQUIRED.
The actual approved reference image must be attached.
Text prompts reinforce the reference; they do not replace it.
A failed generated frame must never become the only style anchor for the next frame.
```

If the canonical reference image is unavailable, stop before paid/production generation.


---

## 10. FACE_LOCK_BLOCK

Append for production whenever a human face is visible. It is especially mandatory for medium-full/full-body framing, side gaze, multi-person scenes, and environment-heavy scenes.

```text
FACE LOCK — MANDATORY:
Preserve the canonical INSTATOON face grammar at every camera distance.

- soft rounded oval face;
- rounded jaw and small rounded chin;
- tiny simple solid-dark oval/dot eyes;
- thin short eyebrows;
- tiny minimal nose mark;
- very small simple mouth;
- subtle peach cheek blush;
- broad simple near-black hair masses around the face.

Camera distance must never cause a more detailed or generic face.
If the face is smaller in frame, simplify it further.

SIDE-GAZE RULE:
Do not lengthen or redesign the eyes to indicate gaze.
Do not add visible sclera, detailed irises, eyelid anatomy, glossy highlights, or a generic attractive webtoon/anime eye shape.
Prefer a slight head turn and minimal positional change of the tiny eye marks.

Farther character = simpler face, never more generic/detail-rich face.
Never substitute a generic GPT/editorial/webtoon face.
```

---

## 11. BACKGROUND_DENSITY_LOCK

Append for outdoor, shop, residential exterior, cafe, office, or any environment-heavy scene.

```text
BACKGROUND DENSITY LOCK:
Keep the environment narratively readable but intentionally simpler than a generic AI illustration.

Preserve only story-relevant anchors.
Reduce incidental architectural and decorative detail.
Windows, railings, bicycles, utility fixtures, furniture, plants, and merchandise should be simplified, icon-like shapes.
Background lines and micro-detail remain lighter and quieter than the character.

Do not make the environment more polished because the character is smaller in frame.
If necessary, remove roughly 30–40% of incidental detail.
```

---

## 12. Canonical reference-role map

Use the approved assets from `REFERENCE_SET.md`.

- `INSTATOON_REF_01_CHARACTER.webp`: primary face / hair / close-to-medium character grammar.
- `INSTATOON_REF_02_FULLBODY.webp`: primary full-body proportion / outfit-scale grammar.
- `INSTATOON_REF_03_INTERACTION.webp`: primary two-person interaction + outdoor balance.
- `INSTATOON_REF_04_INDOOR.webp`: primary indoor density / seated scene.
- `INSTATOON_REF_05_OUTDOOR_APPROVED.webp`: primary outdoor full-body + side-gaze / environment-heavy anchor.

Use the most relevant scene anchor **plus REF_01 as a face anchor when faces are at risk of drift**.
These references control style; they do not require recurring-character identity across unrelated episodes.
