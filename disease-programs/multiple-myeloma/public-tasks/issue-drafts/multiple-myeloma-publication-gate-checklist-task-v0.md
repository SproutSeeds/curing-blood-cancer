# Add A Publication-Gate Checklist For Case-Derived Public Learning

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The public repo can receive only sanitized public learning. A publication gate
should fail closed when privacy, provenance, subtype scope, review status, or
clinical-use boundary is incomplete.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`

## Linked Public Artifacts

- `multiple-myeloma-case-to-cure-pipeline-blueprint-v0`
- `multiple-myeloma-synthetic-case-to-cure-pipeline-v0`
- `docs/private-to-public-workflow.md`
- `governance/PUBLIC_SAFETY.md`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a publication-gate checklist for any case-derived public learning.
- Add fail-closed criteria for privacy, provenance, subtype scope, review
  status, and clinical-use boundary.
- Link the checklist from the case-to-cure blueprint stage gates.

Current public deliverable:

- [Publication-Gate Checklist v0](../../publication-gate-checklist-v0.md)

## Acceptance Checks

- `make validate` passes.
- The checklist blocks PHI, raw records, dates tied to a person, images,
  free-text notes, and re-identification keys.
- The checklist requires source IDs, subtype scope, uncertainty, limitations,
  and review status before publication.
- The checklist distinguishes aggregate learning from patient-specific
  candidate options, monitoring plans, and decisions.
- Completed in public artifact
  `multiple-myeloma-publication-gate-checklist-v0`.

## Do Not Infer

- Do not infer that a public checklist authorizes publication of real case facts
  without private governance.
- Do not downstream patient-specific candidate options or decisions.
- Do not use the public repo as a medical record or clinical decision system.
