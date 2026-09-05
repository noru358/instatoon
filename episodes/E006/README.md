# E006 — 어떻게 오셨어요?

Status: L12.5 RENDER CONTRACT READY — S01 PREFLIGHT NEXT
Updated: 2026-09-06

## 1. Provenance

Human-source-first seed:
- Reddit r/Living_in_Korea, thread: "Something in Korea that embarrassed you"
- URL: https://www.reddit.com/r/Living_in_Korea/comments/1tk2g5g/something_in_korea_that_embarrassed_you/
- source comment: a Korean-language beginner visited a dentist, was asked "어떻게 오셨어요?", answered "자전거 타고왔어요 :)", the receptionist laughed, and the commenter sat down in embarrassment. In replies the commenter clarified that the intended reason for the visit was wisdom-tooth treatment/tooth pain.

Provenance class: HUMAN_SEEDED_INSPIRATION.
Do not invent a materially stronger humiliation or conflict.

## 2. L1-L7 package — current review candidate

### L1 SOURCE DISCOVERY
Selected the dentist-language misunderstanding because it is a direct human anecdote with specific wording and a visible social reaction.

### L2 HUMAN-INTEREST GATE
PASS:
- immediately sceneable;
- clear misunderstanding -> realization state change;
- specific phrase/object/place;
- recognizable embarrassment;
- no moral or invented punchline required.

### L3 SOURCE NORMALIZATION

SOURCE FACTS:
- protagonist is still early in Korean-language learning;
- protagonist visits a dentist in Korea;
- receptionist asks "어떻게 오셨어요?";
- protagonist answers "자전거 타고 왔어요 :)";
- receptionist laughs/giggles;
- protagonist is embarrassed and goes to sit down;
- reply clarifies the expected answer concerned visit reason, e.g. wisdom tooth/tooth pain.

SOURCE VOICE TO PRESERVE:
- the literal misunderstanding of "어떻게 오셨어요?";
- confident/simple "자전거 타고 왔어요 :)";
- embarrassment without a manufactured moral.

### L4 STORY SHAPE
MISUNDERSTANDING_REVEAL.

### L5 STORY BEATS

1. HOOK / SETUP — 한국어 공부 시작한 지 얼마 안 됐을 때 치과에 감.
2. QUESTION — 접수 직원: "어떻게 오셨어요?"
3. CONFIDENT MISREAD — 주인공: "자전거 타고 왔어요 :)"
4. REACTION — 접수 직원이 웃음/피식. 주인공이 순간 이상함을 느낌.
5. RETREAT — 별말 더 못 하고 바로 대기석으로 감.
6. LANDING — 대기석에서 민망해하는 장면. 작은 내레이션으로 "사랑니 뽑으러 간 거였음" 정도만 사실 보충하고 별도 교훈/추가 펀치라인은 넣지 않음.

### L6-L7 DIALOGUE / HUMANIZATION

Current dialogue candidate:
- narration/setup: "한국어 공부 시작한 지 얼마 안 됐을 때 치과 갔는데"
- receptionist: "어떻게 오셨어요?"
- protagonist: "자전거 타고 왔어요 :)"
- receptionist: readable dialogue not required; visual giggle/reaction is preferred because the source only says she giggled
- protagonist then retreats to the waiting seat without an invented clarification exchange
- final small narration candidate: "사랑니 뽑으러 간 거였음"

Do NOT add:
- "아! 무슨 뜻인지 알 것 같아!"
- a moral;
- "그날 한국어 공부 끝냄" or another manufactured closing joke;
- extra explanatory dialogue unless the user approves it;
- the previously invented receptionist clarification question and protagonist "...사랑니요." exchange.

## 3. Cast decision — PARTIAL USER APPROVAL ONLY

User explicitly selected:
- protagonist = episode-only foreign character;
- do not retrofit Gaeun/Harin/Taemin with a one-off overseas-background/language setting.

This is CAST_ONLY approval.
It does NOT approve the full L1-L7 package and does NOT authorize L10-L13.

The episode-local identity digest is created at L11 only after L8 full-package approval.

## 4. Rollback of invalid render

One 9:16 six-panel image was generated prematurely in chat before L8 completion and without the required render contract.

Verdict:
- INVALID_RENDER;
- STORYBOARD_REFERENCE_ONLY at most;
- NOT style reference;
- NOT episode anchor;
- NOT LAST_KNOWN_GOOD;
- must not condition later production.

Why invalid:
- skipped L8 reapproval after cast change;
- skipped L10-L12.5;
- no E006 EPISODE_PLAN / RENDER_MANIFEST;
- canonical REF_V2_D/E were not supplied as actual renderer media;
- free-form prompt rewrote the canonical style;
- six panels were combined into one image instead of one panel per file;
- 9:16 was used instead of the feed/carousel 4:5 master;
- final Korean text was baked into raster instead of L14 vector lettering;
- renderer added unapproved wording.

## 5. L8 approval

PASS — 2026-09-06.
User explicitly approved the corrected full L1-L7 package with "통과".

This supersedes the earlier CAST_ONLY partial state.

## 6. L9 VOICE LEDGER

No new global voice rule promoted from a single episode.
Episode-local preservation rule:
- keep the source-specific literal misunderstanding and brief human embarrassment;
- do not add a neat moral or invented clarification exchange.

## 7. L10-L12 visual/cast plan

- six slides;
- feed/carousel master = 4:5, 1080×1350;
- one panel per image, separate files;
- strict episode continuity;
- no main cast;
- woman_01 = episode-only foreign Korean-language beginner;
- receptionist_01 = episode-only Korean dental receptionist;
- both receive persistent identity digests because each appears in 2+ slides;
- final readable Korean text is L14 vector lettering only.

Camera rhythm:
S01 medium-wide establish → S02 medium two-shot → S03 closer protagonist-favoring medium → S04 tight reaction two-shot → S05 medium/full transition → S06 quiet medium-wide landing.

## 8. L12.5 render contract

Materialized:
- EPISODE_PLAN.json
- RENDER_MANIFEST.json
- PRODUCTION_STATE.json

Required production refs:
- REF_V2_D
- REF_V2_E

Both are BINARY_REQUIRED and must be supplied as actual renderer image media.

Exact next action:
1. validate/compile/authorize E006_S01;
2. confirm current renderer can bind the actual required binaries;
3. generate E006_S01 only, text-free 4:5;
4. user visual QC before any S02 call.
