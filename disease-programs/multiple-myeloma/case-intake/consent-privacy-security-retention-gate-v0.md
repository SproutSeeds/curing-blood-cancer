# Consent Privacy Security Retention Gate v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-consent-privacy-security-retention-gate-v0`
- active ORP item: `consent-privacy-security-retention-gate-v0`
- gate status: public boundary spec complete
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no records, no uploads,
  no consent records, no private case workspace, no public intake
- last reviewed: `2026-04-16`

## Purpose

This gate records the public-safe boundary before any future real multiple
myeloma case intake, storage, retention, emergency handling, clinician review,
or public learning.

It exists because the public projection validator can reject unsafe exports,
but a future real case workflow would still need private consent, privacy,
security, retention, emergency, clinician-review, legal, regulatory, and
publication decisions outside this repo.

This artifact names those blockers. It does not complete them.

## Use Boundary

This gate is not:

- a consent form
- a privacy notice
- a security policy
- a retention policy
- a legal, regulatory, or institutional review
- a clinical workflow
- a clinician assignment process
- an emergency or urgent-care service
- a database, backend, case vault, upload path, account system, or access-control
  implementation
- publication approval
- medical advice, diagnostic guidance, prognosis guidance, treatment advice,
  trial advice, expanded-access advice, monitoring guidance, urgency guidance,
  candidate-option ranking, or a cure claim

Any real case path remains blocked until the private lab and accountable human
owners complete the relevant reviews. The public repo may only carry the shape
of the gate, synthetic examples, blocker language, and public-safe successor
tasks.

## Current Gate Decision

Current decision: `blocked-private-governance-needed`.

No real case intake, storage, retention schedule, emergency handling,
clinician-review workflow, or case-derived public learning is authorized by
this public artifact.

Allowed public successor: `case-feature-normalization-contract-v0`, limited to
public-safe field semantics, unknown states, provenance, timepoint, and
limitation fields. It must not normalize a real person, produce prognosis,
generate options, or rank care paths.

## Gate Verdict Envelope

Any future candidate that claims to advance real intake governance should be
representable as a gate verdict before it can influence public artifacts:

```json
{
  "gate_id": "consent_privacy_security_retention_gate_v0",
  "candidate_scope": "public-boundary|private-implementation|case-derived-learning",
  "status": "public-boundary-ok|blocked-private-needed|human-review-needed|out-of-scope",
  "public_export_allowed": false,
  "real_case_intake_allowed": false,
  "private_owner_needed": true,
  "legal_or_regulatory_review_needed": true,
  "clinician_review_needed": true,
  "privacy_review_needed": true,
  "security_review_needed": true,
  "publication_gate_needed": true,
  "blocked_public_content": []
}
```

The default status is `blocked-private-needed` unless the candidate is only a
generic public boundary artifact, synthetic fixture, schema summary, validator
rule, or public task that contains no real case content.

## Gate Matrix

