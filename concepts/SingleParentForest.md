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

p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v). V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization. Utility profile: x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.

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

**axiomBasis:** Finite typed partial parent function; induced child-to-parent edges; no positive directed cycles. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

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

<a id="node-urn-csabs-operation-SingleParentForest-descendant-or-self"></a>

### descendant-or-self

`urn:csabs:operation/SingleParentForest-descendant-or-self`

**signature:** descendantOrSelf : V²→Prop

**description:** x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-axiom-SingleParentForest-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/SingleParentForest-utility-profile`

**statement:** x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.

**formalStatement:** descendantOrSelf : V²→Prop: x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-theorem-SingleParentForest-descendant-order"></a>

### descendant-order

`urn:csabs:theorem/SingleParentForest-descendant-order`

**statement:** Descendant-or-self, oriented from descendant to ancestor, is a partial order.

**formalStatement:** Descendant-or-self, oriented from descendant to ancestor, is a partial order.

**proofSketch:** Interpret parent edges as a DAG, then apply the reachability-order theorem.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-utility-profile); [acyclic](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-acyclic)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_descendant_order

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Descendant-or-self, oriented from descendant to ancestor, is a partial order.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V), (∀ a, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a a) ∧
    (∀ a b c, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a b →
      Relation.ReflTransGen (Catalog.Programs.parentEdge f) b c → Relation.ReflTransGen (Catalog.Programs.parentEdge f) a c) ∧
    (∀ a b, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a b →
      Relation.ReflTransGen (Catalog.Programs.parentEdge f) b a → a = b)
```

**Source:** [`Catalog.Programs.forest_descendant_order`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Descendant-or-self, oriented from descendant to ancestor, is a partial order. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SingleParentForest-acyclic": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/SingleParentForest-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-SingleParentForest-parent-chains-terminate"></a>

### parent-chains-terminate

`urn:csabs:theorem/SingleParentForest-parent-chains-terminate`

**statement:** The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.

**formalStatement:** The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.

**proofSketch:** The transitive parent closure is irreflexive and transitive on a finite carrier; use finite well-foundedness and relation inclusion.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-utility-profile); [parent-function](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-parent-function); [acyclic](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-acyclic)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_termination

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V), WellFounded (fun w v => Catalog.Programs.parentEdge f v w)
```

**Source:** [`Catalog.Programs.forest_termination`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SingleParentForest-acyclic": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/SingleParentForest-parent-function": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/SingleParentForest-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-SingleParentForest-root-existence"></a>

### root-existence

`urn:csabs:theorem/SingleParentForest-root-existence`

**statement:** Every vertex has a reachable root whose parent is none.

**formalStatement:** Every vertex has a reachable root whose parent is none.

**proofSketch:** Well-founded induction: stop at parent none; otherwise prepend the parent step to the parent’s root path.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-utility-profile); [parent-chains-terminate](SingleParentForest.md#node-urn-csabs-theorem-SingleParentForest-parent-chains-terminate)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_exists

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Every vertex has a reachable root whose parent is none.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V) (v : V), ∃ r, f.parent r = none ∧ Relation.ReflTransGen (Catalog.Programs.parentEdge f) v r
```

**Source:** [`Catalog.Programs.forest_root_exists`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Every vertex has a reachable root whose parent is none. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SingleParentForest-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/SingleParentForest-parent-chains-terminate": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-SingleParentForest-root-uniqueness"></a>

### root-uniqueness

`urn:csabs:theorem/SingleParentForest-root-uniqueness`

**statement:** Any two parent-none roots reachable from the same vertex are equal.

**formalStatement:** Any two parent-none roots reachable from the same vertex are equal.

**proofSketch:** Induct over one path; functional parenthood forces the first steps of both nonempty paths to coincide.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-utility-profile); [parent-function](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-parent-function)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_unique

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Any two parent-none roots reachable from the same vertex are equal.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V)
    (v r s : V) (_hr : f.parent r = none) (_hs : f.parent s = none)
    (_hvr : Relation.ReflTransGen (Catalog.Programs.parentEdge f) v r)
    (_hvs : Relation.ReflTransGen (Catalog.Programs.parentEdge f) v s), r = s
