# Case-To-Public Learning Extraction Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-case-to-public-learning-extraction-gate-v0`
- ORP item: `case-to-public-learning-extraction-gate-v0`
- gate status: public sanitation and publication-gate scaffold complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no public extraction of real case facts; no identifiers, raw
  records, person-linked dates, private correspondence, single-case claims, or
  patient-specific outputs
- last reviewed: `2026-04-16`

## Purpose

This artifact defines the public-safe gate that must sit between future
private case work and any public learning artifact.

It exists so a later private-lab or synthetic-only workflow can decide whether
a proposed public learning record is only a synthetic fixture, generic method
improvement, public-source linkage, separately reviewed aggregate learning,
blocker note, or not-public material. It preserves artifact IDs, source IDs,
issue IDs, review lenses, disposition states, privacy decision state,
allowed output type, uncertainty, limitations, blocked uses, and publication
gate state before anything case-derived can be prepared for public review.

It is not a de-identification system, extractor, case summarizer, publication
workflow, release authorization, clinical review, legal review, regulatory
review, trial finder, treatment selector, monitoring plan, or advice surface.

## Current Gate Decision

Current decision: `public-learning-extraction-gate-only`.

Allowed public behavior:

- represent a proposed learning output as an audit envelope with public IDs,
  source context, review state, uncertainty, limitations, and blocked uses
- narrow the output to one allowed public output type before any artifact work
- route unsafe material to `blocked_private`, `aggregate_review_needed`,
  `source_context_needed`, `human_publication_gate_needed`, or
  `public_release_blocked`
- preserve only synthetic examples, generic method improvements,
  public-source linkages, or separately reviewed aggregate learning as possible
  public release candidates
- activate a synthetic-only dry run that exercises the gate without real case
  material

Blocked behavior:

- public extraction, copying, paraphrasing, summarizing, or publishing of real
  case facts, raw records, images, reports, notes, exact person-linked dates,
  private paths, prompts, identifiers, or re-identification keys
- publication of a single-case observation, trajectory, treatment response,
  outcome, adverse event, molecular finding, trial fit, or monitoring pattern
- copying private correspondence, unpublished expert comments, reviewer
  deliberation, or private permission context into public artifacts
- patient-specific diagnosis, prognosis, treatment guidance, trial guidance,
  eligibility guidance, availability guidance, expanded-access guidance,
  access guidance, monitoring guidance, safety-management guidance, urgency
  guidance, recommendation, sequencing, matching, ranking, or clinical decision
- publication authorization, release announcement, public case report,
  clinical clearance, legal clearance, regulatory clearance, sponsor/site
  decision, institutional-review decision, or treating-team decision

Allowed public successor:
`end-to-end-synthetic-case-dry-run-v0`, limited to a visibly artificial
dry-run artifact that exercises success, omit, refusal, and blocker paths from
synthetic caregiver intake through projection, normalization, evidence
retrieval, review routing, expert validation disposition, and publication-gate
refusal. The successor must not use real case data, identifiers, private
records, patient-specific outputs, recommendations, rankings, matching,
clinical guidance, or publication authorization.

## Extraction Gate Envelope

