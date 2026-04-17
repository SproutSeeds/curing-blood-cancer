# End-To-End Synthetic Case Dry Run v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-end-to-end-synthetic-case-dry-run-v0`
- ORP item: `end-to-end-synthetic-case-dry-run-v0`
- dry-run status: synthetic route table and refusal report complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: synthetic-only; no real case data, identifiers, raw records,
  person-linked dates, free-text case details, private correspondence, or
  patient-specific outputs
- last reviewed: `2026-04-16`

## Purpose

This artifact dry-runs the public-safe case-to-cure path with visibly
artificial fixtures only.

It connects the synthetic caregiver intake fixture, synthetic case-to-cure
pipeline fixture, projection validator, normalization contracts, evidence
retrieval packet, trial and therapy landscape gate, candidate question set,
review-packet builder, expert-validation loop, case-to-public learning
extraction gate, and publication gate into one route table.

It is not a runner, backend, extractor, de-identification system, case
processor, evidence engine, trial finder, matcher, ranker, review-packet
assembler, publication workflow, clinical decision system, or advice surface.

## Current Dry-Run Decision

Current decision: `synthetic-route-table-and-refusal-report-only`.

Allowed public behavior:

- copy synthetic fixture IDs and public artifact IDs
- reference public gate, validator, and owner artifacts
- mark fields as `copy_public_id`, `reference_public_artifact`,
  `synthetic_shape_only`, `omit_missing_or_private`, `refuse_unsafe`, or
  `block_human_gate`
- preserve uncertainty, limitation, blocked-use, publication-gate, and
  human-gate states
- show success, omit, refusal, and blocker paths without using real data

Blocked behavior:

- processing, summarizing, sanitizing, extracting, or publishing real case
  data, raw records, images, notes, reports, person-linked dates, private
  paths, private prompts, identifiers, re-identification keys, rare
  identifying combinations, or free-text case details
- copying private correspondence, unpublished expert comments, reviewer
  deliberation, permission context, or private reviewer identities
- producing diagnosis, prognosis, treatment guidance, trial guidance,
  eligibility guidance, availability guidance, expanded-access guidance,
  monitoring guidance, urgency guidance, safety-management guidance,
  recommendation, sequencing, patient matching, trial matching, comparison,
  prioritization, ranking, candidate option output, clinical decision, release
  authorization, publication authorization, or cure claim

Allowed public successor:
`case-to-cure-master-completion-audit-v0`, limited to auditing whether the
adaptive public backlog is complete, safely blocked by named gate classes, or
ready for a new named phase.

## Dry-Run Inputs

| Input | Role In This Dry Run | Boundary |
| --- | --- | --- |
| [Multiple Myeloma Synthetic Caregiver Intake v0](../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json) | Provides visibly artificial intake sections, unknown states, and public projection booleans. | Not a public intake form and not a real case. |
| [Multiple Myeloma Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md) | Provides synthetic `case_00` through `case_14` stage coverage. | Not permission to run a real case through public artifacts. |
| [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md) | Provides no-PHI, no-free-text, no-advice, no-public-submission, and publication-bypass refusal logic. | Does not process real intake data. |
| [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md) | Provides stage owner artifacts, validator or gate fields, blockers, and allowed public successors. | Stage coverage is not case processing. |
| [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md) | Provides allowed output type, privacy, aggregation, source, review, blocked-use, and publication-gate envelope fields. | Does not extract, de-identify, publish, or authorize learning. |
| [Publication-Gate Checklist v0](publication-gate-checklist-v0.md) | Provides publication blocker language and release decision boundaries. | Cannot be cleared by this dry run. |

## Dry-Run Envelope

Every row in this dry run can be represented with these public-safe fields:

