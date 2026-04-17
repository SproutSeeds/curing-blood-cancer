# Caregiver Intake Public Projection Checklist v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-caregiver-intake-public-projection-checklist-v0`
- named frontier phase: `case-intake-frontier-v0`
- claim level: `open-question`
- status: `public-projection-gate-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only projection checklist, not medical advice

## Purpose

This checklist defines the first public-safe projection gate for the
caregiver case intake frontier.

It says what a future private caregiver intake workflow may project into the
public repo, what must remain private, and which blockers prevent the interface
from becoming a public case upload tool or clinical advice surface.

This is not an intake form, patient guide, triage tool, diagnosis tool,
prognosis tool, treatment recommender, trial matcher, monitoring plan,
expanded-access guide, or cure claim.

## Projection Verdicts

Every future intake-derived output must fail closed into one of these
dispositions before it can be considered for public use.

| Verdict | Meaning | Allowed public successor |
| --- | --- | --- |
| `blocked-private-only` | Contains or may contain real case data, identifiers, raw records, free-text case details, exact dates, contact details, or re-identification risk. | None. Keep in private lab only. |
| `blocked-clinical-advice` | Could be read as diagnosis, prognosis, treatment advice, trial advice, eligibility guidance, monitoring guidance, urgency guidance, expanded-access guidance, or a patient-specific option. | None. Rewrite or remove the output. |
| `needs-privacy-review` | May be aggregate or de-identified, but privacy review has not cleared it. | Private review queue only. |
| `needs-clinician-review` | Uses clinical labels or interpretations that require qualified review. | Private review queue only. |
| `needs-publication-gate` | May be public-safe after privacy, clinician, source, and publication review. | Publication-gate checklist, then cataloged public artifact if approved. |
| `synthetic-only-ok` | Uses visibly artificial data and cannot be mistaken for a real person. | Synthetic fixture, schema test, or prototype documentation. |
| `public-shape-ok` | Defines field names, enum values, gate states, validator logic, or boundary copy without case content. | Public protocol, schema, checklist, or tool update. |

Passing this checklist never authorizes public release of real case content. It
only identifies which public-safe artifact class a projection may enter next.

## Global Gates

| Gate | Pass condition | Immediate blocker |
| --- | --- | --- |
| Data reality gate | The output is synthetic-only, public shape-only, or aggregate-only after explicit review. | Any real person, real case, record excerpt, upload, date tied to a person, image, note, portal export, contact detail, identifier, or re-identification key. |
| Consent and privacy gate | Real intake stays in a private, consented, access-controlled system and `public_export_allowed` is false until publication review. | Public repo stores consent records, names, relationship details, private paths with live identifiers, or raw intake content. |
| Unknown-state gate | Every medical field supports `known`, `unknown`, `not_sure`, and `not_collected` states. | The interface forces certainty, removes "I do not know", or treats missing information as a clinical finding. |
| Source-before-interpretation gate | The intake asks where a value came from before it asks what the value means. | The interface interprets values, response terms, MRD status, labs, genetic context, imaging findings, or disease state for a person. |
| No-advice gate | The output cannot be read as diagnosis, prognosis, treatment, trial, eligibility, expanded-access, monitoring, urgency, or cure guidance. | Any generated recommendation, ranking, warning, next step, trial fit, treatment sequence, candidate option, monitoring interval, or emergency interpretation. |
| Clinician-review gate | Clinical labels remain source-stated or reviewed privately by qualified people. | The public artifact assigns clinical state, risk, relapse, refractory status, frailty, organ status, or response for a person. |
| Final-review gate | Before any private handoff, the caregiver sees privacy, no-advice, no-emergency, and clinician-review boundaries again. | Submission happens without final review or without explicit private-handoff-only language. |
| Publication gate | Public learning can happen only through a reviewed, source-backed, de-identified or aggregate artifact. | The output skips the publication-gate checklist or claims publication approval from intake alone. |

## Section Projection Checklist

| Intake step | Allowed public projection | Must stay private or blocked | Required gate |
| --- | --- | --- | --- |
| `intake_00_boundary` | Boundary copy family, acknowledgment field names, synthetic booleans. | Any reassurance that the tool can answer care questions, handle emergencies, or replace clinicians. | No-advice and emergency-boundary gate. |
| `intake_01_consent_readiness` | Consent status enum names and `public_export_allowed: false` shape. | Signed consent, identity, authorization records, caregiver or patient names, consent dates, private legal details. | Consent and privacy gate. |
| `intake_02_helper_context` | Helper role category and preferred-language category shape, including unknown/not_sure. | Helper name, contact details, exact relationship details, free text, finances, travel constraints, or family identifiers. | Data reality and free-text blocker gate. |
| `intake_03_diagnosis_context` | Source-stated disease-label field shape, source type enum, uncertainty state. | Report files, exact dates, institution, clinician names, accession numbers, or a public diagnosis assertion for a person. | Source-before-interpretation and clinician-review gate. |
| `intake_04_disease_state` | Disease-setting enum shape and uncertainty state. | Determining newly diagnosed, relapsed, refractory, post-transplant, post-CAR T, or maintenance state for a person. | Clinician-review gate. |
| `intake_05_treatment_history` | Therapy-class buckets, approximate sequence bucket shape, source-known flag. | Exact agents, dates, doses, toxicity details, facilities, private notes, or sequencing interpretation. | No-ranking and no-treatment-advice gate. |
| `intake_06_response_mrd_relapse` | Method, sample context, threshold, timepoint bucket, limitation text shape. | Exact MRD values, response interpretation, relapse determination, progression determination, or cure flag. | MRD endpoint guardrail and no-cure-claim gate. |
| `intake_07_labs_measurements` | Lab family, units-known flag, source-known flag, and synthetic examples. | Exact values, collection dates, lab reports, facilities, trend interpretation, monitoring intervals, or urgency flags. | No-monitoring and no-urgency gate. |
| `intake_08_context_modifiers` | Optional source-scoped context labels with unknown/not_sure states. | Prognosis, eligibility, treatment implications, option ranking, exact genomics, pathology identifiers, images, report text, or clinician notes. | Context-modifier boundary and clinician-review gate. |
| `intake_09_records_inventory` | Record-type list shape and available/missing/unknown enum shape. | Files, images, PDFs, portal exports, raw note text, accession numbers, exact dates, institutions, or record content. | Record-upload blocker gate. |
| `intake_10_questions_goals_constraints` | General question categories such as `organize-records` or `understand-what-is-missing`. | Free text, goals, finances, travel limits, caregiver names, care constraints, desired therapy, trial preferences, or personal prioritization. | Free-text and no-advice gate. |
| `intake_11_review_submit` | Review-screen requirements, blocked-public-submission status, private-handoff-only copy. | Public submission, public upload, automatic private routing without consent checks, or any generated patient-specific output. | Final-review, privacy, clinician-review, and publication gate. |

## Allowed Projection Record Shape

Future validators or static prototypes may use this shape with synthetic or
shape-only values:

```json
{
  "projection_id": "synthetic-or-shape-only-id",
  "phase": "case-intake-frontier-v0",
  "verdict": "synthetic-only-ok|public-shape-ok|blocked-private-only|blocked-clinical-advice|needs-privacy-review|needs-clinician-review|needs-publication-gate",
  "contains_real_case_data": false,
  "contains_phi": false,
  "contains_free_text_case_details": false,
  "patient_specific_outputs_allowed": false,
  "public_export_allowed": false,
  "requires_final_review": true,
  "requires_clinician_review": true,
  "requires_privacy_review": true,
  "requires_publication_gate": true,
  "unknown_state_supported": true,
  "allowed_public_successor": "synthetic fixture|public schema|public checklist|public protocol|none"
}
```

The shape is a gate record, not a case record. It must not include patient
facts, clinical interpretations, raw record content, or a path that identifies a
real private case.

## Current Synthetic Fixture Check

The current
[Multiple Myeloma Synthetic Caregiver Intake v0](../../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json)
passes the core public-safety screen because it is marked synthetic-only,
contains no PHI, blocks public submission, keeps exact values out of public
fields, supports unknown states, and requires final review before any private
handoff.

The fixture now includes a shape-only `intake_02_helper_context` section, so
the synthetic flow covers all steps in the product spec. The helper-context
section uses role/category fields only, includes unknown/not_sure states, and
keeps names, contacts, relationship details, and free text private-only.

The fixture also includes a synthetic projection-verdict block that points back
to this checklist, records `synthetic-only-ok`, and keeps public export,
patient-specific outputs, real case publication, PHI, free-text case details,
and upload behavior blocked.

## Cannot Be Used For

This checklist cannot be used to:

- collect real case data in this public repo
- decide whether a case is urgent
- diagnose or stage multiple myeloma
- interpret MRD, response, relapse, labs, imaging, genomics, frailty, organ
  status, or treatment history for a person
- recommend treatment, trials, monitoring, expanded access, or next clinical
  steps
- rank options, mechanisms, products, trials, clinicians, centers, or evidence
- approve public release of case-derived learning
- claim that a cure or vaccine has been found

## Next Phase Task

The case-intake frontier completion audit and downstream private shape
boundary are complete through
[Private Intake Schema Contract v0](private-intake-schema-contract-v0.md).

The static prototype planning layer is complete through
[Static Synthetic Caregiver Prototype Plan v0](static-synthetic-caregiver-prototype-plan-v0.md).
The protocol-level validator layer is complete through
[Caregiver Intake Public Projection Validator v0](caregiver-intake-public-projection-validator-v0.md).
The consent, privacy, security, retention, emergency, and clinician-review
gate is complete through
[Consent Privacy Security Retention Gate v0](consent-privacy-security-retention-gate-v0.md).
The active adaptive master backlog should now move to
`case-feature-normalization-contract-v0` as a public shape-only contract, not a
real case intake, storage, publication, or private-lab workflow.

## Review Boundary

This checklist organizes public research tooling. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance, eligibility
guidance, expanded-access guidance, monitoring guidance, urgency guidance, or a
claim that a cure or vaccine has been found.
