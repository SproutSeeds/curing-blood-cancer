# Multiple Myeloma Public Roadmap v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- roadmap status: `active-v0`
- claim level: `open-question`
- last reviewed: `2026-04-16`
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

- [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
- [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
- [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md)
- [Multiple Myeloma Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

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

### 7. Work The Adaptive Frontier Map

The v0 public loop now has a durable adaptive named phase:

[Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)

The active roadmap remains:

[Multiple Myeloma ORP Frontier Roadmap v0](frontier-roadmap-v0.md)

The adaptive master plan and frontier map turn the completed scaffolding into a
concrete operating plan for expert validation, MRD and endpoint guardrails,
immune therapy landscape work, post-BCMA resistance mapping, precursor-state
boundaries, context modifiers, case-to-cure dry-run plumbing, and public
translation. The adaptive plan adds the rule that each completed step must
inspect its outcome, write a handoff, synthesize the next safest public step,
and queue, activate, or block that step explicitly.

The Clawdad standing brief for this phase is:

[Clawdad Frontier Delegation Packet v0](../../protocols/clawdad-frontier-delegation-packet-v0.md)

Frontier lane order:

1. expert response intake and validation ledger
2. MRD, deep response, and endpoint language
3. immune therapy sequencing and access boundary
4. post-BCMA resistance and relapse mechanisms
5. precursor, risk, and interception questions
6. high-risk, extramedullary, organ, and frailty context
7. case-to-cure pipeline plumbing
8. public translation and contribution surface

Done when:

- the adaptive master backlog is complete or blocked by a named human gate
- every frontier lane has a first public artifact or explicit blocked status
- metadata, catalog entries, README links, and protocols are current
- `make validate` passes
- all remaining work is named as expert-review-needed, private-lab-needed,
  clinical-team-needed, or human-publication-gate-needed

### 8. Build Tools On Top

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

1. Treat [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
   as the completed endpoint for the original v0 public loop.
2. Use [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
   as the live ORP named phase and durable next-step loop.
3. Use [Multiple Myeloma ORP Frontier Roadmap v0](frontier-roadmap-v0.md) as the
   active roadmap context.
4. Use [Clawdad Frontier Delegation Packet v0](../../protocols/clawdad-frontier-delegation-packet-v0.md)
   as the standing Clawdad brief for autonomous public-safe passes.
5. The adaptive case-to-cure loop has completed the loop governor, private
   intake schema/projection boundary, static synthetic caregiver prototype,
   projection validator, and
   [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md),
   plus the
   [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
   and
   [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md),
   and the
   [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md),
   and the
   [Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md),
   and the
   [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md),
   and the
   [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md),
   and the
   [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md),
   and the
   [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md),
   and the
   [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md).
6. The case-to-public learning extraction gate is complete as
   [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md);
   it preserves allowed output type, privacy decision state,
   de-identification basis, aggregation state, minimum-size state,
   single-case claim blockers, public source context, review lens,
   disposition state, uncertainty, limitations, blocked uses, and
   publication-gate state before any private-case learning can become public.
7. The end-to-end synthetic case dry run is complete as
   [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md);
   it exercises success, omit, refusal, and blocker states from synthetic
   caregiver intake through publication-gate refusal without real case data,
   patient-specific outputs, matching, ranking, clinical guidance, or
   publication authorization.
8. The case-to-cure master completion audit is complete as
   [Case-To-Cure Master Completion Audit v0](case-to-cure-master-completion-audit-v0.md);
   it records the adaptive public-safe scope as complete and blocks the next
   state on expert, private-lab, clinical, legal, regulatory, publication, or
   human-review gates unless a human selects a new named public-safe phase.
9. The expert validation loop now preserves issue IDs, artifact IDs, source
   IDs, review lenses, outreach-map role labels, response-ledger disposition
   states, allowed dispositions, uncertainty, blocked uses, and next public
   actions without outreach, private correspondence, unpublished expert
   comments, recommendations, rankings, publication authorization, or clinical
   decisions.
10. The multidisciplinary review packet builder now preserves question IDs,
   artifact IDs, source IDs, review lenses, missing-input blockers, refusals,
   and boundary fields with copy, reference, omit, or refuse behavior only,
   without packet assembly, generated biomedical prose, patient-specific
   output, recommendations, rankings, matching, publication authorization, or
   clinical decisions.
11. The candidate hypothesis review question set now preserves source-scoped
   review questions, evidence packet IDs, landscape gate status, source
   context, uncertainty, review lens, blocked uses, and explicit no
   patient-action output without candidate options, recommendations, rankings,
   matching, treatment guidance, trial guidance, expanded-access guidance,
   monitoring guidance, or patient-specific interpretation.
12. The trial/therapy landscape non-advice gate now preserves trial, therapy,
   product, target, jurisdiction, source freshness, access-date, status,
   limitation, uncertainty, and review fields without availability claims,
   eligibility claims, matching, sequencing, access guidance, ranking, or
   patient-specific interpretation.
12. The evidence retrieval packet preserves public source IDs, query
   records, source freshness, access-date state, limitations, uncertainty,
   no-completeness warnings, review status, and no-advice boundaries without
   patient matching, trial matching, actionability, availability, eligibility,
   monitoring, ranking, or patient-specific interpretation.
13. The molecular immune context contract now preserves cytogenetics,
   genomics, target assays, pathology, flow, immune context, assay validity,
   source validity, source status, timepoint buckets, review gates, and target
   language boundaries before downstream use without actionability, testing,
   treatment, trial, monitoring, ranking, or patient-specific interpretation.
14. The therapy exposure timeline contract now preserves prior therapies,
   exposure, line or timing context, response linkage, toxicity, or constraints
   before downstream use without sequencing, eligibility, access, monitoring,
   ranking, or treatment guidance.
15. Then advance immune therapy and post-BCMA resistance lanes with date-scoped,
   source-backed, non-advisory records.
16. Then define precursor, high-risk, organ, frailty, and case-to-cure dry-run
   plumbing boundaries.
17. Then improve the public translation and contribution surface.
18. Build artifact-generation scripts, evidence graph tooling, target
   prioritization views, trial explorers, extraction helpers, or review-packet
   builders only after their input shapes validate and the relevant frontier
   lane says tooling is unblocked.

## Review Boundary

This roadmap organizes public research work. It does not determine medical
care, evaluate a person's treatment options, recommend a trial, or claim that a
cure or vaccine has been found.
