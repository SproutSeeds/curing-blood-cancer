# Source Registry v0

- registry id: `source-registry-v0`
- date: `2026-04-14`
- scope: public source anchors for Curing Blood Cancer artifacts
- status: initial registry

## Boundary

This registry records public source anchors. It does not endorse any treatment,
rank evidence, or decide what is appropriate for any individual patient.

Use source records as inputs for public artifacts. Do not treat a source record
as a claim by itself.

## Claim-Use Labels

| Label | Meaning |
| --- | --- |
| `overview` | Useful for broad public orientation. |
| `clinical-summary` | Useful for condition and treatment context, especially when written for clinicians. |
| `trial-search` | Useful for finding or filtering trial records. |
| `literature-search` | Useful for locating publications, not for replacing study appraisal. |
| `mechanism-map` | Useful for organizing biological resistance, relapse, or response mechanisms. |
| `regulatory-status` | Useful for checking drug or product approval status. |
| `statistics` | Useful for incidence, mortality, survival, or registry-level population context. |
| `data-reuse` | Useful for public or redistributable data workflows. |

## Records

| Source ID | Owner | Source Type | Blood-Cancer Scope | Claim Uses | Claim Limits |
| --- | --- | --- | --- | --- | --- |
| `acs_blood_cancer_overview` | American Cancer Society | public overview | leukemia, lymphoma, myeloma | `overview` | Not a treatment guideline, trial registry, or primary evidence source. |
| `nci_pdq_myeloma_hp` | National Cancer Institute | health-professional PDQ summary | plasma-cell neoplasms, multiple myeloma | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_aml_hp` | National Cancer Institute | health-professional PDQ summary | adult acute myeloid leukemia | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_all_hp` | National Cancer Institute | health-professional PDQ summary | adult acute lymphoblastic leukemia | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_cll_hp` | National Cancer Institute | health-professional PDQ summary | chronic lymphocytic leukemia | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_cml_hp` | National Cancer Institute | health-professional PDQ summary | chronic myeloid leukemia | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_hodgkin_hp` | National Cancer Institute | health-professional PDQ summary | adult Hodgkin lymphoma | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_nhl_indolent_b_hp` | National Cancer Institute | health-professional PDQ summary | indolent B-cell non-Hodgkin lymphoma | `clinical-summary` | Does not cover every NHL subtype by itself. |
| `nci_pdq_nhl_aggressive_b_hp` | National Cancer Institute | health-professional PDQ summary | aggressive B-cell non-Hodgkin lymphoma | `clinical-summary` | Does not cover every NHL subtype by itself. |
| `nci_pdq_nhl_peripheral_t_hp` | National Cancer Institute | health-professional PDQ summary | peripheral T-cell non-Hodgkin lymphoma | `clinical-summary` | Does not cover every NHL subtype by itself. |
| `nci_pdq_mds_hp` | National Cancer Institute | health-professional PDQ summary | myelodysplastic syndromes | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `nci_pdq_mpn_hp` | National Cancer Institute | health-professional PDQ summary | myeloproliferative neoplasms | `clinical-summary` | Not a formal guideline or patient-specific recommendation. |
| `clinicaltrials_gov` | U.S. National Library of Medicine | trial registry | all blood-cancer subtypes with registered studies | `trial-search` | Trial listings do not prove availability, eligibility, safety, or efficacy. |
| `clinicaltrials_gov_api_v2` | U.S. National Library of Medicine | trial registry API | all blood-cancer subtypes with registered studies | `trial-search`, `data-reuse` | API output is a registry snapshot; trial details, status, eligibility, and site availability still require verification. |
| `pubmed_tedder_bhutani_2025_bcma_resistance` | PubMed-indexed literature | review article | multiple myeloma, BCMA-targeted CAR T-cell therapy, BCMA-targeted bispecific antibodies | `literature-search`, `mechanism-map` | Review article; use for mechanism framing, not patient-specific treatment selection. |
| `pubmed_ledergor_2024_cd4_car_t_exhaustion` | PubMed-indexed literature | research article | multiple myeloma, BCMA-targeted CAR T-cell therapy, T-cell exhaustion | `literature-search`, `mechanism-map` | Study context and cohort details require paper-level appraisal before strong claims. |
| `pubmed_antigen_escape_bcma_directed_2024` | PubMed-indexed literature | research article | multiple myeloma, BCMA-directed therapy, antigen escape | `literature-search`, `mechanism-map` | Mechanism observations should not be generalized beyond the studied context without review. |
| `pubmed_yue_2025_bcma_resistance` | PubMed-indexed literature | review article | multiple myeloma, BCMA-targeted immunotherapy, resistance mechanisms | `literature-search`, `mechanism-map` | Review article; mechanism categories require source-specific extraction before quantitative use. |
| `pubmed_di_meo_2025_sema4a_low_bcma` | PubMed-indexed literature | research article | multiple myeloma, BCMA-low relapse, candidate alternate target | `literature-search`, `mechanism-map` | Preclinical and translational findings do not establish clinical efficacy. |
| `pubmed_plasma_cell_identity_escape_2025` | PubMed-indexed literature | research article | multiple myeloma, anti-BCMA T-cell redirecting therapy, plasma-cell identity escape | `literature-search`, `mechanism-map` | Mechanism findings require source-specific appraisal and should not be treated as clinical guidance. |
| `pubmed` | U.S. National Library of Medicine | literature index | all blood-cancer subtypes | `literature-search` | Indexing a paper does not validate study quality or clinical actionability. |
| `fda_drugs_at_fda` | U.S. Food and Drug Administration | regulatory database | approved drugs and therapeutic biologics | `regulatory-status` | Approval status is not patient-specific appropriateness or comparative effectiveness. |
| `seer_cancer_stat_facts` | National Cancer Institute SEER Program | cancer statistics | selected blood-cancer statistics pages | `statistics` | Population statistics do not predict individual outcome. |

