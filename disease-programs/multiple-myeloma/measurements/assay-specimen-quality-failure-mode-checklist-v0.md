# Assay Specimen Quality Failure Mode Checklist v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `assay-specimen-quality-failure-mode-checklist-v0`
- active ORP item: `assay-specimen-quality-failure-mode-checklist-v0`
- checklist status: public failure-mode checklist
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: public-source-only and synthetic-only; no real case data,
  identifiers, records, uploads, images, raw assay values, exact dates,
  private correspondence, patient-specific predictions, recommendations,
  matching, ranking, lab-validity conclusions, or clinical decisions
- last reviewed: `2026-04-20`

## Purpose

This checklist makes residual-disease modality discordance usable by naming the
assay, specimen, timing, and quality failure modes that must remain visible
before any cross-modality comparison.

It turns the `assay_quality_or_timing_needed` placeholder from
[Residual Disease Modality Discordance Source Extraction v0](residual-disease-modality-discordance-source-extraction-v0.md)
into concrete fail-closed states for measurement contracts, glossary terms,
model-output refusal wrappers, validator planning, and future synthetic
fixtures.

This is not a laboratory-validity review, imaging interpretation, biopsy
interpretation, MRD interpretation, response assessment, monitoring plan,
prognosis tool, treatment selector, trial matcher, model validator,
publication authorization, or claim that a cure has been found.

## Checklist Decision

Current decision: `public-failure-mode-checklist-only`.

Allowed use:

- public source-context extraction
- measurement contract updates
- glossary term routing
- output-wrapper and validator refusal planning
- future synthetic fixture design
- no-outreach public task planning

Blocked use:

- accepting, normalizing, interpreting, publishing, or routing real case data
- reviewing a real laboratory report, imaging report, pathology report, MRD
  result, biopsy, scan, or clinical record
- comparing actual modalities for a person
- declaring assay validity, specimen adequacy, MRD status, imaging status,
  relapse, prognosis, response, treatment action, monitoring action, or trial
  relevance for a person
- ranking assays, laboratories, imaging modalities, sources, treatments,
  trials, mechanisms, routes, or candidate options
- creating model weights, scores, thresholds, probabilities, predictions, or
  recommendations

## Failure-Mode Checklist

| Row ID | Field Family | Trigger | Source IDs | Required Fail-Closed State | Blocked Inference |
| --- | --- | --- | --- | --- | --- |
| `asq_00_method_family_missing` | Method lineage | Residual-disease signal is reported without assay family, platform, analysis method, or with vague "MRD" wording only. | `pubmed_soh_2022_mrd_flow_harmonization`; `fda_mrd_cr_endpoint_guidance_2026`; local anchor: `measurement-normalization-contract-v0` | `method_family_needed` | No cross-source or cross-modality comparison, no response assessment, no prognosis, no monitoring action. |
| `asq_01_threshold_or_detection_limit_missing` | Threshold or detection limit | MRD, blood mass spectrometry, or imaging-linked residual-disease language lacks source-stated cutoff, detection-status, sensitivity, limit of detection, lower limit of quantification, or response criteria. | `pubmed_kumar_2016_imwg_mrd_response_criteria`; `pubmed_soh_2022_mrd_flow_harmonization`; `fda_mrd_cr_endpoint_guidance_2026` | `threshold_needed` | No depth language, no cure wording, no endpoint interpretation, no prognosis, no comparison. |
| `asq_02_specimen_source_or_quality_missing` | Specimen source and quality | Marrow aspirate, blood, serum, tissue, trephine, or imaging context is absent or specimen adequacy, hemodilution, acquisition quality, processing boundary, or sampling limitation is not represented. | `pubmed_soh_2022_mrd_flow_harmonization`; `pubmed_kubicki_2025_blood_ms_mrd`; `pubmed_yip_2025_spatial_transcriptomics_myeloma` | `specimen_quality_needed` | No substitution across specimen types, no response call, no patient-specific residual-disease interpretation. |
| `asq_03_timepoint_alignment_missing` | Timepoint alignment | Timing relative to therapy, response assessment, follow-up, or paired modality assessment is absent, source-defined only in incompatible buckets, or not aligned enough for comparison. | `fda_mrd_cr_endpoint_guidance_2026`; `eclinicalmedicine_2026_mrd_petct_concordance` | `timepoint_alignment_needed` | No discordance interpretation, no durability claim, no prognosis, no monitoring guidance. |
| `asq_04_paired_modality_context_missing` | Paired modality context | Blood mass spectrometry, PET-CT, spatial, microenvironment, or marrow MRD context is present without the paired modality context needed for the claimed comparison. | `pubmed_kubicki_2025_blood_ms_mrd`; `eclinicalmedicine_2026_mrd_petct_concordance`; local anchor: `residual-disease-modality-discordance-source-extraction-v0` | `paired_modality_context_needed` | No modality substitution, no global disease-state flag, no modality ranking, no treatment or monitoring action. |
| `asq_05_imaging_criteria_missing` | Imaging criteria | Imaging residual-disease language appears without imaging modality, criteria, timing, read boundary, or paired marrow-method context. | `eclinicalmedicine_2026_mrd_petct_concordance` | `imaging_context_needed` | No image interpretation, no lesion or site call, no prognosis, no monitoring guidance, no treatment adaptation. |
| `asq_06_spatial_site_sampling_missing` | Spatial site and sampling | Spatial transcriptomics, trephine, niche, microenvironment, or biopsy context appears without site, specimen method, sampling limitation, processing boundary, or cohort scope. | `pubmed_yip_2025_spatial_transcriptomics_myeloma`; `nature_cancer_immune_atlas_myeloma_2026`; `pubmed_wang_2025_bmme_drug_resistance` | `spatial_sampling_context_needed` | No biopsy interpretation, no site-specific disease state, no resistance call, no target selection, no prognosis. |
| `asq_07_host_context_mislabeled_as_residual_disease` | Host context separation | PRO, frailty, toxicity, function, quality-of-life, or missingness context is treated as tumor residual disease or used to infer residual-disease state. | `pubmed_shah_2025_mm_pro_quality`; `pubmed_palumbo_2015_imwg_frailty` | `host_context_not_residual_disease` | No tumor-state inference, no treatment-fit claim, no safety-management guidance, no eligibility guidance. |
| `asq_08_private_or_real_quality_review_needed` | Private review boundary | Request requires real report review, lab-validity judgment, image read, biopsy interpretation, clinician review, private record, or exact person-linked timing. | local anchors: `PUBLIC_SAFETY`, `model-output-boundary-wrapper-v0` | `private_lab_or_clinical_review_needed` | No public processing, no partial interpretation, no report summary, no clinical conclusion. |
| `asq_09_modality_collapse_attempt` | Modality collapse | A tool, prompt, table, or user request tries to collapse one modality result into a global disease state, response state, endpoint state, or advice output. | local anchors: `residual-disease-modality-discordance-source-extraction-v0`, `measurement-normalization-contract-v0`, `model-output-boundary-wrapper-v0`, `myeloma-state-validator-rule-map-v0` | `modality_collapse_blocked` | No global residual-disease flag, no response interpretation, no prognosis, no monitoring, no treatment guidance, no ranking. |

