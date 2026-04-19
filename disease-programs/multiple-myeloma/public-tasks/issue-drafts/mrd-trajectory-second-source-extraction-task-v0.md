# Add A Second Public Source Extraction For MRD Trajectory Split

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific MRD interpretation, or a
cure claim.

## Completion Status

Completed for v0 by
`martinez-lopez-2020-mrd-dynamics-geometry-v0`.

This draft remains as a provenance record for the completed task. A later MRD
trajectory task should define a new source-specific gap rather than reopening
this completed v0 task.

## Why This Matters

The MRD Resistance Geometry Coverage Report currently has one extraction record
for `mrd-trajectory-split-v0`. A second source-specific extraction is needed
before this bucket can be compared across public sources.

## Public Source Anchors

- `pubmed`
- `pubmed_cui_2024_mrd_clonal_evolution`
- `pubmed_martinez_lopez_2020_mrd_dynamics`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `mrd-trajectory-split-v0`.
- Preserve MRD method, specimen, threshold, time point, and paired-sample
  context when available.
- Refresh `mrd-resistance-geometry-coverage-v0` after the extraction is
  accepted.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- Any new source is added to the public source registry before use.
- MRD trajectory language remains source-specific.
- Coverage counts are described only as public artifact coverage.

## Do Not Infer

- Do not infer relapse risk from MRD trajectory labels.
- Do not compare MRD assays or thresholds without aligned measurement context.
- Do not recommend treatment changes from MRD trajectory evidence.
