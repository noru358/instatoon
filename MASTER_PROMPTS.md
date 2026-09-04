# MASTER_PROMPTS.md

# CANONICAL — INSTATOON MASTER PROMPT v2.0
Updated: 2026-09-04

This file is the single authoritative prompt source for image generation.
If another prompt/style document conflicts with this file, this file wins until the conflict is cleaned up.
The pre-2026-09-04 tiny-eye / thin-brown-line style is retired.

## 0. Core production intent

Create a simple hand-drawn 2D Korean Instagram-webcomic illustration.
The goal is not polished beauty. The goal is readable storytelling, consistent characters, expressive reactions, and a deliberately modest handmade finish.

## 1. MASTER VISUAL STYLE LOCK

Use clean black hand-drawn outlines with slight natural irregularity and subtle variation in line weight.
Lines should feel manually drawn rather than mathematically perfect vector paths.

Characters use simplified adult proportions, roughly 4.5–5 heads tall, with slightly oversized heads, narrow shoulders, simple limbs, and minimally simplified hands.
Do not exaggerate chest, hips, muscles, or fashion-model proportions.

FACE:
- large round eyes with large white sclera;
- simple solid black pupils/irises with one tiny white highlight;
- minimal eyelashes;
- thin simple eyebrows;
- almost no nose;
- small graphic mouths;
- open mouths are simple black oval/semicircle shapes with a small flat coral-red inner mouth/tongue;
- no realistic lips, cheek modeling, nose modeling, or facial shading.

HAIR:
- hair is a simple graphic mass;
- strong readable outer silhouette;
- only a few interior strand/wave lines;
- no realistic individual strands;
- no glossy highlight bands;
- no gradient rendering.

COLOR / RENDER:
- mostly flat muted colors;
- sparse hand-drawn texture is allowed on denim, dark clothes, or large flat areas;
- very little or no shading;
- no smooth gradients;
- no painterly modeling;
- skin stays flat and simple.

CLOTHING:
- ordinary contemporary Korean 20s–30s casual clothing;
- simplified into clear graphic shapes;
- only a few necessary fold lines;
- no fashion-illustration exaggeration;
- no realistic fabric rendering.

OVERALL:
simple, readable, slightly imperfect, expressive, charming, intentionally unpolished.
When uncertain, simplify rather than add detail.

## 2. ENVIRONMENT / BACKGROUND STYLE LOCK

All environments and props use the same visual grammar as the characters.

- same simple black hand-drawn outlines;
- flat muted color fills;
- simplified architecture, furniture, plants, streets, windows, signs, and props;
- only enough detail to identify the place;
- large readable shapes instead of many small details;
- simple plausible perspective; slight hand-drawn flatness is acceptable;
- almost no shading;
- no realistic wood grain, glass reflections, metal gloss, fabric texture, or cinematic light;
- low decorative clutter;
- background line density lower than character line density;
- leave breathing room.

The background must look as if the same illustrator who drew the characters casually drew the room, café, street, office, subway, park, or shop.

IMPORTANT:
A fixed background anchor is NOT required for the series.
Story determines location.
Create episode/scene-specific environments using this background style lock.
Only create a location anchor when a location intentionally recurs and continuity benefits from it.

## 3. ANTI-GPT / ANTI-POLISH LOCK

Do not beautify or over-render.

NO:
- polished romance-webtoon rendering;
- glossy anime rendering;
- semi-realistic illustration;
- 3D or 3D-like volume;
- cinematic lighting;
- rim light, bloom, volumetric light, bokeh;
- smooth gradient shading;
- airbrush rendering;
- realistic skin texture;
- glossy skin or hair;
- detailed iris rendering;
- realistic facial anatomy;
- sharp V-line glamour face;
- elaborate fabric texture;
- hyper-detailed background;
- concept-art environment rendering;
- decorative clutter;
- highly polished vector perfection.

