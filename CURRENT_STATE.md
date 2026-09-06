# CURRENT_STATE.md

Updated: 2026-09-06
Repository: noru358/instatoon

Active episode: episodes/E007/README.md

## 현재 위치

큰 흐름: 수집/소재 확정 → L1-L7 재구성 → 사용자 보이스 게이트 → 캐스팅/콘티 → 렌더 계약 → S01 앵커 → 나머지 컷 → 분리 레터링 → 완성.

E007 신규 공정을 시작했다.
현재 PRODUCTION_STATE = L8_AWAITING_APPROVAL.

선택 소재:
- 직장 점심 메뉴를 한참 고민함;
- 모두 "아무거나"라고 하지만 실제 제안은 계속 탈락;
- 결국 맨날 가던 익숙한 곳으로 감.

Human-seeded primary source:
- Reddit r/SideProject — "The 'where do you want to eat / I don't know where do YOU want to eat' conversation ends here"
- 실제 글의 핵심 패턴은 긴 선택 대화 끝에 결국 늘 가던 곳으로 돌아가는 것.
- E007은 이를 한국 직장 점심 맥락으로 각색하되 원문을 한국 회사의 실제 사건인 것처럼 위장하지 않는다.

E007 L1-L7 review package:
- episodes/E007/README.md

## 반자동 실험 운영

- 콘티/L8 승인 전 이미지 생성 금지.
- 승인 후 cast → storyboard → EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN 순.
- 사용자가 레퍼 이미지를 pre-render 단계에서 다시 제공.
- S01은 ChatGPT/native direct generation으로 한 장만 생성해 사람 앵커 승인.
- S01 PASS 후 후속 컷 생성/QC/분리 레터링/완성까지 내부 진행하는 반자동 흐름을 시험.
- 이미지와 레터링은 끝까지 분리 유지.
- AUTO_FINISH runner의 외부 이미지 provider 경로를 이번 채팅 내 반자동 이미지 생성에 억지로 사용하지 않는다.

## 전역 시각 기준

- INSTATOON_STYLE_v2.0.
- approved reference binaries outrank generalized prose.
- one panel = one image file.
- feed/carousel master 4:5, 1080×1350 unless explicitly changed.
- raster art is text-free; lettering is added later.

## 정확한 다음 행동

1. user reviews E007 L1-L7 package;
2. on PASS, resolve smallest story-sufficient cast;
3. build ordered 5–6 slide storyboard and final dialogue;
4. build EPISODE_PLAN / RENDER_MANIFEST / LETTERING_PLAN;
5. receive the user's reference images;
6. generate S01 only and request anchor approval.
