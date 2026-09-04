# WORKFLOW_PROTOCOL.md

# CROSS-ENVIRONMENT WORKFLOW / "갱신" PROTOCOL v1.0

**Effective:** 2026-09-04

Purpose:
Preserve project state, exact decisions, prompts, assets, execution evidence, and next actions so work can move between ChatGPT, Claude, local/manual work, and future environments without silently restarting or losing critical detail.

## 0. Trigger

When the user says **"갱신"**, run the full repository reconciliation process in this document.

"갱신" does not mean append another handoff note. It means:
1. reconcile what changed;
2. modify authoritative existing files;
3. create a new file only for a genuinely new durable artifact/authority;
4. remove or explicitly supersede contradictions;
5. update exact current state and next action;
6. commit/push;
7. verify the remote result;
8. when the AutoPipeline parent exists, update its child-repository pointer too.

## 1. Single-source-of-truth principle

Never rely on chat memory as the only copy of a durable decision.

If a clean environment would need something to continue correctly, preserve it in GitHub:
- project purpose / big flow;
- current phase;
- locked design/style/architecture;
- exact reusable prompts;
- exact asset/reference identities and paths;
- source/provenance;
- episode/experiment state;
- known failure modes;
- QC results;
- execution parameters;
- real blockers;
- exact next action.

## 2. Prefer modification over file proliferation

Do not create NEW_SESSION_HANDOFF, LATEST, FINAL_FINAL, or session-specific state files when an existing canonical file can be updated coherently.

Create a new file only if it is:
1. a new authority layer with a distinct lifecycle;
2. a reusable specification/schema/protocol;
3. an independently auditable episode/experiment/source artifact;
4. a binary/reference asset that cannot be represented losslessly in existing text.

Git history is the archive. Canonical files represent the present.

Do not delete a rule or explanation merely because it came from an older version. During reconciliation:
- preserve any still-valid constraint, rationale, failure lesson, prompt fragment, or evidence;
- merge it into the current authoritative section when it still applies;
- label superseded execution evidence as historical rather than leaving it phrased as a current blocker;
- remove text from the present-state view only when it is duplicated, contradicted by an approved newer rule, or no longer needed to continue correctly.

## 3. Start-of-session restore

Before substantive work:
1. identify the active repository/project;
2. read its README entrypoint;
3. read CURRENT_STATE;
4. follow the authority hierarchy from those files;
5. read the active episode/experiment package;
6. inspect recent relevant commits when needed;
7. do not re-plan from scratch if the repository already defines the state.

If another model/session changed the repo, fetch remote state again before acting.

## 4. During-work recording rule

Record durable evidence in the proper existing artifact:
- architecture decision -> architecture/lock document;
- style failure -> style/generation protocol + active episode evidence;
- exact production outcome -> episode/experiment package;
- changed next action -> CURRENT_STATE;
- changed entrypoint/authority hierarchy -> README.

Keep ephemeral reasoning out unless it changes a durable decision.

## 5. "갱신" reconciliation order

A. Decision reconciliation
- what changed;
- what remains unchanged;
- what old text is now wrong/superseded;
- new blockers;
- new verified evidence.

B. Update durable authorities first if their rules changed.

C. Update the active episode/experiment/source package with exact result, pass/fail, defects, relevant prompt/settings, and next retry condition.

D. Update CURRENT_STATE last with:
- big flow;
- exact detailed current stage;
- completed work;
- current blocker/failure;
- immediate next actions in executable order.

E. Update README only if entrypoint, authority order, project purpose, or canonical-file discovery changed.

F. Commit/push with clear semantic messages.

G. Verify by refetching changed files and/or latest commit. Do not say "updated" until remote state is verified.

H. When `noru358/AutoPipeline` exists:
- update child first;
- advance parent submodule pointer to the verified child commit;
- update parent cross-project state only when needed;
- push and verify parent.

## 6. Asset integrity

Text is not a lossless substitute for important visual/audio assets.

If an asset is a real authority, preserve the actual file in the repository when practical.

Examples:
- canonical style reference images;
- approved master images;
- exact production audio master;
- final render/export.

Do not claim an asset is preserved unless the remote path has been verified.

For large/transient outputs, preserve at minimum exact filename/ID/hash, generation settings, verdict, reason it matters, and authoritative-original location.

## 7. Generative reference rule

If visual identity depends on a reference image:
- the actual approved reference image outranks prose;
- prompts reinforce it; they do not replace it;
- a failed generated image must never become the sole style reference for the next generation;
- style reference and scene/continuity reference are separate roles;
- style reference wins on rendering language.

If the canonical visual reference is unavailable in the current environment, stop production generation rather than inventing the style from text.

## 8. Environment portability

Use repository-relative paths in canonical docs.

Do not depend on:
- one computer's Desktop path;
- one chat's hidden context;
- one model's memory;
- an unrecorded UI selection.

When environment setup matters, record tool/runtime, required version if relevant, environment variable names only, and restoration commands.

Never commit secrets or API keys.

## 9. AutoPipeline parent architecture

Target parent:
`noru358/AutoPipeline`

Use a **Git superproject + submodules**, not copied nested repositories.

Target tree:

```text
AutoPipeline/
├── README.md
├── WORKFLOW_PROTOCOL.md
├── .gitmodules
├── instatoon/   -> noru358/instatoon @ exact commit
└── talkshow/    -> noru358/talkshow @ exact commit
```

Why submodules:
- preserves each child repository's independent history;
- parent records the exact child commit combination;
- avoids duplicate/copy drift;
- supports reproducible environment restoration.

Clone:
```bash
git clone --recurse-submodules <AutoPipeline repo URL>
```

Restore:
```bash
git submodule update --init --recursive
```

Child-specific authorities remain inside each child repository.

## 10. Definition of "lossless"

"Lossless" means a competent model/person in a clean environment can determine:
- what the project is;
- what is locked;
- what has been tried;
- what failed and why;
- exact current state;
- which assets/prompts are authoritative;
- what to do next;

without the previous chat transcript.

It does not mean dumping every conversation sentence into GitHub.

Preserve decision/state fidelity, not conversational noise.
