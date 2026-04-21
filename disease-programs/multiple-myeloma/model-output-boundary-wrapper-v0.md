# Model Output Boundary Wrapper v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `model-output-boundary-wrapper-v0`
- active ORP item: `model-output-boundary-wrapper-v0`
- wrapper status: public no-code boundary protocol
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: synthetic-only and public-source-scoped; no real case data,
  identifiers, raw records, uploads, exact person-linked dates, free-text case
  details, model weights, predictions, recommendations, matching, ranking, or
  clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This wrapper defines the public-safe boundary for future model-output fields in
the myeloma machine representation stack.

It exists so progression, response, MRD, and resistance head placeholders can
be named, refused, and reviewed without creating a model, predictor, scoring
function, endpoint interpreter, therapy selector, trial matcher, or clinical
decision system.

## Wrapper Decision

Current decision: `refusal-and-uncertainty-wrapper-only`.

The wrapper may be used for:

- synthetic fixture validation
- schema and validator planning
- source-extraction task routing
- expert review of model-output language
- public safety checks for blocked downstream uses

The wrapper must not be used for:

- generating scores, thresholds, probabilities, risk categories, response
  categories, MRD interpretations, resistance calls, treatment options, trial
  options, monitoring actions, expanded-access paths, matches, rankings, or
  clinical decisions
- collecting, storing, uploading, transmitting, interpreting, publishing, or
  normalizing real case data
- training, fine-tuning, serving, comparing, validating, or distributing model
  weights

## Output Families

| Output Family ID | Placeholder Meaning | Required Public Boundary |
| --- | --- | --- |
| `progression_head` | Future research placeholder for progression modeling under a source-defined treatment-context bucket. | No prognosis, risk estimate, urgency guidance, monitoring guidance, or patient-specific output. |
| `response_head` | Future research placeholder for response-depth modeling under a named regimen class or line-context bucket. | No response prediction, regimen recommendation, treatment comparison, option ranking, or patient-specific output. |
| `mrd_head` | Future research placeholder for MRD-context modeling when method, sample, threshold, timepoint, and endpoint role are source-defined. | No MRD interpretation, monitoring action, complete-response claim, cure wording, or patient-specific output. |
| `resistance_attribution_head` | Future research placeholder for source-scoped resistance or relapse mechanism families. | No resistance call, target selection, therapy sequencing, trial direction, or patient-specific output. |

## Allowed Placeholder States

| State | Meaning | Required Handling |
| --- | --- | --- |
| `not_implemented` | The public repo has no model head, score, threshold, or executable output. | Keep the output empty and expose only refusal metadata. |
| `research_head_placeholder` | A future research head is named for schema planning only. | Preserve boundaries, source context, missingness, uncertainty, and review status. |
| `calibration_needed` | Any future research use would require calibration evidence and review. | Block interpretation and mark validation as incomplete. |
| `source_context_needed` | Required source IDs, methods, specimens, timepoint buckets, or limitations are missing. | Block reuse until source context exists. |
| `review_needed` | Expert, molecular, measurement, clinical, privacy, publication, or model-governance review is missing. | Block interpretation and downstream publication. |
| `private_lab_needed` | The requested use would require governed private data or lab access. | Keep public output as a blocker only. |
| `blocked_patient_specific` | The requested use would apply to a person, case, record, option, trial, or clinical decision. | Refuse and route to the relevant private, clinical, legal, regulatory, or publication gate. |
| `modality_discordance_visible` | Residual-disease modality context disagrees or paired state is incomplete. | Preserve discordance as an uncertainty/refusal state; do not explain patient meaning. |
| `modality_context_missing` | Required modality family, method, specimen, threshold, timing, paired-state, or source context is missing. | Route to source-context-needed or private-lab-needed without inference. |
| `assay_specimen_quality_needed` | Method family, threshold, specimen quality, timing alignment, paired modality, imaging criteria, spatial sampling, host-context separation, or real-review boundary is missing. | Preserve the specific checklist state; refuse comparison, endpoint interpretation, prognosis, monitoring, treatment, ranking, and decisions. |

## Required Wrapper Fields

