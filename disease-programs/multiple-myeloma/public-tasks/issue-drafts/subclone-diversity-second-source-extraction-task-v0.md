# Add A Second Public Source Extraction For Subclone Diversity

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot currently has review-level subclone diversity coverage. A
second extraction, preferably from a primary study, would make this node more
useful for navigation.

## Public Source Anchors

- `pubmed`
- `pubmed_li_2025_single_cell_myeloma_review`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `subclone-diversity-v0`.
- Preserve clone or subclone measurement method, sample context, and
  progression or treatment context.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports subclone diversity or clonal heterogeneity in
  multiple myeloma.
- Review-level context is not treated as a measured denominator unless the
  source provides measurements.

## Do Not Infer

- Do not infer individual prognosis from subclone diversity.
- Do not compare subclone diversity across sources without aligned methods.
- Do not rank subclone diversity as a relapse mechanism from artifact coverage
  alone.
