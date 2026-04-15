# Private To Public Workflow

The private Curing Blood Cancer lab repo is the upstream workspace. This repo
is the public downstream surface.

## Workflow

1. Create or revise work in `../curing-blood-cancer-lab`.
2. Move candidate material into `../curing-blood-cancer-lab/export-candidates/`.
3. Run the private publication gate.
4. For multiple myeloma case-derived learning, check the public-facing
   [Publication-Gate Checklist v0](../disease-programs/multiple-myeloma/publication-gate-checklist-v0.md)
   before preparing a public release candidate.
5. Rewrite the artifact so it stands alone publicly.
6. Add provenance, blood-cancer subtype scope, and uncertainty.
7. Place it in the appropriate public directory.
8. Record the export in the private `downstream/EXPORT_MANIFEST.md`.

## Public Artifact Requirements

- clear audience
- clear use case
- source list
- blood-cancer subtype scope
- known limitations
- no private data
- no patient-specific advice
- reproducible enough for another person to inspect

## Claim Labels

| Label | Meaning |
| --- | --- |
| `fact` | Directly supported by cited source material. |
| `derived` | Produced by a documented transform from public or releasable data. |
| `hypothesis` | Plausible research idea that needs testing. |
| `open-question` | Known unknown or decision point. |
| `do-not-use-clinically` | Not suitable for treatment decisions. |
