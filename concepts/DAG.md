# Directed acyclic graph

A directed graph with no directed cycle.

**Notation:** G=(V,E); ∀v∈V: (v,v)∉E+

**Stable ID:** `urn:csabs:concept/DAG`

**Categories:** Graph theory

**Kind:** Mathematical structure

**Prerequisites:** [Directed Graph](DirectedGraph.md)

**Specializes:** [Directed Graph](DirectedGraph.md)

## Backlinks

- [Finite acyclic undirected graph (forest)](AcyclicGraph.md) — `relatedConcept`
- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `requiresConcept`
- [Bayesian network (finite discrete variables)](BayesianNetwork.md) — `specializationOf`
- [Finite single-parent rooted forest](SingleParentForest.md) — `requiresConcept`
- [Finite single-parent rooted forest](SingleParentForest.md) — `specializationOf`

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

<a id="node-urn-csabs-theorem-DAG-reachability-partial-order"></a>

### reachability-partial-order

`urn:csabs:theorem/DAG-reachability-partial-order`

**statement:** Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.

**formalStatement:** Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.

**proofSketch:** A nontrivial mutual reachability pair gives a positive cycle, contradicting DAG acyclicity.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [acyclic](DAG.md#node-urn-csabs-axiom-DAG-acyclic)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.dag_reach_order

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} (g : Catalog.DAG V), (∀ a, Relation.ReflTransGen g.edge a a) ∧
    (∀ a b c, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b c →
      Relation.ReflTransGen g.edge a c) ∧
    (∀ a b, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b a → a = b)
```

**Source:** [`Catalog.dag_reach_order`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DAG-acyclic": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-DAG-topological-converse"></a>

### topological-converse

`urn:csabs:theorem/DAG-topological-converse`

**statement:** If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.

**formalStatement:** If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.

**proofSketch:** Lift each positive path into the strict order; a cycle contradicts irreflexivity.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [underlying-digraph](DAG.md#node-urn-csabs-axiom-DAG-underlying-digraph)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.topological_converse

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} (edge : V → V → Prop)
    (lt : V → V → Prop) (_irrefl : ∀ v, ¬ lt v v)
    (_trans : ∀ a b c, lt a b → lt b c → lt a c)
    (_respects : ∀ a b, edge a b → lt a b), ∀ v, ¬ Relation.TransGen edge v v
```

**Source:** [`Catalog.topological_converse`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DAG-underlying-digraph": "The underlying relation is the edge relation; the explicit strict transitive irreflexive respecting order is the theorem hypothesis, not assumed DAG acyclicity."
}
```

<a id="node-urn-csabs-theorem-DAG-all-linear-extensions"></a>

### all-linear-extensions

`urn:csabs:theorem/DAG-all-linear-extensions`

**statement:** a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.

**formalStatement:** a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.

**proofSketch:** Apply the general all-extensions separation theorem to the DAG reachability partial order.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [reachability-partial-order](DAG.md#node-urn-csabs-theorem-DAG-reachability-partial-order); [all-extensions-reflect-order](OrderLinearExtension.md#node-urn-csabs-theorem-OrderLinearExtension-all-extensions-reflect-order)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.dag_all_extensions

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} (g : Catalog.DAG V) (a b : V), Relation.ReflTransGen g.edge a b ↔
    ∀ s : V → V → Prop, IsLinearOrder V s → Relation.ReflTransGen g.edge ≤ s → s a b
```

**Source:** [`Catalog.dag_all_extensions`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:theorem/DAG-reachability-partial-order": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/OrderLinearExtension-all-extensions-reflect-order": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
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
      "urn:csabs:theorem/DAG-positive-reach-irreflexive",
      "urn:csabs:theorem/DAG-reachability-partial-order",
      "urn:csabs:theorem/DAG-topological-converse",
      "urn:csabs:theorem/DAG-all-linear-extensions"
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
  },
  {
    "id": "urn:csabs:theorem/DAG-reachability-partial-order",
    "type": "Theorem",
    "name": "reachability-partial-order",
    "statement": "Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.",
    "formalStatement": "Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.",
    "mathematicalFormulation": "Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric.",
    "proofSketch": "A nontrivial mutual reachability pair gives a positive cycle, contradicting DAG acyclicity.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/DAG"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DAG-acyclic"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.dag_reach_order",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} (g : Catalog.DAG V), (∀ a, Relation.ReflTransGen g.edge a a) ∧\n    (∀ a b c, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b c →\n      Relation.ReflTransGen g.edge a c) ∧\n    (∀ a b, Relation.ReflTransGen g.edge a b → Relation.ReflTransGen g.edge b a → a = b)",
    "leanModelMapping": "Reflexive-transitive DAG reachability is reflexive, transitive and antisymmetric. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DAG-acyclic\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.dag_reach_order"
  },
  {
    "id": "urn:csabs:theorem/DAG-topological-converse",
    "type": "Theorem",
    "name": "topological-converse",
    "statement": "If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.",
    "formalStatement": "If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.",
    "mathematicalFormulation": "If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle.",
    "proofSketch": "Lift each positive path into the strict order; a cycle contradicts irreflexivity.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/DAG"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DAG-underlying-digraph"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.topological_converse",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} (edge : V → V → Prop)\n    (lt : V → V → Prop) (_irrefl : ∀ v, ¬ lt v v)\n    (_trans : ∀ a b c, lt a b → lt b c → lt a c)\n    (_respects : ∀ a b, edge a b → lt a b), ∀ v, ¬ Relation.TransGen edge v v",
    "leanModelMapping": "If a strict transitive irreflexive order respects every edge, the edge relation has no positive cycle. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DAG-underlying-digraph\": \"The underlying relation is the edge relation; the explicit strict transitive irreflexive respecting order is the theorem hypothesis, not assumed DAG acyclicity.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.topological_converse"
  },
  {
    "id": "urn:csabs:theorem/DAG-all-linear-extensions",
    "type": "Theorem",
    "name": "all-linear-extensions",
    "statement": "a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.",
    "formalStatement": "a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.",
    "mathematicalFormulation": "a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability.",
    "proofSketch": "Apply the general all-extensions separation theorem to the DAG reachability partial order.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/DAG"
    ],
    "dependsOn": [
      "urn:csabs:theorem/DAG-reachability-partial-order",
      "urn:csabs:theorem/OrderLinearExtension-all-extensions-reflect-order"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen and TransGen; Order/Extension/Linear.lean: extend_partialOrder; Catalog.dag_all_extensions",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} (g : Catalog.DAG V) (a b : V), Relation.ReflTransGen g.edge a b ↔\n    ∀ s : V → V → Prop, IsLinearOrder V s → Relation.ReflTransGen g.edge ≤ s → s a b",
    "leanModelMapping": "a reaches b iff every linear extension of DAG reachability places a≤b. Quantification over all extensions is essential; one chosen order does not reflect reachability. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:theorem/DAG-reachability-partial-order\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/OrderLinearExtension-all-extensions-reflect-order\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.dag_all_extensions"
  }
]
```
<!-- graph-record:end -->
