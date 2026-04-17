# Extract MRD And Complete-Response Endpoint Context

Stewarded by [frg.earth](https://frg.earth/).

## Boundary

Research-use only. This task is not medical advice, diagnostic guidance,
treatment guidance, trial guidance, eligibility guidance, expanded-access
guidance, monitoring guidance, screening guidance, patient matching, endpoint
ranking, product comparison, or a cure claim.

This task must not use patient-identifying data, real case data, private lab
records, private expert correspondence, unpublished sponsor material, or paid
sources.

## Why This Matters

MRD, complete response, stringent complete response, sustained MRD negativity,
deep response, relapse, and endpoint terms can be reused safely only when
method, sample, threshold, timepoint, duration, endpoint role, and source
limitations remain attached.

## Public Source Anchors

- `fda_mrd_cr_endpoint_guidance_2026`
- `pubmed_kumar_2016_imwg_mrd_response_criteria`
- `pubmed_munshi_2017_mrd_survival_meta_analysis`
- `pubmed_soh_2022_mrd_flow_harmonization`
- `mrd-and-relapse-measurement-glossary-v0`
- `mrd-endpoint-language-guardrail-addendum-v0`

## Linked Public Artifacts

- `mrd-endpoint-language-guardrail-addendum-v0`
- `mrd-and-relapse-measurement-glossary-v0`
- `bcma-measurement-context-audit-v0`
- `source-registry-v0`
- `multiple-myeloma-frontier-roadmap-v0`

## Deliverables

- Extract source-stated definitions and limitations for MRD negativity,
  complete response, stringent complete response, sustained MRD negativity,
  deep response, relapse, progression, PFS, OS, and MRD-plus-CR regulatory
  endpoint context.
- Preserve method, sample or specimen, threshold or detection limit, disease
  state, treatment context, timepoint, duration, endpoint role, denominator,
  source date, and limitation notes where the source provides them.
- Mark missing fields as `source-context-needed`, not as blanks to be filled by
  generated text.
- Propose whether a future validated endpoint-record shape is needed after
  extraction.

## Acceptance Checks

- `make validate` passes after any structured file changes.
- FDA draft guidance status is preserved as draft, nonbinding, and not for
  implementation.
- MRD and response terms remain separate from cure claims, treatment advice,
  trial advice, eligibility guidance, and patient-specific prognosis.
- No endpoint is flattened into a yes/no cure, success, ranking, or
  recommendation flag.
- No private records, real case data, or private expert correspondence are
  copied into public artifacts.

## Do Not Infer

- Do not infer cure from MRD negativity, complete response, stringent complete
  response, sustained MRD negativity, or deep response.
- Do not infer product approval, availability, eligibility, clinical benefit,
  or treatment selection from regulatory endpoint language.
- Do not compare assays, trials, therapies, targets, products, sources,
  mechanisms, artifacts, or evidence by clinical priority.
- Do not create endpoint scoring, patient matching, trial matching, or review
  packet filling from this task.
