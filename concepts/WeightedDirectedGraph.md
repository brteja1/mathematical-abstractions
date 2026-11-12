# Finite real-weighted directed multigraph

A directed multigraph assigning an exact real weight to each edge identity.

**Notation:** (V,E,s,t,w:E→ℝ)

**Stable ID:** `urn:csabs:concept/WeightedDirectedGraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Finite directed multigraph with edge identities](DirectedMultigraph.md), [Exact real number](RealNumber.md)

**Specializes:** [Finite directed multigraph with edge identities](DirectedMultigraph.md)

## Mathematical formulation

A weighted finite directed multigraph adds w:E→ℝ to (V,E,s,t). The weight of an edge list [e₁,…,e\_k] is Σ\_i w(e\_i), including 0 for the empty list. Path composability is a separate predicate.

**Lean formulation** (in its source module context):

```lean
structure WeightedDirectedGraph (V : Type u) (E : Type v) [Fintype V] [Fintype E]
    extends DirectedMultigraph V E where
  weight : E → Real
```

**Source:** [`Catalog.WeightedDirectedGraph`](../lean/Catalog/GraphData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** (V,E,s,t,w:E→ℝ). Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** (V,E,s,t) is a finite directed multigraph; w:E→ℝ is total; pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)

**basisKind:** extensional-structural-definition

**basisScope:** Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.

**specializationNote:** Keep V,E,s,t and forget the weight function. Weights are attached to edge identities, including separate parallel edges.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-WeightedDirectedGraph-weight"></a>

### weight

`urn:csabs:operation/WeightedDirectedGraph-weight`

**signature:** weight : E→ℝ

**description:** Returns the fixed edge weight.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the fixed edge weight.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-WeightedDirectedGraph-walk"></a>

### walk

`urn:csabs:operation/WeightedDirectedGraph-walk`

**signature:** walk : V×Seq(E)×V→Prop

**description:** Uses the same endpoint walk predicate as DirectedMultigraph.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Uses the same endpoint walk predicate as DirectedMultigraph.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-WeightedDirectedGraph-path-weight"></a>

### path-weight

`urn:csabs:operation/WeightedDirectedGraph-path-weight`

**signature:** pathWeight : Seq(E)→ℝ

**description:** Sum of the edge weights, counting repeated traversals.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Sum of the edge weights, counting repeated traversals.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-WeightedDirectedGraph-weighted-carrier"></a>

### weighted-carrier

`urn:csabs:axiom/WeightedDirectedGraph-weighted-carrier`

**statement:** Defining requirement: (V,E,s,t) is a finite directed multigraph; w:E→ℝ is total

**formalStatement:** (V,E,s,t) is a finite directed multigraph; w:E→ℝ is total

**assumptions:** Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-WeightedDirectedGraph-sum-equations"></a>

### sum-equations

`urn:csabs:axiom/WeightedDirectedGraph-sum-equations`

**statement:** Defining requirement: pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)

**formalStatement:** pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)

**assumptions:** Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-WeightedDirectedGraph-weight-concatenation"></a>

### weight-concatenation

`urn:csabs:law/WeightedDirectedGraph-weight-concatenation`

**statement:** pathWeight(p++q)=pathWeight(p)+pathWeight(q)

**formalStatement:** pathWeight(p++q)=pathWeight(p)+pathWeight(q)

**assumptions:** Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [sum-equations](WeightedDirectedGraph.md#node-urn-csabs-axiom-WeightedDirectedGraph-sum-equations)

**proofSketch:** Induct on p; the empty case uses additive zero, and the cons case uses real addition associativity.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V E : Type} [Fintype V] [Fintype E] (g : Catalog.WeightedDirectedGraph V E) (p q : List E), g.pathWeight (p ++ q) = g.pathWeight p + g.pathWeight q
```

