# Myeloma Machine Representation Stack v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-machine-representation-stack-v0`
- stack status: public research architecture draft
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no raw records, no uploads,
  no model weights, no patient-specific predictions
- last reviewed: `2026-04-18`

## Purpose

This artifact defines a concrete machine-representation stack for multiple
myeloma that starts with molecular and clinical inputs and ends with
research-grade outputs for progression-risk modeling, response modeling, MRD
endpoint modeling, and resistance-hypothesis generation.

It is a public architecture note. It is not an autonomous treatment system, a
diagnostic tool, a prognosis tool, a trial matcher, or a claim that multiple
myeloma has been cured.

## Bottom Line

Multiple myeloma should be represented as a multimodal, longitudinal disease
state, not as one static tumor label.

The public machine stack should preserve:

- tumor genomic events
- bulk tumor transcriptome state and subtype probabilities
- bone marrow immune and microenvironment state
- structured clinical context
- treatment exposure history
- MRD, response, relapse, and progression outcome definitions
- source, method, timepoint, missingness, uncertainty, and review status

The sharpest public wedge is a myeloma state engine that can eventually support
research estimates of near-term disease trajectory under a specified treatment
context and explain which source-backed biological features contribute to that
estimate. The output should be a calibrated risk-and-response profile with
uncertainty, not a prescription.

## Source-Backed Architecture Anchors

| Source ID | Public Architecture Use | Boundary |
| --- | --- | --- |
| `nature_genetics_commpass_subtypes_2024` | Supports treating CoMMpass-style WGS, WES, RNA-seq, and longitudinal clinical follow-up as a core baseline-and-progression representation substrate for newly diagnosed multiple myeloma. | Cohort-level source only; not a patient-specific model. |
| `nature_cancer_immune_atlas_myeloma_2026` | Supports representing the marrow ecosystem as cell-state composition, immune programs, and communication summaries rather than a single immune score. | Immune signatures are cohort-level research features; not patient immune advice. |
| `nature_genetics_mm_precursor_genomic_landscape_2025` | Supports representing genomic progression and precursor-to-active disease as a graded event space rather than one binary state. | Not a personal risk calculator, screening guide, or monitoring plan. |
| `nature_communications_rrmm_resistance_2022` | Supports a relapse/resistance branch that is conditioned on treatment exposure and relapsed/refractory biology. | Not a patient-specific resistance call or therapy-ranking system. |
| `fda_mrd_cr_endpoint_guidance_2026` | Supports explicit MRD and complete-response endpoint fields for trial and translational modeling context. | Draft, nonbinding regulatory context; not for implementation or patient interpretation. |
| `jco_ims_imwg_high_risk_consensus_2025` | Supports explicit high-risk genomic staging fields instead of implicit later inference. | Consensus context only; not individual prognosis or treatment selection. |
| `pubmed_high_risk_genomic_consensus_validation_2026` | Supports validating high-risk genomic fields as source-defined cohort features and checking performance beyond existing staging features. | Cohort-level validation source; not a clinical decision system. |
| `nci_pdq_myeloma_hp` | Supports keeping diagnosis, disease state, organ context, and treatment-context terms anchored to public clinical summaries. | Not a formal guideline or patient-specific recommendation. |

## Machine State Object

Every machine-readable myeloma state should be an object with these families:

| Family | Required Shape | Missingness Rule |
| --- | --- | --- |
| `source_context` | source IDs, source type, access date, method, specimen, timepoint bucket, review state | Missing source context blocks interpretation. |
| `tumor_genomic_events` | SNVs, indels, copy-number changes, structural variants, translocations, clonality buckets, mutational-process summaries | Missing assay or threshold remains `unknown`, `not_tested`, or `not_collected`; never infer absence. |
| `transcriptome_state` | expression-subtype probabilities, pathway scores, cell-cycle or stress programs, latent embedding reference | Missing RNA must be handled as a missing modality, not as normal expression. |
| `marrow_ecosystem_state` | cell-type abundances, immune-state embeddings, senescence/exhaustion/inflammatory programs, ligand-receptor or regulatory-network summaries | Missing single-cell data must not block the whole state object. |
| `clinical_context` | age bucket, performance/frailty bucket if source-defined, renal/calcium/hemoglobin/bone context, beta-2 microglobulin and albumin context, transplant eligibility state if source-defined | Public version uses buckets and source-defined states only; no real values or identifiers. |
| `treatment_timeline` | therapy class exposure, line or timing bucket, best prior response category, refractory context, toxicity or constraint category | Must not produce sequencing, eligibility, access, or treatment guidance. |
| `measurement_timeline` | response, MRD, relapse, lab, imaging, method, threshold, sample, timepoint, durability, endpoint role | Must follow the measurement normalization contract and MRD guardrails. |
| `uncertainty_and_review` | missing modality flags, assay limits, cohort shift warnings, calibration state, expert-review status | Uncertainty must travel with every downstream output. |

