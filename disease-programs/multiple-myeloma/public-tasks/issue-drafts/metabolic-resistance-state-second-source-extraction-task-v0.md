# Add A Second Public Source Extraction For Metabolic Resistance State

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot has one metabolic resistance-state signal. A second source
is needed before metabolism can be compared with other residual-state buckets.

## Public Source Anchors

- `pubmed`
- `pubmed_cui_2024_mrd_clonal_evolution`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `metabolic-resistance-state-v0`.
- Preserve assay method, cell-state context, pathway signal, and posttreatment
  context.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports a metabolic resistance or residual-cell
  metabolic-state signal.
- Metabolism is framed as research extraction context, not intervention
  evidence.

## Do Not Infer

- Do not recommend metabolic interventions.
- Do not infer that a metabolic state is dominant across relapse settings.
- Do not translate pathway signals into clinical actionability without expert
  review.
