# Machine Representation Source-Gap Internal Extraction v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `machine-representation-source-gap-internal-extraction-v0`
- ORP item: `machine-representation-source-gap-internal-extraction-v0`
- extraction status: public-source internal extraction complete for v0 anchors
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- communication boundary: no outreach, no private correspondence, no expert
  response intake
- last reviewed: `2026-04-20`

## Purpose

This artifact implements the next no-outreach public-source extraction step
after the machine-representation no-outreach execution packet.

It focuses on the two highest-value source-context gaps in the machine
representation stack:

- therapy-exposure vocabulary and refractory/response-linkage context
- fusion and validation method governance for future machine-state models

It does not open issues, send outreach, request private material, inspect real
case data, implement model code, validate a model, or mark any artifact as
expert-reviewed.

## Extraction Decision

Current decision: `public-source-internal-extraction-only`.

The extraction can upgrade some rows from `source_context_needed` to
`source_id_mapped_with_scope_gap`, but only as public artifact readiness. It
does not clear expert-review, model-governance, clinical, legal, regulatory,
private-lab, publication, or outreach gates.

## Source Delta Summary

| Machine Row | Prior State | Source Delta | New v0 State | Remaining Blocker |
| --- | --- | --- | --- | --- |
| `mse_05_treatment_exposure_context` | `source_context_needed` | Added public anchors for therapy class, product/regulatory vocabulary, response criteria, relapsed/refractory context, and prior-line context. | `source_id_mapped_with_scope_gap` | Exact exposure, toxicity, constraints, refractory state, response linkage, access, eligibility, and sequencing remain private or clinical. |
| `mse_09_fusion_model_architecture` | `source_context_needed` | No direct public source was accepted for the proposed graph/set/dense/single-cell/temporal fusion architecture. | `source_context_needed` | Architecture remains a design proposal until method sources or expert review justify the named encoder families. |
| `mse_11_training_and_validation_standard` | `source_context_needed` | Added public reporting, risk-of-bias, lifecycle, transparency, and early clinical-evaluation anchors. | `source_id_mapped_with_scope_gap` | These are governance/reporting anchors, not benchmark evidence, clinical utility, deployment approval, or model validation. |

## Therapy-Exposure Extraction

| Extraction ID | Source IDs | Extracted Public Field Families | Safe Reuse | Blocked Inference |
| --- | --- | --- | --- | --- |
| `mr_internal_therapy_class_product_vocab_2026_04_20` | `nci_pdq_myeloma_hp`, `nci_cancer_drug_dictionary`, `fda_drugs_at_fda`, `dailymed`, `multiple-myeloma-treatment-class-taxonomy-v0` | Therapy class names, product or agent name anchors, source-defined combination language, product-status source class, and date-stamped regulatory source status. | Non-advisory class/product provenance for synthetic state objects and source-gap rows. | No treatment selection, eligibility, availability, access, sequencing, comparative value, or patient fit. |
| `mr_internal_rrmm_prior_line_context_2026_04_20` | `pubmed_moreau_2021_imwg_rrmm_recommendations`, `pubmed_laubach_2016_imwg_relapsed_management`, `nci_pdq_myeloma_hp` | Relapsed/refractory public terminology, prior-line context, disease-setting labels, and source-defined limitation notes. | Broad source-context labels for research artifacts. | No relapse diagnosis, refractory assessment, line-of-therapy determination, prognosis, treatment advice, trial advice, or urgency guidance. |
| `mr_internal_response_linkage_context_2026_04_20` | `pubmed_kumar_2016_imwg_mrd_response_criteria`, `fda_mrd_cr_endpoint_guidance_2026`, `multiple-myeloma-therapy-exposure-timeline-contract-v0`, `multiple-myeloma-measurement-normalization-contract-v0` | Response, MRD, endpoint-role, sample, threshold, timing, durability, and measurement-linkage fields that must stay source-scoped. | Measurement-aware source extraction for synthetic or aggregate-only machine-state rows. | No patient-specific response call, MRD interpretation, cure claim, prognosis, monitoring action, or treatment decision. |
| `mr_internal_toxicity_constraint_boundary_2026_04_20` | `multiple-myeloma-therapy-exposure-timeline-contract-v0`, `immune-therapy-sequencing-access-boundary-v0`, `dailymed` | Source-status and label-source routing for toxicity or constraint categories. | Boundary labels only: `toxicity_category_source_defined`, `constraint_private`, `label_source_needed`, or `not_reported_by_source`. | No adverse-event management, dose guidance, hold/stop rules, contraindication inference, safety advice, access advice, or eligibility inference. |

## Validation-Governance Extraction

