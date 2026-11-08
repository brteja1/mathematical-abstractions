# Installation and usage

## Prerequisites

Install Git, GNU Make and Python 3.10 or newer with `venv` and pip support. On Debian or Ubuntu:

```sh
sudo apt install git make python3 python3-venv python3-pip
```

The first full setup needs internet access to retrieve ONTFS and Python packages. No hosted graph service, credentials or embedding model is needed. Lean verification is optional and has separate prerequisites below.

## Install and build

```sh
git clone https://github.com/brteja1/mathematical-abstractions.git
cd mathematical-abstractions
make
```

`make` initializes the repository's ONTFS dependency, creates `.venv`, installs ONTFS with RDF and SHACL support, regenerates the catalog and viewer, builds and validates the local ontology projection, and writes coverage from SPARQL queries. It does not install packages into system Python or stage Git changes. The dependency revision is controlled by `dependencies.lock.json`; setup preserves that revision rather than following upstream updates.

Repeated runs reuse the installed environment unless the requirements, dependency lock or setup script changes. After initial setup, builds can run offline using the existing dependency and environment. To reinstall Python dependencies explicitly, run:

```sh
.venv/bin/python -m pip install -r requirements-ontology.txt
make
```

The default environment is `.venv`. To choose another location, use the same setting on subsequent Make commands:

```sh
make VENV=/tmp/mathematical-abstractions-venv
```

Make targets automatically select the environment's Python when it exists. Direct Python commands below use `.venv/bin/python`; adjust the path if you chose a different environment. You can also activate it with `source .venv/bin/activate`.

## Browse and query

Open `visualization/index.html` in a browser to explore the standalone atlas, or read [CONCEPTS.md](CONCEPTS.md) for the complete concept index.

Retrieve small slices of the authoritative Markdown graph:

```sh
.venv/bin/python scripts/catalog.py list --search group
.venv/bin/python scripts/catalog.py get Group --sections operations axioms laws theorems sources
.venv/bin/python scripts/agent_query.py node urn:csabs:concept/Group
.venv/bin/python scripts/agent_query.py dossier Stack --purpose tests --limit 80
```

Query the generated ontology with ONTFS:

```sh
.venv/bin/python scripts/ontology.py context urn:csabs:concept/Group --limit 30
.venv/bin/python scripts/ontology.py query ontology/prerequisites.rq
.venv/bin/ontfs validate
```

See the [ontology guide](docs/ONTOLOGY.md) for graph semantics and scratch graphs. Markdown remains authoritative; edits to the runtime ontology are not automatically imported into the catalog.

## Use the AI test-design skill

Read or register [ai/skills/mathematical-tests/SKILL.md](ai/skills/mathematical-tests/SKILL.md) through your agent's skill-discovery mechanism. Keep the skill connected to this checkout; its helper uses the repository's scripts and environment.

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search queue --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Queue --limit 6 --max-chars 8000
make test-ai
```

From another repository, invoke the helper and Python interpreter by their absolute paths. Consult the skill's [retrieval guide](ai/skills/mathematical-tests/references/retrieval.md) for pagination, budgets and freshness checks.

## Edit and validate

Open the concept's Markdown file directly, for example `concepts/Group.md`. Near the bottom, find the JSON block between `<!-- graph-record:start -->` and `<!-- graph-record:end -->`. This block is the authoritative record: edit its definition, operation signatures, assumptions, claims or source references. The readable Markdown sections above it are generated and will be overwritten by a rebuild. For a new concept, create `concepts/<shortForm>.md` with the same block markers and record structure as an existing concept.

Keep stable IDs unchanged when the mathematical meaning is unchanged. Search existing records before adding claims, and update linked operations or claims in their owning concept files. Shared vocabulary and sources belong in `data/shared.json`. Follow [AGENTS.md](AGENTS.md) for source provenance, claim ownership and mathematical assumptions, then run:

```sh
make
make test test-rdf test-ontology test-ai
```

These checks validate data structure, source metadata, generated artifacts, RDF access and retrieval behavior. They do not establish mathematical truth or prove a software implementation correct. `make coverage` reports catalog coverage; `make help` lists the main targets.

There is no second catalog to maintain. Markdown records feed the ONTFS projection directly; no `catalog.jsonld` file is generated or required. ONTFS validates graph constraints with SHACL, and coverage is queried through SPARQL. Python preflight checks retain safeguards for duplicate IDs, claim ownership, provenance history and derivation cycles before RDF conversion. Validation and coverage reject stale projections, unexported graph edits and modified runtime shapes.

For catalog queries and viewer generation without installing ONTFS, use system Python and the lightweight build target:

```sh
python3 scripts/catalog.py list --search group
make markdown
python3 scripts/catalog.py check
```

These commands require only the Python standard library. Full builds, coverage reports and the required validation suite use ONTFS through the project environment; run `make` before `make test`.

## Optional Lean verification

Install [Elan](https://github.com/leanprover/elan), then prepare the repository's existing Lean/Mathlib project:

```sh
cd lean
lake update
lake exe cache get
lake build
cd ..
make check-lean test-lean
```

The first setup downloads the specified toolchain and precompiled Mathlib artifacts and needs several GB of disk space. Preserve the existing toolchain and dependency revisions. See [lean/README.md](lean/README.md) for witness mappings, verification evidence and limitations. Default `make` does not install Lean or compile proofs.

## Troubleshooting

- **Python cannot create a virtual environment:** install your distribution's Python `venv` package, then rerun `make`.
- **Network or package download failure:** check access to GitHub and your Python package index, then rerun `make`. Dependency installation is marked complete only after pip succeeds.
- **Missing Git metadata:** use a Git clone rather than a downloaded source archive; automatic ONTFS initialization needs the registered dependency.
- **Dependency revision or origin mismatch:** inspect `git submodule status` and `git -C deps/ONTFS status`. Setup checks the registered revision and origin against the lock and refuses inconsistent registrations. Preserve local work before resolving a mismatch; setup never stages a new revision.
- **Local edits in ONTFS:** an initialized checkout at the expected revision is reused without changing its files. Setup refuses to switch a modified checkout to another revision. Preserve your changes before resolving the mismatch.
- **Modified runtime graph:** the exporter refuses to overwrite unexported edits. Preserve the graph and build a scratch projection with `.venv/bin/python scripts/ontology.py --directory /tmp/catalog-ontology build`. Use the same `--directory` for later queries.
- **Missing or stale projection:** rerun `make` after changing catalog or ontology inputs. Generated runtime files are ignored by Git.
- **Permission errors during dependency initialization:** ensure the checkout and its Git metadata are writable. Setup initializes the registered dependency without committing or pushing.