Every model-output placeholder record should carry these fields before any
future validator, fixture, review packet, or machine-representation artifact
can reference it.

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `wrapper_id` | `model-output-boundary-wrapper-v0`. | Wrapper ID only; not a model ID or case ID. |
| `output_family_id` | One of `progression_head`, `response_head`, `mrd_head`, or `resistance_attribution_head`. | Family label only; not an output value. |
| `requested_use` | `schema_planning`, `synthetic_fixture_check`, `validator_rule_check`, `expert_review_question`, or `blocked_patient_specific_use`. | Any patient-specific use must be refused. |
| `state_object_schema_id` | `myeloma-state-object-schema-v0`. | Links to schema shape only; does not authorize interpretation. |
| `synthetic_fixture_ids` | IDs from the synthetic fixture or `fixture_needed`. | Fixtures must be visibly artificial and non-patient-like. |
| `head_status` | One of the allowed placeholder states. | Public status cannot contain a prediction. |
| `source_context_state` | `public_source_scoped`, `synthetic_source`, `source_context_needed`, `private_source_needed`, or `blocked_private_source`. | Missing source context blocks reuse. |
| `input_missingness_state` | `complete_synthetic`, `missing_modality_visible`, `unknown_visible`, `not_tested_visible`, `not_collected_visible`, or `blocked_private_missingness`. | Missingness cannot imply absence, normality, risk level, safety, fit, or no need for review. |
| `residual_disease_modality_state` | `not_applicable`, `single_modality_source_scoped`, `paired_modality_source_scoped`, `modality_discordance_visible`, `modality_context_missing`, `assay_specimen_quality_needed`, `modality_collapse_blocked`, or `private_lab_needed`. | Modality state can only explain why output is refused or incomplete. |
| `uncertainty_state` | `calibration_needed`, `assay_limit`, `method_limit`, `population_mismatch`, `cohort_shift_warning`, `expert_review_needed`, `source_limit`, `modality_discordance_visible`, `modality_context_missing`, or `assay_specimen_quality_needed`. | Uncertainty must travel with the placeholder; residual-disease modality disagreement or missing quality context is not patient meaning. |
| `review_status` | `public_shape_only`, `source_appraisal_needed`, `molecular_review_needed`, `measurement_review_needed`, `clinician_review_needed`, `privacy_review_needed`, `publication_gate_needed`, or `model_governance_needed`. | Missing review defaults to blocked. |
| `gate_status` | `public_schema_only`, `public_fixture_only`, `private_lab_needed`, `clinical_team_needed`, `legal_needed`, `regulatory_needed`, `publication_gate_needed`, or `blocked_patient_specific`. | Gate labels do not authorize public output. |
| `refusal_reason` | Stable refusal code such as `no_model_weights`, `no_prediction_allowed`, `real_case_blocked`, `clinical_use_blocked`, or `publication_gate_needed`. | Refusal must be explicit, not implied. |
| `allowed_public_successor` | `validator_rule_map`, `source_extraction_task`, `expert_review_question`, `synthetic_fixture_update`, or `blocked_only`. | Successor must be public-safe and non-advisory. |
| `blocked_downstream_uses` | List of blocked uses from the blocked-use table below. | Blocks travel with the placeholder. |

## Blocked Downstream Uses

The wrapper must refuse any request that asks for or implies:

| Blocked Use | Refusal Label |
| --- | --- |
| diagnosis, disease-state determination, staging, relapse classification, or refractory classification for a person | `diagnosis_or_classification_blocked` |
| prognosis, progression risk, survival estimate, urgency, or monitoring action for a person | `prognosis_or_monitoring_blocked` |
| response probability, MRD interpretation, complete-response interpretation, durability interpretation, or cure wording for a person | `endpoint_interpretation_blocked` |
| resistance attribution, mechanism ranking, target selection, or actionability for a person | `resistance_or_actionability_blocked` |
| treatment recommendation, therapy sequencing, product comparison, regimen selection, or safety-management advice | `treatment_guidance_blocked` |
| trial recommendation, trial matching, eligibility, availability, access, or expanded-access guidance | `trial_or_access_guidance_blocked` |
| candidate options, patient matching, target ranking, mechanism ranking, evidence ranking, source ranking, or route ranking | `matching_or_ranking_blocked` |
| publication authorization, case-derived claim release, clinical decision, treating-team decision, sponsor decision, institutional decision, legal decision, or regulatory decision | `decision_authorization_blocked` |