Every future case-to-public learning record should be representable with these
fields before any public artifact candidate reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `learning_extract_id` | Stable public gate record ID or `extract_pending`. | Must not include private case IDs, dates, sites, clinicians, or rare feature combinations. |
| `private_origin_class` | `none_synthetic`, `generic_method`, `public_source_only`, `private_case_aggregate_candidate`, `private_case_single_candidate`, `private_correspondence`, or `unknown`. | Anything private, single-case, or correspondence-based starts blocked. |
| `allowed_output_type` | `synthetic_method_fixture`, `generic_method_improvement`, `public_source_linkage`, `deidentified_aggregate_learning_after_gate`, `blocker_note_only`, or `not_public`. | Output type must be narrowed before artifact drafting. |
| `case_linkage_state` | `no_case_linkage`, `synthetic_only`, `aggregate_only_after_review`, `single_case_blocked`, `private_case_blocked`, or `unknown`. | Single-case linkage cannot be public. |
| `privacy_decision_state` | `not_applicable`, `privacy_review_needed`, `privacy_public_boundary_passed`, `privacy_public_boundary_failed`, or `private_governance_needed`. | Privacy pass is not publication authorization or de-identification proof. |
| `deidentification_basis` | `not_applicable`, `synthetic_only`, `public_source_only`, `aggregate_review_documented`, `basis_needed`, or `basis_failed`. | De-identification must not rely on public removal of obvious identifiers alone. |
| `aggregation_state` | `not_applicable`, `aggregate_review_needed`, `aggregate_minimum_met_after_private_review`, `aggregate_too_small`, or `unknown`. | Aggregate learning must not expose a person, site, clinician, date, or rare combination. |
| `minimum_group_size_state` | `not_applicable`, `threshold_recorded_private`, `threshold_needed`, `threshold_failed`, or `human_gate_needed`. | Public repo does not set private cohort thresholds by itself. |
| `single_case_claim_state` | `absent`, `present_blocked`, `unclear_blocked`, or `not_applicable`. | Any single-case claim blocks public release. |
| `public_source_ids` | Source IDs from the source registry, `source_context_needed`, or `not_applicable`. | Public source IDs are provenance anchors only, not evidence completeness or clinical actionability. |
| `artifact_ids` | Public artifact IDs, `artifact_needed`, or `not_applicable`. | Artifact linkage is not review, endorsement, or publication readiness. |
| `issue_ids` | Public issue IDs, review item IDs, `issue_needed`, or `not_applicable`. | Issue state cannot substitute for expert review or publication review. |
| `review_lens` | Public role label from the question set, review builder, expert loop, or `lens_needed`. | Lens is a category, not a named reviewer or decision. |
| `disposition_state` | Allowed disposition from the expert loop, publication gate, or `disposition_needed`. | Disposition content must not copy private correspondence. |
| `uncertainty_state` | `source_context_needed`, `privacy_review_needed`, `aggregate_review_needed`, `expert_review_needed`, `publication_gate_needed`, `private_or_clinical_gate_needed`, `unknown`, or `not_applicable`. | Uncertainty must travel with any public output. |
| `limitation_ids_or_text` | Public limitation IDs, limitation text, or `limitation_needed`. | Limitations are required before public reuse. |
| `blocked_use_flags` | Required flags such as `no_patient_specific_output`, `no_medical_advice`, `no_recommendation`, `no_ranking`, `no_matching`, `no_private_correspondence`, and `no_publication_authorization`. | Flags must be copied into any downstream dry run, artifact, or catalog note. |
| `publication_gate_state` | `not_applicable`, `publication_gate_needed`, `public_release_blocked`, `public_release_candidate_after_human_review`, or `human_publication_gate_needed`. | This gate cannot authorize publication. |
| `human_gate_state` | `not_applicable`, `privacy_needed`, `clinical_needed`, `legal_needed`, `regulatory_needed`, `ethics_needed`, `treating_team_needed`, `publication_needed`, or `multiple_human_gates_needed`. | External decisions remain outside public automation. |
| `allowed_public_successor` | `synthetic_dry_run`, `schema_improvement`, `source_task`, `metadata_repair`, `aggregate_release_candidate_after_human_review`, `blocker_note`, or `none`. | Successor cannot be public case processing or clinical guidance. |
| `public_export_allowed` | `false` by default. | Export can become candidate-only after privacy, source, review, and publication gates, never by this artifact alone. |

## Allowed Output Types

