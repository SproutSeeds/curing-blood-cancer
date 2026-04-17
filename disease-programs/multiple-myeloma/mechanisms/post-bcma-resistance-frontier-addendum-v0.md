# Post-BCMA Resistance Frontier Addendum v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `post-bcma-resistance-frontier-addendum-v0`
- frontier lane: post-BCMA resistance and relapse mechanisms
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This addendum extends the existing post-CAR T relapse mechanism map into a
frontier-facing post-BCMA resistance summary. It labels each mechanism family
by claim level, separates antigen from non-antigen questions, records key
contradiction and uncertainty themes, and links mechanism questions back to
public gaps and contribution tasks.

It does not add a new extraction record because the current coverage report
already says every v0 mechanism bucket has at least two public extraction
records or a documented interpretation boundary. The useful next move is a
claim-level and uncertainty addendum before any mechanism explorer, ranking, or
dashboard.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | Lane 4 asks for a mechanism addendum or extraction queue, gap register updates, and claim levels for every mechanism statement. | Create this mechanism addendum and update gap/navigation links. |
| Existing coverage | The coverage report says no bucket currently needs first extraction or second-source extraction for v0 navigation. | Do not add another extraction record in this pass. |
| Existing gaps | The BCMA evidence-gap register already names frequency, assay context, alternate-target translation, multifactorial resistance, and expert review gaps. | Link these gaps to mechanism families and add a frontier update note. |
| Safety boundary | Mechanism language can easily sound like a patient-specific option or sequence. | Keep every mechanism non-advisory and block ranking, product comparison, and patient action. |

## Source Anchors

- `post-car-t-relapse-mechanism-map-v0`
- `post-car-t-relapse-mechanism-coverage-v0`
- `bcma-antigen-escape-claim-set-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`
- `post-car-t-relapse-mechanism-gap-public-task-queue-v0`
- `mrd-endpoint-language-guardrail-addendum-v0`
- `immune-therapy-sequencing-access-boundary-v0`
- `multiple-myeloma-frontier-roadmap-v0`
- `source-registry-v0`

## Claim-Level Mechanism Matrix

| Mechanism Family | Current Public Basis | Claim Level For Reuse | Linked Public Gap Or Task | Do Not Infer |
| --- | --- | --- | --- | --- |
| BCMA antigen loss, low density, or target alteration | Source-specific extraction records and BCMA claim set. | `derived-claim` plus `open-question` for frequency and cross-product scope. | `bcma-escape-frequency-denominator-gap-v0`; denominator extraction task completed for current v0. | Do not infer frequency across products, disease states, prior-exposure groups, or patients. |
| TNFRSF17 or BCMA alteration | Extraction-field signal inside antigen escape records. | `derived-claim` only when source-specific assay and specimen context are visible. | `bcma-measurement-context-completeness-gap-v0`. | Do not treat alteration, low expression, or absence as a standalone clinical biomarker. |
| Low BCMA density and alternate-target research | Di Meo and target-linked phenotype records. | `hypothesis` plus `open-question` for translation. | `alternate-target-clinical-translation-gap-v0`. | Do not infer clinical efficacy, clinical safety, availability, or target actionability. |
| CAR T fitness, exhaustion, expansion, or persistence | Ledergor extraction plus review-level Yue coverage. | `hypothesis` plus `expert-review-needed` when immune-state details are incomplete. | `non-antigen-loss-relapse-buckets-gap-v0`; CAR T fitness extraction tasks completed for v0. | Do not infer this is the dominant relapse mechanism or a product comparison. |
| Immune microenvironment constraints | Review-level category coverage and extraction signals. | `open-question`; source-context-needed until primary-study fields are extracted. | `non-antigen-loss-relapse-buckets-gap-v0`. | Do not infer causality, patient relevance, or intervention choice from review categories. |
| Plasma-cell identity or lineage-state escape | Maura and Di Meo target-linked phenotype records. | `hypothesis` plus `mechanistic-preclinical` where model or preprint context applies. | `non-antigen-loss-relapse-buckets-gap-v0`; identity extraction tasks completed for v0. | Do not infer clinical readiness, frequency, or that lineage-state escape explains all relapse. |
| Disease burden, site, and high-risk context | Tedder/Bhutani and NCI PDQ disease-context records. | `context-field` plus `open-question`, not a causal mechanism unless source states causality. | `non-antigen-loss-relapse-buckets-gap-v0`; disease-context extraction tasks completed for v0. | Do not infer prognosis, eligibility, treatment selection, or mechanism ranking. |
| Sequential or dual-target immune pressure | Trial and source context fields in mechanism map and immune therapy boundary. | `open-question` for research design context; `trial-registry-snapshot-only` for trial records. | `non-antigen-loss-relapse-buckets-gap-v0`; immune therapy access boundary. | Do not infer therapy sequence, trial fit, expanded-access path, or urgency. |
| Measurement and follow-up gaps | MRD glossary, endpoint guardrail, BCMA measurement audit, and coverage report. | `source-context-needed` until method, specimen, threshold, timepoint, denominator, and follow-up are visible. | `bcma-measurement-context-completeness-gap-v0`; MRD endpoint source extraction task draft. | Do not compare mechanisms when measurement context is missing or inconsistent. |

