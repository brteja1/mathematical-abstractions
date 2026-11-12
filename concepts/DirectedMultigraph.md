# Finite directed multigraph with edge identities

Finite vertex and edge carriers with source and target functions; different edge identities may share endpoints.

**Notation:** (V,E,s:E→V,t:E→V)

**Stable ID:** `urn:csabs:concept/DirectedMultigraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Finite carrier with exhaustive enumeration](FiniteType.md), [Total function](Function.md), [Finite sequence (List datatype)](Sequence.md)

**Related concepts:** [Directed Graph](DirectedGraph.md)

## Backlinks

- [Finite labelled property graph (single-valued profile)](PropertyGraph.md) — `requiresConcept`
- [Finite labelled property graph (single-valued profile)](PropertyGraph.md) — `specializationOf`
- [Finite real-weighted directed multigraph](WeightedDirectedGraph.md) — `requiresConcept`
- [Finite real-weighted directed multigraph](WeightedDirectedGraph.md) — `specializationOf`

## Mathematical formulation

A finite directed multigraph is (V,E,s,t) with source s:E→V and target t:E→V. Distinct edge identities may share endpoints and s(e)=t(e) is allowed.

**Lean formulation** (in its source module context):

```lean
structure DirectedMultigraph (V : Type u) (E : Type v) [Fintype V] [Fintype E] where
  source : E → V
  target : E → V
```

**Source:** [`Catalog.DirectedMultigraph`](../lean/Catalog/GraphData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** (V,E,s:E→V,t:E→V). Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e)); walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)

**basisKind:** extensional-structural-definition

**basisScope:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DirectedMultigraph-source"></a>

### source

`urn:csabs:operation/DirectedMultigraph-source`

**signature:** source : E→V

**description:** Returns edge source.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns edge source.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DirectedMultigraph-target"></a>

### target

`urn:csabs:operation/DirectedMultigraph-target`

**signature:** target : E→V

**description:** Returns edge target.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns edge target.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DirectedMultigraph-walk"></a>

### walk

`urn:csabs:operation/DirectedMultigraph-walk`

**signature:** walk : V×Seq(E)×V→Prop

**description:** walk(a,[],b) iff a=b; walk(a,e::p,b) iff s(e)=a and walk(t(e),p,b).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** walk(a,[],b) iff a=b; walk(a,e::p,b) iff s(e)=a and walk(t(e),p,b).

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DirectedMultigraph-endpoints"></a>

### endpoints

`urn:csabs:axiom/DirectedMultigraph-endpoints`

**statement:** Defining requirement: V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))

**formalStatement:** V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))

**assumptions:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DirectedMultigraph-walk-equations"></a>

### walk-equations

`urn:csabs:axiom/DirectedMultigraph-walk-equations`

**statement:** Defining requirement: walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)

**formalStatement:** walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)

**assumptions:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DirectedMultigraph-single-edge-walk"></a>

### single-edge-walk

`urn:csabs:law/DirectedMultigraph-single-edge-walk`

**statement:** ∀e:E, walk(s(e),[e],t(e))

**formalStatement:** ∀e:E, walk(s(e),[e],t(e))

**assumptions:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [walk-equations](DirectedMultigraph.md#node-urn-csabs-axiom-DirectedMultigraph-walk-equations)

**proofSketch:** Apply the nonempty walk equation and the empty walk equation, both with reflexive endpoints.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {V E : Type} [Fintype V] [Fintype E] (g : Catalog.DirectedMultigraph V E) (e : E), g.path (g.source e) [e] (g.target e)
```

