# Myeloma State Object Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `myeloma-state-object-schema-v0`
- active ORP item: `myeloma-state-object-schema-v0`
- schema status: public markdown schema contract
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: synthetic-only; no real case data, identifiers, raw records,
  uploads, exact person-linked dates, free-text case details, model weights,
  predictions, recommendations, matching, ranking, or clinical decisions
- last reviewed: `2026-04-18`

## Purpose

This schema defines the first public, model-facing myeloma disease-state object
for synthetic examples and future private, governed normalization work.

It translates the myeloma machine representation stack into a public-safe
object shape with source context, modality-specific feature families,
missingness, uncertainty, and review gates. It is not a public intake record, a
normalizer, a model, a predictor, a treatment selector, a trial matcher, or a
clinical decision system.

## Schema Decision

Current decision: `markdown-schema-contract-only`.

The object may be used for:

- schema planning
- synthetic fixture design
- public validator design
- source-extraction task routing
- expert review of field boundaries

The object must not be used for:

- collecting, storing, normalizing, uploading, transmitting, interpreting, or
  publishing real case data
- generating patient-specific diagnosis, prognosis, progression risk,
  response probability, MRD interpretation, resistance calls, treatment advice,
  trial advice, monitoring advice, expanded-access guidance, option ranking,
  or clinical decisions
- training, fine-tuning, serving, comparing, or validating model weights

## Top-Level Object

Every public-safe myeloma state object should be representable with these
top-level families. Only `state_object_metadata`, `source_context`,
`missingness_and_uncertainty`, `review_and_gate_state`, and
`blocked_output_manifest` are required for every object. Modality-specific
families are optional and must carry explicit missingness when absent.

| Family | Required Shape | Public Boundary |
| --- | --- | --- |
| `state_object_metadata` | Schema version, object kind, disease program, synthetic status, object scope, and public export verdict. | No private case IDs, names, record IDs, accessions, source paths, or re-identification keys. |
| `source_context` | Source IDs, source type, source status, method state, specimen or model context, timepoint bucket, access-date state, and provenance review status. | Missing source context blocks interpretation and downstream reuse. |
| `disease_state_context` | Source-stated context bucket, source-defined disease setting, precursor or active-disease state when public-source-defined, and limitation state. | Does not diagnose, stage, classify relapse, classify refractory status, or estimate prognosis for a person. |
| `tumor_genomic_events` | SNV/indel, copy-number, structural variant, translocation, clonality, mutational-process, and high-risk genomic field groups. | Missing assay or threshold remains `unknown`, `not_tested`, or `not_collected`; never infer absence. |
| `transcriptome_state` | Expression-subtype probability state, pathway/program summaries, proliferation or stress program state, and latent embedding reference state. | Missing RNA is a missing modality, not normal expression. |
| `marrow_ecosystem_state` | Cell-type abundance state, immune program state, exhaustion/senescence/inflammatory program state, ligand-receptor summary state, and single-cell availability state. | Missing single-cell marrow data must not block the full state object or imply immune normality. |
| `clinical_context` | Bucketed source-defined clinical context, organ/bone context, frailty/performance context, staging context, and high-risk context links. | Buckets only; no real values, exact dates, personal constraints, prognosis, eligibility, or care-path output. |
| `treatment_timeline` | Therapy class exposure state, line or timing bucket, response linkage state, refractory/resistance context, toxicity/constraint category, and therapy review state. | Follows the therapy exposure contract; no sequencing, availability, eligibility, access, or treatment guidance. |
| `measurement_timeline` | MRD, response, relapse/progression, lab, imaging, endpoint, method, threshold, sample, timepoint, and duration state. | Follows the measurement contract; no response assessment, monitoring guidance, prognosis, or cure language. |
| `evidence_links` | Evidence packet IDs, source registry IDs, query record IDs, public artifact IDs, extraction task IDs, and no-completeness warning state. | Evidence links do not rank sources, match a patient, prove actionability, or authorize publication. |
| `missingness_and_uncertainty` | Modality presence flags, missingness reason, source limitations, assay limitations, cohort-shift warnings, calibration state, and uncertainty state. | Missingness is never evidence of absence, lower risk, safety, treatment fit, trial fit, monitoring need, or cure. |
| `review_and_gate_state` | Review status, gate labels, private-lab need, clinician-review need, source-appraisal need, publication-gate need, and allowed public successor. | Missing review defaults to blocked or review-needed. |
| `blocked_output_manifest` | Explicit booleans or refusal labels for diagnosis, prognosis, treatment, trial, monitoring, expanded access, matching, ranking, publication, and clinical decision outputs. | Must be present so downstream tools refuse unsafe use by default. |

