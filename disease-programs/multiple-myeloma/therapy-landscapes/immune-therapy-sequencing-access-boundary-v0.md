# Immune Therapy Sequencing And Access Boundary v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `immune-therapy-sequencing-access-boundary-v0`
- frontier lane: immune therapy sequencing and access boundary
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This map makes public immune-therapy and target-class references inspectable
without turning them into treatment advice, trial advice, eligibility guidance,
expanded-access guidance, product availability claims, sequencing
recommendations, or rankings.

It is a boundary artifact for CAR T-cell therapy, bispecific antibodies,
antibody-drug conjugates, and adjacent target references in multiple myeloma.
It does not decide what is available, appropriate, safe, effective, urgent, or
better for any person.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | The frontier roadmap names Lane 3 as immune therapy sequencing and access boundary with landscape records and status freshness fields. | Create one class-and-target boundary map before any explorer or dashboard. |
| Existing substrate | The treatment-class taxonomy already names CAR T-cell therapy, bispecific antibodies, antibody-drug conjugates, CD38 antibodies, SLAMF7 antibodies, and public source IDs. | Reuse taxonomy classes and source registry anchors instead of creating recommendations. |
| Status freshness | Regulatory and trial status can change quickly and may differ by product, country, disease state, line of therapy, site, and date. | Store status fields and source IDs; do not assert patient availability or eligibility. |
| Downstream tooling | No validated immune-therapy landscape record set exists yet. | Block sequencing, dashboard, trial matching, access matching, and ranking behavior until a validated record shape exists. |

## Source Anchors

- `nci_pdq_myeloma_hp`
- `nci_cancer_drug_dictionary`
- `clinicaltrials_gov`
- `clinicaltrials_gov_api_v2`
- `fda_drugs_at_fda`
- `dailymed`
- `ema_medicines`
- `dana_farber_car_t_update_2025`
- `fda_linvoseltamab_accelerated_approval_2025`
- `multiple-myeloma-treatment-class-taxonomy-v0`
- `therapy-record-schema-v0`
- `multiple-myeloma-frontier-roadmap-v0`

## Required Status Freshness Fields

Every future immune-therapy landscape record must preserve these fields before
reuse.

| Field | Required Capture | If Missing |
| --- | --- | --- |
| Therapy class | CAR T-cell therapy, bispecific antibody, antibody-drug conjugate, monoclonal antibody, target-linked therapy, or source-defined class. | `therapy-class-needed` |
| Product or agent name | Exact public source name when product-specific status is discussed. | `product-scope-needed` |
| Target or target class | BCMA, GPRC5D, FcRH5, CD38, SLAMF7, SEMA4A, or source-defined target. | `target-context-needed` |
| Status source | FDA, DailyMed, EMA, ClinicalTrials.gov, NCI, PubMed, institutional update, or other public source. | `status-source-needed` |
| Status label | Approved, withdrawn, discontinued, investigational, trial-registry snapshot, mechanism-only, hypothesis-only, or status-not-extracted. | `status-label-needed` |
| Jurisdiction | Country, regulator, registry, institution, or explicit not-applicable. | `jurisdiction-needed` |
| Status date | Source publication date, label date, registry data timestamp, access date, or explicit not reported. | `status-date-needed` |
| Disease-state scope | Source-defined multiple myeloma setting, relapse context, prior-exposure context, or not extracted. | `disease-state-needed` |
| Trial or registry scope | Registry ID, query timestamp, recruitment status, site scope, or explicit not a trial record. | `trial-scope-needed` |
| Uncertainty note | What can change or what was not extracted. | `uncertainty-needed` |
| Limitation text | Why the row cannot be used for care, trial selection, availability, eligibility, or ranking. | `limitation-needed` |

## Landscape Boundary Rows

These rows are intentionally class and target boundary rows. They are not
product records, label summaries, trial listings, or therapy recommendations.

