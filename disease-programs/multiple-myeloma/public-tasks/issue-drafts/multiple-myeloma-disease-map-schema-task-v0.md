# Define The First Disease-Map Schema And Markdown Shape

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The roadmap calls for schemas before generation scripts. A disease-map schema
lets the project validate source-backed map records before building extraction
helpers or dashboards on top.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_soh_2022_mrd_flow_harmonization`

## Linked Public Artifacts

- `schemas/public-task-queue.schema.json`
- `schemas/mechanism-map.schema.json`
- `schemas/measurement-glossary.schema.json`
- `multiple-myeloma-roadmap-public-task-queue-v0`

Current public deliverable:

- [Disease Map Schema v0](../../../../schemas/disease-map-schema-v0.md), with
  [JSON schema](../../../../schemas/disease-map.schema.json), a
  [template record](../../../../schemas/disease-map-template-v0.json), and
  validator coverage.

## Deliverables

- Add a disease-map JSON schema or a clearly named first validated schema slice.
- Add a companion Markdown shape summary.
- Add validator coverage before any generator uses the shape.
- Link the schema from `schemas/README.md`.

## Acceptance Checks

- `make validate` passes.
- The schema requires disease scope, source IDs, claim level, uncertainty,
  limitations, and clinical-use boundary.
- The schema can reference targets, therapies, trials, open questions, evidence
  gaps, and public tasks.
- The schema does not accept patient-specific features or candidate options.
- Completed in public artifact `disease-map-schema-v0`.

## Do Not Infer

- Do not build generation scripts before the shape is validated.
- Do not include patient-specific fields in public disease-map records.
- Do not flatten MRD, relapse, target status, or trial status into one generic
  evidence field.
