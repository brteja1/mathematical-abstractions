# Finite acyclic undirected graph (forest)

A finite simple undirected graph with no simple cycle, permitting the empty graph and multiple connected components.

**Notation:** G=(V,E); V finite; E⊆{{u,v} | u,v∈V, u≠v}; no simple cycle.

**Stable ID:** `urn:csabs:concept/AcyclicGraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Graph](Graph.md)

**Specializes:** [Graph](Graph.md)

**Related concepts:** [Directed acyclic graph](DAG.md), [Finite single-parent rooted forest](SingleParentForest.md)

## Backlinks

- [Tree](Tree.md) — `specializationOf`

## Mathematical formulation

G=(V,E); V finite; E⊆{{u,v} | u,v∈V, u≠v}; no simple cycle. Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**Lean formulation** (in its source module context):

```lean
structure AcyclicGraph (V : Type u) [Fintype V] where
  graph : SimpleGraph V
  acyclic : graph.IsAcyclic
```

**Source:** [`Catalog.AcyclicGraph`](../lean/Catalog/KleeneForests.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.

**Limits:** No chosen roots or orientations, component enumeration, edge-count theorem or graph update algorithm is supplied. Path uniqueness and a family of concrete path-graph models have separate witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite simple undirected adjacency, with symmetry and no loops; absence of simple cycles. No connectivity or nonemptiness axiom.

**basisKind:** defined-structure

**basisScope:** Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**specializationNote:** Keep the same finite vertex set and simple undirected adjacency relation; require additionally that no simple cycle exists.

**verificationObligation:** Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms.

**reviewStatus:** Editorial mathematical interface review; only individually registered witnesses have compiler evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AcyclicGraph-adjacent"></a>

### adjacent

`urn:csabs:operation/AcyclicGraph-adjacent`

**signature:** adjacent : V×V→Prop

**description:** True exactly when {u,v}∈E; symmetric and false for u=v.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** True exactly when {u,v}∈E; symmetric and false for u=v.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AcyclicGraph-neighbors"></a>

### neighbors

`urn:csabs:operation/AcyclicGraph-neighbors`

**signature:** neighbors : V→P(V)

**description:** neighbors(v)={u∈V | {u,v}∈E}.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** neighbors(v)={u∈V | {u,v}∈E}.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AcyclicGraph-reachable"></a>

### reachable

`urn:csabs:operation/AcyclicGraph-reachable`

**signature:** reachable : V×V→Prop

**description:** True iff a finite path connects the vertices; reflexive via the empty path.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** True iff a finite path connects the vertices; reflexive via the empty path.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AcyclicGraph-paths"></a>

### paths

`urn:csabs:operation/AcyclicGraph-paths`

**signature:** paths : V×V→P(List(V))

**description:** All simple paths with the specified endpoints; zero-length path allowed when endpoints coincide.

**precondition:** Inputs belong to the displayed carriers.

**postcondition:** All simple paths with the specified endpoints; zero-length path allowed when endpoints coincide.

**totality:** Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AcyclicGraph-simple-undirected"></a>

### simple-undirected

`urn:csabs:axiom/AcyclicGraph-simple-undirected`

**statement:** The underlying graph is finite, simple and undirected.

**description:** The underlying graph is finite, simple and undirected.

**formalStatement:** V finite; Adj⊆V×V; Adj(u,v)⇔Adj(v,u); ¬Adj(v,v); E is a set of unordered pairs.

**assumptions:** Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-AcyclicGraph-no-cycle"></a>

### no-cycle

`urn:csabs:axiom/AcyclicGraph-no-cycle`

**statement:** No simple undirected cycle exists.

**description:** No simple undirected cycle exists.

**formalStatement:** ∀v∈V, ∀c:Walk(v,v), ¬IsCycle(c).

**assumptions:** Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-AcyclicGraph-path-model-satisfaction"></a>

### path-model-satisfaction

`urn:csabs:theorem/AcyclicGraph-path-model-satisfaction`

**statement:** Every finite path graph is a forest, including the empty graph at n=0.

**description:** Every finite path graph is a forest, including the empty graph at n=0.

**formalStatement:** ∀n∈ℕ, pathGraph(n) is a finite simple acyclic undirected graph on Fin(n).

**assumptions:** Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Derived from the directly linked defining premises; Construct pathForest n using the Mathlib theorem isAcyclic_pathGraph. n=0 covers the empty carrier; n=2 includes two distinct adjacent vertices, so this family is not restricted to edgeless models.

**provenanceKind:** derived

**dependsOn:** [simple-undirected](AcyclicGraph.md#node-urn-csabs-axiom-AcyclicGraph-simple-undirected); [no-cycle](AcyclicGraph.md#node-urn-csabs-axiom-AcyclicGraph-no-cycle)

**proofSketch:** Construct pathForest n using the Mathlib theorem isAcyclic_pathGraph. n=0 covers the empty carrier; n=2 includes two distinct adjacent vertices, so this family is not restricted to edgeless models.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ n : Nat, (Catalog.pathForest n).graph.IsAcyclic
```

