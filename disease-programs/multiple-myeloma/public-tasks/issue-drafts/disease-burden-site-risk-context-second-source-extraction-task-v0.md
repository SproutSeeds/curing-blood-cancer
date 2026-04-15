# Add A Second Public Source Extraction For Disease Burden, Disease Site, And High-Risk Context

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, or a cure claim.

## Why This Matters

The coverage report had first-extraction coverage for disease burden, disease
site, high-risk, prior-therapy, and registry-context fields from
`tedder-bhutani-2025-disease-context-v0`. This task added the second public
source extraction needed for v0 navigation coverage.

Status update: completed with `nci-pdq-2025-disease-context-v0`. The record
uses NCI PDQ as public context-field support only; it does not make a causal
relapse-mechanism claim or clinical guidance claim.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`

## Linked Public Artifacts

- `post-car-t-relapse-mechanism-coverage-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `clinicaltrials-gov-query-protocol-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`
- `nci-pdq-2025-disease-context-v0`

## Deliverables

- Add one source-specific extraction for disease-burden, disease-site,
  high-risk, prior-therapy, or registry-context fields.
- Separate context variables from direct biological relapse mechanisms.
- Preserve source definitions for cytogenetic risk, extramedullary disease,
  prior lines of therapy, prior BCMA exposure, and registry eligibility fields.
- Update the coverage report after the extraction is accepted, or document why
  the selected source only supports field definitions.

## Acceptance Checks

- `make validate` passes.
- The extraction uses the mechanism extraction schema.
- Registry fields are labeled as registry context, not proof of efficacy,
  availability, eligibility, or safety.
- Context fields are not treated as causal mechanisms unless the source
  explicitly supports that interpretation.
- Completed with `nci-pdq-2025-disease-context-v0`; coverage now marks the
  disease-context bucket as `covered-for-v0-navigation`.

## Do Not Infer

- Do not infer patient-specific risk from public registry or overview fields.
- Do not recommend trials or treatments from eligibility fields.
- Do not rank relapse mechanisms from context-field coverage.
