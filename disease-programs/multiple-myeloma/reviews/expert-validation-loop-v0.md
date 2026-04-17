# Expert Validation Loop v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-expert-validation-loop-v0`
- ORP item: `expert-validation-loop-v0`
- loop status: public disposition-loop scaffold complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- communication boundary: no outreach, no private correspondence, no copied
  unpublished expert content
- last reviewed: `2026-04-16`

## Purpose

This artifact defines the recurring public-safe expert validation loop for the
multiple myeloma case-to-cure work.

It connects public issue IDs, reviewer-lens fields, outreach-map role labels,
response-ledger dispositions, source-context gaps, artifact paths, blocked-use
flags, and next public actions. It exists so future passes can route expert
validation signals into public tasks, wording guardrails, metadata repairs,
source requests, or blockers without publishing private replies or treating
issue status as completed review.

It does not send outreach, copy private correspondence, publish unpublished
expert comments, disclose reviewer identities beyond already-public outreach
planning artifacts, validate claims, authorize publication, rank options, or
make clinical decisions.

## Current Loop Decision

Current decision: `public-disposition-loop-only`.

Allowed public behavior:

- read public issue IDs, public issue state, public comment counts, artifact
  IDs, source IDs, and review-lens labels
- map a public review item to an allowed disposition and next public action
- preserve public-source context, uncertainty, limitations, and blocked uses
- create source-context tasks, wording guardrail updates, metadata or link
  repair tasks, clarification requests, public permission blockers, publication
  gate blockers, or no-public-action notes
- keep `expert-review-needed` status when public permission, public authorship,
  source context, or review sufficiency is missing

Blocked behavior:

- outreach action or autonomous contact
- private email, private message, meeting note, unpublished correspondence, or
  private reviewer text copied into public artifacts
- reviewer identity disclosure beyond the existing public outreach map
- treating a public issue, comment count, public shortlist, silence, or private
  reply as endorsement, consensus, expert review, clinical review, or
  publication readiness
- diagnosis, prognosis, treatment guidance, trial guidance, expanded-access
  guidance, monitoring guidance, urgency guidance, safety-management guidance,
  candidate-option guidance, recommendation, matching, sequencing, ranking, or
  clinical decision

Allowed public successor:
`case-to-public-learning-extraction-gate-v0`, limited to a sanitation and
publication gate for future public learning extracted from private case work.
The successor must define privacy, aggregation, source-scope, uncertainty,
review, and publication criteria before any case-derived learning can be
public. It must block identifiers, single-case claims, private correspondence,
unpublished expert comments, recommendations, rankings, treatment or trial
guidance, expanded-access guidance, monitoring guidance, publication
authorization, and clinical decisions.

## Loop Envelope

