# Draft Multiple Myeloma Open Research Map v0.1

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, or a cure claim.

## Why This Matters

The roadmap needs a first public navigation surface that connects the wedge,
source registry, measurement glossary, mechanism map, evidence gaps, public
task queues, and review boundaries in one readable place.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov_api_v2`
- `pubmed`
- `fda_drugs_at_fda`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_munshi_2017_mrd_survival_meta_analysis`

## Linked Public Artifacts

- `multiple-myeloma-public-roadmap-v0`
- `multiple-myeloma-durable-mrd-negative-remission-wedge-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Draft `Multiple Myeloma Open Research Map v0.1`.
- Separate facts, derived claims, hypotheses, open questions, and do-not-use
  clinical material.
- Link source-backed sections to source IDs, maps, gaps, task queues, and review
  packet paths.
- Add catalog and README entries.

Current public deliverable:

- [Multiple Myeloma Open Research Map v0.1](../../open-research-map-v0-1.md)
- [Validated JSON companion](../../open-research-map-v0-1.json)

## Acceptance Checks

- `make validate` passes.
- Every map section has source IDs or an explicit missing-extraction note.
- Scope is multiple myeloma and plasma-cell disease, with disease-state limits
  called out where known.
- No section ranks patient options, recommends therapy, recommends a trial, or
  claims a cure.
- Completed in public artifact `multiple-myeloma-open-research-map-v0-1`.
- JSON companion validates against Disease Map Schema v0.

## Do Not Infer

- Do not infer that navigation means clinical actionability.
- Do not treat public artifact coverage as evidence strength.
- Do not imply the map is comprehensive across all myeloma settings.
