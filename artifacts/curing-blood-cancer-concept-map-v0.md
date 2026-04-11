# Curing Blood Cancer Concept Map v0

- artifact id: `curing-blood-cancer-concept-map-v0`
- date: `2026-04-11`
- artifact class: `map`
- primary audience: researchers, builders, patients, advocates, and funders
- claim level: mixed; each row marks `fact`, `derived`, `hypothesis`, or
  `open-question`

## Boundary

This artifact is public research infrastructure. It is not medical advice, a
diagnostic tool, a treatment recommendation, or a claim that a cure or vaccine
has already been found.

The initiative name, Curing Blood Cancer, is a goal and operating posture. The
artifact's job is to make the path toward that goal more legible: what blood
cancers are, where current intervention classes act, what must be measured, and
what public tooling can help more people contribute responsibly.

## Source Anchors

Canonical source IDs for these and future artifacts live in
[Source Registry v0](../sources/source-registry-v0.md).

- American Cancer Society, blood-cancer overview:
  https://www.cancer.org/cancer/types/blood-cancer.html
- NCI, plasma cell neoplasms / multiple myeloma PDQ:
  https://www.cancer.gov/types/myeloma/hp/myeloma-treatment-pdq
- NCI, adult acute myeloid leukemia PDQ:
  https://www.cancer.gov/types/leukemia/hp/adult-aml-treatment-pdq
- NCI, adult acute lymphoblastic leukemia PDQ:
  https://www.cancer.gov/types/leukemia/hp/adult-all-treatment-pdq
- NCI, chronic lymphocytic leukemia PDQ:
  https://www.cancer.gov/types/leukemia/hp/cll-treatment-pdq
- NCI, chronic myelogenous leukemia PDQ:
  https://www.cancer.gov/types/leukemia/hp/cml-treatment-pdq
- NCI, adult Hodgkin lymphoma PDQ:
  https://www.cancer.gov/types/lymphoma/hp/adult-hodgkin-treatment-pdq
- NCI, adult non-Hodgkin lymphoma PDQ:
  https://www.cancer.gov/types/lymphoma/hp/adult-nhl-treatment-pdq
- NCI, myelodysplastic syndromes PDQ:
  https://www.cancer.gov/types/myeloproliferative/hp/myelodysplastic-treatment-pdq
- NCI, chronic myeloproliferative neoplasms PDQ:
  https://www.cancer.gov/types/myeloproliferative/hp/myeloproliferative-neoplasms-treatment
- ClinicalTrials.gov search surface:
  https://clinicaltrials.gov/

## Disease-Scope Map

| Blood-cancer family | Useful public description | Cure-oriented questions | Claim label |
| --- | --- | --- | --- |
| Leukemias | Blood and bone-marrow cancers commonly organized by acute/chronic behavior and myeloid/lymphoid lineage, including AML, ALL, CLL, and CML. | Which genetic, immune, measurable-residual-disease, and transplant-sensitive subgroups can be driven to durable treatment-free control? | `derived` |
| Lymphomas | Cancers of lymphocytes and the lymphatic system, commonly separated into Hodgkin lymphoma and many non-Hodgkin lymphoma subtypes. | Which subtypes are already curable for many people, which relapse after standard therapy, and where do immune therapies, targeted drugs, vaccines, and cellular therapies change the curve? | `derived` |
| Plasma-cell disorders / myeloma | Plasma-cell neoplasms include multiple myeloma and related conditions. NCI describes multiple myeloma as highly treatable but rarely curable, while some solitary plasmacytomas can be potentially curable. | What combinations, immune targets, minimal-residual-disease strategies, and resistance maps can turn deep response into durable cure? | `fact` + `open-question` |
| Myelodysplastic syndromes | Marrow disorders where blood-cell production is abnormal and can include progression risk toward acute leukemia. | Which molecular and immune states predict transformation, transplant benefit, or disease modification? | `derived` |
| Myeloproliferative neoplasms | Marrow disorders involving overproduction of blood cells, including chronic myeloid and non-CML myeloproliferative diseases. | Which driver mutations, inflammatory circuits, stem-cell reservoirs, and targeted therapies matter for cure rather than control? | `derived` |

## Mechanism Map

| Layer | What To Map | Why It Matters |
| --- | --- | --- |
| Disease identity | exact subtype, lineage, stage, grade, cytogenetics, molecular drivers | Cures are unlikely to be one-size-fits-all across blood cancers. |
| Disease burden | blood counts, marrow involvement, imaging, lymph-node or organ involvement, measurable residual disease | Cure-oriented work needs measurements sensitive enough to detect persistence or relapse. |
| Host context | age, immune status, organ function, infections, prior therapies, transplant fitness | The same intervention can have different risk/benefit profiles in different people. |
| Intervention class | chemotherapy, radiation, targeted therapy, antibody therapy, bispecifics, CAR T, transplant, vaccines, supportive care | Tooling should compare where each class acts and what evidence supports it. |
| Escape and relapse | resistant clones, antigen loss, immune exhaustion, sanctuary sites, stem-cell reservoirs, microenvironment | Durable cure work has to explain failure modes, not only initial response. |
| Public translation | trials, guidelines, approved therapies, datasets, patient-safe explainers, reproducible methods | A public initiative needs artifacts that many people can inspect and improve. |

## Initial Tooling Targets

| Public artifact | Purpose | Status |
| --- | --- | --- |
| Blood-cancer source registry | Keep authoritative source anchors in one place with access dates and scope notes. | `open-question` |
| Subtype taxonomy | Normalize names across leukemia, lymphoma, myeloma, MDS, and MPN artifacts. | `open-question` |
| Trial-search protocol | Help users turn subtype, disease state, location, and constraints into auditable ClinicalTrials.gov searches. | `open-question` |
| Treatment-class taxonomy | Map intervention classes without recommending patient-specific treatment. | `open-question` |
| Cure/vaccine claim schema | Force every claim to carry source, subtype scope, evidence level, and uncertainty. | `derived` |
| Mechanism-to-evidence map | Connect mechanisms, biomarkers, interventions, and relapse modes. | `hypothesis` |

## First Build Sequence

1. Publish this concept map.
2. Build a source registry with one record per authoritative source.
3. Build a multiple-myeloma treatment-class taxonomy as the first subtype test.
4. Build a ClinicalTrials.gov query protocol for blood-cancer artifacts.
5. Build the first schema for cure/vaccine evidence claims.

## Limitations

- This map is a scaffold, not a systematic review.
- It does not rank therapies or trials.
- It does not apply to any individual patient.
- It does not include private or restricted data.
- It will need expert review before being used as a public educational anchor.
