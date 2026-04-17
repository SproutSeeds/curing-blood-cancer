# Case Feature Normalization Contract v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-case-feature-normalization-contract-v0`
- active ORP item: `case-feature-normalization-contract-v0`
- contract status: public shape contract complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no records, no uploads,
  no fillable public case-feature bundle, no patient-specific interpretation
- last reviewed: `2026-04-16`

## Purpose

This contract defines the public-safe shape for normalized disease-state and
context features that may be used later inside a governed private multiple
myeloma case-to-cure workflow.

It exists so the public repo can reason about feature groups, unknown states,
source status, timepoint buckets, review gates, and limitations without
processing a real person or turning context into clinical guidance.

## Use Boundary

This contract is not:

- a fillable public case schema
- an intake form
- a case normalizer
- a database, backend, upload path, account workflow, or public submission path
- a risk score, prognosis tool, eligibility tool, treatment selector, trial
  matcher, monitoring plan, urgency guide, option ranking, or cure claim
- a substitute for clinician, privacy, security, legal, regulatory, or
  publication review

Real case feature normalization remains private-only until consent, privacy,
security, retention, emergency, clinician-review, legal, regulatory, and
publication gates are completed outside this public repo.

## Current Contract Decision

Current decision: `public-shape-only`.

The contract may be used for schema planning, synthetic fixtures, validator
rules, and public task routing. It must not be used to collect, normalize,
interpret, publish, or rank real case features.

Allowed public successor: `measurement-normalization-contract-v0`, limited to
MRD, response, relapse, lab, imaging, method, threshold, sample, timepoint,
durability, endpoint role, source context, uncertainty, and limitation fields.
The successor must block cure claims, prognosis, treatment guidance, trial
guidance, monitoring guidance, and patient-specific interpretation.

## Normalized Feature Envelope

Every public-safe normalized feature group should be representable with these
fields before any downstream artifact reuses it:

| Field | Allowed Public Shape | Required Boundary |
| --- | --- | --- |
| `feature_group_id` | `disease_state`, `measurement_context`, `therapy_exposure_context`, `molecular_immune_context`, `context_modifier`, `evidence_linkage`, or `review_gate_status`. | Group label only; no real case values. |
| `feature_id` | Stable public field name or private-only field-group ID. | Must not contain identifiers, report text, exact dates, sites, clinician names, or rare person-specific combinations. |
| `value_state` | `source_defined_category`, `unknown`, `not_sure`, `not_tested`, `not_collected`, `source_missing`, `private_only`, `synthetic_placeholder`, `not_applicable`, or `blocked_from_public`. | Missingness is never evidence of absence, prognosis, eligibility, urgency, treatment fit, trial fit, or cure. |
| `source_type` | `public_source`, `caregiver_report_private`, `portal_summary_private`, `lab_report_private`, `pathology_report_private`, `imaging_report_private`, `genomics_report_private`, `clinician_note_private`, `unknown`, or `not_collected`. | Source class only; no source contents or private source paths. |
| `source_status` | `source_seen_private`, `source_reported_not_seen`, `source_missing`, `public_source_only`, or `not_collected`. | Public artifacts may preserve status, not the private record. |
| `timepoint_bucket` | `baseline`, `during_treatment`, `post_treatment`, `relapse_context`, `follow_up`, `unknown`, or `not_collected`. | Bucket only; no exact dates tied to a person. |
| `review_status` | `not_reviewed`, `clinician_review_needed`, `lab_validity_review_needed`, `measurement_review_needed`, `privacy_review_needed`, `publication_gate_needed`, `reviewed_private`, or `public_shape_only`. | Public reuse defaults to review-needed unless explicitly synthetic, public-source-only, or approved aggregate. |
| `limitation_note_required` | `true`. | Every feature group needs a limitation note before downstream reuse. |
| `allowed_public_successor` | `schema_improvement`, `synthetic_fixture`, `public_task`, `measurement_contract`, `therapy_timeline_contract`, `molecular_immune_contract`, `evidence_packet_skeleton`, or `none`. | Successor must match the feature group and cannot bypass gates. |
| `public_export_allowed` | `false` by default. | Public export requires synthetic-only, public-source-only, aggregate-learning-only, or publication-gate approval. |

