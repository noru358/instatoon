# SETUP_RENDER.md — 렌더 실행 설정

이 문서는 두 운영 단계를 구분한다.

**현재: MANUAL_VALIDATION**
- 현재 일상 제작은 ChatGPT/native 수동 검증을 우선하고, 유료 API 렌더는 벤치마크/전환 준비 경로로 보존한다.
- 대화형 native 결과는 repository attempt/hash에 묶이지 않은 한 재현 가능한 production artifact로 가장하지 않는다.
- 사용자 기본 게이트는 사전 내용/콘티·계약 → S01 앵커 → 전체 무문자 래스터 세트 → 레터링/완성본이다.
- S02~마지막 컷은 각각 별도 파일로 만들되 운영자 내부 QC로 진행한다. 매 컷 사용자 승인은 기본이 아니다.

**장기: API_PRODUCTION**
- `pipeline/render.py` 계열의 explicit provider adapter가 정식 raster 경로가 된다.
- 한 요청=한 컷, 실제 참조 바이너리, 요청/결과 증거, 재시도/비용 로그를 강제한다.

AUTO_FINISH 코드는 장기 구조 검증용으로 보존하지만 현재 기본 운영에서는 사용하지 않는다.

---

## 한 번만 하는 준비

### 1. API 키 만들기

platform.openai.com 로그인 → 결제수단 등록 후 소액 충전 → `API keys` → `Create new secret key`.
만들어진 `sk-...`를 복사한다. 그 화면을 벗어나면 다시 못 본다.

ChatGPT 구독과는 **별개 과금**이다. 실제 비용은 출력 크기·품질·참조 이미지 입력량에 따라 달라진다.
계정 상태에 따라 GPT Image 사용 전 조직 인증이 필요할 수 있다.

### 2. 키를 레포에 넣기

