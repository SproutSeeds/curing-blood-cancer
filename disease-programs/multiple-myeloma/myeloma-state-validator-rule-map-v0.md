# Myeloma State Validator Rule Map v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `myeloma-state-validator-rule-map-v0`
- active ORP item: `myeloma-state-validator-rule-map-v0`
- map status: public no-code validator rule map
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: synthetic-only and public-source-scoped; no real case data,
  identifiers, raw records, uploads, exact person-linked dates, free-text case
  details, private correspondence, model weights, predictions,
  recommendations, matching, ranking, or clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This map names the first public validator rules for the myeloma machine-state
substrate.

It connects the
[Myeloma State Object Schema v0](../../schemas/myeloma-state-object-schema-v0.md),
[Synthetic Myeloma State Fixture v0](../../examples/synthetic-myeloma-state-fixture-v0.json),
and [Model Output Boundary Wrapper v0](model-output-boundary-wrapper-v0.md)
to stable rule IDs, required fields, synthetic coverage, fail-closed actions,
blocked-use labels, and allowed public successors.

It is not executable validation code. It is not a real-case validator, intake
validator, model validator, scoring system, clinical safety system, publication
gate, treatment selector, trial matcher, monitoring tool, or clinical decision
system.

## Rule Map Decision

Current decision: `no-code-rule-map-only`.

The map may be used for:

- future public validator design
- synthetic fixture checks
- review-packet planning
- source-extraction task routing
- public safety review of rule coverage

The map must not be used for:

- accepting, validating, normalizing, scoring, interpreting, publishing, or
  routing real case data
- generating patient-specific diagnosis, prognosis, progression risk,
  response probability, MRD interpretation, resistance attribution, treatment
  advice, trial advice, monitoring advice, expanded-access guidance, matching,
  ranking, publication authorization, or clinical decisions
- training, fine-tuning, serving, comparing, or validating model weights

## Rule Record Shape

Every future executable validator rule should be traceable to this public shape
before implementation.

| Field | Required Public Shape | Boundary |
| --- | --- | --- |
| `rule_id` | Stable ID from this map. | Rule ID only; not a case ID, model ID, or prediction ID. |
| `owner_artifact_id` | Source artifact that owns the boundary. | Owner link does not authorize real-data use. |
| `source_rule_id` | Existing rule ID such as `mso_00_no_real_case_object` or `mob_02_no_prediction_values`, or `new_rule_needed`. | Source rule anchors provenance only. |
| `required_public_fields` | List of fields that must be visible in public synthetic objects or wrapper records. | Required fields are shape checks, not clinical fields. |
| `synthetic_coverage` | Fixture IDs or `fixture_needed`. | Coverage must be visibly artificial. |
| `pass_condition` | Structural public condition. | A pass does not mean clinical readiness or publication approval. |
| `fail_closed_action` | Refusal, blocker, or review-needed state. | Failure cannot fall back to inference. |
| `blocked_use_labels` | Refusal labels that travel with the failure. | Blocks cannot be suppressed downstream. |
| `allowed_public_successor` | `synthetic_fixture_update`, `source_extraction_task`, `expert_review_question`, `validator_implementation_plan`, `wrapper_integration_dry_run`, `wrapper_negative_safety_fixture_update`, `wrapper_state_machine`, or `blocked_only`. | Successor must stay public-safe and non-advisory. |
| `review_status` | `public_shape_only`, `source_appraisal_needed`, `expert_review_needed`, `privacy_review_needed`, `publication_gate_needed`, or `model_governance_needed`. | Missing review defaults to blocked. |

## Core Rule Map

