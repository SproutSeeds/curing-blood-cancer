# Case-Specific Private-Lab Blocker Register v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-case-specific-private-lab-blocker-register-v0`
- claim level: open-question
- register status: public-safe blocker map
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-15`

## Purpose

This register maps each case-specific stage in the public
[Case-To-Cure Pipeline Blueprint v0](case-to-cure-pipeline-blueprint-v0.md)
to a private-lab task or human-gated blocker.

It closes the completion-audit gap identified in
[Definition-Of-Complete Audit v0](definition-of-complete-audit-v0.md):
remaining case-specific work must be represented publicly as private-lab tasks
or human-gated blockers, not as implied public workflow.

## Use Boundary

This register is not a case record, case intake form, clinical workflow,
medical device, review packet, treatment plan, trial finder, expanded-access
pathway, monitoring plan, publication authorization, or cure claim.

It may be used only to inspect what must stay private or human-gated before
any public method, schema, task, or aggregate learning artifact is created.

## Register Rules

- Every stage entry is generic and public-safe.
- No entry may contain real case data, patient identifiers, raw records, dates
  tied to a person, free-text notes, images, locations, provider names,
  reviewer identities, private record paths, or re-identification keys.
- Public outputs are limited to synthetic examples, generic schemas, source
  updates, measurement or mechanism gaps, public tasks, templates, and
  aggregate artifacts that pass privacy and publication gates.
- Private-lab tasks remain outside this repo.
- Human-gated blockers require the appropriate role or institution outside
  this repo; the public repo cannot complete them.

## Stage Blocker Register

| Stage | Private-Only Input Class | Gate Or Human Owner | Blocker Reason | Allowed Public Output Or Successor | Forbidden Public Output |
| --- | --- | --- | --- | --- | --- |
| `case_00` Governance setup | Consent, authorization, clinician owner, allowed-use scope | Consent and role check | A real case cannot start unless consent, authorization, and role ownership are complete in the private environment. | Generic governance boundary notes only. | Consent documents, person-linked dates, clinician names, institution names, case workspace paths. |
| `case_01` Intake partition | Raw records, reports, images, labs, notes | PHI boundary check | Raw records and identifiers must remain in a case vault or private lab workspace. | Synthetic manifest shape only. | PHI, record numbers, images, raw reports, free-text notes, private URIs, safe-manifest details for a person. |
| `case_02` De-identification plan | PHI inventory and re-identification context | Privacy review | Public release is blocked unless a governed privacy review confirms that no person can be identified. | Generic de-identification checklist if fully generic. | Re-identification keys, exact dates, rare identifying combinations, location/provider details, private de-ID plans. |
| `case_03` Disease-state normalization | Diagnosis, stage, prior lines, response status | Clinician review | Disease-state records require qualified review and must not be public case facts. | Schema improvements and generic disease-state vocabulary. | Patient diagnosis timeline, staging details, prior-line history, response status for a person. |
| `case_04` Measurement normalization | MRD, response, relapse, labs, imaging context | Measurement review | Measurement fields are blocked when method, sample, threshold, timing, or response context is ambiguous or person-linked. | Measurement glossary or gap updates. | Patient MRD status, relapse interpretation, lab values, imaging findings, monitoring advice. |
| `case_05` Molecular and immune context | Genomics, pathology, flow, target assays, immune context | Lab validity review | Molecular and target-assay context requires lab validity review and privacy screening. | Public extraction tasks or generic mechanism gaps. | Raw molecular reports, unique variants, target status for a person, pathology images, actionability claims. |
| `case_06` Exposure and resistance map | Prior therapies, toxicities, refractory status | Clinician review | Therapy exposure and toxicity context are case-specific and cannot be public option-ranking inputs. | Treatment taxonomy gaps or generic exposure vocabulary. | Treatment history, toxicity constraints, refractory status for a person, therapy recommendations. |
| `case_07` Evidence retrieval | Normalized private case features and matched sources | Source freshness check | Evidence packets are blocked unless source provenance and freshness are captured without exposing case matching. | Public source records or query-record patterns. | Case-matched evidence packets, patient-specific trial lists, inferred eligibility, availability claims. |
| `case_08` Candidate hypothesis generation | Evidence packet and private feature links | Safety boundary check | Candidate options are review questions only and must remain private when linked to a person. | Public evidence gaps or research-only task ideas without case linkage. | Patient-specific candidate options, treatment/trial suggestions, expanded-access paths, generated clinical summaries. |
| `case_09` Candidate scoring | Candidate option set and private constraints | No auto-action gate | Scoring is blocked from clinical use and cannot rank patient options. | Rubric improvements and generic no-action guardrails. | Ranked options for a person, clinical priority scores, actionability labels, monitoring decisions. |
| `case_10` Feasibility and exclusion review | Ranked questions, trial/drug records, private constraints | Clinician and site or sponsor verification | Trial status, site availability, sponsor access, and eligibility require external verification. | Public evidence gaps or de-identified query-pattern artifacts. | Eligibility guidance, site availability claims, sponsor-access guidance, enrollment advice. |
| `case_11` Multidisciplinary review | Private packets and reviewer deliberation | Tumor board or equivalent | Review decisions require qualified reviewers and cannot be substituted by a public template. | Reusable review template updates. | Review decision records, reviewer identities, recommendations, expert-review claims without completed review. |
| `case_12` Action-path selection | Review decision and pathway constraints | Clinician owner signoff | Standard-care, trial, expanded-access, research-only, and no-go paths require accountable human signoff. | Generic pathway map vocabulary only. | Selected action path for a person, treatment choice, trial choice, expanded-access recommendation. |
| `case_13` Monitoring plan | Selected path, safety constraints, stop rules | Clinical safety review | Monitoring and stop-rule plans are clinical work and must stay outside the public repo. | Generic monitoring-schema ideas after a future public-safe gate. | Monitoring instructions, stop rules, dose/schedule guidance, adverse-event management for a person. |
| `case_14` Outcome capture | Follow-up data, outcome record, public-learning candidate | Privacy and publication review | Outcome learning cannot be public unless privacy and publication gates pass. | De-identified aggregate artifact only after publication gate. | Follow-up records, outcome status for a person, case-derived learning that identifies or guides a person. |

## Gate-Class Summary

| Gate Class | Public Meaning | Human Or Private Owner |
| --- | --- | --- |
| Consent and role | Work cannot start without private consent, authorization, and accountable owner. | Private lab and clinical owner. |
| PHI and privacy | Person-linked data cannot enter this repo. | Private privacy/governance review. |
| Source freshness | Public sources can be referenced, but case-matched freshness remains private. | Private lab source reviewer. |
| Measurement and lab validity | Disease, MRD, relapse, target, and assay context require review before use. | Clinician, lab reviewer, or qualified reviewer. |
| CDS/regulatory and feasibility | Any software output that could shape care requires separate clinical, legal, regulatory, site, sponsor, and institutional review. | Treating team, trial site, sponsor, institution, regulator, or other accountable body. |
| Safety and publication | Safety constraints and case-derived public learning fail closed unless private review and publication gates pass. | Treating team, safety reviewer, privacy reviewer, and publication gate owner. |

## Public-Safe Successors

Allowed successors from this register are limited to:

- synthetic fixtures with no real case facts
- generic schema summaries that do not invite case upload
- source registry updates
- measurement glossary improvements
- mechanism map updates
- evidence gap records
- public task queues
- review packet templates
- aggregate or de-identified learning artifacts that pass privacy review and
  [Publication-Gate Checklist v0](publication-gate-checklist-v0.md)

## Still Blocked

The following remain blocked in the public repo:

- real case intake
- private case manifests
- raw records, reports, images, notes, dates tied to a person, or identifiers
- fillable public case-feature schemas
- patient-specific candidate options
- treatment, trial, expanded-access, monitoring, or publication advice
- trial matching, patient matching, option ranking, or clinical prioritization
- reviewer identity disclosure
- clinical, legal, regulatory, sponsor, institutional, treating-team, or
  publication decisions
- unsupported cure claims

## Completion Impact

This register resolves the blocker-register gap found by
[Definition-Of-Complete Audit v0](definition-of-complete-audit-v0.md) for the
current v0 public loop.

The next project-owned action should be an aggregate completion handoff or
final audit check, not a new case-processing tool, packet assembler, ranking
system, patient matcher, trial finder, or publication workflow.

Step 33 follow-up: [Public Loop Completion Handoff v0](public-loop-completion-handoff-v0.md)
now records that aggregate endpoint and selects no new public task.

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
- No expert-review substitution.
- No publication authorization.
- No cure claim.

## Limitations

- This register does not complete any private-lab task.
- This register does not verify consent, de-identification, source freshness,
  clinical review, trial eligibility, sponsor access, safety, monitoring, or
  publication readiness for any person.
- This register does not inspect private lab records.
- This register does not authorize public case processing or public case data
  upload.
- This register does not provide medical advice, diagnostic guidance,
  treatment guidance, trial guidance, eligibility guidance, expanded-access
  guidance, monitoring guidance, or a cure claim.
