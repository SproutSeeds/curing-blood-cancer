# Trial Therapy Landscape Non-Advice Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-trial-therapy-landscape-non-advice-gate-v0`
- active ORP item: `trial-therapy-landscape-non-advice-gate-v0`
- gate status: public non-advice gate complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public source landscape context only; no real case data, no
  identifiers, no private records, no patient matching, no trial matching, no
  availability claims, no eligibility claims, no access instructions, no
  sequencing advice, no ranking, and no patient-specific interpretation
- last reviewed: `2026-04-16`

## Purpose

This gate defines how trial, therapy, product, target, jurisdiction, status,
source freshness, access date, limitation, uncertainty, and review fields can
be represented as public multiple myeloma landscape context.

It exists so later artifacts can inspect public trial and therapy landscapes
without becoming trial finders, eligibility checkers, product availability
tools, access guides, sequencing tools, treatment selectors, or candidate
option rankings.

It does not decide whether any therapy, product, target, trial, site, sponsor,
or access pathway is available, appropriate, safe, effective, relevant,
eligible, urgent, better, or next for any person.

## Use Boundary

This gate is not:

- a live trial search, therapy explorer, product dashboard, registry monitor,
  label monitor, scraper, API workflow, database, backend, account workflow,
  public intake form, public submission path, or case-matching system
- a trial matcher, eligibility checker, site finder, sponsor-access guide,
  expanded-access pathway, availability checker, reimbursement or coverage
  guide, referral guide, or urgency guide
- a treatment guide, sequencing guide, testing guide, monitoring plan,
  safety-management guide, prognosis tool, actionability record, option
  selector, comparison engine, or ranking system
- a substitute for source appraisal, clinician review, trial-site
  verification, sponsor verification, regulator or label review, legal review,
  institutional review, treating-team review, privacy review, or publication
  review

Real case-linked landscape review remains private-only until consent, privacy,
security, retention, source-validity, clinical, legal, regulatory,
sponsor/site, treating-team, and publication gates are completed outside this
public repo.

## Current Gate Decision

Current decision: `public-landscape-shape-only`.

This gate may be used for schema planning, source registry hygiene, query
record design, source-extraction tasks, synthetic fixtures, validator rules,
and public task routing. It must not be used to search, match, interpret,
compare, rank, recommend, publish, or authorize trial or therapy context for a
real person.

Allowed public successor:
`candidate-hypothesis-review-question-set-v0`, limited to source-scoped review
questions for qualified humans. The successor must preserve evidence packet
IDs, landscape gate status, source context, uncertainty, review lens, blocked
uses, and explicit no patient-action output. It must block recommendations,
rankings, treatment guidance, trial guidance, expanded-access guidance,
monitoring guidance, urgency guidance, and patient-specific interpretation.

## Landscape Gate Envelope

