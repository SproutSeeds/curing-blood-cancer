# Create A Review-Packet Builder Packet-Assembly Gate

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task may create only a no-code aggregate gate before any review-packet
output or packet assembly. It must not build packet assembly code, generated
packet output, generated biomedical prose, ranking, trial matching,
recommendation behavior, publication workflow, or patient-specific tooling.

Completed by [Review-Packet Builder Packet-Assembly Gate v0](../../reviews/review-packet-builder-packet-assembly-gate-v0.md).

## Why This Matters

The review-packet lane now has a manifest schema, a copied-reference
route-table dry-run tool, a route-table output schema, and validator coverage.
Before any downstream workflow attempts packet assembly, the public repo needs
an aggregate gate that decides whether packet assembly remains blocked or
whether one smallest safe downstream slice can be selected.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `review-packet-builder-manifest-schema-v0`
- `review-packet-manifest-route-table-tool-v0`
- `review-packet-route-table-output-schema-v0`
- `multiple-myeloma-review-packet-builder-dry-run-plan-v0`
- `multiple-myeloma-review-packet-builder-implementation-gate-v0`
- `multiple-myeloma-tooling-readiness-gate-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a no-code packet-assembly gate that reviews the validated manifest,
  route-table tool, route-table output schema, fixtures, and dry-run policy.
- State whether packet assembly remains blocked or one smallest safe downstream
  slice is selected.
- Include a boundary table that keeps generated biomedical prose,
  recommendations, rankings, patient-specific output, trial matching,
  expanded-access guidance, and publication workflow blocked.

## Acceptance Checks

- `make validate` passes.
- The gate references Review-Packet Builder Manifest Schema v0,
  Review-Packet Manifest Route-Table Dry-Run Tool v0, Review-Packet
  Route-Table Output Schema v0, and Review-Packet Builder Dry-Run Plan v0.
- The gate states whether packet assembly remains blocked or a smallest safe
  downstream slice is selected.
- The gate does not add packet assembly code, generated packet output,
  generated biomedical claims, ranking behavior, trial matching,
  recommendation behavior, patient-specific interpretation, or publication
  workflow.
- If a future code slice is selected, it is limited to deterministic copied
  public identifiers, public paths, boundary text, validation status, and
  explicit missing-input or refusal records.

## Do Not Infer

- Do not infer that a packet-assembly gate authorizes clinical use.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from route-table
  readiness.
- Do not use readiness-gate outputs for treatment selection, trial selection,
  expanded-access decisions, monitoring decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
