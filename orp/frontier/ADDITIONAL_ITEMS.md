# Additional Frontier Items: Curing Blood Cancer

- active_list_id: `post-machine-representation-public-safe-research-substrate-v0`
- active_item_id: `machine-representation-expert-validation-execution-v0`

## `case-intake-frontends` Human-Friendly Case Intake Front Ends (`complete`)

- [x] `caregiver-friendly-case-intake-v0` caregiver-friendly case intake front end (`complete`)
  - goal: Design the first public-facing but privacy-preserving case-intake surface so a caregiver can enter a loved one's multiple myeloma details through a simple guided flow, with all real case data routed only to a private, consented, access-controlled system and with no medical advice or public PHI.

## `case-intake-frontier-v0` Caregiver Case Intake Frontier v0 (`complete`)

- [x] `case-intake-next-public-build-slice-v0` Next public-safe caregiver intake build slice (`complete`)
  - goal: Extend the Caregiver Case Intake Product Spec v0 into one concrete public-safe next artifact: private-intake schema contract, public-safe projection validator, no-PHI/no-advice checklist, synthetic fixture expansion, or static synthetic prototype plan.

## `case-to-cure-master-backlog-v0` Case-To-Cure Adaptive Master Backlog v0 (`complete`)

- [x] `case-to-cure-loop-governor-v0` Case-to-cure loop governor (`complete`)
  - goal: Make the loop itself enforce next-step synthesis after each completed public-safe step.
- [x] `private-intake-schema-contract-v0` Private intake schema contract (`complete`)
  - goal: Define the private-only intake record shape and public-safe projection boundary for future consented multiple myeloma case work.
- [x] `static-synthetic-caregiver-prototype-v0` Static synthetic caregiver prototype (`complete`)
  - goal: Design the first synthetic-only public prototype plan for a caregiver-centered intake flow that never accepts real case details.
- [x] `public-projection-validator-v0` Public projection validator (`complete`)
  - goal: Create a fail-closed public projection validator or validator spec for no-PHI, no-advice, synthetic-only public exports.
- [x] `consent-privacy-security-retention-gate-v0` Consent privacy security retention gate (`complete`)
  - goal: Specify the human and technical gates before any real case intake, storage, retention, emergency handling, or clinician review.
- [x] `case-feature-normalization-contract-v0` Case feature normalization contract (`complete`)
  - goal: Define the public-safe shape for normalized disease-state and context features used by the private case-to-cure pipeline.
- [x] `measurement-normalization-contract-v0` Measurement normalization contract (`complete`)
  - goal: Define public-safe MRD, response, relapse, lab, imaging, method, threshold, sample, and timepoint normalization for private case work.
- [x] `therapy-exposure-timeline-contract-v0` Therapy exposure timeline contract (`complete`)
  - goal: Define the private timeline shape for prior therapies, lines, exposures, responses, toxicities, constraints, and refractory context.
- [x] `molecular-immune-context-contract-v0` Molecular immune context contract (`complete`)
  - goal: Define the private/public boundary for cytogenetics, genomics, target assays, pathology, flow, immune context, and source validity fields.
- [x] `evidence-retrieval-packet-v0` Evidence retrieval packet (`complete`)
  - goal: Define a reproducible public-source evidence packet skeleton for future private case questions without patient matching.
- [x] `trial-therapy-landscape-non-advice-gate-v0` Trial therapy landscape non-advice gate (`complete`)
  - goal: Define how trial, therapy, product, target, and access context can be extracted as landscape information without advice.
- [x] `candidate-hypothesis-review-question-set-v0` Candidate hypothesis review question set (`complete`)
  - goal: Represent candidate hypotheses as review questions for qualified humans, not recommendations or rankings.
- [x] `multidisciplinary-review-packet-builder-v0` Multidisciplinary review packet builder (`complete`)
  - goal: Define the public-safe packet builder skeleton and route rules for multidisciplinary review under private and clinical gates.
- [x] `expert-validation-loop-v0` Expert validation loop (`complete`)
  - goal: Make expert validation issue updates and response dispositions part of the recurring public loop.
- [x] `case-to-public-learning-extraction-gate-v0` Case-to-public learning extraction gate (`complete`)
  - goal: Define the sanitation, aggregation, source-scope, uncertainty, privacy, review, and publication gate for any future public learning extracted from a private case.
- [x] `end-to-end-synthetic-case-dry-run-v0` End-to-end synthetic case dry run (`complete`)
  - goal: Dry-run the complete case-to-cure path with synthetic-only artifacts from caregiver intake through publication gate.
