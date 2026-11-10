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

Choose **Subjects**, **Specializations**, or **Dependencies** in the atlas. Subjects use nested arcs; the other views place general concepts or prerequisites above their dependents. Dependency cycles share a level. See the [hierarchy guide](docs/HIERARCHY.md) for the first data-structure/concurrency organization pass and reviewed relationship mappings.

Subject categories use `parentCategory` in `data/shared.json` for nesting. Broad subjects appear on outer arcs; subsubjects appear on inner arcs within the same angular span. Linear and multilinear algebra sits under Algebra. Data structures and concurrency have nested subject families, including synchronization → locks and lock protocols. Selecting a subject includes its subsubjects; this navigation hierarchy does not imply concept specialization or axiom inheritance.

The [Pages workflow](.github/workflows/pages.yml) rebuilds, validates and publishes the viewer on pushes to `main`.

## Installation

Clone this repository and run `make` to install ONTFS and build the catalog, viewer and ontology. See [INSTALL.md](INSTALL.md) for prerequisites, setup, usage and troubleshooting.

## Storage and fields

| Location | Role |
| --- | --- |
| [`concepts/`](concepts/) | One editable Markdown file per concept, with typed links, backlinks, readable operations/claims, and an authoritative marked JSON record block. |
| [`data/shared.json`](data/shared.json) | Authoritative categories, concept kinds, vocabulary and shared sources. |
| [`CONCEPTS.md`](CONCEPTS.md) | Generated complete concept index. |
| [`COVERAGE.md`](COVERAGE.md) | Generated counts and basis coverage, not a completeness certificate. |
| [`visualization/template.html`](visualization/template.html) | Readable page shell for the standalone viewer. |
| [`visualization/styles.css`](visualization/styles.css) | Viewer theme, graph styles and responsive layout. |
| [`visualization/app.js`](visualization/app.js) | Organized graph rendering, labels, selection, details and camera behavior. |
| [`visualization/index.html`](visualization/index.html) | Generated offline page with the styles, script and catalog embedded. |

Edit concepts directly in their `concepts/<shortForm>.md` files. Each file stores its authoritative structured records in a marked JSON block; the readable sections above that block are generated from those records. Update definitions, operations, claims and references in that block, then run `make` to refresh the page, links, indexes, viewer and ontology. Shared vocabulary and sources live in `data/shared.json`.

