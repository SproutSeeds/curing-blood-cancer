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
The current active ORP phase is
`machine-representation-expert-validation-human-authorization-blocker-v0`.
Machine-representation implementation, MRD geometry falsification,
no-outreach expert-validation prep, internal source-gap extraction, frontier
sweep, and residual-disease modality-discordance source extraction are complete
for their named public-safe scopes, but actual expert validation, outreach,
response intake, private-lab work, clinical interpretation, model-governance
clearance, publication, and claim upgrades remain human-gated.
The reusable
[ORP Frontier Gap Sweep Mode v0](orp/modes/frontier-gap-sweep-mode-v0.md)
now captures how to check for drift, blind spots, and the next safest
public-source phase.
The current no-outreach public-source successor, if selected, is
`assay-specimen-quality-failure-mode-checklist-v0`, while the live blocker stays
`machine-representation-expert-validation-human-authorization-blocker-v0`.
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
- `orp/`: live ORP frontier state, queues, and reusable operating modes
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
