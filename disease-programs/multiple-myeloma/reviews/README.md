# Multiple Myeloma Review Packets

Review packets prepare public artifacts for qualified external review.

They are not themselves expert review, clinical guidance, treatment guidance,
trial guidance, or cure claims. Their job is to make the review work precise,
traceable, and safer to do in public.

## Current Packets

| Packet | Status | Boundary |
| --- | --- | --- |
| [Candidate Hypothesis Review Question Set v0](candidate-hypothesis-review-question-set-v0.md) | public-shape-only | question scaffold only; no candidate options, rankings, recommendations, or patient-action output |
| [Multidisciplinary Review Packet Builder v0](multidisciplinary-review-packet-builder-v0.md) | public-shape-only | route-rule skeleton only; copy, reference, omit, or refuse; no generated prose or packet assembly |
| [Expert Validation Loop v0](expert-validation-loop-v0.md) | public-shape-only | disposition loop only; no outreach, private correspondence, copied expert replies, recommendations, rankings, or publication authorization |
| [BCMA Claim Set Expert Review Packet v0](bcma-claim-set-expert-review-packet-v0.md) | expert-review-needed | source-checked is separate from expert-reviewed |
| [Multidisciplinary Review Packet Template v0](multidisciplinary-review-packet-template-v0.md) | expert-review-needed | do not fill public template with real case facts |

## Public Expert Validation Issues

| Index | Status | Boundary |
| --- | --- | --- |
| [Expert Validation Issue Index v0](expert-validation-issue-index-v0.md) | 13 public issues opened | issue creation does not complete expert review |
| [Expert Validation Loop v0](expert-validation-loop-v0.md) | public disposition loop drafted | maps issue state, review lenses, source-context needs, allowed dispositions, blocked uses, and next public actions without private correspondence |
| [Expert Validation Outreach Map v0](expert-validation-outreach-map-v0.md) | public shortlist drafted | named people are candidates, not endorsers or participants |

## Current Builder Specs

| Spec | Status | Boundary |
| --- | --- | --- |
| [Multidisciplinary Review Packet Builder v0](multidisciplinary-review-packet-builder-v0.md) | public-shape-only | front-door route rules for question IDs, artifact IDs, source IDs, review lenses, missing inputs, refusals, and boundaries |
| [Review-Packet Builder Input Manifest Spec v0](review-packet-builder-manifest-spec-v0.md) | source-checked | manifest specification only; no builder code or generated claims |
| [Review-Packet Builder Dry-Run Plan v0](review-packet-builder-dry-run-plan-v0.md) | source-checked | no-code copy, reference, omit, and refuse policy only |
| [Review-Packet Builder Implementation Gate v0](review-packet-builder-implementation-gate-v0.md) | source-checked | selects copied-reference route-table script only; no packet assembly |
| [Review-Packet Manifest Route-Table Dry-Run Tool v0](../../../tools/review_packet_manifest_route_table.py) | source-checked | copied-reference routing only; no generated biomedical prose or packet assembly |
| [Review-Packet Route-Table Output Schema v0](../../../schemas/review-packet-route-table-output-schema-v0.md) | source-checked | route-table output contract only; no packet assembly |
| [Review-Packet Builder Packet-Assembly Gate v0](review-packet-builder-packet-assembly-gate-v0.md) | source-checked | keeps packet assembly blocked; selects a no-code packet-skeleton spec only |
| [Review-Packet Builder Packet-Skeleton Spec v0](review-packet-builder-packet-skeleton-spec-v0.md) | source-checked | empty slots and route references only; no packet output |
| [Review-Packet Builder Recombination Handoff v0](review-packet-builder-recombination-handoff-v0.md) | source-checked | no ready builder task selected; next action is completion audit |
