PYTHON ?= python3
.DEFAULT_GOAL := build
.PHONY: all build test test-rdf check coverage coverage-report visualization help
all: build
build:
	$(PYTHON) scripts/markdown_graph.py
	$(PYTHON) scripts/coverage_report.py
	$(PYTHON) scripts/build_visualization.py
visualization: build
coverage-report: build
check:
	$(PYTHON) scripts/markdown_graph.py --check
	$(PYTHON) scripts/catalog.py check
test: check
	$(PYTHON) -B -m unittest discover -s tests -v
test-rdf:
	$(PYTHON) scripts/catalog.py check --rdf
coverage:
	$(PYTHON) scripts/catalog.py coverage
help:
	@printf '%s\n' 'make build: validate Markdown and regenerate JSON-LD, links, index, coverage and viewer' 'make test: reject structural errors and stale generated records; run regression tests' 'make test-rdf: optional JSON-LD/SPARQL check (rdflib)' 'make coverage: query coverage counts' 'make check-lean: check model and witness bindings without compiling' 'make test-lean: compile models and proofs, audit axioms, and run rejection tests'

VENV ?= .venv
.PHONY: submodules deps-ontology ontology test-ontology
submodules:
	$(PYTHON) scripts/setup_ontfs.py
deps-ontology:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install -r requirements-ontology.txt
ontology:
	$(PYTHON) scripts/ontology.py build
test-ontology:
	$(PYTHON) scripts/ontology.py check
	$(PYTHON) -B -m unittest discover -s tests -p 'test_ontology.py' -v

.PHONY: check-lean test-lean
check-lean:
	$(PYTHON) scripts/lean.py check
test-lean:
	$(PYTHON) scripts/lean.py verify
	CATALOG_TEST_LEAN=1 $(PYTHON) -B -m unittest discover -s tests -p 'test_lean*.py' -v
