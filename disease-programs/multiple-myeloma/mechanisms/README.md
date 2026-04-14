# Multiple Myeloma Mechanisms

Mechanism artifacts for the multiple myeloma program belong here.

Initial focus:

- relapse after deep response
- antigen escape
- immune exhaustion or impaired T-cell fitness
- measurable residual disease persistence
- immune reconstitution and infection-risk constraints

## Maps

| Map | Status | Boundary |
| --- | --- | --- |
| [Post-CAR T Relapse Mechanism Map v0](post-car-t-relapse-mechanism-map-v0.md) | source-checked v0 | research artifact, not medical advice |
| [Post-CAR T Relapse Mechanism Coverage Report v0](post-car-t-relapse-mechanism-coverage-v0.md) | source-checked v0 | coverage counts, not mechanism rankings |

## Extraction Workflow

- [Post-CAR T Relapse Extraction Guide v0](post-car-t-relapse-extraction-guide-v0.md)
- [Extraction Template v0](post-car-t-relapse-extraction-template-v0.json)
- [Example Extraction: Ledergor 2024](extractions/ledergor-2024-cd4-car-t-exhaustion-v0.json)

List extraction signals by mechanism bucket:

```bash
make list-mechanism-extractions
```

List extraction coverage by mechanism bucket:

```bash
make list-mechanism-coverage
```
