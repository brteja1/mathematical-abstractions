# ONTFS ontology integration

The dependency is [brteja1/ONTFS](https://github.com/brteja1/ONTFS), pinned to [`05f166cd3ba37f13984b2746ddbbe56de24d8113`](https://github.com/brteja1/ONTFS/commit/05f166cd3ba37f13984b2746ddbbe56de24d8113), the remote default-branch HEAD verified on 2026-11-07. The declared submodule lives at `deps/ONTFS`. A fixed commit makes future clones reproducible; it does not follow a moving HEAD automatically.

## Setup status and completion

The parent Git repository was initialized on 2026-11-07, and ONTFS was cloned and committed as a submodule at the locked revision. Both its checked-out HEAD and the parent's `160000` gitlink match the lock. The parent repository is published on GitHub; fresh clones must initialize the submodule before using the backend.

Earlier managed-environment filesystem and DNS restrictions prevented registration; these restrictions have been removed. The temporary upstream source used during initial integration checks is no longer needed.

To initialize the dependency in another checkout and install the backend:

```sh
make submodules
make deps-ontology
make PYTHON=.venv/bin/python ontology test-ontology
```

`make submodules` runs `scripts/setup_ontfs.py`: it creates or initializes the real submodule, checks out the locked commit in detached HEAD mode, and stages `.gitmodules` and the `160000` gitlink. It does not commit or push. It refuses to replace a non-Git parent or a dependency checkout containing local edits. Subsequent parent clones can use `git submodule update --init --recursive` after the gitlink is committed.

`make deps-ontology` installs the local submodule and its SHACL extra in a project virtual environment. It does not modify the system Python. Use `PYTHON=.venv/bin/python` for ontology commands once installed. The basic Markdown queries and viewer build remain available without this backend.

## Ontology model

[`ontology/model.ttl`](../ontology/model.ttl) defines the catalog's classes and relationships using the existing vocabulary namespace. Concepts, operations, axioms, laws, theorems, sources, categories and kinds retain their original identities. Axiom/Law/Theorem records are subclasses of a common Claim record class. Documents represent the Markdown files linked to concepts.

The classes describe catalog records. For example, Group is a Concept individual, not an OWL class of all groups. `Group specializationOf Monoid` is therefore an explicit catalog relationship with an interface mapping, not an asserted OWL subclass statement. This avoids treating prerequisite links as logical entailment or transferring claims automatically. Relations retain stored directions; symmetry and transitivity are not silently introduced. SPARQL property paths can deliberately traverse multiple explicit links.

The model declares object properties with appropriate domains/ranges, selected literal metadata, and comments describing interpretation. Export also declares remaining imported predicates as RDF properties without inventing ranges for heterogeneous legacy metadata. No graph content is rewritten to fit a different ontology.

[`ontology/shapes.ttl`](../ontology/shapes.ttl) checks concept interfaces, operation ownership targets, typed claim links and dependency targets. It complements the Python validator. The frozen historical provenance policy, global uniqueness, cycle checks and mathematical entry requirements continue to be enforced by `make test` and the export's preflight validation. SHACL alone is not a replacement for those checks and does not validate mathematical truth.

## Build and query

```sh
.venv/bin/python scripts/ontology.py build
.venv/bin/python scripts/ontology.py check
.venv/bin/python scripts/ontology.py context urn:csabs:concept/Group --depth 1 --limit 30
.venv/bin/python scripts/ontology.py query ontology/prerequisites.rq
```

The build loads authoritative Markdown, validates it, expands it to RDF, and uses ONTFS transactions/storage to create `.ontfs.ttl`. It adds the ontology and Markdown document pointers while preserving all original RDF triples. `.ontfs.shapes.ttl` enables native ONTFS validation; a generation marker tracks inputs and detects local edits before another export. The generated runtime files are ignored by Git and can be reproduced from source.

Use `scripts/ontology.py --directory /tmp/math-ontology build` for a separate scratch graph. Document identifiers are relocatable when pages are inside the graph directory and absolute when outside it, following ONTFS behavior. From the repository graph directory, the installed `ontfs context`, `ontfs query` and `ontfs validate` commands can also access the projection directly.

The wrapper checks a present submodule's HEAD against the lock. Integration tests use the registered submodule when present. The checked-out commit and parent gitlink can be inspected with `git submodule status` and `git ls-files --stage -- deps/ONTFS`.

For test-design agents, [`scripts/test_context.py`](../scripts/test_context.py) adds fixed ONTFS/SPARQL queries with record/character budgets, explicit pagination and premise-depth boundaries. It checks both source-input freshness and projection-file integrity before querying and returns lossless authoritative JSON records selected by ONTFS. The [`mathematical-tests` skill](../ai/skills/mathematical-tests/SKILL.md) uses this helper through its local `scripts/query.py` entrypoint; `make test-ai` exercises the real backend, budget behavior and stale/edit rejection paths.

## Editing and agent proposals

Markdown records remain authoritative. Rebuild the ONTFS projection after changing concepts or ontology files. `check` detects changed inputs, runs native ONTFS SHACL validation and checks the concept count.

ONTFS proposals are useful for experiments in a separate graph. Validate their evidence and assumptions before promoting a change into Markdown, then run the full build and validation suite. A proposal accepted by ONTFS's SHACL checks has not necessarily passed the catalog's provenance, duplicate-meaning or derivation-cycle policy. The exporter refuses to overwrite a modified generated graph, so experimental edits must be preserved separately and reconciled explicitly.

The pinned ONTFS proposal validator compares structured baseline/candidate SHACL violations. It rejects new or worsened violations without treating presentation text differences as new errors. Ontology and SHACL checks establish data structure constraints; Lean/Coq checking remains a separate downstream task.
