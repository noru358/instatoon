# MASTER_PROMPTS.md

# CANONICAL — INSTATOON MASTER PROMPT v2.2
Updated: 2026-09-06

This is the single authoritative visual-generation prompt source.
This file owns prompt wording. If wording conflicts with an approved visual reference, the approved image wins; reconcile the wording rather than redesigning the reference.

## 0. Production intent

Create a simple hand-drawn 2D Instagram webcomic.
Optimize for readable storytelling, consistent identity, expressive reaction, and deliberate visual simplicity.
Do not optimize for glossy beauty or generic AI-illustration polish.

## 1. MASTER VISUAL STYLE LOCK

Use clean black hand-drawn outlines with slight natural irregularity and subtle line-weight variation.
Lines must feel manually drawn, not mathematically perfect vector paths.

CHARACTERS:
- simplified adult proportions, about 4.5–5 heads tall;
- slightly oversized head;
- narrow-to-normal shoulders;
- simple limbs and hands;
- no fashion-model anatomy or exaggerated curves.

FACE:
- preserve the selected identity’s eye shape and expression from its approved image;
- large round eyes are a common style trait, not a command to open every eyelid;
- large white sclera;
- simple solid black pupil/iris;
- one tiny white eye highlight at most;
- minimal eyelashes;
- thin simple eyebrows;
- nearly absent nose;
- small graphic mouth;
- open mouth = simple black oval/semicircle with small flat coral-red inner mouth/tongue;
- no realistic lips, cheek modeling, nose modeling, or facial sculpting.

HAIR:
- broad graphic mass;
- strong simple silhouette;
- only a few interior strand/wave lines;
- no realistic strand rendering;
- no glossy highlight bands;
- no gradient hair rendering.

COLOR / RENDER:
- flat local colors;
- muted but not washed into one global beige palette;
- almost no shading;
- no global paper/grain/noise;
- no watercolor/pencil/canvas texture;
- no airbrushed or modeled lighting;
- if spatial readability requires it, use only a very simple flat contact shadow.

CLOTHING:
- contemporary everyday clothing appropriate to the story;
- clear graphic silhouettes;
- only necessary seams/folds;
- no realistic textile rendering.

When uncertain, simplify rather than add detail.

## 2. ENVIRONMENT / BACKGROUND LOCK

All environments and props must follow the exact same visual grammar as the characters.

- simple black hand-drawn outlines;
- flat local muted fills;
- simplified architecture/furniture/plants/streets/windows/signs/props;
- only the details needed to identify the place and support the story;
- simple plausible perspective with mild hand-drawn flatness;
- background detail density lower than character detail density;
- no realistic wood grain, glass reflection, metal gloss, fabric texture, ambient illumination, or decorative clutter;
- no global beige/sepia mood wash;
- no “cozy lifestyle illustration” treatment.

The room, café, office, subway, park, shop, street, or home must look as if the same comic artist casually drew both people and environment.

## 3. ANTI-AI-POLISH LOCK

NO:
- generic smooth attractive AI face;
- featureless default young-adult face;
- polished romance-webtoon/anime rendering;
- 3D/semi-realistic volume;
- cinematic/cozy lighting;
- rim light, bloom, volumetric light, bokeh;
- gradients or airbrush shading;
- global paper texture/grain/noise;
- warm sepia overlay;
- glossy skin/hair;
- detailed irises;
- realistic facial anatomy;
- elaborate fabric texture;
- hyper-detailed background;
- concept-art environment polish;
- highly perfect vector finish.

Do not make the frame prettier, richer, warmer, more atmospheric, or more finished than the approved references.

## 4. REFERENCE OBEDIENCE

Approved current references control:
- line;
- face grammar;
- eye size;
- hair massing;
- body proportions;
- color/render simplicity;
- detail density;
- overall finish.

Scene text controls what happens, not how the drawing style is redesigned.

Do NOT use pre-reset legacy assets from assets/style_refs/ as current style authority.

## 5. CAST ROUTING RULE

Choose cast from story/context BEFORE rendering.

There is NO quota requiring all three recurring leads to appear.
Per episode and per scene, use only the people who have an actual story function:
- zero, one, two, or all three of Gaeun / Harin / Taemin may appear;
- an episode may use only episode-local/supporting characters;
- supporting or one-off characters (boss, coworker, clerk, date, family member, customer, etc.) may be introduced whenever the premise requires them;
- omit any recurring lead who would exist only to fill space or provide a redundant reaction.

Main cast may appear when the episode naturally suits them:
- Gaeun
- Harin
- Taemin

Never insert a main character merely because the scene needs “a woman” or “a man.”
There is no global Taemin ban.
An episode may explicitly choose an episode-only man instead of Taemin.

Cast routing is story-first, not asset-first: fixed visual style and continuity do not imply fixed cast composition.

This is a PROJECT-WIDE routing invariant. Episode files record only the cast selected for that episode; they must not redefine this policy or encode a per-episode three-person/main-cast quota.

## 6. RECURRING CHARACTER IDENTITY BLOCK

