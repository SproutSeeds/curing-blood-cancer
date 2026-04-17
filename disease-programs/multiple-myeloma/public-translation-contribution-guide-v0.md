# Multiple Myeloma Public Translation And Contribution Guide v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-public-translation-contribution-guide-v0`
- frontier lane: public translation and contribution surface
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This guide helps patients, advocates, researchers, funders, builders, and
reviewers find the right public multiple myeloma artifact without turning the
repo into medical advice.

It also tells contributors which safe review, source-extraction, or evidence-gap
task to use.

This guide is not a patient guide, treatment guide, trial guide, screening
guide, monitoring guide, prognosis tool, personal risk tool, expanded-access
guide, or cure claim.

## Start Here

| Reader Goal | First Three Links | What You Can Learn | What You Cannot Learn |
| --- | --- | --- | --- |
| Understand the public myeloma work | [Disease README](README.md) -> [Public Inventory v0](public-inventory-v0.md) -> [Open Research Map v0.1](open-research-map-v0-1.md) | What artifacts exist and how the research map is organized. | Whether any person has a diagnosis, prognosis, treatment option, trial option, or cure path. |
| Understand the safety boundary | [Disease README](README.md) -> [Public Inventory v0](public-inventory-v0.md) -> [Public Review And Release Gate v0](public-review-release-gate-v0.md) | What the public repo can publish and what remains human-gated. | Permission to publish case-derived learning or use the repo clinically. |
| Understand MRD and endpoint wording | [Disease README](README.md) -> [MRD Endpoint Language Guardrail Addendum v0](measurements/mrd-endpoint-language-guardrail-addendum-v0.md) -> [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md) | Why response-depth terms need method, threshold, sample, timepoint, and endpoint context. | Whether an MRD result means cure, prognosis, or treatment choice for a person. |
| Understand immune therapy and access boundaries | [Disease README](README.md) -> [Immune Therapy Sequencing And Access Boundary v0](therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md) -> [Source Registry v0](../../sources/source-registry-v0.md) | Which status fields must be date-scoped before immune therapy records are reused. | Availability, eligibility, sequencing, referral, access, or treatment advice. |
| Understand post-BCMA resistance questions | [Disease README](README.md) -> [Post-BCMA Resistance Frontier Addendum v0](mechanisms/post-bcma-resistance-frontier-addendum-v0.md) -> [Evidence Gap Register v0](evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md) | Which mechanism statements are facts, derived claims, hypotheses, or open questions. | Mechanism ranking, patient relevance, product comparison, or option selection. |
| Understand precursor and risk language | [Disease README](README.md) -> [Precursor, Risk, And Interception Boundary Note v0](precursors/precursor-risk-interception-boundary-note-v0.md) -> [Source Registry v0](../../sources/source-registry-v0.md) | How MGUS, smoldering myeloma, risk, and interception language is bounded. | Screening advice, personal risk calculation, monitoring, trial fit, or prevention advice. |
| Understand context modifiers | [Disease README](README.md) -> [Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md) -> [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md) | How high-risk, organ, frailty, extramedullary, immune, infection-risk, and exposure labels stay optional and source-scoped. | Prognosis, eligibility, treatment intensity, transplant fit, or option ranking. |
| Understand case-to-cure plumbing | [Disease README](README.md) -> [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md) -> [Publication-Gate Checklist v0](publication-gate-checklist-v0.md) | Which public artifacts own each stage and what must stay private or human-gated. | Case upload, patient matching, trial matching, packet assembly, monitoring, or publication authorization. |
| Find expert-review work | [Disease README](README.md) -> [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md) -> [Expert Response Validation Ledger v0](reviews/expert-response-validation-ledger-v0.md) | Which public review items are open and how responses can be safely dispositioned. | Completed expert review or permission to copy private correspondence. |

## Glossary Index

| Topic | Public Anchor | Use This To Ask | Do Not Use This To Ask |
| --- | --- | --- | --- |
| MRD, response, relapse, and endpoints | [MRD Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md); [Endpoint Guardrail v0](measurements/mrd-endpoint-language-guardrail-addendum-v0.md) | What context a measurement term needs before public reuse. | Whether a result means cure, prognosis, monitoring, or treatment choice. |
| Targets, antigen escape, and mechanisms | [BCMA Claim Set v0](evidence-claims/bcma-antigen-escape-claim-set-v0.md); [Post-BCMA Addendum v0](mechanisms/post-bcma-resistance-frontier-addendum-v0.md) | Which mechanism claims need source context or expert review. | Whether a target or mechanism is actionable for a person. |
| Immune therapies and access | [Immune Therapy Boundary v0](therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md) | Which product, trial, class, and target fields need date-scoped source status. | Availability, eligibility, sequencing, urgency, or access advice. |
| Precursor states and risk | [Precursor Boundary Note v0](precursors/precursor-risk-interception-boundary-note-v0.md) | How precursor-state language can stay source-context-only. | Screening, personal risk, prevention, treatment, or monitoring advice. |
| High-risk and host context | [Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md) | Which context labels must stay optional, source-scoped, non-identifying, and non-directive. | Prognosis, treatment intensity, transplant fit, or frailty assessment for a person. |
| Case-to-cure stages | [Stage Validator Map v0](case-to-cure-stage-validator-map-v0.md) | Which stage owner artifact, validator or gate, and blocker applies. | Public case processing or patient-specific output generation. |
| Review readiness | [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md); [Expert Response Ledger v0](reviews/expert-response-validation-ledger-v0.md) | Which review item needs public-safe expert feedback. | A claim that expert review is complete. |

