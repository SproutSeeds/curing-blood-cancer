# Review-Packet Builder Dry-Run Plan v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-review-packet-builder-dry-run-plan-v0`
- source task: `multiple-myeloma-review-packet-builder-dry-run-plan-task-v0`
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- implementation boundary: dry-run plan only, no builder code
- last reviewed: `2026-04-15`

## Purpose

This plan defines a no-code dry run for a future public review-packet builder.
It exists after the validated [Review-Packet Builder Manifest Schema v0](../../../schemas/review-packet-builder-manifest-schema-v0.md)
and before any review-packet-builder implementation.

The dry run names what a future builder may copy, reference, omit, or refuse
when reading a public placeholder manifest. It must not generate review
packets, rewrite biomedical claims, rank evidence, match patients, select
trials, recommend therapies, authorize publication, or ingest private case
data.

## Boundary

- Public artifacts only.
- Public placeholder manifests only.
- No real case data.
- No patient identifiers.
- No dates tied to a person.
- No free-text clinical notes, raw records, images, re-identification keys, or
  private lab exports.
- No generated biomedical claims.
- No generated public explainer text.
- No evidence-strength ranking.
- No clinical priority, urgency, or patient-relevance fields.
- No treatment recommendation.
- No trial recommendation.
- No eligibility, availability, sponsor-access, or expanded-access guidance.
- No publication authorization.
- No cure claim.
- No builder code.

## Dry-Run Input

The only allowed input for this dry run is the public placeholder manifest:

- `schemas/review-packet-builder-manifest-template-v0.json`

The dry run may inspect that placeholder manifest against:

- `schemas/review-packet-builder-manifest.schema.json`
- `schemas/review-packet-builder-manifest-schema-v0.md`
- `disease-programs/multiple-myeloma/reviews/review-packet-builder-manifest-spec-v0.md`
- `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md`
- `disease-programs/multiple-myeloma/tooling-readiness-gate-v0.md`
- `artifacts/public-artifact-catalog-v0.json`
- `sources/source-registry-v0.json`

Do not substitute any real case material, private records, reviewer identities,
or generated content for missing manifest fields.

## No-Generated-Claims Policy

A future builder may route public references, but it must not create new
biomedical prose.

| Input | Allowed Behavior | Required Refusal |
| --- | --- | --- |
| Existing public artifact title, ID, path, metadata path, artifact class, claim level, review status, and limitation text | Copy exact identifiers and path references into a route table. | Do not summarize, strengthen, soften, or rewrite artifact claims. |
| Public source IDs already present in `source-registry-v0` | Reference IDs and registry paths. | Do not infer efficacy, safety, eligibility, availability, patient fit, or source quality from source presence. |
| Public claim IDs, gap IDs, mechanism group IDs, measurement term IDs, task IDs, query-record IDs, and extraction-record IDs | Reference IDs for reviewer navigation. | Do not rank IDs or convert inclusion into evidence strength, clinical priority, or publication readiness. |
| Required sections from a public review packet template | Copy section labels and required input categories. | Do not fill sections with generated biomedical claims, case facts, recommendations, or reviewer conclusions. |
| Missing inputs | Report explicit missingness and linked public tasks or blocker notes. | Do not invent substitutes, infer omitted fields, or produce fallback clinical text. |
| Unsafe inputs or forbidden fields | Stop the dry run and report the refusal reason. | Do not sanitize and continue when the input includes patient identifiers, real case data, recommendations, rankings, generated claims, publication authorization, or private records. |

## Copy, Reference, Omit, Refuse

| Decision | Meaning | Examples |
| --- | --- | --- |
| Copy | Reuse exact public identifiers, paths, section labels, limitation text, and boundary labels without changing meaning. | Artifact ID, metadata path, schema path, review status, clinical-use boundary. |
| Reference | Link to public IDs for reviewer navigation without creating new assertions. | Claim IDs, gap IDs, source IDs, mechanism group IDs, task IDs. |
| Omit | Leave a packet field empty when a required public input is absent and name the missing input. | Missing expert review status, missing source coverage, missing validation output. |
| Refuse | Stop the dry run when input would breach the public safety boundary. | Patient identifiers, real case facts, free-text notes, generated recommendations, trial matching, publication authorization. |