| Rule ID | Owner Artifact | Source Rule ID | Required Public Fields | Synthetic Coverage | Pass Condition | Fail-Closed Action | Blocked Use Labels | Allowed Public Successor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `msv_00_no_real_case_payload` | `myeloma-state-object-schema-v0` | `mso_00_no_real_case_object` | `state_object_metadata.synthetic_status`, `data_boundary`, `review_and_gate_state` | all fixture IDs | Object is synthetic-only, public-source-only, or private-future-shape placeholder and contains no identifier-like payload fields. | Set `blocked_real_case`; refuse public export; route to `private_lab_needed`. | `diagnosis_or_classification_blocked`, `decision_authorization_blocked` | `blocked_only` |
| `msv_01_required_core_metadata` | `myeloma-state-object-schema-v0` | `mso_01_source_context_required` | `schema_id`, `schema_version`, `object_kind`, `disease_program`, `review_status`, `public_export_allowed` | all fixture IDs | Core metadata exists and identifies only public schema state. | Mark `source_context_needed` or `review_needed`; block interpretation. | `decision_authorization_blocked` | `synthetic_fixture_update` |
| `msv_02_source_context_required` | `myeloma-state-object-schema-v0` | `mso_01_source_context_required` | `source_context.source_ids`, `source_status`, `method_state`, `specimen_or_model_context`, `timepoint_bucket`, `provenance_review_status` | complete multimodal and private-source-blocked fixtures | Source context is public, synthetic, or explicitly blocked; missing context is visible. | Mark `source_context_needed`; block reuse. | `diagnosis_or_classification_blocked`, `matching_or_ranking_blocked` | `source_extraction_task` |
| `msv_03_missingness_not_absence` | `myeloma-state-object-schema-v0` | `mso_02_missingness_not_absence` | `missingness_and_uncertainty.modality_flags`, `uncertainty_state`, field-level `value_state` | missing RNA and missing single-cell fixtures | Unknown, not-tested, not-collected, and missing-modality states remain visible and non-inferential. | Preserve missingness; add review-needed state; block interpretation. | `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `trial_or_access_guidance_blocked` | `synthetic_fixture_update` |
| `msv_04_modality_optional_not_silent` | `myeloma-state-object-schema-v0` | `mso_03_modality_optional_not_silent` | modality family presence flags, `missingness_reason`, `limitation_note_required` | missing RNA and missing single-cell fixtures | Optional RNA or single-cell families can be absent only with explicit reason and limitation. | Add missing-modality flag; block downstream reuse until visible. | `prognosis_or_monitoring_blocked`, `endpoint_interpretation_blocked` | `synthetic_fixture_update` |
| `msv_05_private_source_blocks_public_export` | `myeloma-state-object-schema-v0` | `mso_00_no_real_case_object` | `source_status`, `public_export_allowed`, `review_and_gate_state.publication_gate_needed` | private-source-blocked fixture | Private-source state keeps public export false and exposes no private content. | Refuse public export; route to privacy and publication gates. | `decision_authorization_blocked` | `blocked_only` |
| `msv_06_measurement_contract_linked` | `measurement-normalization-contract-v0` | `mso_04_measurement_routes_to_contract` | `measurement_timeline`, `method_state`, `sample`, `threshold`, `timepoint_bucket`, `endpoint_role`, `limitation_note_required` | complete multimodal fixture | Measurement terms are linked to method, sample, threshold, timepoint, and limitation context. | Block measurement interpretation and cure wording. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked` | `source_extraction_task` |
| `msv_07_therapy_contract_linked` | `therapy-exposure-timeline-contract-v0` | `mso_05_therapy_routes_to_contract` | `treatment_timeline`, `therapy_class_exposure`, `line_or_timing_bucket`, `response_linkage_state`, `therapy_review_state` | complete multimodal fixture | Therapy exposure fields remain descriptive and contract-linked. | Block sequencing, eligibility, access, treatment, and ranking language. | `treatment_guidance_blocked`, `trial_or_access_guidance_blocked`, `matching_or_ranking_blocked` | `source_extraction_task` |
| `msv_08_molecular_immune_contract_linked` | `molecular-immune-context-contract-v0` | `mso_06_molecular_routes_to_contract` | `tumor_genomic_events`, `transcriptome_state`, `marrow_ecosystem_state`, `method_state`, `specimen_or_model_context`, `uncertainty_state` | complete multimodal, missing RNA, and missing single-cell fixtures | Molecular and immune fields preserve source, method, specimen, and uncertainty context. | Block actionability, test guidance, target ranking, treatment fit, and trial fit. | `resistance_or_actionability_blocked`, `treatment_guidance_blocked`, `trial_or_access_guidance_blocked` | `source_extraction_task` |
| `msv_09_evidence_links_not_matching` | `evidence-retrieval-packet-v0` | `mso_07_evidence_links_not_matching` | `evidence_links.source_ids`, `public_artifact_ids`, `query_record_ids`, `no_completeness_warning_state` | complete multimodal fixture | Evidence links are provenance only and carry no match, rank, or completeness claim. | Preserve provenance only or refuse. | `matching_or_ranking_blocked`, `trial_or_access_guidance_blocked` | `source_extraction_task` |
| `msv_10_wrapper_required_for_output_families` | `model-output-boundary-wrapper-v0` | `mob_00_no_real_case_input` | `wrapper_id`, `output_family_id`, `requested_use`, `head_status`, `gate_status` | all fixture IDs | Any progression, response, MRD, or resistance placeholder references the wrapper. | Refuse output-family use until wrapper fields exist. | `prognosis_or_monitoring_blocked`, `endpoint_interpretation_blocked`, `resistance_or_actionability_blocked` | `validator_implementation_plan` |
| `msv_11_no_prediction_values` | `model-output-boundary-wrapper-v0` | `mob_02_no_prediction_values` | `head_status`, `refusal_reason`, `blocked_downstream_uses` | all fixture IDs | No score, threshold, probability, risk category, response category, MRD label, resistance label, or ranking is present. | Refuse with `no_prediction_allowed`. | `prognosis_or_monitoring_blocked`, `endpoint_interpretation_blocked`, `resistance_or_actionability_blocked` | `blocked_only` |
| `msv_12_blocked_use_manifest_required` | `model-output-boundary-wrapper-v0` | `mob_09_no_clinical_guidance` | `blocked_output_manifest`, `blocked_downstream_uses` | all fixture IDs | All diagnosis, prognosis, treatment, trial, monitoring, expanded-access, matching, ranking, publication, and decision outputs are visibly blocked. | Add or preserve blocked-use labels; refuse downstream use. | all blocked-use labels | `validator_implementation_plan` |
| `msv_13_review_gate_required` | `myeloma-state-object-schema-v0` and `model-output-boundary-wrapper-v0` | `mso_09_review_gate_required`, `mob_08_review_gate_required` | `review_and_gate_state`, `review_status`, `gate_status`, `allowed_public_successor` | all fixture IDs | Review and gate states are visible before reuse. | Default to `review_needed` or `publication_gate_needed`. | `decision_authorization_blocked` | `expert_review_question` |
| `msv_14_no_cure_or_clinical_guidance` | `model-output-boundary-wrapper-v0` | `mob_10_no_cure_claim` | `clinical_use_status`, `refusal_reason`, `blocked_downstream_uses` | all fixture IDs | No cure, vaccine, diagnosis, prognosis, treatment, trial, monitoring, urgency, or clinical-decision language appears. | Refuse unsafe language and require expert/publication review. | `diagnosis_or_classification_blocked`, `prognosis_or_monitoring_blocked`, `endpoint_interpretation_blocked`, `treatment_guidance_blocked`, `trial_or_access_guidance_blocked`, `decision_authorization_blocked` | `expert_review_question` |
| `msv_15_residual_modality_discordance_visible` | `residual-disease-modality-discordance-source-extraction-v0`, `measurement-normalization-contract-v0`, and `model-output-boundary-wrapper-v0` | `mnc_12_no_single_modality_global_state`, `mnc_13_modality_discordance_visible`, `mob_11_modality_discordance_refusal` | `residual_disease_modality_state`, modality family, method, sample/specimen, threshold or detection status, timepoint bucket, paired-state context, source context, `limitation_note_required` | residual modality discordance fixture needed | Discordance or missing modality context remains visible and no single modality becomes a global disease-state claim. | Preserve discordance, mark `modality_collapse_blocked`, and refuse output meaning. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `synthetic_fixture_update` |
| `msv_16_assay_specimen_quality_failure_mode_visible` | `assay-specimen-quality-failure-mode-checklist-v0`, `measurement-normalization-contract-v0`, and `model-output-boundary-wrapper-v0` | `mnc_14_assay_specimen_quality_before_discordance`, `mnc_15_real_quality_review_stays_private`, `mob_12_assay_specimen_quality_refusal` | `assay_specimen_quality_state`, method family, threshold or detection status, specimen quality, timepoint alignment, paired-modality context, imaging criteria when relevant, spatial sampling when relevant, host-context separation, review boundary, `limitation_note_required` | `measurement-state-refusal-fixtures-v0` | Missing quality context remains visible and no residual-disease comparison, endpoint interpretation, prognosis, monitoring, treatment, ranking, or decision is emitted. | Preserve the specific checklist state, mark `assay_specimen_quality_needed`, and refuse output meaning or route real-review requests to `private_lab_or_clinical_review_needed`. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `synthetic_fixture_update` |
| `msv_17_measurement_refusal_output_schema_visible` | `measurement-refusal-output-schema-v0`, `measurement-state-refusal-fixtures-v0`, and `model-output-boundary-wrapper-v0` | `mob_12_assay_specimen_quality_refusal` | `output_status`, `source_fixture_id`, `wrapper_state`, `assay_specimen_quality_state`, `refusal_reason`, `blocked_downstream_uses`, `clinical_output_allowed`, `comparison_allowed`, `no_interpretive_text` | `measurement-refusal-output-fixture-v0` | Every synthetic refusal fixture maps to one refused output record and carries the complete blocked downstream-use set. | Preserve the source fixture state, refuse output meaning, and block any interpretive field. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `validator_implementation_plan` |
| `msv_18_measurement_refusal_route_table_visible` | `measurement-refusal-output-route-table-v0`, `measurement-refusal-output-schema-v0`, and `model-output-boundary-wrapper-v0` | `mob_12_assay_specimen_quality_refusal` | `route_id`, `source_output_id`, `source_fixture_id`, `source_checklist_row_id`, `assay_specimen_quality_state`, `route_status`, `public_processing_allowed`, `allowed_route_families`, `destination_contracts`, `blocked_routes`, `route_boundary` | `measurement-refusal-output-route-table-v0` | Every refused output has exactly one route, safe destination contracts are explicit, private/real quality-review requests stay blocked, and forbidden clinical/ranking fields stay absent. | Preserve refusal metadata only; route to synthetic validator, wrapper refusal surface, public navigation, regression fixture, or blocker notice. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `validator_implementation_plan` |
| `msv_19_measurement_refusal_validator_skeleton_visible` | `measurement-refusal-validator-skeleton-v0`, `measurement-refusal-output-route-table-v0`, and `measurement-refusal-output-schema-v0` | `mob_12_assay_specimen_quality_refusal` | `validator_id`, `report_status`, `rules`, `summary`, `route_results`, `blocked_output_manifest`, `forbidden_output_fields`, `route_boundary` | `measurement-refusal-validator-skeleton-report-v0` | The executable skeleton checks the routed refusal records, passes all structural rules, emits only refusal metadata, and keeps the private/real quality-review route blocked. | Preserve validator/report metadata only; reject missing or unsafe routes and block clinical, comparison, ranking, prediction, recommendation, publication, and real-review output. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `negative_safety_fixture_update` |
| `msv_20_measurement_refusal_negative_safety_fixtures_visible` | `measurement-refusal-negative-safety-fixtures-v0`, `measurement-refusal-validator-skeleton-v0`, and `measurement-refusal-output-route-table-v0` | `mob_12_assay_specimen_quality_refusal` | `fixture_set_id`, `target_validator_id`, `negative_fixtures`, `mutations`, `expected_failed_rule_ids`, `data_boundary`, `handoff` | `measurement-refusal-negative-safety-fixtures-v0` | Eleven synthetic negative fixtures fail closed against expected validator rules. | Preserve bad-route fixture metadata only; reject missing routes, duplicate routes, unsafe destination contracts, unsafe route families, clinical/ranking fields, and public processing of private-review routes. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `wrapper_integration_dry_run` |
| `msv_21_measurement_refusal_wrapper_integration_dry_run_visible` | `measurement-refusal-wrapper-integration-dry-run-v0`, `model-output-boundary-wrapper-v0`, and `measurement-refusal-validator-skeleton-report-v0` | `mob_12_assay_specimen_quality_refusal` | `wrapper_integration_dry_run_id`, `target_wrapper_id`, `wrapper_records`, `head_status`, `output_family_id`, `requested_use`, `blocked_downstream_uses`, `handoff` | `measurement-refusal-wrapper-integration-dry-run-v0` | Ten refused measurement outputs map to ten wrapper metadata records; nine are public synthetic refusal records and one remains a private-review blocker. | Preserve wrapper metadata only; reject prediction, clinical, comparison, ranking, real-review, publication, and decision output. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `wrapper_negative_safety_fixture_update` |
| `msv_22_measurement_refusal_wrapper_negative_safety_fixtures_visible` | `measurement-refusal-wrapper-negative-safety-fixtures-v0`, `measurement-refusal-wrapper-integration-dry-run-v0`, and `model-output-boundary-wrapper-v0` | `mob_12_assay_specimen_quality_refusal` | `fixture_set_id`, `target_checker_id`, `target_dry_run_id`, `negative_fixtures`, `mutations`, `expected_failed_check_ids`, `data_boundary`, `handoff` | `measurement-refusal-wrapper-negative-safety-fixtures-v0` | Thirteen synthetic negative fixtures fail closed against expected wrapper dry-run checks. | Preserve unsafe-wrapper fixture metadata only; reject boundary poisoning, missing boundaries, missing or duplicate wrapper records, wrong wrapper IDs, unsafe output families, enabled clinical or prediction output, private-review unblocking, expanded wrapper boundaries, blocked-use gaps, and forbidden clinical/ranking fields. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `wrapper_state_machine` |
| `msv_23_measurement_refusal_wrapper_state_machine_visible` | `measurement-refusal-wrapper-state-machine-v0`, `measurement-refusal-wrapper-integration-dry-run-v0`, `measurement-refusal-wrapper-negative-safety-fixtures-v0`, and `model-output-boundary-wrapper-v0` | `mob_12_assay_specimen_quality_refusal` | `state_machine_id`, `states`, `transitions`, `wrapper_record_traces`, `blocked_transition_rules`, `transition_invariants`, `handoff` | `measurement-refusal-wrapper-state-machine-v0` | Eight safe states, seven safe transitions, ten wrapper-record traces, thirteen negative-fixture blocked rules, and eight invariants keep wrapper movement terminal and refusal-only. | Preserve wrapper transition metadata only; route public synthetic refusals to metadata-only terminal, private/real review to blocker terminal, and unsafe reuse to blocked terminal. | `endpoint_interpretation_blocked`, `prognosis_or_monitoring_blocked`, `treatment_guidance_blocked`, `matching_or_ranking_blocked`, `decision_authorization_blocked` | `wrapper_state_machine_negative_safety_fixture_update` |