## Contributor Task Chooser

| Contribution Need | Use This Public Surface | Required Inputs | Safe Output |
| --- | --- | --- | --- |
| Extract facts from a public source | [Source Extraction issue form](../../.github/ISSUE_TEMPLATE/source-extraction-task.yml) | Source ID or URL, disease scope, extraction goal, mechanism or measurement IDs when known, source limits. | A public extraction request that names what the source supports and does not support. |
| Turn an evidence gap into a public task | [Evidence Gap issue form](../../.github/ISSUE_TEMPLATE/evidence-gap-task.yml) | Gap ID, linked claim IDs, public sources, task statement, confidence-gain statement, not-supported boundary. | A contribution-ready public task. |
| Request expert review of scope, evidence, or wording | [Expert Review issue form](../../.github/ISSUE_TEMPLATE/expert-review-task.yml) | Artifact path or ID, review lens, review findings, public source support, not-supported boundary. | Public-safe expert-review input that can be dispositioned without private correspondence. |
| Propose a wording fix | [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md) if the wording could affect science or safety; otherwise a normal documentation patch. | Exact artifact path, phrase or section, reason it may overclaim, safer replacement, source context when needed. | Narrow wording change that weakens or clarifies public claims. |
| Propose metadata or catalog repair | [Public Artifact Catalog v0](../../artifacts/public-artifact-catalog-v0.md) and the artifact metadata file. | Artifact ID, path, metadata path, source count, limitation count, validation result. | Catalog and metadata consistency improvement. |

## Review Task Map

| Review Area | Start With | Current Safe Status | Next Public Action |
| --- | --- | --- | --- |
| BCMA antigen escape and target-status claims | [BCMA Claim Set Expert Review Packet v0](reviews/bcma-claim-set-expert-review-packet-v0.md); issues #22 through #26 in the [Issue Index](reviews/expert-validation-issue-index-v0.md) | `expert-review-needed` | Submit public source-backed wording, measurement, mechanism, or readability feedback. |
| Disease-state, response, relapse, and MRD boundaries | [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md); issue #27 and issue #29 in the issue index | `expert-review-needed` | Review whether terminology is sufficiently bounded before educational reuse. |
| Cellular therapy, immune-effector, and access language | Multidisciplinary template; issue #28, issue #31, and issue #32 in the issue index | `expert-review-needed` | Review no-sequencing, no-availability, no-eligibility, and no-access-advice wording. |
| Safety, ethics, governance, and public readability | Multidisciplinary template; issue #33 and issue #34 in the issue index | `expert-review-needed` | Review whether a patient, advocate, or builder could mistake an artifact for advice. |
| Context modifiers and case-to-cure plumbing | [Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md); [Stage Validator Map v0](case-to-cure-stage-validator-map-v0.md) | `source-checked`, `expert-review-needed` where review-template language is reused | Confirm fields remain optional, non-identifying, source-scoped, and blocker-routed. |

## Safe Contribution Packet

Before opening an issue or pull request, prepare:

- artifact path or stable ID
- public source IDs, URLs, PMIDs, registry IDs, or regulatory anchors
- linked claim IDs, gap IDs, measurement-term IDs, mechanism IDs, or query IDs
  when known
- what is missing, ambiguous, or overclaimed
- what the contribution does not prove
- clinical-use boundary text
- validation command and result, when files are changed

## Refuse Or Redirect

| Request | Public Response |
| --- | --- |
| "Can I upload records here?" | No. Do not upload records, images, notes, identifiers, dates tied to a person, or private case facts. |
| "What should a patient do?" | This repo cannot answer diagnosis, prognosis, treatment, trial, expanded-access, monitoring, or safety-management questions. |
| "Is a trial or product available for someone?" | This repo cannot determine eligibility, availability, site status, sponsor access, or fit for any person. |
| "Does this mean a cure was found?" | No. The repo tracks open research questions and public-safe infrastructure; it does not claim a cure or vaccine. |
| "Can this artifact be used in a public explainer?" | Only after source scope, uncertainty, limitations, expert-review status, and public-safety boundaries are clear. |

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No credentials, paid APIs, account changes, or restricted datasets.
- No diagnosis, prognosis, treatment, trial, eligibility, expanded-access,
  screening, monitoring, safety-management, or personal-risk advice.
- No target, therapy, trial, source, mechanism, context, artifact, task, or
  evidence ranking.
- No copied private correspondence.
- No generated biomedical claims.
- No expert-review substitution.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This is a navigation and contribution guide, not a scientific review.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not prognosis guidance.
- This is not treatment advice.
- This is not trial advice.
- This is not eligibility guidance.
- This is not expanded-access guidance.
- This is not screening, monitoring, or personal-risk guidance.
- This does not make any artifact expert-reviewed.
- This does not authorize public case processing, public case upload, public
  review-packet assembly, patient matching, trial matching, option ranking, or
  publication workflow.
- This does not claim that multiple myeloma has been cured or that any vaccine
  has been found.
