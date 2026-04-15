# Multiple Myeloma Tooling Readiness Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-tooling-readiness-gate-v0`
- source task: `multiple-myeloma-tooling-readiness-gate-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This gate checks whether the public multiple myeloma lane is ready for a first
small tooling slice after the v0 schema set.

It is an aggregate readiness artifact only. It does not build a generator,
dashboard, explorer, evidence graph, extraction helper, review-packet builder,
trial finder, patient matcher, recommendation system, or generated-claim
pipeline.

## Boundary

- Public artifacts only.
- No real case data.
- No patient-specific interpretation.
- No generated biomedical claims.
- No clinical prioritization.
- No treatment recommendation.
- No trial recommendation.
- No eligibility or availability guidance.
- No expanded-access guidance.
- No target, therapy, trial, mechanism, source, or question ranking.
- No claim that multiple myeloma has been cured.

## Validated Input Shapes

| Shape | Current Status | What It Can Support | What It Cannot Support |
| --- | --- | --- | --- |
| `disease-map-schema-v0` | ready | Map-level navigation, source IDs, claims, hypotheses, open questions, and task links. | It cannot prove map completeness, truth, expert review, or clinical actionability. |
| `target-record-schema-v0` | ready | Public target context, nomenclature, source links, uncertainty, limitations, and no-clinical-use boundary fields. | It cannot imply targetability, expression in any person, efficacy, safety, eligibility, or therapy selection. |
| `therapy-record-schema-v0` | ready | Public therapy-class context, target links, source links, uncertainty, limitations, and no-recommendation boundaries. | It cannot become a treatment menu, dosing guide, sequencing guide, or candidate-option ranking. |
| `trial-landscape-record-schema-v0` | ready | Registry-landscape provenance, query context, accessed dates, freshness notes, uncertainty, and no-eligibility boundaries. | It cannot imply trial eligibility, availability, enrollment fit, sponsor access, efficacy, safety, or appropriateness. |
| `open-question-record-schema-v0` | ready | Public research questions linked to targets, therapies, trial landscapes, claims, gaps, mechanisms, and tasks. | It cannot encode clinical urgency, evidence-strength ranking, patient relevance, or actionability. |
| `public-task-queue.schema.json` | ready | Contribution-ready task queues with source, gap, claim, mechanism, measurement, and safety anchors. | It cannot turn task priority into biological importance, evidence strength, or clinical priority. |

## Readiness Axes

| Axis | Current State | Gate Result |
| --- | --- | --- |
| Schema readiness | Core map, target, therapy, trial-landscape, open-question, and task-queue shapes validate. | Ready for a spec-only first tooling slice. |
| Source coverage | Reusable source IDs exist, and BCMA/post-CAR T v0 mechanism lanes have navigation coverage. | Partial; not ready for automated source extraction or generated evidence claims. |
| Review readiness | Review packet templates exist, but completed qualified expert review is not present. | Partial; tooling must keep review status visible and avoid stronger claims. |
| Safety readiness | Public safety rules, no-clinical-use boundaries, and fail-closed schema constraints exist. | Ready only for tooling specs that preserve references and boundaries without inference. |
| Tooling readiness | No tooling gate had selected a first implementation slice before this artifact. | Ready for a manifest specification, not builder code. |

## Candidate Tooling Gate

| Candidate | Required Inputs | Decision | Reason |
| --- | --- | --- | --- |
| Queryable evidence graph | Disease map, target records, therapy records, open-question records, extraction records, source registry. | Block implementation. | Edge semantics and graph constraints are not defined; graph connectivity could be mistaken for evidence strength. |
| Trial landscape explorer | Trial-landscape records, query protocol, source registry, public task queues. | Block implementation. | Explorer behavior needs stronger no-eligibility, freshness, and no-availability display rules before code. |
| Target prioritization dashboard | Target records, therapy records, claim sets, gap registers, source registry. | Block implementation. | Prioritization views could be mistaken for clinical target ranking or patient option ranking. |
| Extraction helper | Source registry, extraction guide, mechanism map, target and therapy schemas, open-question schema. | Block implementation. | Source-specific extraction-helper schemas and generated-claim controls are not defined. |
| Review-packet builder | Public artifact catalog, task queues, review packet templates, source registry, validated record schemas. | Select spec-only next slice. | A manifest specification can define public inputs for a future builder without generating claims, ranking evidence, or assembling patient-specific content. |

## Selected First Slice

The smallest safe next slice is a **review-packet builder input manifest
specification**, not a builder.

The next task should define a manifest that lists public artifact IDs, source
IDs, schema IDs, task IDs, review-status fields, required limitations, and
validation expectations for a future review-packet builder.

Step 22 status: [Review-Packet Builder Input Manifest Spec v0](reviews/review-packet-builder-manifest-spec-v0.md)
now defines those manifest fields and fail-closed validation expectations.

Step 23 status: [Review-Packet Builder Manifest Schema v0](../../schemas/review-packet-builder-manifest-schema-v0.md)
now defines a validated manifest shape, placeholder template, and validator
coverage for public review-packet-builder input manifests.

Step 24 status: [Review-Packet Builder Dry-Run Plan v0](reviews/review-packet-builder-dry-run-plan-v0.md)
now defines no-code copy, reference, omit, and refuse behavior plus a
no-generated-claims policy.

Step 25 status: [Review-Packet Builder Implementation Gate v0](reviews/review-packet-builder-implementation-gate-v0.md)
conditionally selects one smallest safe code slice: a deterministic
copied-reference route-table dry-run script. Packet assembly, generated claims,
rankings, recommendations, trial matching, patient-specific outputs, and
publication behavior remain blocked.

Step 26 status: [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../tools/review_packet_manifest_route_table.py)
now implements that copied-reference route-table dry run with placeholder and
refusal fixtures. It still does not assemble packets or generate biomedical
prose. The next ready task is a route-table output schema and validator
contract before any downstream workflow relies on route-table records.

Step 27 status: [Review-Packet Route-Table Output Schema v0](../../schemas/review-packet-route-table-output-schema-v0.md)
now validates route-table output records and a public placeholder output
fixture. Packet assembly and generated claims remain blocked. The next ready
task is a no-code packet-assembly gate.

Step 28 status: [Review-Packet Builder Packet-Assembly Gate v0](reviews/review-packet-builder-packet-assembly-gate-v0.md)
keeps packet assembly blocked and selects a no-code packet-skeleton
specification as the next bounded public task.

Step 29 status: [Review-Packet Builder Packet-Skeleton Spec v0](reviews/review-packet-builder-packet-skeleton-spec-v0.md)
defines empty section slots and copied route-table references only. It does
not select schema, validator, packet-output, or builder implementation work by
itself; the next action is aggregate recombination.

Step 30 status: [Review-Packet Builder Recombination Handoff v0](reviews/review-packet-builder-recombination-handoff-v0.md)
closes the current review-builder lane with no ready builder task selected.
The next action is a definition-of-complete audit across the public loop.

The manifest specification must not:

- generate or rewrite biomedical claims
- rank claims, targets, therapies, trials, questions, sources, or tasks
- match any person to a treatment, trial, or expanded-access path
- infer evidence strength from graph links, task priority, schema validity, or
  review packet presence
- include real case data, identifiers, free-text notes, dates tied to a person,
  images, or private records
- produce public explainer text without a later review gate

## Minimum Acceptance For The Next Slice

The next manifest specification should:

- name the public review packet type it supports
- reference only public artifact IDs, paths, schema IDs, source IDs, gap IDs,
  claim IDs, mechanism IDs, measurement IDs, task IDs, and validation outputs
- preserve source-backed provenance, subtype scope, uncertainty, limitations,
  and review status
- keep missing inputs explicit instead of filling them
- state that builder code is still out of scope until the manifest shape is
  validated
- state that manifest validation is not expert review, evidence strength,
  clinical importance, patient relevance, actionability, or publication
  authorization

## Deferred Tooling Conditions

Before any implementation tool starts, a future gate should confirm:

- the tool has a validated input manifest or record shape
- generated outputs, if any, are explicitly prohibited or separately reviewed
- every output carries source IDs, uncertainty, limitations, review status, and
  no-clinical-use boundaries
- the tool cannot rank or recommend targets, therapies, trials, mechanisms, or
  patient options
- the tool cannot accept real case data or private records
- the tool has a validation path that fails closed when required source,
  limitation, or review fields are missing

## Current Decision

Tooling implementation remains blocked.

The next ready public task should define:

`multiple-myeloma-review-packet-builder-dry-run-plan-task-v0`

That task should create a no-code dry-run plan and no-generated-claims policy
for a future review-packet builder. It should not build review-packet-builder
code, generate packets, generate or rewrite biomedical claims, rank evidence,
match any person to a treatment or trial, authorize publication, or use real
case data.

Step 24 selected the next aggregate gate:

`multiple-myeloma-review-packet-builder-implementation-gate-task-v0`

That task should decide whether builder implementation remains blocked or a
smallest safe code slice can be selected. It should not build code.

Step 25 selected the first bounded code slice:

`multiple-myeloma-review-packet-builder-route-table-script-task-v0`

That task may build only a deterministic local route-table dry-run script for
the public placeholder manifest. It must not assemble packets or generate
biomedical prose.

Step 26 selected the next output-contract slice:

`multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0`

That task should define and validate route-table output records only. It must
not build packet assembly, generated claims, ranking, trial matching,
recommendation behavior, patient-specific tooling, or publication workflow.

Step 27 selected the next aggregate gate:

`multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0`

That task should decide whether packet assembly remains blocked or whether one
smallest safe downstream slice exists. It must not build packet assembly,
generated packet output, generated biomedical claims, ranking, trial matching,
recommendation behavior, patient-specific tooling, or publication workflow.

Step 28 selected the next no-code skeleton slice:

`multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0`

That task should define empty review-packet section slots and preserve
route-table references, missing inputs, refusals, review status, limitations,
and boundaries. It must not fill packet sections, create review-packet output,
generate claims, rank evidence, match patients, recommend therapies or trials,
authorize publication, or use real case data.

Step 29 completes that skeleton slice. The next action should be an aggregate
review-packet-builder recombination handoff before any new downstream task is
selected.

Step 30 completes that recombination handoff. The next action should audit the
public roadmap against the loop definition of complete before selecting any
new public task, blocked status, validation gap, or human-gated handoff.

## Limitations

- This gate is source-checked planning, not expert review.
- It does not evaluate any target, therapy, trial, question, source, or task for
  clinical value.
- It does not prove that the current schemas are complete.
- It does not prove that the open research map is comprehensive.
- It does not authorize generated claims, public explainers, dashboards, or
  automated extraction.
- It does not provide medical advice, diagnostic guidance, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
