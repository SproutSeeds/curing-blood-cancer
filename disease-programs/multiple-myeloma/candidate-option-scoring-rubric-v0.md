# Candidate-Option Scoring Rubric v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- rubric status: `public-review-readiness-v0`
- claim level: `open-question`
- last reviewed: `2026-04-15`
- clinical boundary: research-use-only, not medical advice

## Purpose

This rubric helps public contributors organize candidate-option review
questions in the multiple myeloma case-to-cure pipeline.

It does not rank options for any person. It does not recommend treatment,
trial enrollment, expanded access, monitoring, or care. It scores only whether
a candidate-review question is sufficiently sourced, bounded, and reviewable
for a private multidisciplinary process or a public generic artifact update.

## No-Action Principle

Every candidate starts with `no_public_action`.

A score can move a record toward clearer review, better source work, or a
documented no-go state. A score cannot select a pathway, override a clinician,
establish trial eligibility, establish investigational-product access, or
create patient-specific advice.

## Candidate Types

`candidate_type` must be assigned before any score is interpreted.

| Candidate Type | Meaning | Required Owner Before Real-World Use | Public Output |
| --- | --- | --- | --- |
| `standard-care-review` | A question for qualified clinicians about approved or guideline-recognized care in context. | Treating clinician. | Generic source gap or review prompt only. |
| `trial-review` | A question about whether public trial records deserve private site or clinician verification. | Treating clinician and trial site. | De-identified query-pattern artifact or trial-source gap only. |
| `expanded-access-review` | A question about whether an investigational-product pathway is legally, clinically, and operationally possible. | Treating physician, sponsor, institution, and regulator where applicable. | Generic pathway gap only. |
| `research-only-hypothesis` | A biological or translational hypothesis that is not ready for care. | Research lead or expert reviewer. | Evidence gap, source-extraction task, or review packet item. |
| `no-go` | A record that a path should not proceed or should remain blocked. | Treating clinician, review board, or responsible reviewer where relevant. | De-identified safety pattern or blocked-status note only. |

## Required Candidate Record Fields

Any private candidate-option record that uses this rubric should include:

- `candidate_type`
- review question
- source IDs
- claim IDs, evidence-gap IDs, query-record IDs, or regulatory source IDs when
  relevant
- case-feature links stored only in the private workspace
- known constraints
- overclaiming risk
- required review owner
- verification requirements
- public-export decision
- limitations and what-not-to-infer language

Public artifacts may refer to candidate types and generic field names. They
must not contain patient-specific candidate options.

## Score Scale

Each dimension uses a 0 to 3 scale.

| Score | Meaning |
| --- | --- |
| `0` | Missing, unsafe, unsupported, or not reviewable. |
| `1` | Present but weak, ambiguous, or missing key provenance. |
| `2` | Usable for structured review with important caveats. |
| `3` | Strong enough for public review-readiness tracking within its candidate type. |

Higher score means stronger review readiness, not better treatment, better
trial, better access path, or better patient fit.

## Scoring Dimensions

| Dimension | What To Score | What Not To Infer |
| --- | --- | --- |
| `source_provenance` | Source IDs, query-record IDs, claim IDs, and access dates are traceable. | Do not infer source quality or clinical actionability from provenance alone. |
| `evidence_signal_and_uncertainty` | The evidence signal, contradictions, maturity, and limitations are explicit. | Do not infer efficacy, safety, or comparative benefit. |
| `measurement_context` | MRD, response, relapse, target, assay, and sample context are preserved where relevant. | Do not compare measurements across sources without method alignment. |
| `feasibility_verification_readiness` | The record names what clinician, site, sponsor, regulatory, or institutional checks would be needed. | Do not infer that any pathway is feasible or available. |
| `safety_and_overclaiming_controls` | Safety unknowns, overclaiming risk, and no-action language are explicit. | Do not reduce safety review to a public score. |
| `review_owner_clarity` | The record states who must review before any real-world use. | Do not treat public review readiness as qualified review. |
| `public_artifact_readiness` | The record can produce a safe public task, gap, query-pattern, or review prompt without private facts. | Do not downstream patient-specific candidate options. |

## Interpretation Bands

The maximum score is 21. Bands are advisory for artifact work only.

| Total | Public Meaning |
| --- | --- |
| `0-7` | Blocked or no-go for public downstreaming until safety and provenance gaps are resolved. |
| `8-14` | Needs source extraction, measurement clarification, review-owner mapping, or boundary repair. |
| `15-21` | Ready for a generic public task, review prompt, or private multidisciplinary packet item. |

Interpret totals only inside the same `candidate_type`. Do not compare a
trial-review total with a standard-care-review, expanded-access-review,
research-only, or no-go total.

## Type-Specific Gates

### Standard-Care Review

Required before scoring above 1:

- public source IDs for approved or established care context
- clinician-owner requirement
- measurement and disease-state context where relevant
- explicit statement that this is not a recommendation

Public output should be limited to source gaps or generic review prompts.

### Trial Review

Required before scoring above 1:

- ClinicalTrials.gov query record or public trial source ID
- query provenance and source freshness
- site-verification requirement
- eligibility-verification boundary
- explicit statement that this is not trial advice

A trial listing cannot prove availability, eligibility, safety, efficacy, or
fit for any person.

### Expanded-Access Review

Required before scoring above 1:

- investigational-product status or source gap
- treating-physician owner requirement
- sponsor, institutional, and regulatory verification requirements
- safety and logistics unknowns
- explicit statement that this is not expanded-access guidance

If sponsor, regulatory, or treating-physician verification is missing, keep the
record blocked or research-only.

### Research-Only Hypothesis

Required before scoring above 1:

- hypothesis statement
- source IDs or explicit missing-source gap
- translation and safety boundary
- proposed public artifact path, such as extraction task or evidence gap
- explicit statement that the hypothesis is not ready for care

Research-only is a valid endpoint. It should not be upgraded into a clinical
review bucket without new evidence and qualified review.

### No-Go

Required fields:

- reason for no-go or blocked status
- source, safety, feasibility, privacy, or review basis
- owner or review body needed to revisit, if any
- public-safe learning that can be extracted, if any

No-go is a safety-preserving outcome, not a failure.

## Fail-Closed Rules

Set status to blocked or no-go if any of these are true:

- private case facts would be needed in the public repo
- provenance is missing
- measurement context is ambiguous and material to the claim
- trial status, site availability, sponsor access, or eligibility would be
  inferred from public records alone
- safety, toxicity, logistics, or contraindication review is missing
- expanded-access feasibility would require sponsor, regulator, institution, or
  treating-team decisions
- the record could be read as patient-specific advice
- a cure, vaccine, efficacy, safety, or access claim would be unsupported

## Review Boundary

This rubric is a public research artifact. It is not medical advice,
diagnostic guidance, treatment guidance, trial guidance, expanded-access
guidance, monitoring guidance, or a claim that a cure has been found.
