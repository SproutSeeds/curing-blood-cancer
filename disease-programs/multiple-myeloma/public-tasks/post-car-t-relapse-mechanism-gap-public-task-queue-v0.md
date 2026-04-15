# Post-CAR T Relapse Mechanism Gap Public Task Queue v0

Stewarded by [frg.earth](https://frg.earth/).

This queue turns the under-covered buckets in the Post-CAR T Relapse Mechanism
Coverage Report into contribution-ready public source-extraction tasks.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a claim that multiple myeloma has been cured.
- Coverage status is public artifact coverage, not biological priority,
  evidence strength, or mechanism frequency.

## Source Artifact

- [Post-CAR T Relapse Mechanism Coverage Report v0](../mechanisms/post-car-t-relapse-mechanism-coverage-v0.md)

## Task Status

| Task ID | Priority | Status | GitHub Issue | Linked Gap | Mechanism Bucket |
| --- | --- | --- | --- | --- | --- |
| `car-t-fitness-second-source-extraction-task-v0` | high | done | [#15](https://github.com/SproutSeeds/curing-blood-cancer/issues/15) | `non-antigen-loss-relapse-buckets-gap-v0` | `car-t-fitness-exhaustion-persistence-v0` |
| `plasma-cell-identity-first-extraction-task-v0` | high | done | [#14](https://github.com/SproutSeeds/curing-blood-cancer/issues/14) | `non-antigen-loss-relapse-buckets-gap-v0` | `plasma-cell-identity-or-lineage-state-escape-v0` |
| `disease-burden-site-risk-context-first-extraction-task-v0` | medium | ready | [#16](https://github.com/SproutSeeds/curing-blood-cancer/issues/16) | `non-antigen-loss-relapse-buckets-gap-v0` | `disease-burden-site-risk-context-v0` |

## Issue Drafts

- [CAR T fitness second-source extraction](issue-drafts/car-t-fitness-second-source-extraction-task-v0.md)
- [Plasma-cell identity first extraction](issue-drafts/plasma-cell-identity-first-extraction-task-v0.md)
- [Disease burden, site, and risk-context first extraction](issue-drafts/disease-burden-site-risk-context-first-extraction-task-v0.md)

## Task Notes

### CAR T Fitness, Exhaustion, Expansion, Or Persistence

The coverage report now has second-source coverage from
`ledergor-2024-cd4-car-t-exhaustion-v0` and
`yue-2025-bcma-resistance-review-v0`.

Yue 2025 is review-level category coverage for T-cell-driven factors and
immune tumor microenvironment framing. It should not be treated as a
cohort-level measurement source.

Remaining public source anchor for deeper expansion:

- `pubmed_tedder_bhutani_2025_bcma_resistance`

### Plasma-Cell Identity Or Lineage-State Escape

The coverage report now has first-extraction coverage from
`maura-2025-plasma-cell-identity-escape-v0`. The next step is a second
source-specific extraction before any cross-source comparison.

Candidate public source anchors:

- `pubmed_di_meo_2025_sema4a_low_bcma`
- `pubmed_yue_2025_bcma_resistance`

### Disease Burden, Site, And High-Risk Context

The coverage report currently has no extracted signals for this bucket. The
next task adds a first public extraction for context fields that should travel
with relapse-mechanism interpretation.

Candidate public source anchors:

- `nci_pdq_myeloma_hp`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed_tedder_bhutani_2025_bcma_resistance`

## Structured Data

- JSON: [`post-car-t-relapse-mechanism-gap-public-task-queue-v0.json`](post-car-t-relapse-mechanism-gap-public-task-queue-v0.json)
- Metadata: [`post-car-t-relapse-mechanism-gap-public-task-queue-v0.metadata.json`](post-car-t-relapse-mechanism-gap-public-task-queue-v0.metadata.json)

## Next Work

- Work the linked public issues one source-specific extraction at a time.
- Refresh the coverage report after each accepted extraction.
