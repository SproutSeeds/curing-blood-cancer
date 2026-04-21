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

### Expert Review Packet Listing

Run:

```bash
python3 tools/list_review_packets.py
```

Or:

```bash
make list-review-packets
```

The review-packet tool lists expert-review packets and their review items by
claim ID, gap ID, and review status. Review packets are readiness artifacts;
they do not make source-checked claims expert-reviewed.

Show review items for one claim:

```bash
make list-review-packets ARGS="--claim-id bcma-resistance-is-multifactorial-v0"
```

### Review-Packet Manifest Route-Table Dry Run

Run:

```bash
python3 tools/review_packet_manifest_route_table.py
```

Or:

```bash
make review-packet-route-table
```

The route-table dry run reads the public placeholder review-packet builder
manifest, checks public IDs and paths, and emits copied-reference routes,
missing-input records, and refusal records. It is not a review-packet builder,
not expert review, not generated biomedical prose, not medical advice, and not
publication-ready output.

Machine-readable output:

```bash
make review-packet-route-table ARGS="--json"
```

Focused fail-closed checks:

```bash
make review-packet-route-table ARGS="--self-test"
```

The self-test checks the valid placeholder manifest plus refusal cases for a
forbidden field, missing path, unknown source ID, and missing clinical-use
boundary. Route-table outputs validate against
[`Review-Packet Route-Table Output Schema v0`](../schemas/review-packet-route-table-output-schema-v0.md).
The tool uses only the Python standard library and reads only public repository
files.

### MRD Geometry Proof Invariant Check

Run:

```bash
python3 tools/check_mrd_geometry_proof_invariants.py
```

Or:

```bash
make check-mrd-geometry-proof
```

The invariant check reads the public MRD geometry proof plan, coverage report,
task queues, movement ledger, and public-source residual-state fixture. It
verifies that Phase 4 proof-readiness structure is present and that blocked
clinical outputs remain blocked.

Machine-readable output:

```bash
make check-mrd-geometry-proof ARGS="--json"
```

The tool checks research-structure invariants only. It does not validate
clinical utility, rank mechanisms, interpret MRD, recommend therapy, match a
patient, or claim a cure.

### MRD Geometry State Diff

Run:

```bash
python3 tools/diff_mrd_geometry_state.py
```

Or:

```bash
make diff-mrd-geometry-state
```

The state diff compares the current MRD resistance geometry coverage report
against a prior report or, by default, the same path at `HEAD`. It reports
coverage-status, source, extraction-record, and signal movement as structural
artifact changes only.

Machine-readable output:

```bash
make diff-mrd-geometry-state ARGS="--json"
```

The tool does not validate clinical utility, rank mechanisms, interpret MRD,
recommend therapy, match a patient, or claim a cure.

### MRD Geometry Falsification Check

Run:

```bash
python3 tools/check_mrd_geometry_falsification.py
```

Or:

```bash
make check-mrd-geometry-falsification
```

The falsification check reads the MRD geometry coverage report, falsification
matrix, transition model, hypothesis candidate ledger, and benchmark fixtures.
It verifies that every geometry bucket is covered for v0 navigation, every
bucket has weakening/splitting/merging/blocking tests, transition links resolve,
hypotheses remain research-only, and benchmark fixtures fail closed.

Machine-readable output:

```bash
make check-mrd-geometry-falsification ARGS="--json"
```

The tool checks structural research invariants only. It does not validate
clinical utility, rank mechanisms, interpret MRD, recommend therapy, match a
patient, or claim a cure.

### Measurement State Refusal Fixture Check

Run:

```bash
python3 tools/check_measurement_state_refusal_fixtures.py
```

Or:

```bash
make check-measurement-state-refusal-fixtures
```

The measurement-state refusal fixture check reads the assay/specimen quality
failure-mode checklist and the synthetic measurement-state refusal fixtures. It
verifies that every checklist fail-closed state has fixture coverage, all
fixture data-boundary fields remain public synthetic only, blocked outputs are
complete, and real/private quality-review requests stop the public path.

Machine-readable output:

```bash
make check-measurement-state-refusal-fixtures ARGS="--json"
```

The tool checks structural synthetic fixture invariants only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, recommend therapy, rank modalities, match a patient, or claim a cure.

### Measurement Refusal Output Schema Check

Run:

```bash
python3 tools/check_measurement_refusal_output_schema.py
```

Or:

```bash
make check-measurement-refusal-output-schema
```

The measurement-refusal output schema check reads the output schema, the
synthetic measurement-refusal output fixture, and the upstream
measurement-state refusal fixtures. It verifies that every source refusal
fixture has exactly one refused output, the full blocked downstream-use set is
carried on each output, private/real quality-review requests stop public
processing, and forbidden clinical, ranking, prediction, and recommendation
fields stay absent.

Machine-readable output:

```bash
make check-measurement-refusal-output-schema ARGS="--json"
```

The tool checks structural synthetic output invariants only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, recommend therapy, rank modalities, match a patient, or claim a cure.