Every expert-validation loop record should be representable with these fields
before a future ledger, issue-update pass, or public task reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `loop_cycle_id` | Stable public cycle ID or `cycle_pending`. | Cycle ID is for audit only; it is not a review decision. |
| `review_item_id` | Review item ID from the public issue index or `review_item_pending`. | Must not contain private reviewer, case, site, or clinician identifiers. |
| `public_issue_id` | Public GitHub issue number or `public_issue_needed`. | Issue presence does not prove review, endorsement, or source sufficiency. |
| `artifact_ids` | Public artifact IDs or `artifact_needed`. | Artifact inclusion is not evidence strength, correctness, or publication readiness. |
| `source_ids` | Public source IDs, `source_context_needed`, or `not_applicable`. | Source IDs are provenance anchors only; source presence is not consensus. |
| `review_lens` | Lens label from the issue index, outreach map, question set, or `lens_needed`. | Lens is a role category, not a named reviewer, endorsement, or decision. |
| `public_contact_role` | Optional public role or route label from the outreach map. | Do not add private contact details or disclose participation. |
| `response_presence_state` | `no_public_response`, `public_response_untriaged`, `public_response_triaged`, `private_response_disposition_only`, `public_permission_needed`, or `not_applicable`. | Response state is not content and does not upgrade review status. |
| `allowed_disposition` | One allowed disposition from this artifact or the response ledger. | Disposition labels must not copy private correspondence. |
| `disposition_basis` | `public_issue_metadata`, `public_source_context`, `permissioned_public_response`, `private_disposition_only`, `missing_public_source`, `blocked_private_or_clinical`, or `operator_boundary_review`. | Private basis can be represented only as a non-content disposition. |
| `public_source_context` | Source IDs, artifact paths, query IDs, public task IDs, or `source_context_needed`. | Public sources are required before any wording or claim update. |
| `uncertainty_state` | `expert_review_needed`, `source_context_needed`, `permission_needed`, `review_lens_needed`, `publication_gate_needed`, `private_or_clinical_gate_needed`, `unknown`, or `not_applicable`. | Uncertainty must remain visible in downstream artifacts. |
| `blocked_use_flags` | Required blocked uses such as `no_private_correspondence`, `no_unpublished_comments`, `no_medical_advice`, `no_recommendation`, `no_ranking`, `no_patient_specific_output`, and `no_publication_authorization`. | Blocked uses must travel with any loop output. |
| `next_public_action` | `keep_review_needed`, `open_source_task`, `update_wording_guardrail`, `repair_metadata_or_link`, `clarify_issue_scope`, `record_public_permission_blocker`, `route_publication_gate`, `record_private_or_clinical_blocker`, or `no_public_action`. | Action must stay public-safe and non-advisory. |
| `private_material_boundary` | `none_seen`, `private_material_not_copied`, `private_material_blocked`, or `not_applicable`. | Private material never enters public artifacts. |
| `publication_gate_state` | `not_applicable`, `publication_gate_needed`, `public_release_blocked`, or `public_release_candidate_after_review`. | This loop cannot authorize publication. |
| `review_status` | `not_reviewed`, `expert_review_needed`, `source_context_needed`, `public_permission_needed`, `blocked_private_or_clinical`, `public_shape_only`, or `public_disposition_recorded`. | Review status is not clinical validity or claim upgrade. |
| `public_export_allowed` | `false` by default. | Export requires public source context, permission where needed, privacy review, and publication gate when case-derived learning is involved. |

## Allowed Dispositions

| Disposition | Meaning | Public Action |
| --- | --- | --- |
| `keep_expert_review_needed` | No safe public disposition has enough support to close the item. | Keep current language bounded and review-needed. |
| `source_context_needed` | More public provenance, assay, measurement, registry, regulatory, or disease-state context is needed. | Create or update a public source task or source-context note. |
| `public_correction_task` | A public, source-backed correction or addition can be requested. | Open or draft a public task with source IDs and limitations. |
| `wording_guardrail_update` | Public wording should be weaker, clearer, or safer. | Patch wording while preserving source IDs, uncertainty, and blocked uses. |
| `metadata_or_link_repair` | Artifact metadata, catalog entry, or navigation link needs repair. | Update metadata, catalog, or links; do not change claim status. |
| `issue_clarification_needed` | The public issue needs a narrower ask or clearer boundary. | Update issue-facing wording only if public and non-advisory. |
| `public_permission_needed` | A response may be useful but cannot be represented publicly yet. | Record permission-needed status without copying content. |
| `human_publication_gate_needed` | The next step may affect public release readiness. | Route to publication gate; do not publish from this loop. |
| `private_correspondence_blocked` | The only available signal is private or unpublished. | Record non-content blocker and keep public artifacts unchanged. |
| `out_of_scope_or_no_public_action` | The request is outside the public repo or has no safe public follow-up. | Record no public action and preserve the boundary. |
| `superseded_by_public_source` | A public source or artifact already resolves the narrow issue. | Link the public source and keep limitations visible. |

These labels can be crosswalked to the existing response ledger dispositions,
but this loop uses underscore names for machine-safe future records.

## Loop Stages

