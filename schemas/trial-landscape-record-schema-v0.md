# Trial-Landscape Record Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `trial-landscape-record.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for blood-cancer trial landscapes
- claim level: `open-question`
- boundary: research-use-only, not medical advice

## Purpose

This schema defines a standalone public trial-landscape record shape before any
trial explorer, evidence graph, extraction helper, review-packet builder, or
map-generation tool depends on registry fields.

It is a public research contract only. It is not a trial finder, not trial
guidance, not eligibility guidance, not enrollment advice, not an availability
claim for any person, not sponsor access guidance, not expanded-access
guidance, not a treatment recommendation, and not a patient-matching record.

## Files

- [Trial-Landscape Record JSON Schema](./trial-landscape-record.schema.json)
- [Trial-Landscape Record Template v0](./trial-landscape-record-template-v0.json)

## Required Record Shape

Every trial-landscape record must include:

| Field | Purpose |
| --- | --- |
| `trial_landscape_record_id` | Stable public trial-landscape record ID. |
| `date` | Public record date. |
| `title` | Human-readable record title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `disease_scope` | Disease, subtype, disease-state, and excluded-scope notes. |
| `landscape_scope` | Public landscape type and summary fields. |
| `registry_provenance` | Registry source IDs, data timestamp, access date, query scope, and optional query-record links. |
| `claim_level` | Record claim level. |
| `source_ids` | Public source registry IDs. |
| `uncertainty` | Summary and known unknowns. |
| `limitations` | What the record does not prove or authorize. |
| `do_not_infer` | Explicit overclaiming guardrails. |
| `clinical_use_boundary` | Non-clinical use boundaries. |
| `review` | Creation, review status, and review notes. |

## Allowed Links

Trial-landscape records may link to:

| Link Field | Allowed Use | Not Allowed |
| --- | --- | --- |
| `target_record_ids` | Public target-context linkage. | Targetability, patient expression, or actionability. |
| `therapy_record_ids` | Public therapy-context linkage. | Treatment selection, sequencing, or option ranking. |
| `linked_claim_ids` | Public claim context. | Proof that a trial, therapy, or target is effective, safe, available, or appropriate. |
| `linked_gap_ids` | Evidence-gap provenance. | Priority, urgency, or evidence strength. |
| `mechanism_group_ids` | Mechanism-map grouping. | Mechanism frequency or patient relevance. |
| `public_task_ids` | Contribution tasks. | Clinical importance by task priority. |
| `registry_provenance.trial_query_record_ids` | Public query-record provenance. | Eligibility, enrollment advice, availability claims, or trial matching. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add patient-specific candidate options, treatment choices, trial
  matches, trial rankings, eligibility guidance, enrollment advice, availability
  claims for any person, sponsor access instructions, expanded-access guidance,
  dosing, sequencing, or actionability scores.
- Do not use a valid trial-landscape record as proof that a trial is available,
  eligible, safe, effective, appropriate, enrolling, accessible, or relevant to
  any person.
- Do not build trial explorer, evidence graph, extraction-helper, or review
  packet tooling until trial-landscape records validate against this schema.

## Validation

The public validator checks any JSON document with
`trial_landscape_record_id` against
`schemas/trial-landscape-record.schema.json`.

The validator also rejects common clinical-use fields such as eligibility,
enrollment advice, availability-for-a-person, sponsor access, expanded-access
guidance, candidate options, option ranking, trial matching, treatment
recommendation, real case data, and patient identifiers.

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated trial landscape and should not be treated
as evidence.

## Limitations

- Schema validation checks shape, not truth.
- Registry source IDs show where a record points, not whether a registry record
  is fresh, available, appropriate, eligible, or relevant to any person.
- Expert review is still required before stronger public language.
- Source-specific extraction-helper schemas remain future work.