## Synthetic Scenario Coverage

| Fixture ID | Required Rule Coverage | Expected Public Result |
| --- | --- | --- |
| `synthetic_state_complete_multimodal_v0` | `msv_00` through `msv_14`, with complete synthetic modality context. | Passes only as a synthetic shape check; prediction, advice, matching, ranking, and clinical use remain blocked. |
| `synthetic_state_missing_rna_v0` | `msv_00`, `msv_01`, `msv_02`, `msv_03`, `msv_04`, `msv_08`, `msv_10` through `msv_14`. | Missing RNA remains visible and cannot be treated as normal expression, lower risk, treatment fit, or no need for review. |
| `synthetic_state_missing_single_cell_v0` | `msv_00`, `msv_01`, `msv_02`, `msv_03`, `msv_04`, `msv_08`, `msv_10` through `msv_14`. | Missing single-cell marrow state remains visible and cannot imply immune normality or block the whole synthetic state. |
| `synthetic_state_private_source_blocked_v0` | `msv_00`, `msv_02`, `msv_05`, `msv_10`, `msv_11`, `msv_12`, `msv_13`, and `msv_14`. | Public export stays blocked; private-source status exposes no private content and cannot produce public interpretation. |
| `synthetic_state_residual_modality_discordance_v0` | `msv_00`, `msv_01`, `msv_02`, `msv_03`, `msv_06`, `msv_10` through `msv_15`. | Residual-disease modalities remain source-scoped and discordant/missing context refuses endpoint interpretation, prognosis, monitoring, treatment, ranking, and decisions. |
| `measurement-state-refusal-fixtures-v0` | `msv_00`, `msv_01`, `msv_02`, `msv_03`, `msv_06`, `msv_10` through `msv_16`. | Ten synthetic fixtures cover missing method, threshold, specimen quality, timing, paired modality, imaging criteria, spatial sampling, host-context separation, private review need, and modality collapse; each refuses comparison, endpoint interpretation, prognosis, monitoring, treatment, ranking, matching, report review, lab validity, imaging interpretation, biopsy interpretation, and decisions. |
| `measurement-refusal-output-fixture-v0` | `msv_10` through `msv_17`. | Ten refused output records preserve the source fixture state, carry the complete blocked downstream-use set, expose no interpretive text, and stop public processing for private/real quality-review requests. |
| `measurement-refusal-output-route-table-v0` | `msv_10` through `msv_18`. | Ten route records preserve the refused output state, keep destination contracts explicit, route normal synthetic refusals only to safe refusal surfaces, and route private/real quality-review requests only as public blocker notices. |
| `measurement-refusal-validator-skeleton-report-v0` | `msv_10` through `msv_19`. | The validator report passes seven structural rules over ten routes, emits refusal metadata only, and preserves one private-review blocker without clinical, comparison, ranking, prediction, recommendation, publication, or real-review output. |
| `measurement-refusal-negative-safety-fixtures-v0` | `msv_10` through `msv_20`. | Eleven negative fixtures mutate route safety and must fail closed for missing routes, duplicate routes, blocked-manifest gaps, unsafe destination contracts, unsafe route families, forbidden clinical/ranking fields, and public processing of private-review routes. |
| `measurement-refusal-wrapper-integration-dry-run-v0` | `msv_10` through `msv_21`. | Ten wrapper metadata records preserve refused output state, keep `mrd_head` as a placeholder family only, keep the private-review row blocked, and emit no prediction, interpretation, comparison, ranking, real-review, publication, or decision output. |
| `measurement-refusal-wrapper-negative-safety-fixtures-v0` | `msv_10` through `msv_22`. | Thirteen wrapper negative fixtures mutate wrapper metadata safety and must fail closed for boundary poisoning, missing boundaries, missing or duplicate wrapper records, wrong wrapper IDs, unsafe output families, enabled clinical or prediction output, private-review unblocking, expanded wrapper boundaries, blocked-use gaps, and forbidden clinical/ranking fields. |
| `measurement-refusal-wrapper-state-machine-v0` | `msv_10` through `msv_23`. | Eight wrapper transition states and seven transitions trace ten wrapper records to safe terminals and route thirteen unsafe-wrapper mutations to the blocked terminal without output emission. |