| Stage | Public-Safe Operation | Fail-Closed Rule |
| --- | --- | --- |
| `evl_00_public_issue_lookup` | Read the public issue index for issue ID, review item, packet, focus, and artifact path. | If no public issue or artifact path exists, mark `source_context_needed` or `issue_clarification_needed`. |
| `evl_01_review_lens_mapping` | Map the review lens from the issue index, outreach map, candidate question set, or builder route. | Do not infer a named reviewer, endorsement, or participant. |
| `evl_02_response_state_check` | Read only safe public metadata and ledger disposition state. | Do not copy private correspondence or unpublished expert comments. |
| `evl_03_public_source_context_check` | Check source IDs, public artifact paths, query IDs, task IDs, and limitation context. | If public source context is missing, do not update claim strength. |
| `evl_04_disposition_selection` | Choose one allowed disposition and one next public action. | If the signal asks for advice, ranking, matching, or patient-specific output, block as private or clinical. |
| `evl_05_public_action_route` | Route to source task, wording guardrail update, metadata repair, issue clarification, blocker, or publication gate. | Do not route to outreach, private-lab work, clinical decision, or publication authorization. |
| `evl_06_orp_handoff` | Record what the loop revealed and activate the next public-safe item. | Public learning extraction requires its own sanitation and publication gate. |

## Source Inputs

| Input | Loop Use | Boundary |
| --- | --- | --- |
| [Expert Validation Issue Index v0](expert-validation-issue-index-v0.md) | Provides public issue IDs, review item IDs, packet names, focus categories, artifact paths, and next public actions. | Issue creation does not complete expert review. |
| [Expert Validation Outreach Map v0](expert-validation-outreach-map-v0.md) | Provides public role/lens planning and public shortlist context. | The map is not outreach, endorsement, participation, or validation. |
| [Expert Response Validation Ledger v0](expert-response-validation-ledger-v0.md) | Provides public-safe response state and allowed disposition rules. | Ledger entries do not copy private correspondence or prove expert authorship. |
| [Candidate Hypothesis Review Question Set v0](candidate-hypothesis-review-question-set-v0.md) | Provides review-lens, uncertainty, blocked-use, and no-patient-action fields for question-scoped review. | Questions are not options, recommendations, rankings, or actions for a person. |
| [Multidisciplinary Review Packet Builder v0](multidisciplinary-review-packet-builder-v0.md) | Provides copy, reference, omit, and refuse behavior for question and artifact routes. | Builder routing cannot assemble packets, generate prose, or authorize review. |
| [Publication-Gate Checklist v0](../publication-gate-checklist-v0.md) | Provides release blockers and publication decision outcomes. | This loop cannot publish or clear case-derived learning. |
| [Source Registry v0](../../../sources/source-registry-v0.md) | Provides reusable public source IDs and claim-use limits. | Source presence is not evidence completeness, consensus, or clinical actionability. |
| [Public Safety](../../../governance/PUBLIC_SAFETY.md) | Provides repository-wide public safety rules. | Safety rules remain upstream of every disposition. |
| [Private-To-Public Workflow](../../../docs/private-to-public-workflow.md) | Provides private-to-public export requirements and claim labels. | Export still requires private governance and public review. |
| [Case-To-Cure Adaptive Master Plan v0](../case-to-cure-adaptive-master-plan-v0.md) | Provides the next-step synthesis rule. | The master plan is not complete until the completion audit is reached or blocked. |
| [Case-To-Cure Pipeline Blueprint v0](../case-to-cure-pipeline-blueprint-v0.md) | Provides pipeline stage context and public/private boundaries. | Pipeline stages are not real case processing. |

## Fail-Closed Loop Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `evl_00_no_private_correspondence` | Private emails, private messages, unpublished replies, meeting notes, or private reviewer text must not be copied or paraphrased into public artifacts. | Record `private_correspondence_blocked` or `public_permission_needed`. |
| `evl_01_public_permission_required` | Expert response content can be represented only when it is already public or permissioned for public use and has public source context. | Keep content out of public and record a non-content disposition. |
| `evl_02_no_outreach_action` | This artifact cannot send outreach, prepare outbound messages as completed action, or change public participation status. | Record a public planning status only. |
| `evl_03_no_identity_disclosure` | Do not add private reviewer identities, contact details, affiliations tied to participation, or deliberation notes. | Use public role labels or block. |
| `evl_04_source_context_required` | Wording or claim updates need public source IDs, artifact paths, or explicit source-needed status. | Route to source task or keep expert-review-needed. |
| `evl_05_no_advice_or_ranking` | No loop output may recommend, rank, sequence, match, or guide treatment, trials, expanded access, monitoring, urgency, or safety management. | Refuse and mark private-or-clinical blocker. |
| `evl_06_no_review_upgrade_by_metadata` | Issue state, comment count, outreach listing, or private reply presence cannot upgrade an item to expert-reviewed. | Keep review-needed unless public, permissioned, source-contextual review is documented. |
| `evl_07_no_publication_authorization` | Disposition records cannot authorize release or case-derived public learning. | Route to publication gate or block. |
| `evl_08_successor_match` | Loop findings must route to the correct public-safe successor. | Route public learning questions to `case-to-public-learning-extraction-gate-v0`; route private case facts to private-lab-needed. |

