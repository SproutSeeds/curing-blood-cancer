# BCMA Antigen Escape Claim Set v0

Stewarded by [frg.earth](https://frg.earth/).

This claim set converts public post-BCMA relapse extraction records into a
small set of source-bounded claims. Its job is to make the next artifact layer
more usable: contributors can see what the current public sources support, what
they do not support, and which measurements should be preserved before stronger
claims are attempted.

## Use Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a claim that multiple myeloma has been cured.

## Source Extractions

- [`firestone-2024-bcma-antigen-escape-v0`](../mechanisms/extractions/firestone-2024-bcma-antigen-escape-v0.json): antigen escape after BCMA-directed therapies.
- [`di-meo-2025-sema4a-low-bcma-v0`](../mechanisms/extractions/di-meo-2025-sema4a-low-bcma-v0.json): low BCMA density and SEMA4A alternate-target research.
- [`di-meo-2025-target-linked-phenotype-v0`](../mechanisms/extractions/di-meo-2025-target-linked-phenotype-v0.json): target-linked phenotype fields for identity or lineage-state review.
- [`tedder-bhutani-2025-bcma-resistance-review-v0`](../mechanisms/extractions/tedder-bhutani-2025-bcma-resistance-review-v0.json): BCMA resistance as a multifactorial review frame.
- [`tedder-bhutani-2025-disease-context-v0`](../mechanisms/extractions/tedder-bhutani-2025-disease-context-v0.json): disease burden, site, high-risk, prior-therapy, and registry-context fields.
- [`nci-pdq-2025-disease-context-v0`](../mechanisms/extractions/nci-pdq-2025-disease-context-v0.json): disease burden, site, high-risk, disease-state, and prior-therapy context fields.
- [`ledergor-2024-cd4-car-t-exhaustion-v0`](../mechanisms/extractions/ledergor-2024-cd4-car-t-exhaustion-v0.json): CAR T persistence and exhaustion context.

## Measurement Dependencies

This claim set references measurement terms from
[`mrd-and-relapse-measurement-glossary-v0`](../measurements/mrd-and-relapse-measurement-glossary-v0.md):

- `bone-marrow-target-status`
- `soluble-bcma`
- `antigen-density`
- `normal-tissue-reactivity-screen`
- `relapse-or-disease-progression`

## Claims

### Target Presence Should Be Extracted

BCMA target presence, absence, assay type, specimen context, and prior
BCMA-directed exposure should be preserved in public research extraction
records before maps interpret sequential anti-BCMA strategy context.

This supports better public evidence mapping. It does not support choosing,
ranking, or sequencing treatment.

### TNFRSF17 Loss Is A Trackable Escape Signal

`TNFRSF17` alteration or loss is a source-supported BCMA antigen escape field
to track within source-specific relapse extractions, especially when paired
pre-treatment and relapse samples are available.

This supports adding target-alteration fields to extraction templates. It does
not estimate how often this mechanism occurs across BCMA-directed products,
disease states, or treatment sequences.

### Low BCMA Density Supports Alternate-Target Research Tracking

Low-to-negative BCMA expression after BCMA CAR T relapse is a source-backed
reason to track alternate-target research signals and target-linked phenotype
fields, including SEMA4A in the cited translational and preclinical source.

This supports a public research bucket for alternate-target evidence. It does
not claim SEMA4A-directed CAR T therapy works in patients.

### BCMA Resistance Is Multifactorial

BCMA antigen escape should not be treated as the only public relapse-mechanism
hypothesis. Public maps should continue to track tumor-intrinsic, immune-cell,
microenvironment, sequencing, disease-context, and measurement factors.

This supports maintaining a multi-bucket relapse map. It does not prove any
resistance-overcoming strategy improves survival or creates cure-like
durability.

## Structured Data

- JSON: [`bcma-antigen-escape-claim-set-v0.json`](bcma-antigen-escape-claim-set-v0.json)
- Metadata: [`bcma-antigen-escape-claim-set-v0.metadata.json`](bcma-antigen-escape-claim-set-v0.metadata.json)

## Review Status

This claim set is source-checked, not expert-reviewed.

Use
[`bcma-claim-set-expert-review-packet-v0`](../reviews/bcma-claim-set-expert-review-packet-v0.md)
to collect qualified review comments before any claim is upgraded, scored for
evidence strength, or used in a public education layer.

## Next Work

- Complete qualified expert review using the review packet.
- Add claim-level strength scoring only after extraction fields are complete.
- Split alternate-target research claims into target-specific claim sets when
  enough source records exist.
