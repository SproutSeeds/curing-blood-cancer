# MRD Trajectory Contradiction Mining Note v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent proof plan: `mrd-resistance-geometry-proof-plan-v0`
- source task: `mrd-trajectory-contradiction-mining-task-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This note tests whether the MRD trajectory edge survives contradiction
pressure without collapsing measurement trajectory into residual biological
state.

## Sources Tested

| Source | Extraction Record | Frame |
| --- | --- | --- |
| `pubmed_cui_2024_mrd_clonal_evolution` | `cui-2024-mrd-clonal-evolution-geometry-v0` | single-cell residual clone and transcriptional-state context |
| `pubmed_martinez_lopez_2020_mrd_dynamics` | `martinez-lopez-2020-mrd-dynamics-geometry-v0` | serial NGS MRD dynamics context |

## Contradiction Result

Status: `pass-with-separation-required`

The edge survives only if the geometry keeps measurement trajectory separate
from residual biological state.

The two sources can both support `mrd-trajectory-split-v0` for v0 navigation,
but they are not interchangeable:

- Cui 2024 contributes single-cell residual malignant plasma-cell and
  transcriptional evolution context.
- Martinez-Lopez 2020 contributes serial MRD dynamics context using a different
  measurement frame.
- Assay method, specimen, threshold or sensitivity, source-defined timing, and
  cohort context must remain visible before comparison.

## Movement Decision

| Field | Decision |
| --- | --- |
| geometry element | `measurement-trajectory-axis-v0` |
| decision | keep axis, preserve assay-frame split |
| edge status | `source-bounded; comparison-provisional` |
| required movement | no merge with residual biological state |
| proof test | `structural-separability-test-v0`; `contradiction-response-test-v0`; `safety-invariance-test-v0` |

## Blocked Inferences

- No patient-specific MRD interpretation.
- No relapse forecast.
- No monitoring recommendation.
- No treatment recommendation.
- No assay or threshold ranking.
- No cure claim.

## Next Work

- Record this decision in `mrd-resistance-geometry-movement-ledger-v0`.
- Keep future MRD trajectory extractions source-frame specific.
- If a new source mixes assay method or residual-state biology, split the edge
  before using it for proof-readiness.

## Structured Data

- JSON: [`mrd-trajectory-contradiction-mining-note-v0.json`](mrd-trajectory-contradiction-mining-note-v0.json)
- Metadata: [`mrd-trajectory-contradiction-mining-note-v0.metadata.json`](mrd-trajectory-contradiction-mining-note-v0.metadata.json)
