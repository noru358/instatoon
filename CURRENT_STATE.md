# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E007/README.md

## 현재 위치

큰 흐름:
수집/소재 확정 → L1-L7 → L8 사용자 승인 → 캐스팅/콘티 → 비주얼 플랜 → 구조화 계약 → 레퍼/프리플라이트 → 개별 래스터 → 분리 레터링 → 최종 QC → 완성.

E007:
- fresh L1-L7: USER APPROVED;
- cast/storyboard: USER APPROVED with Harin as protagonist;
- visual plan: USER APPROVED;
- reference authority: USER SUPPLIED and hash-confirmed against canonical REF_V2_D + REF_V2_E;
- structured files created: EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN;
- machine stage: VISUAL_PLAN_READY;
- current checkpoint: L12.5 structured-contract user review;
- no raster, anchor, or frame QC exists yet.

## Reference binding

Required canonical binaries:
- REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
  SHA-256 dbddf458a97c89781075e6be03ab2c393eff75b95e8856f044bd81f29310ec07
- REF_V2_E_3PERSON_INDOOR_SCENE.jpeg
  SHA-256 b49683276f94ba5621e3602d7e3d714b0f2e637b2c41fc1fd132bdf6f336b049

The active-conversation uploads match those exact hashes.
Both are BINARY_REQUIRED for production raster.

## 현재 운영 모드 — MANUAL_VALIDATION

1. every meaningful production stage is shown to the user and explicitly reviewed;
2. no auto-finish;
3. one slide = one raster file;
4. raster is text-free;
5. every raster slide is user-reviewed before the next;
6. lettering and final export are separately reviewed.

## 정확한 다음 행동

1. present the L12.5 structured contract summary to the user;
2. wait for explicit approval or edits;
3. after approval set stage RENDER_CONTRACT_READY;
4. run final media-binding authorization for S01 using both exact reference binaries;
5. generate S01 only;
6. stop for manual S01 QC.
