# Mathematical Abstractions

A knowledge graph of mathematical abstractions for modeling software, developing formal proofs, and deriving software tests. The catalog describes mathematical behavior independently of particular implementations, making definitions, assumptions and reusable properties available to people and AI agents.

Start with the [concept index](CONCEPTS.md), explore the [interactive atlas](https://brteja1.github.io/mathematical-abstractions/), or query selected records with Python.

Key subject areas include logic and foundations, algebra and linear algebra, probability and statistics, geometry, data structures, programming semantics, concurrency, cryptography and information theory. See the concept index for current coverage and individual concept pages for definitions, assumptions and sources.

## What each concept records

- A definition, notation, carrier, equality convention and chosen mathematical basis.
- Operations with signatures, preconditions, outcomes and definedness.
- Axioms, laws and theorems with stable identities, assumptions, applicability and derivation premises.
- Typed links to prerequisites, specializations and related concepts, without automatic axiom inheritance.
- Source references, precise locators and provenance notes.
- Separate Lean model and proof-witness bindings where available.

## Browse online

The [interactive atlas](https://brteja1.github.io/mathematical-abstractions/) supports subject categories, specialization hierarchies, search, relationship filters, concept details, keyboard selection, pan and zoom. Concept links open the corresponding Markdown records on GitHub. The standalone [`visualization/index.html`](visualization/index.html) also works offline.

Choose **Subjects**, **Specializations**, or **Dependencies** in the atlas. Subjects use nested arcs; the other views place general concepts or prerequisites above their dependents. Dependency cycles share a level. See the [hierarchy guide](docs/HIERARCHY.md) for navigation and relationship conventions.

Subject categories use `parentCategory` in `data/shared.json` for nesting. Broad subjects appear on outer arcs; subsubjects appear on inner arcs within the same angular span. Selecting a subject includes its subsubjects; this navigation hierarchy does not imply concept specialization or axiom inheritance.

The [Pages workflow](.github/workflows/pages.yml) rebuilds, validates and publishes the viewer on pushes to `main`.

## Installation

Clone this repository and run `make` to install ONTFS and build the catalog, viewer and ontology. See [INSTALL.md](INSTALL.md) for prerequisites, setup, usage and troubleshooting.

After reviewing catalog changes against their Lean mappings, run `make update-lean-bindings` to refresh binding fingerprints, then `make check-lean` and `make test-lean`. Preview changes with `LEAN_FLAGS=--dry-run`, or select bindings with `LEAN_IDS="Graph BipartiteGraph"`. See the [Lean workflow](lean/README.md).

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

See [agent workflows](docs/AGENT_WORKFLOWS.md) for proof planning, test design and specification consistency reviews, and [AGENTS.md](AGENTS.md) for the catalog's contribution requirements.

## Query from AI agents

Python 3 and the standard library are sufficient; no service, credentials, embedding model or network is needed.

```sh
python3 scripts/catalog.py list --search group
python3 scripts/catalog.py list --category probability
python3 scripts/catalog.py get Group --sections operations
python3 scripts/agent_query.py node urn:csabs:concept/Group
```

Category queries include all descendant subjects and accept a suffix or full category ID; for example, `--category synchronization` includes Lock, Mutex and LamportBakery.

Commands emit JSON and read current Markdown records directly. `get` expands only requested sections; `node` fetches a selected stable concept/claim/operation/source ID. Focused fields are the default, with `--view lean` for needed typed material and `--view full` for complete records. Fetch a theorem by ID or request `--sections theorems` only when its result or proof is required. `neighbors` supports chosen edge types and incoming edges. Use a `dossier` only when the task needs its broader interface/prerequisite/claim closure; its node limit is not a relevance filter. Retrieve only needed omitted premises before relying on a truncated result.

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

All four AI skills retrieve context progressively: start with compact candidates and focused concept/operation records, fetch axioms/laws for the current obligation, and fetch theorems only when their results or proofs are needed. Lean excerpts and full records are opt-in through `--view lean` and `--view full`; operation-only interfaces are the default. Their shared [formulation guide](ai/skills/mathematical-tests/references/formulations.md) is consulted when typed correspondence or witness evidence is needed. Retained assumptions and partial-model limits remain explicit. Mathematical citations stay separate from local Lean sources queried with `sources ID --kind formulation`.

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

## AI skill for abstraction discovery

[`ai/skills/abstraction-discovery/SKILL.md`](ai/skills/abstraction-discovery/SKILL.md) guides agents in inspecting unannotated code, data structures, and APIs to uncover candidate mathematical abstractions. It maps operational signatures to catalog concepts (e.g., binary combination to `Monoid`, state reconciliation to `JoinSemilattice`, sorting/comparison to `TotalOrder`), evaluates governing algebraic laws (associativity, identity, transitivity, commutativity), produces counterexamples for violated laws, and recommends principled refactorings.

For example, ask an agent:

> Read `ai/skills/abstraction-discovery/SKILL.md` and inspect `path/to/code.py`. Discover candidate mathematical abstractions, report broken algebraic laws or missing invariants with reproducible counterexamples, and propose an algebraic refactoring.

The [discovery guide](ai/skills/abstraction-discovery/references/discovery-guide.md) catalogs common code anti-patterns and their mathematical causes; the [metrics aggregator example](ai/skills/abstraction-discovery/references/metrics-example.md) demonstrates diagnosing broken associativity and refactoring into a sound Monoid.

## AI skill for formal model checking

[`ai/skills/formal-model-checking/SKILL.md`](ai/skills/formal-model-checking/SKILL.md) guides agents in formulating and verifying concurrent protocols, state machines, and distributed algorithms using formal model checkers (TLA+, Alloy, Z3). Grounded in catalog concepts such as `Lock`, `Mutex`, `LabelledTransitionSystem`, and `LinearTemporalLogic`, it structures state variables, atomic transition relations (`Init` and `Next`), safety invariants (such as mutual exclusion), and liveness properties under explicit fairness constraints.

For example, ask an agent:

> Read `ai/skills/formal-model-checking/SKILL.md` and model `path/to/protocol.md` with TLA+ or Alloy. Verify mutual exclusion and deadlock freedom against catalog concept `Lock`, and report any counterexample traces.

The [backend selection guide](ai/skills/formal-model-checking/references/backend-selection.md) compares verification engines and state-space mitigation techniques; the [mutex TLA+ example](ai/skills/formal-model-checking/references/mutex-tla-example.md) includes a complete Ticket Lock specification and an executable Python state-space explorer demonstrating invariant checking and error-trace generation.

### Acknowledgment

I would like to thank my colleague, Mr. Devendra Bhave, for introducing me to the technique of using mathematical abstractions to guide software test design.

## Lean formalization

Every concept page now includes a readable mathematical formulation and the selected Lean declaration, with its carrier/assumption mapping, source module and limitations. Registered witness claims also show their quantified Lean proposition and direct premise mapping. These fields live in the authoritative Markdown JSON records and are visible in the offline viewer. Read excerpts in their linked module context; library aliases are interpretations, and partial models retain their missing obligations. `make check-lean` rejects excerpts or mappings that drift from the Lean sources/bindings. The local formulation sources are distinct from independent mathematical references and do not repair historical citation gaps.

The [`lean/`](lean/README.md) Lake project provides models or explicitly partial interfaces for all current catalog concepts, with pinned Lean/Mathlib versions and individually mapped law/theorem witnesses. A separate [`bindings.json`](lean/bindings.json) links stable catalog IDs to declarations, expected types, premise mappings and limitations. `make test-lean` compiles and audits witnesses, rejects admitted or fabricated proofs, and records fresh compiler evidence. Model coverage does not mean every catalog claim has been proved. See the [formalization guide](lean/README.md) for setup, coverage and adding a new theorem.

## ONTFS ontology backend

[ONTFS](https://github.com/brteja1/ONTFS) is a local ontology knowledge-graph tool for organizing and querying linked records. This repository uses it to expose the catalog through RDF/SPARQL, validate graph constraints with SHACL, and retrieve bounded context for AI test design. Markdown remains the authoritative source. See the [ontology guide](docs/ONTOLOGY.md) for the model and query workflow.
