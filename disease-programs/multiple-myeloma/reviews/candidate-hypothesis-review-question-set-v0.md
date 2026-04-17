# Candidate Hypothesis Review Question Set v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-candidate-hypothesis-review-question-set-v0`
- ORP item: `candidate-hypothesis-review-question-set-v0`
- question-set status: public question-only scaffold complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public source and synthetic method context only; no real case
  data, no identifiers, no private records, no patient matching, no trial
  matching, no candidate options for a person, no recommendations, no ranking,
  no availability or eligibility claims, and no patient-specific
  interpretation
- last reviewed: `2026-04-16`

## Purpose

This question set defines how candidate hypotheses can be framed for qualified
human review without becoming candidate options, treatment choices, trial
choices, expanded-access paths, monitoring plans, rankings, or patient action.

It exists so later review-packet work can preserve evidence packet IDs,
landscape gate status, source context, uncertainty, review lens, blocked uses,
and explicit no-action boundaries before any private multidisciplinary review
packet is assembled.

It does not generate hypotheses for a person, select hypotheses, score
hypotheses, rank hypotheses, recommend care, recommend trials, recommend
expanded access, or decide what any person should do.

## Use Boundary

This question set is not:

- a candidate-option list, treatment selector, trial selector,
  expanded-access pathway, monitoring plan, urgency guide, referral guide,
  prognosis tool, actionability record, evidence ranking, option ranking, or
  cure claim
- a private multidisciplinary review packet, tumor-board packet, clinician
  summary, real case summary, or public case-derived learning artifact
- a scoring engine, rubric runner, route-table builder, review-packet builder,
  natural-language generator, database, backend, account workflow, upload path,
  public intake form, or public submission path
- a substitute for source appraisal, clinician review, molecular review,
  pathology review, trial-status verification, sponsor or site verification,
  regulatory review, ethics review, legal review, treating-team review, privacy
  review, or publication review

Real case-linked candidate hypothesis review remains private-only until
consent, privacy, security, retention, source-validity, clinical, legal,
regulatory, sponsor/site, treating-team, and publication gates are completed
outside this public repo.

## Current Question-Set Decision

Current decision: `public-question-scaffold-only`.

This artifact may be used for schema planning, source-task routing, review
packet planning, synthetic fixtures, validator rules, and public task hygiene.
It must not be used to create, select, score, rank, compare, recommend,
publish, or authorize candidate options for a real person.

Allowed public successor:
`multidisciplinary-review-packet-builder-v0`, limited to a public-safe packet
builder skeleton and route rules. The successor must preserve question IDs,
artifact IDs, source IDs, review-lens fields, missing-input blockers, safety
boundaries, and no-generated-claims behavior. It must block real case facts,
generated biomedical prose, patient-specific outputs, recommendations,
rankings, trial matching, eligibility, availability, expanded-access guidance,
monitoring guidance, publication authorization, and clinical decisions.

## Question Envelope

