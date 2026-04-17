# Multiple Myeloma Expert Response Validation Ledger v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-expert-response-validation-ledger-v0`
- claim level: open-question
- ledger status: public-safe response intake map
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This ledger maps the current public expert-validation issues to safe response
dispositions, artifact paths, and next public actions.

It is the first frontier artifact for expert response intake. It records issue
state and disposition readiness without copying private correspondence,
publishing expert email text, or treating any response as medical advice,
endorsement, consensus, or completed review.

## Intake Boundary

This ledger may use public issue metadata, public artifact IDs, public source
IDs, and safe disposition labels.

This ledger must not include:

- private emails or unpublished correspondence
- patient-identifying data or real case data
- diagnosis, prognosis, treatment, trial, expanded-access, monitoring, or
  candidate-option guidance
- reviewer comments that require private permission before publication
- statements that imply endorsement, expert consensus, publication readiness,
  or clinical validity

## Allowed Dispositions

| Disposition | Meaning | What It Allows | What It Does Not Allow |
| --- | --- | --- | --- |
| `wording-fix-needed` | Public wording should be weakened, clarified, or made safer. | Open a public artifact wording task or patch with source-preserving language. | Does not upgrade the claim to expert-reviewed. |
| `source-context-needed` | More public provenance, assay, measurement, disease-state, regulatory, or registry context is needed. | Add source extraction tasks or source-context notes. | Does not fill missing context from private records. |
| `expert-review-satisfied-for-item` | A specific item has enough public, permissioned, source-contextual response to update its local status. | Mark only that item as satisfied and link the public basis. | Does not imply broad endorsement, clinical validity, or publication readiness. |
| `keep-expert-review-needed` | The item remains open because no safe public disposition has been completed. | Keep current artifact language bounded and review-needed. | Does not block public artifact navigation. |
| `needs-public-source-before-use` | A response or proposed change needs a public source before use. | Add a source-request task or source-registry delta. | Does not cite private correspondence as evidence. |
| `blocked-private-or-clinical` | The next step needs private records, clinical judgment, sponsor/site verification, regulatory/legal review, or another non-public decision. | Record a blocker and fail closed. | Does not route the work into public tooling. |
| `out-of-scope-for-public-repo` | The request is not appropriate for the public repo. | Close or defer the public issue with a boundary note. | Does not create private-work instructions in public. |

## Disposition Rules

- Default status is `keep-expert-review-needed`.
- A public issue comment does not change artifact status by itself.
- A private response may be represented only as a non-content disposition, such
  as `source-context-needed` or `blocked-private-or-clinical`, unless the
  reviewer gives public permission and public source context exists.
- `expert-review-satisfied-for-item` requires a public issue link, reviewer
  permission or public authorship, source context, and an artifact update that
  preserves limitations.
- If a response asks for patient-specific interpretation, treatment guidance,
  trial guidance, expanded-access guidance, monitoring guidance, or option
  ranking, the disposition must be `blocked-private-or-clinical`.
- If a response proposes a stronger cure, safety, efficacy, eligibility,
  availability, or treatment-path claim without public source support, the
  disposition must be `needs-public-source-before-use` or
  `wording-fix-needed`.

## Current Issue Ledger

Issue metadata was checked from the public GitHub issue API on `2026-04-16`.
The ledger records public issue state and public comment counts only; comment
text is not copied here.

