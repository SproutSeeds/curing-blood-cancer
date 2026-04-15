# Multiple Myeloma Schema And Tooling Phase Inventory v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-schema-tooling-phase-inventory-v0`
- source task: `multiple-myeloma-schema-tooling-phase-inventory-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This inventory marks the phase boundary after the first public myeloma map,
disease-map schema, source registry expansion, and v0 mechanism extraction
coverage have landed.

It chooses the next validated shape before any evidence graph, trial explorer,
target prioritization dashboard, extraction helper, review-packet builder, or
generation script is created.

## Boundary

- This is a public planning and schema-readiness artifact.
- It does not add biomedical claims.
- It does not add extraction records.
- It does not rank targets, therapies, trials, mechanisms, datasets, or public
  tasks by clinical importance.
- It is not medical advice, diagnostic guidance, treatment guidance, trial
  guidance, expanded-access guidance, eligibility guidance, monitoring
  guidance, or a cure claim.

## Current Phase Facts

| Fact | Public Basis | What It Allows | What It Does Not Allow |
| --- | --- | --- | --- |
| The multiple myeloma open research map has a validated JSON companion. | `multiple-myeloma-open-research-map-v0-1`; `disease-map-schema-v0` | Reuse one stable disease-map contract. | It does not prove the map is complete, expert-reviewed, or clinically actionable. |
| Current post-CAR T mechanism buckets have v0 navigation coverage. | `post-car-t-relapse-mechanism-coverage-v0` | Pause ad hoc extraction siblings and inspect the next phase. | It does not rank mechanisms or establish frequency. |
| Public task queues validate against `public-task-queue.schema.json`. | `multiple-myeloma-roadmap-public-task-queue-v0`; validator output | Add bounded next tasks before implementation. | It does not mean task priority is evidence strength. |
| Source anchors now cover target, therapy, trial, regulatory, label, and dataset classes. | `source-registry-v0` | Define source-backed shape requirements. | A source ID does not prove actionability, efficacy, safety, eligibility, availability, or patient fit. |
| Standalone target, therapy, trial-landscape, and open-question record schemas are present. | `schemas/`; `disease-map-schema-v0`; `target-record-schema-v0`; `therapy-record-schema-v0`; `trial-landscape-record-schema-v0`; `open-question-record-schema-v0`; `multiple-myeloma-tooling-readiness-gate-v0` | Use the tooling readiness gate to select a spec-only first slice. | It does not authorize generators, explorers, dashboards, extraction helpers, or builder code. |

## Existing Validated Shapes

| Shape | Status | Reuse Before Tooling |
| --- | --- | --- |
| Artifact metadata and public catalog | ready | Use for discoverability and catalog checks. |
| Public task queue | ready | Use for contribution-ready task queues. |
| Disease map | ready | Use for map-level facts, derived claims, hypotheses, open questions, target records, therapy records, trial records, and task links. |
| Evidence claim and claim set | ready | Use for source-bounded claim organization. |
| Evidence gap register | ready | Use for public gap and task provenance. |
| Mechanism map, extraction, and coverage | ready | Use for source-backed mechanism lanes and coverage metrics. |
| Measurement glossary and audit | ready | Use for measurement terms and missing-context checks. |
| Case-to-cure synthetic pipeline | ready | Use only for synthetic public plumbing, never real case data. |
| Expert review packet | ready | Use for review readiness, not completed expert review. |
| Target record | ready | Use for public target context, source links, uncertainty, and non-clinical boundaries. |
| Therapy record | ready | Use for public therapy-class context, source links, uncertainty, and non-clinical boundaries. |
| Trial-landscape record | ready | Use for public registry landscape provenance, data freshness, query links, uncertainty, and no-eligibility boundaries. |
| Open-question record | ready | Use for public research questions, cross-links, uncertainty, and non-clinical boundaries. |

## Candidate Next Shapes

| Candidate | Status | Why | Boundary |
| --- | --- | --- | --- |
| Target-record schema | completed | Target records are already embedded in the disease-map schema, source anchors exist for gene and target naming, and target shape is needed before evidence graph or target-prioritization tooling. | Must not imply targetability, expression in any person, therapy selection, trial selection, efficacy, safety, or actionability. |
| Therapy-record schema | completed | Therapy classes need a target and source context first to avoid option-ranking language. | Must not become a treatment menu or candidate-option ranking. |
| Trial-landscape record schema | completed | Trial-query provenance exists, but a landscape schema needs no-eligibility and registry-freshness constraints. | Must not imply eligibility, availability, enrollment advice, sponsor access, efficacy, or safety. |
| Open-question record schema | completed | Target, therapy, and trial-landscape schemas now expose clearer cross-links for standalone question records. | Must not treat question priority as evidence strength or clinical importance. |
| Public-task record schema | existing queue shape sufficient for now | `public-task-queue.schema.json` already validates task queues. | Standalone task records can wait until task queues need cross-repo federation. |
| Source-specific extraction-helper schema | deferred | Helpers should wait for the next record shape they will populate. | Must not generate claims or fill missing evidence. |
| Evidence graph tooling | blocked after readiness gate | Graph nodes now have core contracts, but edge semantics and no-evidence-strength display rules are not defined. | Must not convert graph connectivity into evidence strength. |
| Trial explorer tooling | blocked after readiness gate | Registry data has shape, but explorer behavior needs stronger freshness, no-eligibility, and no-recommendation display rules before code. | Must not be a trial finder for any person. |
| Target prioritization dashboard | blocked after readiness gate | Target records have shape, but prioritization views need stronger no-ranking boundaries. | Must not rank patient options or clinical targets. |
| Review-packet builder manifest specification | completed | The spec defines public inputs, validation expectations, and missing-input handling before builder code. | Must not generate claims, rank evidence, assemble patient-specific content, or authorize publication. |
| Review-packet builder manifest schema | completed | The manifest schema now defines a public input contract, placeholder template, and validator coverage before builder code. | Must not become builder code or generated packet output. |
| Review-packet builder dry-run plan | completed | The dry-run plan defines copy, reference, omit, and refuse behavior plus a no-generated-claims policy before any builder code. | Must not generate packets, rewrite biomedical claims, rank evidence, authorize publication, or use real case data. |
| Review-packet builder implementation gate | completed | The gate conditionally selects a deterministic copied-reference route-table script and keeps packet assembly and generated claims blocked. | Must not become packet assembly, generated packet output, generated claims, patient matching, ranking, or recommendations. |
| Review-packet builder route-table script | completed | The local dry-run script copies public IDs/paths/boundaries and reports missing inputs/refusals. | Must not generate claims, generate packets, rank evidence, match patients, recommend options, or use private data. |
| Review-packet builder route-table output schema | completed | Route-table output now has a schema, placeholder fixture, and validator coverage. | Must not authorize packet assembly, generated claims, ranking, recommendations, patient matching, or publication workflows. |
| Review-packet builder packet-assembly gate | completed | The no-code gate keeps packet assembly blocked and selects a packet-skeleton specification only. | Must not build packet assembly, generated packet output, generated claims, ranking, recommendations, patient matching, or publication workflows. |
| Review-packet builder packet-skeleton spec | completed | The static skeleton spec defines empty packet section slots that preserve route-table references, missing inputs, refusals, review status, limitations, and boundaries. | Must not fill packet sections, generate claims, create review-packet output, rank evidence, recommend options, or use real case data. |
| Review-packet builder recombination handoff | completed | The aggregate handoff closes the current review-builder lane with no ready builder task selected. | Must not invent packet assembly, packet-output, schema, validator, or implementation work without a completion audit or future gate. |

## Selected Aggregate Work Object

[Tooling Readiness Gate v0](tooling-readiness-gate-v0.md) now completes the
schema-backed aggregate gate.

Gate result:

- implementation tooling remains blocked
- evidence graph, trial explorer, target prioritization dashboard, extraction
  helper, review-packet builder code, generators, patient matchers, ranking
  tools, and recommendation systems remain out of scope
- the selected next slice is a review-packet builder input manifest
  specification
- the next slice is spec-only and must not generate biomedical claims, rank
  evidence, assemble patient-specific content, or authorize publication

Minimum readiness-gate requirements:

- name the validated input schemas it depends on
- separate schema readiness, source coverage, review readiness, and tooling
  readiness
- preserve no-patient-data, no-recommendation, no-trial-guidance, no-ranking,
  and no-generated-claim boundaries
- either select one smallest safe public tooling slice or keep tooling blocked

## Next Handoff

No implementation task is selected by the packet-skeleton spec or the
recombination handoff.

The next action should be a definition-of-complete audit across the autonomous
loop. That audit should decide whether any remaining work is a blocked status,
a missing public artifact, a validation gap, a navigation repair, a private-lab
handoff, or loop completion. It should not add packet assembly, generated
claims, ranking, trial matching, recommendation behavior, patient-specific
tooling, or publication workflow.

Step 31 status: [Definition-Of-Complete Audit v0](definition-of-complete-audit-v0.md)
identifies a single remaining public-loop gap: a case-specific private-lab
blocker register. The next ready task is
`multiple-myeloma-case-specific-private-lab-blocker-register-task-v0`. This is
not a review-builder implementation task.

Step 32 status: [Case-Specific Private-Lab Blocker Register v0](case-specific-private-lab-blocker-register-v0.md)
maps the remaining case-specific stage range to private-lab tasks or
human-gated blockers. The next action should be an aggregate completion
handoff, not case-processing tooling.

Step 33 status: [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
marks the current multiple myeloma public v0 loop endpoint. No ready public
task is selected by the handoff; future work should start only through a new
named phase, human review, or aggregate gate.

## Step 17 Status Update

[Target Record Schema v0](../../schemas/target-record-schema-v0.md) now defines
the first standalone target-context shape with a placeholder template and
validator coverage.

The next ready validated-shape task is
`multiple-myeloma-therapy-record-schema-task-v0`. It should define a
therapy-record schema only. It should not create treatment recommendations,
candidate options, therapy rankings, dosing guidance, eligibility guidance,
expanded-access guidance, real case data, or tooling.

## Step 18 Status Update

[Therapy Record Schema v0](../../schemas/therapy-record-schema-v0.md) now
defines the first standalone therapy-context shape with a placeholder template
and validator coverage.

The next ready validated-shape task is
`multiple-myeloma-trial-landscape-record-schema-task-v0`. It should define a
trial-landscape record schema only. It should not create eligibility guidance,
enrollment advice, trial recommendations, availability claims for any person,
sponsor access instructions, expanded-access guidance, real case data, or
tooling.

## Step 19 Status Update

[Trial-Landscape Record Schema v0](../../schemas/trial-landscape-record-schema-v0.md)
now defines the first standalone registry-landscape shape with a placeholder
template and validator coverage.

The next ready validated-shape task is
`multiple-myeloma-open-question-record-schema-task-v0`. It should define an
open-question record schema only. It should not create clinical priorities,
evidence-strength rankings, urgency labels, patient-specific relevance,
treatment recommendations, trial recommendations, expanded-access guidance,
real case data, or tooling.

## Step 20 Status Update

[Open-Question Record Schema v0](../../schemas/open-question-record-schema-v0.md)
now defines the first standalone public research-question shape with a
placeholder template and validator coverage.

The next ready aggregate public task is
`multiple-myeloma-tooling-readiness-gate-task-v0`. It should create a
schema-backed tooling readiness gate only. It should not build an evidence
graph, trial explorer, target prioritization dashboard, extraction helper,
review-packet builder, generator, ranking tool, patient matcher, clinical
recommendation system, or generated-claim pipeline.

## Step 21 Status Update

[Tooling Readiness Gate v0](tooling-readiness-gate-v0.md) now maps candidate
tooling ideas against validated schemas and selects a review-packet builder
input manifest specification as the smallest safe next slice.

The next ready public task is
`multiple-myeloma-review-packet-builder-manifest-spec-task-v0`. It should
define a manifest specification only. It should not build review-packet-builder
code, generate or rewrite biomedical claims, rank evidence, match any person to
a trial or therapy, authorize publication, or use real case data.

## Step 22 Status Update

[Review-Packet Builder Input Manifest Spec v0](reviews/review-packet-builder-manifest-spec-v0.md)
now defines public manifest fields, forbidden fields, and fail-closed
validation expectations for future review-packet-builder inputs.

The next ready public task is
`multiple-myeloma-review-packet-builder-manifest-schema-task-v0`. It should
define a schema, placeholder template, and validator coverage only. It should
not build review-packet-builder code, generate review packets, generate or
rewrite biomedical claims, rank evidence, match any person to a trial or
therapy, authorize publication, or use real case data.

## Step 23 Status Update

[Review-Packet Builder Manifest Schema v0](../../schemas/review-packet-builder-manifest-schema-v0.md)
now defines the validated public manifest shape and placeholder template for
future review-packet-builder inputs.

The next ready public task is
`multiple-myeloma-review-packet-builder-dry-run-plan-task-v0`. It should
define a no-code dry-run plan and no-generated-claims policy only. It should
not build review-packet-builder code, generate review packets, generate or
rewrite biomedical claims, rank evidence, match any person to a trial or
therapy, authorize publication, or use real case data.

## Step 24 Status Update

[Review-Packet Builder Dry-Run Plan v0](reviews/review-packet-builder-dry-run-plan-v0.md)
now defines copy, reference, omit, and refuse behavior for a future
review-packet-builder dry run without code or generated claims.

The next ready public task is
`multiple-myeloma-review-packet-builder-implementation-gate-task-v0`. It
should define an aggregate implementation gate only. It should not build
review-packet-builder code, generate review packets, generate or rewrite
biomedical claims, rank evidence, match any person to a trial or therapy,
authorize publication, or use real case data.

## Step 25 Status Update

[Review-Packet Builder Implementation Gate v0](reviews/review-packet-builder-implementation-gate-v0.md)
now conditionally selects a deterministic copied-reference route-table dry-run
script as the first bounded code slice.

The next ready public task is
`multiple-myeloma-review-packet-builder-route-table-script-task-v0`. It should
build a local route-table dry-run script only. It should not assemble review
packets, generate or rewrite biomedical claims, rank evidence, match any person
to a trial or therapy, authorize publication, or use real case data.

## Step 26 Status Update

[Review-Packet Manifest Route-Table Dry-Run Tool v0](../../tools/review_packet_manifest_route_table.py)
now implements the deterministic copied-reference route-table script with a
placeholder fixture, a forbidden-field refusal fixture, and self-test coverage
for forbidden fields, missing paths, unknown source IDs, and missing boundaries.

The next ready public task is
`multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0`. It
should define and validate route-table output records only. It should not
assemble review packets, generate or rewrite biomedical claims, rank evidence,
match any person to a trial or therapy, authorize publication, or use real case
data.

## Step 27 Status Update

[Review-Packet Route-Table Output Schema v0](../../schemas/review-packet-route-table-output-schema-v0.md)
now defines and validates route-table output records, with the public
placeholder fixture at
`examples/review-packet-route-table-output-fixture-v0.json`.

The next ready public task is
`multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0`. It
should define a no-code aggregate gate before any review-packet output. It
should not assemble review packets, generate or rewrite biomedical claims, rank
evidence, match any person to a trial or therapy, authorize publication, or use
real case data.

## Step 28 Status Update

[Review-Packet Builder Packet-Assembly Gate v0](reviews/review-packet-builder-packet-assembly-gate-v0.md)
now records the aggregate decision after manifest, route-table, output-schema,
fixture, and dry-run prerequisites: packet assembly remains blocked.

The next ready public task is
`multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0`. It
should define a no-code packet-skeleton specification with empty section slots
only. It should preserve route-table references, missing inputs, refusals,
review status, limitations, and boundaries without assembling packets,
generating or rewriting biomedical claims, ranking evidence, matching any
person to a trial or therapy, authorizing publication, or using real case data.

## Step 29 Status Update

[Review-Packet Builder Packet-Skeleton Spec v0](reviews/review-packet-builder-packet-skeleton-spec-v0.md)
now defines the selected no-code skeleton slice. It names empty packet section
slots, route-table references, missing-input slots, refusal slots, review
status fields, limitations, and boundary slots without creating packet output.

The next action is an aggregate review-packet-builder recombination handoff.
No schema, validator, packet-output, or builder implementation task is selected
by the skeleton spec itself.

## Step 30 Status Update

[Review-Packet Builder Recombination Handoff v0](reviews/review-packet-builder-recombination-handoff-v0.md)
now records the aggregate endpoint for the current review-builder lane. It
keeps packet assembly, packet output, generated claims, ranking, patient
matching, trial matching, recommendation behavior, publication workflow, and
real case data blocked.

The next action is a definition-of-complete audit against the autonomous loop
criteria. No ready public task is selected by the review-builder lane.

## Limitations

- This inventory is source-checked planning, not expert review.
- It is scoped to the current public myeloma lane and BCMA/post-CAR T public
  artifacts.
- It does not make the open research map comprehensive across all myeloma
  states.
- It does not resolve dataset, regulatory, public-task federation, or
  extraction-helper schemas.
- It does not authorize generator or dashboard work.
- It does not provide medical advice or clinical prioritization.
