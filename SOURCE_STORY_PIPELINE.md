# SOURCE_STORY_PIPELINE.md

# SOURCE → STORY PIPELINE v0.1

**Status:** ACTIVE DESIGN BASELINE  
**Effective:** 2026-09-04

Purpose:
Turn raw anecdotes, experiences, incidents, community stories, and relatable observations into a complete story plan **before any paid illustration is generated**.

---

## 0. Pipeline

```text
SOURCE POOL
   ↓
FAST FILTER
   ↓
HUMAN-INTEREST GATE
   ↓
STORY SOURCE PACK
   ↓
ANGLE / PREMISE
   ↓
FORMAT + STORY SHAPE
   ↓
LANDING FIRST
   ↓
WHOLE-EPISODE BEAT MAP
   ↓
STORY QC
   ↓
HUMAN PLAN GATE
   ↓
VISUAL DIRECTOR
   ↓
EPISODE_PLAN
   ↓
RENDER PREFLIGHT / PRODUCTION
```

---

## 1. SOURCE POOL

v0.1 source modes:

### A. PERSONAL / USER-SUPPLIED
- direct experience;
- notes;
- chat recollection;
- anecdote provided by user.

### B. COMMUNITY STORY
- post + comments;
- anonymous forum story;
- social-media anecdote;
- reply that materially changes the story.

### C. REAL-WORLD INCIDENT
- human-interest news;
- workplace/customer incident;
- unusual but low-context public event.

### D. RELATABLE OBSERVATION
- everyday behavior;
- common social code;
- recurring annoyance;
- recognizable routine.

Do not prioritize “important topics.”
Prioritize **drawable human moments**.

---

## 2. FAST FILTER

Reject immediately if:
- mostly factual explainer;
- no identifiable person/action;
- no visible event;
- requires more than about two slides of context before trigger;
- only value is controversy;
- cannot be safely/publicly adapted;
- content is generic enough to be written without any source.

Keep candidates with:
- specific action;
- memorable phrase;
- odd object/detail;
- clear embarrassment/irritation/surprise;
- strong before/after;
- recognizably human behavior.

---

## 3. HUMAN-INTEREST GATE

Score 0–2 each:
- sceneability;
- state change;
- specificity;
- emotional signal;
- relatability;
- landing potential.

Rules:
- `sceneability >= 1`
- `state_change >= 1`
- total target >= 8/12

Hard-kill rules from `STORY_GRAMMAR.md` override the total.

Store:
- pass / hold / kill;
- one-sentence rationale;
- strongest visual scene;
- strongest human detail.

---

## 4. STORY SOURCE PACK

Do this once and reuse downstream.

```json
{
  "source_id": "SRC-0001",
  "source_mode": "community_story",
  "raw_sources": [],
  "people": [],
  "setting": [],
  "chronology": [],
  "memorable_lines": [],
  "concrete_details": [],
  "emotion_turns": [],
  "uncertainties": [],
  "do_not_invent": [],
  "privacy_public_treatment": [],
  "candidate_visual_scenes": []
}
```

Do not write polished copy here.
This layer protects source truth from later rewriting.

---

## 5. ANGLE / PREMISE

For v0.1, angle is not a thesis about society.
It is the **specific human promise of the episode**.

Good shape:
- “퇴근 10분 전에 ‘간단한 일’이 들어오면 생기는 일”
- “소개팅에서 상대 직업을 완전히 잘못 알아들은 썰”
- “배달이 잘못 온 줄 알고 세 번 전화했는데…”
- “단톡방에서 ‘넵’ 하나 보내는 데 왜 이렇게 오래 걸리나”

Premise formula:

```text
[person / familiar situation]
+ [specific trigger or friction]
+ [what makes this worth watching]
```

Reject category labels:
- 직장인의 하루
- 연애 이야기
- 요즘 MZ세대
- 내향인 특징

---

## 6. FORMAT ROUTER v0.1

Only two active outputs.

### STORY_ARC
Choose when:
- event chronology matters;
- reader wants to know what happens next;
- a source incident exists.

### RELATABLE_SCENARIO
Choose when:
- core value is recognition;
- chronology is invented/secondary;
- one familiar behavior can be dramatized as a mini-scene.

