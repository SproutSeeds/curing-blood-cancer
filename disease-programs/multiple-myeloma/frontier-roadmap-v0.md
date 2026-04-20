# Multiple Myeloma ORP Frontier Roadmap v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- roadmap status: `active-frontier-v0`
- claim level: `open-question`
- last reviewed: `2026-04-20`
- clinical boundary: research-use-only, not medical advice

## Purpose

This is the public ORP frontier roadmap for the next phase of Curing Blood
Cancer's multiple myeloma work.

The previous public loop established a source-backed wedge, public task queues,
case-to-cure plumbing boundaries, review-packet builder gates, expert
validation issues, and a public release gate. This frontier roadmap gives the
next autonomous loop a concrete map to work through until the public surface is
useful enough for expert validation, public contribution, and future
private-lab case work.

This roadmap does not claim that multiple myeloma has been cured. It defines
the tooling, evidence, validation, and safety plumbing needed to work toward
cure-oriented questions without using private case data in public.

## Operating Boundary

All work in this roadmap must remain public-safe.

Allowed:

- public-source summaries with provenance and uncertainty
- schemas, validators, protocols, maps, glossaries, task queues, and review
  packets
- synthetic examples that cannot be mistaken for a real person
- public issue-ready validation requests and artifact-improvement tasks
- stewardship marks that connect the work to frg.earth

Not allowed:

- patient-identifying data, real case data, private records, dates tied to a
  person, images, notes, or re-identification keys
- trial eligibility advice, treatment advice, diagnosis, prognosis, expanded
  access advice, or ranking of patient options
- unsupported claims that a cure, vaccine, treatment path, or clinical strategy
  has been found
- private email text, unpublished expert replies, credentials, restricted
  datasets, or paid services
- autonomous sending of outreach, commits, pushes, releases, billing changes,
  or destructive repository changes

## Frontier Thesis

The public work becomes more valuable when it connects eight things without
collapsing them into clinical advice:

1. durable deep response and measurable residual disease language
2. immune therapy sequencing and resistance
3. post-BCMA relapse mechanisms
4. precursor and early-interception questions
5. high-risk, extramedullary, organ, and frailty contexts
6. case-to-cure pipeline plumbing that can dry-run without real data
7. expert validation loops that keep claims modest
8. public translation that helps non-specialists participate safely
9. caregiver intake plumbing that helps a caregiver-like helper organize a future
   private case without public PHI or advice

The aim is a public research operating system for defining better questions,
not a clinical decision system.

## Canonical Inputs

The frontier loop should inspect these public artifacts before each pass:

