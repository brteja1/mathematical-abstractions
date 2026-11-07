# Tree

A nonempty finite connected acyclic simple undirected graph.

**Notation:** T=(V,E); connected(T) ∧ acyclic(T)

**Stable ID:** `urn:csabs:concept/Tree`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Graph](Graph.md)

**Specializes:** [Graph](Graph.md)

## Interface and scope

**axiomBasis:** Selected presentation: A nonempty connected acyclic simple undirected graph. Governing rules: This tree variant has a nonempty finite simple undirected underlying graph. Every pair of vertices is joined by a finite path. There is no simple undirected cycle.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same finite simple undirected graph; nonemptiness, connectivity and acyclicity are additional constraints.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-Tree-basis-neighbors"></a>

### neighbors

`urn:csabs:operation/Tree-basis-neighbors`

**signature:** neighbors : V→𝒫(V)

**description:** Returns the adjacent vertices in the underlying finite undirected graph.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Tree-underlying-graph"></a>

### underlying-graph

`urn:csabs:axiom/Tree-underlying-graph`

**statement:** This tree variant has a nonempty finite simple undirected underlying graph.

**formalStatement:** V finite ∧ V≠∅; E⊆{e⊆V:card(e)=2}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Tree-connected"></a>

### connected

`urn:csabs:axiom/Tree-connected`

**statement:** Every pair of vertices is joined by a finite path.

**formalStatement:** ∀u,v∈V:∃path u⇝v

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Tree-acyclic"></a>

### acyclic

`urn:csabs:axiom/Tree-acyclic`

**statement:** There is no simple undirected cycle.

**formalStatement:** No cycle v₀,…,vₖ=v₀ with k≥3 and v₀,…,vₖ₋₁ distinct

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-Tree-core"></a>

### law/Tree-core

`urn:csabs:law/Tree-core`

**statement:** A finite tree has exactly one fewer edge than vertices.

**formalStatement:** V finite ⇒ card(E)=card(V)−1

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**proofSketch:** Induct on vertex count: the one-vertex tree has no edges; removing a leaf and its incident edge preserves a tree.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [underlying-graph](Tree.md#node-urn-csabs-axiom-Tree-underlying-graph); [connected](Tree.md#node-urn-csabs-axiom-Tree-connected); [acyclic](Tree.md#node-urn-csabs-axiom-Tree-acyclic)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Tree-unique-simple-path"></a>

### unique-simple-path

`urn:csabs:theorem/Tree-unique-simple-path`

**statement:** There is exactly one simple path between any two vertices of a tree.

**formalStatement:** ∀u,v∈V ∃!simple path u⇝v

**proofSketch:** Connectivity gives a path, removable cycles give a simple one; two different simple paths would form a cycle.

**assumptions:** The explicit basis, carriers, and side conditions stated for Tree apply.

**dependsOn:** [underlying-graph](Tree.md#node-urn-csabs-axiom-Tree-underlying-graph); [connected](Tree.md#node-urn-csabs-axiom-Tree-connected); [acyclic](Tree.md#node-urn-csabs-axiom-Tree-acyclic)

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
    "id": "urn:csabs:concept/Tree",
    "type": "Concept",
    "shortForm": "Tree",
    "fullName": "Tree",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A nonempty finite connected acyclic simple undirected graph.",
    "notation": "T=(V,E); connected(T) ∧ acyclic(T)",
    "hasOperation": [
      "urn:csabs:operation/Tree-basis-neighbors"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Tree-underlying-graph",
      "urn:csabs:axiom/Tree-connected",
      "urn:csabs:axiom/Tree-acyclic"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/Tree-core",
      "urn:csabs:theorem/Tree-unique-simple-path"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Graph"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A nonempty connected acyclic simple undirected graph. Governing rules: This tree variant has a nonempty finite simple undirected underlying graph. Every pair of vertices is joined by a finite path. There is no simple undirected cycle.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Graph"
    ],
    "specializationNote": "Keep the same finite simple undirected graph; nonemptiness, connectivity and acyclicity are additional constraints."
  },
  {
    "id": "urn:csabs:operation/Tree-basis-neighbors",
    "type": "Operation",
    "name": "neighbors",
    "signature": "neighbors : V→𝒫(V)",
    "description": "Returns the adjacent vertices in the underlying finite undirected graph.",
    "concept": "urn:csabs:concept/Tree"
  },
  {
    "id": "urn:csabs:axiom/Tree-underlying-graph",
    "type": "Axiom",
    "name": "underlying-graph",
    "statement": "This tree variant has a nonempty finite simple undirected underlying graph.",
    "formalStatement": "V finite ∧ V≠∅; E⊆{e⊆V:card(e)=2}",
    "appliesTo": [
      "urn:csabs:concept/Tree"
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
    "id": "urn:csabs:axiom/Tree-connected",
    "type": "Axiom",
    "name": "connected",
    "statement": "Every pair of vertices is joined by a finite path.",
    "formalStatement": "∀u,v∈V:∃path u⇝v",
    "appliesTo": [
      "urn:csabs:concept/Tree"
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
    "id": "urn:csabs:axiom/Tree-acyclic",
    "type": "Axiom",
    "name": "acyclic",
    "statement": "There is no simple undirected cycle.",
    "formalStatement": "No cycle v₀,…,vₖ=v₀ with k≥3 and v₀,…,vₖ₋₁ distinct",
    "appliesTo": [
      "urn:csabs:concept/Tree"
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
    "id": "urn:csabs:law/Tree-core",
    "type": "Theorem",
    "statement": "A finite tree has exactly one fewer edge than vertices.",
    "formalStatement": "V finite ⇒ card(E)=card(V)−1",
    "appliesTo": [
      "urn:csabs:concept/Tree"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "proofSketch": "Induct on vertex count: the one-vertex tree has no edges; removing a leaf and its incident edge preserves a tree.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/Tree-underlying-graph",
      "urn:csabs:axiom/Tree-connected",
      "urn:csabs:axiom/Tree-acyclic"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Tree-unique-simple-path",
    "type": "Theorem",
    "name": "unique-simple-path",
    "statement": "There is exactly one simple path between any two vertices of a tree.",
    "formalStatement": "∀u,v∈V ∃!simple path u⇝v",
    "proofSketch": "Connectivity gives a path, removable cycles give a simple one; two different simple paths would form a cycle.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Tree apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Tree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Tree-underlying-graph",
      "urn:csabs:axiom/Tree-connected",
      "urn:csabs:axiom/Tree-acyclic"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
