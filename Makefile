.PHONY: help validate list-artifacts list-claim-sets list-evidence-gaps list-mechanism-extractions

help:
	@printf '%s\n' 'Available targets:'
	@printf '  %-28s %s\n' 'validate' 'Run public artifact integrity checks'
	@printf '  %-28s %s\n' 'list-artifacts' 'List tracked public artifact files'
	@printf '  %-28s %s\n' 'list-claim-sets' 'List claim sets with measurement links'
	@printf '  %-28s %s\n' 'list-evidence-gaps' 'List evidence gaps by claim, priority, or type'
	@printf '  %-28s %s\n' 'list-mechanism-extractions' 'List mechanism extraction signals by bucket'

validate:
	python3 tools/validate_public_artifacts.py

list-artifacts:
	@git ls-files '*.md' '*.json' '*.py' | sort

list-claim-sets:
	python3 tools/list_claim_sets.py $(ARGS)

list-evidence-gaps:
	python3 tools/list_evidence_gaps.py $(ARGS)

list-mechanism-extractions:
	python3 tools/list_mechanism_extractions.py $(ARGS)
