# Tools

Public scripts, packages, and prototypes live here.

Tools should favor:

- transparent inputs
- blood-cancer-specific scope
- source provenance
- reproducible transforms
- readable outputs
- conservative medical framing

## Current Tools

### Public Artifact Validator

Run:

```bash
python3 tools/validate_public_artifacts.py
```

The validator checks:

- every public JSON file parses
- evidence-claim records match `schemas/evidence-claim.schema.json`
- mechanism maps match `schemas/mechanism-map.schema.json`
- mechanism extraction records match `schemas/mechanism-extraction.schema.json`
- source IDs resolve against `sources/source-registry-v0.json`
- taxonomy class IDs resolve against public taxonomies
- mechanism IDs resolve against public mechanism maps
- evidence-claim trial query IDs resolve against query-record examples
- query records include API provenance and study URLs

It uses only the Python standard library.

### Mechanism Extraction Listing

Run:

```bash
python3 tools/list_mechanism_extractions.py
```

Or:

```bash
make list-mechanism-extractions
```

The listing tool groups post-CAR T relapse extraction signals by mechanism
bucket so contributors can see which buckets are accumulating evidence.

Optional arguments can be passed through `ARGS`:

```bash
make list-mechanism-extractions ARGS="--mechanism-id bcma-antigen-loss-or-low-density-v0"
```

### Mechanism Coverage Listing

Run:

```bash
python3 tools/list_mechanism_coverage.py
```

Or:

```bash
make list-mechanism-coverage
```

The coverage tool counts public extraction records and signals by mechanism
bucket. Its counts are artifact-coverage metrics only, not mechanism-frequency,
evidence-strength, or biological-importance rankings.

Show only buckets that need more extraction:

```bash
make list-mechanism-coverage ARGS="--under-covered"
```
