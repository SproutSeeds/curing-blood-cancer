# MRD Geometry Falsification Matrix v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent phase plan: `mrd-resistance-geometry-phase-plan-v0`
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This matrix makes every MRD geometry node falsifiable before the system can use
it for hypothesis generation.

A node is allowed to move only if the source-backed movement stays structural:
weaken, split, merge as source-bounded context, block a claim, retain the current
state, or route back to source extraction.

## Boundary

- No patient-specific MRD interpretation.
- No diagnosis, prognosis, monitoring, treatment, target, product, sequence, or
  trial guidance.
- No mechanism or evidence ranking.
- No clinical validation claim.
- No cure claim.

## Matrix

| Geometry Bucket | Hypothesis Scope | Weaken If | Split If | Block If |
| --- | --- | --- | --- | --- |
| `mrd-trajectory-split-v0` | measurement movement under assay, specimen, threshold, timing, and cohort constraints | a new source shows trajectory labels are assay artifacts without aligned method context | different MRD methods produce distinct trajectory categories that should not share one edge | relapse risk, monitoring, treatment, or patient-specific MRD interpretation is inferred from trajectory labels |
| `residual-transcriptional-adaptation-v0` | residual malignant plasma-cell state under method, exposure, and timing constraints | state labels are not reproducible across source-defined methods or therapy exposures | adaptive state, pathway context, and therapy-exposure context require separate typed subnodes | state labels are used as treatment selectors, target selectors, prognosis tools, or monitoring rules |
| `metabolic-resistance-state-v0` | metabolic pathway context as a residual-state branch, not an intervention claim | metabolic findings are review-only or source-general and cannot be tied to residual disease context | fatty-acid oxidation, lipid uptake, adipocyte interaction, and metabolic stress require separate typed contexts | metabolic context becomes supplement guidance, biomarker use, target selection, prognosis, or treatment advice |
| `nfkb-selective-state-v0` | NF-kB pathway context as a source-bounded residual-state branch | NF-kB signal is broad pathway review context without selective residual-cell support | canonical/noncanonical pathway context or malignant/TME context requires separation | NF-kB context becomes target selection, pathway ranking, drug guidance, prognosis, or actionability |
| `genetic-nongenetic-coupling-v0` | provisional clone-state coupling edge, not causality or dominance | clone identity and transcriptional state fail to co-vary in aligned source frames | genetic clone architecture, transcriptional state, and therapy exposure require independent transition tracks | coupling becomes causal ranking, genetic-versus-nongenetic dominance, patient-specific resistance attribution, or treatment guidance |
| `tme-shelter-interactions-v0` | microenvironment support context with explicit inference-method limits | cell-interaction inference is review-level or computational-only without source support | immune, stromal, adipocyte, cytokine, and spatial contexts require separate support layers | TME context becomes microenvironment-targeting recommendation, mechanism ranking, or patient-specific biology |
| `subclone-diversity-v0` | clone-architecture diversity under genomic method and sampling constraints | subclone diversity differs by platform or sampling frame enough to block comparison | newly diagnosed, residual, relapse, and first-relapse clone architecture require separate contexts | subclone diversity becomes prognosis, relapse risk, treatment selection, or mechanism ranking |
| `single-cell-translation-gap-v0` | technology-readiness and implementation context, separate from biology | a source claims clinical readiness without platform, workflow, validation, or implementation context | cost, standardization, data complexity, ethics, workflow, and validation require separate readiness blockers | translation context becomes test-ordering guidance, platform recommendation, monitoring guidance, or treatment guidance |
| `t-cell-therapy-pressure-v0` | immune-redirection and therapy-exposure context, not product or sequence advice | immune-state association is not reproducible across product, timing, or response contexts | BCMA, non-BCMA, CAR T, bispecific, persistence, exhaustion, and niche contexts require separate support layers | therapy pressure becomes product comparison, target selection, treatment sequencing, trial fit, or prognosis |
| `unmet-high-risk-context-v0` | high-risk disease-context modifier, not personal risk or treatment fit | high-risk definitions differ enough that sources cannot be compared | genomic, functional, extramedullary, plasma-cell leukemia, early-relapse, and treatment-refractory contexts require separate modifiers | high-risk context becomes personal prognosis, eligibility, treatment selection, transplant fit, trial fit, or monitoring guidance |

## Structured Data

- JSON: [`mrd-geometry-falsification-matrix-v0.json`](mrd-geometry-falsification-matrix-v0.json)
- Metadata: [`mrd-geometry-falsification-matrix-v0.metadata.json`](mrd-geometry-falsification-matrix-v0.metadata.json)