| Field | Public Shape |
| --- | --- |
| `dry_run_id` | `multiple-myeloma-end-to-end-synthetic-case-dry-run-v0` |
| `fixture_ids` | Public synthetic fixture IDs only. |
| `stage_id` | `case_00` through `case_14` or `intake_00` through `intake_11`. |
| `owner_artifact_ids` | Public artifact IDs or public paths only. |
| `synthetic_input_class` | `synthetic_fixture`, `public_artifact_reference`, `missing_source_context`, `unsafe_private_material`, or `human_gate_needed`. |
| `route_decision` | `copy_public_id`, `reference_public_artifact`, `synthetic_shape_only`, `omit_missing_or_private`, `refuse_unsafe`, or `block_human_gate`. |
| `gate_or_validator_ids` | Public gate IDs only. |
| `expected_public_state` | Synthetic stage coverage, public-source linkage, gate state, blocker note, or no public output. |
| `private_material_state` | `none`, `omitted`, `refused`, or `human_gate_needed`. |
| `blocked_use_flags` | Must include no patient-specific output, no medical advice, no recommendation, no ranking, no matching, no private correspondence, and no publication authorization. |
| `omitted_field_state` | Names only the field class omitted, not the private value. |
| `refusal_reason` | Public-safe reason label, never private content. |
| `publication_gate_state` | `not_applicable`, `publication_gate_needed`, `public_release_blocked`, or `human_publication_gate_needed`. |
| `allowed_public_output` | Synthetic route record, source-context task, metadata repair, blocker note, or no output. |
| `public_export_allowed` | `false` for case-derived outputs; synthetic route-table artifact only. |
| `next_public_action` | Master audit, source task, metadata repair, or no public action. |

## End-To-End Route Table

