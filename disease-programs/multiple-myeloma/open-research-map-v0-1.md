# Multiple Myeloma Open Research Map v0.1

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-open-research-map-v0-1`
- artifact class: map
- claim level: open-question
- machine-readable companion: [`open-research-map-v0-1.json`](open-research-map-v0-1.json)
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This map is the first public navigation surface for the multiple myeloma lane.
It connects the cure wedge, source registry, measurement glossary, relapse
mechanism map, evidence gaps, public task queues, case-to-cure safety plumbing,
and review packets into one source-backed orientation layer.

It is not a systematic review, clinical pathway, treatment ranking, trial
finder, expanded-access guide, prognosis tool, monitoring plan, or cure claim.

## Scope

In scope:

- multiple myeloma and related plasma-cell disease context
- durable measurable-residual-disease-negative remission as a cure-oriented
  research question
- relapse and resistance mechanisms after immune therapy, especially post-BCMA
  and post-CAR T settings where public artifacts already exist
- public measurement terms for MRD, response, relapse, target status, and
  antigen density
- public-source trial, regulatory, literature, and review-readiness lanes
- public contribution tasks that improve source coverage, schemas, and review
  readiness

Out of scope:

- patient-specific diagnosis, prognosis, treatment selection, trial selection,
  expanded-access selection, monitoring instructions, or candidate-option
  ranking
- private records, real case facts, re-identification keys, raw notes, images,
  exact dates tied to a person, or restricted datasets
- claims that multiple myeloma has been cured or that any vaccine, biomarker,
  target, trial, or therapy is established for any person
- comprehensive coverage across all myeloma disease states

## Claim Legend

| Label | Meaning In This Map | Required Boundary |
| --- | --- | --- |
| `fact` | A source-backed orientation statement from a public artifact or public source. | Preserve source ID and scope. |
| `derived claim` | A statement produced by a documented public artifact, extraction, or map. | Preserve method, source IDs, and limitations. |
| `hypothesis` | A research idea or mechanism lane needing stronger extraction or review. | Do not present as established or actionable. |
| `open question` | A known unknown or contribution target. | Name what source, schema, or review work is missing. |
| `do-not-use clinically` | A safety boundary or blocked interpretation. | Keep separate from decision-support language. |

## Map Nodes

| Node | Claim Label | What It Navigates | Source IDs And Public Anchors | Current Use | Do Not Infer |
| --- | --- | --- | --- | --- | --- |
| `disease-scope-and-wedge-v0-1` | fact + open question | Multiple myeloma and plasma-cell disease as the first cure-oriented wedge. | `nci_pdq_myeloma_hp`; [Cure Wedge v0](cure-wedge-durable-mrd-negative-remission-v0.md); [Public Roadmap v0](public-roadmap-v0.md) | Orient contributors to the durable MRD-negative remission and relapse-prevention question. | Do not infer that a cure has been found or that the wedge applies to any person. |
| `deep-response-measurement-v0-1` | fact + derived claim + open question | MRD, response, relapse, target-status, antigen-density, and endpoint vocabulary. | `nci_pdq_myeloma_hp`, `pubmed_kumar_2016_imwg_mrd_response_criteria`, `pubmed_munshi_2017_mrd_survival_meta_analysis`, `pubmed_soh_2022_mrd_flow_harmonization`; [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md) | Keep measurement terms visible before comparing papers, trials, or mechanism claims. | Do not treat MRD negativity, response, target status, or antigen density as cure, prognosis, or treatment guidance. |
| `post-car-t-relapse-mechanisms-v0-1` | derived claim + hypothesis + open question | Mechanism buckets after deep response or post-CAR T relapse. | `pubmed_tedder_bhutani_2025_bcma_resistance`, `pubmed_ledergor_2024_cd4_car_t_exhaustion`, `pubmed_antigen_escape_bcma_directed_2024`, `pubmed_yue_2025_bcma_resistance`, `pubmed_di_meo_2025_sema4a_low_bcma`, `pubmed_plasma_cell_identity_escape_2025`; [Post-CAR T Relapse Mechanism Map v0](mechanisms/post-car-t-relapse-mechanism-map-v0.md); [Coverage Report v0](mechanisms/post-car-t-relapse-mechanism-coverage-v0.md) | Navigate target escape, immune fitness, plasma-cell identity, disease-context, dual-target, and measurement-gap lanes. | Do not infer mechanism frequency, patient relevance, product comparison, or treatment sequencing. |
| `bcma-antigen-escape-and-alternate-targets-v0-1` | derived claim + hypothesis | BCMA target status, TNFRSF17 alteration, low BCMA, SEMA4A, and multi-factorial resistance language. | `pubmed_antigen_escape_bcma_directed_2024`, `pubmed_di_meo_2025_sema4a_low_bcma`, `pubmed_yue_2025_bcma_resistance`; [BCMA Claim Set v0](evidence-claims/bcma-antigen-escape-claim-set-v0.md); [BCMA Evidence Gap Register v0](evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md) | Preserve source-backed claim boundaries and route under-covered mechanisms into public tasks. | Do not infer target actionability, alternate-target readiness, clinical efficacy, or clinical safety. |
| `trial-and-regulatory-landscape-v0-1` | fact + open question + do-not-use clinically | Trial-query provenance, registry snapshots, and regulatory-source boundaries. | `clinicaltrials_gov`, `clinicaltrials_gov_api_v2`, `fda_drugs_at_fda`; [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md); [CAR T Query Record Example](../../examples/multiple-myeloma-car-t-query-record-v0.json) | Keep trial and regulatory records source-linked before any landscape artifact is built. | Do not infer eligibility, availability, enrollment advice, sponsor access, regulatory feasibility, efficacy, or safety. |
| `case-to-cure-public-plumbing-v0-1` | open question + do-not-use clinically | Public-safe case-to-cure interfaces that support private work without public case data. | `nci_pdq_myeloma_hp`, `clinicaltrials_gov_api_v2`, `pubmed`, `fda_drugs_at_fda`; [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md); [Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md); [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md) | Route private-lab templates, public feature summaries, trial-query provenance, candidate rubric, and publication gates. | Do not upload, infer, or reconstruct real case data in public. |
| `candidate-review-and-publication-gates-v0-1` | do-not-use clinically + open question | No-action candidate-option review readiness and fail-closed publication gating. | [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md); [Publication-Gate Checklist v0](publication-gate-checklist-v0.md); [Private To Public Workflow](../../docs/private-to-public-workflow.md); [Public Safety](../../governance/PUBLIC_SAFETY.md) | Keep public review, private governance, and release-readiness boundaries visible. | Do not infer candidate ranking, clinical action, publication authorization, or private governance completion. |
| `expert-review-readiness-v0-1` | open question + do-not-use clinically | Source-checked versus expert-reviewed status, reviewer roles, and public review packet paths. | [BCMA Claim Set Expert Review Packet v0](reviews/bcma-claim-set-expert-review-packet-v0.md); [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md) | Make review needs traceable before public explainers or stronger claims are attempted. | Do not infer expert review has occurred because a packet exists. |
| `contribution-queue-v0-1` | open question | Public work items for map, source registry, schema, and review infrastructure. | [Multiple Myeloma Roadmap Public Task Queue v0](public-tasks/multiple-myeloma-roadmap-public-task-queue-v0.md); [BCMA Public Task Queue v0](public-tasks/bcma-antigen-escape-public-task-queue-v0.md); [Post-CAR T Mechanism Gap Public Task Queue v0](public-tasks/post-car-t-relapse-mechanism-gap-public-task-queue-v0.md) | Show contributors where source extraction, schema, registry, and review work should land next. | Do not treat task priority as evidence strength, patient relevance, or clinical importance. |

## Current Source-Backed Lanes

| Lane | Ready Public Anchors | Missing Or Under-Covered Work |
| --- | --- | --- |
| Disease and outcome frame | Cure wedge, public roadmap, source registry, NCI PDQ source ID. | Broader disease-state tables for frontline, relapsed, refractory, precursor, and post-cellular-therapy settings. |
| MRD and relapse measurement | Measurement glossary, MRD consensus and meta-analysis source IDs. | Extraction checks for MRD threshold, specimen, timing, confirmation interval, imaging context, and follow-up duration. |
| Post-CAR T and post-BCMA relapse biology | Mechanism map, coverage report, claim set, extraction records, BCMA evidence gaps, plasma-cell identity second-source coverage, and disease-burden/site-risk second-source context coverage. | More non-BCMA, non-CAR T, bispecific, high-risk, microenvironment, immune-reconstitution, sequencing, and primary-study extraction lanes. |
| Trial and regulatory navigation | ClinicalTrials.gov query protocol, query record example, FDA, DailyMed, EMA, WHO ICTRP, and ClinicalTrials.gov API source anchors. | Dedicated trial landscape map, registry freshness fields, product/source taxonomy, and explicit no-eligibility validators. |
| Case-to-cure public safety plumbing | Blueprint, synthetic fixture, case-feature summary, candidate rubric, publication gate. | Private-only template work remains outside this repo; public validators for case-derived release records are still future work. |
| Review readiness | BCMA review packet and multidisciplinary template. | Completed qualified expert comments and follow-up artifact updates are not present. |
| Contribution workflow | Roadmap task queue, issue drafts, disease-map schema, and JSON companion. | Broader non-BCMA gap register and source-specific extraction tests remain unresolved. |

## Open Questions For v0.2

1. Which additional source-specific extraction rules are required before the
   map can compare coverage across target, therapy, trial, regulatory, and
   dataset classes beyond the current BCMA/post-CAR T emphasis?
2. Which disease-map schema fields need refinement after the first
   machine-readable companion is drafted and validated?
3. Which deeper relapse-mechanism source classes need explicit public tasks
   before the map expands beyond current v0 navigation coverage?
4. Which trial-query fields are enough for landscape navigation while still
   blocking eligibility, availability, and recommendation inferences?
5. Which review packet items must be completed before public explainers or
   stronger educational summaries can reuse this map?
6. Which aggregate case-derived learnings, if any, can pass the publication gate
   without exposing real case facts?

## Current Contribution Targets

| Target | Public Task | Why It Is Next |
| --- | --- | --- |
| Definition-of-complete audit | no ready task selected yet | The review-builder recombination handoff is complete; the next move is to audit the public loop against completion criteria before selecting any new task. |
| Source registry expansion follow-up | `multiple-myeloma-source-registry-expansion-task-v0` | Initial target, therapy, trial, regulatory, labeling, and dataset anchors are present; future work should add source-specific extraction needs as maps and tooling demand them. |
| Open research map refinement | `multiple-myeloma-open-research-map-task-v0` follow-up | v0.1 is a navigation layer, not comprehensive coverage. |
| Expert review | `multiple-myeloma-multidisciplinary-review-packet-task-v0` and BCMA review items | Stronger public language should wait for mapped qualified review. |

The [Schema And Tooling Phase Inventory v0](schema-tooling-phase-inventory-v0.md)
is the current phase-boundary artifact. It marks the second-source extraction
coverage pass complete for v0 navigation. [Target Record Schema v0](../../schemas/target-record-schema-v0.md)
and [Therapy Record Schema v0](../../schemas/therapy-record-schema-v0.md) now
validate the public target and therapy-context shapes.
[Trial-Landscape Record Schema v0](../../schemas/trial-landscape-record-schema-v0.md)
now validates registry-landscape provenance and no-eligibility boundaries, and
[Open-Question Record Schema v0](../../schemas/open-question-record-schema-v0.md)
now validates public research-question shape. [Tooling Readiness Gate v0](tooling-readiness-gate-v0.md)
keeps implementation tooling blocked and selects a review-packet builder input
manifest specification as the first spec-only slice.
[Review-Packet Builder Input Manifest Spec v0](reviews/review-packet-builder-manifest-spec-v0.md)
now defines the manifest field boundary, and [Review-Packet Builder Manifest
Schema v0](../../schemas/review-packet-builder-manifest-schema-v0.md) now
validates public input manifests. [Review-Packet Builder Dry-Run Plan v0](reviews/review-packet-builder-dry-run-plan-v0.md)
now defines no-code copy, reference, omit, and refuse behavior. Builder code
is limited by [Review-Packet Builder Implementation Gate v0](reviews/review-packet-builder-implementation-gate-v0.md)
to a deterministic copied-reference route-table dry-run script only.
[Review-Packet Manifest Route-Table Dry-Run Tool v0](../../tools/review_packet_manifest_route_table.py)
now implements that first bounded code slice. [Review-Packet Route-Table Output
Schema v0](../../schemas/review-packet-route-table-output-schema-v0.md)
validates route-table output records. [Review-Packet Builder Packet-Assembly
Gate v0](reviews/review-packet-builder-packet-assembly-gate-v0.md) keeps
packet assembly blocked and selects a no-code packet-skeleton specification as
the next bounded work object. [Review-Packet Builder Packet-Skeleton Spec v0](reviews/review-packet-builder-packet-skeleton-spec-v0.md)
now completes that no-code slice with empty section slots only. No downstream
schema, validator, packet-output, or builder task is selected without a
recombination handoff. [Review-Packet Builder Recombination Handoff v0](reviews/review-packet-builder-recombination-handoff-v0.md)
now completes that handoff and points to a definition-of-complete audit.

## Review And Publication Boundaries

- Source-checked does not mean expert-reviewed.
- Artifact coverage does not mean evidence strength.
- A source ID does not mean the source supports a clinical action.
- A trial registry record does not mean a trial is available, appropriate, or
  eligible for any person.
- A mechanism hypothesis does not rank treatment choices.
- A publication-gate checklist does not authorize public release of real case
  facts without private governance.

## How The Machine-Readable Companion Is Used

This v0.1 map was drafted Markdown-only because a disease-map schema did not
exist yet. [Disease Map Schema v0](../../schemas/disease-map-schema-v0.md) now
defines the stable shape for disease-map, target, therapy, trial,
open-question, and public-task records. The
[JSON companion](open-research-map-v0-1.json) validates against that schema so
future extraction helpers, evidence graph tooling, or map builders can reuse a
stable contract. `Target Record Schema v0` and `Therapy Record Schema v0` now
define standalone target and therapy-context shapes. `Trial-Landscape Record
Schema v0` now defines standalone registry-landscape provenance and freshness
shape. `Open-Question Record Schema v0` now defines standalone research-question
shape. `Tooling Readiness Gate v0` now records the no-tooling-yet aggregate
decision: implementation remains blocked, and the first selected work object
was a review-packet builder input manifest specification. That specification
led to a validated manifest schema, no-code dry-run plan, and implementation
gate. The copied-reference route-table dry-run script and route-table output
schema now exist. The packet-assembly gate keeps assembly blocked and selects
a no-code packet-skeleton specification, which now exists. The next action is
definition-of-complete audit before any new downstream task is selected.
Schema validation checks shape only; it does not make any map node true,
comprehensive, expert-reviewed, clinically actionable, or relevant to any
person.

## Review Boundary

This map organizes public research artifacts. It is not medical advice,
diagnostic guidance, treatment guidance, trial guidance, expanded-access
guidance, monitoring guidance, or a claim that multiple myeloma has been cured.