Every candidate hypothesis review question should be representable with these
fields before a later review packet, manifest, or route table reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `question_set_id` | Stable public question-set ID or `question_set_pending`. | ID is for audit only; it is not a case, option, score, or recommendation ID. |
| `question_id` | Stable public question ID or `question_pending`. | Question IDs must not contain private case identifiers, exact dates, sites, clinicians, or rare person-specific combinations. |
| `candidate_hypothesis_type` | `standard_care_review_question`, `trial_review_question`, `expanded_access_boundary_question`, `research_only_hypothesis_question`, `target_or_biomarker_context_question`, `measurement_or_endpoint_context_question`, `safety_or_feasibility_boundary_question`, `no_go_or_blocker_review_question`, or `not_applicable`. | Type selects reviewer lens only; it is not a candidate option type for a person. |
| `question_text` | Public, source-scoped question text with placeholders or generic source-defined terms. | Must not include real case values, recommendations, rankings, or patient-action wording. |
| `evidence_packet_ids` | Evidence packet IDs, `evidence_packet_needed`, or `not_applicable`. | Evidence links preserve provenance only; they do not establish evidence strength, relevance, or actionability. |
| `landscape_gate_ids` | Trial/therapy landscape gate IDs, `landscape_gate_needed`, or `not_applicable`. | Landscape links are non-advisory and cannot imply availability, eligibility, trial fit, or access. |
| `source_registry_ids` | Public source IDs, `source_registry_id_needed`, or `not_applicable`. | Source IDs are required before a question can cite a public source. |
| `query_record_ids` | Query record IDs, `query_record_needed`, or `not_applicable`. | Query provenance is required for trial, product, source-refresh, and evidence-retrieval questions. |
| `context_artifact_links` | Links to public measurement, therapy exposure, molecular/immune, mechanism, target, landscape, or public-task artifacts. | Links preserve public field groups only; no private case contents or report text. |
| `review_lens` | `clinician_review`, `trial_operations_review`, `molecular_review`, `pathology_or_flow_review`, `regulatory_or_access_review`, `safety_ethics_review`, `patient_communication_review`, `source_appraisal_review`, or `publication_gate_review`. | Review lens is not reviewer identity, endorsement, decision, or completed review. |
| `required_review_roles` | Role labels copied from public review templates or `role_needed`. | Roles must not expose private reviewer identities or imply review is complete. |
| `claim_level_allowed` | `open-question`, `hypothesis`, `do-not-use-clinically`, or `claim_not_allowed`. | Candidate questions cannot upgrade claim strength. |
| `uncertainty_state` | `source_limit`, `query_limit`, `freshness_limit`, `measurement_limit`, `landscape_limit`, `translation_limit`, `feasibility_limit`, `review_needed`, `unknown`, or `none_stated_by_source`. | Uncertainty must remain visible and cannot be erased by generated wording. |
| `blocked_use_flags` | List of blocked uses such as `no_patient_matching`, `no_trial_matching`, `no_recommendation`, `no_ranking`, `no_actionability`, `no_eligibility`, `no_availability`, `no_expanded_access_guidance`, `no_monitoring_guidance`, and `no_publication_authorization`. | Blocked uses are required before public reuse. |
| `no_patient_action_output` | `true`. | Every public question must state that it produces no action for a person. |
| `review_status` | `not_reviewed`, `source_appraisal_needed`, `clinician_review_needed`, `molecular_review_needed`, `trial_status_verification_needed`, `regulatory_review_needed`, `ethics_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Missing review blocks interpretation and downstream patient-linked reuse. |
| `allowed_public_successor` | `review_packet_builder_skeleton`, `source_registry_delta`, `query_record_template`, `public_task`, `schema_improvement`, `blocker_note`, or `none`. | Successor must match the missing dependency and cannot bypass source, clinical, privacy, trial, sponsor, regulatory, ethics, or publication gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Review Question Families

These families are reusable public question forms. They are not candidate
options and they are not ranked.

| Family ID | Public-Safe Question Form | Required Context | Blocked Use |
| --- | --- | --- | --- |
| `chq_standard_care_context_v0` | What public source and reviewer context would be needed to discuss a source-defined standard-care concept as a generic review question? | Source IDs, disease scope, measurement context, clinician-review-needed status, and no-action boundary. | Do not recommend, compare, sequence, or personalize standard care. |
| `chq_trial_landscape_context_v0` | What public registry and landscape fields would a qualified reviewer need before discussing a trial concept generically? | Evidence packet ID, query record, ClinicalTrials.gov source IDs, landscape gate status, freshness, access date, and trial-operations lens. | Do not infer eligibility, availability, site status, sponsor access, enrollment fit, or trial recommendation. |
| `chq_expanded_access_boundary_v0` | What public source gaps and external decision classes would need review before an investigational or expanded-access concept could even be discussed privately? | Product or regulatory source context, sponsor/regulator/institution/treating-physician decision classes, uncertainty, and blocker state. | Do not provide expanded-access instructions, feasibility claims, access routes, or timing guidance. |
| `chq_research_only_mechanism_v0` | What mechanism, target, or biology question remains research-only, and which public sources or reviewer roles would clarify it? | Mechanism map, target context, source IDs, molecular or translational review lens, and limitations. | Do not infer actionability, targetability, treatment fit, trial fit, or patient relevance. |
| `chq_measurement_endpoint_context_v0` | What measurement, endpoint, sample, method, threshold, timepoint, or durability context is missing before a review question can be safely framed? | Measurement normalization contract, MRD guardrails, source IDs, and measurement-review lens. | Do not infer response, relapse, prognosis, monitoring need, or cure. |
| `chq_safety_feasibility_boundary_v0` | What safety, ethics, feasibility, logistics, or source-validity blockers must remain visible before any private review? | Safety/ethics lens, uncertainty, review status, and blocked-use flags. | Do not create safety-management guidance, urgency guidance, contraindication claims, access guidance, or feasibility conclusions. |
| `chq_no_go_or_blocker_v0` | What public-safe blocker or no-go question should remain closed until named review, source, privacy, or publication gates are satisfied? | Blocker type, required owner role, source or privacy basis, and no-action boundary. | Do not treat no-go as failure, recommendation, ranking, or clinical decision. |

## Question Text Rules

Use question-only wording:

- "What public source context is missing before this can be reviewed?"
- "Which qualified reviewer role would need to inspect this source-scoped
  question?"
- "What uncertainty or limitation must stay attached to this question?"
- "What is explicitly blocked from inference or public action?"
- "What public task or blocker should this question route to next?"

Do not use action wording:

- "Should the patient..."
- "The next option is..."
- "Best", "better", "preferred", "more promising", or "ranked"
- "Eligible", "available", "open for this person", or "recommended"
- "Proceed", "refer", "enroll", "switch", "start", "stop", "monitor", or
  "seek expanded access"

## Fail-Closed Question Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `chq_00_no_real_case_content` | Public questions must not include private case values, identifiers, records, reports, images, exact dates tied to a person, clinician names, site names tied to a person, source paths, or free-text case details. | Block or move to private-lab-needed. |
| `chq_01_question_only` | Candidate hypotheses must be phrased as review questions, not options, instructions, recommendations, or conclusions. | Rewrite as a question or block. |
| `chq_02_source_context_required` | Questions need public source IDs, evidence packet IDs, or explicit missing-source states before downstream reuse. | Route to source registry delta, evidence packet, or source extraction task. |
| `chq_03_landscape_gate_required` | Trial, therapy, product, target, jurisdiction, status, or access-context questions need the landscape non-advice gate. | Route back to `trial-therapy-landscape-non-advice-gate-v0` or mark landscape-context-needed. |
| `chq_04_review_lens_required` | Questions need a reviewer lens or explicit missing-role state. | Mark `role_needed`; block packet assembly. |
| `chq_05_no_scoring_or_ranking` | The public question set cannot score, rank, compare, prioritize, or select hypotheses, sources, options, therapies, products, targets, mechanisms, or trials. | Remove score/rank language or block. |
| `chq_06_no_availability_or_eligibility` | Trial and product questions cannot imply availability, eligibility, site status, sponsor access, or enrollment fit. | Add verification-needed boundary or block. |
| `chq_07_no_actionability` | Target, marker, mechanism, molecular, or immune language cannot imply actionability, testing need, treatment fit, or trial fit. | Route to molecular, target, or mechanism review; block actionability wording. |
| `chq_08_no_publication_authorization` | Question inclusion cannot authorize publication or public release of case-derived learning. | Route to publication gate or block. |
| `chq_09_successor_match` | Question-set gaps must route to the correct public-safe successor. | Route packet skeleton needs to `multidisciplinary-review-packet-builder-v0`, source gaps to registry/query tasks, and public learning to the publication gate. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `chq_test_01_private_case_blocked` | A question includes a real therapy history, molecular report phrase, location, exact date, or free-text case note. | Block public export as private-only. |
| `chq_test_02_option_rewritten` | A question says a therapy, trial, target, or pathway should be considered next. | Rewrite as source-scoped review question; block recommendation. |
| `chq_test_03_ranked_hypothesis_blocked` | A question labels one hypothesis as most promising, best, preferred, or higher priority for care. | Remove ranking and preserve as unranked review context only. |
| `chq_test_04_trial_fit_blocked` | A question pairs a trial registry row with eligibility, availability, site, or enrollment wording. | Preserve registry provenance only; block trial matching and advice. |
| `chq_test_05_missing_lens_blocked` | A question lacks reviewer role, source context, uncertainty, or blocked-use flags. | Mark missing fields and block packet assembly. |
| `chq_test_06_research_only_ok` | Generic mechanism question has public source IDs, uncertainty, translational review lens, limitations, blocked-use flags, and no patient-action output. | Allow as public review-question scaffold only. |
| `chq_test_07_no_go_ok` | Generic blocker question records source, privacy, review, or publication gates and no public action output. | Allow as blocker question, not a decision for a person. |

## What This Step Revealed

The public repo can now frame candidate hypotheses as review questions without
creating public candidate options. The question set exposes a useful next
dependency: a future multidisciplinary review packet builder must be able to
copy, reference, omit, and refuse question fields without generating
biomedical prose, adding rankings, or assembling real packets.

The next safest public step is therefore
`multidisciplinary-review-packet-builder-v0`.

## Handoff State

`candidate-hypothesis-review-question-set-v0` is complete as a public
question-only scaffold.

The following remain blocked outside this artifact:

- real case-linked hypothesis generation, candidate-option lists, treatment
  selection, trial selection, expanded-access path selection, monitoring plan
  selection, or action-path selection
- public processing of real case values, private records, source documents,
  reports, images, notes, exact dates tied to a person, source paths,
  identifiers, or private prompts
- scoring, ranking, prioritizing, comparing, recommending, or selecting
  hypotheses, sources, therapies, products, targets, mechanisms, trials, or
  options for a person
- availability, eligibility, enrollment, site-status, sponsor-access,
  expanded-access, access, sequencing, referral, monitoring, urgency,
  safety-management, prognosis, treatment, trial, or patient-specific guidance
- public review-packet assembly, generated biomedical prose, or publication of
  case-derived learning without privacy, clinician, source-validity, legal,
  regulatory, sponsor/site, treating-team, and publication gates

ORP should mark this item complete and activate
`multidisciplinary-review-packet-builder-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, therapy histories, molecular reports, pathology reports,
  clinician names, site names tied to a person, sponsor contacts, private
  paths, or free-text case details.
