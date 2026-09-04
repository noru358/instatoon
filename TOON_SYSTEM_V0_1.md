# TOON_SYSTEM_V0_1.md

# TOON SYSTEM v0.1 — SEMI-AUTOMATED INSTATOON PRODUCTION ARCHITECTURE

**Status:** ACTIVE DESIGN BASELINE  
**Effective:** 2026-09-04

Purpose:
Create a low-cost, repeatable semi-automated Instagram-toon production system whose stable identity comes from the **overall art style + visual grammar**, not from recurring characters.

This system is intentionally separate from the Talkshow video pipeline.

---

## 0. System thesis

The unit of planning is the **entire episode**.

The unit of rendering is the **slide**.

The unit of style identity is the **project visual language**.

The unit of editability is the **vector narrative layer**.

Do not optimize individual frames independently.

---

## 1. Pipeline

```text
SOURCE / IDEA
   ↓
SOURCE NORMALIZATION
   ↓
ANGLE GATE
   ↓
FORMAT ROUTER
   ↓
WHOLE-EPISODE SWIPE SCRIPT
   ↓
VISUAL DIRECTOR
   ↓
EPISODE PLAN / PAGE SPECS
   ↓
WHOLE-EPISODE PREFLIGHT
   ↓
2-SLIDE RENDER PREFLIGHT
   ↓
RENDERER
   ├─ raster art where needed
   └─ vector-only / spot-art pages where cheaper
   ↓
VECTOR LETTERER / COMPOSER
   ↓
QC
   ↓
HUMAN TASTE GATE
   ↓
EXPORT / PUBLISH
   ↓
PERFORMANCE RECORD
```

---

## 2. Do not implement v0.1 as a swarm of agents

Token and coordination cost matter.

v0.1 should use:
- one orchestrator;
- typed stage outputs;
- deterministic validators where possible;
- a small number of high-value generative calls;
- cached canonical style/grammar documents.

Do not create independent agents that repeatedly debate or rewrite the same episode.

Default LLM-call philosophy:
1. source/angle reasoning;
2. whole-episode script + visual-plan reasoning;
3. optional focused revision after human feedback.

Everything else should be structured transformation, deterministic rendering, or targeted QC when possible.

---

## 3. Canonical artifacts

### 3.1 CONTENT_MASTER.json
Semantic/editorial truth. No render details.

Contains:
- source list;
- topic;
- angle;
- premise when a chronological story needs a compact causal formulation;
- audience;
- factual claims;
- human-origin quotes/comments if used;
- tone;
- intended reader payoff;
- safety/public-treatment notes.

### 3.2 STORY_PLAN.json
Whole-episode narrative truth before page styling.

Contains:
- format and story shape;
- premise and point of view;
- emotional engine and landing;
- ordered beats with state change and swipe question;
- must-use details and source refs.

### 3.3 EPISODE_PLAN.json
Whole-episode visual and page plan built from the accepted story plan.

Contains:
- narrative format;
- slide count;
- slide order;
- role of every slide;
- text objects;
- art direction;
- page archetype;
- render mode;
- continuity mode;
- visual rhythm;
- provenance refs.

### 3.4 RENDER_MANIFEST.json
Execution state only.

Contains:
- prompt hash;
- style version;
- grammar version;
- model/tool;
- output path;
- generation count;
- targeted edits;
- QC result;
- cost/credit record.

Never mix editorial truth with generation history.

---

## 4. CONTENT_MASTER schema

Illustrative shape:

```json
{
  "episode_id": "E0001",
  "source_mode": "community|news|observation|original|user_story|mixed",
  "sources": [
    {
      "id": "S1",
      "type": "url|text|comment|data",
      "locator": "...",
      "raw_excerpt": "...",
      "claim_status": "opinion|reported|verified|needs_check"
    }
  ],
  "topic": "one sentence",
  "angle": "one sentence",
  "premise": "compact story formulation when applicable",
  "audience": "who should immediately care",
  "reader_payoff": "what changes in the reader after finishing",
  "tone": ["dry", "warm", "awkward"],
  "facts": [],
  "gold_lines": [],
  "public_treatment": []
}
```

The angle is mandatory. `premise` may refine the angle into a chronological story promise but may not replace it silently.

A broad topic without an angle does not proceed.

---

## 5. FORMAT ROUTER

Active v0.1 values:
- `STORY_ARC`
- `RELATABLE_SCENARIO`

Routing is based on the human story structure, not the source.

### STORY_ARC
Question:
“Does the reader mainly want to know what happened next?”

### RELATABLE_SCENARIO
Question:
“Is the main payoff recognition of a familiar behavior/situation that can be dramatized as a mini-scene?”

Dormant / future:
- `OBSERVATION_SET`
- `EXPLAINER_CAUSAL`
- `CONTRAST_REFRAME`

If a candidate is mainly analytical/informational, hold it for future expansion rather than forcing it into v0.1.

Detailed shape routing and story rules: `STORY_GRAMMAR.md`.

---

## 6. WHOLE-EPISODE SWIPE SCRIPT