## Fail-Closed Rules

| Rule ID | Rule | Fail-Closed Action |
| --- | --- | --- |
| `asq_rule_00_quality_before_comparison` | Method, specimen, threshold, timing, paired-modality context, and source status must be represented before comparison. | Mark the specific missing quality state and block comparison language. |
| `asq_rule_01_missing_quality_is_not_negative` | Missing assay, specimen, timing, imaging, or spatial context cannot imply absence of disease or absence of disagreement. | Preserve missingness and require a limitation note. |
| `asq_rule_02_threshold_before_depth_language` | Response-depth or MRD-depth language requires source-stated threshold, detection limit, or criteria. | Mark `threshold_needed`; block cure, prognosis, endpoint interpretation, and comparison. |
| `asq_rule_03_paired_timing_before_discordance_language` | Discordance language requires source-defined paired modality timing or an explicit missing-timing state. | Mark `timepoint_alignment_needed` or `paired_modality_context_needed`; block patient meaning. |
| `asq_rule_04_imaging_and_spatial_context_do_not_equal_interpretation` | Imaging, biopsy, spatial, or microenvironment context may be source-scoped only. | Preserve method and sampling context; block image, biopsy, site, resistance, prognosis, and treatment interpretation. |
| `asq_rule_05_host_context_separate_from_residual_disease` | PRO, frailty, toxicity, function, and burden context cannot be converted into tumor residual-disease state. | Mark `host_context_not_residual_disease`; keep host context separate. |
| `asq_rule_06_real_review_requests_stop_public_path` | Real reports, scans, biopsies, raw values, private records, and lab-validity questions must leave the public path. | Mark `private_lab_or_clinical_review_needed`; refuse public interpretation. |

## Synthetic Fixture Pressure

Future synthetic fixtures should include at least these public-safe pressure
cases. They are not real records.

