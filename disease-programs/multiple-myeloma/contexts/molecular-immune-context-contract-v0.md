# Molecular Immune Context Contract v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-molecular-immune-context-contract-v0`
- active ORP item: `molecular-immune-context-contract-v0`
- contract status: public shape contract complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no records, no uploads,
  no molecular reports, no pathology reports, no images, no raw assay values,
  no exact dates, no patient-specific target calls, no fillable public
  molecular or immune context record
- last reviewed: `2026-04-16`

## Purpose

This contract defines the public-safe shape for cytogenetic, genomic,
target-assay, pathology, flow-cytometry, immune-context, assay-validity, and
source-validity fields that may later be used inside a governed private
multiple myeloma case-to-cure workflow.

It exists so downstream artifacts can preserve source, method, specimen or
model context, timepoint bucket, therapy and measurement linkage, uncertainty,
review gates, and limitations before any evidence retrieval or hypothesis
review reuses molecular or immune language.

It does not decide what is present in a person, what should be tested, what is
actionable, what treatment fits, what trial fits, or what should happen next.

## Use Boundary

This contract is not:

- a fillable public molecular profile
- a genomics, cytogenetics, pathology, flow, immune-fitness, target-expression,
  or assay-result interpreter
- an actionability record, biomarker report, test-ordering guide, target-fit
  guide, treatment selector, trial matcher, monitoring plan, urgency guide,
  option ranking, prognosis tool, or cure claim
- a target-prioritization, mechanism-scoring, evidence-ranking, or product
  comparison system
- a database, backend, upload path, account workflow, public intake form,
  public submission path, or private-lab implementation
- a substitute for clinician, laboratory-validity, molecular-pathology,
  privacy, legal, regulatory, sponsor, site, treating-team, or publication
  review

Real molecular and immune context normalization remains private-only until
consent, privacy, security, retention, clinician-review, lab-validity,
source-validity, legal, regulatory, and publication gates are completed outside
this public repo.

## Current Contract Decision

Current decision: `public-shape-only`.

This contract may be used for schema planning, synthetic fixtures, validator
rules, source-extraction tasks, and public task routing. It must not be used to
collect, normalize, interpret, publish, compare, rank, or authorize use of real
molecular, pathology, flow, or immune-context data.

Allowed public successor: `evidence-retrieval-packet-v0`, limited to a
reproducible public-source evidence packet skeleton with source IDs, query
records, freshness checks, limitation fields, uncertainty, no-completeness
warnings, and no-advice boundaries. The successor must block patient matching,
trial matching, treatment selection, target actionability, eligibility claims,
monitoring guidance, ranking, and patient-specific interpretation.

## Molecular Immune Context Envelope

