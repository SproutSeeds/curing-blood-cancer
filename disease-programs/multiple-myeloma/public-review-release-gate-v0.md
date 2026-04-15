# Multiple Myeloma Public Review And Release Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-public-review-release-gate-v0`
- claim level: open-question
- gate status: next named phase seed
- clinical boundary: research-use-only, not medical advice
- release boundary: review gate, not release authorization
- last reviewed: `2026-04-15`

## Purpose

This gate starts the next named phase after
[Multiple Myeloma Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md).

The completed v0 autonomous loop produced a public artifact surface. This gate
defines what must be checked before that surface is treated as public-release
ready, announced, expanded, or used as the base for another autonomous loop.

It is intentionally human-gated. It does not authorize publication, release,
clinical use, expert-review claims, private case work, or new automation by
itself.

## Gate Decision

Current decision: `human-review-required`.

No release, public announcement, tag, case-derived publication, clinical
workflow, or new autonomous phase should start until the checklist below is
reviewed and a human operator selects the next named phase.

## Required Review Lanes

| Lane | Reviewer Role | Must Check | Output |
| --- | --- | --- | --- |
| Public safety | maintainer or governance reviewer | no PHI, no private records, no credentials, no patient-specific advice, no unsupported cure or vaccine claims | pass, fix list, or block |
| Scientific provenance | myeloma-informed reviewer | source IDs, subtype scope, uncertainty language, limitation text, and claim-level labels | pass, source-fix list, or expert-review-needed |
| Patient/public readability | patient advocate, caregiver advocate, or plain-language reviewer | whether public artifacts can be understood without private context and without implying care guidance | readability fixes or pass |
| Engineering integrity | repository maintainer | validation, schema examples, deterministic tool behavior, catalog/navigation coherence, and ignored local state | pass, test-fix list, or block |
| Stewardship | frg.earth steward or delegated maintainer | stewardship mark, public/private boundary, contribution pathway, and release framing | pass, framing fixes, or block |

## Pre-Release Checklist

Before any public-release action:

1. Run `make validate`.
2. Run `make review-packet-route-table ARGS="--self-test"`.
3. Run `make list-public-artifacts ARGS="--scope myeloma"` and confirm the
   expected public artifacts are navigable.
4. Run `make list-public-tasks ARGS="--status ready"` and confirm whether a
   new phase is intentionally queued or no tasks are ready.
5. Inspect the public artifact catalog for metadata count drift.
6. Inspect `.gitignore` and `git status --ignored --short` enough to confirm
   local Clawdad state, private data, and credentials are not tracked.
7. Review the public-loop completion handoff, definition-of-complete audit, and
   case-specific private-lab blocker register together.
8. Confirm that release notes do not imply treatment, trial, expanded-access,
   monitoring, ranking, or cure guidance.

## Release-Framing Rules

Allowed framing:

- public research infrastructure
- source-backed maps and schemas
- public-safe case-to-cure plumbing
- contribution and review readiness
- research-use-only tooling
- multiple myeloma public v0 artifact surface

Forbidden framing:

- cure found
- vaccine found
- treatment recommendation
- trial recommendation
- eligibility or expanded-access guidance
- patient matching
- target, therapy, trial, or option ranking
- expert-reviewed claims unless a named expert-review artifact says so
- publication-ready case-derived learning

## Decision Outcomes

| Outcome | Meaning | Next Action |
| --- | --- | --- |
| `release-ready-after-review` | Human reviewers passed all lanes and accepted the release framing. | Create a release note or PR description; then a human may publish. |
| `fixes-needed` | Review found public-safe corrections that do not require private data or external decisions. | Create a bounded fix queue and validate before reconsidering release. |
| `expert-review-needed` | Scientific language needs qualified review before stronger framing. | Keep claim levels modest and create or update expert-review packets. |
| `blocked-private-or-human` | Work requires private data, clinical judgment, legal/regulatory review, sponsor/site decisions, credentials, paid services, or account changes. | Stop public automation and move the item to private-lab or human-gated tracking. |
| `new-named-phase` | A human selects a new public phase with a clear aggregate gate. | Add a phase gate and task model before restarting autonomous work. |

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No credentials, account changes, paid APIs, or restricted datasets.
- No patient-specific diagnosis, prognosis, treatment, trial, expanded-access,
  monitoring, or candidate-option guidance.
- No target, therapy, trial, source, mechanism, artifact, task, or evidence
  ranking.
- No generated biomedical claims.
- No expert-review substitution.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This gate does not make any artifact release-ready by itself.
- This gate does not complete human review.
- This gate does not make any artifact expert-reviewed.
- This gate does not prove source coverage is comprehensive.
- This gate does not inspect private lab records or real case data.
- This gate does not authorize case-derived publication.
- This gate does not authorize review-packet assembly, generated packet output,
  generated claims, ranking, recommendation behavior, patient matching, trial
  matching, or publication workflow.
- This gate does not authorize public case processing or public case data
  upload.
- This gate does not provide medical advice, diagnostic guidance, treatment
  guidance, trial guidance, eligibility guidance, expanded-access guidance,
  monitoring guidance, or a cure claim.
