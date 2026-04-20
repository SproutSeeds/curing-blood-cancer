# ORP Frontier Gap Sweep Mode v0

Stewarded by [frg.earth](https://frg.earth/).

- mode id: `frontier-gap-sweep-mode-v0`
- protocol status: `active-v0`
- claim level: open-question
- default boundary: public-safe research operations only
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This mode gives ORP a repeatable way to ask:

- Are we still pointed at the north star?
- What has actually been created?
- What is stale, half-landed, or contradictory?
- What does current public research suggest we are underweighting?
- What is the next safest public step?

It exists because an adaptive research loop cannot only consume a static task
list. Sometimes the next step is revealed only after the previous step lands.
This mode makes that recognition explicit, auditable, and safe.

## Activation Triggers

Run this mode when a human asks any version of:

- "check on it now"
- "are we off base?"
- "what is obvious that we are not thinking about?"
- "do a deep dive pro research look"
- "what happened to the delegation run?"
- "why did it only complete a few items?"
- "what is next on the frontier?"

Also run this mode after a major phase closes, after validation fails in a way
that suggests control-plane drift, or when a delegate creates a public artifact
that is not yet reflected in catalogs, navigation, or ORP state.

## Required Inputs

At minimum, inspect:

- `git status --short`
- `orp/frontier/state.json`
- `orp/frontier/additional-items.json`
- `orp/frontier/roadmap.json`
- `disease-programs/multiple-myeloma/frontier-roadmap-v0.md`
- `disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md`
- `protocols/clawdad-frontier-delegation-packet-v0.md`
- `protocols/clawdad-autonomous-research-loop-v0.md`
- `artifacts/public-artifact-catalog-v0.json`
- `sources/source-registry-v0.md`
- `tools/validate_public_artifacts.py`

For science-facing sweeps, perform a current public-source scan. Prefer
official, primary, peer-reviewed, or registry sources. Date-stamp the scan and
keep source claims modest.

## Mode Loop

1. Freeze the public boundary.
   Confirm that the sweep will not use real case data, private records,
   identifiers, private correspondence, credentials, restricted datasets,
   patient-specific medical claims, autonomous outreach, issue operations, or
   publication actions.

2. Audit the live control plane.
   Compare ORP state, additional queue, roadmap, Clawdad packet, public README,
   disease-program README, public inventory, and artifact catalog. Flag stale
   active-phase names, missing catalog entries, changed metadata counts,
   untracked artifacts, failed validation, and closed subphases that were
   mistaken for initiative completion.

3. Audit the current artifact surface.
   Summarize what exists, what is complete for v0, what is human-gated, what is
   expert-review-needed, and what is private-lab-needed. Do not upgrade claims
   because an artifact exists.

4. Run a public-source frontier scan.
   Search for current sources that could change the priority map. Capture only
   high-signal anchors. Separate source-backed signals from inference. Do not
   treat papers, regulatory pages, trials, or institutional pages as patient
   advice.

5. Build a blind-spot register.
   For each blind spot, record:
   - `gap_id`
   - what is underweighted
   - why it matters
   - source anchors
   - public-safe next move
   - blocked uses
   - required human, expert, private-lab, clinical, legal, regulatory,
     publication, or model-governance gate

6. Fix small public-surface drift when safe.
   It is in scope to update stale navigation, add missing catalog entries,
   wire metadata, or create a public-safe mode artifact. It is not in scope to
   send outreach, open issues, publish private correspondence, create clinical
   outputs, or perform destructive repository actions unless separately
   authorized.

7. Synthesize the next queue.
   Name the highest-value public-safe phase. If the next real work is blocked,
   record the blocker and suggest the nearest no-outreach public-source
   extraction or status-prep phase.

8. Validate.
   Run `make validate` after artifact, metadata, catalog, schema, validator, or
   source-registry changes. Run focused checks when the touched surface has a
   dedicated validator.

9. Report and hand off.
   Produce a concise status payload with changed files, validation results,
   drift found, blind spots, blockers, and next queue recommendation.

## Output Shape

Every mode run should produce or update a public-safe note with this shape:

```json
{
  "mode_id": "frontier-gap-sweep-mode-v0",
  "sweep_date": "YYYY-MM-DD",
  "current_state": "active ORP phase",
  "validation": "passed|failed|not-run",
  "direction_assessment": "on-base|drifting|blocked",
  "drift_found": [],
  "frontier_sources": [],
  "blind_spots": [],
  "public_safe_next_queue": [],
  "hard_blockers": [],
  "files_changed": []
}
```

The first disease-specific run is
[Multiple Myeloma Frontier Gap Sweep v0](../../disease-programs/multiple-myeloma/frontier-gap-sweep-v0.md).

## Hard Stops

Stop and report a blocker if the sweep would require:

- patient-identifying data, real case data, raw records, images, notes, dates
  tied to a person, private case facts, or re-identification keys
- credentials, private lab access, restricted datasets, paid APIs, billing,
  account changes, or private correspondence
- diagnosis, prognosis, treatment advice, trial advice, expanded-access
  advice, monitoring advice, urgency guidance, candidate option ranking, or
  patient-specific interpretation
- autonomous outreach, issue operations, publication, release, push, merge, or
  destructive repository operations without explicit human authorization
- clinical, legal, regulatory, sponsor, institutional-review, treating-team,
  or model-governance decisions

## What This Mode Is Not

- Not a systematic review.
- Not expert review.
- Not source ranking or evidence ranking.
- Not a clinical decision-support mode.
- Not a treatment, trial, prognosis, diagnosis, monitoring, or urgency mode.
- Not a mode for using private case data in public.
- Not a cure claim.

## Definition Of Done

A run of this mode is done when:

- live ORP direction is stated clearly
- stale control-plane or navigation drift is fixed or recorded
- current public-source frontier signals are summarized with provenance
- blind spots are recorded as public-safe tasks or blockers
- the next public-safe queue item is named
- validation passes, or validation failure is reported with exact blockers
