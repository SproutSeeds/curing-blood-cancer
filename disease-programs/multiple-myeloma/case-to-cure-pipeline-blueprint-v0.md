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

The adaptive execution plan for continuing this work is
[Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md).
That plan keeps the large cure-oriented scope visible while requiring each
completed step to inspect its result, write a handoff, and synthesize the next
safe public step.
The current adaptive-loop handoff is
[Case-To-Cure Loop Governor Handoff v0](case-to-cure-loop-governor-handoff-v0.md),
which closes the loop-governor item and activates the private intake schema
contract as the next public-safe dependency.

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

The public caregiver-facing intake product target is
[Caregiver Case Intake Product Spec v0](case-intake/caregiver-case-intake-product-spec-v0.md).
It defines the plain-language flow, field groups, privacy boundary, and
private handoff contract for future real intake work. It does not collect real
case data, authorize public uploads, or provide medical advice.

The public projection gate for that intake phase is
[Caregiver Intake Public Projection Checklist v0](case-intake/caregiver-intake-public-projection-checklist-v0.md).
It defines fail-closed verdicts, no-PHI checks, no-advice checks, unknown-state
requirements, final-review requirements, and the boundary between private
intake content and public shape-only or synthetic artifacts.

The public completion handoff for the current intake phase is
[Case Intake Frontier Completion Audit Handoff v0](case-intake/case-intake-frontier-completion-audit-handoff-v0.md).
It closes the current autonomous public slice without authorizing real intake,
uploads, advice, clinical interpretation, publication, or private-lab work.

The public shape contract for a future private intake record is
[Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md).
It defines field groups, unknown states, provenance, private-only content, and
projection outcomes without creating a live schema, backend, public upload
path, or case record.

The public static prototype plan is
[Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md).
It maps the synthetic `intake_00` through `intake_11` screens, refusal paths,
copy families, and fixture bindings without creating a public form, live
backend, upload path, public submission, or patient-specific output.

The public static frontend prototype is
[Static Synthetic Caregiver Intake Frontend v0](case-intake/static-synthetic-caregiver-intake-frontend-v0.html).
It turns the synthetic screen plan into a no-build HTML/CSS/JS prototype with
section navigation, unknown/not-sure paths, final-review cues, emergency and
clinician-review boundaries, disabled private handoff controls, and no form
submission, upload, backend, auth, database, email, storage, advice, matching,
ranking, or patient-specific output.

The public projection validator spec is
[Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md).
It defines fail-closed protocol checks for PHI, real case details, free text,
uploads, advice language, unknown-state inference, review-gate claims,
allowed-successor mismatches, and publication bypass without processing real
case data.

The consent, privacy, security, retention, emergency, and clinician-review
gate is
[Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md).
It records the human and technical blockers before any real case intake,
storage, retention, emergency handling, clinician review, or case-derived
public learning.

The public shape contract for normalized case features is
[Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md).
It defines feature groups, value states, source status, timepoint buckets,
review gates, limitations, and allowed public successors without creating a
fillable real-case schema, normalizer, or patient-specific interpretation.

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
- [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)

These companions describe allowed public field groups, normalization states,
and publication boundaries. They are not fillable public case schemas.

The public shape contract for measurement normalization is
[Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md).
It preserves MRD, response, relapse, lab, imaging, method, threshold, sample,
timepoint, durability, endpoint role, source context, uncertainty, and
limitation fields without publishing real values or producing monitoring,
prognosis, treatment, trial, ranking, or cure-claim output.

The public shape contract for therapy exposure timelines is
[Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md).
It preserves therapy class, exposure state, broad timing bucket, response
linkage, toxicity or constraint category, refractory context, source status,
review status, uncertainty, and limitations without publishing real therapy
histories or producing sequencing, eligibility, access, monitoring, ranking,
or treatment guidance.

The public shape contract for molecular and immune context is
[Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md).
It preserves cytogenetic, genomic, target-assay, pathology, flow, immune
context, assay-validity, source-validity, timepoint, therapy-linkage,
measurement-linkage, uncertainty, review, and limitation fields without
publishing real reports or producing actionability, testing, treatment, trial,
monitoring, ranking, or patient-specific interpretation.