```

**Source:** [`Catalog.Programs.forest_root_unique`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Any two parent-none roots reachable from the same vertex are equal. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SingleParentForest-parent-function": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/SingleParentForest-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-SingleParentForest-rootOf-equation"></a>

### rootOf-equation

`urn:csabs:theorem/SingleParentForest-rootOf-equation`

**statement:** parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.

**formalStatement:** parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.

**proofSketch:** Choose the existence witness; uniqueness equates it to the root obtained by first following the parent.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](SingleParentForest.md#node-urn-csabs-axiom-SingleParentForest-utility-profile); [root-existence](SingleParentForest.md#node-urn-csabs-theorem-SingleParentForest-root-existence); [root-uniqueness](SingleParentForest.md#node-urn-csabs-theorem-SingleParentForest-root-uniqueness)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_equation

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.

**Lean formulation** (in its source module context):

```lean
∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V) (v : V), f.parent (Catalog.Programs.forestRootOf f v) = none ∧
    Relation.ReflTransGen (Catalog.Programs.parentEdge f) v (Catalog.Programs.forestRootOf f v) ∧
    (∀ w, f.parent v = some w → Catalog.Programs.forestRootOf f v = Catalog.Programs.forestRootOf f w) ∧
    (f.parent v = none → Catalog.Programs.forestRootOf f v = v)
