# Review-Packet Builder Manifest Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- schema id: `review-packet-builder-manifest.schema.json`
- status: `draft-v0`
- disease focus: `multiple myeloma` first, reusable for public review-packet input manifests
- claim level: `open-question`
- boundary: research-use-only, not medical advice
- implementation boundary: schema and manifest template only, no builder code

## Purpose

This schema defines a public review-packet builder input manifest shape before
any review-packet builder code exists.

The manifest shape can list public artifacts, schemas, source IDs, reference
IDs, missing inputs, validation expectations, and safety boundaries for a
future builder. It cannot generate review packets, rewrite claims, rank
evidence, match patients, select trials, recommend therapies, authorize
publication, or ingest private case data.

## Files

- [Review-Packet Builder Manifest JSON Schema](./review-packet-builder-manifest.schema.json)
- [Review-Packet Builder Manifest Template v0](./review-packet-builder-manifest-template-v0.json)

## Required Record Shape

Every review-packet builder manifest record must include:

| Field | Purpose |
| --- | --- |
| `review_packet_builder_manifest_id` | Stable public manifest record ID. |
| `date` | Public record date. |
| `title` | Human-readable manifest title. |
| `disease_program` | Disease-program lane such as `multiple-myeloma`. |
| `manifest_scope` | Disease, subtype, manifest-use, and excluded-scope notes. |
| `packet_type` | Public packet type the manifest targets. |
| `target_packet` | Public packet artifact ID, path, review status, and packet boundary. |
| `artifact_inputs` | Public artifact IDs, paths, metadata paths, class, claim level, review status, required sections, and limitations. |
| `schema_inputs` | Public schema paths, template paths, and validation scope. |
| `claim_level` | Record claim level. |
| `source_ids` | Public source registry IDs. |
| `source_inputs` | Source registry path, source IDs, and source-use boundary. |
| `validation_expectations` | Required checks, fail-closed conditions, and forbidden fields. |
| `missing_inputs` | Explicit blockers and next public tasks instead of generated substitutes. |
| `limitations` | What the manifest record does not prove or authorize. |
| `do_not_infer` | Explicit overclaiming guardrails. |
| `clinical_use_boundary` | Non-clinical use boundaries. |
| `builder_code_boundary` | Required false flags for builder code, generated claims, patient-specific outputs, and publication authorization. |
| `review` | Creation, review status, and review notes. |

## Allowed Links

Manifest records may link to:

| Link Field | Allowed Use | Not Allowed |
| --- | --- | --- |
| `artifact_inputs[].artifact_id` | Public artifact routing. | Evidence strength, publication approval, or expert-review completion. |
| `schema_inputs[].schema_id` | Public schema routing. | Builder-code authorization. |
| `source_ids` and `source_inputs.source_ids` | Provenance anchors. | Efficacy, safety, availability, eligibility, or patient fit. |
| `reference_ids.linked_claim_ids` | Public claim routing. | Claim strengthening or clinical actionability. |
| `reference_ids.linked_gap_ids` | Gap provenance. | Clinical priority. |
| `reference_ids.mechanism_group_ids` | Mechanism-map routing. | Mechanism frequency or patient relevance. |
| `reference_ids.measurement_term_ids` | Measurement-context routing. | Monitoring guidance. |
| `reference_ids.public_task_ids` | Contribution routing. | Task priority as evidence strength. |
| `reference_ids.trial_query_record_ids` | Trial-query provenance. | Trial eligibility or enrollment advice. |
| `reference_ids.extraction_record_ids` | Source-extraction provenance. | Generated claim substitution. |

## Public Safety Rules

- Do not add patient identifiers, raw records, images, dates tied to a person,
  free-text clinical notes, re-identification keys, or real case data.
- Do not add generated biomedical claims, generated public explainers, builder
  outputs, clinical priorities, evidence-strength rankings, urgency guidance,
  patient relevance, actionability scores, candidate options, treatment
  recommendations, trial recommendations, eligibility guidance, enrollment
  advice, availability claims for any person, sponsor-access instructions,
  expanded-access guidance, or publication authorization.
- Do not use a valid manifest as proof that review has happened, evidence is
  stronger, a claim is ready for public education, a builder may run, or any
  person should take an action.

## Validation

The public validator checks any JSON document with
`review_packet_builder_manifest_id` against
`schemas/review-packet-builder-manifest.schema.json`.

The validator also:

- enforces required no-clinical-use boundary values
- rejects duplicate manifest IDs
- verifies artifact input paths and metadata paths exist
- verifies artifact inputs use known artifact IDs
- verifies nested source IDs resolve through the source registry
- requires builder-code, generated-claim, patient-specific-output, and
  publication-authorization flags to be false
- rejects common real-case, generated-claim, ranking, recommendation,
  trial-guidance, expanded-access, publication-authorization, and builder-output
  fields

The template file exists only to exercise the schema and demonstrate the
allowed shape. It is not a generated review packet and should not be treated as
expert review or publication approval.

## Limitations

- Schema validation checks shape, not truth.
- Manifest inclusion does not imply expert review, evidence strength,
  clinical importance, patient relevance, actionability, or publication
  authorization.
- Builder code remains limited to the copied-reference route-table dry-run
  script selected by the aggregate implementation gate; packet assembly and
  generated claims remain blocked.
- The manifest schema does not provide medical advice, diagnostic guidance,
  treatment guidance, trial guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
