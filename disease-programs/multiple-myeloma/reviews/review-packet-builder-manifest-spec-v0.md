# Review-Packet Builder Input Manifest Spec v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-review-packet-builder-manifest-spec-v0`
- source task: `multiple-myeloma-review-packet-builder-manifest-spec-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: manifest specification only, no builder code
- last reviewed: `2026-04-15`

## Purpose

This specification defines the public input manifest a future review-packet
builder would need before it can assemble review packets from validated public
artifacts.

It is not a builder. It does not generate review packets, rewrite claims,
summarize evidence, rank records, match patients, select trials, recommend
therapies, authorize publication, or ingest private case data.

## Boundary

- Public artifacts only.
- No real case data.
- No patient identifiers.
- No dates tied to a person.
- No free-text notes, raw records, images, re-identification keys, or private
  lab exports.
- No generated biomedical claims.
- No evidence-strength ranking.
- No clinical priority, urgency, or patient-relevance fields.
- No treatment recommendation.
- No trial recommendation.
- No eligibility, availability, sponsor-access, or expanded-access guidance.
- No publication authorization.
- No cure claim.

## Supported Public Packet Types

| Packet Type | Current Public Anchor | Manifest Use | Do Not Infer |
| --- | --- | --- | --- |
| `multidisciplinary-review-packet-template` | `multiple-myeloma-multidisciplinary-review-packet-template-v0` | Route public artifact references into reviewer-role sections. | Do not fill public packets with real case facts or imply expert review is complete. |
| `claim-set-expert-review-packet` | `bcma-claim-set-expert-review-packet-v0` | Route claim, gap, measurement, mechanism, extraction, and task IDs into review items. | Do not infer claim strength or clinical actionability from inclusion. |

## Manifest Sections

| Section | Required Fields | Allowed Values | Boundary |
| --- | --- | --- | --- |
| Manifest identity | `manifest_id`, `title`, `disease_program`, `packet_type`, `created`, `last_reviewed`, `review_status`, `clinical_use_boundary` | Public identifiers and dates for the manifest itself. | No patient-specific dates or private review identities. |
| Target packet | `target_packet_artifact_id`, `target_packet_path`, `target_packet_status`, `target_packet_limitations` | Public review packet templates or source-checked packets only. | Packet presence is not expert review. |
| Artifact inputs | `artifact_id`, `path`, `metadata_path`, `artifact_class`, `claim_level`, `review_status`, `required_sections`, `limitations` | IDs and paths already present in public catalog or metadata. | Inclusion is not evidence strength, clinical importance, or publication approval. |
| Schema inputs | `schema_id`, `schema_path`, `template_path`, `validation_command`, `validation_scope` | Public schema and template references only. | Schema validity checks shape only. |
| Source inputs | `source_ids`, `source_registry_path`, `accessed`, `source_use` | Source IDs already present in `source-registry-v0`. | A source ID does not prove efficacy, safety, eligibility, availability, or patient fit. |
| Reference IDs | `claim_ids`, `gap_ids`, `mechanism_group_ids`, `measurement_term_ids`, `task_ids`, `query_record_ids`, `extraction_record_ids` | Public IDs that validators can resolve. | IDs are routing anchors, not rankings. |
| Missing inputs | `missing_input_id`, `missing_kind`, `reason_missing`, `blocking_state`, `next_public_task_id` | Explicit missingness and task routing. | Missing fields must not be filled by generation. |
| Review routing | `review_item_id`, `focus`, `required_roles`, `reviewer_action_needed`, `claim_language_action` | Reviewer roles and actions copied from public review templates. | Do not identify reviewers publicly unless separately approved. |
| Safety boundary | `what_not_to_infer`, `clinical_use_boundary`, `publication_gate_boundary` | Required no-use statements. | The manifest cannot authorize clinical or publication decisions. |

## Required Manifest Behaviors

A valid future manifest should:

- reference only public artifact IDs, paths, metadata paths, schemas, source
  IDs, claim IDs, gap IDs, mechanism IDs, measurement IDs, query-record IDs,
  extraction-record IDs, and task IDs
- preserve disease scope, subtype scope, source provenance, uncertainty,
  limitations, review status, and no-clinical-use boundary fields
- keep missing or incomplete inputs explicit
- route missing inputs to public tasks instead of generating substitutions
- keep source-checked, expert-review-needed, expert-reviewed, blocked, and
  deprecated states distinct
- fail closed when required source, limitation, review, or safety fields are
  missing

## Forbidden Manifest Fields

A manifest schema or validator should reject fields that imply:

- patient identity or case reconstruction
- diagnosis, prognosis, monitoring, treatment, trial, expanded-access, or
  publication decisions
- candidate options for a person
- trial eligibility, availability, enrollment fit, sponsor access, or site
  access
- standard-care, investigational, trial, target, therapy, mechanism, source, or
  question rankings
- evidence-strength scoring unless a later reviewed protocol explicitly
  defines non-clinical scoring boundaries
- generated claim text, generated public explainer text, generated medical
  summaries, or unreviewed rewritten claims
- cure, vaccine, or established-treatment claims

## Validation Expectations

The next validation contract should define a JSON schema and placeholder
manifest template before any builder code exists.

Minimum fail-closed checks:

- `manifest_id` is present and public.
- `packet_type` is one of the supported public packet types.
- every artifact input has a public path and metadata path
- every source ID resolves to `source-registry-v0`
- every linked claim, gap, mechanism, measurement, query-record, extraction,
  and task ID resolves through an existing validator collection where available
- every artifact input declares limitations and review status
- every missing input has a blocking state and next public task or blocker note
- every safety boundary includes no-patient-data, no-recommendation,
  no-trial-guidance, no-expanded-access-guidance, no-publication-authorization,
  and no-cure-claim language
- forbidden fields are rejected, not ignored

## Builder Code Gate

Builder code remains blocked until all of the following exist:

- a validated manifest schema
- a public placeholder manifest template
- validator coverage for manifest records
- a no-generated-claims policy for any assembled packet output
- a human-readable dry-run plan that names what a future builder may copy,
  reference, omit, or refuse
- an aggregate implementation gate that selects a smallest safe code slice or
  keeps builder implementation blocked
- a copied-reference route-table script with refusal fixtures before any packet
  assembly

Even after those exist, a builder must not create clinical guidance, rankings,
trial matching, expanded-access pathways, publication authorization, or
patient-specific outputs.

## Current Decision

The next ready public task should define:

`multiple-myeloma-review-packet-builder-route-table-script-task-v0`

That task should create only the copied-reference route-table dry-run script
selected by the implementation gate. It should not assemble review packets or
generate biomedical prose.

## Limitations

- This is a manifest specification, not a working builder.
- It is source-checked planning, not expert review.
- It does not validate any real manifest record yet.
- It does not make any source-checked artifact expert-reviewed.
- It does not make any claim stronger.
- It does not rank targets, therapies, trials, questions, mechanisms, sources,
  artifacts, tasks, or evidence.
- It does not authorize publication.
- It does not provide medical advice, diagnostic guidance, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
