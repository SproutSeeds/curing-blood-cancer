# Create A Case-Specific Private-Lab Blocker Register

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, monitoring guidance, clinical prioritization, publication
authorization, or a cure claim.

This task may create only a public-safe blocker register that maps remaining
case-specific pipeline work to private-lab tasks or human-gated blockers. It
must not include real case data, private records, patient identifiers, free-text
notes, exact dates tied to a person, images, candidate-option rankings,
treatment recommendations, trial recommendations, expanded-access guidance, or
monitoring instructions.

Completed by [Case-Specific Private-Lab Blocker Register v0](../../case-specific-private-lab-blocker-register-v0.md).

## Why This Matters

The definition-of-complete audit found one unresolved public-loop criterion:
remaining case-specific steps are described across the case-to-cure blueprint,
stage gates, and private-to-public workflow, but they are not yet consolidated
as a public register of private-lab tasks and human-gated blockers.

The register should make the boundary inspectable before anyone builds real
case tooling or downstreams case-derived public learning.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`

## Linked Public Artifacts

- `multiple-myeloma-definition-of-complete-audit-v0`
- `multiple-myeloma-case-to-cure-pipeline-blueprint-v0`
- `multiple-myeloma-synthetic-case-to-cure-pipeline-v0`
- `case-feature-bundle-public-summary-v0`
- `multiple-myeloma-publication-gate-checklist-v0`
- `multiple-myeloma-candidate-option-scoring-rubric-v0`
- `multiple-myeloma-multidisciplinary-review-packet-template-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add `Case-Specific Private-Lab Blocker Register v0` as a public-safe
  protocol or dataset artifact.
- Map each `case_00` through `case_14` stage to:
  - private-only input class
  - human gate or private-lab gate
  - blocker reason
  - allowed public output, if any
  - forbidden public output
  - public-safe successor task or blocked status
- Include metadata, catalog, and README navigation.
- Keep all examples generic or synthetic; do not add fillable real-case fields.

Current public deliverable:

- [Case-Specific Private-Lab Blocker Register v0](../../case-specific-private-lab-blocker-register-v0.md)

## Acceptance Checks

- `make validate` passes.
- Every stage from `case_00` through `case_14` has a private-lab or human-gated
  blocker entry.
- The register distinguishes consent, PHI, source freshness, measurement, lab
  validity, CDS/regulatory, feasibility, safety, and publication gates.
- The register states that clinical, legal, regulatory, sponsor, institutional,
  treating-team, and publication decisions remain outside the public repo.
- The register does not include real case data, patient identifiers, exact
  person-linked dates, notes, images, rare identifying combinations, private
  record paths, or re-identification keys.
- The register does not recommend treatment, trial enrollment, expanded access,
  monitoring, or candidate-option ranking for any person.
- Completed in the public artifact `multiple-myeloma-case-specific-private-lab-blocker-register-v0`.

## Do Not Infer

- Do not infer that a blocker register authorizes real case processing in the
  public repo.
- Do not infer that any private-lab task has been completed.
- Do not infer clinical readiness, expert review, publication authorization,
  trial availability, sponsor access, patient fit, efficacy, safety, or cure
  from a blocker entry.
- Do not use this register for treatment selection, trial selection,
  expanded-access decisions, monitoring decisions, or patient-specific review.
