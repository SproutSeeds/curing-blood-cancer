# Multiple Myeloma Public Roadmap v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- roadmap status: `active-v0`
- claim level: `open-question`
- last reviewed: `2026-04-15`
- clinical boundary: research roadmap, not medical advice

## Purpose

This is the canonical public plan for turning the multiple myeloma lane inside
Curing Blood Cancer into a source-backed research engine.

The goal is not to claim that a cure has been found. The goal is to make the
path toward cure-oriented questions easier to inspect, improve, reproduce, and
share from public evidence.

## Operating Frame

The public repo should become trustworthy first, useful second, and
computational third.

That means:

- every claim carries scope, source IDs, and uncertainty
- public artifacts are readable without private lab context
- private lab work is downstreamed only after sanitation and review
- source registries and evidence maps come before dashboards or claims
- the first multiple myeloma wedge stays narrow enough to produce real artifacts
- tools should help people ask better questions before they rank answers

## Roadmap Sequence

### 1. Define The Wedge

The first disease wedge is durable measurable-residual-disease-negative
remission and relapse prevention in multiple myeloma.

This work defines:

- disease and disease-state scope
- cure-oriented outcome questions
- what belongs in public
- what must remain private or excluded
- measurement terms that must not be flattened
- failure modes that deserve structured tracking

Canonical starting artifact:

- [Cure Wedge v0](cure-wedge-durable-mrd-negative-remission-v0.md)

Done when:

- the wedge has inclusion and exclusion rules
- the key outcome and failure-mode terms are public and source-backed
- non-specialists can tell what this program is and is not trying to do

### 2. Build The Evidence Map

The evidence map should organize what is known, what is uncertain, and where
source-backed extraction is still missing.

Initial map domains:

- disease biology and plasma-cell identity
- high-risk disease contexts and subtype markers
- immune environment and immune escape
- treatment classes and combination strategies
- MRD, relapse, response, and durability measurements
- post-CAR T and post-BCMA relapse mechanisms
- trial landscape signals
- public-source evidence gaps

Current starting artifacts:

- [Post-CAR T Relapse Mechanism Map v0](mechanisms/post-car-t-relapse-mechanism-map-v0.md)
- [Post-CAR T Relapse Mechanism Coverage Report v0](mechanisms/post-car-t-relapse-mechanism-coverage-v0.md)
- [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md)
- [BCMA Antigen Escape Evidence Gap Register v0](evidence-gaps/bcma-antigen-escape-evidence-gap-register-v0.md)

Done when:

- map records distinguish fact, derived claim, hypothesis, and open question
- every map node has provenance or is marked as needing extraction
- contributors can see exactly which missing extractions would improve the map

### 3. Expand The Source Registry

The source registry is the public answer to: where does truth come from here?

It should track:

- source owner
- source type
- stable URL or accession
- access date
- disease scope
- claim uses
- claim limits
- redistribution constraints where relevant

Priority public source classes:

- NCI summaries and public cancer references
- PubMed-indexed literature
- ClinicalTrials.gov records and API v2 snapshots
- FDA labels, approvals, and review records
- treatment-class and target taxonomies
- public datasets that can be redistributed or referenced safely

Canonical starting artifact:

- [Source Registry v0](../../sources/source-registry-v0.md)

Done when:

- every public artifact cites stable source IDs where possible
- source IDs are reusable across claim sets, maps, protocols, and tasks
- sources are explicit about what they cannot prove

### 4. Implement The Artifact Pipeline

The pipeline should turn public sources into clean public artifacts without
blurring provenance.

Initial artifact families:

- `sources.json`
- `disease-map.json`
- `targets.json`
- `therapies.json`
- `trials.json`
- `open-questions.json`
- public task queues
- review packets
- readable Markdown companions

Pipeline requirements:

- generated or derived records keep source IDs
- schemas describe the shape before tools depend on it
- validation runs before publication
- private upstream context is never required to use public output
- public-safe limitation text is present on every artifact

Current schema/tooling phase:

- `Disease Map Schema v0`, `Target Record Schema v0`, `Therapy Record Schema
  v0`, and `Trial-Landscape Record Schema v0` now validate public map, target,
  therapy, and registry-landscape shapes.
- `Open-Question Record Schema v0` now validates public research-question
  records before evidence graph, map-builder, extraction-helper, or
  review-packet-builder tooling depends on question fields.
- [Tooling Readiness Gate v0](tooling-readiness-gate-v0.md) selects a
  review-packet builder input manifest specification as the first spec-only
  slice before any generator, dashboard, explorer, extraction helper, or
  review-packet builder code is added.
