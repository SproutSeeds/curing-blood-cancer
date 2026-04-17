# Precursor, Risk, And Interception Boundary Note v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `precursor-risk-interception-boundary-note-v0`
- frontier lane: precursor, risk, and interception questions
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This boundary note defines how the public repo may discuss monoclonal
gammopathy of undetermined significance, smoldering multiple myeloma, early
intervention, interception, risk, and prevention-adjacent research without
turning those topics into screening advice, personal risk advice, diagnosis,
prognosis, treatment advice, trial advice, monitoring guidance, or prevention
claims.

It is a guardrail and open-question queue. It is not a patient guide.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | Lane 5 asks for a precursor boundary note, source registry delta, risk-language guardrail, and open-question queue. | Create one boundary artifact with the queue inside it. |
| Existing substrate | The NCI PDQ myeloma source already covers MGUS and smoldering myeloma in a health-professional context. | Reuse the existing NCI source ID and add specific IMWG precursor-state source anchors. |
| Safety risk | Precursor language can easily become screening, personal-risk, monitoring, anxiety, or early-treatment guidance. | Fail closed: population or source-context language only. |
| Next unresolved range | Public tasks need source-backed extraction of definitions, risk-model fields, and early-intervention wording before any dashboard or plain-language page. | Use an open-question queue, not a calculator or explorer. |

## Source Anchors

- `nci_pdq_myeloma_hp`
- `pubmed_kyle_2010_mgus_smm_imwg`
- `pubmed_mateos_2020_smm_risk_model`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `multiple-myeloma-frontier-roadmap-v0`
- `source-registry-v0`

## Boundary Matrix

| Topic | Allowed Public Use | Required Context Fields | Blocked Public Use |
| --- | --- | --- | --- |
| MGUS | Source-scoped precursor-state term and population-level research context. | Source ID, definition source, cohort or population context, progression endpoint, uncertainty, and limitations. | Screening recommendation, diagnosis, personal risk estimate, monitoring schedule, or reassurance/escalation language. |
| Smoldering multiple myeloma | Source-scoped disease-state term and research-context label for open questions. | Source ID, diagnostic-definition source, risk-model source when used, time horizon, outcome, cohort, and limitations. | Treatment recommendation, trial fit, personal prognosis, or conversion of a risk group into individual advice. |
| Early intervention | Research topic for source extraction and trial-language review. | Trial or literature source, disease-state definition, intervention context, endpoint, status date, and no-advice boundary. | Recommendation to seek, avoid, start, delay, or compare any intervention. |
| Interception and prevention-adjacent research | Open-question language about public research directions. | Source type, disease state, target population, endpoint, maturity, and claim level. | Claim that prevention exists, vaccine claim, individual prevention plan, or public screening prompt. |
| Risk factors and risk models | Cohort-level or source-reported variables to preserve for research maps. | Cohort, model, variables, time horizon, outcome, calibration or validation status when reported, and source limitations. | Personal calculator, individualized risk score, prognosis, anxiety prompt, or clinical monitoring instruction. |
| Public readability | Wording that makes boundaries clear for non-specialists. | Plain statement of what the artifact cannot answer. | Patient-facing calls to test, screen, treat, monitor, enroll, or self-stratify. |

## Risk-Language Guardrail Fields

Any future precursor or interception artifact must preserve these fields before
reusing risk or early-intervention language:

| Field | Requirement | Refusal Rule |
| --- | --- | --- |
| `source_id` | Stable public source ID from the registry. | Refuse unsourced precursor or risk claims. |
| `disease_state_definition` | Source-defined MGUS, smoldering myeloma, active myeloma, or other plasma-cell state. | Refuse to merge precursor-state language with active-treatment language. |
| `population_or_cohort` | Population, cohort, registry, or study context when stated. | Refuse individual applicability claims. |
| `risk_variables` | Source-reported variables only. | Refuse new risk factors invented from local notes or private case data. |
| `time_horizon` | Time horizon or follow-up frame when the source provides one. | Refuse timeless progression claims. |
| `endpoint_or_outcome` | Progression, diagnosis, response, intervention, trial endpoint, or other source-defined outcome. | Refuse cure, prevention, or clinical benefit claims unless directly source-backed and still non-advisory. |
| `validation_status` | Whether the source describes validation, retrospective analysis, prospective validation need, or unresolved uncertainty. | Refuse to treat a model as generally validated without source context. |
| `allowed_reuse` | Research map, source extraction, issue draft, or review question. | Refuse patient-facing calculators, screening prompts, treatment selection, trial selection, or monitoring schedules. |

