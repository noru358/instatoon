# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E007/README.md

## 현재 위치

큰 흐름:
수집/소재 확정 → L1-L7 → 캐스팅/콘티 → 구조화 계약 → 레퍼/프리플라이트 → 개별 래스터 → 분리 레터링 → 최종 QC → 완성.

E007:
- L1-L7: USER APPROVED.
- cast: Gaeun / Harin / Taemin, USER APPROVED for this episode.
- six-slide storyboard/dialogue intent: USER APPROVED.
- reference authority: REF_V2_D + REF_V2_E, USER CONFIRMED.
- machine state: STORYBOARD_READY.
- EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN: not built yet.
- machine-valid episode anchor: none.

A chat-native S01 was visually approved, but it has no repository render attempt/hash.
It is taste evidence only and must not be falsely recorded as a machine-bound anchor.

Several subsequent native-chat attempts are INVALID:
- six slides merged into one page;
- baked Korean text / labels;
- small-panel anatomy degradation, including face/hand defects.

These failed outputs are not references or repair bases.

## 현재 운영 모드 — MANUAL_VALIDATION

Temporary policy until the image API/provider adapter is connected and measured:

1. every stage is shown to the user and explicitly reviewed;
2. no auto-finish after S01;
3. each raster slide is handled one at a time;
4. raster and lettering remain separate;
5. lettering proof is manually reviewed;
6. final export is manually reviewed.

This phase is for validating the production specification while staying within the ChatGPT subscription where possible.
It is intentionally more manual than the long-term target.

The GitHub QC workflow therefore defaults to STANDARD, not AUTO_FINISH.
AUTO_FINISH code is preserved as future infrastructure but is not the default operating mode.

## Renderer diagnosis from E007

The user's reference upload was not the problem.
The failure came from using a long-context conversational native image interface as if it were an isolated batch renderer.

Observed repeated failure:
- request intended for one slide was reinterpreted as "complete the whole six-panel comic";
- single-panel / text-free constraints were overridden by global episode context.

Therefore:
- do not treat repeated MULTI_PANEL / BAKED_TEXT as ordinary stochastic image noise;
- after two repeated hard-contract failures in the same conversation-inferred path, stop retrying that path;
- use a clean dedicated manual render context as a temporary workaround;
- long-term fix is an explicit provider adapter with one request = one slide.

## Long-term target — API_PRODUCTION

User-facing checkpoints should eventually shrink again to:
storyboard approval → reference confirmation → S01 approval → finished episode.

Internal target:
- isolated image API request per slide;
- explicit compiled payload;
- actual canonical refs + approved S01 anchor supplied as binaries;
- image-provider adapter; GPT-Image-2 is the initial benchmark candidate, not a hardcoded permanent choice;
- local deterministic QC-0 for file count / ratio / single-panel / no baked semantic text where detectable;
- low-cost vision QC adapter; DeepSeek Flash Vision is the initial benchmark candidate;
- QC-1 style/identity, QC-2 anatomy/scene;
- deterministic Python lettering;
- cost, attempt count, first-pass rate, repair reason, and provider/model logged per slide.

Do not hardcode estimated dollar cost as a permanent policy before measuring real episodes.
Use the first three API-produced episodes to establish actual cost and first-pass-rate baselines.

## Visual QC clarification

A larger open mouth while laughing is not itself a defect.
Fail only when mouth treatment breaks the approved drawing language, identity, or facial proportions.

Anatomy high-risk cues include:
- hands near face;
- multiple exposed fingers;
- crossed/overlapping hands;
- phone or utensil grip;
- chopsticks;
- physical contact / occlusion.

These cues raise QC strictness; they do not prohibit the pose.

## 정확한 다음 행동 — next session

1. read CURRENT_STATE + episodes/E007/README.md + PRODUCTION_STATE.json;
2. serialize the already-approved E007 package into EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN;
3. run preflight / consistency checks;
4. show those structured contracts and preflight result to the user for manual approval;
5. only then resume one-slide-at-a-time raster validation.

Do not re-ask approval for L1-L7 or the approved six-slide storyboard unless the content materially changes.
