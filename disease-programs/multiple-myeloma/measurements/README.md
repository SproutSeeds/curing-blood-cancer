# Multiple Myeloma Measurements

Stewarded by [frg.earth](https://frg.earth/).

This directory holds public measurement definitions and endpoint guardrails for
the multiple myeloma disease program.

## Current Artifacts

- [MRD and Relapse Measurement Glossary v0](mrd-and-relapse-measurement-glossary-v0.md)
- [MRD Endpoint Language Guardrail Addendum v0](mrd-endpoint-language-guardrail-addendum-v0.md)
- [Measurement Normalization Contract v0](measurement-normalization-contract-v0.md)
- [BCMA Measurement Context Audit v0](bcma-measurement-context-audit-v0.md)
- [Residual Disease Modality Discordance Source Extraction v0](residual-disease-modality-discordance-source-extraction-v0.md)
- [Assay Specimen Quality Failure Mode Checklist v0](assay-specimen-quality-failure-mode-checklist-v0.md)
- [Measurement Refusal Output Route Table v0](measurement-refusal-output-route-table-v0.md)
- [Measurement Refusal Validator Skeleton v0](measurement-refusal-validator-skeleton-v0.md)
- [Measurement Refusal Negative Safety Fixtures v0](measurement-refusal-negative-safety-fixtures-v0.md)
- [Measurement Refusal Wrapper Integration Dry Run v0](measurement-refusal-wrapper-integration-dry-run-v0.md)

## Boundary

- Research artifacts only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Measurement terms must preserve source IDs, assay context, specimen context,
  time point, sensitivity threshold, modality family, paired-state context,
  assay/specimen quality, and uncertainty when available.
- Residual-disease modality-discordance artifacts must expose disagreement or
  missing context as a boundary, not as patient-specific meaning.
- Assay/specimen quality artifacts must expose missing method, threshold,
  specimen quality, timing, paired-modality, imaging, spatial, host-context,
  private-review, and modality-collapse states as fail-closed boundaries.
- Measurement-refusal wrapper integration artifacts must expose refused outputs
  to the model-output wrapper as metadata only, not as prediction,
  interpretation, ranking, real-review, publication, or decision output.
- Synthetic measurement-state refusal fixtures live in
  [`examples/measurement-state-refusal-fixtures-v0.json`](../../../examples/measurement-state-refusal-fixtures-v0.json)
  so those boundaries can be checked without real records or clinical output.
- Measurement-refusal route tables may route refusal metadata only; they must
  not emit interpretation, comparison, ranking, treatment, trial, monitoring,
  publication, decision, or cure outputs.
- Measurement-refusal validator skeletons may emit structural validation
  reports only; they must not emit MRD interpretation, assay validity,
  comparison, ranking, advice, publication, decision, or cure outputs.
- Measurement-refusal negative safety fixtures may mutate synthetic route
  tables only to prove fail-closed behavior; they must not contain real reports,
  raw values, advice, ranking, publication, decision, or cure outputs.
