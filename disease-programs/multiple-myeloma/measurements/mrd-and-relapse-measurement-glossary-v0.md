# MRD And Relapse Measurement Glossary v0

Stewarded by [frg.earth](https://frg.earth/).

This glossary defines the measurement terms that future public artifacts need
before comparing durable remission, relapse, or cure-oriented signals in
multiple myeloma.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a claim that multiple myeloma has been cured.

## Why This Exists

MRD, relapse, and response terms can sound precise while hiding important
context. Public artifacts should not compare a trial, paper, claim set, or
mechanism map unless the measurement method, specimen, threshold, time point,
and follow-up duration are visible.

## Source Anchors

- `nci_pdq_myeloma_hp`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_munshi_2017_mrd_survival_meta_analysis`
- `pubmed_soh_2022_mrd_flow_harmonization`
- `fda_mrd_cr_endpoint_guidance_2026`
- `pubmed_antigen_escape_bcma_directed_2024`
- `pubmed_di_meo_2025_sema4a_low_bcma`
- `pubmed_wang_2025_bmme_drug_resistance`
- `pubmed_shah_2025_mm_pro_quality`
- `pubmed_yip_2025_spatial_transcriptomics_myeloma`
- `eclinicalmedicine_2026_mrd_petct_concordance`
- `pubmed_kubicki_2025_blood_ms_mrd`

## Core Terms

| Term | Public Use | Do Not Infer |
| --- | --- | --- |
| Measurable residual disease | Use as the umbrella term for highly sensitive residual myeloma measurement. | Do not treat MRD status as a cure claim. |
| MRD negativity | Always pair with method, specimen, threshold, and time point. | Do not read "negative" as "no disease exists anywhere." |
| MRD sensitivity threshold | Record values such as `10^-5` only when the source states the assay threshold. | Do not assume every assay or study used the same threshold. |
| Bone marrow MRD | Record aspirate source, method, sample adequacy, and timing. | Do not assume marrow sampling captures every disease site. |
| Flow cytometry MRD | Record flow method, sensitivity, and analysis approach. | Do not compare across studies without method harmonization. |
| Sequencing MRD | Record sequencing platform or validated equivalent and threshold. | Do not treat sequencing and flow as interchangeable without context. |
| Imaging plus MRD | Use when source combines marrow MRD with imaging response context. | Do not use marrow MRD alone to rule out extramedullary disease. |
| Sustained MRD negativity | Record duration and confirmation interval. | Do not collapse a single MRD-negative time point into sustained negativity. |
| Complete response | Use as a conventional response category when source-defined. | Do not equate complete response with MRD negativity or cure. |
| Stringent complete response | Use only with source-defined criteria. | Do not treat it as deeper than MRD without MRD data. |
| Progression-free survival | Use as a trial or study endpoint with follow-up context. | Do not interpret as patient-specific prognosis. |
| Overall survival | Use as a study endpoint with population and follow-up context. | Do not infer individual survival. |
| Relapse or disease progression | Record the source definition and measurement trigger. | Do not compare relapse claims unless definitions align. |
| Bone marrow target status | Record target name, specimen source, assay method, timing, prior target exposure, and response context. | Do not use target status alone as treatment guidance. |
| Antigen density | Record target name, density unit or scoring method, specimen or model context, and comparator target. | Do not infer clinical efficacy from target density. |
| Soluble BCMA | Record blood assay, timing, paired marrow target status, and therapy sequence. | Do not use soluble BCMA alone for patient-specific interpretation. |
| Normal-tissue reactivity screen | Record target, model system, tissue panel, assay method, and clinical translation status. | Do not treat a preclinical screen as proof of patient safety. |
| Blood mass spectrometry MRD | Record peripheral blood or serum mass-spectrometry assay family, timing, threshold or detection-status language, paired marrow context when source-defined, and limitations. | Do not infer substitution for marrow MRD, prognosis, monitoring action, treatment adaptation, response status, or patient-specific meaning. |
| MRD/PET-CT modality discordance | Preserve paired marrow MRD and PET-CT categories, imaging modality, marrow method/threshold, timing alignment, cohort, and endpoint role when source-defined. | Do not interpret images, infer prognosis, guide monitoring or treatment, rank modalities, or collapse discordance into one disease-state flag. |
| Spatial marrow architecture context | Record biopsy or trephine context, spatial method, cell or niche context, cohort scope, site/sampling limitation, and method boundary. | Do not interpret biopsy, imaging, site-specific disease state, prognosis, treatment selection, or resistance status for a person. |
| Assay/specimen quality | Preserve method lineage, threshold status, sample adequacy, specimen quality, timing alignment, duration/follow-up, and not-reported states before comparison; route failures through the assay/specimen quality checklist. | Do not compare modalities or infer response, prognosis, monitoring, or decisions when quality or timing context is missing. |
| Paired-modality timing context | Record the source-defined timing relationship between residual-disease modalities before using discordance language. | Do not treat paired results as comparable when assessment timing is missing, incompatible, or not source-defined. |
| Residual-disease modality discordance | Use as the visible uncertainty state when residual-disease modalities disagree or paired context is missing. | Do not collapse one modality into global disease status or infer patient-specific meaning, prognosis, treatment response, monitoring action, or modality ranking. |

## Minimum Fields For Future Artifacts

- assay or endpoint name
- specimen source
- assay method
- sensitivity threshold or detection limit
- time point relative to therapy
- confirmation interval when sustained status is claimed
- imaging context when relevant
- population and disease-state scope
- follow-up duration
- source IDs
- measurement-term IDs when a claim set depends on these terms
- modality family and paired-modality state when comparing residual-disease signals
- assay/specimen quality, paired-modality timing alignment, and fail-closed
  quality states before cross-modality comparison

## Structured Data

- JSON: [`mrd-and-relapse-measurement-glossary-v0.json`](mrd-and-relapse-measurement-glossary-v0.json)
- Metadata: [`mrd-and-relapse-measurement-glossary-v0.metadata.json`](mrd-and-relapse-measurement-glossary-v0.metadata.json)

## Endpoint Guardrail

- Use the [MRD Endpoint Language Guardrail Addendum v0](mrd-endpoint-language-guardrail-addendum-v0.md)
  before reusing MRD, complete response, stringent complete response,
  sustained MRD negativity, deep response, relapse, progression, PFS, OS, or
  regulatory endpoint language in downstream artifacts.

## Next Work

Residual-disease modality-discordance extraction now adds blood mass spectrometry MRD, MRD/PET-CT discordance, spatial marrow architecture, assay/specimen quality, paired-modality timing context, and explicit discordance-state terms. The later [Assay Specimen Quality Failure Mode Checklist v0](assay-specimen-quality-failure-mode-checklist-v0.md) turns those quality requirements into fail-closed states, [Measurement State Refusal Fixtures v0](../../../examples/measurement-state-refusal-fixtures-v0.json) pressure-tests those states with synthetic inputs, [Measurement Refusal Output Schema v0](../../../schemas/measurement-refusal-output-schema-v0.md) defines the refused output shape, [Measurement Refusal Output Route Table v0](measurement-refusal-output-route-table-v0.md) routes refused records only as refusal metadata, [Measurement Refusal Validator Skeleton v0](measurement-refusal-validator-skeleton-v0.md) checks the route/report structure without clinical meaning, [Measurement Refusal Negative Safety Fixtures v0](measurement-refusal-negative-safety-fixtures-v0.md) prove those checks fail closed on synthetic bad-route mutations, [Measurement Refusal Wrapper Integration Dry Run v0](measurement-refusal-wrapper-integration-dry-run-v0.md) maps refused outputs to wrapper metadata only, [Measurement Refusal Wrapper Negative Safety Fixtures v0](measurement-refusal-wrapper-negative-safety-fixtures-v0.md) prove unsafe wrapper mutations fail closed, [Measurement Refusal Wrapper State Machine v0](measurement-refusal-wrapper-state-machine-v0.md) makes safe refusal terminal transitions explicit, and [Measurement Refusal Wrapper State Machine Negative Safety Fixtures v0](measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0.md) proves unsafe transition-surface mutations fail closed. These terms are representation boundaries only; they do not authorize interpretation, ranking, monitoring, treatment, prognosis, model output, or cure claims.

- Add disease-state-specific endpoint tables for frontline, relapsed, and
  post-CAR T settings.
- Link each claim set to required measurement terms.
- Audit positive and negative wrapper state-machine coverage without returning
  clinical meaning.