```

**Source:** [`Catalog.Programs.forest_root_equation`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated. The root case fixes v itself.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SingleParentForest-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/SingleParentForest-root-existence": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/SingleParentForest-root-uniqueness": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

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
    "axiomBasis": "Finite typed partial parent function; induced child-to-parent edges; no positive directed cycles. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "p:V→Option(V); E(v,w) ⇔ p(v)=Some(w); ¬E⁺(v,v). V finite, possibly empty; exact vertex identities; unordered children and arbitrarily many components. Edges point child-to-parent; roots have parent None, never a self-parent sentinel. No sharing of a child between parents, cycles or dangling references. Parent function alone does not exclude cycles: acyclicity is a separate rule. A root and its descendants form a rooted tree after forgetting edge orientation; RootedTree currently uses an undirected carrier, so that relation is a construction rather than a literal specialization. Utility profile: x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.",
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
      "urn:csabs:operation/SingleParentForest-root-of",
      "urn:csabs:operation/SingleParentForest-descendant-or-self"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SingleParentForest-parent-function",
      "urn:csabs:axiom/SingleParentForest-acyclic",
      "urn:csabs:axiom/SingleParentForest-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/SingleParentForest-unique-root"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SingleParentForest-descendant-order",
      "urn:csabs:theorem/SingleParentForest-parent-chains-terminate",
      "urn:csabs:theorem/SingleParentForest-root-existence",
      "urn:csabs:theorem/SingleParentForest-root-uniqueness",
      "urn:csabs:theorem/SingleParentForest-rootOf-equation"
    ],
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
    "id": "urn:csabs:operation/SingleParentForest-descendant-or-self",
    "type": "Operation",
    "concept": "urn:csabs:concept/SingleParentForest",
    "name": "descendant-or-self",
    "signature": "descendantOrSelf : V²→Prop",
    "description": "x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
    "id": "urn:csabs:axiom/SingleParentForest-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.",
    "formalStatement": "descendantOrSelf : V²→Prop: x≼y iff zero or more parent steps take x to y. This orientation places roots above descendants; it is a partial order, not a total order.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
  },
  {
    "id": "urn:csabs:theorem/SingleParentForest-descendant-order",
    "type": "Theorem",
    "name": "descendant-order",
    "statement": "Descendant-or-self, oriented from descendant to ancestor, is a partial order.",
    "formalStatement": "Descendant-or-self, oriented from descendant to ancestor, is a partial order.",
    "mathematicalFormulation": "Descendant-or-self, oriented from descendant to ancestor, is a partial order.",
    "proofSketch": "Interpret parent edges as a DAG, then apply the reachability-order theorem.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-utility-profile",
      "urn:csabs:axiom/SingleParentForest-acyclic"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_descendant_order",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V), (∀ a, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a a) ∧\n    (∀ a b c, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a b →\n      Relation.ReflTransGen (Catalog.Programs.parentEdge f) b c → Relation.ReflTransGen (Catalog.Programs.parentEdge f) a c) ∧\n    (∀ a b, Relation.ReflTransGen (Catalog.Programs.parentEdge f) a b →\n      Relation.ReflTransGen (Catalog.Programs.parentEdge f) b a → a = b)",
    "leanModelMapping": "Descendant-or-self, oriented from descendant to ancestor, is a partial order. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SingleParentForest-acyclic\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/SingleParentForest-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.forest_descendant_order"
  },
  {
    "id": "urn:csabs:theorem/SingleParentForest-parent-chains-terminate",
    "type": "Theorem",
    "name": "parent-chains-terminate",
    "statement": "The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.",
    "formalStatement": "The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.",
    "mathematicalFormulation": "The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate.",
    "proofSketch": "The transitive parent closure is irreflexive and transitive on a finite carrier; use finite well-foundedness and relation inclusion.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-utility-profile",
      "urn:csabs:axiom/SingleParentForest-parent-function",
      "urn:csabs:axiom/SingleParentForest-acyclic"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_termination",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V), WellFounded (fun w v => Catalog.Programs.parentEdge f v w)",
    "leanModelMapping": "The converse parent-step relation of a finite single-parent acyclic forest is well-founded; forward parent chains terminate. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SingleParentForest-acyclic\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/SingleParentForest-parent-function\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/SingleParentForest-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.forest_termination"
  },
  {
    "id": "urn:csabs:theorem/SingleParentForest-root-existence",
    "type": "Theorem",
    "name": "root-existence",
    "statement": "Every vertex has a reachable root whose parent is none.",
    "formalStatement": "Every vertex has a reachable root whose parent is none.",
    "mathematicalFormulation": "Every vertex has a reachable root whose parent is none.",
    "proofSketch": "Well-founded induction: stop at parent none; otherwise prepend the parent step to the parent’s root path.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-utility-profile",
      "urn:csabs:theorem/SingleParentForest-parent-chains-terminate"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_exists",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V) (v : V), ∃ r, f.parent r = none ∧ Relation.ReflTransGen (Catalog.Programs.parentEdge f) v r",
    "leanModelMapping": "Every vertex has a reachable root whose parent is none. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SingleParentForest-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/SingleParentForest-parent-chains-terminate\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.forest_root_exists"
  },
  {
    "id": "urn:csabs:theorem/SingleParentForest-root-uniqueness",
    "type": "Theorem",
    "name": "root-uniqueness",
    "statement": "Any two parent-none roots reachable from the same vertex are equal.",
    "formalStatement": "Any two parent-none roots reachable from the same vertex are equal.",
    "mathematicalFormulation": "Any two parent-none roots reachable from the same vertex are equal.",
    "proofSketch": "Induct over one path; functional parenthood forces the first steps of both nonempty paths to coincide.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-utility-profile",
      "urn:csabs:axiom/SingleParentForest-parent-function"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_unique",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V)\n    (v r s : V) (_hr : f.parent r = none) (_hs : f.parent s = none)\n    (_hvr : Relation.ReflTransGen (Catalog.Programs.parentEdge f) v r)\n    (_hvs : Relation.ReflTransGen (Catalog.Programs.parentEdge f) v s), r = s",
    "leanModelMapping": "Any two parent-none roots reachable from the same vertex are equal. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SingleParentForest-parent-function\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/SingleParentForest-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.forest_root_unique"
  },
  {
    "id": "urn:csabs:theorem/SingleParentForest-rootOf-equation",
    "type": "Theorem",
    "name": "rootOf-equation",
    "statement": "parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.",
    "formalStatement": "parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.",
    "mathematicalFormulation": "parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). If parent(v)=none then rootOf(v)=v.",
    "proofSketch": "Choose the existence witness; uniqueness equates it to the root obtained by first following the parent.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/SingleParentForest"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SingleParentForest-utility-profile",
      "urn:csabs:theorem/SingleParentForest-root-existence",
      "urn:csabs:theorem/SingleParentForest-root-uniqueness"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, TransGen; Data/Fintype/Card.lean: Finite.wellFounded_of_trans_of_irrefl; constructed functional-parent root proofs; Catalog.Programs.forest_root_equation",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V : Type u} [Fintype V] (f : Catalog.Programs.SingleParentForest V) (v : V), f.parent (Catalog.Programs.forestRootOf f v) = none ∧\n    Relation.ReflTransGen (Catalog.Programs.parentEdge f) v (Catalog.Programs.forestRootOf f v) ∧\n    (∀ w, f.parent v = some w → Catalog.Programs.forestRootOf f v = Catalog.Programs.forestRootOf f w) ∧\n    (f.parent v = none → Catalog.Programs.forestRootOf f v = v)",
    "leanModelMapping": "parent(rootOf(v))=none, v reaches rootOf(v), and parent(v)=some(w) implies rootOf(v)=rootOf(w). Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated. The root case fixes v itself.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SingleParentForest-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/SingleParentForest-root-existence\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/SingleParentForest-root-uniqueness\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.forest_root_equation"
  }
]
```
<!-- graph-record:end -->
