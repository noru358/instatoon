# E001 — 편의점 음유시인

Status: **PREFLIGHT REJECTED — GLOBAL STYLE RECOVERY REQUIRED**

This is the first real TOON SYSTEM v0.1 prototype.

## Why this episode

The source contains unusually strong human-specific details:
- troublesome regular;
- unexpectedly sincere sentence;
- two opened ice bars;
- one in each hand;
- insistence on taking a bite;
- deadpan aftermath.

It is therefore useful for testing whether the system preserves **source texture** rather than converting everything into generic AI storytelling.

## Current gate

The entire 7-slide story and visual plan exists.

Before paid/raster generation, review:
1. story rhythm;
2. exact slide count;
3. hook wording;
4. source quote treatment;
5. landing;
6. visual variety.

If approved, render preflight:
- Slide 1 cover;
- Slide 5 representative high-risk body slide.

Only after both pass should the remaining raster slides be generated.


---

## Preflight execution result — 2026-09-04

Generated:
- Slide 1 cover preflight
- Slide 5 high-risk interaction preflight

### Verdict
**REJECT BOTH — systemic style failure.**

Story semantics were mostly readable, but the rendering language drifted heavily toward a generic AI/GPT illustration look.

### Observed global style defects
1. **Eyes:** white sclera + separate pupils instead of tiny solid-dark eye grammar.
2. **Hair:** many internal strokes / textured hair rather than broad flat near-black masses.
3. **Texture:** pervasive paper/grain/pencil-like surface texture.
4. **Shading:** more modeled skin/clothing/background shading than the lock permits.
5. **Lighting:** convenience-store night scene became cozy/atmospheric with refrigerator/window/lamp glow.
6. **Background density:** products, refrigerators, lamps, window architecture and counter equipment were individually rendered too strongly.
7. **Finish:** image reads as polished editorial/anime-adjacent AI illustration rather than a modest low-density anecdote comic.
8. **Slide 5 compound error:** Slide 1, already style-failed, was reused as a style/continuity anchor, causing the wrong style to propagate.
9. **Slide 5 action error:** both ice bars appear already bitten/notched and the handoff is less clean than specified; this frame should precede the worker taking a bite.

### Root cause
The execution did **not** use the true canonical visual reference image as the primary style authority.

The first render used a summarized textual style description. That allowed the image model's generic illustration prior to fill ambiguous details.

The second render then used the first failed frame as the principal reference, compounding the drift.

### System correction
- STYLE_LOCK hardened to `INSTATOON_STYLE_v1.1`.
- MASTER_PROMPTS adds explicit anti-GPT-default flatness/texture/eye/hair/background rules.
- GENERATION_PROTOCOL now requires an actual approved canonical style image before production raster generation.
- Failed preflight frames may not become style anchors.

### Current blocker
The repository currently contains textual style authorities but **no verified canonical style-reference image binary**.

Do not spend another production generation until the approved reference image is actually preserved and available to the generation environment.

### Next retry sequence
1. preserve/verify 1–3 canonical style-reference images in repository assets;
2. attach canonical style reference + scene facts for Slide 1;
3. run Slide 1 only;
4. QC style fingerprint;
5. only if Slide 1 passes, run Slide 5 with canonical style reference as style authority and accepted Slide 1 only as episode-continuity aid;
6. do not bulk-render remaining slides until both pass.
