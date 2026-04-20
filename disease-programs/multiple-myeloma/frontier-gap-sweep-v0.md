# Multiple Myeloma Frontier Gap Sweep v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-frontier-gap-sweep-v0`
- sweep date: `2026-04-20`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only; no real case data, identifiers, raw
  records, uploads, private correspondence, patient-specific predictions,
  recommendations, matching, ranking, or clinical decisions

## Purpose

This sweep checks whether the current public multiple myeloma direction is
still aligned with the cure-oriented north star, what the repo has actually
built, what is blocked, and what obvious frontier gaps should be promoted into
the next public-safe work queue.

It also serves as the first disease-specific test case for a reusable ORP mode:
[ORP Frontier Gap Sweep Mode v0](../../orp/modes/frontier-gap-sweep-mode-v0.md).

## Current Direction

The current direction is not off-base.

The public program has moved from general blood-cancer ambition into a focused
multiple myeloma operating system with:

- caregiver-intake and private/public boundary plumbing
- case-to-cure normalization contracts
- machine-readable myeloma state object scaffolding
- MRD, response, relapse, therapy-exposure, molecular, immune, and context
  boundary artifacts
- a model-output refusal wrapper before any prediction behavior
- MRD resistance geometry coverage, transition, hypothesis, benchmark, and
  falsification artifacts
- expert-validation issue and outreach scaffolding that remains human-gated

The active ORP state is correctly conservative:
`machine-representation-expert-validation-human-authorization-blocker-v0`.
The machine-representation no-outreach prep is complete, and the MRD geometry
falsification lane is complete as public research substrate, but neither one
clears expert review, external outreach, private-lab, clinical, legal,
regulatory, publication, or model-governance gates.

## Direction Drift Found

The sweep found two practical drift points:

| Drift | Status | Fix |
| --- | --- | --- |
| Some navigation text still referenced `machine-representation-expert-validation-execution-v0` as the active item. | Stale wording. | Update navigation to point at `machine-representation-expert-validation-human-authorization-blocker-v0`. |
| A source-gap internal extraction existed but was not fully wired into downstream source-extraction/task-queue/catalog navigation. | Half-landed public artifact. | Preserve it, wire it, and keep validation-green. |

The second drift is useful. It shows the need for a generalized ORP mode that
does not only ask "what task is next?" but also asks "what did the task reveal,
what got half-landed, what source context changed, and what blind spot is now
obvious?"

## External Source Sweep

The high-signal current-source scan suggests the machine representation stack
is directionally right, but the next frontier should add sharper treatment of
modality discordance, spatial disease, blood-based residual disease, and
human-function outcomes.

| Source Anchor | Public Signal | Implication For This Repo |
| --- | --- | --- |
| FDA 2026 draft guidance on MRD and CR endpoints | FDA frames MRD negativity in bone marrow by flow- or sequencing-based methods in patients with complete response as a proposed accelerated-approval endpoint context, while noting the draft is nonbinding. | Keep MRD endpoint language source-specific, draft-status-aware, and separate from cure claims or personal monitoring guidance. |
| Immune Atlas of MM, Nature Cancer 2026 | Single-cell bone marrow immune signatures add outcome-stratification signal when combined with cytogenetics and participant characteristics. | Keep marrow immune state in the machine stack, but preserve cohort, method, missingness, and no-prognosis boundaries. |
| Blood Neoplasia 2025 mass-spectrometry MRD study | Peripheral blood mass spectrometry can complement bone-marrow NGS MRD in cohort-level response assessment. | Add a blood-based residual-disease modality lane instead of treating marrow MRD as the only residual-disease readout. |
| 2026 MRD/PET-CT systematic review and meta-analysis | Bone-marrow MRD and PET-CT are central but discordance and joint prognostic context need explicit handling. | Add a modality-discordance field and imaging-residual-disease gap lane. |
| Spatial transcriptomics of human marrow trephines, Blood 2025 | Spatial architecture of marrow disease can be profiled from biopsy specimens. | Add spatial/marrow-architecture context as a research gap separate from single-cell composition. |
| Multiple myeloma PRO systematic review, 2025 | Patient-reported outcome quality in MM trial protocols and publications is a distinct methodological concern. | Cure-oriented tooling should track function, toxicity, quality of life, and frailty as first-class context, not afterthoughts. |
| Bone marrow microenvironment resistance review, 2025 | Marrow niches are repeatedly implicated in drug-resistance mechanisms. | Keep resistance hypotheses ecosystem-aware, not tumor-cell-only. |

These source anchors are not clinical instructions, treatment comparisons, or
evidence ranks. They are public signals for which repo lanes deserve sharper
source extraction.

## Frontier Blind Spots