| Row ID | Class Or Target Context | Examples Already Named Elsewhere | Status Freshness State | Required Source Checks | Uncertainty And Boundary |
| --- | --- | --- | --- | --- | --- |
| `immune-class-car-t-bcma-v0` | CAR T-cell therapy with common BCMA target context. | idecabtagene vicleucel and ciltacabtagene autoleucel appear as taxonomy examples. | `status-source-required` | FDA or local regulator, product label, DailyMed or equivalent label, ClinicalTrials.gov if trial context is used, and source access date. | Class presence does not imply availability, eligibility, safety, efficacy, sequencing, urgency, or durability for any person. |
| `immune-class-bispecific-bcma-v0` | Bispecific antibody with BCMA target context. | teclistamab, elranatamab, and linvoseltamab are public source examples that need product-specific verification before reuse. | `status-source-required` | FDA or local regulator, product label, DailyMed or equivalent label, ClinicalTrials.gov if trial context is used, and source access date. | Do not infer class interchangeability, post-BCMA fit, product access, sequencing, or comparative value. |
| `immune-class-bispecific-gprc5d-v0` | Bispecific antibody with GPRC5D target context. | talquetamab appears as a taxonomy example. | `status-source-required` | FDA or local regulator, product label, DailyMed or equivalent label, ClinicalTrials.gov if trial context is used, and source access date. | Target difference does not imply a next option, alternate-target suitability, or lower risk. |
| `immune-class-adc-bcma-v0` | Antibody-drug conjugate with BCMA target context. | belantamab mafodotin appears as a taxonomy example. | `status-change-sensitive` | FDA or local regulator, product label, withdrawn or discontinued status source when relevant, ClinicalTrials.gov if trial context is used, and source access date. | Regulatory status can change; do not infer availability, re-approval, access route, safety, efficacy, or sequencing. |
| `immune-target-fcrh5-v0` | FcRH5 target context for immune redirection research. | No product status is asserted in this map. | `mechanism-or-trial-source-needed` | PubMed, ClinicalTrials.gov, regulator if product-specific status is discussed, and source access date. | Target presence in a trial or paper does not establish actionability or availability. |
| `immune-target-cd38-v0` | CD38 antibody class and target context. | daratumumab and isatuximab appear as taxonomy examples. | `status-source-required` | FDA or local regulator, label source, NCI context source, and source access date. | A target class is not a sequencing rule and does not imply patient fit. |
| `immune-target-slamf7-v0` | SLAMF7 antibody class and target context. | elotuzumab appears as a taxonomy example. | `status-source-required` | FDA or local regulator, label source, NCI context source, and source access date. | A listed antibody target does not imply comparative benefit, eligibility, or next-line use. |
| `immune-target-sema4a-v0` | SEMA4A candidate adjacent-target research context. | Di Meo low-BCMA/SEMA4A public extraction appears in mechanism work. | `hypothesis-only` | PubMed source extraction, normal-tissue reactivity context, translational safety context, and source access date. | Research signal only; do not infer clinical safety, efficacy, availability, or target actionability. |

## Access-Boundary Rules

Use these rules before any future trial explorer, product dashboard, therapy
landscape, source extraction, or review packet references immune therapy
status.

| Rule | Required Behavior | Blocked Behavior |
| --- | --- | --- |
| Product status | Copy source ID, source date, access date, jurisdiction, and status label. | Do not summarize a product as available or unavailable for any person. |
| Trial status | Copy registry ID, registry timestamp, recruitment status, site scope, and query URL when used. | Do not infer eligibility, site availability, sponsor access, enrollment advice, or trial fit. |
| Sequencing language | Use only as source-framed research question or prior-exposure context. | Do not say what should come before or after another therapy for a person. |
| Target language | Treat target names as record keys that require assay, disease-state, and source context. | Do not infer target actionability from target presence, low expression, or trial use. |
| Comparison language | Preserve source scope and denominator before any class or product comparison. | Do not rank classes, products, trials, targets, mechanisms, or sources. |
| Access language | Route real access, eligibility, insurance, timing, referral, and expanded-access questions to clinical teams and responsible institutions. | Do not generate access instructions or expanded-access paths. |

## Allowed Status Values

- `approved-product-date-stamped`
- `withdrawn-or-discontinued-date-stamped`
- `investigational-date-stamped`
- `trial-registry-snapshot-only`
- `mechanism-or-trial-source-needed`
- `hypothesis-only`
- `status-source-required`
- `status-change-sensitive`
- `status-not-extracted`

These values are record-quality labels for public research infrastructure.
They are not clinical status labels for any person.

## Next Public Task Draft

The next useful public contribution is source extraction, not a dashboard:

- extract product-specific status fields from FDA, DailyMed, EMA, NCI, and
  registry sources into a validated immune-therapy landscape record shape
- keep CAR T, bispecific, antibody-drug conjugate, CD38, SLAMF7, FcRH5, and
  adjacent-target rows date-stamped and non-advisory
- preserve withdrawn, discontinued, investigational, and trial-only contexts
  without converting them into access guidance

## Limitations

- This is a public research map, not a treatment guide.
- This is not medical advice.
- This is not diagnostic guidance.
- This is not treatment, trial, eligibility, expanded-access, monitoring, or
  referral guidance.
- This does not claim that any immune therapy cures multiple myeloma.
- This does not rank therapies, products, targets, trials, mechanisms, sources,
  artifacts, or evidence.
- This does not establish current availability, eligibility, safety, efficacy,
  indication, access route, sequencing, or patient fit.
- This does not use real case data, patient-identifying data, private records,
  private expert correspondence, or private lab context.
- Regulatory status, labels, trial status, site availability, and product
  availability can change after the source access date.
- Any real patient-specific question belongs with treating clinicians, trial
  sites, sponsors, institutions, and responsible regulators, not this repo.
