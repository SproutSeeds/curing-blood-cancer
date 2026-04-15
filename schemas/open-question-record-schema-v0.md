# Open-Question Record Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `open-question-record.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for blood-cancer research questions
- claim level: `open-question`
- boundary: research-use-only, not medical advice

## Purpose

This schema defines a standalone public open-question record shape before any
evidence graph, map builder, extraction helper, review-packet builder, or
generation script depends on question fields.

It is a public research contract only. It is not an evidence-strength ranking,
not clinical priority, not urgency guidance, not a patient-relevance record,
not an actionability record, not treatment guidance, not trial guidance, and
not expanded-access guidance.

## Files

- [Open-Question Record JSON Schema](./open-question-record.schema.json)
- [Open-Question Record Template v0](./open-question-record-template-v0.json)

## Required Record Shape

Every open-question record must include:

| Field | Purpose |
| --- | --- |
| `open_question_record_id` | Stable public open-question record ID. |
| `date` | Public record date. |
| `title` | Human-readable record title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `disease_scope` | Disease, subtype, disease-state, and excluded-scope notes. |
| `question_text` | Public research question text. |
| `question_type` | Question category such as target, therapy, trial-landscape, measurement, mechanism, review-readiness, source-coverage, schema-tooling, case-to-cure-boundary, or tooling-readiness. |
| `question_context` | Public summary and optional non-clinical question fields. |
| `claim_level` | Record claim level. |
| `source_ids` | Public source registry IDs. |
| `uncertainty` | Summary and known unknowns. |
| `limitations` | What the record does not prove or authorize. |
| `do_not_infer` | Explicit overclaiming guardrails. |
| `clinical_use_boundary` | Non-clinical use boundaries. |
| `review` | Creation, review status, and review notes. |

## Allowed Links

Open-question records may link to:

| Link Field | Allowed Use | Not Allowed |
| --- | --- | --- |
| `target_record_ids` | Public target-context linkage. | Targetability, patient expression, or actionability. |
| `therapy_record_ids` | Public therapy-context linkage. | Treatment selection, sequencing, or option ranking. |
| `trial_landscape_record_ids` | Public registry-landscape linkage. | Eligibility, availability, enrollment advice, or trial recommendation. |
| `linked_claim_ids` | Public claim context. | Proof that the question is resolved or clinically important. |
| `linked_gap_ids` | Evidence-gap provenance. | Priority, urgency, or evidence strength. |
| `mechanism_group_ids` | Mechanism-map grouping. | Mechanism frequency or patient relevance. |
| `measurement_term_ids` | Measurement-context linkage. | Monitoring guidance or patient-specific interpretation. |
| `public_task_ids` | Contribution tasks. | Clinical importance by task priority. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add patient-specific candidate options, treatment choices, trial
  choices, clinical priorities, evidence-strength rankings, urgency guidance,
  patient relevance, actionability scores, eligibility guidance, enrollment
  advice, availability claims for any person, or expanded-access guidance.
- Do not use a valid open-question record as proof that a question is clinically
  important, urgent, resolved, actionable, patient-relevant, or higher evidence
  than another question.
- Do not build evidence graph, map-builder, extraction-helper, review-packet,
  or generation tooling until open-question records validate against this
  schema and a separate tooling readiness gate names the first safe slice.

## Validation

The public validator checks any JSON document with
`open_question_record_id` against `schemas/open-question-record.schema.json`.

The validator also rejects common clinical-use fields such as clinical
priority, evidence-strength scoring, urgency, patient relevance, actionability,
candidate options, treatment choice, trial choice, trial matching, expanded
access, real case data, and patient identifiers.

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated question list and should not be treated as
evidence.

## Limitations

- Schema validation checks shape, not truth.
- Source IDs show where a record points, not whether a question is well-framed,
  important, urgent, actionable, expert-reviewed, or answerable.
- Expert review is still required before stronger public language.
- Tooling should wait for a separate readiness gate after this shape validates.
