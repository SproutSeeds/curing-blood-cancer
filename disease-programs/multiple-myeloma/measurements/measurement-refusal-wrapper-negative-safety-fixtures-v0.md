# Measurement Refusal Wrapper Negative Safety Fixtures v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-wrapper-negative-safety-fixtures-v0`
- source task: `measurement-refusal-wrapper-negative-safety-fixtures-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: synthetic wrapper fail-closed fixtures only
- last reviewed: `2026-04-20`

## Purpose

This artifact pressure-tests the
[Measurement Refusal Wrapper Integration Dry Run v0](measurement-refusal-wrapper-integration-dry-run-v0.md).

It exists so the public repo can prove that unsafe changes to wrapper metadata
fail closed before any wrapper state machine, model-output reuse, report
quality-review path, publication workflow, or clinical interpretation path.

## Fixture Pack

The synthetic negative fixture pack lives at:

- `examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json`

The fixtures mutate only the public wrapper dry-run report:

- `examples/measurement-refusal-wrapper-integration-dry-run-v0.json`

## Executable Check

The checker lives at:

- `tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py`

Run it with:

```bash
make check-measurement-refusal-wrapper-negative-safety-fixtures
```

## Negative Cases

The fixture pack verifies fail-closed behavior for:

- prediction boundary flags
- missing clinical boundary labels
- missing wrapper records
- duplicate wrapper records
- wrong wrapper IDs
- unsafe output-family changes
- enabled clinical output
- enabled prediction output
- unblocked private or real quality-review rows
- wrapper-boundary expansion beyond refusal metadata
- missing blocked downstream uses
- forbidden clinical interpretation fields
- forbidden ranking fields

## Required Fail-Closed Behavior

Each negative fixture must make the wrapper dry-run checker fail. A passing
unsafe mutation is a blocker for model-output reuse, wrapper state transitions,
public export, publication, private-review routing, and clinical interpretation.

The fixtures are not evidence that the wrapper validates real data. They only
prove that this public synthetic wrapper dry-run surface rejects known unsafe
mutations.

## Blocked Output

This phase must not emit or authorize:

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

`measurement-refusal-wrapper-negative-safety-fixtures-v0` is complete when the
fixture pack, checker, metadata, catalog, inventory, ORP state, and Clawdad
state are all wired and `make validate` passes.
The follow-on [Measurement Refusal Wrapper State Machine v0](measurement-refusal-wrapper-state-machine-v0.md)
is now complete as synthetic wrapper transition metadata.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0`.

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
