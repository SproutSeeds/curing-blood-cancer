# Multiple Myeloma Public Inventory v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-public-inventory-v0`
- claim level: open-question
- inventory status: public v0 current-state map
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This inventory summarizes what the public multiple myeloma lane contains now.
It is written for maintainers, contributors, researchers, advocates, and
builders who need the repo's current shape without private context.

It is not a scientific review, clinical review, patient guide, treatment
guide, trial guide, or cure claim.

## At A Glance

After the expert-validation outreach map is cataloged, the public multiple
myeloma surface contains 49 metadata-tracked artifacts:

| Class | Count | Meaning |
| --- | ---: | --- |
| dataset | 15 | Catalogs, public task queues, evidence-gap records, measurement context, issue indexes, outreach maps, source registry, and synthetic examples. |
| map | 4 | Cure-wedge, open research, concept, and mechanism maps. |
| protocol | 20 | Roadmaps, gates, review plans, handoffs, checklists, and review-packet protocols. |
| schema | 8 | Validated shapes for disease maps, target records, therapy records, trial landscapes, open questions, case summaries, and review-packet routing. |
| taxonomy | 1 | Multiple myeloma treatment-class vocabulary. |
| tool | 1 | Review-packet manifest route-table dry-run tool. |

## What Exists

| Area | Current Public Artifacts | Status |
| --- | --- | --- |
| Program navigation | [Public Roadmap v0](public-roadmap-v0.md), [Open Research Map v0.1](open-research-map-v0-1.md), [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md), [Public Review And Release Gate v0](public-review-release-gate-v0.md), this inventory, and the release-gate pass. | Navigable public v0 surface. |
| Case-to-cure plumbing | [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md), [Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md), [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md), [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md), and [Publication-Gate Checklist v0](publication-gate-checklist-v0.md). | Public-safe shape only; no real case data or patient-specific advice. |
| Evidence and gaps | [BCMA Antigen Escape Claim Set v0](evidence-claims/bcma-antigen-escape-claim-set-v0.md), [BCMA Antigen Escape Evidence Gap Register v0](evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md), measurement audits, and public task queues. | Source-backed and limitation-heavy; expert review still needed. |
| Mechanism work | [Post-CAR T Relapse Mechanism Map v0](mechanisms/post-car-t-relapse-mechanism-map-v0.md), extraction guide, extraction records, and coverage report. | Navigation coverage only; counts are not evidence-strength rankings. |
| Review readiness | [BCMA Claim Set Expert Review Packet v0](reviews/bcma-claim-set-expert-review-packet-v0.md), [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md), [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md), [Expert Validation Outreach Map v0](reviews/expert-validation-outreach-map-v0.md), manifest specs, dry-run plans, packet-assembly gates, and recombination handoff. | Expert-review-needed; 13 public validation issues are opened; outreach candidates are mapped; packet assembly remains blocked. |
| Schemas and tools | Disease-map, target, therapy, trial-landscape, open-question, review-packet manifest, route-table output, and case-feature summary schemas, plus the route-table dry-run tool. | Validated public tooling substrate; no generated clinical claims. |
| Source anchors | [Source Registry v0](../../sources/source-registry-v0.md), [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md), and [Treatment-Class Taxonomy v0](../../taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md). | Reusable public provenance anchors; not proof of completeness. |

## Current Readiness

| Question | Current Answer |
| --- | --- |
| Is the public v0 artifact surface complete for the current autonomous loop? | Yes, for the definition-of-complete used by the public loop handoff. |
| Are there ready public tasks left in the current queues? | No. The current ready-task listing reports zero ready tasks. |
| Is the public surface ready for protected-branch review? | Yes, after validation and release-gate checks pass. |
| Is the science complete? | No. The repo keeps source scope, uncertainty, and limitations visible. |
| Are claims expert-reviewed? | No. Review packets still mark expert-review-needed items. |
| Are public expert-validation issues opened? | Yes. Issues [#22](https://github.com/SproutSeeds/curing-blood-cancer/issues/22) through [#34](https://github.com/SproutSeeds/curing-blood-cancer/issues/34) map to the current 13 review items. |
| Is this a patient-care system? | No. It is public research infrastructure only. |
| Does this contain real case data? | No. The public lane uses synthetic examples and blocker registers. |
| Can it guide treatment, trial selection, monitoring, or expanded access? | No. Those uses remain explicitly blocked. |

## Most Useful Entry Points

Start here:

1. [Public Roadmap v0](public-roadmap-v0.md) for the initiative plan.
2. [Open Research Map v0.1](open-research-map-v0-1.md) for the first
   source-backed myeloma map.
3. [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
   for the public-safe pipeline shape.
4. [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
   for why the autonomous v0 loop stopped.
5. [Public Review And Release Gate v0](public-review-release-gate-v0.md) for
   release constraints.
6. [Public Review Release Gate Pass v0](public-review-release-gate-pass-v0.md)
   for the current PR-readiness pass.
7. [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md)
   for the public expert-review request surface.
8. [Expert Validation Outreach Map v0](reviews/expert-validation-outreach-map-v0.md)
   for the public shortlist of people and reviewer lenses to contact.
9. [Public Artifact Catalog v0](../../artifacts/public-artifact-catalog-v0.md)
   for the full metadata-backed listing.

## What Comes Next

The next public-safe work should start only after protected-branch review.
Useful next phases include:

- expert-review response tracking and artifact updates from issues #22 through
  #34
- source-backed map expansion with a new gate and explicit source rules
- plain-language review for patients, caregivers, and public contributors
- synthetic-only tooling checks that preserve no-ranking and no-advice
  boundaries
- private-lab handoffs outside this public repo when real case work is needed

## What This Is Not

This inventory is not:

- medical advice
- diagnosis, prognosis, treatment, trial, eligibility, monitoring, or
  expanded-access guidance
- a target, therapy, trial, source, mechanism, artifact, task, or evidence
  ranking
- expert review
- clinical review
- a claim that multiple myeloma has been cured
- a claim that any vaccine has been found
- authorization to process public case data
- authorization to publish case-derived learning

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No credentials, paid APIs, account changes, or restricted datasets.
- No patient-specific diagnosis, prognosis, treatment, trial, expanded-access,
  monitoring, or candidate-option guidance.
- No target, therapy, trial, source, mechanism, artifact, task, or evidence
  ranking.
- No generated biomedical claims.
- No expert-review substitution.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This inventory is a navigation artifact, not a scientific review.
- This inventory does not prove source coverage is comprehensive.
- This inventory does not grade evidence quality.
- This inventory does not make claims expert-reviewed.
- This inventory does not inspect private lab records or real case data.
- This inventory does not authorize generated claims, ranking,
  recommendation behavior, patient matching, trial matching, review-packet
  assembly, or publication workflow.
- This inventory does not provide medical advice, diagnostic guidance,
  treatment guidance, trial guidance, eligibility guidance, expanded-access
  guidance, monitoring guidance, or a cure claim.
