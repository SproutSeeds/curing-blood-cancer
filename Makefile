.PHONY: help validate list-artifacts list-public-artifacts list-claim-sets list-evidence-gaps list-mechanism-extractions list-mechanism-coverage list-public-tasks list-review-packets review-packet-route-table check-mrd-geometry-proof diff-mrd-geometry-state check-mrd-geometry-falsification check-measurement-state-refusal-fixtures check-measurement-refusal-output-schema check-measurement-refusal-output-route-table check-measurement-refusal-validator-skeleton check-measurement-refusal-negative-safety-fixtures check-measurement-refusal-wrapper-integration-dry-run check-measurement-refusal-wrapper-negative-safety-fixtures

help:
	@printf '%s\n' 'Available targets:'
	@printf '  %-28s %s\n' 'validate' 'Run public artifact integrity checks'
	@printf '  %-28s %s\n' 'list-artifacts' 'List tracked public artifact files'
	@printf '  %-28s %s\n' 'list-public-artifacts' 'List public artifact metadata records'
	@printf '  %-28s %s\n' 'list-claim-sets' 'List claim sets with measurement links'
	@printf '  %-28s %s\n' 'list-evidence-gaps' 'List evidence gaps by claim, priority, or type'
	@printf '  %-28s %s\n' 'list-mechanism-extractions' 'List mechanism extraction signals by bucket'
	@printf '  %-28s %s\n' 'list-mechanism-coverage' 'List extraction coverage by mechanism bucket'
	@printf '  %-28s %s\n' 'list-public-tasks' 'List contribution-ready public tasks'
	@printf '  %-28s %s\n' 'list-review-packets' 'List expert-review packets and review items'
	@printf '  %-28s %s\n' 'review-packet-route-table' 'Dry-run copied-reference review-packet manifest routing'
	@printf '  %-28s %s\n' 'check-mrd-geometry-proof' 'Check MRD geometry proof-readiness invariants'
	@printf '  %-28s %s\n' 'diff-mrd-geometry-state' 'Diff MRD geometry coverage state movement'
	@printf '  %-28s %s\n' 'check-mrd-geometry-falsification' 'Check MRD geometry falsification invariants'
	@printf '  %-28s %s\n' 'check-measurement-state-refusal-fixtures' 'Check measurement-state refusal fixture invariants'
	@printf '  %-28s %s\n' 'check-measurement-refusal-output-schema' 'Check measurement-refusal output schema invariants'
	@printf '  %-28s %s\n' 'check-measurement-refusal-output-route-table' 'Check measurement-refusal output route-table invariants'
	@printf '  %-28s %s\n' 'check-measurement-refusal-validator-skeleton' 'Run measurement-refusal validator skeleton'
	@printf '  %-28s %s\n' 'check-measurement-refusal-negative-safety-fixtures' 'Check measurement-refusal negative safety fixtures'
	@printf '  %-28s %s\n' 'check-measurement-refusal-wrapper-integration-dry-run' 'Check measurement-refusal wrapper integration dry run'
	@printf '  %-28s %s\n' 'check-measurement-refusal-wrapper-negative-safety-fixtures' 'Check measurement-refusal wrapper negative safety fixtures'

validate:
	python3 tools/validate_public_artifacts.py

list-artifacts:
	@git ls-files '*.md' '*.json' '*.py' | sort

list-public-artifacts:
	python3 tools/list_public_artifacts.py $(ARGS)

list-claim-sets:
	python3 tools/list_claim_sets.py $(ARGS)

list-evidence-gaps:
	python3 tools/list_evidence_gaps.py $(ARGS)

list-mechanism-extractions:
	python3 tools/list_mechanism_extractions.py $(ARGS)

list-mechanism-coverage:
	python3 tools/list_mechanism_coverage.py $(ARGS)

list-public-tasks:
	python3 tools/list_public_tasks.py $(ARGS)

list-review-packets:
	python3 tools/list_review_packets.py $(ARGS)

review-packet-route-table:
	python3 tools/review_packet_manifest_route_table.py $(ARGS)

check-mrd-geometry-proof:
	python3 tools/check_mrd_geometry_proof_invariants.py $(ARGS)

diff-mrd-geometry-state:
	python3 tools/diff_mrd_geometry_state.py $(ARGS)

check-mrd-geometry-falsification:
	python3 tools/check_mrd_geometry_falsification.py $(ARGS)

check-measurement-state-refusal-fixtures:
	python3 tools/check_measurement_state_refusal_fixtures.py $(ARGS)

check-measurement-refusal-output-schema:
	python3 tools/check_measurement_refusal_output_schema.py $(ARGS)

check-measurement-refusal-output-route-table:
	python3 tools/check_measurement_refusal_output_route_table.py $(ARGS)

check-measurement-refusal-validator-skeleton:
	python3 tools/measurement_refusal_validator_skeleton.py $(ARGS)

check-measurement-refusal-negative-safety-fixtures:
	python3 tools/check_measurement_refusal_negative_safety_fixtures.py $(ARGS)

check-measurement-refusal-wrapper-integration-dry-run:
	python3 tools/check_measurement_refusal_wrapper_integration_dry_run.py $(ARGS)

check-measurement-refusal-wrapper-negative-safety-fixtures:
	python3 tools/check_measurement_refusal_wrapper_negative_safety_fixtures.py $(ARGS)
