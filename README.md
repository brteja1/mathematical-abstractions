# Mathematical Abstractions

A knowledge graph of mathematical abstractions for modeling software, developing formal proofs, and deriving software tests. The catalog describes mathematical behavior independently of particular implementations, making definitions, assumptions and reusable properties available to people and AI agents.

Start with the [concept index](CONCEPTS.md), explore the [interactive atlas](https://brteja1.github.io/mathematical-abstractions/), or query selected records with Python. Examples include [groups](concepts/Group.md), [binary trees](concepts/BinaryTree.md), [probability spaces](concepts/ProbabilitySpace.md), and [linearizability](concepts/Linearizability.md).

The catalog spans foundations, types, logic, algebra, order, combinatorics, probability, measure theory, topology, geometry, linear algebra, numeric computation, data structures, databases, programming semantics and concurrency. Coverage grows through explicit definitions and sourced claims rather than an assumption that any subject is complete.

## What each concept records

- A definition, notation, carrier, equality convention and chosen mathematical basis.
- Operations with signatures, preconditions, outcomes and definedness.
- Axioms, laws and theorems with stable identities, assumptions, applicability and derivation premises.
- Typed links to prerequisites, specializations and related concepts, without automatic axiom inheritance.
- Source references, precise locators and provenance notes.
- Separate Lean model and proof-witness bindings where available.

## Browse online

The [interactive atlas](https://brteja1.github.io/mathematical-abstractions/) supports subject categories, specialization hierarchies, search, relationship filters, concept details, keyboard selection, pan and zoom. Concept links open the corresponding Markdown records on GitHub. The standalone [`visualization/index.html`](visualization/index.html) also works offline.

The [Pages workflow](.github/workflows/pages.yml) rebuilds, validates and publishes the viewer on pushes to `main`.

## Storage and fields

| Location | Role |
| --- | --- |
| [`concepts/`](concepts/) | One editable Markdown file per concept, with typed links, backlinks, readable operations/claims, and an authoritative marked JSON record block. |
| [`data/shared.json`](data/shared.json) | Authoritative JSON-LD context, categories, concept kinds, vocabulary and shared sources. |
| [`catalog.jsonld`](catalog.jsonld) | Generated interoperable JSON-LD export for RDF/SPARQL tools. |
| [`CONCEPTS.md`](CONCEPTS.md) | Generated complete concept index. |
| [`COVERAGE.md`](COVERAGE.md) | Generated counts and basis coverage, not a completeness certificate. |
| [`visualization/template.html`](visualization/template.html) | Editable viewer template; `index.html` is generated. |

Markdown graph records are authoritative. `make build` generates their readable prose, backlinks, indexes, JSON-LD export, coverage report and viewer. Edit the marked JSON blocks in concept pages or the shared context/source data, then rebuild.

The [foundational data-model guide](docs/FOUNDATIONAL_DATA_MODELS.md) maps the broad computer-science core to the catalog: types and values, collection ADTs, trees and graphs, streams, numeric data, state, and database/interchange models. It documents 35 additions, explicit instantiations such as strings and records, selected conventions, and remaining variants.

See [agent workflows](docs/AGENT_WORKFLOWS.md) for proof planning and test design, and [AGENTS.md](AGENTS.md) for the catalog's contribution requirements.

## Query from AI agents

Python 3 and the standard library are sufficient; no service, credentials, embedding model or network is needed.

```sh
python3 scripts/catalog.py list --search group
python3 scripts/catalog.py list --category probability
python3 scripts/catalog.py get Group --sections operations axioms laws theorems sources
python3 scripts/agent_query.py neighbors Group --incoming --depth 1 --limit 40
python3 scripts/agent_query.py dossier Group --purpose proof --limit 80
python3 scripts/agent_query.py dossier Stack --purpose tests --limit 80
python3 scripts/agent_query.py node urn:csabs:concept/Group
```

Commands emit JSON. Retrieval reads current Markdown records directly. `get` expands only requested sections; `node` fetches any stable concept/claim/operation/source ID. `neighbors` supports chosen edge types and incoming edges. A `dossier` traverses interfaces, prerequisites, sources and derivation premises within an explicit node limit, reports truncation, and includes task instructions. Retrieve omitted premises before relying on a truncated result.

The graph helps agents select definitions, assemble proof obligations, follow premises and derive test properties. Catalog statements and proof sketches are informal specifications; selected claims have separate compiled Lean witnesses. Applying either to software requires mapping the mathematical carriers, operations, equality and assumptions to the target API.

## Maintain and extend

1. Search names, synonyms, notation and meaning before adding a concept or claim. Reuse existing records when appropriate; keep distinct semantic variants explicit.
2. Edit the marked JSON array at the bottom of the relevant concept page. Keep the Concept and its operation/claim records together; shared claims have exactly one stored record and may be referenced from multiple concepts. Do not duplicate their IDs. To add a page, use the same block markers and filename equal to `shortForm`.
3. Add sources and vocabulary to `data/shared.json` as needed. Every new Concept/Axiom/Law/Theorem requires direct links to consulted sources, `sourceLocator`, `sourceNote` and `provenanceKind`. Derived claims need `dependsOn` and a meaningful proof sketch. Record actual source consultation dates and keep citation gaps visible.
4. Record carriers, equality, empty cases, totality, overflow, rounding, nondeterminism and concurrency assumptions as relevant. Explain specialization mappings; never infer automatic axiom inheritance.
5. Run the build and checks:

```sh
make build
make test
make test-rdf  # optional: requires rdflib
```

`make build` validates authoritative records, regenerates readable page bodies and backlinks, exports JSON-LD, and rebuilds coverage and the offline viewer. Changes to generated prose alone are overwritten; `make test` rejects stale Markdown projections/exports and viewer data. Claims shared by pages are stored once in the first linked page by shortForm sort order after building. Find the marked record by stable ID to edit it.

Checks cover unique IDs and short forms, typed references, operation ownership, claim applicability, explicit bases and assumptions, acyclic derivation/specialization links, source provenance, page links and generated-artifact consistency.

Validation checks structure and citation metadata. Mathematical correctness, source entailment and informal-to-formal correspondence require separate review; compiled proof evidence is checked through the Lean workflow.

## AI skill for abstraction-based tests

[`ai/skills/mathematical-tests/SKILL.md`](ai/skills/mathematical-tests/SKILL.md) guides agents from a software API to applicable mathematical concepts, axioms and laws, then to runnable tests. It covers API/operation mappings, definedness, numeric policies, nondeterminism and evidence limitations. Agents should read the skill explicitly or register this directory using their host's skill-discovery mechanism.

Its Python helper uses the pinned ONTFS projection for compact searches and selected interfaces, claims, premises and direct citations. Responses have hard record/character budgets, pagination and depth-boundary flags; complete mathematical records are preserved. Stale or locally edited runtime graphs are rejected. After the [ONTFS setup](docs/ONTOLOGY.md):

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search queue --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Queue --limit 6 --max-chars 8000
make PYTHON=.venv/bin/python test-ai
```

The helper works from other repositories via its absolute path. See the skill's [retrieval guide](ai/skills/mathematical-tests/references/retrieval.md) for setup, source freshness, pagination and exact limits. No full graph dump or embedding service is needed.

### Acknowledgment

I would like to thank my colleague, Mr. Devendra Bhave, for introducing me to the technique of using mathematical abstractions to guide software test design.

## Lean formalization

The [`lean/`](lean/README.md) Lake project provides models or explicitly partial interfaces for all 142 catalog concepts, with pinned Lean/Mathlib versions and 52 compiled law/theorem witnesses. This includes the [finite ordered binary-tree abstraction](concepts/BinaryTree.md), with an explicit empty case and witnesses for every recorded binary-tree law/theorem. A separate [`bindings.json`](lean/bindings.json) links stable catalog IDs to declarations, expected types, premise mappings and limitations. `make test-lean` compiles and audits witnesses, rejects admitted or fabricated proofs, and records fresh compiler evidence. Model coverage does not mean every catalog claim has been proved. See the [formalization guide](lean/README.md) for setup, coverage and adding a new theorem.

## ONTFS ontology backend

The ontology is modeled in [`ontology/model.ttl`](ontology/model.ttl), with [`SHACL shapes`](ontology/shapes.ttl), an ONTFS exporter and bounded context/SPARQL access. ONTFS is configured as the submodule dependency `deps/ONTFS`, pinned to `05f166cd3ba37f13984b2746ddbbe56de24d8113` in [`dependencies.lock.json`](dependencies.lock.json). See [setup status and ontology workflow](docs/ONTOLOGY.md).

```sh
make submodules
make deps-ontology
make PYTHON=.venv/bin/python ontology test-ontology
.venv/bin/python scripts/ontology.py context urn:csabs:concept/Group --limit 30
.venv/bin/python scripts/ontology.py query ontology/prerequisites.rq
```

ONTFS is registered as a submodule at the locked commit. After cloning this repository, run `make submodules`, then `make deps-ontology` to install the ontology backend into the project virtual environment.
