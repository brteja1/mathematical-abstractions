# B-tree (balanced multiway search tree)

A finite ordered multiway search tree with distinct keys, bounded node occupancy and all leaves at the same depth.

**Notation:** BTree_t(A)⊆RoseTree(List(A)), t∈ℕ, t≥2; node(ks,cs); keys(T)=set(inorder(T)).

**Stable ID:** `urn:csabs:concept/BTree`

**Categories:** Data structures → Tree structures

**Kind:** Abstract data type

**Prerequisites:** [Finite ordered rose tree](RoseTree.md), [Finite sequence (List datatype)](Sequence.md), [Total Order](TotalOrder.md), [Finite set collection](FiniteSet.md)

**Specializes:** [Finite ordered rose tree](RoseTree.md)

**Related concepts:** [Strict binary search tree](BinarySearchTree.md)

## Mathematical formulation

The current partial Lean carrier is BTreeShape(A)=RoseTree(List(A)). It stores ordered children and a finite key list per node. No occupancy, search-order or equal-leaf-depth predicate is encoded in this carrier.

**Lean formulation** (in its source module context):

```lean
abbrev BTreeShape (A : Type u) := RoseTree (List A)
```

**Source:** [`Catalog.BTreeShape`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Raw RoseTree (List A): each node carries a finite key list and an ordered finite child list. Empty B-tree shape is RoseTree.node [] []. Structural equality preserves keys and child order.

**Limits:** Partial raw-shape interpretation only. Minimum degree, occupancy, arity, key ordering, balance, membership, height and updates are not formalized; no B-tree proof witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite rose-tree carrier with key-list labels; root-aware occupancy, child arity, strict inorder ordering, equal leaf depth; key-set observers and invariant-preserving updates.

**basisKind:** extensional-structural-definition

**basisScope:** Fixed t≥2 and linear order on A. Distinct keys, including keys in internal nodes. Empty is node([],[]); every other root has 1..2t−1 keys; nonroot nodes have t−1..2t−1 keys. Structural equality retains shape. Height counts node levels, so height(empty)=1. Updates may choose any valid output shape with the specified key set; duplicate insertion and absent deletion preserve keys but need not preserve shape. Pure sequential specification; no storage layout, concurrent semantics or algorithmic running-time guarantee.

**specializationNote:** Instantiate RoseTree labels with finite key lists and retain ordered children and structural equality; restrict this carrier by the explicit occupancy, arity, order and balance invariants. Empty B-tree is node([],[]), a nonempty rose tree with no keys. No axiom inheritance.

**verificationObligation:** Fix minimum degree (not maximum order), key comparison and structural versus key-set equality.; Do not transfer binary-tree operations or implementation complexity through related links.; Map relational update outcomes to the target implementation; distinguish B-tree from B+ tree.

**reviewStatus:** Editorial mathematical specification; Lean binding covers raw shapes only, not B-tree invariants or proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BTree-empty"></a>

### empty

`urn:csabs:operation/BTree-empty`

**signature:** empty_t : BTree_t(A)

**description:** Construct the root leaf with no keys.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** empty_t=node([],[])

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BTree-inorder"></a>

### inorder

`urn:csabs:operation/BTree-inorder`

**signature:** inorder : BTree_t(A)→List(A)

**description:** Read keys in search order.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** For a leaf, inorder(node(ks,[]))=ks; otherwise interleave inorder(c₀),k₀,inorder(c₁),…,kₘ₋₁,inorder(cₘ).

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BTree-member"></a>

### member

`urn:csabs:operation/BTree-member`

**signature:** member : BTree_t(A)×A→Bool

**description:** Decide key membership.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** member(T,x) ⇔ x∈keys(T)

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BTree-insert"></a>

### insert

`urn:csabs:operation/BTree-insert`

**signature:** insert : BTree_t(A)×A→𝒫(BTree_t(A))

**description:** Specify insertion outcomes.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** T′∈insert(T,x) ⇔ keys(T′)=keys(T)∪{x}

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BTree-delete"></a>

### delete

`urn:csabs:operation/BTree-delete`

**signature:** delete : BTree_t(A)×A→𝒫(BTree_t(A))

**description:** Specify deletion outcomes.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** T′∈delete(T,x) ⇔ keys(T′)=keys(T)∖{x}

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BTree-height"></a>

### height

`urn:csabs:operation/BTree-height`

**signature:** height : BTree_t(A)→ℕ

**description:** Count levels from root to leaf.

**precondition:** t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.

**totality:** Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.

**postcondition:** A leaf has height 1; an internal node has 1+max child height.

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BTree-occupancy"></a>

### occupancy

`urn:csabs:axiom/BTree-occupancy`

**statement:** Root and nonroot key counts obey minimum-degree bounds.

**formalStatement:** For every node with m keys: m≤2t−1; if nonroot then m≥t−1; if root then m≥1 unless it is the unique empty leaf node([],[]).

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

<a id="node-urn-csabs-axiom-BTree-arity"></a>

### arity

`urn:csabs:axiom/BTree-arity`

**statement:** Leaves have no children; internal nodes have one more child than keys.

**formalStatement:** At every node(ks,cs), cs=[] or |cs|=|ks|+1; an internal root has |ks|≥1.

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

<a id="node-urn-csabs-axiom-BTree-ordering"></a>

### ordering

`urn:csabs:axiom/BTree-ordering`

**statement:** Inorder interleaves children and separator keys and is strictly increasing.

**formalStatement:** inorder(node(ks,[]))=ks; inorder(node([k₀,…,kₘ₋₁],[c₀,…,cₘ]))=inorder(c₀)·[k₀]·…·[kₘ₋₁]·inorder(cₘ); inorder(T) is strictly increasing.

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

<a id="node-urn-csabs-axiom-BTree-balance"></a>

### balance

`urn:csabs:axiom/BTree-balance`

**statement:** All actual leaves have the same depth.

**formalStatement:** ∃d∈ℕ, every leaf occurrence in T has edge depth d; height(T)=d+1.

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

<a id="node-urn-csabs-axiom-BTree-observers"></a>

### observers

`urn:csabs:axiom/BTree-observers`

**statement:** Empty and membership are defined by their key-set interpretation.

**formalStatement:** empty_t=node([],[]); keys(T)=set(inorder(T)); member(T,x) ⇔ x∈keys(T).

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

<a id="node-urn-csabs-axiom-BTree-updates"></a>

### updates

`urn:csabs:axiom/BTree-updates`

**statement:** Updates preserve the B-tree invariants and have exactly the specified key sets.

**formalStatement:** insert(T,x)={U∈BTree_t(A) | keys(U)=keys(T)∪{x}}; delete(T,x)={U∈BTree_t(A) | keys(U)=keys(T)∖{x}}; both sets are nonempty.

**assumptions:** t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality.

**ruleRole:** defining-rule

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

**reviewStatus:** Editorial defining rule; not a compiled theorem.

## Laws

<a id="node-urn-csabs-law-BTree-insert-membership"></a>

### insert-membership

`urn:csabs:law/BTree-insert-membership`

**statement:** Insertion adds precisely the chosen key.

**formalStatement:** U∈insert(T,x) ⇒ (member(U,y) ⇔ y=x ∨ member(T,y))

**assumptions:** The fixed minimum degree, linear order and finite carrier in BTree basisScope apply.

**dependsOn:** [updates](BTree.md#node-urn-csabs-axiom-BTree-updates); [observers](BTree.md#node-urn-csabs-axiom-BTree-observers)

**proofSketch:** Substitute the union key-set equation into membership and use membership in a singleton union.

**reviewStatus:** editorial derivation; not machine-proved

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Catalog derivation from the linked defining premises; no compiled proof is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-law-BTree-delete-membership"></a>

### delete-membership

`urn:csabs:law/BTree-delete-membership`

**statement:** Deletion removes precisely the chosen key.

**formalStatement:** U∈delete(T,x) ⇒ (member(U,y) ⇔ member(T,y) ∧ y≠x)

**assumptions:** The fixed minimum degree, linear order and finite carrier in BTree basisScope apply.

**dependsOn:** [updates](BTree.md#node-urn-csabs-axiom-BTree-updates); [observers](BTree.md#node-urn-csabs-axiom-BTree-observers)

**proofSketch:** Substitute the difference key-set equation into membership.

**reviewStatus:** editorial derivation; not machine-proved

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Catalog derivation from the linked defining premises; no compiled proof is asserted.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-BTree-height-key-bound"></a>

### height-key-bound

`urn:csabs:theorem/BTree-height-key-bound`

**statement:** Occupancy and balance bound height in terms of key count.

**formalStatement:** For n=|keys(T)|>0 and h=height(T): 2t^(h−1)−1≤n≤(2t)^h−1.

**assumptions:** The fixed minimum degree, linear order and finite carrier in BTree basisScope apply.

**dependsOn:** [occupancy](BTree.md#node-urn-csabs-axiom-BTree-occupancy); [arity](BTree.md#node-urn-csabs-axiom-BTree-arity); [ordering](BTree.md#node-urn-csabs-axiom-BTree-ordering); [balance](BTree.md#node-urn-csabs-axiom-BTree-balance); [observers](BTree.md#node-urn-csabs-axiom-BTree-observers)

**proofSketch:** At level zero a nonempty root has at least one key. For h≥2 it has at least two children and subsequent internal nodes at least t; sum minimum keys 1+2(t−1)Σ(i=0..h−2)t^i. At most (2t)^i nodes occur at level i, each with 2t−1 keys. Strict ordering identifies key count with total key occurrences. For h=1 use the root bounds.

**reviewStatus:** editorial derivation; not machine-proved

**source:** [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Catalog derivation from the linked defining premises; no compiled proof is asserted.

**provenanceKind:** derived

## Concept provenance

- [Pat Morin: Open Data Structures, section 14.2 B-Trees](https://opendatastructures.org/ods-python/14_2_B_Trees.html); accessedOn: 2026-11-08; sourceRole: definition-and-search-tree-interface-reference

**sourceLocator:** §14.2 definition; §§14.2.1–14.2.3 search, addition, removal

**sourceNote:** Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BTree",
    "type": "Concept",
    "shortForm": "BTree",
    "fullName": "B-tree (balanced multiway search tree)",
    "category": [
      "urn:csabs:category/tree-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite ordered multiway search tree with distinct keys, bounded node occupancy and all leaves at the same depth.",
    "notation": "BTree_t(A)⊆RoseTree(List(A)), t∈ℕ, t≥2; node(ks,cs); keys(T)=set(inorder(T)).",
    "requiresConcept": [
      "urn:csabs:concept/RoseTree",
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/TotalOrder",
      "urn:csabs:concept/FiniteSet"
    ],
    "specializationOf": [
      "urn:csabs:concept/RoseTree"
    ],
    "specializationNote": "Instantiate RoseTree labels with finite key lists and retain ordered children and structural equality; restrict this carrier by the explicit occupancy, arity, order and balance invariants. Empty B-tree is node([],[]), a nonempty rose tree with no keys. No axiom inheritance.",
    "relatedConcept": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "axiomBasis": "Finite rose-tree carrier with key-list labels; root-aware occupancy, child arity, strict inorder ordering, equal leaf depth; key-set observers and invariant-preserving updates.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Fixed t≥2 and linear order on A. Distinct keys, including keys in internal nodes. Empty is node([],[]); every other root has 1..2t−1 keys; nonroot nodes have t−1..2t−1 keys. Structural equality retains shape. Height counts node levels, so height(empty)=1. Updates may choose any valid output shape with the specified key set; duplicate insertion and absent deletion preserve keys but need not preserve shape. Pure sequential specification; no storage layout, concurrent semantics or algorithmic running-time guarantee.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical specification; Lean binding covers raw shapes only, not B-tree invariants or proofs.",
    "verificationObligation": [
      "Fix minimum degree (not maximum order), key comparison and structural versus key-set equality.",
      "Do not transfer binary-tree operations or implementation complexity through related links.",
      "Map relational update outcomes to the target implementation; distinguish B-tree from B+ tree."
    ],
    "hasOperation": [
      "urn:csabs:operation/BTree-empty",
      "urn:csabs:operation/BTree-inorder",
      "urn:csabs:operation/BTree-member",
      "urn:csabs:operation/BTree-insert",
      "urn:csabs:operation/BTree-delete",
      "urn:csabs:operation/BTree-height"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BTree-occupancy",
      "urn:csabs:axiom/BTree-arity",
      "urn:csabs:axiom/BTree-ordering",
      "urn:csabs:axiom/BTree-balance",
      "urn:csabs:axiom/BTree-observers",
      "urn:csabs:axiom/BTree-updates"
    ],
    "hasLaw": [
      "urn:csabs:law/BTree-insert-membership",
      "urn:csabs:law/BTree-delete-membership"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BTree-height-key-bound"
    ],
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev BTreeShape (A : Type u) := RoseTree (List A)",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.BTreeShape",
    "formulationScope": "partial",
    "leanModelMapping": "Raw RoseTree (List A): each node carries a finite key list and an ordered finite child list. Empty B-tree shape is RoseTree.node [] []. Structural equality preserves keys and child order.",
    "leanModelLimitations": "Partial raw-shape interpretation only. Minimum degree, occupancy, arity, key ordering, balance, membership, height and updates are not formalized; no B-tree proof witnesses.",
    "mathematicalFormulation": "The current partial Lean carrier is BTreeShape(A)=RoseTree(List(A)). It stores ordered children and a finite key list per node. No occupancy, search-order or equal-leaf-depth predicate is encoded in this carrier."
  },
  {
    "id": "urn:csabs:operation/BTree-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty_t : BTree_t(A)",
    "description": "Construct the root leaf with no keys.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "empty_t=node([],[])",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BTree-inorder",
    "type": "Operation",
    "name": "inorder",
    "signature": "inorder : BTree_t(A)→List(A)",
    "description": "Read keys in search order.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "For a leaf, inorder(node(ks,[]))=ks; otherwise interleave inorder(c₀),k₀,inorder(c₁),…,kₘ₋₁,inorder(cₘ).",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BTree-member",
    "type": "Operation",
    "name": "member",
    "signature": "member : BTree_t(A)×A→Bool",
    "description": "Decide key membership.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "member(T,x) ⇔ x∈keys(T)",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BTree-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : BTree_t(A)×A→𝒫(BTree_t(A))",
    "description": "Specify insertion outcomes.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "T′∈insert(T,x) ⇔ keys(T′)=keys(T)∪{x}",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BTree-delete",
    "type": "Operation",
    "name": "delete",
    "signature": "delete : BTree_t(A)×A→𝒫(BTree_t(A))",
    "description": "Specify deletion outcomes.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "T′∈delete(T,x) ⇔ keys(T′)=keys(T)∖{x}",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BTree-height",
    "type": "Operation",
    "name": "height",
    "signature": "height : BTree_t(A)→ℕ",
    "description": "Count levels from root to leaf.",
    "precondition": "t≥2, fixed linear order, and all tree inputs satisfy the B-tree invariants.",
    "totality": "Total mathematical observer or constructor; insert/delete are nonempty sets of admissible outcomes.",
    "postcondition": "A leaf has height 1; an internal node has 1+max child height.",
    "concept": "urn:csabs:concept/BTree",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BTree-occupancy",
    "type": "Axiom",
    "name": "occupancy",
    "statement": "Root and nonroot key counts obey minimum-degree bounds.",
    "formalStatement": "For every node with m keys: m≤2t−1; if nonroot then m≥t−1; if root then m≥1 unless it is the unique empty leaf node([],[]).",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:axiom/BTree-arity",
    "type": "Axiom",
    "name": "arity",
    "statement": "Leaves have no children; internal nodes have one more child than keys.",
    "formalStatement": "At every node(ks,cs), cs=[] or |cs|=|ks|+1; an internal root has |ks|≥1.",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:axiom/BTree-ordering",
    "type": "Axiom",
    "name": "ordering",
    "statement": "Inorder interleaves children and separator keys and is strictly increasing.",
    "formalStatement": "inorder(node(ks,[]))=ks; inorder(node([k₀,…,kₘ₋₁],[c₀,…,cₘ]))=inorder(c₀)·[k₀]·…·[kₘ₋₁]·inorder(cₘ); inorder(T) is strictly increasing.",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:axiom/BTree-balance",
    "type": "Axiom",
    "name": "balance",
    "statement": "All actual leaves have the same depth.",
    "formalStatement": "∃d∈ℕ, every leaf occurrence in T has edge depth d; height(T)=d+1.",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:axiom/BTree-observers",
    "type": "Axiom",
    "name": "observers",
    "statement": "Empty and membership are defined by their key-set interpretation.",
    "formalStatement": "empty_t=node([],[]); keys(T)=set(inorder(T)); member(T,x) ⇔ x∈keys(T).",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:axiom/BTree-updates",
    "type": "Axiom",
    "name": "updates",
    "statement": "Updates preserve the B-tree invariants and have exactly the specified key sets.",
    "formalStatement": "insert(T,x)={U∈BTree_t(A) | keys(U)=keys(T)∪{x}}; delete(T,x)={U∈BTree_t(A) | keys(U)=keys(T)∖{x}}; both sets are nonempty.",
    "assumptions": [
      "t≥2; A has a fixed linear order; finite rose-tree carrier with structural equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "ruleRole": "defining-rule",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Minimum degree t is the source parameter B. Finite key-set profile; update outcomes specify allowed valid shapes, not an algorithm.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial defining rule; not a compiled theorem."
  },
  {
    "id": "urn:csabs:law/BTree-insert-membership",
    "type": "Law",
    "name": "insert-membership",
    "statement": "Insertion adds precisely the chosen key.",
    "formalStatement": "U∈insert(T,x) ⇒ (member(U,y) ⇔ y=x ∨ member(T,y))",
    "assumptions": [
      "The fixed minimum degree, linear order and finite carrier in BTree basisScope apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BTree-updates",
      "urn:csabs:axiom/BTree-observers"
    ],
    "proofSketch": "Substitute the union key-set equation into membership and use membership in a singleton union.",
    "reviewStatus": "editorial derivation; not machine-proved",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Catalog derivation from the linked defining premises; no compiled proof is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:law/BTree-delete-membership",
    "type": "Law",
    "name": "delete-membership",
    "statement": "Deletion removes precisely the chosen key.",
    "formalStatement": "U∈delete(T,x) ⇒ (member(U,y) ⇔ member(T,y) ∧ y≠x)",
    "assumptions": [
      "The fixed minimum degree, linear order and finite carrier in BTree basisScope apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BTree-updates",
      "urn:csabs:axiom/BTree-observers"
    ],
    "proofSketch": "Substitute the difference key-set equation into membership.",
    "reviewStatus": "editorial derivation; not machine-proved",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Catalog derivation from the linked defining premises; no compiled proof is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BTree-height-key-bound",
    "type": "Theorem",
    "name": "height-key-bound",
    "statement": "Occupancy and balance bound height in terms of key count.",
    "formalStatement": "For n=|keys(T)|>0 and h=height(T): 2t^(h−1)−1≤n≤(2t)^h−1.",
    "assumptions": [
      "The fixed minimum degree, linear order and finite carrier in BTree basisScope apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/BTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BTree-occupancy",
      "urn:csabs:axiom/BTree-arity",
      "urn:csabs:axiom/BTree-ordering",
      "urn:csabs:axiom/BTree-balance",
      "urn:csabs:axiom/BTree-observers"
    ],
    "proofSketch": "At level zero a nonempty root has at least one key. For h≥2 it has at least two children and subsequent internal nodes at least t; sum minimum keys 1+2(t−1)Σ(i=0..h−2)t^i. At most (2t)^i nodes occur at level i, each with 2t−1 keys. Strict ordering identifies key count with total key occurrences. For h=1 use the root bounds.",
    "reviewStatus": "editorial derivation; not machine-proved",
    "source": [
      "urn:csabs:source/ods-btrees"
    ],
    "sourceLocator": "§14.2 definition; §§14.2.1–14.2.3 search, addition, removal",
    "sourceNote": "Catalog derivation from the linked defining premises; no compiled proof is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
