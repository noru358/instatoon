# AUTOMATION_TRANSITION.md

Updated: 2026-09-06
Status: MANUAL_VALIDATION ACTIVE + API_PRODUCTION ROADMAP + AUTO_FINISH PRESERVED

## 0. 목표와 판단

목표는 실제 인간 소재 → 대본/콘티 → 승인 그림체로 그린 컷 → 대사 합성 → 완성 만화를 하나의 실행 경로로 연결하는 것이다.
ChatGPT 대화 자체를 자동 조작하는 것이 아니라, 앱 밖에서도 같은 입력과 승인 상태로 이어지는 생산기를 만든다.

현재는 **실제 렌더 어댑터 + 영속 상태 게이트 + 실험적 AUTO_FINISH 오케스트레이터**까지 연결돼 있다.
후속 컷 자동 vision QC와 deterministic lettering/export 경로도 코드로 존재하며 STANDARD 수동 경로를 병렬 유지한다.
다만 이 AUTO_FINISH 경로로 현행 v2 회차를 처음부터 끝까지 실제 유료 provider 호출로 완주한 표본은 아직 없으므로,
정확한 무오류율을 산출할 자료는 없다. 리포에는 현행 v2 기준으로 전체 순서를 통과한 완성 회차가 보존돼 있지 않다.
E001 최종 PNG/SVG는 v1 역사 자료이며, E004 스타일 합격 기록은 회차 전체 합격이 아니다.
이는 과거 대화에서 좋은 이미지가 전혀 없었다는 뜻이 아니라, 새 환경에서 재현·계측할 증거가 부족하다는 뜻이다.

## 1. 이번 감사에서 직접 확인한 것

기준 원격 커밋: `2e13a3f7cc568646e4e5a7fd61bef42ce5525dbc`.
범위: root 문서 10개, E001–E005 제작 기록과 구조화 입력, 코드/테스트/CI/스키마,
현재 실제 D/E 이미지, 상위 AutoPipeline의 미디어 가드와 submodule 구조.
새 이미지 생성이나 유료 API 호출은 하지 않았다.

| 확인 | 결과 / 의미 |
|---|---|
| 기존 테스트 9개 + 활성 E005 validate | 모두 PASS. 입력 검사 통과를 의미하며 이미지 품질 근거는 아님 |
| 그림·QC 파일 없이 최종 컷에 caller `PASS` 제출 | S07 AUTHORIZED. 순서/검수 상태를 저장·대조하지 않음 |
| 격리한 복사본에서 필수 JPEG 내용을 비이미지 바이트로 교체 | 기존 validate PASS. 당시 expected_hash가 null이며 실제 해시 계산도 없었음 |
| L8 확인 코드 | 없음. E005 승인은 README 기록에 있고 가드는 읽지 않음 |
| 렌더러 호출 코드 | 자식/부모 가드 모두 없음. 미디어 전달 증거도 호출자가 제출 |
| 스키마 파일 | 존재하나 가드가 전체 JSON Schema를 로드·검증하지 않음 |
| 회차 보조 앵커 | 문서는 필수 재사용, E005 매니페스트는 D/E 두 이미지뿐. 등록/전달 경로 미구현 |
| 대사·레이아웃 | E005 README에 대사 의도/일부 문장, JSON에는 확정 대사 객체·좌표 없음. L14 자동 합성기 없음 |
| 현행 native 도구 | 이번 Work 도구에 명시적 prompt와 referenced_image_paths가 있음. 옛 'native 불가' 안내는 현행 능력 판정이 아님 |
| 시각 기준과 문장 | D/E의 태민 고유 눈매와 제한적 표면 디테일을 공통 원형 눈·절대 무질감 문장이 덮을 위험 |

## 2. 핵심 오류와 해결 방향

### A. 단계 누락 / 다른 회차 진행 — 우선순위 1

문서 안에 E003/E004/E005 현재 안내와 중복된 다음 행동이 섞여 있었다.
가드는 계획/매니페스트 일치만 확인하므로 승인 전 대본을 만들어도 L8을 통과했는지 알 수 없다.

