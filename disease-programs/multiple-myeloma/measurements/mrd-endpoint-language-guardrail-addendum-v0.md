# MRD Endpoint Language Guardrail Addendum v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `mrd-endpoint-language-guardrail-addendum-v0`
- frontier lane: MRD, deep response, and endpoint language
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This addendum makes MRD, complete response, stringent complete response,
sustained MRD negativity, deep response, relapse, and endpoint language safer
to reuse in public multiple myeloma artifacts.

It prevents response-depth language from becoming a cure claim, prognosis,
treatment recommendation, trial recommendation, monitoring instruction,
eligibility claim, expanded-access suggestion, or patient-specific option
ranking.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | The frontier roadmap names Lane 2 as a finite first artifact: an MRD and endpoint language addendum with public source-extraction tasks. | Create this guardrail as the first Lane 2 artifact. |
| Existing substrate | The MRD glossary already defines terms, and the BCMA measurement audit already shows how missing measurement context is represented. | Extend by adding endpoint-status and refusal rules, not by creating a new tool. |
| Regulatory context | The FDA page is a January 2026 draft guidance page, content current as of 2026-01-20, and says the draft is nonbinding and not for implementation. | Use only as regulatory-context provenance, not as clinical guidance or product status. |
| Downstream tooling | No validated endpoint-record shape exists yet. | Block endpoint scoring, ranking, or dashboard use until source fields are extracted and validated. |

## Source Anchors

