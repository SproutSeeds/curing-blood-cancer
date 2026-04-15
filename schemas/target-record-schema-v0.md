# Target Record Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `target-record.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for blood-cancer target maps
- claim level: `open-question`
- boundary: research-use-only, not medical advice

## Purpose

This schema defines a standalone public target-record shape before any target
prioritization, evidence graph, extraction helper, therapy-record, or
trial-landscape tooling depends on target data.

It is a public research contract only. It is not a patient target-status
record, not an actionability record, not a treatment-selection record, not a
trial-matching record, and not a ranking system.

## Files

- [Target Record JSON Schema](./target-record.schema.json)
- [Target Record Template v0](./target-record-template-v0.json)

## Required Record Shape

Every target record must include:

| Field | Purpose |
| --- | --- |
| `target_record_id` | Stable public target-record ID. |
| `date` | Public record date. |
| `title` | Human-readable record title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `disease_scope` | Disease, subtype, disease-state, and excluded-scope notes. |
| `target_symbol` | Public gene, protein, antigen, pathway, or marker symbol. |
| `target_name` | Human-readable target name. |
| `target_record_type` | Target context class. |
| `target_context` | Source-backed public target context fields. |
| `claim_level` | Record claim level. |
| `source_ids` | Public source registry IDs. |
| `uncertainty` | Summary and known unknowns. |
| `limitations` | What the record does not prove or authorize. |
| `do_not_infer` | Explicit overclaiming guardrails. |
| `clinical_use_boundary` | Non-clinical use boundaries. |
| `review` | Creation, review status, and review notes. |

## Allowed Links

Target records may link to:

| Link Field | Allowed Use | Not Allowed |
| --- | --- | --- |
| `linked_claim_ids` | Public claim context. | Proof that a target is clinically actionable. |
| `linked_gap_ids` | Evidence-gap provenance. | Priority, urgency, or evidence strength. |
| `mechanism_group_ids` | Mechanism-map grouping. | Mechanism frequency or patient relevance. |
| `therapy_record_ids` | Future therapy-record cross-links. | Treatment selection or option ranking. |
| `trial_record_ids` | Future trial-landscape cross-links. | Eligibility, availability, or enrollment advice. |
| `public_task_ids` | Contribution tasks. | Clinical importance by task priority. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add patient-specific target expression, antigen-density values, assay
  values, candidate options, treatment choices, trial matching, actionability
  scores, or ranking fields.
- Do not use a valid target record as proof that a target is targetable,
  expressed in a person, clinically actionable, safe, effective, available, or
  relevant to any person.
- Do not build target prioritization, evidence graph, or extraction-helper
  tooling until target records validate against this schema.

## Validation

The public validator checks any JSON document with `target_record_id` against
`schemas/target-record.schema.json`.

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated target map and should not be treated as
evidence.

## Limitations

- Schema validation checks shape, not truth.
- Source IDs show where a record points, not whether the source supports a
  stronger claim.
- Expert review is still required before stronger public language.
- Source-specific extraction-helper schemas remain future work.
