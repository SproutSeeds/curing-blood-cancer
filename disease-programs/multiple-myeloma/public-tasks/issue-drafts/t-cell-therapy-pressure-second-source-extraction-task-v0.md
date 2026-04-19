# Add A Second Public Source Extraction For T-Cell Therapy Pressure

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot has one treatment-landscape source for T-cell therapy
pressure. A second extraction is needed before therapy-pressure context can be
compared or routed to expert review.

## Public Source Anchors

- `pubmed`
- `pubmed_besliu_2025_evolving_landscape_myeloma`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `t-cell-therapy-pressure-v0`.
- Preserve therapy class, target class, relapse setting, prior exposure, and
  sequencing uncertainty.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports T-cell-directed therapy pressure, target
  sequence, or immune-redirection context.
- Product and target statements remain descriptive and are not converted into
  treatment comparisons.

## Do Not Infer

- Do not recommend CAR T, bispecific antibodies, targets, products, or
  treatment sequences.
- Do not compare BCMA and GPRC5D approaches from this task.
- Do not infer patient-specific trial fit or therapy fit.
