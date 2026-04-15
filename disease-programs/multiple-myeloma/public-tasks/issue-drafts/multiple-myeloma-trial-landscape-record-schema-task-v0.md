# Define A Public Trial-Landscape Record Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, enrollment guidance,
expanded-access guidance, sponsor access guidance, or a cure claim.

## Why This Matters

Target Record Schema v0 and Therapy Record Schema v0 now define public target
and therapy-context contracts. The next validated shape should define
trial-landscape records before trial explorer, evidence graph,
extraction-helper, or review-packet-builder tooling depends on registry fields.

The schema should organize public registry and query provenance without turning
trial records into eligibility checks, recommendations, availability claims for
any person, or patient matches.

Completed in `trial-landscape-record-schema-v0`.

## Public Source Anchors

- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `who_ictrp_search_portal`
- `nci_pdq_myeloma_hp`
- `fda_drugs_at_fda`
- `dailymed`
- `ema_medicines`
- `pubmed`

## Linked Public Artifacts

- `target-record-schema-v0`
- `therapy-record-schema-v0`
- `clinicaltrials-gov-query-protocol-v0`
- `multiple-myeloma-schema-tooling-phase-inventory-v0`
- `disease-map-schema-v0`
- `source-registry-v0`

## Deliverables

- Add `schemas/trial-landscape-record.schema.json`.
- Add `schemas/trial-landscape-record-schema-v0.md`.
- Add `schemas/trial-landscape-record-template-v0.json` with public placeholder
  values only.
- Add validator coverage for records with `trial_landscape_record_id`.
- Add catalog, README, roadmap, and task links.
- Completed deliverable: `schemas/trial-landscape-record-schema-v0.md`.

## Acceptance Checks

- `make validate` passes.
- The schema requires trial-landscape ID, registry source IDs, query or
  registry provenance, data timestamp or accessed date, disease scope, source
  IDs, uncertainty, limitations, review status, and clinical-use boundary.
- The schema can link to target records, therapy records, claims, gaps,
  mechanism groups, and public tasks without requiring patient-specific
  eligibility or matching fields.
- The schema rejects or omits eligibility guidance, enrollment advice,
  availability claims for any person, treatment recommendations, sponsor access
  instructions, expanded-access guidance, and real case data.
- The Markdown companion states that trial-landscape validation checks shape
  only, not eligibility, availability, appropriateness, safety, efficacy,
  enrollment status, or patient fit.

## Do Not Infer

- Do not infer trial eligibility from a valid trial-landscape record.
- Do not infer trial availability, enrollment fit, sponsor access, safety,
  efficacy, or appropriateness for any person.
- Do not use the schema for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank trials, therapies, products, or targets.
