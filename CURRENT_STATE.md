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
- machine stage: RENDER_CONTRACT_READY;
- L12.5 structured contract: USER APPROVED;
- current checkpoint: S02 blocked in current render context; clean-context retry required;
- no machine-bound raster, anchor, or frame QC exists yet.
- S01 latest QC: USER PASSED visual quality after background-extra repair; baked raster text/signage remains a known deferred contract defect and is not considered compliant.
- S02 current failure: two consecutive native/chat attempts reproduced the S01 office-group scene instead of the elevator-alone scene. Both outputs are INVALID and discarded.

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

1. open a clean dedicated render context;
2. restore CURRENT_STATE + E007 package + canonical REF_V2_D + REF_V2_E;
3. render S02 only: Harin alone inside closed elevator, relaxed shoulders/face, no other people, no readable text;
4. stop for manual S02 QC;
5. do not render S03 before explicit S02 PASS.