**Source:** [`Catalog.GraphDataProofs.path_weight_append`](../lean/Catalog/GraphData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Real weights are exact; pathWeight is the List sum after mapping weight. List append is sequence concatenation. The identity holds for all edge lists, without requiring walk validity or nonnegative weights.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/WeightedDirectedGraph-sum-equations": "Interpreted premise: pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p). Real weights are exact; pathWeight is the List sum after mapping weight. List append is sequence concatenation. The identity holds for all edge lists, without requiring walk validity or nonnegative weights."
}
```

## Theorems

<a id="node-urn-csabs-theorem-WeightedDirectedGraph-negative-loop-unbounded"></a>

### negative-loop-unbounded

`urn:csabs:theorem/WeightedDirectedGraph-negative-loop-unbounded`

**statement:** If s(e)=t(e)=v and w(e)<0, walk weights from v to v have no lower bound

**formalStatement:** If s(e)=t(e)=v and w(e)<0, walk weights from v to v have no lower bound

**assumptions:** Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [weighted-carrier](WeightedDirectedGraph.md#node-urn-csabs-axiom-WeightedDirectedGraph-weighted-carrier); [sum-equations](WeightedDirectedGraph.md#node-urn-csabs-axiom-WeightedDirectedGraph-sum-equations); [walk-equations](DirectedMultigraph.md#node-urn-csabs-axiom-DirectedMultigraph-walk-equations)

**proofSketch:** Traversing e n times is a valid closed walk of weight n·w(e); negative multiples are unbounded below in ℝ.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Algebra/Order/Archimedean/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/WeightedDirectedGraph",
    "type": "Concept",
    "shortForm": "WeightedDirectedGraph",
    "fullName": "Finite real-weighted directed multigraph",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A directed multigraph assigning an exact real weight to each edge identity.",
    "notation": "(V,E,s,t,w:E→ℝ)",
    "requiresConcept": [
      "urn:csabs:concept/DirectedMultigraph",
      "urn:csabs:concept/RealNumber"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/WeightedDirectedGraph-weight",
      "urn:csabs:operation/WeightedDirectedGraph-walk",
      "urn:csabs:operation/WeightedDirectedGraph-path-weight"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/WeightedDirectedGraph-weighted-carrier",
      "urn:csabs:axiom/WeightedDirectedGraph-sum-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/WeightedDirectedGraph-weight-concatenation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/WeightedDirectedGraph-negative-loop-unbounded"
    ],
    "axiomBasis": "(V,E,s,t) is a finite directed multigraph; w:E→ℝ is total; pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DirectedMultigraph"
    ],
    "specializationNote": "Keep V,E,s,t and forget the weight function. Weights are attached to edge identities, including separate parallel edges.",
    "leanFormulation": "structure WeightedDirectedGraph (V : Type u) (E : Type v) [Fintype V] [Fintype E]\n    extends DirectedMultigraph V E where\n  weight : E → Real",
    "formulationSource": "urn:csabs:source/local-lean-GraphData",
    "formulationLocator": "Catalog.WeightedDirectedGraph",
    "formulationScope": "model",
    "leanModelMapping": "(V,E,s,t,w:E→ℝ). Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A weighted finite directed multigraph adds w:E→ℝ to (V,E,s,t). The weight of an edge list [e₁,…,e_k] is Σ_i w(e_i), including 0 for the empty list. Path composability is a separate predicate."
  },
  {
    "id": "urn:csabs:operation/WeightedDirectedGraph-weight",
    "type": "Operation",
    "name": "weight",
    "signature": "weight : E→ℝ",
    "description": "Returns the fixed edge weight.",
    "concept": "urn:csabs:concept/WeightedDirectedGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the fixed edge weight.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/WeightedDirectedGraph-walk",
    "type": "Operation",
    "name": "walk",
    "signature": "walk : V×Seq(E)×V→Prop",
    "description": "Uses the same endpoint walk predicate as DirectedMultigraph.",
    "concept": "urn:csabs:concept/WeightedDirectedGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Uses the same endpoint walk predicate as DirectedMultigraph.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/WeightedDirectedGraph-path-weight",
    "type": "Operation",
    "name": "path-weight",
    "signature": "pathWeight : Seq(E)→ℝ",
    "description": "Sum of the edge weights, counting repeated traversals.",
    "concept": "urn:csabs:concept/WeightedDirectedGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Sum of the edge weights, counting repeated traversals.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/WeightedDirectedGraph-weighted-carrier",
    "type": "Axiom",
    "name": "weighted-carrier",
    "statement": "Defining requirement: (V,E,s,t) is a finite directed multigraph; w:E→ℝ is total",
    "formalStatement": "(V,E,s,t) is a finite directed multigraph; w:E→ℝ is total",
    "assumptions": [
      "Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/WeightedDirectedGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/WeightedDirectedGraph-sum-equations",
    "type": "Axiom",
    "name": "sum-equations",
    "statement": "Defining requirement: pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)",
    "formalStatement": "pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p)",
    "assumptions": [
      "Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/WeightedDirectedGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/WeightedDirectedGraph-weight-concatenation",
    "type": "Law",
    "name": "weight-concatenation",
    "statement": "pathWeight(p++q)=pathWeight(p)+pathWeight(q)",
    "formalStatement": "pathWeight(p++q)=pathWeight(p)+pathWeight(q)",
    "assumptions": [
      "Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/WeightedDirectedGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/WeightedDirectedGraph-sum-equations"
    ],
    "proofSketch": "Induct on p; the empty case uses additive zero, and the cons case uses real addition associativity.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V E : Type} [Fintype V] [Fintype E] (g : Catalog.WeightedDirectedGraph V E) (p q : List E), g.pathWeight (p ++ q) = g.pathWeight p + g.pathWeight q",
    "formulationSource": "urn:csabs:source/local-lean-GraphData",
    "formulationLocator": "Catalog.GraphDataProofs.path_weight_append",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Real weights are exact; pathWeight is the List sum after mapping weight. List append is sequence concatenation. The identity holds for all edge lists, without requiring walk validity or nonnegative weights.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/WeightedDirectedGraph-sum-equations\": \"Interpreted premise: pathWeight([])=0; pathWeight(e::p)=w(e)+pathWeight(p). Real weights are exact; pathWeight is the List sum after mapping weight. List append is sequence concatenation. The identity holds for all edge lists, without requiring walk validity or nonnegative weights.\"}"
  },
  {
    "id": "urn:csabs:theorem/WeightedDirectedGraph-negative-loop-unbounded",
    "type": "Theorem",
    "name": "negative-loop-unbounded",
    "statement": "If s(e)=t(e)=v and w(e)<0, walk weights from v to v have no lower bound",
    "formalStatement": "If s(e)=t(e)=v and w(e)<0, walk weights from v to v have no lower bound",
    "assumptions": [
      "Negative, zero and positive weights allowed; parallel edges may have different weights. Weight of any finite edge list is defined even if not a walk. No shortest-path existence, nonnegative-weight or Dijkstra assumption.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/WeightedDirectedGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/WeightedDirectedGraph-weighted-carrier",
      "urn:csabs:axiom/WeightedDirectedGraph-sum-equations",
      "urn:csabs:axiom/DirectedMultigraph-walk-equations"
    ],
    "proofSketch": "Traversing e n times is a valid closed walk of weight n·w(e); negative multiples are unbounded below in ℝ.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core",
      "urn:csabs:source/mathlib-real-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights; Real.exists_isLUB, Real.isLUB_sSup, ConditionallyCompleteLinearOrder instance",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
