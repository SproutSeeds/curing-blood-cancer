# Clone-State Coupling Contradiction Mining Note v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent proof plan: `mrd-resistance-geometry-proof-plan-v0`
- source task: `clone-state-coupling-contradiction-mining-task-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This note tests whether clone-state coupling survives contradiction pressure
without becoming causal ranking, mechanism dominance, or patient-specific
resistance attribution.

## Sources Tested

| Source | Extraction Record | Frame |
| --- | --- | --- |
| `pubmed_cui_2024_mrd_clonal_evolution` | `cui-2024-mrd-clonal-evolution-geometry-v0` | genetic and nongenetic coupling in therapy-induced clonal evolution |
| `pubmed_cohen_2021_resistance_single_cell` | `cohen-2021-resistance-single-cell-geometry-v0` | transcriptional clone and resistant-state context |
| `pubmed_li_2025_single_cell_myeloma_review` | `li-2025-single-cell-myeloma-geometry-v0` | review-level subclone diversity and single-cell context |

## Contradiction Result

Status: `pass-with-provisional-edge-only`

The coupling survives as an edge, not as a merged axis.

The current sources support keeping clone architecture and residual biological
state linked, but the link must remain source-specific and provisional:

- clone identity, clone architecture, transcriptional state, therapy exposure,
  and sample timing remain separate fields
- review-level subclone diversity remains separate from cohort-level clone
  measurement
- correlation language must not become causality or clinical actionability

## Movement Decision

| Field | Decision |
| --- | --- |
| geometry element | `clone-state-coupling-edge-axis-v0` |
| decision | keep provisional edge |
| edge status | `source-specific; split-ready` |
| required movement | split into clone-inference and transcriptional-state subedges if future contradiction weakens the edge |
| proof test | `structural-separability-test-v0`; `contradiction-response-test-v0`; `safety-invariance-test-v0` |

## Blocked Inferences

- No causal ranking.
- No genetic-versus-nongenetic dominance claim.
- No patient-specific resistance attribution.
- No prognosis.
- No target selection.
- No treatment recommendation.
- No cure claim.

## Next Work

- Record this decision in `mrd-resistance-geometry-movement-ledger-v0`.
- Keep the coupling edge provisional in future axis revisions.
- Add a separate subclone-diversity second-source extraction before using
  subclone diversity as more than review-level context.

## Structured Data

- JSON: [`clone-state-coupling-contradiction-mining-note-v0.json`](clone-state-coupling-contradiction-mining-note-v0.json)
- Metadata: [`clone-state-coupling-contradiction-mining-note-v0.metadata.json`](clone-state-coupling-contradiction-mining-note-v0.metadata.json)
