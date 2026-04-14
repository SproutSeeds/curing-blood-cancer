# BCMA Antigen Escape Public Task Queue v0

Stewarded by [frg.earth](https://frg.earth/).

This queue converts the BCMA antigen escape evidence gap register into
contribution-ready public tasks.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a claim that multiple myeloma has been cured.

## Ready Tasks

| Task ID | Priority | Issue Form | Linked Gap |
| --- | --- | --- | --- |
| `bcma-target-status-denominator-extraction-task-v0` | high | source extraction | `bcma-escape-frequency-denominator-gap-v0` |
| `bcma-measurement-context-field-audit-task-v0` | high | evidence gap | `bcma-measurement-context-completeness-gap-v0` |
| `sema4a-translation-safety-extraction-task-v0` | high | source extraction | `alternate-target-clinical-translation-gap-v0` |
| `non-antigen-loss-bucket-coverage-task-v0` | medium | evidence gap | `non-antigen-loss-relapse-buckets-gap-v0` |
| `bcma-claim-set-expert-review-task-v0` | medium | expert review | `expert-review-readiness-gap-v0` |

## Issue Drafts

- [Target-status denominator extraction](issue-drafts/bcma-target-status-denominator-extraction-task-v0.md)
- [Measurement-context field audit](issue-drafts/bcma-measurement-context-field-audit-task-v0.md)
- [SEMA4A translation and safety extraction](issue-drafts/sema4a-translation-safety-extraction-task-v0.md)
- [Non-antigen-loss bucket coverage](issue-drafts/non-antigen-loss-bucket-coverage-task-v0.md)
- [BCMA claim-set expert review](issue-drafts/bcma-claim-set-expert-review-task-v0.md)

## Structured Data

- JSON: [`bcma-antigen-escape-public-task-queue-v0.json`](bcma-antigen-escape-public-task-queue-v0.json)
- Metadata: [`bcma-antigen-escape-public-task-queue-v0.metadata.json`](bcma-antigen-escape-public-task-queue-v0.metadata.json)

## Next Work

- Open public GitHub issues from these drafts after the contributor intake kit
  is merged.
- Add issue URLs back into the structured task queue once issues exist.
- Add task queues for MRD endpoint definitions and non-BCMA relapse mechanisms.
