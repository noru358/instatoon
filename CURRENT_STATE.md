# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E006/README.md

## 현재 위치

큰 흐름: 수동 제작 검증 → 상태/렌더 가드 강화 → 최소 실행 경로 연결 → 독립 CLI → 웹 도구.

E006 "어떻게 오셨어요?"의 corrected L1-L7 package가 2026-09-06 사용자 명시 승인 PASS.
현재 PRODUCTION_STATE = RENDER_CONTRACT_READY.

완료:
- L1-L8 PASS;
- L9 episode-local voice preservation recorded, no unsupported global rule promotion;
- L10 storyboard/cast routing complete;
- L11 woman_01 + receptionist_01 persistent identity digests complete;
- L12 six-slide whole-episode visual plan complete;
- L12.5 EPISODE_PLAN / SHA-bound RENDER_MANIFEST materialized.

## E006 production lock

- 6 slides.
- Feed/carousel master 4:5, 1080×1350.
- ONE PANEL = ONE IMAGE FILE.
- L13 raster is text-free.
- L14 adds final Korean text/bubbles.
- no main cast in this episode.
- required canonical style media: REF_V2_D + REF_V2_E, both BINARY_REQUIRED.
- first accepted E006 frame becomes a secondary episode style/identity anchor for later slides.

The earlier premature 9:16 six-panel render remains INVALID_RENDER / STORYBOARD_REFERENCE_ONLY and must not be used as a visual reference.

## 정확한 다음 행동

1. run render_guard validate for E006.
2. compile E006_S01 from MASTER_PROMPTS + EPISODE_PLAN + RENDER_MANIFEST.
3. authorize S01 only with actual supplied-media evidence for REF_V2_D/E.
4. if the current renderer cannot bind those exact images as media, STOP at L13 preflight rather than text-only fallback.
5. if authorized, generate S01 only as text-free 4:5.
6. user style/identity QC PASS is required before S02.

## 구조 개선

Persisted state gate remains active:
- CAST_ONLY != L8 full approval;
- caller string PASS cannot substitute for artifact-bound QC;
- pre-render active episodes are valid states;
- render authorization is fail closed.

## 현행 시각 기준

- INSTATOON_STYLE_v2.0.
- REF_V2_D: assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
- REF_V2_E: assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg
- approved binaries outrank generalized prose.
