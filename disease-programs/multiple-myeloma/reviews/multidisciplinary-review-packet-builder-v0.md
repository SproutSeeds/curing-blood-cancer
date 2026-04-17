# Multidisciplinary Review Packet Builder v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-multidisciplinary-review-packet-builder-v0`
- ORP item: `multidisciplinary-review-packet-builder-v0`
- builder status: public route-rule skeleton complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: route-rule skeleton only; no packet assembly, no
  generated prose, no builder backend, no real case data
- last reviewed: `2026-04-16`

## Purpose

This artifact defines the public-safe front door for a future
multidisciplinary review packet builder. It binds the candidate hypothesis
question scaffold to the existing review-packet manifest, route-table, and
empty packet-skeleton work.

It exists so a later private or synthetic-only workflow can route question
IDs, artifact IDs, source IDs, review-lens fields, missing-input blockers,
safety boundaries, and no-generated-claims behavior without turning those
routes into packet contents.

It does not assemble review packets, fill packet sections, write biomedical
prose, summarize evidence, select reviewers, disclose reviewer identities,
rank candidates, match trials, recommend therapies, authorize publication, or
process a real case.

## Current Builder Decision

Current decision: `public-route-rule-skeleton-only`.

Allowed public behavior:

- copy exact public identifiers, paths, section labels, review-status labels,
  limitation text, and boundary text
- reference public source IDs, artifact IDs, question IDs, query IDs, task IDs,
  and schema IDs
- omit fields that do not have public, source-scoped, validated inputs
- refuse any route that contains real case facts, private records, generated
  biomedical prose, patient-specific interpretation, ranking, recommendation,
  trial matching, eligibility, availability, expanded-access guidance,
  monitoring guidance, publication authorization, or clinical decisions

Blocked behavior:

- packet assembly
- generated packet output
- generated biomedical prose
- generated public explainers or medical summaries
- real case fact ingestion
- private record ingestion
- patient-specific outputs
- recommendation, ranking, prioritization, comparison, or candidate selection
- trial matching, eligibility, availability, site-status, sponsor-access, or
  enrollment inference
- expanded-access, access, monitoring, urgency, referral, treatment, or safety
  guidance
- publication authorization or expert-review substitution

The next public-safe step after this builder skeleton is
`expert-validation-loop-v0`, limited to public-safe expert validation issue and
disposition plumbing. It must not publish private correspondence or treat
silence, outreach mapping, or issue status as expert validation.

## Source Inputs

| Input | Builder Use | Boundary |
| --- | --- | --- |
| [Candidate Hypothesis Review Question Set v0](candidate-hypothesis-review-question-set-v0.md) | Provides question IDs, review lenses, evidence packet IDs, landscape gate IDs, blocked-use flags, and no patient-action output. | Questions are not candidate options, recommendations, rankings, or patient actions. |
| [Multidisciplinary Review Packet Template v0](multidisciplinary-review-packet-template-v0.md) | Provides public section labels and required review-field families. | Sections must stay empty in public; no real case facts or reviewer conclusions. |
| [Review-Packet Builder Input Manifest Spec v0](review-packet-builder-manifest-spec-v0.md) | Provides manifest field groups and forbidden manifest fields. | Manifest shape is not packet assembly. |
| [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md) | Provides validated public manifest shape. | Schema validation checks shape only, not source completeness or clinical meaning. |
| [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../../tools/review_packet_manifest_route_table.py) | Provides copied-reference route-table behavior for public placeholder inputs. | Tool output is not a packet and not expert review. |
| [Review-Packet Route-Table Output Schema v0](../../../schemas/review-packet-route-table-output-schema-v0.md) | Provides route, missing-input, refusal, and boundary output fields. | Output records cannot become packet contents. |
| [Review-Packet Builder Packet-Skeleton Spec v0](review-packet-builder-packet-skeleton-spec-v0.md) | Provides empty slots for copied route references, missing inputs, refusals, and boundaries. | Empty slots remain empty; no generated sections. |
| [Evidence Retrieval Packet v0](../evidence-retrieval-packet-v0.md) | Provides public evidence packet IDs, source freshness, limitations, and no-advice boundaries. | Evidence packet IDs do not establish relevance, strength, or actionability. |
| [Trial Therapy Landscape Non-Advice Gate v0](../therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md) | Provides trial, therapy, product, target, jurisdiction, status, freshness, access-date, uncertainty, and limitation context. | Landscape context is not availability, eligibility, matching, ranking, sequencing, or access guidance. |
| [Publication-Gate Checklist v0](../publication-gate-checklist-v0.md) | Provides public release blockers and case-derived learning gates. | Builder routes cannot authorize publication. |
| [Source Registry v0](../../../sources/source-registry-v0.md) | Provides public source IDs and source context. | Source presence is not evidence completeness or clinical endorsement. |
| [Caregiver Intake Public Projection Validator v0](../case-intake/caregiver-intake-public-projection-validator-v0.md) | Provides no-PHI and no-advice projection refusal logic. | Real case content remains private-only. |
| [Private Intake Schema Contract v0](../case-intake/private-intake-schema-contract-v0.md) | Provides private/public partition boundaries. | Private field groups cannot be copied into public routes. |
| [Public Safety](../../../governance/PUBLIC_SAFETY.md) and [Private-To-Public Workflow](../../../docs/private-to-public-workflow.md) | Provide repository-wide release and sanitation boundaries. | Human gates remain required for any case-derived public learning. |

