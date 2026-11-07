# Mathematical Abstractions for Computer Science

The machine-readable catalog is [`catalog.jsonld`](catalog.jsonld), a JSON-LD knowledge graph. Treat it as the source of truth for concept facts. [`CATALOG.md`](CATALOG.md) is a discovery roadmap and explanatory overview; consult individual graph records for authoritative structured definitions, operations, axioms, laws, and theorems.

## Why a graph

Concepts, operations, categories, axioms, laws, theorems, variants, and sources are separately addressable nodes. Typed edges connect them. An agent can retrieve one concept and just its requested claim types instead of loading the full catalog. Cross-cutting facts such as “which concepts have partial operations?” can be queried across concepts.

## Entry model

Every `Concept` node has:

- `shortForm`: stable compact identifier, unique within this catalog.
- `fullName`: preferred human-readable name.
- `category`: one or more broad subject areas.
- `kind`: controlled concept kind, such as `mathematical-structure`, `relation`, `function`, `principle`, `data-type`, `abstract-data-type`, or `semantic-model`.
- `definition`: descriptive-language definition.
- `notation`: mathematical definition/signature in a string, preserving standard notation.
- `hasOperation`, `hasAxiom`, `hasLaw`, `hasTheorem`: links to separately identified claim nodes.
- Optional `relatedConcept`, `specializationOf`, and `source` links.
- `specializationNote`, when present, explains how to instantiate or restrict the parent interface, including any underlying structure or type identification.

An `Operation` has `name`, `signature`, and `description`; optional fields include `precondition`, `postcondition`, and `totality` where specified. Axioms/laws/theorems each have a stable ID, `statement` in natural language, `formalStatement` in notation where available, and optional `assumptions`, `proofSketch`, `source`, and `appliesTo`. Their distinct RDF types prevent a defining axiom from being mistaken for a consequence or an operational convention. Derived induction and inference principles use `Theorem` nodes with `ruleRole: "proof-principle"`, assumptions, proof sketches, and explicit `dependsOn` premises. They remain in `hasTheorem`; a principle is not automatically a new foundational axiom. Do not encode a theorem as an axiom merely because it is useful.

Categories and kinds are controlled vocabulary nodes, not free text. Use multiple category links for concepts at disciplinary intersections. Add aliases and external IDs as optional metadata; Wikidata QIDs and Wikipedia links are discovery/identity aids, not authority for mathematical truth. Record convention choices (e.g. unital ring, overflow semantics, equality model) in the relevant concept or claim.

## Query examples

JSON-LD expands to RDF. With Apache Jena `arq` and a JSON-LD-capable RDF loader, queries can be run over the graph. The following are SPARQL patterns over the catalog namespace (`https://w3id.org/cs-abstractions/v1#`); a production loader should use the bundled JSON-LD context.

Retrieve a concept's concise definition and notation:

```sparql
PREFIX ca: <https://w3id.org/cs-abstractions/v1#>
SELECT ?name ?definition ?notation WHERE {
  ?concept a ca:Concept ; ca:shortForm "FixedWidthUnsignedInteger" ;
           ca:fullName ?name ; ca:definition ?definition ; ca:notation ?notation .
}
```

Retrieve only its operations:

```sparql
PREFIX ca: <https://w3id.org/cs-abstractions/v1#>
SELECT ?name ?signature ?description WHERE {
  ?concept ca:shortForm "FixedWidthUnsignedInteger" ; ca:hasOperation ?op .
  ?op ca:name ?name ; ca:signature ?signature ; ca:description ?description .
}
```

Retrieve a selected claim kind (replace `hasLaw` with `hasAxiom` or `hasTheorem`):

```sparql
PREFIX ca: <https://w3id.org/cs-abstractions/v1#>
SELECT ?claim ?statement ?formal WHERE {
  ?concept ca:shortForm "FloatingPointType" ; ca:hasLaw ?claim .
  ?claim ca:statement ?statement .
  OPTIONAL { ?claim ca:formalStatement ?formal }
}
```

Find concepts by category or concept kind by joining to category/kind nodes. Agents should query by stable `shortForm`, request only the needed claim predicates, then follow related concepts only when the current task needs them.

## Maintenance conventions

- Keep IDs stable and human-readable: `urn:csabs:concept:<short-form>` and `urn:csabs:<claim-kind>:<slug>`.
- Never reuse an ID for a changed mathematical meaning. Create a variant node when conventions differ materially.
- Link every operation/claim from its subject concept and every source-backed claim to its source node when practical.
- Separate abstract mathematics from programming-language semantics. For example, mathematical integers, modular integers, C unsigned arithmetic, and C signed arithmetic are distinct concepts.
- State assumptions and preconditions explicitly. A missing field or empty claim-link array means “not yet cataloged”, not “false” or “no such fact exists”.
- Keep descriptive definitions concise; put queryable details in operations and claim nodes. Use `formalStatement` for machine-readable mathematical notation where feasible, and identify the notation language when escaping or syntax matters.
- Wikipedia/Wikidata are useful for discovery and identity reconciliation. For axioms and theorem statements, prefer textbooks, standards, original papers, or formal-library references and attach provenance.

