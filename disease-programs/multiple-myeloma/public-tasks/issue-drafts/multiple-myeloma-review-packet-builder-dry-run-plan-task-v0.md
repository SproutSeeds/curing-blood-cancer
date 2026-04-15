# Define A No-Code Review-Packet Builder Dry-Run Plan

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task should create a dry-run plan and no-generated-claims policy only. It
should not build a review-packet builder, generator, dashboard, explorer,
ranking tool, trial finder, patient matcher, recommendation system, generated
packet output, or generated-claim pipeline.

## Why This Matters

[Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md)
now validates public input manifests for future review-packet-builder work.
Before code exists, the public project needs a dry-run plan that defines what a
future builder may copy, reference, omit, or refuse without generating or
strengthening biomedical claims.

The next finite endpoint is a no-code dry-run and refusal contract, not
implementation.

## Status

Completed by [Review-Packet Builder Dry-Run Plan v0](../../reviews/review-packet-builder-dry-run-plan-v0.md).
The next public-safe endpoint is
`multiple-myeloma-review-packet-builder-implementation-gate-task-v0`.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `review-packet-builder-manifest-schema-v0`
- `multiple-myeloma-review-packet-builder-manifest-spec-v0`
- `multiple-myeloma-tooling-readiness-gate-v0`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `multiple-myeloma-roadmap-public-task-queue-v0`
- `multiple-myeloma-multidisciplinary-review-packet-template-v0`

## Deliverables

- Add a public no-code dry-run plan for future review-packet-builder behavior.
- Add a no-generated-claims policy for future builder work.
- Define copy, reference, omit, and refuse behavior for public artifact inputs,
  schema inputs, source IDs, limitations, review status, validation outputs,
  and missing inputs.
- Keep all examples public-placeholder only.
- Update catalog, roadmap, readiness gate, task queue, and open research map
  links if the plan becomes a public artifact.

## Acceptance Checks

- `make validate` passes.
- The plan references Review-Packet Builder Manifest Schema v0 and its
  placeholder manifest as the only manifest inputs.
- The plan states that future builder work may copy existing public artifact
  references and metadata but must not generate, rewrite, rank, summarize as
  advice, or strengthen biomedical claims.
- The plan separates allowed copy, allowed reference, required omission, and
  hard refusal behavior for missing or unsafe inputs.
- No builder code, generator, dashboard, explorer, ranking tool, trial finder,
  patient matcher, recommendation system, generated packet output, or
  generated-claim pipeline is added.

## Do Not Infer

- Do not infer that a dry-run plan authorizes review-packet-builder code.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from manifest
  validation or dry-run planning.
- Do not use dry-run examples for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