Every public-safe trial or therapy landscape row should be representable with
these fields before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `landscape_record_id` | Stable public ID or `landscape_record_pending`. | ID is for audit only; it is not a case, trial-match, or recommendation ID. |
| `landscape_question_id` | Public research question ID, source-extraction task ID, evidence-gap ID, or `question_pending`. | Question must be generic or public-source-only; no private case values. |
| `landscape_context_type` | `trial_registry_context`, `therapy_record_context`, `product_status_context`, `target_context`, `mechanism_context`, `regulatory_context`, `labeling_context`, `dataset_context`, `source_refresh_context`, or `review_gate_context`. | Context type organizes public evidence only; it does not establish patient fit. |
| `source_registry_ids` | Public source IDs from `source-registry-v0`, or `source_registry_id_needed`. | Source IDs are required before a row can support any public claim. |
| `query_record_ids` | Query record IDs, query templates, or `query_record_needed`. | Query provenance is required for trial registry and fast-changing landscape context. |
| `therapy_record_ids` | Therapy-record IDs, public therapy-class IDs, or `therapy_record_needed`. | Therapy links are context only, not selection, sequencing, or ranking. |
| `trial_landscape_record_ids` | Trial-landscape record IDs or `trial_landscape_record_needed`. | Trial links are context only, not eligibility, enrollment, or availability. |
| `product_or_agent_state` | `class_only`, `product_source_defined`, `agent_source_defined`, `product_scope_needed`, `source_missing`, `status_not_extracted`, or `not_applicable`. | Product or agent terms need source, jurisdiction, date, and limitation context before reuse. |
| `therapy_class_state` | Treatment-class taxonomy ID, source-defined class, `class_needed`, or `not_applicable`. | Class labels do not imply appropriateness, access, efficacy, safety, or superiority. |
| `target_or_marker_state` | Target record ID, source-defined target, `target_context_needed`, `source_missing`, or `not_applicable`. | Target terms do not imply targetability, actionability, testing need, treatment fit, or trial fit. |
| `jurisdiction_state` | `jurisdiction_source_defined`, `jurisdiction_needed`, `registry_scope_only`, `not_reported_by_source`, or `not_applicable`. | Jurisdiction is source context only; it is not availability or access for a person. |
| `status_label_state` | `source_defined_status`, `status_label_needed`, `status_not_extracted`, `not_reported_by_source`, or `not_applicable`. | A status label must not be translated into a personal availability, eligibility, or access claim. |
| `status_date_state` | `source_date_recorded`, `registry_timestamp_recorded`, `access_date_recorded`, `status_date_needed`, `date_not_reported_by_source`, or `not_applicable`. | Date state supports audit and freshness only; it does not freeze source truth. |
| `source_freshness_state` | `freshness_checked`, `freshness_needed`, `stale_by_design`, `source_update_unknown`, or `not_applicable`. | Freshness must be visible for registry, product, regulatory, labeling, and fast-moving therapy rows. |
| `access_date_state` | `access_date_recorded`, `access_date_needed`, `source_date_recorded`, `source_date_not_reported`, or `not_applicable`. | Access dates support reproducibility only; they are not clinical validity. |
| `registry_status_state` | `registry_snapshot_only`, `registry_status_needed`, `not_a_trial_record`, `status_not_reported_by_source`, or `not_applicable`. | Registry state cannot imply site availability, enrollment fit, sponsor access, or eligibility. |
| `disease_scope_state` | `multiple_myeloma_source_defined`, `plasma_cell_disease_source_defined`, `subtype_scope_needed`, `source_scope_unclear`, or `not_applicable`. | Disease scope is not diagnosis, prognosis, risk, or treatment-path guidance. |
| `trial_or_registry_scope_state` | `registry_id_recorded`, `query_scope_recorded`, `site_scope_source_defined`, `trial_scope_needed`, `not_a_trial_record`, or `not_applicable`. | Site, trial, or registry scope is not site availability or enrollment advice. |
| `landscape_role` | `background_context`, `therapy_reference`, `trial_registry_context`, `regulatory_context`, `label_context`, `source_refresh_needed`, `review_question_context`, or `not_an_evidence_claim`. | Role does not grade, rank, or validate the row. |
| `uncertainty_state` | `source_limit`, `freshness_limit`, `registry_limit`, `jurisdiction_limit`, `definition_mismatch`, `population_mismatch`, `expert_review_needed`, `unknown`, or `none_stated_by_source`. | Uncertainty must remain visible before reuse. |
| `limitation_note_required` | `true`. | Every row needs limitation text before downstream reuse. |
| `do_not_infer_required` | `true`. | Every row needs explicit overclaiming guardrails. |
| `review_status` | `not_reviewed`, `source_appraisal_needed`, `trial_status_verification_needed`, `sponsor_site_verification_needed`, `regulatory_review_needed`, `clinician_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation and downstream patient-linked reuse. |
| `allowed_public_successor` | `source_registry_delta`, `query_record_template`, `public_task`, `candidate_hypothesis_question_set`, `schema_improvement`, or `none`. | Successor must match the missing dependency and cannot bypass source, clinical, privacy, trial, sponsor, regulatory, or publication gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Landscape Component Semantics

| Component | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| Trial registry landscape | Public registry provenance, registry status label, query scope, data timestamp, access date, and limitation note. | ClinicalTrials.gov query protocol fields, source IDs, freshness state, and review status. | Do not infer eligibility, availability, enrollment, site status, sponsor access, trial fit, or trial recommendation. |
| Therapy or product landscape | Public therapy class, product or agent scope, source-defined status, jurisdiction, date, and limitation note. | Therapy-record schema, treatment-class taxonomy, source registry, and status freshness fields. | Do not infer indication, access, product availability, suitability, comparative value, sequencing, or recommendation. |
| Target or mechanism landscape | Public target, marker, antigen, mechanism, or source-defined context. | Target or mechanism record, method or source context, uncertainty, and review gate. | Do not infer target actionability, testing need, treatment fit, trial fit, safety, efficacy, or patient relevance. |
| Regulatory or label status context | Public source ID, regulator or label source, jurisdiction, source date, access date, and extracted status label. | FDA, DailyMed, EMA, or other source registry context and limitation text. | Do not infer personal access, coverage, prescribing, standard of care, availability, safety, efficacy, or suitability. |
| Jurisdiction and status-date context | Source-defined geographic or regulator scope plus status or access date. | Explicit source, date state, and jurisdiction state. | Do not generalize one jurisdiction, source date, or status label to another setting or to a person. |
| Source freshness and access-date context | Whether a fast-moving source has current provenance fields. | Source registry ID, query record, access date, and freshness state. | Do not treat stale, missing, or incomplete sources as proof of no trial, no product, no status, no evidence, or no option. |
| Therapy exposure linkage | Public link to therapy exposure timeline contract fields, class IDs, broad timepoint buckets, and review status. | Therapy exposure timeline contract and limitation notes. | Do not convert exposure, prior class, response linkage, toxicity, or refractory context into sequencing, eligibility, or treatment guidance. |
| Evidence packet linkage | Public link to evidence packet IDs, query records, source limits, no-completeness warnings, and review state. | Evidence retrieval packet fields and source appraisal status. | Do not rank evidence, claim completeness, match a person, or make clinical conclusions. |
| Review and publication gate status | Review roles needed before stronger reuse or release. | Review status and publication-gate labels. | Do not publish case-derived landscape learning or clinical conclusions from an unreviewed row. |

## Unknown And Missing-State Rules

Unknown and missing landscape states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `source_registry_id_needed` | A source has not been assigned a stable public source ID. | Block claim use and create a source registry delta task. |
| `query_record_needed` | A trial, registry, product, or source-refresh search lacks reproducible query provenance. | Block downstream reuse beyond generic task routing. |
| `freshness_needed` | A fast-moving source lacks a freshness check. | Block status, registry, product, access, and availability-adjacent language. |
| `access_date_needed` | Access date is missing. | Mark source-context-needed before reuse. |
| `jurisdiction_needed` | Source scope or regulator geography is missing. | Preserve missingness; do not generalize status across settings. |
| `status_label_needed` | A public source has not been extracted into a source-defined status label. | Keep as extraction task, not a status claim. |
| `trial_scope_needed` | Registry ID, query scope, or site scope is not captured. | Block trial landscape reuse beyond task routing. |
| `review_needed` | Source appraisal, trial-status, sponsor/site, regulatory, clinician, privacy, or publication review has not occurred. | Do not upgrade claim level or reuse for downstream decisions. |
| `blocked_private` | The landscape row would depend on private case values or private records. | Keep private or rewrite as a generic public-source question. |

Missing landscape data is never evidence of no evidence, no source, no trial,
no site, no sponsor access, no product, no indication, no availability, no
eligibility, no actionability, no need for review, no treatment fit, no trial
fit, no monitoring need, no urgency, no prognosis, or cure.

## Fail-Closed Landscape Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `ttl_00_no_real_case_context` | Public landscape rows must not include private case values, identifiers, records, reports, images, exact dates tied to a person, clinician names, site names tied to a person, source paths, or free-text case details. | Block or move to private-lab-needed. |
| `ttl_01_evidence_packet_prerequisite` | Landscape rows need evidence packet IDs, source IDs, or explicit missing-source states before downstream reuse. | Route to `evidence-retrieval-packet-v0` or mark source-context-needed. |
| `ttl_02_source_registry_required` | Every public source needs a source registry ID or explicit missing-source state. | Create a source registry delta task; block claim use. |
| `ttl_03_query_record_required` | Trial registry, source refresh, and fast-changing landscape rows need query provenance or an explicit missing-query state. | Mark `query_record_needed`; block downstream reuse. |
| `ttl_04_freshness_and_access_visible` | Trial, regulatory, labeling, product, therapy, and registry rows need freshness and access-date state. | Mark `freshness_needed` or `access_date_needed`; block status language. |
| `ttl_05_status_not_personal_availability` | Source-defined status, jurisdiction, registry status, or label context cannot be summarized as available or unavailable for any person. | Rewrite as source context or block. |
| `ttl_06_no_eligibility_or_enrollment_inference` | Trial records cannot imply eligibility, enrollment fit, site availability, sponsor access, or trial recommendation. | Add verification-needed boundary or block. |
| `ttl_07_no_sequencing_or_treatment_guidance` | Therapy class, product, prior exposure, target, trial, or status context cannot imply what should be used before, after, instead of, or next for a person. | Rewrite as public-source context or block. |
| `ttl_08_no_target_actionability` | Target, marker, antigen, mechanism, or assay language cannot imply actionability, testing need, treatment fit, or trial fit. | Route to molecular, target, or mechanism source review; block actionability wording. |
| `ttl_09_no_ranking_or_comparison_output` | Source order, query counts, trial status, products, targets, mechanisms, endpoints, or regulatory labels cannot rank sources, trials, therapies, mechanisms, targets, products, or options. | Rewrite as unranked provenance or block. |
| `ttl_10_no_access_or_expanded_access_instructions` | Public landscape rows cannot generate access steps, referral steps, sponsor contact paths, expanded-access paths, insurance guidance, or timing guidance. | Block and route real-world questions to responsible clinical and institutional processes. |
| `ttl_11_review_gate_required` | Review status must be visible before downstream reuse. | Default to source appraisal, trial-status, sponsor/site, regulatory, clinician, privacy, or publication gate needed. |
| `ttl_12_successor_match` | Landscape gaps must route to the correct public-safe successor. | Route hypothesis framing to `candidate-hypothesis-review-question-set-v0`, source gaps to registry/query tasks, and public learning to the publication gate. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `ttl_test_01_status_without_date` | Product or trial status appears without source date, access date, or freshness state. | Mark `freshness_needed`; block status reuse. |
| `ttl_test_02_registry_row_as_trial_match` | Trial registry row is paired with language about fit, enrollment, eligibility, or availability. | Preserve registry provenance only; block matching and advice. |
| `ttl_test_03_product_as_available` | A source-defined product status is summarized as available or unavailable for a person. | Rewrite as source, jurisdiction, date, and limitation context; block availability claim. |
| `ttl_test_04_target_as_actionable` | Target or marker row is paired with treatment, test, or trial direction. | Preserve target context only; block actionability and guidance. |
| `ttl_test_05_ranked_landscape` | Query counts or status labels are used to rank products, trials, targets, sources, or mechanisms. | Rewrite as unranked provenance; block ranking output. |
| `ttl_test_06_private_case_linkage` | Landscape row includes therapy history, molecular report phrase, location, exact date, or free-text case note from a person. | Block public export as private-only. |
| `ttl_test_07_public_shape_ok` | Generic row with source IDs, query record, therapy and trial record IDs, jurisdiction, status label, freshness, access date, uncertainty, limitation, do-not-infer text, and review status. | Allow as schema planning, public source extraction, public task routing, or candidate-hypothesis question context only. |

## What This Step Revealed

With the evidence retrieval packet complete, the public repo can now represent
trial and therapy landscape context as date-stamped, source-scoped, unranked
public provenance. The missing next dependency is not a trial explorer or
therapy dashboard. It is a question-only review surface that can frame
candidate hypotheses for qualified humans while preserving source limits,
landscape gate status, uncertainty, and blocked uses.

The next safest public step is therefore
`candidate-hypothesis-review-question-set-v0`.

## Handoff State

`trial-therapy-landscape-non-advice-gate-v0` is complete as a public
non-advice landscape gate.

The following remain blocked outside this artifact:

- live trial search, therapy explorer, product dashboard, registry monitor,
  label monitor, source scraper, API workflow, database, backend, account
  workflow, upload path, public submission path, or case-matching system
- public processing of real case values, private records, source documents,
  reports, images, notes, exact dates tied to a person, source paths,
  identifiers, or private prompts
- patient matching, trial matching, evidence grading, product ranking, trial
  ranking, source ranking, target ranking, mechanism ranking, therapy ranking,
  option ranking, or comparative recommendations
- availability, eligibility, enrollment, site-status, sponsor-access,
  expanded-access, access, sequencing, referral, monitoring, urgency,
  safety-management, prognosis, treatment, trial, or patient-specific guidance
- publication of case-derived landscape rows or learning without privacy,
  clinician, source-validity, legal, regulatory, sponsor/site, treating-team,
  and publication gates

ORP should mark this item complete and activate
`candidate-hypothesis-review-question-set-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names tied to a person, sponsor contacts, private
  paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow,
  live trial search, therapy explorer, product dashboard, registry monitor,
  source scraper, or API workflow.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, therapy ranking, trial
  ranking, product ranking, option ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public non-advice gate, not an executable schema.
- This is not a live trial, therapy, product, regulator, label, or source
  status monitor.
- This is not a real landscape record set.
- This does not run literature, registry, regulatory, labeling, dataset,
  therapy, product, or trial searches.
- This does not process, normalize, store, route, publish, match, compare,
  rank, verify, or authorize use of real case-linked landscape context.
- This does not complete source appraisal, consent, privacy, security,
  retention, clinician-review, molecular-review, trial-status verification,
  sponsor/site verification, legal, regulatory, institutional, treating-team,
  or publication gates.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, complete, publication-ready,
  regulatory-ready, or useful for any person.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, urgency guidance, safety-management guidance, emergency guidance,
  referral guidance, evidence ranking, option ranking, or a cure claim.
