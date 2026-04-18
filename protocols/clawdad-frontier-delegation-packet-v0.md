# Clawdad Frontier Delegation Packet v0

Stewarded by [frg.earth](https://frg.earth/).

- protocol status: `active-frontier-v0`
- delegate target: `curing-blood-cancer`
- disease focus: `multiple-myeloma`
- claim level: `open-question`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only, not medical advice

## Purpose

This packet is the standing brief for Clawdad to delegate the full
[Multiple Myeloma ORP Frontier Roadmap v0](../disease-programs/multiple-myeloma/frontier-roadmap-v0.md)
to completion in public-safe autonomous passes.

The delegate should work through the frontier lanes until each lane has a first
useful public artifact, metadata, catalog coverage, navigation links,
validation, and either a clear next task or an explicit blocker.

The delegate must not use real case data, send outreach, publish private
responses, claim a cure, or produce medical advice.

## North Star

Advance the multiple myeloma public program from completed v0 scaffolding into
a frontier operating map that can support expert validation, public
contribution, and future private-lab case work.

The live operating mode is adaptive. A completed public-safe step must produce
a handoff and a next-step synthesis. A closed subphase is not a reason to stop
unless the adaptive master completion audit says the public-safe scope is
complete or an explicit human gate blocks all next work.

The useful output is not more words. The useful output is a public research
system where each artifact answers:

- what question it helps inspect
- what public sources support it
- what is uncertain
- what it cannot be used for
- what validator or gate prevents unsafe downstream use
- what the next contribution-ready task is

## Durable Adaptive Mode

The delegate must treat
`disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md`
as the canonical operating plan.

For every pass:

1. read the active ORP live state in `orp/frontier/state.json`
2. read the active additional queue in `orp/frontier/additional-items.json`
3. complete one public-safe step or report the exact blocker
4. inspect what the completed step revealed
5. write or update a completion handoff when a step or subplan closes
6. synthesize the next safest public step
7. queue, activate, or block that step explicitly

Do not mark the multiple myeloma initiative complete because the case-intake
phase, frontier lanes, or a small additional item completed. Those are
subphase completions. The active master queue is complete only after
`case-to-cure-master-completion-audit-v0` is complete or blocked by a named
expert, private-lab, clinical, legal, regulatory, publication, or compute gate.

## Hard Stops

Stop and report a blocker instead of proceeding if a task requires:

- patient-identifying data, raw records, notes, dates tied to a person, images,
  private case data, or re-identification keys
- credentials, secrets, restricted datasets, paid APIs, account changes, or
  private lab access that is not already available
- diagnosis, prognosis, treatment advice, trial advice, expanded-access advice,
  monitoring advice, screening advice, or candidate option ranking
- unsupported cure, vaccine, treatment-path, or clinical-outcome claims
- copying private expert emails or unpublished private correspondence into
  public artifacts
- autonomous outreach, commits, pushes, releases, destructive repository
  operations, billing changes, or publication actions
- clinical, legal, regulatory, sponsor, institutional-review, or treating-team
  decisions

All outputs must stay research-use-only and not medical advice.

## Required Inputs

Inspect these files at the start of each pass:

- `disease-programs/multiple-myeloma/frontier-roadmap-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md`
- `disease-programs/multiple-myeloma/public-roadmap-v0.md`
- `disease-programs/multiple-myeloma/public-loop-completion-handoff-v0.md`
- `disease-programs/multiple-myeloma/public-inventory-v0.md`
- `disease-programs/multiple-myeloma/reviews/expert-validation-issue-index-v0.md`
- `disease-programs/multiple-myeloma/reviews/expert-validation-outreach-map-v0.md`
- `disease-programs/multiple-myeloma/case-intake/caregiver-case-intake-product-spec-v0.md`
- `disease-programs/multiple-myeloma/case-intake/caregiver-intake-public-projection-checklist-v0.md`
- `disease-programs/multiple-myeloma/case-intake/private-intake-schema-contract-v0.md`
- `disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-prototype-plan-v0.md`
- `disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-intake-frontend-v0.html`
- `disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-intake-frontend-smoke-test-v0.md`
- `disease-programs/multiple-myeloma/case-intake/caregiver-intake-public-projection-validator-v0.md`
- `disease-programs/multiple-myeloma/case-intake/consent-privacy-security-retention-gate-v0.md`
- `disease-programs/multiple-myeloma/case-feature-normalization-contract-v0.md`
- `disease-programs/multiple-myeloma/machine-representation-stack-v0.md`
- `disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md`
- `disease-programs/multiple-myeloma/measurements/mrd-endpoint-language-guardrail-addendum-v0.md`
- `disease-programs/multiple-myeloma/measurements/measurement-normalization-contract-v0.md`
- `taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md`
- `disease-programs/multiple-myeloma/therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md`
- `disease-programs/multiple-myeloma/therapy-landscapes/therapy-exposure-timeline-contract-v0.md`
- `disease-programs/multiple-myeloma/contexts/molecular-immune-context-contract-v0.md`
- `disease-programs/multiple-myeloma/evidence-retrieval-packet-v0.md`
- `disease-programs/multiple-myeloma/therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md`
- `disease-programs/multiple-myeloma/reviews/candidate-hypothesis-review-question-set-v0.md`
- `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-builder-v0.md`
- `disease-programs/multiple-myeloma/reviews/expert-validation-loop-v0.md`
- `disease-programs/multiple-myeloma/case-to-public-learning-extraction-gate-v0.md`
- `disease-programs/multiple-myeloma/end-to-end-synthetic-case-dry-run-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md`
- `protocols/clinicaltrials-gov-query-protocol-v0.md`
- `examples/multiple-myeloma-synthetic-caregiver-intake-v0.json`
- `examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md`
- `artifacts/public-artifact-catalog-v0.md`
- `artifacts/public-artifact-catalog-v0.json`
- `orp/frontier/state.json`
- `orp/frontier/version-stack.json`
- `orp/frontier/additional-items.json`
- `sources/source-registry-v0.md`
- `schemas/`
- `tools/validate_public_artifacts.py`
- `governance/PUBLIC_SAFETY.md`
- `docs/private-to-public-workflow.md`

## Delegation Queue

Choose the highest-value unblocked slice that can be completed, validated, and
reported in one pass. Work in this order unless validation or dependency state
makes another slice clearly safer.

### Active Named Phase. Case-To-Cure Adaptive Master Plan v0

The current active named phase is `myeloma-machine-representation-implementation-v0`
inside `case-to-cure-adaptive-master-plan-v0`.
The active phase is `myeloma-machine-representation-implementation-v0`.
The active additional queue is `myeloma-machine-representation-implementation-v0`.
The active additional item is `myeloma-state-object-schema-v0`.

This phase follows the smoke-tested static caregiver frontend prototype. The
next public-safe work is machine-state schema plumbing derived from the
myeloma machine representation stack, while real case data, model weights,
patient-specific predictions, and clinical decision behavior stay blocked.

Required output for the next pass:

- define the smallest useful public `myeloma-state-object-schema-v0` artifact
  for synthetic-only disease-state examples
- use [Myeloma Machine Representation Stack v0](../disease-programs/multiple-myeloma/machine-representation-stack-v0.md),
  case-feature normalization, measurement normalization, therapy exposure
  timeline, molecular/immune context, evidence retrieval, and public safety
  governance as boundaries
- represent source context, tumor genomic events, transcriptome state, marrow
  ecosystem state, clinical context, treatment timeline, measurement timeline,
  missingness, uncertainty, and review status without accepting real case data
- keep every field non-directive and source-scoped; use unknown/not-tested/
  not-collected states instead of inferring absence
- include synthetic example expectations or fixture notes only if they cannot
  be mistaken for a real person
- block real case data, identifiers, raw records, uploads, person-linked
  dates, free-text case details, private correspondence, patient-specific
  outputs, recommendations, rankings, matching, treatment guidance, trial
  guidance, expanded-access guidance, monitoring guidance, publication
  authorization, clinical judgment, outreach, private lab access, and
  publication decisions

Done when:

- the selected deliverable exists as a public-safe artifact, validator,
  fixture, navigation update, or explicit blocker note
- no real case data, identifiers, records, uploads, or free-text case details
  appear in the public repo
- no output can be read as diagnosis, prognosis, treatment advice, trial
  advice, monitoring advice, urgency guidance, expanded-access guidance, or a
  cure claim
- the ORP additional queue has either an active next item, a pending next item,
  or a specific blocker explaining why no public-safe next item can run
- `make validate` passes

Stop instead of proceeding if the next step requires a real case, a live
backend, credentials, private lab access, clinical interpretation, outreach, or
publication approval. If that happens, write the blocker and move to the next
public-safe adjacent item when one exists.

### 1. Expert Response Intake And Validation Ledger

Create a public-safe ledger or status map for existing expert validation issues.

Required output:

- an artifact that maps review items to public-safe status, allowed
  dispositions, artifact paths, and next actions
- metadata and catalog entry
- disease-program README link
- no copied private correspondence

Done when:

- all existing expert validation items have a status and next public action
- any expert response content is represented only as a safe disposition unless
  public permission and public source context exist

### 2. MRD, Deep Response, And Endpoint Language

Create or extend a measurement/endpoint artifact that prevents MRD and response
language from becoming cure claims.

Required output:

- endpoint addendum or guardrail note
- source-backed fields for method, threshold, sample, timepoint, durability,
  endpoint status, and limitations
- public tasks for missing source extraction

Done when:

- downstream artifacts can reference response depth without implying cure
- unresolved terms stay marked expert-review-needed or source-context-needed

### 3. Immune Therapy Sequencing And Access Boundary

Create or extend immune therapy landscape records without clinical guidance.

Required output:

- therapy landscape or target-class crosswalk artifact
- status freshness fields and source IDs
- explicit no-availability, no-eligibility, no-ranking boundary

Done when:

- CAR T, bispecific, antibody-drug conjugate, and adjacent target references
  have status, date, and uncertainty fields before any explorer or dashboard
  work

### 4. Post-BCMA Resistance And Relapse Mechanisms

Expand public mechanism and evidence-gap coverage for post-BCMA relapse.

Required output:

- mechanism addendum or extraction queue
- gap register updates
- claim levels for every mechanism statement

Done when:

- antigen and non-antigen mechanism questions link to public contribution tasks
- no mechanism statement implies patient-specific action

### 5. Precursor, Risk, And Interception Questions

Define public boundaries for MGUS, smoldering multiple myeloma, early
intervention, and prevention-adjacent language.

Required output:

- boundary note
- source registry delta or explicit no-add reason
- open-question queue

Done when:

- precursor language cannot be read as screening advice, personal risk advice,
  or treatment advice

### 6. High-Risk, Extramedullary, Organ, And Frailty Context

Create a public-safe disease-context modifier map.

Required output:

- context taxonomy or case-feature bundle addendum
- synthetic fixture coverage for modifier fields, if schemas are touched
- review-packet checklist update, if applicable

Done when:

- context fields are optional, non-identifying, and cannot produce prognosis or
  option ranking

### 7. Case-To-Cure Pipeline Plumbing

Make the dry-run pipeline exact enough to serve a future private-lab case.

Required output:

- stage validator map, dry-run graph, or blocker-to-private-lab task map
- links to owner artifacts, validators, and blocked conditions for every stage
- no real case data

Done when:

- every stage from private intake to public learning extraction has an owner
  artifact, gate, and blocker field

### 8. Public Translation And Contribution Surface

Make the public surface easier for non-specialists and contributors.

Required output:

- plain-language companion, glossary index, contribution guide, or issue
  template packet
- clear clinical-use boundary
- links from the disease-program README

Done when:

- non-specialists can navigate safely and contributors know exactly what review
  task is being requested

## Loop Algorithm

For each pass:

1. Inspect `git status --short`.
2. Read the required inputs.
3. Select exactly one queue slice.
4. State the selected slice and why it is the best next move.
5. Make the smallest useful edit set.
6. Add or update metadata, catalog entries, README links, protocol links, and
   validation logic required by the edit.
7. Run `make validate`.
8. If relevant, run `make list-public-artifacts ARGS="--scope myeloma"`.
9. Report changed files, validation result, public-safety check, blockers, and
   next queue slice.
10. Stop if remaining work requires expert responses, real case data, clinical
    judgment, private lab access, outreach, or a human publication decision.

## Output Payload

End each pass with a concise status payload:

```json
{
  "selected_frontier_lane": "short description",
  "why_now": "one sentence",
  "files_changed": ["relative/path.md"],
  "validation": "passed|failed|not-run",
  "public_safety_check": "passed|blocked",
  "lane_status": "advanced|complete|blocked",
  "blockers": [],
  "what_completed_step_revealed": "short description",
  "next_step_synthesis": "short description",
  "next_frontier_lane": "short description"
}
```

## Definition Of Complete

The frontier delegation loop is complete when:

- `case-to-cure-master-completion-audit-v0` is complete or blocked by a named
  human gate
- the active ORP additional queue has no pending public-safe item left
- every frontier lane in
  `disease-programs/multiple-myeloma/frontier-roadmap-v0.md` has a first public
  artifact or explicit blocked status
- every new artifact has metadata and appears in both public catalogs
- the disease-program README and protocol README link to the frontier work
- expert validation issues have public-safe statuses and next actions
- MRD and endpoint language has guardrails against cure overclaiming
- immune therapy and trial references are date-scoped and non-advisory
- post-BCMA resistance gaps have public task coverage
- precursor and high-risk context language is bounded and non-directive
- the case-to-cure dry run maps each stage to owner artifacts, validators, and
  blockers
- public translation artifacts make contribution safer for non-specialists
- `make validate` passes
- all remaining work is explicitly labeled as expert-review-needed,
  private-lab-needed, clinical-team-needed, or human-publication-gate-needed

## Review Boundary

This protocol directs public autonomous research operations. It does not
provide medical advice, diagnostic guidance, treatment guidance, trial guidance,
expanded-access guidance, screening guidance, monitoring guidance, or a claim
that a cure or vaccine has been found.