## Layer 1. Raw Ingest

The raw ingest layer should accept tumor-normal DNA sequencing, bulk tumor
RNA-seq, optional single-cell bone marrow profiling, and structured clinical
data.

Public architecture decision:

- treat CoMMpass-style WGS, WES, RNA-seq, and longitudinal clinical follow-up
  as the first matched multimodal training pattern
- treat single-cell marrow profiling as an optional feature block, not a
  required field for every case
- represent diagnostic and disease-state context as source-defined clinical
  fields, never as public diagnosis

Blocked:

- public upload of reports or raw sequencing files
- public processing of real molecular data
- diagnosis or disease-state determination for any person

## Layer 2. Molecular Event Extraction

The DNA representation should be an event graph, not a flat spreadsheet of VCF
rows.

First-class event objects:

- SNV and indel events
- copy-number events
- structural variants and translocations
- clonality or cancer-cell-fraction buckets when source-defined
- mutational-process summaries
- high-risk genomic staging flags when source-defined
- longitudinal clonal-evolution markers

Myeloma-specific features should include source-defined TP53 status, del(17p),
chromosome 1 abnormalities, IgH translocation groups, RAS/MAPK pathway
alterations, NF-kB pathway alterations, and other public-source-supported driver
groups. These features must stay source-scoped and non-actionable.

## Layer 3. Tumor Transcriptome And Subtype Layer

The RNA layer should encode both continuous expression state and subtype
probability.

Representation objects:

- expression-subtype probability vector
- pathway-activity scores
- proliferation, cell-cycle, stress, unfolded-protein, and immune-evasion
  program summaries when source-defined
- latent transcriptomic embedding reference
- progression-timepoint transition flag when serial sampling supports it

This layer exists because source-backed CoMMpass analyses show that copy-number
and expression subtypes carry important disease-state information. It should
not be used to infer a treatment path for a person.

## Layer 4. Bone Marrow Microenvironment Layer

The marrow layer should be represented as a cell-state composition and
communication graph.

Representation objects:

- cell-type abundance vector
- state-specific cell embeddings
- T-cell exhaustion or senescence program summaries when source-defined
- myeloid inflammatory program summaries when source-defined
- ligand-receptor or regulatory-network summaries
- immune-signature source and validation status

Single-cell data are sparse and often missing in real workflows. The system must
therefore allow this modality to be absent while preserving a visible
`single_cell_not_available` or `single_cell_not_collected` state.

## Layer 5. Clinical Context Layer

The clinical layer should encode the non-molecular context that remains
decisive in myeloma modeling.

Representation objects:

- age bucket
- performance, frailty, and transplant-eligibility state when source-defined
- renal, calcium, hemoglobin, bone, infection, and extramedullary context
- beta-2 microglobulin, albumin, LDH, and staging context when source-defined
- prior line and exposure context
- best prior response category
- timing of progression or relapse bucket
- source-defined high-risk genomic staging flags

This layer must remain descriptive and review-gated. It cannot decide prognosis,
fitness, eligibility, urgency, monitoring, or treatment.

## Layer 6. Longitudinal Disease-State Timeline

Each patient-state representation should be a time-ordered trajectory.

Timeline nodes may include:

- diagnosis
- induction
- transplant
- consolidation
- maintenance
- MRD assessment
- biochemical progression
- clinical relapse
- post-relapse therapy
- response assessment
- adverse event or constraint bucket

The temporal encoder should consume ordered disease-state snapshots with
elapsed-time buckets and treatment-exposure context. Public artifacts may only
use synthetic timeline examples or public cohort-level abstractions.

## Layer 7. Fusion Model

The fusion model should be multimodal and temporal.

Candidate architecture:

- graph or set encoder for genomic events
- dense encoder for transcriptomic embeddings
- sparse-aware encoder for single-cell state summaries
- structured encoder for clinical context
- temporal transformer, survival-aware sequence model, or competing-risk model
  over disease-state snapshots
- missing-modality masks and calibration metadata

The design requirement is not one universal base model. The requirement is a
shared patient-state backbone that can represent what is known, what is missing,
what is source-defined, and what remains uncertain.

## Layer 8. Prediction Heads

The first research heads should be narrow and auditable:

