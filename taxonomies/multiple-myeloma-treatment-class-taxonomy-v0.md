# Multiple Myeloma Treatment-Class Taxonomy v0

- taxonomy id: `multiple-myeloma-treatment-class-taxonomy-v0`
- date: `2026-04-13`
- blood-cancer scope: multiple myeloma and related plasma-cell disease
- artifact class: `taxonomy`
- claim level: mixed; rows mark `fact`, `derived`, `hypothesis`, or
  `open-question`

## Boundary

This taxonomy is public research infrastructure. It is not medical advice, a
treatment guideline, a sequencing recommendation, or a claim that any class is
appropriate for any individual person.

Use it to organize evidence, artifacts, and public tools. For clinical
decisions, treating clinicians need patient-specific diagnosis, disease state,
risk biology, organ function, prior therapies, goals, and safety constraints.

## Source IDs

This taxonomy uses source IDs from [Source Registry v0](../sources/source-registry-v0.md).

- `nci_pdq_myeloma_hp`
- `fda_drugs_at_fda`
- `clinicaltrials_gov`
- `pubmed`

## Taxonomy Table

| Class ID | Treatment Class | Non-Exhaustive Examples | Organizing Logic | Cure-Oriented Question | Claim Label | Source IDs | Claim Limits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `myeloma_class_proteasome_inhibitor` | Proteasome inhibitors | bortezomib, carfilzomib, ixazomib | Disrupt protein degradation stress pathways in myeloma cells. | Which combinations and disease states convert deep response into durable treatment-free control? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Class membership does not imply suitability, sequence, or superiority. |
| `myeloma_class_immunomodulatory_agent` | Immunomodulatory agents | lenalidomide, pomalidomide, thalidomide | Immune and tumor-microenvironment modulation with direct anti-myeloma effects. | Which maintenance or combination strategies suppress residual disease without unacceptable toxicity? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Examples are not recommendations and require regulatory/status checks. |
| `myeloma_class_corticosteroid` | Corticosteroids | dexamethasone, prednisone | Broad anti-inflammatory and anti-myeloma effects; commonly used in combinations. | Can steroid exposure be reduced while preserving durable control in defined subgroups? | `fact` + `open-question` | `nci_pdq_myeloma_hp` | Supportive/combinational role varies by regimen and patient context. |
| `myeloma_class_alkylator_or_cytotoxic` | Alkylators and cytotoxic chemotherapy | melphalan, cyclophosphamide, doxorubicin-based regimens | Direct cytotoxic damage to dividing or vulnerable malignant cells. | Where do older cytotoxic approaches remain essential relative to targeted and immune therapies? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Toxicity, transplant context, and patient fitness matter; not a sequence recommendation. |
| `myeloma_class_anti_cd38_antibody` | Anti-CD38 monoclonal antibodies | daratumumab, isatuximab | Antibody targeting of CD38-expressing plasma cells with immune-mediated effects. | Which anti-CD38 combinations best deepen measurable residual disease negativity and durability? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Class target does not determine individual eligibility or comparative benefit. |
| `myeloma_class_other_monoclonal_antibody` | Other monoclonal antibodies | elotuzumab | Antibody approaches outside anti-CD38, such as immune-cell engagement through other targets. | Which non-CD38 antibody targets matter for relapse biology or combination design? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Non-exhaustive and target-specific; not all antibodies share mechanism or evidence. |
| `myeloma_class_bispecific_antibody` | Bispecific antibodies | teclistamab, elranatamab, talquetamab | Redirect T cells or other immune activity toward myeloma-associated targets such as BCMA or GPRC5D. | How can immune redirection produce durable control while managing relapse, antigen escape, infection risk, and T-cell fitness? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda`, `clinicaltrials_gov` | Trial and approval status must be checked by product, date, country, and disease state. |
| `myeloma_class_car_t_cell_therapy` | CAR T-cell therapy | idecabtagene vicleucel, ciltacabtagene autoleucel | Patient T cells engineered to recognize myeloma-associated targets, commonly BCMA in current products. | What determines long-term remission after CAR T: target persistence, T-cell fitness, tumor burden, antigen escape, or consolidation? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda`, `clinicaltrials_gov` | Product-specific indications, safety monitoring, access, and eligibility vary. |
| `myeloma_class_antibody_drug_conjugate` | Antibody-drug conjugates | belantamab mafodotin as a BCMA-directed example | Antibody targeting paired with a cytotoxic payload. | Can targeted payload delivery be made durable and safe enough to complement cellular or bispecific approaches? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda`, `clinicaltrials_gov` | Regulatory status can change; always verify current approval and availability. |
| `myeloma_class_nuclear_export_inhibitor` | Nuclear export inhibitors | selinexor | Target nuclear export biology to alter cancer-cell survival programs. | Which molecular contexts predict benefit from nuclear export disruption? | `fact` + `open-question` | `nci_pdq_myeloma_hp`, `fda_drugs_at_fda` | Class is not broadly interchangeable with immune or proteasome strategies. |
| `myeloma_class_special_context_targeted_agent` | Special-context targeted agents | venetoclax in biomarker-defined contexts | Target a vulnerability in selected molecular contexts rather than all myeloma. | Can subtype-specific vulnerabilities create cure-like control for molecularly defined myeloma groups? | `derived` + `open-question` | `nci_pdq_myeloma_hp`, `pubmed`, `clinicaltrials_gov` | Biomarker context and regulatory status must be checked; not a general myeloma recommendation. |
| `myeloma_class_autologous_stem_cell_transplant` | Autologous stem-cell transplant strategy | high-dose therapy followed by autologous stem-cell rescue | Intensive consolidation strategy used in selected eligible patients. | Which patients need transplant for durable control, and which can reach similar durability through modern immune combinations? | `fact` + `open-question` | `nci_pdq_myeloma_hp` | Eligibility and timing are clinical decisions, not taxonomy decisions. |
| `myeloma_class_radiation_local_control` | Radiation / local control | radiation for selected plasmacytoma or symptomatic local disease contexts | Local disease control rather than systemic myeloma eradication. | Where does local control intersect with systemic cure-oriented strategies? | `fact` + `open-question` | `nci_pdq_myeloma_hp` | Local therapy does not substitute for systemic disease assessment. |
| `myeloma_class_supportive_care_bone_renal_infection` | Supportive and complication-directed care | bone-strengthening agents, renal support, infection prevention, transfusion support | Prevent or manage organ damage and treatment complications. | Which supportive-care improvements enable patients to safely receive curative-intent or durability-focused therapy? | `derived` + `open-question` | `nci_pdq_myeloma_hp` | Supportive care is essential but is not itself a cure claim. |
| `myeloma_class_vaccine_or_immunoprevention_research` | Vaccine and immunoprevention research | trial-specific vaccine or immune-priming approaches | Research lane for training or reshaping immunity against myeloma-associated antigens or precursors. | Can vaccines prevent progression from precursor states or prevent relapse after deep response? | `hypothesis` + `open-question` | `clinicaltrials_gov`, `pubmed` | Research category only; not an established standard treatment class in this taxonomy. |

## Measurement Layer

These are not treatment classes, but they matter for cure-oriented tooling.

| Measurement ID | Measurement Layer | Why It Matters |
| --- | --- | --- |
| `myeloma_measure_mrd` | measurable residual disease | Cure-oriented claims need sensitive persistence/relapse measurements. |
| `myeloma_measure_cytogenetics_molecular` | cytogenetics and molecular risk | Subgroups may differ in depth, durability, relapse pattern, and intervention fit. |
| `myeloma_measure_organ_function` | renal, marrow, immune, bone, and infection status | Organ context shapes feasibility and safety of treatment strategies. |
| `myeloma_measure_prior_exposure` | prior therapy exposure and resistance | Relapse biology and prior class exposure constrain future options and trial fit. |

## Initial Use

Use this taxonomy to:

- tag future myeloma artifacts by treatment class
- normalize source-backed public maps
- structure trial-search outputs
- separate treatment classes from cure-oriented hypotheses
- prevent public artifacts from implying patient-specific treatment advice

## Limitations

- This is not exhaustive.
- This is not a clinical guideline.
- This does not sequence therapies.
- This does not rank efficacy or safety.
- Regulatory status can change; check FDA or local regulator sources for
  product-specific status.
- Clinical trial availability and eligibility must be confirmed directly with
  trial sites and clinicians.
