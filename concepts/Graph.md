# Graph

A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant.

**Notation:** G=(V,E); E⊆{e: e={u,v},u,v∈V,u≠v }

**Stable ID:** `urn:csabs:concept/Graph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Set](Set.md)

**Specializes:** [Finite simple undirected hypergraph](Hypergraph.md)

## Backlinks

- [Finite acyclic undirected graph (forest)](AcyclicGraph.md) — `requiresConcept`
- [Finite acyclic undirected graph (forest)](AcyclicGraph.md) — `specializationOf`
- [Finite simple graph with chosen bipartition](BipartiteGraph.md) — `requiresConcept`
- [Finite simple graph with chosen bipartition](BipartiteGraph.md) — `specializationOf`
- [Tree](Tree.md) — `requiresConcept`

## Mathematical formulation

For a finite vertex type V, a simple undirected graph is Adj:V→V→Prop with Adj(u,v)↔Adj(v,u) and ¬Adj(v,v). There are no parallel edges; an empty vertex type is permitted. Utility profile: All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).

**Lean formulation** (in its source module context):

```lean
abbrev Graph (V : Type u) [Fintype V] := SimpleGraph V
```

**Source:** [`Catalog.Graph`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib SimpleGraph V with explicit Fintype V; symmetric irreflexive adjacency.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant. Governing rules: A graph has a finite vertex set and edges are unordered two-element subsets. Adjacency means sharing an edge; it is symmetric and irreflexive in this variant. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:**  Represent each undirected simple edge {u,v}, u≠v, by its two-element vertex subset. The 2-uniform hypergraph retains exactly the finite simple graph; adjacency corresponds to membership of {u,v} in H. No automatic inheritance of claims.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Graph-neighbors"></a>

### neighbors

`urn:csabs:operation/Graph-neighbors`

**signature:** N : V→𝒫(V)

**description:** Returns vertices sharing an edge with the input vertex.

<a id="node-urn-csabs-operation-Graph-component-of"></a>

### component-of

`urn:csabs:operation/Graph-component-of`

**signature:** componentOf : Graph(V)×V→Set(V)

**description:** All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Graph-components"></a>

### components

`urn:csabs:operation/Graph-components`

**signature:** components : Graph(V)→Set(Set(V))

**description:** {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Graph-bounded-reachability"></a>

### bounded-reachability

`urn:csabs:operation/Graph-bounded-reachability`

**signature:** boundedReach : Graph(V)×ℕ×V²→Prop

**description:** Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Graph-simple-finite"></a>

### simple-finite

`urn:csabs:axiom/Graph-simple-finite`

**statement:** A graph has a finite vertex set and edges are unordered two-element subsets.

**formalStatement:** V finite; E⊆{e⊆V:card(e)=2}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Graph-adjacency"></a>

### adjacency

`urn:csabs:axiom/Graph-adjacency`

**statement:** Adjacency means sharing an edge; it is symmetric and irreflexive in this variant.

**formalStatement:** adj(u,v) iff {u,v}∈E; N(u)={v∈V:adj(u,v)}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Graph-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/Graph-utility-profile`

**statement:** All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).