- No public intake form, upload path, backend, database, account workflow,
  route-table builder, review-packet builder, scoring engine, or generated
  biomedical prose.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  availability, access, expanded-access, monitoring, urgency,
  safety-management, referral, publication, or candidate-option guidance.
- No patient matching, trial matching, target actionability, source ranking,
  evidence ranking, target ranking, mechanism ranking, therapy ranking, trial
  ranking, product ranking, option ranking, or review decision.
- No cure or vaccine claim.

## Limitations

- This is a public question-only scaffold, not an executable schema.
- This is not a real candidate-option record set.
- This does not assemble review packets.
- This does not run scoring, routing, literature, registry, regulatory,
  labeling, dataset, therapy, product, target, mechanism, or trial searches.
- This does not process, normalize, store, route, publish, match, compare,
  rank, verify, or authorize use of real case-linked candidate hypotheses.
- This does not complete source appraisal, consent, privacy, security,
  retention, clinician-review, molecular-review, trial-status verification,
  sponsor/site verification, legal, regulatory, institutional, treating-team,
  ethics, or publication gates.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, complete, publication-ready,
  regulatory-ready, or useful for any person.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  availability guidance, expanded-access guidance, access guidance, monitoring
  guidance, urgency guidance, safety-management guidance, emergency guidance,
  referral guidance, evidence ranking, option ranking, or a cure claim.