| Fixture Pressure ID | Shape | Expected Boundary |
| --- | --- | --- |
| `asq_fixture_00_mrd_negative_no_threshold` | Synthetic MRD-negative source context has method and specimen but no threshold or detection limit. | Mark `threshold_needed`; no deep response, cure, prognosis, endpoint interpretation, or comparison. |
| `asq_fixture_01_marrow_mrd_no_specimen_quality` | Synthetic marrow MRD context lacks adequacy, hemodilution, or specimen-quality state. | Mark `specimen_quality_needed`; no cross-modality comparison or response call. |
| `asq_fixture_02_petct_mrd_timepoints_misaligned` | Synthetic PET-CT and marrow MRD context are both source-scoped but assessment timing is not aligned. | Mark `timepoint_alignment_needed`; no discordance interpretation or monitoring guidance. |
| `asq_fixture_03_blood_ms_without_paired_marrow` | Synthetic blood mass spectrometry residual-disease context has no paired marrow context. | Mark `paired_modality_context_needed`; no substitution for marrow MRD and no response call. |
| `asq_fixture_04_spatial_context_without_site` | Synthetic spatial marrow context has method family but no site, specimen method, or sampling limitation. | Mark `spatial_sampling_context_needed`; no site-specific state or resistance interpretation. |
| `asq_fixture_05_quality_review_requested_for_real_report` | Prompt requests quality review of a real lab report, imaging report, biopsy report, or private record. | Mark `private_lab_or_clinical_review_needed`; refuse public processing and route to private review gates. |
| `asq_fixture_06_single_modality_global_state_attempt` | Prompt converts one residual-disease modality into a global disease-state or advice output. | Mark `modality_collapse_blocked`; refuse endpoint interpretation, prognosis, monitoring, treatment, ranking, and decisions. |

## What This Step Revealed

Residual-disease geometry needs quality gates before it needs more expressive
geometry. A visible modality-discordance state is not enough unless method
family, threshold, specimen quality, timing alignment, paired context, imaging
criteria, spatial sampling, and host-context separation are visible first.

The highest-value public successor was therefore
`measurement-state-refusal-fixture-extension-v0`, which is now complete as
[Measurement State Refusal Fixtures v0](../../../examples/measurement-state-refusal-fixtures-v0.json)
and a companion structural checker. The later
[Measurement Refusal Output Schema v0](../../../schemas/measurement-refusal-output-schema-v0.md)
is also complete, so future work can route refused records without returning
clinical meaning.
[Measurement Refusal Output Route Table v0](measurement-refusal-output-route-table-v0.md)
now completes that routing layer as refusal metadata only.
The follow-on [Measurement Refusal Validator Skeleton v0](measurement-refusal-validator-skeleton-v0.md)
is also complete as a synthetic-only structural report over those routes.
The follow-on [Measurement Refusal Negative Safety Fixtures v0](measurement-refusal-negative-safety-fixtures-v0.md)
are complete as synthetic fail-closed checks for unsafe route mutations.
The follow-on [Measurement Refusal Wrapper Integration Dry Run v0](measurement-refusal-wrapper-integration-dry-run-v0.md)
is complete as wrapper metadata only.
The follow-on [Measurement Refusal Wrapper Negative Safety Fixtures v0](measurement-refusal-wrapper-negative-safety-fixtures-v0.md)
are complete as synthetic fail-closed checks for unsafe wrapper mutations.
The follow-on [Measurement Refusal Wrapper State Machine v0](measurement-refusal-wrapper-state-machine-v0.md)
is complete as synthetic wrapper transition metadata.

## Handoff State

`assay-specimen-quality-failure-mode-checklist-v0` is complete as a public
failure-mode checklist.

ORP should keep the active blocker at
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Actual expert-validation execution, outreach, issue operations, response
intake, private-lab work, model validation, clinical interpretation, claim
upgrade, publication, and real quality review remain blocked.

The completed successor is
`measurement-refusal-wrapper-state-machine-negative-safety-fixtures-v0`. The next
no-outreach public-source successor, if selected, is
`measurement-refusal-wrapper-state-machine-falsification-audit-v0`.

## Public Safety Check

- No patient-identifying data.
- No real case data.
- No private records, reports, images, notes, exact person-linked dates, raw
  assay values, sequencing records, portal exports, accessions, private paths,
  free-text case details, private correspondence, or re-identification keys.
- No public intake form, upload path, backend, database, account workflow,
  model weights, scoring code, prediction API, executable normalizer, or
  executable validator.
- No diagnosis, prognosis, MRD interpretation, response assessment, relapse
  assessment, imaging interpretation, biopsy interpretation, lab-validity
  conclusion, treatment guidance, trial guidance, eligibility guidance,
  expanded-access guidance, monitoring guidance, urgency guidance, publication
  authorization, or clinical decision.
- No patient matching, trial matching, assay ranking, modality ranking, source
  ranking, evidence ranking, mechanism ranking, target ranking, option ranking,
  or route ranking.
- No cure or vaccine claim.

## Limitations

- This is a public failure-mode checklist, not a systematic review.
- This does not grade evidence or rank sources, assays, laboratories,
  modalities, criteria, mechanisms, treatments, trials, or options.
- This does not establish assay interchangeability, endpoint acceptance,
  prognosis, clinical utility, model validity, deployment readiness, or
  publication readiness.
- This does not perform laboratory, imaging, pathology, biopsy, MRD, response,
  relapse, prognosis, monitoring, treatment, trial, eligibility, or safety
  review for a person.
- This does not implement model code, validation code, data processing,
  normalization, scoring, training, inference, calibration, benchmarking, or
  deployment.
- This does not clear human-review, expert-review, private-lab,
  clinical-team, legal, regulatory, publication, or model-governance gates.
