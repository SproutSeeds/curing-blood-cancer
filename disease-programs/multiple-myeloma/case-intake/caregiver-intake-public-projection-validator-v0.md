# Caregiver Intake Public Projection Validator v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-caregiver-intake-public-projection-validator-v0`
- active ORP item: `public-projection-validator-v0`
- master plan: `case-to-cure-adaptive-master-plan-v0`
- claim level: `open-question`
- status: `protocol-level-validator-spec-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only projection validator spec, not medical
  advice

## Purpose

This validator spec turns the caregiver intake projection checklist, private
intake schema contract, and static synthetic prototype refusal paths into
fail-closed public projection checks.

It is a protocol-level validator spec, not a live intake processor, backend,
case router, upload handler, publication approval, clinical decision tool, or
public form.

The validator's job is simple: a public projection either remains synthetic,
shape-only, or reviewed/gated aggregate work, or it is blocked.

## Validator Boundary

The validator may inspect:

- public shape fields
- synthetic fixture fields
- projection verdict fields
- gate booleans
- declared allowed successors
- static prototype refusal paths
- public artifact metadata and catalog linkage

The validator must not inspect, ingest, store, route, or transform:

- real case data
- patient or caregiver identifiers
- exact dates tied to a person
- contact details
- signed consent records
- report text, note text, images, portal exports, uploaded files, or private
  paths
- free-text case details
- private-lab case records
- clinical interpretations for a person

## Input Classes

| Input class | Allowed examples | Required verdict |
| --- | --- | --- |
| Synthetic fixture | Visible artificial fixture with `uses_real_patient_data: false`. | `synthetic-only-ok` |
| Public shape contract | Field names, enum names, booleans, gate states, allowed successor labels. | `public-shape-ok` |
| Static prototype documentation | Screen plan, refusal path, copy family, fixture binding. | `synthetic-only-ok` or `public-shape-ok` |
| Future reviewed aggregate | De-identified or aggregate learning after privacy, clinician, source, and publication gates. | `needs-publication-gate` until all gates pass |
| Real or possibly real case content | Anything tied to a person, record, date, identifier, note, report, upload, or free text. | `blocked-private-only` |
| Advice-like output | Diagnosis, prognosis, treatment, trial, monitoring, urgency, expanded-access, ranking, or cure-claim output. | `blocked-clinical-advice` |

Unrecognized input classes fail closed to `blocked-private-only` unless a
maintainer explicitly reclassifies the public shape in a reviewed artifact.

## Required Projection Envelope

Every candidate public projection must be representable as a shape-only record
with these fields before it can pass:

| Field | Required value or rule |
| --- | --- |
| `projection_id` | Synthetic or shape-only identifier; no private case ID. |
| `source_artifact_id` | Public artifact id, not a private path. |
| `projection_verdict` | One allowed verdict from the projection checklist. |
| `contains_real_case_data` | `false` for any public artifact. |
| `contains_phi` | `false` for any public artifact. |
| `contains_free_text_case_details` | `false` for any public artifact. |
| `contains_upload_or_record_content` | `false` for any public artifact. |
| `patient_specific_outputs_allowed` | `false` for any public artifact. |
| `public_submission_allowed` | `false` for any caregiver-intake prototype or fixture. |
| `public_export_allowed` | `false` unless privacy, clinician, source, and publication gates are recorded. |
| `unknown_state_supported` | `true` for medical or case-context fields. |
| `requires_final_review` | `true` before any private handoff concept. |
| `requires_clinician_review` | `true` when clinical labels exist. |
| `requires_privacy_review` | `true` for anything derived from real intake. |
| `requires_publication_gate` | `true` before public learning can be downstreamed. |
| `allowed_public_successor` | One of `synthetic fixture`, `public protocol`, `public schema`, `public checklist`, `public task`, `publication-gate queue`, or `none`. |

If a required field is missing, the validator fails closed.

## Fail-Closed Rules

| Rule id | Check | Fail verdict | Public repair path |
| --- | --- | --- | --- |
| `ppv_00_required_envelope` | Candidate lacks the required projection envelope or uses an unrecognized verdict. | `blocked-private-only` | Rewrite as public shape-only or synthetic-only. |
| `ppv_01_real_data_phi` | Any flag, field, text, path, or attachment suggests real case data, PHI, record content, image, portal export, upload, note, report, contact detail, exact date, identifier, accession number, institution-specific case path, or re-identification key. | `blocked-private-only` | Keep private; remove from public artifact. |
| `ppv_02_free_text_case_details` | Candidate accepts or displays unconstrained narrative about a person, family, logistics, finances, travel, goals, symptoms, or care constraints. | `blocked-private-only` | Replace with shape-only category enums or keep private. |
| `ppv_03_public_submission` | Candidate enables public submit, save/resume storage, network transmission, account workflow, real private handoff, or public export without publication-gate clearance. | `blocked-private-only` | Keep prototype static or route to private governed implementation outside this repo. |
| `ppv_04_advice_language` | Candidate can be read as diagnosis, staging, prognosis, treatment advice, trial advice, eligibility guidance, monitoring guidance, urgency guidance, expanded-access guidance, option ranking, patient matching, trial matching, or cure claim. | `blocked-clinical-advice` | Rewrite as boundary copy, source-context question, or private clinical review blocker. |
| `ppv_05_unknown_state_inference` | Candidate converts `unknown`, `not_sure`, `not_tested`, `not_collected`, or `source_missing` into a finding, absence, risk, eligibility, urgency, or next step. | `blocked-clinical-advice` | Preserve uncertainty and mark source-context-needed or review-needed. |
| `ppv_06_source_before_interpretation` | Candidate interprets MRD, response, relapse, labs, imaging, genetics, context modifiers, treatment exposure, or disease state before source type, source status, method, threshold, timepoint, and review status are preserved. | `blocked-clinical-advice` | Add source-context fields or block reuse. |
| `ppv_07_missing_review_gates` | Candidate claims privacy, clinician, source, consent, or publication review has occurred without a public gate record or allowed successor. | `needs-publication-gate` | Route to publication-gate or private review; do not publish as learning. |
| `ppv_08_synthetic_fixture_binding` | Candidate claims `synthetic-only-ok` without binding to the public synthetic fixture or without `uses_real_patient_data: false`. | `blocked-private-only` | Bind to the synthetic fixture or mark as private-only. |
| `ppv_09_allowed_successor_mismatch` | Candidate verdict and allowed successor conflict, such as advice output marked as a protocol, real content marked as a fixture, or publication-gate-needed output marked public-ready. | `blocked-private-only` | Correct verdict and successor before reuse. |
| `ppv_10_static_prototype_refusal` | Candidate lacks refusal paths for identifiers, free text, uploads, advice requests, unknown-state inference, and public submission attempts. | `public-shape-ok` only after repair | Add refusal paths before any prototype documentation is cataloged. |

## Synthetic Test Matrix

| Test id | Candidate | Expected verdict | Required reason |
| --- | --- | --- | --- |
| `ppv_test_00_fixture_pass` | Current synthetic caregiver intake fixture. | `synthetic-only-ok` | Artificial fixture, no PHI, public submission false, final review true. |
| `ppv_test_01_shape_contract_pass` | Private intake schema contract field names and enum values only. | `public-shape-ok` | Shape-only; no real case content. |
| `ppv_test_02_static_plan_pass` | Static prototype screen plan and refusal table. | `public-shape-ok` | Documentation-only; no live UI, backend, or uploads. |
| `ppv_test_03_identifier_block` | Candidate includes name, contact detail, exact date, accession number, institution, or private path. | `blocked-private-only` | Real or re-identification risk. |
| `ppv_test_04_free_text_block` | Candidate includes pasted report text, note text, portal text, family constraints, or goals. | `blocked-private-only` | Free-text case details. |
| `ppv_test_05_upload_block` | Candidate includes upload control, image, PDF, screenshot, or record content. | `blocked-private-only` | Public repo cannot accept records. |
| `ppv_test_06_advice_block` | Candidate answers what treatment, trial, monitoring, expanded-access path, or urgent action should happen. | `blocked-clinical-advice` | Patient-specific guidance risk. |
| `ppv_test_07_unknown_inference_block` | Candidate turns `unknown` or `not_sure` into a negative finding or care implication. | `blocked-clinical-advice` | Uncertainty was converted into interpretation. |
| `ppv_test_08_publication_gate_block` | Candidate says case-derived public learning is approved without gate evidence. | `needs-publication-gate` | Publication approval cannot come from intake alone. |

## Handoff State

`public-projection-validator-v0` is complete for the protocol-level validator
spec layer.

The validator spec revealed that the next safest public step is
`consent-privacy-security-retention-gate-v0`: the validator can name fail
states, but a future real intake system still needs an explicit public blocker
map for consent, privacy, security, retention, emergency handling,
clinician-review, and human approval before any real case workflow exists.

This handoff does not authorize:

- executable processing of real case data
- public uploads
- live intake
- public submission
- private-lab handoff
- clinical interpretation
- publication of case-derived learning

The ORP additional queue should activate
`consent-privacy-security-retention-gate-v0` next unless validation, metadata,
catalog, or public-safety checks reveal a more urgent repair task.

## Review Boundary

This validator spec organizes public research tooling. It does not provide
medical advice, diagnostic guidance, treatment guidance, trial guidance,
eligibility guidance, expanded-access guidance, monitoring guidance, urgency
guidance, or a claim that a cure or vaccine has been found.
