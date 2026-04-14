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
- source IDs resolve against `sources/source-registry-v0.json`
- taxonomy class IDs resolve against public taxonomies
- evidence-claim trial query IDs resolve against query-record examples
- query records include API provenance and study URLs

It uses only the Python standard library.
