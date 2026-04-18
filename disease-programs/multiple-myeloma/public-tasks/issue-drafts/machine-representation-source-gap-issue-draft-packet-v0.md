# Machine Representation Source-Gap Issue Draft Packet v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `machine-representation-source-gap-issue-draft-packet-v0`
- active ORP item: `machine-representation-source-gap-issue-draft-packet-v0`
- packet status: human-reviewable issue draft text; no autonomous issue creation
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only; no real case data, identifiers, raw
  records, uploads, exact person-linked dates, free-text case details, private
  correspondence, model weights, predictions, recommendations, matching,
  ranking, or clinical decisions
- last reviewed: `2026-04-18`

## Purpose

This packet turns the ready tasks in
[Machine Representation Source-Gap Task Queue v0](../machine-representation-source-gap-task-queue-v0.md)
into reusable public issue draft text.

It exists so a human maintainer can review, edit, split, or decline issue text
before any public issue is opened. It does not open issues, send outreach,
request private material, rank sources, rank evidence, create model behavior,
authorize publication, or provide clinical guidance.

## Use Boundary

- Research-use only.
- Public sources only.
- Not medical advice.
- Not diagnostic guidance.
- Not prognosis guidance.
- Not treatment advice.
- Not trial advice.
- Not eligibility guidance.
- Not expanded-access guidance.
- Not monitoring guidance.
- Not publication authorization.
- Not a claim that multiple myeloma has been cured.
- Draft order follows the task queue, not clinical priority, source quality,
  biological importance, therapeutic relevance, or patient relevance.

## Source Artifacts

- [Machine Representation Source-Gap Task Queue v0](../machine-representation-source-gap-task-queue-v0.md)
- [Machine Representation Source Extraction v0](../../machine-representation-source-extraction-v0.md)
- [Myeloma Machine Representation Stack v0](../../machine-representation-stack-v0.md)
- [Myeloma State Validator Rule Map v0](../../myeloma-state-validator-rule-map-v0.md)
- [Model Output Boundary Wrapper v0](../../model-output-boundary-wrapper-v0.md)
- [Evidence Retrieval Packet v0](../../evidence-retrieval-packet-v0.md)
- [Source Registry v0](../../../../sources/source-registry-v0.md)
- [Public Safety](../../../../governance/PUBLIC_SAFETY.md)

## Draft Packet Rules

| Rule | Required Shape | Refusal Boundary |
| --- | --- | --- |
| Human review first | Every draft is text for review, not an opened issue. | Do not call GitHub APIs, send outreach, tag reviewers, or publish. |
| Public sources only | Use public source IDs, artifact IDs, public metadata, and source-context-needed labels. | Do not request patient records, private correspondence, unpublished sponsor material, or restricted data. |
| Source-scoped ask | Ask for source-stated fields, limitations, methods, and uncertainty. | Do not ask contributors to infer absence, actionability, clinical importance, or patient relevance. |
| Blocked outputs preserved | Each draft carries blocked uses from the task queue. | A completed extraction cannot enable advice, matching, ranking, prediction, or publication authorization. |
| Missingness visible | Unknown, not tested, not collected, and source-context-needed remain explicit. | Do not fill missing fields with generated biomedical text. |

## Draft 1. Modality Scope Source Extraction

Suggested title:
`[source extraction]: machine representation modality scope and cohort limits`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-modality-scope-source-extraction-task-v0`

Linked source-extraction rows:
`mse_00`, `mse_01`, `mse_02`

Public source anchors:

- `nature_genetics_commpass_subtypes_2024`
- `machine-representation-source-extraction-v0`
- `myeloma-state-object-schema-v0`
- `source-registry-v0`

Draft body:

Extract public, source-stated context for the modality families used by the
myeloma state object and machine-representation stack. Focus on cohort scope,
longitudinal follow-up limits, source-defined feature families, and what
modalities are explicitly present, absent, not tested, or not collected in the
public source.

Allowed inputs:

- public source IDs
- public artifact IDs
- public metadata
- source-stated methods, cohort descriptors, and limitation text

Blocked outputs:

- prognosis
- treatment advice
- trial advice
- monitoring advice
- patient matching
- source ranking
- evidence ranking
- model validation
- clinical utility claims

Done criteria:

- modality coverage is source-scoped
- cohort and follow-up limits are attached
- missing modalities use `unknown`, `not_tested`, or `not_collected`
- a no-add reason is recorded if the public source does not support a field
- no real case data or patient-like examples are introduced

No-advice copy:
This issue asks for public source extraction only. It must not be used to infer
patient prognosis, treatment options, trial eligibility, monitoring actions, or
model readiness.

## Draft 2. Immune Atlas Field Source Extraction

Suggested title:
`[source extraction]: immune atlas field families for synthetic state objects`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-immune-atlas-field-source-extraction-task-v0`

