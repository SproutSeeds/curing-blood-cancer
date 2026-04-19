# MRD Resistance Geometry Pilot v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- cure wedge: durable MRD-negative remission and relapse prevention
- artifact status: `source-checked-v0`
- last reviewed: `2026-04-19`
- clinical boundary: research artifact, not medical advice

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a patient-specific MRD interpretation.
- Not a claim that multiple myeloma has been cured.

## Question

Can a flexible geometry map help organize measurable residual disease,
resistance, clonal evolution, therapy pressure, and tumor-microenvironment
biology in multiple myeloma while preserving uncertainty?

## Geometry Template

This pilot uses a dynamic radial vector field.

| Coordinate | Meaning | Guardrail |
| --- | --- | --- |
| `radius` | Evidence-to-action distance. Inner values are closer to source-backed measurement or review-supported clinical context; outer values are farther from action and closer to unresolved research hypotheses. | Outer nodes must not be converted into clinical advice. |
| `theta` | Mechanism domain: tumor clone, resistant state, metabolism, immune or marrow microenvironment, measurement, and therapy pressure. | Domains are research buckets, not rankings. |
| `z` | Disease or treatment phase: diagnosis, post-induction, MRD-negative, MRD-positive, relapse or refractory disease, and post-T-cell-directed therapy. | Phases are source-context markers, not patient timelines. |
| `vector` | Directional pressure or movement, such as induction therapy pressure, immune redirection, clonal selection, or measurement uncertainty. | Vectors describe research hypotheses, not interventions. |
| `tension` | Uncertainty that must remain visible before a claim is upgraded. | Tension fields should be reviewed before public education reuse. |

## V0 Nodes

| Node | Domain | Source-Backed Observation | Geometry Placement | Public Use |
| --- | --- | --- | --- | --- |
| `mrd-trajectory-split` | measurement plus clonal response | A 2024 single-cell study reported posttreatment patterns including MRD-negative clonal elimination and MRD-positive clonal stabilization or selection. | inner-to-mid radius; post-induction z layer; vector from induction pressure to residual-state separation | Separate "deep response" from "residual clone state" in research maps. |
| `transcriptional-adaptation` | resistant state | The same study supports tracking transcriptional adaptation alongside genetic evolution. | mid radius; adaptive-state theta; vector toward plasticity | Preserve nongenetic state fields in extraction templates. |
| `metabolic-resistance` | metabolism | The study reported fatty-acid-oxidation enrichment in cycling-resistant plasma cells. | mid radius; metabolism theta; posttreatment z layer | Track metabolism as a research bucket, not a treatment instruction. |
| `nfkb-selective-state` | resistant state | The study reported NF-kB pathway preference in selective plasma cells. | mid radius; resistant-state theta; MRD-positive z layer | Track pathway-state hypotheses with source-specific limits. |
| `genetic-nongenetic-coupling` | tumor clone plus cell state | The study reported a correlation between genetic and transcriptional dynamics. | mid radius; bridge between clone and state domains | Avoid clone-only maps when representing resistance. |
| `tme-shelter-interactions` | marrow and immune microenvironment | The study reported stronger tumor-microenvironment interactions in selective plasma cells. | mid-to-outer radius; microenvironment theta; MRD-positive z layer | Track interaction fields before ranking mechanisms. |
| `subclone-diversity` | tumor clone | A 2025 single-cell review describes dynamic subclonal diversity and genomic instability across myeloma progression. | mid radius; clone theta; multi-phase z span | Keep heterogeneity visible as a structural feature. |
| `single-cell-translation-gap` | measurement and tooling | Reviews emphasize clinical-translation barriers for single-cell technologies, including cost, data complexity, standardization, and ethical considerations. | outer radius; measurement theta; all z layers | Keep implementation readiness separate from biological plausibility. |
| `t-cell-therapy-pressure` | therapy pressure | A 2025 treatment-landscape review describes BCMA- and GPRC5D-directed immune therapies alongside continued relapse and sequencing questions. | mid-to-outer radius; therapy-pressure theta; RRMM and post-T-cell-directed z layers | Represent therapy pressure without recommending sequencing. |
| `unmet-high-risk-context` | disease context | The treatment-landscape review identifies extramedullary disease and plasma cell leukemia as ongoing high-unmet-need contexts. | outer radius; context theta; relapse/RRMM z layer | Mark context modifiers requiring expert review. |

## What This Does Not Prove

- It does not rank mechanisms by frequency or importance.
- It does not choose, compare, or sequence therapies.
- It does not interpret an individual person's MRD result.
- It does not estimate relapse risk.
- It does not recommend CAR T, bispecific antibodies, vaccines, trials, or
  metabolic interventions.
- It does not claim that single-cell profiling is clinically routine.
- It does not claim that multiple myeloma has been cured.

## Source Anchors

- `pubmed_cui_2024_mrd_clonal_evolution`: Cui et al., Clinical Cancer Research, 2024, PMID: 38900040, PMCID: PMC11369626, DOI: 10.1158/1078-0432.CCR-24-0545.
- `pubmed_li_2025_single_cell_myeloma_review`: Li et al., Cancers, 2025, PMID: 40002248, PMCID: PMC11852428, DOI: 10.3390/cancers17040653.
- `pubmed_besliu_2025_evolving_landscape_myeloma`: Besliu et al., Cancers, 2025, PMID: 39941892, PMCID: PMC11817212, DOI: 10.3390/cancers17030525.

## Structured Data

- JSON: [`mrd-resistance-geometry-pilot-v0.json`](mrd-resistance-geometry-pilot-v0.json)
- Metadata: [`mrd-resistance-geometry-pilot-v0.metadata.json`](mrd-resistance-geometry-pilot-v0.metadata.json)

## Source-Specific Extractions

- [`cui-2024-mrd-clonal-evolution-geometry-v0`](extractions/cui-2024-mrd-clonal-evolution-geometry-v0.json): MRD trajectory split, transcriptional adaptation, metabolism, NF-kB state, genetic/nongenetic coupling, and tumor-microenvironment interaction signals.
- [`li-2025-single-cell-myeloma-geometry-v0`](extractions/li-2025-single-cell-myeloma-geometry-v0.json): subclone diversity, tumor-microenvironment context, and single-cell translation-gap signals.
- [`besliu-2025-treatment-landscape-geometry-v0`](extractions/besliu-2025-treatment-landscape-geometry-v0.json): T-cell therapy pressure and unmet high-risk context signals.

## Review Status

This pilot is source-checked, not expert-reviewed.

Before reuse in public education, route it to reviewers with expertise in
multiple myeloma, MRD measurement, single-cell analysis, tumor
microenvironment biology, and immune therapy sequencing.

## Next Work

- Convert nodes into source-specific extraction records.
- Add expert-review questions for each coordinate and tension field.
- Compare this geometry map against a flat mechanism list.
- Keep all patient-specific or case-specific reasoning out of the public stream.