Do not “improve” the reference.
A prettier, richer, shinier, more realistic result is usually a failure.

## 4. REFERENCE OBEDIENCE

When current approved reference images are attached:
- treat them as the primary visual authority;
- use them for line, face grammar, eye size, hair massing, palette, shading restraint, body proportions, detail density, and overall finish;
- scene text controls what happens, not how the style is redesigned.

Do not use pre-reset assets from `assets/style_refs/` as canonical references unless REFERENCE_SET.md explicitly marks them current.

## 5. CHARACTER IDENTITY LOCK

For recurring characters:
preserve hairstyle silhouette, hair length/part, clothing, clothing colors, age, gender presentation, body silhouette, characteristic eye/eyebrow expression, and salient accessories.

Do not redesign a recurring character because the scene changes.
Translate the same identity into the locked style.

CURRENT MAIN CAST:
- Gaeun: recurring main character.
- Harin: recurring main character; black socks when socks are visible.
- Taemin: recurring main character; current approved identity is the black-haired male based on the user-approved 2026-09-04 reference, normally black jacket/black inner top/cream trousers/black sneakers unless episode wardrobe explicitly changes.

EPISODE-ONLY CHARACTERS:
New one-off people are allowed and expected when the story needs them.
They must use the same master visual style but do not inherit main-character identity.

## 6. SCENE PROMPT TEMPLATE

SCENE FACTS:
[episode / slide number]
[who is present]
[location]
[action]
[essential props]
[expression/reaction]
[camera distance and angle]
[negative space required for text]

STORY CLARITY:
State the single beat the viewer must understand immediately.

CONTINUITY:
[recurring character identity block if relevant]
[episode-only temporary character note if chronological continuity is needed]

Then apply:
1. MASTER VISUAL STYLE LOCK
2. ENVIRONMENT / BACKGROUND STYLE LOCK
3. ANTI-GPT / ANTI-POLISH LOCK
4. REFERENCE OBEDIENCE when reference is attached

## 7. OUTPUT FORMAT LOCK

Primary outputs:
- Instagram carousel / feed toon: 4:5, target 1080×1350.
- Reels / Shorts: 9:16, target 1080×1920.
- 16:9 is NOT the default for this project; use only for explicit landscape/long-form derivatives.

Plan the story once, then render/adapt compositions for each output track.
Do not stretch one finished image into a different ratio.

## 8. TEXT / LETTERING RULE

For production automation, important Korean captions/dialogue should preferably remain an editable vector/layout layer rather than being irreversibly baked into raster art.
Generated text inside an image may be used for quick prototype evaluation, but final export should preserve editability and typo control.

## 9. COMPILED PRODUCTION PROMPT

Draw in a simple hand-drawn 2D Korean Instagram webcomic style based closely on the approved reference sheets. Use black hand-inked outlines with slight natural irregularity, simplified adult 4.5–5-head proportions, slightly oversized heads, large round white eyes with simple black pupils and one tiny highlight, almost no nose, small graphic mouths, hair as broad simple masses with only a few interior lines, flat muted colors, sparse hand-drawn texture, and minimal or no shading.

All backgrounds and props must follow exactly the same visual grammar: simple black outlines, flat muted fills, simplified shapes, low detail density, simple plausible perspective, almost no shading, no realistic material rendering, and no decorative clutter. The same illustrator must appear to have drawn both characters and environment.

Do not beautify or over-render. No polished romance-webtoon look, glossy anime look, semi-realism, 3D volume, cinematic lighting, gradients, airbrush shading, glossy skin/hair, detailed irises, realistic facial anatomy, elaborate fabric texture, hyper-detailed backgrounds, or concept-art polish. When uncertain, simplify rather than add detail.

Preserve any recurring character identity exactly. New episode-only characters are allowed but must use the same style.

[INSERT SCENE FACTS + STORY BEAT + OUTPUT RATIO HERE]
