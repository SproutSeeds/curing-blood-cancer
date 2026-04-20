# MRD Resistance Geometry Second-Source Task Queue v0

Stewarded by [frg.earth](https://frg.earth/).

This queue turns the under-covered buckets in the MRD Resistance Geometry
Coverage Report into contribution-ready public source-extraction tasks.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a patient-specific MRD interpretation.
- Not a claim that multiple myeloma has been cured.
- Coverage status is public artifact coverage, not biological priority,
  evidence strength, clinical readiness, or mechanism frequency.

## Source Artifact

- [MRD Resistance Geometry Coverage Report v0](../mechanisms/mrd-resistance-geometry-coverage-v0.md)

## Task Status

| Task ID | Priority | Status | Linked Gap | Mechanism Bucket |
| --- | --- | --- | --- | --- |
| `mrd-trajectory-second-source-extraction-task-v0` | high | done | `non-antigen-loss-relapse-buckets-gap-v0` | `mrd-trajectory-split-v0` |
| `residual-transcriptional-adaptation-second-source-extraction-task-v0` | high | done | `non-antigen-loss-relapse-buckets-gap-v0` | `residual-transcriptional-adaptation-v0` |
| `genetic-nongenetic-coupling-second-source-extraction-task-v0` | high | done | `non-antigen-loss-relapse-buckets-gap-v0` | `genetic-nongenetic-coupling-v0` |
| `metabolic-resistance-state-second-source-extraction-task-v0` | medium | ready | `non-antigen-loss-relapse-buckets-gap-v0` | `metabolic-resistance-state-v0` |
| `nfkb-selective-state-second-source-extraction-task-v0` | medium | ready | `non-antigen-loss-relapse-buckets-gap-v0` | `nfkb-selective-state-v0` |
| `subclone-diversity-second-source-extraction-task-v0` | medium | ready | `non-antigen-loss-relapse-buckets-gap-v0` | `subclone-diversity-v0` |
| `single-cell-translation-gap-second-source-extraction-task-v0` | medium | ready | `expert-review-readiness-gap-v0` | `single-cell-translation-gap-v0` |
| `t-cell-therapy-pressure-second-source-extraction-task-v0` | medium | ready | `non-antigen-loss-relapse-buckets-gap-v0` | `t-cell-therapy-pressure-v0` |
| `unmet-high-risk-context-second-source-extraction-task-v0` | medium | ready | `non-antigen-loss-relapse-buckets-gap-v0` | `unmet-high-risk-context-v0` |

## Issue Drafts

- [MRD trajectory second-source extraction](issue-drafts/mrd-trajectory-second-source-extraction-task-v0.md)
- [Residual transcriptional adaptation second-source extraction](issue-drafts/residual-transcriptional-adaptation-second-source-extraction-task-v0.md)
- [Genetic/nongenetic coupling second-source extraction](issue-drafts/genetic-nongenetic-coupling-second-source-extraction-task-v0.md)
- [Metabolic resistance state second-source extraction](issue-drafts/metabolic-resistance-state-second-source-extraction-task-v0.md)
- [NF-kB selective state second-source extraction](issue-drafts/nfkb-selective-state-second-source-extraction-task-v0.md)
- [Subclone diversity second-source extraction](issue-drafts/subclone-diversity-second-source-extraction-task-v0.md)
- [Single-cell translation gap second-source extraction](issue-drafts/single-cell-translation-gap-second-source-extraction-task-v0.md)
- [T-cell therapy pressure second-source extraction](issue-drafts/t-cell-therapy-pressure-second-source-extraction-task-v0.md)
- [Unmet high-risk context second-source extraction](issue-drafts/unmet-high-risk-context-second-source-extraction-task-v0.md)

## Completed Work

| Task ID | Completed By | Coverage Effect |
| --- | --- | --- |
| `mrd-trajectory-second-source-extraction-task-v0` | `martinez-lopez-2020-mrd-dynamics-geometry-v0` | `mrd-trajectory-split-v0` is now `covered-for-v0-navigation`. |
| `residual-transcriptional-adaptation-second-source-extraction-task-v0` | `cohen-2021-resistance-single-cell-geometry-v0` | `residual-transcriptional-adaptation-v0` is now `covered-for-v0-navigation`. |
| `genetic-nongenetic-coupling-second-source-extraction-task-v0` | `cohen-2021-resistance-single-cell-geometry-v0` | `genetic-nongenetic-coupling-v0` is now `covered-for-v0-navigation`. |

## Priority Order

1. Metabolic and NF-kB selective-state buckets, because they test whether
   pathway-state branches should remain separate or fold into residual state.
2. Therapy pressure and high-risk context, because they protect the map from
   pretending all relapse settings are comparable.
3. Subclone diversity, because it tests whether clone architecture needs more
   explicit branching before internal adversarial review.
4. Single-cell translation gap, because it keeps research-tooling resolution
   separate from clinical readiness.

## Structured Data

- JSON: [`mrd-resistance-geometry-second-source-task-queue-v0.json`](mrd-resistance-geometry-second-source-task-queue-v0.json)
- Metadata: [`mrd-resistance-geometry-second-source-task-queue-v0.metadata.json`](mrd-resistance-geometry-second-source-task-queue-v0.metadata.json)

## Next Work

- Select the first metabolic or NF-kB selective-state source.
- Add a source-registry record for the chosen source if needed.
- Add one source-specific mechanism extraction for
  `metabolic-resistance-state-v0` or `nfkb-selective-state-v0`.
- Refresh the MRD Resistance Geometry Coverage Report after each accepted
  extraction.