이번 정리: CURRENT_STATE의 현재 회차/다음 행동을 하나로 통일하고 과거 기록을 비활성으로 표시했다.
중복 게이트를 제거하고 각 규칙의 소유 문서를 README에 명시했다.

필요한 실행 구현:
- DB의 run/stage 상태로 순서를 결정한다. Markdown을 여러 군데 읽고 다음 단계를 추측하지 않는다.
- 현재 검수 패키지의 해시와 사용자 L8 승인 기록을 연결한다.
- 대본·비트가 실질적으로 바뀌면 해당 승인을 재검수한다. 단순 파일 포맷 변경으로 불필요하게 승인을 무효화하지 않는다.
- 한 번 승인된 같은 패키지는 재승인을 요구하지 않는다.
- 상태가 허용한 다음 작업만 실행하는 단일 진입점을 둔다.

### B. 참조 미전달 / 그림체 이탈 — 우선순위 1

파일 존재·파일 열람·실제 생성 입력은 서로 다르다. 현재 CLI는 마지막 항목을 자기신고로 받는다.
따라서 필수 참조라고 적어도 생성 호출에서 이미지를 빠뜨릴 수 있다.

이번 정리: 로컬 필수 미디어에 SHA-256을 기록하고 실제 파일과 대조하도록 고쳤다.
현재 인터페이스의 입력 능력으로 경로를 선택하도록 낡은 native 단정을 제거했다.

필요한 실행 구현:
- 어댑터가 필수 참조 바이트/경로를 로드하고 동일 요청에 컴파일 프롬프트와 이미지 입력을 결합한다.
- supplied evidence는 그 요청에서 도출한다. 모델이 '넣었다'고 쓴 값을 증거로 삼지 않는다.
- 호출 직전 계획/프롬프트/참조의 스냅샷 해시와 실제 요청을 기록하고 결과 ID/파일에 연결한다.
- 공급자가 명시적 이미지 입력·참조 수를 지원하는지 실제 인터페이스 기준으로 검사한다.
- native/direct 우선 원칙을 유지한다. 연결돼 있다는 이유만으로 Higgsfield 등 외부 렌더러를 소환하지 않는다.
- 실제 이미지 입력은 충실도 보장의 필요 조건이다. 그림체 합격 자체는 이미지 비교로 확인한다.

### C. 공통 문장이 승인 이미지와 충돌 / 컷마다 얼굴 변화 — 우선순위 1

실제 승인 이미지는 최상위 시각 기준이다. 눈 크기·눈꺼풀·표정까지 하나의 문장으로 강제하면 인물 고유 특징이 바뀐다.
또한 회차 전용 인물의 글 설명만 매번 전달하는 것은 얼굴 연속성의 충분한 증거가 아니다.

이번 정리: 승인 이미지가 일반화된 프롬프트보다 우선하도록 정합성을 맞췄다.
공통 문장이 고유 눈매·자연 표정·승인된 선의 성질을 재설계하지 않도록 컴파일 문장에도 반영했다.
스타일 참조에 있는 세 사람·거실·구도를 새 회차에 그대로 복제하지 않도록 역할을 명시했다.

필요한 실행 구현:
- 첫 실제 회차 컷을 스타일/인물 기준으로 확인하고, 승인 이미지를 후속 컷의 보조 실제 미디어로 등록한다.
- 원래 그림체 참조 + 승인된 회차 인물 이미지 + 현재 컷 장면을 역할별로 전달한다.
- 주연은 선택한 인물만, 단역은 대본에서 만든 동일 identity digest를 유지한다.
- 일회성 인물의 별도 캐릭터 시트를 매번 만들 필요는 없다.
- 앵커는 새 컷의 구도/동작을 고정하지 않는다. 실패한 이미지를 다음 참조로 연결하지 않는다.
- E004 스타일 승인 앵커는 파일이 리포에 없으므로 해당 회차 재개 시 복구/재승인한다.

A/B/C 원본 누락은 보존 공백이지만 D/E가 존재하는 E005의 당장 필수 차단 사유는 아니다.
참조를 더 모으거나 학습 모델부터 만드는 것을 1순위 해결책으로 삼을 근거는 아직 없다.
먼저 지금 가진 승인 이미지가 실제로 들어가는 경로부터 검증한다.