- `fda_mrd_cr_endpoint_guidance_2026`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_munshi_2017_mrd_survival_meta_analysis`
- `pubmed_soh_2022_mrd_flow_harmonization`
- `mrd-and-relapse-measurement-glossary-v0`
- `bcma-measurement-context-audit-v0`
- `multiple-myeloma-frontier-roadmap-v0`
- `governance-public-safety`

## Required Endpoint Context Fields

Any public artifact that reuses MRD or response-depth language must preserve
these fields or mark the record `source-context-needed`.

| Field | Capture Requirement | Fail-Closed Status |
| --- | --- | --- |
| Source term | Exact source wording for MRD, CR, stringent CR, sustained MRD negativity, relapse, progression, or endpoint status. | `source-context-needed` |
| Measurement method | Flow cytometry, sequencing, imaging, clinical response category, or source-defined endpoint method. | `method-needed` |
| Sample or specimen | Bone marrow, imaging context, blood, tissue, model system, or source-defined sample context. | `sample-context-needed` |
| Threshold or detection limit | Assay sensitivity, cutoff, detection limit, scoring rule, or explicit missing threshold. | `threshold-needed` |
| Disease state | Frontline, relapsed/refractory, post-BCMA, post-CAR T, maintenance, or source-defined cohort context. | `disease-state-needed` |
| Treatment context | Class, regimen context, study arm context, or explicit no-treatment-context-present. | `treatment-context-needed` |
| Timepoint | Assessment timepoint relative to therapy, study visit, response assessment, relapse, or progression. | `timepoint-needed` |
| Duration or confirmation interval | Confirmation interval, sustained-response duration, follow-up duration, or explicit not reported. | `duration-needed` |
| Endpoint role | Source-defined response category, exploratory endpoint, surrogate or intermediate endpoint under review, regulatory endpoint context, clinical outcome endpoint, or not an endpoint. | `endpoint-role-needed` |
| Population denominator | Cohort, arm, denominator, evaluable population, or explicit denominator missing. | `denominator-needed` |
| Source IDs | Public source IDs and artifact IDs used to support the term. | `provenance-needed` |
| Limitation note | Plain statement of what cannot be inferred from the term. | `limitation-needed` |

## Response-Term Guardrails

| Term | Public Use | Required Context | Do Not Infer |
| --- | --- | --- | --- |
| MRD negativity | Use only as a source-defined measurement state. | Method, specimen, threshold, timepoint, disease state, and source ID. | Do not infer no disease anywhere, cure, treatment success, or patient-specific prognosis. |
| Sustained MRD negativity | Use only when the source reports repeat MRD-negative assessments and the confirmation interval. | All MRD fields plus interval, duration, and follow-up context. | Do not turn one negative assessment into durable remission or cure. |
| Complete response | Use as a conventional source-defined response category. | Source criteria, disease state, treatment context, assessment timing, and whether MRD was assessed separately. | Do not equate CR with MRD negativity, clinical benefit, cure, or treatment choice. |
| Stringent complete response | Use as a source-defined response category with stricter criteria than CR. | Source criteria, denominator, timing, and whether MRD or imaging context is present. | Do not treat stringent CR as deeper than MRD without source-stated MRD data. |
| Deep response | Use only if mapped to a source-defined category or explicitly marked ambiguous. | Term definition, category mapping, and source limitation note. | Do not use as a standalone endpoint or quality signal. |
| Relapse or progression | Use only with the source's event definition and measurement trigger. | Event definition, timepoint, assessment method, and denominator. | Do not compare relapse claims across sources unless definitions align. |
| Progression-free survival | Use as a study-level endpoint with population and follow-up context. | Source endpoint definition, population, follow-up, and analysis context. | Do not infer patient-specific prognosis or therapy ranking. |
| Overall survival | Use as a population-level study endpoint with follow-up context. | Source endpoint definition, population, follow-up, and analysis context. | Do not infer individual survival or treatment selection. |
| MRD plus CR regulatory context | Use only to describe source-stated endpoint context in public research tracking. | Regulatory source, draft/final status, method, sample, threshold, CR definition, and source limitation. | Do not infer approval, availability, eligibility, product status, clinical benefit, or trial advice. |

## Endpoint Status Values

| Status Value | Allowed Public Use | Blocked Inference |
| --- | --- | --- |
| `source-defined-response-category` | A response category described by a public source. | Not a cure claim or patient outcome claim. |
| `exploratory-endpoint` | A research endpoint requiring source context and review. | Not validated clinical actionability. |
| `surrogate-or-intermediate-endpoint-under-review` | A source-stated endpoint status that requires source date and limitation text. | Not proof of clinical benefit or treatment effect for a person. |
| `regulatory-endpoint-context` | A regulatory-context statement from a public source, including draft or nonbinding status when relevant. | Not product availability, approval, eligibility, treatment, or trial guidance. |
| `clinical-outcome-endpoint` | A study endpoint such as PFS or OS with population and follow-up context. | Not individual prognosis. |
| `not-an-endpoint` | A term is being used as descriptive measurement context only. | Not a scoring feature. |
| `source-context-needed` | Required source fields are missing or ambiguous. | Not reusable in generated claims, dashboards, ranking, or review packets. |

## Fail-Closed Rules

Public artifacts must use `source-context-needed` or `wording-fix-needed`
when any of these conditions appear:

- MRD or CR language lacks method, sample, threshold, timepoint, or source ID.
- "Negative" is worded as if residual disease cannot exist anywhere.
- Complete response, stringent complete response, deep response, or MRD
  negativity is used as a cure claim.
- MRD, CR, PFS, OS, relapse, or progression language is used to rank therapies,
  trials, targets, products, sources, mechanisms, or patient options.
- A draft or nonbinding regulatory source is worded as if it establishes
  clinical actionability, product approval, eligibility, availability, or
  treatment choice.
- A population-level endpoint is converted into patient-specific prognosis.
- A missing endpoint field is silently filled from private records, memory, or
  generated prose.

## Public Source-Extraction Task Queue

This pass creates a public task draft instead of a new endpoint-record schema.
The next contributor should extract source fields before any dashboard,
scoring, or endpoint-record tooling is added.

| Task ID | Status | Purpose | Issue Draft |
| --- | --- | --- | --- |
| `multiple-myeloma-mrd-endpoint-source-extraction-task-v0` | ready | Extract FDA, IMWG, and MRD literature endpoint context into public fields for method, sample, threshold, timepoint, duration, endpoint role, limitation, and source date. | [MRD endpoint source extraction task](../public-tasks/issue-drafts/multiple-myeloma-mrd-endpoint-source-extraction-task-v0.md) |

## Downstream Use Rule

A downstream artifact may reference MRD or response-depth terms only if it
copies this guardrail's required fields or links to a validated source record
that contains them. If the fields are absent, the downstream artifact must
carry `source-context-needed` and must not support generated claims, scoring,
trial matching, patient matching, review-packet filling, or recommendation
behavior.

## Limitations

- This is a public research guardrail, not a scientific review.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not treatment, trial, eligibility, expanded-access, or monitoring
  guidance.
- This does not claim that MRD negativity, complete response, stringent
  complete response, or sustained MRD negativity means cure.
- This does not establish that any endpoint is clinically validated for any
  patient or decision.
- This does not rank assays, endpoints, trials, therapies, products, targets,
  sources, mechanisms, artifacts, or evidence.
- This does not use real case data, patient-identifying data, or private lab
  records.
- This does not authorize endpoint dashboards, scoring, generated claims,
  patient matching, trial matching, or review-packet generation.
- Regulatory, endpoint, and trial contexts can change after the access date.