The public architecture note for translating these contracts into a
model-facing disease-state object is
[Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md).
It defines feature families, missing-modality rules, fusion-layer boundaries,
prediction-head boundaries, and validation standards without creating a model,
processing real data, or producing patient-specific predictions.

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
- [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md)
- [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md)
- [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
- [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
- [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md)
- [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
- [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)

Public-safe companion:

[Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md) defines the
public-source-only packet skeleton for source IDs, query records, source
freshness, access-date state, limitations, uncertainty, no-completeness
warnings, review status, and no-advice boundaries. It does not perform patient
matching, trial matching, target actionability, evidence ranking, or
patient-specific interpretation.

[Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md)
defines the public landscape gate for trial, therapy, product, target,
jurisdiction, status, source freshness, access-date, limitation, uncertainty,
and review fields. It does not perform availability checks, eligibility
checks, trial matching, patient matching, sequencing, access guidance, ranking,
or patient-specific interpretation.

[Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md)
defines the public question-only scaffold for candidate hypothesis review. It
preserves evidence packet IDs, landscape gate status, source context,
uncertainty, review lens, blocked uses, and no patient-action output without
creating candidate options, recommendations, rankings, patient matching, trial
matching, availability, eligibility, treatment guidance, trial guidance,
expanded-access guidance, monitoring guidance, or patient-specific
interpretation.

[Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md)
defines the public route-rule skeleton for review packet planning. It routes
question IDs, artifact IDs, source IDs, review lenses, missing-input blockers,
refusals, and boundary fields by copy, reference, omit, or refuse behavior
only. It does not assemble packets, generate biomedical prose, process real
case facts, create patient-specific outputs, recommend, rank, match trials,
infer eligibility or availability, authorize publication, or make clinical
decisions.

[Expert Validation Loop v0](reviews/expert-validation-loop-v0.md) defines the
public disposition-loop scaffold for issue-linked validation work. It preserves
issue IDs, artifact IDs, source IDs, review lenses, outreach-map role labels,
response-ledger states, allowed dispositions, uncertainty, blocked uses, and
next public actions without outreach, private correspondence, unpublished
expert comments, recommendations, rankings, publication authorization, or
clinical decisions.

[Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md)
defines the public sanitation and publication gate for future case-derived
learning. It preserves allowed output type, privacy decision state,
de-identification basis, aggregation state, single-case claim blockers, public
source context, review lens, disposition state, uncertainty, limitations,
blocked uses, and publication-gate state before any private-case learning can
be prepared for public review. It does not extract, de-identify, summarize,
publish, advise, rank, match, or authorize case-derived learning.

[End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md)
defines the synthetic route table from caregiver intake through
publication-gate refusal. It exercises success, omit, refusal, and blocker
paths without running a real case, assembling review packets, generating case
summaries, matching trials, ranking options, giving clinical guidance, or
authorizing publication.

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

The current public stage validator and owner map is:

- [Case-To-Cure Stage Validator And Owner Map v0](case-to-cure-stage-validator-map-v0.md)

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

The active queue is governed by
[Case-To-Cure Adaptive Master Plan v0](case-to-cure-adaptive-master-plan-v0.md)
and the ORP additional list `case-to-cure-master-backlog-v0`.

The first public-safe queue items are:

1. Complete the loop governor so a completed subphase always produces a
   next-step synthesis before the run stops. Completed by
   [Case-To-Cure Loop Governor Handoff v0](case-to-cure-loop-governor-handoff-v0.md).
2. Define the private intake schema contract and public projection boundary for
   the caregiver intake flow. Completed by
   [Private Intake Schema Contract v0](case-intake/private-intake-schema-contract-v0.md).
3. Design a static synthetic caregiver prototype before any live data capture.
   Completed by
   [Static Synthetic Caregiver Prototype Plan v0](case-intake/static-synthetic-caregiver-prototype-plan-v0.md).
4. Create a public projection validator or validator spec that fails closed on
   PHI, advice, rankings, urgency guidance, and publication without a gate.
   Completed by
   [Caregiver Intake Public Projection Validator v0](case-intake/caregiver-intake-public-projection-validator-v0.md).
5. Define consent, privacy, security, retention, emergency, and
   clinician-review gates before any real case intake. Completed by
   [Consent Privacy Security Retention Gate v0](case-intake/consent-privacy-security-retention-gate-v0.md).
6. Keep any fillable `case-feature-bundle.schema.json` private, and use
   [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md)
   and
   [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md)
   as the public shape and normalization boundary. Completed by
   [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md).
7. Define the measurement normalization contract for MRD, response, relapse,
   labs, imaging, method, threshold, sample, timepoint, durability, endpoint
   role, source context, uncertainty, and limitation fields before these terms
   are used downstream. Completed by
   [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md).
8. Define the therapy exposure timeline contract before prior therapies, lines,
   exposure, response linkage, toxicities, constraints, or refractory context
   are used downstream. Completed by
   [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md).
9. Define the molecular immune context contract before cytogenetics, genomics,
   target assays, pathology, flow, immune context, assay validity, source
   validity, or target language are used downstream. Completed by
   [Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md).
10. Define the model-facing machine representation stack before progression,
   response, MRD, or resistance modeling heads are specified downstream.
   Started by [Myeloma Machine Representation Stack v0](machine-representation-stack-v0.md)
   and bounded by
   [Myeloma State Object Schema v0](../../schemas/myeloma-state-object-schema-v0.md);
   fixture coverage is now represented by
   [Synthetic Myeloma State Fixture v0](../../examples/synthetic-myeloma-state-fixture-v0.json).
   output-boundary refusal is now represented by
   [Model Output Boundary Wrapper v0](model-output-boundary-wrapper-v0.md).
   validator-rule coverage is now represented by
   [Myeloma State Validator Rule Map v0](myeloma-state-validator-rule-map-v0.md).
   source-extraction coverage is now represented by
   [Machine Representation Source Extraction v0](machine-representation-source-extraction-v0.md).
   source-gap task routing is now represented by
   [Machine Representation Source-Gap Task Queue v0](public-tasks/machine-representation-source-gap-task-queue-v0.md).
   issue-draft text is now represented by
   [Machine Representation Source-Gap Issue Draft Packet v0](public-tasks/issue-drafts/machine-representation-source-gap-issue-draft-packet-v0.md).
   phase audit is now represented by
   [Machine Representation Implementation Completion Audit v0](machine-representation-implementation-completion-audit-v0.md).
   The next state is a human-gated blocker, not model output.
11. Define the evidence retrieval packet skeleton before public-source queries,
   source freshness, query records, public evidence IDs, or limitation ledgers
   are used downstream. Completed by
   [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md).
12. Define the trial/therapy landscape non-advice gate before trial, therapy,
   product, target, jurisdiction, status, freshness, or access-context fields
   are reused downstream. Completed by
   [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md).
13. Define the candidate hypothesis review question set before candidate
   hypotheses are framed for review packets or public task routing. Completed
   by
   [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md).
14. Define the multidisciplinary review packet builder skeleton before
   question IDs, artifact IDs, source IDs, reviewer lenses, missing-input
   blockers, refusals, or no-generated-claims behavior are reused downstream.
   Completed by
   [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md).
15. Define the expert validation loop before issue statuses, outreach maps,
   response ledgers, or safe dispositions are treated as recurring review
   infrastructure. Completed by
   [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md).
16. Define the case-to-public learning extraction gate before any future
   private-case learning can be sanitized, aggregated, source-scoped, reviewed,
   or publication-gated for public use. Completed by
   [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md).
17. Advance the end-to-end synthetic case dry run before any future real-case
   exercise of the public pipeline. Completed by
   [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md).
18. Run the case-to-cure master completion audit before any new autonomous
   case-to-cure item is selected. Completed by
   [Case-To-Cure Master Completion Audit v0](case-to-cure-master-completion-audit-v0.md),
   which blocks the next state on expert, private-lab, clinical, legal,
   regulatory, publication, or human-review gates unless a human selects a new
   named public-safe phase.
19. Build the human-selected public static caregiver intake frontend only as a
   synthetic prototype. Completed by
   [Static Synthetic Caregiver Intake Frontend v0](case-intake/static-synthetic-caregiver-intake-frontend-v0.html);
   the next public-safe item is a smoke-test report for no-submit,
   no-storage, no-upload, no-backend, responsive layout, refusal-copy,
   emergency-boundary, clinician-review, and no-advice behavior.
19. Use the case-matching provenance fields in
   [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md)
   for public-safe trial-query records.
20. Use [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md)
   to separate standard-care review, trial review, expanded-access review,
   research-only hypotheses, and no-go decisions without ranking patient
   options.
21. Use [Publication-Gate Checklist v0](publication-gate-checklist-v0.md)
   before any case-derived public learning is downstreamed.
22. Use the
   [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md)
   for private multidisciplinary myeloma review packets.

## Review Boundary

This blueprint is a planning and tooling artifact. It is not medical advice,
diagnostic guidance, treatment guidance, trial guidance, expanded-access
guidance for any person, or a claim that a cure has been found.