- [Review-Packet Builder Input Manifest Spec v0](reviews/review-packet-builder-manifest-spec-v0.md)
  defines manifest fields and fail-closed validation expectations.
- [Review-Packet Builder Manifest Schema v0](../../schemas/review-packet-builder-manifest-schema-v0.md)
  now validates public input manifests for future review-packet-builder work;
  [Review-Packet Builder Dry-Run Plan v0](reviews/review-packet-builder-dry-run-plan-v0.md)
  now defines no-code copy, reference, omit, and refuse behavior. Builder code
  remains limited by [Review-Packet Builder Implementation Gate v0](reviews/review-packet-builder-implementation-gate-v0.md),
  which conditionally selects only a deterministic copied-reference route-table
  dry-run script. [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../tools/review_packet_manifest_route_table.py)
  now implements that copied-reference slice. [Review-Packet Route-Table Output
  Schema v0](../../schemas/review-packet-route-table-output-schema-v0.md)
  validates route-table output records before downstream use. [Review-Packet
  Builder Packet-Assembly Gate v0](reviews/review-packet-builder-packet-assembly-gate-v0.md)
  keeps packet assembly blocked and selects a no-code packet-skeleton
  specification as the next safe step. [Review-Packet Builder Packet-Skeleton
  Spec v0](reviews/review-packet-builder-packet-skeleton-spec-v0.md) now
  defines empty section slots and copied route references only; the next action
  is aggregate recombination before any new downstream task is selected.
  [Review-Packet Builder Recombination Handoff v0](reviews/review-packet-builder-recombination-handoff-v0.md)
  now closes that lane and points to a definition-of-complete audit before any
  new task is selected. [Definition-Of-Complete Audit v0](definition-of-complete-audit-v0.md)
  now identifies the remaining public-loop gap as a case-specific private-lab
  blocker register, not more review-builder implementation.
  [Case-Specific Private-Lab Blocker Register v0](case-specific-private-lab-blocker-register-v0.md)
  now maps `case_00` through `case_14` to private-lab tasks or human-gated
  blockers without adding real case data or case-processing tools.
  [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
  now marks the current v0 autonomous public loop endpoint with no ready public
  task selected.
- Trial explorer tooling remains blocked until registry-landscape records are
  used only with freshness, provenance, uncertainty, and no-eligibility
  boundaries.

Current validation entrypoint:

```bash
make validate
```

Case-specific plumbing:

- [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
- [Multiple Myeloma Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md)

Done when:

- public artifacts can be regenerated or audited from documented inputs
- validators catch broken source, taxonomy, claim, gap, and task references
- new artifacts can be added without hand-building every index

### 5. Start Hypothesis Scoring

Hypothesis scoring should prioritize research directions without pretending to
make clinical decisions.

Scoring dimensions:

- evidence strength
- uncertainty and contradiction
- translational relevance
- feasibility from public data
- novelty or neglected value
- measurement clarity
- safety and overclaiming risk
- contribution readiness

Done when:

- scoring criteria are public and inspectable
- scores explain their evidence basis and limitations
- weak or speculative claims are visibly labeled
- no score is presented as medical advice, treatment advice, or trial advice

### 6. Publish The First Useful Public Artifact

The first major public release should be a multiple myeloma open research map.

Working target:

[Multiple Myeloma Open Research Map v0.1](open-research-map-v0-1.md)

It should help researchers, patients, advocates, builders, and funders see the
landscape more clearly without requiring them to trust private context.

The artifact should include:

- disease and outcome scope
- source registry links
- measurement glossary links
- treatment and target categories
- relapse mechanism map links
- known evidence gaps
- contribution-ready public tasks
- clear clinical-use boundary

Done when:

- the map is useful as a public navigation surface
- each section links to source-backed records
- the artifact is modest about uncertainty and does not claim a cure

### 7. Build Tools On Top

Tooling should sit on top of the evidence layer, not replace it.

Candidate tools:

- queryable evidence graph
- paper and trial extraction helpers
- trial landscape explorer
- target prioritization dashboard
- evidence-gap task generator
- review packet builder
- public explainer generator for non-specialists
- reproducible notebooks for selected public datasets

Done when:

- tools preserve source IDs and uncertainty
- outputs are reproducible or reviewable
- non-specialists can use public artifacts more safely
- expert reviewers can inspect the evidence path behind each output

## Canonical Workstreams

| Workstream | Canonical Path | Public Output |
| --- | --- | --- |
| Wedge definition | `disease-programs/multiple-myeloma/` | cure wedge and roadmap |
| Evidence claims | `disease-programs/multiple-myeloma/evidence-claims/` | source-backed claim sets |
| Evidence gaps | `disease-programs/multiple-myeloma/evidence-gaps/` | public gap registers |
| Measurements | `disease-programs/multiple-myeloma/measurements/` | MRD, relapse, and endpoint definitions |
| Mechanisms | `disease-programs/multiple-myeloma/mechanisms/` | relapse and resistance maps |
| Public tasks | `disease-programs/multiple-myeloma/public-tasks/` | contribution-ready issue queues |
| Reviews | `disease-programs/multiple-myeloma/reviews/` | expert-review packets |
| Trial maps | `disease-programs/multiple-myeloma/trial-maps/` | trial landscape artifacts |
| Shared sources | `sources/` | reusable source IDs |
| Shared schemas | `schemas/` | validation contracts |
| Shared tools | `tools/` | public validators and listing helpers |

## Private-To-Public Boundary

Public:

- source-backed derived artifacts
- public source IDs and extraction protocols
- sanitized summaries and review packets
- contribution-ready tasks
- reproducible public-data tools

Private:

- patient-identifying data
- private records
- restricted datasets
- credentials
- unreviewed exports
- lab notes that are not ready for public interpretation

Every public downstream artifact should be usable without access to the private
lab repo.

## Immediate Next Queue

1. Work the contribution-ready tasks in
   [Multiple Myeloma Roadmap Public Task Queue v0](public-tasks/multiple-myeloma-roadmap-public-task-queue-v0.md).
2. Use [Multiple Myeloma Open Research Map v0.1](open-research-map-v0-1.md)
   as the current navigation surface.
3. Use the
   [Schema And Tooling Phase Inventory v0](schema-tooling-phase-inventory-v0.md)
   as the phase boundary before adding generators.
4. Use [Tooling Readiness Gate v0](tooling-readiness-gate-v0.md) as the
   aggregate no-tooling-yet checkpoint.
5. Keep the validated trial-landscape and open-question shapes as public
   research context only, not eligibility, availability, enrollment, clinical
   priority, urgency, evidence-strength ranking, or guidance tooling.
6. Use [Review-Packet Builder Input Manifest Spec v0](reviews/review-packet-builder-manifest-spec-v0.md)
   as the spec-only boundary for future review-packet-builder inputs.
7. Use [Review-Packet Builder Manifest Schema v0](../../schemas/review-packet-builder-manifest-schema-v0.md)
   as the validated manifest boundary before any review-packet-builder code.
8. Use [Review-Packet Builder Dry-Run Plan v0](reviews/review-packet-builder-dry-run-plan-v0.md)
   as the no-code copy, reference, omit, and refuse boundary.
9. Use [Review-Packet Builder Implementation Gate v0](reviews/review-packet-builder-implementation-gate-v0.md)
   as the aggregate gate before any review-packet-builder implementation.
10. Build only `multiple-myeloma-review-packet-builder-route-table-script-task-v0`
   as the first copied-reference dry-run code slice; keep packet assembly,
   generated packet output, and generated biomedical claim handling blocked.
11. Define `multiple-myeloma-review-packet-builder-route-table-output-schema-task-v0`
   before any downstream workflow relies on route-table output records.
12. Use `multiple-myeloma-review-packet-builder-packet-assembly-gate-task-v0`
   as a no-code aggregate gate before any review-packet output or packet
   assembly work.
13. Define `multiple-myeloma-review-packet-builder-packet-skeleton-spec-task-v0`
   as a no-code empty-section skeleton before any packet assembly output.
14. Run an aggregate review-packet-builder recombination handoff before any
   new packet-output, schema, validator, or builder task is selected.
15. Use [Definition-Of-Complete Audit v0](definition-of-complete-audit-v0.md)
   as the aggregate audit across roadmap items, case-to-cure
   stages, synthetic fixtures, source registry sufficiency, validators,
   navigation, and remaining private-lab or human-gated blockers.
16. Use [Case-Specific Private-Lab Blocker Register v0](case-specific-private-lab-blocker-register-v0.md)
   as the public-safe blocker map before any real case tooling.
17. Use [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
   as the current endpoint for the v0 public loop; select no new public task
   without a new named phase, human review, or aggregate gate.
18. Build artifact-generation scripts, evidence graph tooling, target
   prioritization views, trial explorers, extraction helpers, or review-packet
   builders only after their input shapes validate.

## Review Boundary

This roadmap organizes public research work. It does not determine medical
care, evaluate a person's treatment options, recommend a trial, or claim that a
cure or vaccine has been found.
