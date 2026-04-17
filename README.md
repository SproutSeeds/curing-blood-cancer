# Curing Blood Cancer

Public artifacts for blood-cancer cure and vaccine discovery tooling.

Stewarded by [frg.earth](https://frg.earth/).

This repo exists to make complex biomedical evidence easier to inspect,
combine, question, and reuse. It is the public downstream surface for work
prepared in the private lab repo at `../curing-blood-cancer-lab`.

## Mission

Build in public toward practical tools that help people define, compare, and
pursue blood-cancer cures and vaccines from transparent sources, structured
data, and reproducible methods.

## What Belongs Here

- source-backed blood-cancer subtype and mechanism maps
- data provenance templates
- evidence-level schemas
- public-domain or redistributable derived datasets
- trial-search and literature-review protocols
- small tools that make biomedical evidence easier to inspect
- examples that help non-specialists use the artifacts safely

## What Does Not Belong Here

- patient-identifying data
- private medical records
- portal exports
- restricted datasets
- credentials
- patient-specific clinical recommendations
- unsupported claims that a cure or vaccine has been found

## Disease Scope

- leukemia
- lymphoma
- multiple myeloma and related plasma-cell disorders
- myelodysplastic syndromes
- myeloproliferative neoplasms
- adjacent marrow, immune, and hematopoietic stem-cell biology when it informs
  blood-cancer cure or vaccine work

## First Focus

The first concrete focus is [multiple myeloma and related plasma-cell
disorders](disease-programs/multiple-myeloma/README.md), with artifacts
designed so the public surface can expand across blood-cancer subtypes.

The active ORP frontier plan is
[Multiple Myeloma ORP Frontier Roadmap v0](disease-programs/multiple-myeloma/frontier-roadmap-v0.md).
The live ORP phase is now the
[Case-To-Cure Adaptive Master Plan v0](disease-programs/multiple-myeloma/case-to-cure-adaptive-master-plan-v0.md),
which keeps a durable backlog and requires every completed step to synthesize
the next safest public step.
The current active backlog item is the case-to-cure master completion audit,
unlocked by the completed
[End-To-End Synthetic Case Dry Run v0](disease-programs/multiple-myeloma/end-to-end-synthetic-case-dry-run-v0.md),
[Case-To-Public Learning Extraction Gate v0](disease-programs/multiple-myeloma/case-to-public-learning-extraction-gate-v0.md),
[Expert Validation Loop v0](disease-programs/multiple-myeloma/reviews/expert-validation-loop-v0.md),
[Multidisciplinary Review Packet Builder v0](disease-programs/multiple-myeloma/reviews/multidisciplinary-review-packet-builder-v0.md),
[Candidate Hypothesis Review Question Set v0](disease-programs/multiple-myeloma/reviews/candidate-hypothesis-review-question-set-v0.md),
[Trial Therapy Landscape Non-Advice Gate v0](disease-programs/multiple-myeloma/therapy-landscapes/trial-therapy-landscape-non-advice-gate-v0.md),
[Evidence Retrieval Packet v0](disease-programs/multiple-myeloma/evidence-retrieval-packet-v0.md),
[Molecular Immune Context Contract v0](disease-programs/multiple-myeloma/contexts/molecular-immune-context-contract-v0.md),
[Therapy Exposure Timeline Contract v0](disease-programs/multiple-myeloma/therapy-landscapes/therapy-exposure-timeline-contract-v0.md),
[Measurement Normalization Contract v0](disease-programs/multiple-myeloma/measurements/measurement-normalization-contract-v0.md),
[Case Feature Normalization Contract v0](disease-programs/multiple-myeloma/case-feature-normalization-contract-v0.md),
[Consent Privacy Security Retention Gate v0](disease-programs/multiple-myeloma/case-intake/consent-privacy-security-retention-gate-v0.md),
[Caregiver Intake Public Projection Validator v0](disease-programs/multiple-myeloma/case-intake/caregiver-intake-public-projection-validator-v0.md),
[Static Synthetic Caregiver Prototype Plan v0](disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-prototype-plan-v0.md)
and
[Private Intake Schema Contract v0](disease-programs/multiple-myeloma/case-intake/private-intake-schema-contract-v0.md).
The saved Clawdad delegation brief for that map is
[Clawdad Frontier Delegation Packet v0](protocols/clawdad-frontier-delegation-packet-v0.md).
The caregiver case intake foundation is the completed first subphase,
anchored by the
[Caregiver Case Intake Product Spec v0](disease-programs/multiple-myeloma/case-intake/caregiver-case-intake-product-spec-v0.md).

## Repository Map

- `artifacts/`: public maps, taxonomies, and explanatory outputs
- `datasets/`: redistributable data products and manifests
- `disease-programs/`: focused blood-cancer disease lanes
- `docs/`: public documentation and workflow notes
- `examples/`: small worked examples
- `governance/`: contribution, safety, and publication rules
- `protocols/`: reusable research and review workflows
- `schemas/`: structured data contracts
- `sources/`: stable public source registries
- `taxonomies/`: stable classification systems for artifacts and tools
- `tools/`: scripts and tool prototypes

## Validation

Run the public artifact validator:

```bash
make validate
```

The validator checks JSON parsing, claim-set, evidence-claim, and evidence-gap
schema conformance, artifact metadata, artifact catalogs, measurement context
audits, measurement glossaries, mechanism maps, mechanism extractions, source ID
references, taxonomy ID references, mechanism-group links,
extraction-record links, measurement-term links, claim links, public-task links,
and query-record links.

You can also call the validator directly:

```bash
python3 tools/validate_public_artifacts.py
```

List public artifact metadata records:

```bash
make list-public-artifacts
```

List structured claim sets and their measurement dependencies:

```bash
make list-claim-sets
```

List evidence gaps and their linked claims:

```bash
make list-evidence-gaps
```

List contribution-ready public tasks:

```bash
make list-public-tasks
```

## Contributing

Use [CONTRIBUTING.md](CONTRIBUTING.md) and the GitHub issue forms for evidence
gap tasks, source extraction tasks, and expert review tasks. Contributions must
preserve source IDs, disease scope, measurement context, uncertainty, and the
public safety boundary.

For multiple myeloma-specific navigation and issue selection, start with the
[Multiple Myeloma Public Translation And Contribution Guide v0](disease-programs/multiple-myeloma/public-translation-contribution-guide-v0.md).
