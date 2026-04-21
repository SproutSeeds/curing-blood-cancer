# Clawdad Autonomous Research Loop v0

Stewarded by [frg.earth](https://frg.earth/).

- protocol status: `active-v0`
- delegate target: `curing-blood-cancer`
- disease focus: `multiple-myeloma`
- claim level: `open-question`
- last reviewed: `2026-04-20`
- clinical boundary: research-use-only, not medical advice

## Purpose

This protocol is the standing brief for a Clawdad delegate that continuously
iterates through the public Curing Blood Cancer plan until the planned public
artifacts, schemas, protocols, validators, and contribution tasks are complete.

The loop should build in public from sanitized materials only. It should make
the public surface more useful for researchers, patients, advocates, builders,
and reviewers without exposing private lab context or implying that any cure,
vaccine, treatment, trial, or expanded-access path has been established for any
person.

## North Star

Advance the multiple myeloma lane from a public roadmap into a working,
source-backed research engine and machine-readable disease-state substrate.

The original v0 public loop reached a completion handoff. The active named
phase is now the
[Case-To-Cure Adaptive Master Plan v0](../disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md),
and the delegate should keep moving through that current plan:

- make public artifacts easier to inspect
- convert roadmap items into contribution-ready task queues
- expand source-backed myeloma maps, schemas, and review packets
- improve synthetic case-to-cure plumbing without using real case data
- turn machine-representation notes into synthetic-only schema and fixture
  plumbing before any model weights, predictions, matching, ranking, or
  clinical decision behavior
- add validators before relying on generated outputs
- keep every claim scoped, sourced, and modest
- preserve the frg.earth stewardship mark where appropriate
- after each completed step, synthesize the next safest public step before
  stopping

## Hard Boundaries

The delegate must stop and report a blocker instead of proceeding if work would
require any of the following:

- patient-identifying data, raw records, dates tied to a person, images, free
  text notes, re-identification keys, or real case data
- credentials, secrets, private records, restricted datasets, paid APIs, account
  changes, billing changes, or private lab access that is not already available
- patient-specific diagnosis, prognosis, treatment advice, trial advice,
  expanded-access advice, monitoring instructions, or candidate option ranking
- unsupported cure or vaccine claims
- clinical, legal, regulatory, sponsor, institutional-review, or treating-team
  decisions
- destructive repository operations, commits, pushes, or publication actions
  without explicit human instruction

All outputs must remain research-use-only and not medical advice.

## Required Public Safety Rules

Every artifact the delegate creates or updates must follow these rules:

- include provenance, disease or subtype scope, uncertainty, and limitations
- distinguish facts, derived claims, hypotheses, open questions, and do-not-use
  clinical material
- update metadata and catalog records when adding public artifacts
- keep private upstream references non-sensitive
- keep public artifacts understandable without private context
- preserve the repo boundary: public artifacts only
- run `make validate` after edits that change artifacts, metadata, schemas, or
  validators
- do not overwrite unrelated user work in the working tree

## Canonical Inputs

The loop should inspect these files at the start of a pass:

- `disease-programs/multiple-myeloma/frontier-roadmap-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md`
- `disease-programs/multiple-myeloma/public-roadmap-v0.md`
- `disease-programs/multiple-myeloma/public-loop-completion-handoff-v0.md`
- `protocols/clawdad-frontier-delegation-packet-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md`
- `disease-programs/multiple-myeloma/machine-representation-stack-v0.md`
- `disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-intake-frontend-smoke-test-v0.md`
- `examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md`
- `artifacts/public-artifact-catalog-v0.md`
- `artifacts/public-artifact-catalog-v0.json`
- `orp/frontier/state.json`
- `orp/frontier/additional-items.json`
- `orp/modes/frontier-gap-sweep-mode-v0.md`
- `sources/source-registry-v0.md`
- `schemas/`
- `tools/validate_public_artifacts.py`
- `governance/PUBLIC_SAFETY.md`
- `docs/private-to-public-workflow.md`

## Iteration Queue

Work the queue in public-safe slices. Choose the highest-value item that can be
completed, validated, and explained in one delegate pass.

1. Work the active ORP additional item in the active ORP additional list,
   currently
   `machine-representation-expert-validation-human-authorization-blocker-v0`
   inside
   `post-machine-representation-public-safe-research-substrate-v0`. The
   machine-representation implementation gate remains uncleared; the completed
   MRD geometry falsification phase, no-outreach expert-validation prep,
   internal source-gap extraction pass, frontier gap sweep, residual-disease
   modality-discordance source extraction, assay/specimen quality failure-mode
   checklist, measurement-state refusal fixtures, measurement-refusal output
   schema, measurement-refusal output route table, measurement-refusal
   validator skeleton/report, measurement-refusal negative safety
   fixtures/checker, and measurement-refusal wrapper integration dry
   run/checker, and measurement-refusal wrapper negative safety
   fixtures/checker are public-safe substrates, not expert review or
   authorization for outreach.
2. When an item completes, synthesize and activate or queue the next safe item
   before stopping. After residual-disease modality-discordance extraction, the
   assay/specimen quality checklist, measurement-state refusal fixtures,
   measurement-refusal output schema, measurement-refusal output route table,
   measurement-refusal validator skeleton, measurement-refusal negative
   safety fixtures, measurement-refusal wrapper integration dry run, and
   measurement-refusal wrapper negative safety fixtures are now complete; the
   next no-outreach successor candidate is
   `measurement-refusal-wrapper-state-machine-v0`.
3. Run [ORP Frontier Gap Sweep Mode v0](../orp/modes/frontier-gap-sweep-mode-v0.md)
   when the human asks for a direction check, when a delegate sees stale state,
   or when the next public-safe item is not obvious.
4. Work the expert response intake and validation ledger lane from
   `disease-programs/multiple-myeloma/frontier-roadmap-v0.md`.
5. Work the MRD, deep response, and endpoint language lane.
6. Work the immune therapy sequencing and access boundary lane.
7. Work the post-BCMA resistance and relapse mechanisms lane.
8. Work the precursor, risk, and interception questions lane.
9. Work the high-risk, extramedullary, organ, and frailty context lane.
10. Work the case-to-cure pipeline plumbing lane.
11. Work the public translation and contribution surface lane.
12. Add tooling only when the relevant frontier lane says the validated input
   shape, safety boundary, and public artifact path are unblocked.

## Loop Algorithm

For each autonomous pass:

1. Inspect `git status --short`, the canonical inputs, and validation state.
2. Select exactly one coherent next artifact or tool improvement.
3. State the selected item and why it is the best next move.
4. Make the smallest useful edit set.
5. Add or update metadata, catalog entries, README links, and validation logic
   required by the edit.
6. Run `make validate`.
7. If relevant, run a focused listing command such as
   `make list-public-artifacts ARGS="--scope myeloma"`.
8. Inspect what the completed step revealed and synthesize the next safe step.
9. Activate, queue, or explicitly block that next step in ORP.
10. Report files changed, validation result, and the next recommended queue
   item.
11. If blocked by a hard boundary, stop and write a blocker note instead of
   improvising around the boundary.

## Output Discipline

Each pass should end with a concise status payload that is easy for a human
operator to scan:

```json
{
  "selected_item": "short description",
  "why_now": "one sentence",
  "files_changed": ["relative/path.md"],
  "validation": "passed|failed|not-run",
  "public_safety_check": "passed|blocked",
  "blockers": [],
  "what_completed_step_revealed": "short description",
  "next_step_synthesis": "short description",
  "next_item": "short description"
}
```

## Definition Of Complete

This autonomous loop is complete when:

- `case-to-cure-master-completion-audit-v0` is complete or explicitly blocked
  by a named human gate
- the ORP active additional queue has no pending public-safe item left
- every active frontier roadmap lane has a public artifact, public task,
  schema, protocol, validator, or explicit blocked status
- the case-to-cure blueprint has public-safe schema summaries, gate checklists,
  and synthetic fixtures for each stage
- the first multiple myeloma open research map is present and source-backed
- source registry entries are sufficient for the first open research map
- validators pass across metadata, catalogs, source links, task references, and
  schema examples
- public README and catalog paths make the work navigable
- all remaining case-specific steps are represented as private-lab tasks or
  human-gated blockers
- remaining frontier work is labeled as expert-review-needed,
  private-lab-needed, clinical-team-needed, or human-publication-gate-needed

## Review Boundary

This protocol directs public research operations. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance,
expanded-access guidance, or a claim that a cure or vaccine has been found.
