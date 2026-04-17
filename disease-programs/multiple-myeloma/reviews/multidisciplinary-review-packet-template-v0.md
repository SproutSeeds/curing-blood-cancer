# Multidisciplinary Review Packet Template v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- packet type: reusable public review template
- linked gap: `expert-review-readiness-gap-v0`
- review status: expert-review-needed
- clinical boundary: research-use-only, not medical advice
- public data boundary: do not fill this public template with real case facts
- last reviewed: `2026-04-16`

## Purpose

This packet template prepares future private multiple myeloma review packets for
multidisciplinary review without downstreaming real case data into the public
repo.

It does not make any artifact expert-reviewed. It gives the private lab and
public contributors a source-backed scaffold for the reviewer roles, review
questions, status boundaries, and safety language that must be preserved before
any case-derived learning can become a public artifact candidate.

## Do Not Fill Publicly

Do not place real case facts, patient identifiers, raw records, dates tied to a
person, images, free-text notes, clinician names, site names, sponsor contacts,
candidate options, monitoring plans, or treatment decisions in this public
template.

Private case work may copy this structure into a private workspace. Public
outputs may only use sanitized, synthetic, generic method, public-source, or
separately reviewed aggregate learning that passes the
[Publication-Gate Checklist v0](../publication-gate-checklist-v0.md).

## Status Boundary

- Source-checked means public-source-backed and structurally validated.
- Expert-review-needed means qualified reviewers have not completed review.
- Expert-reviewed must wait for completed reviewer comments and a follow-up
  artifact update.
- Blocked means the material must remain private or be rewritten before public
  review because privacy, provenance, scope, review status, or clinical-use
  boundary is incomplete.

## Target Public Artifacts

| Artifact | Current Status | Review Goal |
| --- | --- | --- |
| `multiple-myeloma-case-to-cure-pipeline-blueprint-v0` | source-checked | Confirm that the staged pipeline keeps case-specific work private and public artifacts generic. |
| `case-feature-bundle-public-summary-v0` | source-checked | Confirm that public field groups cannot be mistaken for a case upload schema. |
| `high-risk-organ-frailty-context-modifier-map-v0` | source-checked | Confirm that context modifiers remain optional, source-scoped, non-identifying, and cannot produce prognosis, eligibility, treatment, or option ranking. |
| `multiple-myeloma-candidate-option-scoring-rubric-v0` | source-checked | Confirm that review-readiness scoring cannot become candidate ranking or action guidance. |
| `multiple-myeloma-publication-gate-checklist-v0` | source-checked | Confirm that publication gates fail closed before case-derived public learning is released. |
| `mrd-and-relapse-measurement-glossary-v0` | source-checked | Confirm that MRD, relapse, target, and response terms are precise enough for review packet routing. |
| `post-car-t-relapse-mechanism-map-v0` | source-checked | Confirm that mechanism buckets stay navigation-oriented and do not become mechanism rankings. |
| `clinicaltrials-gov-query-protocol-v0` | source-checked | Confirm that trial-query provenance stays separate from eligibility, availability, and recommendation claims. |

## Review Sections

| Review Item | Focus | Required Roles | Public Action |
| --- | --- | --- | --- |
| `hematology-disease-state-review-template-v0` | claim scope | myeloma clinician, outcomes reviewer | Confirm disease-state, response, relapse, and MRD wording boundaries. |
| `context-modifier-review-template-v0` | context boundary | myeloma clinician, geriatric or organ-context reviewer, patient-protection reviewer | Confirm high-risk, extramedullary, organ, frailty, performance-status, immune, infection-risk, and prior-exposure fields remain optional and non-directive. |
| `cellular-therapy-review-template-v0` | translation boundary | cellular therapy clinician or translational scientist | Confirm CAR T, bispecific, and immune-effector context remains source-backed and non-prescriptive. |
| `pathology-measurement-review-template-v0` | measurement assumptions | pathology, flow, MRD, or assay reviewer | Confirm specimen, assay, threshold, timing, and target-status fields are sufficient before comparison. |
| `genomics-target-biology-review-template-v0` | source quality | genomics, target biology, or translational reviewer | Confirm source maturity, model context, and target-biology limits are explicit. |
| `trial-operations-review-template-v0` | translation boundary | trial operations reviewer, clinician reviewer | Confirm trial records stay registry-pattern artifacts and do not imply eligibility or availability. |
| `regulatory-access-review-template-v0` | unsupported inference | regulatory, sponsor-access, or ethics reviewer | Confirm expanded-access and investigational-pathway language stays generic and non-advisory. |
| `safety-ethics-review-template-v0` | safety language | safety, ethics, or patient-protection reviewer | Confirm toxicity, logistics, privacy, and consent boundaries are visible and fail closed. |
| `patient-communication-review-template-v0` | public readability | patient advocate, science communicator, clinician reviewer | Confirm public readers will not mistake the packet for medical advice or a care pathway. |

## Required Review Fields

Each private review item copied from this template should capture:

- reviewer role, not reviewer identity, for any public downstream summary
- linked public source IDs
- linked claim, gap, mechanism, measurement, query-record, and task IDs where
  relevant
- current review status
- uncertainty and missingness
- limitations
- what-not-to-infer language
- reviewer action needed
- claim language action
- safety boundary
- publication-gate decision state

## Completion Gate

- At least one qualified reviewer must complete each selected review item
  before any target artifact is labeled expert-reviewed.
- Reviewer comments must map back to public source IDs, claim IDs, gap IDs,
  measurement term IDs, query-record IDs, extraction record IDs, or task IDs.
- Any claim-strength increase requires explicit reviewer support and a
  follow-up pull request.
- Any private case-derived learning must pass the publication gate before any
  public artifact is prepared.
- Any incomplete evidence should weaken or clarify public wording rather than
  strengthen it.

## What This Template Does Not Do

- It does not diagnose, prognose, treat, monitor, or rank options for any
  person.
- It does not recommend standard care, trial enrollment, expanded access, or
  investigational products.
- It does not establish trial eligibility, site availability, sponsor
  availability, regulatory feasibility, clinical safety, comparative benefit,
  or cure.
- It does not make source-checked artifacts expert-reviewed.
- It does not authorize public release of real case facts.

## Structured Data

- JSON: [`multidisciplinary-review-packet-template-v0.json`](multidisciplinary-review-packet-template-v0.json)
- Metadata: [`multidisciplinary-review-packet-template-v0.metadata.json`](multidisciplinary-review-packet-template-v0.metadata.json)

## Review Boundary

This template is review infrastructure. It is not medical advice, diagnostic
guidance, treatment guidance, trial guidance, expanded-access guidance,
monitoring guidance, or a claim that multiple myeloma has been cured.