## Feature Group Semantics

| Feature Group | Public-Safe Meaning | Required Context | Blocked Use |
| --- | --- | --- | --- |
| Disease-state envelope | Source-stated disease setting, response vocabulary, and review-needed flags for private normalization planning. | `value_state`, source type, source status, timepoint bucket, review status, and limitation note. | Do not assert diagnosis, disease stage, relapse status, refractory status, prognosis, urgency, or care path for a person. |
| Context modifier | Optional, source-scoped labels such as high-risk, extramedullary, organ, bone, immune, frailty, performance, or prior-exposure context. | Use the context modifier map's `public_value_state` behavior and require source context. | Do not infer prognosis, eligibility, treatment intensity, trial fit, monitoring need, or option ranking. |
| Measurement context placeholder | A pointer that measurement terms need their own method, threshold, sample, timepoint, endpoint, and limitation semantics. | Route to `measurement-normalization-contract-v0`. | Do not flatten MRD, response, relapse, lab, or imaging language into cure, progression, safety, or monitoring claims. |
| Therapy exposure placeholder | A pointer that therapy exposures need their own line, class, source, response, toxicity, and constraint semantics. | Route to `therapy-exposure-timeline-contract-v0`. | Do not infer sequencing, eligibility, availability, recommendation, or ranking. |
| Molecular and immune placeholder | A pointer that cytogenetic, genomic, target-assay, pathology, flow, and immune context need source and method validity semantics. | Route to `molecular-immune-context-contract-v0`. | Do not infer actionability, target fit, test need, treatment choice, or trial fit. |
| Evidence linkage | Public source IDs, public artifact IDs, or task IDs that may support later public-source retrieval. | Source registry IDs and limitations. | Do not case-match a person to evidence, products, trials, or candidate options. |
| Review and gate status | Whether a feature group is public-shape-only, private-review-needed, publication-gate-needed, or blocked. | Explicit gate label and blocker class. | Do not treat missing review as permission to publish or interpret. |

## Unknown And Missing-State Rules

Unknown and missing states must remain first-class values:

| State | Meaning | Required Public Handling |
| --- | --- | --- |
| `unknown` | The private team or caregiver does not know. | Preserve as uncertainty; do not infer a finding. |
| `not_sure` | The private reporter is unsure. | Preserve as uncertainty; do not convert to present or absent. |
| `not_tested` | A test or assessment is not known to have occurred. | Do not infer absence of a feature or need for a test. |
| `not_collected` | The field was not collected for the public-safe shape. | Do not infer that the information is unavailable privately. |
| `source_missing` | A recalled or named concept lacks source context. | Mark source-context-needed before reuse. |
| `private_only` | The field may exist only in a governed private workspace. | Do not project into public artifacts. |
| `blocked_from_public` | The field is unsafe to reuse publicly. | Remove, rewrite as a generic task, or keep private. |

Missing data is never evidence of absence, risk, treatment fit, trial fit,
monitoring need, urgency, or cure.

## Fail-Closed Normalization Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `cfn_00_no_real_bundle` | A public artifact must not contain a filled case-feature bundle for a real person. | Block or move to private-lab-needed. |
| `cfn_01_required_value_state` | Every feature group must carry a `value_state`. | Mark source-context-needed or schema-improvement-needed. |
| `cfn_02_source_before_value` | A source class and source status must be present before a value-like label can be reused. | Treat as `source_missing` and block interpretation. |
| `cfn_03_timepoint_bucket_only` | Public artifacts may use timepoint buckets only. | Remove exact dates tied to a person. |
| `cfn_04_missing_not_absence` | Unknown, not-sure, not-tested, not-collected, and source-missing states cannot imply absence or reassurance. | Preserve uncertainty and add a limitation note. |
| `cfn_05_context_non_directive` | Context modifiers cannot produce prognosis, eligibility, treatment, monitoring, urgency, or ranking. | Rewrite as non-directive context or block. |
| `cfn_06_measurement_defer` | Measurement-specific fields must route to the measurement normalization contract. | Block response-depth, MRD, relapse, lab, or imaging interpretation until the measurement contract exists. |
| `cfn_07_therapy_defer` | Therapy-specific fields must route to the therapy exposure timeline contract. | Block sequencing, recommendation, and eligibility language. |
| `cfn_08_molecular_defer` | Molecular and immune fields must route to the molecular/immune context contract. | Block actionability, testing, treatment, or trial-fit inference. |
| `cfn_09_review_gate_required` | Review status must be visible before downstream reuse. | Default to `review_needed` or `publication_gate_needed`. |
| `cfn_10_public_successor_match` | Allowed public successor must match the feature group. | Block successor if it bypasses measurement, therapy, molecular, evidence, privacy, or publication gates. |

