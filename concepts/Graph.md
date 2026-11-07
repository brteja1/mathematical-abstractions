# Graph

A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant.

**Notation:** G=(V,E); E⊆{{u,v}:u,v∈V,u≠v}

**Stable ID:** `urn:csabs:concept/Graph`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Set](Set.md)

## Backlinks

- [Tree](Tree.md) — `requiresConcept`
- [Tree](Tree.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Selected presentation: A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant. Governing rules: A graph has a finite vertex set and edges are unordered two-element subsets. Adjacency means sharing an edge; it is symmetric and irreflexive in this variant.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

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
    "notation": "G=(V,E); E⊆{{u,v}:u,v∈V,u≠v}",
    "hasOperation": [
      "urn:csabs:operation/Graph-neighbors"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Graph-simple-finite",
      "urn:csabs:axiom/Graph-adjacency"
    ],
    "hasLaw": [
      "urn:csabs:law/Graph-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Graph-adjacency-symmetric"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite simple undirected graph consists of vertices and unordered pairs of distinct vertices as edges; loops and multiple edges are excluded in this variant. Governing rules: A graph has a finite vertex set and edges are unordered two-element subsets. Adjacency means sharing an edge; it is symmetric and irreflexive in this variant.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
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
    "id": "urn:csabs:axiom/Graph-simple-finite",
    "type": "Axiom",
    "name": "simple-finite",
    "statement": "A graph has a finite vertex set and edges are unordered two-element subsets.",
    "formalStatement": "V finite; E⊆{e⊆V:card(e)=2}",
    "appliesTo": [
      "urn:csabs:concept/Graph"
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
      "urn:csabs:concept/Graph"
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
  }
]
```
<!-- graph-record:end -->
