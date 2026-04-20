# Source Registry v0

- registry id: `source-registry-v0`
- date: `2026-04-19`
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
| `context-modifier` | Useful for source-defined disease-state, organ, frailty, functional, or host-context fields without patient-specific decision logic. |
| `regulatory-status` | Useful for checking drug or product approval status. |
| `regulatory-context` | Useful for public regulatory endpoint, guidance, and review-context language without implying product status or clinical use. |
| `statistics` | Useful for incidence, mortality, survival, or registry-level population context. |
| `data-reuse` | Useful for public or redistributable data workflows. |
| `measurement-standard` | Useful for response, MRD, assay, and endpoint definitions. |
| `target-reference` | Useful for gene, protein, antigen, or target identifier normalization. |
| `nomenclature` | Useful for stable symbols, names, and cross-references. |
| `therapy-reference` | Useful for drug, agent, class, and synonym normalization. |
| `precursor-risk-context` | Useful for source-defined precursor-state and cohort-level risk-model context without personal risk calculation. |
| `trial-registry-aggregate` | Useful for cross-registry trial discovery. |
| `labeling` | Useful for public product-label review. |
| `dataset-discovery` | Useful for locating public datasets before appraisal. |
| `genomics-data` | Useful for cancer genomics data discovery and cohort-level analysis planning. |
| `machine-representation` | Useful for architecture and schema decisions about machine-readable disease-state representations without patient-specific decision logic. |

## Records

