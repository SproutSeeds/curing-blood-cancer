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
| `disease-burden-site-risk-context-first-extraction-task-v0` | medium | done | [#16](https://github.com/SproutSeeds/curing-blood-cancer/issues/16) | `non-antigen-loss-relapse-buckets-gap-v0` | `disease-burden-site-risk-context-v0` |
| `plasma-cell-identity-second-source-extraction-task-v0` | high | done | pending | `non-antigen-loss-relapse-buckets-gap-v0` | `plasma-cell-identity-or-lineage-state-escape-v0` |
| `disease-burden-site-risk-context-second-source-extraction-task-v0` | medium | done | pending | `non-antigen-loss-relapse-buckets-gap-v0` | `disease-burden-site-risk-context-v0` |

## Issue Drafts

- [CAR T fitness second-source extraction](issue-drafts/car-t-fitness-second-source-extraction-task-v0.md)
- [Plasma-cell identity first extraction](issue-drafts/plasma-cell-identity-first-extraction-task-v0.md)
- [Disease burden, site, and risk-context first extraction](issue-drafts/disease-burden-site-risk-context-first-extraction-task-v0.md)
- [Plasma-cell identity second-source extraction](issue-drafts/plasma-cell-identity-second-source-extraction-task-v0.md)
- [Disease burden, site, and risk-context second-source extraction](issue-drafts/disease-burden-site-risk-context-second-source-extraction-task-v0.md)

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

The coverage report now has second-source coverage from
`maura-2025-plasma-cell-identity-escape-v0` and
`di-meo-2025-target-linked-phenotype-v0`.

Di Meo 2025 supports target-linked phenotype field coverage. It should not be
treated as a harmonized lineage-state ontology or a clinical target-readiness
claim.

Candidate public source anchors:

- `pubmed_yue_2025_bcma_resistance`

### Disease Burden, Site, And High-Risk Context

The coverage report now has second-source context-field coverage from
`tedder-bhutani-2025-disease-context-v0` and
`nci-pdq-2025-disease-context-v0`.

NCI PDQ supports disease-burden, site, high-risk, disease-state, and
prior-therapy context labels. It should not be treated as causal relapse
evidence, patient-specific risk guidance, treatment guidance, trial guidance,
eligibility guidance, efficacy evidence, or safety evidence.

Candidate public source anchors:

- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `pubmed_tedder_bhutani_2025_bcma_resistance`

## Structured Data

- JSON: [`post-car-t-relapse-mechanism-gap-public-task-queue-v0.json`](post-car-t-relapse-mechanism-gap-public-task-queue-v0.json)
- Metadata: [`post-car-t-relapse-mechanism-gap-public-task-queue-v0.metadata.json`](post-car-t-relapse-mechanism-gap-public-task-queue-v0.metadata.json)

## Next Work

- Current ready second-source extraction tasks are complete for v0 navigation.
- Refresh the coverage report after each accepted extraction.
- Use `make list-public-tasks ARGS="--status ready"` and
  `make list-mechanism-coverage ARGS="--under-covered"` before creating the
  next explicit schema, tooling, or deeper extraction task instead of adding
  ad hoc extraction siblings.
