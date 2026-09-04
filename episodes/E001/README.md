# E001 — 편의점 음유시인

Status: **PREFLIGHT BLOCKED — generated output not retrievable from this environment**

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
  - image_gen gen_id: `8b27651d-2cd4-4762-bcf3-bd41c538c303`
  - size: 1122×1402
  - SHA-256: `85457dbe9b47206e9dbfe900a2c1de8a5d54ca6612d6b6c1968f47ca4b11fe9c`
- Slide 5 high-risk interaction preflight
  - image_gen gen_id: `b392eb14-d6b0-4a98-83f0-6a29bb9b68ed`
  - size: 1122×1402
  - SHA-256: `b68b5bf5fafd80a9d8fe1b6705b8f845612ca2efbeab9b9cc2f73982f471bc79`

The failed PNG binaries are not claimed as GitHub-preserved; the identifiers/hashes are retained as execution evidence.

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


---

## Preflight retry — run 002, 2026-09-04

First retry using actual canonical binary style references (the blocker from run 001).

Setup:
- worker fixed as an early-20s Korean woman (see `EPISODE_PLAN.json` continuity);
- style anchors: `INSTATOON_REF_01_CHARACTER` + `INSTATOON_REF_04_INDOOR`, uploaded and attached;
- prompts assembled deterministically from `prompts/SLIDE_01_SCENE.txt` + `prompts/_BLOCKS_COMMON.txt`;
- new leading REFERENCE ROLE block forbids reusing the reference person's identity;
- renderer: Topview `image_edit`, Nano Banana Pro, 4:5, 2K.

Result:
- task `3e37d3c71fea4c82ae4f9afdf0360d08` — **generation succeeded**, 0.8 credit,
  1856×2304;
- the result binary **could not be downloaded** — both Topview result hosts are
  denied by this environment's egress policy (403 to CONNECT).

Verdict: **NOT ASSESSED.** No QC verdict may be recorded for a frame that could
not be retrieved and inspected. The slide is neither accepted nor rejected.

See `RENDER_MANIFEST.json` blockers `EGRESS_001` and `REFS_001`.

Slides 2–7 are fully prompt-assembled and ready to submit the moment slide 1 and
slide 5 clear the cost gate.
