# Measurement Refusal Wrapper State Machine v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-wrapper-state-machine-v0`
- source task: `measurement-refusal-wrapper-state-machine-v0`
- status: public synthetic transition state machine
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: synthetic-only and public-source-scoped; no real case data,
  identifiers, raw records, uploads, exact person-linked dates, free-text case
  details, private correspondence, model weights, predictions,
  recommendations, matching, ranking, or clinical decisions
- last reviewed: `2026-04-21`

## Purpose

This artifact turns the measurement-refusal wrapper dry run into an explicit
state machine.

The goal is not to create model output. The goal is to make wrapper movement
auditable before any future model-facing artifact can reuse refused measurement
metadata.

The state machine defines three safe terminal outcomes:

- metadata-only public refusal terminal
- private or real quality-review blocker terminal
- unsafe wrapper reuse blocked terminal

## Machine Artifact

The machine-readable state machine lives at:

- `examples/measurement-refusal-wrapper-state-machine-v0.json`

The executable checker is:

- `tools/check_measurement_refusal_wrapper_state_machine.py`

Run:

```bash
make check-measurement-refusal-wrapper-state-machine
```

The checker verifies that:

- the state machine targets
  `measurement-refusal-wrapper-integration-dry-run-v0`
- the state machine targets
  `measurement-refusal-wrapper-negative-safety-fixtures-v0`
- all data-boundary fields remain false
- all required clinical boundary labels remain present
- all eight required states exist
- all seven required transitions exist
- every transition emits no output
- each of the ten wrapper dry-run records has one safe trace
- the private-review row terminates in the private-review blocker state
- all thirteen wrapper negative safety fixtures route to the unsafe-reuse
  blocked terminal
- forbidden clinical, prediction, ranking, recommendation, real-review,
  publication, and patient-specific output keys stay absent
- the human authorization blocker remains active

## State Set

| State ID | Meaning | Terminal |
| --- | --- | --- |
| `mrsms_00_refused_output_received` | A synthetic refused measurement output is present. | No |
| `mrsms_01_route_validated_refusal_only` | The refused output has exactly one refusal-only route. | No |
| `mrsms_02_wrapper_metadata_assembled` | Wrapper metadata exists and still carries refusal-only fields. | No |
| `mrsms_03_public_refusal_wrapper_ready` | Public synthetic refusal metadata is ready for metadata-only use. | No |
| `mrsms_04_private_or_real_review_blocker_ready` | A private or real quality-review request is visibly blocked. | No |
| `mrsms_05_metadata_only_public_terminal` | Public path terminates as refusal metadata only. | Yes |
| `mrsms_06_private_or_real_review_blocker_terminal` | Private or real review path terminates as a blocker only. | Yes |
| `mrsms_07_unsafe_wrapper_reuse_blocked_terminal` | Unsafe wrapper mutation terminates as blocked reuse only. | Yes |

## Transition Contract

Allowed movement is narrow:

1. refused output to validated refusal route
2. validated refusal route to wrapper metadata
3. wrapper metadata to public refusal-ready state
4. wrapper metadata to private-review blocker-ready state
5. public refusal-ready state to metadata-only public terminal
6. private-review blocker-ready state to private-review blocker terminal
7. unsafe wrapper mutation to unsafe wrapper reuse blocked terminal

Every transition keeps:

- `clinical_output_allowed: false`
- `prediction_output_allowed: false`
- `comparison_allowed: false`
- `matching_or_ranking_allowed: false`
- `real_review_output_allowed: false`
- `publication_authorization_allowed: false`
- no generated interpretation
- no model output
- no route expansion

## What This Adds

The previous wrapper dry run proved that refused measurement outputs can map to
wrapper metadata only. The previous wrapper negative safety fixture pack proved
that unsafe wrapper mutations fail closed.

This state machine connects those two facts. It makes the allowed movement
explicit and gives future checks a concrete transition surface to test.

## Handoff State

`measurement-refusal-wrapper-state-machine-v0` is complete when the JSON state
machine, protocol, checker, metadata, catalog, inventory, ORP state, and
Clawdad state are wired and validation passes.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The follow-on
[Measurement Refusal Wrapper State Machine Negative Safety Fixtures v0](measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0.md)
is now complete and proves that known unsafe transition mutations fail closed.
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

## Limitations

- This is a public synthetic transition state machine, not a clinical safety
  system.
- This does not process or validate real reports.
- This does not validate MRD methods, specimens, thresholds, scans, biopsies,
  or private lab records.
- This does not prove that any private implementation is safe, clinically
  useful, calibrated, legally usable, publication-ready, or regulatory-ready.
- This does not clear expert-review, private-lab, clinical-team, legal,
  regulatory, publication, model-governance, or human-review gates.
- This does not claim that multiple myeloma has been cured.
