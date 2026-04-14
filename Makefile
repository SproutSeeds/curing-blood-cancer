.PHONY: help validate list-artifacts list-mechanism-extractions

help:
	@printf '%s\n' 'Available targets:'
	@printf '  %-28s %s\n' 'validate' 'Run public artifact integrity checks'
	@printf '  %-28s %s\n' 'list-artifacts' 'List tracked public artifact files'
	@printf '  %-28s %s\n' 'list-mechanism-extractions' 'List mechanism extraction signals by bucket'

validate:
	python3 tools/validate_public_artifacts.py

list-artifacts:
	@git ls-files '*.md' '*.json' '*.py' | sort

list-mechanism-extractions:
	python3 tools/list_mechanism_extractions.py $(ARGS)
