# Add A Second Public Source Extraction For Genetic And Nongenetic Coupling

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot uses clone and state as separate axes. A second extraction
for genetic/nongenetic coupling tests whether that structure is scientifically
useful beyond one source.

## Public Source Anchors

- `pubmed`
- `pubmed_cui_2024_mrd_clonal_evolution`
- `pubmed_cohen_2021_resistance_single_cell`

## Completion Status

Status: `done`

Completed through:

- `cohen-2021-resistance-single-cell-geometry-v0`
- signal: `cohen-2021-clone-state-coupling-signal-v0`

The task is complete for v0 navigation only. The bucket remains
expert-review-needed before any claim upgrade.

## Deliverables

- Added one source-specific mechanism extraction using the existing extraction
  schema.
- Mapped an extracted signal to `genetic-nongenetic-coupling-v0`.
- Preserved clone inference method, transcriptional-state method, and
  paired-sample context when available.
- Refreshed `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports a link between clone architecture and
  nongenetic or transcriptional state.
- Correlation language is not converted into causal or clinical actionability
  language.

## Do Not Infer

- Do not infer causality from correlation.
- Do not rank genetic versus nongenetic mechanisms from one extraction.
- Do not use this task for patient-specific prognosis or treatment selection.
