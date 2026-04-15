# Add A Second Public Source Extraction For Plasma-Cell Identity Or Lineage-State Escape

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, or a cure claim.

## Why This Matters

The coverage report has first-extraction coverage for plasma-cell identity or
lineage-state escape from `maura-2025-plasma-cell-identity-escape-v0`, but the
bucket remains single-source. A second public source extraction is needed before
the map compares identity or lineage-state coverage across sources.

## Public Source Anchors

- `pubmed_di_meo_2025_sema4a_low_bcma`
- `pubmed_yue_2025_bcma_resistance`

## Linked Public Artifacts

- `di-meo-2025-target-linked-phenotype-v0`
- `post-car-t-relapse-mechanism-coverage-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `bcma-antigen-escape-claim-set-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`

## Deliverables

- Add one source-specific extraction for plasma-cell identity, lineage-state
  escape, or target-linked phenotype change.
- Preserve source-defined identity labels, peer-review status, model or sample
  context, and measurement method.
- Update the coverage report after the extraction is accepted, or document why
  the selected source does not support this bucket.

## Acceptance Checks

- `make validate` passes.
- The extraction uses the mechanism extraction schema.
- BCMA-low, BCMA-retained, alternate-target, and lineage-state signals are
  separated only when the source supports separation.
- Coverage counts remain artifact coverage, not mechanism frequency, biological
  priority, product comparison, or clinical relevance.
- Completed with `di-meo-2025-target-linked-phenotype-v0`; the extraction is
  target-linked phenotype-field coverage, not a harmonized lineage-state
  ontology.

## Do Not Infer

- Do not infer clinical efficacy for any alternate target from identity-state
  evidence alone.
- Do not treat preclinical, review, or preprint framing as clinical guidance.
- Do not compare mechanisms across sources until extraction fields are aligned
  and reviewed.
