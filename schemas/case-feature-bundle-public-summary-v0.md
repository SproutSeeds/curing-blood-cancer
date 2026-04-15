# Case-Feature Bundle Public Summary v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact status: `public-shape-summary-v0`
- claim level: `open-question`
- last reviewed: `2026-04-15`
- clinical boundary: research-use-only, not medical advice

## Purpose

This artifact describes the public-safe shape of a future private
`case-feature-bundle` for multiple myeloma case-to-cure research workflows.

It is not a public intake form, not a case upload template, and not a schema
that should be filled with real case facts in this repo. It exists so public
contributors can understand which field groups the private pipeline expects,
which provenance and uncertainty fields must travel with those groups, and
which material must never cross into the public repository.

## Non-Intake Boundary

Do not use this artifact to submit or reconstruct a real case.

Never place any of the following in this repo:

- patient identifiers or re-identification keys
- raw records, reports, images, notes, or free text from a medical record
- dates tied to a person
- provider names, site names, record numbers, addresses, or locations that
  could identify a person
- rare combinations of clinical, genomic, pathology, timing, or treatment facts
  that could identify a person without privacy review
- patient-specific candidate options, rankings, recommendations, monitoring
  plans, or review decisions

Real case features belong only in a governed private environment with consent,
authorization, privacy review, clinical ownership, and audit controls.

## Relationship To The Private Shape

The private lab may define a fillable private schema at a path such as:

```text
../curing-blood-cancer-lab/cases/<case_id>/normalized/case-feature-bundle.json
```

That private schema is outside this public repo. This public summary can guide
the allowed field groups and safety gates, but it must not become a public case
record format.

## Public-Safe Field Groups

| Field Group | Public-Safe Description | Required Public Context | Not Allowed In Public |
| --- | --- | --- | --- |
| Disease-state envelope | Controlled categories describing myeloma disease setting, response-state vocabulary, and risk-context field names. | Disease program, disease-state scope, source IDs, uncertainty, missingness flags, review status. | Real diagnosis details, staging dates, exact course timeline, clinician notes, or rare feature combinations. |
| Measurement context | Field names for MRD method, assay sensitivity or threshold, specimen context, imaging linkage, response state, and relapse definition. | Measurement-term IDs, source-defined methods, threshold provenance, sample-context notes, limitation text. | Actual test dates, raw lab values, images, report text, unreviewed assay interpretation, or patient-level prognosis. |
| Therapy exposure context | Treatment-class IDs, exposure-field names, line-context categories, response-field names, and constraint-field names. | Treatment taxonomy IDs, source IDs, class-level uncertainty, review owner, missingness notes. | Drug-specific instructions, doses, schedules, toxicity advice, sequencing recommendations, or patient-specific rankings. |
| Molecular and immune context | Field names for target assay categories, genomic-feature buckets, immune-fitness categories, and mechanism-link fields. | Source IDs, mechanism-group IDs, assay-method provenance, lab-validity review status, overclaiming boundary. | Unique variants, raw molecular reports, images, unreviewed target calls, or clinical actionability claims. |
| Evidence linkage | Links from private features to public source, claim, evidence-gap, mechanism, measurement, trial-query, and extraction IDs. | Stable public IDs, source freshness status, retrieval date class, and limitations. | Public links that expose private record locations, real case IDs, or identifying source combinations. |
| Review and gate status | Field names for consent gate, PHI gate, measurement review, lab-validity review, source freshness, and publication gate state. | Review role, gate name, pass or blocked state, missing information, and public-export decision. | Names of clinicians, institutions, sponsors, sites, reviewers, or review dates tied to a person. |

## Allowed Public Outputs

The public repo may contain:

- this shape summary
- synthetic fixtures with no real case facts
- public source IDs and query record IDs
- schema-improvement notes
- measurement glossary updates
- mechanism or evidence-gap updates derived from public sources
- aggregate or de-identified learning only after a publication gate

The public repo must not contain a filled `case-feature-bundle` for a real
person.

## Minimal Public-Safe Record State

If a future public artifact refers to case-feature-bundle work, it should use
one of these public-safe states instead of exposing case data:

| State | Meaning |
| --- | --- |
| `private-only-field-group` | The field group exists only in the private workflow and is named publicly for schema planning. |
| `synthetic-example-only` | The field group is demonstrated with synthetic placeholders only. |
| `aggregate-learning-only` | A privacy-reviewed aggregate or de-identified learning can be public, but no person-level record is exposed. |
| `schema-improvement-only` | The public output is a generic schema, glossary, source, or validation improvement. |
| `blocked-from-public` | The field group, value, or combination is too identifying, too case-specific, or too clinically actionable for public release. |

## Provenance Requirements

Any public method artifact downstream of this shape must preserve:

- disease program and disease-state scope
- public source IDs
- measurement-term IDs when measurement context is involved
- mechanism-group IDs when biological context is involved
- claim IDs, evidence-gap IDs, or query-record IDs when relevant
- uncertainty and missingness notes
- review status
- clinical-use boundary
- limitations and what-not-to-infer language

## Publication Gate

Case-derived public learning must fail closed unless all of the following are
true:

- privacy review confirms that no person can be identified directly or through
  feature combinations
- all source, measurement, mechanism, and review provenance is captured
- the output is aggregate, synthetic, or generic method learning
- clinical-use boundary language is present
- uncertainty and limitations are explicit
- no patient-specific candidate option, treatment decision, trial advice,
  expanded-access advice, or monitoring instruction is included

Use the multiple myeloma
[Publication-Gate Checklist v0](../disease-programs/multiple-myeloma/publication-gate-checklist-v0.md)
as the public release-readiness protocol for this boundary.

## Validator Opportunities

Future validators should check that public artifacts referring to
case-feature-bundle work:

- use one of the public-safe record states above
- do not contain real case fields or free-text notes
- link to public source IDs and measurement-term IDs where applicable
- include limitations and clinical-use boundary text
- keep `public_export_allowed` false for any case-specific record

## Review Boundary

This artifact is a public method summary. It does not provide diagnosis,
prognosis, treatment guidance, trial guidance, expanded-access guidance,
monitoring guidance, or a claim that a cure has been found.