| Extraction ID | Source IDs | Extracted Public Field Families | Safe Reuse | Blocked Inference |
| --- | --- | --- | --- | --- |
| `mr_internal_prediction_reporting_context_2026_04_20` | `pubmed_tripod_ai_2024_prediction_model_reporting` | Reporting context for prediction-model studies, including data/source description, participant context, predictors, outcomes, model specification, missing data, performance reporting, and calibration reporting. | Public checklist pressure for future synthetic-only validation plans. | No model validity, clinical utility, deployment readiness, benchmark performance, or patient-specific prediction. |
| `mr_internal_prediction_bias_applicability_context_2026_04_20` | `pubmed_probast_2019_prediction_model_risk_of_bias` | Risk-of-bias and applicability pressure fields for participants, predictors, outcomes, and analysis. | Public appraisal structure for future model-study review. | No evidence grading, source ranking, model approval, clinical validity, or recommendation behavior. |
| `mr_internal_gmlp_lifecycle_context_2026_04_20` | `fda_imdrf_gmlp_guiding_principles_2025` | Lifecycle and governance pressure fields: representative data, independent training/test sets, reference data, intended-use fit, human-AI team performance, clinically relevant testing, transparency, and monitoring for drift or retraining risk. | Governance checklist language for blocked future model work. | No regulatory clearance, device status, deployment authorization, clinical safety claim, or model performance claim. |
| `mr_internal_decide_ai_live_eval_context_2026_04_20` | `pmc_decide_ai_2022_early_clinical_eval` | Early live-evaluation reporting context, human factors, implementation environment, user variability, safety, and dataset-shift warnings. | Future gate language if a live clinical decision-support study is ever proposed. | No live clinical use, clinical trial authorization, patient-impact claim, or public deployment. |

## Updated Row Dispositions

| Row ID | Disposition | Rationale | Next Safe Action |
| --- | --- | --- | --- |
| `mse_05_treatment_exposure_context` | `source_id_mapped_with_scope_gap` | Public source IDs now cover class/product vocabulary, response criteria, relapse/refractory context, and source-status routing. | Patch the machine-representation source extraction table and keep review-needed boundaries. |
| `mse_09_fusion_model_architecture` | `keep_source_context_needed` | The selected governance sources constrain validation and reporting, but they do not justify the proposed fusion architecture or named encoder families. | Keep architecture as design proposal; search for source-specific multimodal fusion method anchors in a separate future pass if selected. |
| `mse_11_training_and_validation_standard` | `source_id_mapped_with_scope_gap` | Public governance/reporting/risk-of-bias sources now support validation-standard pressure fields. | Patch the machine-representation source extraction table; block benchmark, utility, and deployment claims. |

## Task Queue Dispositions

| Task ID | Disposition | Reason |
| --- | --- | --- |
| `mr-therapy-exposure-source-gap-task-v0` | `done-for-v0-source-anchors` | Public source IDs were added or reused for therapy vocabulary, response linkage, refractory context, and limitations. |
| `mr-fusion-validation-method-source-gap-task-v0` | `partial-method-governance-mapped` | Validation/governance sources were mapped for `mse_11`; fusion architecture support for `mse_09` remains source-context-needed. |
| `mr-output-wrapper-review-question-task-v0` | `ready-after-source-delta` | The new validation-governance anchors sharpen refusal-wrapper questions, but expert review and output behavior remain blocked. |

## Public Safety Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `mrgie_00_no_outreach` | This extraction cannot contact reviewers, tag people, open issues, or request private material. | Record only public-source deltas and blockers. |
| `mrgie_01_no_private_case_data` | Do not use records, reports, notes, dates, therapy histories, molecular files, images, correspondence, or real case facts. | Block and route to private-lab-needed. |
| `mrgie_02_no_source_ranking` | Source IDs are anchors, not evidence ranks or clinical priorities. | Use source IDs only for provenance and limitation fields. |
| `mrgie_03_no_architecture_upgrade_without_source` | Generic model-governance sources cannot validate a specific fusion architecture. | Keep `mse_09` source-context-needed. |
| `mrgie_04_no_validation_claim` | Reporting and governance sources do not validate any myeloma model. | Block benchmark, calibration, clinical utility, and deployment claims. |
| `mrgie_05_no_therapy_inference` | Therapy exposure sources cannot infer sequencing, access, eligibility, refractory state, or next treatment. | Keep therapy rows source-scoped and non-advisory. |

## Handoff State

`machine-representation-source-gap-internal-extraction-v0` is complete for the
selected no-outreach source-delta slice.

It should update:

- [Machine Representation Source Extraction v0](machine-representation-source-extraction-v0.md)
- [Machine Representation Source-Gap Task Queue v0](public-tasks/machine-representation-source-gap-task-queue-v0.md)
- [Source Registry v0](../../sources/source-registry-v0.md)
- ORP state and Clawdad delegation notes

The next autonomous work should remain blocked by
`machine-representation-expert-validation-human-authorization-blocker-v0`
unless a human selects a new named no-outreach source extraction phase, such as
fusion-architecture method-source extraction or output-wrapper boundary audit.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, therapy histories, reports, images, notes, exact
  person-linked dates, private paths, private correspondence, or
  re-identification keys.
- No outreach, public issue operation, tagging, reviewer contact, private
  response intake, or expert-review claim.
- No model code, model weights, training, inference, calibration,
  benchmarking, scoring, deployment, API, or validation output.
- No diagnosis, prognosis, treatment guidance, trial guidance, eligibility
  guidance, expanded-access guidance, monitoring guidance, urgency guidance,
  safety-management guidance, recommendation, ranking, matching, publication
  authorization, clinical decision, or cure claim.

## Limitations

- This is source extraction, not a systematic review.
- This is not expert review.
- This is not model governance clearance.
- This does not validate a fusion architecture or machine-learning model.
- This does not prove source completeness.
- This does not update or open public expert-validation issues.
- This does not inspect private lab records or real case data.
- This does not authorize real case intake, private-lab access, clinical
  interpretation, public release, legal approval, regulatory readiness, sponsor
  decisions, institutional decisions, treating-team decisions, or publication.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, safety-management guidance,
  urgency guidance, publication guidance, or a cure claim.
