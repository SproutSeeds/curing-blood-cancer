# Measurement Refusal Output Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-output-schema-v0`
- source task: `measurement-refusal-output-schema-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: refusal output schema only, no clinical output
- last reviewed: `2026-04-20`

## Purpose

This schema defines the public-safe output shape for measurement-state refusal
records produced from synthetic assay/specimen quality failure fixtures.

It exists after the assay/specimen quality checklist and measurement-state
refusal fixtures, and before any later route table, validator, or model-wrapper
tool can reuse a measurement-state placeholder.

## Output Scope

Allowed output fields are limited to:

- refusal-output set identity
- schema identity
- synthetic fixture provenance
- public synthetic data-boundary statements
- clinical-use and no-clinical-output boundaries
- source fixture and checklist-row links
- stable refusal states
- blocked downstream uses
- fail-closed booleans
- validation notes and no-infer statements

Each record must be an explicit `refused` output in the
`measurement_state_refusal` family. Every output must carry
`wrapper_state: assay_specimen_quality_needed`, one specific
`assay_specimen_quality_state`, and the complete blocked downstream-use list.

## Refused Scope

Measurement refusal output records must not contain:

- patient identifiers, case identifiers, accessions, exact person-linked dates,
  raw values, raw reports, free-text clinical notes, images, biopsies, private
  paths, uploads, private correspondence, or restricted records
- MRD values, thresholds, response categories, risk scores, probabilities,
  labels, model scores, model weights, rankings, or generated interpretation
- diagnosis, prognosis, endpoint interpretation, residual-disease comparison,
  monitoring guidance, treatment guidance, trial guidance, patient matching,
  modality ranking, evidence ranking, report interpretation, lab-validity
  conclusions, imaging interpretation, biopsy interpretation, clinical
  decisions, publication authorization, or cure claims

## Validator Coverage

`tools/check_measurement_refusal_output_schema.py` validates the synthetic
fixture against this schema and checks that:

- public data-boundary fields remain false
- every measurement-state refusal fixture has exactly one output record
- each output preserves the expected fail-closed state
- every output blocks the full downstream-use set
- the private/real quality-review fixture stops public processing
- forbidden clinical, ranking, prediction, and recommendation fields are absent

## Example Fixture

The placeholder fixture is generated from public synthetic inputs only:

- `examples/measurement-refusal-output-fixture-v0.json`

It is not a patient report, not MRD interpretation, not lab validation, not
model inference, not medical advice, and not publication-ready text.

## Limitations

- Schema validation checks output shape only.
- The schema does not generate any measurement interpretation.
- The schema does not validate assay performance, specimen adequacy, imaging
  findings, biopsy findings, thresholds, response criteria, or real reports.
- The schema does not compare residual-disease modalities.
- The schema does not rank assays, modalities, evidence, treatments, trials,
  options, sources, mechanisms, artifacts, tasks, claims, or questions.
- The schema does not provide diagnosis, prognosis, monitoring guidance,
  treatment guidance, trial guidance, eligibility guidance, expanded-access
  guidance, publication authorization, or a cure claim.