Linked source-extraction rows:
`mse_03`

Public source anchors:

- `nature_cancer_immune_atlas_myeloma_2026`
- `synthetic-myeloma-state-fixture-v0`
- `myeloma-state-validator-rule-map-v0`
- `source-registry-v0`

Draft body:

Extract public immune-atlas field families that can be referenced by
synthetic-only myeloma state objects. Preserve source-stated method context,
cell-state or ecosystem vocabulary, missingness labels, sample context, and
limitations. Keep immune state descriptors separate from patient-specific
fitness, prognosis, treatment fit, or trial fit.

Allowed inputs:

- public immune-atlas source IDs
- public artifact IDs
- source-stated method and limitation text
- public metadata

Blocked outputs:

- immune-status advice
- prognosis
- treatment fit
- trial fit
- eligibility guidance
- monitoring guidance
- model features for real cases

Done criteria:

- field families are source-scoped
- method context and limitations remain attached
- missingness is explicit
- synthetic-only reuse is stated
- no patient-specific interpretation appears

No-advice copy:
This issue asks for public field-family extraction only. It does not support
immune profiling advice, therapy selection, trial selection, monitoring
guidance, or patient-specific model input.

## Draft 3. Clinical And Context Crosswalk Source Extraction

Suggested title:
`[source extraction]: clinical and context labels for machine-state crosswalks`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-context-crosswalk-source-task-v0`

Linked source-extraction rows:
`mse_04`, `mse_07`

Public source anchors:

- `nci_pdq_myeloma_hp`
- `jco_ims_imwg_high_risk_consensus_2025`
- `pubmed_high_risk_genomic_consensus_validation_2026`
- `nature_genetics_mm_precursor_genomic_landscape_2025`
- `molecular-immune-context-contract-v0`
- `high-risk-organ-frailty-context-modifier-map-v0`

Draft body:

Crosswalk source-defined clinical, high-risk, organ, frailty, and precursor
labels to public context contracts for machine-state review. Preserve source
scope, disease-state definitions, uncertainty, and limitations. Use context
labels only as public research descriptors, not as calculators or patient
stratification tools.

Allowed inputs:

- public source IDs
- public context-contract artifacts
- source-stated definitions and limitations
- public metadata

Blocked outputs:

- diagnosis
- prognosis
- eligibility guidance
- screening advice
- personal risk advice
- treatment guidance
- trial guidance
- ranking or calculator fields

Done criteria:

- each label is source-scoped
- missing definitions remain `source_context_needed`
- no calculator, score, urgency, or action field is introduced
- precursor and high-risk language stays non-directive
- no real case facts are included

No-advice copy:
This issue asks for public terminology crosswalk work only. It does not support
diagnosis, prognosis, personal risk assessment, screening decisions, treatment
selection, trial selection, or urgency guidance.

## Draft 4. Therapy Exposure Vocabulary Source Gap

Suggested title:
`[source extraction]: therapy exposure vocabulary for non-advisory state timelines`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-therapy-exposure-source-gap-task-v0`

Linked source-extraction rows:
`mse_05`

Public source anchors:

- `therapy-exposure-timeline-contract-v0`
- `multiple-myeloma-treatment-class-taxonomy-v0`
- `immune-therapy-sequencing-access-boundary-v0`
- `source-registry-v0`

Draft body:

Identify public source IDs or record a no-add reason for therapy-exposure
vocabulary used in non-advisory synthetic state timelines. Focus on
source-stated therapy class labels, exposure timing vocabulary, response
linkage fields, refractory-context language, toxicity or constraint context
when source-stated, and limitations.

Allowed inputs:

- public source IDs
- public taxonomy and timeline artifacts
- source-stated vocabulary and limitations
- no-add reasons when source context is insufficient

Blocked outputs:

