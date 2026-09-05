# SETUP_RENDER.md — 렌더 실행 설정

`pipeline/render.py`는 그림을 만드는 **유일한 정식 경로**다.
참조 이미지를 실제로 요청에 싣고, 결과를 저장하고, 무엇을 보냈는지 기록한다.
채팅 안의 내장 이미지 도구는 프로덕션에 쓰지 않는다.

파이썬 설치나 터미널은 필요 없다. 전부 GitHub 브라우저에서 한다.

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

그림을 확인한 뒤 `Actions` → `qc` → `Run workflow`

| 입력 | 설명 |
|---|---|
| slide | 방금 본 컷 번호 |
| verdict | PASS 또는 FAIL |
| note | FAIL이면 이유 한 줄 |

### 순서

```
render --slide 1  →  눈으로 확인  →  qc --slide 1 PASS
                                          ↓
                                    render --slide 2  →  qc --slide 2 PASS  →  ...
                                          ↓
                                    전 컷 PASS → stage LETTERING
```

---

## 상태 연동

이 어댑터는 별도의 상태 파일을 만들지 않는다.
`episodes/<ID>/PRODUCTION_STATE.json` 하나만 읽고 쓴다.

| 사건 | stage 전이 |
|---|---|
| S01 렌더 성공 | `RENDER_CONTRACT_READY` → `FIRST_FRAME_QC_PENDING` |
| S01 QC PASS | `FIRST_FRAME_QC_PENDING` → `REMAINING_RENDER`, 해당 컷이 회차 앵커로 등록 |
| S01 QC FAIL | `RENDER_CONTRACT_READY`로 복귀, 앵커 해제 |
| 전 컷 QC PASS | `LETTERING` |

`frame_qc` 항목은 `render_guard._require_persisted_qc`가 요구하는 형태
(`slide_id` / `status` / `inspected_output` / `attempt_id` / `artifact_sha256`)로 기록된다.

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
