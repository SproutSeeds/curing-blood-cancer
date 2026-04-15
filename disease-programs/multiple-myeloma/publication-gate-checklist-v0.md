# Publication-Gate Checklist v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: multiple myeloma
- artifact type: public safety protocol
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- public data boundary: no real case data, no patient identifiers, no raw
  records, no re-identification keys

## Purpose

This checklist defines the public release gate for any case-derived learning
that might be downstreamed into the public multiple myeloma lane.

The gate is fail-closed. A checklist pass means only that a public artifact can
be prepared for ordinary repository review. It does not authorize publication
of real case facts, establish clinical truth, establish trial eligibility,
recommend treatment, recommend expanded access, recommend monitoring, or
complete private governance.

## Allowed Public Output Types

| Output Type | Allowed Public Shape | Not Allowed |
| --- | --- | --- |
| Synthetic method fixture | Fully synthetic example that exercises public schemas, protocols, or tooling. | Real case timelines, rare feature combinations, clinician notes, images, or identifiers. |
| Generic method improvement | A reusable checklist, template, schema summary, protocol field, or validator rule. | Private lab operations, re-identification keys, patient-specific decisions, or unreleasable source text. |
| Aggregate learning | De-identified aggregate pattern that has passed private governance and public safety review. | Any single-person fact, date tied to a person, site-level trace, or combination that could identify someone. |
| Public-source linkage | Linkage between public source IDs, claim IDs, gap IDs, query-record IDs, or measurement terms. | Linkage that reveals a private case, treating institution, clinician, sponsor contact, or real case trajectory. |

## Required Release Record

Every proposed case-derived public artifact should record:

- proposed public artifact ID and artifact class
- allowed output type
- disease and subtype scope
- public source IDs and access dates
- linked claim, evidence-gap, measurement-term, mechanism, query-record, or
  task IDs where relevant
- uncertainty and missingness notes
- limitations and what-not-to-infer language
- review status and needed reviewer roles
- privacy decision state
- clinical-use boundary
- final gate decision

## Gate Checklist

| Gate ID | Requirement | Pass Evidence | Fail-Closed Action |
| --- | --- | --- | --- |
| `gate-output-type` | The artifact is synthetic, generic method learning, public-source linkage, or separately reviewed aggregate learning. | Release record names one allowed output type. | Block public release until output type is narrowed. |
| `gate-privacy` | No PHI, identifiers, raw records, re-identification keys, exact dates tied to a person, images, free-text notes, or identifying feature combinations are present. | Privacy review state is `passed-public-boundary` and the artifact contains only public-safe fields. | Block release and return to private governance. |
| `gate-private-provenance` | Any private upstream reference is non-sensitive and does not expose records, dates, people, sites, sponsors, or treating-team context. | Metadata uses only a coarse private upstream path or omits private references. | Remove or rewrite the reference before public review. |
| `gate-public-provenance` | Public source IDs, artifact IDs, query-record IDs, claim IDs, evidence-gap IDs, or measurement-term IDs are present where the artifact depends on them. | Release record lists stable public IDs and source access dates. | Block release until provenance is traceable. |
| `gate-scope` | Disease, subtype, mechanism, treatment-class, measurement, and setting boundaries are explicit. | Scope field states what is and is not covered. | Rewrite scope before public review. |
| `gate-uncertainty` | Uncertainty, missingness, contradictions, and limitations are stated in plain language. | Limitations and what-not-to-infer sections are present. | Block release until limitations are explicit. |
| `gate-claim-label` | Facts, derived claims, hypotheses, open questions, and do-not-use-clinically material are separated. | Release record names the claim label used by each substantive statement. | Split or relabel claims before release. |
| `gate-review-status` | Source-checked, expert-review-needed, expert-reviewed, blocked, and deprecated statuses remain distinct. | Review status and needed reviewer roles are visible. | Block release if review status is ambiguous or overstated. |
| `gate-clinical-boundary` | The artifact contains no diagnosis, prognosis, treatment advice, trial advice, expanded-access advice, monitoring instruction, candidate ranking, or cure claim. | Clinical boundary text is present and matches repository safety rules. | Block release and remove clinical-use language. |
| `gate-candidate-options` | Patient-specific candidate options, option rankings, and action recommendations are not downstreamed. | Candidate material is absent or reduced to generic task, gap, query-pattern, or review prompt language. | Block release or convert to private-only review packet work. |
| `gate-external-decisions` | Clinical, legal, regulatory, sponsor, institutional-review, and treating-team decisions stay outside the public repo. | Release record names external decision classes as out of scope. | Block release until decision language is removed. |
| `gate-repository-readiness` | Metadata, catalog links, validation status, and public navigation links are prepared before publication. | `make validate` passes and catalog or README links are updated when required. | Keep artifact out of public release until validation passes. |

## Decision Outcomes

| Decision | Meaning | Public Action |
| --- | --- | --- |
| `blocked-private` | The material contains real case facts, private context, or unresolved governance. | Do not publish. Keep work private. |
| `revise-public-method` | The public idea is useful but needs narrower wording, provenance, or boundary repair. | Revise before repository review. |
| `aggregate-review-needed` | Aggregate learning may be possible but needs explicit private governance and public safety review. | Hold until all gates are documented. |
| `public-release-candidate` | The artifact is public-safe enough for normal repository review. | Review like any other public artifact; this is not clinical clearance. |
| `public-release-blocked` | One or more public safety gates failed. | Do not publish until failures are resolved. |

## Claim Separation Rules

| Claim Type | Public Use | Required Boundary |
| --- | --- | --- |
| Fact | Directly sourced public statement. | Cite source ID and scope. |
| Derived claim | Output of a documented public transform. | State method, assumptions, and limitations. |
| Hypothesis | Research idea requiring testing. | Do not present as validated or clinically actionable. |
| Open question | Known unknown or review point. | State what evidence or review is missing. |
| Do-not-use clinically | Safety warning or nonclinical placeholder. | Keep separate from decision-support language. |

## Do Not Publish

- patient-identifying data
- raw records, images, notes, exact dates tied to a person, or re-identification
  keys
- real case feature bundles or timelines
- patient-specific candidate options, rankings, or monitoring plans
- trial eligibility, site availability, sponsor availability, or expanded-access
  feasibility claims for a person
- clinical, legal, regulatory, sponsor, institutional-review, or treating-team
  decisions
- unsupported cure, vaccine, biomarker, safety, efficacy, or comparative
  benefit claims

## What This Checklist Does Not Prove

This checklist does not prove that any artifact is medically correct, complete,
expert-reviewed, clinically useful, legally cleared, regulatory-ready, sponsor
accepted, trial-eligible, or appropriate for any person. It only records whether
a public artifact candidate has satisfied the public repository safety boundary
for review.

## Review Boundary

This checklist is a public safety and publication-readiness protocol. It is not
medical advice, diagnostic guidance, treatment guidance, trial guidance,
expanded-access guidance, monitoring guidance, or a claim that multiple myeloma
has been cured.
