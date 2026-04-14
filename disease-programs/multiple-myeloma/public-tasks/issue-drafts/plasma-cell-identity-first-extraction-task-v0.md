# Add The First Public Extraction For Plasma-Cell Identity Or Lineage-State Escape

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, or a cure claim.

## Why This Matters

The public coverage report currently has no extracted signals for plasma-cell
identity or lineage-state escape. The first extraction should make the bucket
usable for public navigation while preserving uncertainty and source scope.

## Public Source Anchors

- `pubmed_plasma_cell_identity_escape_2025`
- `pubmed_di_meo_2025_sema4a_low_bcma`
- `pubmed_yue_2025_bcma_resistance`

## Linked Public Artifacts

- `post-car-t-relapse-mechanism-coverage-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `bcma-antigen-escape-claim-set-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`

## Deliverables

- Add one source-specific mechanism extraction for identity-state escape,
  lineage-state escape, or target-linked phenotype change after anti-BCMA
  therapy.
- Preserve peer-review status, model context, sample pairing, measurement
  method, and target-state scope.
- Separate BCMA-low, BCMA-retained, alternate-target, and identity-state signals
  when the source supports separation.
- Refresh the coverage report after the extraction is accepted.

## Acceptance Checks

- `make validate` passes.
- Preprint or preclinical status is preserved when present in the source
  record.
- Identity-state labels are kept source-specific unless an explicit mapping
  note is added.
- No clinical efficacy or safety claim is inferred from identity-state evidence
  alone.

## Do Not Infer

- Do not infer clinical efficacy for any alternate target.
- Do not treat a preprint or model-system result as clinical guidance.
- Do not claim that lineage-state escape is frequent without denominator-backed
  evidence.