| Issue | Review Item | Packet | Focus | Target Artifact Path | Public Issue State | Public Comment State | Current Ledger Disposition | Next Public Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [#22](https://github.com/SproutSeeds/curing-blood-cancer/issues/22) | `target-status-claim-scope-review-v0` | BCMA claim set expert review packet | claim-scope | `disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md`; `disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T04:52:38Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage only public, source-backed response content; if wording is too strong, use `wording-fix-needed`; if assay or specimen context is missing, use `source-context-needed`. |
| [#23](https://github.com/SproutSeeds/curing-blood-cancer/issues/23) | `tnfrsf17-loss-biomarker-review-v0` | BCMA claim set expert review packet | measurement-assumptions | `disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md`; `disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T04:51:49Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for source-specific wording, denominator context, and biomarker limitations; require public source context before any stronger claim. |
| [#24](https://github.com/SproutSeeds/curing-blood-cancer/issues/24) | `sema4a-translation-boundary-review-v0` | BCMA claim set expert review packet | translation-boundary | `disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md`; `disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T04:51:00Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for alternate-target wording, normal-tissue context, and safety uncertainty; keep treatment or target-actionability implications blocked. |
| [#25](https://github.com/SproutSeeds/curing-blood-cancer/issues/25) | `multifactorial-resistance-scope-review-v0` | BCMA claim set expert review packet | unsupported-inference | `disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md`; `disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T04:50:10Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for over-weighted mechanism language, contradiction context, and non-antigen relapse gaps; do not convert mechanisms into patient options. |
| [#26](https://github.com/SproutSeeds/curing-blood-cancer/issues/26) | `public-language-safety-review-v0` | BCMA claim set expert review packet | public-readability | `disease-programs/multiple-myeloma/reviews/bcma-claim-set-expert-review-packet-v0.md`; `disease-programs/multiple-myeloma/evidence-claims/bcma-antigen-escape-claim-set-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T00:49:12Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for language that could be mistaken for diagnosis, treatment guidance, trial guidance, evidence-strength ranking, or cure claim. |
| [#27](https://github.com/SproutSeeds/curing-blood-cancer/issues/27) | `hematology-disease-state-review-template-v0` | multidisciplinary review packet template | claim-scope | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T00:49:06Z` | 2 public comments; not copied or dispositioned here | `keep-expert-review-needed` | Triage for disease-state, response, relapse, and MRD boundaries; keep prognosis and treatment-selection language blocked. |
| [#28](https://github.com/SproutSeeds/curing-blood-cancer/issues/28) | `cellular-therapy-review-template-v0` | multidisciplinary review packet template | translation-boundary | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T01:37:37Z` | 2 public comments; not copied or dispositioned here | `keep-expert-review-needed` | Triage for CAR T, bispecific, and immune-effector language; keep sequencing, availability, eligibility, and recommendation inferences blocked. |
| [#29](https://github.com/SproutSeeds/curing-blood-cancer/issues/29) | `pathology-measurement-review-template-v0` | multidisciplinary review packet template | measurement-assumptions | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T00:47:31Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for specimen source, assay method, threshold, sensitivity, timing, and denominator fields before any comparison language. |
| [#30](https://github.com/SproutSeeds/curing-blood-cancer/issues/30) | `genomics-target-biology-review-template-v0` | multidisciplinary review packet template | source-quality | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T01:36:48Z` | 2 public comments; not copied or dispositioned here | `keep-expert-review-needed` | Triage for source maturity, model-system boundaries, antigen-density context, and target-biology limitations. |
| [#31](https://github.com/SproutSeeds/curing-blood-cancer/issues/31) | `trial-operations-review-template-v0` | multidisciplinary review packet template | translation-boundary | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md`; `protocols/clinicaltrials-gov-query-protocol-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T00:46:40Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for registry-pattern language only; keep eligibility, availability, site verification, sponsor access, and trial recommendation blocked. |
| [#32](https://github.com/SproutSeeds/curing-blood-cancer/issues/32) | `regulatory-access-review-template-v0` | multidisciplinary review packet template | unsupported-inference | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md`; `disease-programs/multiple-myeloma/candidate-option-scoring-rubric-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T01:35:58Z` | 2 public comments; not copied or dispositioned here | `keep-expert-review-needed` | Triage for generic access-pathway wording only; any sponsor, site, regulatory, legal, or institutional decision remains outside the public repo. |
| [#33](https://github.com/SproutSeeds/curing-blood-cancer/issues/33) | `safety-ethics-review-template-v0` | multidisciplinary review packet template | safety-language | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md`; `disease-programs/multiple-myeloma/publication-gate-checklist-v0.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T00:45:49Z` | 1 public comment; not copied or dispositioned here | `keep-expert-review-needed` | Triage for privacy, consent, safety, release, and overclaiming boundaries; keep any case-specific or clinical safety decision blocked. |
| [#34](https://github.com/SproutSeeds/curing-blood-cancer/issues/34) | `patient-communication-review-template-v0` | multidisciplinary review packet template | public-readability | `disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-template-v0.md`; `disease-programs/multiple-myeloma/README.md` | open; labels: `help wanted`, `multiple myeloma`, `expert review`; updated `2026-04-16T01:35:09Z` | 2 public comments; not copied or dispositioned here | `keep-expert-review-needed` | Triage for public readability and no-advice framing; keep personal risk, treatment, trial, monitoring, or cure implications blocked. |

## Reviewer-Lens Summary

| Reviewer Lens | Issues | Current Public Status | Next Safe Action |
| --- | --- | --- | --- |
| Hematology and disease state | #22, #25, #27 | `keep-expert-review-needed` | Triage only public, source-backed responses and update wording or context tasks if needed. |
| Pathology, assay, MRD, and measurement | #22, #23, #27, #29 | `keep-expert-review-needed` | Preserve specimen, assay, threshold, timing, sensitivity, and denominator context. |
| Cellular therapy and immunotherapy | #24, #28 | `keep-expert-review-needed` | Keep CAR T, bispecific, target, and sequencing language non-prescriptive. |
| Genomics and target biology | #23, #30 | `keep-expert-review-needed` | Require source maturity and model-system context before stronger target-biology language. |
| Trial operations and access | #31, #32 | `keep-expert-review-needed` | Keep registry, regulatory, sponsor, site, and access language generic and non-advisory. |
| Safety, ethics, and governance | #32, #33 | `keep-expert-review-needed` | Fail closed when privacy, consent, clinical safety, legal, regulatory, sponsor, institutional, or publication gates are incomplete. |
| Patient advocacy and public communication | #26, #34 | `keep-expert-review-needed` | Use wording fixes only when they improve clarity without creating advice or action language. |
| Tooling and public artifact governance | #26, #31, #33, #34 | `keep-expert-review-needed` | Do not use responses to authorize generated claims, ranking, matching, packet assembly, or publication workflow. |

## Lane Status

Frontier Lane 1 now has a first public artifact for expert response intake.

The lane remains operationally open because no issue is marked
`expert-review-satisfied-for-item` in this ledger. All 13 items have a safe
status and next public action, but expert-review-needed status remains until a
future public-source-backed disposition is recorded and validated.

The next frontier lane is MRD, deep response, and endpoint language.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No credentials, paid APIs, account changes, or restricted datasets.
- No private emails or unpublished correspondence.
- No patient-specific diagnosis, prognosis, treatment, trial, expanded-access,
  monitoring, screening, or candidate-option guidance.
- No target, therapy, trial, source, mechanism, artifact, task, or evidence
  ranking.
- No generated biomedical claims.
- No expert-review substitution.
- No publication authorization.
- No cure or vaccine claim.

## Limitations

- This ledger is a public response-intake map, not completed expert review.
- This ledger does not prove that any public issue response is expert-authored,
  source-backed, or sufficient for artifact revision.
- Public comment counts do not establish consensus, endorsement, correctness,
  safety, efficacy, eligibility, availability, patient fit, or clinical value.
- This ledger does not copy, summarize, or rely on private correspondence.
- This ledger does not inspect private lab records or real case data.
- This ledger does not authorize generated claims, ranking, recommendation
  behavior, patient matching, trial matching, review-packet assembly, or
  publication workflow.
- This ledger does not make any artifact expert-reviewed or publication-ready.
- This ledger does not provide medical advice, diagnostic guidance, treatment
  guidance, trial guidance, eligibility guidance, expanded-access guidance,
  screening guidance, monitoring guidance, or a cure claim.
