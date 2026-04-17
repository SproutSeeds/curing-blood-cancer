# Private Intake Schema Contract v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-private-intake-schema-contract-v0`
- active ORP item: `private-intake-schema-contract-v0`
- master plan: `case-to-cure-adaptive-master-plan-v0`
- claim level: `open-question`
- status: `public-shape-contract-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only private-intake shape contract, not
  medical advice

## Purpose

This contract defines the public-safe shape of a future private multiple
myeloma intake record.

It exists so the public repo can reason about private intake fields, unknown
states, provenance, private-only content, and projection rules without storing
or inventing real case data. It is a markdown contract first; it is not an
executable schema, a live backend design, a database model, a case intake form,
or a private-lab implementation.

This contract is not a patient guide, diagnostic tool, treatment recommender,
trial matcher, prognosis tool, monitoring plan, urgency guide,
expanded-access guide, or cure claim.

## Contract Boundary

The future real intake record belongs only in a governed private environment.
The public repo may define:

- field group names
- allowed status values
- provenance fields
- unknown and not-sure states
- private-only rules
- public projection rules
- synthetic examples and validator requirements

The public repo must not contain:

- names, contact details, exact relationships, addresses, birth dates, medical
  record numbers, portal identifiers, accession numbers, re-identification keys,
  or signed consent records
- raw records, images, notes, reports, portal exports, screenshots, exact dates
  tied to a person, or free-text case details
- exact patient values, private clinician interpretations, private lab outputs,
  or case-specific rankings
- diagnosis, prognosis, treatment advice, trial advice, eligibility guidance,
  monitoring guidance, urgency guidance, expanded-access guidance, or cure
  claims

## Contract Envelope

A future private intake record should carry a private envelope like this. The
example is shape-only and uses placeholders, not real case data.

```json
{
  "record_id": "private-generated-id",
  "case_id": "private-pseudonymous-id",
  "disease_program": "multiple-myeloma",
  "schema_contract": "private-intake-schema-contract-v0",
  "intake_source": "caregiver-intake",
  "consent_state": "pending|approved|withdrawn|not_collected",
  "public_export_allowed": false,
  "contains_phi": true,
  "requires_final_review": true,
  "requires_clinician_review": true,
  "requires_privacy_review": true,
  "requires_publication_gate_before_public_learning": true
}
```

The contract envelope is not a public case record. Any real implementation
must keep it outside this repo.

## Allowed State Values

Every medical or case-context field group must support these state values:

| State | Meaning | Public projection rule |
| --- | --- | --- |
| `known` | A source exists in the private record. | Project only shape, synthetic examples, or reviewed aggregate learning. |
| `unknown` | The caregiver or private team does not know. | Preserve as uncertainty; do not infer. |
| `not_sure` | The caregiver is unsure or the source is ambiguous. | Preserve as uncertainty; do not convert to a clinical finding. |
| `not_tested` | A test or assessment is not known to have occurred. | Do not infer absence of a finding. |
| `not_collected` | The field was not asked, not answered, or intentionally skipped. | Do not infer. |
| `source_missing` | A claim was recalled but no source record is present. | Treat as source-context-needed. |
| `review_needed` | A qualified private reviewer must inspect the source. | Keep private until review. |
| `not_applicable` | The field is outside the scope of the intake path. | Do not reuse as a clinical conclusion. |

Missing data is never evidence of absence, prognosis, treatment fit, trial fit,
urgency, monitoring need, or cure-oriented success.

## Provenance Fields

Each field group should carry provenance before interpretation:

| Field | Allowed values or shape | Public rule |
| --- | --- | --- |
| `source_type` | `caregiver_report`, `portal_summary`, `lab_report`, `pathology_report`, `imaging_report`, `genomics_report`, `clinician_note`, `unknown`, `not_collected` | Source category only; no report text or identifiers. |
| `source_status` | `source_seen_private`, `source_reported_not_seen`, `source_missing`, `not_collected` | Public projection can preserve source status but not private content. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `follow_up`, `unknown`, `not_collected` | Use buckets only; no exact dates tied to a person. |
| `date_precision` | `none_public`, `year_only_if_reviewed`, `relative_bucket`, `private_exact_date` | Exact dates stay private. |
| `value_status` | `exact_private`, `bucket_public_if_reviewed`, `synthetic_only`, `not_collected` | Exact values stay private. |
| `review_status` | `not_reviewed`, `clinician_review_needed`, `privacy_review_needed`, `reviewed_private`, `publication_gate_needed` | Public release requires the publication gate. |

## Field Group Contract

| Field group | Public-safe shape | Private-only content | Projection rule |
| --- | --- | --- | --- |
| Governance and consent | Consent state enum, allowed-use enum, clinician-owner required flag, privacy-review required flag. | Signed consent, identities, authorizations, legal records, contact details, private owner IDs. | No public projection except shape-only gate fields. |
| Helper context | Helper role category, preferred-language category, confidence state. | Helper name, contact details, exact relationship, family details, free text, caregiver constraints. | Shape-only or synthetic-only. |
| Diagnosis context | Source-stated disease label, source type, uncertainty state. | Report files, exact diagnosis date, institution, clinician names, accession numbers, pathology text. | Synthetic or reviewed aggregate only; no public diagnosis assertion for a person. |
| Disease state | Source-stated setting enum and uncertainty state. | Exact timeline, private clinician interpretation, institution-specific staging details. | Source-scoped labels only; no prognosis, urgency, or option routing. |
| Treatment exposure | Therapy class buckets, approximate sequence bucket, source-known flag. | Exact drugs, doses, dates, toxicities, facilities, prescribing clinicians, narrative notes. | Class-level synthetic or reviewed aggregate only; no sequencing advice. |
| Response, MRD, relapse | Method, sample context, threshold-known flag, timepoint bucket, limitation text. | Exact MRD values, response interpretation, report images, accession numbers, exact collection dates. | Never a cure flag; public reuse must follow MRD endpoint guardrails. |
| Labs and measurements | Lab family, unit-known flag, source-known flag, timepoint bucket. | Exact values, report PDFs, lab facility, exact dates, trend interpretation. | Synthetic or reviewed aggregate only; no monitoring or urgency output. |
| Molecular and immune context | Known/unknown flag, source type, reviewed-feature bucket. | Exact variants, karyotype, pathology identifiers, flow data, report text. | No public case projection by default; use only reviewed aggregate or source-extraction tasks. |
| Context modifiers | Optional source-scoped flags for bone, renal, infection, organ, frailty, immune, extramedullary, and function context. | Images, report text, clinician notes, exact values, private assessments. | Optional labels only; no prognosis, eligibility, treatment intensity, or ranking. |
| Records inventory | Record-type enum, availability state, missing/unknown state. | Files, portal exports, screenshots, raw note text, exact dates, institutions, accession numbers. | Shape-only record inventory; no uploads or contents. |
| Questions, goals, constraints | General question category and boundary acknowledgment. | Free text, finances, travel details, care constraints, desired treatment or trial preferences, personal prioritization. | No public projection except generalized category after review. |
| Review and private handoff | Final-review required flag, public submission blocked flag, private-handoff-only state. | Private paths, case IDs, reviewer identities, handoff timestamps, support notes. | Shape-only gate fields; no public case routing. |

## Public Projection Rules

Every private field group must resolve to one of these projection outcomes
before any public reuse:

| Projection outcome | Public meaning | Allowed successor |
| --- | --- | --- |
| `blocked-private-only` | Contains or may contain private case data, identifiers, exact dates, report content, free text, or re-identification risk. | None; keep private. |
| `blocked-advice-risk` | Could be read as diagnosis, prognosis, treatment advice, trial advice, monitoring advice, urgency guidance, expanded-access advice, ranking, or a cure claim. | Rewrite, remove, or keep private. |
| `public-shape-only` | Defines names, enums, gates, or validator expectations without case content. | Public contract, schema summary, checklist, or protocol. |
| `synthetic-only-ok` | Uses visibly artificial data that cannot be mistaken for a real person. | Synthetic fixture or static prototype. |
| `reviewed-aggregate-needed` | Might become public only after privacy, clinician, source, and publication review. | Publication-gate queue only. |
| `source-extraction-task-ok` | Reveals a public source gap without carrying case details. | Public task or source extraction queue. |

Public projection must fail closed. A field cannot be projected merely because
it is common, useful, or already known to a caregiver.

## Future Validator Hooks

A later validator or validator spec should reject any public output if:

- `contains_phi` is true
- `public_export_allowed` is true before publication review
- a field carries a name, contact detail, exact date tied to a person,
  identifier, accession number, institution-specific case path, report text,
  note text, uploaded file, image, portal export, or private URI
- a field converts `unknown`, `not_sure`, `not_tested`, `not_collected`, or
  `source_missing` into a clinical finding
- a field produces a diagnosis, prognosis, treatment option, trial option,
  monitoring interval, urgency instruction, expanded-access path, ranking,
  recommendation, or cure-oriented outcome claim
- a field claims privacy, clinician, source, or publication review that has not
  occurred

## What This Step Revealed

The caregiver intake foundation can now move from product flow to private
record shape without using real data.

The next safest public step is a static synthetic caregiver prototype plan. It
can use this contract's field groups, unknown states, and projection outcomes
to show how a caregiver-centered intake interface would behave without accepting real
case details, uploading records, generating advice, or reaching a live backend.

The public projection validator remains important, but it can follow the static
prototype or be selected if the prototype exposes a more urgent validation gap.

## Handoff State

`private-intake-schema-contract-v0` is complete for the markdown contract
layer.

This handoff does not authorize:

- executable schema enforcement
- a live intake backend
- public uploads
- public storage of private records
- real case processing
- clinical interpretation
- publication of case-derived learning

The ORP additional queue should activate `static-synthetic-caregiver-prototype-v0`
next unless validation, metadata, catalog, or public-safety checks reveal a
more urgent repair task.

## Review Boundary

This contract organizes public research tooling. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance, eligibility
guidance, expanded-access guidance, monitoring guidance, urgency guidance, or a
claim that a cure or vaccine has been found.
