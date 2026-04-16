# Multiple Myeloma Expert Validation Issue Index v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-expert-validation-issue-index-v0`
- claim level: open-question
- issue status: public expert-validation requests opened
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This index links the current multiple myeloma expert-review packet items to
public GitHub issues.

The issues ask public-facing experts to validate language, provenance,
measurement context, source maturity, translational boundaries, and safety
framing. They do not ask reviewers to provide patient-specific medical advice,
diagnosis, prognosis, treatment recommendations, trial recommendations,
eligibility guidance, expanded-access guidance, or cure claims.

## Issue Set

| Packet | Review Item | Focus | Issue |
| --- | --- | --- | --- |
| BCMA Claim Set Expert Review Packet v0 | `target-status-claim-scope-review-v0` | claim-scope | [#22](https://github.com/SproutSeeds/curing-blood-cancer/issues/22) |
| BCMA Claim Set Expert Review Packet v0 | `tnfrsf17-loss-biomarker-review-v0` | measurement-assumptions | [#23](https://github.com/SproutSeeds/curing-blood-cancer/issues/23) |
| BCMA Claim Set Expert Review Packet v0 | `sema4a-translation-boundary-review-v0` | translation-boundary | [#24](https://github.com/SproutSeeds/curing-blood-cancer/issues/24) |
| BCMA Claim Set Expert Review Packet v0 | `multifactorial-resistance-scope-review-v0` | unsupported-inference | [#25](https://github.com/SproutSeeds/curing-blood-cancer/issues/25) |
| BCMA Claim Set Expert Review Packet v0 | `public-language-safety-review-v0` | public-readability | [#26](https://github.com/SproutSeeds/curing-blood-cancer/issues/26) |
| Multidisciplinary Review Packet Template v0 | `hematology-disease-state-review-template-v0` | claim-scope | [#27](https://github.com/SproutSeeds/curing-blood-cancer/issues/27) |
| Multidisciplinary Review Packet Template v0 | `cellular-therapy-review-template-v0` | translation-boundary | [#28](https://github.com/SproutSeeds/curing-blood-cancer/issues/28) |
| Multidisciplinary Review Packet Template v0 | `pathology-measurement-review-template-v0` | measurement-assumptions | [#29](https://github.com/SproutSeeds/curing-blood-cancer/issues/29) |
| Multidisciplinary Review Packet Template v0 | `genomics-target-biology-review-template-v0` | source-quality | [#30](https://github.com/SproutSeeds/curing-blood-cancer/issues/30) |
| Multidisciplinary Review Packet Template v0 | `trial-operations-review-template-v0` | translation-boundary | [#31](https://github.com/SproutSeeds/curing-blood-cancer/issues/31) |
| Multidisciplinary Review Packet Template v0 | `regulatory-access-review-template-v0` | unsupported-inference | [#32](https://github.com/SproutSeeds/curing-blood-cancer/issues/32) |
| Multidisciplinary Review Packet Template v0 | `safety-ethics-review-template-v0` | safety-language | [#33](https://github.com/SproutSeeds/curing-blood-cancer/issues/33) |
| Multidisciplinary Review Packet Template v0 | `patient-communication-review-template-v0` | public-readability | [#34](https://github.com/SproutSeeds/curing-blood-cancer/issues/34) |

## Packet Links

- [BCMA Claim Set Expert Review Packet v0](bcma-claim-set-expert-review-packet-v0.md)
- [BCMA Claim Set Expert Review Packet v0 JSON](bcma-claim-set-expert-review-packet-v0.json)
- [Multidisciplinary Review Packet Template v0](multidisciplinary-review-packet-template-v0.md)
- [Multidisciplinary Review Packet Template v0 JSON](multidisciplinary-review-packet-template-v0.json)

## Reviewer Request

For each issue, reviewers are asked to:

- check whether the public wording is too strong, unclear, or misleading
- identify missing source, assay, measurement, or disease-state context
- flag unsupported inference or accidental clinical-action language
- suggest weaker or clearer wording where needed
- cite source IDs, PMIDs, URLs, registry IDs, or regulatory anchors when
  possible
- state what readers must not infer from the review

## Resolution Path

An issue response can produce one of these public outcomes:

- `wording-fix-needed`: public artifact wording should be weakened or clarified
- `source-context-needed`: more provenance or measurement context is needed
- `expert-review-satisfied-for-item`: the specific item has enough expert
  response to update its local status
- `keep-expert-review-needed`: current language can remain public, but stronger
  claims stay blocked
- `blocked-private-or-clinical`: the next step needs private records, clinical
  judgment, institutional review, sponsor/site decisions, legal/regulatory
  review, or other non-public action

No issue response should be treated as medical advice or patient-specific
guidance.

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
- No expert-review substitution before qualified reviewers respond.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This index tracks issue requests, not completed expert review.
- Creating an issue does not validate any claim.
- Issue responses must be reviewed before artifact status changes.
- Expert-review-needed status remains until a follow-up artifact records the
  review outcome.
- This index does not prove source coverage is comprehensive.
- This index does not inspect private lab records or real case data.
- This index does not authorize generated claims, ranking, recommendation
  behavior, patient matching, trial matching, review-packet assembly, or
  publication workflow.
- This index does not provide medical advice, diagnostic guidance, treatment
  guidance, trial guidance, eligibility guidance, expanded-access guidance,
  monitoring guidance, or a cure claim.