| Stage | Synthetic Input | Owner Artifacts And Gates | Route Decision | Expected Public State |
| --- | --- | --- | --- | --- |
| `intake_00` Boundary screen | Synthetic caregiver confirms no medical advice, emergency, and no public real-data boundary. | Caregiver fixture; product spec; projection checklist. | `copy_public_id`; `reference_public_artifact`. | Synthetic boundary acknowledgement only. |
| `intake_01` Consent readiness | Synthetic consent status is `pending`; public export is false. | Consent privacy security retention gate. | `block_human_gate`. | Real intake remains consent-gated. |
| `intake_02` Helper context | Helper role, language, confidence, relationship, and free text are unknown or private-only. | Private intake schema contract; projection validator. | `omit_missing_or_private`. | Helper identity and relationship details omitted. |
| `intake_03` Diagnosis context | Source-stated synthetic label says multiple myeloma; no exact dates. | Case feature normalization contract. | `synthetic_shape_only`. | Source-stated disease label shape only, no diagnosis output. |
| `intake_04` Disease state | Disease setting unknown; clinician review needed. | Case feature normalization contract; stage validator map. | `block_human_gate`. | Disease-state interpretation remains clinical-review-needed. |
| `intake_05` Treatment history | Prior therapy class unknown; sequence and exact agents private-only. | Therapy exposure timeline contract. | `omit_missing_or_private`; `refuse_unsafe` if sequence is inferred. | Therapy exposure shape only, no sequencing. |
| `intake_06` Response and MRD | MRD status, method, and response term source are unknown. | Measurement normalization contract; MRD endpoint guardrail. | `omit_missing_or_private`; `refuse_unsafe` for cure wording. | Endpoint terms remain unknown; no cure flag. |
| `intake_07` Labs and measurements | Lab reports unknown; exact values not public. | Measurement normalization contract; projection validator. | `omit_missing_or_private`. | Units and value context remain private-review-needed. |
| `intake_08` Context modifiers | Bone, renal, infection, cytogenetic, extramedullary, and frailty context are unknown. | Context modifier map; molecular immune context contract. | `synthetic_shape_only`. | Optional context fields stay unknown and non-directive. |
| `intake_09` Records inventory | Record types unknown; public upload disallowed. | Projection validator; consent gate. | `refuse_unsafe`. | Public file upload and record contents remain blocked. |
| `intake_10` Questions and constraints | Question categories are generic; free text and logistics private-only. | Candidate question set; private intake contract. | `omit_missing_or_private`. | Generic question categories only. |
| `intake_11` Review and submit | Synthetic fixture is not ready for private handoff; public submission false. | Static synthetic prototype plan; projection validator. | `block_human_gate`. | No public submission or real handoff. |
| `case_00` Governance setup | Synthetic consent placeholder and synthetic owner role. | Pipeline blueprint; consent gate; blocker register. | `block_human_gate`. | Governance boundary note only. |
| `case_01` Intake partition | Synthetic record inventory has no files and no identifiers. | Synthetic pipeline fixture; projection validator. | `synthetic_shape_only`. | Synthetic manifest shape only. |
| `case_02` De-identification plan | Synthetic PHI inventory contains no real identifiers. | Publication gate; private-to-public workflow. | `block_human_gate`. | De-identification remains private governance work. |
| `case_03` Disease-state normalization | Synthetic disease-state placeholders. | Case feature normalization contract; context modifier map. | `reference_public_artifact`. | Schema feedback only; no diagnosis interpretation. |
| `case_04` Measurement normalization | Synthetic MRD and relapse placeholders. | Measurement normalization contract; MRD guardrail. | `reference_public_artifact`; `omit_missing_or_private`. | Measurement gap or source-context updates only. |
| `case_05` Molecular and immune context | Synthetic target-assay and immune-context placeholders. | Molecular immune context contract; mechanism maps. | `synthetic_shape_only`. | Public extraction task candidates only. |
| `case_06` Exposure and resistance map | Synthetic exposure and resistance placeholders. | Therapy exposure timeline contract; immune therapy boundary; scoring rubric. | `reference_public_artifact`; `refuse_unsafe` for sequencing or ranking. | Generic exposure vocabulary only. |
| `case_07` Evidence retrieval | Public source IDs and query IDs only. | Evidence retrieval packet; source registry; ClinicalTrials.gov protocol. | `copy_public_id`; `reference_public_artifact`. | Public-source linkage and limitation state only. |
| `case_08` Candidate hypothesis generation | Synthetic candidate review-question IDs. | Candidate hypothesis review question set; scoring rubric. | `copy_public_id`; `refuse_unsafe` for options. | Question-only review scaffold. |
| `case_09` Candidate scoring | Synthetic rubric context only. | Candidate-option scoring rubric. | `refuse_unsafe`. | No score, ranking, or option priority for care. |
| `case_10` Feasibility and exclusion review | Synthetic trial-query and access-context placeholders. | Trial therapy landscape non-advice gate; ClinicalTrials.gov protocol. | `refuse_unsafe`; `block_human_gate`. | No availability, eligibility, site, sponsor, or access output. |
| `case_11` Multidisciplinary review | Synthetic review body label only. | Multidisciplinary review packet builder; expert validation loop. | `copy_public_id`; `reference_public_artifact`; `refuse_unsafe` for generated packets. | Route rules only, no packet assembly. |
| `case_12` Action-path selection | Synthetic decision label is `needs-more-data`. | Scoring rubric; publication gate; public review gate. | `block_human_gate`. | External clinical decision remains blocked. |
| `case_13` Monitoring plan | Synthetic monitoring placeholder only. | Measurement glossary; publication gate. | `refuse_unsafe`. | No monitoring advice or safety-management guidance. |
| `case_14` Outcome capture | Synthetic public-learning candidate flag and publication-gate result. | Case-to-public learning extraction gate; publication gate; public review gate. | `refuse_unsafe`; `block_human_gate`. | Publication-gate refusal; no public case learning. |

## Success, Omit, Refusal, And Blocker Paths

| Path Type | Demonstrated By | Public Outcome |
| --- | --- | --- |
| Success | Public synthetic fixture IDs, source IDs, query IDs, artifact IDs, and stage IDs propagate through the route table. | Synthetic route record and public artifact references only. |
| Omit | Helper context, exact agents, exact dates, lab values, raw records, free text, logistics, constraints, and private review details are represented only by field classes. | Private field classes are omitted without values. |
| Refusal | Public upload, cure wording, therapy sequencing, candidate scoring, eligibility, availability, trial matching, generated packet prose, monitoring advice, and publication-ready claims. | Unsafe output is refused with public reason labels. |
| Blocker | Consent, privacy, de-identification, clinician review, trial-site or sponsor verification, clinical decision, legal/regulatory review, and publication review. | Human gate classes remain active blockers outside the public repo. |

## Synthetic Gate Tests

These tests describe expected dry-run behavior. They are not executable tests
and are not real case records.

