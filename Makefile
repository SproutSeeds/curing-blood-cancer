.PHONY: help validate list-artifacts list-public-artifacts list-claim-sets list-evidence-gaps list-mechanism-extractions list-mechanism-coverage list-public-tasks list-review-packets

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