## Initial coverage

The graph starts with sets, relations, functions, products and power sets, equivalence/partitions, Boolean algebra, semigroups/monoids/groups, rings/semirings/fields, arrays/sequences/stacks/queues, integer models, and floating-point types. The roadmap in `CATALOG.md` identifies further areas to add, including logic, order theory, graphs, programming semantics, and concurrency.

## Local retrieval without an RDF service

The standard-library CLI reads the graph locally and emits only the requested concept and sections:

```sh
python3 scripts/catalog.py list --category concurrency
python3 scripts/catalog.py list --search invariant
python3 scripts/catalog.py get Map --sections operations laws
python3 scripts/catalog.py get Group --sections axioms laws theorems dependencies
python3 scripts/catalog.py check
python3 scripts/catalog.py check --rdf
```

The final command optionally uses `rdflib` for JSON-LD expansion and a SPARQL concept-count check. Normal retrieval has no external dependencies or network access. The default `get` includes definitions and reference IDs but does not expand operations or claims; each requested section expands only its immediate nodes. Dependency traversal is explicit: retrieve the named prerequisite concept in a subsequent call. There is no automatic inference from `specializationOf` or `requiresConcept`; a parent carrier and its operations must be instantiated correctly before transferring its laws.

The graph now includes order and fixed points, classical logic, counting and induction, graph structures, data types, proof contracts, transition systems, and concurrency semantics. It also records relational schemas, finite database relations, functional dependencies and candidate keys; finite sets and ordered unique collections; formal and regular languages, DFA/NFA recognizers, context-free grammars and Turing machines; labelled transition systems, finite-trace equivalence, finite serial Kripke structures, modal logic K and infinite-trace LTL. Each addition has directly linked consulted sources and scoped semantic conventions. Each entry has a queryable coverage status. `basis-reviewed` means its selected defining interface and representative derived results have been documented and reviewed editorially; it does not assert an exhaustive theorem list. Claim review status distinguishes editorial summaries from formal proofs. Formal statements currently use informal Unicode mathematical notation; they are queryable strings, not executable proof-assistant syntax. Proof sketches are included for selected elementary results. External references are optional further evidence, never required for local retrieval.

Concept and claim IDs are stored as absolute URNs, and vocabulary class IDs use the graph namespace. This avoids implementation-dependent relative-URN resolution. The vocabulary namespace is a local identifier convention, not a claim of a registered or hosted schema.

## Interactive radial visualization

Open `visualization/index.html` directly in a browser. It is a standalone artifact with embedded catalog data and no network dependencies. Colored circumference arcs represent subject areas; concept points occupy the inner circular layer. The overview shows concepts without an explicit `specializationOf` parent. Selecting a concept reveals its direct specializations and retains its ancestors (including multiple-parent paths). Deeper levels appear as you select their parents. Subconcept labels appear only for children of the selected parent and for the selected concept itself; other retained ancestors appear as context points without labels. Search, the dropdown, category details, and relationship buttons can reach every concept, including hidden ones. This display hierarchy uses explicit specialization links, not prerequisites or automatic inheritance.

Hover or focus a node to trace its connections; edge gradients run from the source category colour to the destination category colour. Selection smoothly adjusts the viewport to fit the selected concept and its direct children, including their labels and a margin. Ancestors remain available in the graph without expanding the selection viewport. Radial spacing adapts to the visible slice, with subject arcs beyond the concept labels. Wheel scrolling and + / − animate zoom; drag the background to pan. Fit frames all currently visible concepts without collapsing the hierarchy. Clear selection or Escape restores the overview. Reduced-motion preferences disable camera animation. Relationship checkboxes control edges whose endpoints are visible; category arcs highlight memberships, including secondary memberships. Each node stays within its first category. Keyboard users can Tab through visible nodes and arcs and press Enter to select.

After editing the catalog or `visualization/template.html`, refresh the standalone artifact:

```sh
python3 scripts/build_visualization.py
```

The diagram shows explicit concept-to-concept prerequisite, specialization, and related-concept edges; claim nodes remain available in the details panel. It does not invent connections for concepts whose relationships are not yet recorded. The viewer uses the direction stored in the catalog (for example, Group → Monoid means Group requires Monoid).

## Concept hierarchies

