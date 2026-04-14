# Evidence Claim Schema v0

- schema id: `evidence-claim.schema.json`
- date: `2026-04-14`
- scope: public Curing Blood Cancer evidence and hypothesis claims

## Purpose

This schema makes public claims harder to overstate. Every claim must identify
what kind of claim it is, which blood-cancer subtype it applies to, what
evidence level supports it, which source IDs support it, where uncertainty
remains, and why it should not be used as clinical advice.

## Files

- [Evidence Claim JSON Schema](./evidence-claim.schema.json)
- [Evidence Claim Template v0](./evidence-claim-template-v0.json)
- [Evidence Claim Example v0](./evidence-claim-example-v0.json)

## Required Fields

| Field | Purpose |
| --- | --- |
| `claim_id` | Stable local ID for citation and updates. |
| `claim_text` | The exact public claim being made. |
| `claim_kind` | Type of claim, such as mechanism, biomarker, trial landscape, cure hypothesis, or vaccine hypothesis. |
| `claim_status` | Whether the statement is a fact, derived claim, hypothesis, open question, or do-not-use-clinically item. |
| `blood_cancer_scope` | Subtype, disease state, population scope, and excluded scope. |
| `evidence_level` | Source-summary, registry, regulatory, clinical-trial, systematic-review, preclinical, or hypothesis-only level. |
| `source_ids` | Stable IDs from the source registry. |
| `clinical_use_boundary` | Explicit public safety boundary. |
| `uncertainty` | Known unknowns and possible failure modes. |
| `limitations` | Plain-language limits. |
| `review` | Created date, last reviewed date, and review status. |

## Use Rules

- Use `cure-hypothesis` or `vaccine-hypothesis` only when uncertainty is
  explicit.
- Use `do-not-use-clinically` when a claim could be misunderstood as clinical
  guidance.
- Use source IDs from [Source Registry v0](../sources/source-registry-v0.md).
- Use taxonomy class IDs when claims refer to a stable treatment class.
- Never use a valid schema record as proof that a claim is true.
- Expert review should be recorded in `review`, not implied by confident prose.
