# ONTFS ontology integration

[ONTFS](https://github.com/brteja1/ONTFS) provides local RDF graph storage, SPARQL queries and SHACL validation for the catalog. Run `make` from the repository root to configure and install it and build the projection. See [INSTALL.md](../INSTALL.md) for installation and troubleshooting.

## Ontology model

[`ontology/model.ttl`](../ontology/model.ttl) defines the catalog's classes and relationships using the existing vocabulary namespace. Concepts, operations, axioms, laws, theorems, sources, categories and kinds retain their original identities. Axiom/Law/Theorem records are subclasses of a common Claim record class. Documents represent the Markdown files linked to concepts.

The classes describe catalog records. For example, Group is a Concept individual, not an OWL class of all groups. `Group specializationOf Monoid` is therefore an explicit catalog relationship with an interface mapping, not an asserted OWL subclass statement. This avoids treating prerequisite links as logical entailment or transferring claims automatically. Relations retain stored directions; symmetry and transitivity are not silently introduced. SPARQL property paths can deliberately traverse multiple explicit links.

The model declares object properties with appropriate domains/ranges, selected literal metadata, and comments describing interpretation. Export also declares remaining imported predicates as RDF properties without inventing ranges for heterogeneous legacy metadata. No graph content is rewritten to fit a different ontology.

[`ontology/shapes.ttl`](../ontology/shapes.ttl) checks concept interfaces, operation ownership targets, typed claim links and dependency targets. It complements the Python validator. The frozen historical provenance policy, global uniqueness, cycle checks and mathematical entry requirements continue to be enforced by `make test` and the export's preflight validation. SHACL alone is not a replacement for those checks and does not validate mathematical truth.

## Validation and coverage

`make` builds the ONTFS projection, validates it with native SHACL, and writes `COVERAGE.md` using SPARQL counts of explicit interface links. `make coverage` returns the same coverage as JSON; `make test-rdf` checks the existing projection without rebuilding it. There is no stored JSON-LD catalog. Python validates authoritative records before conversion to preserve duplicate-ID, provenance-history, ownership and derivation-cycle safeguards.

Validation and coverage require a fresh, unmodified projection and the original generated shapes. They refuse stale inputs, local runtime edits or changed shapes rather than overwriting them. `make test` also checks the generated coverage report for staleness.

## Build and query

```sh
.venv/bin/python scripts/ontology.py build
.venv/bin/python scripts/ontology.py check
.venv/bin/python scripts/ontology.py context urn:csabs:concept/Group --depth 1 --limit 30
.venv/bin/python scripts/ontology.py query ontology/prerequisites.rq
```

The build loads authoritative Markdown, validates it, expands it to RDF, and uses ONTFS transactions/storage to create `.ontfs.ttl`. It adds the ontology and Markdown document pointers while preserving all original RDF triples. `.ontfs.shapes.ttl` enables native ONTFS validation; a generation marker tracks inputs and detects local edits before another export. The generated runtime files are ignored by Git and can be reproduced from source.

Use `scripts/ontology.py --directory /tmp/math-ontology build` for a separate scratch graph. Document identifiers are relocatable when pages are inside the graph directory and absolute when outside it, following ONTFS behavior. From the repository graph directory, the installed `ontfs context`, `ontfs query` and `ontfs validate` commands can also access the projection directly.

For test-design agents, [`scripts/test_context.py`](../scripts/test_context.py) adds fixed ONTFS/SPARQL queries with record/character budgets, explicit pagination and premise-depth boundaries. It checks both source-input freshness and projection-file integrity before querying and returns lossless authoritative JSON records selected by ONTFS. The [`mathematical-tests` skill](../ai/skills/mathematical-tests/SKILL.md) uses this helper through its local `scripts/query.py` entrypoint; `make test-ai` exercises the real backend, budget behavior and stale/edit rejection paths.

## Editing and agent proposals

Markdown records remain authoritative. Rebuild the ONTFS projection after changing concepts or ontology files. `check` detects changed inputs, runs native ONTFS SHACL validation and checks the concept count.

ONTFS proposals are useful for experiments in a separate graph. Validate their evidence and assumptions before promoting a change into Markdown, then run the full build and validation suite. A proposal accepted by ONTFS's SHACL checks has not necessarily passed the catalog's provenance, duplicate-meaning or derivation-cycle policy. The exporter refuses to overwrite a modified generated graph, so experimental edits must be preserved separately and reconciled explicitly.

The pinned ONTFS proposal validator compares structured baseline/candidate SHACL violations. It rejects new or worsened violations without treating presentation text differences as new errors. Ontology and SHACL checks establish data structure constraints; Lean/Coq checking remains a separate downstream task.
