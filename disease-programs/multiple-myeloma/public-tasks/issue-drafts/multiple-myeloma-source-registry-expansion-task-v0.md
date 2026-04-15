# Expand Reusable Myeloma Source Registry Anchors

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The first open research map and future tooling need reusable source IDs before
they can cite target, therapy, trial, regulatory, and dataset sources without
ad hoc references.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`
- `seer_cancer_stat_facts`

## Linked Public Artifacts

- `source-registry-v0`
- `multiple-myeloma-public-roadmap-v0`
- `clinicaltrials-gov-query-protocol-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

Current public deliverable:

- [Source Registry v0](../../../../sources/source-registry-v0.md), expanded
  with reusable target, therapy, trial, regulatory, labeling, and dataset
  source anchors.

## Deliverables

- Add or revise public source registry records for target, therapy, trial,
  regulatory, and dataset source classes.
- Keep Markdown and JSON source registry views aligned.
- Add claim-use and claim-limit text for each source class.

## Acceptance Checks

- `make validate` passes.
- Each source record has owner, source type, blood-cancer scope, claim uses,
  claim limits, URL, and access date.
- Sources are public and do not require credentials, paid access, account
  changes, or restricted datasets.
- Claim limits state what the source cannot prove.
- Completed in public artifact `source-registry-v0`.

## Do Not Infer

- Do not treat source presence as proof of evidence quality.
- Do not infer approval, efficacy, availability, eligibility, or safety from
  registry presence alone.
- Do not add private or restricted source dependencies.
