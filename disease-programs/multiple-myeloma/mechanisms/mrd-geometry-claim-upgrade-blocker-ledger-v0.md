# MRD Geometry Claim Upgrade Blocker Ledger v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent phase plan: `mrd-resistance-geometry-phase-plan-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This ledger records what would have to be true before any MRD resistance
geometry language could move beyond research-map navigation. Phase 5 does not
upgrade any claim. It makes the blockers explicit so the system can keep moving
without accidentally turning structure into advice.

## Boundary

- No patient-specific MRD interpretation.
- No relapse or prognosis forecast.
- No monitoring recommendation.
- No treatment, target, supplement, product, sequence, or trial guidance.
- No mechanism ranking or evidence ranking.
- No clinical validation claim.
- No cure claim.

## Blocker Table

| Blocker ID | Current Status | Blocked Output | Evidence Required Before Upgrade |
| --- | --- | --- | --- |
| `residual-state-actionability-claim-block-v0` | blocked | residual-state actionability | source-aligned residual-state measurements, independent replication, method context, contradiction review, and clinical validation design |
| `nfkb-target-selection-claim-block-v0` | blocked | NF-kB target selection | primary source extraction tied to the exact residual setting, intervention evidence, safety context, and expert review |
| `metabolic-intervention-claim-block-v0` | blocked | metabolic intervention or supplement guidance | primary residual-state evidence, intervention-specific data, safety evidence, and nonclinical-to-clinical translation review |
| `subclone-prognosis-claim-block-v0` | blocked | prognosis from subclone diversity | aligned genomic methods, longitudinal outcome design, external validation, and patient-level calibration review |
| `car-t-pressure-sequencing-claim-block-v0` | blocked | CAR T or immune therapy sequencing | comparative therapy evidence, product and target context, eligibility and safety review, and clinical guideline appraisal |
| `mrd-trajectory-relapse-risk-claim-block-v0` | blocked | relapse-risk forecast from MRD trajectory | assay-aligned serial MRD evidence, threshold context, specimen context, model validation, and clinical calibration |
| `geometry-clinical-validation-claim-block-v0` | blocked | clinical validation of the geometry | prespecified validation protocol, external datasets, locked outputs, error analysis, and expert review |
| `cure-claim-block-v0` | blocked | cure claim | durable outcome evidence, subtype scope, treatment context, time horizon, independent review, and explicit uncertainty |

## Current Decision

All blocker rows remain blocked. The geometry can become more structured,
more source-backed, and more testable, but it cannot become clinical guidance
from artifact coverage counts.

## Structured Data

- JSON: [`mrd-geometry-claim-upgrade-blocker-ledger-v0.json`](mrd-geometry-claim-upgrade-blocker-ledger-v0.json)
- Metadata: [`mrd-geometry-claim-upgrade-blocker-ledger-v0.metadata.json`](mrd-geometry-claim-upgrade-blocker-ledger-v0.metadata.json)