| Output Type | Allowed Public Shape | Required Block |
| --- | --- | --- |
| `synthetic_method_fixture` | Visibly artificial example that exercises schemas, gate states, validators, and refusal paths. | No real case values, rare combinations, person-linked dates, or private paths. |
| `generic_method_improvement` | Reusable field, checklist, validator rule, template, or metadata repair. | No private lab operation detail, private record detail, or patient-specific inference. |
| `public_source_linkage` | Linkage among public source IDs, artifact IDs, query IDs, issue IDs, task IDs, or limitation IDs. | No linkage that reveals a private case trajectory, institution, clinician, sponsor, or family constraint. |
| `deidentified_aggregate_learning_after_gate` | Aggregate pattern only after private governance, privacy review, source context, reviewer roles, and publication gate are documented. | No single-person fact, small-cell pattern, exact date, rare combination, or public clinical action. |
| `blocker_note_only` | Public note that names the blocked gate class and next safe owner. | No private content, no advice, no claim upgrade. |
| `not_public` | Material remains private or out of scope. | Do not summarize, sanitize, paraphrase, or publish. |

## Gate Stages

| Stage | Public-Safe Operation | Fail-Closed Rule |
| --- | --- | --- |
| `cpl_00_origin_classification` | Classify whether proposed learning is synthetic, public-source-only, generic method, aggregate candidate, single-case candidate, correspondence, or unknown. | Unknown, private, correspondence, or single-case origin blocks public release. |
| `cpl_01_output_type_narrowing` | Choose one allowed output type. | If output type is missing or mixed, route to `revise_public_method` or `not_public`. |
| `cpl_02_privacy_boundary_check` | Check identifiers, raw records, exact dates, rare combinations, private paths, and re-identification risk state. | Any unresolved privacy state blocks release and routes to private governance. |
| `cpl_03_aggregation_check` | Check aggregate status, minimum-size state, and single-case-claim state. | Single-case claims and insufficient aggregate states block public release. |
| `cpl_04_public_provenance_check` | Preserve public source IDs, artifact IDs, issue IDs, query IDs, and limitation links. | Missing public provenance blocks claim use and routes to source-context task or blocker. |
| `cpl_05_review_disposition_check` | Preserve review lens, expert-loop disposition, uncertainty, and needed human gates. | Public issue or disposition state cannot substitute for expert, clinical, privacy, or publication review. |
| `cpl_06_clinical_use_check` | Check blocked-use flags for advice, matching, ranking, monitoring, eligibility, availability, access, and clinical decisions. | Any patient-action wording blocks the output. |
| `cpl_07_publication_gate_route` | Route to publication gate outcome or blocker. | This gate cannot authorize publication, release, protected-branch merge, announcement, or case report. |
| `cpl_08_orp_handoff` | Record what the gate revealed and activate the next public-safe item. | The next item must be synthetic-only dry run, not real case extraction. |

## Decision Outcomes

| Decision | Meaning | Public Action |
| --- | --- | --- |
| `blocked_private` | The material contains private case facts, identifiers, records, raw details, correspondence, or unresolved governance. | Do not publish; keep private or record blocker note only. |
| `revise_public_method` | A useful public method shape exists but needs narrower wording, provenance, limitations, or blocked-use flags. | Revise as a generic method improvement. |
| `source_context_needed` | Public source IDs, artifact IDs, issue IDs, or limitation context are missing. | Open or update a public source-context task. |
| `aggregate_review_needed` | Aggregate learning might be possible but lacks privacy, cohort-size, review, or publication-gate evidence. | Hold until private governance and public safety gates are documented. |
| `human_publication_gate_needed` | The output may become a release candidate only after human review. | Route to publication gate; do not publish from this gate. |
| `public_release_candidate_after_human_review` | The envelope records a candidate state after required human gates. | Prepare for ordinary repository review only; this is not clinical clearance. |
| `public_release_blocked` | One or more public safety gates failed. | Do not publish until resolved and re-reviewed. |

## Source Inputs

