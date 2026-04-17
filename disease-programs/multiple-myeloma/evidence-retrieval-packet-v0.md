# Evidence Retrieval Packet v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-evidence-retrieval-packet-v0`
- active ORP item: `evidence-retrieval-packet-v0`
- packet status: public source skeleton complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public sources only; no real case data, no identifiers, no
  private records, no case matching, no trial matching, no target
  actionability, no ranking, no patient-specific interpretation
- last reviewed: `2026-04-16`

## Purpose

This packet defines the public-safe evidence retrieval shape for future
private multiple myeloma case-to-cure questions.

It exists so downstream work can preserve source IDs, query records, source
freshness, access-date state, limitations, uncertainty, no-completeness
warnings, and review status before any evidence, trial, therapy, target, or
mechanism language is reused.

It does not retrieve evidence for a person, match a person to evidence, match
a person to trials, rank sources, interpret targets, or advise on treatment,
monitoring, access, eligibility, or trial participation.

## Use Boundary

This packet is not:

- a case-matched evidence packet
- a trial matcher, eligibility checker, availability checker, site finder, or
  expanded-access pathway
- a target actionability record, biomarker interpretation, evidence grade,
  treatment selector, option ranking, prognosis tool, monitoring plan, or cure
  claim
- a live retrieval system, search engine, scraper, API workflow, database,
  backend, account workflow, upload path, or public submission path
- a substitute for source appraisal, clinician review, molecular review,
  trial-site verification, sponsor verification, legal review, regulatory
  review, privacy review, or publication review

Real case-linked evidence retrieval remains private-only until consent,
privacy, security, retention, source-validity, clinician-review, legal,
regulatory, sponsor/site, treating-team, and publication gates are completed
outside this public repo.

## Current Packet Decision

Current decision: `public-source-skeleton-only`.

This packet may be used for schema planning, source registry hygiene, query
record design, synthetic fixtures, validator rules, and public task routing. It
must not be used to retrieve, match, interpret, rank, publish, or recommend
evidence for a real person.

Allowed public successor:
`trial-therapy-landscape-non-advice-gate-v0`, limited to non-advisory
landscape fields for trial, therapy, product, target, jurisdiction, status,
source freshness, access-date state, limitations, and uncertainty. The
successor must block availability claims, eligibility claims, sequencing
advice, urgency guidance, expanded-access guidance, ranking, and
patient-specific trial or treatment guidance.

## Packet Envelope

