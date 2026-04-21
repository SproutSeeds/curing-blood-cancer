# Residual Disease Modality Discordance Source Extraction v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `residual-disease-modality-discordance-source-extraction-v0`
- active ORP item: `residual-disease-modality-discordance-source-extraction-v0`
- extraction status: public source-extraction table
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only and synthetic-only; no real case data,
  identifiers, records, uploads, images, raw assay values, exact dates,
  private correspondence, patient-specific predictions, recommendations,
  matching, ranking, or clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This artifact extracts public source context for residual-disease modality
discordance in multiple myeloma.

The public system already has marrow MRD, response, relapse, imaging, and
model-output guardrails. The frontier gap is that those signals must not be
collapsed into a single false residual-disease flag. Bone marrow MRD, peripheral
blood mass spectrometry, PET-CT or other imaging context, spatial trephine
biology, specimen quality, and host/PRO context can all describe different
parts of the research state.

This extraction is not a response assessment, imaging interpretation,
monitoring plan, prognosis tool, treatment selector, trial matcher, model
validator, publication authorization, or claim that a cure has been found.

## Extraction Decision

Current decision: `modality-discordance-source-extraction-only`.

Allowed use:

- public source-context extraction
- measurement contract updates
- glossary term routing
- model-output refusal and missingness rule planning
- future synthetic fixture design
- no-outreach public task planning

Blocked use:

- accepting, normalizing, interpreting, publishing, or routing real case data
- declaring MRD status, imaging status, blood assay status, spatial disease
  state, relapse, prognosis, treatment response, or monitoring action for a
  person
- treating a negative result in one modality as absence of disease in another
  modality
- substituting peripheral blood residual-disease assays for marrow MRD
- interpreting PET-CT, MRI, biopsy, or spatial transcriptomics for a person
- ranking modalities, assays, treatments, trials, mechanisms, or sources
- creating model weights, scores, thresholds, probabilities, or predictions

## Source Extraction Rows

