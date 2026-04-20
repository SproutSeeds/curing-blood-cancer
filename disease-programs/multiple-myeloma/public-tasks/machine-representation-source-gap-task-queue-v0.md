# Machine Representation Source-Gap Task Queue v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `machine-representation-source-gap-task-queue-v0`
- active ORP item: `machine-representation-source-gap-task-queue-v0`
- queue status: public contribution task queue
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only; no real case data, identifiers, raw
  records, uploads, exact person-linked dates, free-text case details, private
  correspondence, model weights, predictions, recommendations, matching,
  ranking, or clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This queue turns the contribution task seeds in
[Machine Representation Source Extraction v0](../machine-representation-source-extraction-v0.md)
into public, contribution-ready source-gap tasks.

It exists so contributors can help close `source_context_needed` and
`expert_review_needed` rows before any stronger downstream use of the myeloma
machine-representation stack.

It is not a source ranking, evidence ranking, model roadmap, extraction result,
clinical interpretation, treatment selector, trial matcher, prognosis tool,
monitoring tool, publication decision, or claim that a cure has been found.

## Use Boundary

- Research-use only.
- Public sources only.
- Not medical advice.
- Not diagnostic guidance.
- Not prognosis guidance.
- Not treatment advice.
- Not trial advice.
- Not eligibility guidance.
- Not expanded-access guidance.
- Not monitoring guidance.
- Not publication authorization.
- Not a claim that multiple myeloma has been cured.
- Task priority means public artifact readiness, not patient relevance,
  evidence strength, biological importance, clinical priority, or treatment
  value.

## Source Artifacts

- [Machine Representation Source Extraction v0](../machine-representation-source-extraction-v0.md)
- [Machine Representation Source-Gap Internal Extraction v0](../machine-representation-source-gap-internal-extraction-v0.md)
- [Myeloma Machine Representation Stack v0](../machine-representation-stack-v0.md)
- [Myeloma State Validator Rule Map v0](../myeloma-state-validator-rule-map-v0.md)
- [Model Output Boundary Wrapper v0](../model-output-boundary-wrapper-v0.md)
- [Evidence Retrieval Packet v0](../evidence-retrieval-packet-v0.md)
- [Source Registry v0](../../../sources/source-registry-v0.md)
- [Public Safety](../../../governance/PUBLIC_SAFETY.md)

## Task Record Shape

| Field | Required Public Shape | Boundary |
| --- | --- | --- |
| `task_id` | Stable public task ID. | Not a source rank, clinical priority, case ID, or model ID. |
| `trigger_rows` | Source-extraction row IDs such as `mse_05`. | Row IDs route work only; they do not grade evidence. |
| `source_context_state` | `source_id_mapped_with_scope_gap`, `source_context_needed`, `boundary_only`, or `expert_review_needed`. | Missing source context remains visible. |
| `allowed_inputs` | Public source IDs, public artifacts, public metadata, and public issue drafts only. | No private records, emails, real cases, uploads, or restricted data. |
| `blocked_outputs` | Uses that must remain refused after task completion. | Blocks cannot be removed by a completed task. |
| `done_criteria` | Public-source extraction, no-add reason, limitation note, or review question. | Done does not mean clinical readiness, source completeness, or publication approval. |
| `next_successor` | `issue_draft`, `source_registry_delta`, `artifact_update`, `expert_review_question`, or `blocked_only`. | Successor must stay public-safe and non-advisory. |

## Task Queue

