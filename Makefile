.PHONY: help validate list-artifacts

help:
	@printf '%s\n' 'Available targets:'
	@printf '  %-16s %s\n' 'validate' 'Run public artifact integrity checks'
	@printf '  %-16s %s\n' 'list-artifacts' 'List tracked public artifact files'

validate:
	python3 tools/validate_public_artifacts.py

list-artifacts:
	@git ls-files '*.md' '*.json' '*.py' | sort
