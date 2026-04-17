# Additional Frontier Items: Curing Blood Cancer

- active_list_id: `public-caregiver-intake-frontend-v0`
- active_item_id: `static-synthetic-caregiver-intake-frontend-v0`

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

## `public-caregiver-intake-frontend-v0` Public Caregiver Intake Frontend v0 (`active`)

- [ ] `static-synthetic-caregiver-intake-frontend-v0` Static synthetic caregiver intake frontend (`active`)
  - goal: Build the first static, synthetic-only public caregiver intake frontend prototype for multiple myeloma case organization, using existing public artifacts as boundaries and refusing real patient data.
