# Therapy Exposure Timeline Contract v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-therapy-exposure-timeline-contract-v0`
- active ORP item: `therapy-exposure-timeline-contract-v0`
- contract status: public shape contract complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no records, no uploads,
  no exact therapy dates, no doses, no schedules, no facilities, no prescriber
  names, no narrative toxicity history, no fillable public therapy timeline
- last reviewed: `2026-04-16`

## Purpose

This contract defines the public-safe shape for prior therapy exposure, line or
timing context, response linkage, toxicity or tolerability labels, constraints,
refractory context, and source status that may later be used inside a governed
private multiple myeloma case-to-cure workflow.

It exists so downstream artifacts can preserve therapy class, exposure state,
relative timing, measurement linkage, uncertainty, review gates, and
limitations before any evidence retrieval, hypothesis review, or trial and
therapy landscape work reuses therapy-context language.

It does not decide what a person has received, should receive, can access, is
eligible for, is refractory to, is unsafe for, or should do next.

## Use Boundary

This contract is not:

- a fillable public therapy history
- a medication list, treatment timeline, dosing record, schedule, or regimen
  parser
- a treatment, trial, expanded-access, monitoring, safety-management, referral,
  or urgency guide
- a sequencing tool, eligibility tool, availability checker, actionability
  engine, candidate-option selector, patient matcher, trial matcher, option
  ranking, prognosis tool, or cure claim
- a response assessment, refractory-status assessment, toxicity assessment, or
  treatment-fitness assessment for any person
- a database, backend, upload path, account workflow, public intake form,
  public submission path, or private-lab implementation
- a substitute for clinician, consent, privacy, security, legal, regulatory,
  sponsor, site, institutional, treating-team, or publication review

Real therapy timeline normalization remains private-only until consent,
privacy, security, retention, clinician-review, source-validity, legal,
regulatory, and publication gates are completed outside this public repo.

## Current Contract Decision

Current decision: `public-shape-only`.

This contract may be used for schema planning, synthetic fixtures, validator
rules, source-extraction tasks, and public task routing. It must not be used to
collect, normalize, interpret, publish, compare, sequence, or rank real therapy
exposures.

Allowed public successor: `molecular-immune-context-contract-v0`, limited to
field semantics for cytogenetics, genomics, target assays, pathology, flow,
immune context, assay/source validity, timepoint buckets, review status, and
limitations. The successor must block actionability claims, test guidance,
treatment fit, trial fit, eligibility claims, ranking, monitoring guidance,
and patient-specific interpretation.

## Therapy Timeline Envelope

