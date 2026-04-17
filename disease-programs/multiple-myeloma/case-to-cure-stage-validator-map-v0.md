# Case-To-Cure Stage Validator And Owner Map v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-case-to-cure-stage-validator-map-v0`
- frontier lane: case-to-cure pipeline plumbing
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-16`

## Purpose

This map makes the public case-to-cure dry run exact enough to inspect without
processing a real case. It maps each `case_00` through `case_14` stage to an
owner artifact, public validator or gate, blocked condition, and allowed public
successor.

This map is not a pipeline runner, case intake form, review packet, treatment
plan, trial finder, monitoring plan, publication authorization, or cure claim.

## Phase Handoff Guard

| Check | Finding | Decision |
| --- | --- | --- |
| Frontier endpoint | Lane 7 asks for a stage validator map, dry-run graph, or blocker-to-private-lab task map. | Create one no-code stage validator and owner map. |
| Existing substrate | The blueprint defines `case_00` through `case_14`; the blocker register maps each stage to private-lab or human-gated blockers; the synthetic fixture validates stage presence. | Recombine the existing substrate instead of adding a pipeline runner. |
| Validation state | `tools/validate_public_artifacts.py` already checks synthetic pipeline stage coverage and publication-gate booleans. | Treat machine validation as shape coverage only; keep clinical, privacy, source, and publication decisions human-gated. |
| Safety risk | A case-to-cure map can be misread as patient matching, option ranking, or care workflow. | Keep every row generic, fail-closed, and non-advisory. |

## Current Public Validators And Gates

| Validator Or Gate | Public Role | What It Does Not Do |
| --- | --- | --- |
| `make validate` / `validate_case_to_cure_synthetic_pipelines` | Confirms the synthetic example has `case_00` through `case_14`, uses no real patient data, contains no PHI, and keeps patient-specific outputs unpublished. | Does not validate a real case, consent, privacy, clinical interpretation, source matching, or publication readiness. |
| [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md) | Defines stage names, private/public inputs and outputs, and gate classes. | Does not authorize case processing. |
| [Case-Specific Private-Lab Blocker Register v0](case-specific-private-lab-blocker-register-v0.md) | Maps each stage to private-lab or human-gated blockers. | Does not complete private-lab tasks or human decisions. |
| [Publication-Gate Checklist v0](publication-gate-checklist-v0.md) | Blocks case-derived public learning unless public-safety, provenance, uncertainty, and clinical-use boundaries pass. | Does not authorize publication or clinical use by itself. |
| [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md) | Preserves allowed output type, privacy state, aggregation state, source context, review dispositions, uncertainty, limitations, blocked uses, and publication-gate state before case-derived learning can be public. | Does not extract, de-identify, summarize, publish, advise, rank, match, or authorize case-derived learning. |
| [End-To-End Synthetic Case Dry Run v0](end-to-end-synthetic-case-dry-run-v0.md) | Demonstrates success, omit, refusal, and blocker paths from synthetic caregiver intake through publication-gate refusal using public fixture and artifact IDs only. | Does not run a real case, assemble packets, generate case summaries, match trials, rank options, provide guidance, or authorize publication. |
| [Public Review And Release Gate v0](public-review-release-gate-v0.md) | Requires human review before release framing, announcement, or new automation. | Does not make artifacts release-ready without review. |

## Stage Validator And Owner Map

| Stage | Owner Artifact | Validator Or Gate Field | Blocked Condition | Allowed Public Successor |
| --- | --- | --- | --- | --- |
| `case_00` Governance setup | [Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md); [Case-Specific Private-Lab Blocker Register v0](case-specific-private-lab-blocker-register-v0.md) | consent and role check; synthetic stage coverage validator | Consent, authorization, allowed-use scope, or accountable private owner is missing. | Generic governance boundary notes only. |
| `case_01` Intake partition | [Synthetic Case-To-Cure Pipeline v0](../../examples/multiple-myeloma-synthetic-case-to-cure-pipeline-v0.md); blocker register | PHI boundary check; synthetic no-PHI validator | Raw records, reports, images, notes, identifiers, or re-identification keys would enter public space. | Synthetic manifest shape only. |
| `case_02` De-identification plan | blocker register; [Publication-Gate Checklist v0](publication-gate-checklist-v0.md) | privacy review; publication privacy gates | Any value, date, site, provider, rare combination, or private plan could identify a person. | Generic de-identification checklist language only. |
| `case_03` Disease-state normalization | [Case-Feature Bundle Public Summary v0](../../schemas/case-feature-bundle-public-summary-v0.md); [Case Feature Normalization Contract v0](case-feature-normalization-contract-v0.md); [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md); [Context Modifier Map v0](contexts/high-risk-organ-frailty-context-modifier-map-v0.md) | clinician review; source-scoped context boundary | Diagnosis timeline, staging details, prior-line history, response status, or context values are person-linked or clinically interpreted. | Schema improvements and generic disease-state vocabulary. |
| `case_04` Measurement normalization | [MRD And Relapse Measurement Glossary v0](measurements/mrd-and-relapse-measurement-glossary-v0.md); [MRD Endpoint Language Guardrail Addendum v0](measurements/mrd-endpoint-language-guardrail-addendum-v0.md); [Measurement Normalization Contract v0](measurements/measurement-normalization-contract-v0.md) | measurement review; endpoint-language guardrail | MRD, response, relapse, sample, threshold, timepoint, imaging, or lab context is ambiguous or person-linked. | Measurement glossary, measurement contract, or source-context gap updates only. |
| `case_05` Molecular and immune context | [Molecular Immune Context Contract v0](contexts/molecular-immune-context-contract-v0.md); [Post-CAR T Relapse Mechanism Map v0](mechanisms/post-car-t-relapse-mechanism-map-v0.md); [Post-BCMA Resistance Frontier Addendum v0](mechanisms/post-bcma-resistance-frontier-addendum-v0.md); context modifier map | lab validity review; molecular, pathology, flow, source-validity, and mechanism claim-level boundary | Assay validity, target status, genomic features, immune context, or rare combinations require private review. | Public extraction tasks, generic mechanism gaps, source-context notes, or evidence-packet skeleton fields only. |
| `case_06` Exposure and resistance map | [Treatment-Class Taxonomy v0](../../taxonomies/multiple-myeloma-treatment-class-taxonomy-v0.md); [Immune Therapy Sequencing And Access Boundary v0](therapy-landscapes/immune-therapy-sequencing-access-boundary-v0.md); [Therapy Exposure Timeline Contract v0](therapy-landscapes/therapy-exposure-timeline-contract-v0.md); [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md) | clinician review; no-sequencing and no-ranking boundary | Therapy history, toxicity constraints, refractory status, or sequencing context could become patient-specific advice. | Therapy exposure contract, taxonomy gaps, or generic exposure vocabulary only. |
| `case_07` Evidence retrieval | [Evidence Retrieval Packet v0](evidence-retrieval-packet-v0.md); [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md); [Source Registry v0](../../sources/source-registry-v0.md); [ClinicalTrials.gov Query Protocol v0](../../protocols/clinicaltrials-gov-query-protocol-v0.md); immune therapy boundary | source freshness check; query-record provenance; landscape no-advice gate; case-matching provenance fields | Source freshness, provenance, URL/accession capture, limitation fields, no-completeness warnings, status dates, jurisdiction, or case-matching boundary is missing. | Public source records, query-record patterns, evidence packet skeleton updates, landscape gate updates, or provenance-field updates only. |
| `case_08` Candidate hypothesis generation | [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md); [Candidate-Option Scoring Rubric v0](candidate-option-scoring-rubric-v0.md); [Open Research Map v0.1](open-research-map-v0-1.md); public schemas | question-only review scaffold; safety boundary check; no patient-specific option gate; no scoring or ranking gate | Candidate options are linked to a person or framed as instructions, recommendations, ranked choices, treatment guidance, trial guidance, expanded-access guidance, monitoring guidance, availability, eligibility, or patient-specific interpretation. | Candidate review-question scaffold updates, packet-builder skeleton route rules, public evidence gaps, or research-only task ideas without case linkage. |
| `case_09` Candidate scoring | candidate-option scoring rubric | no auto-action gate; no-ranking boundary | Any score ranks options for care, implies actionability, or prioritizes patient treatment/trial paths. | Rubric improvements and generic no-action guardrails only. |
| `case_10` Feasibility and exclusion review | [Trial Therapy Landscape Non-Advice Gate v0](therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md); ClinicalTrials.gov protocol; source registry; immune therapy boundary | clinician, site, sponsor, regulatory, and no-availability/no-eligibility/no-ranking gate | Trial status, site availability, sponsor access, eligibility, product availability, access route, or feasibility is unverified. | De-identified query-pattern artifacts, non-advisory landscape fields, or public evidence gaps only. |
| `case_11` Multidisciplinary review | [Multidisciplinary Review Packet Builder v0](reviews/multidisciplinary-review-packet-builder-v0.md); [Multidisciplinary Review Packet Template v0](reviews/multidisciplinary-review-packet-template-v0.md); [Candidate Hypothesis Review Question Set v0](reviews/candidate-hypothesis-review-question-set-v0.md); [Expert Response Validation Ledger v0](reviews/expert-response-validation-ledger-v0.md); [Expert Validation Loop v0](reviews/expert-validation-loop-v0.md) | route-rule skeleton; copy/reference/omit/refuse gate; public disposition-loop gate; tumor board or equivalent; expert-review-needed gate | Private packets, reviewer deliberation, reviewer identities, reviewer decisions, private correspondence, unpublished expert comments, generated packet prose, recommendations, rankings, matching, or patient-specific outputs would enter public space. | Reusable review-template updates, builder route-rule updates, expert-validation loop plumbing, public-safe disposition maps, or public-learning extraction gate records only. |
| `case_12` Action-path selection | candidate-option rubric; publication gate; public review and release gate | clinician owner signoff; external-decision gate | Standard-care, trial, expanded-access, research-only, or no-go path is selected for a person. | Generic pathway vocabulary only. |
| `case_13` Monitoring plan | MRD glossary; publication gate; public review and release gate | clinical safety review; no-monitoring-advice gate | Monitoring, stop rules, dose or schedule details, safety management, or adverse-event guidance is person-linked. | Generic monitoring-schema ideas only after a future public-safe gate. |
| `case_14` Outcome capture | [Case-To-Public Learning Extraction Gate v0](case-to-public-learning-extraction-gate-v0.md); publication gate; public review and release gate; synthetic pipeline fixture | privacy and publication review; extraction gate envelope; synthetic publication booleans | Follow-up data, outcome status, case-derived learning, single-case claims, or any feature combination could identify or guide a person. | Synthetic dry-run record, blocker note, public-source linkage, or de-identified aggregate artifact only after privacy, review, and publication gates. |

## Frontier Required Stage Coverage

| Frontier Required Stage | Covered By | Public Status |
| --- | --- | --- |
| Private intake and consent boundary | `case_00` through `case_02` | Private-lab-needed and privacy-gated. |
| Public-safe feature bundle projection | `case_03` through `case_06` | Summary and context labels only; no public case upload. |
| Source-backed disease-state context | `case_03` through `case_05` | Source-scoped vocabulary and review routing only. |
| Evidence map selection | `case_07` | Public source/query patterns only; no case-matched evidence packet. |
| Trial and therapy landscape context | `case_07` and `case_10` | No availability, eligibility, access, or treatment advice. |
| Candidate hypothesis review | `case_08` and `case_09` | Review-readiness only; no option ranking for care. |
| Multidisciplinary packet assembly | `case_11` | Template updates only; public packet assembly remains blocked. |
| Expert review and issue-linked validation | `case_11` | Expert-review-needed until public-safe dispositions exist. |
| Public learning extraction | `case_14` | Extraction-gate and publication-gate-needed before any aggregate artifact. |
| End-to-end synthetic dry run | `intake_00` through `intake_11` and `case_00` through `case_14` | Synthetic route table covers success, omit, refusal, and blocker states without real data. |
| Blocker register update | `case_00` through `case_14` | Every stage has a private-lab or human-gated blocker field. |

## No-Real-Case Dry-Run Graph

```text
synthetic stage coverage
  -> public owner artifact links
  -> gate or validator field
  -> blocker reason
  -> allowed public successor
  -> publication gate before any case-derived learning