**Source:** [`Catalog.forest_model_satisfaction`](../lean/Catalog/KleeneForests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AcyclicGraph-no-cycle": "Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.",
  "urn:csabs:axiom/AcyclicGraph-simple-undirected": "Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality."
}
```

<a id="node-urn-csabs-theorem-AcyclicGraph-path-uniqueness"></a>

### path-uniqueness

`urn:csabs:theorem/AcyclicGraph-path-uniqueness`

**statement:** Between fixed vertices of a forest there is at most one simple path.

**description:** Between fixed vertices of a forest there is at most one simple path.

**formalStatement:** ∀v,w∈V, ∀p,q∈Paths(v,w), p=q.

**assumptions:** Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.

**reviewStatus:** Editorial statement; consult the separate Lean witness binding for exact proof scope.

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Derived from the directly linked defining premises; Apply Mathlib IsAcyclic.subsingleton_path; two distinct simple paths would produce a cycle. Disconnected pairs have no path; the conclusion asserts uniqueness, not existence.

**provenanceKind:** derived

**dependsOn:** [simple-undirected](AcyclicGraph.md#node-urn-csabs-axiom-AcyclicGraph-simple-undirected); [no-cycle](AcyclicGraph.md#node-urn-csabs-axiom-AcyclicGraph-no-cycle)

**proofSketch:** Apply Mathlib IsAcyclic.subsingleton_path; two distinct simple paths would produce a cycle. Disconnected pairs have no path; the conclusion asserts uniqueness, not existence.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.AcyclicGraph V) (v w : V) (p q : f.graph.Path v w), p = q
```

