# Public Artifact Catalog v0

Stewardship mark: frg.earth.

Date: 2026-04-14

Clinical-use boundary: research-use-only. This catalog is a public navigation
artifact, not medical advice, diagnostic guidance, treatment guidance, trial
guidance, or a claim that a cure or vaccine has been found.

## Purpose

Make the public Curing Blood Cancer repo easier to inspect by listing every
tracked public artifact that has metadata, where it lives, what class it is,
what claim level it carries, and how many source and limitation records its
metadata declares.

## How To Use

Run the metadata-backed listing command:

```bash
make list-public-artifacts
```

Filter to the current multiple myeloma lane:

```bash
make list-public-artifacts ARGS="--scope myeloma"
```

Read the machine-readable catalog at
[public-artifact-catalog-v0.json](./public-artifact-catalog-v0.json).

## Current Artifacts

| Artifact | Class | Claim Level | Public Path |
| --- | --- | --- | --- |
| Curing Blood Cancer Concept Map v0 | map | derived | [artifacts/curing-blood-cancer-concept-map-v0.md](./curing-blood-cancer-concept-map-v0.md) |
| Public Artifact Catalog v0 | dataset | derived | [artifacts/public-artifact-catalog-v0.md](./public-artifact-catalog-v0.md) |
| Multiple Myeloma Durable MRD-Negative Remission Cure Wedge v0 | map | open-question | [disease-programs/multiple-myeloma/cure-wedge-durable-mrd-negative-remission-v0.md](../disease-programs/multiple-myeloma/cure-wedge-durable-mrd-negative-remission-v0.md) |
| BCMA Antigen Escape Claim Set v0 | dataset | derived | [disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md](../disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md) |
| BCMA Antigen Escape Evidence Gap Register v0 | dataset | open-question | [disease-programs/multiple-myeloma/evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md](../disease-programs/multiple-myeloma/evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md) |
| MRD And Relapse Measurement Glossary v0 | dataset | derived | [disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md](../disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md) |
| BCMA Measurement Context Audit v0 | dataset | open-question | [disease-programs/multiple-myeloma/measurements/bcma-measurement-context-audit-v0.md](../disease-programs/multiple-myeloma/measurements/bcma-measurement-context-audit-v0.md) |
| Post-CAR T Relapse Extraction Guide v0 | protocol | derived | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-extraction-guide-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-extraction-guide-v0.md) |
| Post-CAR T Relapse Mechanism Map v0 | map | derived | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.md) |
| Post-CAR T Relapse Mechanism Coverage Report v0 | dataset | open-question | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-coverage-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-coverage-v0.md) |
| BCMA Antigen Escape Public Task Queue v0 | dataset | open-question | [disease-programs/multiple-myeloma/public-tasks/bcma-antigen-escape-public-task-queue-v0.md](../disease-programs/multiple-myeloma/public-tasks/bcma-antigen-escape-public-task-queue-v0.md) |
| ClinicalTrials.gov Query Protocol v0 | protocol | derived | [protocols/clinicaltrials-gov-query-protocol-v0.md](../protocols/clinicaltrials-gov-query-protocol-v0.md) |
| Evidence Claim Schema v0 | schema | derived | [schemas/evidence-claim-schema-v0.md](../schemas/evidence-claim-schema-v0.md) |
| Source Registry v0 | dataset | derived | [sources/source-registry-v0.md](../sources/source-registry-v0.md) |
| Multiple Myeloma Treatment-Class Taxonomy v0 | taxonomy | derived | [taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md](../taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md) |

## Update Rules

- Add or update the artifact's `*.metadata.json` file first.
- Run `make validate` before publishing.
- Keep public artifacts source-backed and modest about uncertainty.
- Do not place patient-identifying data, private records, credentials,
  restricted datasets, treatment advice, diagnostic advice, trial
  recommendations, or unsupported cure/vaccine claims in this repo.
