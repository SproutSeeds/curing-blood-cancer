# Curing Blood Cancer

Public artifacts for blood-cancer cure and vaccine discovery tooling.

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

The first concrete focus is multiple myeloma and related plasma-cell disorders,
with artifacts designed so the public surface can expand across blood-cancer
subtypes.

## Repository Map

- `artifacts/`: public maps, taxonomies, and explanatory outputs
- `datasets/`: redistributable data products and manifests
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
python3 tools/validate_public_artifacts.py
```

The validator checks JSON parsing, evidence-claim schema conformance, source ID
references, taxonomy ID references, and query-record links.