The script is created for the full episode in one pass.

Each slide contains:
- `role`: HOOK / ESTABLISH / DEVELOP / TURN / LANDING etc.;
- `beat`: one sentence describing what changes;
- `reader_question_after`: what makes the next swipe worthwhile;
- `copy_intent`: what the text must accomplish;
- `source_refs`: provenance.

The script must pass:
- no duplicate beats;
- no filler;
- no orphan payoff;
- no hook/body mismatch;
- no final moral added merely because the model likes conclusions.

---

## 7. VISUAL DIRECTOR

The Visual Director reads the **entire swipe script** before assigning any page.

It selects per slide:
- page archetype;
- focal subject;
- literal vs metaphorical treatment;
- whether a person is needed;
- whether dialogue is needed;
- camera/composition;
- negative-space requirement;
- render mode;
- continuity references;
- visual relation to previous/next slide.

It also produces one episode-level rhythm description, for example:

```text
cover hero → ordinary scene → split compare → close detail →
visual metaphor → quiet landing
```

This prevents six near-identical AI illustrations.

---

## 8. EPISODE_PLAN schema

Illustrative shape:

```json
{
  "episode_id": "E0001",
  "style_version": "INSTATOON_STYLE_v1.2",
  "visual_grammar_version": "INSTATOON_VISUAL_GRAMMAR_v0.1",
  "story_grammar_version": "INSTATOON_STORY_GRAMMAR_v0.1",
  "format": "STORY_ARC",
  "continuity_mode": "LIGHT",
  "slide_count": 7,
  "episode_rhythm": "...",
  "slides": [
    {
      "index": 1,
      "role": "HOOK",
      "beat": "...",
      "page_archetype": "HERO_SCENE",
      "render_mode": "RASTER_PLUS_VECTOR",
      "art_direction": {
        "story_clarity": "...",
        "subjects": [],
        "action": "...",
        "location": "...",
        "composition": "...",
        "negative_space": {
          "preferred_region": "top|bottom|left|right|center",
          "purpose": "title|narration|dialogue"
        }
      },
      "text_objects": [
        {
          "id": "T1",
          "kind": "title|narration|dialogue|label|sfx|source_note",
          "content": "...",
          "speaker": null,
          "priority": 1
        }
      ],
      "continuity_refs": [],
      "source_refs": []
    }
  ]
}
```

---

## 9. Prompt assembly

Prompts are built from typed data.

Do not ask an LLM to rewrite the style every time.

Per raster slide:

```text
SCENE FACTS
+ STORY CLARITY
+ NEGATIVE-SPACE / NO-TEXT requirement
+ episode-local continuity block if required
+ selected canonical reference(s) from REFERENCE_SET.md — mandatory for production raster
+ REFERENCE_OBEDIENCE_BLOCK — mandatory for production raster
+ FACE_LOCK_BLOCK when a face is visible
+ IDENTITY_PRESERVATION_BLOCK only when episode-local identity continuity is required
+ BACKGROUND_DENSITY_LOCK for environment-heavy scenes
+ MASTER_STYLE_PROMPT
+ NEGATIVE_STYLE_PROMPT
+ ANTI_GPT_DEFAULT_BLOCK — mandatory for production raster
```

`STYLE_LOCK.md` defines the normative style boundary. `REFERENCE_SET.md` defines the approved binary inputs. `MASTER_PROMPTS.md` implements those authorities as stable text blocks.

Scene copy must not redefine the style.

---

## 10. Art-generation policy

Characters are not a required persistent asset system.

The image model generates a complete raster art base appropriate to the slide.

Rules:
- no readable text;
- no baked-in dialogue balloons;
- no unnecessary decorative detail;
- preserve planned negative space;
- use episode-local continuity only when needed.

For `STRICT_EPISODE`:
generate or select a temporary episode reference after the first accepted relevant slide, then reuse it for that episode only.

Do not turn this into a recurring-character master-sheet requirement.

---

## 11. Vector renderer

All semantic text is placed after image generation.

Suggested implementation:
- SVG or HTML/CSS as page-description layer;
- Sharp for deterministic rasterization/compositing;
- fonts stored/configured by project, not generated in-image.

Vector objects:
- captions;
- bubbles;
- tails;
- labels;
- arrows;
- underlines;
- emphasis circles;
- dividers;
- SFX;
- small source notes.

Advantages:
- zero image-model spelling risk;
- easy text edits;
- localization;
- layout measurement;
- consistent brand typography;
- low-cost revisions.

---

## 12. Render strategy by page

Before paid generation, select one:

```text
RASTER_FULL
RASTER_PLUS_VECTOR
VECTOR_PLUS_SPOT_ART
VECTOR_ONLY
```

The system should optimize for **semantic clarity per paid render**, not maximize illustration count.

Typical 7-slide target:
- 4–6 paid raster illustrations;
- 1–3 vector-heavy/spot-art slides;
- depending on format.

This is a planning target, not a mandatory quota.

---

## 13. Render preflight / cost protection

The complete episode plan must exist first.

Then:

