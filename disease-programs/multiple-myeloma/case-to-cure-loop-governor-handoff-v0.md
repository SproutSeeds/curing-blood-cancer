# Case-To-Cure Loop Governor Handoff v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-case-to-cure-loop-governor-handoff-v0`
- master plan: `case-to-cure-adaptive-master-plan-v0`
- completed ORP item: `case-to-cure-loop-governor-v0`
- activated ORP item: `private-intake-schema-contract-v0`
- claim level: `open-question`
- status: `loop-governor-handoff-v0`
- last reviewed: `2026-04-16`
- clinical boundary: research-use-only loop handoff, not medical advice

## Purpose

This handoff records the first adaptive-loop governor pass for the public
multiple myeloma case-to-cure program.

The governor's job is to prevent a completed subphase from becoming a false
stop condition. After the caregiver intake foundation closed, the active ORP
state and additional queue now point to the adaptive master plan, require a
handoff after each completed public-safe step, and keep a next public-safe item
active until the master completion audit is reached or a named blocker stops
all remaining work.

This is not a case intake form, backend, private-lab system, clinical protocol,
diagnosis tool, treatment recommender, trial matcher, monitoring plan,
expanded-access guide, urgency guide, or cure claim.

## Completion Verdict

`case-to-cure-loop-governor-v0` is complete for the current public autonomous
loop.

The loop governor is complete because the public operating surface now has:

- a canonical adaptive master plan
- ORP live state pointing at that master plan
- a durable additional queue for case-to-cure work
- a rule that each completed step must inspect what changed, write a handoff,
  synthesize the next safest public step, and queue, activate, or block it
- an activated next public-safe item: `private-intake-schema-contract-v0`

The master plan is not complete. This handoff closes only the loop-governor
item and moves the active queue to the next bounded public-safe dependency.

## Evidence Map

| Governor requirement | Public evidence | Audit status |
| --- | --- | --- |
| Adaptive master plan is canonical. | [Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md) defines the durable loop, master backlog, handoff rule, and master completion boundary. | pass |
| ORP live frontier points to the adaptive plan. | [ORP Frontier State](../../orp/frontier/state.json) names `case-to-cure-adaptive-master-plan-v0` as the active milestone. | pass |
| Durable backlog exists. | [ORP Frontier Additional Items](../../orp/frontier/additional-items.json) contains `case-to-cure-master-backlog-v0` with public-safe pending items through the master completion audit. | pass |
| Version stack records the active adaptive version. | [ORP Frontier Version Stack](../../orp/frontier/version-stack.json) keeps `v2` as the current adaptive master-plan frontier. | pass |
| Delegation brief prevents premature stopping. | [Clawdad Frontier Delegation Packet v0](../../protocols/clawdad-frontier-delegation-packet-v0.md) requires reading ORP state, writing handoffs, synthesizing next steps, and continuing until master audit or explicit blocker. | pass |
| Prior subphase is closed without becoming the master endpoint. | [Case Intake Frontier Completion Audit Handoff v0](case-intake/case-intake-frontier-completion-audit-handoff-v0.md) closes `case-intake-frontier-v0` while leaving downstream private-intake, validator, prototype, and gate work explicitly bounded. | pass |
| Next public-safe step is selected. | The ORP additional queue now activates `private-intake-schema-contract-v0` after completing `case-to-cure-loop-governor-v0`. | pass |

## What The Completed Step Revealed

The completed case-intake subphase created enough public-safe intake foundation
to expose the next dependency: a private-intake schema contract.

The caregiver product spec, public projection checklist, and synthetic fixture
now define the human-friendly flow and fail-closed public projection boundary.
They do not yet define the private-only record shape that a future consented,
access-controlled private lab system would need before executable validators,
static prototypes, or normalization contracts can be made precise.

That means the safest next public step is not another intake handoff. It is a
shape-only contract that states:

- which field groups belong in private intake
- which values can remain `unknown`, `not_sure`, `not_tested`, or
  `not_collected`
- which fields are private-only and can never be projected into public
  artifacts
- what provenance, timepoint, unit, and source-status fields are required
- how public projections fail closed before any publication or reuse

## ORP Queue Update

| ORP field | Before this handoff | After this handoff |
| --- | --- | --- |
| `active_milestone` | `case-to-cure-adaptive-master-plan-v0` | `case-to-cure-adaptive-master-plan-v0` |
| `active_phase` | `case-to-cure-loop-governor-v0` | `private-intake-schema-contract-v0` |
| `active_item_id` | `case-to-cure-loop-governor-v0` | `private-intake-schema-contract-v0` |
| `case-to-cure-loop-governor-v0` status | `active` | `complete` |
| `private-intake-schema-contract-v0` status | `pending` | `active` |

## Next Step Synthesis

The next public-safe item is `private-intake-schema-contract-v0`.

The next pass should create a markdown contract, not a live schema or backend.
It should link to the caregiver intake product spec, projection checklist,
synthetic fixture, case-to-cure blueprint, and private-to-public workflow. It
should define private-only field groups and public projection rules without
collecting, inventing, or publishing any real case data.

The contract must preserve:

- no patient-identifying data in the public repo
- no real records, reports, uploads, portal exports, notes, images, exact dates
  tied to a person, contact details, consent records, or re-identification keys
- unknown and not-sure states
- final review before private handoff
- consent, privacy, clinician-review, and publication gates
- no diagnosis, prognosis, treatment advice, trial advice, monitoring advice,
  expanded-access advice, urgency guidance, option ranking, or cure claim

## Blocked Uses

This handoff cannot be used to:

- collect real case data
- define a live private database
- authorize storage, upload, or transmission of private records
- approve consent, privacy, security, retention, emergency, or clinician-review
  processes
- interpret any person's diagnosis, disease state, risk, response, relapse,
  treatment history, genomics, imaging, labs, frailty, organ context, or care
  needs
- recommend treatments, trials, monitoring, expanded access, urgency actions,
  clinicians, centers, products, sources, mechanisms, or evidence
- assemble case packets
- publish case-derived learning
- claim that multiple myeloma has been cured or that a vaccine has been found

## Handoff Boundary

The adaptive master plan remains active. The public autonomous loop should
continue with `private-intake-schema-contract-v0` unless that item reveals a
hard blocker requiring real case data, a live backend, credentials, private lab
access, clinical interpretation, outreach, publication approval, or another
external decision.

If the private-intake contract is completed safely, the loop should write its
own handoff, inspect what it revealed, and then activate or block the next
public-safe item from `case-to-cure-master-backlog-v0`.

## Review Boundary

This handoff organizes public research operations. It does not provide medical
advice, diagnostic guidance, treatment guidance, trial guidance, eligibility
guidance, expanded-access guidance, monitoring guidance, urgency guidance, or a
claim that a cure or vaccine has been found.