### D. 그림은 있는데 읽을 수 있는 완성 만화가 없음 — 우선순위 1

무문자 그림만 생산하면 폰 오발송·답장·층수 같은 핵심 정보가 전달되지 않는다.
현재 E005의 구조화 계획에는 컷별 최종 한국어 대사와 말풍선 위치가 없고 L14 합성 코드도 없다.

필요한 실행 구현:
- 승인 대사를 한 곳에 보존하고 컷마다 text_id, 역할, 화자, 문장, 위치, 읽기 순서를 구조화한다.
- 폰 화면/숫자도 중요한 이야기 텍스트면 같은 레이어에서 처리한다.
- SVG 또는 동등한 편집 가능한 레이아웃으로 한글·말풍선을 결정적으로 합성한다.
- 입력 캔버스와 최종 1080×1350 좌표 변환을 명시하고, 얼굴/손/핵심 소품을 자르거나 이미지를 늘리지 않는다.
- 줄바꿈·최소 글자 크기·넘침·읽기 순서를 코드로 검사하고 휴대폰 크기로 최종 확인한다.
- 최종 PNG와 편집 가능한 원본을 함께 저장한다. 배경·인물까지 전부 벡터 분리하는 것은 완료 조건이 아니다.

### E. 검수 PASS가 실제 그림과 연결되지 않음 — 우선순위 1

지금 `--previous-frame-qc PASS`는 어느 파일을 누가 봤는지 확인하지 않는다.
전 컷 승인 문자열만으로 파일이 없는 다음 컷에 갈 수 있고, 기존 잘못된 결과를 자동 회수하지도 못한다.

필요한 실행 구현:
- QC verdict를 run_id / slide_id / attempt_id / 입력 버전 / 결과 파일 해시에 연결한다.
- 실제 파일을 확인한 기록만 다음 단계에 사용한다. 다른 회차·다른 시도·수정 전 파일의 PASS는 재사용하지 않는다.
- 첫 컷의 그림체/인물 합격 후 후속 컷을 진행하고, 후속 컷도 개별 이미지 검수를 거친 뒤 최종 내보낸다.
- explicit payload는 첫 컷 뒤 묶음 생성 가능, inferred payload는 매 컷 순차 검수라는 기존 정책을 유지한다.
- 자동 시각 판단은 후보 판정이며 취향 합격의 절대 증명이 아니다.
- 국소 오류면 좋은 원본에서 해당 부분만 수정한다. 공통 오류면 공통 입력을 고치고 영향받는 컷만 다시 만든다.

## 3. 이번 정리의 범위

수정 완료:
- 현재 상태/회차 혼선 및 중복된 게이트 설명 정리, 옛 회차를 비활성 기록으로 구분;
- 승인 이미지 우선, 인물 눈매와 자연 표정 보존, 스타일/구도/배우 참조 역할 명료화;
- 필수 로컬 미디어 SHA-256 고정·실제 대조;
- Active episode 중복 선언 차단;
- 컴파일 결과에 실제 story beat 포함, 미치환 INSERT 표식 제거;
- 구현된 검사와 아직 없는 실행기/검수/합성 기능 구분.

당시 감사 시점에 미구현이었던 항목 중 §7/§8에서 후속 구현된 것:
- 이미지 provider 호출 어댑터;
- L8/이미지 QC/실행 순서의 영속 상태;
- 회차 앵커 등록/후속 참조 전달;
- 한글 deterministic 합성기·완성본 내보내기;
- bounded retry와 STANDARD rollback.

여전히 후속 과제:
- 자동 소재 수집·대본 단계의 외부 독립 실행기;
- 실제 비용 계측/회차 예산 hard stop;
- 장기 운영용 DB/큐로의 승격과 중복 호출 방지 강화.

전체 JSON Schema 검증 연결, 상태 enum/캐스팅 참조 정합성 강화 등은 실제 실행기 입력 경계에서 함께 처리한다.
각 필드를 위한 문서나 승인 단계를 따로 늘리지 않는다.

## 4. 외부 도구의 최소 구조

