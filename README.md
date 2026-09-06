# instatoon

실제 사람이 쓴 인터넷 소재 → 대본/콘티 → **승인된 시각 에셋 조립** → 편집 가능한 대사/말풍선 → 검수/내보내기.

최종 목표는 ChatGPT 대화 기억 없이 실행되는 독립 생산 도구다.

## Current architecture

2026-09-07부터 최종 컷의 기본 렌더 방식은 **full-frame generation이 아니라 deterministic asset composition**이다.

Canonical path:

`source → story/dialogue → storyboard → asset resolve → ASSET_GAP authoring → approved registry → deterministic composition → lettering/UI → QC/export`

중요:
- 생성 모델은 **새 부품 제작기 / 예외 렌더러**다.
- 승인된 인물·배경·소품을 새 컷마다 다시 그리지 않는다.
- 필요한 부품이 없으면 컷 전체를 생성하지 않고 `ASSET_GAP`을 만든다.
- 최종 장면은 asset ID + 좌표 + scale + rotation + z-order로 조립한다.
- 의미가 있는 글자/UI는 생성 이미지에 굽지 않는다.

상세 단일 기준: [ASSET_COMPOSITION_PROTOCOL.md](ASSET_COMPOSITION_PROTOCOL.md).

현재 제작 위치와 다음 행동은 [CURRENT_STATE.md](CURRENT_STATE.md)를 따른다.

## Start / restore

새 세션에서:
1. `README.md`와 `CURRENT_STATE.md`를 읽는다.
2. `ASSET_COMPOSITION_PROTOCOL.md`를 읽고 현재 renderer ownership을 확인한다.
3. 필요한 창작 authority만 읽는다:
   - 소재/대사: `SOURCE_STORY_PIPELINE.md`
   - 그림체/인물 authoring: `STYLE_LOCK.md`, `MASTER_PROMPTS.md`, `REFERENCE_SET.md`
   - 컷 의미/구도: `VISUAL_GRAMMAR.md`
   - 신규 생성 asset/exception QC: `GENERATION_PROTOCOL.md`
4. 최종 컷 제작 전 `assets/production/registry.json`에서 필요한 승인 asset을 resolve한다.
5. 없는 시각 요소만 asset으로 제작·승인·등록한다.
6. AutoPipeline `pipeline/compositor.py`로 무문자 컷을 결정적으로 조립한다.
7. `pipeline/lettering.py` 계열에서 텍스트를 별도 합성한다.

대화 기억만으로 old S01→S02 full-frame generation workflow를 복구하지 않는다.

## Production ownership

| 영역 | Authority |
|---|---|
| 실제 인간 소재·각색·대사 | SOURCE_STORY_PIPELINE.md |
| storyboard/visual semantics | VISUAL_GRAMMAR.md |
| final renderer boundary / asset-gap routing | ASSET_COMPOSITION_PROTOCOL.md |
| drawing language / character authoring | STYLE_LOCK.md + MASTER_PROMPTS.md + REFERENCE_SET.md |
| generative asset/exception QC | GENERATION_PROTOCOL.md |
| approved composition assets | assets/production/registry.json |
| deterministic raster composition | AutoPipeline pipeline/compositor.py |
| lettering / editable text | pipeline/lettering.py |
| current execution state | CURRENT_STATE.md |
| historical automation notes | AUTOMATION_TRANSITION.md |

사용자의 명시 지시가 최상위다. 과거 episode 파일이나 archive는 CURRENT_STATE가 명시적으로 활성화하지 않는 한 실행 권위가 아니다.

## Fixed principles

- 옴니버스. 반복 주연은 선택 가능하며 매 회차 강제하지 않는다.
- 실제 인간 소재를 우선한다.
- 기본 최종물은 4:5, 1080×1350, **한 컷 = 한 파일**.
- 최종 art raster는 기본 무문자다.
- 캐릭터 동일성은 재생성으로 유지하는 것이 아니라 승인 asset 재사용으로 유지한다.
- 구도 다양성은 crop/scale/position/layer/pose asset 선택으로 만든다.
- story-valid pose/view가 없으면 새 asset을 만든다. 이야기를 asset library에 억지로 맞추지 않는다.
- rejected/stale/hash-mismatched asset은 조립에 사용할 수 없다.
- 신규 생성 asset은 기존 style/identity/anatomy/geometry QC를 통과해야 한다.
- full-frame generation은 명시적 exception lane만 허용한다.
- 실패 수리는 최소 범위다. 잘못된 asset 하나 때문에 관련 없는 승인 컷을 다시 만들지 않는다.

## Code paths

Default final raster:

```sh
# run from the AutoPipeline superproject root
python -m pipeline.compositor \
  --project-root instatoon \
  --registry assets/production/registry.json \
  --scene instatoon/episodes/<ID>/composition/slide_01.json \
  --output instatoon/episodes/<ID>/renders/slide_01_art.png
```

Legacy/full-frame generative adapter:

`pipeline/render.py`는 기본 실행이 fail-closed이며, 명시적인 `--exception-lane` 없이 full-frame 생성에 사용할 수 없다.

기존 `render_guard.py`, hash-bound QC, reference binding, quarantine 로직은 폐기되지 않았다. 최종 컷 전체를 반복 샘플링하는 대신 **신규 asset authoring / 예외 샷**의 안전장치로 역할이 이동한다.

## Current migration

현재는 `ASSET_SYSTEM_CALIBRATION` 단계다. 이전 E001 full-frame 생성 실험은 중단되었으며 자동으로 새 production asset이 되지 않는다.

다음 완료 조건:
1. 최소 starter asset pack 제작/승인/등록;
2. 4-slide pilot scene contract 작성;
3. compositor로 4개의 별도 4:5 frame 생성;
4. 필요한 경우에만 승인된 exception shot 사용;
5. lettering을 별도 deterministic layer로 완료.

이 pilot이 통과한 뒤 fresh E001 제작을 시작한다.
