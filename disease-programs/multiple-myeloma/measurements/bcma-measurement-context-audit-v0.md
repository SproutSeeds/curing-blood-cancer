# BCMA Measurement Context Audit v0

Stewarded by [frg.earth](https://frg.earth/).

Date: 2026-04-14

Clinical-use boundary: research-use-only. This audit is not medical advice,
diagnostic guidance, treatment guidance, trial guidance, product comparison,
or a cure/vaccine claim.

## Purpose

Flag which BCMA target-status and antigen-density records currently preserve
measurement context, and which records still need assay, specimen, threshold,
timing, paired-measurement, or relapse/progression detail before reuse.

## Required Context Fields

| Field | Why It Matters |
| --- | --- |
| Assay method | Different platforms and scoring methods can change the meaning of target status. |
| Specimen source | Bone marrow, plasmacytoma, blood, model, and normal-tissue measurements are not interchangeable. |
| Threshold, scoring method, or detection limit | Low, negative, absent, detectable, and molecules-per-cell statements need source-defined context. |
| Time point relative to therapy | Pre-treatment, relapse, progression, post-exposure, and paired samples support different interpretations. |
| Paired measurements | Paired pre/post or blood/marrow context can support a different statement than unpaired data. |
| Relapse or progression definition | Disease-state labels need the source definition before comparison. |
| Missing-context notes | Public artifacts should state what context is absent before later claims reuse a measurement. |

## Audit Summary

| Record | Assay | Specimen | Threshold | Timing | Paired | Disease State | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Firestone target-loss signal | captured | captured | partial | captured | captured | partial | Denominator context preserved; not a general rate. |
| Firestone soluble-BCMA signal | missing | partial | missing | partial | captured | missing | Candidate context only; not a standalone rule. |
| Di Meo low-BCMA signal | missing | missing | missing | partial | missing | partial | Method details remain incomplete in public extraction. |
| Di Meo SEMA4A-density signal | missing | missing | partial | partial | partial | missing | Molecules-per-cell language is present, but assay/specimen context is not. |
| BCMA target-presence claim | partial | partial | missing | partial | partial | missing | Claim requires linked extraction context before reuse. |
| Low-BCMA density claim | missing | missing | partial | partial | missing | missing | Remains an open-question research-tracking claim. |

## Current Boundary

- Do not compare target status or antigen density across sources without assay,
  specimen, threshold, and timing context.
- Do not treat a measurement term as sufficient evidence by itself.
- Do not infer patient-level actionability from missing-context flags.
- Do not recommend testing, treatment, sequencing, or trial participation.
- Do not turn low-BCMA or SEMA4A target-biology observations into clinical
  efficacy or safety claims.

## Structured Data

- JSON: [`bcma-measurement-context-audit-v0.json`](bcma-measurement-context-audit-v0.json)
- Metadata: [`bcma-measurement-context-audit-v0.metadata.json`](bcma-measurement-context-audit-v0.metadata.json)