| Task ID | Public Priority | Status | Trigger Rows | Source Context State | Allowed Public Inputs | Blocked Outputs | Done Criteria | Next Successor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `mr-modality-scope-source-extraction-task-v0` | high | ready | `mse_00`, `mse_01`, `mse_02` | `source_id_mapped_with_scope_gap` | `nature_genetics_commpass_subtypes_2024`, source registry, machine stack, state schema | prognosis, treatment, trial, monitoring, matching, ranking, model validation | Extract modality coverage, cohort scope, longitudinal follow-up limits, and source-defined feature families, or record a no-add reason. | `issue_draft` |
| `mr-immune-atlas-field-source-extraction-task-v0` | high | ready | `mse_03` | `source_id_mapped_with_scope_gap` | `nature_cancer_immune_atlas_myeloma_2026`, source registry, synthetic fixture, validator map | immune-status advice, prognosis, treatment fit, trial fit, monitoring guidance | Extract public immune-atlas field families, missingness labels, method context, and limitation text for synthetic-only reuse. | `issue_draft` |
| `mr-context-crosswalk-source-task-v0` | high | ready | `mse_04`, `mse_07` | `source_id_mapped_with_scope_gap` | `nci_pdq_myeloma_hp`, `jco_ims_imwg_high_risk_consensus_2025`, `pubmed_high_risk_genomic_consensus_validation_2026`, `nature_genetics_mm_precursor_genomic_landscape_2025`, context contracts | diagnosis, prognosis, eligibility, screening advice, personal risk advice, treatment guidance, trial guidance | Crosswalk source-defined clinical, high-risk, organ, frailty, and precursor labels to public context contracts without calculator fields. | `issue_draft` |
| `mr-therapy-exposure-source-gap-task-v0` | high | complete-for-v0-source-anchors | `mse_05` | `source_id_mapped_with_scope_gap` | `nci_pdq_myeloma_hp`, `nci_cancer_drug_dictionary`, `fda_drugs_at_fda`, `dailymed`, `pubmed_moreau_2021_imwg_rrmm_recommendations`, `pubmed_laubach_2016_imwg_relapsed_management`, `pubmed_kumar_2016_imwg_mrd_response_criteria`, `fda_mrd_cr_endpoint_guidance_2026`, therapy exposure timeline contract, treatment-class taxonomy, immune therapy boundary, source registry | sequencing, eligibility, availability, access guidance, treatment advice, trial advice, ranking, refractory assessment, toxicity management | V0 source anchors are recorded in [Machine Representation Source-Gap Internal Extraction v0](../machine-representation-source-gap-internal-extraction-v0.md); exact exposure, toxicity, access, eligibility, sequencing, and patient-specific response linkage remain blocked. | `artifact_update` |
| `mr-endpoint-field-source-task-v0` | high | ready | `mse_06` | `source_id_mapped` | `fda_mrd_cr_endpoint_guidance_2026`, measurement normalization contract, MRD glossary, MRD endpoint guardrail | cure claim, endpoint interpretation, prognosis, monitoring guidance, treatment guidance, trial guidance | Extract method, threshold, sample, timepoint, durability, endpoint role, and limitation fields into source-scoped measurement task language. | `artifact_update` |
| `mr-relapse-resistance-scope-task-v0` | medium | ready | `mse_08` | `source_id_mapped_with_scope_gap` | `nature_communications_rrmm_resistance_2022`, post-BCMA frontier addendum, post-CAR T mechanism map | resistance diagnosis, treatment ranking, trial matching, mechanism ranking, actionability | Extract relapse/resistance feature families as cohort-level mechanism context and map unresolved gaps to mechanism task surfaces. | `issue_draft` |
| `mr-fusion-validation-method-source-gap-task-v0` | medium | partial-method-governance-mapped | `mse_09`, `mse_11` | `mse_09`: `source_context_needed`; `mse_11`: `source_id_mapped_with_scope_gap` | `pubmed_tripod_ai_2024_prediction_model_reporting`, `pubmed_probast_2019_prediction_model_risk_of_bias`, `fda_imdrf_gmlp_guiding_principles_2025`, `pmc_decide_ai_2022_early_clinical_eval`, machine stack, source registry, validator map | model implementation, model comparison, scoring, prediction, clinical deployment, clinical utility claim, benchmark claim, regulatory clearance claim | Governance sources are mapped for validation-standard pressure fields, but no direct method source validates the proposed fusion architecture or encoder families. | `expert_review_question` |
| `mr-output-wrapper-review-question-task-v0` | medium | ready | `mse_10`, `mse_12` | `boundary_only` and `expert_review_needed` | model-output boundary wrapper, validator rule map, source extraction table, case-to-cure gates | progression risk output, response probability, MRD interpretation, resistance attribution, recommendation, ranking, publication authorization | Draft public expert-review questions about wrapper refusals, blocked-use labels, and case-to-cure linkage without requesting real cases or clinical decisions. | `expert_review_question` |

## Public Issue Draft Packet Seed

The public-safe issue draft packet is complete as
[Machine Representation Source-Gap Issue Draft Packet v0](issue-drafts/machine-representation-source-gap-issue-draft-packet-v0.md):
a single packet of issue-draft text for the ready tasks above.

That packet must not open issues, send outreach, request private material, ask
for clinical judgment, rank sources, or authorize publication. It should only
prepare reusable draft text that a human can review before any public issue is
created.

## What This Step Revealed

The source-extraction table already provides enough structure for a task
queue. The later
[Machine Representation Source-Gap Internal Extraction v0](../machine-representation-source-gap-internal-extraction-v0.md)
closes the therapy-exposure source-anchor slice for v0 and partially closes
the validation-governance slice. It also confirms an important no-add result:
the fusion architecture row remains source-context-needed because general
model-governance sources do not justify the specific graph, set, dense,
sparse-aware, or temporal encoder families proposed in the machine stack.

The implementation completion audit is now complete as
[Machine Representation Implementation Completion Audit v0](../machine-representation-implementation-completion-audit-v0.md).
The no-outreach expert-validation preparation packet is now complete as
[Machine Representation Expert Validation No-Outreach Execution Packet v0](../reviews/machine-representation-expert-validation-no-outreach-execution-packet-v0.md).
The next state remains
`machine-representation-expert-validation-human-authorization-blocker-v0`
unless a new no-outreach, public-source-only phase is explicitly selected.

## Handoff State

`machine-representation-source-gap-task-queue-v0` is complete as a public task
queue.

ORP should keep this item complete and keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, issue operations, outreach, response intake,
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
- No source ranking, evidence ranking, patient matching, trial matching, target
  ranking, mechanism ranking, option ranking, diagnosis, prognosis,
  progression-risk output, response-probability output, MRD interpretation,
  resistance call, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decision.
- No autonomous outreach, issue creation, publication, pull request, commit, or
  push.
- No cure or vaccine claim.

## Limitations

- This is a public task queue, not completed source extraction.
- This does not rank tasks, sources, evidence, mechanisms, therapies, trials,
  candidate options, or patient states.
- This does not prove source completeness, clinical validity, model validity,
  calibration, generalizability, or clinical utility.
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
