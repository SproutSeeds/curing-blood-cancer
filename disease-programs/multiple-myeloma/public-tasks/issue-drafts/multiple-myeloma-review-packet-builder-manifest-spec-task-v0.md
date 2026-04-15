# Define A Review-Packet Builder Input Manifest Spec

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task should create a manifest specification only. It should not build a
review-packet builder, generator, dashboard, explorer, ranking tool, trial
finder, patient matcher, recommendation system, or generated-claim pipeline.

## Why This Matters

The tooling readiness gate selected review-packet builder input manifest
specification as the smallest safe first tooling slice.

A manifest can name public artifact inputs, source IDs, schema IDs, task IDs,
validation outputs, limitations, and review status for a future builder without
generating or rewriting biomedical claims.

Completed in `multiple-myeloma-review-packet-builder-manifest-spec-v0`.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

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

- Add a public review-packet builder input manifest specification.
- Define manifest fields for public artifact IDs, paths, schema IDs, source
  IDs, claim IDs, gap IDs, mechanism IDs, measurement IDs, task IDs,
  validation outputs, limitations, and review status.
- Define validation expectations for a future manifest before any builder code.
- Include boundary language blocking generated claims, ranking, patient
  matching, clinical recommendations, trial guidance, expanded-access guidance,
  publication authorization, and real case data.
- Add catalog, README, roadmap, open research map, and phase inventory links if
  the manifest specification becomes a reusable public protocol artifact.
- Completed deliverable:
  `disease-programs/multiple-myeloma/reviews/review-packet-builder-manifest-spec-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The specification references only public artifacts, public schemas, public
  task queues, public source IDs, and public validation outputs.
- The specification preserves provenance, subtype scope, uncertainty,
  limitations, review status, and no-clinical-use boundaries.
- The specification keeps missing inputs explicit instead of filling or
  generating claims.
- The specification states that manifest validation is not expert review,
  evidence strength, clinical importance, patient relevance, actionability, or
  publication authorization.
- No builder code, generator, dashboard, explorer, ranking tool, trial finder,
  patient matcher, recommendation system, or generated-claim pipeline is added.

## Do Not Infer

- Do not infer that a manifest specification authorizes review-packet-builder
  code.
- Do not infer evidence strength, clinical importance, patient relevance, or
  actionability from manifest inclusion.
- Do not use a manifest for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, or tasks by clinical priority.