| Test ID | Synthetic Input Shape | Expected Route |
| --- | --- | --- |
| `e2e_test_01_full_synthetic_path_ok` | All rows use public fixture IDs, public artifact IDs, source IDs, and gate-state labels only. | Allow synthetic route-table artifact. |
| `e2e_test_02_identifier_refused` | A candidate row contains a real name, contact detail, private case ID, private path, exact date, image, note, or report phrase. | `refuse_unsafe`; no public content. |
| `e2e_test_03_private_field_omitted` | A row needs exact therapy agents, lab values, helper relationship details, logistics, free text, or raw record content. | `omit_missing_or_private`; field class only. |
| `e2e_test_04_missing_source_context_blocked` | A proposed public claim lacks source IDs, query IDs, limitations, or uncertainty. | `block_human_gate` or source-context task; no claim use. |
| `e2e_test_05_generated_case_summary_refused` | A candidate output summarizes the synthetic path as if it were a person's course. | `refuse_unsafe`; no case summary. |
| `e2e_test_06_candidate_ranking_refused` | A row scores, prioritizes, compares, or ranks options. | `refuse_unsafe`; no ranking or recommendation. |
| `e2e_test_07_trial_access_refused` | A row implies availability, eligibility, site fit, sponsor access, or trial match. | `refuse_unsafe`; no trial or access guidance. |
| `e2e_test_08_private_expert_comment_refused` | A row depends on private correspondence or unpublished reviewer comments. | `refuse_unsafe`; public disposition only. |
| `e2e_test_09_publication_ready_claim_refused` | A row says the dry run authorizes release, publication, clinical use, or public case learning. | `block_human_gate`; publication authorization remains outside the repo. |

## What This Step Revealed

The public pipeline now has a single synthetic-only proof surface from
caregiver intake through publication-gate refusal. The useful remaining work
is no longer another stage contract; it is a master completion audit that
checks whether the adaptive public backlog is complete, safely blocked, or
ready for a new named phase.

The next safest public step is therefore
`case-to-cure-master-completion-audit-v0`.

## Handoff State

`end-to-end-synthetic-case-dry-run-v0` is complete as a public route table and
refusal report.

The following remain blocked outside this artifact:

- real case intake, public case upload, private-lab case processing, raw record
  processing, de-identification automation, public case extraction, generated
  case summaries, generated review packets, public case reports, or
  publication workflows
- identifiers, raw records, images, notes, report text, exact dates tied to a
  person, private paths, private prompts, re-identification keys, private
  correspondence, unpublished expert comments, reviewer deliberation, private
  permission context, or rare identifying combinations
- patient-specific diagnosis, prognosis, treatment guidance, trial guidance,
  eligibility guidance, availability guidance, expanded-access guidance,
  access guidance, monitoring guidance, urgency guidance, safety-management
  guidance, recommendation, matching, sequencing, ranking, comparison,
  prioritization, option selection, publication authorization, release
  authorization, or clinical decision
- consent, privacy, legal, regulatory, clinical, treating-team, sponsor, site,
  ethics, institutional-review, security, retention, emergency, and
  publication decisions

ORP should mark this item complete and activate
`case-to-cure-master-completion-audit-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, raw records, images, notes, exact person-linked dates,
  raw assay values, therapy histories, molecular reports, pathology reports,
  flow reports, genomics reports, clinician names, site names tied to a
  person, sponsor contacts, contact details, private paths, private prompts,
  private case IDs, or re-identification keys.
- No private correspondence, unpublished expert comments, reviewer
  deliberation, single-case claims, public case report, de-identification
  automation, generated case summary, generated review packet, or publication
  workflow.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, product ranking, therapy
  ranking, trial ranking, option ranking, comparison, prioritization, or review
  decision.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This is a public dry-run artifact, not executable validation code.
- This uses synthetic fixtures and public artifact references only.
- This does not inspect private lab records, private correspondence, expert
  replies, or real case data.
- This does not prove that future real-case intake, de-identification,
  normalization, source retrieval, review packet assembly, expert validation,
  public learning extraction, or publication can be done safely.
- This does not complete consent review, privacy review, clinical review,
  legal review, regulatory review, sponsor or site verification,
  institutional review, ethics review, security review, retention review,
  emergency handling, publication review, release review, or protected-branch
  review.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, urgency guidance, safety-management guidance, or a cure claim.