## Validator Implementation Boundary

A future executable validator may reference this map only if it stays within
these boundaries:

- synthetic fixtures and public metadata only
- structural checks only
- no real case payloads
- no raw records, reports, images, notes, exact person-linked dates, accessions,
  private paths, private correspondence, or re-identification keys
- no model weights, scores, thresholds, probabilities, categories,
  predictions, matches, rankings, recommendations, or clinical action text
- no publication authorization

Any request outside those boundaries must return a blocker state, not a partial
or inferred result.

## What This Step Revealed

Residual-disease modality-discordance extraction adds one important validator pressure: future checks must preserve modality disagreement as visible structure, not normalize it away. `msv_15` therefore bridges the measurement contract, output wrapper, and source extraction table before any executable validator or synthetic fixture can reuse discordant residual-disease context.

The later [Assay Specimen Quality Failure Mode Checklist v0](measurements/assay-specimen-quality-failure-mode-checklist-v0.md)
adds `msv_16`: future checks must preserve missing method, threshold, specimen
quality, timing alignment, paired modality, imaging criteria, spatial sampling,
host-context separation, private review need, and modality-collapse attempts as
visible refusal states before any residual-disease comparison can be tested.

The state-object schema, synthetic fixture, and output wrapper now form a
coherent public substrate, but their rules need explicit IDs before future
tools or review packets can cite them safely. The highest-value next unit is
source extraction for the machine-representation stack, because the rule map
now shows where architecture claims need exact source context before stronger
downstream use.

