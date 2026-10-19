# Docs & agent tooling. Add your project's build/test targets below the marker.
PY ?= python3

.PHONY: help feature adr lesson docs-check sync-agents check-agents check

help:            ## list targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-14s %s\n", $$1, $$2}'

feature:         ## scaffold a feature: make feature name=user-auth
	@$(PY) scripts/new_feature.py "$(name)"

adr:             ## new ADR: make adr title="Use Postgres"
	@$(PY) scripts/new_adr.py "$(title)"

docs-check:      ## lint docs structure, status consistency, links
	@$(PY) scripts/docs_check.py

sync-agents:     ## regenerate .claude/ from .agents/
	@$(PY) scripts/sync_agents.py

check-agents:    ## fail if .claude/ drifted from .agents/
	@$(PY) scripts/sync_agents.py --check

check: docs-check check-agents  ## everything CI runs

# ---- project targets (FILL) ----