### Stage A — two-slide preflight
Render:
1. cover;
2. highest-risk representative body slide.

Check:
- style lock;
- page grammar;
- text-safe space;
- complexity;
- general compatibility.

If both fail in the same systematic way:
STOP.

Do not render the remaining five or six slides.

Fix the systemic prompt/reference issue first.

### Stage B — bulk first pass
Render all remaining paid slides once.

### Stage C — targeted repair
Prefer local edit.
Regenerate only the failing slide when necessary.

Default budget:
- first pass: 1 paid render per planned raster slide;
- targeted regeneration budget: up to 2 additional paid generations per episode before human review;
- exceeding budget requires an explicit reason.

---

## 14. QC hierarchy

### QC-0 — deterministic plan checks
No vision model required:
- slide count;
- every slide has a role;
- no duplicated beat;
- vector text is present where required;
- source refs exist for factual/quoted material;
- render mode valid;
- no missing negative-space spec.

### QC-1 — style / visual grammar
Check:
- `STYLE_LOCK.md`;
- `VISUAL_GRAMMAR.md`;
- simplicity;
- clarity;
- focal hierarchy;
- background density;
- page archetype correctness.

### QC-2 — defect
Check:
- anatomy;
- hands;
- object intersections;
- impossible geometry;
- accidental text;
- continuity failure where required.

### QC-3 — lettering
Deterministic where possible:
- overflow;
- clipping;
- minimum margins;
- bubble-tail target;
- line breaks;
- reading order;
- contrast.

### QC-4 — editorial/taste
Human gate.

Question:
“Would I actually swipe through and post this?”

If no:
return to angle, swipe script, or visual plan.
Do not let an automated QC agent rewrite everything into bland average content.

---

## 15. Human / AI division

### Human must own
1. final approval of topic/angle when the channel is still learning;
2. approval of whole-episode plan before substantial paid rendering, at least during v0.1;
3. final taste/publish decision;
4. explicit style/grammar version changes.

### AI can own
- source normalization;
- candidate angle generation;
- format routing;
- first whole-episode swipe script;
- whole-episode visual direction;
- page specs;
- prompt assembly;
- vector layout draft;
- deterministic QC;
- first defect diagnosis;
- performance logging.

### AI must not own by default
- silent modification of locked style;
- silent modification of locked visual grammar;
- endless auto-regeneration;
- automatic “make it more engaging” rewrites after every metric fluctuation.

---

## 16. Cost map

### Near-zero / local
- JSON validation;
- slide-role validation;
- SVG layout;
- font/layout measurement;
- compositing;
- export;
- simple deterministic QC.

### Low
- one or two LLM planning calls;
- source summarization;
- caption generation;
- focused vision QC.

### Main variable cost
- image generation;
- repeated image regeneration;
- expensive external research if used indiscriminately.

Therefore the system reduces cost by:
1. planning globally before generation;
2. using vector-only pages when sufficient;
3. two-slide style preflight;
4. one first-pass render per raster page;
5. targeted repair instead of complete reruns;
6. no multi-agent debate loops;
7. no recurring-character asset-generation requirement.

---

## 17. Token-cost controls

To reduce LLM token spend:

- reference style by `style_version` during reasoning; inject the full style prompt only at final image-prompt assembly;
- store normalized source once;
- store episode plan as structured JSON;
- renderer receives compact local slide spec + required global continuity digest, not the entire conversation;
- deterministic checks before vision/LLM checks;
- no separate agent for each slide;
- generate the full swipe script and visual plan in one episode-level call;
- cache stable prompt blocks by hash.

---

## 18. Performance feedback

Track by episode:
- format;
- topic / angle;
- slide count;
- cover type;
- landing type;
- raster render count;
- regeneration count;
- production cost;
- production minutes;
- views/reach;
- likes/comments/shares/saves;
- completion/swipe indicators where available;
- qualitative reactions.

Performance may suggest experiments such as:
- shorter episode;
- different cover grammar;
- more/less explainer density;
- different format choice.

It may not automatically mutate `STYLE_LOCK.md` or `VISUAL_GRAMMAR.md`.

---

## 19. v0.1 implementation order

Do not build the full application yet.

1. Lock visual grammar.
2. Create three prototype episodes across the active formats and distinct story shapes.
3. Manually inspect which page archetypes and render modes recur.
4. Finalize JSON schemas.
5. Implement deterministic vector renderer.
6. Implement prompt assembler.
7. Add render manifest / budget tracking.
8. Add deterministic QC.
9. Only then add source automation and performance feedback.

The first prototypes are for extracting the production system, not proving that an autonomous agent can publish unattended.

---

## 20. v0.1 success criterion

The system succeeds when a user can provide a topic/source and, with only a few human approvals, obtain a coherent 5–9 slide Instagram-toon that:

- clearly belongs to the locked visual style;
- has a deliberate whole-episode arc;
- does not depend on recurring character identity;
- uses editable vector lettering;
- does not waste paid generations on slides that do not need them;
- can be corrected locally rather than regenerated from scratch;
- records enough structured data to make the next episode cheaper and more consistent.
