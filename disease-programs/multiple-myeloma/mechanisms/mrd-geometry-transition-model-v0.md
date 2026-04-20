# MRD Geometry Transition Model v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent phase plan: `mrd-resistance-geometry-phase-plan-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This model defines how the MRD geometry is allowed to move.

Allowed movement is structural: coverage movement, weakening, splitting,
source-bounded context linking, claim blocking, retaining a source-bounded
state, or routing back to source extraction.

## Allowed Transition Types

| Transition Type | Meaning |
| --- | --- |
| `coverage-status-movement` | Artifact coverage only; not evidence strength or clinical readiness. |
| `weaken-edge` | Weakening is structural and cannot become clinical negative evidence. |
| `split-node` | Splitting improves source traceability and does not rank branches. |
| `merge-linked-context` | Merge is structural context linking only, not claim strengthening. |
| `block-claim` | Unsafe claim remains blocked. |
| `retain-source-bounded-state` | No claim upgrade. |
| `route-to-source-extraction` | Routes work to source extraction instead of inference. |

## Forbidden Transitions

- artifact coverage to clinical readiness.
- source signal to patient-specific MRD interpretation.
- pathway context to target selection.
- high-risk context to personal prognosis.
- therapy-pressure context to treatment sequencing.
- hypothesis candidate to treatment advice.
- geometry movement to cure claim.

## Structured Data

- JSON: [`mrd-geometry-transition-model-v0.json`](mrd-geometry-transition-model-v0.json)
- Metadata: [`mrd-geometry-transition-model-v0.metadata.json`](mrd-geometry-transition-model-v0.metadata.json)
