# instatoon

실제 사람이 쓴 인터넷 소재 → 대본/콘티 → 승인된 그림체의 만화 → 편집 가능한 대사 합성 → 검수/내보내기.
최종 목표는 ChatGPT 대화 기억 없이 실행되는 독립 도구다.

현재는 **수동 제작 규칙 + 일부 입력 검증 코드** 단계다. 완성된 자동 생산기는 아니다.
현재 제작 위치는 [CURRENT_STATE.md](CURRENT_STATE.md), 구현 현황·진단·외부화 순서는 [AUTOMATION_TRANSITION.md](AUTOMATION_TRANSITION.md)를 따른다.

## 작업 시작

1. 이 파일과 CURRENT_STATE.md에서 활성 에피소드와 현재 작업을 확인한다.
2. `Active episode: NONE`이면 정상적인 fail-closed idle 상태다. 기존 회차를 임의로 복구하지 말고 SOURCE_STORY_PIPELINE.md의 L1-L7부터 새 회차 후보를 준비한다.
3. 활성 회차가 있을 때만 해당 README/EPISODE_PLAN/RENDER_MANIFEST를 읽는다.
4. SOURCE_STORY_PIPELINE.md, MASTER_PROMPTS.md, STYLE_LOCK.md, REFERENCE_SET.md, VISUAL_GRAMMAR.md, GENERATION_PROTOCOL.md와 필요한 **실제 이미지**를 확인한다.
5. 제작 직전 `python pipeline/render_guard.py validate`를 실행한다.

외부화 작업일 때만 AUTOMATION_TRANSITION.md, 환경 이동·갱신 시 WORKFLOW_PROTOCOL.md를 추가로 읽는다.
단계별로 필요한 입력을 사용하고, 전체 대화·과거 실패 기록을 이미지 프롬프트에 통째로 넣지 않는다.

## 다섯 작업 묶음

| 작업 | 기존 단계 | 결과 |
|---|---|---|
| 소재 수집 | L1–L3 | 실제 출처, 살릴 디테일·말투, 각색 범위 |
| 대본 작성·사용자 검수 | L4–L9 | 비트와 자연스러운 대사, L8 명시 승인 |
| 콘티·그림 | L10–L13 | 전체 컷 계획, 실제 참조 이미지가 전달된 그림 |
| 대사·말풍선 합성 | L14 | 편집 가능한 글자/말풍선과 최종 이미지 |
| 검수·출력 | L15, 이후 L16 | 순서·그림체·가독성을 확인한 만화; 성과는 후속 업무 |

이는 기존 단계의 표시를 묶은 것이며 L8 승인이나 작업 순서를 없애지 않는다.
한 실행자가 여러 역할을 맡을 수 있다. 별도 에이전트 실행을 의미하지 않는다.

## 기준의 소유자

| 내용 | 단일 소유 문서 |
|---|---|
| 실제 승인 그림체·인물 기준, 참조 역할/파일 | REFERENCE_SET.md와 지정된 승인 이미지 |
| 생성기에 보낼 스타일 문장 | MASTER_PROMPTS.md, 컴파일용 §12 |
| 그림체 판정 경계 | STYLE_LOCK.md |
| 소재·대사·캐스팅·L8 승인 | SOURCE_STORY_PIPELINE.md |
| 컷 구성·비율·대사 배치 | VISUAL_GRAMMAR.md |
| 생성·참조 전달·연속성·수정·QC | GENERATION_PROTOCOL.md |
| 현재 에피소드·다음 행동 | CURRENT_STATE.md |
| 회차별 내용 | episodes/<ID>/README.md 및 JSON |
| 갱신·환경 이동 | WORKFLOW_PROTOCOL.md |
| 구현 현황과 외부화 설계 | AUTOMATION_TRANSITION.md |

사용자의 명시 지시가 우선이다. 시각적 충돌은 승인 이미지로 판단하고, 공통 문장이 인물 고유 눈매·표정을 덮어쓰지 않게 고친다.
에피소드의 장면·배우·의상 지시는 이야기 내용을 정하며 공통 그림체를 재설계하지 않는다.
과거 회차와 `archive/pre_redesign/`은 현행 실행 지시가 아니다. 활성 에피소드는 CURRENT_STATE의 단일 `Active episode:` 줄로만 결정한다. 값이 `NONE`이면 렌더/auto-finish는 차단되며, L8 사용자 승인 뒤 새 회차 패키지를 만들 때만 활성화한다.

## 고정된 제작 원칙

- 옴니버스. Gaeun/Harin/Taemin은 선택 가능한 주연이며 매번 강제하지 않는다.
- 새 작품은 새 인간 소재부터 시작한다. 순수 창작은 SOURCE_STORY_PIPELINE의 예외 조건을 따른다.
- 학습 단계에서는 L1–L7 결과를 제시하고 L8 사용자 승인 후에 콘티·그림으로 넘어간다.
- INSTATOON_STYLE_v2.0. v1 이미지는 역사 자료이며 대체 참조가 아니다.
- 기본 최종물은 4:5, 1080×1350. **한 컷 = 한 이미지 파일**, 생성 호출도 컷마다 분리한다. 통합 컷·콜라주는 대체 납품물이 아니다. 9:16은 파생본. 컷 수는 이야기에 맞춘다.
- 그림은 무문자 원본, 대사·말풍선은 별도 편집 요소. 배경·인물을 각각 벡터화하는 것은 필수가 아니다.
- MANUAL_VALIDATION의 기본 사용자 게이트는 **사전 내용/콘티·계약 → S01 앵커 → 전체 무문자 래스터 세트 → 레터링/완성본**이다. S02~마지막 컷은 각각 별도 파일로 생성하되 운영자가 내부 QC하며 진행한다. **한 컷=한 파일이지, 한 컷=한 사용자 승인 게이트가 아니다.** 상세 실행은 GENERATION_PROTOCOL §0.5.
- 주연은 그림체+해당 인물 정체성, 조연은 그림체만 참조하고 나이·성별·차림새는 이야기로 정한다. 승인된 회차 이미지는 이후 컷의 실제 보조 이미지로 전달한다.
- 좋은 그림의 국소 오류는 좋은 원본에서 해당 부분만 고친다.

## 코드가 현재 보장하는 범위

`pipeline/render_guard.py`는 활성 회차 또는 명시적 idle 상태, 계획/매니페스트 정합성, 로컬 필수 미디어 SHA-256,
일부 필수 필드, 컴파일, 호출자가 제출한 미디어/QC 값의 일관성을 검사한다. `Active episode: NONE`은 validate PASS이지만 `render_ready=false`이고 실제 렌더 명령은 fail-closed로 거부된다.

**이 코드는 생성기를 호출하지 않으며, L8 승인·실제 미디어 전송·실제 이미지 QC를 증명하지 않는다.**
`validate` PASS와 CI 통과는 만화 품질 PASS가 아니다. 실제 생성 연결 전에는 운영자가 GENERATION_PROTOCOL을 실행해야 한다.

```sh
python -m unittest pipeline.test_render_guard
python pipeline/render_guard.py validate
# 활성 회차가 있을 때만:
python pipeline/render_guard.py compile --episode E001 --slide 1
```

예시의 회차 번호는 실행할 때 CURRENT_STATE에서 읽는다. 과거 파일·실패 기록은 보존하되 현행 지시와 혼합하지 않는다.
