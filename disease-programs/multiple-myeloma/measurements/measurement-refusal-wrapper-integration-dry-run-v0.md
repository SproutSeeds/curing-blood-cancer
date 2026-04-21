# Measurement Refusal Wrapper Integration Dry Run v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-wrapper-integration-dry-run-v0`
- source task: `measurement-refusal-wrapper-integration-dry-run-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: synthetic wrapper metadata only
- last reviewed: `2026-04-20`

## Purpose

This artifact dry-runs the connection between refused measurement outputs and
the [Model Output Boundary Wrapper v0](../model-output-boundary-wrapper-v0.md).

It exists after the validator and negative safety fixture phases so the public
repo can prove that refused assay/specimen quality outputs can reach the
wrapper only as refusal metadata, not as model output.

## Dry-Run Report

The generated dry-run report lives at:

- `examples/measurement-refusal-wrapper-integration-dry-run-v0.json`

It uses these public synthetic inputs:

- `examples/measurement-refusal-output-fixture-v0.json`
- `disease-programs/multiple-myeloma/measurements/measurement-refusal-output-route-table-v0.json`
- `examples/measurement-refusal-validator-skeleton-report-v0.json`
- `disease-programs/multiple-myeloma/model-output-boundary-wrapper-v0.md`

## Executable Check

The checker lives at:

- `tools/check_measurement_refusal_wrapper_integration_dry_run.py`

It verifies that every refused measurement output has one wrapper metadata
record and that every record preserves the refusal-only boundary.

Run it with:

```bash
make check-measurement-refusal-wrapper-integration-dry-run
```

Regenerate the report with:

```bash
make check-measurement-refusal-wrapper-integration-dry-run ARGS="--write-report"
```

## Required Wrapper Behavior

Every wrapper record must:

- use `wrapper_id: model-output-boundary-wrapper-v0`
- use `output_family_id: mrd_head`
- use `requested_use: synthetic_fixture_check`
- carry `head_status: assay_specimen_quality_needed`
- preserve the source fixture, source route, source checklist row, and refusal
  reason
- keep `clinical_output_allowed`, `prediction_output_allowed`,
  `comparison_allowed`, `matching_or_ranking_allowed`,
  `real_review_output_allowed`, and `publication_authorization_allowed` false
- keep `no_interpretive_text` true
- preserve every blocked downstream use from the refused output record

The private or real quality-review row must remain a blocker with
`public_processing_allowed: false`, `gate_status: private_lab_needed`, and
`review_status: privacy_review_needed`.

## Blocked Output

The dry run must not emit or authorize:

- MRD interpretation
- assay or specimen validity conclusions
- residual-disease comparison
- diagnosis, prognosis, monitoring, treatment, trial, eligibility, or
  expanded-access guidance
- patient matching, assay ranking, modality ranking, evidence ranking, source
  ranking, actionability scoring, or option ranking
- model weights, scores, thresholds, probabilities, response categories,
  resistance labels, or prediction APIs
- report interpretation, imaging interpretation, biopsy interpretation, or
  clinical decisions
- publication authorization or cure claims

## Handoff State

`measurement-refusal-wrapper-integration-dry-run-v0` is complete when the
generated report, checker, metadata, catalog, inventory, ORP state, and Clawdad
state are all wired and `make validate` passes.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-negative-safety-fixtures-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No raw reports, raw values, scans, biopsies, accessions, or exact
  person-linked dates.
- No model weights.
- No model output.
- No MRD interpretation.
- No assay or specimen validity conclusion.
- No residual-disease comparison.
- No diagnosis, prognosis, monitoring, treatment, trial, eligibility,
  expanded-access, matching, ranking, clinical-decision, publication, or cure
  output.