| 구성 | 책임 |
|---|---|
| Instatoon 리포 | 인간 소재/대사/그림체 규칙, 프롬프트, 승인 참조, 프로젝트별 입력·시각 QC 기준 |
| AutoPipeline 엔진 | 실행 순서·승인·재시도·시간 제한·도구 호출·비용·저장·다음 작업 결정 |
| 모델/공급자 어댑터 | 제한된 단계 입력으로 작업, 명시적 프롬프트+미디어 전달, 결과/요청 증거 반환 |
| 런타임 DB | run/stage/attempt, 승인, QC, 입력·출력 해시, 오류·재시도·비용 기록 |
| 아티팩트 저장소 | 생성 이미지, 편집 원본, 최종 내보내기; 초기는 로컬 디렉터리 가능 |
| UI | 시작, 검수 승인, 문제 컷 수정, 결과 다운로드 |

초기에는 Python CLI + SQLite + 로컬 아티팩트 폴더면 충분하다.
서버 워커·큐·오브젝트 저장소는 실제 병렬 작업/운영 요구가 생길 때 추가한다. Git을 작업 큐로 쓰지 않는다.
공급자 공식 API를 우선하고, MCP는 환경 간 연동이 유용할 때 사용한다. 브라우저 자동화는 가능하고 허용된 경우의 격리된 최후 어댑터다.
ChatGPT Work의 도구 입력 가능 여부는 독립 API의 모델·비용·품질 동등성을 증명하지 않는다. 선택한 외부 API에서 별도 확인해야 한다.

### 현행 운영 모드와 단일 컷 출력

사용자 검수 시점과 참조 배분은 GENERATION_PROTOCOL §0.5를 단일 기준으로 삼는다.
각 render job은 slide 하나와 하나의 출력 파일에 대응한다. `format.panels_per_image=1`, `delivery_mode=SEPARATE_FILES`를 계획/매니페스트에서 검사한다.
전체 에피소드 콘티를 한 이미지 호출에 보내지 않는다. 여러 작업의 묶음 실행은 각각 독립 요청/파일이며 합본 이미지 생성을 뜻하지 않는다.
향후 결과 검사기는 파일 수/slide ID 대응과 실제 이미지의 단일 패널 여부를 검사해야 한다. 현재 가드는 입력 선언만 검증한다.

### 실행 상태와 입력

UI의 다섯 묶음은 README 표를 따른다. 엔진은 다음 상태를 저장한다.

SOURCE_CANDIDATES → SOURCE_SELECTED/NORMALIZED → STORY_PLANNED → DIALOGUE_DRAFTED/HUMANIZED
→ USER_VOICE_GATE → STORYBOARD/CAST/EPISODE_IDENTITY_READY → VISUAL_PLAN_READY
→ PLAN/MANIFEST_BOUND → PREFLIGHT_VALIDATED → FIRST_FRAME_RENDER/QC
→ REMAINING_RASTER → VECTOR_LETTER → FINAL_QC → HUMAN_TASTE_GATE → EXPORT_READY.
PUBLISHED / PERFORMANCE_RECORDED는 내보내기 이후의 선택적 운영 단계다.

새 인물이 2컷 이상이면 identity digest를 내부에서 만든다. 별도 인간 승인 단계는 추가하지 않는다.
L1–L16 역할은 유지하되 한 실행자가 순차 수행할 수 있다. 별도 에이전트 수가 품질 기준은 아니다.
모든 완료 단계는 stage / role / actual actor / input & provenance / output / status / QC / next를 기록한다.

### 공통 media contract

AutoPipeline의 MEDIA_INPUT_CONTRACT가 공통 선언/능력/공급 모델을 소유한다.
자식의 RENDER_MANIFEST.media_requirements를 공통 job requirements로 매핑한다.

필드: requirement_id, role, media_type, source_id, conditioning, required, expected_hash.
역할 예: style, character_identity, episode_anchor, repair_base, location_anchor.
부모 엔진에 REF_V2 이름이나 특정 회차 분기를 하드코딩하지 않는다.

