# Cure Wedge v0: Durable MRD-Negative Remission in Multiple Myeloma

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- wedge status: `active-v0`
- claim level: `open-question`
- last reviewed: `2026-04-14`
- clinical boundary: research artifact, not medical advice

## Purpose

This wedge makes multiple myeloma the first focused disease program inside
Curing Blood Cancer.

The cure-oriented question is:

> What would it take to turn deep multiple myeloma responses into durable,
> measurable-residual-disease-negative remission with fewer relapses?

This is not a claim that such a cure has been found. It is a public research
frame for organizing sources, mechanisms, trial landscapes, and tool outputs.

## Why This Wedge

Multiple myeloma already has a rich public evidence surface: treatment-class
summaries, clinical-trial records, regulatory records, literature records, and
measurable residual disease research.

It is also narrow enough to build useful tooling without flattening all blood
cancers into one disease.

## Scope

Included:

- multiple myeloma and closely related plasma-cell disease context
- durable remission and relapse-prevention questions
- measurable residual disease as a measurement layer
- CAR T-cell therapy, bispecific antibodies, monoclonal antibodies, transplant
  strategy, maintenance, supportive care, and vaccine/immunoprevention research
  as research lanes
- public-source trial and literature maps

Excluded:

- patient-specific treatment selection
- trial eligibility advice
- clinician-facing guidelines
- unsupported cure claims
- private records or restricted datasets

## Cure-Oriented Outcomes To Track

- sustained measurable residual disease negativity
- progression-free survival and overall survival as source-defined endpoints
- treatment-free or low-burden durable remission where source-defined
- relapse timing after deep response
- relapse mechanism after immune therapy
- quality-of-life and infection-risk context when public sources support it

## Failure Modes To Map

- antigen escape after immune targeting
- T-cell exhaustion or inadequate immune fitness
- relapse after BCMA-directed therapy
- high-risk cytogenetic or molecular context
- extramedullary disease
- infection risk and immune reconstitution after intensive immune therapy
- manufacturing, access, and timing constraints for cellular therapy
- overgeneralizing one product, trial, or disease state to all myeloma

## Initial Program Tracks

| Track | Question | Starting Artifact |
| --- | --- | --- |
| Deep response measurement | Which public sources define and measure durable MRD negativity? | `opportunity-map-v0.json` |
| Immune relapse biology | Why do some deep responses after CAR T or bispecific therapy relapse? | `evidence-claims/multiple-myeloma-durable-remission-wedge-v0.json` |
| Trial landscape | Which recruiting studies target durability, relapse prevention, or immune redirection? | `examples/multiple-myeloma-car-t-query-record-v0.json` |
| Tooling | What data shapes make opportunities comparable and auditable? | `schemas/opportunity-map.schema.json` |

## Source Anchors

- NCI PDQ plasma-cell neoplasms / multiple myeloma treatment summary:
  `nci_pdq_myeloma_hp`
- ClinicalTrials.gov and API v2: `clinicaltrials_gov`,
  `clinicaltrials_gov_api_v2`
- PubMed: `pubmed`
- FDA Drugs@FDA: `fda_drugs_at_fda`

## Review Boundary

This wedge can organize public research work, but it cannot determine medical
care. Any clinical interpretation requires qualified clinician review and
current source verification.
