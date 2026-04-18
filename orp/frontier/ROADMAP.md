# Roadmap: Case-To-Cure Adaptive Master Plan v0

- active_version: `v2`
- active_milestone: `case-to-cure-adaptive-master-plan-v0`
- band: `exact`
- next_action: `Run static-synthetic-caregiver-intake-frontend-smoke-test-v0: document public-safety smoke checks for the static frontend, including no submit path, no storage, no uploads, no backend calls, responsive layout, refusal copy, and no-advice boundaries.`

## Phases

- [x] **Phase case-to-cure-loop-governor-v0: Case-To-Cure Loop Governor v0** - Make the public multiple myeloma case-to-cure plan durable and adaptive: each completed step must inspect its outcome, synthesize the next safest public step, and queue or block that step explicitly.
- [x] **Phase private-intake-schema-contract-v0: Private Intake Schema Contract v0** - Define the private-only intake record shape and public-safe projection boundary for future consented multiple myeloma case work.
- [x] **Phase static-synthetic-caregiver-prototype-v0: Static Synthetic Caregiver Prototype v0** - Design the first synthetic-only public prototype plan for a caregiver-centered intake flow that never accepts real case details.
- [x] **Phase public-projection-validator-v0: Public Projection Validator v0** - Create a fail-closed public projection validator or validator spec for no-PHI, no-advice, synthetic-only public exports.
- [x] **Phase consent-privacy-security-retention-gate-v0: Consent Privacy Security Retention Gate v0** - Specify the human and technical gates before any real case intake, storage, retention, emergency handling, or clinician review.
- [x] **Phase case-feature-normalization-contract-v0: Case Feature Normalization Contract v0** - Define the public-safe shape for normalized disease-state and context features used by the private case-to-cure pipeline.
- [x] **Phase measurement-normalization-contract-v0: Measurement Normalization Contract v0** - Define public-safe MRD, response, relapse, lab, imaging, method, threshold, sample, and timepoint normalization for private case work.
- [x] **Phase therapy-exposure-timeline-contract-v0: Therapy Exposure Timeline Contract v0** - Define the private timeline shape for prior therapies, lines, exposures, responses, toxicities, constraints, and refractory context.
- [x] **Phase molecular-immune-context-contract-v0: Molecular Immune Context Contract v0** - Define the private/public boundary for cytogenetics, genomics, target assays, pathology, flow, immune context, and source validity fields.
- [x] **Phase evidence-retrieval-packet-v0: Evidence Retrieval Packet v0** - Define a reproducible public-source evidence packet skeleton for future private case questions without patient matching.
- [x] **Phase trial-therapy-landscape-non-advice-gate-v0: Trial Therapy Landscape Non-Advice Gate v0** - Define how trial, therapy, product, target, and access context can be extracted as landscape information without advice.
- [x] **Phase candidate-hypothesis-review-question-set-v0: Candidate Hypothesis Review Question Set v0** - Represent candidate hypotheses as source-scoped review questions for qualified humans, not recommendations, rankings, or patient-action outputs.
- [x] **Phase multidisciplinary-review-packet-builder-v0: Multidisciplinary Review Packet Builder v0** - Define the public-safe packet builder skeleton and route rules for multidisciplinary review under private and clinical gates.
- [x] **Phase expert-validation-loop-v0: Expert Validation Loop v0** - Make expert validation issue updates and response dispositions part of the recurring public loop without private correspondence or clinical decisions.
- [x] **Phase case-to-public-learning-extraction-gate-v0: Case-To-Public Learning Extraction Gate v0** - Define the sanitation, aggregation, source-scope, uncertainty, privacy, review, and publication gate for any future public learning extracted from a private case.
- [x] **Phase end-to-end-synthetic-case-dry-run-v0: End-To-End Synthetic Case Dry Run v0** - Dry-run the complete case-to-cure path with synthetic-only artifacts from caregiver intake through publication gate.
- [x] **Phase case-to-cure-master-completion-audit-v0: Case-To-Cure Master Completion Audit v0** - Audit whether the adaptive master plan is complete, safely blocked, or ready for a new named phase.
- [ ] **Phase case-to-cure-public-scope-human-gate-blocker-v0: Case-To-Cure Public-Scope Human Gate Blocker v0** - Block further autonomous case-to-cure work until a human selects a new named public-safe phase or clears a named gate.
- [ ] **Phase public-caregiver-intake-frontend-v0: Public Caregiver Intake Frontend v0** - Maintain the public-facing, static, synthetic-only caregiver intake frontend prototype and verify it stays non-collecting, non-advisory, and public-safe.