## Open-Question Queue

| Queue ID | Public Question | Source Basis | Next Public Action | Boundary |
| --- | --- | --- | --- | --- |
| `precursor-state-definition-extraction-v0` | Which source-defined terms and thresholds are needed before the repo can mention MGUS or smoldering myeloma consistently? | `nci_pdq_myeloma_hp`; `pubmed_kyle_2010_mgus_smm_imwg` | Create a source-extraction issue draft for precursor definitions and exclusions. | Do not use the extraction as diagnosis guidance. |
| `smm-risk-model-context-extraction-v0` | Which cohort, variable, time-horizon, and validation fields are needed before smoldering-risk language appears in maps? | `pubmed_mateos_2020_smm_risk_model`; `pubmed_kyle_2010_mgus_smm_imwg` | Draft a risk-model context extraction template with no score output. | Do not create a personal risk calculator. |
| `early-intervention-trial-language-boundary-v0` | How should early-intervention trials be cited without implying a treatment path? | `clinicaltrials_gov`; `clinicaltrials_gov_api_v2`; source registry trial limits | Draft trial-language refusal rules for precursor-state records. | Do not imply availability, eligibility, urgency, or trial fit. |
| `immunoprevention-term-guardrail-v0` | How should vaccine, immune-priming, and prevention-adjacent research be separated from prevention claims? | Public roadmap opportunity map and future source extraction. | Create a source-backed term guardrail before any immunoprevention map. | Do not imply an established vaccine or prevention strategy. |
| `public-readability-anxiety-check-v0` | Which words make precursor-state artifacts sound like personal risk advice? | Expert-validation public-readability lens. | Add a public readability checklist item for precursor artifacts. | Do not prompt self-stratification, screening, or medical action. |

## Source Registry Delta

This pass adds two public literature source anchors for precursor-state
language:

- `pubmed_kyle_2010_mgus_smm_imwg`
- `pubmed_mateos_2020_smm_risk_model`

The existing `nci_pdq_myeloma_hp` source is also marked as usable for
precursor-risk context. These records are for public research terminology and
source extraction only. They do not authorize personal risk estimates,
screening guidance, monitoring schedules, treatment recommendations, trial
recommendations, or prevention claims.

## Allowed Wording

Use:

- "source-defined precursor-state terminology"
- "cohort-level risk-model context"
- "open research question"
- "early-intervention trial-language boundary"
- "prevention-adjacent research hypothesis"

Do not use:

- "you should be screened"
- "your risk is"
- "high-risk patients should"
- "early treatment is recommended"
- "trial option"
- "prevention strategy"
- "vaccine path"
- "monitoring schedule"

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No patient-specific diagnosis, prognosis, treatment, trial, eligibility,
  expanded-access, screening, monitoring, or prevention guidance.
- No personal risk calculator.
- No risk ranking.
- No cure or vaccine claim.
- No expert-review substitution.

## Limitations

- This is a public boundary note, not a scientific review.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not screening guidance.
- This is not personal risk advice.
- This is not prognosis guidance.
- This is not treatment advice.
- This is not trial advice.
- This is not monitoring guidance.
- This is not prevention guidance.
- It does not make MGUS, smoldering myeloma, early intervention, or
  prevention-adjacent language expert-reviewed.
- It does not prove source coverage is comprehensive.
- It does not use patient-identifying data, real case data, private records, or
  private expert correspondence.
