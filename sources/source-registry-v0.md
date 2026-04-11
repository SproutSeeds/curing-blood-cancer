# Source Registry v0

- registry id: `source-registry-v0`
- date: `2026-04-11`
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
