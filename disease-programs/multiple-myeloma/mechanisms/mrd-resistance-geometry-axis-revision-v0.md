# MRD Resistance Geometry Axis Revision v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- parent map: `mrd-resistance-geometry-pilot-v0`
- parent decision: `mrd-resistance-geometry-axis-revision-decision-v0`
- parent audit results: `mrd-resistance-geometry-intelligence-audit-results-v0`
- linked contradiction queue:
  `mrd-resistance-geometry-contradiction-mining-task-queue-v0`
- human outreach policy: none
- clinical boundary: research-use-only, not medical advice
- last reviewed: `2026-04-20`

## Purpose

This artifact implements the first axis revision for the MRD Resistance
Geometry Pilot.

The original pilot used a dynamic radial vector field. This revision keeps that
geometry flexible, but makes the moving parts explicit so the map does not
collapse assay method, residual cell state, clone architecture, therapy
exposure, and context into one overloaded node.

## Boundary

- Research-use only.
- Not medical advice.
- Not diagnostic guidance.
- Not a monitoring recommendation.
- Not a treatment recommendation.
- Not a trial recommendation.
- Not a patient-specific MRD interpretation.
- Not a mechanism ranking.
- Not clinical validation.
- Not a claim that multiple myeloma has been cured.
- No external human outreach is required or scheduled.

## Revision Result

The v0 geometry is revised into four explicit structures:

| Structure | Role | Status |
| --- | --- | --- |
| `measurement-trajectory-axis-v0` | Track source-defined MRD and response dynamics without interpreting an individual result. | source-bounded |
| `residual-biological-state-axis-v0` | Track residual malignant plasma-cell states and pathway-state observations without actionability. | source-bounded with under-covered branches |
| `clone-architecture-axis-v0` | Track clone identity, clone architecture, and subclone context without prognosis. | source-bounded |
| `clone-state-coupling-edge-axis-v0` | Link clone architecture to residual biological state while keeping clone and state separate. | provisional and source-specific |

Support layers remain visible but cannot rank or recommend:

- tumor microenvironment support layer
- therapy pressure support layer
- disease context support layer
- translation readiness support layer

## Why This Revision

The audit result passed all six audit items for research-map continuation only.
That means the structure can move forward, but only with the following
constraints:

- measurement trajectory and residual biological state stay separate
- clone-state coupling stays provisional and source-specific
- pathway-state nodes remain descriptive, not actionable
- coverage counts stay artifact-readiness metrics only
- contradiction-mining tasks remain unresolved follow-up
- clinical, patient-specific, and cure-language outputs stay blocked

## Revised Axis Rules

### Measurement Trajectory

The measurement axis can move by assay, specimen, threshold or sensitivity
context, source-defined timing, and response context.

It must not move into:

- relapse prediction
- monitoring guidance
- assay ranking
- patient-specific MRD interpretation

### Residual Biological State

The residual-state axis can branch by transcriptional state, therapy exposure,
sampling time, and source-defined resistant-state context.

Metabolic and NF-kB pathway branches remain under-covered until second-source
extraction is added.

It must not move into:

- target selection
- treatment recommendation
- supplement or metabolic intervention suggestion
- routine clinical single-cell decision support

### Clone Architecture

The clone axis can branch by clone-inference method, subclone context, and
source-defined clone labels.

Review-level subclone diversity remains separate from cohort-level clone
measurements.

It must not move into:

- individual prognosis
- causal dominance
- genetic-versus-nongenetic ranking
- patient-specific resistance attribution

### Clone-State Coupling

Clone-state coupling is an edge, not a merged axis.

It can stay in the map only as provisional and source-specific. If
contradiction mining weakens it, the edge should split into clone-inference and
transcriptional-state subedges or be downgraded.

It must not move into:

- clinical resistance calls
- target selection
- causal ranking
- actionability claims

## Movement Rules

- New source extraction may move a node from under-covered to
  covered-for-v0-navigation only as artifact coverage.
- Contradiction mining may split or weaken an edge before any claim upgrade.
- Measurement trajectory can move independently from residual biological
  state.
- Residual biological state can branch by pathway, therapy exposure, or
  source-defined cell state.
- Clone architecture can branch by clone-inference method and subclone context.
- No movement rule can create clinical guidance, patient-specific
  interpretation, mechanism ranking, or cure language.

## Remaining Open Work

- Run contradiction-mining tasks before any claim upgrade.
- Add second-source extraction for metabolic resistance state.
- Add second-source extraction for NF-kB selective state.
- Add second-source extraction for therapy pressure, high-risk context,
  subclone diversity, and single-cell translation gaps.

## Structured Data

- JSON: [`mrd-resistance-geometry-axis-revision-v0.json`](mrd-resistance-geometry-axis-revision-v0.json)
- Metadata: [`mrd-resistance-geometry-axis-revision-v0.metadata.json`](mrd-resistance-geometry-axis-revision-v0.metadata.json)
- Residual state object: [`myeloma-residual-state-object-v0`](myeloma-residual-state-object-v0.md)