**formalStatement:** componentOf : Graph(V)×V→Set(V): All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; components : Graph(V)→Set(Set(V)): {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; boundedReach : Graph(V)×ℕ×V²→Prop: Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Graph-core"></a>

### law/Graph-core

`urn:csabs:law/Graph-core`

**statement:** The sum of vertex degrees equals twice the number of edges (handshaking lemma).

**formalStatement:** Σ(v∈V) deg(v)=2·card(E)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [simple-finite](Graph.md#node-urn-csabs-axiom-Graph-simple-finite); [adjacency](Graph.md#node-urn-csabs-axiom-Graph-adjacency)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Graph-adjacency-symmetric"></a>

### adjacency-symmetric

`urn:csabs:theorem/Graph-adjacency-symmetric`

**statement:** Adjacency is symmetric in the undirected graph variant.

**formalStatement:** adj(u,v) iff adj(v,u)

**proofSketch:** The unordered pair {u,v} equals {v,u}.

**assumptions:** The explicit basis, carriers, and side conditions stated for Graph apply.

**dependsOn:** [simple-finite](Graph.md#node-urn-csabs-axiom-Graph-simple-finite); [adjacency](Graph.md#node-urn-csabs-axiom-Graph-adjacency)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Graph-bounded-reachability-closure"></a>

### bounded-reachability-closure

`urn:csabs:theorem/Graph-bounded-reachability-closure`

**statement:** For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges.

**formalStatement:** For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges.

**proofSketch:** Induction over the bound and over reflexive-transitive closure.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](Graph.md#node-urn-csabs-axiom-Graph-utility-profile); [adjacency](Graph.md#node-urn-csabs-axiom-Graph-adjacency)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion; Catalog.boundedReach_closure

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

For any edge relation E, (∃n,Bₙ(a,b)) iff E\*(a,b), where Bₙ permits at most n edges.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} (edge : V → V → Prop) (a b : V), (∃ n, Catalog.boundedReach edge n a b) ↔ Relation.ReflTransGen edge a b
```

**Source:** [`Catalog.boundedReach_closure`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Graph-adjacency": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/Graph-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-Graph-component-characterization"></a>

### component-characterization

`urn:csabs:theorem/Graph-component-characterization`

**statement:** componentOf(v)=componentOf(w) iff v and w are reachable.

**formalStatement:** componentOf(v)=componentOf(w) iff v and w are reachable.

**proofSketch:** Undirected reachability is reflexive, symmetric and transitive; transfer membership along paths.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](Graph.md#node-urn-csabs-axiom-Graph-utility-profile); [simple-finite](Graph.md#node-urn-csabs-axiom-Graph-simple-finite)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion; Catalog.graph_components

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

componentOf(v)=componentOf(w) iff v and w are reachable.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} (g : SimpleGraph V) (v w : V), (Catalog.componentOf g v = Catalog.componentOf g w ↔ g.Reachable v w)
```

**Source:** [`Catalog.graph_components`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** componentOf(v)=componentOf(w) iff v and w are reachable. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Graph-simple-finite": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/Graph-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Graph",
    "type": "Concept",
    "shortForm": "Graph",
    "fullName": "Graph",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant.",
    "notation": "G=(V,E); E⊆{e: e={u,v},u,v∈V,u≠v }",
    "hasOperation": [
      "urn:csabs:operation/Graph-neighbors",
      "urn:csabs:operation/Graph-component-of",
      "urn:csabs:operation/Graph-components",
      "urn:csabs:operation/Graph-bounded-reachability"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Graph-simple-finite",
      "urn:csabs:axiom/Graph-adjacency",
      "urn:csabs:axiom/Graph-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/Graph-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Graph-adjacency-symmetric",
      "urn:csabs:theorem/Graph-bounded-reachability-closure",
      "urn:csabs:theorem/Graph-component-characterization"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant. Governing rules: A graph has a finite vertex set and edges are unordered two-element subsets. Adjacency means sharing an edge; it is symmetric and irreflexive in this variant. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Hypergraph"
    ],
    "specializationNote": " Represent each undirected simple edge {u,v}, u≠v, by its two-element vertex subset. The 2-uniform hypergraph retains exactly the finite simple graph; adjacency corresponds to membership of {u,v} in H. No automatic inheritance of claims.",
    "leanFormulation": "abbrev Graph (V : Type u) [Fintype V] := SimpleGraph V",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.Graph",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib SimpleGraph V with explicit Fintype V; symmetric irreflexive adjacency.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For a finite vertex type V, a simple undirected graph is Adj:V→V→Prop with Adj(u,v)↔Adj(v,u) and ¬Adj(v,v). There are no parallel edges; an empty vertex type is permitted. Utility profile: All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b)."
  },
  {
    "id": "urn:csabs:operation/Graph-neighbors",
    "type": "Operation",
    "name": "neighbors",
    "signature": "N : V→𝒫(V)",
    "description": "Returns vertices sharing an edge with the input vertex.",
    "concept": "urn:csabs:concept/Graph"
  },
  {
    "id": "urn:csabs:operation/Graph-component-of",
    "type": "Operation",
    "concept": "urn:csabs:concept/Graph",
    "name": "component-of",
    "signature": "componentOf : Graph(V)×V→Set(V)",
    "description": "All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Graph-components",
    "type": "Operation",
    "concept": "urn:csabs:concept/Graph",
    "name": "components",
    "signature": "components : Graph(V)→Set(Set(V))",
    "description": "{componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "{componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Graph-bounded-reachability",
    "type": "Operation",
    "concept": "urn:csabs:concept/Graph",
    "name": "bounded-reachability",
    "signature": "boundedReach : Graph(V)×ℕ×V²→Prop",
    "description": "Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Graph-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).",
    "formalStatement": "componentOf : Graph(V)×V→Set(V): All vertices reachable from v by a finite undirected path, including v; an isolated vertex has singleton component.; components : Graph(V)→Set(Set(V)): {componentOf(v) | v∈V}; for the empty graph the component collection is empty. Components partition V.; boundedReach : Graph(V)×ℕ×V²→Prop: Path length at most n, including zero-length paths: B₀(a,b) iff a=b; Bₙ₊₁(a,b) iff a=b or ∃c,E(a,c)∧Bₙ(c,b).",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/Graph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Graph-core",
    "type": "Law",
    "statement": "The sum of vertex degrees equals twice the number of edges (handshaking lemma).",
    "formalStatement": "Σ(v∈V) deg(v)=2·card(E)",
    "appliesTo": [
      "urn:csabs:concept/Graph"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Graph-simple-finite",
      "urn:csabs:axiom/Graph-adjacency"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Graph-adjacency-symmetric",
    "type": "Theorem",
    "name": "adjacency-symmetric",
    "statement": "Adjacency is symmetric in the undirected graph variant.",
    "formalStatement": "adj(u,v) iff adj(v,u)",
    "proofSketch": "The unordered pair {u,v} equals {v,u}.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Graph apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Graph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Graph-simple-finite",
      "urn:csabs:axiom/Graph-adjacency"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Graph-bounded-reachability-closure",
    "type": "Theorem",
    "name": "bounded-reachability-closure",
    "statement": "For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges.",
    "formalStatement": "For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges.",
    "mathematicalFormulation": "For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges.",
    "proofSketch": "Induction over the bound and over reflexive-transitive closure.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Graph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Graph-utility-profile",
      "urn:csabs:axiom/Graph-adjacency"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion; Catalog.boundedReach_closure",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} (edge : V → V → Prop) (a b : V), (∃ n, Catalog.boundedReach edge n a b) ↔ Relation.ReflTransGen edge a b",
    "leanModelMapping": "For any edge relation E, (∃n,Bₙ(a,b)) iff E*(a,b), where Bₙ permits at most n edges. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Graph-adjacency\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/Graph-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.boundedReach_closure"
  },
  {
    "id": "urn:csabs:theorem/Graph-component-characterization",
    "type": "Theorem",
    "name": "component-characterization",
    "statement": "componentOf(v)=componentOf(w) iff v and w are reachable.",
    "formalStatement": "componentOf(v)=componentOf(w) iff v and w are reachable.",
    "mathematicalFormulation": "componentOf(v)=componentOf(w) iff v and w are reachable.",
    "proofSketch": "Undirected reachability is reflexive, symmetric and transitive; transfer membership along paths.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/Graph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Graph-utility-profile",
      "urn:csabs:axiom/Graph-simple-finite"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Combinatorics/SimpleGraph/Path.lean: Reachable; Logic/Relation.lean: ReflTransGen; constructed bounded-length recursion; Catalog.graph_components",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} (g : SimpleGraph V) (v w : V), (Catalog.componentOf g v = Catalog.componentOf g w ↔ g.Reachable v w)",
    "leanModelMapping": "componentOf(v)=componentOf(w) iff v and w are reachable. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Graph-simple-finite\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/Graph-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.graph_components"
  }
]
```
<!-- graph-record:end -->
