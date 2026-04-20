# Measurement Refusal Output Route Table v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `measurement-refusal-output-route-table-v0`
- source task: `measurement-refusal-output-route-table-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: refusal routing only, no clinical output
- last reviewed: `2026-04-20`

## Purpose

This route table defines where checked measurement-refusal output records may
travel next.

It exists after [Measurement Refusal Output Schema v0](../../../schemas/measurement-refusal-output-schema-v0.md)
and before any synthetic validator or model-wrapper path consumes refused
measurement-state outputs.

## Routing Rule

Every route starts from one refused output record in
[`examples/measurement-refusal-output-fixture-v0.json`](../../../examples/measurement-refusal-output-fixture-v0.json).
The route table does not create, interpret, summarize, compare, rank, or
rewrite those records. It copies only refusal metadata, source fixture links,
the assay/specimen quality state, blocked downstream uses, and route boundary
tags.

Allowed route families are:

- `structural_validator_input`
- `model_output_boundary_refusal_surface`
- `public_navigation_index`
- `synthetic_regression_fixture`
- `private_review_blocker_notice`

The private or real quality-review state is stricter than the other synthetic
states. It cannot route into public processing; it can only remain visible as a
public blocker notice, navigation record, or synthetic regression fixture.

## Refused Route Scope

The route table blocks:

- diagnosis, prognosis, endpoint interpretation, MRD interpretation, and
  residual-disease comparison
- monitoring guidance, treatment guidance, trial guidance, eligibility
  guidance, expanded-access guidance, and clinical decisions
- patient matching, assay ranking, modality ranking, evidence ranking, source
  ranking, actionability scoring, and option ranking
- report interpretation, lab-validity conclusions, imaging interpretation, and
  biopsy interpretation
- publication authorization and cure claims

## Companion JSON

The structured route table lives in:

- `measurement-refusal-output-route-table-v0.json`

It contains one route record for each of the ten measurement-refusal output
fixture records.

## Validator Coverage

`tools/check_measurement_refusal_output_route_table.py` checks that:

- the route table is public synthetic only
- every refused output record has exactly one route record
- route records preserve the source output, source fixture, checklist row,
  assay/specimen quality state, refusal reason, public-processing state, and
  blocked downstream-use set
- normal refusal records route only to safe refusal surfaces
- the private or real quality-review state routes only as a public blocker
- forbidden clinical, ranking, prediction, and recommendation fields are absent

## Handoff State

`measurement-refusal-output-route-table-v0` is complete as a public synthetic
route table.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-validator-skeleton-v0`.

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
