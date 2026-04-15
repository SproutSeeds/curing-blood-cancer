# Case-To-Cure Pipeline Blueprint v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- pipeline status: `blueprint-v0`
- claim level: `open-question`
- last reviewed: `2026-04-15`
- clinical boundary: research pipeline blueprint, not medical advice

## Purpose

This artifact defines the exact pipeline plumbing needed to move from a future
consented multiple myeloma case toward a cure-oriented action plan without
placing actual case data in the public repo.

The public repo can specify data contracts, gates, source flows, scoring logic,
and publication boundaries. It cannot hold patient-identifying data, determine
care, recommend a treatment, recommend a trial, or claim that a cure has been
found.

## Cure-Oriented Definition

For a particular case, "cure" must be operationalized by the treating clinical
team before any analysis begins.

Candidate case-specific outcomes may include:

- sustained measurable-residual-disease-negative remission
- durable relapse-free survival after deep response
- treatment-free or low-burden remission where clinically appropriate
- prevention of an expected relapse mechanism after prior therapy
- safe transition from active disease control to long-term monitoring

The pipeline may help organize evidence around those outcomes. It does not
prove that any outcome is achievable for a person.

## Safety And Governance Boundary

This blueprint assumes:

- real case data stays outside this public repo
- consent and authorization are handled before any case workflow starts
- PHI, identifiers, raw clinical records, and re-identification keys remain in a
  governed private environment
- any patient-specific clinical decision is made by qualified clinicians
- any software that produces patient-specific treatment outputs receives
  appropriate legal, regulatory, safety, and quality review before use
- investigational-product access is handled through trial enrollment,
  expanded-access pathways, or other clinician-governed mechanisms

## Data Zones

| Zone | Location | Contains | Public? |
| --- | --- | --- | --- |
| Case vault | outside this repo | PHI, raw records, re-identification keys, consents, clinician notes | no |
| Private lab case workspace | `../curing-blood-cancer-lab/cases/<case_id>/` | normalized case features, evidence packets, review drafts | no |
| Public method surface | this repo | schemas, protocols, source maps, synthetic examples, de-identified aggregate learnings | yes |
| Clinical system of record | treating institution | official clinical decisions, orders, monitoring, adverse events | no |

## Pipeline Overview

| Stage | Name | Private Input | Public Input | Private Output | Public Output | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| `case_00` | Governance setup | consent, authorization, clinician owner | this blueprint | case workspace and audit log | none | consent and role check |
| `case_01` | Intake partition | raw records, reports, images, labs | source registry shape | PHI inventory and safe manifest | synthetic manifest shape only | PHI boundary check |
| `case_02` | De-identification plan | PHI inventory | HHS de-identification guidance | de-identification plan | public de-ID checklist, if generic | privacy review |
| `case_03` | Disease-state normalization | diagnosis, stage, prior lines, response status | myeloma glossary and wedge | normalized disease-state record | schema improvements only | clinician review |
| `case_04` | Measurement normalization | MRD, response, relapse, labs, imaging | measurement glossary | measurement context record | measurement gap updates | measurement review |
| `case_05` | Molecular and immune context | genomics, pathology, flow, target assays | mechanism maps and source registry | molecular/immune feature table | public extraction tasks only | lab validity review |
| `case_06` | Exposure and resistance map | prior therapies, toxicities, refractory status | treatment taxonomy | therapy exposure map | taxonomy gaps | clinician review |
| `case_07` | Evidence retrieval | normalized case features | NCI, PubMed, ClinicalTrials.gov, FDA sources | source-backed evidence packet | public source/query records | source freshness check |
| `case_08` | Candidate hypothesis generation | evidence packet | claim schemas and opportunity map | candidate option set | no patient-specific options | safety boundary check |
| `case_09` | Candidate scoring | candidate option set | scoring rubric | ranked research and clinical-review questions | de-identified scoring rubric updates | no auto-action gate |
| `case_10` | Feasibility and exclusion review | ranked questions, records | public trial/drug sources | feasibility notes | public evidence gaps | clinician and site verification |
| `case_11` | Multidisciplinary review | all private packets | public review packet template | review decision record | reusable review template updates | tumor board or equivalent |
| `case_12` | Action-path selection | review decision | regulatory and source references | standard-care, trial, expanded-access, research-only, or no-go path | generic pathway map | clinician owner signoff |
| `case_13` | Monitoring plan | selected path | measurement glossary | monitoring and stop-rule plan | generic monitoring schema | clinical safety review |
| `case_14` | Outcome capture | follow-up data | outcome schema draft | outcome and learning record | de-identified aggregate artifact only | privacy and publication review |

## Plumbing Contracts

These contracts describe the shape of the future pipeline. They are not case
records.