The next safest public step is therefore
`machine-representation-source-extraction-v0`: a public-source extraction table
that maps machine-representation claims to source IDs, source-context needs,
and expert-review needs without creating model code, predictions, advice,
matching, ranking, or patient-specific interpretation.

That source-extraction table is now complete as
[Machine Representation Source Extraction v0](machine-representation-source-extraction-v0.md).
The next safest public step is
`machine-representation-source-gap-task-queue-v0`.

The later [Measurement State Refusal Fixtures v0](../../examples/measurement-state-refusal-fixtures-v0.json)
now closes the `msv_16` fixture gap. The companion
[`measurement-state-refusal-fixture-check-v0`](../../tools/check_measurement_state_refusal_fixtures.py)
checks that all ten assay/specimen quality fail-closed states remain covered
and blocked in synthetic fixtures only.
The later [Measurement Refusal Output Fixture v0](../../examples/measurement-refusal-output-fixture-v0.json)
and [`measurement-refusal-output-schema-check-v0`](../../tools/check_measurement_refusal_output_schema.py)
close `msv_17` as a refused-output shape check, not as clinical validation or
model-output authorization.

The later [Measurement Refusal Output Route Table v0](measurements/measurement-refusal-output-route-table-v0.md)
and [`measurement-refusal-output-route-table-check-v0`](../../tools/check_measurement_refusal_output_route_table.py)
close `msv_18` as deterministic refusal routing for synthetic records only.
It does not authorize clinical interpretation, model output, real-report
review, ranking, publication, or patient-specific decisions.

