# MRD Resistance Geometry Coverage Report v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `mrd-resistance-geometry-pilot-v0`
- linked gaps: `non-antigen-loss-relapse-buckets-gap-v0`, `expert-review-readiness-gap-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-19`

## Purpose

This report counts the current public extraction records and extracted signals
by MRD Resistance Geometry Pilot mechanism bucket.

It exists so the geometry map can become a research instrument: the map should
show which nodes are source-backed enough for v0 navigation, which nodes still
need second-source extraction, and which nodes must not be treated as clinical
or educational claims yet.

## Boundary

- Coverage counts are public artifact coverage metrics only.
- Coverage counts are not evidence-strength rankings.
- Coverage counts are not mechanism-frequency estimates.
- Coverage counts are not biological-importance rankings.
- Covered-for-v0-navigation does not mean clinically ready.
- Needs-second-source-extraction means more source extraction is needed before
  comparison; it does not mean low priority or low importance.
- This report is not medical advice, diagnostic guidance, treatment guidance,
  trial guidance, patient-specific MRD interpretation, or a cure claim.

## Coverage Table

| Geometry Bucket | Signals | Extraction Records | Status | Next Extraction Need |
| --- | ---: | ---: | --- | --- |
| MRD trajectory split | 2 | 2 | covered-for-v0-navigation | Use for navigation only; do not infer patient-specific MRD meaning from counts. |
| Residual transcriptional adaptation | 2 | 2 | covered-for-v0-navigation | Use for navigation only; do not infer treatment selection or patient-specific MRD meaning from counts. |
| Metabolic resistance state | 2 | 2 | covered-for-v0-navigation | Use for navigation only; do not infer intervention, biomarker, prognosis, or actionability meaning from counts. |
| NF-kB selective state | 2 | 2 | covered-for-v0-navigation | Use for navigation only; do not infer target selection, pathway ranking, prognosis, or actionability meaning from counts. |
| Genetic and nongenetic coupling | 2 | 2 | covered-for-v0-navigation | Use for navigation only; keep clone identity and transcriptional state as separate linked fields. |
| Tumor microenvironment shelter interactions | 2 | 2 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Subclone diversity | 1 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |
| Single-cell translation gap | 1 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |
| T-cell therapy pressure | 1 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |
| Unmet high-risk context | 1 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |

## Summary

- Mechanism buckets: `10`
- Current source-specific extraction records: `7`
- Current extracted signals: `16`
- Buckets needing first extraction: `0`
- Buckets needing second-source extraction: `4`
- Buckets covered for v0 navigation: `6`

## What The Report Says

The geometry pilot now has a first extraction for every bucket. That is enough
to navigate the map, but not enough to compare most nodes.

Six buckets currently have at least two extraction records:

| Bucket | Current Extraction Records |
| --- | --- |
| `mrd-trajectory-split-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `martinez-lopez-2020-mrd-dynamics-geometry-v0` |
| `residual-transcriptional-adaptation-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `cohen-2021-resistance-single-cell-geometry-v0` |
| `metabolic-resistance-state-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `wang-2025-lipid-metabolism-geometry-v0` |
| `nfkb-selective-state-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `lu-2024-signaling-pathways-geometry-v0` |
| `genetic-nongenetic-coupling-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `cohen-2021-resistance-single-cell-geometry-v0` |
| `tme-shelter-interactions-v0` | `cui-2024-mrd-clonal-evolution-geometry-v0`; `li-2025-single-cell-myeloma-geometry-v0` |

That does not mean these nodes are more important than other nodes. It means
they currently have the cleanest public artifact coverage.

## Under-Covered Buckets

The following buckets need second-source extraction before comparison:

- `subclone-diversity-v0`
- `single-cell-translation-gap-v0`
- `t-cell-therapy-pressure-v0`
- `unmet-high-risk-context-v0`

## Next Extraction Needs

The metabolic and NF-kB second-source records are now complete for v0
navigation only. The review-level second sources do not upgrade either pathway
branch into actionability, biomarker, treatment, or target evidence.

Prioritize the remaining second-source records in this order:

1. Therapy pressure and high-risk context, because they protect the map from
   pretending all relapse settings are comparable.
2. Subclone diversity, because it tests whether clone architecture needs more
   explicit branching before internal adversarial review.
3. Single-cell translation gap, because it keeps the research-tooling layer
   separate from clinical readiness.

## Structured Data

- JSON: [`mrd-resistance-geometry-coverage-v0.json`](mrd-resistance-geometry-coverage-v0.json)
- Metadata: [`mrd-resistance-geometry-coverage-v0.metadata.json`](mrd-resistance-geometry-coverage-v0.metadata.json)
