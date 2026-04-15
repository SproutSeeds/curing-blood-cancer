# Therapy Record Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `therapy-record.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for blood-cancer therapy maps
- claim level: `open-question`
- boundary: research-use-only, not medical advice

## Purpose

This schema defines a standalone public therapy-record shape before any therapy
landscape, trial explorer, evidence graph, extraction helper, or review-packet
builder depends on therapy fields.

It is a public research contract only. It is not a treatment recommendation,
not a candidate-option record, not a therapy ranking, not dosing guidance, not
trial guidance, not expanded-access guidance, and not a patient-matching record.

## Files

- [Therapy Record JSON Schema](./therapy-record.schema.json)
- [Therapy Record Template v0](./therapy-record-template-v0.json)

## Required Record Shape

Every therapy record must include:

| Field | Purpose |
| --- | --- |
| `therapy_record_id` | Stable public therapy-record ID. |
| `date` | Public record date. |
| `title` | Human-readable record title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `disease_scope` | Disease, subtype, disease-state, and excluded-scope notes. |
| `therapy_name` | Public therapy-class, modality, or strategy name. |
| `therapy_class` | Human-readable therapy grouping. |
| `therapy_record_type` | Therapy context class. |
| `therapy_context` | Source-backed public therapy context fields. |
| `claim_level` | Record claim level. |
| `source_ids` | Public source registry IDs. |
| `uncertainty` | Summary and known unknowns. |
| `limitations` | What the record does not prove or authorize. |
| `do_not_infer` | Explicit overclaiming guardrails. |
| `clinical_use_boundary` | Non-clinical use boundaries. |
| `review` | Creation, review status, and review notes. |

## Allowed Links

Therapy records may link to:

| Link Field | Allowed Use | Not Allowed |
| --- | --- | --- |
| `target_record_ids` | Public target-context linkage. | Targetability, patient expression, or actionability. |
| `linked_claim_ids` | Public claim context. | Proof that a therapy is effective, safe, available, or appropriate. |
| `linked_gap_ids` | Evidence-gap provenance. | Priority, urgency, or evidence strength. |
| `mechanism_group_ids` | Mechanism-map grouping. | Mechanism frequency or patient relevance. |
| `trial_record_ids` | Future trial-landscape cross-links. | Eligibility, availability, enrollment advice, or trial recommendation. |
| `public_task_ids` | Contribution tasks. | Clinical importance by task priority. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add patient-specific candidate options, treatment choices, therapy
  rankings, dosing, sequencing, eligibility, availability claims for any person,
  expanded-access guidance, trial matching, or actionability scores.
- Do not use a valid therapy record as proof that a therapy is effective, safe,
  available, eligible, indicated, appropriate, sequenced, or relevant to any
  person.
- Do not build therapy landscape, trial explorer, evidence graph, or
  extraction-helper tooling until therapy records validate against this schema.

## Validation

The public validator checks any JSON document with `therapy_record_id` against
`schemas/therapy-record.schema.json`.

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated therapy landscape and should not be
treated as evidence.

## Limitations

- Schema validation checks shape, not truth.
- Source IDs show where a record points, not whether the source supports a
  stronger claim.
- Expert review is still required before stronger public language.
- Source-specific extraction-helper schemas remain future work.