## Required Core Fields

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `schema_id` | `myeloma-state-object-schema-v0`. | Schema ID only; not a case ID. |
| `schema_version` | `v0`. | Public schema version only. |
| `object_kind` | `synthetic_fixture`, `public_schema_test`, `public_source_summary`, or `private_future_shape_placeholder`. | Public objects cannot be real case records. |
| `synthetic_status` | `synthetic_only`, `public_source_only`, `private_future_shape_placeholder`, or `blocked_real_case`. | Any real case value forces `blocked_real_case`. |
| `disease_program` | `multiple-myeloma`. | Disease label does not diagnose a person. |
| `source_ids` | Public source IDs or `source_id_needed`. | Source IDs are required before claim-like reuse. |
| `source_status` | `public_source_only`, `synthetic_source`, `source_missing`, `private_source_needed`, `source_seen_private`, or `not_collected`. | Public artifacts may preserve source status, not private contents. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `follow_up`, `study_visit_source_defined`, `unknown`, or `not_collected`. | Buckets only; no exact dates tied to a person. |
| `review_status` | `public_shape_only`, `not_reviewed`, `source_appraisal_needed`, `molecular_review_needed`, `measurement_review_needed`, `clinician_review_needed`, `privacy_review_needed`, `publication_gate_needed`, or `reviewed_private`. | Missing review blocks interpretation. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Modality Field Pattern

Each modality-specific field should use the same public pattern:

| Field | Meaning | Boundary |
| --- | --- | --- |
| `field_group_id` | Stable family label such as `tumor_genomic_events` or `measurement_timeline`. | Family label only. |
| `field_id` | Stable public field name. | Must not contain identifiers, exact dates, report text, facility names, clinician names, accessions, or private source paths. |
| `value_state` | `source_defined_category`, `source_defined_numeric_bucket`, `unknown`, `not_sure`, `not_tested`, `not_collected`, `source_missing`, `not_reported_by_source`, `private_only`, `synthetic_placeholder`, or `blocked_from_public`. | Missingness is preserved; absence is never inferred. |
| `method_state` | `source_defined_method`, `method_needed`, `method_not_reported`, `not_applicable`, or `private_only`. | Methods must be visible before comparing, interpreting, or reusing terms. |
| `specimen_or_model_context` | `bone_marrow`, `blood`, `tumor_normal_dna`, `bulk_rna`, `single_cell_marrow`, `clinical_record_private`, `public_cohort`, `model_system`, `context_needed`, or `not_applicable`. | Context does not authorize patient-specific interpretation. |
| `linkage_state` | `measurement_contract_linked`, `therapy_contract_linked`, `molecular_immune_contract_linked`, `evidence_packet_linked`, `linkage_needed`, or `not_applicable`. | Linkage preserves provenance only; it cannot create guidance. |
| `uncertainty_state` | `source_limit`, `assay_limit`, `method_limit`, `missing_modality`, `population_mismatch`, `cohort_shift_warning`, `calibration_needed`, `expert_review_needed`, `unknown`, or `none_stated_by_source`. | Uncertainty must travel with downstream outputs. |
| `limitation_note_required` | `true`. | Every field group needs a limitation note before reuse. |