Specialization edges point from the more specific concept to its parent. The existing entries now expose these hierarchies (arrows below mean `specializationOf`, not prerequisites):

- Group → Monoid → Semigroup; Field → Ring → Semiring.
- TotalOrder → PartialOrder → Preorder → Relation; EquivalenceRelation → Preorder; WellFoundedRelation → Relation.
- CompleteLattice → Lattice → PartialOrder; BooleanAlgebra → Lattice.
- ClosureOperator → MonotoneFunction → Function → PartialFunction → Relation; Map → PartialFunction with finite domain.
- Tree → Graph; DAG → DirectedGraph.
- Bisimulation → Simulation → Relation.
- OptionType → SumType with parameters UnitType and A.
- Binary16, Binary32, Binary64 and Binary128 → FloatingPointType at their recorded format parameters.
- ProbabilitySpace → MeasureSpace → MeasurableSpace; RandomVariable → MeasurableFunction → Function.
- SmoothManifold → Manifold → TopologicalSpace.
- Tensor → VectorSpace → Group; TensorProduct → VectorSpace; LinearMap → Function; Matrix → Function at fixed shape.
- BayesianNetwork → DAG after forgetting its variable carriers and probability tables. MarkovChain relates to transition systems through its support graph; probabilities are additional information.

Each newly recorded edge has a `specializationNote` explaining the interface mapping. These links organize existing definitions; they do not copy or automatically inherit operations, axioms, or proofs. Existing claim IDs, ownership, and provenance remain intact. Similar-looking axioms with different carriers or assumptions are not automatically interchangeable.

Graph denotes finite simple undirected graphs, so DirectedGraph is not its specialization. HappensBefore uses a strict relation, so it is not linked as a specialization of the non-strict PartialOrder. Fixed-width integer policies and bit-vector representations remain distinct from exact integer or residue-class structures. PowerSet is a construction producing a set and is linked to Set as a related concept rather than a specialization. Parameter instantiation and explicit forgetting of structure must be distinguished from arbitrary representation changes.

## Make targets

Run these commands from the project root:

| Command | Action |
| --- | --- |
| `make` or `make visualization` | Generate `visualization/index.html` when the catalog, template, or builder changes; check graph sanity before rebuilding. |
| `make -B visualization` | Force graph checks and regenerate the visualization. |
| `make test` | Check unique node IDs and concept short forms, resolved graph references, and required concept, operation, and claim fields. |
| `make test-rdf` | Run the same checks, expand JSON-LD to RDF, and verify the SPARQL concept count. Requires `rdflib`. |
| `make help` | List targets. |

Override the Python interpreter as needed, for example `make PYTHON=.venv/bin/python test-rdf`. Tests check graph structure and RDF access; they do not prove the mathematical claims or test browser rendering.

## Axiom bases and derivations

A sparse definition is not a complete verification interface. Expanded entries should state a chosen axiom basis and provide constructors, eliminators, computation equations (beta rules), extensionality or uniqueness equations (eta rules), and the hypotheses needed for derived claims. Definitions of auxiliary operations should also be recorded as equations. Axioms are relative to a presentation: constructor computation equations can be primitive rules in a type theory or theorems about a tagged-set implementation.

The expanded SumType, ProductType, OptionType, EmptyType, UnitType, and FunctionType entries use extensional total set-like types. In that convention function equality is pointwise. This does not silently supply function extensionality in an intensional proof assistant, nor laws for languages with bottom values, effects, or exceptions.

SumType records `case-inl`, `case-inr`, `sum-eta`, `map-sum-definition`, coproduct uniqueness, injection disjointness/injectivity, map identity/composition, case fusion, and sum isomorphisms. `absurd-unique` belongs to EmptyType and is reachable through SumType's prerequisites. `dependsOn` connects claims to the operations and claims used in their derivations; `requiresConcept` connects concepts. Proof sketches and external references support inspection but are not formal proofs. Local claim names are catalog identifiers, not assertions that a source library uses those exact names.

Use `make coverage` or `python3 scripts/catalog.py coverage` to inspect per-concept operation/axiom/law/theorem counts and whether an axiom basis is documented. Empty axiom lists require review, rather than mechanically adding axioms: some concepts are constructions from an existing theory. Neither nonempty lists nor an `expanded` status certify completeness. All current entries have now received an editorial basis review; their `basisScope` records the interface covered. This does not certify formal consistency, every theorem, or every alternative semantic model.


## Basis review across the current catalog

All 89 current concepts document a chosen basis, individually identified governing rules, and selected derived results. Defining rules include first-order ZF schemas, algebraic structure equations, relational constraints, constructor/eliminator rules, ADT contracts, and operational semantic definitions. The `ruleRole` field identifies their role; a construction’s definition is not a new axiom of the foundational logic. All variables range over the stated carriers.

