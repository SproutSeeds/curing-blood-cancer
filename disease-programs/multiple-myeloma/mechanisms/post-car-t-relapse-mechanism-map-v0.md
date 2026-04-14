# Post-CAR T Relapse Mechanism Map v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- cure wedge: durable MRD-negative remission and relapse prevention
- artifact status: `source-checked-v0`
- last reviewed: `2026-04-14`
- clinical boundary: research artifact, not medical advice

## Question

When multiple myeloma relapses after a deep response to CAR T-cell therapy,
which mechanism buckets should public tooling track first?

## Why This Matters

Durable remission work needs a failure map. A treatment can produce deep
responses while still failing to produce cure-like durability if relapse is
driven by target escape, impaired CAR T persistence, hostile immune context,
baseline disease state, or measurement gaps.

This map turns that problem into public extraction fields.

## Initial Mechanism Buckets

| Bucket | Working Role | What To Extract Next |
| --- | --- | --- |
| BCMA antigen loss, low density, or target alteration | Tumor cells may become harder for BCMA-directed cells to recognize. | BCMA expression, genetic alteration, soluble BCMA, assay type, timing before and after relapse |
| CAR T fitness, exhaustion, expansion, or persistence | The therapeutic T-cell product may fail to expand, persist, or remain functional enough for durable control. | expansion kinetics, persistence duration, exhaustion markers, phenotype, manufacturing context |
| Plasma-cell identity or lineage-state escape | Myeloma cells may shift phenotype or state while evading targeted immune pressure. | plasma-cell marker changes, transcriptional state, clonal evolution, retained or lost BCMA |
| Disease burden, site, and high-risk context | Baseline tumor and patient context may shape response depth and relapse timing. | tumor burden, extramedullary disease, cytogenetic risk, prior therapy exposure |
| Sequential or dual-target immune pressure | Prior BCMA exposure and next-target strategies may change the relapse landscape. | target sequence, prior BCMA-directed therapy, alternate targets, dual-target trial design |
| Measurement and follow-up gaps | Relapse interpretation is weak when sampling, timing, or MRD methods are inconsistent. | MRD method, imaging, marrow sampling, blood markers, follow-up interval |

## What This Does Not Prove

- It does not estimate how common each mechanism is.
- It does not compare CAR T products.
- It does not recommend CAR T, bispecifics, vaccines, trials, or sequencing.
- It does not determine whether any individual should receive a treatment.
- It does not claim that a cure has been found.

## Next Public Artifacts

1. `post-car-t-relapse-extraction-template-v0`
2. `bcma-antigen-escape-claim-set-v0`
3. `mrd-and-relapse-measurement-glossary-v0`

## Source Anchors

This v0 map uses the public source registry records:

- `nci_pdq_myeloma_hp`
- `pubmed_tedder_bhutani_2025_bcma_resistance`
- `pubmed_ledergor_2024_cd4_car_t_exhaustion`
- `pubmed_antigen_escape_bcma_directed_2024`
- `pubmed_yue_2025_bcma_resistance`
- `pubmed_di_meo_2025_sema4a_low_bcma`
- `pubmed_plasma_cell_identity_escape_2025`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `fda_drugs_at_fda`

