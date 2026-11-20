# Finite single-parent rooted forest

A finite vertex carrier with a partial parent function whose upward chains are acyclic; each component has one root.

**Notation:** p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v).

**Stable ID:** `urn:csabs:concept/SingleParentForest`

**Categories:** Graph theory, Data structures → Tree structures

**Kind:** Mathematical structure

**Prerequisites:** [Directed acyclic graph](DAG.md)

**Specializes:** [Directed acyclic graph](DAG.md)

**Related concepts:** [Finite rooted undirected tree](RootedTree.md), [Finite ordered rose tree](RoseTree.md), [Single-inheritance class table and dynamic dispatch](ClassTable.md), [Partial function](PartialFunction.md)

## Backlinks

- [Finite acyclic undirected graph (forest)](AcyclicGraph.md) — `relatedConcept`
- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `relatedConcept`
- [Finite rooted undirected tree](RootedTree.md) — `relatedConcept`

## Mathematical formulation

p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v). V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.

**Lean formulation** (in its source module context):

```lean
structure SingleParentForest (V : Type u) [Fintype V] where
  parent : V → Option V
  acyclic : ∀ v, ¬ Relation.TransGen (fun x y => parent x = some y) v v
```

**Source:** [`Catalog.Programs.SingleParentForest`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** partial

**Interpretation:** Finite V, Option-valued parent and explicit absence of positive child-to-parent cycles. Equality is vertex equality.

**Limits:** No root-following implementation, unique-root proof or update algorithm; no dangling references by typing. No witnesses registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite typed partial parent function; induced child-to-parent edges; no positive directed cycles.

**basisKind:** extensional-structural-definition

**basisScope:** V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.

**specializationNote:** Take the same V and child-to-parent relation E(v,w) iff p(v)=Some(w). Acyclicity gives a DAG; finite carrier and at most one outgoing edge are added constraints.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SingleParentForest-parent"></a>

### parent

`urn:csabs:operation/SingleParentForest-parent`

**signature:** p : V → Option(V)

**description:** Return the unique parent, or None exactly at a root.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return the unique parent, or None exactly at a root.

**totality:** Total on the displayed typed domain.

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SingleParentForest-children"></a>

### children

`urn:csabs:operation/SingleParentForest-children`

**signature:** children : V → P(V)

**description:** children(v)={u | p(u)=Some(v)}.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** children(v)={u | p(u)=Some(v)}.

**totality:** Total on the displayed typed domain.

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SingleParentForest-roots"></a>

### roots

`urn:csabs:operation/SingleParentForest-roots`

**signature:** roots : Forest → P(V)

**description:** roots={v | p(v)=None}; empty forest has no roots.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** roots={v | p(v)=None}; empty forest has no roots.

**totality:** Total on the displayed typed domain.

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SingleParentForest-root-of"></a>

### root-of

`urn:csabs:operation/SingleParentForest-root-of`

**signature:** rootOf : V → V

**description:** Follow parent links to the unique terminal root; rootOf(r)=r for roots.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Follow parent links to the unique terminal root; rootOf(r)=r for roots.

**totality:** Total for vertices in a finite acyclic forest; no input vertices exist for the empty forest.

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SingleParentForest-parent-function"></a>

### parent-function

`urn:csabs:axiom/SingleParentForest-parent-function`

**description:** Defining rule for Finite single-parent rooted forest

**statement:** V finite; p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); roots={v | p(v)=None}.

**formalStatement:** V finite; p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); roots={v | p(v)=None}.

**assumptions:** V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-SingleParentForest-acyclic"></a>

### acyclic

`urn:csabs:axiom/SingleParentForest-acyclic`

**description:** Defining rule for Finite single-parent rooted forest

**statement:** For every v∈V, ¬E⁺(v,v), where E⁺ denotes positive-length finite reachability.

**formalStatement:** For every v∈V, ¬E⁺(v,v), where E⁺ denotes positive-length finite reachability.

**assumptions:** V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-SingleParentForest-unique-root"></a>

### unique-root

`urn:csabs:law/SingleParentForest-unique-root`

**description:** ∀v∈V, ∃!r∈roots, E*(v,r).

**statement:** ∀v∈V, ∃!r∈roots, E*(v,r).

**formalStatement:** ∀v∈V, ∃!r∈roots, E*(v,r).

**assumptions:** V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.

**dependsOn:** [parent-function](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-parent-function); [acyclic](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-acyclic)

