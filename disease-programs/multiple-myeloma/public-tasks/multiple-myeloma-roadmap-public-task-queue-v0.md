# Multiple Myeloma Roadmap Public Task Queue v0

Stewarded by [frg.earth](https://frg.earth/).

This queue turns the multiple myeloma public roadmap and case-to-cure blueprint
into contribution-ready public tasks. It is a bridge from the roadmap to
reviewable pull requests, not a clinical priority list.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not expanded-access guidance.
- Not a claim that multiple myeloma has been cured.
- Task priority means public artifact readiness, not patient relevance,
  evidence strength, biological importance, or treatment value.

## Source Artifacts

- [Multiple Myeloma Public Roadmap v0](../public-roadmap-v0.md)
- [Case-To-Cure Pipeline Blueprint v0](../case-to-cure-pipeline-blueprint-v0.md)
- [BCMA Antigen Escape Evidence Gap Register v0](../evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md)
- [Source Registry v0](../../../sources/source-registry-v0.md)

## Scope Note

This first roadmap queue uses currently validated public gap IDs so the tasks
can pass the existing public-task schema. The gap anchors are strongest for
BCMA and post-CAR T relapse artifacts. A future pass should add a broader
non-BCMA roadmap gap register before treating these tasks as comprehensive
coverage of the myeloma program.

## Task Status

| Task ID | Priority | Status | Issue Form | Linked Gap |
| --- | --- | --- | --- | --- |
| `multiple-myeloma-open-research-map-task-v0` | high | done | pull request | `non-antigen-loss-relapse-buckets-gap-v0` |
| `multiple-myeloma-source-registry-expansion-task-v0` | high | done | source extraction | `non-antigen-loss-relapse-buckets-gap-v0` |
| `multiple-myeloma-disease-map-schema-task-v0` | high | done | pull request | `bcma-measurement-context-completeness-gap-v0` |
| `multiple-myeloma-schema-tooling-phase-inventory-task-v0` | high | done | pull request | `bcma-measurement-context-completeness-gap-v0` |
| `multiple-myeloma-target-record-schema-task-v0` | high | done | pull request | `alternate-target-clinical-translation-gap-v0` |
| `multiple-myeloma-therapy-record-schema-task-v0` | high | done | pull request | `alternate-target-clinical-translation-gap-v0` |
| `multiple-myeloma-trial-landscape-record-schema-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-open-question-record-schema-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-tooling-readiness-gate-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-manifest-spec-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-manifest-schema-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-dry-run-plan-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-implementation-gate-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-route-table-script-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-case-specific-private-lab-blocker-register-task-v0` | high | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-case-feature-bundle-summary-task-v0` | high | done | pull request | `bcma-measurement-context-completeness-gap-v0` |
| `multiple-myeloma-candidate-option-scoring-rubric-task-v0` | medium | done | pull request | `alternate-target-clinical-translation-gap-v0` |
| `multiple-myeloma-publication-gate-checklist-task-v0` | medium | done | pull request | `expert-review-readiness-gap-v0` |
| `multiple-myeloma-multidisciplinary-review-packet-task-v0` | medium | done | expert review | `expert-review-readiness-gap-v0` |

## Issue Drafts

- [Open research map task](issue-drafts/multiple-myeloma-open-research-map-task-v0.md)
- [Source registry expansion task](issue-drafts/multiple-myeloma-source-registry-expansion-task-v0.md)
- [Disease-map schema task](issue-drafts/multiple-myeloma-disease-map-schema-task-v0.md)
- [Schema/tooling phase inventory task](issue-drafts/multiple-myeloma-schema-tooling-phase-inventory-task-v0.md)
- [Target-record schema task](issue-drafts/multiple-myeloma-target-record-schema-task-v0.md)
- [Therapy-record schema task](issue-drafts/multiple-myeloma-therapy-record-schema-task-v0.md)
- [Trial-landscape record schema task](issue-drafts/multiple-myeloma-trial-landscape-record-schema-task-v0.md)
- [Open-question record schema task](issue-drafts/multiple-myeloma-open-question-record-schema-task-v0.md)
- [Tooling readiness gate task](issue-drafts/multiple-myeloma-tooling-readiness-gate-task-v0.md)
- [Review-packet builder manifest spec task](issue-drafts/multiple-myeloma-review-packet-builder-manifest-spec-task-v0.md)
- [Review-packet builder manifest schema task](issue-drafts/multiple-myeloma-review-packet-builder-manifest-schema-task-v0.md)
- [Review-packet builder dry-run plan task](issue-drafts/multiple-myeloma-review-packet-builder-dry-run-plan-task-v0.md)
- [Review-packet builder implementation gate task](issue-drafts/multiple-myeloma-review-packet-builder-implementation-gate-task-v0.md)
- [Review-packet builder route-table script task](issue-drafts/multiple-myeloma-review-packet-builder-route-table-script-task-v0.md)
- [Review-packet builder route-table output schema task](issue-drafts/multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0.md)
- [Review-packet builder packet-assembly gate task](issue-drafts/multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0.md)
- [Review-packet builder packet-skeleton spec task](issue-drafts/multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0.md)
- [Case-specific private-lab blocker register task](issue-drafts/multiple-myeloma-case-specific-private-lab-blocker-register-task-v0.md)
- [Case-feature bundle summary task](issue-drafts/multiple-myeloma-case-feature-bundle-summary-task-v0.md)
- [Candidate-option scoring rubric task](issue-drafts/multiple-myeloma-candidate-option-scoring-rubric-task-v0.md)
- [Publication-gate checklist task](issue-drafts/multiple-myeloma-publication-gate-checklist-task-v0.md)
- [Multidisciplinary review packet task](issue-drafts/multiple-myeloma-multidisciplinary-review-packet-task-v0.md)

## Task Notes

### Open Research Map

Draft `Multiple Myeloma Open Research Map v0.1` as a navigation artifact that
links the wedge, measurement glossary, mechanism map, source registry, public
tasks, and review boundaries. It must separate facts, derived claims,
hypotheses, and open questions.

Current public deliverable:

- [Multiple Myeloma Open Research Map v0.1](../open-research-map-v0-1.md)
- [Open Research Map v0.1 JSON Companion](../open-research-map-v0-1.json)

### Source Registry Expansion

Add reusable target, therapy, trial, regulatory, and dataset source anchors
before new maps or tools depend on them. New source records should state what
they can and cannot prove.

Current public deliverable:

- [Source Registry v0](../../../sources/source-registry-v0.md), expanded with
  target, therapy, trial, regulatory, labeling, and dataset source anchors.

### Disease-Map Schema

Define the validated shape for disease-map, target, therapy, trial,
open-question, and task references before building generation scripts.

Current public deliverable:

- [Disease Map Schema v0](../../../schemas/disease-map-schema-v0.md), with
  JSON schema, template record, and validator coverage.

### Schema And Tooling Phase Inventory

Current extraction-ready tasks are complete for v0 navigation. Before adding
evidence graph, trial explorer, target prioritization, extraction-helper, or
review-packet builder tooling, inventory the next schema slices and choose the
next validated shape deliberately.

Ready public task:

- [Schema/tooling phase inventory task](issue-drafts/multiple-myeloma-schema-tooling-phase-inventory-task-v0.md), completed by
  [Multiple Myeloma Schema And Tooling Phase Inventory v0](../schema-tooling-phase-inventory-v0.md)

### Target-Record Schema

The schema/tooling phase inventory selects target-record schema as the next
validated shape. This should land before evidence graph, target prioritization,
extraction-helper, therapy-record, or trial-landscape tooling depends on target
fields.

Current public deliverable:

- [Target Record Schema v0](../../../schemas/target-record-schema-v0.md), with
  JSON schema, template record, and validator coverage.

### Therapy-Record Schema

Target Record Schema v0 now defines the public target-context contract. The
next validated shape should define therapy records before evidence graph,
therapy landscape, trial explorer, extraction-helper, or review-packet-builder
tooling depends on therapy fields.

Current public deliverable:

- [Therapy Record Schema v0](../../../schemas/therapy-record-schema-v0.md),
  with JSON schema, template record, and validator coverage.

### Trial-Landscape Record Schema

Target Record Schema v0 and Therapy Record Schema v0 now define target and
therapy-context contracts. The next validated shape should define
trial-landscape records with registry provenance, freshness, and no-eligibility
boundaries before trial explorer or evidence graph tooling depends on trial
fields.

Current public deliverable:

- [Trial-Landscape Record Schema v0](../../../schemas/trial-landscape-record-schema-v0.md),
  with JSON schema, template record, and validator coverage.

### Open-Question Record Schema

Target Record Schema v0, Therapy Record Schema v0, and Trial-Landscape Record
Schema v0 now define public target, therapy, and trial-landscape contracts.
Open-Question Record Schema v0 defines public research-question records before
evidence graph, map-builder, extraction-helper, or review-packet-builder
tooling depends on question fields.

Current public deliverable:

- [Open-Question Record Schema v0](../../../schemas/open-question-record-schema-v0.md),
  with JSON schema, template record, and validator coverage.

### Tooling Readiness Gate

Disease Map Schema v0, Target Record Schema v0, Therapy Record Schema v0,
Trial-Landscape Record Schema v0, Open-Question Record Schema v0, and the
public task queue shape now provide validated inputs for an aggregate readiness
gate. The gate decides whether a smallest safe first tooling slice exists
before any evidence graph, trial explorer, target prioritization,
extraction-helper, review-packet-builder, or generator work begins.

Current public deliverable:

- [Multiple Myeloma Tooling Readiness Gate v0](../tooling-readiness-gate-v0.md),
  which selects a review-packet builder input manifest specification as the
  next spec-only slice and keeps implementation tooling blocked.

### Review-Packet Builder Manifest Spec

The tooling readiness gate selects a review-packet builder input manifest
specification as the smallest safe next slice. The specification defines public
input shape, validation expectations, and no-generated-claim boundaries before
any builder code exists.

Current public deliverable:

- [Review-Packet Builder Input Manifest Spec v0](../reviews/review-packet-builder-manifest-spec-v0.md),
  which selects manifest schema and validator coverage as the next finite
  contract before builder code.

### Review-Packet Builder Manifest Schema

The manifest specification names the fields, forbidden fields, and fail-closed
validation expectations. The schema task turns that specification into a
validated JSON schema and placeholder template before any review-packet-builder
code exists.

Current public deliverable:

- [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md),
  with JSON schema, placeholder manifest, and validator coverage.

### Review-Packet Builder Dry-Run Plan

The manifest schema validates public input references, but builder code remains
blocked until a dry-run plan states what a future builder may copy, reference,
omit, or refuse without generating or strengthening biomedical claims.

Current public deliverable:

- [Review-Packet Builder Dry-Run Plan v0](../reviews/review-packet-builder-dry-run-plan-v0.md),
  with no-code copy, reference, omit, and refuse behavior.

### Review-Packet Builder Implementation Gate

The manifest schema and dry-run plan are now public-safe prerequisites, but
builder code remains blocked until an aggregate implementation gate decides
whether a smallest safe code slice can exist without generated claims,
patient-specific outputs, ranking, recommendation, or publication behavior.

Current public deliverable:

- [Review-Packet Builder Implementation Gate v0](../reviews/review-packet-builder-implementation-gate-v0.md),
  which conditionally selects a deterministic copied-reference route-table
  dry-run script as the next smallest safe code slice.

### Review-Packet Builder Route-Table Script

The implementation gate permits only a deterministic local script that reads
public placeholder inputs, validates copied references, reports missing inputs
and refusals, and does not assemble packets or generate biomedical prose.

Current public deliverables:

- [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../../tools/review_packet_manifest_route_table.py)
- [Route-table placeholder fixture](../../../examples/review-packet-builder-route-table-placeholder-fixture-v0.json)
- [Forbidden-field refusal fixture](../../../examples/review-packet-builder-forbidden-input-fixture-v0.json)

### Review-Packet Route-Table Output Schema

The copied-reference route-table tool now needs a validated output contract
before any downstream review-packet workflow can rely on its records. This next
step should define the route-table output shape and validator coverage only.
It must not assemble packets or generate biomedical prose.

Current public deliverables:

- [Review-Packet Route-Table Output Schema v0](../../../schemas/review-packet-route-table-output-schema-v0.md)
- [Review-packet route-table output fixture](../../../examples/review-packet-route-table-output-fixture-v0.json)

### Review-Packet Builder Packet-Assembly Gate

The manifest, route-table tool, route-table output schema, and dry-run policy
now exist. The next step should be a no-code aggregate gate that decides
whether packet assembly remains blocked or whether one smallest safe downstream
slice can be selected. It must not build packet assembly or generate biomedical
prose.

Current public deliverable:

- [Review-packet builder packet-assembly gate task](issue-drafts/multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0.md)
- [Review-Packet Builder Packet-Assembly Gate v0](../reviews/review-packet-builder-packet-assembly-gate-v0.md)

### Review-Packet Builder Packet-Skeleton Spec

The packet-assembly gate keeps packet assembly blocked and selects one
spec-only next slice. The next step should define empty packet section slots
that preserve copied route-table references, missing inputs, refusals, review
status, limitations, and boundaries without filling sections or generating
claims.

Current public deliverable:

- [Review-packet builder packet-skeleton spec task](issue-drafts/multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0.md)
- [Review-Packet Builder Packet-Skeleton Spec v0](../reviews/review-packet-builder-packet-skeleton-spec-v0.md)

Next action:

- [Review-Packet Builder Recombination Handoff v0](../reviews/review-packet-builder-recombination-handoff-v0.md)
  now closes the current review-builder lane.
- [Definition-Of-Complete Audit v0](../definition-of-complete-audit-v0.md)
  now identifies the case-specific private-lab blocker register as the single
  next ready public task.

### Case-Specific Private-Lab Blocker Register

The definition-of-complete audit found that real case-specific steps are
described across the blueprint, stage gates, and private-to-public workflow,
but are not yet consolidated as public-safe private-lab or human-gated
blockers.

Current public deliverable:

- [Case-Specific Private-Lab Blocker Register v0](../case-specific-private-lab-blocker-register-v0.md)

Completion handoff:

- [Public Loop Completion Handoff v0](../public-loop-completion-handoff-v0.md)
  selects no new ready public task and closes the current v0 autonomous public
  loop until a new named phase, human review, or aggregate gate is created.

### Case-Feature Bundle Summary

Write a public-safe summary of the private-only `case-feature-bundle` shape.
The summary should describe allowed structure while refusing real case upload,
free-text notes, dates tied to a person, identifiers, or patient-specific use.

Current public deliverable:

- [Case-Feature Bundle Public Summary v0](../../../schemas/case-feature-bundle-public-summary-v0.md)

### Candidate-Option Scoring Rubric

Create a rubric that separates standard-care review, trial review,
expanded-access review, research-only hypotheses, and no-go records. Scores
must describe review readiness, uncertainty, and overclaiming risk only.

Current public deliverable:

- [Candidate-Option Scoring Rubric v0](../candidate-option-scoring-rubric-v0.md)

### Publication Gate Checklist

Add a checklist for any case-derived public learning. It should fail closed
when privacy, provenance, subtype scope, review status, or clinical-use
boundary is incomplete.

Current public deliverable:

- [Publication-Gate Checklist v0](../publication-gate-checklist-v0.md)

### Multidisciplinary Review Packet

Create a reusable multiple myeloma review packet template that a private lab
could fill without downstreaming case-specific facts to the public repo.

Current public deliverable:

- [Multidisciplinary Review Packet Template v0](../reviews/multidisciplinary-review-packet-template-v0.md)

## Structured Data

- JSON: [`multiple-myeloma-roadmap-public-task-queue-v0.json`](multiple-myeloma-roadmap-public-task-queue-v0.json)
- Metadata: [`multiple-myeloma-roadmap-public-task-queue-v0.metadata.json`](multiple-myeloma-roadmap-public-task-queue-v0.metadata.json)

## Review Boundary

This queue organizes public contribution work. It does not determine medical
care, evaluate any person's options, recommend a trial, recommend
expanded-access pursuit, or claim that a cure has been found.