## Missingness States

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `unknown` | The public or private source context does not know. | Preserve as uncertainty; do not infer a finding. |
| `not_sure` | The source or reporter is unsure. | Preserve uncertainty; do not convert to present or absent. |
| `not_tested` | A test or modality is not known to have occurred. | Do not infer absence of a feature or need for testing. |
| `not_collected` | The public-safe shape did not collect the field. | Do not infer that private records lack it. |
| `not_reported_by_source` | A public source did not report the field. | Preserve missingness and add a limitation note. |
| `source_missing` | A named concept lacks source context. | Mark source-context-needed before reuse. |
| `private_only` | The detail may exist only in a governed private workspace. | Do not project into public artifacts. |
| `blocked_from_public` | The detail is unsafe to reuse publicly. | Remove, rewrite as a generic task, or keep private. |

## Prediction-Head Boundary Fields

The machine representation stack names possible research heads for
progression, response, MRD, and resistance attribution. This schema may reserve
head-boundary fields, but it must not populate predictions.

| Boundary Field | Allowed Value | Required Refusal |
| --- | --- | --- |
| `progression_head_status` | `not_implemented`, `research_head_placeholder`, `calibration_needed`, or `blocked_patient_specific`. | No prognosis or risk estimate for a person. |
| `response_head_status` | `not_implemented`, `research_head_placeholder`, `calibration_needed`, or `blocked_patient_specific`. | No response prediction, regimen recommendation, or ranking. |
| `mrd_head_status` | `not_implemented`, `research_head_placeholder`, `calibration_needed`, or `blocked_patient_specific`. | No MRD interpretation, monitoring output, or cure wording. |
| `resistance_attribution_head_status` | `not_implemented`, `research_head_placeholder`, `calibration_needed`, or `blocked_patient_specific`. | No patient-specific resistance call, target selection, or trial direction. |
| `model_weight_status` | `absent`. | Public repo contains no model weights. |
| `clinical_use_status` | `not_allowed`. | Not medical advice and not clinical decision support. |

## Fail-Closed Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `mso_00_no_real_case_object` | A public state object must not contain a real case, identifier, report, image, raw molecular file, note, accession, exact person-linked date, facility, clinician, private path, or free-text case detail. | Block public export and move to private-lab-needed. |
| `mso_01_source_context_required` | Claim-like field reuse requires source IDs, source status, method/specimen context, timepoint bucket, review status, and limitation note. | Mark `source_context_needed`; block interpretation. |
| `mso_02_missingness_not_absence` | Missing DNA, RNA, single-cell, clinical, treatment, or measurement data cannot imply absence, lower risk, normal state, eligibility, safety, or no need for review. | Preserve explicit missingness and uncertainty. |
| `mso_03_modality_optional_not_silent` | Optional modality families may be absent only with visible missingness reason and uncertainty state. | Add missing-modality flag before downstream reuse. |
| `mso_04_measurement_routes_to_contract` | MRD, response, relapse, lab, imaging, endpoint, method, threshold, sample, and timepoint fields must follow the measurement normalization contract. | Block measurement interpretation and cure wording. |
| `mso_05_therapy_routes_to_contract` | Therapy exposure, line, response linkage, toxicity, constraint, refractory, transplant, cellular therapy, or trial-exposure fields must follow the therapy exposure contract. | Block sequencing, eligibility, access, treatment, and ranking language. |
| `mso_06_molecular_routes_to_contract` | Cytogenetic, genomic, target-assay, pathology, flow, immune, and assay-validity fields must follow the molecular immune context contract. | Block actionability, test guidance, treatment fit, trial fit, and target ranking. |
| `mso_07_evidence_links_not_matching` | Evidence links, source IDs, and query IDs cannot match a person to evidence, products, trials, targets, or options. | Preserve provenance only or block. |
| `mso_08_prediction_heads_empty` | Public artifacts cannot populate patient-specific prediction heads. | Keep as `not_implemented` or `blocked_patient_specific`. |
| `mso_09_review_gate_required` | Review and gate status must be visible before any downstream reuse. | Default to review-needed or publication-gate-needed. |
| `mso_10_no_clinical_guidance` | The object cannot generate diagnosis, prognosis, treatment, trial, expanded-access, monitoring, urgency, referral, publication, or clinical-decision outputs. | Refuse and route to the appropriate private, clinical, legal, regulatory, or publication gate. |

