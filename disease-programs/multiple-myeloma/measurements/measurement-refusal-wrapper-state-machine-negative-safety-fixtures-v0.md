# Measurement Refusal Wrapper State Machine Negative Safety Fixtures v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0`
- source task: `measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0`
- status: public synthetic transition fail-closed fixtures
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: synthetic wrapper state-machine negative fixtures only
- last reviewed: `2026-04-21`

## Purpose

This artifact pressure-tests the
[Measurement Refusal Wrapper State Machine v0](measurement-refusal-wrapper-state-machine-v0.md).

The previous state machine made safe wrapper refusal movement explicit. This
fixture pack asks a harder question: does the checker fail closed when the
state machine itself drifts?

It exists so future model-output reuse, public export, publication workflow,
quality-review routing, or clinical interpretation cannot quietly inherit a
broken transition surface.

## Fixture Pack

The synthetic negative fixture pack lives at:

- `examples/measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0.json`

The fixtures mutate only the public wrapper state-machine dataset:

- `examples/measurement-refusal-wrapper-state-machine-v0.json`

## Executable Check

The checker lives at:

- `tools/check_measurement_refusal_wrapper_state_machine_negative_safety_fixtures.py`

Run it with:

```bash
make check-measurement-refusal-wrapper-state-machine-negative-safety-fixtures
```

The checker applies each mutation to a temporary copy of the state machine and
then runs the existing state-machine checker. Every mutation must trigger the
expected fail-closed check IDs.

## Negative Cases

The fixture pack verifies fail-closed behavior for:

- prediction boundary poisoning
- missing clinical boundary labels
- missing required states
- duplicate state identifiers
- terminal states no longer marked terminal
- state-level clinical output permission
- missing required transitions
- transitions that emit output
- transitions pointing to unknown destination states
- public traces diverted to private-review terminals
- private-review traces diverted to public terminals
- missing blocked downstream uses inside traces
- missing unsafe-transition blocker rules
- unsafe rules routed to the wrong terminal
- missing transition invariants
- forbidden clinical interpretation keys
- handoff human-gate drift

## Required Fail-Closed Behavior

Each negative fixture must make the state-machine checker fail. A passing
unsafe mutation is a blocker for model-output reuse, wrapper transition reuse,
public export, publication, private-review routing, and clinical interpretation.

These fixtures are not evidence that the wrapper validates real data. They only
prove that this public synthetic state-machine surface rejects known unsafe
transition mutations.

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

`measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0` is
complete when the fixture pack, checker, metadata, catalog, inventory, ORP
state, and Clawdad state are all wired and `make validate` passes.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-state-machine-falsification-audit-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No raw reports, raw values, scans, biopsies, accessions, or exact
  person-linked dates.
- No private correspondence.
- No model weights.
- No model output.
- No MRD interpretation.
- No assay or specimen validity conclusion.
- No residual-disease comparison.
- No diagnosis, prognosis, monitoring, treatment, trial, eligibility,
  expanded-access, matching, ranking, clinical-decision, publication, or cure
  output.
