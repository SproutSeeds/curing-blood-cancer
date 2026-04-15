# Multiple Myeloma Synthetic Case-To-Cure Pipeline v0

Stewarded by [frg.earth](https://frg.earth/).

- example id: `multiple-myeloma-synthetic-case-to-cure-pipeline-v0`
- disease program: `multiple-myeloma`
- claim level: `open-question`
- data status: synthetic only
- clinical boundary: research-use-only, not medical advice

## Purpose

This example exercises the public case-to-cure pipeline plumbing without using
real case data.

It shows how a future consented case could move through the pipeline stages
defined in [Case-To-Cure Pipeline Blueprint v0](../disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md)
while keeping real records, identifiers, candidate options, and clinical
decisions outside the public repo.

## Machine-Readable Example

- [Synthetic pipeline JSON](./multiple-myeloma-synthetic-case-to-cure-pipeline-v0.json)
- [Synthetic pipeline schema](../schemas/case-to-cure-synthetic-pipeline.schema.json)

## What This Demonstrates

- case vault, private lab workspace, and public method surface are separate
- every case-like value is synthetic
- no PHI, raw records, dates tied to a person, or re-identification keys are
  present
- candidate options are framed as review questions, not instructions
- standard-care, trial, expanded-access, research-only, and no-go paths are
  buckets for human review
- the publication gate blocks patient-specific outputs from public downstreaming

## Public-To-Private Flow

The public repo contributes:

- schemas
- source IDs
- measurement terms
- treatment taxonomy IDs
- trial-query record IDs
- safety and publication gates
- synthetic examples

The private lab would hold, for a real consented case:

- raw records
- consent and authorization files
- normalized case features
- evidence packets
- candidate option review questions
- clinician or multidisciplinary review records
- monitoring and outcome records

## Stage Coverage

The JSON example covers all stages from `case_00` through `case_14`:

- governance setup
- intake partition
- de-identification planning
- disease-state normalization
- measurement normalization
- molecular and immune context
- exposure and resistance mapping
- evidence retrieval
- candidate hypothesis generation
- candidate scoring
- feasibility and exclusion review
- multidisciplinary review
- action-path selection
- monitoring plan
- outcome capture

## Review Boundary

This example is a tooling demonstration. It is not medical advice, diagnostic
guidance, treatment guidance, trial guidance, expanded-access guidance, or a
claim that multiple myeloma has been cured.
