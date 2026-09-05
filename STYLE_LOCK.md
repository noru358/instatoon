# STYLE_LOCK.md

# INSTATOON_STYLE_v2.0 — CURRENT VISUAL PASS/FAIL LOCK
Approved: 2026-09-04
Continuity clarification: 2026-09-05

The pre-reset tiny-eye / thin brown-line style is retired.

## Core fingerprint

- simple hand-drawn 2D Instagram-webcomic look;
- black outlines with slight natural irregularity;
- flat local colors;
- almost no modeled shading;
- large round eyes with white sclera + simple black pupil/iris + tiny highlight;
- nearly absent nose;
- small graphic mouth;
- hair as broad graphic masses with only a few interior lines;
- simplified adult proportions around 4.5–5 heads tall;
- contemporary everyday clothing simplified into readable shapes;
- backgrounds drawn by the same visual hand as characters.

The target is controlled simplicity, not low technical quality.

## Anti-drift fingerprint

Current observed failure modes are hard fails when they become visually dominant:

1. generic smooth attractive AI face, especially a featureless young-adult face;
2. warm beige/sepia wash applied across the entire scene;
3. cozy café/editorial ambience replacing flat comic color;
4. global paper grain/noise/pencil-like surface texture;
5. soft ambient shading or ambient-occlusion around objects;
6. material rendering on wood, glass, metal, fabric, skin, or hair;
7. glossy or strand-heavy hair;
8. detailed iris/facial anatomy;
9. polished romance-webtoon/anime finish;
10. hyper-detailed background or concept-art environment treatment;
11. a background that looks more rendered than the characters.

Do not solve “plain” by adding atmosphere, texture, lighting, or decorative detail.

## Color rule

Use local object colors, not one global mood filter.

Examples:
- wall can be simple warm/off-white;
- wood can be one or two flat browns;
- plants can be a flat muted green;
- clothes retain their own clear local colors.

No blanket beige haze.
No vignette.
No cinematic warm lighting.
No soft realistic shadow system.

A single simple contact shadow is allowed only when needed for spatial readability.

## Background rule

Story chooses location.
A fixed location-anchor library is not a mandatory stage.

Backgrounds:
- use the same outline language as characters;
- use large simple shapes;
- include only location-identifying details;
- stay lower in line/detail density than the characters;
- avoid realistic material/light rendering.

Create a persistent background anchor only if a location intentionally repeats and continuity proves useful.

## Cast rule

Main cast:
- Gaeun
- Harin
- Taemin

They are reusable, not mandatory.

Episode context decides whether a main character appears.
There is NO global Taemin-ban rule.
Do not default to Taemin merely because an episode needs a male character.

New episode-only people are expected.

## Episode-only character continuity rule

If a newly introduced non-main character will appear in 2+ cuts:
1. derive that character internally from the story, social role, and scene context;
2. check that face, hair, age, clothing, and social role fit the episode;
3. check that the person does not accidentally duplicate a main character;
4. record a compact identity digest and reuse it across all cuts in the same production batch.

This is an internal continuity operation, not a separate deliverable or user approval stage.
A standalone character sheet is optional and should be created only when direct batch continuity fails or the character is intentionally promoted for reuse.

One-frame background extras may skip this step.

## Continuity rule

A local correction must not trigger a full visual redesign.

When a frame is already good except for one defect:
- preserve the accepted composition, scene blocking, background, palette, and identity;
- edit only the named defect;
- use the last known good frame/reference as the base;
- never promote a visibly regressed retry into the new anchor.

## Change control

No silent mutation.

A material style change requires:
1. explicit proposed change;
2. visual comparison;
3. user approval;
4. version update.

MASTER_PROMPTS.md is the canonical full prompt implementation.