## Fail-Closed Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `mob_00_no_real_case_input` | Model-output placeholders cannot accept real case data, identifiers, records, reports, images, raw files, exact person-linked dates, private correspondence, or free-text case details. | Refuse and route to `private_lab_needed`; no public output. |
| `mob_01_no_model_weights` | The public repo cannot contain or imply model weights, trained heads, prediction APIs, scoring code, thresholds, cut points, or calibration artifacts. | Keep `head_status` as `not_implemented` or `calibration_needed`. |
| `mob_02_no_prediction_values` | Public placeholders cannot contain scores, probabilities, risk categories, response categories, MRD labels, resistance labels, or ranked mechanisms for a person. | Refuse with `no_prediction_allowed`. |
| `mob_03_missingness_not_absence` | Missing DNA, RNA, single-cell, clinical, therapy, measurement, or evidence fields cannot imply absence, normality, lower risk, safety, treatment fit, trial fit, or no need for review. | Preserve missingness and uncertainty states. |
| `mob_04_measurement_guardrail` | MRD, complete response, response depth, relapse, progression, and endpoint language must follow the measurement normalization contract and MRD endpoint guardrail addendum. | Refuse endpoint interpretation and cure wording. |
| `mob_05_therapy_non_advice` | Therapy-exposure context can describe class and timing buckets only; it cannot sequence, compare, recommend, or rank therapies. | Refuse treatment guidance and ranking. |
| `mob_06_molecular_non_actionability` | Molecular and immune fields can preserve source-defined context only; they cannot create actionability, target selection, test guidance, trial fit, or treatment fit. | Refuse actionability and trial/treatment use. |
| `mob_07_evidence_not_matching` | Evidence packet IDs, query IDs, and source IDs cannot match a person to sources, mechanisms, products, trials, options, or actions. | Preserve provenance only or refuse. |
| `mob_08_review_gate_required` | Source appraisal, expert review, molecular review, measurement review, clinician review, privacy review, publication gate, and model governance states must remain visible. | Default to `review_needed` or `publication_gate_needed`. |
| `mob_09_no_clinical_guidance` | No placeholder output can provide diagnosis, prognosis, treatment, trial, expanded-access, monitoring, urgency, safety-management, publication, or clinical-decision output. | Refuse and route to the appropriate gate label. |
| `mob_10_no_cure_claim` | MRD negativity, complete response, response depth, resistance mechanism, or modeled trajectory language cannot be converted into a cure or vaccine claim. | Refuse cure wording and require expert review. |
| `mob_11_modality_discordance_refusal` | A future wrapper may expose residual-disease modality discordance or missing modality context, but it cannot output what that means for a person. | Preserve `modality_discordance_visible` or `modality_context_missing`; refuse prognosis, endpoint interpretation, monitoring, treatment, ranking, matching, and decisions. |
| `mob_12_assay_specimen_quality_refusal` | A future wrapper may expose missing method, threshold, specimen quality, timepoint alignment, paired modality, imaging criteria, spatial sampling, host-context separation, private review need, or modality collapse, but it cannot explain what that means for a person. | Preserve `assay_specimen_quality_needed` and the specific checklist state; refuse comparison, endpoint interpretation, prognosis, monitoring, treatment, ranking, matching, and decisions. |

## Synthetic Fixture Alignment

