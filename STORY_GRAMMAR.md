# STORY_GRAMMAR.md

# INSTATOON STORY GRAMMAR v0.1 — ACTIVE EDITORIAL / SWIPE-SEQUENCE LOCK

**Status:** ACTIVE BASELINE  
**Effective:** 2026-09-04  
**Applies to:** v0.1 production only  
**Active formats:** `STORY_ARC`, `RELATABLE_SCENARIO`

This document defines how a source or idea becomes a **short, swipe-driven anecdote / experience / incident / relatable comic**.

It does not define drawing style.  
- Art style authority: `STYLE_LOCK.md`
- Page/sequential visual authority: `VISUAL_GRAMMAR.md`

The v0.1 editorial focus is deliberately narrow:

> **people experiencing something + a specific emotional/social turn + a memorable landing**

Explainer, listicle, information-card, and abstract issue-analysis formats are not active production targets in v0.1.

---

## 0. Core thesis

A successful v0.1 episode should feel less like “content explaining a topic” and more like:

> “야 이런 일 있었는데…”  
> or  
> “이 상황 진짜 겪어본 사람만 안다.”

The system therefore optimizes for:
- sceneability;
- human specificity;
- state change;
- emotional recognition;
- compact dialogue/action;
- a natural landing.

It does **not** optimize for:
- information density;
- completeness;
- formal explanation;
- moral lessons;
- generic engagement language.

---

## 1. The unit of writing is the whole episode

Never write slide 1, render it, then invent slide 2.

The writer must first produce:
1. source truth;
2. one-sentence story premise;
3. one-sentence emotional engine;
4. ending/landing direction;
5. whole-episode beat sequence;
6. then slide copy.

The reader should experience a coherent arc across swipes.

---

## 2. Human-interest gate

A candidate enters production only if it has enough **human event energy**.

### Mandatory pass conditions

At least four of these six should be clearly present, and `SCENEABILITY` plus `CHANGE` are mandatory.

1. **SCENEABILITY**
   - Can at least three distinct moments be pictured?
   - Is there a person, place, object, action, or visible reaction?

2. **CHANGE**
   - Does something change from beginning to end?
   - New information, embarrassment, escalation, misunderstanding, realization, relief, frustration, etc.

3. **SPECIFICITY**
   - Is there a concrete detail that makes this feel lived rather than generic?
   - Exact object, phrase, timing, place behavior, social cue, odd habit.

4. **EMOTION**
   - Is there a recognizable feeling?
   - awkwardness, relief, irritation, guilt, anticipation, smugness, panic, warmth, disbelief, embarrassment, etc.

5. **RECOGNITION**
   - Can a reader plausibly think “나도 이래” or “아 이런 사람 있지”?

6. **LANDING POTENTIAL**
   - Is there a natural final beat: punch, realization, image, aftershock, or emotionally sticky line?

### Hard-kill conditions

Do not rescue with AI invention if:
- the source is mainly explanation with no scenes;
- the only interesting part is a fact/statistic;
- the source needs long background context before anything happens;
- the “funny part” must be invented by the model;
- every beat is interchangeable/generic;
- the story only works after adding a neat moral;
- the event has no meaningful change;
- visualizing it would produce mostly people standing and explaining.

---

## 3. Source truth before adaptation

For sourced anecdotes/incidents, first extract a compact `STORY_SOURCE_PACK`.

Required fields:
- who is involved;
- where/when if relevant;
- chronological facts;
- exact or near-exact memorable wording;
- concrete objects/actions;
- emotional turns;
- uncertainty / disputed details;
- what must not be invented;
- privacy/public-treatment notes if relevant.

Do not summarize away weird or human details.

The system may compress, reorder for clarity, or lightly oralize.
It may not manufacture a stronger incident than the source contains.

---

## 4. Active format A — STORY_ARC

### Definition

Use when the reader's main question is:

> **“그래서 무슨 일이 있었는데?”**

The meaning depends on temporal progression.

Best for:
- personal anecdote;
- workplace incident;
- dating/friend/family incident;
- embarrassing mistake;
- absurd encounter;
- community story;
- customer/service story;
- school/army/part-time-job experience;
- minor real-world conflict.

### Core rule

**Every body slide changes the state.**

A body slide must introduce at least one:
- new action;
- new fact;
- new obstacle;
- new response;
- new misunderstanding;
- new emotional state.

