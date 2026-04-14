# BCMA Antigen Escape Evidence Gap Register v0

Stewarded by [frg.earth](https://frg.earth/).

This register turns the current BCMA antigen escape claim set into a public
work queue. It names what the current source-backed artifacts do not yet prove
and what would make the next version more useful.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a claim that multiple myeloma has been cured.

## Linked Public Artifacts

- Claim set: [`bcma-antigen-escape-claim-set-v0`](../evidence-claims/bcma-antigen-escape-claim-set-v0.md)
- Mechanism map: [`post-car-t-relapse-mechanism-map-v0`](../mechanisms/post-car-t-relapse-mechanism-map-v0.md)
- Measurement glossary: [`mrd-and-relapse-measurement-glossary-v0`](../measurements/mrd-and-relapse-measurement-glossary-v0.md)

## Highest-Value Gaps

### Mechanism Frequency

The public artifact set can identify BCMA antigen loss, low density, and target
alteration as mechanisms to track, but it does not estimate how often each
mechanism occurs across products, disease states, or treatment sequences.

Next public work: extract full-paper cohort denominators, assay methods, timing,
and product context for each source that reports post-BCMA relapse target
status.

### Assay Context

The current claim set depends on target status, soluble BCMA, antigen density,
and relapse definitions, but these terms are not enough unless each source also
preserves specimen, assay, threshold, time point, and paired-measurement
context.

Next public work: add extraction fields that make missing assay context visible
before any claim is strengthened.

### Alternate-Target Translation

The current SEMA4A-linked claim is preclinical and translational. It supports
tracking alternate-target research, not clinical efficacy.

Next public work: separate tumor antigen-density evidence from normal-tissue
reactivity, model context, trial-readiness, and clinical safety evidence.

### Multifactorial Resistance

BCMA antigen escape should not collapse the relapse map into one mechanism.
Immune-cell fitness, microenvironment, disease context, therapy sequencing, and
measurement gaps still need source-by-source extraction.

Next public work: add extraction records that populate the non-antigen-loss
buckets with the same rigor as target-status records.

### Expert Review

The current artifacts are source-checked public organization artifacts. They
need expert review before becoming educational anchors or evidence-strength
summaries.

Next public work: use the
[`bcma-claim-set-expert-review-packet-v0`](../reviews/bcma-claim-set-expert-review-packet-v0.md)
to collect qualified review notes for claim-level scope, measurement
assumptions, source quality, and public-language safety.

## Structured Data

- JSON: [`bcma-antigen-escape-evidence-gap-register-v0.json`](bcma-antigen-escape-evidence-gap-register-v0.json)
- Metadata: [`bcma-antigen-escape-evidence-gap-register-v0.metadata.json`](bcma-antigen-escape-evidence-gap-register-v0.metadata.json)

## Next Work

- Complete qualified review using the claim-review packet.
- Add full-text extraction tasks for sources already anchored in the source
  registry.
- Add a public issue template that converts each gap into a contributor task.
