# Create A Schema-Backed Tooling Readiness Gate

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, or a cure claim.

## Why This Matters

Disease Map Schema v0, Target Record Schema v0, Therapy Record Schema v0,
Trial-Landscape Record Schema v0, Open-Question Record Schema v0, and the
public task queue shape now give the myeloma lane enough validated structure to
inspect tooling readiness.

The next aggregate work object should decide whether a smallest safe first
tooling slice exists, without building the tool yet and without turning schema
validity into evidence strength, clinical actionability, trial guidance, or
patient relevance.

Completed in `multiple-myeloma-tooling-readiness-gate-v0`.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `disease-map-schema-v0`
- `target-record-schema-v0`
- `therapy-record-schema-v0`
- `trial-landscape-record-schema-v0`
- `open-question-record-schema-v0`
- `multiple-myeloma-open-research-map-v0-1`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a public tooling readiness gate artifact.
- Map evidence graph, trial explorer, target prioritization, extraction helper,
  and review-packet builder ideas to the validated input schemas they require.
- Include a no-tooling-yet decision table that names one smallest safe first
  tooling slice or records why tooling remains blocked.
- Add catalog, README, roadmap, and open research map links if the gate becomes
  a reusable public protocol artifact.
- Completed deliverable:
  `disease-programs/multiple-myeloma/tooling-readiness-gate-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The gate references the validated disease-map, target-record, therapy-record,
  trial-landscape-record, open-question-record, and public task queue shapes.
- The gate distinguishes schema readiness, source coverage, review readiness,
  and tooling readiness without treating any as clinical actionability.
- The gate either selects one smallest safe public tooling slice or records why
  tooling remains blocked.
- The gate does not build a generator, dashboard, explorer, ranking tool, trial
  finder, patient matcher, or recommendation system.

## Do Not Infer

- Do not infer that schema readiness means tooling should generate biomedical
  claims.
- Do not infer that graph connectivity, task priority, or review readiness is
  evidence strength.
- Do not use a tooling gate for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, or mechanisms by
  clinical priority.