### Measurement Refusal Output Route-Table Check

Run:

```bash
python3 tools/check_measurement_refusal_output_route_table.py
```

Or:

```bash
make check-measurement-refusal-output-route-table
```

The measurement-refusal output route-table check reads the synthetic refused
output fixture and the measurement-refusal route table. It verifies that every
refused output has exactly one route, the route preserves the source output and
assay/specimen quality state, the full blocked downstream-use set travels with
each route, normal synthetic refusals route only to safe refusal surfaces, and
private/real quality-review requests route only as public blocker notices.

Machine-readable output:

```bash
make check-measurement-refusal-output-route-table ARGS="--json"
```

The tool checks structural synthetic routing invariants only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, recommend therapy, rank modalities, match a patient, or claim a cure.

### Measurement Refusal Validator Skeleton

Run:

```bash
python3 tools/measurement_refusal_validator_skeleton.py
```

Or:

```bash
make check-measurement-refusal-validator-skeleton
```

The measurement-refusal validator skeleton reads the synthetic refused output
fixture and the measurement-refusal route table. It verifies public synthetic
boundaries, no-advice labels, one route per refused output, complete blocked
route manifests, required destination contracts, private-review blocker
routing, and refusal-metadata-only emitted route fields.

Machine-readable report:

```bash
make check-measurement-refusal-validator-skeleton ARGS="--json"
```

Refresh the public synthetic report fixture:

```bash
make check-measurement-refusal-validator-skeleton ARGS="--write-report"
```

The validator skeleton checks structural synthetic routing only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, recommend therapy, rank modalities, match a patient, or claim a cure.

### Measurement Refusal Negative Safety Fixtures

Run:

```bash
python3 tools/check_measurement_refusal_negative_safety_fixtures.py
```

Or:

```bash
make check-measurement-refusal-negative-safety-fixtures
```

The negative-safety checker reads
`examples/measurement-refusal-negative-safety-fixtures-v0.json`, mutates the
public synthetic measurement-refusal route table in memory, and verifies that
the validator skeleton fails closed with the expected rule IDs.

Machine-readable report:

```bash
make check-measurement-refusal-negative-safety-fixtures ARGS="--json"
```

The checker exercises synthetic bad-route states only. It does not validate
clinical utility, interpret MRD, validate assays or specimens, review reports,
recommend therapy, rank modalities, match a patient, or claim a cure.

### Measurement Refusal Wrapper Integration Dry Run

Run:

```bash
python3 tools/check_measurement_refusal_wrapper_integration_dry_run.py
```

Or:

```bash
make check-measurement-refusal-wrapper-integration-dry-run
```

The wrapper dry-run checker reads
`examples/measurement-refusal-wrapper-integration-dry-run-v0.json` and verifies
that all ten refused measurement outputs map to
`model-output-boundary-wrapper-v0` as refusal metadata only.

Regenerate the dry-run report:

```bash
make check-measurement-refusal-wrapper-integration-dry-run ARGS="--write-report"
```

Machine-readable report:

```bash
make check-measurement-refusal-wrapper-integration-dry-run ARGS="--json"
```

The checker exercises synthetic wrapper metadata only. It does not validate
clinical utility, interpret MRD, validate assays or specimens, review reports,
produce model output, recommend therapy, rank modalities, match a patient, or
claim a cure.

### Measurement Refusal Wrapper Negative Safety Fixtures

Run:

```bash
python3 tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py
```

Or:

```bash
make check-measurement-refusal-wrapper-negative-safety-fixtures
```

The wrapper negative-safety checker reads
`examples/measurement-refusal-wrapper-negative-safety-fixtures-v0.json`, mutates
the wrapper dry-run report in memory, and verifies that the wrapper dry-run
checker fails closed with the expected check IDs.

Machine-readable report:

```bash
make check-measurement-refusal-wrapper-negative-safety-fixtures ARGS="--json"
```

The checker exercises synthetic wrapper mutation states only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, produce model output, recommend therapy, rank modalities, match a
patient, or claim a cure.

### Measurement Refusal Wrapper State Machine

Run:

```bash
python3 tools/check_measurement_refusal_wrapper_state_machine.py
```

Or:

```bash
make check-measurement-refusal-wrapper-state-machine
```

The wrapper state-machine checker reads
`examples/measurement-refusal-wrapper-state-machine-v0.json`, the wrapper dry
run, and the wrapper negative-safety fixtures. It verifies eight safe states,
seven safe transitions, ten wrapper-record traces, thirteen blocked unsafe
transition rules, eight invariants, and the preserved human-gate handoff.

Machine-readable report:

```bash
make check-measurement-refusal-wrapper-state-machine ARGS="--json"
```

The checker exercises synthetic wrapper transition metadata only. It does not
validate clinical utility, interpret MRD, validate assays or specimens, review
reports, produce model output, recommend therapy, rank modalities, match a
patient, or claim a cure.
