# Residual-State Contradiction Mining Note v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent proof plan: `mrd-resistance-geometry-proof-plan-v0`
- source task: `residual-state-contradiction-mining-task-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This note tests whether residual biological state survives contradiction
pressure as a usable geometry axis, or whether the axis is too broad and needs
internal substructure before the map can keep moving.

## Sources Tested

| Source | Extraction Record | Frame |
| --- | --- | --- |
| `pubmed_cui_2024_mrd_clonal_evolution` | `cui-2024-mrd-clonal-evolution-geometry-v0` | single-cell residual malignant plasma-cell state and pathway context |
| `pubmed_cohen_2021_resistance_single_cell` | `cohen-2021-resistance-single-cell-geometry-v0` | resistant transcriptional-state and clone-state coupling context |
| `pubmed_wang_2025_lipid_metabolism_myeloma` | `wang-2025-lipid-metabolism-geometry-v0` | review-level metabolic pathway context |
| `pubmed_lu_2024_myeloma_signaling_pathways` | `lu-2024-signaling-pathways-geometry-v0` | review-level NF-kB and signaling-pathway context |

## Contradiction Result

Status: `pass-with-substructure-required`

The axis survives, but only as an internally typed residual-state axis.

The contradiction pressure is useful: if we call everything "residual state,"
the geometry gets lazy. Transcriptional adaptation, metabolic context, NF-kB
pathway context, therapy pressure, microenvironment context, and clone-state
coupling are not the same object. They can sit near each other, but they must
not collapse into one untyped signal.

## Movement Decision

| Field | Decision |
| --- | --- |
| geometry element | `residual-biological-state-axis-v0` |
| decision | keep axis, require typed substructure |
| edge status | `source-bounded; split-ready` |
| required movement | no pathway, clone, therapy-pressure, or TME collapse |
| proof test | `structural-separability-test-v0`; `contradiction-response-test-v0`; `safety-invariance-test-v0` |

## Required Substructure

- `transcriptional-adaptation-state-v0`
- `metabolic-pathway-state-context-v0`
- `nfkb-pathway-state-context-v0`
- `clone-state-coupling-context-v0`
- `therapy-pressure-context-v0`
- `microenvironment-context-v0`
- `measurement-trajectory-context-v0`

These labels are research-map structure only. They are not biomarkers,
targets, treatments, intervention paths, or clinical outputs.

## Blocked Inferences

- No patient-specific residual-state interpretation.
- No pathway actionability.
- No target selection.
- No treatment or supplement suggestion.
- No MRD relapse-risk forecast.
- No mechanism ranking.
- No cure claim.

## Next Work

- Mark the residual-state contradiction task done.
- Keep future residual-state extractions typed by method, source frame, and
  therapy or sampling context.
- Use the claim-upgrade blocker ledger before any future language tries to turn
  a pathway/state label into a clinical claim.

## Structured Data

- JSON: [`residual-state-contradiction-mining-note-v0.json`](residual-state-contradiction-mining-note-v0.json)
- Metadata: [`residual-state-contradiction-mining-note-v0.metadata.json`](residual-state-contradiction-mining-note-v0.metadata.json)
