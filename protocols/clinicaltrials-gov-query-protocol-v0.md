# ClinicalTrials.gov Query Protocol v0

- protocol id: `clinicaltrials-gov-query-protocol-v0`
- date: `2026-04-14`
- scope: blood-cancer trial discovery and provenance capture
- artifact class: `protocol`
- claim level: `derived`

## Boundary

This protocol is for public trial discovery and artifact provenance. It is not
medical advice, an eligibility decision, an enrollment recommendation, or a
claim that any trial is safe, effective, open, or appropriate for any person.

ClinicalTrials.gov records can be incomplete, stale, or changed after a search.
For any real person, eligibility and availability must be verified by the trial
site and treating clinicians.

Case-matching provenance fields in this protocol are public-safe audit context
only. They may describe which allowed field groups motivated a query, but they
must not include private case values, identifiers, dates tied to a person,
free-text notes, images, eligibility conclusions, or patient-specific trial
recommendations.

## Source IDs

This protocol uses source IDs from [Source Registry v0](../sources/source-registry-v0.md).

- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`

## Search Surfaces

| Surface | Use | Required Record |
| --- | --- | --- |
| ClinicalTrials.gov web search | Human-readable exploration and sharing. | Public search URL, date, search terms, filters. |
| ClinicalTrials.gov API v2 `/studies` | Reproducible query capture and tool workflows. | API URL, query params, API version, data timestamp, total count if requested. |
| ClinicalTrials.gov API v2 `/version` | Freshness/provenance check. | `apiVersion` and `dataTimestamp`. |

## Minimum Query Inputs

| Field | Required | Example | Notes |
| --- | --- | --- | --- |
| `condition` | yes | `Multiple Myeloma` | Use accepted subtype language where possible. |
| `intervention_or_class` | recommended | `CAR T` or `teclistamab` | Can be a treatment class, target, drug, device, or vaccine concept. |
| `recruitment_status` | recommended | `RECRUITING`, `NOT_YET_RECRUITING` | `ACTIVE_NOT_RECRUITING` may be useful for landscape review but not enrollment discovery. |
| `location` | optional | `United States`, `Chicago, Illinois`, `Europe` | Location search can miss trials with unusual site records. |
| `age_group` | optional | `ADULT`, `OLDER_ADULT` | Record if used; do not infer eligibility from age filter alone. |
| `phase` | optional | `PHASE1`, `PHASE2`, `PHASE3` | Phase filters help landscape review but do not rank quality. |
| `source_taxonomy_class` | optional | `myeloma_class_car_t_cell_therapy` | Use taxonomy IDs when mapping searches to artifacts. |
| `case_matching_provenance` | optional | public-safe field groups only | Use only for research provenance; never include real case values or infer eligibility. |

## API Pattern

Base endpoint:

```text
https://clinicaltrials.gov/api/v2/studies
```

Recommended query parameters:

| Parameter | Example | Meaning |
| --- | --- | --- |
| `query.cond` | `Multiple Myeloma` | Condition or disease query. |
| `query.intr` | `CAR T` | Intervention query. |
| `query.locn` | `United States` | Location query. |
| `filter.overallStatus` | `RECRUITING,NOT_YET_RECRUITING` | Recruitment status filter. |
| `countTotal` | `true` | Ask API to return `totalCount`. |
| `pageSize` | `10` | Number of records returned in this page. |

Example API query:

```text
https://clinicaltrials.gov/api/v2/studies?query.cond=Multiple%20Myeloma&query.intr=CAR%20T&query.locn=United%20States&filter.overallStatus=RECRUITING,NOT_YET_RECRUITING&countTotal=true&pageSize=10
```

Freshness endpoint:

```text
https://clinicaltrials.gov/api/v2/version
```

On `2026-04-14`, this endpoint returned `apiVersion` `2.0.5` and
`dataTimestamp` `2026-04-13T13:00:05`.

## Query Procedure

1. Choose the disease scope.
2. Choose one intervention class, target, drug, vaccine concept, or mechanism.
3. Decide whether the goal is enrollment discovery, landscape review, or source
   monitoring.
4. Choose recruitment statuses.
5. Build a web-search URL for human review.
6. Build an API URL for reproducibility.
7. Fetch `/api/v2/version` and record `apiVersion` plus `dataTimestamp`.
8. Fetch the `/api/v2/studies` query with `countTotal=true`.
9. Record the query in `clinicaltrials-gov-query-record-template-v0.json`.
10. If the query is for case-matching research, record only public-safe
    case-matching provenance fields and exclude private case facts.
11. Review trial records manually before making any public artifact claim.
12. If the search is used in a public artifact, cite the query record and avoid
    patient-specific recommendation language.

## Output Record Fields

Every query record should include:

- protocol id
- query id
- run date
- source IDs
- disease scope
- taxonomy class ID if available
- intended use
- web URL
- API URL
- API version
- API data timestamp
- query parameters
- case-matching provenance block, if the intended use is
  `case-matching-research`
- total count if requested
- review notes
- limitations

## Case-Matching Research Provenance

Use these fields only to explain why a public-safe trial query was run. They do
not establish trial relevance, eligibility, availability, safety, efficacy, or
fit for any person.

| Field | Required For Case-Matching Research? | Public-Safe Meaning |
| --- | --- | --- |
| `case_matching_use` | yes | Boolean stating whether the query was motivated by a private or synthetic case-feature workflow. |
| `case_feature_bundle_public_summary_id` | yes | Public summary ID that defines allowed field groups, currently `case-feature-bundle-public-summary-v0`. |
| `case_feature_bundle_state` | yes | One of the public-safe states from the case-feature bundle summary, such as `private-only-field-group`, `synthetic-example-only`, `aggregate-learning-only`, or `schema-improvement-only`. |
| `public_feature_group_ids` | yes | Generic field-group names, such as disease-state, measurement, therapy exposure, molecular/immune context, or evidence linkage. |
| `public_feature_to_query_rationale` | yes | Short rationale connecting public-safe field groups to query terms without exposing private values. |
| `excluded_private_fields` | yes | Explicit list of private material excluded from the query record. |
| `matching_boundary` | yes | Boundary text stating that the record is not an eligibility decision or trial recommendation. |
| `verification_required_before_use` | yes | Required human or institutional checks before any real-world trial discussion. |

Allowed `public_feature_group_ids` are shape-level labels only:

- `disease-state-envelope`
- `measurement-context`
- `therapy-exposure-context`
- `molecular-immune-context`
- `evidence-linkage`
- `review-and-gate-status`

Do not record a diagnosis timeline, actual prior therapies, assay results,
genomic details, locations, clinician notes, or other private case facts in a
public query record.

## Status Policy

| Status | Use In This Protocol |
| --- | --- |
| `RECRUITING` | Enrollment-discovery searches. Still requires site verification. |
| `NOT_YET_RECRUITING` | Near-future landscape searches. Still requires site verification. |
| `ACTIVE_NOT_RECRUITING` | Landscape or comparator searches, not enrollment discovery. |
| `COMPLETED` | Evidence/history searches, not enrollment discovery. |
| `TERMINATED`, `WITHDRAWN`, `SUSPENDED` | Failure-mode or historical searches; record carefully. |

## Limits

- A trial listing is not proof that a trial is open at a specific site.
- A trial listing is not proof that a person is eligible.
- A trial listing is not proof of safety or efficacy.
- Case-matching provenance is not proof that a trial is relevant to a person.
- Search counts can change as ClinicalTrials.gov records are updated.
- Query strings can miss studies that use different disease or intervention
  wording.
- ClinicalTrials.gov is a registry, not a substitute for source-paper review or
  clinician judgment.