**Source:** [`Catalog.GraphDataProofs.single_edge_path`](../lean/Catalog/GraphData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Catalog path is the graph walk predicate (not a simple path); finite List E retains edge identity and repeated traversals. The singleton follows the cons and empty walk equations.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DirectedMultigraph-walk-equations": "Interpreted premise: walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b). Catalog path is the graph walk predicate (not a simple path); finite List E retains edge identity and repeated traversals. The singleton follows the cons and empty walk equations."
}
```

## Theorems

<a id="node-urn-csabs-theorem-DirectedMultigraph-walk-concatenation"></a>

### walk-concatenation

`urn:csabs:theorem/DirectedMultigraph-walk-concatenation`

**statement:** walk(a,p,b) ∧ walk(b,q,c) ⇒ walk(a,p++q,c)

**formalStatement:** walk(a,p,b) ∧ walk(b,q,c) ⇒ walk(a,p++q,c)

**assumptions:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [walk-equations](DirectedMultigraph.md#node-urn-csabs-axiom-DirectedMultigraph-walk-equations)

**proofSketch:** Induct on p. The empty case substitutes a=b; the cons case keeps the first source and applies induction to its tail.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DirectedMultigraph",
    "type": "Concept",
    "shortForm": "DirectedMultigraph",
    "fullName": "Finite directed multigraph with edge identities",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Finite vertex and edge carriers with source and target functions; different edge identities may share endpoints.",
    "notation": "(V,E,s:E→V,t:E→V)",
    "requiresConcept": [
      "urn:csabs:concept/FiniteType",
      "urn:csabs:concept/Function",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "hasOperation": [
      "urn:csabs:operation/DirectedMultigraph-source",
      "urn:csabs:operation/DirectedMultigraph-target",
      "urn:csabs:operation/DirectedMultigraph-walk"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DirectedMultigraph-endpoints",
      "urn:csabs:axiom/DirectedMultigraph-walk-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/DirectedMultigraph-single-edge-walk"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DirectedMultigraph-walk-concatenation"
    ],
    "axiomBasis": "V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e)); walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure DirectedMultigraph (V : Type u) (E : Type v) [Fintype V] [Fintype E] where\n  source : E → V\n  target : E → V",
    "formulationSource": "urn:csabs:source/local-lean-GraphData",
    "formulationLocator": "Catalog.DirectedMultigraph",
    "formulationScope": "model",
    "leanModelMapping": "(V,E,s:E→V,t:E→V). Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A finite directed multigraph is (V,E,s,t) with source s:E→V and target t:E→V. Distinct edge identities may share endpoints and s(e)=t(e) is allowed."
  },
  {
    "id": "urn:csabs:operation/DirectedMultigraph-source",
    "type": "Operation",
    "name": "source",
    "signature": "source : E→V",
    "description": "Returns edge source.",
    "concept": "urn:csabs:concept/DirectedMultigraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns edge source.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DirectedMultigraph-target",
    "type": "Operation",
    "name": "target",
    "signature": "target : E→V",
    "description": "Returns edge target.",
    "concept": "urn:csabs:concept/DirectedMultigraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns edge target.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DirectedMultigraph-walk",
    "type": "Operation",
    "name": "walk",
    "signature": "walk : V×Seq(E)×V→Prop",
    "description": "walk(a,[],b) iff a=b; walk(a,e::p,b) iff s(e)=a and walk(t(e),p,b).",
    "concept": "urn:csabs:concept/DirectedMultigraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "walk(a,[],b) iff a=b; walk(a,e::p,b) iff s(e)=a and walk(t(e),p,b).",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DirectedMultigraph-endpoints",
    "type": "Axiom",
    "name": "endpoints",
    "statement": "Defining requirement: V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))",
    "formalStatement": "V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))",
    "assumptions": [
      "Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DirectedMultigraph",
      "urn:csabs:concept/PropertyGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DirectedMultigraph-walk-equations",
    "type": "Axiom",
    "name": "walk-equations",
    "statement": "Defining requirement: walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)",
    "formalStatement": "walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b)",
    "assumptions": [
      "Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DirectedMultigraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DirectedMultigraph-single-edge-walk",
    "type": "Law",
    "name": "single-edge-walk",
    "statement": "∀e:E, walk(s(e),[e],t(e))",
    "formalStatement": "∀e:E, walk(s(e),[e],t(e))",
    "assumptions": [
      "Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DirectedMultigraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DirectedMultigraph-walk-equations"
    ],
    "proofSketch": "Apply the nonempty walk equation and the empty walk equation, both with reflexive endpoints.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V E : Type} [Fintype V] [Fintype E] (g : Catalog.DirectedMultigraph V E) (e : E), g.path (g.source e) [e] (g.target e)",
    "formulationSource": "urn:csabs:source/local-lean-GraphData",
    "formulationLocator": "Catalog.GraphDataProofs.single_edge_path",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Catalog path is the graph walk predicate (not a simple path); finite List E retains edge identity and repeated traversals. The singleton follows the cons and empty walk equations.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DirectedMultigraph-walk-equations\": \"Interpreted premise: walk(a,[],b)⇔a=b; walk(a,e::p,b)⇔s(e)=a ∧ walk(t(e),p,b). Catalog path is the graph walk predicate (not a simple path); finite List E retains edge identity and repeated traversals. The singleton follows the cons and empty walk equations.\"}"
  },
  {
    "id": "urn:csabs:theorem/DirectedMultigraph-walk-concatenation",
    "type": "Theorem",
    "name": "walk-concatenation",
    "statement": "walk(a,p,b) ∧ walk(b,q,c) ⇒ walk(a,p++q,c)",
    "formalStatement": "walk(a,p,b) ∧ walk(b,q,c) ⇒ walk(a,p++q,c)",
    "assumptions": [
      "Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DirectedMultigraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DirectedMultigraph-walk-equations"
    ],
    "proofSketch": "Induct on p. The empty case substitutes a=b; the cons case keeps the first source and applies induction to its tail.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-quiver-core",
      "urn:csabs:source/ods-graphs-core"
    ],
    "sourceLocator": "Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