[The coverage table](COVERAGE.md) summarizes every entry. Regenerate it with `make coverage-report`; use `make coverage` for JSON. Claim dependencies are explicit where recorded, and concept prerequisites remain separate. The current interface uses informal mathematical Unicode, with proof sketches for selected consequences. It is not an executable formal theory. Floating-point entries describe the listed numeric interfaces; bit-level NaN payloads, complete trap handling, and transcendental-library contracts remain outside the declared scope.

`make test` now checks basis metadata, operation ownership, claim-link types, assumptions and formal statements, and acyclic derivation links. Mutation tests demonstrate rejection of missing bases, wrongly typed claims, dangling/cyclic dependencies, duplicate IDs, absent operation explanations, and missing formal rules. `make test-rdf` additionally checks JSON-LD expansion and SPARQL access. These are structural checks, not proofs that all mathematical statements are valid.

## Required provenance for new data

Every new concept, axiom, law, and theorem must have a direct `source` link. Each addition also records `sourceLocator` (a section, named definition/theorem, or page), `sourceNote` describing the adaptation, and `provenanceKind` (`direct`, `adapted`, or `derived`). Derived claims link their premises using `dependsOn`. Source records identify the title, URL/local path/bibliographic citation, actual access date, and source role. Consult supporting material before recording it; topic lists and related references are not automatically proof evidence.

Historical gaps are listed in `provenance_legacy.json` and marked `legacy-source-missing` in the graph. They have not been retrospectively supplied with unverifiable references. The baseline may shrink as sources are verified; it must not be extended for new additions. Existing source-linked nodes remain subject to source-presence checks. `make test` rejects new unsourced entries and incomplete provenance metadata; the checks cannot establish that a source supports a mathematical statement.

## Probability and geometric interfaces

The 2026-11-07 extension adds 16 concepts without changing historical concept or claim identities. `MeasurableSpace` includes the sigma-algebra interface, `MeasureSpace` adds a nonnegative measure, and `ProbabilitySpace` adds normalization. `MeasurableFunction`, `RandomVariable`, and `ConditionalProbability` cover measurable maps, pushforward laws and positive-event conditioning. `BayesianNetwork` uses finite discrete variables and normalized tables on a finite DAG; `MarkovChain` uses a nonempty finite state set, discrete time, a fixed row-stochastic matrix and an initial row distribution. These entries do not assert causal interpretation, faithfulness, stationarity, irreducibility or convergence without further assumptions.

`TopologicalSpace` records open-set structure; `Manifold` adds a fixed finite dimension, Hausdorff separation, a countable basis and local charts without boundary; `SmoothManifold` adds a chosen maximal C∞ atlas. `VectorSpace`, `LinearMap`, `Matrix`, `TensorProduct` and `Tensor` supply the algebraic interfaces. Matrices allow zero dimensions and exact field arithmetic. Tensor valence and dual factors are explicit; coordinate arrays require bases and do not define a basis-independent tensor by shape alone. Smooth manifolds are not assumed to have a metric, connection or orientation, and tensors at a vector space are distinct from tensor fields on a manifold.

Sources consulted for this extension include Axler’s [Measure, Integration & Real Analysis](https://measure.axler.net/MIRA.pdf) (§§2B–2C) and [Linear Algebra Done Right](https://linear.axler.net/LADR4e.pdf) (§§1B, 3A–3F, 9D), Lee’s [author-hosted Chapter 1](https://sites.math.washington.edu/~lee/Books/ISM/c01.pdf), the [Cambridge Markov Chains notes](https://www.dpmms.cam.ac.uk/~rrw1/markov/M.pdf) (§§1.2, 1.5), Stanford CS228 notes on [probability](https://ermongroup.github.io/cs228-notes/preliminaries/probabilityreview/) and [Bayesian networks](https://ermongroup.github.io/cs228-notes/representation/directed/), and the Mathlib definition and universal-property references linked directly from graph nodes. The Axler books are licensed CC BY-NC 4.0; the graph records that attribution and license link. Interfaces and editorial derivations are adapted to catalog notation, with general-field and empty-case conventions stated explicitly. Every new concept and claim has direct source provenance; the historical provenance baseline is unchanged.

For example:

```sh
python3 scripts/catalog.py get ProbabilitySpace --sections axioms theorems sources
python3 scripts/catalog.py get BayesianNetwork --sections operations axioms theorems
python3 scripts/catalog.py get MarkovChain --sections operations theorems
python3 scripts/catalog.py get Manifold --sections axioms dependencies
python3 scripts/catalog.py get Tensor --sections axioms theorems sources
```
