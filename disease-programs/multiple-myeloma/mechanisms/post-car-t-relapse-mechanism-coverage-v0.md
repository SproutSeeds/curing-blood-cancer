# Post-CAR T Relapse Mechanism Coverage Report v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `post-car-t-relapse-mechanism-map-v0`
- linked gap: `non-antigen-loss-relapse-buckets-gap-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

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
| BCMA antigen loss, low density, or target alteration | 5 | 4 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| CAR T fitness, exhaustion, expansion, or persistence | 5 | 2 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Plasma-cell identity or lineage-state escape | 5 | 2 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Disease burden, site, and high-risk context | 8 | 2 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Sequential or dual-target immune pressure | 5 | 3 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |
| Measurement and follow-up gaps | 7 | 6 | covered-for-v0-navigation | Use for navigation only; do not rank biological importance from counts. |

## Under-Covered Buckets

### Needs Second Source Extraction

No mechanism buckets currently need first extraction or second-source
extraction for v0 navigation. This does not mean the mechanism map is complete
or that buckets can be ranked; it only means every current bucket has at least
two public extraction records or a documented interpretation boundary.

### Second-Source Coverage Added

- `disease-burden-site-risk-context-v0`
  - current public extractions:
    `tedder-bhutani-2025-disease-context-v0`,
    `nci-pdq-2025-disease-context-v0`
  - note: NCI PDQ supports disease-burden, site, high-risk, disease-state, and
    prior-therapy context fields, not causal relapse-mechanism claims,
    eligibility guidance, treatment guidance, or patient-specific risk
    interpretation

- `plasma-cell-identity-or-lineage-state-escape-v0`
  - current public extractions:
    `maura-2025-plasma-cell-identity-escape-v0`,
    `di-meo-2025-target-linked-phenotype-v0`
  - note: Di Meo 2025 supports target-linked phenotype field coverage, not a
    harmonized lineage-state ontology or clinical target-readiness claim

- `car-t-fitness-exhaustion-persistence-v0`
  - current public extractions: `ledergor-2024-cd4-car-t-exhaustion-v0`,
    `yue-2025-bcma-resistance-review-v0`
  - note: Yue 2025 is review-level category coverage for T-cell-driven and
    immune tumor microenvironment resistance framing; it is not cohort-level
    measurement evidence

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
