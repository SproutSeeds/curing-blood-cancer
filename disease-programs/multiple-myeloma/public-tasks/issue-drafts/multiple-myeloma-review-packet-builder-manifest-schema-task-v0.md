# Define A Validated Review-Packet Builder Manifest Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task should create the manifest schema and placeholder template only. It
should not build a review-packet builder, generator, dashboard, explorer,
ranking tool, trial finder, patient matcher, recommendation system, or
generated-claim pipeline.

## Why This Matters

The review-packet builder input manifest specification defines the fields and
fail-closed validation expectations needed before any future builder code.

The next finite endpoint is a validated manifest contract: a JSON schema,
template record, Markdown companion, and validator coverage for records with
`review_packet_builder_manifest_id`.

## Status

Completed by [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md).
The next public-safe endpoint is
`multiple-myeloma-review-packet-builder-dry-run-plan-task-v0`.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `multiple-myeloma-review-packet-builder-manifest-spec-v0`
- `multiple-myeloma-tooling-readiness-gate-v0`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `disease-map-schema-v0`
- `target-record-schema-v0`
- `therapy-record-schema-v0`
- `trial-landscape-record-schema-v0`
- `open-question-record-schema-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`
- `multiple-myeloma-multidisciplinary-review-packet-template-v0`

## Deliverables

- Add `schemas/review-packet-builder-manifest.schema.json`.
- Add `schemas/review-packet-builder-manifest-schema-v0.md`.
- Add `schemas/review-packet-builder-manifest-template-v0.json` with public
  placeholder values only.
- Add validator coverage for records with
  `review_packet_builder_manifest_id`.
- Add catalog, README, roadmap, open research map, and phase inventory links.

## Acceptance Checks

- `make validate` passes.
- The schema requires manifest ID, packet type, target packet, public artifact
  inputs, source IDs, limitations, review status, missing-input handling, and
  clinical-use boundary fields.
- The schema can link public artifact IDs, paths, metadata paths, schema IDs,
  source IDs, claim IDs, gap IDs, mechanism IDs, measurement IDs, task IDs,
  query-record IDs, and extraction-record IDs without requiring generated text.
- The validator rejects patient identifiers, real case data, generated
  biomedical claims, treatment recommendations, trial recommendations,
  expanded-access guidance, publication authorization, rankings, clinical
  priority, urgency, and patient relevance fields.
- No builder code, generator, dashboard, explorer, ranking tool, trial finder,
  patient matcher, recommendation system, or generated-claim pipeline is added.

## Do Not Infer

- Do not infer that a validated manifest schema authorizes
  review-packet-builder code.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from manifest
  validation.
- Do not use manifest records for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