## Dry-Run Steps

1. Validate the placeholder manifest with `make validate`.
2. Confirm all `builder_code_boundary` flags remain `false`.
3. Confirm the manifest references only public artifact IDs, paths, metadata
   paths, schemas, source IDs, and public reference IDs.
4. Build a route table in prose only, mapping each manifest section to copy,
   reference, omit, or refuse behavior.
5. Report missing inputs explicitly with their linked public task or blocker.
6. Refuse the dry run if any input includes patient identifiers, real case data,
   private records, generated biomedical claims, recommendations, rankings,
   expanded-access guidance, publication authorization, or cure claims.
7. Do not create code, packet output, generated claims, generated summaries, or
   patient-specific artifacts.

## Dry-Run Route Table

| Manifest Section | Dry-Run Behavior | Output Boundary |
| --- | --- | --- |
| Manifest identity | Copy public manifest ID, date, disease program, title, and packet type. | No inference about review completion or publication readiness. |
| Target packet | Reference the public packet template ID and path. | Do not fill packet sections. |
| Artifact inputs | Copy public IDs, paths, metadata paths, claim levels, review status, and limitations. | Do not summarize or rewrite artifact claims. |
| Schema inputs | Reference schema and template paths. | Schema validity checks shape only. |
| Source inputs | Reference source IDs and source registry path. | Source IDs do not imply clinical actionability. |
| Reference IDs | Reference IDs for reviewer navigation. | IDs are not rankings, priorities, or recommendations. |
| Missing inputs | Omit generated substitutes and route to public tasks or blockers. | Missing inputs remain missing. |
| Validation expectations | Copy required fail-closed checks. | Validation is not expert review. |
| Clinical-use boundary | Copy required no-use statements. | No medical advice or guidance. |
| Builder-code boundary | Copy required false flags. | No builder code or generated packet output. |

## Required Refusals

The dry run must stop if the manifest or proposed inputs include:

- patient identifiers, real case data, free-text notes, raw records, images, or
  private records
- generated biomedical claims, generated summaries, generated explainers, or
  rewritten claim language
- treatment recommendations, trial recommendations, eligibility guidance,
  enrollment advice, availability claims for any person, expanded-access
  guidance, or sponsor-access instructions
- clinical priority, urgency, evidence-strength ranking, patient relevance,
  actionability, candidate options, or option ranking
- publication authorization or reviewer identity disclosure
- cure, vaccine, or established-treatment claims

## Implementation Gate

This dry-run plan does not authorize builder code.

[Review-Packet Builder Implementation Gate v0](review-packet-builder-implementation-gate-v0.md)
now confirms that only a deterministic copied-reference route-table dry-run
script may proceed. It requires:

- the manifest schema and placeholder template still validate
- the dry-run route table is sufficient for a first code slice
- the first code slice has no generated-claim behavior
- output is limited to copied identifiers, copied boundary text, public paths,
  and explicit missing-input reports
- refusal behavior is tested before any public packet assembly
- the tool cannot accept real case data or private records
- the tool cannot rank or recommend targets, therapies, trials, mechanisms,
  sources, artifacts, tasks, or patient options

## Limitations

- This is a dry-run plan, not a builder.
- It is source-checked planning, not expert review.
- It does not generate review packets or biomedical claims.
- It does not prove that source coverage is complete.
- It does not make any artifact expert-reviewed.
- It does not make any claim stronger.
- It does not rank evidence, targets, therapies, trials, sources, mechanisms,
  artifacts, tasks, or questions.
- It does not authorize publication.
- It does not provide medical advice, diagnostic guidance, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, or a cure claim.