레포 → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`

- Name: `OPENAI_API_KEY`
- Secret: 복사한 `sk-...`

키는 이후 로그에도 화면에도 찍히지 않는다.

---

## 매번 하는 일

### 컷 한 장 뽑기

`Actions` 탭 → 왼쪽 `render` → `Run workflow`

| 입력 | 설명 |
|---|---|
| slide | 뽑을 컷 번호 |
| episode | 비우면 CURRENT_STATE.md의 활성 회차 |
| dry_run | 체크하면 **과금 없이** 게이트만 돌린다 |

처음 한 번은 `dry_run`으로 확인하는 것을 권한다.
어떤 참조 이미지가 실제로 묶였는지, 프롬프트 해시가 무엇인지 로그에 전부 찍힌다.

성공하면 그림이 `episodes/<회차>/renders/slide_NN_art.png`로 레포에 자동 커밋된다.

### 검수 기록하기

`Actions` → `qc` → `Run workflow`.

`scope=frame`:
- S01 PASS는 `inspection_kind=user`로 기록한다.
- S02 이후 PASS/FAIL은 보통 `inspection_kind=operator_internal`로 기록한다.
- 이는 컷별 품질 증거이며, 사용자 승인 게이트를 뜻하지 않는다.

`scope=raster_set`:
- 모든 컷이 현재 artifact-bound PASS가 된 뒤 전체 무문자 세트를 사용자가 보고 PASS/FAIL한다.
- PASS일 때만 `LETTERING`으로 이동한다.

`finish_mode=auto_finish`은 S01 USER PASS 직후 자동 완주 실험을 선택할 때만 사용한다. MANUAL_VALIDATION 기본은 `standard`.

### 현재 순서 — MANUAL_VALIDATION

```
pre-raster content/storyboard/contracts → 사용자 승인
→ S01 한 장 → 사용자 앵커 QC
→ S02 ... 마지막 컷: 한 컷씩 생성 + 운영자 내부 QC
→ complete text-free raster set → 사용자 전체 작화 QC
→ separated lettering / final composition
→ 사용자 최종 QC
```

**한 컷=한 파일**은 유지하지만 **한 컷=한 사용자 승인**은 아니다.

현재는 `finish_mode=standard`가 기본이다.
AUTO_FINISH는 코드에서 제거하지 않으며, S01 뒤 남은 사용자 게이트를 자동 QC로 대체하는 별도 실험 경로다.

---

## 상태 연동

이 어댑터는 별도의 상태 파일을 만들지 않는다.
`episodes/<ID>/PRODUCTION_STATE.json` 하나만 읽고 쓴다.

| 사건 | stage 전이 |
|---|---|
| S01 렌더 성공 | `RENDER_CONTRACT_READY` → `FIRST_FRAME_QC_PENDING` |
| S01 QC PASS | `FIRST_FRAME_QC_PENDING` → `REMAINING_RENDER`, 해당 컷이 회차 앵커로 등록 |
| S01 QC FAIL | `RENDER_CONTRACT_READY`로 복귀, 앵커 해제 |
| 전 컷 내부 QC PASS | `RASTER_SET_QC_PENDING` |
| 전체 무문자 세트 USER PASS | `LETTERING` |

`frame_qc` 항목은 `render_guard._require_persisted_qc`가 요구하는 형태
(`slide_id` / `status` / `inspected_output` / `attempt_id` / `artifact_sha256` / `inspector`)로 기록된다.
S01의 정상 앵커 PASS는 `inspector=USER`, 후속 수동 제작 컷은 보통 `inspector=OPERATOR_INTERNAL`이다.

---

## 이 경로가 실제로 막는 것

- **참조 미전달** — 코드가 파일을 직접 열어 요청에 싣는다. "넣었다"고 신고하는 인자가 없다.
- **참조 바꿔치기** — 매 실행마다 SHA-256을 대조하고 다르면 거부한다.
- **프롬프트 즉석 재작성** — `MASTER_PROMPTS.md §12` + `EPISODE_PLAN`에서 컴파일한 것만 쓴다.
- **단계 건너뛰기** — `PRODUCTION_STATE.current_stage`가 허용하지 않으면 거부한다.
- **PASS 재사용** — 판정은 이미지 파일의 SHA-256과 attempt_id에 묶인다.
  재렌더하면 자동으로 무효가 되고, 이 파이프라인이 만들지 않은 이미지에는 판정을 못 찍는다.
- **승인된 컷 덮어쓰기** — PASS 상태의 컷은 FAIL을 먼저 기록해야 다시 렌더할 수 있다.
- **글자 굽기 / 합본** — 프롬프트에 `RASTER_TEXT: NONE`, 계약에 `panels_per_image=1`이 강제된다.

매 생성마다 `renders/attempts/<attempt_id>.json`에 프롬프트 전문, 참조 해시, 모델명,
결과 해시가 남는다. 조건별 그림체 합격률을 나중에 세어볼 수 있다.

---

## 알아둘 제약

**출력 비율.** 기본 모델 `gpt-image-2`는 유효한 임의 해상도를 받을 수 있으므로
처음부터 정확한 4:5인 `1024×1280`으로 요청한다. 결과가 4:5가 아니면 자동 크롭으로 숨기지 않고
렌더 실패로 처리한다. 정상 결과만 1080×1350으로 리사이즈한다.

**모델 이름.** 기본값 `DEFAULT_MODEL = "gpt-image-2"`.
이 모델은 참조 이미지 입력을 자동으로 high-fidelity 처리하므로 `input_fidelity` 값을 따로 보내지 않는다.
실험이 필요할 때만 `INSTATOON_IMAGE_MODEL` 환경변수 또는 CLI `--model`로 덮어쓴다.

**앵커.** 첫 PASS 컷이 이후 모든 컷 요청에 실제 이미지로 함께 들어간다.
`GENERATION_PROTOCOL §0.5`가 요구하지만 구현이 없던 부분이며, 컷별 얼굴 드리프트를 막는 장치다.

**미검증.** 이 어댑터로 실제 생성을 성공시킨 적은 아직 없다.
게이트 동작은 확인했지만 그림체 합격 여부는 첫 실주행 전까지 미측정이다.
`E006_L13_MEDIA_BINDING_001` 블로커는 첫 렌더가 성공하면 닫는다.


## 동시 실행 / stale 결과 보호

`render`와 `qc`는 같은 `instatoon-production` concurrency lock을 사용한다.
그래서 Actions끼리는 동시에 `PRODUCTION_STATE.json`을 수정하지 않는다.

또한 provider 호출이나 사람 QC가 진행되는 동안 GPT 앱 등 다른 경로에서 같은 브랜치의
`EPISODE_PLAN`, `RENDER_MANIFEST`, `PRODUCTION_STATE`, canonical prompt/reference가 바뀌면
해당 결과를 새 계약 위에 rebase해 밀지 않는다. push 직전에 origin을 다시 확인하고 관련 입력이
달라졌으면 그 render/QC를 **STALE로 폐기(exit 2)** 한다. unrelated commit만 바뀐 경우에만 rebase한다.


---

## 실험 모드: anchor-gated AUTO_FINISH

목적은 STANDARD의 **S01 이후 전체 래스터 세트/레터링·최종 사용자 게이트까지 자동 QC로 대체**하는 것이다. 콘티/대본 승인과 S01 앵커의 사람 승인은 그대로 둔다.

### 활성화 조건

AUTO_FINISH는 아래가 모두 참일 때만 시작한다.

1. S01이 이 렌더 어댑터가 만든 실제 파일이고 사람 QC PASS가 해시/attempt에 묶여 있음;
2. S01이 `episode_anchor`로 등록됨;
3. stage가 `REMAINING_RENDER`;
4. 회차에 `LETTERING_PLAN.json`이 있고 현재 `EPISODE_PLAN.json` Git blob SHA에 묶여 있음.

4번이 중요한 이유는 자동 완주 도중 새 대사나 새 레이아웃을 즉석에서 만들지 않기 위해서다.
레터링 문구/배치는 whole-episode visual/text plan에서 미리 확정한다.

### LETTERING_PLAN

스키마: `schemas/lettering_plan.schema.json`.

각 텍스트 항목은 최소 다음을 가진다.

- `text_id`
- `kind`: caption / speech / chat / sfx
- `text`: 확정 문구
- `box`: `[x, y, width, height]` 0~1 정규화 좌표
- 필요할 때 `tail_to`, `align`, 글자 크기/패딩 옵션

### 이미지와 레터링 분리

AUTO_FINISH도 레이어 분리를 유지한다.

- 원본 그림: `renders/slide_NN_art.png`
- 투명 레터링 레이어: `lettering/slide_NN_overlay.png`
- 합성 완성본: `exports/slide_NN_final.png`

`pipeline/lettering.py`는 원본 art를 덮어쓰지 않는다. 한글은 GitHub Actions에서 설치한 시스템 Nanum 폰트로
결정적으로 합성하며, 폰트 바이너리는 저장소에 커밋하지 않는다.

### 자동 이미지 QC

`pipeline/auto_finish.py`는 각 후속 컷마다 현재 후보 + 사람이 승인한 S01 앵커 + canonical style refs +
해당 slide contract를 vision QC에 함께 보낸다. 명확한 PASS만 정상 frame_qc PASS로 저장한다.

- 기본 confidence gate: 0.88
- 컷당 기본 최대 시도: 3
- 회차 전체 후속 render attempt 기본 상한: 10
- STOCHASTIC 실패만 동일 canonical 입력으로 재시도
- PLAN_OR_PROMPT / 비재시도형 실패는 즉시 롤백

자동 PASS도 artifact SHA-256과 render attempt_id에 묶인다.

### 롤백

예상 가능한 실패는 워크플로 전체를 막아놓지 않고 `PRODUCTION_STATE.json`에 이유를 남긴 뒤:

- 이미지/자동 시각 QC 실패 → `mode=STANDARD`, stage `REMAINING_RENDER`
- 레터링/최종 레이아웃 QC 실패 → `mode=STANDARD`, stage `LETTERING`

이미 합격한 컷은 유지하고 실패 컷 이후를 수동 표준 경로로 이어간다.
AUTO_FINISH용 별도 mutable state 파일은 만들지 않는다.


---

## 장기 API_PRODUCTION provider 전략

목표는 특정 벤더를 영구 하드코딩하는 것이 아니라 provider adapter 뒤에서 교체 가능하게 만드는 것이다.

초기 벤치마크 후보:
- image render: GPT-Image-2;
- vision QC: DeepSeek Flash Vision;
- lettering: existing deterministic Python compositor.

권장 라우팅 원칙:
- image generation은 medium/default quality부터 시작;
- QC 실패 또는 anatomy-high-risk 컷만 필요한 경우 고품질/재시도 승격;
- vision QC보다 먼저 로컬 QC-0(파일/비율/패널/텍스트 계약)을 수행;
- 첫 3개 API 완성 회차에서 실제 provider/model, attempts, first-pass rate, repair reasons, cost를 기록;
- 예상 편당 달러 숫자를 영구 정책으로 하드코딩하지 않고 실측 후 예산 cap을 결정한다.

장기 API_PRODUCTION의 자동 경로 UX는:
`콘티/계약 승인 → 레퍼 확인 → S01 승인 → 완성본`.

현재 STANDARD MANUAL_VALIDATION의 사용자 UX는:
`콘티/계약 승인 → S01 승인 → 전체 무문자 작화 승인 → 레터링/완성 승인`.
API는 사용자가 매번 조작하는 외부 툴이 아니라 내부 격리 렌더 엔진이다.