| Fixture ID | Expected Wrapper Behavior | Public Safety Property |
| --- | --- | --- |
| `synthetic_state_complete_multimodal_v0` | All four output families may be present only as `research_head_placeholder`, `calibration_needed`, or `not_implemented`; no values are populated. | Complete synthetic modalities do not authorize predictions or advice. |
| `synthetic_state_missing_rna_v0` | Transcriptome-dependent placeholders must carry `missing_modality_visible` and `calibration_needed`. | Missing RNA is visible and cannot be treated as normal expression. |
| `synthetic_state_missing_single_cell_v0` | Marrow ecosystem placeholders must carry `missing_modality_visible`; other families remain review-gated. | Optional single-cell data can be absent without implying immune normality. |
| `synthetic_state_private_source_blocked_v0` | Every output family must carry `blocked_private_source`, `publication_gate_needed`, and `blocked_patient_specific` where applicable. | Private-source status blocks public interpretation and publication. |
| `synthetic_state_residual_modality_discordance_v0` | MRD-family placeholders must carry `modality_discordance_visible`, `modality_context_missing`, or `modality_collapse_blocked`; no values are populated. | Discordance is visible as a refusal reason and cannot produce endpoint interpretation, prognosis, monitoring, treatment, ranking, or decisions. |
| `measurement-state-refusal-fixtures-v0` | MRD-family placeholders must carry `assay_specimen_quality_needed` plus one specific checklist state: `method_family_needed`, `threshold_needed`, `specimen_quality_needed`, `timepoint_alignment_needed`, `paired_modality_context_needed`, `imaging_context_needed`, `spatial_sampling_context_needed`, `host_context_not_residual_disease`, `private_lab_or_clinical_review_needed`, or `modality_collapse_blocked`; no values are populated. | Missing quality context is visible as a refusal reason and cannot produce comparison, endpoint interpretation, prognosis, monitoring, treatment, ranking, matching, real-report review, lab-validity conclusions, imaging interpretation, biopsy interpretation, or decisions. |
| `measurement-refusal-output-fixture-v0` | Every measurement refusal output record must be `refused`, carry `assay_specimen_quality_needed`, preserve the source fixture's specific checklist state, block all downstream clinical/ranking/interpretive uses, and expose no interpretive text. | Refusal states can be routed or checked without producing MRD interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, publication authorization, or decisions. |
| `measurement-refusal-output-route-table-v0` | Every refused output record must have exactly one route record, preserve source fixture and checklist state, keep complete blocked downstream uses, and route only to safe refusal metadata surfaces. | Routed refusals can feed future synthetic validators or wrappers without producing interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, publication authorization, or decisions. |
| `measurement-refusal-validator-skeleton-report-v0` | The validator report must carry `measurement-refusal-validator-skeleton-v0`, pass all structural rules, cover ten routed outputs, keep nine refusal-metadata routes plus one private-review blocker, and emit no clinical or comparison fields. | Structural validation reports can document refusal-route integrity without producing interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, publication authorization, or decisions. |
| `measurement-refusal-negative-safety-fixtures-v0` | Negative fixtures must make the validator fail closed on synthetic missing routes, duplicate routes, unsafe contracts, unsafe route families, forbidden clinical fields, forbidden ranking fields, and public processing of private quality-review routes. | Bad refusal routes are rejected before any wrapper dry run can reuse them, without producing interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, publication authorization, or decisions. |
| `measurement-refusal-wrapper-integration-dry-run-v0` | Every refused output record maps to one `mrd_head` wrapper metadata record with `head_status: assay_specimen_quality_needed`; the private-review row stays `private_lab_needed`. | Refused measurement records can touch the wrapper only as metadata, without producing prediction, interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, real-review, publication authorization, or decisions. |
| `measurement-refusal-wrapper-negative-safety-fixtures-v0` | Negative fixtures must make the wrapper dry-run checker fail closed on synthetic boundary poisoning, missing boundaries, missing or duplicate wrapper records, wrong wrapper IDs, unsafe output families, enabled clinical or prediction output, private-review unblocking, expanded wrapper boundaries, missing blocked uses, and forbidden clinical or ranking fields. | Unsafe wrapper metadata mutations are rejected before a wrapper state machine or model-facing artifact can reuse them, without producing prediction, interpretation, comparison, lab validity, prognosis, monitoring, treatment, matching, ranking, real-review, publication authorization, or decisions. |
| `measurement-refusal-wrapper-state-machine-v0` | Every wrapper record traces through safe refusal states to a public metadata-only terminal or private/real-review blocker terminal, and every wrapper negative-safety fixture routes to an unsafe-reuse blocked terminal. | Wrapper movement is explicit transition metadata only; it cannot emit model output, prediction, interpretation, comparison, ranking, real-review, publication authorization, clinical decisions, or cure claims. |

## What This Step Revealed

