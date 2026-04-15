# Add A Candidate-Option Scoring Rubric With No-Action Safeguards

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The case-to-cure blueprint needs a scoring rubric that can organize review
questions without ranking patient options or issuing instructions.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`

## Linked Public Artifacts

- `multiple-myeloma-case-to-cure-pipeline-blueprint-v0`
- `clinicaltrials-gov-query-protocol-v0`
- `multiple-myeloma-treatment-class-taxonomy-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a rubric that separates standard-care review, trial review,
  expanded-access review, research-only hypotheses, and no-go records.
- Include dimensions for evidence strength, uncertainty, feasibility,
  measurement clarity, review owner, and overclaiming risk.
- Add boundary language stating that scores are not recommendations.

Current public deliverable:

- [Candidate-Option Scoring Rubric v0](../../candidate-option-scoring-rubric-v0.md)

## Acceptance Checks

- `make validate` passes.
- `candidate_type` is required before any score is interpreted.
- Trial-review and expanded-access categories require clinician, site, sponsor,
  and regulatory verification language.
- Research-only and no-go records are first-class outcomes.
- No score is presented as treatment advice, trial advice, or a patient-specific
  ranking.
- Completed in the public artifact
  `multiple-myeloma-candidate-option-scoring-rubric-v0`.

## Do Not Infer

- Do not infer that a higher score means better treatment.
- Do not rank clinical pathways on a single patient-action axis.
- Do not turn hypothesis scores into clinical action.