| Gap ID | What We Are Underweighting | Why It Matters | Public-Safe Next Move | Hard Boundary |
| --- | --- | --- | --- | --- |
| `fgs_01_modality_discordance` | Discordance among marrow MRD, blood-based residual disease, imaging, and spatial/marrow-biopsy signals. | A patient-state engine that collapses discordant residual-disease modalities into one flag will be brittle. | Completed as `residual-disease-modality-discordance-source-extraction-v0`; next pressure is synthetic refusal fixtures. | No patient MRD interpretation, monitoring advice, imaging advice, or prognosis. |
| `fgs_02_spatial_and_site_state` | Spatial marrow architecture, focal lesions, and extramedullary disease as separate disease-site context. | Single-cell abundance and bulk molecular state can miss site structure and disease outside sampled marrow. | Create a spatial/imaging context map that is explicitly separate from treatment selection. | No diagnostic imaging recommendation, lesion interpretation, staging advice, or urgency guidance. |
| `fgs_03_blood_based_residual_disease` | Peripheral blood residual-disease assays, especially mass spectrometry, as complementary research signals. | Blood-based signals may complement marrow-based MRD but require assay, method, threshold, and endpoint boundaries. | Extend the measurement normalization contract with a blood-based residual-disease candidate field group. | No substitution of blood tests for marrow MRD, no monitoring plan, no response call. |
| `fgs_04_assay_and_specimen_quality` | Sample quality, hemodilution, missingness, failed assays, sensitivity, threshold, timing, and method lineage. | The machine stack needs refusal reasons for bad or incomplete measurement context before it needs better prediction heads. | Completed as `assay-specimen-quality-failure-mode-checklist-v0`, `measurement-state-refusal-fixture-extension-v0`, `measurement-refusal-output-schema-v0`, `measurement-refusal-output-route-table-v0`, and `measurement-refusal-validator-skeleton-v0`; next pressure is `measurement-refusal-negative-safety-fixtures-v0`. | No lab interpretation or test-ordering advice. |
| `fgs_05_human_fitness_and_toxicity` | Frailty, infection risk, toxicity history, neuropathy, renal function, patient-reported outcomes, and ability to sustain therapy. | A "cure" path is not only tumor control; durable benefit depends on host resilience and lived burden. | Create a PRO/toxicity/frailty source-context lane tied to caregiver intake and therapy-exposure contracts. | No fitness-for-treatment, dose, safety, or transplant/CAR-T eligibility guidance. |
| `fgs_06_transportability_and_bias` | External validation, real-world data quality, calendar-time drift, center effects, access bias, and missing-modality bias. | CoMMpass-style molecular richness is powerful but not automatically transportable to every future case or care setting. | Create a model-validation transportability and bias checklist grounded in TRIPOD+AI, PROBAST, GMLP, and DECIDE-AI anchors. | No model validation claim, clinical utility claim, or deployment claim. |
| `fgs_07_fusion_architecture_evidence` | Direct method evidence for the proposed graph/set/dense/sparse/temporal fusion architecture. | Governance sources constrain validation, but they do not prove the named architecture is correct. | Keep `mse_09` source-context-needed and run a future method-source extraction if selected. | No model implementation, benchmark, scoring, prediction, or model comparison. |
| `fgs_08_expert_review_conversion` | Turning expert-validation packets into real public review without flooding people or implying endorsement. | The repo has the review scaffolding but still needs human authorization, throttling, and public issue discipline. | Keep the active human-authorization blocker; if cleared, open narrow issue-based validation requests by reviewer lens. | No autonomous outreach, no private correspondence publication, no expert-review claim upgrade without review evidence. |
| `fgs_09_private_lab_bridge` | Governed private case workspace, consent, access control, audit logs, and sanitized learning export. | Public artifacts cannot reach a particular case without a private, consented, reviewable lab path. | Keep public work synthetic; define only private-lab blocker and projection checks until the private workspace exists. | No real intake, no PHI, no public case facts, no patient-specific outputs. |

## Highest-Value Next Public-Safe Queue

If the human does not authorize outreach, the next public-safe work should be
one of these no-outreach phases:

1. `measurement-refusal-negative-safety-fixtures-v0`
2. `spatial-imaging-residual-disease-context-v0`
3. `blood-based-mrd-mass-spectrometry-context-v0`
4. `fitness-toxicity-pro-context-source-extraction-v0`
5. `model-validation-transportability-bias-map-v0`
6. `fusion-architecture-method-source-extraction-v0`

The prior top recommendation,
`residual-disease-modality-discordance-source-extraction-v0`, and its
assay/specimen quality successor are now complete. The later
`measurement-state-refusal-fixture-extension-v0` synthetic fixture pressure,
`measurement-refusal-output-schema-v0`, and
`measurement-refusal-output-route-table-v0` are also complete. The later
`measurement-refusal-validator-skeleton-v0` is complete as a synthetic-only
structural report over routed refusal records. The top remaining
recommendation is `measurement-refusal-negative-safety-fixtures-v0`, because
the validator now needs adversarial/bad-route coverage before any
model-output path can reference those refusal records.

## ORP Mode Decision

This sweep should become a reusable ORP mode.

Mode name:
`frontier-gap-sweep-mode-v0`

Canonical mode artifact:
[ORP Frontier Gap Sweep Mode v0](../../orp/modes/frontier-gap-sweep-mode-v0.md)

Activation trigger:
Run the mode whenever the user asks whether the direction is off-base, what the
frontier looks like, what we are not thinking about, or why a delegation loop
appears to have completed too little.

Required output:

- current state audit
- validation status
- drift corrections
- external source sweep with dates and provenance
- blind-spot register
- public-safe next queue
- hard blockers
- Clawdad/ORP handoff

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, portal exports, images, notes, molecular files, exact
  dates tied to a person, private correspondence, or re-identification keys.
- No diagnosis, prognosis, treatment guidance, trial guidance, eligibility
  guidance, expanded-access guidance, monitoring guidance, urgency guidance,
  safety-management guidance, model prediction, recommendation, ranking,
  matching, publication authorization, or clinical decision.
- No claim that multiple myeloma has been cured or that a vaccine has been
  found.

## Limitations

- This is a source-informed gap sweep, not a systematic review.
- It does not rank sources, evidence, therapies, trials, mechanisms, or models.
- It does not establish model validity, clinical utility, endpoint acceptance,
  assay interchangeability, or clinical readiness.
- It does not clear expert-review, human-review, private-lab, clinical, legal,
  regulatory, publication, or outreach gates.