## Builder Route Envelope

Every public builder route should be representable with these fields before any
future manifest, route table, or packet skeleton reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `builder_profile_id` | `multidisciplinary_review_packet_builder_v0` or later public version. | Profile ID is for audit only; it is not a packet or review decision. |
| `route_id` | Stable public route ID or `route_pending`. | Must not include private case IDs, dates, sites, clinicians, or rare combinations. |
| `question_id` | Candidate question ID, `question_needed`, or `not_applicable`. | Question ID does not create a candidate option or recommendation. |
| `artifact_id` | Public catalog artifact ID or `artifact_needed`. | Artifact inclusion is not evidence strength, clinical priority, or publication readiness. |
| `metadata_path` | Public metadata path or `metadata_needed`. | Metadata must exist before copying artifact class, claim level, source count, or limitation count. |
| `source_ids` | Public source IDs, `source_id_needed`, or `not_applicable`. | Source IDs are provenance anchors only. |
| `review_lens` | Reviewer lens copied from the question set or `lens_needed`. | Lens is a role category, not a named reviewer, endorsement, or decision. |
| `target_packet_section` | Public section label from the multidisciplinary template or `section_needed`. | Section labels may be copied; section prose must remain empty. |
| `route_decision` | `copy`, `reference`, `omit`, or `refuse`. | The builder cannot invent substitutes or weaken refusals. |
| `missing_input_id` | Missing-input ID or `not_applicable`. | Missing inputs stay visible and block packet filling. |
| `refusal_id` | Refusal ID or `not_applicable`. | Refusals stop the route; they are not warnings. |
| `boundary_tags` | Required tags such as `research-use-only`, `not-medical-advice`, `no-generated-claims`, `no-real-case-data`, `no-ranking`, and `no-publication-authorization`. | Boundary tags must be copied into any future route-table or skeleton output. |
| `public_output_allowed` | `route_table_only`, `empty_skeleton_only`, `blocker_note_only`, or `false`. | No filled packet content is allowed. |

## Route Rules

| Decision | Builder May Do | Builder Must Not Do |
| --- | --- | --- |
| `copy` | Copy exact public IDs, paths, metadata paths, section labels, review statuses, limitation text, and boundary text. | Do not summarize, rewrite, strengthen, soften, rank, or interpret copied material. |
| `reference` | Link public question IDs, artifact IDs, source IDs, query IDs, schema IDs, route IDs, and task IDs for reviewer navigation. | Do not infer completeness, evidence strength, patient relevance, actionability, availability, eligibility, or publication readiness. |
| `omit` | Leave a route or skeleton field empty and name the missing public input or blocker. | Do not fill missing inputs with generated prose, adjacent sources, assumptions, or private facts. |
| `refuse` | Stop a route when any unsafe field or use appears. Preserve refusal kind, location, field, and reason. | Do not sanitize and continue; do not downgrade refusals to warnings. |

## Review Lens Routing

| Review Lens | Allowed Route Target | Required Block |
| --- | --- | --- |
| `clinician_review` | Empty clinical-context section label and copied public source/question IDs. | No diagnosis, prognosis, treatment recommendation, monitoring guidance, urgency guidance, or patient-specific interpretation. |
| `trial_operations_review` | Empty trial-context section label and copied registry/query/landscape IDs. | No trial matching, eligibility, availability, site status, enrollment fit, sponsor access, or trial recommendation. |
| `molecular_review` | Empty molecular-context section label and copied assay/source-validity IDs. | No target actionability, testing advice, therapy fit, trial fit, or patient relevance. |
| `pathology_or_flow_review` | Empty pathology/flow-context section label and copied source-validity IDs. | No report interpretation, diagnostic guidance, or case-specific conclusion. |
| `regulatory_or_access_review` | Empty regulatory/access-context section label and blocker IDs. | No expanded-access instructions, feasibility claims, access route, timing guidance, or sponsor/site decisions. |
| `safety_ethics_review` | Empty safety/ethics section label and copied blocker IDs. | No safety-management advice, contraindication claims, urgency guidance, or clinical decision. |
| `patient_communication_review` | Empty communication-boundary section label and copied no-use language. | No patient-facing advice, reassurance, urgency language, or action instruction. |
| `source_appraisal_review` | Empty source-appraisal section label and copied source/gap IDs. | No evidence ranking, source ranking, claim upgrading, or proof of completeness. |
| `publication_gate_review` | Empty publication-gate section label and copied gate IDs. | No publication authorization or case-derived public learning. |

