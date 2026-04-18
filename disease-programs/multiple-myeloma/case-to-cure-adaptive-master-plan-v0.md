# Case-To-Cure Adaptive Master Plan v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- plan status: `active-master-plan-v0`
- claim level: `open-question`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only, not medical advice

## Purpose

This is the canonical public operating plan for the Curing Blood Cancer
multiple myeloma initiative.

The north star is to build the public and private tooling needed to work toward
a cure for multiple myeloma, including eventual support for a particular
consented case. This plan does not claim that multiple myeloma has been cured.
It defines how the project should keep moving from one completed public-safe
step to the next without pretending that every future step can be known in
advance.

## Public Boundary

This public repo may define methods, schemas, validators, synthetic examples,
roadmaps, gates, public issue requests, and source-backed maps.

This public repo must not contain:

- patient-identifying data
- real case data
- raw records, images, notes, dates tied to a person, or re-identification keys
- private lab records, credentials, restricted datasets, or unreviewed exports
- diagnosis, prognosis, treatment advice, trial advice, monitoring advice,
  expanded-access advice, urgency guidance, or patient-specific ranking
- unsupported cure, vaccine, treatment-path, or clinical-outcome claims

Real case work belongs in the governed private lab with consent, privacy,
clinical, legal, regulatory, and publication gates.

## Operating Hierarchy

The initiative should always be organized in this order:

1. North star: cure multiple myeloma by building a transparent, source-backed,
   reviewable research system that can eventually support real consented cases.
2. Master pillars: caregiver intake, private case workspace, public-safe
   projection, normalization, evidence retrieval, therapy and trial landscape
   context, candidate hypothesis review, multidisciplinary review, expert
   validation, and public learning extraction.
3. Milestones: named chunks of work that have a public artifact, validator,
   blocker, or handoff target.
4. Subplans: focused plans inside a milestone. A subplan may have one step or
   many steps, and it may be expanded only when the prior step reveals what is
   actually needed next.
5. Steps: the smallest useful artifact, validator, fixture, schema, map, issue,
   or handoff that can be completed and validated in one pass.
6. Completion handoffs: every step ends by naming what changed, what is still
   blocked, and the next safest step.

The project should not try to pre-create hundreds or thousands of future steps.
It should pre-create the durable process that generates the next step from the
result of the step that just completed.

## Required Loop

Every autonomous or human-assisted pass must follow this loop:

1. Inspect the current ORP live frontier, additional queued items, repo status,
   validation state, and relevant canonical artifacts.
2. Select exactly one public-safe step that can be completed in the pass.
3. State why that step is the best next move under the north star.
4. Make the smallest useful edit set.
5. Update metadata, catalog coverage, navigation links, and safety boundaries
   as needed.
6. Run validation after artifact, metadata, schema, validator, or catalog
   changes.
7. Write or update a handoff that records the outcome.
8. Synthesize the next step from the outcome before stopping.
9. Queue that next step in ORP unless it is blocked by a hard boundary.
10. If blocked, record the blocker and the human gate needed to unblock it.

There is no valid "done" state for the master plan unless the master plan's
completion audit has been reached and all remaining work is explicitly marked
as expert-review-needed, private-lab-needed, clinical-team-needed,
regulatory-needed, publication-gate-needed, or out-of-scope.

## Next-Step Synthesis

After each completed step, choose the next step using this decision ladder:

1. Fix validation, metadata, catalog, link, or public-safety failures created by
   the step just completed.
2. Complete the next direct dependency for the same subplan if it is now
   obvious and public-safe.
3. If the completed step revealed a missing schema, validator, fixture, gate,
   or source extraction need, add that as the next subplan step.
4. If the subplan is complete, write a subplan handoff and move to the next
   highest-value unblocked master pillar.
5. If the next needed work requires real case data, clinical interpretation,
   outreach, private lab access, publication approval, or a legal/regulatory
   decision, record the blocker and choose the next public-safe adjacent step.
6. If no safe public step remains in the current milestone, open a new named
   milestone or mark the master plan blocked with the exact human gate.

The completion handoff should always answer:

- What was completed?
- What changed in the public artifact surface?
- What evidence, source, or review context supports it?
- What remains uncertain?
- What use is explicitly blocked?
- What did the completed step reveal that was not known before?
- What is the next safest public step?
- What private, expert, clinical, legal, regulatory, or publication gate is
  waiting outside the public repo?

## Master Pillars

### 1. Caregiver Intake

Goal:

Make it easy for a caregiver-like caregiver to organize a future consented case
without putting real case data in public or receiving medical advice from the
public interface.

Current public anchors:

