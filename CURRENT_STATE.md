# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E006/README.md

## 현재 위치

큰 흐름: 수동 제작 검증 → 상태/렌더 가드 강화 → 최소 실행 경로 연결 → 독립 CLI → 웹 도구.

현재 활성 회차는 E006 "어떻게 오셨어요?"다.
E006은 L1-L7 검토 후보가 준비되어 있고, 사용자가 "단회성 외국인 주인공"이라는 CAST 결정만 승인했다.
현재 PRODUCTION_STATE = CAST_RESOLVED, L8 USER VOICE GATE = PENDING.

따라서 L10 이후 제작이나 raster generation은 현재 권한 없음.

## E006 롤백 상태

직전 채팅에서 생성된 9:16 6컷 합본은 INVALID_RENDER / STORYBOARD_REFERENCE_ONLY로 폐기한다.

하드 실패:
- L8 전체 패키지 승인 전에 작화 진입;
- E006 EPISODE_PLAN / RENDER_MANIFEST 없이 free-form 생성;
- canonical REF_V2_D/E 실제 미디어 미전달;
- canonical compiler 미사용;
- 한 컷=한 파일 규칙 위반;
- feed master 4:5 대신 9:16 합본;
- raster에 최종 한글/말풍선 직접 생성;
- 승인되지 않은 대사 추가;
- 현행 v2 그림체와 다른 generic polished webtoon 스타일.

이 이미지는 스타일 레퍼런스, 회차 앵커, LAST_KNOWN_GOOD로 절대 승격하지 않는다.

## 구조 개선 — 2026-09-06

원격 main에 다음 실행 강제를 반영했다.

- episodes/<ID>/PRODUCTION_STATE.json을 machine-facing 실행 상태 원장으로 도입.
- CAST_ONLY와 L1_L7_FULL_PACKAGE 승인을 분리.
- compile/authorize는 L8 전체승인 없이는 fail closed.
- caller의 단순 previous-frame-qc PASS 문자열은 권한 증거가 아님.
- 후속 conversation-inferred 컷은 slide/attempt/artifact SHA에 묶인 persisted QC PASS가 필요.
- active episode가 pre-render 단계여도 CI/상태 검증은 정상 동작하며, render contract가 생기기 전에는 render validation으로 오인하지 않음.
- 구조 변경 후 GitHub Actions unit tests와 active validation 단계 PASS 확인.

관련 커밋:
- f444f403697b708c3d5477a70dea32aa9f5d42a8
- 73f3570a1a992e57d6a78abee7b40e719dc08681

## 정확한 다음 행동

1. episodes/E006/README.md의 L1-L7 전체 패키지를 사용자에게 다시 제시한다.
2. 명시적 전체 승인 전에는 L10, L11, L12, L12.5, L13으로 넘어가지 않는다.
3. 승인 후에만 회차 전용 외국인 identity digest와 전체 컷 계획을 만든다.
4. E006 EPISODE_PLAN.json + RENDER_MANIFEST.json을 materialize하고 render_guard validate/compile/authorize를 거친다.
5. REF_V2_D/E를 실제 이미지 미디어로 전달하여 S01 한 컷만 text-free 4:5로 생성한다.
6. 사용자 그림체/인물 검수 PASS 뒤에만 후속 컷으로 진행한다.

## 현행 시각 기준

- INSTATOON_STYLE_v2.0.
- REF_V2_D: assets/style_refs/v2_current/REF_V2_D_MAIN_CAST_GAEUN_HARIN_TAEMIN.jpeg
- REF_V2_E: assets/style_refs/v2_current/REF_V2_E_3PERSON_INDOOR_SCENE.jpeg
- 실제 승인 이미지가 일반화된 스타일 문장보다 우선한다.
- current v2 production은 BINARY_CONDITIONED reference use가 원칙이다.

## 이전 회차

E005는 render contract가 존재하는 이전 활성 회차이며 L8 승인 상태와 구조화 입력이 보존되어 있다.
E001-E004는 각 역사/학습 기록으로 유지한다.