If mainly educational or analytical:
`HOLD_FOR_FUTURE_FORMAT`.

---

## 7. STORY SHAPE ROUTER

### STORY_ARC
- INCIDENT_ESCALATION
- MISUNDERSTANDING_REVEAL
- ERROR_SPIRAL
- ACCUMULATION_BREAK
- EXPECTATION_REVERSAL

### RELATABLE_SCENARIO
- MICRO_SKIT
- INNER_OUTER_GAP
- RITUAL
- TINY_ANNOYANCE
- SOCIAL_CODE

Router outputs:
- chosen shape;
- why it fits;
- alternate only if genuinely plausible.

No multi-agent debate over shape.

---

## 8. LANDING FIRST

Before expanding middle beats, define the likely final beat.

Store:
- landing type;
- source/observation basis;
- approximate final visual;
- approximate final line if one exists.

Without a landing, generative writing tends to fill slides with exposition and append a generic conclusion.

---

## 9. WHOLE-EPISODE BEAT MAP

Create all beats in one pass.
Do not polish text yet.

For every beat:
- role;
- state before;
- change;
- state after;
- what is visible;
- reader question after;
- source refs;
- must-use detail.

Example topology:

```text
1 HOOK
State: reader knows nothing
Change: protagonist freezes at 5:50 as boss approaches
Question: 왜 저 표정이지?

2 BASELINE
State: nearly finished work
Change: protagonist has already mentally checked out
Question: 설마?

3 TRIGGER
Boss: "이거 간단한 건데..."
Change: new task appears
Question: 얼마나 간단한데?
```

This is the key planning artifact.

---

## 10. COPY PASS

Only after beat map passes.

For each slide:
- narration if necessary;
- dialogue if natural;
- SFX / small label;
- optional silent beat.

Copy stays subordinate to visual action.

---

## 11. STORY QC

Deterministic structural checks:
- premise non-empty;
- active format only;
- story shape valid;
- 5–8 slides default;
- state delta on every body slide;
- landing specified;
- at least two specific details;
- no two consecutive pure-exposition slides;
- source refs on sourced beats.

Semantic QC:
- believable causality;
- source fidelity;
- dialogue naturalness;
- no generic moral;
- no manufactured escalation;
- enough visual scenes.

Human taste:
- “Would I tell/share this story to someone?”
- “Would I swipe?”
- “Does the ending actually land?”

---

## 12. HUMAN GATES

### Gate A — Candidate / premise
Show:
- source summary;
- premise;
- strongest detail;
- proposed format/shape;
- landing direction.

Action:
`GO / HOLD / KILL / TWEAK`

### Gate B — Whole story plan
Show:
- all slide beats;
- rough text;
- visual idea per slide;
- landing.

Action:
`APPROVE / EDIT`

No paid raster generation before Gate B during v0.1.

### Gate C — Final taste
After vector composition/QC:
`PUBLISH / REPAIR / KILL`

---

## 13. TOKEN-COST DESIGN

Do not use one LLM call per slide.

Preferred:
1. **Call 1:** source pack + premise + format/shape + beat map;
2. human gate;
3. **Call 2:** polished slide copy + visual-director-ready annotations;
4. optional focused repair call only if needed.

Stable grammar/style docs are referenced by version during reasoning.
Full style prompt is injected only by the raster prompt assembler.

---

## 14. SOURCE DISCOVERY AUTOMATION — later

Potential future collectors:
- selected communities;
- user-submitted stories;
- trend/social feeds;
- human-interest news;
- comments.

But first prove:
- gate selects good material;
- story grammar produces strong episodes;
- visual pipeline is cheap enough.

Do not build a large crawler before the selection grammar is validated.

---

## 15. Performance learning

Track:
- source mode;
- format;
- story shape;
- emotion engine;
- hook mechanism;
- landing type;
- slide count;
- production cost/time;
- performance.

Use repeated evidence across several posts to suggest experiments.

Do not:
- automatically rewrite style;
- copy one viral structure forever;
- optimize toward generic ragebait;
- replace human-interest gate with raw engagement score.