### Case Intake Manifest

Private-only path:

```text
../curing-blood-cancer-lab/cases/<case_id>/intake/case-intake-manifest.json
```

Shape:

```json
{
  "case_id": "private-pseudonymous-id",
  "disease_program": "multiple-myeloma",
  "consent_status": "pending|approved|withdrawn",
  "clinical_owner": "private-role-reference",
  "allowed_uses": ["care-support", "research-review", "public-aggregate-learning"],
  "raw_record_inventory": [
    {
      "record_type": "pathology|lab|imaging|genomics|treatment-history|note",
      "source_system": "private",
      "contains_phi": true,
      "received_at": "YYYY-MM-DD",
      "private_uri": "case-vault://..."
    }
  ],
  "public_export_allowed": false
}
```

### Normalized Case Feature Bundle

Private-only path:

```text
../curing-blood-cancer-lab/cases/<case_id>/normalized/case-feature-bundle.json
```

Shape:

```json
{
  "case_id": "private-pseudonymous-id",
  "disease_state": {
    "diagnosis": "multiple myeloma",
    "disease_setting": "newly-diagnosed|relapsed|refractory|post-CAR-T|post-transplant|maintenance",
    "response_state": "source-defined",
    "risk_context": ["private-reviewed-feature"]
  },
  "measurement_context": {
    "mrd_method": "flow|ngs|imaging|unknown",
    "mrd_threshold": "source-defined",
    "sample_context": "bone-marrow|blood|imaging|other",
    "relapse_definition": "source-defined"
  },
  "therapy_exposure": [
    {
      "class_id": "myeloma_class_*",
      "agent_or_strategy": "private-reviewed",
      "line_context": "private-reviewed",
      "response": "source-defined",
      "toxicity_or_constraint": "private-reviewed"
    }
  ],
  "molecular_immune_context": {
    "target_assays": ["BCMA|GPRC5D|FcRH5|other|unknown"],
    "genomic_features": ["private-reviewed"],
    "immune_fitness_notes": ["private-reviewed"]
  }
}
```

Public-safe companion:

- [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md)

The companion describes allowed public field groups and publication boundaries.
It is not a fillable public case schema.

### Evidence Packet

Private path:

```text
../curing-blood-cancer-lab/cases/<case_id>/evidence/evidence-packet.json
```

Public dependencies:

- [Source Registry v0](../../sources/source-registry-v0.md)
- [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md)
- [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md)
- [Post-CAR T Relapse Mechanism Map v0](mechanisms/post-car-t-relapse-mechanism-map-v0.md)

Shape:

```json
{
  "case_id": "private-pseudonymous-id",
  "source_freshness": [
    {
      "source_id": "clinicaltrials_gov_api_v2",
      "checked_at": "YYYY-MM-DD",
      "version_or_timestamp": "source-defined"
    }
  ],
  "matched_public_claims": ["claim_id"],
  "matched_evidence_gaps": ["gap_id"],
  "matched_trial_queries": ["query_record_id"],
  "matched_regulatory_records": ["source_id-or-private-reference"],
  "limitations": ["case-specific limitations and missing data"]
}
```

### Candidate Option Record

Private-only path:

```text
../curing-blood-cancer-lab/cases/<case_id>/candidates/candidate-option-set.json
```

Candidate options must be framed as review questions, not instructions.

Shape:

```json
{
  "candidate_id": "private-candidate-id",
  "candidate_type": "standard-care-review|trial-review|expanded-access-review|research-only|no-go",
  "review_question": "What should qualified clinicians evaluate?",
  "evidence_basis": ["source_id", "claim_id", "query_record_id"],
  "case_feature_links": ["private-feature-id"],
  "known_constraints": ["private-reviewed"],
  "overclaiming_risk": "low|medium|high",
  "requires_clinician_review": true,
  "requires_site_or_sponsor_verification": true,
  "public_export_allowed": false
}
```

Public-safe companion:

- [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md)

The rubric scores public review readiness only. It does not rank options for a
person or authorize action.

### Review Decision Record

Private-only path:

```text
../curing-blood-cancer-lab/cases/<case_id>/review/review-decision-record.json
```

Shape:

```json
{
  "review_id": "private-review-id",
  "review_body": "tumor-board|clinician-panel|research-review|ethics-review",
  "review_date": "YYYY-MM-DD",
  "decision": "standard-care-path|trial-path|expanded-access-path|research-only|no-go|needs-more-data",
  "rationale": ["private-reviewed"],
  "required_confirmations": [
    "eligibility verified by trial site",
    "label and safety reviewed by clinician",
    "expanded-access criteria reviewed where relevant"
  ],
  "monitoring_requirements": ["private-reviewed"],
  "public_learning_candidate": false
}
```

