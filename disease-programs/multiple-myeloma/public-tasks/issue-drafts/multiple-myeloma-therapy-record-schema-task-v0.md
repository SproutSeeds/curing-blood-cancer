# Define A Public Therapy-Record Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, therapy
prioritization, dosing guidance, sequencing guidance, or a cure claim.

## Why This Matters

Target Record Schema v0 now defines a public target-context contract. The next
validated shape should define therapy records before evidence graph, therapy
landscape, trial explorer, extraction-helper, or review-packet-builder tooling
depends on therapy fields.

The schema should organize public therapy-class or modality context without
turning therapies into candidate options, recommendations, rankings, or patient
matches.

## Status

Completed in `therapy-record-schema-v0`.

## Public Source Anchors

- `nci_cancer_drug_dictionary`
- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `fda_drugs_at_fda`
- `dailymed`
- `ema_medicines`
- `pubmed`

## Linked Public Artifacts

- `target-record-schema-v0`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `disease-map-schema-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `candidate-option-scoring-rubric-v0`
- `source-registry-v0`

## Deliverables

- Add `schemas/therapy-record.schema.json`.
- Add `schemas/therapy-record-schema-v0.md`.
- Add `schemas/therapy-record-template-v0.json` with public placeholder values
  only.
- Add validator coverage for records with `therapy_record_id`.
- Add catalog, README, roadmap, and task links.
- Completed deliverable: `schemas/therapy-record-schema-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The schema requires therapy ID, therapy class or modality, disease scope,
  source IDs, claim level, uncertainty, limitations, review status, and
  clinical-use boundary.
- The schema can link to target records, claims, gaps, mechanism groups, trial
  records, and public tasks without requiring patient-specific candidate
  options.
- The schema rejects or omits treatment recommendations, option rankings,
  dosing, eligibility, availability claims for any person, expanded-access
  guidance, and real case data.
- The Markdown companion states that therapy-record validation checks shape
  only, not efficacy, safety, availability, eligibility, sequencing, or patient
  fit.

## Do Not Infer

- Do not infer therapy value from a valid therapy record.
- Do not rank therapies, products, trials, or targets.
- Do not use the schema for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not infer that any therapy is available, appropriate, safe, effective, or
  indicated for any person.