현행 CLI 필드: `--renderer-explicit-media`, `--supported-media-type`, `--supplied-media`.
`--style-media-bound` / `--episode-anchor-bound`는 현행 CLI에 존재하지 않는다.
실행기 도입 시 실제 요청에서 공급 증거를 생성하고 별도 자기신고 플래그로 돌아가지 않는다.

## 5. 구현 순서와 완료 조건

1. **승인된 E005 한 편의 제작 경로 연결.** 신규 소재 발굴부터 다시 하지 않는다.
   컴파일된 S01 + 실제 D/E → 이미지 → 검수/앵커 → 후속 컷 → 한글 합성 → 최종 파일까지 연결한다.
   동시에 최소 실행 상태/승인/실패 기록을 저장한다. 문서 17단계를 모두 대형 프레임워크로 구현할 필요는 없다.
2. **소재·대본 단계를 같은 엔진 앞에 연결.** 실제 출처·원문 말투/특이 디테일과 각색 범위를 보존한다.
   현재 L8 승인은 유지한다. 소재를 못 찾았다고 인간 출처를 꾸며 쓰지 않는다.
3. **독립 CLI에서 재개 가능한 실행.** 대화 기억 없이 시작·상태 조회·승인·컷 수정·내보내기 가능해야 한다.
   예시: run / status / approve voice-gate / approve taste-gate / retry --slide --scope / export.
4. **그 경로 위에 웹 화면.** 검수와 다운로드에 필요한 UI부터 붙이고, 무인 게시/성과 대시보드는 뒤로 미룬다.

최소 반복 검증 제안은 같은 그림 20회가 아니라 서로 다른 구성의 완성 회차 3편이다.
예: 실내 대화, 동작·소품 중심, 장소/의상이 바뀌는 이야기. 선택한 API/모델 버전을 기록한다.
이는 초기 결함을 찾는 표본이며 3편 성공으로 통계적 무오류를 주장하지 않는다.

측정:
- 필수 이미지 누락 생성 호출 수;
- 승인 없이 넘어간 단계 수;
- 그림체 1차 합격 컷 / 전체 컷;
- 얼굴/소품/대사 오류로 재작업한 컷;
- 사용자 개입 횟수, 회차당 시간·비용;
- 재시작 후 중복 과금 없이 이어졌는지;
- 최종 순서·한글 가독성·편집 원본 존재.

## 6. 운영 경계와 과잉 설계 방지

- 현재 인간 게이트: L8 대본, 합의한 시각 검수, 최종 취향/게시, 중요한 스타일 변경.
- 같은 승인에 반복 확인을 요구하지 않고 명시 승인 범위를 저장한다.
- 유료 작업에는 공급자/요청 ID, 시도 횟수, 예상·실제 비용(알 수 있는 경우), 회차 예산과 중단 한도를 기록한다.
- 로컬 수정과 공통 입력 수정을 구분하고 실패한 재시도에서 연쇄 생성하지 않는다.
- 품질 판단은 이야기 이해, 합의 그림체, 인물/소품 연속성, 대사 가독성에 집중한다.
- 수집 소재에 맞는 말투·이상한 디테일을 살리고, QC가 재미를 평균적인 교훈으로 바꾸지 않게 한다.
- 성과는 주제/길이/훅 실험의 입력이며 그림체·목소리·주연 정책을 자동 변경하지 않는다.
- 규칙은 소유 문서에 갱신하고 새 handoff/락/예외 파일을 계속 붙이지 않는다.


## 7. Implemented short-term state gate — 2026-09-06

The repository now has a fail-closed `PRODUCTION_STATE.json` sidecar contract and render_guard enforcement.

Implemented now:
- full L8 approval is distinct from CAST_ONLY / other partial decisions;
- compile/validate require persisted full-package L8 approval;
- render authorization requires an allowed production stage;
- caller-supplied `PASS` text no longer authorizes continuation;
- conversation-inferred slide N requires persisted QC PASS for slide N-1 bound to slide_id + attempt_id + artifact SHA-256;
- explicit-payload continuation requires persisted first-frame QC.

This sidecar is intentionally a short-term bridge. The future AutoPipeline runtime DB should preserve the same invariants and become the sole mutable execution-state authority.


## 8. 2026-09-06 구현 델타 — anchor-gated AUTO_FINISH 실험

