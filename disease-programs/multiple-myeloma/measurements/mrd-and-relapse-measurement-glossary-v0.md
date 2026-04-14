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
- `pubmed_antigen_escape_bcma_directed_2024`
- `pubmed_di_meo_2025_sema4a_low_bcma`

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

## Structured Data

- JSON: [`mrd-and-relapse-measurement-glossary-v0.json`](mrd-and-relapse-measurement-glossary-v0.json)
- Metadata: [`mrd-and-relapse-measurement-glossary-v0.metadata.json`](mrd-and-relapse-measurement-glossary-v0.metadata.json)

## Next Work

- Add disease-state-specific endpoint tables for frontline, relapsed, and
  post-CAR T settings.
- Link each claim set to required measurement terms.
- Add extraction checks that flag MRD claims missing threshold, specimen, or
  time point.