| Row ID | Modality Or Context | Source IDs | Public Extraction | Required Missingness/Discordance State | Blocked Inference |
| --- | --- | --- | --- | --- | --- |
| `rdm_00_marrow_mrd_anchor` | Bone marrow MRD by flow or sequencing. | `pubmed_kumar_2016_imwg_mrd_response_criteria`; `pubmed_soh_2022_mrd_flow_harmonization`; `fda_mrd_cr_endpoint_guidance_2026`; local anchors: `mrd-and-relapse-measurement-glossary-v0`, `measurement-normalization-contract-v0` | Preserve method, sample, threshold, timepoint, disease-state context, endpoint role, source status, and limitation note. | `marrow_mrd_source_scoped`; missing threshold, method, sample adequacy, or timing remains `source_context_needed`. | No cure claim, no "no disease anywhere" claim, no patient MRD interpretation, no monitoring action. |
| `rdm_01_blood_mass_spectrometry_anchor` | Peripheral blood residual-disease measurement by mass spectrometry. | `pubmed_kubicki_2025_blood_ms_mrd`; local anchors: `mrd-and-relapse-measurement-glossary-v0`, `measurement-normalization-contract-v0` | Preserve assay family, serum/peripheral-blood context, paired marrow context when source-defined, timing, cohort, threshold or detection-status language, and limitation note. | `blood_ms_complementary_context`; absent paired marrow or assay threshold context remains visible. | No substitution for marrow MRD, no monitoring plan, no prognosis, no treatment adaptation, no response call. |
| `rdm_02_pet_ct_imaging_anchor` | PET-CT residual-disease context and paired marrow MRD/PET-CT categories. | `eclinicalmedicine_2026_mrd_petct_concordance`; local anchors: `mrd-and-relapse-measurement-glossary-v0`, `mrd-endpoint-language-guardrail-addendum-v0`, `measurement-normalization-contract-v0` | Preserve paired modality state, imaging modality, timing alignment, marrow MRD method/threshold, cohort, endpoint role, and discordance category when source-defined. | `mrd_petct_discordance_visible`; all four paired categories remain distinct when source-defined. | No image interpretation, no prognosis for a person, no monitoring advice, no treatment adaptation, no lesion/site call. |
| `rdm_03_spatial_trephine_anchor` | Spatial transcriptomics and marrow trephine architecture. | `pubmed_yip_2025_spatial_transcriptomics_myeloma`; `nature_cancer_immune_atlas_myeloma_2026`; local anchor: `machine-representation-stack-v0` | Preserve biopsy/specimen context, spatial method, cell/niche context, cohort scope, site/sampling limitation, and method boundary. | `spatial_context_research_only`; missing spatial data is not absence of focal or extramedullary disease. | No biopsy interpretation, no diagnostic site call, no imaging advice, no treatment selection, no prognosis. |
| `rdm_04_microenvironment_niche_anchor` | Bone marrow microenvironment and niche-mediated residual/resistance context. | `nature_cancer_immune_atlas_myeloma_2026`; `pubmed_wang_2025_bmme_drug_resistance`; local anchors: `mrd-resistance-geometry-transition-model-v0`, `myeloma-residual-state-object-v0` | Preserve microenvironment, immune, stromal, niche, and resistance context as cohort/source-level biology only. | `microenvironment_context_source_scoped`; missing microenvironment data cannot imply immune normality or low resistance risk. | No mechanism ranking, no target selection, no treatment guidance, no resistance call for a person. |
| `rdm_05_assay_quality_timing_anchor` | Method, threshold, sample adequacy, hemodilution/specimen quality, and assessment timing. | `pubmed_soh_2022_mrd_flow_harmonization`; `fda_mrd_cr_endpoint_guidance_2026`; `eclinicalmedicine_2026_mrd_petct_concordance`; local anchor: `measurement-normalization-contract-v0` | Preserve method lineage, threshold status, sample context, timing alignment, duration/follow-up, and not-reported states before comparison. | `assay_quality_or_timing_needed` when quality, threshold, or timepoint alignment is missing. | No cross-modality comparison, no response call, no monitoring action, no clinical decision. |
| `rdm_06_host_burden_context_anchor` | Patient-reported outcome, toxicity-burden, function, and missingness context as adjacent non-tumor state. | `pubmed_shah_2025_mm_pro_quality`; `pubmed_palumbo_2015_imwg_frailty`; local anchors: `case-feature-normalization-contract-v0`, `therapy-exposure-timeline-contract-v0` | Preserve PRO/frailty/toxicity-burden context as host-state and missingness context separate from residual-disease measurement. | `host_context_not_residual_disease`; absence of PRO or frailty context remains visible. | No fitness-for-treatment, no safety management, no dose guidance, no eligibility guidance, no patient-specific burden assessment. |
| `rdm_07_output_refusal_anchor` | Model-output and validator behavior when modalities disagree or are missing. | local anchors: `model-output-boundary-wrapper-v0`, `myeloma-state-validator-rule-map-v0`, `residual-disease-modality-discordance-source-extraction-v0` | Preserve discordance as a visible uncertainty and refusal reason. The system may say the modality context is discordant or incomplete, but not what it means for a person. | `modality_discordance_visible`; `modality_collapse_blocked`; `private_lab_needed` for real data. | No score, no probability, no MRD interpretation, no response probability, no progression risk, no treatment or monitoring recommendation. |

## Discordance Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `rdm_rule_00_no_single_modality_global_state` | A negative or positive residual-disease signal in one modality cannot become a global disease-state claim. | Preserve modality family and mark cross-modality state `not_established`. |
| `rdm_rule_01_paired_modalities_stay_paired` | Paired marrow MRD and PET-CT categories must remain paired and source-defined when a source reports them. | Keep all reported paired states distinct; do not collapse into one binary flag. |
| `rdm_rule_02_blood_ms_is_complementary_context` | Peripheral blood mass spectrometry may be represented as complementary source context only. | Block substitution for marrow MRD and require assay, threshold/detection-status, timing, and limitation notes. |
| `rdm_rule_03_spatial_missingness_not_absence` | Missing spatial or site-state context cannot imply absence of focal, spatially restricted, or extramedullary disease. | Preserve `spatial_context_missing` and block interpretation. |
| `rdm_rule_04_assay_quality_before_comparison` | Cross-modality comparison requires method, threshold, sample/specimen, timing, and source status. | Mark `assay_quality_or_timing_needed`; block comparison language. |
| `rdm_rule_05_output_wrapper_refuses_meaning` | A future output wrapper can expose discordance/missingness state but cannot explain what it means for a person. | Return refusal labels for prognosis, endpoint interpretation, monitoring, treatment, ranking, and decisions. |