**Source:** [`Catalog.forest_path_unique`](../lean/Catalog/KleeneForests.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.

**Limits:** Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/AcyclicGraph-no-cycle": "Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.",
  "urn:csabs:axiom/AcyclicGraph-simple-undirected": "Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality."
}
```

## Concept provenance

- [Mathlib: acyclic simple graphs and trees (pinned source)](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean); path: lean/.lake/packages/mathlib/Mathlib/Combinatorics/SimpleGraph/Acyclic.lean; accessedOn: 2026-11-20; sourceRole: Consulted upstream formal-library mathematical definitions and proofs at the pinned revision; Kyle Miller and Mathlib contributors, Apache-2.0.

**sourceLocator:** Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679

**sourceNote:** Definition adapted to the explicitly stated catalog carrier and operations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AcyclicGraph",
    "type": "Concept",
    "shortForm": "AcyclicGraph",
    "fullName": "Finite acyclic undirected graph (forest)",
    "definition": "A finite simple undirected graph with no simple cycle, permitting the empty graph and multiple connected components.",
    "notation": "G=(V,E); V finite; E⊆{{u,v} | u,v∈V, u≠v}; no simple cycle.",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "synonyms": [
      "Undirected forest",
      "Acyclic undirected graph",
      "Finite graph-theoretic forest"
    ],
    "axiomBasis": "Finite simple undirected adjacency, with symmetry and no loops; absence of simple cycles. No connectivity or nonemptiness axiom.",
    "basisKind": "defined-structure",
    "basisScope": "Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; only individually registered witnesses have compiler evidence.",
    "verificationObligation": [
      "Instantiate the stated carrier, equality, operation and definedness conventions. Typed links do not transfer axioms."
    ],
    "mathematicalFormulation": "G=(V,E); V finite; E⊆{{u,v} | u,v∈V, u≠v}; no simple cycle. Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten.",
    "hasOperation": [
      "urn:csabs:operation/AcyclicGraph-adjacent",
      "urn:csabs:operation/AcyclicGraph-neighbors",
      "urn:csabs:operation/AcyclicGraph-reachable",
      "urn:csabs:operation/AcyclicGraph-paths"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AcyclicGraph-simple-undirected",
      "urn:csabs:axiom/AcyclicGraph-no-cycle"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/AcyclicGraph-path-model-satisfaction",
      "urn:csabs:theorem/AcyclicGraph-path-uniqueness"
    ],
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "requiresConcept": [
      "urn:csabs:concept/Graph"
    ],
    "specializationOf": [
      "urn:csabs:concept/Graph"
    ],
    "specializationNote": "Keep the same finite vertex set and simple undirected adjacency relation; require additionally that no simple cycle exists.",
    "relatedConcept": [
      "urn:csabs:concept/DAG",
      "urn:csabs:concept/SingleParentForest"
    ],
    "leanFormulation": "structure AcyclicGraph (V : Type u) [Fintype V] where\n  graph : SimpleGraph V\n  acyclic : graph.IsAcyclic",
    "formulationSource": "urn:csabs:source/local-lean-KleeneForests",
    "formulationLocator": "Catalog.AcyclicGraph",
    "formulationScope": "model",
    "leanModelMapping": "Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.",
    "leanModelLimitations": "No chosen roots or orientations, component enumeration, edge-count theorem or graph update algorithm is supplied. Path uniqueness and a family of concrete path-graph models have separate witnesses."
  },
  {
    "id": "urn:csabs:operation/AcyclicGraph-adjacent",
    "type": "Operation",
    "name": "adjacent",
    "signature": "adjacent : V×V→Prop",
    "description": "True exactly when {u,v}∈E; symmetric and false for u=v.",
    "concept": "urn:csabs:concept/AcyclicGraph",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "True exactly when {u,v}∈E; symmetric and false for u=v.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AcyclicGraph-neighbors",
    "type": "Operation",
    "name": "neighbors",
    "signature": "neighbors : V→P(V)",
    "description": "neighbors(v)={u∈V | {u,v}∈E}.",
    "concept": "urn:csabs:concept/AcyclicGraph",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "neighbors(v)={u∈V | {u,v}∈E}.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AcyclicGraph-reachable",
    "type": "Operation",
    "name": "reachable",
    "signature": "reachable : V×V→Prop",
    "description": "True iff a finite path connects the vertices; reflexive via the empty path.",
    "concept": "urn:csabs:concept/AcyclicGraph",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "True iff a finite path connects the vertices; reflexive via the empty path.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AcyclicGraph-paths",
    "type": "Operation",
    "name": "paths",
    "signature": "paths : V×V→P(List(V))",
    "description": "All simple paths with the specified endpoints; zero-length path allowed when endpoints coincide.",
    "concept": "urn:csabs:concept/AcyclicGraph",
    "precondition": "Inputs belong to the displayed carriers.",
    "postcondition": "All simple paths with the specified endpoints; zero-length path allowed when endpoints coincide.",
    "totality": "Total on the stated typed domain; predicates and sets are mathematical, with no algorithmic complexity claim.",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AcyclicGraph-simple-undirected",
    "type": "Axiom",
    "name": "simple-undirected",
    "statement": "The underlying graph is finite, simple and undirected.",
    "description": "The underlying graph is finite, simple and undirected.",
    "formalStatement": "V finite; Adj⊆V×V; Adj(u,v)⇔Adj(v,u); ¬Adj(v,v); E is a set of unordered pairs.",
    "assumptions": [
      "Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten."
    ],
    "appliesTo": [
      "urn:csabs:concept/AcyclicGraph"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/AcyclicGraph-no-cycle",
    "type": "Axiom",
    "name": "no-cycle",
    "statement": "No simple undirected cycle exists.",
    "description": "No simple undirected cycle exists.",
    "formalStatement": "∀v∈V, ∀c:Walk(v,v), ¬IsCycle(c).",
    "assumptions": [
      "Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten."
    ],
    "appliesTo": [
      "urn:csabs:concept/AcyclicGraph"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Definition adapted to the explicitly stated catalog carrier and operations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/AcyclicGraph-path-model-satisfaction",
    "type": "Theorem",
    "name": "path-model-satisfaction",
    "statement": "Every finite path graph is a forest, including the empty graph at n=0.",
    "description": "Every finite path graph is a forest, including the empty graph at n=0.",
    "formalStatement": "∀n∈ℕ, pathGraph(n) is a finite simple acyclic undirected graph on Fin(n).",
    "assumptions": [
      "Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten."
    ],
    "appliesTo": [
      "urn:csabs:concept/AcyclicGraph"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Derived from the directly linked defining premises; Construct pathForest n using the Mathlib theorem isAcyclic_pathGraph. n=0 covers the empty carrier; n=2 includes two distinct adjacent vertices, so this family is not restricted to edgeless models.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AcyclicGraph-simple-undirected",
      "urn:csabs:axiom/AcyclicGraph-no-cycle"
    ],
    "proofSketch": "Construct pathForest n using the Mathlib theorem isAcyclic_pathGraph. n=0 covers the empty carrier; n=2 includes two distinct adjacent vertices, so this family is not restricted to edgeless models.",
    "leanFormulation": "∀ n : Nat, (Catalog.pathForest n).graph.IsAcyclic",
    "formulationSource": "urn:csabs:source/local-lean-KleeneForests",
    "formulationLocator": "Catalog.forest_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AcyclicGraph-no-cycle\": \"Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.\", \"urn:csabs:axiom/AcyclicGraph-simple-undirected\": \"Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.\"}"
  },
  {
    "id": "urn:csabs:theorem/AcyclicGraph-path-uniqueness",
    "type": "Theorem",
    "name": "path-uniqueness",
    "statement": "Between fixed vertices of a forest there is at most one simple path.",
    "description": "Between fixed vertices of a forest there is at most one simple path.",
    "formalStatement": "∀v,w∈V, ∀p,q∈Paths(v,w), p=q.",
    "assumptions": [
      "Finite vertex set V, possibly empty, with exact vertex identities; edges are unordered distinct pairs, without loops or parallel edges. A cycle is a closed walk of length at least three with no repeated vertices except its endpoints. Immediate backtracking along an edge is not a cycle. Connectivity and roots are not required; isolated vertices are allowed. Paths are finite simple paths, including the length-zero path at a vertex. This is undirected acyclicity; a DAG may have an undirected cycle after directions are forgotten."
    ],
    "appliesTo": [
      "urn:csabs:concept/AcyclicGraph"
    ],
    "reviewStatus": "Editorial statement; consult the separate Lean witness binding for exact proof scope.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-acyclic-pinned"
    ],
    "sourceLocator": "Mathlib/Combinatorics/SimpleGraph/Acyclic.lean: IsAcyclic, isAcyclic_bot, isAcyclic_iff_subsingleton_path, isAcyclic_pathGraph; pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679",
    "sourceNote": "Derived from the directly linked defining premises; Apply Mathlib IsAcyclic.subsingleton_path; two distinct simple paths would produce a cycle. Disconnected pairs have no path; the conclusion asserts uniqueness, not existence.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/AcyclicGraph-simple-undirected",
      "urn:csabs:axiom/AcyclicGraph-no-cycle"
    ],
    "proofSketch": "Apply Mathlib IsAcyclic.subsingleton_path; two distinct simple paths would produce a cycle. Disconnected pairs have no path; the conclusion asserts uniqueness, not existence.",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.AcyclicGraph V) (v w : V) (p q : f.graph.Path v w), p = q",
    "formulationSource": "urn:csabs:source/local-lean-KleeneForests",
    "formulationLocator": "Catalog.forest_path_unique",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.",
    "leanModelLimitations": "Proves the displayed Lean proposition only; semantic correspondence is reviewed metadata. No software implementation correctness or deductive-system completeness is asserted.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/AcyclicGraph-no-cycle\": \"Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.\", \"urn:csabs:axiom/AcyclicGraph-simple-undirected\": \"Direct defining premise interpreted using Finite V via Fintype V; graph : SimpleGraph V supplies symmetric irreflexive adjacency; graph.IsAcyclic excludes cyclic walks. Exact vertex equality.\"}"
  }
]
```
<!-- graph-record:end -->
