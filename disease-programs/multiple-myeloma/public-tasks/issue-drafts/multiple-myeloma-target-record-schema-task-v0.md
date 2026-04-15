# Define A Public Target-Record Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, target
prioritization, or a cure claim.

## Why This Matters

The schema/tooling phase inventory selects target-record schema as the next
validated shape. Target records are already embedded in the disease-map schema,
and public source anchors exist for target naming and context, but no
standalone target-record contract exists yet.

Define that shape before evidence graph, target prioritization, extraction
helper, therapy-record, or trial-landscape work depends on target fields.

## Status

Completed in `target-record-schema-v0`.

## Public Source Anchors

- `hgnc_gene_names`
- `ncbi_gene`
- `nci_cancer_drug_dictionary`
- `nci_pdq_myeloma_hp`
- `pubmed`
- `pubmed_antigen_escape_bcma_directed_2024`
- `pubmed_di_meo_2025_sema4a_low_bcma`

## Linked Public Artifacts

- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `disease-map-schema-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `source-registry-v0`
- `bcma-antigen-escape-claim-set-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`

## Deliverables

- Add `schemas/target-record.schema.json`.
- Add `schemas/target-record-schema-v0.md`.
- Add `schemas/target-record-template-v0.json` with public placeholder values
  only.
- Add validator coverage for records with `target_record_id`.
- Add catalog, README, roadmap, and task links.
- Completed deliverable: `schemas/target-record-schema-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The schema requires target ID, target name or symbol, disease scope, source
  IDs, claim level, uncertainty, limitations, review status, and clinical-use
  boundary.
- The schema can link to claims, gaps, mechanism groups, therapy records, trial
  records, and public tasks without requiring those downstream records to
  exist yet.
- The schema rejects or omits patient-specific target expression, candidate
  options, actionability scores, treatment choices, trial matching, and real
  case data.
- The Markdown companion states that target-record validation checks shape
  only, not targetability, efficacy, safety, eligibility, availability, or
  patient fit.

## Do Not Infer

- Do not infer target actionability from a valid target record.
- Do not infer that a target is expressed in any person.
- Do not rank targets, therapies, trials, or products.
- Do not use the schema for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