## Synthetic Fixture Pressure

Future synthetic fixtures should include at least these public-safe cases:

| Fixture Pressure ID | Shape | Expected Boundary |
| --- | --- | --- |
| `rdm_fixture_00_marrow_negative_pet_positive` | Synthetic source context where marrow MRD is negative and PET-CT is positive in a source-defined paired category. | Preserve discordance; no prognosis, monitoring, imaging interpretation, or treatment action. |
| `rdm_fixture_01_marrow_positive_pet_negative` | Synthetic source context where marrow MRD is positive and PET-CT is negative. | Preserve discordance; no modality ranking or clinical inference. |
| `rdm_fixture_02_blood_ms_negative_marrow_missing` | Blood mass-spectrometry negativity with marrow context missing. | Mark complementary context only; block substitution and response call. |
| `rdm_fixture_03_spatial_context_missing` | Synthetic state has marrow MRD and immune context but no spatial/site-state data. | Missing spatial context remains visible and cannot imply absence of focal disease. |
| `rdm_fixture_04_assay_quality_missing` | MRD status reported without threshold, sample quality, or timing alignment. | Mark source-context-needed; block cross-modality comparison. |

## What This Step Revealed

The public machine-representation stack should treat residual-disease modality
discordance as a first-class state, not as noise. The safest immediate change is
not a model. It is a stronger measurement and output boundary:

- source IDs for blood mass spectrometry, marrow MRD/PET-CT discordance, spatial
  trephine architecture, microenvironment niche context, and PRO missingness
- glossary terms that separate modality families
- measurement-normalization rules that block single-modality global claims
- wrapper/validator rules that refuse prediction or advice when modalities
  disagree or are missing

The no-outreach successor
[Assay Specimen Quality Failure Mode Checklist v0](assay-specimen-quality-failure-mode-checklist-v0.md)
is now complete. It makes modality discordance more useful by turning missing
method, specimen, threshold, timing, sample quality, paired modality, imaging,
spatial, host-context, private-review, and modality-collapse conditions into
explicit fail-closed states.

## Handoff State

`residual-disease-modality-discordance-source-extraction-v0` is complete as a
public source-extraction table.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, and publication remain blocked.

The next no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-negative-safety-fixtures-v0`, after the
assay/specimen quality checklist, measurement-state refusal fixture extension,
measurement-refusal output schema, measurement-refusal output route table,
measurement-refusal validator skeleton, and measurement-refusal negative safety
fixtures, and measurement-refusal wrapper integration dry run.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  molecular values, sequencing records, portal exports, accessions, private
  paths, free-text case details, private correspondence, or re-identification
  keys.
- No public intake form, upload path, backend, database, account workflow,
  model weights, scoring code, prediction API, executable normalizer, or
  executable validator.
- No diagnosis, prognosis, MRD interpretation, response assessment, relapse
  assessment, imaging interpretation, biopsy interpretation, treatment guidance,
  trial guidance, eligibility guidance, expanded-access guidance, monitoring
  guidance, urgency guidance, publication authorization, or clinical decision.
- No patient matching, trial matching, modality ranking, source ranking,
  evidence ranking, mechanism ranking, target ranking, option ranking, or route
  ranking.
- No cure or vaccine claim.

## Limitations

- This is source extraction, not a systematic review.
- This does not grade evidence or rank modalities.
- This does not establish assay interchangeability, endpoint acceptance,
  prognosis, clinical utility, model validity, or deployment readiness.
- This does not implement model code, validation code, data processing,
  normalization, scoring, training, inference, calibration, benchmarking, or
  deployment.
- This does not clear human-review, expert-review, private-lab,
  clinical-team, legal, regulatory, publication, or model-governance gates.