| Head | Output | Required Boundary |
| --- | --- | --- |
| progression head | calibrated near-term and medium-term progression-risk estimates under a named treatment-context bucket | Research estimate only; no prognosis advice. |
| response head | probability of response-depth category for a named regimen class or line-context bucket | No regimen recommendation or ranking. |
| MRD head | probability or classification of MRD negativity context when method, sample, threshold, timepoint, and CR context are present | Must follow MRD endpoint guardrails and FDA draft-guidance limitations. |
| resistance-attribution head | source-scoped plausible mechanism families that may explain failure patterns | Hypothesis generation only; no patient-specific resistance call. |

Every head must output uncertainty, missing-modality flags, calibration state,
source IDs, and blocked-use text.

## Layer 9. Resistance And Relapse Branch

The relapse branch should be separate from the newly diagnosed baseline model.

Rationale:

- relapsed/refractory cohorts show resistance biology that should not be
  flattened into baseline risk
- treatment exposure changes the meaning of features
- therapy-conditioned feature importance may differ after proteasome inhibitor,
  IMiD, anti-CD38, BCMA-directed, bispecific, CAR T, or other class exposure

This branch should learn therapy-conditioned relapse patterns only in
retrospective, research, and expert-reviewed contexts. It must not infer what a
person is resistant to or what therapy should come next.

## Training Strategy

The defensible training strategy is staged:

1. build unimodal encoders for genomic events, bulk RNA, single-cell marrow
   state, and structured clinical timeline data
2. train a matched multimodal backbone on patients with genomics, RNA, and
   clinical follow-up
3. fine-tune therapy-conditioned heads for progression, MRD, and response
4. add the relapse branch using relapsed/refractory cohorts
5. run shadow-mode retrospective review against synthetic and de-identified,
   governed, private-lab cases before any prospective use is considered

The model should learn a portable patient-state representation. It should not
memorize one dataset's labels, clinical practices, or site mix.

## MVP

The first public-safe MVP is not a clinical model. It is a specification and
synthetic fixture set for a newly diagnosed myeloma baseline-and-early-course
state object.

MVP inputs:

- CoMMpass-style tumor genomic events
- CoMMpass-style tumor RNA subtype and expression-program summaries
- structured clinical variables
- treatment-context bucket
- response/MRD/progression endpoint fields
- optional immune-atlas-derived signature fields

MVP outputs:

- progression-risk research head specification
- response-depth research head specification
- MRD-context research head specification
- uncertainty and missing-modality report
- no-advice refusal wrapper

MVP must not output treatment recommendations, trial recommendations, prognosis
for a person, option ranking, monitoring guidance, expanded-access guidance, or
clinical urgency.

## Validation Standard

Validation should be harder than a normal academic benchmark.

Required validation design:

- site-aware split
- calendar-time split
- newly diagnosed and relapsed/refractory evaluation kept separate
- calibration assessment, not just discrimination
- robustness under missing modalities
- comparison against existing staging, cytogenetics, and clinician-accessible
  features
- subgroup and ancestry-aware error analysis where source data permits
- explicit dataset-shift warnings

The key question is whether the representation adds source-backed signal beyond
existing staging and cytogenetic features, not whether it rediscovered them.

## Safety Boundary

This stack can support:

- trial enrichment research
- biomarker discovery
- mechanistic stratification
- structured case review inside a private, governed, consented workspace
- public schema and synthetic fixture development
- expert validation of language, source scope, and model boundaries

This stack must not:

- choose therapy
- recommend trials
- rank options
- infer eligibility or availability
- overrule standard-of-care judgment
- present speculative resistance calls as clinical truth
- expose real case data in public
- claim cure, vaccine, or validated clinical utility

## What This Step Revealed

The current case-to-cure pipeline already has many of the safety and
normalization contracts needed for a future machine state engine. The missing
public-safe layer is a model-facing state-object specification that translates
those contracts into feature families, missing-modality rules, prediction-head
boundaries, and validation requirements.

## Next Public-Safe Implementation Atoms

Recommended next atoms:

1. `myeloma-state-object-schema-v0`: executable or markdown schema for the
   model-facing state object, using synthetic-only examples.
2. `machine-representation-source-extraction-v0`: source-extraction table that
   maps each architecture claim to exact public source lines and unresolved
   expert-validation needs.
3. `synthetic-myeloma-state-fixture-v0`: synthetic fixture with missing DNA,
   missing RNA, missing single-cell, and complete multimodal scenarios.
4. `model-output-boundary-wrapper-v0`: refusal and uncertainty wrapper for
   progression, response, MRD, and resistance heads.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No uploads, backend, model weights, or raw molecular records.
- No diagnosis, prognosis, treatment advice, trial advice, monitoring advice,
  expanded-access advice, urgency guidance, option ranking, or cure claim.
- All claims are source-scoped, cohort-level, and marked open-question until
  expert validation and source extraction are complete.
