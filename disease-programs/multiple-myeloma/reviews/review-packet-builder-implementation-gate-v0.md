# Review-Packet Builder Implementation Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-review-packet-builder-implementation-gate-v0`
- source task: `multiple-myeloma-review-packet-builder-implementation-gate-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: aggregate gate only, no builder code in this artifact
- gate result: conditional smallest-safe-code-slice selected
- last reviewed: `2026-04-15`

## Purpose

This gate decides whether review-packet-builder implementation remains fully
blocked or whether a smallest safe code slice can be selected after the manifest
schema and dry-run plan.

It is not builder code. It does not assemble review packets, rewrite claims,
generate biomedical summaries, rank evidence, match patients, select trials,
recommend therapies, authorize publication, or ingest private case data.

## Gate Inputs

| Input | Status | Gate Use |
| --- | --- | --- |
| [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md) | validated shape | Defines allowed manifest fields, required boundaries, and forbidden-field checks. |
| [Review-Packet Builder Manifest Template v0](../../../schemas/review-packet-builder-manifest-template-v0.json) | placeholder only | Provides public test input with no real case data. |
| [Review-Packet Builder Dry-Run Plan v0](review-packet-builder-dry-run-plan-v0.md) | source-checked plan | Defines copy, reference, omit, and refuse behavior. |
| [Review-Packet Builder Input Manifest Spec v0](review-packet-builder-manifest-spec-v0.md) | source-checked spec | Defines public manifest intent and builder-code gate. |
| [Multiple Myeloma Tooling Readiness Gate v0](../tooling-readiness-gate-v0.md) | aggregate no-tooling-yet gate | Keeps generated claims, ranking, trial matching, and recommendations blocked. |
| [Multidisciplinary Review Packet Template v0](multidisciplinary-review-packet-template-v0.md) | template only | Provides section labels that may be referenced but not filled. |

## Decision Table

| Readiness Check | Gate Finding | Decision |
| --- | --- | --- |
| Manifest schema validation | Existing validator checks manifest records and placeholder shape. | Pass for copied-reference dry-run input only. |
| Placeholder-only input | The manifest template uses public placeholder values and public artifact IDs. | Pass for local fixture use; real case data remains refused. |
| No-generated-claims policy | Dry-run plan forbids generated biomedical prose, claim rewriting, advice summaries, and evidence strengthening. | Pass for route-table output only. |
| Refusal behavior | Dry-run plan names required refusals for patient data, recommendations, rankings, generated claims, publication authorization, and private records. | Pass if the first code slice implements refusal checks before output. |
| Output boundary | The only acceptable output is copied public identifiers, public paths, boundary text, validation status, missing-input reports, and refusal reasons. | Pass for a route-table dry-run script; fail for packet assembly. |
| Review status | Public review packet templates remain expert-review-needed. | Pass only if output preserves review status and never implies expert review. |
| Clinical boundary | All source artifacts retain research-use-only, no-medical-advice boundaries. | Pass only if copied boundaries remain visible in output. |
| Implementation scope | No code exists in this gate artifact. | Pass for selecting a future code task only. |

## Gate Result

Implementation is **not** ready for a review-packet builder.

A smallest safe code slice is conditionally selected:

`multiple-myeloma-review-packet-builder-route-table-script-task-v0`

That task may implement a deterministic route-table dry-run script only. The
script may read the public placeholder manifest and catalog metadata, validate
known IDs and paths, and emit copied-reference route-table data plus explicit
missing-input or refusal records.

Everything else remains blocked:

- generated review packets
- generated or rewritten biomedical claims
- generated public explainers or medical summaries
- target, therapy, trial, mechanism, source, artifact, task, or evidence ranking
- patient matching, treatment selection, trial selection, or expanded-access
  routing
- real case data, private records, free-text notes, images, or dates tied to a
  person
- publication authorization or expert-review substitution

## Allowed Future Code Slice

The selected future script may:

- read `schemas/review-packet-builder-manifest-template-v0.json`
- validate manifest shape through existing `make validate` behavior
- read public artifact catalog metadata for IDs, paths, claim levels, review
  status, and limitations
- produce a route table with copied IDs, copied paths, copied boundary text,
  validation status, missing-input records, and refusal reasons
- fail closed when required source, limitation, review, boundary, schema, or
  path fields are missing

The selected future script must not:

- call external services
- accept arbitrary case uploads or private records
- generate prose claims, review packets, evidence summaries, recommendations,
  rankings, patient-specific outputs, or public explainers
- mutate source artifacts
- publish or authorize publication

## Required First-Code Acceptance

Before the future route-table script can be treated as complete, it must:

- run locally without credentials, network access, paid services, or accounts
- use only public repo files
- include a fixture based on the public placeholder manifest
- include a refusal fixture for a forbidden field
- include validation or test coverage that fails closed
- document that the script output is not a review packet, not expert review,
  not medical advice, and not publication-ready text

## Step 26 Status

[Review-Packet Manifest Route-Table Dry-Run Tool v0](../../../tools/review_packet_manifest_route_table.py)
now completes the selected first code slice. It reads only public repo files,
emits copied-reference routes, reports missing inputs, and refuses forbidden
fields. It includes a placeholder fixture, a forbidden-field refusal fixture,
and a self-test for forbidden fields, missing paths, unknown source IDs, and
missing clinical-use boundaries.

The next bounded task is
`multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0`.
That task should validate route-table output records before any downstream
workflow can rely on them. Packet assembly, generated biomedical prose,
rankings, recommendations, patient matching, trial matching, expanded-access
guidance, and publication workflow remain blocked.

Step 27 status:
[Review-Packet Route-Table Output Schema v0](../../../schemas/review-packet-route-table-output-schema-v0.md)
now validates route-table output records. The next bounded task is the no-code
`multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0`, which
must decide whether packet assembly remains blocked before any review-packet
output is attempted.

## Limitations

- This is an implementation gate, not a working builder.
- It is source-checked planning, not expert review.
- It permits only a copied-reference route-table dry-run script and an output
  schema gate before any downstream packet workflow.
- It does not generate review packets or biomedical claims.
- It does not prove source coverage is complete.
- It does not make any artifact expert-reviewed.
- It does not make any claim stronger.
- It does not rank evidence, targets, therapies, trials, sources, mechanisms,
  artifacts, tasks, or questions.
- It does not authorize publication.
- It does not provide medical advice, diagnostic guidance, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
