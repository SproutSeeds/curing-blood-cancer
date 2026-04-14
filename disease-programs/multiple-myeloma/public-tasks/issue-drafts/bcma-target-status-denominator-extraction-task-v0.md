# Source Extraction Task: BCMA Target-Status Denominators

Stewarded by [frg.earth](https://frg.earth/).

## Issue Form

Use `.github/ISSUE_TEMPLATE/source-extraction-task.yml`.

## Task ID

`bcma-target-status-denominator-extraction-task-v0`

## Linked Gap

`bcma-escape-frequency-denominator-gap-v0`

## Linked Claims

- `bcma-target-presence-should-be-extracted-v0`
- `tnfrsf17-loss-is-trackable-escape-signal-v0`

## Public Sources

- `pubmed_antigen_escape_bcma_directed_2024`

## Task

Extract denominator-ready fields for BCMA target-status observations:

- cohort denominator
- numerator for target loss, low expression, or target alteration
- BCMA-directed product or class
- prior BCMA exposure
- assay method
- specimen source
- target-assay timing
- relapse state
- paired measurements when available

## Acceptance Checks

- `make validate` passes.
- Extraction records preserve source IDs, mechanism IDs, measurement-term IDs,
  and clinical-use boundary.
- No mechanism-frequency estimate is added unless denominator context is
  explicit.

## What This Does Not Support

- Does not infer that BCMA antigen escape is common or rare.
- Does not compare products.
- Does not recommend therapy sequencing.
- Does not provide patient-specific interpretation.
