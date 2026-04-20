# Measurement Normalization Contract v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-measurement-normalization-contract-v0`
- active ORP item: `measurement-normalization-contract-v0`
- contract status: public shape contract complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no records, no images,
  no raw lab values, no exact dates, no fillable public measurement record
- last reviewed: `2026-04-20`

## Purpose

This contract defines the public-safe shape for MRD, response, relapse, lab,
imaging, target-measurement, residual-disease modality-discordance, and
endpoint-context fields that may later be used inside a governed private
multiple myeloma case-to-cure workflow.

It exists so downstream artifacts can preserve method, threshold, sample,
timepoint, durability, endpoint role, source context, uncertainty, and
limitations before any term is reused. It does not interpret a measurement for
a person.

## Use Boundary

This contract is not:

- a fillable public measurement schema
- a lab, imaging, pathology, or MRD result interpreter
- a response assessment tool
- a relapse or progression assessment tool
- a monitoring plan, urgency guide, safety-management guide, prognosis tool,
  treatment selector, trial matcher, option ranking, or cure claim
- a database, backend, upload path, account workflow, public intake form, or
  public submission path
- a substitute for clinician, laboratory-validity, privacy, legal, regulatory,
  or publication review

Real measurement normalization remains private-only until consent, privacy,
security, retention, clinician-review, lab-validity, legal, regulatory, and
publication gates are completed outside this public repo.

## Current Contract Decision

Current decision: `public-shape-only`.

This contract may be used for schema planning, synthetic fixtures, validator
rules, source-extraction tasks, and public task routing. It must not be used to
collect, normalize, interpret, publish, trend, or rank real measurements.

Allowed public successor: `therapy-exposure-timeline-contract-v0`, limited to
field semantics for prior therapy classes, line or exposure context, response
linkage, toxicity or constraint labels, source status, timepoint buckets, and
limitations. The successor must block sequencing advice, eligibility claims,
treatment guidance, trial guidance, monitoring guidance, ranking, and
patient-specific interpretation.

## Measurement Envelope