## Synthetic Loop Tests

These tests describe validator expectations. They are not real expert
responses.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `evl_test_01_private_email_blocked` | A private email says wording should change but is not public or permissioned. | Record `private_correspondence_blocked`; do not copy content. |
| `evl_test_02_public_issue_status_ok` | Public issue metadata shows open status, labels, and comment count. | Preserve as status only; keep `expert_review_needed` until triaged. |
| `evl_test_03_public_source_task_ok` | Public issue identifies a missing source ID and safe extraction need. | Route to `public_correction_task` or `source_context_needed`. |
| `evl_test_04_private_quote_blocked` | Proposed update includes a quote from unpublished correspondence. | Block and require public permission plus public source context. |
| `evl_test_05_outreach_action_blocked` | Proposed loop action says to contact a named person. | Block autonomous outreach; retain only public planning role context. |
| `evl_test_06_advice_wording_blocked` | Response suggests what a patient should do next. | Mark private-or-clinical blocker; no public action except boundary note. |
| `evl_test_07_publication_claim_blocked` | Disposition says expert response makes the artifact publication-ready. | Route to publication gate; do not authorize release. |

## What This Step Revealed

The public repo can now make expert validation recurring without making the
loop into outreach, response ingestion, private correspondence handling, or
expert-review substitution. The loop can preserve issue IDs, artifact IDs,
source IDs, review lenses, allowed dispositions, uncertainty, blocked uses,
and next public actions, but any future public learning extracted from private
case work still needs a separate sanitation and publication gate.

The next safest public step is therefore
`case-to-public-learning-extraction-gate-v0`.

## Handoff State

`expert-validation-loop-v0` is complete as a public disposition-loop scaffold.

The following remain blocked outside this artifact:

- autonomous outreach, contact, or follow-up
- private correspondence intake, copied private email text, unpublished expert
  comments, meeting notes, or private reviewer deliberation
- private reviewer identities, private contact details, participation claims,
  endorsements, consensus claims, or reviewer decisions
- real case facts, private records, raw reports, images, notes, exact dates
  tied to a person, private paths, identifiers, prompts, or re-identification
  keys
- diagnosis, prognosis, treatment guidance, trial guidance, eligibility
  guidance, availability guidance, expanded-access guidance, access guidance,
  monitoring guidance, urgency guidance, safety-management guidance,
  recommendation, ranking, matching, sequencing, patient-specific output,
  publication authorization, or clinical decision
- public learning extraction from private case work without privacy,
  aggregation, source-scope, uncertainty, legal, clinical, regulatory,
  treating-team, and publication gates

ORP should mark this item complete and activate
`case-to-public-learning-extraction-gate-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names tied to a person, sponsor contacts, contact
  details, private paths, private prompts, or re-identification keys.
- No private correspondence, unpublished expert comments, private reviewer
  identities, or completed outreach.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, therapy ranking, trial
  ranking, product ranking, option ranking, or review decision.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This is a public loop contract, not a response ingestion system.
- This is not outreach, expert review, clinical review, or publication review.
- This does not inspect private correspondence, private lab records, or real
  case data.
- This does not prove that any public issue response is expert-authored,
  source-backed, sufficient, endorsed, consensus-based, or clinically valid.
- This does not make any artifact expert-reviewed or publication-ready.
- This does not authorize generated claims, ranking, recommendation behavior,
  patient matching, trial matching, review-packet assembly, response
  publication, or case-derived public learning.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, monitoring guidance,
  safety-management guidance, urgency guidance, publication guidance, or a
  cure claim.
