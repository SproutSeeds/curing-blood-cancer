# Inventory The Downstream Schema And Tooling Phase

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, expanded-access guidance, patient-specific
prioritization, or a cure claim.

## Why This Matters

The current v0 mechanism extraction queue has no ready tasks and no
under-covered buckets for v0 navigation. The roadmap still says generation
scripts and tooling must wait for validated shapes. This task creates the
phase inventory that decides which target, therapy, trial, open-question,
public-task, or tooling schema slice should come next.

Status update: completed in
`multiple-myeloma-schema-tooling-phase-inventory-v0`. The inventory selects
`multiple-myeloma-target-record-schema-task-v0` as the next ready validated
shape task.

## Public Source Anchors

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `fda_drugs_at_fda`
- `dailymed`
- `ema_medicines`
- `who_ictrp_search_portal`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`
- `pubmed`

## Linked Public Artifacts

- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `disease-map-schema-v0`
- `public-task-queue.schema.json`
- `source-registry-v0`
- `post-car-t-relapse-mechanism-coverage-v0`

## Deliverables

- Add a public phase inventory that lists candidate next schema or tooling
  slices.
- Separate ready schema slices from blocked, deferred, and needs-human review
  work.
- Recommend one next validated shape before any evidence graph, trial
  explorer, target prioritization, extraction helper, or review-packet builder
  is created.
- Update roadmap or open-research-map navigation so the next phase is explicit.

## Acceptance Checks

- `make validate` passes.
- The inventory states which schema slices already exist and which are missing.
- The inventory does not add generation scripts or extract new biomedical
  claims.
- Each next-phase candidate lists source IDs, public safety boundary, and
  blocker status.
- The selected next task remains research-use-only and cannot be interpreted
  as clinical prioritization.
- Completed in `multiple-myeloma-schema-tooling-phase-inventory-v0`.

## Do Not Infer

- Do not infer that a ready schema task is evidence strength, biological
  priority, patient relevance, or treatment value.
- Do not build tooling before the relevant shape is validated.
- Do not create target, therapy, trial, or open-question records that imply
  actionability, availability, eligibility, efficacy, safety, or cure.
