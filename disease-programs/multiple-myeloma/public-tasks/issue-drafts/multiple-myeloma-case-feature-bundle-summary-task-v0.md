# Draft A Public-Safe Case-Feature-Bundle Shape Summary

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The case-to-cure blueprint names a private-only `case-feature-bundle`. The
public repo needs a safe shape summary so contributors understand the allowed
structure without uploading real case data.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov_api_v2`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_soh_2022_mrd_flow_harmonization`

## Linked Public Artifacts

- `multiple-myeloma-case-to-cure-pipeline-blueprint-v0`
- `multiple-myeloma-synthetic-case-to-cure-pipeline-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a public-safe summary of private-only case-feature-bundle field groups.
- Add a do-not-upload boundary for real cases, identifiers, free-text notes,
  dates tied to a person, images, and re-identification keys.
- Link the summary from the case-to-cure blueprint if it becomes a standalone
  artifact.

Current public deliverable:

- [Case-Feature Bundle Public Summary v0](../../../../schemas/case-feature-bundle-public-summary-v0.md)

## Acceptance Checks

- `make validate` passes.
- Examples are generic placeholders or synthetic values only.
- The artifact states that real case data belongs only in a governed private
  environment.
- Measurement context, disease-state scope, source provenance, uncertainty, and
  limitations are preserved.
- Completed in the public artifact `case-feature-bundle-public-summary-v0`.

## Do Not Infer

- Do not create a public intake form for real case upload.
- Do not publish rare combinations, exact dates, notes, locations, provider
  names, record IDs, or images.
- Do not imply the public repo can evaluate an individual case.