Every public-safe therapy exposure field should be representable with these
fields before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `therapy_event_group_id` | `prior_therapy_exposure`, `current_or_recent_therapy_context`, `line_or_sequence_context`, `response_linkage`, `toxicity_or_tolerability_context`, `constraint_context`, `refractory_or_resistance_context`, `transplant_cellular_therapy_context`, `clinical_trial_exposure_context`, `supportive_or_local_context`, or `not_applicable`. | Group label only; no real case timeline. |
| `therapy_event_id` | Stable public field name or private-only field-group ID. | Must not contain private case IDs, identifiers, exact dates, facilities, clinicians, site names, record text, or rare person-specific combinations. |
| `therapy_class_id` | Treatment-class taxonomy ID, source-defined therapy class, `class_needed`, `class_unknown`, or `not_applicable`. | Class labels organize context only; they do not imply appropriateness, sequence, access, efficacy, safety, or superiority. |
| `agent_or_product_state` | `class_only`, `product_or_agent_source_defined`, `combination_source_defined`, `agent_private`, `agent_unknown`, `source_missing`, `not_collected`, or `not_applicable`. | Product names require source context and cannot imply availability, indication, eligibility, access, or patient fit. |
| `exposure_state` | `exposed_source_defined`, `not_exposed_source_defined`, `unknown`, `not_sure`, `not_collected`, `source_missing`, `private_only`, `synthetic_placeholder`, or `blocked_from_public`. | Missing exposure is never evidence of no exposure, eligibility, next step, or safety. |
| `line_or_timing_bucket` | `frontline_context`, `maintenance_context`, `early_relapse_context`, `later_relapse_context`, `transplant_context`, `cellular_therapy_context`, `clinical_trial_context`, `source_defined_bucket`, `unknown`, `not_collected`, or `private_only`. | Use buckets only; do not publish exact line numbers, dates, cycles, schedules, or person-linked chronology. |
| `relative_order_state` | `source_defined_before_after`, `same_regimen_source_defined`, `order_unknown`, `not_collected`, `not_applicable`, or `private_only`. | Relative order records provenance only; it is not sequencing advice. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `follow_up`, `study_visit_source_defined`, `unknown`, or `not_collected`. | Bucket only; no exact dates tied to a person. |
| `response_linkage_state` | `measurement_contract_linked`, `source_defined_response_context`, `response_context_needed`, `not_reported_by_source`, `not_applicable`, or `private_only`. | Response linkage must follow the measurement normalization contract and cannot become outcome, prognosis, or treatment guidance. |
| `toxicity_or_tolerability_state` | `toxicity_category_source_defined`, `tolerability_constraint_source_defined`, `toxicity_unknown`, `not_collected`, `not_applicable`, `private_only`, or `blocked_from_public`. | Do not publish narrative toxicity history, grades tied to a person, adverse-event management, stop rules, dose changes, or safety advice. |
| `constraint_state` | `source_defined_constraint_category`, `goal_or_preference_private`, `logistic_or_financial_private`, `unknown`, `not_collected`, `not_applicable`, or `private_only`. | Goals, preferences, finances, travel, access, family logistics, and care constraints are private unless rewritten as generic categories after review. |
| `refractory_or_resistance_state` | `source_defined_refractory_context`, `resistance_mechanism_needed`, `source_missing`, `not_reported_by_source`, `not_applicable`, or `private_only`. | Do not infer refractory status, resistance mechanism, target loss, next option, or trial fit for a person. |
| `source_type` | `public_source`, `caregiver_report_private`, `portal_summary_private`, `medication_record_private`, `clinician_note_private`, `trial_record_private`, `unknown`, or `not_collected`. | Source class only; no source contents or private source paths. |
| `source_status` | `source_seen_private`, `source_reported_not_seen`, `source_missing`, `public_source_only`, `not_reported_by_source`, or `not_collected`. | Preserve source status, not the private record. |
| `source_ids` | Public source IDs, artifact IDs, or `provenance_needed`. | Public source IDs are required before public-source reuse. |
| `review_status` | `not_reviewed`, `clinician_review_needed`, `source_validity_review_needed`, `measurement_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation and downstream patient-linked reuse. |
| `limitation_note_required` | `true`. | Every therapy exposure group needs a limitation note before downstream reuse. |
| `allowed_public_successor` | `schema_improvement`, `synthetic_fixture`, `public_task`, `molecular_immune_contract`, `evidence_packet_skeleton`, `trial_therapy_landscape_gate`, or `none`. | Successor must match the missing dependency and cannot bypass privacy, source, molecular, evidence, trial, clinical, or publication gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Therapy Timeline Group Semantics

| Timeline Group | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| Prior therapy exposure | Source-defined class, exposure state, source status, and broad timing bucket. | Therapy class, exposure state, source type, source status, timepoint bucket, review status, and limitation note. | Do not infer what should come next, whether a class is exhausted, or whether a person is eligible for any therapy or trial. |
| Current or recent therapy context | Broad context label for source-defined current or recent treatment in a private record or public source. | Source type, source status, timepoint bucket, privacy review, and limitation note. | Do not publish current treatment for a real person or provide monitoring, continuation, stopping, or switching guidance. |
| Line or sequence context | Source-defined order or broad bucket needed for provenance. | Relative-order state, line or timing bucket, source status, and review gate. | Do not convert sequence context into sequencing advice, standard-of-care instructions, or comparative ranking. |
| Response linkage | Link from therapy context to measurement-context fields. | Measurement normalization contract fields and source-defined timepoint bucket. | Do not claim response, relapse, durability, failure, benefit, or cure for a person. |
| Toxicity or tolerability context | Source-defined category or private-only tolerability constraint. | Source category, private/public boundary, review status, and limitation note. | Do not publish narrative adverse-event history, safety management, dose guidance, contraindication claims, or urgency guidance. |
| Constraint context | Broad category for constraints that may affect private review. | Private-only default, source status, review status, and limitation note. | Do not publish goals, finances, travel details, caregiver logistics, preferences, access needs, or social context as public case facts. |
| Refractory or resistance context | Source-defined refractory or resistance label that needs molecular, measurement, and therapy context before reuse. | Source wording, therapy class, measurement linkage, molecular/immune context status, and clinician review. | Do not infer resistance mechanism, target loss, next target, treatment choice, trial fit, or prognosis. |
| Transplant or cellular therapy context | Class-level context for autologous transplant strategy or cellular therapy exposure. | Treatment-class taxonomy ID, source status, timepoint bucket, and limitation note. | Do not infer transplant eligibility, CAR T eligibility, product access, referral timing, safety, or suitability. |
| Clinical trial exposure context | Source-defined trial participation or trial-arm context. | Trial source class, registry/public source ID when public, private-only default for real cases, and review gate. | Do not infer trial eligibility, enrollment opportunity, site availability, sponsor access, treatment fit, or outcome. |
| Supportive or local context | Class-level support or local-control context when needed for source provenance. | Source status, broad category, and limitation note. | Do not provide supportive-care, radiation, renal, infection, bone, transfusion, dose, or monitoring guidance. |

## Unknown And Missing-State Rules

Unknown and missing therapy states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `unknown` | The private team or source context does not know. | Preserve as uncertainty; do not infer exposure, absence, sequence, eligibility, or safety. |
| `not_sure` | The private reporter is unsure. | Preserve as uncertainty; do not convert to exposed or not exposed. |
| `not_collected` | The public-safe shape did not collect the field. | Do not infer that private records lack the information. |
| `source_missing` | A recalled or named therapy concept lacks source context. | Mark source-context-needed before reuse. |
| `not_reported_by_source` | A public source did not report a required context field. | Preserve missingness and add a limitation note. |
| `private_only` | The therapy detail may exist only in a governed private workspace. | Do not project into public artifacts. |
| `blocked_from_public` | The field is unsafe to reuse publicly. | Remove, rewrite as a generic task, or keep private. |

Missing data is never evidence of no exposure, class sensitivity, class
resistance, eligibility, ineligibility, access, safety, toxicity risk, treatment
fit, trial fit, monitoring need, urgency, prognosis, or cure.

## Fail-Closed Timeline Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `tetc_00_no_real_timeline` | Public artifacts must not contain real therapy timelines, exact dates, doses, schedules, cycles, facilities, prescriber names, notes, record text, private paths, or patient-specific treatment histories. | Block or move to private-lab-needed. |
| `tetc_01_class_required` | Therapy exposure rows need a taxonomy class, source-defined class, or explicit missing-class state. | Mark `class-needed`; block downstream reuse. |
| `tetc_02_source_before_exposure` | Exposure labels need source type and source status before reuse. | Treat as `source_missing` and block interpretation. |
| `tetc_03_timepoint_bucket_only` | Public artifacts may use broad timepoint or line/timing buckets only. | Remove exact dates, line counts, cycles, schedules, and person-linked chronology. |
| `tetc_04_no_sequence_inference` | Prior exposure, relative order, or class history cannot imply what should come before or after another therapy. | Rewrite as source-context-only or block. |
| `tetc_05_no_access_or_eligibility` | Product, trial, class, target, prior-exposure, or status terms cannot imply availability, eligibility, access route, referral, enrollment, or expanded-access path. | Add limitation text or block. |
| `tetc_06_response_linkage_needs_measurement` | Response, MRD, relapse, progression, or durability language linked to therapy must route through the measurement normalization contract. | Mark measurement-context-needed; block outcome, prognosis, and cure language. |
| `tetc_07_toxicity_no_management` | Toxicity or tolerability categories cannot produce dose, hold, stop, monitoring, safety-management, urgency, or contraindication guidance. | Keep private or rewrite as generic source-context category. |
| `tetc_08_refractory_context_non_advisory` | Refractory or resistance context cannot infer resistance mechanism, target loss, next target, treatment choice, trial fit, or prognosis. | Route molecular, immune, and mechanism context to `molecular-immune-context-contract-v0`. |
| `tetc_09_constraints_private_by_default` | Goals, preferences, logistics, finances, access needs, and caregiver constraints are private by default. | Keep private or convert to non-identifying category only after privacy and publication review. |
| `tetc_10_review_gate_required` | Review status must be visible before downstream reuse. | Default to `clinician_review_needed`, `privacy_review_needed`, or `publication_gate_needed`. |
| `tetc_11_successor_match` | Therapy gaps must route to the correct public-safe successor. | Route molecular/immune context to `molecular-immune-context-contract-v0`, evidence needs to `evidence-retrieval-packet-v0` only after prerequisites close, and trial/product landscape needs to `trial-therapy-landscape-non-advice-gate-v0`. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `tetc_test_01_exposure_source_missing` | Prior therapy class is named but source status is missing. | Mark `source-context-needed`; block sequencing, eligibility, and ranking language. |
| `tetc_test_02_exact_date_blocked` | Therapy event includes a person-linked start date, stop date, cycle count, dose, facility, or prescriber. | Block public export as private-only. |
| `tetc_test_03_sequence_rewritten` | Artifact says a class came after another class and implies the next class to use. | Preserve relative-order state only; block recommendation and sequencing wording. |
| `tetc_test_04_response_deferred` | Therapy exposure is paired with response or MRD language but lacks measurement contract fields. | Route to measurement normalization; block outcome, prognosis, and cure claims. |
| `tetc_test_05_toxicity_no_advice` | Toxicity category appears with a proposed monitoring or dose action. | Block safety-management output; keep only source-defined category after review. |
| `tetc_test_06_refractory_no_next_target` | Refractory context is used to suggest an alternate target or trial class. | Block actionability; route target and assay context to molecular/immune contract. |
| `tetc_test_07_public_shape_ok` | Generic therapy group with class ID, exposure state, source type, source status, timepoint bucket, response linkage state, review status, and limitation note. | Allow as schema planning or public-source extraction shape only. |

## What This Step Revealed

The public repo can safely define therapy exposure timeline semantics, but
prior exposure becomes unsafe if molecular, immune, cytogenetic, target-assay,
pathology, flow, and source-validity context are missing. Without those fields,
therapy history can too easily become target actionability, trial fit,
sequencing, resistance interpretation, or patient-option ranking.

The safest next public step is therefore
`molecular-immune-context-contract-v0`: a shape-only contract for cytogenetic,
genomic, target-assay, pathology, flow, immune context, assay/source validity,
timepoint buckets, review gates, and limitations without actionability,
testing, treatment, trial, or ranking guidance.

## Handoff State

`therapy-exposure-timeline-contract-v0` is complete as a public shape contract.

The following remain blocked outside this artifact:

- executable public normalization of real therapy histories
- public case uploads, save/resume workflows, accounts, storage, medication
  records, timeline records, exact dates, doses, schedules, cycles, facilities,
  prescribers, clinician notes, toxicity narratives, or source documents
- therapy exposure interpretation, refractory assessment, response assessment,
  safety management, toxicity management, prognosis, treatment guidance, trial
  guidance, eligibility guidance, availability claims, access guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, referral
  guidance, ranking, or cure claims
- publication of case-derived therapy timeline learning without privacy,
  clinician, source, and publication gates

ORP should mark this item complete and activate
`molecular-immune-context-contract-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  values, doses, schedules, cycles, facilities, prescribers, private paths, or
  free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case therapy timeline.
- No patient-specific diagnosis, response assessment, refractory assessment,
  prognosis, treatment, trial, eligibility, expanded-access, access,
  availability, monitoring, urgency, safety-management, toxicity-management,
  referral, publication, or candidate-option guidance.
- No patient matching, trial matching, option ranking, evidence ranking, or
  review decision.
- No cure or vaccine claim.

## Limitations

- This is a public shape contract, not an executable schema.
- This is not a real therapy timeline.
- This does not process, normalize, store, route, publish, sequence, compare,
  rank, or authorize use of real therapy exposure data.
- This does not complete consent, privacy, security, retention,
  clinician-review, source-validity, legal, regulatory, institutional, sponsor,
  site, treating-team, or publication gates.
- This does not validate molecular, immune, evidence retrieval, trial, therapy
  landscape, candidate hypothesis, multidisciplinary review, monitoring-plan,
  or public-learning extraction semantics.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, or regulatory-ready.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, access guidance, monitoring guidance, urgency
  guidance, safety-management guidance, toxicity-management guidance,
  emergency guidance, referral guidance, or a cure claim.