- therapy sequencing
- eligibility guidance
- availability guidance
- access guidance
- treatment advice
- trial advice
- product comparison
- therapy ranking

Done criteria:

- proposed source IDs are public and citable
- source gaps remain visible when unresolved
- timeline language stays descriptive and non-directive
- therapy classes are not ranked or compared
- no patient-specific exposure path is described

No-advice copy:
This issue asks for public vocabulary support only. It does not support therapy
selection, sequencing, access decisions, eligibility decisions, trial matching,
or product comparison.

## Draft 5. Endpoint Field Source Extraction

Suggested title:
`[source extraction]: endpoint field context for machine-state measurement timelines`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-endpoint-field-source-task-v0`

Linked source-extraction rows:
`mse_06`

Public source anchors:

- `fda_mrd_cr_endpoint_guidance_2026`
- `measurement-normalization-contract-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `mrd-endpoint-language-guardrail-addendum-v0`

Draft body:

Extract source-scoped endpoint field context for synthetic measurement
timelines. Preserve method, threshold, sample or specimen, timepoint,
durability, endpoint role, disease state, denominator context when available,
and source limitations. Keep MRD and response language separate from cure
claims and patient-specific prognosis.

Allowed inputs:

- public endpoint and MRD source IDs
- public measurement artifacts
- source-stated endpoint definitions and limitations
- public metadata

Blocked outputs:

- cure claims
- endpoint interpretation for a patient
- prognosis
- monitoring guidance
- treatment guidance
- trial guidance
- endpoint ranking

Done criteria:

- endpoint fields remain source-scoped
- draft or nonbinding source status is preserved where applicable
- missing endpoint context remains visible
- no endpoint is converted into a yes/no success or cure field
- `make validate` passes if structured artifacts are changed

No-advice copy:
This issue asks for public endpoint field extraction only. It does not support
MRD interpretation, treatment decisions, monitoring actions, trial decisions,
prognosis, or cure claims.

## Draft 6. Relapse And Resistance Scope Extraction

Suggested title:
`[source extraction]: relapse and resistance feature families for machine-state context`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-relapse-resistance-scope-task-v0`

Linked source-extraction rows:
`mse_08`

Public source anchors:

- `nature_communications_rrmm_resistance_2022`
- `post-bcma-resistance-frontier-addendum-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `source-registry-v0`

Draft body:

Extract cohort-level relapse and resistance feature families that can be used
as public mechanism context for synthetic machine-state artifacts. Preserve
source scope, sample context, mechanism vocabulary, measurement limitations,
and unresolved gaps. Keep feature families separate from diagnosis,
actionability, treatment selection, or mechanism ranking.

Allowed inputs:

- public source IDs
- public mechanism artifacts
- source-stated mechanism and measurement context
- public limitation text

Blocked outputs:

- resistance diagnosis
- treatment ranking
- trial matching
- mechanism ranking
- actionability claims
- patient-specific interpretation

Done criteria:

- feature families are cohort-level and source-scoped
- antigen and non-antigen mechanisms are not ranked
- unresolved gaps map to public mechanism task surfaces
- no clinical action language is introduced
- no real case data appears

No-advice copy:
This issue asks for public mechanism-context extraction only. It does not
support resistance diagnosis, treatment selection, trial matching, mechanism
ranking, or actionability claims.

## Draft 7. Fusion And Validation Method Source Gap

Suggested title:
`[source extraction]: public method sources for fusion and validation boundaries`

Suggested issue form:
`.github/ISSUE_TEMPLATE/source-extraction-task.yml`

Task ID:
`mr-fusion-validation-method-source-gap-task-v0`

Linked source-extraction rows:
`mse_09`, `mse_11`

Public source anchors:

- `machine-representation-stack-v0`
- `myeloma-state-validator-rule-map-v0`
- `source-registry-v0`

Draft body:

Find public method or governance source IDs for multimodal fusion boundaries
and validation standards, or record `source_context_needed` with a no-add
reason. Focus on source-stated method categories, validation split concepts,
missing-modality robustness, calibration review, dataset-shift warnings,
subgroup review, and limitations. Do not implement or compare models.

Allowed inputs:

- public method or governance sources
- public artifact IDs
- source-stated limitations
- expert-review-needed labels when source context is insufficient

Blocked outputs:

