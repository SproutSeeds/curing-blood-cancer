# Measurement Refusal Validator Skeleton v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-validator-skeleton-v0`
- source task: `measurement-refusal-validator-skeleton-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: synthetic structural validation only
- last reviewed: `2026-04-20`

## Purpose

This artifact defines the first executable skeleton for validating
measurement-refusal routes.

It exists after [Measurement Refusal Output Route Table v0](measurement-refusal-output-route-table-v0.md)
and before any model-output wrapper integration. It checks that refused
measurement-state records remain refusal metadata only.

## Executable Skeleton

The executable validator lives at:

- `tools/measurement_refusal_validator_skeleton.py`

It reads:

- `examples/measurement-refusal-output-fixture-v0.json`
- `disease-programs/multiple-myeloma/measurements/measurement-refusal-output-route-table-v0.json`

It emits:

- `examples/measurement-refusal-validator-skeleton-report-v0.json`

## Validator Rules

The skeleton checks:

- public synthetic data boundaries are false for real case data, identifiers,
  raw records, uploads, exact person-linked dates, private correspondence,
  model weights, predictions, recommendations, matching, ranking, and clinical
  decisions
- no-advice clinical boundary labels are present
- every refused output record has exactly one route
- the blocked route manifest carries all required blocked downstream outputs
- required destination contracts are present
- each route preserves refusal-only metadata, source fixture links, checklist
  row, assay/specimen quality state, route status, route boundary, and blocked
  routes
- the generated report emits only allowed route fields

## Allowed Output

The validator may emit only a structural validation report. Route-level results
may include:

- route identifiers
- source output, source fixture, and source checklist IDs
- assay/specimen quality state
- route status and route boundary
- public-processing flag
- allowed route families
- destination contracts
- blocked route labels
- `validator_decision`

The `validator_decision` values are limited to:

- `accepted_refusal_metadata_only`
- `blocked_private_review_notice_only`

## Blocked Output

The skeleton must not emit:

- MRD interpretation
- assay or specimen validity conclusions
- residual-disease comparison
- diagnosis, prognosis, monitoring, treatment, trial, eligibility, or
  expanded-access guidance
- patient matching, assay ranking, modality ranking, evidence ranking, source
  ranking, actionability scoring, or option ranking
- report interpretation, imaging interpretation, biopsy interpretation, or
  clinical decisions
- publication authorization or cure claims

## Handoff State

`measurement-refusal-validator-skeleton-v0` is complete when the executable
validator, report fixture, metadata, navigation, inventory, and ORP state are
all wired and `make validate` passes.
The follow-on [Measurement Refusal Negative Safety Fixtures v0](measurement-refusal-negative-safety-fixtures-v0.md)
are now complete as synthetic fail-closed tests for the validator.
The follow-on [Measurement Refusal Wrapper Integration Dry Run v0](measurement-refusal-wrapper-integration-dry-run-v0.md)
is now complete as wrapper metadata only.
The follow-on [Measurement Refusal Wrapper Negative Safety Fixtures v0](measurement-refusal-wrapper-negative-safety-fixtures-v0.md)
are now complete as synthetic fail-closed tests for unsafe wrapper mutations.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-state-machine-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No raw reports, raw values, scans, biopsies, accessions, or exact
  person-linked dates.
- No MRD interpretation.
- No assay or specimen validity conclusion.
- No residual-disease comparison.
- No diagnosis, prognosis, monitoring, treatment, trial, eligibility,
  expanded-access, matching, ranking, clinical-decision, publication, or cure
  output.
