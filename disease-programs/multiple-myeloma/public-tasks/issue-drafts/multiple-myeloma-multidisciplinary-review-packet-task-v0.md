# Create A Multidisciplinary Multiple Myeloma Review Packet Template

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

Future private case work needs a reusable review packet template that separates
hematology, cellular therapy, pathology, genomics, trial operations,
regulatory, safety, ethics, and communication review without downstreaming real
case facts.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`

## Linked Public Artifacts

- `multiple-myeloma-case-to-cure-pipeline-blueprint-v0`
- `bcma-claim-set-expert-review-packet-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a reusable multidisciplinary myeloma review packet template.
- Include sections for reviewer role, source IDs, uncertainty, limitations,
  required confirmations, and blocked/open questions.
- Add a do-not-fill-publicly boundary for real case facts.

Current public deliverable:

- [Multidisciplinary Review Packet Template v0](../../reviews/multidisciplinary-review-packet-template-v0.md)

## Acceptance Checks

- `make validate` passes.
- The template contains no real case data.
- Review status separates source-checked, expert-review-needed,
  expert-reviewed, and blocked states.
- The template does not recommend treatment, trial enrollment, or expanded
  access for any person.
- Completed in public artifact
  `multiple-myeloma-multidisciplinary-review-packet-template-v0`.

## Do Not Infer

- Do not infer expert review has occurred because a template exists.
- Do not fill the public template with real case facts.
- Do not treat review prompts as medical advice.