| Input | Gate Use | Boundary |
| --- | --- | --- |
| [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md) | Provides issue IDs, review lenses, allowed dispositions, uncertainty, blocked uses, and next public actions. | Dispositions are not endorsements, expert review, or publication authorization. |
| [Publication-Gate Checklist v0](publication-gate-checklist-v0.md) | Provides allowed output types, release record fields, gate checklist, and decision outcomes. | The checklist itself cannot publish real case facts or authorize clinical use. |
| [Private-To-Public Workflow](../../docs/private-to-public-workflow.md) | Provides export-candidate, provenance, limitation, and private upstream requirements. | Private export still requires governed review before public drafting. |
| [Public Safety](../../governance/PUBLIC_SAFETY.md) | Provides repository-wide no-private-data, no-advice, provenance, and uncertainty rules. | Safety rules remain upstream of every extraction decision. |
| [Source Registry v0](../../sources/source-registry-v0.md) | Provides public source IDs and claim-use limits. | Source presence is not evidence completeness, consensus, or clinical actionability. |
| [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md) | Provides stage owners, gates, blockers, and allowed successors for `case_00` through `case_14`. | Stage coverage is not real case processing. |
| [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md) | Provides private/public zones and the `case_14` outcome-capture boundary. | Blueprint language cannot select action paths or publish outcomes. |
| [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md) | Provides next-step synthesis and master-completion rules. | The master plan is not complete until the completion audit is reached or blocked. |
| [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md) | Provides no-PHI and no-advice projection refusal logic. | Projection checks cannot process real case data publicly. |
| [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md) | Provides consent, privacy, security, retention, emergency, clinician-review, and publication blockers. | The gate does not authorize real intake or storage. |
| [Multiple Myeloma Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md) | Provides a synthetic-only stage fixture for the next dry run. | Synthetic fixture coverage is not permission to use real cases. |

## Fail-Closed Gate Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `cpl_00_no_private_case_material` | Public outputs must not include identifiers, raw records, reports, images, notes, exact person-linked dates, private paths, private prompts, or re-identification keys. | Mark `blocked_private`; do not summarize or sanitize into public. |
| `cpl_01_no_single_case_claim` | A single case fact, trajectory, outcome, response, adverse event, assay result, or treatment sequence cannot become a public claim. | Mark `single_case_claim_state=present_blocked`. |
| `cpl_02_output_type_required` | Every proposed output must name one allowed output type. | Route to `revise_public_method` or `not_public`. |
| `cpl_03_privacy_state_required` | Case-derived learning needs privacy decision state, de-identification basis, aggregation state, and human-gate state. | Route to `private_governance_needed` or `aggregate_review_needed`. |
| `cpl_04_public_source_context_required` | Public-source, artifact, issue, or query IDs are required when a public artifact depends on source context. | Route to `source_context_needed`; block claim use. |
| `cpl_05_no_private_correspondence` | Private email, private messages, unpublished expert comments, or reviewer deliberation cannot be copied, paraphrased, or represented as content. | Record `private_correspondence` origin and block or require public permission plus source context. |
| `cpl_06_review_state_visible` | Review lens, disposition state, uncertainty, limitations, and blocked-use flags must remain visible downstream. | Block or revise until fields are explicit. |
| `cpl_07_no_advice_matching_or_ranking` | No output may recommend, rank, sequence, match, compare, prioritize, or guide treatment, trials, expanded access, monitoring, urgency, safety management, or care. | Mark `public_release_blocked`. |
| `cpl_08_publication_gate_required` | Any case-derived public learning must route through publication-gate state and human publication review. | Mark `human_publication_gate_needed`; this artifact cannot publish. |
| `cpl_09_successor_match` | The next public-safe work after this gate must be synthetic-only dry run or a public method repair. | Activate `end-to-end-synthetic-case-dry-run-v0`; route real case extraction to private-lab-needed. |

## Synthetic Gate Tests

