# Review-Packet Builder Packet-Skeleton Spec v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-review-packet-builder-packet-skeleton-spec-v0`
- source task: `multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: packet-skeleton specification only, no packet output
- last reviewed: `2026-04-15`

## Purpose

This specification defines an empty review-packet skeleton that can preserve
route-table references, missing-input records, refusal records, review status,
limitations, and output boundaries without filling any packet section.

It is not packet assembly. It does not generate review packets, fill review
sections, rewrite claims, summarize evidence, rank evidence, match patients,
select trials, recommend therapies, authorize publication, or ingest private
case data.

## Scope

The skeleton may name public review-packet section slots and the copied route
records that would be needed to review those slots later.

The skeleton must keep all section content empty. Missing inputs remain
missing, refusal records remain refusals, and review statuses remain copied
status labels only.

## Source Inputs

| Input | Status | Skeleton Use |
| --- | --- | --- |
| [Review-Packet Builder Packet-Assembly Gate v0](review-packet-builder-packet-assembly-gate-v0.md) | source-checked gate | Selects this spec-only slice and keeps packet assembly blocked. |
| [Review-Packet Route-Table Output Schema v0](../../../schemas/review-packet-route-table-output-schema-v0.md) | validated output shape | Defines copied route, missing-input, refusal, boundary, and do-not-infer records. |
| [Review-Packet Route-Table Output Fixture v0](../../../examples/review-packet-route-table-output-fixture-v0.json) | public placeholder fixture | Provides public placeholder route IDs and boundaries only. |
| [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../../tools/review_packet_manifest_route_table.py) | copied-reference tool | Produces route-table records without packet output or generated prose. |
| [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md) | validated input shape | Defines public manifest inputs and forbidden manifest fields. |
| [Review-Packet Builder Dry-Run Plan v0](review-packet-builder-dry-run-plan-v0.md) | source-checked plan | Defines copy, reference, omit, and refuse behavior. |
| [Multidisciplinary Review Packet Template v0](multidisciplinary-review-packet-template-v0.md) | expert-review-needed template | Provides public section labels that must not be filled in public. |
| [Multiple Myeloma Roadmap Public Task Queue v0](../public-tasks/multiple-myeloma-roadmap-public-task-queue-v0.md) | public task queue | Records this task and the current no-clinical-use boundary. |

## Empty Slot Contract

A packet skeleton may include only:

- skeleton identity fields
- copied route-table identity fields
- target packet artifact ID, path, review status, and limitations
- public section labels copied from a review packet template
- route IDs and manifest-section names that point back to route-table output
- missing-input records copied from route-table output
- refusal records copied from route-table output
- copied clinical-use and output-boundary statements
- do-not-infer statements

A packet skeleton must not include:

- filled section prose
- generated biomedical summaries
- generated or rewritten claims
- case facts, patient identifiers, raw records, free-text notes, images, or
  dates tied to a person
- reviewer identities or private review comments
- treatment, trial, eligibility, expanded-access, monitoring, or publication
  guidance
- evidence-strength ranking, clinical priority, urgency, actionability,
  patient relevance, option ranking, or trial matching
- cure, vaccine, or established-treatment claims

## Skeleton Sections

| Skeleton Slot | Allowed Contents | Required Empty State |
| --- | --- | --- |
| `skeleton_identity` | `skeleton_spec_id`, date, disease program, claim level, clinical-use boundary, source route-table ID. | No patient-specific dates or private identifiers. |
| `target_packet_reference` | Target packet artifact ID, path, copied review status, copied limitations, and packet boundary. | Do not fill target packet sections. |
| `route_table_reference` | Route-table ID, input manifest ID, route-table status, route IDs, and output-boundary strings. | Do not transform route records into packet content. |
| `artifact_reference_slots` | Artifact IDs, paths, metadata paths, claim levels, review statuses, limitations, and required section labels copied from routes. | Do not summarize or rewrite artifact content. |
| `review_section_slots` | Review item ID, focus label, required role labels, source route IDs, and empty content state. | Do not add reviewer conclusions or generated claims. |
| `missing_input_slots` | Missing-input IDs, kinds, reasons, blocking states, and next public task IDs copied from route-table output. | Do not fill missing inputs by inference. |
| `refusal_slots` | Refusal kind, location, field, reason, and value copied from route-table output. | Do not sanitize and continue after unsafe inputs. |
| `boundary_slots` | Clinical-use boundary, output boundary, limitations, and do-not-infer statements. | Do not weaken or omit no-use boundaries. |

## Template Section Mapping

| Review Template Section | Skeleton Mapping | Boundary |
| --- | --- | --- |
| Purpose and public boundary | Copy section label and route-table boundary references. | Do not create explanatory medical prose. |
| Target public artifacts | Link to artifact reference slots by route ID. | Inclusion is not evidence strength, clinical importance, or publication readiness. |
| Review sections | Copy review item IDs, focus labels, and required role labels. | Roles are needed review functions, not named reviewers or completed review. |
| Required review fields | Preserve empty fields for source IDs, claim IDs, gap IDs, measurement IDs, review status, uncertainty, limitations, and safety boundary. | Empty fields stay empty until a reviewed public artifact fills them. |
| Completion gate | Copy the gate label and source routes only. | Do not infer expert review, reviewer agreement, or publication approval. |
| What this template does not do | Copy do-not-infer and clinical-use boundary references. | Boundaries must remain visible in any future output. |

## Missing Inputs And Refusals

The skeleton must make missingness and refusal states visible without repairing
them.

When a route-table record reports a missing input, the skeleton may copy:

- missing-input ID
- missing kind
- reason missing
- blocking state
- next public task IDs

It must not synthesize substitute source IDs, claim text, review conclusions,
evidence summaries, or packet sections.

When a route-table record reports a refusal, the skeleton may copy:

- refusal kind
- location
- field
- reason
- value when already present in the route-table refusal record

It must not clean the unsafe field, continue the packet workflow, or downgrade
the refusal to a warning.

## Required Boundaries

Every future skeleton record or Markdown skeleton derived from this spec must
state:

- `research-use-only`
- `not-medical-advice`
- `not-diagnostic-guidance`
- `not-treatment-recommendation`
- `not-trial-recommendation`
- `not-expanded-access-guidance`
- `not-publication-authorization`
- `not-expert-review`
- `no-generated-claims`
- `no-real-case-data`
- `no-packet-assembly`
- `no-cure-claim`

## Current Handoff

This spec completes the selected no-code skeleton slice.

It does not authorize packet assembly, packet-output generation, skeleton
schema work, or a builder implementation by itself. The next project-owned
action should be a recombination review of the review-packet-builder lane to
decide whether any remaining work is a blocked status, a general validation
lemma, or a newly justified bounded downstream task.

## Limitations

- This is a packet-skeleton specification, not a packet assembler.
- It is source-checked planning, not expert review.
- It does not generate review packets or biomedical claims.
- It does not fill review sections.
- It does not prove source coverage is complete.
- It does not make any artifact expert-reviewed.
- It does not make any claim stronger.
- It does not rank evidence, targets, therapies, trials, sources, mechanisms,
  artifacts, tasks, gaps, claims, or questions.
- It does not authorize publication.
- It does not validate real case data, private records, patient-specific
  outputs, reviewer identities, or publication decisions.
- It does not provide medical advice, diagnostic guidance, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
- It does not establish that packet assembly is safe to build.