Every public-safe evidence retrieval packet should be representable with these
fields before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `packet_id` | Stable public packet ID or `packet_pending`. | ID is for audit only; it is not a case ID. |
| `retrieval_question_id` | Public research question ID, source-extraction task ID, evidence-gap ID, or `question_pending`. | Question must be generic or public-source-only; no private case values. |
| `retrieval_intent` | `source_discovery`, `source_refresh`, `query_record_capture`, `mechanism_context`, `measurement_context`, `therapy_landscape_context`, `trial_landscape_context`, `hypothesis_review_prep`, or `public_task_routing`. | Intent cannot become patient matching, clinical triage, option selection, or care planning. |
| `normalized_context_links` | Links to case-feature, measurement, therapy exposure, molecular/immune, mechanism, target, or public-task artifacts. | Links preserve public field groups only; no real case contents or report text. |
| `source_registry_ids` | Source IDs from `source-registry-v0`, or `source_registry_id_needed`. | Public source IDs are required before a source can support claims or retrieval notes. |
| `query_record_ids` | Query record IDs, query templates, or `query_record_needed`. | Query provenance is required; raw private prompts or case details are blocked. |
| `source_type` | `trial_registry`, `literature_index`, `regulatory_database`, `labeling_database`, `public_dataset_index`, `public_overview`, `measurement_standard`, `target_reference`, `therapy_reference`, `mechanism_source`, or `source_type_needed`. | Source type does not establish quality, completeness, relevance, eligibility, availability, safety, efficacy, or actionability. |
| `source_freshness_state` | `freshness_checked`, `freshness_needed`, `stale_by_design`, `source_update_unknown`, or `not_applicable`. | Freshness must be visible for trial, product, regulatory, registry, and fast-moving therapy references. |
| `access_date_state` | `access_date_recorded`, `access_date_needed`, `source_date_recorded`, `source_date_not_reported`, or `not_applicable`. | Access dates support audit only; they do not freeze source truth. |
| `retrieval_status` | `not_started`, `query_planned`, `query_recorded`, `source_seen_public`, `source_extract_pending`, `source_context_needed`, `review_needed`, `blocked_private`, or `public_shape_only`. | Status must not imply a complete search, evidence sufficiency, or clinical readiness. |
| `evidence_role` | `background_context`, `measurement_definition`, `mechanism_context`, `therapy_reference`, `trial_registry_context`, `regulatory_context`, `dataset_discovery`, `source_appraisal_needed`, or `not_an_evidence_claim`. | Role does not grade, rank, or validate the source. |
| `claim_level_allowed` | `fact`, `derived`, `hypothesis`, `open-question`, `do-not-use-clinically`, or `claim_not_allowed`. | Claim level must stay lower when source appraisal, method context, or review is missing. |
| `uncertainty_state` | `source_limit`, `query_limit`, `freshness_limit`, `definition_mismatch`, `population_mismatch`, `method_limit`, `registry_limit`, `expert_review_needed`, `unknown`, or `none_stated_by_source`. | Uncertainty cannot be erased by generated wording. |
| `limitation_note_required` | `true`. | Every packet needs limitation and what-not-to-infer text before reuse. |
| `no_completeness_warning_required` | `true`. | Public packets must warn that a search or source list may be incomplete. |
| `review_status` | `not_reviewed`, `source_appraisal_needed`, `measurement_review_needed`, `molecular_review_needed`, `clinician_review_needed`, `trial_status_verification_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation and downstream patient-linked reuse. |
| `allowed_public_successor` | `schema_improvement`, `source_registry_delta`, `query_record_template`, `public_task`, `trial_therapy_landscape_gate`, `candidate_hypothesis_question_set`, or `none`. | Successor must match the missing dependency and cannot bypass source, clinical, privacy, trial, sponsor, or publication gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Packet Component Semantics

| Component | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| Source registry snapshot | Stable source IDs, owner, source type, claim-use labels, and claim limits. | Source registry record and access date. | Do not treat registry presence as evidence quality, actionability, availability, or clinical relevance. |
| Literature query record | Search terms, public URL or index query, run date, and intended public use. | Query terms, source IDs, date, limitation note, and appraisal-needed state. | Do not replace paper appraisal, rank papers, infer patient relevance, or claim completeness. |
| Trial registry query record | Public trial query fields, source IDs, API/version freshness when available, and no-advice boundary. | ClinicalTrials.gov protocol fields, source freshness, access date, and verification-needed state. | Do not infer trial availability, eligibility, enrollment fit, sponsor access, site status, or trial recommendation. |
| Regulatory or label source record | Source ID, jurisdiction, product or class context, source date, access date, and limitation note. | Regulatory source ID and status freshness. | Do not infer patient suitability, comparative value, access, coverage, availability, or treatment choice. |
| Dataset discovery record | Public dataset index source, disease scope, reuse caveat, and access date. | Dataset source ID, public/restricted status, and limitation note. | Do not infer clinical truth, patient comparability, or permission to use controlled-access data. |
| Normalized context linkage | Public links to measurement, therapy exposure, and molecular/immune shape contracts. | Context link IDs and review status. | Do not insert real values, case timelines, molecular reports, therapy histories, or patient-specific summaries. |
| Source extraction linkage | Link to source-extraction tasks, gap IDs, mechanism groups, measurement terms, or open-question records. | Public artifact IDs and claim level. | Do not convert open questions into claims, options, rankings, or next actions. |
| Limitation and no-completeness ledger | Explicit missingness, query limitations, source limitations, and stale-source warnings. | Limitation note and no-completeness warning. | Do not imply that absence from a packet means absence from evidence, trials, products, or care options. |
| Review and publication gate state | Review roles needed before reuse or release. | Review status and gate labels. | Do not publish case-derived learning or clinical conclusions from an unreviewed packet. |

## Unknown And Missing-State Rules

Unknown and missing evidence states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `source_registry_id_needed` | A source has not been assigned a stable public source ID. | Block claim use and create a source registry delta task. |
| `query_record_needed` | A search or retrieval action lacks reproducible query provenance. | Block reuse beyond a generic task. |
| `freshness_needed` | A fast-moving source lacks a current freshness check. | Block trial, product, regulatory, or status language. |
| `access_date_needed` | Access date is missing. | Add source-context-needed before reuse. |
| `source_context_needed` | A source is named but the role, limit, or scope is not captured. | Keep as open question or extraction task. |
| `review_needed` | Source appraisal or domain review has not occurred. | Do not upgrade claim level or reuse for downstream decisions. |
| `blocked_private` | The retrieval would depend on private case values or private records. | Keep private or rewrite as a generic public-source question. |

Missing evidence is never evidence of no evidence, no trial, no therapy, no
target, no availability, no eligibility, no risk, no actionability, no need for
review, no prognosis, no monitoring need, no treatment fit, or cure.

## Fail-Closed Retrieval Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `erp_00_no_real_case_query` | Public packets must not include private case values, identifiers, records, reports, images, exact dates, clinician names, site names, source paths, or free-text case details. | Block or move to private-lab-needed. |
| `erp_01_source_registry_required` | Every source used for public retrieval needs a source registry ID or explicit missing-source state. | Create a source registry delta task; block claim use. |
| `erp_02_query_record_required` | Every retrieval action needs a reproducible public query record or explicit query-missing state. | Mark `query_record_needed`; block downstream reuse. |
| `erp_03_freshness_visible` | Trial, regulatory, labeling, therapy, product, and fast-moving landscape sources need freshness and access-date state. | Mark `freshness_needed` or `access_date_needed`; block status language. |
| `erp_04_no_completeness_claim` | A packet cannot say the search is complete or that no evidence exists unless a reviewed protocol specifically supports that narrow statement. | Add no-completeness warning or block. |
| `erp_05_no_evidence_ranking` | Source order, counts, endpoints, trial status, labels, or query results cannot rank sources, mechanisms, targets, therapies, trials, or options. | Rewrite as unranked provenance or block. |
| `erp_06_no_patient_matching` | Public packets cannot match a person to evidence, therapies, products, targets, studies, trials, sites, or access routes. | Remove case linkage or move to private-lab-needed. |
| `erp_07_no_trial_matching` | Trial registry queries cannot imply eligibility, availability, enrollment fit, site status, sponsor access, or trial recommendation. | Add verification-needed boundary or block. |
| `erp_08_no_actionability` | Target, molecular, immune, therapy, or mechanism language cannot imply actionability or patient fit. | Route to source extraction or expert review; block actionability wording. |
| `erp_09_no_clinical_guidance` | Evidence packets cannot produce diagnosis, prognosis, treatment, trial, monitoring, safety-management, urgency, referral, expanded-access, or care-path guidance. | Rewrite as public-source context or block. |
| `erp_10_context_links_required` | Measurement, therapy exposure, and molecular/immune terms need their upstream shape-contract links before evidence reuse. | Route back to the missing contract or mark source-context-needed. |
| `erp_11_review_gate_required` | Review status must be visible before downstream reuse. | Default to source appraisal, clinician, trial-status, privacy, or publication gate needed. |
| `erp_12_successor_match` | Evidence gaps must route to the correct public-safe successor. | Route landscape extraction to `trial-therapy-landscape-non-advice-gate-v0`, hypothesis framing to `candidate-hypothesis-review-question-set-v0`, and public learning to the publication gate. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `erp_test_01_source_missing` | A source is cited by name but has no source registry ID. | Mark `source_registry_id_needed`; block claim use. |
| `erp_test_02_query_missing` | A public literature or trial search appears without query terms, run date, or source ID. | Mark `query_record_needed`; block downstream reuse. |
| `erp_test_03_stale_trial_status` | A trial registry result is reused without freshness or access-date state. | Mark `freshness_needed`; block availability or eligibility language. |
| `erp_test_04_private_case_prompt_blocked` | A packet query contains a therapy history, molecular report phrase, location, exact date, or free-text case note. | Block public export as private-only. |
| `erp_test_05_no_completeness_warning` | A packet says no trials or no evidence exist after one query. | Add no-completeness warning and block the absence claim. |
| `erp_test_06_target_actionability_blocked` | A source about a target is paired with treatment, trial, or test direction. | Preserve source context only; block actionability and guidance. |
| `erp_test_07_public_shape_ok` | Generic packet with source IDs, query record, freshness state, access-date state, context links, uncertainty, limitation note, no-completeness warning, and review status. | Allow as schema planning, public task routing, or public-source extraction shape only. |

## What This Step Revealed

With the case-feature, measurement, therapy exposure, and molecular/immune
contracts complete, the public repo can now describe evidence retrieval as an
auditable packet skeleton rather than a live retrieval or matching system.

The next missing public dependency is the trial and therapy landscape boundary.
Trial, therapy, product, target, jurisdiction, status, source-freshness, and
limitation fields need their own non-advisory gate before any landscape record
or hypothesis review can reuse evidence retrieval outputs safely.

The next safest public step is therefore
`trial-therapy-landscape-non-advice-gate-v0`.

## Handoff State

`evidence-retrieval-packet-v0` is complete as a public-source packet skeleton.

The following remain blocked outside this artifact:

- live evidence retrieval, scraping, API workflows, databases, accounts,
  uploads, or public submissions
- public processing of real case values, private records, source documents,
  reports, images, notes, exact dates, source paths, identifiers, or private
  prompts
- patient matching, trial matching, target actionability, evidence grading,
  evidence ranking, source ranking, mechanism ranking, therapy ranking, trial
  ranking, product ranking, or option ranking
- availability, eligibility, enrollment, site-status, sponsor-access,
  expanded-access, sequencing, referral, monitoring, urgency, safety,
  efficacy, prognosis, treatment, trial, or patient-specific guidance
- publication of case-derived evidence packets or learning without privacy,
  clinician, source-validity, legal, regulatory, sponsor/site, treating-team,
  and publication gates

ORP should mark this item complete and activate
`trial-therapy-landscape-non-advice-gate-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names, sponsor contacts, private paths, or free-text
  case details.
- No public intake form, upload path, backend, database, account workflow,
  search engine, scraper, API workflow, or case-matched retrieval packet.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, option ranking, or
  review decision.
- No cure or vaccine claim.

## Limitations

- This is a public packet skeleton, not an executable schema.
- This is not a live retrieval workflow.
- This is not a real evidence packet.
- This does not run literature, registry, regulatory, labeling, dataset, or
  trial searches.
- This does not process, normalize, store, route, publish, match, compare,
  rank, grade, or authorize use of real case-linked evidence.
- This does not complete source appraisal, consent, privacy, security,
  retention, clinician-review, molecular-review, trial-status verification,
  sponsor/site verification, legal, regulatory, institutional, treating-team,
  or publication gates.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, complete, publication-ready, regulatory-ready,
  or useful for any person.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, urgency guidance, safety-management guidance, emergency guidance,
  referral guidance, evidence ranking, option ranking, or a cure claim.
