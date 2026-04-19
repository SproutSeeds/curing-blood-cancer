# Add A Second Public Source Extraction For Residual Transcriptional Adaptation

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot currently has one source-specific extraction for residual
transcriptional adaptation. A second source is needed before this node can be
compared or used in expert-review routing.

## Public Source Anchors

- `pubmed`
- `pubmed_cui_2024_mrd_clonal_evolution`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `residual-transcriptional-adaptation-v0`.
- Preserve malignant plasma cell state, therapy exposure, assay method, and
  posttreatment timing.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports residual transcriptional adaptation or an
  equivalent source-defined residual-state signal.
- Review-level summaries are not treated as cohort-level measurements unless
  the source provides them.

## Do Not Infer

- Do not infer clinical actionability from transcriptional-state labels.
- Do not rank residual-state mechanisms without aligned source extraction.
- Do not treat scRNA-seq findings as routine clinical decision support.