## Synthetic Object Expectations

Future synthetic fixtures should include visibly artificial state objects only.
The first fixture set should cover:

| Fixture ID | Purpose | Required Safety Property |
| --- | --- | --- |
| `synthetic_state_complete_multimodal_v0` | Exercises all modality families with synthetic placeholders and public-source links. | Clearly synthetic; no real values, no exact dates, no model outputs. |
| `synthetic_state_missing_rna_v0` | Exercises missing transcriptome rules. | Missing RNA stays `missing_modality`; no normal-expression inference. |
| `synthetic_state_missing_single_cell_v0` | Exercises optional marrow ecosystem rules. | Missing single-cell data does not block the state object or imply immune normality. |
| `synthetic_state_private_source_blocked_v0` | Exercises private-source and publication-gate refusals. | Public export remains blocked and no private content appears. |

The first fixture file is now
[Synthetic Myeloma State Fixture v0](../examples/synthetic-myeloma-state-fixture-v0.json).
It exercises the scenarios below without real case data, model outputs, or
clinical guidance.

## What This Step Revealed

The machine representation stack can be translated into a public schema only
when the schema separates required provenance and review metadata from optional
modality families. The highest-risk fields are not the genomic or RNA labels
themselves; the risk is silent missingness and downstream prediction-head
language that could look like prognosis, treatment selection, trial matching,
or resistance interpretation.

The model-output boundary wrapper is now complete as
[Model Output Boundary Wrapper v0](../disease-programs/multiple-myeloma/model-output-boundary-wrapper-v0.md),
which defines refusal and uncertainty rules for progression, response, MRD, and
resistance head placeholders before any downstream model-facing work appears.
The next safest public step is `myeloma-state-validator-rule-map-v0`, a no-code
rule map that connects the schema, synthetic fixture, and wrapper to
fail-closed checks.

That validator rule map is now complete as
[Myeloma State Validator Rule Map v0](../disease-programs/multiple-myeloma/myeloma-state-validator-rule-map-v0.md).
The source-extraction table is now complete as
[Machine Representation Source Extraction v0](../disease-programs/multiple-myeloma/machine-representation-source-extraction-v0.md).
The next safest public step is `machine-representation-source-gap-task-queue-v0`.

## Handoff State

`myeloma-state-object-schema-v0` is complete as a public markdown schema
contract.

The following remain blocked outside this artifact:

- executable public normalization of real case data
- public uploads, save/resume workflows, accounts, storage, raw records,
  sequencing files, reports, notes, exact dates, images, accessions, private
  paths, or re-identification keys
- model weights, prediction heads, patient-specific progression risk, response
  probability, MRD interpretation, resistance attribution, treatment guidance,
  trial guidance, monitoring guidance, expanded-access guidance, matching,
  ranking, publication authorization, or clinical decisions
- publication of case-derived machine-state learning without privacy,
  clinician, source-validity, expert-review, legal, regulatory, and
  publication gates

ORP has marked this item complete. The synthetic fixture, model-output wrapper,
validator rule map, and source-extraction items are complete, and the next
public-safe active item should be
`machine-representation-source-gap-task-queue-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, raw sequencing records, portal exports, accessions, private
  paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case state object.
- No model weights, predictions, diagnosis, prognosis, treatment, trial,
  eligibility, expanded-access, monitoring, urgency, safety-management,
  publication, or candidate-option guidance.
- No patient matching, trial matching, target ranking, mechanism ranking,
  option ranking, evidence ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public markdown schema contract, not executable JSON Schema.
- This is not a real myeloma state object.
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
  expanded-access guidance, monitoring guidance, urgency guidance, emergency
  guidance, or a cure claim.