- [Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md)
- [Caregiver Intake Public Projection Checklist v0](case-intake/caregiver-intake-public-projection-checklist-v0.md)
- [Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md)
- [Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md)
- [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md)
- [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md)
- [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
- [Synthetic Caregiver Intake v0](../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json)

Next subplan shape:

- private intake schema contract
- static synthetic prototype plan
- public projection validator
- consent, privacy, security, retention, emergency, and clinician-review gates
- case-feature normalization contract

### 2. Private Case Workspace Boundary

Goal:

Define what the private lab needs before a real case can be processed without
leaking private material into public artifacts.

Next subplan shape:

- private workspace manifest contract
- role and consent checklist
- data minimization and retention rules
- private-to-public projection boundary
- blocker register updates

### 3. Public-Safe Projection

Goal:

Build a public projection layer that allows only schema shape, synthetic data,
aggregate learning, and approved sanitized artifacts to leave the private lab.

Next subplan shape:

- executable projection validator
- no-PHI and no-advice checks
- public export refusal reasons
- synthetic success, omit, refuse, and blocker fixtures
- publication-gate hook

### 4. Case Normalization

Goal:

Normalize disease state, measurement context, molecular and immune context,
therapy exposure, and constraints without making patient-specific claims in
public.

Next subplan shape:

- case-feature normalization contract, completed by
  [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
- measurement normalization contract, completed by
  [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md)
- therapy exposure timeline contract, completed by
  [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md)
- molecular and immune context contract, completed by
  [Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md)
- machine-facing disease-state representation architecture, started by
  [Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
- unknown, not-tested, not-sure, and source-missing states

### 5. Evidence Retrieval

Goal:

Turn normalized public-safe questions into reproducible public-source evidence
packets, never patient matching.

Next subplan shape:

- evidence retrieval packet skeleton, completed by
  [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md)
- source freshness rules
- query-record provenance
- source limitation ledger
- no-completeness and no-advice boundaries

### 6. Therapy And Trial Landscape Context

Goal:

Map therapies, trials, targets, and access context as public research
landscape, not eligibility or treatment guidance.

Current public anchor:

- [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md)
- [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
- [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

Next subplan shape:

- non-advisory therapy landscape records
- trial query and date-stamp fields
- access-boundary refusal language
- product, target, and mechanism crosswalks
- explicit no-ranking gates

### 7. Candidate Hypothesis Review

Goal:

Represent possible research or clinical-review hypotheses as questions for
qualified humans, not recommendations.

Current public anchor:

- [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
- [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

Next subplan shape:

- candidate hypothesis question set, completed by
  [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
- no-ranking review rubric
- uncertainty and source-limitation fields
- expert-review-needed labels
- hard refusal for patient action outputs

### 8. Multidisciplinary Review Packet

Goal:

Prepare structured review packets that route relevant public artifacts and
private case summaries to qualified reviewers inside the proper private and
clinical gates.

Current public anchor:

- [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

Next subplan shape:

- packet builder route-rule skeleton, completed by
  [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- packet builder manifest
- route-table validator
- reviewer lens map
- clinician-owner gate
- tumor-board or equivalent review boundary

### 9. Expert Validation

Goal:

Use public issues and expert outreach to pressure-test language, claim scope,
source interpretation, and safety boundaries.

Current public anchor:

- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

Next subplan shape:

- public expert validation issue updates
- response disposition ledger
- source-backed correction tasks
- reviewer-lens gap map
- public-safe citation and attribution rules

### 10. Public Learning Extraction

Goal:

Convert only approved, sanitized, non-identifying, non-advisory learning back
into public artifacts after human publication review.

Current public anchor:

- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

Next subplan shape:

- publication and sanitation gate, completed by
  [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- allowed output type and public-source linkage fields
- de-identification and aggregation check
- limitations and uncertainty update
- no single-case claim rule

### 11. End-To-End Synthetic Dry Run

Goal:

Exercise the whole case-to-cure pipeline with synthetic-only fixtures before
any real case appears in the public work.

Next subplan shape:

- synthetic caregiver intake fixture, completed by
  [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)
- synthetic private manifest shape
- synthetic projection record
- synthetic evidence retrieval packet
- synthetic review packet route
- synthetic blocker and refusal paths
- validation report

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

### 12. Cure-Oriented Completion Audit

Goal:

Audit what is complete, what is blocked, what requires expert review, and what
would be needed before the system could responsibly support a real consented
case.

Next subplan shape:

- master backlog completion audit, completed by
  [Case-To-Cure Master Completion Audit v0](case-to-cure-master-completion-audit-v0.md)
- unresolved blocker map
- expert-review gap map
- private-lab handoff map
- clinical and regulatory gate map
- public release readiness gate

Next public step: `case-to-cure-public-scope-human-gate-blocker-v0`, unless a
human selects a new named public-safe phase.

## Initial Durable Backlog

These items should seed ORP/Clawdad. They are intentionally larger than one
edit but smaller than the whole initiative. Each item should produce a concrete
artifact, validator, fixture, handoff, or blocker note, then synthesize the next
step.

| ID | Pillar | First Public-Safe Deliverable |
| --- | --- | --- |
| `case-to-cure-loop-governor-v0` | Required loop | ORP/Clawdad loop governor that prevents premature completion and requires next-step synthesis |
| `private-intake-schema-contract-v0` | Caregiver intake | Public contract for private intake schema and private handoff fields |
| `static-synthetic-caregiver-prototype-v0` | Caregiver intake | Static synthetic prototype plan for the caregiver-centered intake flow |
| `public-projection-validator-v0` | Public-safe projection | Executable or protocol-level projection validator for no-PHI and no-advice checks |
| `consent-privacy-security-retention-gate-v0` | Private case workspace | Consent, privacy, security, retention, emergency, and clinician-review gate specification |
| `case-feature-normalization-contract-v0` | Case normalization | Normalized feature bundle contract tied to public-safe projection rules |
| `measurement-normalization-contract-v0` | Case normalization | MRD, response, relapse, lab, imaging, method, threshold, and timepoint normalization contract |
| `therapy-exposure-timeline-contract-v0` | Case normalization | Prior therapy, line, exposure, response, toxicity, and constraint timeline contract |
| `molecular-immune-context-contract-v0` | Case normalization | Cytogenetic, genomic, target-assay, pathology, and immune context contract |
| `myeloma-machine-representation-stack-v0` | Case normalization | Source-backed public architecture for the model-facing myeloma state object, fusion layers, prediction-head boundaries, and validation standards |
| `evidence-retrieval-packet-v0` | Evidence retrieval | Source-backed evidence packet skeleton with freshness and limitation fields |
| `trial-therapy-landscape-non-advice-gate-v0` | Therapy and trial landscape | Non-advisory trial and therapy landscape extraction gate |
| `candidate-hypothesis-review-question-set-v0` | Candidate hypothesis review | Question-only hypothesis packet that cannot rank or recommend patient action |
| `multidisciplinary-review-packet-builder-v0` | Multidisciplinary review | Public-safe review packet builder skeleton and route rules |
| `expert-validation-loop-v0` | Expert validation | Issue-linked expert validation loop with public-safe disposition updates |
| `case-to-public-learning-extraction-gate-v0` | Public learning extraction | Publication and sanitation gate for any public learning extracted from a case |
| `end-to-end-synthetic-case-dry-run-v0` | Synthetic dry run | Full synthetic pipeline dry run from intake to publication gate |
| `case-to-cure-master-completion-audit-v0` | Completion audit | Audit that decides whether the master plan is complete, blocked, or ready for the next named phase |
| `case-to-cure-public-scope-human-gate-blocker-v0` | Human gate blocker | Blocked next state after the master completion audit; no autonomous public-safe case-to-cure item remains without human phase selection or named gate clearance |
| `public-caregiver-intake-frontend-v0` | Public static frontend | Human-selected next phase for a static, synthetic-only caregiver intake prototype that refuses real patient data and does not provide medical advice |
| `static-synthetic-caregiver-intake-frontend-v0` | Public static frontend | Completed no-build HTML/CSS/JS caregiver intake prototype using synthetic fixture content, disabled handoff controls, and no submit, upload, backend, storage, advice, matching, ranking, or patient-specific output |
| `static-synthetic-caregiver-intake-frontend-smoke-test-v0` | Public static frontend | Active smoke-test report item for no-submit, no-storage, no-upload, no-network, responsive layout, refusal copy, emergency boundary, clinician-review boundary, and no-advice checks |

## Clawdad Delegation Rule

Clawdad should not stop merely because one named phase closes. A closed phase
means:

1. read the completion handoff
2. synthesize what the closed phase revealed
3. update ORP with the next public-safe item
4. move to that item unless a hard boundary blocks it

Clawdad may stop only when:

- validation fails and cannot be fixed safely in the pass
- the next required work is hard-blocked by the public boundary
- compute or operator limits require a pause
- the master completion audit says the entire public-safe scope is complete or
  externally blocked

## Source Anchors

- [Multiple Myeloma ORP Frontier Roadmap v0](frontier-roadmap-v0.md)
- [Case-To-Cure Loop Governor Handoff v0](case-to-cure-loop-governor-handoff-v0.md)
- [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
- [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md)
- [Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
- [Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md)
- [Caregiver Intake Public Projection Checklist v0](case-intake/caregiver-intake-public-projection-checklist-v0.md)
- [Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md)
- [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
- [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md)
- [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md)
- [Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md)
- [Static Synthetic Caregiver Intake Frontend v0](case-intake/static-synthetic-caregiver-intake-frontend-v0.html)
- [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md)
- [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)
- [Case-To-Cure Master Completion Audit v0](case-to-cure-master-completion-audit-v0.md)
- [Public Review And Release Gate v0](public-review-release-gate-v0.md)
- [Publication-Gate Checklist v0](publication-gate-checklist-v0.md)
- [Source Registry v0](../../sources/source-registry-v0.md)
- [Private-To-Public Workflow](../../docs/private-to-public-workflow.md)

## Review Boundary

This plan organizes public research operations. It does not provide diagnosis,
prognosis, treatment advice, trial advice, expanded-access advice, monitoring
advice, screening advice, or a claim that a cure or vaccine has been found.
