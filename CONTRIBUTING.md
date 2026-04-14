# Contributing

Stewarded by [frg.earth](https://frg.earth/).

Thank you for helping improve the public Curing Blood Cancer artifact surface.
This repo is for source-backed public research tooling, not medical advice.

## What To Contribute

- source extractions from public, citable sources
- evidence gap tasks tied to existing gap IDs
- measurement definitions and missing-context notes
- schema, validator, and listing-tool improvements
- expert-review notes that tighten claims, uncertainty, or safety language
- documentation that makes public artifacts easier to inspect and reuse

## What Not To Contribute

- patient-identifying data
- private medical records
- portal exports
- credentials
- restricted or non-redistributable datasets
- patient-specific clinical interpretation
- treatment, diagnostic, or trial recommendations
- unsupported claims that a cure or vaccine has been found

## Before Opening An Issue

1. Check the relevant artifact:
   - [BCMA claim set](disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md)
   - [BCMA evidence gap register](disease-programs/multiple-myeloma/evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md)
   - [MRD and relapse measurement glossary](disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md)
2. Use the issue form that matches the work:
   - evidence gap task
   - source extraction task
   - expert review task
3. Include public source IDs, URLs, PMIDs, or registry IDs where available.
4. State what the source supports and what it does not support.

## Before Opening A Pull Request

Run:

```bash
make validate
```

When relevant, also run:

```bash
make list-claim-sets
make list-evidence-gaps
make list-mechanism-extractions
```

Every PR should preserve:

- source IDs
- disease scope
- measurement context
- evidence level
- uncertainty
- public safety boundaries

## Review Standard

Public biomedical claims should answer:

- What is the blood-cancer subtype and disease state?
- What exact source supports this?
- What evidence level is being used?
- What measurement context is required?
- What does this not prove?
- Who should review it before stronger public use?

Use [Claim Review Checklist v0](governance/CLAIM_REVIEW_CHECKLIST.md) for
claim, gap, mechanism, and measurement artifacts.
