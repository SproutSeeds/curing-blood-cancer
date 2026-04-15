# Disease Map Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `disease-map.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for blood-cancer maps
- claim level: `open-question`
- boundary: research-use-only, not medical advice

## Purpose

This schema defines the first validated public shape for disease-map records.
It lets future map builders connect disease scope, sources, facts, derived
claims, hypotheses, open questions, targets, therapies, trials, evidence gaps,
and public tasks without inventing a new JSON contract for each map.

The schema is a public research contract only. It is not a generator, not a
patient intake format, not a clinical decision aid, not a trial-matching record,
and not a place to publish case-derived private features.

## Files

- [Disease Map JSON Schema](./disease-map.schema.json)
- [Disease Map Template v0](./disease-map-template-v0.json)

## Required Record Shape

Every disease-map record must include:

| Field | Purpose |
| --- | --- |
| `disease_map_id` | Stable public map ID. |
| `date` | Public map date. |
| `title` | Human-readable map title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `disease_scope` | Disease and subtype scope. |
| `claim_level` | Overall record claim level. |
| `clinical_use_boundary` | Explicit non-clinical use boundaries. |
| `source_ids` | Public source registry IDs supporting map construction. |
| `uncertainty` | Summary, review status, and known unknowns. |
| `limitations` | What the map does not prove or authorize. |
| `facts` | Source-backed factual statements with scope and limitations. |
| `derived_claims` | Derived claims that still require source IDs and limits. |
| `hypotheses` | Hypotheses separated from facts and claims. |
| `open_questions` | Named research questions with gap and task links. |
| `target_records` | Public target-context records. |
| `therapy_records` | Public therapy-class or modality records. |
| `trial_records` | Public registry or landscape records. |
| `linked_gap_ids` | Evidence-gap IDs that the map touches. |
| `public_task_ids` | Contribution tasks that can improve the map. |
| `review` | Creation, review status, and review notes. |

## Claim Separation

Disease maps must keep these record types separate:

| Record type | Allowed use | Not allowed |
| --- | --- | --- |
| `facts` | Public, source-backed statements with scoped limitations. | Patient relevance, treatment direction, or uncited medical claims. |
| `derived_claims` | Source-linked interpretation that remains reviewable. | Stronger claims than the sources support. |
| `hypotheses` | Research ideas that are explicitly uncertain. | Cure claims, therapy ranking, or clinical action. |
| `open_questions` | Named unknowns and contribution targets. | Evidence strength, urgency, or patient importance by priority alone. |
| `target_records` | Public target naming, source, and gap linkage. | Targetability, expression in a person, or clinical actionability. |
| `therapy_records` | Public therapy-class organization and source linkage. | Treatment recommendation or option ranking. |
| `trial_records` | Registry landscape or query-protocol linkage. | Eligibility, availability, enrollment advice, or trial recommendation. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add candidate-option records or patient-specific option rankings.
- Do not flatten MRD status, relapse status, target status, trial status, and
  review status into a generic evidence field.
- Do not use a valid disease-map record as proof that any claim is true.
- Do not build generation scripts until records validate against this schema.

## Validation

The public validator checks any JSON document with `disease_map_id` against
`schemas/disease-map.schema.json`.

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated disease map and should not be treated as
evidence.

## Limitations

- Schema validation checks shape, not truth.
- Source IDs show where a record points, not whether the source supports a
  stronger claim.
- Expert review is still required before stronger public language.
- More source-specific extraction rules are needed before map tooling can
  compare coverage across disease lanes.