## Contradiction And Uncertainty Register

| Register ID | Uncertainty Or Contradiction | Why It Matters | Public Next Action |
| --- | --- | --- | --- |
| `post-bcma-target-retained-vs-target-loss-v0` | Some relapse records may involve target loss or low density, while others may retain target expression or lack enough assay context. | Antigen escape must not collapse all post-BCMA relapse into one mechanism. | Preserve assay, specimen, timing, prior exposure, and denominator context before comparison. |
| `review-level-vs-primary-study-v0` | Review articles can name mechanism families that primary-study records may not measure consistently. | Review-level categories are useful for navigation but weak for claim strengthening. | Mark review-level rows `source-context-needed` until primary-study extraction exists. |
| `target-density-vs-target-actionability-v0` | Tumor target-density signals are separate from normal-tissue reactivity, safety, efficacy, and clinical readiness. | Alternate-target language can be misread as a therapy option. | Keep target-density, normal-tissue, model, and clinical-safety fields separate. |
| `context-field-vs-causal-mechanism-v0` | Disease burden, site, high-risk biology, prior exposure, and eligibility context may shape relapse interpretation without being the direct cause. | Context fields can become accidental prognosis or option-ranking language. | Label context rows as context fields unless a source explicitly supports causality. |
| `trial-design-vs-treatment-sequence-v0` | Trials may test prior-exposure or next-target concepts without proving a sequence. | Trial references can look like pathway advice. | Link to the immune therapy access boundary before any trial or product reuse. |
| `mrd-depth-vs-mechanism-claim-v0` | Deep response, MRD negativity, relapse timing, and mechanism claims depend on measurement method and follow-up. | Response depth can be mistaken for cure, prognosis, or mechanism proof. | Apply the MRD endpoint guardrail before interpreting relapse mechanism timing. |

## Gap Register Frontier Update

The existing BCMA evidence-gap register remains the active public gap register
for this lane. This addendum adds the frontier interpretation:

- The public map has v0 navigation coverage across antigen and non-antigen
  buckets.
- The unresolved frontier gap is not first extraction coverage; it is stronger
  source-specific comparison without ranking or patient-action inference.
- Future tasks should focus on primary-study extraction depth, contradiction
  capture, and measurement harmonization before new dashboards or mechanism
  scoring.
- Mechanism claims must carry one of these statuses before reuse:
  `derived-claim`, `hypothesis`, `open-question`, `context-field`,
  `source-context-needed`, `mechanistic-preclinical`, or
  `expert-review-needed`.

## Public Contribution Boundary

Future public tasks may:

- extract source-specific denominators, assay methods, specimen context,
  target status, immune-state fields, disease-site context, prior-exposure
  context, and follow-up fields
- add contradiction notes when two public sources use different assays,
  populations, response definitions, or mechanism labels
- propose a validated contradiction-register shape before any mechanism
  dashboard

Future public tasks must not:

- rank mechanisms, products, targets, trials, therapies, sources, artifacts, or
  evidence
- infer a direct patient option from any mechanism
- infer diagnosis, prognosis, treatment, trial, expanded-access, monitoring,
  eligibility, referral, or sequencing guidance
- use real case data or private lab records
- claim that any mechanism explains all relapse or that any intervention cures
  multiple myeloma

## Limitations

- This is a public research addendum, not a scientific review.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not treatment, trial, expanded-access, eligibility, referral, or
  monitoring guidance.
- This does not claim that multiple myeloma has been cured.
- This does not identify the most important or most frequent relapse mechanism.
- This does not compare products, trials, targets, mechanisms, or evidence
  strength.
- This does not establish clinical actionability for BCMA loss, low BCMA,
  SEMA4A, CAR T fitness, immune microenvironment, lineage-state, disease-site,
  high-risk, prior-exposure, or MRD findings.
- This does not use patient-identifying data, real case data, private records,
  or private expert correspondence.
- Expert review is still needed before use as an educational anchor.
