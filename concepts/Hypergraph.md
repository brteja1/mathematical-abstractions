# Finite simple undirected hypergraph

A finite set of vertices and a set of undirected hyperedges, each a vertex subset of cardinality at least two.

**Notation:** (V,H), H⊆𝒫(V), ∀e∈H, |e|≥2

**Stable ID:** `urn:csabs:concept/Hypergraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Finite set collection](FiniteSet.md), [Power set](PowerSet.md)

## Backlinks

- [Graph](Graph.md) — `specializationOf`

## Interface and scope

**axiomBasis:** V,H finite; every e∈H is a subset of V with |e|≥2; incident(v,e) ⇔ v∈e; degree(v)=|{e∈H | v∈e}|

**basisKind:** extensional-structural-definition

**basisScope:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Hypergraph-edges"></a>

### edges

`urn:csabs:operation/Hypergraph-edges`

**signature:** edges : Hypergraph(V)→FinSet(FinSet(V))

**description:** Returns H.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns H.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Hypergraph-incident"></a>

### incident

`urn:csabs:operation/Hypergraph-incident`

**signature:** incident : V×H→Prop

**description:** incident(v,e) iff v∈e.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** incident(v,e) iff v∈e.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Hypergraph-degree"></a>

### degree

`urn:csabs:operation/Hypergraph-degree`

**signature:** degree : Hypergraph(V)×V→ℕ

**description:** Number of e∈H containing v.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Number of e∈H containing v.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Hypergraph-hyperedges"></a>

### hyperedges

`urn:csabs:axiom/Hypergraph-hyperedges`

**statement:** Defining requirement: V,H finite; every e∈H is a subset of V with |e|≥2

**formalStatement:** V,H finite; every e∈H is a subset of V with |e|≥2

**assumptions:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Hypergraph-incidence"></a>

### incidence

`urn:csabs:axiom/Hypergraph-incidence`

**statement:** Defining requirement: incident(v,e) ⇔ v∈e

**formalStatement:** incident(v,e) ⇔ v∈e

**assumptions:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Hypergraph-degree-definition"></a>

### degree-definition

`urn:csabs:axiom/Hypergraph-degree-definition`

**statement:** Defining requirement: degree(v)=|{e∈H | v∈e}|

**formalStatement:** degree(v)=|{e∈H | v∈e}|

**assumptions:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Hypergraph-edge-nonempty"></a>

### edge-nonempty

`urn:csabs:law/Hypergraph-edge-nonempty`

**statement:** e∈H ⇒ e≠∅

**formalStatement:** e∈H ⇒ e≠∅

**assumptions:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [hyperedges](Hypergraph.md#node-urn-csabs-axiom-Hypergraph-hyperedges)

**proofSketch:** Its finite cardinality is at least two, hence positive.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-Hypergraph-handshake-incidence"></a>

### handshake-incidence

`urn:csabs:theorem/Hypergraph-handshake-incidence`

**statement:** Σv∈V degree(v)=Σe∈H |e|

**formalStatement:** Σv∈V degree(v)=Σe∈H |e|

**assumptions:** Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [hyperedges](Hypergraph.md#node-urn-csabs-axiom-Hypergraph-hyperedges); [incidence](Hypergraph.md#node-urn-csabs-axiom-Hypergraph-incidence); [degree-definition](Hypergraph.md#node-urn-csabs-axiom-Hypergraph-degree-definition)

**proofSketch:** Both sides count the same finite incidence pairs (v,e) with v∈e, grouped by vertex and edge respectively.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Paul E. Black: NIST Dictionary of Algorithms and Data Structures, hypergraph](https://xlinux.nist.gov/dads/HTML/hypergraph.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Definition and Formal Definition: undirected hyperedges containing at least two vertices

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Hypergraph",
    "type": "Concept",
    "shortForm": "Hypergraph",
    "fullName": "Finite simple undirected hypergraph",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A finite set of vertices and a set of undirected hyperedges, each a vertex subset of cardinality at least two.",
    "notation": "(V,H), H⊆𝒫(V), ∀e∈H, |e|≥2",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/PowerSet"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Hypergraph-edges",
      "urn:csabs:operation/Hypergraph-incident",
      "urn:csabs:operation/Hypergraph-degree"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Hypergraph-hyperedges",
      "urn:csabs:axiom/Hypergraph-incidence",
      "urn:csabs:axiom/Hypergraph-degree-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/Hypergraph-edge-nonempty"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Hypergraph-handshake-incidence"
    ],
    "axiomBasis": "V,H finite; every e∈H is a subset of V with |e|≥2; incident(v,e) ⇔ v∈e; degree(v)=|{e∈H | v∈e}|",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Hypergraph-edges",
    "type": "Operation",
    "name": "edges",
    "signature": "edges : Hypergraph(V)→FinSet(FinSet(V))",
    "description": "Returns H.",
    "concept": "urn:csabs:concept/Hypergraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns H.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Hypergraph-incident",
    "type": "Operation",
    "name": "incident",
    "signature": "incident : V×H→Prop",
    "description": "incident(v,e) iff v∈e.",
    "concept": "urn:csabs:concept/Hypergraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "incident(v,e) iff v∈e.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Hypergraph-degree",
    "type": "Operation",
    "name": "degree",
    "signature": "degree : Hypergraph(V)×V→ℕ",
    "description": "Number of e∈H containing v.",
    "concept": "urn:csabs:concept/Hypergraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Number of e∈H containing v.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Hypergraph-hyperedges",
    "type": "Axiom",
    "name": "hyperedges",
    "statement": "Defining requirement: V,H finite; every e∈H is a subset of V with |e|≥2",
    "formalStatement": "V,H finite; every e∈H is a subset of V with |e|≥2",
    "assumptions": [
      "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Hypergraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Hypergraph-incidence",
    "type": "Axiom",
    "name": "incidence",
    "statement": "Defining requirement: incident(v,e) ⇔ v∈e",
    "formalStatement": "incident(v,e) ⇔ v∈e",
    "assumptions": [
      "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Hypergraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Hypergraph-degree-definition",
    "type": "Axiom",
    "name": "degree-definition",
    "statement": "Defining requirement: degree(v)=|{e∈H | v∈e}|",
    "formalStatement": "degree(v)=|{e∈H | v∈e}|",
    "assumptions": [
      "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Hypergraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Hypergraph-edge-nonempty",
    "type": "Law",
    "name": "edge-nonempty",
    "statement": "e∈H ⇒ e≠∅",
    "formalStatement": "e∈H ⇒ e≠∅",
    "assumptions": [
      "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Hypergraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Hypergraph-hyperedges"
    ],
    "proofSketch": "Its finite cardinality is at least two, hence positive.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/Hypergraph-handshake-incidence",
    "type": "Theorem",
    "name": "handshake-incidence",
    "statement": "Σv∈V degree(v)=Σe∈H |e|",
    "formalStatement": "Σv∈V degree(v)=Σe∈H |e|",
    "assumptions": [
      "Selected NIST convention excludes empty and singleton edges. V and H may be empty. No parallel hyperedges, orientation, repeated incidence or edge identities beyond vertex subsets. Equality is literal finite-set equality.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Hypergraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Hypergraph-hyperedges",
      "urn:csabs:axiom/Hypergraph-incidence",
      "urn:csabs:axiom/Hypergraph-degree-definition"
    ],
    "proofSketch": "Both sides count the same finite incidence pairs (v,e) with v∈e, grouped by vertex and edge respectively.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/nist-hypergraph-core"
    ],
    "sourceLocator": "Definition and Formal Definition: undirected hyperedges containing at least two vertices",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
