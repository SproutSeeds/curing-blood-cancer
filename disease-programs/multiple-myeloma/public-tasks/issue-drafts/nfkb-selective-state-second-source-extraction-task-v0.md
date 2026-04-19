# Add A Second Public Source Extraction For NF-kB Selective State

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot has one NF-kB selective-state signal. A second source is
needed before the pathway-state node can be compared or used in expert-review
questions.

## Public Source Anchors

- `pubmed`
- `pubmed_cui_2024_mrd_clonal_evolution`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `nfkb-selective-state-v0`.
- Preserve pathway-state context, selective-cell context, and assay method.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports NF-kB pathway state in a relevant myeloma
  resistance or residual disease context.
- Pathway-state language is not converted into drug-target guidance.

## Do Not Infer

- Do not recommend targeting NF-kB.
- Do not rank NF-kB against other pathway states from this queue.
- Do not infer patient-specific biology from pathway-state extraction.
