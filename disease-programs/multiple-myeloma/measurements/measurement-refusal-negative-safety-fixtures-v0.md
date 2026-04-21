# Measurement Refusal Negative Safety Fixtures v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-negative-safety-fixtures-v0`
- source task: `measurement-refusal-negative-safety-fixtures-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: synthetic fail-closed validation only
- last reviewed: `2026-04-20`

## Purpose

This artifact defines synthetic negative fixtures for the measurement-refusal
validator skeleton.

It exists after [Measurement Refusal Validator Skeleton v0](measurement-refusal-validator-skeleton-v0.md)
so the public repo can test unsafe route-table changes before any wrapper or
model-output surface reuses refused measurement records.

## Fixture Pack

The fixture pack lives at:

- `examples/measurement-refusal-negative-safety-fixtures-v0.json`

It mutates the public baseline inputs:

- `examples/measurement-refusal-output-fixture-v0.json`
- `disease-programs/multiple-myeloma/measurements/measurement-refusal-output-route-table-v0.json`

The mutations are synthetic only. They intentionally create bad route-table
states so the validator must fail closed.

## Executable Check

The checker lives at:

- `tools/check_measurement_refusal_negative_safety_fixtures.py`

It verifies that every negative fixture makes
`measurement-refusal-validator-skeleton-v0` return `report_status: fail` with
the expected failed rule IDs.

Run it with:

```bash
make check-measurement-refusal-negative-safety-fixtures
```

## Negative Cases

The fixture pack covers:

- prediction boundary flag set true
- missing no-advice clinical boundary
- missing route for a refused output
- duplicated route for a refused output
- missing blocked-route manifest entry
- missing destination contract
- unsafe route family
- clinical output flag enabled
- private or real quality-review route made publicly processable
- forbidden clinical guidance field
- forbidden ranking field

## Blocked Output

The negative fixtures must not emit or authorize:

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

`measurement-refusal-negative-safety-fixtures-v0` is complete when the fixture
pack, checker, metadata, catalog, inventory, ORP state, and Clawdad state are
all wired and `make validate` passes.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0`, after
`measurement-refusal-wrapper-integration-dry-run-v0` mapped refused measurement
outputs to wrapper metadata only and
`measurement-refusal-wrapper-negative-safety-fixtures-v0` proved unsafe wrapper
mutations fail closed, and `measurement-refusal-wrapper-state-machine-v0` made
safe wrapper terminal transitions explicit.

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