The later [Measurement Refusal Validator Skeleton v0](measurements/measurement-refusal-validator-skeleton-v0.md)
and [`measurement-refusal-validator-skeleton-tool-v0`](../../tools/measurement_refusal_validator_skeleton.py)
close `msv_19` as executable structural validation over the refusal route
table. The generated report remains synthetic-only and does not authorize
clinical interpretation, comparison, ranking, model output, real-report review,
publication, or patient-specific decisions.

The later [Measurement Refusal Negative Safety Fixtures v0](measurements/measurement-refusal-negative-safety-fixtures-v0.md)
and [`measurement-refusal-negative-safety-fixture-check-v0`](../../tools/check_measurement_refusal_negative_safety_fixtures.py)
close `msv_20` by proving the validator fails closed on eleven synthetic bad
routes. The fixture pack carries no real case data, model output, clinical
interpretation, ranking, real-report review, publication authorization, or
patient-specific decision content.

The later [Measurement Refusal Wrapper Integration Dry Run v0](measurements/measurement-refusal-wrapper-integration-dry-run-v0.md)
and [`measurement-refusal-wrapper-integration-dry-run-check-v0`](../../tools/check_measurement_refusal_wrapper_integration_dry_run.py)
close `msv_21` by proving refused measurement outputs can touch the wrapper
only as refusal metadata. The dry run carries no model weights, prediction,
clinical interpretation, ranking, real-review output, publication
authorization, or patient-specific decision content.