## URL Registry

| Source ID | URL | Accessed |
| --- | --- | --- |
| `acs_blood_cancer_overview` | https://www.cancer.org/cancer/types/blood-cancer.html | 2026-04-11 |
| `nci_pdq_myeloma_hp` | https://www.cancer.gov/types/myeloma/hp/myeloma-treatment-pdq | 2026-04-11 |
| `nci_pdq_aml_hp` | https://www.cancer.gov/types/leukemia/hp/adult-aml-treatment-pdq | 2026-04-11 |
| `nci_pdq_all_hp` | https://www.cancer.gov/types/leukemia/hp/adult-all-treatment-pdq | 2026-04-11 |
| `nci_pdq_cll_hp` | https://www.cancer.gov/types/leukemia/hp/cll-treatment-pdq | 2026-04-11 |
| `nci_pdq_cml_hp` | https://www.cancer.gov/types/leukemia/hp/cml-treatment-pdq | 2026-04-11 |
| `nci_pdq_hodgkin_hp` | https://www.cancer.gov/types/lymphoma/hp/adult-hodgkin-treatment-pdq | 2026-04-11 |
| `nci_pdq_nhl_indolent_b_hp` | https://www.cancer.gov/types/lymphoma/hp/indolent-b-cell-lymphoma-treatment-pdq | 2026-04-11 |
| `nci_pdq_nhl_aggressive_b_hp` | https://www.cancer.gov/types/lymphoma/hp/aggressive-b-cell-lymphoma-treatment-pdq | 2026-04-11 |
| `nci_pdq_nhl_peripheral_t_hp` | https://www.cancer.gov/types/lymphoma/hp/peripheral-t-cell-lymphoma-pdq | 2026-04-11 |
| `nci_pdq_mds_hp` | https://www.cancer.gov/types/myeloproliferative/hp/myelodysplastic-treatment-pdq | 2026-04-11 |
| `nci_pdq_mpn_hp` | https://www.cancer.gov/types/myeloproliferative/hp/myeloproliferative-neoplasms-treatment | 2026-04-11 |
| `clinicaltrials_gov` | https://clinicaltrials.gov/ | 2026-04-11 |
| `clinicaltrials_gov_api_v2` | https://clinicaltrials.gov/data-api/about-api | 2026-04-14 |
| `pubmed_tedder_bhutani_2025_bcma_resistance` | https://pubmed.ncbi.nlm.nih.gov/40710330/ | 2026-04-14 |
| `pubmed_ledergor_2024_cd4_car_t_exhaustion` | https://pubmed.ncbi.nlm.nih.gov/38574299/ | 2026-04-14 |
| `pubmed_antigen_escape_bcma_directed_2024` | https://pubmed.ncbi.nlm.nih.gov/38728378/ | 2026-04-14 |
| `pubmed_yue_2025_bcma_resistance` | https://pubmed.ncbi.nlm.nih.gov/39818472/ | 2026-04-14 |
| `pubmed_di_meo_2025_sema4a_low_bcma` | https://pubmed.ncbi.nlm.nih.gov/41072416/ | 2026-04-14 |
| `pubmed_plasma_cell_identity_escape_2025` | https://pubmed.ncbi.nlm.nih.gov/41415462/ | 2026-04-14 |
| `pubmed` | https://pubmed.ncbi.nlm.nih.gov/ | 2026-04-11 |
| `fda_drugs_at_fda` | https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database | 2026-04-11 |
| `seer_cancer_stat_facts` | https://seer.cancer.gov/statfacts/ | 2026-04-11 |

## Initial Use Policy

- Prefer NCI PDQ health-professional summaries for condition and treatment
  context in public artifacts.
- Prefer ClinicalTrials.gov for trial discovery, then verify specific trial
  status and eligibility before making any claim about availability.
- Prefer PubMed for literature discovery only; appraise the actual paper before
  using it as evidence.
- Prefer FDA sources for approval status, labeling, and regulatory context.
- Prefer ACS and SEER for public-friendly overview and population-level
  statistics.
