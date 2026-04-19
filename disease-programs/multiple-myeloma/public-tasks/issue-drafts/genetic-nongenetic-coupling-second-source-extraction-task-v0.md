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

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `genetic-nongenetic-coupling-v0`.
- Preserve clone inference method, transcriptional-state method, and
  paired-sample context when available.
- Refresh `mrd-resistance-geometry-coverage-v0`.

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