- [x] `case-to-cure-master-completion-audit-v0` Case-to-cure master completion audit (`complete`)
  - goal: Audit whether the adaptive master plan is complete, safely blocked, or ready for a new named phase.
- [ ] `case-to-cure-public-scope-human-gate-blocker-v0` Case-to-cure public-scope human gate blocker (`blocked`)
  - goal: Record that no autonomous public-safe case-to-cure backlog item remains after the master completion audit.

## `public-caregiver-intake-frontend-v0` Public Caregiver Intake Frontend v0 (`complete`)

- [x] `static-synthetic-caregiver-intake-frontend-v0` Static synthetic caregiver intake frontend (`complete`)
  - goal: Build the first static, synthetic-only public caregiver intake frontend prototype for multiple myeloma case organization, using existing public artifacts as boundaries and refusing real patient data.
- [x] `static-synthetic-caregiver-intake-frontend-smoke-test-v0` Static synthetic caregiver intake frontend smoke test (`complete`)
  - goal: Document public-safety smoke checks for the static synthetic caregiver intake frontend so the prototype is auditable before any future UI iteration.

## `myeloma-machine-representation-implementation-v0` Myeloma Machine Representation Implementation v0 (`complete`)

- [x] `myeloma-state-object-schema-v0` Myeloma state object schema (`complete`)
  - goal: Define the first public, synthetic-only myeloma disease-state object schema derived from the machine representation stack.
- [x] `synthetic-myeloma-state-fixture-v0` Synthetic myeloma state fixture (`complete`)
  - goal: Create synthetic-only myeloma state object fixtures that exercise the schema across complete multimodal, missing RNA, missing single-cell, and private-source-blocked scenarios.
- [x] `model-output-boundary-wrapper-v0` Model output boundary wrapper (`complete`)
  - goal: Define reusable public-safe refusal and uncertainty rules for progression, response, MRD, and resistance head placeholders before any model-facing output work.
- [x] `myeloma-state-validator-rule-map-v0` Myeloma state validator rule map (`complete`)
  - goal: Define no-code validator rules for myeloma state objects, synthetic fixtures, and model-output boundary wrapper fields without validating real cases or creating prediction behavior.
- [x] `machine-representation-source-extraction-v0` Machine representation source extraction (`complete`)
  - goal: Map myeloma machine-representation architecture claims to public source IDs, source-context gaps, extraction status, uncertainty, and expert-review needs without model code, predictions, advice, matching, or ranking.
- [x] `machine-representation-source-gap-task-queue-v0` Machine representation source-gap task queue (`complete`)
  - goal: Turn machine-representation source-context gaps and contribution task seeds into a public task queue without model code, predictions, advice, matching, ranking, clinical interpretation, outreach, or publication decisions.
- [x] `machine-representation-source-gap-issue-draft-packet-v0` Machine representation source-gap issue draft packet (`complete`)
  - goal: Prepare reusable public issue draft text for machine-representation source-gap tasks without opening issues, sending outreach, requesting private material, creating model code, predictions, advice, matching, ranking, or clinical interpretation.
- [x] `machine-representation-implementation-completion-audit-v0` Machine representation implementation completion audit (`complete`)
  - goal: Audit whether the human-selected machine-representation implementation phase is complete or whether another public-safe adjacent item remains, without opening issues, sending outreach, requesting private material, validating real cases, producing model outputs, advice, matching, ranking, or publication authorization.
- [ ] `machine-representation-public-scope-human-gate-blocker-v0` Machine representation public-scope human gate blocker (`blocked`)
  - goal: Record that no autonomous public-safe machine-representation implementation item remains after the completion audit.

## `post-machine-representation-public-safe-research-substrate-v0` Post-Machine-Representation Public-Safe Research Substrate v0 (`active`)

- [x] `mrd-resistance-geometry-falsification-v0` MRD Resistance Geometry Falsification v0 (`complete`)
  - goal: Record the human-selected public-safe MRD resistance geometry falsification lane after the machine-representation human gate, without clearing that gate or creating clinical claims.
- [x] `orp-clawdad-phase-6-control-plane-reconciliation-v0` ORP/Clawdad Phase 6 Control-Plane Reconciliation v0 (`complete`)
  - goal: Reconcile ORP and Clawdad state after the human-selected MRD geometry falsification phase so the machine-representation human gate is not silently treated as cleared.
- [ ] `machine-representation-expert-validation-execution-v0` Machine Representation Expert Validation Execution v0 (`blocked`)
  - goal: Resume the machine-representation expert-validation lane by opening or tracking public-safe source-gap review issues only after human authorization, while keeping external outreach and expert-review gates explicit.
