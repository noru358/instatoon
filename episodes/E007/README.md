# E007 — 엘리베이터 혼자 타면

Status: L12.5 STRUCTURED CONTRACT AWAITING USER APPROVAL — MANUAL_VALIDATION
Updated: 2026-09-06

## 0. Reset record

The user explicitly reset E007 on 2026-09-06 and requested a fresh production run in actual MANUAL_VALIDATION mode.
The previous office-lunch E007 package and approvals are historical only and do not authorize current production.

## 1. Source / L1-L7 — USER APPROVED

Human-source seed:
- Reddit r/tifu
- "TIFU forgetting that elevators aren’t private"
- https://www.reddit.com/r/tifu/comments/1ll61ou/tifu_forgetting_that_elevators_arent_private/
- provenance: HUMAN_SEEDED_INSPIRATION

Approved engine:
professional office persona → goofy private elevator ritual → security mirrors the private phrase → CCTV realization.

Approved adaptation boundary:
- Korean-localize setting/dialogue;
- no named-company fabrication;
- no punishment, viral exposure, coworkers watching footage, or stronger humiliation.

Approved text:
- caption: "회사에선 나름 멀쩡한 척함."
- Harin: "오~ / 오늘 좀 나오는데?"
- security: "오~ 오늘 좀 나오는데~"
- Harin: "…네?"
- final reaction: "!?"

L8 evidence:
2026-09-06 user replied "ㅇㅋ" after reviewing the full fresh L1-L7 package.

## 2. L10 cast / storyboard — USER APPROVED WITH EDITS

Main protagonist:
- Harin.

Episode-only supporting character:
- security_01: middle-aged Korean building security employee; dry/calm, not mocking.

User edits incorporated:
- replace the original episode-only male protagonist with Harin;
- delete the awkward security line "아, 아닙니다. 저희끼리 한 말이에요.";
- after Harin says "…네?", security_01 responds only with a quick finger gesture;
- replace final "설마." with "!?"

Seven-slide sequence:
1. S01 public persona — Harin appears composed at work.
2. S02 switch — elevator doors close; she visibly relaxes.
3. S03 private ritual — silly mirror pose / small dance; "오~ 오늘 좀 나오는데?"
4. S04 instant reset — doors open; Harin returns to professional mode.
5. S05 phrase leaks — security_01 casually repeats "오~ 오늘 좀 나오는데~".
6. S06 suspicion — Harin "…네?"; security_01 gives a silent quick finger gesture.
7. S07 landing — Harin looks up at CCTV; reaction text "!?"

## 3. L11/L12 visual plan — USER APPROVED

- Harin identity remains canonical; face/hair/drawing grammar must not be redesigned.
- office-casual staging may adapt clothing only within the established character language.
- security_01 is episode-local and visually plain, non-threatening, non-caricatured.
- backgrounds: simple office elevator lobby, elevator interior, building lobby/security desk.
- S03 comedy is body/shoulder/expression driven; avoid complex finger anatomy.
- S06 uses one simplified hand gesture; hand QC risk HIGH.
- S07 uses understated frozen realization, not screaming.
- raster remains text-free; lettering is separate.

## 4. Reference authority — CONFIRMED 2026-09-06

The user supplied two images in the active conversation.

They exactly match the repository canonical binaries by dimensions and SHA-256:

### REF_V2_D — main cast / Harin identity authority
- repo path: assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
- dimensions: 1448 × 1086
- SHA-256: dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07
- role: Harin face/hair/body/line/color/character-identity authority.

### REF_V2_E — scene/style application authority
- repo path: assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg
- dimensions: 1536 × 864
- SHA-256: b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049
- role: scene-level drawing language, indoor background density, character/environment integration.

Production requirement:
both references are BINARY_REQUIRED and must be supplied as actual image media to the renderer for every canonical raster call.
The user-uploaded active-conversation copies are equivalent to the repo binaries.

## 5. L12.5 structured contract — BUILT, USER REVIEW PENDING

Created:
- episodes/E007/EPISODE_PLAN.json
- episodes/E007/RENDER_MANIFEST.json
- episodes/E007/LETTERING_PLAN.json

Contract:
- 7 slides;
- 4:5, 1080×1350;
- exactly one panel per image;
- separate files;
- raster text-free;
- Harin main cast;
- security_01 episode-local continuity on S05-S06;
- REF_V2_D + REF_V2_E exact canonical media required;
- unexpected concept policy FAIL_CLOSED;
- conversation-inferred rendering is sequential and every frame is user-gated in MANUAL_VALIDATION.

Lettering plan locks only the already-approved copy:
- S01 caption;
- S03 Harin line;
- S05 security line;
- S06 Harin "…네?";
- S07 "!?"
with S02/S04 textless.

## 6. Current manual checkpoint

STOP before raster.

User must review/approve the structured contract.
After approval:
1. mark production stage RENDER_CONTRACT_READY;
2. perform final media-binding preflight;
3. render S01 only with both actual reference images;
4. user manually reviews S01 before any S02 call.
