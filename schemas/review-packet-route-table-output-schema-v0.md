# Review-Packet Route-Table Output Schema v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `review-packet-route-table-output-schema-v0`
- source task: `multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: output schema only, no packet assembly
- last reviewed: `2026-04-15`

## Purpose

This schema defines the allowed shape for copied-reference route-table outputs
from `tools/review_packet_manifest_route_table.py`.

It exists after the deterministic route-table dry-run script and before any
downstream review-packet workflow relies on route-table records.

## Output Scope

Allowed output fields are limited to:

- route-table identity
- input manifest identity
- route-table status
- copied public route records
- explicit missing-input records
- refusal records
- validation checks
- clinical-use and output boundaries
- do-not-infer statements

## Refused Scope

Route-table output records must not contain:

- patient identifiers, case identifiers, real case data, raw records, free-text
  clinical notes, images, reviewer identities, or private records
- generated biomedical claims, generated public explainers, rewritten claim
  language, generated packet output, or packet assembly fields
- treatment recommendations, trial recommendations, eligibility guidance,
  enrollment advice, availability claims for any person, expanded-access
  guidance, or sponsor-access instructions
- evidence-strength ranking, clinical priority, urgency, patient relevance,
  actionability, candidate options, option ranking, or trial matching
- publication authorization or cure claims

## Validator Coverage

`make validate` now checks route-table output records with
`route_table_id` against `schemas/review-packet-route-table-output.schema.json`.

The validator also checks:

- duplicate `route_table_id` values
- required output-boundary statements
- required clinical-use boundaries for non-refusal records
- status/record consistency for ready versus refused route tables
- forbidden-field rejection across nested route-table output

## Example Fixture

The placeholder fixture is generated from public placeholder inputs only:

- `examples/review-packet-route-table-output-fixture-v0.json`

It is not a review packet, not expert review, not generated biomedical prose,
not medical advice, and not publication-ready text.

## Limitations

- Schema validation checks output shape only.
- The schema does not authorize packet assembly.
- The schema does not generate or rewrite biomedical claims.
- The schema does not make any artifact expert-reviewed.
- The schema does not prove source coverage is complete.
- The schema does not rank evidence, targets, therapies, trials, sources,
  mechanisms, artifacts, tasks, gaps, claims, or questions.
- The schema does not provide medical advice, diagnostic guidance, treatment
  guidance, trial guidance, eligibility guidance, expanded-access guidance,
  monitoring guidance, or a cure claim.
