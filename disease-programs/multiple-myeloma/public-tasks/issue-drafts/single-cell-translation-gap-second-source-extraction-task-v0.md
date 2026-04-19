# Add A Second Public Source Extraction For The Single-Cell Translation Gap

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot needs a technology-readiness layer so high-resolution
research maps are not mistaken for routine clinical decision support.

## Public Source Anchors

- `pubmed`
- `pubmed_li_2025_single_cell_myeloma_review`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `single-cell-translation-gap-v0`.
- Preserve implementation barriers such as cost, standardization, data
  complexity, clinical workflow, or ethics.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports clinical-translation or implementation-readiness
  limitations for single-cell technologies.
- Implementation barriers remain separate from biological mechanism claims.

## Do Not Infer

- Do not claim single-cell profiling is routine clinical decision support.
- Do not recommend any test or platform.
- Do not treat implementation barriers as evidence against the underlying
  biology.