A slide that only repeats “I was shocked” in a different pose is filler.

---

## 5. STORY_ARC canonical shapes

The router chooses a `story_shape` after selecting `STORY_ARC`.

### 5.1 INCIDENT_ESCALATION
Use when a normal situation becomes increasingly strange/bad/funny.

Typical 7-slide rhythm:
1. **HOOK** — show the abnormality or promise the incident
2. **BASELINE** — minimum context
3. **TRIGGER** — first thing goes wrong / odd
4. **RESPONSE** — protagonist reacts or tries to handle it
5. **ESCALATION** — situation gets more specific/worse
6. **PEAK / TURN** — strongest reveal or confrontation
7. **LANDING** — aftermath / punch / residue

### 5.2 MISUNDERSTANDING_REVEAL
Use when tension comes from an incorrect interpretation.

Typical 7-slide rhythm:
1. HOOK — “나는 진짜 X인 줄 알았다”
2. SETUP
3. FIRST CLUE
4. WRONG INTERPRETATION
5. COMMITMENT / CONSEQUENCE
6. REVEAL
7. AFTERSHOCK / LANDING

Hard rule:
The misunderstanding must be believable from the information available at that point.

### 5.3 ERROR_SPIRAL
Use for embarrassment / mistake stories.

Typical 7-slide rhythm:
1. HOOK — hint at disaster
2. CONFIDENCE / NORMAL
3. FIRST MISTAKE
4. NOTICE
5. BAD RECOVERY ATTEMPT
6. WORSE RESULT / EXPOSURE
7. SHAME TAG / LANDING

Hard rule:
Do not add a second artificial mistake merely to extend length.

### 5.4 ACCUMULATION_BREAK
Use when many small annoyances or repeated events lead to one breaking point.

Typical 6–8-slide rhythm:
1. HOOK / thesis through a scene
2. small occurrence
3. repeat with variation
4. repeat with higher cost
5. protagonist coping
6. final small trigger
7. break / reaction
8. optional quiet aftermath

Hard rule:
Each repetition must increase or vary pressure.

### 5.5 EXPECTATION_REVERSAL
Use when the protagonist expects one outcome and gets another.

Typical rhythm:
1. desired/feared expectation
2. setup
3. signals reinforcing expectation
4. decisive moment
5. actual outcome
6. reaction
7. tag

Do not turn this into clickbait where the reveal has no emotional relevance.

---

## 6. STORY_ARC slide-count templates

Slide count follows story density, not a quota.

### 5 slides
`HOOK → SETUP/TRIGGER → RESPONSE → TURN → LANDING`

### 6 slides
`HOOK → SETUP → TRIGGER → ESCALATE → TURN → LANDING`

### 7 slides — default
`HOOK → BASELINE → TRIGGER → RESPONSE → ESCALATE → PEAK/TURN → LANDING`

### 8 slides
`HOOK → SETUP → TRIGGER → RESPONSE → COMPLICATION → ESCALATION → TURN → LANDING`

If an 8-slide story has no real complication, compress it.

---

## 7. STORY_ARC hook grammar

Slide 1 should not explain everything.

Good hook mechanisms:
- **abnormal image** — protagonist already in the weird situation;
- **quoted line** — one strange sentence from the incident;
- **consequence first** — show the aftermath, then rewind minimally;
- **recognizable dread** — “그 말이 나오는 순간 끝났다”;
- **specific promise** — “면접에서 내가 회사 대표한테 한 말”.

Avoid:
- “오늘은 제가 겪은 일을 소개해드릴게요”;
- full backstory;
- fake suspense unrelated to payoff;
- vague “충격적인 일이 있었습니다”.

The hook must be paid off by the actual source.

---

## 8. STORY_ARC setup compression

Context is a tax.

Default setup budget:
- one slide;
- often one or two text objects only.

Ask:
> What is the minimum information required to understand the trigger?

Start the story **as late as possible**.

---

## 9. STORY_ARC dialogue rule

Dialogue should sound like a person inside a moment, not a narrator explaining the plot.

Prefer:
- fragments;
- short questions;
- interrupted sentences;
- mundane wording;
- source-derived odd phrases;
- small social cues.

Avoid:
- characters saying facts both already know;
- perfectly formed exposition;
- everyone speaking in the same register;
- artificial punchlines;
- “그러니까 네 말은…” summaries unless naturally motivated.

Narration is allowed when it removes clumsy exposition.

