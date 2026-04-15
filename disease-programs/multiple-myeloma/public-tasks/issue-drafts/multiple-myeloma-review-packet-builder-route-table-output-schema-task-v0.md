# Define A Review-Packet Route-Table Output Schema

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, clinical prioritization, generated biomedical claims, publication
authorization, or a cure claim.

This task may define only a validated output shape for the deterministic
copied-reference route-table dry run. It must not build packet assembly,
generated packet output, generated biomedical prose, ranking, trial matching,
recommendation behavior, publication workflow, or patient-specific tooling.

## Why This Matters

The first code slice now emits copied-reference route-table output from public
placeholder inputs. Before any downstream tool can rely on that output, the
repo needs a validated output schema and placeholder fixture so route-table
records remain fail-closed and cannot drift into generated claims or review
packets.

## Public Source Anchors

- `pubmed`
- `clinicaltrials_gov_api_v2`
- `nci_pdq_myeloma_hp`
- `hgnc_gene_names`
- `nci_cancer_drug_dictionary`

## Linked Public Artifacts

- `review-packet-manifest-route-table-tool-v0`
- `multiple-myeloma-review-packet-builder-implementation-gate-v0`
- `multiple-myeloma-review-packet-builder-dry-run-plan-v0`
- `review-packet-builder-manifest-schema-v0`
- `multiple-myeloma-review-packet-builder-manifest-spec-v0`
- `multiple-myeloma-tooling-readiness-gate-v0`
- `multiple-myeloma-roadmap-public-task-queue-v0`

## Deliverables

- Add a JSON schema for route-table dry-run outputs produced by
  `tools/review_packet_manifest_route_table.py`.
- Add a placeholder route-table output fixture generated only from public
  placeholder inputs.
- Add validator coverage for route-table output records.
- Document that route-table records are copied-reference routing only, not
  review packets, expert review, generated biomedical prose, recommendations,
  rankings, or publication-ready text.

## Acceptance Checks

- `make validate` passes.
- The output schema requires `route_table_id`, `input_manifest_id`,
  `route_table_status`, `copied_reference_routes`, `missing_input_records`,
  `refusal_records`, `output_boundary`, and `do_not_infer`.
- The validator rejects generated claims, patient identifiers,
  recommendations, rankings, trial matching, expanded-access guidance,
  publication authorization, private records, and packet assembly fields.
- The fixture is built only from public placeholder inputs and does not include
  real case data or generated biomedical content.
- No review packet assembly, generated prose, clinical ranking, trial finder,
  recommendation system, patient-specific workflow, or publication workflow is
  added.

## Do Not Infer

- Do not infer that a route-table output schema authorizes packet assembly.
- Do not infer expert review, evidence strength, clinical importance, patient
  relevance, actionability, or publication authorization from route-table
  output records.
- Do not use route-table output for treatment selection, trial selection,
  expanded-access decisions, monitoring decisions, or cure claims.
- Do not rank questions, trials, therapies, products, targets, sources,
  mechanisms, artifacts, tasks, or evidence by clinical priority.
