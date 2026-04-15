# Define A Public Open-Question Record Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, urgency guidance, clinical prioritization, or a cure claim.

## Why This Matters

Target Record Schema v0, Therapy Record Schema v0, and Trial-Landscape Record
Schema v0 now define public target, therapy, and trial-landscape contracts.
The next validated shape should define standalone open-question records before
evidence graph, map-builder, extraction-helper, or review-packet-builder
tooling depends on question fields.

The schema should organize public research questions without turning question
records into evidence-strength rankings, clinical priority lists, patient
relevance claims, or actionability claims.

Completed in `open-question-record-schema-v0`.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `target-record-schema-v0`
- `therapy-record-schema-v0`
- `trial-landscape-record-schema-v0`
- `disease-map-schema-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`

## Deliverables

- Add `schemas/open-question-record.schema.json`.
- Add `schemas/open-question-record-schema-v0.md`.
- Add `schemas/open-question-record-template-v0.json` with public placeholder
  values only.
- Add validator coverage for records with `open_question_record_id`.
- Add catalog, README, roadmap, and task links.
- Completed deliverable: `schemas/open-question-record-schema-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The schema requires open-question ID, question text, question type, disease
  scope, source IDs, uncertainty, limitations, review status, and clinical-use
  boundary.
- The schema can link to target records, therapy records, trial-landscape
  records, claims, gaps, mechanism groups, and public tasks without requiring
  clinical priority, urgency, or patient-specific fields.
- The schema rejects or omits clinical priority, evidence-strength ranking,
  urgency, treatment recommendations, trial recommendations, expanded-access
  guidance, and real case data.
- The Markdown companion states that open-question validation checks shape
  only, not evidence strength, clinical importance, patient relevance, or
  actionability.

## Do Not Infer

- Do not infer that an open question is clinically urgent because it validates.
- Do not infer evidence strength, patient relevance, or actionability from an
  open-question record.
- Do not use open-question records for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, or targets by clinical
  priority.
