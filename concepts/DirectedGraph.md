# Directed Graph

A graph whose edges are ordered vertex pairs; loops are allowed unless excluded by an additional condition.

**Notation:** G=(V,E); E⊆V×V

**Stable ID:** `urn:csabs:concept/DirectedGraph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Binary relation](Relation.md)

## Backlinks

- [Directed acyclic graph](DAG.md) — `requiresConcept`
- [Directed acyclic graph](DAG.md) — `specializationOf`
- [Finite directed multigraph with edge identities](DirectedMultigraph.md) — `relatedConcept`
- [Markov chain (finite-state, discrete-time, time-homogeneous)](MarkovChain.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A graph whose edges are ordered vertex pairs; loops are allowed unless excluded by an additional condition. Governing rules: A directed graph is a vertex set with a binary edge relation. Reachability admits zero steps; positive reachability requires at least one.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-DirectedGraph-successors"></a>

### successors

`urn:csabs:operation/DirectedGraph-successors`

**signature:** succ : V→𝒫(V)

**description:** Returns direct outgoing neighbors.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DirectedGraph-typed-edges"></a>

### typed-edges

`urn:csabs:axiom/DirectedGraph-typed-edges`

**statement:** A directed graph is a vertex set with a binary edge relation.

**formalStatement:** E⊆V×V; succ(v)={w∈V:(v,w)∈E}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-DirectedGraph-reachability"></a>

### reachability

`urn:csabs:axiom/DirectedGraph-reachability`

**statement:** Reachability admits zero steps; positive reachability requires at least one.

**formalStatement:** Reach=E* = identity_V ∪ E+; E+={(v₀,vₙ): n≥1 and ∀i<n:(vᵢ,vᵢ₊₁)∈E}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-DirectedGraph-core"></a>

### law/DirectedGraph-core

`urn:csabs:law/DirectedGraph-core`

**statement:** Reachability by zero or more edges is reflexive and transitive.

**formalStatement:** Reach=E*

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [typed-edges](DirectedGraph.md#node-urn-csabs-axiom-DirectedGraph-typed-edges); [reachability](DirectedGraph.md#node-urn-csabs-axiom-DirectedGraph-reachability)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-DirectedGraph-reachability-transitive"></a>

### reachability-transitive

`urn:csabs:theorem/DirectedGraph-reachability-transitive`

**statement:** Finite path reachability is transitive.

**formalStatement:** Reach(u,v)∧Reach(v,w)⇒Reach(u,w)

**proofSketch:** Concatenate the two finite paths, allowing either to have zero length.

**assumptions:** The explicit basis, carriers, and side conditions stated for DirectedGraph apply.

**dependsOn:** [typed-edges](DirectedGraph.md#node-urn-csabs-axiom-DirectedGraph-typed-edges); [reachability](DirectedGraph.md#node-urn-csabs-axiom-DirectedGraph-reachability)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DirectedGraph",
    "type": "Concept",
    "shortForm": "DirectedGraph",
    "fullName": "Directed Graph",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A graph whose edges are ordered vertex pairs; loops are allowed unless excluded by an additional condition.",
    "notation": "G=(V,E); E⊆V×V",
    "hasOperation": [
      "urn:csabs:operation/DirectedGraph-successors"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DirectedGraph-typed-edges",
      "urn:csabs:axiom/DirectedGraph-reachability"
    ],
    "hasLaw": [
      "urn:csabs:law/DirectedGraph-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DirectedGraph-reachability-transitive"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A graph whose edges are ordered vertex pairs; loops are allowed unless excluded by an additional condition. Governing rules: A directed graph is a vertex set with a binary edge relation. Reachability admits zero steps; positive reachability requires at least one.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/DirectedGraph-successors",
    "type": "Operation",
    "name": "successors",
    "signature": "succ : V→𝒫(V)",
    "description": "Returns direct outgoing neighbors.",
    "concept": "urn:csabs:concept/DirectedGraph"
  },
  {
    "id": "urn:csabs:axiom/DirectedGraph-typed-edges",
    "type": "Axiom",
    "name": "typed-edges",
    "statement": "A directed graph is a vertex set with a binary edge relation.",
    "formalStatement": "E⊆V×V; succ(v)={w∈V:(v,w)∈E}",
    "appliesTo": [
      "urn:csabs:concept/DirectedGraph"
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
    "id": "urn:csabs:axiom/DirectedGraph-reachability",
    "type": "Axiom",
    "name": "reachability",
    "statement": "Reachability admits zero steps; positive reachability requires at least one.",
    "formalStatement": "Reach=E* = identity_V ∪ E+; E+={(v₀,vₙ): n≥1 and ∀i<n:(vᵢ,vᵢ₊₁)∈E}",
    "appliesTo": [
      "urn:csabs:concept/DirectedGraph"
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
    "id": "urn:csabs:law/DirectedGraph-core",
    "type": "Law",
    "statement": "Reachability by zero or more edges is reflexive and transitive.",
    "formalStatement": "Reach=E*",
    "appliesTo": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/DirectedGraph-typed-edges",
      "urn:csabs:axiom/DirectedGraph-reachability"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/DirectedGraph-reachability-transitive",
    "type": "Theorem",
    "name": "reachability-transitive",
    "statement": "Finite path reachability is transitive.",
    "formalStatement": "Reach(u,v)∧Reach(v,w)⇒Reach(u,w)",
    "proofSketch": "Concatenate the two finite paths, allowing either to have zero length.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for DirectedGraph apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DirectedGraph-typed-edges",
      "urn:csabs:axiom/DirectedGraph-reachability"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