ONTFS supplies the generated RDF projection for SHACL validation and SPARQL coverage reporting. Ordinary catalog queries and viewer generation read the Markdown records directly. See the [editing workflow](INSTALL.md#edit-and-validate).

The [foundational data-model guide](docs/FOUNDATIONAL_DATA_MODELS.md) maps the broad computer-science core to the catalog: types and values, collection ADTs, trees and graphs, streams, numeric data, state, and database/interchange models. It documents 35 additions, explicit instantiations such as strings and records, selected conventions, and remaining variants.

The [logic guide](docs/LOGIC.md) maps propositional and first-order syntax, semantic queries, substitution, natural deduction, normal forms, completeness and compactness, with explicit provenance and formalization limits.

The [object-oriented models guide](docs/OBJECT_ORIENTED_MODELS.md) connects object identity and aliasing, class lookup and dispatch, method contracts and write effects, visible-state invariants, behavioral subtyping and exclusive heap separation. It explains how exposed representations can break invariants and documents the Lean model limitations.

The [template metaprogramming guide](docs/TEMPLATE_METAPROGRAMMING.md) covers kinded partial metafunctions, class partial-specialization selection, SFINAE versus hard errors, identity-based constraint subsumption, packs/folds, staged name lookup and a checked constant-evaluation fragment. It uses an explicit C++20 draft profile and includes [compiler-checked examples](examples/template_metaprogramming.md).

The [generic-programming guide](docs/GENERIC_PROGRAMMING.md) adds shared signatures, argument binding and instantiation, then separate Java and VHDL profiles. Java covers bounds, nominal generic subtyping, capture, erasure and inference, with runnable compiler examples. VHDL covers generic interfaces, association and elaboration; its illustrative example is explicitly unexecuted because no VHDL compiler is installed locally.

See [agent workflows](docs/AGENT_WORKFLOWS.md) for proof planning, test design and specification consistency reviews, and [AGENTS.md](AGENTS.md) for the catalog's contribution requirements.

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

Category queries include all descendant subjects and accept a suffix or full category ID; for example, `--category synchronization` includes Lock, Mutex and LamportBakery.

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
make test-rdf  # ONTFS SHACL validation and SPARQL count check
```

`make build` validates authoritative records, regenerates readable page bodies and backlinks, builds and validates the ONTFS projection, and rebuilds SPARQL coverage and the offline viewer. Changes to generated prose alone are overwritten; `make test` rejects stale Markdown pages, ontology projections, coverage and viewer data. Claims shared by pages are stored once in the first linked page by shortForm sort order after building. Find the marked record by stable ID to edit it.

Checks cover unique IDs and short forms, typed references, operation ownership, claim applicability, explicit bases and assumptions, acyclic derivation/specialization links, source provenance, page links and generated-artifact consistency.

Validation checks structure and citation metadata. Mathematical correctness, source entailment and informal-to-formal correspondence require separate review; compiled proof evidence is checked through the Lean workflow.

## AI skill for specification consistency

The [specification-consistency skill](ai/skills/specification-consistency/SKILL.md) guides agents in finding conflicting requirements and impossible operation contracts. It maps specification clauses to catalog definitions and explicit assumptions, then helps agents construct and execute suitable checks. It covers joint satisfiability, required input coverage, vacuous preconditions, and stateful or temporal obligations.

To use it, ask an agent:

> Read `ai/skills/specification-consistency/SKILL.md` and check `path/to/spec.md` for inconsistencies. Report conflicting clause IDs, required scenarios, reproducible evidence, assumptions and unchecked obligations.

Agents can read the skill explicitly or register its directory using their host's skill-discovery mechanism. It reuses the standard-library catalog commands and, when available, the bounded ONTFS retrieval helper. Depending on the specification, checks may use exhaustive finite enumeration, an installed solver/model checker, or Lean. The skill does not install a general-purpose consistency solver.

The [runnable Boolean example](ai/skills/specification-consistency/references/boolean-example.md) uses only Python's standard library. It demonstrates a conflict missed by pairwise checks, an input with no permitted output, and verification of a proposed repair. The [checking and reporting guide](ai/skills/specification-consistency/references/checking-and-reporting.md) explains backend selection and evidence requirements.

Catalog and SHACL validation check structure; semantic consistency requires a justified model and a separate check. Findings distinguish demonstrated conflicts from ambiguities, conditional results and inconclusive searches. A bounded search or a single satisfying instance does not establish that every required input or behavior is supported.

## AI skills for implementation and review

Use [implementation-mapping](ai/skills/implementation-mapping/SKILL.md) to translate a catalog-based specification into concrete types, API operations, equality/observations, state representations, errors and implementation obligations. Its [mapping template](ai/skills/implementation-mapping/assets/implementation-map.md) belongs beside the target software and records specification clauses, catalog IDs, decisions and evidence. When code generation is requested, the skill guides implementation from that mapping.

Use [implementation-conformance](ai/skills/implementation-conformance/SKILL.md) to compare code with the specification and mapping. It checks the mapping's interpretation as well as implementation behavior, distinguishes defects from ambiguities, and reports supported, violated and unchecked obligations with scoped evidence. The [worked stack example](ai/skills/implementation-mapping/references/stack-example.md) demonstrates a capacity mismatch that small push/pop tests can miss and includes runnable Python checks.

For example, ask an agent:

> Read `ai/skills/implementation-mapping/SKILL.md`, map `path/to/spec.md` to the API in `path/to/project`, then implement the resolved obligations using that project's conventions. Keep unresolved semantic decisions explicit.

> Read `ai/skills/implementation-conformance/SKILL.md` and review `path/to/project` against its specification and implementation mapping. Report clause/obligation IDs, counterexamples, execution evidence and unchecked behavior.

The skills reuse existing catalog retrieval, specification-consistency and mathematical-test workflows. Read them explicitly or register their directories with the agent host; placing them in `ai/skills/` alone does not enable automatic discovery. They add no runtime dependency to generated software. Tests and abstract model proofs do not by themselves establish implementation refinement.

## AI skill for abstraction-based tests

[`ai/skills/mathematical-tests/SKILL.md`](ai/skills/mathematical-tests/SKILL.md) guides agents from a software API to applicable mathematical concepts, axioms and laws, then to runnable tests. It covers API/operation mappings, definedness, numeric policies, nondeterminism and evidence limitations. Agents should read the skill explicitly or register this directory using their host's skill-discovery mechanism.

Its Python helper uses the ONTFS projection for compact searches and selected interfaces, claims, premises and direct citations. Responses have hard record/character budgets, pagination and depth-boundary flags; complete mathematical records are preserved. Stale or locally edited runtime graphs are rejected. After [installation](INSTALL.md):

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search queue --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Queue --limit 6 --max-chars 8000
make test-ai
```

The helper works from other repositories via its absolute path. See the skill's [retrieval guide](ai/skills/mathematical-tests/references/retrieval.md) for setup, source freshness, pagination and exact limits. No full graph dump or embedding service is needed.

### Acknowledgment

I would like to thank my colleague, Mr. Devendra Bhave, for introducing me to the technique of using mathematical abstractions to guide software test design.

## Lean formalization

The [`lean/`](lean/README.md) Lake project provides models or explicitly partial interfaces for all current catalog concepts, with pinned Lean/Mathlib versions and 52 compiled law/theorem witnesses. This includes the [finite ordered binary-tree abstraction](concepts/BinaryTree.md), with an explicit empty case and witnesses for every recorded binary-tree law/theorem. A separate [`bindings.json`](lean/bindings.json) links stable catalog IDs to declarations, expected types, premise mappings and limitations. `make test-lean` compiles and audits witnesses, rejects admitted or fabricated proofs, and records fresh compiler evidence. Model coverage does not mean every catalog claim has been proved. See the [formalization guide](lean/README.md) for setup, coverage and adding a new theorem.

## ONTFS ontology backend

[ONTFS](https://github.com/brteja1/ONTFS) is a local ontology knowledge-graph tool for organizing and querying linked records. This repository uses it to expose the catalog through RDF/SPARQL, validate graph constraints with SHACL, and retrieve bounded context for AI test design. Markdown remains the authoritative source. See the [ontology guide](docs/ONTOLOGY.md) for the model and query workflow.
