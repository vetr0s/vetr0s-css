PORT ?= 1314

.PHONY: check serve

check:
	@python3 scripts/check.py

serve: check
	@echo "serving on http://localhost:$(PORT)"
	@python3 -m http.server $(PORT)