Every public-safe measurement field should be representable with these fields
before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `measurement_group_id` | `mrd_status`, `response_category`, `relapse_or_progression`, `lab_measurement`, `imaging_measurement`, `endpoint_context`, `target_or_antigen_measurement`, or `not_applicable`. | Group label only; no real case values. |
| `measurement_term_id` | Stable public term ID from the glossary or `source_term_pending`. | Term IDs are not claims that the measurement applies to a person. |
| `source_term` | Exact source wording or `source_term_missing`. | Source wording must not be replaced by generated interpretation. |
| `value_state` | `source_defined_category`, `numeric_private`, `qualitative_private`, `unknown`, `not_sure`, `not_tested`, `not_collected`, `source_missing`, `not_reported_by_source`, `private_only`, `synthetic_placeholder`, or `blocked_from_public`. | Public artifacts do not carry real numeric values, images, private qualitative interpretations, or person-specific trends. |
| `method_state` | `source_defined_method`, `method_needed`, `method_not_reported`, `not_applicable`, or `private_only`. | Method must be visible before MRD, response, relapse, imaging, or lab terms are reused. |
| `sample_context` | `bone_marrow`, `blood`, `urine`, `serum`, `imaging`, `tissue`, `model_system`, `source_defined_other`, `sample_context_needed`, `not_reported_by_source`, or `not_applicable`. | Sample context is required before comparing or reusing measurement terms. |
| `threshold_status` | `source_defined_threshold`, `threshold_needed`, `threshold_not_reported`, `not_applicable`, or `private_only`. | Do not assume assay sensitivity, cutoff, detection limit, or scoring rule. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `follow_up`, `study_visit_source_defined`, `unknown`, or `not_collected`. | Bucket only; no exact dates tied to a person. |
| `duration_context` | `single_assessment`, `confirmation_interval_source_defined`, `sustained_duration_source_defined`, `follow_up_duration_source_defined`, `duration_needed`, `not_reported_by_source`, or `not_applicable`. | Sustained status and endpoints need duration or explicit missingness. |
| `endpoint_role` | `source-defined-response-category`, `exploratory-endpoint`, `surrogate-or-intermediate-endpoint-under-review`, `regulatory-endpoint-context`, `clinical-outcome-endpoint`, `not-an-endpoint`, or `source-context-needed`. | Endpoint role does not establish actionability, clinical benefit, approval, or prognosis. |
| `disease_state_context` | Source-defined cohort or case-feature context bucket, or `disease_state_needed`. | Do not infer personal diagnosis, stage, relapse, or refractory status. |
| `treatment_context_state` | `class_context_source_defined`, `study_arm_context_source_defined`, `treatment_context_needed`, `no_treatment_context_present`, or `private_only`. | Treatment context supports provenance only; it cannot become treatment guidance. |
| `source_ids` | Public source IDs, artifact IDs, or `provenance_needed`. | Public source IDs are required before reuse. |
| `residual_disease_modality_state` | `single_modality_source_scoped`, `paired_modality_source_scoped`, `modality_discordance_visible`, `modality_missing`, `modality_comparison_blocked`, or `private_only`. | Cross-modality state is a representation boundary only; it cannot become prognosis, monitoring, treatment, response, or global disease-state interpretation. |
| `review_status` | `not_reviewed`, `measurement_review_needed`, `lab_validity_review_needed`, `clinician_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation. |
| `limitation_note_required` | `true`. | Every measurement group needs a limitation note before downstream reuse. |
| `allowed_public_successor` | `schema_improvement`, `synthetic_fixture`, `public_task`, `therapy_timeline_contract`, `molecular_immune_contract`, `evidence_packet_skeleton`, or `none`. | Successor must match the missing dependency and cannot bypass gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Measurement Group Semantics

| Measurement Group | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| MRD status | Source-defined MRD term, method, sample, threshold, timepoint, and limitation fields. | Method, specimen, threshold, timepoint, disease-state context, source IDs, and review status. | Do not infer no disease anywhere, cure, clinical benefit, treatment success, prognosis, or monitoring action. |
| Response category | Source-defined CR, stringent CR, partial response, deep response, or other response term. | Source criteria, disease-state context, treatment context, timepoint, denominator when study-level, and limitation note. | Do not equate response with MRD negativity, cure, treatment choice, or patient-specific outcome. |
| Relapse or progression | Source-defined event term, trigger, method, timepoint, and denominator when study-level. | Event definition, source term, assessment method, timepoint, and source IDs. | Do not compare relapse claims across sources unless definitions align. |
| Lab measurement | Field family, unit-known state, source-known state, timepoint bucket, and limitation note. | Source type, method or assay when relevant, unit-known flag, and review status. | Do not publish real values, trends, urgent flags, dose implications, monitoring schedules, or safety-management advice. |
| Imaging measurement | Imaging-context field name, source-defined response or lesion context, and limitation note. | Modality/source context, timepoint bucket, review status, and privacy gate. | Do not publish images, read scans, identify sites, infer progression, or guide monitoring. |
| Endpoint context | Study-level endpoint role, population denominator, source status, duration, and limitation note. | Endpoint role, denominator, source IDs, follow-up or duration, and public-source date. | Do not convert population endpoints into individual prognosis, product status, availability, or treatment guidance. |
| Target or antigen measurement | Source-defined target assay, antigen density, soluble marker, or normal-tissue screen context. | Target name, method, sample or model context, comparator, timepoint, and source limitations. | Do not infer actionability, treatment fit, test need, safety, efficacy, or trial fit. |
| Residual-disease modality comparison | Source-defined comparison context across marrow MRD, blood mass spectrometry, PET-CT/imaging, spatial marrow architecture, microenvironment, and host-context fields. | Modality family, method, specimen/sample, threshold or detection-status, timing alignment, paired-state context, source IDs, assay/specimen quality, review status, and limitation note. | Do not create a global disease-state flag, substitute one modality for another, interpret images or biopsies, rank modalities, infer prognosis, guide monitoring, guide treatment, or make patient-specific response calls. |

## Unknown And Missing-State Rules

Unknown and missing measurement states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `unknown` | The private team or source context does not know. | Preserve as uncertainty; do not infer a result. |
| `not_sure` | The private reporter is unsure. | Preserve as uncertainty; do not convert to positive or negative. |
| `not_tested` | A test or assessment is not known to have occurred. | Do not infer absence of a finding or need for a test. |
| `not_collected` | The public-safe shape did not collect the field. | Do not infer that private records lack the information. |
| `source_missing` | A recalled or named concept lacks source context. | Mark source-context-needed before reuse. |
| `not_reported_by_source` | A public source did not report a required context field. | Preserve the missingness and add a limitation note. |
| `numeric_private` | A numeric value may exist privately. | Do not project the value publicly. |
| `qualitative_private` | A qualitative interpretation may exist privately. | Do not project the interpretation publicly. |
| `blocked_from_public` | The field is unsafe to reuse publicly. | Remove, rewrite as a generic task, or keep private. |
| `modality_discordance_visible` | Residual-disease modalities disagree or paired context is incomplete. | Preserve the discordance state and block patient-specific meaning, prognosis, monitoring, treatment, and ranking. |

Missing data is never evidence of no disease, absence of relapse, safety,
efficacy, prognosis, treatment fit, trial fit, monitoring need, urgency, or
cure.

## Fail-Closed Normalization Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `mnc_00_no_real_values` | Public artifacts must not contain real lab values, MRD values, images, report text, exact dates tied to a person, or patient-specific trends. | Block or move to private-lab-needed. |
| `mnc_01_source_term_required` | Every measurement term needs source wording or an explicit missing-source state. | Mark `source-context-needed`. |
| `mnc_02_mrd_context_required` | MRD terms need method, sample, threshold, timepoint, disease-state context, and source ID. | Block MRD reuse until missing fields are present or explicitly missing. |
| `mnc_03_sustained_status_needs_duration` | Sustained MRD negativity or durable response language needs confirmation interval, duration, and follow-up context. | Rewrite as single-assessment or mark `duration-needed`. |
| `mnc_04_response_not_cure` | Complete response, stringent complete response, deep response, or MRD negativity cannot become a cure claim. | Rewrite or block as `blocked-clinical-advice`. |
| `mnc_05_relapse_definition_required` | Relapse or progression terms need event definition, trigger, method, and timepoint. | Mark `source-context-needed`; block cross-source comparison. |
| `mnc_06_labs_no_monitoring` | Lab families, units, or values cannot produce monitoring, urgency, dose, safety-management, or care-path guidance. | Keep values private and use source/field planning only. |
| `mnc_07_imaging_no_interpretation` | Imaging fields cannot publish images, identify sites, interpret lesions, or infer progression for a person. | Keep private or convert to generic imaging-context task. |
| `mnc_08_endpoint_role_required` | Endpoint language needs role, denominator, duration or follow-up, and source-date context. | Mark `endpoint-role-needed` or `denominator-needed`. |
| `mnc_09_population_not_prognosis` | PFS, OS, response rates, or study endpoints cannot become patient-specific prognosis or option ranking. | Rewrite as population-level source context only. |
| `mnc_10_regulatory_context_non_advisory` | Draft, nonbinding, or regulatory endpoint context cannot imply product status, availability, eligibility, or treatment choice. | Add limitation text or block. |
| `mnc_11_successor_match` | Measurement gaps must route to the correct public-safe successor. | Route therapy context to `therapy-exposure-timeline-contract-v0`, molecular context to `molecular-immune-context-contract-v0`, and evidence context to `evidence-retrieval-packet-v0` only after prerequisites close. |
| `mnc_12_no_single_modality_global_state` | A residual-disease signal from one modality cannot become a global disease-state, response, prognosis, treatment, monitoring, or cure claim. | Preserve modality family and mark cross-modality state `not_established` or `modality_discordance_visible`. |
| `mnc_13_modality_discordance_visible` | Paired residual-disease modalities, blood-based assays, spatial context, and host context must keep disagreement or missingness visible before reuse. | Route to `residual-disease-modality-discordance-source-extraction-v0`, require assay/specimen quality context, and block interpretation. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `mnc_test_01_mrd_missing_threshold` | MRD negativity with method and sample but no source-defined threshold. | Mark `threshold-needed`; block cure, prognosis, and comparison language. |
| `mnc_test_02_single_mrd_not_sustained` | One MRD-negative timepoint labeled as sustained. | Rewrite as single-assessment or mark `duration-needed`. |
| `mnc_test_03_cr_not_mrd` | Complete response term without MRD method or threshold. | Preserve as response category only; do not equate with MRD negativity or cure. |
| `mnc_test_04_lab_value_private` | Lab measurement includes a numeric value or exact date tied to a person. | Block public export as private-only. |
| `mnc_test_05_relapse_undefined` | Relapse term lacks event definition or measurement trigger. | Mark `source-context-needed`; block cross-source comparison. |
| `mnc_test_06_pfs_population_only` | PFS endpoint from a study is reused in a case-feature context. | Preserve population endpoint context; block patient-specific prognosis. |
| `mnc_test_07_public_shape_ok` | Generic measurement group with source term, method state, sample context, threshold status, timepoint bucket, endpoint role, source IDs, review status, and limitation note. | Allow as schema planning or public-source extraction shape only. |
| `mnc_test_08_marrow_petct_discordance` | Source-defined paired context has marrow MRD negative and PET-CT positive, or the reverse. | Preserve `modality_discordance_visible`; block prognosis, monitoring, imaging interpretation, treatment action, and modality ranking. |
| `mnc_test_09_blood_ms_without_marrow` | Blood mass spectrometry residual-disease result is reported while marrow context is missing. | Mark `blood_ms_complementary_context`; block substitution for marrow MRD, response calls, monitoring, prognosis, and treatment adaptation. |

## What This Step Revealed

The public repo can safely define a measurement envelope, but measurement terms
depend on therapy timing, exposure, line context, and source-defined treatment
context before downstream evidence retrieval can be meaningful.

A later public-source extraction pass completed [Residual Disease Modality Discordance Source Extraction v0](residual-disease-modality-discordance-source-extraction-v0.md). This contract now treats cross-modality residual-disease disagreement as a first-class visible state rather than a field to collapse. The next no-outreach successor, if selected, is `assay-specimen-quality-failure-mode-checklist-v0` so method, specimen, threshold, timing, and quality failures stay explicit before any future synthetic fixture or validator work.

The safest next public step is therefore
`therapy-exposure-timeline-contract-v0`: a shape-only contract for prior
therapies, exposure classes, line or timing context, response linkage, toxicity
or constraint labels, source status, timepoint buckets, and limitations without
sequencing advice or ranking.

## Handoff State

`measurement-normalization-contract-v0` is complete as a public shape
contract.

The following remain blocked outside this artifact:

- executable public normalization of real measurements
- public case uploads, save/resume workflows, accounts, storage, reports,
  images, exact dates, raw values, or source documents
- response assessment, relapse assessment, imaging interpretation, lab-value
  interpretation, MRD actionability, prognosis, treatment guidance, trial
  guidance, monitoring guidance, urgency guidance, expanded-access guidance,
  ranking, or cure claims
- publication of case-derived measurement learning without privacy, clinician,
  source, and publication gates

ORP should mark this item complete and activate
`therapy-exposure-timeline-contract-v0` next.

A later residual-disease modality-discordance update extends this complete shape contract without clearing any human gate. ORP should keep `machine-representation-expert-validation-human-authorization-blocker-v0` active while treating `assay-specimen-quality-failure-mode-checklist-v0` as the next no-outreach public-source successor if selected.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  values, or free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case measurement schema.
- No patient-specific diagnosis, response assessment, relapse assessment,
  prognosis, treatment, trial, eligibility, expanded-access, monitoring,
  urgency, safety-management, publication, or candidate-option guidance.
- No patient matching, trial matching, option ranking, evidence ranking, or
  review decision.
- No cure or vaccine claim.

## Limitations

- This is a public shape contract, not an executable schema.
- This is not a real measurement record.
- This does not process, normalize, store, route, publish, trend, compare, or
  authorize use of real measurement data.
- This does not complete consent, privacy, security, retention,
  clinician-review, lab-validity, legal, regulatory, institutional, sponsor,
  site, treating-team, or publication gates.
- This does not validate therapy exposure, molecular, immune, evidence
  retrieval, trial, therapy landscape, candidate hypothesis, multidisciplinary
  review, monitoring-plan, or public-learning extraction semantics.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, or regulatory-ready.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, emergency
  guidance, or a cure claim.