| Gate ID | Gate Class | Required Before Real Case Work | Public-Safe Shape | Fail-Closed Public Block |
| --- | --- | --- | --- | --- |
| `cpsr_00_role_and_consent_authority` | Consent and role | Accountable private owner, consent authority, caregiver role boundary, allowed-use scope, and withdrawal handling. | Enum names and blocker language only. | Consent documents, signatures, person-linked dates, names, relationship details, authorizations, or private owner IDs. |
| `cpsr_01_identity_contact_phi_partition` | PHI partition | Private case vault that separates identifiers, contacts, raw records, reports, images, notes, and re-identification keys from public artifacts. | Generic partition map only. | Names, contact details, medical record numbers, accession numbers, report text, images, exact dates tied to a person, private paths, or keys. |
| `cpsr_02_minimum_necessary_intake` | Data minimization | Private field inventory that records why each real field is needed, which fields are optional, and which fields should not be collected. | Required/optional/unknown field classes only. | Public intake prompts that invite real free text, uploads, private goals, finances, travel details, clinician names, site names, or exact timelines. |
| `cpsr_03_security_access_audit` | Security and access | Private access-control model, authentication, authorization, audit logging, secret management, workspace isolation, and incident path. | Blocker checklist language only. | Credentials, account setup details, access tokens, private workspace URIs, security architecture claims, or proof that security review passed. |
| `cpsr_04_retention_deletion_withdrawal` | Retention and deletion | Private retention schedule, deletion path, withdrawal handling, backup treatment, and audit trail approved by accountable owners. | Retention-status enum names only. | Real retention dates, case-specific deletion requests, private storage details, or claims that public artifacts can manage withdrawal. |
| `cpsr_05_emergency_boundary` | Emergency and urgent-care boundary | Prominent copy that the system cannot handle emergencies or urgent symptoms, plus private routing policy reviewed outside this repo. | Boundary copy requirements only. | Triage, urgency classification, symptom interpretation, escalation instructions, or claims that the tool can respond to emergencies. |
| `cpsr_06_clinician_review_owner` | Clinician review | Named private clinical owner or qualified review process before any clinical label, interpretation, packet, or action path is used. | Review-needed flags only. | Clinician names, review decisions, diagnosis assertions for a person, treatment interpretations, option choices, or monitoring plans. |
| `cpsr_07_deidentification_reidentification` | Privacy review | Governed privacy review for de-identification, rare combinations, dates, sites, provider traces, and re-identification risk. | Generic de-identification blocker language only. | De-identified single-case facts, rare feature combinations, exact dates, sites, providers, private de-ID plans, or re-identification keys. |
| `cpsr_08_publication_gate` | Public learning | Publication-gate record for any case-derived public learning, with allowed output type, provenance, uncertainty, clinical-use boundary, and final decision. | Link to the publication-gate checklist and public release record shape. | Public learning that skips privacy, clinician, source, or publication review; any public claim based on one real case. |
| `cpsr_09_external_decision_boundary` | Legal, regulatory, sponsor, institutional, and treating-team decisions | Human decisions outside the public repo for legal, regulatory, institutional, sponsor/site, treating-team, and publication issues. | External decision classes named as blockers. | Legal clearance claims, regulatory readiness claims, sponsor/site claims, treating-team decisions, trial access claims, or publication authorization. |
| `cpsr_10_public_successor_boundary` | Next public work | A public successor may define shapes, synthetic fixtures, validators, tasks, or generic boundary language only. | Public-safe successor ID and limitations. | Any successor that accepts real case details, generates clinical outputs, links a person to evidence, ranks options, or claims gate completion. |

## Required Private Owners Before Real Intake

The public repo cannot assign or verify these owners, but any future real case
workflow would need them before work starts:

| Owner Class | Public Status | Why It Remains Blocked Here |
| --- | --- | --- |
| Consent and allowed-use owner | `private-lab-needed` | Consent records, authorization scope, and withdrawal handling are private legal and governance records. |
| Privacy and de-identification reviewer | `private-lab-needed` | Public artifacts cannot inspect or certify real PHI, rare combinations, or re-identification risk. |
| Security owner | `private-lab-needed` | Access control, audit logs, incident handling, and secret management are operational controls outside this repo. |
| Retention owner | `private-lab-needed` | Retention and deletion policies depend on private systems, consent scope, and accountable human review. |
| Emergency-boundary owner | `clinical-team-needed` | Emergency and urgent-care routing must be reviewed by accountable humans and cannot be generated by public tooling. |
| Clinician-review owner | `clinical-team-needed` | Diagnosis, response, relapse, treatment exposure, toxicity, and action-path interpretation require qualified review. |
| Legal, regulatory, institutional, sponsor, or site owner | `human-gate-needed` | Public automation cannot complete external decisions. |
| Publication gate owner | `human-publication-gate-needed` | Case-derived public learning requires a reviewed release record and cannot be approved by intake alone. |

## Allowed Public Outputs

This gate allows only:

- this public boundary spec
- synthetic examples with visibly artificial data
- generic field names, enum names, and blocker IDs
- public-safe validator rules and test cases
- public task descriptions that do not require real case data
- schema summaries that cannot be filled with a real person's details
- links to existing public safety, publication, and private-to-public workflow
  artifacts

## Forbidden Public Outputs

