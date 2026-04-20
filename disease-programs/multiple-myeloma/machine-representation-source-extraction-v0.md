# Machine Representation Source Extraction v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `machine-representation-source-extraction-v0`
- active ORP item: `machine-representation-source-extraction-v0`
- extraction status: public source-extraction table
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only and synthetic-only; no real case data,
  identifiers, raw records, uploads, exact person-linked dates, free-text case
  details, private correspondence, model weights, predictions,
  recommendations, matching, ranking, or clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This artifact maps the public machine-representation architecture claims in
[Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
to source IDs, source-context gaps, extraction status, uncertainty, review
status, blocked uses, and next public contribution tasks.

It is a source-extraction table. It is not a model, normalizer, validator,
evidence ranking, source ranking, clinical interpretation, treatment selector,
trial matcher, prognosis tool, monitoring tool, publication authorization, or
claim that a cure has been found.

## Extraction Decision

Current decision: `source-extraction-table-only`.

Allowed use:

- public source-context review
- contribution task routing
- expert-review question planning
- validator rule coverage review
- future synthetic fixture updates

Blocked use:

- accepting, normalizing, interpreting, publishing, or routing real case data
- scoring or ranking sources, evidence, mechanisms, treatments, trials,
  candidate options, or patient states
- producing progression risk, response probability, MRD interpretation,
  resistance attribution, diagnosis, prognosis, monitoring guidance, treatment
  guidance, trial guidance, expanded-access guidance, or clinical decisions
- training, fine-tuning, serving, comparing, or validating model weights

## Extraction Row Shape

| Field | Required Public Shape | Boundary |
| --- | --- | --- |
| `row_id` | Stable extraction row ID. | Not a case ID, source rank, prediction ID, or review decision. |
| `architecture_claim` | Source-scoped claim from the machine stack. | Descriptive architecture only; not clinical guidance. |
| `source_ids` | Source registry IDs or `source_context_needed`. | Source IDs do not prove completeness or clinical validity. |
| `extraction_status` | `source_id_mapped`, `source_id_mapped_with_scope_gap`, `source_context_needed`, or `boundary_only`. | No status authorizes model use or patient interpretation. |
| `uncertainty` | Limitation, cohort scope, missingness, or review gap. | Missing evidence cannot be filled by inference. |
| `review_status` | `public_shape_only`, `source_appraisal_needed`, `expert_review_needed`, or `model_governance_needed`. | Missing review defaults to blocked. |
| `blocked_uses` | Blocked downstream uses that travel with the row. | Blocks cannot be removed by downstream tooling. |
| `next_public_task` | Contribution-ready task that uses public sources only. | Task must not request real case data, advice, ranking, outreach, or publication decisions. |

## Architecture Source Extraction Table

| Row ID | Architecture Claim | Source IDs | Extraction Status | Uncertainty And Review | Blocked Uses | Next Public Task |
| --- | --- | --- | --- | --- | --- | --- |
| `mse_00_multimodal_state_backbone` | A myeloma state object should preserve genomic, transcriptomic, clinical, treatment, and measurement context as a longitudinal multimodal state. | `nature_genetics_commpass_subtypes_2024`; local anchors: `myeloma-state-object-schema-v0`, `myeloma-state-validator-rule-map-v0` | `source_id_mapped_with_scope_gap` | CoMMpass-style multimodal coverage is cohort-level and does not prove a portable patient-state model; expert review needed before stronger language. | prognosis, treatment, trial, monitoring, matching, ranking, model validation, clinical decisions | Extract source-defined modality coverage, cohort scope, and longitudinal follow-up limits from the public source. |
| `mse_01_tumor_genomic_event_graph` | DNA representation should preserve source-defined SNV, indel, copy-number, structural-variant, translocation, clonality, mutational-process, and high-risk genomic context. | `nature_genetics_commpass_subtypes_2024`; `nature_genetics_mm_precursor_genomic_landscape_2025`; `jco_ims_imwg_high_risk_consensus_2025`; `pubmed_high_risk_genomic_consensus_validation_2026` | `source_id_mapped_with_scope_gap` | Event names and high-risk labels must stay source-defined; this table does not decide actionability, risk, prognosis, or testing. | diagnosis, prognosis, actionability, test guidance, treatment fit, trial fit, option ranking | Create a public extraction note for source-defined event families, assay context, and uncertainty labels. |
| `mse_02_transcriptome_state` | Bulk RNA representation may include expression-subtype probabilities, pathway scores, program summaries, or latent embedding references when source-defined. | `nature_genetics_commpass_subtypes_2024` | `source_id_mapped_with_scope_gap` | Subtype and pathway language needs exact public extraction before reuse; synthetic fixtures cannot imply a real subtype or probability. | response prediction, prognosis, treatment selection, trial matching, ranking | Extract public transcriptome subtype and expression-program labels with method and limitation fields. |
| `mse_03_marrow_ecosystem_state` | Bone marrow immune and microenvironment state should be represented as cell-state composition, immune programs, and communication summaries when source-defined. | `nature_cancer_immune_atlas_myeloma_2026` | `source_id_mapped_with_scope_gap` | Single-cell data are optional and sparse; missing single-cell context must remain visible and cannot imply immune normality. | immune-status advice, prognosis, treatment fit, trial fit, monitoring guidance | Extract allowed public immune-atlas summary fields, missingness labels, and review warnings. |
| `mse_04_clinical_context_buckets` | Clinical context should use source-defined buckets for disease state, organ context, staging-related context, frailty or performance context, and high-risk genomic context. | `nci_pdq_myeloma_hp`; `jco_ims_imwg_high_risk_consensus_2025`; `pubmed_high_risk_genomic_consensus_validation_2026`; local anchors: `case-feature-normalization-contract-v0`, `high-risk-organ-frailty-context-modifier-map-v0` | `source_id_mapped_with_scope_gap` | Public context labels are descriptive only and need expert review before any review-packet or model-facing reuse. | diagnosis, prognosis, eligibility, urgency, monitoring, treatment guidance, trial guidance | Crosswalk public clinical-context labels to the case-feature and context-modifier contracts without creating patient-facing categories. |
| `mse_05_treatment_exposure_context` | Treatment exposure history should be represented by therapy class, line or timing bucket, response linkage, refractory context, toxicity or constraint category, and source/review status. | `nci_pdq_myeloma_hp`; `nci_cancer_drug_dictionary`; `fda_drugs_at_fda`; `dailymed`; `pubmed_moreau_2021_imwg_rrmm_recommendations`; `pubmed_laubach_2016_imwg_relapsed_management`; `pubmed_kumar_2016_imwg_mrd_response_criteria`; `fda_mrd_cr_endpoint_guidance_2026`; local anchors: `therapy-exposure-timeline-contract-v0`, `multiple-myeloma-treatment-class-taxonomy-v0`, `immune-therapy-sequencing-access-boundary-v0` | `source_id_mapped_with_scope_gap` | Public anchors now support class/product vocabulary, relapsed/refractory terminology, response linkage, and status-source routing, but exact exposure, toxicity, constraints, refractory state, access, eligibility, sequencing, and patient-specific response linkage remain private or clinical. | sequencing, eligibility, availability, access guidance, treatment advice, trial advice, ranking, refractory assessment, toxicity management | Preserve the v0 source delta in [Machine Representation Source-Gap Internal Extraction v0](machine-representation-source-gap-internal-extraction-v0.md) and keep review-needed boundaries. |
| `mse_06_measurement_timeline_and_mrd` | Measurement timeline fields should preserve response, MRD, relapse, lab, imaging, method, threshold, sample, timepoint, durability, endpoint role, source context, and limitation state. | `fda_mrd_cr_endpoint_guidance_2026`; local anchors: `measurement-normalization-contract-v0`, `mrd-and-relapse-measurement-glossary-v0`, `mrd-endpoint-language-guardrail-addendum-v0` | `source_id_mapped` | FDA source is draft and nonbinding; MRD and response-depth language cannot be reused as cure, prognosis, monitoring, or treatment language. | cure claim, endpoint interpretation, prognosis, monitoring guidance, treatment guidance, trial guidance | Extract endpoint-role, method, threshold, sample, and timepoint fields into source-scoped measurement tasks. |
| `mse_07_precursor_progression_context` | Precursor-to-active disease and progression context should be represented as graded public-source event space, not as a binary personal risk state. | `nature_genetics_mm_precursor_genomic_landscape_2025`; local anchor: `precursor-risk-interception-boundary-note-v0` | `source_id_mapped_with_scope_gap` | Precursor source context is cohort-level; no screening, personal risk, prevention, monitoring, or early-intervention guidance can be inferred. | screening advice, personal risk advice, prevention claims, monitoring guidance, treatment guidance, trial guidance | Extract source-defined precursor/progression terms and boundary language without calculator fields. |
| `mse_08_relapse_resistance_branch` | Relapsed/refractory and resistance biology should be represented as therapy-conditioned research context separate from newly diagnosed baseline modeling. | `nature_communications_rrmm_resistance_2022`; local anchors: `post-bcma-resistance-frontier-addendum-v0`, `post-car-t-relapse-mechanism-map-v0` | `source_id_mapped_with_scope_gap` | Resistance observations are cohort-level and cannot be used as patient-specific resistance calls or therapy rankings. | resistance diagnosis, treatment ranking, trial matching, mechanism ranking, actionability | Extract source-defined relapse/resistance feature families and map them to mechanism-gap tasks. |
| `mse_09_fusion_model_architecture` | Fusion architecture may use graph or set encoders, dense transcriptome encoders, sparse-aware single-cell encoders, structured clinical encoders, and temporal models. | local anchor: `multiple-myeloma-machine-representation-stack-v0`; `source_context_needed` | `source_context_needed` | This is a design proposal in the public stack, not source-extracted model evidence or implementation guidance. Generic AI/ML governance sources were not accepted as direct validation of this architecture. | model implementation, model comparison, scoring, prediction, clinical deployment | Identify direct public method sources or expert-review questions for the proposed fusion architecture before any implementation plan. |
| `mse_10_prediction_head_boundaries` | Progression, response, MRD, and resistance heads may be named only as research-output placeholders with uncertainty, calibration, missingness, and blocked-use state. | local anchors: `model-output-boundary-wrapper-v0`, `myeloma-state-validator-rule-map-v0`, `evidence-retrieval-packet-v0` | `boundary_only` | Boundary is mapped, but no prediction head is implemented, validated, calibrated, or clinically usable. | progression risk, response probability, MRD interpretation, resistance attribution, recommendation, ranking | Draft expert-review questions about whether the refusal wrapper and blocked-use labels are complete enough for future synthetic-only outputs. |
| `mse_11_training_and_validation_standard` | Future validation should consider site-aware, calendar-time, newly diagnosed versus relapsed/refractory separation, calibration, missing-modality robustness, comparator features, subgroup review, and dataset-shift warnings. | `pubmed_tripod_ai_2024_prediction_model_reporting`; `pubmed_probast_2019_prediction_model_risk_of_bias`; `fda_imdrf_gmlp_guiding_principles_2025`; `pmc_decide_ai_2022_early_clinical_eval`; local anchor: `multiple-myeloma-machine-representation-stack-v0` | `source_id_mapped_with_scope_gap` | Reporting, risk-of-bias, lifecycle, transparency, and early-evaluation sources can pressure future validation plans, but they do not validate any myeloma model, benchmark, calibration, clinical utility, or deployment readiness. | clinical utility claim, model validation claim, deployment readiness, publication authorization, benchmark claim, regulatory clearance claim | Preserve governance anchors as pressure fields only; keep model validation, utility, and deployment claims blocked. |
| `mse_12_public_case_to_cure_linkage` | Machine-state artifacts should connect to private intake, case-feature normalization, measurement normalization, therapy exposure, molecular context, evidence retrieval, and publication gates. | local anchors: `case-to-cure-pipeline-blueprint-v0`, `case-to-cure-stage-validator-map-v0`, `case-to-public-learning-extraction-gate-v0` | `boundary_only` | Linkage is public-plumbing only and does not authorize private-lab access, real intake, publication, or clinical interpretation. | public intake, real-case routing, publication authorization, clinical decisions | Keep linkage references current and create source-gap tasks only from public artifacts. |

## Contribution Task Seeds

| Task ID | Trigger Rows | Public-Safe Task | Done When |
| --- | --- | --- | --- |
| `mr_source_task_00_modality_scope` | `mse_00`, `mse_01`, `mse_02` | Extract modality coverage, cohort scope, and longitudinal follow-up limitations from public CoMMpass-linked source context. | Rows cite source-defined fields and keep all model and patient-use claims blocked. |
| `mr_source_task_01_immune_atlas_fields` | `mse_03` | Extract public immune-atlas field families and missingness labels that can be used in synthetic-only fixtures. | Marrow ecosystem labels include method, source, uncertainty, and no-advice boundary. |
| `mr_source_task_02_context_crosswalk` | `mse_04`, `mse_07` | Crosswalk clinical, high-risk, organ, frailty, and precursor labels to existing public context contracts. | Context terms remain optional, source-scoped, non-identifying, and non-directive. |
| `mr_source_task_03_therapy_exposure_sources` | `mse_05` | Identify public sources for therapy-exposure vocabulary, response linkage, refractory context, and limitation fields. | Complete for v0 source anchors in [Machine Representation Source-Gap Internal Extraction v0](machine-representation-source-gap-internal-extraction-v0.md); scope gaps remain blocked. |
| `mr_source_task_04_endpoint_fields` | `mse_06` | Extract MRD and response endpoint field requirements from public measurement sources and guardrails. | Method, threshold, sample, timepoint, durability, endpoint role, and limitation fields are explicit. |
| `mr_source_task_05_resistance_scope` | `mse_08` | Extract relapse/resistance feature families as cohort-level mechanism context only. | No patient-specific resistance call, option ranking, or actionability language appears. |
| `mr_source_task_06_model_method_sources` | `mse_09`, `mse_11` | Find public method or governance sources for fusion architecture and validation standards, or keep them expert-review-needed. | Complete only for validation-governance anchors on `mse_11`; `mse_09` fusion architecture remains `source_context_needed`. |
| `mr_source_task_07_wrapper_review_questions` | `mse_10`, `mse_12` | Draft expert-review questions for prediction-head boundaries, wrapper refusals, and case-to-cure linkage. | Questions do not request real case data, clinical judgment, option ranking, or publication approval. |

## What This Step Revealed

The machine-representation stack has adequate public source IDs for several
biological and measurement anchors. The later
[Machine Representation Source-Gap Internal Extraction v0](machine-representation-source-gap-internal-extraction-v0.md)
adds public source anchors for therapy-exposure context and validation
governance, while deliberately leaving the fusion architecture proposal
source-context-needed. That split is important: governance sources can pressure
future model validation language, but they do not validate a model architecture
or make any clinical-output behavior safe.

The next safest public step is therefore
`machine-representation-source-gap-task-queue-v0`: a public task queue that
turns the task seeds above into source extraction tasks with blocked-use labels,
review status, and no-advice wording.

That task queue is now complete as
[Machine Representation Source-Gap Task Queue v0](public-tasks/machine-representation-source-gap-task-queue-v0.md).
The issue draft packet is now complete as
[Machine Representation Source-Gap Issue Draft Packet v0](public-tasks/issue-drafts/machine-representation-source-gap-issue-draft-packet-v0.md).
The implementation completion audit is now complete as
[Machine Representation Implementation Completion Audit v0](machine-representation-implementation-completion-audit-v0.md).
The no-outreach expert-validation preparation packet is now complete as
[Machine Representation Expert Validation No-Outreach Execution Packet v0](reviews/machine-representation-expert-validation-no-outreach-execution-packet-v0.md).
The public-source internal extraction pass is now complete as
[Machine Representation Source-Gap Internal Extraction v0](machine-representation-source-gap-internal-extraction-v0.md).
The next state remains
`machine-representation-expert-validation-human-authorization-blocker-v0`
unless a new no-outreach, public-source-only phase is explicitly selected.

## Handoff State

`machine-representation-source-extraction-v0` is complete as a public
source-extraction table.

ORP has marked this item complete. The source-gap task queue, issue draft
packet, implementation completion audit, no-outreach execution packet, and
internal source-gap extraction pass are complete. The active blocker remains
`machine-representation-expert-validation-human-authorization-blocker-v0`:
actual expert-validation execution, issue operations, outreach, response intake,
claim upgrade, and clinical interpretation remain blocked.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, sequencing records, portal exports, accessions, private
  paths, free-text case details, private correspondence, or re-identification
  keys.
- No public intake form, upload path, backend, account workflow, database,
  model weights, scoring code, prediction API, executable normalizer, or
  executable validator.
- No diagnosis, prognosis, progression-risk output, response-probability
  output, MRD interpretation, resistance call, treatment guidance, trial
  guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, urgency guidance, publication authorization, or clinical decision.
- No patient matching, trial matching, target ranking, mechanism ranking,
  option ranking, evidence ranking, or source ranking.
- No cure or vaccine claim.

## Limitations

- This is a public source-extraction table, not a systematic review.
- This does not rank sources, grade evidence, or assert source completeness.
- This does not extract full methods, cohorts, endpoints, or feature
  definitions from the cited sources.
- This does not implement model code, validation code, data processing,
  normalization, scoring, training, inference, calibration, benchmarking, or
  deployment.
- This does not authorize real case intake, private-lab access, publication,
  clinical interpretation, clinical use, legal approval, regulatory readiness,
  sponsor decisions, institutional decisions, or treating-team decisions.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decisions.
- This does not claim that multiple myeloma has been cured or that a vaccine
  has been found.