When a main character is selected:
preserve the approved hairstyle silhouette, hair length/part, clothing when locked for that episode, age/presentation, body silhouette, facial identity, and salient accessories.

Current notes:
- Harin: black socks when socks are visible.
- Taemin: approved 2026-09-04 black-haired identity; do not clone him into unrelated episode-only men.

## 7. EPISODE-LOCAL CHARACTER DESIGN BLOCK

For any newly introduced important person who appears in 2+ cuts:

INTERNALLY, before assembling the episode batch:
- choose a face/hair/clothing combination that fits the story role and social context;
- make the person visually distinct from main cast;
- avoid generic smooth AI-pretty facial design;
- preserve the same v2 drawing language;
- record one compact identity digest as the episode-only continuity source.

THEN, for every frame in the coordinated batch:
- preserve the digest's face structure, hair silhouette, age, clothing, and recognizable details;
- vary only pose/expression/camera as required by the beat.

Do not improvise a new version of the person panel by panel.
Do not create or present a separate character sheet by default. Use a temporary internal image anchor only as an exception when direct batch continuity fails.

## 8. SCENE PROMPT TEMPLATE

SCENE:
[episode / slide]
[characters and which recurring reference or episode-only identity digest each uses]
[location]
[action]
[essential props]
[expression/reaction]
[camera/composition]
[negative space for later vector text]

STORY CLARITY:
[one thing the viewer must understand instantly]

PRESERVE:
[last-known-good composition/areas when this is a repair]

CHANGE ONLY:
[named local defect when this is a repair]

Then apply:
- MASTER VISUAL STYLE LOCK
- ENVIRONMENT / BACKGROUND LOCK
- ANTI-AI-POLISH LOCK
- REFERENCE OBEDIENCE
- identity/episode-local anchor block as applicable

## 9. REPAIR / LAST-KNOWN-GOOD BLOCK

If a previous frame is visually accepted except for a local defect:

Use the accepted frame as the base.
Change ONLY the explicitly named defect.
Preserve all unmentioned:
- character identity;
- camera;
- pose/blocking;
- background;
- composition;
- palette;
- linework;
- story beat.

Do not regenerate the whole scene merely to fix a local issue.
If a retry visibly regresses, discard it and return to the last known good frame.

## 10. OUTPUT FORMAT

- Instagram carousel/feed: 4:5, 1080×1350.
- Reels/Shorts: 9:16, 1080×1920.
- 16:9 only when explicitly requested for landscape/long-form.

Plan semantics once; adapt composition per output ratio.
Never stretch one finished render.

## 11. TEXT RULE

Production raster art should normally contain NO important readable text.

Generate:
- character;
- environment;
- props;
- non-text reaction marks when appropriate;
- planned empty space.

Add final narration/dialogue/bubbles/SFX as an editable vector/layout layer after art generation.

Prototype baked-in text may be used only for quick taste tests, not as the canonical publish master.

## 12. COMPILED PRODUCTION PROMPT

Draw exactly one standalone panel for the requested slide, in one image. No multi-panel page, strip, grid, collage or sheet. Input character sheets and scene references are references only; do not reproduce their layout.

Draw a simple hand-drawn 2D Instagram-webcomic frame matching the approved v2 references. Use slightly irregular black outlines, simplified adult 4.5–5-head proportions, large round white eyes with simple black pupils/irises and at most one tiny highlight, almost no nose, small graphic mouths, broad simple hair masses, flat local muted colors, and almost no shading.

Draw the environment with the exact same comic language: simple black outlines, large flat shapes, low detail density, simple perspective, no realistic materials, no decorative clutter, no global beige/sepia wash, and no cozy/cinematic atmosphere.

Do not beautify or over-render. No generic smooth AI-pretty faces, glossy anime/webtoon finish, paper grain, gradients, airbrush shading, detailed irises, realistic facial anatomy, glossy hair, textile rendering, ambient lighting, or hyper-detailed backgrounds.

The attached approved images are the visual authority. Common eye/proportion descriptions must not override an approved identity’s eye shape, eyelids or natural expression. Do not exaggerate texture, lighting or detail beyond the references, and do not redesign their accepted line quality to satisfy an absolute prose ban.

Use style-only references for drawing language, not their cast, room, pose, framing or palette wholesale. Render only the episode-selected people in the planned scene.

For a recurring character, preserve that selected person’s referenced identity. For an episode-only person, transfer drawing language only: use the story-specified age, gender/presentation, body, hair and clothing rather than copying the reference people. Simplified adult proportions describe the current adult cast, not a rule to turn children, older people or different physiques into those adults. Keep the same drawing language through these variations.

Use the story-selected recurring-character reference or the internally derived episode-only identity digest consistently. Once an episode image is accepted, also use its actual image as the secondary identity/style anchor on later cuts; the current scene contract still controls action and composition. If this is a repair and a last-known-good frame exists, preserve it and change only the named defect.

The compiler appends the exact story beat, scene contract, output format and required media below.