This gate blocks:

- real case intake, public submission, public save/resume, public uploads, or
  public account workflows
- signed consent, authorization records, identity, contact details,
  relationship details, private workspace paths, or private case IDs
- raw records, reports, images, notes, exact dates tied to a person, medical
  record numbers, accession numbers, sites, provider names, sponsor contacts,
  or re-identification keys
- free-text case details, private family goals, finances, travel details, or
  personal constraints
- clinical labels interpreted for a person
- treatment, trial, expanded-access, monitoring, urgency, safety-management, or
  candidate-option outputs
- patient matching, trial matching, option ranking, evidence ranking, or
  generated review decisions
- publication of case-derived learning without privacy, clinician, source, and
  publication gates

## Implementation Readiness Checklist

Before any future private implementation can be considered, the answer to each
question must be documented outside this public repo:

| Question | Current Public Answer | Required Non-Public Resolution |
| --- | --- | --- |
| Who is allowed to authorize intake and withdrawal? | Unknown and blocked. | Private consent and allowed-use record. |
| Where are identifiers and raw records stored? | Not in public. | Private case vault and access controls. |
| What fields are necessary for the stated private purpose? | Public field classes only. | Private data-minimization review. |
| How are access, audit logs, incidents, and secrets handled? | Not specified publicly. | Private security review and operational controls. |
| How long is data retained, and how is deletion handled? | Not specified publicly. | Private retention/deletion policy and accountable owner. |
| What happens if a caregiver describes urgent symptoms? | Public tooling cannot triage or respond. | Human-reviewed emergency-boundary copy and private routing policy. |
| Who can clinically interpret case fields? | No one in the public repo. | Qualified private clinical owner or review process. |
| What can become public? | Only synthetic, generic, source-backed, or reviewed aggregate material. | Publication-gate record and human publication decision. |

## What This Gate Revealed

The remaining blocker before real intake is not a missing public form. It is a
set of private governance and human-owner decisions that public automation
cannot complete.

The safest public next step is therefore not a backend, database, upload path,
consent flow, emergency handler, or clinician workflow. The safest public next
step is `case-feature-normalization-contract-v0`: a shape-only contract for
normalized case features that preserves unknown, not-tested, source-missing,
provenance, timepoint, and limitation fields without producing prognosis,
option ranking, or patient-specific guidance.

## Handoff State

`consent-privacy-security-retention-gate-v0` is complete as a public boundary
spec.

The following remain blocked outside this repo:

- real case intake
- consent workflow
- identity and contact handling
- private storage, access control, audit logs, incidents, secrets, retention,
  deletion, and withdrawal
- emergency handling
- clinician ownership and clinical interpretation
- legal, regulatory, institutional, sponsor, site, treating-team, and
  publication decisions
- case-derived public learning

ORP should mark this item complete and activate
`case-feature-normalization-contract-v0` next.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records.
- No uploads, forms, accounts, backend, database, or storage path.
- No consent records, authorization records, re-identification keys, private
  workspace paths, or private owner identities.
- No patient-specific diagnosis, prognosis, treatment, trial, expanded-access,
  monitoring, urgency, safety-management, publication, or candidate-option
  guidance.
- No patient matching, trial matching, option ranking, evidence ranking, or
  review decision.
- No legal, regulatory, clinical, sponsor, institutional, treating-team, or
  publication clearance.
- No cure or vaccine claim.

## Limitations

- This is a public boundary spec, not a real governance system.
- This does not complete consent, authorization, privacy, security, retention,
  deletion, withdrawal, incident, emergency, clinician-review, legal,
  regulatory, institutional, sponsor, site, treating-team, or publication
  review.
- This does not inspect private lab records or real case data.
- This does not authorize real intake, storage, case processing, publication,
  clinical interpretation, packet assembly, patient matching, trial matching,
  option ranking, or care-path selection.
- This does not prove that any future private implementation is safe, legal,
  secure, clinically appropriate, publication-ready, or regulatory-ready.
- This does not provide medical advice, diagnostic guidance, prognosis
  guidance, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, emergency
  guidance, or a cure claim.
