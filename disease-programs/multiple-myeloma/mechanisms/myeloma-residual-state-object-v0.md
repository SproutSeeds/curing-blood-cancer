# Myeloma Residual State Object v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent axis revision: `mrd-resistance-geometry-axis-revision-v0`
- parent schema: `myeloma-state-object-schema-v0`
- data boundary: public-source-only; no real case data
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This object is the structured companion to the MRD Resistance Geometry Axis
Revision.

It gives the revised geometry a public-safe state pocket: measurement
trajectory, residual biological state, clone architecture, and clone-state
coupling can be represented together without merging them into one clinical or
patient-specific output.

## Boundary

- Public-source-only.
- No real case data.
- No patient identifiers.
- No private records.
- Not medical advice.
- Not diagnostic guidance.
- Not a monitoring recommendation.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a patient-specific MRD interpretation.
- Not a prognosis, resistance call, mechanism ranking, or cure claim.

## Required Families

| Family | Purpose | Boundary |
| --- | --- | --- |
| `source_context` | Carries source IDs, extraction records, assay context, specimen or model context, timepoint bucket, and provenance review status. | Missing source context blocks interpretation. |
| `measurement_trajectory_state` | Represents source-defined MRD and response trajectory labels as measurement context. | No relapse forecast, monitoring guidance, or patient-specific MRD interpretation. |
| `residual_biological_state` | Represents source-defined residual malignant plasma-cell states and resistant-state programs. | No treatment, target, supplement, monitoring, or actionability output. |
| `clone_architecture_state` | Represents clone identity, clone architecture, subclone diversity, and clone-inference context. | No patient-specific resistance attribution, prognosis, or causal ranking. |
| `clone_state_coupling_state` | Represents provisional links between clone architecture and residual biological state. | Coupling is an edge, not a merged axis or clinical resistance call. |
| `missingness_and_uncertainty` | Carries missing modality, under-covered branch, assay mismatch, source limitation, and contradiction-mining state. | Missingness is never evidence of absence, lower risk, treatment fit, trial fit, monitoring need, or cure. |
| `blocked_output_manifest` | Makes unsafe outputs fail closed. | Diagnosis, prognosis, treatment, trial, monitoring, ranking, validation, and cure outputs are blocked. |

## Optional Support Families

| Family | Purpose | Boundary |
| --- | --- | --- |
| `support_context_layers` | Preserves microenvironment, therapy pressure, disease context, and translation-readiness modifiers. | Support layers modify research interpretation needs only; they cannot rank or recommend. |

## Minimum Public Object

A public-safe residual state object must include:

- `schema_id`
- `residual_state_object_id`
- `source_context`
- `measurement_trajectory_state`
- `residual_biological_state`
- `clone_architecture_state`
- `clone_state_coupling_state`
- `missingness_and_uncertainty`
- `blocked_output_manifest`

## Fail-Closed Outputs

The object blocks:

- diagnosis
- prognosis
- relapse risk
- MRD interpretation
- monitoring guidance
- treatment guidance
- target selection
- trial guidance
- patient matching
- mechanism ranking
- evidence ranking
- clinical validation
- cure claims

## Structured Data

- JSON: [`myeloma-residual-state-object-v0.json`](myeloma-residual-state-object-v0.json)
- Metadata: [`myeloma-residual-state-object-v0.metadata.json`](myeloma-residual-state-object-v0.metadata.json)