The residual-disease modality-discordance source extraction adds a more precise MRD-head refusal state: one modality cannot stand in for all residual-disease context. The later [Assay Specimen Quality Failure Mode Checklist v0](measurements/assay-specimen-quality-failure-mode-checklist-v0.md) adds the next refusal layer: method, threshold, specimen quality, timing alignment, paired modality, imaging criteria, spatial sampling, host-context separation, private review, and modality collapse must fail closed before the wrapper can even expose discordance. The [Measurement State Refusal Fixtures v0](../../examples/measurement-state-refusal-fixtures-v0.json) now pressure-test every one of those states, [Measurement Refusal Output Schema v0](../../schemas/measurement-refusal-output-schema-v0.md) turns them into checked refused output records, [Measurement Refusal Output Route Table v0](measurements/measurement-refusal-output-route-table-v0.md) routes those records only as refusal metadata, [Measurement Refusal Validator Skeleton v0](measurements/measurement-refusal-validator-skeleton-v0.md) emits a structural report over that route table, [Measurement Refusal Negative Safety Fixtures v0](measurements/measurement-refusal-negative-safety-fixtures-v0.md) prove the validator fails closed on bad route mutations, [Measurement Refusal Wrapper Integration Dry Run v0](measurements/measurement-refusal-wrapper-integration-dry-run-v0.md) maps the refused outputs to wrapper metadata only, [Measurement Refusal Wrapper Negative Safety Fixtures v0](measurements/measurement-refusal-wrapper-negative-safety-fixtures-v0.md) prove unsafe wrapper mutations fail closed, and [Measurement Refusal Wrapper State Machine v0](measurements/measurement-refusal-wrapper-state-machine-v0.md) now makes the safe terminal transitions explicit. The wrapper may expose `modality_discordance_visible`, `modality_context_missing`, or `assay_specimen_quality_needed`, but only as reasons to refuse interpretation, prediction, monitoring, treatment, ranking, matching, real-report review, or decisions.

The synthetic fixture repeats the same blocked-output manifest across scenarios.
That repetition is useful: the safest reusable unit is a small wrapper that
names output families, required refusal fields, uncertainty states, review
states, and blocked downstream uses before any validator or future model-facing
artifact can reference progression, response, MRD, or resistance heads.

The next safest public step is therefore `myeloma-state-validator-rule-map-v0`:
a no-code validator rule map that connects the state-object schema, synthetic
fixtures, and this wrapper to stable fail-closed checks.

That validator rule map is now complete as
[Myeloma State Validator Rule Map v0](myeloma-state-validator-rule-map-v0.md).
The source-extraction table is now complete as
[Machine Representation Source Extraction v0](machine-representation-source-extraction-v0.md).
The next safest public step is `machine-representation-source-gap-task-queue-v0`,
a contribution-ready public task queue for source-context gaps.

## Handoff State

`model-output-boundary-wrapper-v0` is complete as a public no-code boundary
protocol.

The following remain blocked outside this artifact:

- executable public model-output validation for real case data
- public uploads, accounts, storage, raw records, sequencing files, reports,
  notes, exact dates, images, accessions, private paths, or re-identification
  keys
- model weights, prediction heads, scoring functions, thresholds,
  probabilities, risk categories, response probabilities, MRD interpretations,
  resistance calls, treatment guidance, trial guidance, monitoring guidance,
  expanded-access guidance, matching, ranking, publication authorization, or
  clinical decisions
- publication of case-derived machine-state outputs without privacy,
  clinician, source-validity, expert-review, legal, regulatory, model
  governance, and publication gates

ORP has marked this item complete. The validator rule map and
source-extraction table are complete, and the next public-safe active item
should be `machine-representation-source-gap-task-queue-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, raw sequencing records, portal exports, accessions, private
  paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case state object.
- No model weights, scores, probabilities, thresholds, predictions, diagnosis,
  prognosis, treatment, trial, eligibility, expanded-access, monitoring,
  urgency, safety-management, publication, or candidate-option guidance.
- No patient matching, trial matching, target ranking, mechanism ranking,
  option ranking, evidence ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public no-code boundary protocol, not an executable validator.
- This is not a real model-output record.
- This does not process, normalize, store, route, publish, predict, compare,
  rank, or authorize use of real case, molecular, therapy, measurement,
  evidence, or review data.
- This does not complete consent, privacy, security, retention,
  clinician-review, source-validity, lab-validity, molecular-review,
  expert-review, legal, regulatory, institutional, sponsor, site,
  treating-team, publication, or model-governance gates.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, regulatory-ready,
  calibrated, generalizable, or clinically useful.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decisions.
- This does not claim that multiple myeloma has been cured or that a vaccine
  has been found.