이 절은 위 감사 시점의 “미구현” 문구보다 최신 구현 상태다. 과거 진단은 원인 기록으로 보존하되,
현재 실행 가능 여부는 이 절과 실제 코드가 우선한다.

### 승인 토폴로지

두 운영 모드를 공통 구조로 병렬 지원한다.

**STANDARD**
- 기존 수동 경로를 그대로 유지한다.
- L8 승인 → S01 사람 QC → 후속 컷 render/QC → LETTERING → final QC/export.

**AUTO_FINISH (experimental default at the S01 QC action)**
- L8/콘티 패키지 승인 유지;
- S01 앵커는 반드시 사람이 실제 출력 이미지를 보고 PASS;
- 그 PASS 이벤트 이후에만 내부 자동 완주를 시작;
- 후속 raster는 기존 `pipeline/render.py`를 그대로 사용;
- 자동 vision QC가 후속 컷을 보수적으로 검사하고 artifact/attempt에 묶인 PASS만 기록;
- 확정 `LETTERING_PLAN.json`을 `pipeline/lettering.py`가 별도 레이어로 합성;
- 최종 레이아웃 vision QC PASS 후 `EXPORT_READY`.

AUTO_FINISH는 이미지와 레터링을 하나의 생성 호출로 합치지 않는다.

### 상태 계약

두 모드 모두 mutable authority는 `episodes/<ID>/PRODUCTION_STATE.json` 하나다.
AUTO_FINISH는 선택적 `automation` 객체만 추가한다.

핵심 필드:
- `mode: AUTO_FINISH | STANDARD`
- `status: RUNNING | COMPLETED | ROLLED_BACK`
- S01 human-PASS trigger와 anchor hash
- max attempts / confidence threshold
- event log
- last_error / rollback stage
- final QC report

QC 상세 증거는 artifact 쪽 JSON으로 남기되 다음 단계 권한을 결정하는 두 번째 상태 저장소로 사용하지 않는다.

### 자동 검수와 재시도

자동 검수는 취향 판단을 대체하는 절대적 진실이 아니라 **앵커 승인 이후의 반복 결함 탐지기**다.
따라서 fail-open이 아니라 fail-closed다.

- PASS + confidence threshold 충족 + critical failure 없음일 때만 자동 PASS;
- 일반 생성 노이즈로 분류된 STOCHASTIC 실패만 동일 canonical 입력으로 컷당 최대 3회;
- 회차 전체 후속 render attempt도 기본 10회로 제한해 연쇄 비용 폭주를 막음;
- cast/scene/prompt/contract 수정이 필요해 보이는 실패는 반복 생성하지 않고 STANDARD로 복귀;
- 실패한 이미지는 episode anchor나 새로운 authority로 승격하지 않는다.

### 레터링 입력 계약

자동 완주에는 `LETTERING_PLAN.json`이 필요하다. 이는 앵커 승인 이후 새 창작을 추가하기 위한 파일이 아니라,
콘티/whole-episode visual-text plan에서 이미 확정된 카피와 배치를 실행 가능한 형태로 저장하는 계약이다.

스키마: `schemas/lettering_plan.schema.json`.

합성 산출물은 항상 분리된다:
- art raster;
- transparent lettering overlay;
- final composite.

### 롤백 계약

AUTO_FINISH 실패 시 표준 모드를 삭제/재설계하지 않는다.

- remaining raster 또는 자동 frame QC 실패 → `STANDARD / REMAINING_RENDER`;
- lettering 또는 final layout QC 실패 → `STANDARD / LETTERING`;
- 이미 유효한 PASS + hash-bound artifact는 보존;
- 오류 원인과 마지막 자동 이벤트를 상태에 기록.

이 구조 때문에 실험을 폐기하더라도 데이터 포맷/렌더러를 다시 갈아엎을 필요 없이
`.github/workflows/qc.yml`에서 `finish_mode=standard`를 선택하면 기존 공정으로 즉시 복귀한다.


### 후발 반복 인물의 보조 identity anchor