## Synthetic Test Cases

These cases describe validator expectations. They are not real case records.

| Test ID | Synthetic Input Shape | Expected Public Verdict |
| --- | --- | --- |
| `cfn_test_01_unknown_preserved` | Disease-state envelope with `value_state: "unknown"` and source status `source_missing`. | Keep as uncertainty; no diagnosis, prognosis, or routing output. |
| `cfn_test_02_not_tested_preserved` | Molecular placeholder with `value_state: "not_tested"`. | Do not infer absence of a target, actionability, test need, or treatment fit. |
| `cfn_test_03_private_context_blocked` | Context modifier carrying exact dates, site names, or report text. | Block public export as `private_only` or `blocked_from_public`. |
| `cfn_test_04_measurement_deferred` | MRD or relapse phrase without method, threshold, sample, timepoint, and endpoint role. | Route to `measurement-normalization-contract-v0`; block cure or monitoring language. |
| `cfn_test_05_successor_mismatch` | Therapy exposure group routed directly to evidence scoring. | Block; route first to therapy exposure timeline contract. |
| `cfn_test_06_public_shape_ok` | Generic field-group label with value state, source class, source status, timepoint bucket, review status, limitation note, and no person-specific content. | Allow as schema planning or synthetic fixture shape only. |

## What This Step Revealed

The public repo can safely define the normalized case-feature envelope, but it
cannot safely define all measurement, therapy exposure, and molecular/immune
semantics in one artifact.

The highest-risk next public dependency is measurement language. MRD,
response-depth, relapse, labs, and imaging can easily become cure claims,
prognosis, or monitoring guidance if method, threshold, sample, timepoint,
durability, endpoint role, source context, and limitations are missing.

The next safest public step is therefore
`measurement-normalization-contract-v0`.

## Handoff State

`case-feature-normalization-contract-v0` is complete as a public shape
contract.

The following remain blocked outside this artifact:

- executable public normalization of real case data
- public case uploads, save/resume workflows, accounts, storage, or records
- exact timelines, dates tied to a person, reports, images, notes, private
  source paths, identifiers, sites, or provider names
- clinician interpretation, diagnosis assertions, response assessment,
  prognosis, eligibility, treatment guidance, trial guidance, monitoring
  guidance, urgency guidance, expanded-access guidance, ranking, or cure claims
- publication of case-derived learning without privacy, clinician, source, and
  publication gates

ORP should mark this item complete and activate
`measurement-normalization-contract-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, or
  free-text case details.
- No public intake form, upload path, backend, database, account workflow, or
  fillable real-case schema.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  expanded-access, monitoring, urgency, safety-management, publication, or
  candidate-option guidance.
- No patient matching, trial matching, option ranking, evidence ranking, or
  review decision.
- No cure or vaccine claim.

## Limitations

- This is a public shape contract, not an executable schema.
- This is not a real case-feature bundle.
- This does not process, normalize, store, route, publish, or authorize use of
  real case data.
- This does not complete consent, privacy, security, retention, emergency,
  clinician-review, legal, regulatory, institutional, sponsor, site,
  treating-team, or publication gates.
- This does not validate measurement, therapy exposure, molecular, immune,
  evidence retrieval, trial, therapy landscape, candidate hypothesis,
  multidisciplinary review, or public-learning extraction semantics.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, or regulatory-ready.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, emergency
  guidance, or a cure claim.