---

## 10. STORY_ARC landing types

Select one before detailed slide writing.

### PUNCH
A final comic beat.

### AFTERSHOCK
The funniest/strangest consequence appears after the apparent ending.

### HUMAN_RESIDUE
A small emotional image or line remains.

### CALLBACK
Return to an object/phrase from an earlier slide.

### DEADPAN
End on an understated reaction rather than explaining why it is funny.

### OPEN_RECOGNITION
End where readers can supply their own similar experience.

Avoid generic:
- “그래서 소통이 중요하다.”
- “우리 모두 힘내요.”
- “여러분도 이런 경험 있으신가요?” as the actual ending.

A caption may ask a question later; the comic itself should still land.

---

## 11. Active format B — RELATABLE_SCENARIO

### Definition

Use when the main reader reaction should be:

> **“아 씨 나도 이럼.”**

This is not primarily a list of traits.
The v0.1 default is a **mini-scenario** that dramatizes one familiar behavior or social moment.

Best for:
- workplace habits;
- commuting;
- delivery/cafe/restaurant;
- dating/friends/family;
- messaging;
- sleep/procrastination;
- shopping;
- school;
- social anxiety;
- minor money habits;
- Korean everyday-life moments.

### Core rule

A relatable post must contain:
1. a recognizable trigger;
2. a recognizable internal/external response;
3. one sharpened moment that feels more specific than a generic meme.

---

## 12. RELATABLE_SCENARIO canonical shapes

### 12.1 MICRO_SKIT
One familiar situation played as a miniature story.

Typical 6–7 slides:
1. recognition hook
2. normal baseline
3. trigger
4. immediate reaction
5. escalation / inner-vs-outer conflict
6. crystallized relatable moment
7. tag / aftershock

### 12.2 INNER_OUTER_GAP
Comedy/empathy comes from what a person shows vs thinks.

Typical rhythm:
1. hook
2. external polite behavior
3. internal reality
4. situation worsens
5. stronger external control
6. internal collapse
7. quiet landing

### 12.3 RITUAL
A familiar repeated routine.

Typical rhythm:
1. thesis through concrete scene
2. ritual step A
3. ritual step B
4. ritual step C
5. tiny disruption
6. revealing reaction / payoff

### 12.4 TINY_ANNOYANCE
A small inconvenience is treated with disproportionate emotional truth.

Typical rhythm:
1. “the moment”
2. initial inconvenience
3. attempt to ignore/fix
4. inconvenience persists
5. internal emotional exaggeration
6. deadpan real-world outcome

### 12.5 SOCIAL_CODE
A familiar unspoken interaction pattern.

Typical rhythm:
1. recognizable social cue
2. expected response
3. second cue
4. unspoken interpretation
5. behavior shaped by that interpretation
6. payoff that confirms the code

---

## 13. Relatable does not mean generic

Reject premises such as:
- “직장인은 월요일이 싫다”
- “사람은 배고프면 짜증난다”
- “내향인은 집이 좋다”

unless there is a specific observable behavior.

Upgrade by asking:
- What exactly does the person do?
- What object is involved?
- What sentence is always said?
- What timing makes this familiar?
- What contradiction makes it human?

Good relatable material is **behavioral**, not just categorical.

---

## 14. Avoid listicle drift

The v0.1 system should normally reject:

> “OO할 때 특징 5가지”

if each slide is an independent bullet.

For now:
- choose the strongest example and turn it into a mini-scenario;
- or connect examples into one escalating routine.

This keeps the account closer to comics than card-news.

---

## 15. Emotional engine

Every episode gets one primary `emotion_engine`.

Examples:
- awkward anticipation;
- secondhand embarrassment;
- irritation;
- smug satisfaction;
- panic;
- relief;
- warm recognition;
- guilt;
- disbelief;
- petty jealousy;
- social exhaustion.

The Visual Director uses this to choose expression intensity, pacing, framing, and landing tone.

---

## 16. State-delta test

For every slide after slide 1, write:

> “Compared with the previous slide, what changed?”

Valid:
- new action;
- new fact;
- new emotional level;
- new interpretation;
- new social relationship;
- new consequence.

Invalid:
- “same thing, but another drawing.”

If no delta exists, merge or delete the slide.

---

## 17. Swipe-question test

For slides 1 through the penultimate slide, record `reader_question_after`.

