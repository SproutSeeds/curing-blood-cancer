# Build A Review-Packet Manifest Route-Table Dry-Run Script

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task may implement only the deterministic copied-reference route-table
script selected by [Review-Packet Builder Implementation Gate v0](../../reviews/review-packet-builder-implementation-gate-v0.md).
It must not build a review-packet builder, generator, dashboard, explorer,
ranking tool, trial finder, patient matcher, recommendation system, generated
packet output, generated public explainer, or generated-claim pipeline.

## Why This Matters

The implementation gate conditionally allows one smallest safe code slice:
a local dry-run script that reads the public placeholder manifest, validates
public references, and emits only copied-reference route-table data, explicit
missing-input records, and refusal reasons.

The script must prove refusal behavior before any future packet assembly can be
considered.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `multiple-myeloma-review-packet-builder-implementation-gate-v0`
- `multiple-myeloma-review-packet-builder-dry-run-plan-v0`
- `review-packet-builder-manifest-schema-v0`
- `multiple-myeloma-review-packet-builder-manifest-spec-v0`
- `multiple-myeloma-tooling-readiness-gate-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a deterministic local route-table dry-run script.
- Add a fixture based on `schemas/review-packet-builder-manifest-template-v0.json`.
- Add a refusal fixture for at least one forbidden manifest field.
- Add documentation explaining the script output is copied-reference routing
  only, not a review packet, not expert review, not generated biomedical text,
  and not publication-ready.
- Add focused tests or validation checks that fail closed on missing paths,
  missing source IDs, missing boundary fields, or forbidden inputs.

## Acceptance Checks

- `make validate` passes.
- The script reads only public repo files and requires no network, credentials,
  accounts, paid services, or private records.
- The script output is limited to copied public identifiers, public paths,
  boundary text, validation status, missing-input records, and refusal reasons.
- The script rejects patient identifiers, real case data, generated claims,
  recommendations, rankings, trial matching, expanded-access guidance,
  publication authorization, and private records.
- No generated review packets, generated biomedical prose, generated public
  explainers, patient-specific outputs, ranking views, trial finder,
  recommendation system, or publication workflow is added.

## Do Not Infer

- Do not infer that a route-table script is a review-packet builder.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from route-table
  output.
- Do not use route-table output for treatment selection, trial selection,
  expanded-access decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
