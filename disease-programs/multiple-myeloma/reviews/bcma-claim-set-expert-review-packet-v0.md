# BCMA Claim Set Expert Review Packet v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- claim set: `bcma-antigen-escape-claim-set-v0`
- gap register: `bcma-antigen-escape-evidence-gap-register-v0`
- linked gap: `expert-review-readiness-gap-v0`
- review status: expert-review-needed
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-14`

## Purpose

This packet prepares the BCMA claim set and evidence gap register for qualified
expert review.

It does not make the artifacts expert-reviewed. It gives reviewers a precise
map of what to check, which IDs each review note should reference, and where
public wording should be weakened or clarified when evidence is incomplete.

## Status Boundary

- Source-checked means public-source-backed and structurally validated.
- Expert-review-needed means qualified reviewers have not completed review.
- Expert-reviewed must wait for completed reviewer comments and a follow-up
  artifact update.

## Target Artifacts

| Artifact | Current Status | Review Goal |
| --- | --- | --- |
| `bcma-antigen-escape-claim-set-v0` | source-checked | Review claim scope, evidence level, measurement assumptions, safety language, and unsupported inference. |
| `bcma-antigen-escape-evidence-gap-register-v0` | source-checked | Review whether gaps and next actions are the right public work queue for the current evidence. |
| `bcma-measurement-context-audit-v0` | source-checked | Review whether the measurement-context fields are sufficient before stronger claims are attempted. |
| `post-car-t-relapse-mechanism-coverage-v0` | source-checked | Review whether coverage gaps are framed as artifact gaps rather than mechanism rankings. |

## Review Items

| Review Item | Focus | Linked Claims | Linked Gaps | Action |
| --- | --- | --- | --- | --- |
| `target-status-claim-scope-review-v0` | claim scope | `bcma-target-presence-should-be-extracted-v0` | `bcma-escape-frequency-denominator-gap-v0`, `bcma-measurement-context-completeness-gap-v0`, `expert-review-readiness-gap-v0` | Confirm or weaken target-status claim boundaries. |
| `tnfrsf17-loss-biomarker-review-v0` | measurement assumptions | `tnfrsf17-loss-is-trackable-escape-signal-v0` | `bcma-escape-frequency-denominator-gap-v0`, `bcma-measurement-context-completeness-gap-v0`, `expert-review-readiness-gap-v0` | Review whether biomarker language should remain source-specific or weaken further. |
| `sema4a-translation-boundary-review-v0` | translation boundary | `low-bcma-density-supports-alternate-target-research-tracking-v0` | `alternate-target-clinical-translation-gap-v0`, `bcma-measurement-context-completeness-gap-v0`, `expert-review-readiness-gap-v0` | Confirm SEMA4A remains alternate-target research context only. |
| `multifactorial-resistance-scope-review-v0` | unsupported inference | `bcma-resistance-is-multifactorial-v0` | `non-antigen-loss-relapse-buckets-gap-v0`, `expert-review-readiness-gap-v0` | Review multifactorial framing without mechanism ranking. |
| `public-language-safety-review-v0` | public readability | all four BCMA claim IDs | `expert-review-readiness-gap-v0` | Check that public readers will not mistake claims for guidance. |

## Reviewer Questions

### Claim Scope

- Are claims limited to public research extraction and mapping?
- Does any wording imply patient-level interpretation?
- Should any claim be weakened before it appears in a public explainer?

### Measurement Assumptions

- Are assay method, specimen source, timing, threshold, paired-measurement, and
  denominator fields sufficient?
- Which measurement fields are minimum viable before comparison?
- Which missing fields should block stronger claims?

### Source Quality

- Are review articles, public abstracts, and observational findings labeled
  with the right evidence level?
- Which claims require full-text appraisal before public education use?
- Which claims need additional primary sources?

### Translation And Safety Boundary

- Are preclinical and translational signals kept separate from clinical
  efficacy?
- Is normal-tissue safety context separate from clinical safety?
- Are trial-registry and protocol boundaries clear?

### Public Language

- Would a patient, advocate, or builder mistake any claim for medical advice?
- Are unsupported treatment, diagnostic, trial, safety, frequency, and cure
  inferences blocked?
- Are source-checked and expert-reviewed statuses visibly distinct?

## Completion Gate

- At least one qualified reviewer must complete each review item before any
  target artifact is labeled expert-reviewed.
- Reviewer comments must map back to claim IDs, gap IDs, source IDs,
  measurement term IDs, and extraction record IDs.
- Any claim-strength increase requires explicit reviewer support and a
  follow-up pull request.
- Any incomplete evidence should weaken or clarify public wording rather than
  strengthen it.

## Structured Data

- JSON: [`bcma-claim-set-expert-review-packet-v0.json`](bcma-claim-set-expert-review-packet-v0.json)
- Metadata: [`bcma-claim-set-expert-review-packet-v0.metadata.json`](bcma-claim-set-expert-review-packet-v0.metadata.json)

