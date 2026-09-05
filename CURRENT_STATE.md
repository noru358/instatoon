# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E006/README.md

## 현재 위치

큰 흐름: 수집/소재 확정 → L1-L7 재구성 → 사용자 보이스 게이트 → 캐스팅/콘티 → 렌더 계약 → 첫 컷 QC → 나머지 컷.

E006는 사용자가 기존 치과 에피소드 대신 **직장 내 모순된 자율/보고 요구** 주제로 교체했다.
현재 PRODUCTION_STATE = L8_AWAITING_APPROVAL.

새 L1-L7 후보는 episodes/E006/README.md에 기록되어 있다.
기존 치과 EPISODE_PLAN / RENDER_MANIFEST는 새 패키지 승인 전까지 **SUPERSEDED / DO_NOT_RENDER** 이다.

## 새 E006 핵심

Human-seeded source:
- Reddit r/living_in_korea_now — "is there a middle ground in korean work culture"
- 독립적으로 처리하면 "왜 말 안 했어?"
- 다음엔 물어보면 "이런 것까지 왜 물어봐? 알아서 해."
- 단일 실제 사건을 거짓으로 재현하지 말고, 반복되는 직장 모순 패턴을 압축 각색한다.

## 캐스팅 전역 규칙 — 갱신됨

- Gaeun / Harin / Taemin 전원 출연 의무 없음.
- 회차/컷마다 스토리 기능이 있는 인물만 사용.
- 메인 캐릭터는 0~3명 모두 가능.
- 상사, 동료, 점원, 소개팅 상대, 가족 등 조연/단역을 자유롭게 사용할 수 있음.
- 조연이 2컷 이상 반복되면 episode-local identity digest를 만든다.
- 그림체/렌더 락과 캐스트 구성은 별개다: **스타일은 고정, 캐스팅은 유동**.

Authoritative details:
- MASTER_PROMPTS.md §5
- GENERATION_PROTOCOL.md §0.5

## 시각 기준

- INSTATOON_STYLE_v2.0.
- REF_V2_D: assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
- REF_V2_E: assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg
- approved binaries outrank generalized prose.
- one panel = one image file.
- feed/carousel master 4:5, 1080×1350 unless the episode explicitly selects another output.
- L13 raster text-free; lettering comes later.

## 공통 파이프라인 실험 — AUTO_FINISH

2026-09-06부터 공통 실행 구조에 두 모드를 병렬 지원한다.

- `STANDARD`: 기존 컷별 이미지/검수/레터링 경로.
- `AUTO_FINISH`: 콘티/L8 승인과 S01 사람 앵커 승인은 유지하고, S01 PASS 뒤 후속 이미지 생성→자동 QC→분리 레터링→최종 QC→export를 내부 완주.
- 이미지와 레터링은 계속 별도 산출물로 보존.
- 자동 실패 시 `PRODUCTION_STATE.automation`에 원인을 기록하고 `STANDARD`의 `REMAINING_RENDER` 또는 `LETTERING`으로 롤백.
- AUTO_FINISH는 현재 EPISODE_PLAN에 바인딩된 `LETTERING_PLAN.json`이 없으면 유료 후속 렌더 전에 fail-closed 롤백.

구현:
- `pipeline/auto_finish.py`
- `pipeline/lettering.py`
- `schemas/lettering_plan.schema.json`
- `.github/workflows/qc.yml`의 `finish_mode`

이 변경은 **E006의 현재 승인 상태를 건드리지 않는다**. E006는 여전히 L8_AWAITING_APPROVAL이며,
새 패키지 승인→콘티/plan/manifest/lettering plan→S01 생성/사람 승인 순서를 먼저 밟는다.

## 정확한 다음 행동

1. user reviews E006 new L1-L7 package;
2. on PASS, lock the smallest story-sufficient cast;
3. build whole-episode storyboard and episode-local identity digests;
4. rebuild EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN from the approved package;
5. render S01 only and run visual/style QC before remaining frames.
