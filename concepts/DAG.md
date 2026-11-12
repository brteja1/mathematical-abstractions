# Directed acyclic graph

A directed graph with no directed cycle.

**Notation:** G=(V,E); ∀v∈V: (v,v)∉E+

**Stable ID:** `urn:csabs:concept/DAG`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Directed Graph](DirectedGraph.md)

**Specializes:** [Directed Graph](DirectedGraph.md)

## Backlinks

- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `specializationOf`

## Mathematical formulation

A DAG is (V,E) with E⊆V×V and ∀v,¬E⁺(v,v), where E⁺ is nonempty finite-path reachability. The declaration does not require finite V.

**Lean formulation** (in its source module context):

```lean
structure DAG (V : Type u) where
  edge : DirectedGraph V
  acyclic : ∀ v, ¬ Relation.TransGen edge v v
```

**Source:** [`Catalog.DAG`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Directed edge relation plus absence of positive TransGen cycles.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A directed graph with no directed cycle. Governing rules: The carrier and edge relation define a directed graph. There is no nonempty directed path from a vertex back to itself.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same directed vertex and edge sets; absence of directed cycles also excludes loops.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-DAG-basis-successors"></a>

### successors

`urn:csabs:operation/DAG-basis-successors`

**signature:** successors : V→𝒫(V)

**description:** Returns direct successors in the underlying directed graph.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DAG-underlying-digraph"></a>

### underlying-digraph

`urn:csabs:axiom/DAG-underlying-digraph`

**statement:** The carrier and edge relation define a directed graph.

**formalStatement:** E⊆V×V

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-DAG-acyclic"></a>

### acyclic

`urn:csabs:axiom/DAG-acyclic`

**statement:** There is no nonempty directed path from a vertex back to itself.

**formalStatement:** ∀v∈V:(v,v)∉E+

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-law-DAG-core"></a>

### law/DAG-core

`urn:csabs:law/DAG-core`

**statement:** Every finite DAG has a topological ordering.

**formalStatement:** V finite ⇒ ∃order: (u,v)∈E ⇒ u precedes v

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**proofSketch:** A finite nonempty DAG has a vertex of indegree zero, since repeatedly following predecessors otherwise creates a cycle. Remove it and induct.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [underlying-digraph](DAG.md#node-urn-csabs-axiom-DAG-underlying-digraph); [acyclic](DAG.md#node-urn-csabs-axiom-DAG-acyclic)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-DAG-positive-reach-irreflexive"></a>

### positive-reach-irreflexive

`urn:csabs:theorem/DAG-positive-reach-irreflexive`

**statement:** Positive reachability in a DAG is irreflexive and transitive.

**formalStatement:** ¬E+(v,v); E+(u,v)∧E+(v,w)⇒E+(u,w)

**proofSketch:** Irreflexivity is acyclicity; concatenation of positive paths gives transitivity.

**assumptions:** The explicit basis, carriers, and side conditions stated for DAG apply.

**dependsOn:** [underlying-digraph](DAG.md#node-urn-csabs-axiom-DAG-underlying-digraph); [acyclic](DAG.md#node-urn-csabs-axiom-DAG-acyclic)

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
    "id": "urn:csabs:concept/DAG",
    "type": "Concept",
    "shortForm": "DAG",
    "fullName": "Directed acyclic graph",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A directed graph with no directed cycle.",
    "notation": "G=(V,E); ∀v∈V: (v,v)∉E+",
    "hasOperation": [
      "urn:csabs:operation/DAG-basis-successors"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DAG-underlying-digraph",
      "urn:csabs:axiom/DAG-acyclic"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:law/DAG-core",
      "urn:csabs:theorem/DAG-positive-reach-irreflexive"
    ],
    "requiresConcept": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A directed graph with no directed cycle. Governing rules: The carrier and edge relation define a directed graph. There is no nonempty directed path from a vertex back to itself.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "specializationNote": "Keep the same directed vertex and edge sets; absence of directed cycles also excludes loops.",
    "leanFormulation": "structure DAG (V : Type u) where\n  edge : DirectedGraph V\n  acyclic : ∀ v, ¬ Relation.TransGen edge v v",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.DAG",
    "formulationScope": "model",
    "leanModelMapping": "Directed edge relation plus absence of positive TransGen cycles.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A DAG is (V,E) with E⊆V×V and ∀v,¬E⁺(v,v), where E⁺ is nonempty finite-path reachability. The declaration does not require finite V."
  },
  {
    "id": "urn:csabs:operation/DAG-basis-successors",
    "type": "Operation",
    "name": "successors",
    "signature": "successors : V→𝒫(V)",
    "description": "Returns direct successors in the underlying directed graph.",
    "concept": "urn:csabs:concept/DAG"
  },
  {
    "id": "urn:csabs:axiom/DAG-underlying-digraph",
    "type": "Axiom",
    "name": "underlying-digraph",
    "statement": "The carrier and edge relation define a directed graph.",
    "formalStatement": "E⊆V×V",
    "appliesTo": [
      "urn:csabs:concept/DAG"
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
    "id": "urn:csabs:axiom/DAG-acyclic",
    "type": "Axiom",
    "name": "acyclic",
    "statement": "There is no nonempty directed path from a vertex back to itself.",
    "formalStatement": "∀v∈V:(v,v)∉E+",
    "appliesTo": [
      "urn:csabs:concept/DAG"
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
    "id": "urn:csabs:law/DAG-core",
    "type": "Theorem",
    "statement": "Every finite DAG has a topological ordering.",
    "formalStatement": "V finite ⇒ ∃order: (u,v)∈E ⇒ u precedes v",
    "appliesTo": [
      "urn:csabs:concept/DAG"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "proofSketch": "A finite nonempty DAG has a vertex of indegree zero, since repeatedly following predecessors otherwise creates a cycle. Remove it and induct.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/DAG-underlying-digraph",
      "urn:csabs:axiom/DAG-acyclic"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/DAG-positive-reach-irreflexive",
    "type": "Theorem",
    "name": "positive-reach-irreflexive",
    "statement": "Positive reachability in a DAG is irreflexive and transitive.",
    "formalStatement": "¬E+(v,v); E+(u,v)∧E+(v,w)⇒E+(u,w)",
    "proofSketch": "Irreflexivity is acyclicity; concatenation of positive paths gives transitivity.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for DAG apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/DAG"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DAG-underlying-digraph",
      "urn:csabs:axiom/DAG-acyclic"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