- model implementation
- model comparison
- scoring
- prediction
- clinical deployment
- clinical utility claims
- benchmark claims

Done criteria:

- public method sources are identified or source gaps remain explicit
- validation concepts stay governance-level and non-executable
- no performance, calibration, or utility claim is made
- no model code or training instruction is introduced
- expert-review-needed labels remain visible

No-advice copy:
This issue asks for public method-source context only. It does not support
model implementation, benchmarking, prediction, clinical deployment, or claims
of clinical utility.

## Draft 8. Output Wrapper Expert-Review Questions

Suggested title:
`[expert review]: model-output wrapper refusals and blocked-use labels`

Suggested issue form:
`.github/ISSUE_TEMPLATE/expert-review-task.yml`

Task ID:
`mr-output-wrapper-review-question-task-v0`

Linked source-extraction rows:
`mse_10`, `mse_12`

Public source anchors:

- `model-output-boundary-wrapper-v0`
- `myeloma-state-validator-rule-map-v0`
- `machine-representation-source-extraction-v0`
- `case-to-cure-pipeline-blueprint-v0`
- `case-to-public-learning-extraction-gate-v0`

Draft body:

Review whether the public model-output wrapper uses sufficiently clear refusal
states, blocked-use labels, uncertainty language, and case-to-cure linkage for
research-only machine-state artifacts. The review should focus on public
wording, artifact boundaries, and fail-closed routing. It must not request real
cases, clinical judgment, model outputs, predictions, treatment advice, trial
advice, or publication authorization.

Allowed inputs:

- public artifact IDs
- public wording suggestions
- public source IDs where relevant
- expert-review-needed disposition labels

Blocked outputs:

- progression-risk output
- response probability
- MRD interpretation
- resistance attribution
- recommendation
- ranking
- clinical decision
- publication authorization

Done criteria:

- review questions map to public artifacts and source-extraction rows
- suggested wording strengthens or preserves refusal boundaries
- missing review remains `expert_review_needed`
- no private correspondence is copied
- no reviewer is named unless already present in public source context

No-advice copy:
This issue asks for public boundary review only. It does not support model
output generation, patient-specific prediction, treatment guidance, trial
guidance, monitoring guidance, clinical decisions, or publication approval.

## What This Step Revealed

The task queue is mature enough for issue-facing draft text, but the safe
handoff is still human-reviewed and non-submitting. The implementation
completion audit is now complete, because the phase success criteria are
represented by schema, synthetic fixture, output wrapper, validator rule map,
source extraction, task queue, issue draft packet, and audit artifacts.

## Handoff State

`machine-representation-source-gap-issue-draft-packet-v0` is complete as a
human-reviewable issue draft packet.

ORP should mark this item complete and activate
`machine-representation-public-scope-human-gate-blocker-v0` until a human
selects a new named public-safe phase or clears a named gate.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, sequencing records, portal exports, accessions, private
  paths, free-text case details, private correspondence, or re-identification
  keys.
- No public intake form, upload path, backend, account workflow, database,
  model weights, scoring code, prediction API, executable normalizer, or
  executable validator.
- No source ranking, evidence ranking, patient matching, trial matching, target
  ranking, mechanism ranking, option ranking, diagnosis, prognosis,
  progression-risk output, response-probability output, MRD interpretation,
  resistance call, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decision.
- No autonomous outreach, issue creation, publication, pull request, commit, or
  push.
- No cure or vaccine claim.

## Limitations

- This is draft issue text, not opened GitHub issues.
- This does not send outreach, tag reviewers, request private responses, or
  create an expert-validation event.
- This does not complete source extraction, source registry updates, artifact
  updates, expert review, publication review, or clinical review.
- This does not rank tasks, sources, evidence, mechanisms, therapies, trials,
  candidate options, patient states, or contributor priorities.
- This does not prove source completeness, clinical validity, model validity,
  calibration, generalizability, or clinical utility.
- This does not implement model code, validation code, data processing,
  normalization, scoring, training, inference, calibration, benchmarking, or
  deployment.
- This does not authorize real case intake, private-lab access, publication,
  clinical interpretation, clinical use, legal approval, regulatory readiness,
  sponsor decisions, institutional decisions, or treating-team decisions.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decisions.
- This does not claim that multiple myeloma has been cured or that a vaccine
  has been found.
