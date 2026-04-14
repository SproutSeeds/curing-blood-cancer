# Add The First Public Extraction For Disease Burden, Disease Site, And High-Risk Context

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, or a cure claim.

## Why This Matters

Relapse-mechanism comparison needs disease-state context. The public coverage
report currently has no extraction record for disease burden, disease site, and
high-risk context, so this task adds the first public context extraction.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed_tedder_bhutani_2025_bcma_resistance`

## Linked Public Artifacts

- `post-car-t-relapse-mechanism-coverage-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`

## Deliverables

- Add one public extraction for disease burden, disease site, high-risk,
  prior-therapy, and eligibility-context fields.
- Separate context variables from direct biological relapse mechanisms.
- Preserve the source's definitions for cytogenetic risk, extramedullary
  disease, prior lines of therapy, prior BCMA exposure, and eligibility fields.
- Refresh the coverage report after the extraction is accepted.

## Acceptance Checks

- `make validate` passes.
- Registry fields are labeled as registry context, not proof of efficacy,
  availability, eligibility, or safety.
- Context fields are not treated as causal mechanisms unless the source
  explicitly supports that interpretation.
- No patient-specific risk interpretation is added.

## Do Not Infer

- Do not infer individual risk from public registry or overview fields.
- Do not recommend trials or treatments from eligibility fields.
- Do not rank relapse mechanisms before context extraction is more complete.