| Source ID | Owner | Source Type | Blood-Cancer Scope | Claim Uses | Claim Limits |
| --- | --- | --- | --- | --- | --- |
| `acs_blood_cancer_overview` | American Cancer Society | public overview | leukemia, lymphoma, myeloma | `overview` | Not a treatment guideline, trial registry, or primary evidence source. |
| `nci_pdq_myeloma_hp` | National Cancer Institute | health-professional PDQ summary | plasma-cell neoplasms, multiple myeloma, MGUS, smoldering multiple myeloma | `clinical-summary`, `precursor-risk-context`, `context-modifier` | Not a formal guideline, screening recommendation, personal risk calculator, prognosis tool, or patient-specific recommendation. |
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
| `hgnc_gene_names` | HUGO Gene Nomenclature Committee | gene nomenclature database | human gene symbols and names relevant to blood-cancer target records | `target-reference`, `nomenclature`, `data-reuse` | Gene nomenclature and stable IDs do not establish expression, function, targetability, evidence quality, or clinical actionability. |
| `ncbi_gene` | National Center for Biotechnology Information | gene database | genes and mapped phenotypes relevant to blood-cancer target records | `target-reference`, `data-reuse` | Gene records integrate references and cross-links but do not establish target validity, disease relevance, or clinical actionability. |
| `nci_cancer_drug_dictionary` | National Cancer Institute | cancer drug dictionary | cancer drugs and investigational agents | `therapy-reference` | Drug definitions, synonyms, and trial links are not treatment recommendations, approval status, efficacy evidence, safety evidence, or availability claims. |
| `who_ictrp_search_portal` | World Health Organization | clinical trial search portal | global clinical-trial records | `trial-search`, `trial-registry-aggregate` | Aggregated registry presence does not prove eligibility, availability, data quality, safety, efficacy, or local trial status. |
| `dailymed` | U.S. National Library of Medicine | structured product labeling database | drug labels submitted to FDA | `labeling`, `regulatory-status` | Label presence is not a complete listing of FDA-regulated products and does not determine patient-specific appropriateness. |
| `ema_medicines` | European Medicines Agency | medicines regulatory information | centrally authorised or EMA-evaluated medicines | `regulatory-status`, `therapy-reference` | EMA pages may not include nationally authorised medicines or complete treatment options and are not patient-specific guidance. |
| `ncbi_geo` | National Center for Biotechnology Information | functional genomics data repository | public functional genomics datasets, including blood-cancer studies when deposited | `dataset-discovery`, `data-reuse`, `literature-search` | Submitted datasets vary in consent, reuse terms, metadata completeness, and study quality; dataset presence does not establish clinical truth. |
| `nci_gdc_data_portal` | National Cancer Institute Genomic Data Commons | cancer genomics data portal and API | NCI cancer genomics programs and harmonized datasets | `dataset-discovery`, `genomics-data`, `data-reuse` | Some data require controlled access; cohort inclusion and harmonization do not establish patient-specific interpretation or clinical actionability. |
| `dana_farber_car_t_update_2025` | Dana-Farber Cancer Institute | physician clinical resource update | multiple myeloma, CAR T-cell therapy, immune effector therapy | `overview`, `clinical-summary` | Institutional update; use for public research context only, not product status verification, referral advice, eligibility, availability, or treatment sequencing. |
| `pubmed_kumar_2016_imwg_mrd_response_criteria` | PubMed-indexed literature | consensus statement | multiple myeloma, response criteria, minimal residual disease | `literature-search`, `measurement-standard` | Consensus criteria; use for public measurement definitions, not patient-specific interpretation. |
| `pubmed_munshi_2017_mrd_survival_meta_analysis` | PubMed-indexed literature | meta-analysis | multiple myeloma, minimal residual disease, survival outcomes | `literature-search`, `measurement-standard` | Outcome association does not provide patient-specific prognosis or prove a treatment strategy. |
| `pubmed_soh_2022_mrd_flow_harmonization` | PubMed-indexed literature | research article | multiple myeloma, measurable residual disease, flow cytometry | `literature-search`, `measurement-standard`, `data-reuse` | Flow-cytometry harmonization source; does not replace local laboratory validation or clinical interpretation. |
| `pubmed_martinez_lopez_2020_mrd_dynamics` | PubMed-indexed literature / Blood Advances | open-access observational study | multiple myeloma, measurable residual disease, MRD dynamics, serial MRD monitoring, response depth | `literature-search`, `measurement-standard`, `mechanism-map` | Single-institution retrospective MRD dynamics source; use for source-specific extraction only, not patient-specific prognosis, monitoring instructions, treatment selection, or clinical decision support. |
| `pubmed_cohen_2021_resistance_single_cell` | PubMed-indexed literature / Nature Medicine | research article | multiple myeloma, primary refractory multiple myeloma, early relapse, single-cell RNA sequencing, resistance pathways, transcriptional clones | `literature-search`, `mechanism-map`, `genomics-data`, `machine-representation` | Prospective translational-trial source; use for source-specific resistance-state and clone-state extraction only, not patient-specific prognosis, treatment selection, target actionability, monitoring guidance, or cure claims. |
| `fda_mrd_cr_endpoint_guidance_2026` | U.S. Food and Drug Administration | draft guidance | multiple myeloma, minimal residual disease, complete response, accelerated approval endpoints | `measurement-standard`, `regulatory-context` | Draft, nonbinding regulatory context; not for implementation and not a patient-specific interpretation, product approval, availability, eligibility, treatment-selection, or trial-advice source. |
| `nature_genetics_commpass_subtypes_2024` | MMRF CoMMpass Network / Nature Genetics | open-access research article | multiple myeloma, newly diagnosed multiple myeloma, CoMMpass, genomics, transcriptomics, longitudinal clinical data | `literature-search`, `genomics-data`, `dataset-discovery`, `machine-representation` | Cohort-level molecular profiling source; not a patient-specific prognostic model, treatment selector, trial matcher, or clinical decision system. |
| `nature_cancer_immune_atlas_myeloma_2026` | Immune Atlas Consortium / Nature Cancer | open-access research article | multiple myeloma, newly diagnosed multiple myeloma, bone marrow microenvironment, single-cell RNA sequencing, immune atlas | `literature-search`, `genomics-data`, `context-modifier`, `machine-representation` | Cohort-level immune microenvironment source; does not establish patient-specific immune status, prognosis, treatment fit, trial fit, monitoring guidance, or intervention guidance. |
| `nature_genetics_mm_precursor_genomic_landscape_2025` | Nature Genetics | open-access research article | multiple myeloma, MGUS, smoldering multiple myeloma, precursor states, genomic progression | `literature-search`, `genomics-data`, `precursor-risk-context`, `machine-representation` | Cohort-level genomic progression source; not a personal risk calculator, screening recommendation, monitoring instruction, treatment recommendation, or trial recommendation. |
| `nature_communications_rrmm_resistance_2022` | Multiple Myeloma Research Consortium / Nature Communications | open-access research article | multiple myeloma, relapsed refractory multiple myeloma, genetic heterogeneity, drug resistance, relapse biology | `literature-search`, `genomics-data`, `mechanism-map`, `machine-representation` | Relapsed/refractory cohort-level resistance source; mechanism observations must not be used to rank patient options, infer therapy resistance for a person, or guide treatment. |
| `jco_ims_imwg_high_risk_consensus_2025` | International Myeloma Society / International Myeloma Working Group | consensus recommendations | multiple myeloma, newly diagnosed multiple myeloma, high-risk myeloma, genomic staging | `literature-search`, `context-modifier`, `machine-representation` | Consensus genomic staging source; not patient-specific prognostic advice, treatment selection, transplant-fit guidance, trial guidance, or monitoring guidance. |
| `pubmed_high_risk_genomic_consensus_validation_2026` | PubMed-indexed literature / Blood | validation study | multiple myeloma, newly diagnosed multiple myeloma, first relapse, high-risk genomic staging, next-generation sequencing | `literature-search`, `genomics-data`, `context-modifier`, `machine-representation` | Cohort-level validation study; not a patient-specific prognosis tool, treatment selector, trial matcher, or clinical decision system. |
| `pubmed_kyle_2010_mgus_smm_imwg` | PubMed-indexed literature | consensus perspective | multiple myeloma, MGUS, smoldering multiple myeloma, precursor states | `literature-search`, `precursor-risk-context` | Consensus perspective for source extraction; not a personal risk calculator, monitoring instruction, screening recommendation, or treatment recommendation. |
| `pubmed_mateos_2020_smm_risk_model` | Blood Cancer Journal / IMWG | open-access research article | smoldering multiple myeloma, risk stratification, precursor states | `literature-search`, `precursor-risk-context` | Cohort-level risk-model context; does not determine individual prognosis, screening, monitoring, treatment fit, or trial eligibility. |
| `pubmed_palumbo_2015_imwg_frailty` | PubMed-indexed literature | IMWG report | multiple myeloma, frailty, geriatric assessment, host context | `literature-search`, `context-modifier` | Frailty and geriatric-assessment context for source extraction; not a prognosis tool, treatment-fit tool, transplant-fit tool, monitoring instruction, or patient-specific assessment. |
| `pubmed_tedder_bhutani_2025_bcma_resistance` | PubMed-indexed literature | review article | multiple myeloma, BCMA-targeted CAR T-cell therapy, BCMA-targeted bispecific antibodies | `literature-search`, `mechanism-map`, `context-modifier` | Review article; use for mechanism and context-field framing, not patient-specific treatment selection. |
| `pubmed_ledergor_2024_cd4_car_t_exhaustion` | PubMed-indexed literature | research article | multiple myeloma, BCMA-targeted CAR T-cell therapy, T-cell exhaustion | `literature-search`, `mechanism-map`, `therapy-pressure-context` | Study context and cohort details require paper-level appraisal before strong claims; not product comparison, therapy sequencing, patient-specific prognosis, or treatment guidance. |
| `pubmed_antigen_escape_bcma_directed_2024` | PubMed-indexed literature | research article | multiple myeloma, BCMA-directed therapy, antigen escape | `literature-search`, `mechanism-map` | Mechanism observations should not be generalized beyond the studied context without review. |
| `pubmed_yue_2025_bcma_resistance` | PubMed-indexed literature | review article | multiple myeloma, BCMA-targeted immunotherapy, resistance mechanisms | `literature-search`, `mechanism-map` | Review article; mechanism categories require source-specific extraction before quantitative use. |
| `pubmed_di_meo_2025_sema4a_low_bcma` | PubMed-indexed literature | research article | multiple myeloma, BCMA-low relapse, candidate alternate target | `literature-search`, `mechanism-map` | Preclinical and translational findings do not establish clinical efficacy. |
| `pubmed_plasma_cell_identity_escape_2025` | PubMed-indexed literature | preprint record | multiple myeloma, anti-BCMA T-cell redirecting therapy, plasma-cell identity escape | `literature-search`, `mechanism-map` | Preprint; not peer reviewed at access date. Mechanism findings require source-specific appraisal and should not be treated as clinical guidance. |
| `pubmed_bolli_2014_genomic_heterogeneity_myeloma` | PubMed-indexed literature / Nature Communications | open-access research article | multiple myeloma, clonal heterogeneity, subclone diversity, genomic evolution, mutational profiles | `literature-search`, `mechanism-map`, `geometry-discrimination`, `subclone-context` | Primary genomic evolution study; use for cohort/source-specific subclone-diversity extraction only, not patient-specific prognosis, relapse prediction, treatment selection, or cure claims. |
| `pubmed_wang_2025_lipid_metabolism_myeloma` | PubMed-indexed literature / Frontiers in Oncology | open-access review article | multiple myeloma, lipid metabolism, tumor microenvironment, drug resistance, metabolic reprogramming | `literature-search`, `mechanism-map`, `geometry-proof`, `metabolic-context` | Review article; use for metabolic pathway context and public artifact coverage only, not metabolic intervention guidance, biomarker use, prognosis, treatment selection, or patient-specific interpretation. |
| `pubmed_lu_2024_myeloma_signaling_pathways` | PubMed-indexed literature / Molecular Biomedicine | open-access review article | multiple myeloma, signaling pathways, NF-kB pathway, drug resistance, bone marrow microenvironment | `literature-search`, `mechanism-map`, `geometry-proof`, `pathway-context` | Review article; use for NF-kB pathway context and public artifact coverage only, not target selection, pathway ranking, treatment guidance, prognosis, or patient-specific interpretation. |
| `pubmed` | U.S. National Library of Medicine | literature index | all blood-cancer subtypes | `literature-search` | Indexing a paper does not validate study quality or clinical actionability. |
| `fda_drugs_at_fda` | U.S. Food and Drug Administration | regulatory database | approved drugs and therapeutic biologics | `regulatory-status` | Approval status is not patient-specific appropriateness or comparative effectiveness. |
| `fda_linvoseltamab_accelerated_approval_2025` | U.S. Food and Drug Administration | regulatory notice | multiple myeloma, BCMA, bispecific antibody, accelerated approval | `regulatory-status`, `therapy-reference` | Product-specific regulatory notice; does not establish availability, eligibility, treatment selection, comparative efficacy, sequencing, or patient fit. |
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
| `hgnc_gene_names` | https://www.genenames.org/ | 2026-04-15 |
| `ncbi_gene` | https://www.ncbi.nlm.nih.gov/gene/ | 2026-04-15 |
| `nci_cancer_drug_dictionary` | https://www.cancer.gov/publications/dictionaries/cancer-drug | 2026-04-15 |
| `who_ictrp_search_portal` | https://trialsearch.who.int/ | 2026-04-15 |
| `dailymed` | https://dailymed.nlm.nih.gov/dailymed/ | 2026-04-15 |
| `ema_medicines` | https://www.ema.europa.eu/en/medicines | 2026-04-15 |
| `ncbi_geo` | https://www.ncbi.nlm.nih.gov/geo/info/overview.html | 2026-04-15 |
| `nci_gdc_data_portal` | https://gdc.cancer.gov/ | 2026-04-15 |
| `dana_farber_car_t_update_2025` | https://www.dana-farber.org/for-physicians/clinical-resources/hematologic-malignancies/advances-newsletter/2025-issue-20/multiple-myeloma-cart-t-cell-therapy-update | 2026-04-16 |
| `pubmed_kumar_2016_imwg_mrd_response_criteria` | https://pubmed.ncbi.nlm.nih.gov/27511158/ | 2026-04-14 |
| `pubmed_munshi_2017_mrd_survival_meta_analysis` | https://pubmed.ncbi.nlm.nih.gov/27632282/ | 2026-04-14 |
| `pubmed_soh_2022_mrd_flow_harmonization` | https://pubmed.ncbi.nlm.nih.gov/35005838/ | 2026-04-14 |
| `pubmed_martinez_lopez_2020_mrd_dynamics` | https://pubmed.ncbi.nlm.nih.gov/32706892/ | 2026-04-19 |
| `pubmed_cohen_2021_resistance_single_cell` | https://pubmed.ncbi.nlm.nih.gov/33619369/ | 2026-04-19 |
| `fda_mrd_cr_endpoint_guidance_2026` | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/minimal-residual-disease-and-complete-response-multiple-myeloma-use-endpoints-support-accelerated | 2026-04-16 |
| `nature_genetics_commpass_subtypes_2024` | https://www.nature.com/articles/s41588-024-01853-0 | 2026-04-18 |
| `nature_cancer_immune_atlas_myeloma_2026` | https://www.nature.com/articles/s43018-025-01072-4 | 2026-04-18 |
| `nature_genetics_mm_precursor_genomic_landscape_2025` | https://www.nature.com/articles/s41588-025-02196-0 | 2026-04-18 |
| `nature_communications_rrmm_resistance_2022` | https://www.nature.com/articles/s41467-022-31430-0 | 2026-04-18 |
| `jco_ims_imwg_high_risk_consensus_2025` | https://pubmed.ncbi.nlm.nih.gov/40489728/ | 2026-04-18 |
| `pubmed_high_risk_genomic_consensus_validation_2026` | https://pubmed.ncbi.nlm.nih.gov/40991836/ | 2026-04-18 |
| `pubmed_kyle_2010_mgus_smm_imwg` | https://pubmed.ncbi.nlm.nih.gov/20410922/ | 2026-04-16 |
| `pubmed_mateos_2020_smm_risk_model` | https://www.nature.com/articles/s41408-020-00366-3 | 2026-04-16 |
| `pubmed_palumbo_2015_imwg_frailty` | https://pubmed.ncbi.nlm.nih.gov/25628469/ | 2026-04-16 |
| `pubmed_tedder_bhutani_2025_bcma_resistance` | https://pubmed.ncbi.nlm.nih.gov/40710330/ | 2026-04-14 |
| `pubmed_ledergor_2024_cd4_car_t_exhaustion` | https://pubmed.ncbi.nlm.nih.gov/38574299/ | 2026-04-14 |
| `pubmed_antigen_escape_bcma_directed_2024` | https://pubmed.ncbi.nlm.nih.gov/38728378/ | 2026-04-14 |
| `pubmed_yue_2025_bcma_resistance` | https://pubmed.ncbi.nlm.nih.gov/39818472/ | 2026-04-14 |
| `pubmed_di_meo_2025_sema4a_low_bcma` | https://pubmed.ncbi.nlm.nih.gov/41072416/ | 2026-04-14 |
| `pubmed_plasma_cell_identity_escape_2025` | https://pubmed.ncbi.nlm.nih.gov/41415462/ | 2026-04-14 |
| `pubmed_bolli_2014_genomic_heterogeneity_myeloma` | https://pubmed.ncbi.nlm.nih.gov/24429703/ | 2026-04-20 |
| `pubmed_wang_2025_lipid_metabolism_myeloma` | https://pubmed.ncbi.nlm.nih.gov/40110197/ | 2026-04-20 |
| `pubmed_lu_2024_myeloma_signaling_pathways` | https://pubmed.ncbi.nlm.nih.gov/38961036/ | 2026-04-20 |
| `pubmed` | https://pubmed.ncbi.nlm.nih.gov/ | 2026-04-11 |
| `fda_drugs_at_fda` | https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database | 2026-04-11 |
| `fda_linvoseltamab_accelerated_approval_2025` | https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-linvoseltamab-gcpt-relapsed-or-refractory-multiple-myeloma | 2026-04-16 |
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