Examples:
- “그래서 뭐라고 했는데?”
- “왜 저러지?”
- “들켰나?”
- “이게 더 심해지나?”
- “결국 어떻게 됐지?”
- “나만 그런 게 아니구나?”

The question does not need to appear on the page.

If there is no natural forward pull, the beat sequence may be flat.

Do not manufacture artificial cliffhangers at every slide.

---

## 18. Visual-story rule

Show rather than narrate when:
- action is visually obvious;
- the object/reaction is the joke;
- spatial relation matters;
- facial/social timing matters.

Use narration when:
- time must jump;
- one short context fact is required;
- illustrating the sentence would add no value.

Do not make a character stand still while a large narration block explains what could have been a scene.

---

## 19. Specific-detail rule

Each episode should preserve at least 2–4 specific human details from source/observation.

Examples:
- exact object;
- timestamp;
- distinctive phrase;
- strange product;
- tiny physical habit;
- interface behavior;
- clothing mistake;
- food item;
- seat position;
- social etiquette detail.

Generic AI rewriting tends to remove exactly these details.

---

## 20. Anti-AI writing rules

Default reject/repair signals:
- every sentence is polished;
- all characters speak in complete explanatory sentences;
- the ending summarizes the theme;
- generic wisdom such as “결국”, “어쩌면”, “우리 모두”, “소소하지만” is added without need;
- obvious setup → obvious moral;
- quirky source language is normalized away;
- writer invents a cleverer punchline than the source warrants;
- too many “ㅋㅋ” are inserted to simulate humanity;
- every slide has a caption explaining the image.

Human texture > verbal smoothness.

---

## 21. Provenance / invention boundary

For real incidents:
- preserve core chronology and consequences;
- preserve memorable source-line attitude;
- compress only for readability;
- label uncertain details internally.

Allowed AI additions:
- minimal connective narration;
- scene transition wording;
- anonymized neutral filler actions;
- non-semantic visual staging.

Not allowed:
- new conflict;
- new humiliation;
- new accusation;
- new punchline presented as real;
- materially stronger ending than the source.

For original relatable scenarios, AI may invent, but the premise must still pass specificity and recognizability gates.

---

## 22. Whole-episode story spec

Before visual planning, produce:

```json
{
  "format": "STORY_ARC|RELATABLE_SCENARIO",
  "story_shape": "INCIDENT_ESCALATION|...",
  "premise": "...",
  "point_of_view": "...",
  "emotion_engine": "...",
  "specific_details": ["..."],
  "landing_type": "PUNCH|AFTERSHOCK|...",
  "landing_beat": "...",
  "beats": [
    {
      "index": 1,
      "role": "HOOK",
      "state_before": "...",
      "state_after": "...",
      "beat": "...",
      "reader_question_after": "...",
      "source_refs": []
    }
  ]
}
```

The Visual Director consumes this entire object.

---

## 23. Story QC before visual planning

PASS only if:
- premise can be stated in one sentence;
- format and shape are clear;
- slide count matches actual event density;
- each body beat changes state;
- at least 2 specific human details survive;
- no context dump;
- no filler reaction slide;
- landing exists before copy polishing;
- ending is not a generic moral;
- source-derived stories do not rely on AI-invented escalation;
- dialogue is oral/readable;
- the episode feels drawable.

If it fails, fix the story skeleton before generating images.

---

## 24. Research basis / rationale

The grammar follows observed properties of Instagram-toon and carousel storytelling:
- Korean Instatoon research identifies **simplicity and clarity** as core visual characteristics and reports that simpler, popular/everyday subjects are easier for users to understand and empathize with.
- Research on Instatoon authenticity emphasizes everyday experience, simple narrative, and simple drawing as strengths rather than defects.
- Contemporary creator workflow guidance places most effort in planning: selecting a real incident/emotion/relatable point, defining the first-slide hook and ending direction, then building the page-level storyboard.
- Carousel storytelling practice treats the first slide as a self-sufficient hook, middle slides as succinct narrative beats, and the last slide as a memorable/shareable landing.

This project applies those principles specifically to anecdote / experience / incident / relatable comics.

---

## 25. v0.1 exclusions / future expansion

Dormant for now:
- EXPLAINER_CAUSAL
- CONTRAST_REFRAME as a standalone information format
- OBSERVATION_SET / “traits list”
- educational card-news
- product explainers
- infographic-first posts

Do not expand v0.1 merely to cover more topic types.
