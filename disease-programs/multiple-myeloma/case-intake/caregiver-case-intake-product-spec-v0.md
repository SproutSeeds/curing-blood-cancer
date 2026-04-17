# Caregiver Case Intake Product Spec v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-caregiver-case-intake-product-spec-v0`
- named frontier phase: `case-intake-frontier-v0`
- ORP live phase target: `case-intake-product-spec-v0`
- claim level: `open-question`
- status: `active-phase-target-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research intake product specification, not medical advice

## Purpose

This artifact defines the first public-safe product specification for a
caregiver-friendly case intake surface.

The goal is to make it easy for a caregiver to organize a loved one's multiple
myeloma case details for a future private lab workflow without putting real
case data in this public repo and without turning the interface into clinical
advice.

This is a product and data-boundary artifact. It is not a patient guide,
clinical intake form, diagnosis tool, treatment recommender, trial matcher,
prognosis tool, monitoring plan, or cure claim.

## Who This Is For

The reference user is a caregiver or family advocate: motivated, worried, not
expected to know hematology vocabulary, and likely holding a mixture of portal
notes, lab reports, memory, screenshots, and questions.

The experience should let that caregiver say "I do not know" without shame,
save partial progress, review what will be shared, and understand that any real
case work must happen privately with consent and clinician involvement.

## Product Principle

The public repo may define:

- plain-language flow copy
- field inventory
- synthetic-only examples
- public-safe projection rules
- private handoff contracts
- no-advice and privacy boundary text
- validation gates and blocker states

The public repo must not contain:

- real patient identifiers
- real case details
- raw records, images, portal exports, notes, or dates tied to a person
- private contact details
- patient-specific inferences
- diagnosis, treatment, trial, prognosis, monitoring, urgency, or
  expanded-access guidance

## Caregiver Flow

| Step | Caregiver-facing intent | Public-safe implementation note |
| --- | --- | --- |
| `intake_00_boundary` | Explain what the system can and cannot do. | Show no-advice, no-emergency, privacy, consent, and clinician-review boundaries before any data entry. |
| `intake_01_consent_readiness` | Confirm the caregiver understands that real case data belongs only in a private system. | Public artifact documents the required consent states; it does not collect consent records. |
| `intake_02_helper_context` | Let the helper describe their relationship and what they are trying to organize. | Relationship, names, contact details, and free text are private-only in any real system. |
| `intake_03_diagnosis_context` | Capture the diagnosis label and where the information came from. | Public version only defines fields and uncertainty states. |
| `intake_04_disease_state` | Capture whether the case is newly diagnosed, relapsed, refractory, post-transplant, post-CAR T, maintenance, or unknown. | These states are source-scoped labels for routing evidence review, not clinical determinations. |
| `intake_05_treatment_history` | Build a plain-language treatment timeline. | Public projection may keep treatment classes only; exact dates, doses, clinicians, facilities, and free text stay private. |
| `intake_06_response_mrd_relapse` | Capture response, MRD, relapse, and progression terms only with source context. | Reuses MRD and endpoint guardrails; no response term can become a cure flag. |
| `intake_07_labs_measurements` | Let the caregiver enter key values only when units, dates, and source reports are available. | Exact values are private; public artifacts may use synthetic or aggregate patterns only after publication review. |
| `intake_08_context_modifiers` | Capture context such as bone, renal, infection, organ, frailty, immune status, cytogenetic/genomic, or extramedullary notes when known. | Optional, uncertain, source-scoped, non-identifying, and never used to generate prognosis or option ranking. |
| `intake_09_records_inventory` | List what record types exist and what is missing. | Public shape mirrors the case-to-cure manifest but never stores files or record contents. |
| `intake_10_questions_goals_constraints` | Capture what the family wants help organizing. | Goals and constraints are private free text; public projection is blocked unless generalized and reviewed. |
| `intake_11_review_submit` | Review before private submission. | Must show "not medical advice" and "private handoff only" again before submission. |

## Minimum Field Inventory

Each field group must support `known`, `unknown`, `not_sure`, and
`not_collected` states. Fields that can identify a person are private-only.

| Field group | Minimum public-safe shape | Private-only details | Provenance anchor | Public projection rule |
| --- | --- | --- | --- | --- |
| Governance | consent status enum, allowed-use enum, clinician-owner required flag | signed consent, identity, authorization records | Case-To-Cure Pipeline Blueprint v0 | no public projection |
| Helper context | helper role category, preferred-language category | helper name, contact, relationship details, free text | Public Safety Governance | no public projection |
| Diagnosis context | source-stated disease label, uncertainty, source type | report files, exact date, institution, clinician names | NCI PDQ and public roadmap | synthetic or aggregate only |
| Disease state | source-stated disease setting plus unknown/not sure | exact timeline, treating site, private clinician interpretation | Case-To-Cure Pipeline Blueprint v0 | synthetic or reviewed aggregate only |
| Treatment exposure | therapy class, approximate sequence bucket, response source status | exact agents, dates, doses, toxicities, facilities, notes | Treatment taxonomy and therapy boundary | class-level synthetic or reviewed aggregate only |
| Response, MRD, relapse | method, sample context, threshold, timepoint bucket, limitation text | exact values, report images, accession numbers, exact dates | MRD glossary and endpoint guardrail | never as cure flag |
| Labs and measurements | lab family, units-known flag, source-known flag, timepoint bucket | exact values, collection dates, facility, report PDFs | Measurement glossary and case-to-cure blueprint | synthetic or aggregate only |
| Cytogenetic/genomic context | known/unknown flag, source type, reviewed-feature bucket | exact variants, karyotype reports, pathology report identifiers | Context modifier map and source registry | no public case projection by default |
| Imaging, bone, renal, infection, organ, frailty context | optional context flags with source and uncertainty | images, report text, exact values, clinician notes | Context modifier map | synthetic or aggregate only |
| Record inventory | record-type list, missing/available state | files, portal exports, names, dates, identifiers | Case-To-Cure Pipeline Blueprint v0 | shape only |
| Family questions and constraints | question category and boundary acknowledgment | free text, goals, finances, travel limits, caregiver names | Public translation guide and public safety governance | no public projection |

## Required Interface Behaviors

- Use plain-language section titles.
- Put "I do not know" and "not sure" beside every medical field.
- Accept partial progress.
- Keep units and date helpers attached to the field they explain.
- Ask for the source of a value before asking for interpretation.
- Show a final review screen before private handoff.
- Display the clinical boundary before start and before submit.
- Route emergencies, urgent symptoms, and patient-specific care questions away
  from the tool and toward appropriate clinical or emergency channels.
- Never generate a treatment, trial, eligibility, prognosis, monitoring, or
  urgency output.

## Private Handoff Contract

Any real implementation must hand off to a private system, not this repo.

Private-only target paths remain conceptual until the private lab implements
them:

```text
../curing-blood-cancer-lab/cases/<case_id>/intake/caregiver-intake-draft.json
../curing-blood-cancer-lab/cases/<case_id>/intake/case-intake-manifest.json
../curing-blood-cancer-lab/cases/<case_id>/normalized/case-feature-bundle.json
```

Minimum private handoff envelope:

```json
{
  "handoff_id": "private-generated-id",
  "case_id": "private-pseudonymous-id",
  "disease_program": "multiple-myeloma",
  "source": "caregiver-intake",
  "consent_status": "pending|approved|withdrawn",
  "contains_phi": true,
  "public_export_allowed": false,
  "requires_clinician_review": true,
  "requires_privacy_review": true,
  "requires_publication_gate_before_any_public_learning": true
}
```

## Public Synthetic Fixture

The first public fixture is
[Multiple Myeloma Synthetic Caregiver Intake v0](../../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json).

The fixture is visibly artificial, contains no real patient data, and exists to
test field shape, unknown states, no-advice copy, and private handoff blocking.

## Boundary Copy Seed

Use this wording family in future interface prototypes:

> This tool helps organize information for private review. It does not diagnose,
> recommend treatment, recommend trials, estimate prognosis, monitor symptoms,
> or handle emergencies. Do not enter real medical details into any public demo.

The exact product copy can improve, but the meaning cannot weaken.

## Clawdad Objective

The original autonomous objective was `case-intake-frontier-v0`, now closed by
the [Case Intake Frontier Completion Audit Handoff v0](case-intake-frontier-completion-audit-handoff-v0.md).

Current adaptive successors are governed by the
[Case-To-Cure Adaptive Master Plan v0](../case-to-cure-adaptive-master-plan-v0.md).
The current private intake shape boundary is
[Private Intake Schema Contract v0](private-intake-schema-contract-v0.md).

Clawdad should extend caregiver-intake work only through public-safe artifacts:

- schema draft or data contract for private intake and public projection
- synthetic fixture expansion
- no-advice interface copy
- validator or checklist for PHI/advice blockers
- navigation links and catalog updates

Clawdad must stop if the next step requires real case data, private records,
credentials, outreach, clinical interpretation, or a live intake backend.

## Review Boundary

This specification organizes public research tooling. It does not provide
medical advice, diagnostic guidance, treatment guidance, trial guidance,
eligibility guidance, expanded-access guidance, monitoring guidance, urgency
guidance, or a claim that a cure or vaccine has been found.