The later [Measurement Refusal Wrapper Negative Safety Fixtures v0](measurements/measurement-refusal-wrapper-negative-safety-fixtures-v0.md)
and [`measurement-refusal-wrapper-negative-safety-fixture-check-v0`](../../tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py)
close `msv_22` by proving the wrapper dry-run surface fails closed on thirteen
synthetic unsafe wrapper mutations. The fixture pack carries no real case data,
model output, clinical interpretation, ranking, real-report review,
publication authorization, or patient-specific decision content.

The later [Measurement Refusal Wrapper State Machine v0](measurements/measurement-refusal-wrapper-state-machine-v0.md)
and [`measurement-refusal-wrapper-state-machine-check-v0`](../../tools/check_measurement_refusal_wrapper_state_machine.py)
close `msv_23` by making refusal-wrapper movement explicit as transition
metadata. Public synthetic refusals terminate as metadata-only, private or real
quality-review requests terminate as blockers, and unsafe wrapper reuse
terminates as blocked without model output, prediction, interpretation,
ranking, real-review, publication authorization, or patient-specific decision
content.

## Handoff State

`myeloma-state-validator-rule-map-v0` is complete as a public no-code rule map.

The following remain blocked outside this artifact:

- executable real-case validation
- public uploads, accounts, storage, raw records, sequencing files, reports,
  notes, exact dates, images, accessions, private paths, or re-identification
  keys
- model weights, scoring functions, prediction APIs, thresholds,
  probabilities, risk categories, response probabilities, MRD interpretations,
  resistance calls, treatment guidance, trial guidance, monitoring guidance,
  expanded-access guidance, matching, ranking, publication authorization, or
  clinical decisions
- publication of case-derived machine-state outputs without privacy,
  clinician, source-validity, expert-review, legal, regulatory, model
  governance, and publication gates

ORP has marked this item complete. The source-extraction table is complete, and
the next public-safe active item should be
`machine-representation-source-gap-task-queue-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, raw sequencing records, portal exports, accessions, private
  paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case state object.
- No model weights, executable validator, scores, probabilities, thresholds,
  predictions, diagnosis, prognosis, treatment, trial, eligibility,
  expanded-access, monitoring, urgency, safety-management, publication, or
  candidate-option guidance.
- No patient matching, trial matching, target ranking, mechanism ranking,
  option ranking, evidence ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public no-code rule map, not executable validator software.
- This is not a real validation result.
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
