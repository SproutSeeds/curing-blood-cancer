# Source Extraction Task: SEMA4A Translation And Safety Context

Stewarded by [frg.earth](https://frg.earth/).

## Issue Form

Use `.github/ISSUE_TEMPLATE/source-extraction-task.yml`.

## Task ID

`sema4a-translation-safety-extraction-task-v0`

## Linked Gap

`alternate-target-clinical-translation-gap-v0`

## Linked Claim

- `low-bcma-density-supports-alternate-target-research-tracking-v0`

## Public Sources

- `pubmed_di_meo_2025_sema4a_low_bcma`

## Task

Separate SEMA4A target-biology evidence from translation and safety evidence:

- tumor antigen density
- normal-tissue reactivity
- model context
- preclinical activity
- clinical translation status
- trial-registry status when available

## Acceptance Checks

- Preclinical activity is not labeled as clinical efficacy.
- Tumor target expression is separate from normal-tissue safety context.
- Trial-readiness claims include registry or protocol context when available.
- `make validate` passes.

## What This Does Not Support

- Does not infer that SEMA4A-directed CAR T therapy works in patients.
- Does not recommend alternate-target interventions.
- Does not establish clinical safety.
