# Static Synthetic Caregiver Prototype Plan v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-static-synthetic-caregiver-prototype-plan-v0`
- active ORP item: `static-synthetic-caregiver-prototype-v0`
- master plan: `case-to-cure-adaptive-master-plan-v0`
- claim level: `open-question`
- status: `static-synthetic-prototype-plan-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only prototype plan, not medical advice

## Purpose

This plan defines the first static, synthetic-only caregiver prototype for the
multiple myeloma case-to-cure intake flow.

It shows how a caregiver-centered intake interface should behave using the public
product spec, private intake schema contract, projection checklist, and
synthetic fixture. It does not create a fillable form, live backend, upload
path, data store, account workflow, private-lab system, triage surface, or
clinical decision support tool.

This is a static prototype plan, not an intake implementation.

## Prototype Boundary

The prototype may include:

- static screen inventory
- screen copy requirements
- synthetic fixture bindings
- unknown and not-sure state behavior
- source-before-interpretation prompts
- final review requirements
- projection and refusal states
- no-advice, privacy, clinician-review, and publication-gate copy

The prototype must not include:

- real case data
- names, contact details, exact relationships, exact dates tied to a person,
  identifiers, accession numbers, record excerpts, report text, note text,
  images, portal exports, or uploads
- free-text case details
- private paths that identify a real case
- diagnosis, prognosis, treatment advice, trial advice, eligibility guidance,
  monitoring guidance, urgency guidance, expanded-access guidance, option
  ranking, or cure claims
- a live submit button, real save/resume behavior, account creation, storage,
  or network transmission

## Static Prototype Mode

| Prototype field | Required value | Why |
| --- | --- | --- |
| `prototype_mode` | `static-documentation-only` | Prevents the plan from becoming a public intake tool. |
| `data_mode` | `synthetic-fixture-only` | Blocks real case data and PHI. |
| `upload_enabled` | `false` | Blocks records, images, notes, portal exports, and screenshots. |
| `free_text_case_details_enabled` | `false` | Blocks accidental disclosure and advice prompts. |
| `public_submission_allowed` | `false` | Prevents public routing of case content. |
| `private_handoff_live` | `false` | Keeps real implementation outside this repo. |
| `patient_specific_outputs_allowed` | `false` | Blocks diagnosis, prognosis, treatment, trial, monitoring, urgency, and ranking outputs. |
| `projection_verdict` | `synthetic-only-ok` or `blocked-private-only` | Makes the prototype fail closed. |

## Screen Plan

| Screen | Static intent | Synthetic fixture binding | Required gate |
| --- | --- | --- | --- |
| `intake_00_boundary` | Start with no-advice, no-emergency, no-public-real-data, privacy, consent, and clinician-review copy. | `sections[].section_id == intake_00_boundary` | No-advice and emergency-boundary gate. |
| `intake_01_consent_readiness` | Explain that real consent belongs only in a private, governed system. | `intake_01_consent_readiness.synthetic_answers.consent_status` | Consent and privacy gate. |
| `intake_02_helper_context` | Ask only role category and language category in static mode; show that names, contact, relationship details, and free text stay private. | `intake_02_helper_context.synthetic_answers` | Data reality and free-text blocker gate. |
| `intake_03_diagnosis_context` | Ask for source type before label confidence; never diagnose. | `intake_03_diagnosis_context.synthetic_answers` | Source-before-interpretation and clinician-review gate. |
| `intake_04_disease_state` | Show source-stated disease setting as unknown/not_sure capable; never determine state. | `intake_04_disease_state.synthetic_answers` | Clinician-review gate. |
| `intake_05_treatment_history` | Show therapy-class buckets and sequence-known state; block exact agents, dates, doses, facilities, and notes. | `intake_05_treatment_history.synthetic_answers` | No-ranking and no-treatment-advice gate. |
| `intake_06_response_mrd_relapse` | Preserve MRD, response, relapse, method, threshold, and timepoint as source-context fields; never show cure flags. | `intake_06_response_mrd_relapse.synthetic_answers` | MRD endpoint guardrail and no-cure-claim gate. |
| `intake_07_labs_measurements` | Show units/source prompts and unknown state; block exact values and monitoring interpretation. | `intake_07_labs_measurements.synthetic_answers` | No-monitoring and no-urgency gate. |
| `intake_08_context_modifiers` | Show optional context labels as unknown/not_sure and source-required. | `intake_08_context_modifiers.synthetic_answers` | Context-modifier and clinician-review gate. |
| `intake_09_records_inventory` | Show record-type availability only; no upload widget or record contents. | `intake_09_records_inventory.synthetic_answers` | Record-upload blocker gate. |
| `intake_10_questions_goals_constraints` | Allow only general question categories; no free text, finances, travel constraints, therapy preferences, or personal prioritization. | `intake_10_questions_goals_constraints.synthetic_answers` | Free-text and no-advice gate. |
| `intake_11_review_submit` | Show final review and private-handoff-only copy; keep public submission disabled. | `intake_11_review_submit.synthetic_answers` | Final-review, privacy, clinician-review, and publication gate. |

## Required Static Copy Families

Every static screen must keep these meaning-preserving copy families visible:

| Copy family | Minimum meaning |
| --- | --- |
| Not medical advice | The prototype organizes information for private review and does not answer care questions. |
| No emergency handling | The prototype cannot handle urgent symptoms or emergencies. |
| No public real data | Public demos must use synthetic examples only. |
| Private handoff only | Any real intake belongs in a private, consented, access-controlled system. |
| Unknown is allowed | "I do not know" and "not sure" are always acceptable. |
| Source before interpretation | The interface asks where a value came from before asking what it means. |
| Clinician review needed | Clinical labels remain source-stated or privately reviewed. |
| Publication gate needed | Any future public learning needs privacy, clinician, source, and publication review. |

## Refusal And Blocker Paths

| Attempted action | Static prototype response | Public successor |
| --- | --- | --- |
| Enter a name, contact detail, exact date, location, institution, accession number, or identifier. | Block and explain that identifiers belong only in the private system. | None. |
| Paste free-text case details, notes, portal text, report excerpts, or family constraints. | Block and explain that public demos cannot accept free-text case content. | None. |
| Upload a report, image, screenshot, portal export, or record. | No upload control appears; the screen states uploads are private-lab-only. | None. |
| Ask "what treatment should we choose?" or similar advice. | Refuse and restate that the prototype cannot provide treatment, trial, prognosis, monitoring, urgency, or expanded-access guidance. | Public safety boundary copy only. |
| Treat `unknown` or `not_sure` as a finding. | Refuse the inference and preserve uncertainty. | Validator test case. |
| Try to submit publicly. | Keep public submission disabled and show private-handoff-only copy. | Synthetic fixture only. |

## Fixture Binding Rules

The static prototype should bind only to
[Multiple Myeloma Synthetic Caregiver Intake v0](../../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json).

Binding rules:

- Each screen maps to one `section_id`.
- The prototype may display synthetic enum values and booleans only.
- The prototype may not add new medical facts beyond the synthetic fixture.
- Missing fixture fields become `not_collected` or a prototype gap, not an
  inferred clinical state.
- Projection uses the fixture's `public_projection_result`.
- If a future fixture adds fields, the prototype must still pass the private
  intake schema contract and public projection checklist.

## Prototype Readiness Checklist

| Check | Required status |
| --- | --- |
| All `intake_00` through `intake_11` screens are represented. | required |
| All medical fields allow `unknown`, `not_sure`, or `not_collected`. | required |
| No upload, live submit, account, network, or storage behavior exists. | required |
| No exact values, dates, identifiers, record contents, or free-text case details appear. | required |
| No screen generates interpretation, advice, ranking, urgency, or cure claims. | required |
| Final review and private-handoff-only copy appear before the disabled submit state. | required |
| Public projection fails closed to `synthetic-only-ok`, `public-shape-only`, or a blocked verdict. | required |

## What This Step Revealed

The public case-intake surface now has enough shape to plan static screens
without reaching for a live product implementation.

The next safest public step is `public-projection-validator-v0`: a validator or
validator spec that turns the prototype's refusal paths, projection outcomes,
and private-intake contract rules into fail-closed checks. That validator
should still start as protocol-level logic unless an executable schema is
needed and can be kept synthetic-only.

## Handoff State

`static-synthetic-caregiver-prototype-v0` is complete for the static prototype
planning layer.

This handoff does not authorize:

- a public form
- a live demo
- a backend or database
- save/resume storage
- record uploads
- real case intake
- private-lab processing
- public submission
- clinical interpretation
- publication of case-derived learning

The ORP additional queue should activate `public-projection-validator-v0` next
unless validation, metadata, catalog, or public-safety checks reveal a more
urgent repair task.

## Review Boundary

This plan organizes public research tooling. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance, eligibility
guidance, expanded-access guidance, monitoring guidance, urgency guidance, or a
claim that a cure or vaccine has been found.
