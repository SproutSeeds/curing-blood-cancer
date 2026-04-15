# Public Artifact Catalog v0

Stewardship mark: frg.earth.

Date: 2026-04-15

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
| Multiple Myeloma Public Roadmap v0 | protocol | open-question | [disease-programs/multiple-myeloma/public-roadmap-v0.md](../disease-programs/multiple-myeloma/public-roadmap-v0.md) |
| Multiple Myeloma Open Research Map v0.1 | map | open-question | [disease-programs/multiple-myeloma/open-research-map-v0-1.md](../disease-programs/multiple-myeloma/open-research-map-v0-1.md) |
| Multiple Myeloma Schema And Tooling Phase Inventory v0 | protocol | open-question | [disease-programs/multiple-myeloma/schema-tooling-phase-inventory-v0.md](../disease-programs/multiple-myeloma/schema-tooling-phase-inventory-v0.md) |
| Multiple Myeloma Tooling Readiness Gate v0 | protocol | open-question | [disease-programs/multiple-myeloma/tooling-readiness-gate-v0.md](../disease-programs/multiple-myeloma/tooling-readiness-gate-v0.md) |
| Case-To-Cure Pipeline Blueprint v0 | protocol | open-question | [disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md](../disease-programs/multiple-myeloma/case-to-cure-pipeline-blueprint-v0.md) |
| Candidate-Option Scoring Rubric v0 | protocol | open-question | [disease-programs/multiple-myeloma/candidate-option-scoring-rubric-v0.md](../disease-programs/multiple-myeloma/candidate-option-scoring-rubric-v0.md) |
| Publication-Gate Checklist v0 | protocol | open-question | [disease-programs/multiple-myeloma/publication-gate-checklist-v0.md](../disease-programs/multiple-myeloma/publication-gate-checklist-v0.md) |
| Multidisciplinary Review Packet Template v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md](../disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md) |
| Review-Packet Builder Input Manifest Spec v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-manifest-spec-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-manifest-spec-v0.md) |
| Review-Packet Builder Dry-Run Plan v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-dry-run-plan-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-dry-run-plan-v0.md) |
| Review-Packet Builder Implementation Gate v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-implementation-gate-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-implementation-gate-v0.md) |
| Review-Packet Builder Packet-Assembly Gate v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-packet-assembly-gate-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-packet-assembly-gate-v0.md) |
| Review-Packet Builder Packet-Skeleton Spec v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-packet-skeleton-spec-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-packet-skeleton-spec-v0.md) |
| Review-Packet Builder Recombination Handoff v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/review-packet-builder-recombination-handoff-v0.md](../disease-programs/multiple-myeloma/reviews/review-packet-builder-recombination-handoff-v0.md) |
| Multiple Myeloma Definition-Of-Complete Audit v0 | protocol | open-question | [disease-programs/multiple-myeloma/definition-of-complete-audit-v0.md](../disease-programs/multiple-myeloma/definition-of-complete-audit-v0.md) |
| Case-Specific Private-Lab Blocker Register v0 | dataset | open-question | [disease-programs/multiple-myeloma/case-specific-private-lab-blocker-register-v0.md](../disease-programs/multiple-myeloma/case-specific-private-lab-blocker-register-v0.md) |
| Multiple Myeloma Public Loop Completion Handoff v0 | protocol | open-question | [disease-programs/multiple-myeloma/public-loop-completion-handoff-v0.md](../disease-programs/multiple-myeloma/public-loop-completion-handoff-v0.md) |
| Review-Packet Manifest Route-Table Dry-Run Tool v0 | tool | open-question | [tools/review_packet_manifest_route_table.py](../tools/review_packet_manifest_route_table.py) |
| Review-Packet Route-Table Output Schema v0 | schema | open-question | [schemas/review-packet-route-table-output-schema-v0.md](../schemas/review-packet-route-table-output-schema-v0.md) |
| Multiple Myeloma Synthetic Case-To-Cure Pipeline v0 | dataset | open-question | [examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md](../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md) |
| Multiple Myeloma Durable MRD-Negative Remission Cure Wedge v0 | map | open-question | [disease-programs/multiple-myeloma/cure-wedge-durable-mrd-negative-remission-v0.md](../disease-programs/multiple-myeloma/cure-wedge-durable-mrd-negative-remission-v0.md) |
| BCMA Antigen Escape Claim Set v0 | dataset | derived | [disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md](../disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md) |
| BCMA Antigen Escape Evidence Gap Register v0 | dataset | open-question | [disease-programs/multiple-myeloma/evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md](../disease-programs/multiple-myeloma/evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md) |
| BCMA Claim Set Expert Review Packet v0 | protocol | open-question | [disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md](../disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md) |
| MRD And Relapse Measurement Glossary v0 | dataset | derived | [disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md](../disease-programs/multiple-myeloma/measurements/mrd-and-relapse-measurement-glossary-v0.md) |
| BCMA Measurement Context Audit v0 | dataset | open-question | [disease-programs/multiple-myeloma/measurements/bcma-measurement-context-audit-v0.md](../disease-programs/multiple-myeloma/measurements/bcma-measurement-context-audit-v0.md) |
| Post-CAR T Relapse Extraction Guide v0 | protocol | derived | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-extraction-guide-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-extraction-guide-v0.md) |
| Post-CAR T Relapse Mechanism Map v0 | map | derived | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-map-v0.md) |
| Post-CAR T Relapse Mechanism Coverage Report v0 | dataset | open-question | [disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-coverage-v0.md](../disease-programs/multiple-myeloma/mechanisms/post-car-t-relapse-mechanism-coverage-v0.md) |
| Post-CAR T Relapse Mechanism Gap Public Task Queue v0 | dataset | open-question | [disease-programs/multiple-myeloma/public-tasks/post-car-t-relapse-mechanism-gap-public-task-queue-v0.md](../disease-programs/multiple-myeloma/public-tasks/post-car-t-relapse-mechanism-gap-public-task-queue-v0.md) |
| Multiple Myeloma Roadmap Public Task Queue v0 | dataset | open-question | [disease-programs/multiple-myeloma/public-tasks/multiple-myeloma-roadmap-public-task-queue-v0.md](../disease-programs/multiple-myeloma/public-tasks/multiple-myeloma-roadmap-public-task-queue-v0.md) |
| BCMA Antigen Escape Public Task Queue v0 | dataset | open-question | [disease-programs/multiple-myeloma/public-tasks/bcma-antigen-escape-public-task-queue-v0.md](../disease-programs/multiple-myeloma/public-tasks/bcma-antigen-escape-public-task-queue-v0.md) |
| ClinicalTrials.gov Query Protocol v0 | protocol | derived | [protocols/clinicaltrials-gov-query-protocol-v0.md](../protocols/clinicaltrials-gov-query-protocol-v0.md) |
| Clawdad Autonomous Research Loop v0 | protocol | open-question | [protocols/clawdad-autonomous-research-loop-v0.md](../protocols/clawdad-autonomous-research-loop-v0.md) |
| Case-Feature Bundle Public Summary v0 | schema | open-question | [schemas/case-feature-bundle-public-summary-v0.md](../schemas/case-feature-bundle-public-summary-v0.md) |
| Disease Map Schema v0 | schema | open-question | [schemas/disease-map-schema-v0.md](../schemas/disease-map-schema-v0.md) |
| Evidence Claim Schema v0 | schema | derived | [schemas/evidence-claim-schema-v0.md](../schemas/evidence-claim-schema-v0.md) |
| Target Record Schema v0 | schema | open-question | [schemas/target-record-schema-v0.md](../schemas/target-record-schema-v0.md) |
| Therapy Record Schema v0 | schema | open-question | [schemas/therapy-record-schema-v0.md](../schemas/therapy-record-schema-v0.md) |
| Trial-Landscape Record Schema v0 | schema | open-question | [schemas/trial-landscape-record-schema-v0.md](../schemas/trial-landscape-record-schema-v0.md) |
| Open-Question Record Schema v0 | schema | open-question | [schemas/open-question-record-schema-v0.md](../schemas/open-question-record-schema-v0.md) |
| Review-Packet Builder Manifest Schema v0 | schema | open-question | [schemas/review-packet-builder-manifest-schema-v0.md](../schemas/review-packet-builder-manifest-schema-v0.md) |
| Source Registry v0 | dataset | derived | [sources/source-registry-v0.md](../sources/source-registry-v0.md) |
| Multiple Myeloma Treatment-Class Taxonomy v0 | taxonomy | derived | [taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md](../taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md) |

## Update Rules

- Add or update the artifact's `*.metadata.json` file first.
- Run `make validate` before publishing.
- Keep public artifacts source-backed and modest about uncertainty.
- Do not place patient-identifying data, private records, credentials,
  restricted datasets, treatment advice, diagnostic advice, trial
  recommendations, or unsupported cure/vaccine claims in this repo.