```

The graph is intentionally one-way. It does not route from a public artifact
back to a real person, does not accept case uploads, and does not generate
review-packet content.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No raw records, images, notes, dates tied to a person, re-identification
  keys, private paths, reviewer identities, site names, sponsor contacts, or
  clinician names.
- No patient-specific diagnosis, prognosis, treatment, trial, expanded-access,
  monitoring, safety-management, publication, or candidate-option guidance.
- No target, therapy, trial, source, mechanism, context, artifact, task, or
  evidence ranking.
- No generated biomedical claims.
- No packet assembly, patient matching, trial matching, or case processing.
- No cure or vaccine claim.

## Limitations

- This is a public stage map, not a pipeline implementation.
- This does not inspect private lab records or real case data.
- This does not validate consent, de-identification, clinical interpretation,
  source matching, trial eligibility, sponsor access, safety, monitoring, or
  publication readiness for any person.
- The current machine validator checks synthetic fixture coverage and safety
  booleans only.
- It does not authorize public case processing, public case upload, generated
  packet output, recommendation behavior, ranking, patient matching, trial
  matching, or publication workflow.
- It does not make any artifact expert-reviewed or publication-ready.
- It does not provide medical advice, diagnostic guidance, prognosis guidance,
  treatment guidance, trial guidance, eligibility guidance, expanded-access
  guidance, monitoring guidance, safety-management guidance, or a cure claim.