Every public-safe molecular or immune context field should be representable
with these fields before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `context_group_id` | `cytogenetic_context`, `genomic_feature_context`, `target_assay_context`, `pathology_context`, `flow_context`, `immune_cell_context`, `microenvironment_context`, `normal_tissue_or_safety_context`, `mechanism_linkage_context`, `source_validity_context`, or `not_applicable`. | Group label only; no real case profile. |
| `context_field_id` | Stable public field name, public target-record ID, mechanism-group ID, or private-only field-group ID. | Must not contain private case IDs, identifiers, report text, exact dates, assay accession numbers, facilities, clinicians, or rare person-specific combinations. |
| `feature_or_marker_state` | `source_defined_category`, `cytogenetic_category_source_defined`, `genomic_bucket_source_defined`, `target_symbol_source_defined`, `immune_category_source_defined`, `pathology_category_source_defined`, `unknown`, `not_sure`, `not_tested`, `not_collected`, `source_missing`, `private_only`, `synthetic_placeholder`, or `blocked_from_public`. | Source-defined labels organize context only; they do not imply actionability, test need, treatment fit, trial fit, prognosis, or patient relevance. |
| `assay_method_state` | `source_defined_method`, `method_needed`, `method_not_reported`, `not_applicable`, or `private_only`. | Method must be visible before target, genomic, pathology, flow, or immune context is reused. |
| `specimen_or_model_context` | `bone_marrow`, `blood`, `plasmacytoma_or_tissue`, `pathology_specimen`, `flow_specimen`, `cell_product`, `model_system`, `normal_tissue_context`, `source_defined_other`, `specimen_context_needed`, `not_reported_by_source`, or `not_applicable`. | Specimen and model contexts are not interchangeable and cannot become patient-specific interpretation. |
| `threshold_or_scoring_state` | `source_defined_threshold`, `source_defined_scoring_rule`, `threshold_needed`, `scoring_not_reported`, `not_applicable`, or `private_only`. | Do not assume positivity, negativity, density, cutoff, scoring method, detection limit, or clinical relevance. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `post_bcma_context`, `follow_up`, `study_visit_source_defined`, `unknown`, or `not_collected`. | Bucket only; no exact dates tied to a person. |
| `therapy_linkage_state` | `therapy_contract_linked`, `prior_exposure_context_needed`, `class_context_source_defined`, `no_therapy_context_present`, `not_applicable`, or `private_only`. | Therapy linkage must follow the therapy exposure timeline contract and cannot become sequencing, eligibility, access, or recommendation language. |
| `measurement_linkage_state` | `measurement_contract_linked`, `assay_measurement_context_needed`, `response_or_relapse_context_needed`, `no_measurement_context_present`, `not_applicable`, or `private_only`. | Measurement linkage must follow the measurement normalization contract and cannot become outcome, monitoring, or cure language. |
| `source_type` | `public_source`, `caregiver_report_private`, `portal_summary_private`, `pathology_report_private`, `flow_report_private`, `genomics_report_private`, `lab_report_private`, `clinician_note_private`, `unknown`, or `not_collected`. | Source class only; no source contents or private source paths. |
| `source_status` | `source_seen_private`, `source_reported_not_seen`, `source_missing`, `public_source_only`, `not_reported_by_source`, or `not_collected`. | Preserve source status, not the private record. |
| `source_ids` | Public source IDs, artifact IDs, mechanism-group IDs, target-record IDs, or `provenance_needed`. | Public source IDs are required before public-source reuse. |
| `uncertainty_state` | `source_limit`, `method_limit`, `specimen_limit`, `threshold_limit`, `timepoint_limit`, `definition_mismatch`, `expert_review_needed`, `private_review_needed`, `unknown`, or `none_stated_by_source`. | Uncertainty must be visible before reuse and cannot be erased by generated wording. |
| `review_status` | `not_reviewed`, `molecular_review_needed`, `pathology_review_needed`, `flow_review_needed`, `lab_validity_review_needed`, `clinician_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation and downstream patient-linked reuse. |
| `limitation_note_required` | `true`. | Every molecular or immune context group needs a limitation note before downstream reuse. |
| `allowed_public_successor` | `schema_improvement`, `synthetic_fixture`, `public_task`, `evidence_packet_skeleton`, `trial_therapy_landscape_gate`, `candidate_hypothesis_question_set`, or `none`. | Successor must match the missing dependency and cannot bypass privacy, source, evidence, clinical, trial, molecular, or publication gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Context Group Semantics

| Context Group | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| Cytogenetic context | Source-defined cytogenetic category, method state, specimen context, and source status. | Source term, method, specimen, timepoint bucket, review status, and limitation note. | Do not infer prognosis, risk-adapted care, eligibility, urgency, treatment intensity, transplant fit, or option ranking. |
| Genomic feature context | Source-defined genomic-feature bucket or private-only feature group needed for future review. | Source type, method state, variant or feature bucket state, source status, uncertainty, and review gate. | Do not publish unique variants from a person, interpret pathogenicity, infer actionability, recommend testing, or guide care. |
| Target assay context | Source-defined target, antigen, density, soluble marker, or expression context. | Target symbol or record ID, assay method, specimen or model context, threshold or scoring state, timepoint bucket, and source IDs. | Do not infer target presence in a person, targetability, treatment fit, trial fit, normal-tissue safety, efficacy, or access. |
| Pathology context | Source-defined pathology or tissue context needed to route private review. | Specimen context, method/source status, privacy review, and limitation note. | Do not publish report text, images, diagnosis assertions, site details, or patient-specific interpretation. |
| Flow context | Source-defined flow-cytometry or immune-phenotype context. | Method, specimen, threshold or scoring state, source status, and lab-validity review. | Do not infer MRD status, immune competence, infection risk, treatment fit, monitoring need, or prognosis. |
| Immune cell context | Source-defined T-cell, CAR T fitness, exhaustion, expansion, persistence, immune reconstitution, or immune-state field. | Source-defined method, timepoint bucket, therapy linkage, measurement linkage, source IDs, and uncertainty. | Do not compare products, infer dominant relapse mechanism, assign immune fitness, or recommend interventions. |
| Microenvironment context | Source-defined immune microenvironment, infection-risk, or inflammatory context. | Context modifier map linkage, source status, uncertainty, and review gate. | Do not provide infection-risk estimates, prophylaxis, vaccination, monitoring, or supportive-care guidance. |
| Normal tissue or safety context | Source-defined normal-tissue, off-tumor, model, or translational safety field. | Model/specimen context, source status, limitation text, and translation-safety boundary. | Do not infer clinical safety, tolerability, efficacy, availability, or patient fit. |
| Mechanism linkage context | Link from molecular or immune context to mechanism groups or extraction records. | Mechanism group ID, source IDs, claim level, measurement linkage, therapy linkage, and limitation note. | Do not rank mechanisms, targets, products, trials, sources, or evidence, and do not infer patient action. |
| Source validity context | Whether source, method, specimen, threshold, timepoint, and review status are sufficient for reuse. | Explicit missingness, review-needed state, and limitation note. | Do not treat missing review or missing source detail as permission to interpret. |

## Unknown And Missing-State Rules

Unknown and missing molecular or immune states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `unknown` | The private team or source context does not know. | Preserve as uncertainty; do not infer presence, absence, actionability, or reassurance. |
| `not_sure` | The private reporter is unsure. | Preserve as uncertainty; do not convert to present, absent, positive, negative, high, or low. |
| `not_tested` | A test or assessment is not known to have occurred. | Do not infer absence of a feature or need for a test. |
| `not_collected` | The public-safe shape did not collect the field. | Do not infer that private records lack the information. |
| `source_missing` | A recalled or named molecular or immune concept lacks source context. | Mark source-context-needed before reuse. |
| `not_reported_by_source` | A public source did not report a required context field. | Preserve missingness and add a limitation note. |
| `private_only` | The detail may exist only in a governed private workspace. | Do not project into public artifacts. |
| `blocked_from_public` | The field is unsafe to reuse publicly. | Remove, rewrite as a generic task, or keep private. |

Missing data is never evidence of absence, actionability, target fit,
treatment fit, trial fit, safety, efficacy, prognosis, monitoring need,
urgency, or cure.

## Fail-Closed Context Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `micc_00_no_real_profile` | Public artifacts must not contain real molecular profiles, pathology reports, flow reports, genomics reports, images, exact dates, report text, accession numbers, private paths, or patient-specific target calls. | Block or move to private-lab-needed. |
| `micc_01_source_before_feature` | Molecular or immune labels need source type and source status before reuse. | Treat as `source_missing` and block interpretation. |
| `micc_02_method_required` | Target, cytogenetic, genomic, pathology, flow, or immune context needs method state or explicit method missingness. | Mark `method_needed` or `method_not_reported`; block actionability and comparison language. |
| `micc_03_specimen_context_required` | Assay terms need specimen, model, or source-defined context before reuse. | Mark `specimen_context_needed`; block cross-source comparison. |
| `micc_04_threshold_not_assumed` | Target density, expression, positive/negative, low/high, or marker-state language needs threshold or scoring context when source-defined. | Mark `threshold_needed`; block targetability, efficacy, safety, and trial-fit inference. |
| `micc_05_timepoint_bucket_only` | Public artifacts may use broad timepoint buckets only. | Remove exact dates and person-linked chronology. |
| `micc_06_not_tested_not_guidance` | `not_tested`, `unknown`, and `not_collected` states cannot imply need for testing, absence of a feature, or reassurance. | Preserve missingness and add a limitation note. |
| `micc_07_target_language_non_actionable` | Target, antigen, marker, and pathway terms cannot imply target actionability or patient fit. | Rewrite as source-context-only or block. |
| `micc_08_mechanism_link_non_ranking` | Mechanism links cannot rank mechanisms, products, trials, targets, sources, or evidence. | Keep as provenance or public task routing only. |
| `micc_09_therapy_link_needs_timeline` | Prior exposure, refractory, or class context must route through the therapy exposure timeline contract. | Mark therapy-context-needed; block sequencing, eligibility, access, and treatment guidance. |
| `micc_10_measurement_link_needs_contract` | Response, relapse, MRD, target-measurement, or assay-measurement terms must route through the measurement normalization contract. | Mark measurement-context-needed; block monitoring, prognosis, and cure language. |
| `micc_11_review_gate_required` | Review status must be visible before downstream reuse. | Default to molecular, pathology, flow, lab-validity, clinician, privacy, or publication review needed. |
| `micc_12_successor_match` | Molecular and immune gaps must route to the correct public-safe successor. | Route public-source retrieval needs to `evidence-retrieval-packet-v0`, landscape needs to `trial-therapy-landscape-non-advice-gate-v0`, and hypothesis questions to `candidate-hypothesis-review-question-set-v0`. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `micc_test_01_target_assay_missing_method` | Target assay label is present but assay method is missing. | Mark `method_needed`; block actionability, target-fit, treatment, and trial language. |
| `micc_test_02_not_tested_preserved` | Genomic feature group has `feature_or_marker_state: "not_tested"`. | Do not infer absence of a feature or need for testing. |
| `micc_test_03_exact_report_blocked` | Molecular context includes report text, accession number, image, exact date, facility, or clinician. | Block public export as private-only. |
| `micc_test_04_low_target_no_option` | Low or high target expression is paired with a suggested therapy class or trial direction. | Preserve source-defined target context only; block treatment, trial, and ranking wording. |
| `micc_test_05_mechanism_link_non_ranking` | Mechanism group is linked to a feature and described as the most likely relapse cause. | Block ranking and patient-specific causality; keep only source-context linkage. |
| `micc_test_06_flow_no_mrd_inference` | Flow context appears without measurement contract fields. | Route to measurement normalization; block MRD, response, prognosis, and monitoring claims. |
| `micc_test_07_public_shape_ok` | Generic context group with source type, source status, method state, specimen context, timepoint bucket, review status, uncertainty, and limitation note. | Allow as schema planning or public-source extraction shape only. |

## What This Step Revealed

The public repo can safely define molecular and immune context semantics when
target, assay, specimen, threshold, timepoint, therapy linkage, measurement
linkage, uncertainty, and review gates stay visible.

With the case-feature, measurement, therapy exposure, and molecular immune
contracts now defined, the next missing public dependency is not another case
field. It is the evidence retrieval packet skeleton: a reproducible,
public-source-only structure for source IDs, query records, freshness checks,
limitations, no-completeness warnings, and no-advice boundaries before any
future private case question asks for evidence.

The next safest public step is therefore `evidence-retrieval-packet-v0`.

## Handoff State

`molecular-immune-context-contract-v0` is complete as a public shape contract.

The following remain blocked outside this artifact:

- executable public normalization of real molecular, pathology, flow, genomic,
  or immune-context data
- public case uploads, save/resume workflows, accounts, storage, reports,
  images, exact dates, raw assay values, variant lists, accession numbers,
  facilities, clinicians, private paths, or source documents
- target actionability, test guidance, biomarker interpretation, pathology
  interpretation, flow interpretation, immune-fitness interpretation,
  mechanism ranking, prognosis, treatment guidance, trial guidance,
  eligibility guidance, access guidance, expanded-access guidance, monitoring
  guidance, urgency guidance, safety-management guidance, referral guidance,
  ranking, or cure claims
- publication of case-derived molecular or immune learning without privacy,
  clinician, source-validity, lab-validity, and publication gates

ORP should mark this item complete and activate
`evidence-retrieval-packet-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, variant lists, accession numbers, facilities, clinicians,
  private paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case molecular or immune context profile.
- No patient-specific diagnosis, molecular interpretation, pathology
  interpretation, flow interpretation, target actionability, prognosis,
  treatment, trial, eligibility, expanded-access, access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target ranking, mechanism ranking,
  option ranking, evidence ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public shape contract, not an executable schema.
- This is not a real molecular profile.
- This is not a target-status record for any person.
- This does not process, normalize, store, route, publish, compare, rank, or
  authorize use of real molecular or immune context data.
- This does not complete consent, privacy, security, retention,
  clinician-review, molecular-review, pathology-review, flow-review,
  lab-validity, source-validity, legal, regulatory, institutional, sponsor,
  site, treating-team, or publication gates.
- This does not validate evidence retrieval, trial, therapy landscape,
  candidate hypothesis, multidisciplinary review, monitoring-plan, or
  public-learning extraction semantics.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, or regulatory-ready.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, access guidance, testing guidance, monitoring
  guidance, urgency guidance, safety-management guidance, emergency guidance,
  referral guidance, or a cure claim.