These tests describe validator expectations. They are not real case records or
expert responses.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `cpl_test_01_private_record_blocked` | Proposed learning includes a report phrase, private path, exact date, or source record detail. | `blocked_private`; no public artifact content. |
| `cpl_test_02_single_case_anecdote_blocked` | Proposed learning says one case responded, relapsed, progressed, tolerated, or failed a treatment. | `public_release_blocked`; single-case claim remains private. |
| `cpl_test_03_aggregate_missing_state_blocked` | Aggregate pattern is proposed without privacy decision, aggregation state, minimum-size state, or publication-gate state. | `aggregate_review_needed`. |
| `cpl_test_04_public_source_linkage_ok` | Public source IDs, artifact IDs, issue IDs, uncertainty, limitations, and blocked uses are linked without private case facts. | Allow `public_source_linkage` as a public method record. |
| `cpl_test_05_synthetic_fixture_ok` | Visibly artificial fixture exercises gate fields and refusal paths. | Allow `synthetic_method_fixture` for dry-run use only. |
| `cpl_test_06_private_expert_email_blocked` | Proposed learning depends on unpublished expert email text. | Block private correspondence; record non-content disposition only. |
| `cpl_test_07_advice_or_ranking_blocked` | Proposed learning ranks options or says what a patient should do next. | `public_release_blocked`. |
| `cpl_test_08_publication_ready_claim_blocked` | Proposed learning says gate completion makes an artifact public-ready or clinically cleared. | Route to publication gate; no authorization. |

## What This Step Revealed

The public repo can now name the exact sanitation boundary for case-derived
learning without creating a de-identification engine, extractor, publication
workflow, or clinical decision surface. The key missing proof is no longer a
new gate; it is a synthetic-only end-to-end dry run that shows the current
public pipeline can carry success, omit, refusal, and blocker states from
intake through publication gate without touching real case material.

The next safest public step is therefore
`end-to-end-synthetic-case-dry-run-v0`.

## Handoff State

`case-to-public-learning-extraction-gate-v0` is complete as a public
sanitation and publication-gate scaffold.

The following remain blocked outside this artifact:

- real case extraction, public case summaries, public case reports, public
  outcome records, raw record processing, or de-identification automation
- identifiers, raw records, images, notes, report text, exact dates tied to a
  person, private paths, private prompts, re-identification keys, or rare
  identifying feature combinations
- single-case claims, private correspondence, unpublished expert comments,
  reviewer deliberation, reviewer identity disclosure, or copied private
  permission context
- patient-specific diagnosis, prognosis, treatment guidance, trial guidance,
  eligibility guidance, availability guidance, expanded-access guidance,
  access guidance, monitoring guidance, urgency guidance, safety-management
  guidance, recommendation, matching, sequencing, ranking, option selection,
  publication authorization, release authorization, or clinical decision
- clinical, privacy, legal, regulatory, sponsor, institutional-review,
  treating-team, ethics, security, retention, emergency, or publication
  decisions

ORP should mark this item complete and activate
`end-to-end-synthetic-case-dry-run-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names tied to a person, sponsor contacts, contact
  details, private paths, private prompts, or re-identification keys.
- No single-case claims, public case report, de-identification automation,
  private correspondence, unpublished expert comments, or reviewer decisions.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, product ranking, therapy
  ranking, trial ranking, option ranking, or review decision.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This is a public gate contract, not an executable validator.
- This is not a de-identification system, extractor, case summarizer, case
  report, publication workflow, release authorization, or private governance
  workflow.
- This does not inspect private lab records, private correspondence, expert
  replies, or real case data.
- This does not prove that any future aggregate learning is sufficiently
  de-identified, source-backed, reviewed, legally cleared, regulatory-ready,
  clinically appropriate, publication-ready, or useful for any person.
- This does not complete expert review, clinical review, molecular review,
  pathology review, trial-status verification, sponsor/site verification,
  privacy review, legal review, regulatory review, ethics review,
  treating-team review, or publication review.
- This does not authorize generated claims, public case processing, public
  case upload, response publication, patient matching, trial matching, target
  actionability, recommendation behavior, source ranking, evidence ranking,
  target ranking, mechanism ranking, product ranking, therapy ranking, trial
  ranking, option ranking, or case-derived public learning.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, safety-management guidance, urgency guidance, publication
  guidance, or a cure claim.
