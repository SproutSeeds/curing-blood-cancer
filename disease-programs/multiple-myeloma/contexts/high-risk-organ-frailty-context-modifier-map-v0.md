# High-Risk, Extramedullary, Organ, And Frailty Context Modifier Map v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `high-risk-organ-frailty-context-modifier-map-v0`
- frontier lane: high-risk, extramedullary, organ, and frailty context
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This map defines public-safe context modifier fields for multiple myeloma
research artifacts. It covers high-risk biology, extramedullary or disease-site
context, renal and bone context, immune and infection-risk context, performance
status, frailty, and prior exposure without creating patient-specific decision
logic.

The map is not a case intake form, risk score, prognosis tool, eligibility
tool, treatment guide, trial guide, monitoring guide, or review-packet output.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | Lane 6 asks for a context taxonomy or case-feature addendum, organ/frailty boundary note, and review-packet checklist update. | Create this context modifier map with an embedded review-packet checklist. |
| Existing substrate | Case-feature bundle summary already names a private-only disease-state envelope and risk-context field names. Mechanism extractions already preserve disease burden, site, high-risk, prior-therapy, renal-function, and bone-lesion context. | Reuse existing source-backed field labels instead of changing schemas in this pass. |
| Synthetic fixture guard | No schema fields are added or changed. | Do not add synthetic fixtures in this pass. |
| Safety risk | Context fields can become accidental prognosis, eligibility, treatment selection, trial matching, or option ranking. | Keep all fields optional, source-scoped, non-identifying, and non-directive. |

## Source Anchors

- `case-feature-bundle-public-summary-v0`
- `nci-pdq-2025-disease-context-v0`
- `tedder-bhutani-2025-disease-context-v0`
- `post-bcma-resistance-frontier-addendum-v0`
- `multiple-myeloma-multidisciplinary-review-packet-template-v0`
- `nci_pdq_myeloma_hp`
- `pubmed_palumbo_2015_imwg_frailty`
- `source-registry-v0`

## Public-Safe Context Field Shape

Future public artifacts may refer to a context modifier only with this
minimal shape:

| Field | Requirement | Refusal Rule |
| --- | --- | --- |
| `context_modifier_id` | Stable public identifier, such as `high-risk-cytogenetic-context-v0` or `frailty-context-v0`. | Refuse free-text patient descriptors. |
| `context_family` | One of the families below. | Refuse mixed context categories that hide source scope. |
| `public_value_state` | `source-defined-category`, `missing`, `unknown`, `private-only`, `synthetic-placeholder`, or `not-applicable`. | Refuse real values from a person in public artifacts. |
| `source_ids` | Public source IDs or extraction record IDs. | Refuse unsourced context claims. |
| `definition_source` | Source that defines the term, threshold, or field label. | Refuse harmonized labels without a definition source. |
| `uncertainty` | Missingness, source-limit, definition-mismatch, or expert-review-needed notes. | Refuse certainty language. |
| `allowed_reuse` | Research map routing, review-packet checklist, schema planning, or synthetic-only fixture planning. | Refuse prognosis, eligibility, treatment, trial, monitoring, referral, or option-ranking use. |

## Context Modifier Matrix