- [Public Roadmap v0](public-roadmap-v0.md)
- [Open Research Map v0.1](open-research-map-v0-1.md)
- [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
- [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
- [Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
- [Residual Disease Modality Discordance Source Extraction v0](measurements/residual-disease-modality-discordance-source-extraction-v0.md)
- [Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md)
- [Static Synthetic Caregiver Intake Frontend Smoke Test v0](case-intake/static-synthetic-caregiver-intake-frontend-smoke-test-v0.md)
- [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
- [Public Review And Release Gate v0](public-review-release-gate-v0.md)
- [Public Inventory v0](public-inventory-v0.md)
- [Public Review Release Gate Pass v0](public-review-release-gate-pass-v0.md)
- [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md)
- [Expert Validation Outreach Map v0](reviews/expert-validation-outreach-map-v0.md)
- [Clawdad Frontier Delegation Packet v0](../../protocols/clawdad-frontier-delegation-packet-v0.md)
- [Source Registry v0](../../sources/source-registry-v0.md)
- [Public Artifact Catalog v0](../../artifacts/public-artifact-catalog-v0.md)

## Frontier Lanes

Work each lane in small, validated public slices. A lane is not complete just
because one note exists; it is complete when the first useful public artifact,
metadata, catalog entry, navigation link, and validation pass exist.

### Lane 1. Expert Response Intake And Validation Ledger

Goal:

Turn expert outreach and public issue validation into a durable review system.

Why this matters:

The repo already has expert validation issue framing. The next frontier is to
make incoming expert feedback useful without publishing private email content or
overstating consensus.

Public artifacts to create:

- public-safe expert response ledger template
- validation disposition taxonomy
- issue-to-artifact review status map
- reviewer-lens summary that separates hematology, transplant, immunotherapy,
  MRD, patient advocacy, data governance, and tooling concerns

Current frontier artifact:

- [Expert Response Validation Ledger v0](reviews/expert-response-validation-ledger-v0.md)
  maps all 13 public expert-validation issues to safe dispositions, public
  issue state, artifact paths, reviewer lenses, and next public actions without
  copying private correspondence.

Allowed public response dispositions:

- `wording-fix-needed`
- `source-context-needed`
- `expert-review-satisfied-for-item`
- `keep-expert-review-needed`
- `needs-public-source-before-use`
- `blocked-private-or-clinical`
- `out-of-scope-for-public-repo`

Completion criteria:

- each existing expert validation item has a status field and next public
  action
- private emails are not copied into public artifacts
- any expert view is attributed only when permission and public source context
  are available
- unresolved clinical interpretation remains labeled as expert-review-needed

### Lane 2. MRD, Deep Response, And Endpoint Language

Goal:

Make MRD, complete response, sustained MRD negativity, relapse, and endpoint
language precise enough for public research artifacts.

Why this matters:

MRD language can be technically meaningful and easy to misuse. Public tools must
preserve method, threshold, sample context, timepoint, durability, and endpoint
status before downstream scoring or maps use the terms.

Public artifacts to create or extend:

- [MRD Endpoint Language Guardrail Addendum v0](measurements/mrd-endpoint-language-guardrail-addendum-v0.md)
- measurement-context audit updates
- endpoint-language guardrail note
- public task draft for missing MRD extraction records:
  [MRD endpoint source extraction task](public-tasks/issue-drafts/multiple-myeloma-mrd-endpoint-source-extraction-task-v0.md)

Minimum fields to preserve:

- measurement method
- sample type
- assay sensitivity or threshold, when stated by the source
- disease state
- treatment context
- timepoint and duration language
- endpoint status, such as exploratory, surrogate, regulatory, or clinical
  outcome context
- uncertainty and source limitations

Completion criteria:

- endpoint terms are linked to source-backed definitions
- the repo distinguishes response depth from cure claims
- future tooling cannot flatten MRD into a yes/no cure flag

### Lane 3. Immune Therapy Sequencing And Access Boundary

Goal:

Map immune therapy classes and sequencing questions without producing treatment
or trial advice.

Why this matters:

CAR T-cell therapies, bispecific antibodies, antibody-drug conjugates, and
emerging targets are central to current multiple myeloma research. Public
artifacts need to track the landscape while avoiding implied recommendations.

Public artifacts to create or extend:

- [Immune Therapy Sequencing And Access Boundary v0](therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md)
- therapy status freshness fields
- target-class crosswalk for BCMA, GPRC5D, FcRH5, CD38, SLAMF7, and adjacent
  targets when public sources support inclusion
- public access-boundary note for trial and product references

Required boundaries:

- do not imply availability, eligibility, urgency, or ranking
- distinguish approved products, investigational agents, withdrawn products,
  trials, mechanisms, and hypotheses
- date-stamp regulatory or trial status references
- send all patient-specific questions to clinical teams, not the repo

Completion criteria:

- immune therapy records carry source IDs, date context, and uncertainty
- trial or product references cannot be read as treatment advice
- therapy maps link back to public source records and limitation text

### Lane 4. Post-BCMA Resistance And Relapse Mechanisms

Goal:

Expand the mechanism map from BCMA antigen escape into broader post-BCMA and
post-cellular-therapy relapse questions.

Why this matters:

Durable remission work needs structured accounting for why deep responses fail.
Public maps should make evidence gaps and mechanism hypotheses inspectable.

Public artifacts to create or extend:

- [Post-BCMA Resistance Frontier Addendum v0](mechanisms/post-bcma-resistance-frontier-addendum-v0.md)
  as the antigen and non-antigen relapse mechanism map addendum.
- high-priority contradiction and uncertainty register fields inside the
  addendum.
- target-context links from mechanism questions to public evidence gaps.
- extraction queue updates only where the coverage report says v0 coverage is
  missing.

Mechanism families to track:

- antigen escape or antigen downregulation
- BCMA loss or alteration, where source-backed
- T-cell exhaustion, phenotype, fitness, and persistence
- immune microenvironment constraints
- tumor burden and disease-state modifiers
- non-BCMA target escape and lineage or plasma-cell state changes
- high-risk or extramedullary contexts

Completion criteria:

- each mechanism claim is labeled as fact, derived claim, hypothesis, or open
  question
- evidence gaps are contribution-ready
- no mechanism map implies a direct patient option

### Lane 5. Precursor, Risk, And Interception Questions

Goal:

Define how MGUS, smoldering multiple myeloma, early intervention, and
prevention-adjacent questions can be discussed safely in this public repo.

Why this matters:

The cure-oriented frame must eventually address when disease can be intercepted
without creating public overdiagnosis, overtreatment, or anxiety tooling.

Public artifacts to create:

- [Precursor, Risk, And Interception Boundary Note v0](precursors/precursor-risk-interception-boundary-note-v0.md)
  as the precursor/interception boundary note.
- source registry delta for MGUS and smoldering multiple myeloma public sources.
- risk-language guardrail fields inside the boundary note.
- open-question queue for prevention-adjacent research.

Required boundaries:

- no screening advice
- no risk calculator for personal use
- no treatment recommendation for precursor states
- no conversion of population risk factors into individual prognosis

Completion criteria:

- precursor state language is separated from active myeloma treatment language
- public tasks identify what source-backed extraction is missing
- patient-facing text is careful, modest, and non-directive

### Lane 6. High-Risk, Extramedullary, Organ, And Frailty Context

Goal:

Capture disease-state and host-context modifiers that affect research questions
without creating patient-specific decision logic.

Why this matters:

Multiple myeloma is not a single context. Cytogenetics, extramedullary disease,
renal function, bone disease, immune status, infection risk, performance status,
frailty, and prior therapy exposure can change what evidence means.

Public artifacts to create or extend:

- [High-Risk, Extramedullary, Organ, And Frailty Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md)
  as the disease-state modifier taxonomy, organ-context boundary, frailty
  boundary, and review-packet checklist seed.
- public-safe case-feature bundle addendum, only after a schema lane selects
  optional context-field changes.
- synthetic fixture coverage, only after schema fields change and synthetic
  combinations pass privacy review.

Completion criteria:

- context fields are optional, source-scoped, and non-identifying
- synthetic fixtures exercise modifier fields without resembling a person
- no context modifier produces eligibility, treatment, or prognosis output

### Lane 7. Case-To-Cure Pipeline Plumbing

Goal:

Make the exact pipeline from private case context to public artifacts visible
without requiring real case data.

Why this matters:

The initiative needs to be able to serve a particular case later. Before a real
case exists in the public work, the repo needs a dry-run map of every stage,
input, validation gate, blocker, and public output boundary.

Public artifacts to create or extend:

- [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md)
  as the case-to-cure stage validator map, owner-artifact map,
  blocker-to-private-lab map, and no-real-case dry-run graph.
- synthetic route-table expansion only after the route-table schema lane
  selects a bounded fixture update.
- public release gate hooks remain the existing publication and public-review
  gates until a future human-selected automation phase.

Required stages:

1. private intake and consent boundary
2. public-safe feature bundle projection
3. source-backed disease-state context
4. evidence map selection
5. trial and therapy landscape context, explicitly not advice
6. candidate hypothesis review, explicitly not ranking for care
7. multidisciplinary packet assembly
8. expert review and issue-linked validation
9. public learning extraction, only after sanitation and publication gate
10. blocker register update for anything that remains private or clinical

Completion criteria:

- every pipeline stage has an owner artifact, validator, and blocked-condition
  field
- synthetic examples cover success, omit, refuse, and blocker paths
- the public repo can show the pipeline without showing a real person

### Lane 8. Public Translation And Contribution Surface

Goal:

Make the public surface legible to patients, advocates, builders, funders, and
researchers without softening the safety boundary.

Why this matters:

The project is build-in-public. The work should be useful to the greater
population, not only to internal operators, but it must not become advice.

Public artifacts to create:

- [Multiple Myeloma Public Translation And Contribution Guide v0](public-translation-contribution-guide-v0.md)
  as the plain-language research-map companion, glossary index, contribution
  guide, and issue-template chooser.
- future issue-template edits only after contributors identify a specific
  missing field or unsafe ambiguity in the existing source extraction,
  evidence gap, or expert review forms.

Completion criteria:

- non-specialists can find the right artifact within three links from the
  disease-program README
- contribution requests are specific and safe
- every plain-language page says what it cannot answer

## Completion Matrix

| Lane | First Frontier Artifact | Next Shape Or Tooling Need | Validation | Done Criteria |
| --- | --- | --- | --- | --- |
| Expert response intake | [Expert Response Validation Ledger v0](reviews/expert-response-validation-ledger-v0.md) | future disposition schema or issue-update task, only after public-source-backed responses are triaged | metadata, catalog, link check | all validation issues have status and next action; expert-review-needed remains until a safe public disposition is recorded |
| MRD and endpoints | [MRD Endpoint Language Guardrail Addendum v0](measurements/mrd-endpoint-language-guardrail-addendum-v0.md) plus [Residual Disease Modality Discordance Source Extraction v0](measurements/residual-disease-modality-discordance-source-extraction-v0.md) | assay/specimen quality failure-mode checklist, then synthetic fixture pressure | `make validate` plus source IDs | response depth and residual-disease modality context cannot be read as cure, prognosis, monitoring, treatment, or global disease-state claims |
| Immune therapy sequencing | [Immune Therapy Sequencing And Access Boundary v0](therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md) | validated therapy landscape record shape | metadata, catalog, source IDs | no treatment, trial, or access advice |
| Post-BCMA resistance | [Post-BCMA Resistance Frontier Addendum v0](mechanisms/post-bcma-resistance-frontier-addendum-v0.md) | validated contradiction-register shape before any dashboard or scoring work | metadata, catalog, claim-level, and gap reference validation | mechanisms link to public gaps and cannot imply patient options |
| Precursor/interception | [Precursor, Risk, And Interception Boundary Note v0](precursors/precursor-risk-interception-boundary-note-v0.md) | source extraction issue drafts and no-calculator risk-context shape | metadata, catalog, source registry, and source review | no screening or personal risk tooling |
| High-risk/context | [High-Risk, Extramedullary, Organ, And Frailty Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md) | case-feature addendum and synthetic fixture only after schema field changes | metadata, catalog, source registry, and review-packet checklist updates | optional, source-scoped context labels; no prognosis, eligibility, treatment, or option ranking |
| Case-to-cure plumbing | [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md) | dry-run fixture or structured graph only after a bounded schema/tooling lane selects it | synthetic pipeline, metadata, catalog, and artifact validation | each stage has owner artifact, validator or gate, and blocker field |
| Public translation | [Multiple Myeloma Public Translation And Contribution Guide v0](public-translation-contribution-guide-v0.md) | [Frontier Completion Audit Handoff v0](frontier-completion-audit-handoff-v0.md) | metadata, catalog, public-safety, and link check | non-specialists can navigate safely and contributors know the exact safe task surface |

Current frontier completion artifact:

- [Frontier Completion Audit Handoff v0](frontier-completion-audit-handoff-v0.md)
  records that all eight frontier lanes have first public artifacts and that no
  new ready public task is selected without a new named phase gate.

## Active Named Phase: Case-To-Cure Adaptive Master Plan v0

The current live ORP frontier points to
`case-to-cure-adaptive-master-plan-v0` and the active human-selected phase
`public-caregiver-intake-frontend-v0`.

Canonical active artifact:

- [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
- [Case-To-Cure Loop Governor Handoff v0](case-to-cure-loop-governor-handoff-v0.md)
- [Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md)
- [Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md)
- [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md)
- [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md)
- [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
- [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md)
- [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md)
- [Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md)
- [Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
- [Static Synthetic Caregiver Intake Frontend Smoke Test v0](case-intake/static-synthetic-caregiver-intake-frontend-smoke-test-v0.md)
- [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md)
- [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md)
- [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
- [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)
- [Case-To-Cure Master Completion Audit v0](case-to-cure-master-completion-audit-v0.md)
- [Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md)
- [Synthetic Caregiver Intake v0](../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json)

The active backlog is the ORP additional list
`post-machine-representation-public-safe-research-substrate-v0`, with active
item `machine-representation-expert-validation-human-authorization-blocker-v0`.
It exists because machine-representation implementation, MRD resistance geometry
falsification, and no-outreach expert-validation prep are complete for their
named public-safe scopes, while expert-validation execution and outreach remain
human-gated.

Active loop rule:

1. complete one public-safe step
2. inspect what the completed step revealed
3. write or update a completion handoff
4. synthesize the next safest public step
5. queue or activate that step in ORP
6. stop only if the next work is blocked by a public-safety, expert, private
   lab, clinical, legal, regulatory, publication, or compute boundary

This active phase supersedes the old "no ready tasks" endpoint. A completed
subphase means the loop should read the handoff and choose what follows; it
does not mean the multiple myeloma initiative is complete.

The completed loop-governor item is `case-to-cure-loop-governor-v0`, the
completed private intake shape item is `private-intake-schema-contract-v0`,
and the completed static prototype item is
`static-synthetic-caregiver-prototype-v0`. The completed protocol validator
item is `public-projection-validator-v0`. The completed consent and governance
boundary item is `consent-privacy-security-retention-gate-v0`.
The completed case-normalization envelope item is
`case-feature-normalization-contract-v0`.
The completed measurement item is `measurement-normalization-contract-v0`.
The completed therapy exposure item is
`therapy-exposure-timeline-contract-v0`.
The completed molecular and immune context item is
`molecular-immune-context-contract-v0`.
The completed evidence retrieval item is `evidence-retrieval-packet-v0`.
The completed trial/therapy landscape item is
`trial-therapy-landscape-non-advice-gate-v0`.
The completed candidate hypothesis review question item is
`candidate-hypothesis-review-question-set-v0`.
The completed multidisciplinary review packet builder item is
`multidisciplinary-review-packet-builder-v0`.
The completed expert validation loop item is `expert-validation-loop-v0`.
The completed case-to-public learning extraction gate item is
`case-to-public-learning-extraction-gate-v0`.
The completed end-to-end synthetic dry-run item is
`end-to-end-synthetic-case-dry-run-v0`.
The completed master audit item is `case-to-cure-master-completion-audit-v0`.
The previously active queue item
`case-to-cure-public-scope-human-gate-blocker-v0` recorded the safe stop after
the master audit. A human-selected public frontend phase produced a static
prototype. The completed frontend item is
[Static Synthetic Caregiver Intake Frontend v0](case-intake/static-synthetic-caregiver-intake-frontend-v0.html),
and the completed smoke-test item is
[Static Synthetic Caregiver Intake Frontend Smoke Test v0](case-intake/static-synthetic-caregiver-intake-frontend-smoke-test-v0.md).
The completed queue items now include `myeloma-state-object-schema-v0`,
captured as
[Myeloma State Object Schema v0](../../schemas/myeloma-state-object-schema-v0.md),
and `synthetic-myeloma-state-fixture-v0`, captured as
[Synthetic Myeloma State Fixture v0](../../examples/synthetic-myeloma-state-fixture-v0.json).
The completed queue item now also includes `model-output-boundary-wrapper-v0`,
captured as
[Model Output Boundary Wrapper v0](model-output-boundary-wrapper-v0.md).
The completed queue item now also includes `myeloma-state-validator-rule-map-v0`,
captured as
[Myeloma State Validator Rule Map v0](myeloma-state-validator-rule-map-v0.md).
The completed queue item now also includes `machine-representation-source-extraction-v0`,
captured as
[Machine Representation Source Extraction v0](machine-representation-source-extraction-v0.md).
The completed queue item now also includes
`machine-representation-source-gap-task-queue-v0`, captured as
[Machine Representation Source-Gap Task Queue v0](public-tasks/machine-representation-source-gap-task-queue-v0.md).
The completed queue item now also includes
`machine-representation-source-gap-issue-draft-packet-v0`, captured as
[Machine Representation Source-Gap Issue Draft Packet v0](public-tasks/issue-drafts/machine-representation-source-gap-issue-draft-packet-v0.md).
The completed queue item now also includes
`machine-representation-implementation-completion-audit-v0`, captured as
[Machine Representation Implementation Completion Audit v0](machine-representation-implementation-completion-audit-v0.md).
The machine-representation implementation queue closed as
`machine-representation-public-scope-human-gate-blocker-v0`, meaning no further
autonomous public-safe machine-representation implementation item remains
without human selection of a new named phase or clearance of a named gate.

A human later selected `mrd-resistance-geometry-falsification-v0` as a
public-safe research-substrate phase. That phase completed through public
source extraction, falsification matrix, transition model, hypothesis ledger,
benchmark fixtures, and invariant checks. It did not clear expert-review,
human-review, private-lab, clinical-team, model-governance, legal, regulatory,
publication, or outreach gates.

The current active queue item is
`machine-representation-expert-validation-human-authorization-blocker-v0`.
The no-outreach machine-representation source-gap prep is complete, and the
subsequent internal source-gap extraction added therapy-exposure and
validation-governance anchors, but actual expert-validation execution,
external outreach, response intake, issue operations, private-lab work,
clinical interpretation, publication, and expert-review claim upgrades remain
blocked unless a human explicitly authorizes scope or selects a new named
no-outreach public-source phase.

The completed queue item now also includes
`residual-disease-modality-discordance-source-extraction-v0`, captured as
[Residual Disease Modality Discordance Source Extraction v0](measurements/residual-disease-modality-discordance-source-extraction-v0.md).

The current direction-check artifact is
[Multiple Myeloma Frontier Gap Sweep v0](frontier-gap-sweep-v0.md), which
promoted residual-disease modality discordance, spatial/imaging context,
blood-based MRD, assay/specimen quality, human fitness/toxicity, and
transportability/bias as the next obvious public-safe research gaps. The
selected residual-disease modality-discordance source extraction is now
complete; the next no-outreach public-source successor, if selected, is
`assay-specimen-quality-failure-mode-checklist-v0`.

Completion criteria:

- the adaptive master plan is linked from roadmap, README, case-to-cure
  blueprint, inventory, catalog, ORP stack, and Clawdad packet
- ORP active state points at the adaptive master plan and current active item
- ORP additional queue contains durable public-safe case-to-cure backlog items
- each completed step must synthesize and queue the next step or record a hard
  blocker
- no real case data, identifiers, records, uploads, or patient-specific advice
  appear in public artifacts
- `make validate` passes

## Completed Subphase: Case Intake Frontier v0

The completed named subphase gate is `case-intake-frontier-v0`.

This phase exists because the public loop completed its original eight lanes,
and the initiative needed a concrete caregiver-facing intake foundation before
a future private case can move through the case-to-cure pipeline.

Canonical phase artifact:

- [Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md)

Public projection gate:

- [Caregiver Intake Public Projection Checklist v0](case-intake/caregiver-intake-public-projection-checklist-v0.md)

Completion audit handoff:

- [Case Intake Frontier Completion Audit Handoff v0](case-intake/case-intake-frontier-completion-audit-handoff-v0.md)

Synthetic fixture:

- [Multiple Myeloma Synthetic Caregiver Intake v0](../../examples/multiple-myeloma-synthetic-caregiver-intake-v0.json)

Completion criteria:

- the caregiver intake spec is linked from the case-to-cure blueprint,
  disease-program README, public inventory, and public catalog
- the field inventory distinguishes minimum, optional, unknown, and
  private-only fields without using real case data
- the synthetic fixture demonstrates the flow without resembling a real person
- privacy, consent, emergency, clinician-review, and no-medical-advice
  boundaries are explicit
- the public projection checklist defines fail-closed no-PHI and no-advice
  gates before any future intake-derived output can become public
- the synthetic fixture includes `intake_02_helper_context` and a synthetic
  projection-verdict block without real case data or free-text case details
- the case-intake completion audit/handoff records the phase as closed for the
  current public autonomous loop

Clawdad should treat this subphase as closed and continue through the adaptive
master backlog now that the ORP live frontier points somewhere else.

## Clawdad Delegation Mode

Clawdad should use this roadmap as the active frontier map and the
[Clawdad Frontier Delegation Packet v0](../../protocols/clawdad-frontier-delegation-packet-v0.md)
as its standing brief.

For each pass, Clawdad should:

1. inspect `git status --short`
2. read this roadmap, the adaptive master plan, ORP live state, ORP additional
   queue, the public roadmap, the public loop handoff, the catalog, and the
   safety rules
3. select exactly one frontier lane slice or active ORP additional item
4. create or update the smallest useful public artifact set
5. update metadata, catalog entries, README links, and protocol references
6. run `make validate`
7. report the changed files, validation result, lane status, blockers, and next
   lane slice
8. synthesize the next step from the completed step's outcome and queue,
   activate, or block it explicitly

Clawdad should stop instead of proceeding when the next required work requires
expert responses, real case data, clinical decisions, private lab data, legal
or regulatory decisions, publication approval, or another explicit human gate.

## Frontier Definition Of Complete

This frontier phase is complete when:

- every lane has a first public artifact or an explicit public-safe blocked
  status
- every new artifact has metadata and catalog coverage
- the disease-program README and protocol index make the frontier navigable
- expert validation items have a public-safe status ledger
- MRD and endpoint language has guardrails that prevent cure overclaiming
- immune therapy and trial references carry date, status, source, and
  no-advice boundaries
- post-BCMA mechanism gaps have source-backed public tasks
- precursor and high-risk context language is bounded and non-directive
- the case-to-cure dry run maps every stage to owner artifacts, validators, and
  blockers
- translation artifacts let non-specialists participate without receiving
  advice
- `make validate` passes
- remaining blockers are named as expert-review-needed, private-lab-needed,
  clinical-team-needed, or human-publication-gate-needed

## Source Anchors

- [NCI Plasma Cell Neoplasms / Multiple Myeloma Treatment PDQ](https://www.cancer.gov/types/myeloma/hp/myeloma-treatment-pdq)
- [FDA Draft Guidance On MRD And Complete Response In Multiple Myeloma](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/minimal-residual-disease-and-complete-response-multiple-myeloma-use-endpoints-support-accelerated)
- [Bone Marrow Microenvironment Drug Resistance Source](https://pubmed.ncbi.nlm.nih.gov/40440932/)
- [Multiple Myeloma PRO Quality Source](https://pubmed.ncbi.nlm.nih.gov/40729465/)
- [Spatial Transcriptomics Myeloma Source](https://pubmed.ncbi.nlm.nih.gov/40643106/)
- [MRD/PET-CT Concordance And Discordance Source](https://www.sciencedirect.com/science/article/pii/S258953702600115X)
- [Blood Mass Spectrometry MRD Source](https://pubmed.ncbi.nlm.nih.gov/40919481/)
- [FDA Linvoseltamab Accelerated Approval Notice](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-grants-accelerated-approval-linvoseltamab-gcpt-relapsed-or-refractory-multiple-myeloma)
- [Dana-Farber Multiple Myeloma CAR T-Cell Therapy Update](https://www.dana-farber.org/for-physicians/clinical-resources/hematologic-malignancies/advances-newsletter/2025-issue-20/multiple-myeloma-cart-t-cell-therapy-update)
- [IMWG Frailty Report](https://pubmed.ncbi.nlm.nih.gov/25628469/)
- [Expert Validation Issue Index v0](reviews/expert-validation-issue-index-v0.md)
- [Expert Response Validation Ledger v0](reviews/expert-response-validation-ledger-v0.md)
- [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
- [Case-To-Cure Loop Governor Handoff v0](case-to-cure-loop-governor-handoff-v0.md)
- [Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md)
- [Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md)
- [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md)
- [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md)
- [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
- [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)

## Review Boundary

This roadmap organizes public research work. It does not provide diagnosis,
prognosis, treatment advice, trial advice, expanded-access advice, screening
advice, monitoring advice, or a claim that a cure or vaccine has been found.
