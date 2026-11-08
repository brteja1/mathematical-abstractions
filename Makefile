VENV ?= .venv
PYTHON ?= $(if $(wildcard $(VENV)/bin/python),$(VENV)/bin/python,python3)
.DEFAULT_GOAL := all
.PHONY: all build markdown test test-rdf check coverage coverage-report visualization help
all: build
build: coverage-report
markdown:
	$(PYTHON) scripts/markdown_graph.py
	$(PYTHON) scripts/build_visualization.py
visualization: markdown
coverage-report: ontology
	$(PYTHON) scripts/coverage_report.py
check: deps-ontology
	$(PYTHON) scripts/markdown_graph.py --check
	$(PYTHON) scripts/catalog.py check
	$(PYTHON) scripts/ontology.py check
	$(PYTHON) scripts/coverage_report.py --check
test: check
	$(PYTHON) -B -m unittest discover -s tests -v
test-rdf: deps-ontology
	$(PYTHON) scripts/ontology.py check
coverage: deps-ontology
	$(PYTHON) scripts/coverage_report.py --json
help:
	@printf '%s\n' 'make: install ONTFS in the project environment and build the catalog and ontology' 'See INSTALL.md for installation, usage and troubleshooting.'
	@printf '%s\n' 'make build: install ONTFS, build and validate the graph, and regenerate coverage and viewer' 'make markdown: regenerate Markdown pages, index and viewer without ONTFS' 'make test: reject structural errors and stale generated records; run regression tests' 'make test-rdf: validate the ONTFS projection with SHACL and SPARQL' 'make coverage: query ONTFS coverage counts' 'make test-ai: exercise bounded ONTFS retrieval for the AI test-design skill' 'make check-lean: check model and witness bindings without compiling' 'make test-lean: compile models and proofs, audit axioms, and run rejection tests'

.PHONY: submodules deps-ontology ontology test-ontology
submodules:
	$(PYTHON) scripts/setup_ontfs.py
deps-ontology: $(VENV)/.ontology-installed
$(VENV)/.ontology-installed: requirements-ontology.txt dependencies.lock.json scripts/setup_ontfs.py | submodules
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install -r requirements-ontology.txt
	@touch $@
ontology: markdown deps-ontology
	$(PYTHON) scripts/ontology.py build
	$(PYTHON) scripts/ontology.py check
test-ontology:
	$(PYTHON) scripts/ontology.py check
	$(PYTHON) -B -m unittest discover -s tests -p 'test_ontology.py' -v

.PHONY: test-ai check-lean test-lean
test-ai:
	$(PYTHON) -B -c "import sys; sys.path.insert(0, 'scripts'); from ontology import backend; backend()"
	$(PYTHON) -B -m unittest discover -s tests -p 'test_test_context.py' -v

check-lean:
	$(PYTHON) scripts/lean.py check
test-lean:
	$(PYTHON) scripts/lean.py verify
	CATALOG_TEST_LEAN=1 $(PYTHON) -B -m unittest discover -s tests -p 'test_lean*.py' -v