| Context Family | Public Field Examples | Allowed Use | Blocked Use |
| --- | --- | --- | --- |
| High-risk cytogenetic or molecular context | `del17p-context`, `t_4_14-context`, `t_14_16-context`, `t_14_20-context`, `1q-gain-or-amplification-context`, `1p32-deletion-context`, `plasma-cell-leukemia-context` | Preserve source-defined high-risk field names before comparing public research artifacts. | Do not infer prognosis, risk-adapted treatment, eligibility, urgency, or patient fit. |
| Extramedullary and disease-site context | `extramedullary-plasmacytoma-context`, `soft-tissue-site-context`, `bone-lesion-context`, `sampling-site-context` | Route source-defined disease-site labels into mechanism or review questions. | Do not interpret images, diagnose site involvement, rank severity, or assign prognosis. |
| Renal and organ context | `renal-function-context`, `organ-function-context`, `lab-validity-review-needed` | Preserve organ-function field names as source or private-lab context labels. | Do not provide renal monitoring, dose, supportive-care, eligibility, or safety-management guidance. |
| Bone disease context | `lytic-bone-lesion-context`, `bone-disease-context`, `imaging-linkage-needed` | Preserve public field names for source extraction and review routing. | Do not provide imaging interpretation, fracture-risk advice, or supportive-care guidance. |
| Immune status and infection-risk context | `immune-status-context`, `infection-risk-context`, `immune-reconstitution-context` | Mark that immune and infection context may affect research interpretation. | Do not provide infection-risk estimates, prophylaxis advice, vaccination advice, or monitoring instructions. |
| Performance status and frailty context | `performance-status-context`, `frailty-context`, `geriatric-assessment-context`, `functional-status-context` | Preserve source-defined geriatric or functional-assessment terms for research review. | Do not label a person as fit or frail, predict toxicity, assign transplant fit, or choose treatment intensity. |
| Prior exposure and therapy-history context | `prior-therapy-class-context`, `prior-bcma-exposure-context`, `relapsed-or-refractory-context` | Preserve exposure context before interpreting public mechanism, trial, or landscape artifacts. | Do not infer sequence, next therapy, trial fit, availability, eligibility, or urgency. |

## Review-Packet Context Checklist

Any future private review packet or public route table that references context
modifiers must ask:

| Checklist Item | Required Public Handling |
| --- | --- |
| Is the context field optional? | If no, block public reuse. |
| Is the value source-defined, missing, unknown, private-only, synthetic, or not applicable? | Record only the public-safe state. |
| Does the field require private lab validity, clinical interpretation, imaging review, or geriatric assessment? | Keep the value private and expose only the blocker. |
| Could the field imply prognosis, eligibility, treatment selection, monitoring, or option ranking? | Rewrite to a non-directive context label or block. |
| Is the field rare or identifying in combination with other features? | Keep it private unless privacy review approves aggregate or synthetic reuse. |
| Is an expert reviewer needed before public educational reuse? | Mark `expert-review-needed`. |

## Public Task Queue Seeds

These are queue seeds, not active ready tasks:

| Queue Seed | Public Work Needed | Boundary |
| --- | --- | --- |
| `context-modifier-definition-extraction-v0` | Extract source definitions for high-risk, extramedullary, renal, bone, immune, frailty, and prior-exposure fields into a non-identifying term table. | No prognosis or eligibility output. |
| `context-modifier-case-feature-addendum-v0` | Draft a case-feature bundle addendum that lists optional context fields and public-safe states only. | No public case upload or real values. |
| `context-modifier-synthetic-fixture-v0` | Add synthetic placeholder coverage only after a schema or fixture lane is selected. | Synthetic-only, no rare feature combinations. |
| `context-modifier-review-checklist-v0` | Extend future review-packet route tables to include optional context-field blockers. | No packet assembly or patient-specific review output. |

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No real context values for a person.
- No diagnosis, prognosis, treatment, trial, eligibility, expanded-access,
  monitoring, referral, safety-management, or option-ranking guidance.
- No source, mechanism, context, artifact, task, or evidence ranking.
- No cure or vaccine claim.

## Limitations

- This is a public context modifier map, not a clinical review.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not prognosis guidance.
- This is not treatment advice.
- This is not trial advice.
- This is not eligibility guidance.
- This is not monitoring guidance.
- This is not a frailty score, organ-function score, risk calculator, or
  disease-severity tool.
- It does not decide what context matters for any person.
- It does not change the case-feature bundle schema or add a public intake
  form.
- It does not use patient-identifying data, real case data, private records, or
  private expert correspondence.