## Fail-Closed Builder Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `mrb_00_no_real_case_content` | Routes must not contain real case facts, identifiers, records, reports, images, free-text notes, exact dates tied to a person, private paths, or private prompts. | Refuse and mark `private-lab-needed`. |
| `mrb_01_no_generated_prose` | Routes must not create biomedical prose, claim rewrites, summaries, explanations, or filled packet sections. | Refuse and keep output to route-table or empty skeleton only. |
| `mrb_02_question_ids_only` | Candidate-question inputs may be copied or referenced only as question IDs and public boundary fields. | Refuse candidate-option, recommendation, ranking, or patient-action wording. |
| `mrb_03_source_and_metadata_required` | Artifact and source routes require public metadata paths, source IDs, or explicit missing-input states. | Omit and report missing input; do not infer. |
| `mrb_04_lens_required` | Review routes require a public review lens or `lens_needed`. | Omit route target until lens is supplied. |
| `mrb_05_no_matching` | Builder routes cannot match a person to trials, therapies, products, targets, mechanisms, sources, or reviewers. | Refuse matching fields and route to blocker. |
| `mrb_06_no_availability_or_eligibility` | Trial/product/access routes cannot infer availability, eligibility, site status, sponsor access, enrollment fit, or feasibility. | Refuse or preserve as unverified landscape context only. |
| `mrb_07_no_publication_authorization` | Route inclusion cannot authorize publication or public release of case-derived learning. | Route to publication gate or refuse. |
| `mrb_08_successor_match` | Gaps must route to the correct next public-safe step. | Route expert disposition gaps to `expert-validation-loop-v0`; route public learning to publication gate; route private case facts to private-lab-needed. |

## Synthetic Route Tests

These tests are public validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `mrb_test_01_question_route_ok` | Public question ID has evidence packet ID, landscape gate ID, review lens, uncertainty, blocked uses, and no patient-action output. | Copy or reference into route table only; leave packet section empty. |
| `mrb_test_02_missing_source_omitted` | Public question lacks source ID or metadata path. | Omit route field, report missing input, and do not generate substitute text. |
| `mrb_test_03_generated_summary_refused` | Proposed route includes a generated medical summary or rewritten claim. | Refuse as generated biomedical prose. |
| `mrb_test_04_real_case_refused` | Proposed route includes a real therapy history, report phrase, location, exact date, private note, or private path. | Refuse as private-only. |
| `mrb_test_05_trial_fit_refused` | Proposed route pairs a trial registry row with eligibility, availability, enrollment fit, site status, or recommendation wording. | Refuse trial matching/advice; preserve registry provenance only if safe. |
| `mrb_test_06_ranked_candidate_refused` | Proposed route ranks candidate questions, therapies, trials, targets, mechanisms, sources, or options. | Refuse ranking and preserve unranked IDs only. |
| `mrb_test_07_publication_gate_refused` | Proposed route treats inclusion in a packet skeleton as public release approval. | Refuse and route to publication gate. |

## What This Step Revealed

The public repo can now connect candidate review questions to the existing
review-packet-builder substrate without opening packet assembly. The remaining
near-term gap is not more builder machinery; it is the expert-validation loop
that records how public issue statuses, outreach maps, response ledgers, and
safe dispositions recur after review questions or packet routes expose a
needed human lens.

The next safest public step is therefore `expert-validation-loop-v0`.

## Handoff State

`multidisciplinary-review-packet-builder-v0` is complete as a public
route-rule skeleton.

The following remain blocked outside this artifact:

- real multidisciplinary packet assembly, tumor-board packets, clinician
  summaries, reviewer deliberation, reviewer identities, or reviewer decisions
- generated packet output, generated biomedical prose, generated summaries,
  generated public explainers, claim rewriting, or filled packet sections
- real case values, private records, raw reports, images, notes, exact dates
  tied to a person, source paths, identifiers, private prompts, or
  re-identification keys
- patient-specific outputs, diagnosis, prognosis, treatment guidance, trial
  guidance, eligibility guidance, availability guidance, expanded-access
  guidance, monitoring guidance, urgency guidance, referral guidance,
  safety-management guidance, action-path selection, publication authorization,
  or clinical decisions
- ranking, scoring, prioritizing, comparing, recommending, matching, or
  selecting candidates, sources, artifacts, tasks, targets, mechanisms,
  therapies, products, trials, reviewers, or options for a person

ORP should mark this item complete and activate `expert-validation-loop-v0`
next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names tied to a person, sponsor contacts, private
  paths, or free-text case details.
- No public intake form, upload path, backend, account workflow, packet
  assembler, generated-prose workflow, or public submission path.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency, referral,
  publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, therapy ranking, trial
  ranking, product ranking, option ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public route-rule skeleton, not executable builder code.
- This is not a real review-packet builder.
- This does not assemble review packets or packet skeleton outputs.
- This does not validate a real manifest, route table, or packet.
- This does not process, normalize, store, route, publish, match, compare,
  rank, verify, or authorize use of real case-linked review inputs.
- This does not complete expert review, clinician review, molecular review,
  pathology review, trial-status verification, sponsor/site verification,
  regulatory review, legal review, ethics review, privacy review,
  treating-team review, or publication review.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, urgency guidance, referral guidance, evidence ranking, option
  ranking, or a cure claim.
