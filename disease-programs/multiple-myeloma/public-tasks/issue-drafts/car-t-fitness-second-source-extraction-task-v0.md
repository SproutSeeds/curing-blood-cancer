# Add A Second Public Source Extraction For CAR T Fitness, Exhaustion, Expansion, Or Persistence

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, or a cure claim.

## Why This Matters

The public coverage report currently has one extraction record for the CAR T
fitness, exhaustion, expansion, or persistence bucket. A second source-specific
extraction is needed before the repo can compare this bucket across public
sources.

## Public Source Anchors

- `pubmed_tedder_bhutani_2025_bcma_resistance`
- `pubmed_yue_2025_bcma_resistance`

## Linked Public Artifacts

- `post-car-t-relapse-mechanism-coverage-v0`
- `post-car-t-relapse-mechanism-map-v0`
- `bcma-antigen-escape-evidence-gap-register-v0`

## Deliverables

- Add one source-specific mechanism extraction using the existing extraction
  schema.
- Map extracted signals to `car-t-fitness-exhaustion-persistence-v0`.
- Separate review-level mechanism framing from source-specific measurement
  facts.
- Refresh the coverage report after the extraction is accepted.

## Acceptance Checks

- `make validate` passes.
- The extraction preserves source IDs, mechanism group IDs, measurement term
  IDs, and the clinical-use boundary.
- Review-article statements are not treated as cohort-level measurements unless
  the source provides those measurements.
- Coverage counts are described only as artifact coverage.

## Do Not Infer

- Do not infer that CAR T exhaustion or persistence is the dominant relapse
  mechanism.
- Do not compare products or recommend therapy sequencing.
- Do not make patient-specific relapse interpretations.
