# MRD Resistance Geometry Axis Revision Decision v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `mrd-resistance-geometry-pilot-v0`
- parent plan: `mrd-resistance-geometry-phase-plan-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-19`

## Purpose

This decision records the Phase 2 structural answer for the MRD Resistance
Geometry Pilot.

The question was whether residual disease should be mapped as clone
persistence, biological state adaptation, measurement trajectory, or a flexible
coupled system.

## Decision

Keep three axes separate:

- measurement trajectory
- biological residual state
- clone architecture

Add explicit coupling edges between clone architecture and transcriptional or
adaptive state.

This is the flexible structure that best preserves the source evidence so far.
It lets the geometry move without collapsing assay method, sampling time,
therapy exposure, clone identity, and cell state into one overloaded node.

## Why

The second-source pass separates the evidence frames:

| Evidence Frame | Source IDs | Extraction Records | Structural Implication |
| --- | --- | --- | --- |
| MRD measurement trajectory | `pubmed_cui_2024_mrd_clonal_evolution`; `pubmed_martinez_lopez_2020_mrd_dynamics` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `martinez-lopez-2020-mrd-dynamics-geometry-v0` | Keep measurement direction and assay method as their own axis. |
| Residual transcriptional state | `pubmed_cui_2024_mrd_clonal_evolution`; `pubmed_cohen_2021_resistance_single_cell` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `cohen-2021-resistance-single-cell-geometry-v0` | Keep residual-cell biology as its own axis. |
| Clone-state coupling | `pubmed_cui_2024_mrd_clonal_evolution`; `pubmed_cohen_2021_resistance_single_cell` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `cohen-2021-resistance-single-cell-geometry-v0` | Add coupling edges, but do not merge clone identity and state. |

## What Changes

- `residual-transcriptional-adaptation-v0` moves to
  `covered-for-v0-navigation`.
- `genetic-nongenetic-coupling-v0` moves to
  `covered-for-v0-navigation`.
- Phase 2 is done for v0.
- Phase 3 is ready to assemble an expert-review packet.

## What Does Not Change

- This is not medical advice.
- This is not diagnostic guidance.
- This is not treatment, monitoring, or trial guidance.
- This is not a patient-specific MRD interpretation.
- This does not rank resistance mechanisms by frequency, importance, evidence
  strength, or clinical actionability.
- This does not claim that multiple myeloma has been cured.

## Phase 3 Gate

Phase 3 can now ask expert reviewers a sharper question:

> Are measurement trajectory, residual biological state, clone architecture,
> and clone-state coupling named and bounded correctly for a public research
> geometry?

Until that review happens, the geometry remains source-checked and
expert-review-needed.

## Structured Data

- JSON: [`mrd-resistance-geometry-axis-revision-decision-v0.json`](mrd-resistance-geometry-axis-revision-decision-v0.json)
- Metadata: [`mrd-resistance-geometry-axis-revision-decision-v0.metadata.json`](mrd-resistance-geometry-axis-revision-decision-v0.metadata.json)