**proofSketch:** A nonterminating parent walk on finite V repeats a vertex and yields a positive cycle. Thus it reaches a root. Since each step is determined by p, any two walks from v coincide until the first root, where no further step exists; endpoints are equal.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [OpenDSA: General Trees, Fall 2024](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all-0013bb43-a12f-4ab3-9b86-73b317f1e37e/fall-2024/Public_OpenDSA_F24/html/GenTreeIntro.html); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SingleParentForest",
    "type": "Concept",
    "shortForm": "SingleParentForest",
    "fullName": "Finite single-parent rooted forest",
    "definition": "A finite vertex carrier with a partial parent function whose upward chains are acyclic; each component has one root.",
    "notation": "p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v).",
    "category": [
      "urn:csabs:category/graphs",
      "urn:csabs:category/tree-structures"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.",
    "axiomBasis": "Finite typed partial parent function; induced child-to-parent edges; no positive directed cycles.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v). V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization.",
    "requiresConcept": [
      "urn:csabs:concept/DAG"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RootedTree",
      "urn:csabs:concept/RoseTree",
      "urn:csabs:concept/ClassTable",
      "urn:csabs:concept/PartialFunction"
    ],
    "hasOperation": [
      "urn:csabs:operation/SingleParentForest-parent",
      "urn:csabs:operation/SingleParentForest-children",
      "urn:csabs:operation/SingleParentForest-roots",
      "urn:csabs:operation/SingleParentForest-root-of"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SingleParentForest-parent-function",
      "urn:csabs:axiom/SingleParentForest-acyclic"
    ],
    "hasLaw": [
      "urn:csabs:law/SingleParentForest-unique-root"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DAG"
    ],
    "specializationNote": "Take the same V and child-to-parent relation E(v,w) iff p(v)=Some(w). Acyclicity gives a DAG; finite carrier and at most one outgoing edge are added constraints.",
    "leanFormulation": "structure SingleParentForest (V : Type u) [Fintype V] where\n  parent : V → Option V\n  acyclic : ∀ v, ¬ Relation.TransGen (fun x y => parent x = some y) v v",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.SingleParentForest",
    "formulationScope": "partial",
    "leanModelMapping": "Finite V, Option-valued parent and explicit absence of positive child-to-parent cycles. Equality is vertex equality.",
    "leanModelLimitations": "No root-following implementation, unique-root proof or update algorithm; no dangling references by typing. No witnesses registered."
  },
  {
    "id": "urn:csabs:operation/SingleParentForest-parent",
    "type": "Operation",
    "name": "parent",
    "signature": "p : V → Option(V)",
    "description": "Return the unique parent, or None exactly at a root.",
    "concept": "urn:csabs:concept/SingleParentForest",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return the unique parent, or None exactly at a root.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SingleParentForest-children",
    "type": "Operation",
    "name": "children",
    "signature": "children : V → P(V)",
    "description": "children(v)={u | p(u)=Some(v)}.",
    "concept": "urn:csabs:concept/SingleParentForest",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "children(v)={u | p(u)=Some(v)}.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SingleParentForest-roots",
    "type": "Operation",
    "name": "roots",
    "signature": "roots : Forest → P(V)",
    "description": "roots={v | p(v)=None}; empty forest has no roots.",
    "concept": "urn:csabs:concept/SingleParentForest",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "roots={v | p(v)=None}; empty forest has no roots.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SingleParentForest-root-of",
    "type": "Operation",
    "name": "root-of",
    "signature": "rootOf : V → V",
    "description": "Follow parent links to the unique terminal root; rootOf(r)=r for roots.",
    "concept": "urn:csabs:concept/SingleParentForest",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Follow parent links to the unique terminal root; rootOf(r)=r for roots.",
    "totality": "Total for vertices in a finite acyclic forest; no input vertices exist for the empty forest.",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SingleParentForest-parent-function",
    "type": "Axiom",
    "name": "parent-function",
    "description": "Defining rule for Finite single-parent rooted forest",
    "statement": "V finite; p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); roots={v | p(v)=None}.",
    "formalStatement": "V finite; p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); roots={v | p(v)=None}.",
    "assumptions": [
      "V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SingleParentForest-acyclic",
    "type": "Axiom",
    "name": "acyclic",
    "description": "Defining rule for Finite single-parent rooted forest",
    "statement": "For every v∈V, ¬E⁺(v,v), where E⁺ denotes positive-length finite reachability.",
    "formalStatement": "For every v∈V, ¬E⁺(v,v), where E⁺ denotes positive-length finite reachability.",
    "assumptions": [
      "V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/SingleParentForest-unique-root",
    "type": "Law",
    "name": "unique-root",
    "description": "∀v∈V, ∃!r∈roots, E*(v,r).",
    "statement": "∀v∈V, ∃!r∈roots, E*(v,r).",
    "formalStatement": "∀v∈V, ∃!r∈roots, E*(v,r).",
    "assumptions": [
      "V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-parent-function",
      "urn:csabs:axiom/SingleParentForest-acyclic"
    ],
    "proofSketch": "A nonterminating parent walk on finite V repeats a vertex and yields a positive cycle. Thus it reaches a root. Since each step is determined by p, any two walks from v coincide until the first root, where no further step exists; endpoints are equal.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/opendsa-general-trees-2024"
    ],
    "sourceLocator": "§18.1.1.1 General Tree Definitions and Terminology: forest, root and unique parent; adapted to unordered forests including the empty forest.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
