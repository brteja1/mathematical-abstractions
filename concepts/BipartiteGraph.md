# Finite simple graph with chosen bipartition

A finite simple undirected graph with a designated Boolean color for each vertex such that adjacent vertices have different colors.

**Notation:** (G,c:V→Bool), Adj(u,v)⇒c(u)≠c(v)

**Stable ID:** `urn:csabs:concept/BipartiteGraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Graph](Graph.md), [Two-valued Boolean type](BooleanType.md)

**Specializes:** [Graph](Graph.md)

## Interface and scope

**axiomBasis:** Adj is symmetric and irreflexive on finite V; ∀u,v, Adj(u,v)⇒c(u)≠c(v); side(b)={v∈V | c(v)=b}

**basisKind:** extensional-structural-definition

**basisScope:** The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.

**basisInstantiation:** Reuse Graph rules with the same finite V, two-element undirected edges and adjacent=adj. Boolean coloring covers all V, including isolated vertices; sides are the two color fibers.

**specializationNote:** Forget c and keep the same finite simple undirected adjacency. Proper coloring is an additional explicit invariant; bipartition sides may be empty.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BipartiteGraph-color"></a>

### color

`urn:csabs:operation/BipartiteGraph-color`

**signature:** color : V→Bool

**description:** Returns the designated side.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the designated side.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BipartiteGraph-adjacent"></a>

### adjacent

`urn:csabs:operation/BipartiteGraph-adjacent`

**signature:** adjacent : V×V→Prop

**description:** The underlying simple undirected adjacency.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** The underlying simple undirected adjacency.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BipartiteGraph-side"></a>

### side

`urn:csabs:operation/BipartiteGraph-side`

**signature:** side : Bool→FinSet(V)

**description:** side(b)={v | color(v)=b}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** side(b)={v | color(v)=b}.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

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

<a id="node-urn-csabs-axiom-BipartiteGraph-proper-coloring"></a>

### proper-coloring

`urn:csabs:axiom/BipartiteGraph-proper-coloring`

**statement:** Defining requirement: ∀u,v, Adj(u,v)⇒c(u)≠c(v)

**formalStatement:** ∀u,v, Adj(u,v)⇒c(u)≠c(v)

**assumptions:** The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BipartiteGraph-sides"></a>

### sides

`urn:csabs:axiom/BipartiteGraph-sides`

**statement:** Defining requirement: side(b)={v∈V | c(v)=b}

**formalStatement:** side(b)={v∈V | c(v)=b}

**assumptions:** The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-BipartiteGraph-adjacent-colors"></a>

### adjacent-colors

`urn:csabs:law/BipartiteGraph-adjacent-colors`

**statement:** Adj(u,v)⇒c(u)≠c(v)

**formalStatement:** Adj(u,v)⇒c(u)≠c(v)

**assumptions:** The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [proper-coloring](BipartiteGraph.md#node-urn-csabs-axiom-BipartiteGraph-proper-coloring)

**proofSketch:** Apply the proper-coloring invariant.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-BipartiteGraph-sides-partition"></a>

### sides-partition

`urn:csabs:theorem/BipartiteGraph-sides-partition`

**statement:** side(false)∩side(true)=∅ ∧ side(false)∪side(true)=V

**formalStatement:** side(false)∩side(true)=∅ ∧ side(false)∪side(true)=V

**assumptions:** The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [sides](BipartiteGraph.md#node-urn-csabs-axiom-BipartiteGraph-sides); [enumeration](BooleanType.md#node-urn-csabs-axiom-BooleanType-enumeration)

**proofSketch:** Every Boolean color is exactly one of the two distinct enumeration values.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Combinatorics/SimpleGraph/Bipartite.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/SimpleGraph/Bipartite.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** SimpleGraph bipartite graphs, bipartitions and two-colorability

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BipartiteGraph",
    "type": "Concept",
    "shortForm": "BipartiteGraph",
    "fullName": "Finite simple graph with chosen bipartition",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A finite simple undirected graph with a designated Boolean color for each vertex such that adjacent vertices have different colors.",
    "notation": "(G,c:V→Bool), Adj(u,v)⇒c(u)≠c(v)",
    "requiresConcept": [
      "urn:csabs:concept/Graph",
      "urn:csabs:concept/BooleanType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/BipartiteGraph-color",
      "urn:csabs:operation/BipartiteGraph-adjacent",
      "urn:csabs:operation/BipartiteGraph-side"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Graph-simple-finite",
      "urn:csabs:axiom/Graph-adjacency",
      "urn:csabs:axiom/BipartiteGraph-proper-coloring",
      "urn:csabs:axiom/BipartiteGraph-sides"
    ],
    "hasLaw": [
      "urn:csabs:law/BipartiteGraph-adjacent-colors"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BipartiteGraph-sides-partition"
    ],
    "axiomBasis": "Adj is symmetric and irreflexive on finite V; ∀u,v, Adj(u,v)⇒c(u)≠c(v); side(b)={v∈V | c(v)=b}",
    "basisKind": "extensional-structural-definition",
    "basisScope": "The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Graph"
    ],
    "specializationNote": "Forget c and keep the same finite simple undirected adjacency. Proper coloring is an additional explicit invariant; bipartition sides may be empty.",
    "basisInstantiation": "Reuse Graph rules with the same finite V, two-element undirected edges and adjacent=adj. Boolean coloring covers all V, including isolated vertices; sides are the two color fibers."
  },
  {
    "id": "urn:csabs:operation/BipartiteGraph-color",
    "type": "Operation",
    "name": "color",
    "signature": "color : V→Bool",
    "description": "Returns the designated side.",
    "concept": "urn:csabs:concept/BipartiteGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the designated side.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BipartiteGraph-adjacent",
    "type": "Operation",
    "name": "adjacent",
    "signature": "adjacent : V×V→Prop",
    "description": "The underlying simple undirected adjacency.",
    "concept": "urn:csabs:concept/BipartiteGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "The underlying simple undirected adjacency.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BipartiteGraph-side",
    "type": "Operation",
    "name": "side",
    "signature": "side : Bool→FinSet(V)",
    "description": "side(b)={v | color(v)=b}.",
    "concept": "urn:csabs:concept/BipartiteGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "side(b)={v | color(v)=b}.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Graph-simple-finite",
    "type": "Axiom",
    "name": "simple-finite",
    "statement": "A graph has a finite vertex set and edges are unordered two-element subsets.",
    "formalStatement": "V finite; E⊆{e⊆V:card(e)=2}",
    "appliesTo": [
      "urn:csabs:concept/Graph",
      "urn:csabs:concept/BipartiteGraph"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Graph-adjacency",
    "type": "Axiom",
    "name": "adjacency",
    "statement": "Adjacency means sharing an edge; it is symmetric and irreflexive in this variant.",
    "formalStatement": "adj(u,v) iff {u,v}∈E; N(u)={v∈V:adj(u,v)}",
    "appliesTo": [
      "urn:csabs:concept/Graph",
      "urn:csabs:concept/BipartiteGraph"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/BipartiteGraph-proper-coloring",
    "type": "Axiom",
    "name": "proper-coloring",
    "statement": "Defining requirement: ∀u,v, Adj(u,v)⇒c(u)≠c(v)",
    "formalStatement": "∀u,v, Adj(u,v)⇒c(u)≠c(v)",
    "assumptions": [
      "The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BipartiteGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BipartiteGraph-sides",
    "type": "Axiom",
    "name": "sides",
    "statement": "Defining requirement: side(b)={v∈V | c(v)=b}",
    "formalStatement": "side(b)={v∈V | c(v)=b}",
    "assumptions": [
      "The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BipartiteGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/BipartiteGraph-adjacent-colors",
    "type": "Law",
    "name": "adjacent-colors",
    "statement": "Adj(u,v)⇒c(u)≠c(v)",
    "formalStatement": "Adj(u,v)⇒c(u)≠c(v)",
    "assumptions": [
      "The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BipartiteGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BipartiteGraph-proper-coloring"
    ],
    "proofSketch": "Apply the proper-coloring invariant.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BipartiteGraph-sides-partition",
    "type": "Theorem",
    "name": "sides-partition",
    "statement": "side(false)∩side(true)=∅ ∧ side(false)∪side(true)=V",
    "formalStatement": "side(false)∩side(true)=∅ ∧ side(false)∪side(true)=V",
    "assumptions": [
      "The chosen coloring is observable: swapping colors gives a possibly different value. Empty graph and empty color classes allowed. This is a bundled bipartition, not only the existential property of admitting one.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BipartiteGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BipartiteGraph-sides",
      "urn:csabs:axiom/BooleanType-enumeration"
    ],
    "proofSketch": "Every Boolean color is exactly one of the two distinct enumeration values.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-bipartite-core"
    ],
    "sourceLocator": "SimpleGraph bipartite graphs, bipartitions and two-colorability",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
