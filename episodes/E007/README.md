# E007 — 엘리베이터 혼자 타면

Status: S01 USER APPROVED — REMAINING RASTER INTERNAL QC / CLEAN CONTEXT REQUIRED
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

## 5. L12.5 structured contract — USER APPROVED

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
- conversation-inferred rendering is sequential after S01, but S02~final use operator/internal QC rather than per-frame user approval.

Lettering plan locks only the already-approved copy:
- S01 caption;
- S03 Harin line;
- S05 security line;
- S06 Harin "…네?";
- S07 "!?"
with S02/S04 textless.

## 6. L12.5 + S01 gates — PASSED

L12.5 structured contract: USER APPROVED 2026-09-06.
Evidence: user replied "통과".

S01 visual anchor: USER APPROVED 2026-09-06, with one explicitly tolerated defect recorded below.

Current production stage:
REMAINING_RENDER.

MANUAL_VALIDATION approval topology now applied to this episode:
- S01 was the user-facing visual anchor gate;
- S02~S07 are produced as separate files with operator/internal QC;
- the next normal user gate is the COMPLETE text-free raster set;
- lettering begins only after that full-set user PASS.

The current conversation-inferred render context is blocked for S02 because it repeated the wrong S01 scene twice. This is a renderer-context blocker, not a request for another user approval.


## 7. S01 manual QC

User verdict: PASS WITH KNOWN TEXT DEFECT.

Passed:
- Harin identity;
- overall drawing quality;
- background-extra diversity after repair;
- scene readability.

Known deferred defect:
- readable caption/background text was baked into the raster despite the text-free contract.

Policy:
- do not reinterpret this as contract-compliant;
- continue only because the user explicitly chose to proceed for this manual validation run;
- later slides should enforce no readable raster text more strongly;
- S01 remains a visual continuity/taste anchor only unless a repository-bound artifact/attempt record is later created.

Next:
resume at S02 in a clean render context. Internally QC S02, then continue S03~S07. Do not ask for per-slide user approval unless a material taste/contract decision cannot be resolved internally. Present the complete text-free raster set for the next user gate.


## 8. S02 repeated context failure

Current-context native/chat render path: HARD STOP.

Two consecutive attempts intended for S02 produced the S01 office-group composition again.

Required S02 contract:
- Harin alone;
- inside a closed office elevator;
- public persona relaxes;
- no coworkers or other passengers;
- no readable text/signage/labels.

Observed invalid output:
- office-group scene;
- multiple coworkers;
- essentially S01 semantics.

Classification:
WRONG_SCENE / CONTEXT_CONTAMINATION.

Both outputs are INVALID:
- not S02;
- not anchors;
- not repair bases;
- not LAST_KNOWN_GOOD.

Per GENERATION_PROTOCOL, do not retry this conversation-inferred path again after two repeated hard-contract failures.

Exact resume action:
1. use a clean dedicated render context;
2. restore REF_V2_D + REF_V2_E and the exact E007 S02 contract;
3. render S02 only and perform operator/internal QC;
4. if PASS, continue S03~S07 sequentially with the same internal-QC rule;
5. after every raster is acceptable, present the complete text-free art set to the user;
6. only that full-set USER PASS authorizes lettering.