S01에 없는 episode-local 인물이 뒤 컷에서 처음 등장하고 이후에도 반복될 수 있다.
AUTO_FINISH는 그 인물의 `appears_in`을 읽어 **첫 QC PASS 등장 컷**만 character-specific identity anchor로 등록한다.
후속 해당 인물 컷에는 S01 episode anchor와 함께 이 보조 앵커를 실제 미디어로 전달한다.

- 캐릭터 이름 하드코딩 없음;
- 2컷 이상 반복되는 episode-local 인물만 대상;
- 실패 이미지 승격 금지;
- 원본 anchor slide가 나중에 FAIL 처리되면 매핑도 제거;
- S01 전체 회차 앵커는 계속 고정 유지.


## 9. 2026-09-06 operating decision — MANUAL_VALIDATION now, API_PRODUCTION later

The E007 native-chat continuation experiment changed the immediate operating policy.

### What failed

The user-provided reference images were not the failure source.
S01 could be visually acceptable, but after S01 approval the long conversational native image context repeatedly produced:
- one six-panel comic page instead of one slide file;
- baked Korean dialogue / labels;
- small-panel face/hand degradation;
- recurring content drift because the renderer saw the global episode context.

This means the current chat-native path is useful for taste/visual experiments but is not a reliable isolated batch renderer.

Repeated MULTI_PANEL / BAKED_TEXT after a single-slide instruction is classified as a **renderer/context isolation failure**, not stochastic noise.
Do not keep spending retries on that path.

### Immediate operating mode

Until the image API/provider adapter is connected:
- STANDARD / manual validation is the default;
- every material stage is explicitly user-reviewed;
- every raster slide is generated and reviewed separately;
- lettering is separate and reviewed separately;
- final export is reviewed separately;
- AUTO_FINISH remains implemented but is dormant by default.

This is intentionally slower. The purpose is to validate that each stage and contract actually works before paying for automated API runs.

ChatGPT subscription/native generation can be used for temporary manual tests where useful.
A native output that is not persisted with an attempt/hash is not a machine-authoritative anchor even if the user likes it.

### Long-term provider architecture

The production engine should be provider-neutral.

Initial benchmark candidates:
- **image renderer:** GPT-Image-2;
- **vision QC:** DeepSeek Flash Vision;
- **lettering:** deterministic Python compositor already implemented.

These model names are starting candidates, not permanent pipeline constants.

Provider adapter responsibilities:
1. accept only the compiled contract for one slide;
2. load the exact required media binaries;
3. issue one isolated provider request;
4. persist request/model/media/output evidence;
5. return cost/usage where available;
6. never infer the next slide or the whole episode from conversation state.

QC architecture:
- QC-0 local/machine contract first: file mapping, aspect/dimensions, one-panel, no baked semantic text where detectable;
- QC-1 vision style/identity;
- QC-2 vision anatomy/scene;
- retry only the failing slide;
- hard renderer/context failures do not receive blind stochastic retries.

### Cost/quality policy

Do not optimize on sticker price per image alone.
Measure **accepted final slide cost**:
`total image generation spend / number of accepted slides`.

Log:
- provider/model;
- quality tier;
- attempts;
- first-pass result;
- retry/repair reason;
- QC result;
- actual usage/cost if the provider exposes it.

Use the first three fully API-produced episodes to establish:
- first-pass acceptance rate;
- mean attempts per accepted slide;
- mean episode cost;
- anatomy-high-risk failure rate;
- style/identity failure rate.

Only then set the production budget cap.

The current working hypothesis is medium/default image quality first, with higher-cost generation reserved for QC failures or anatomy-high-risk slides. This is a benchmark hypothesis, not a hardcoded rule.

## 10. E007 handoff implication

E007 is the manual validation episode.

Already approved:
- L1-L7;
- Gaeun/Harin/Taemin cast for this episode;
- six-slide storyboard/dialogue intent;
- REF_V2_D + REF_V2_E as current visual authorities.

Not yet machine-authoritative:
- chat-native visually approved S01, because it lacks repository attempt/hash binding.

Invalid:
- all post-S01 six-panel/baked-text native continuation outputs.

Next session starts by serializing the approved E007 package into EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN and asking the user to manually approve the structured contracts/preflight before any further raster work.
