# Clawdad Autonomous Research Loop v0

Stewarded by [frg.earth](https://frg.earth/).

- protocol status: `active-v0`
- delegate target: `curing-blood-cancer`
- disease focus: `multiple-myeloma`
- claim level: `open-question`
- last reviewed: `2026-04-15`
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
source-backed research engine.

The delegate should keep moving through the current plan:

- make public artifacts easier to inspect
- convert roadmap items into contribution-ready task queues
- expand source-backed myeloma maps, schemas, and review packets
- improve synthetic case-to-cure plumbing without using real case data
- add validators before relying on generated outputs
- keep every claim scoped, sourced, and modest
- preserve the frg.earth stewardship mark where appropriate

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

- `disease-programs/multiple-myeloma/public-roadmap-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md`
- `examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md`
- `artifacts/public-artifact-catalog-v0.md`
- `artifacts/public-artifact-catalog-v0.json`
- `sources/source-registry-v0.md`
- `schemas/`
- `tools/validate_public_artifacts.py`
- `governance/PUBLIC_SAFETY.md`
- `docs/private-to-public-workflow.md`

## Iteration Queue

Work the queue in public-safe slices. Choose the highest-value item that can be
completed, validated, and explained in one delegate pass.

1. Convert the multiple myeloma roadmap into contribution-ready public task
   queues.
2. Turn the synthetic case-to-cure example into private-lab template
   specifications and public task drafts without adding real case data.
3. Draft a public-safe `case-feature-bundle` schema summary that describes
   allowed shape without inviting case upload.
4. Extend the ClinicalTrials.gov query protocol with provenance fields for
   case-matching research use.
5. Add a candidate-option scoring rubric that separates standard-care review,
   trial review, expanded-access review, research-only hypotheses, and no-go
   records.
6. Add a publication-gate checklist for any case-derived public learning.
7. Create a multidisciplinary multiple myeloma review packet template.
8. Draft `Multiple Myeloma Open Research Map v0.1`.
9. Expand the source registry for target, therapy, trial, regulatory, and
   dataset sources.
10. Define disease-map, target, therapy, trial, open-question, and public-task
    schemas before building generation scripts.
11. Add tooling only on top of validated shapes: evidence graph, trial explorer,
    target prioritization, extraction helpers, and review packet builders.

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
8. Report files changed, validation result, and the next recommended queue
   item.
9. If blocked by a hard boundary, stop and write a blocker note instead of
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
  "next_item": "short description"
}
```

## Definition Of Complete

This autonomous loop is complete when:

- every roadmap item has a public artifact, public task, schema, protocol,
  validator, or explicit blocked status
- the case-to-cure blueprint has public-safe schema summaries, gate checklists,
  and synthetic fixtures for each stage
- the first multiple myeloma open research map is present and source-backed
- source registry entries are sufficient for the first open research map
- validators pass across metadata, catalogs, source links, task references, and
  schema examples
- public README and catalog paths make the work navigable
- all remaining case-specific steps are represented as private-lab tasks or
  human-gated blockers

## Review Boundary

This protocol directs public research operations. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance,
expanded-access guidance, or a claim that a cure or vaccine has been found.
