# Post-CAR T Relapse Mechanism Coverage Report v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `post-car-t-relapse-mechanism-map-v0`
- linked gap: `non-antigen-loss-relapse-buckets-gap-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-14`

## Purpose

This report counts the current public extraction records and extracted signals
by post-CAR T relapse mechanism bucket.

It exists so the public roadmap does not mistake the bucket with the cleanest
structured artifacts for the most biologically important bucket.

## Boundary

- Coverage counts are public artifact coverage metrics only.
- Coverage counts are not evidence-strength rankings.
- Coverage counts are not mechanism-frequency estimates.
- Coverage counts are not biological-importance rankings.
- Under-covered means more extraction is needed before comparison; it does not
  mean low priority or low importance.
- This report is not medical advice, diagnostic guidance, treatment guidance,
  trial guidance, or a cure claim.

## Coverage Table

| Mechanism Bucket | Signals | Extraction Records | Status | Next Extraction Need |
| --- | ---: | ---: | --- | --- |
| BCMA antigen loss, low density, or target alteration | 4 | 3 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| CAR T fitness, exhaustion, expansion, or persistence | 3 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |
| Plasma-cell identity or lineage-state escape | 2 | 1 | needs-second-source-extraction | Add at least one additional public source extraction before comparison. |
| Disease burden, site, and high-risk context | 0 | 0 | needs-first-extraction | Add the first source-specific extraction. |
| Sequential or dual-target immune pressure | 5 | 3 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Measurement and follow-up gaps | 6 | 5 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |

## Under-Covered Buckets

### Needs First Extraction

- `disease-burden-site-risk-context-v0`
  - public source anchors: `nci_pdq_myeloma_hp`, `clinicaltrials_gov`,
    `clinicaltrials_gov_api_v2`,
    `pubmed_tedder_bhutani_2025_bcma_resistance`
  - next step: create a source-specific extraction for baseline burden,
    disease site, high-risk context, and prior-exposure fields

### Needs Second Source Extraction

- `car-t-fitness-exhaustion-persistence-v0`
  - current public extraction: `ledergor-2024-cd4-car-t-exhaustion-v0`
  - public source anchors for expansion:
    `pubmed_tedder_bhutani_2025_bcma_resistance`,
    `pubmed_yue_2025_bcma_resistance`
  - next step: add at least one additional source-specific extraction before
    comparing immune fitness, exhaustion, persistence, or expansion signals
- `plasma-cell-identity-or-lineage-state-escape-v0`
  - current public extraction:
    `maura-2025-plasma-cell-identity-escape-v0`
  - public source anchors for expansion:
    `pubmed_yue_2025_bcma_resistance`,
    `pubmed_di_meo_2025_sema4a_low_bcma`
  - next step: add at least one additional source-specific extraction before
    comparing identity or lineage-state evidence across sources

## Reproduce

Run:

```bash
make list-mechanism-coverage
```

Machine-readable report:

```bash
make list-mechanism-coverage ARGS="--json"
```

Under-covered buckets only:

```bash
make list-mechanism-coverage ARGS="--under-covered"
```

Structured data:

- JSON: [`post-car-t-relapse-mechanism-coverage-v0.json`](post-car-t-relapse-mechanism-coverage-v0.json)
- Metadata: [`post-car-t-relapse-mechanism-coverage-v0.metadata.json`](post-car-t-relapse-mechanism-coverage-v0.metadata.json)
