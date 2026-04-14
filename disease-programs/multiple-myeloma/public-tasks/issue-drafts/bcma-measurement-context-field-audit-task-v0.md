# Evidence Gap Task: BCMA Measurement-Context Field Audit

Stewarded by [frg.earth](https://frg.earth/).

## Issue Form

Use `.github/ISSUE_TEMPLATE/evidence-gap-task.yml`.

## Task ID

`bcma-measurement-context-field-audit-task-v0`

## Linked Gap

`bcma-measurement-context-completeness-gap-v0`

## Linked Claims

- `bcma-target-presence-should-be-extracted-v0`
- `low-bcma-density-supports-alternate-target-research-tracking-v0`

## Public Sources

- `pubmed_antigen_escape_bcma_directed_2024`
- `pubmed_di_meo_2025_sema4a_low_bcma`

## Task

Audit current BCMA claim and extraction records for missing measurement
context. Identify whether each record captures:

- assay method
- specimen source
- threshold, scoring method, or detection limit
- time point relative to therapy
- paired measurements
- relapse or progression definition
- missing-context notes

## Acceptance Checks

- Missing context is explicitly flagged.
- Measurement terms are not treated as sufficient evidence by themselves.
- Proposed schema or extraction-template changes are source-bounded.
- `make validate` passes.

## What This Does Not Support

- Does not compare target status or antigen density across sources without
  method context.
- Does not infer patient-level actionability.
- Does not recommend testing or treatment.
