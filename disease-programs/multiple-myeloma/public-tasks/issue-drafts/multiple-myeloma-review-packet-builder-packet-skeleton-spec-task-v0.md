# Define A Review-Packet Builder Packet-Skeleton Spec

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task may define only a no-code packet-skeleton specification. It must not
build packet assembly code, generated packet output, generated biomedical
prose, ranking, trial matching, recommendation behavior, publication workflow,
or patient-specific tooling.

Completed by [Review-Packet Builder Packet-Skeleton Spec v0](../../reviews/review-packet-builder-packet-skeleton-spec-v0.md).

## Why This Matters

The packet-assembly gate keeps packet assembly blocked but selects one safe
next step: define a static skeleton shape that can name empty review-packet
section slots and route-table references without filling sections or generating
claims.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `multiple-myeloma-review-packet-builder-packet-assembly-gate-v0`
- `review-packet-route-table-output-schema-v0`
- `review-packet-manifest-route-table-tool-v0`
- `review-packet-builder-manifest-schema-v0`
- `multiple-myeloma-review-packet-builder-dry-run-plan-v0`
- `multiple-myeloma-multidisciplinary-review-packet-template-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a no-code packet-skeleton specification that maps public review-packet
  section labels to route-table references, missing-input slots, and refusal
  states.
- State that skeleton slots are empty and must not be filled with generated
  biomedical prose, case facts, recommendations, rankings, or reviewer
  conclusions.
- Define refusal behavior for patient identifiers, real case data, generated
  claims, treatment/trial recommendations, expanded-access guidance,
  publication authorization, and private records.

## Acceptance Checks

- `make validate` passes.
- The spec references the packet-assembly gate, route-table output schema,
  route-table tool, manifest schema, dry-run plan, and review packet template.
- The spec defines empty section slots only and does not create review-packet
  output.
- The spec preserves route-table IDs, route decisions, review status,
  limitation text, missing-input records, refusal records, and output
  boundaries.
- No packet assembly code, generated packet output, generated prose, clinical
  ranking, trial finder, recommendation system, patient-specific workflow, or
  publication workflow is added.

## Do Not Infer

- Do not infer that a packet skeleton is a review packet.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from skeleton fields.
- Do not use a packet skeleton for treatment selection, trial selection,
  expanded-access decisions, monitoring decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
