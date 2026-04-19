# Add A Second Public Source Extraction For Unmet High-Risk Context

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, patient-specific interpretation, or a cure
claim.

## Why This Matters

The geometry pilot uses high-risk and unmet-need context to keep relapse maps
from pretending all disease settings are comparable. This context needs a
second source before comparison.

## Public Source Anchors

- `pubmed`
- `pubmed_besliu_2025_evolving_landscape_myeloma`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `unmet-high-risk-context-v0`.
- Preserve disease context, risk context, subtype scope, and source
  limitations.
- Refresh `mrd-resistance-geometry-coverage-v0`.

## Acceptance Checks

- `python3 tools/validate_public_artifacts.py` passes.
- The selected source supports high-risk, extramedullary, plasma cell leukemia,
  or related unmet-need context.
- Context variables are not treated as causal mechanisms unless the source
  explicitly supports that interpretation.

## Do Not Infer

- Do not infer patient-specific prognosis.
- Do not recommend treatment or trial options for high-risk contexts.
- Do not compare high-risk contexts without aligned source definitions.