## Candidate Pathways

The pipeline should sort outputs into pathway buckets. It should not auto-select
a treatment.

| Pathway | Meaning | Required Human Owner | Public Output |
| --- | --- | --- | --- |
| Standard-care review | Evaluate approved or guideline-recognized options in context | treating clinician | none, except generic source gaps |
| Trial review | Evaluate trials that may be relevant | treating clinician and trial site | de-identified query-pattern artifact |
| Expanded-access review | Evaluate whether an investigational product pathway is legally and clinically possible | treating physician or sponsor | generic pathway notes only |
| Research-only hypothesis | Preserve a biological hypothesis that is not ready for care | research lead | public evidence gap or task |
| No-go | Record why a path should not proceed | treating clinician or review board | de-identified safety pattern only |

## Stage Gates

No case can move forward unless the active gate passes.

| Gate | Blocks If |
| --- | --- |
| Consent gate | consent, authorization, or allowed-use scope is missing |
| PHI gate | identifiers or re-identification keys would enter public space |
| Source gate | source freshness, provenance, or URL/accession capture is missing |
| Measurement gate | MRD, relapse, response, or sample context is ambiguous |
| Lab validity gate | assay source, method, or clinical validity is not reviewable |
| CDS/regulatory gate | software would output patient-specific treatment instructions without review |
| Feasibility gate | trial status, site availability, sponsor access, or eligibility is unverified |
| Safety gate | toxicity, organ function, infection risk, logistics, or contraindications are not reviewed |
| [Publication gate](publication-gate-checklist-v0.md) | public output could identify a person, expose private case facts, or imply treatment, trial, expanded-access, monitoring, or candidate-option advice |

## Public Artifact Plumbing

Only these public artifact types should downstream from case work:

- synthetic examples that contain no real case facts
- source registry updates
- measurement glossary improvements
- mechanism map updates
- evidence gap records
- public task queues
- review packet templates
- aggregate or de-identified learning artifacts that pass privacy review
  and the [Publication-Gate Checklist v0](publication-gate-checklist-v0.md)

Never downstream:

- raw records
- exact dates tied to a person
- unique variants or combinations that could identify a person without review
- locations, provider names, record numbers, images, or free-text notes
- patient-specific candidate options
- treatment, trial, or expanded-access recommendations

## Future Commands

These commands do not exist yet. They define the intended tool surface.

```bash
make validate
python3 tools/plan_case_pipeline.py --disease-program multiple-myeloma
python3 tools/build_case_evidence_packet.py --private-case <case_id> --no-public-export
python3 tools/check_case_publication_gate.py --private-case <case_id>
python3 tools/downstream_public_learning.py --private-case <case_id> --aggregate-only
```

Expected command behavior:

- read private case manifests only from the private lab repo
- write patient-specific outputs only to private case workspaces
- write public outputs only after an explicit publication gate
- fail closed when source provenance, consent, or de-identification status is
  incomplete

## Synthetic Public Fixture

The current public fixture is:

- [Multiple Myeloma Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md)

It demonstrates the full `case_00` through `case_14` pipeline with synthetic
placeholders only. It contains no real case data, no PHI, no patient-specific
candidate option, and no treatment or trial recommendation.

## How This Leads Toward A Particular Cure

For a future real case, the pipeline should produce a clinician-review packet
that answers:

1. What is the current disease and measurement state?
2. What biological failure modes are plausible for this case?
3. What evidence-backed paths are already established enough for clinical
   review?
4. What trials or investigational paths deserve site or sponsor verification?
5. What hypotheses are research-only and should not drive care?
6. What safety constraints, monitoring requirements, and stop rules matter?
7. What outcome would count as durable remission or cure-oriented success for
   this person?

The answer must remain a review packet until qualified clinicians, applicable
review boards, trial sites, sponsors, and regulators complete their parts.

## Immediate Implementation Queue

1. Add a private-only synthetic case manifest template in the lab repo.
2. Keep any fillable `case-feature-bundle.schema.json` private, and use
   [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md)
   as the public shape boundary.
3. Use the case-matching provenance fields in
   [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md)
   for public-safe trial-query records.
4. Use [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md)
   to separate standard-care review, trial review, expanded-access review,
   research-only hypotheses, and no-go decisions without ranking patient
   options.
5. Use [Publication-Gate Checklist v0](publication-gate-checklist-v0.md)
   before any case-derived public learning is downstreamed.
6. Use the
   [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md)
   for private multidisciplinary myeloma review packets.

## Review Boundary

This blueprint is a planning and tooling artifact. It is not medical advice,
diagnostic guidance, treatment guidance, trial guidance, expanded-access
guidance for any person, or a claim that a cure has been found.
