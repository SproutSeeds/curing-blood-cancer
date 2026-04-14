# Post-CAR T Relapse Extraction Guide v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `post-car-t-relapse-mechanism-map-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-14`

## Purpose

This guide turns the post-CAR T relapse mechanism map into repeatable
extraction work.

The core flow is:

```text
public source -> extraction record -> mechanism bucket -> evidence claim
```

## What To Extract

For each paper, trial record, regulatory record, or source summary, extract:

- source ID and public URL
- disease setting
- therapy or intervention context
- mechanism bucket or buckets
- observed signal
- measurement fields
- denominator context when a source reports numerator and denominator fields
- limitations
- what the source does and does not support

## Mechanism Buckets

Use the mechanism IDs from
`post-car-t-relapse-mechanism-map-v0.json`.

Initial buckets:

- `bcma-antigen-loss-or-low-density-v0`
- `car-t-fitness-exhaustion-persistence-v0`
- `plasma-cell-identity-or-lineage-state-escape-v0`
- `disease-burden-site-risk-context-v0`
- `sequential-or-dual-target-immune-pressure-v0`
- `measurement-and-follow-up-gaps-v0`

## Extraction Rules

- One extraction record should cover one source.
- Do not infer mechanism frequency unless the source reports enough data.
- When a source reports denominator-ready target-status fields, preserve the
  numerator, denominator, denominator basis, product context, prior target
  exposure, assay method, specimen source, assay timing, response or relapse
  state, and what frequency claims remain unsupported.
- Do not turn association into causation without explicit support.
- Do not compare products unless the source was designed for that comparison.
- Do not use an extraction as treatment, sequencing, trial, or eligibility
  advice.
- Mark preprints and source-type limits clearly.

## Review Questions

Before publishing an extraction, ask:

- Is the source public and represented in `sources/source-registry-v0.json`?
- Does every `source_id` resolve?
- Does every `mechanism_group_id` resolve?
- Are measurement fields specific enough for later comparison?
- Does the record say what it does not support?
- Would a reader mistake the artifact for medical advice?

## Files

- Template: `post-car-t-relapse-extraction-template-v0.json`
- Example: `extractions/ledergor-2024-cd4-car-t-exhaustion-v0.json`
- Example: `extractions/firestone-2024-bcma-antigen-escape-v0.json`
- Example: `extractions/tedder-bhutani-2025-bcma-resistance-review-v0.json`
- Example: `extractions/di-meo-2025-sema4a-low-bcma-v0.json`
