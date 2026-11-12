# Strict binary search tree

A finite ordered binary tree whose inorder key sequence is strictly increasing under a fixed linear order.

**Notation:** BST(A)={t∈BT(A) | inorder(t) strictly increasing}

**Stable ID:** `urn:csabs:concept/BinarySearchTree`

**Categories:** Data structures → Tree structures

**Kind:** Abstract data type

**Prerequisites:** [Finite ordered binary tree with node labels](BinaryTree.md), [Total Order](TotalOrder.md), [Finite set collection](FiniteSet.md)

**Specializes:** [Finite ordered binary tree with node labels](BinaryTree.md)

## Backlinks

- [B-tree (balanced multiway search tree)](BTree.md) — `relatedConcept`

## Mathematical formulation

The selected carrier is {t∈BT(A) | inorder(t) is strictly increasing}, for a linear order A. Membership is x∈inorder(t); duplicate keys are excluded and the empty tree is permitted.

**Lean formulation** (in its source module context):

```lean
structure BinarySearchTree (A : Type u) [LinearOrder A] where
  tree : Catalog.BinaryTree A
  ordered : (Catalog.BinaryTree.inorder tree).Pairwise (· < ·)
```

**Source:** [`Catalog.BinarySearchTree`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** BST(A)={t∈BT(A) | inorder(t) strictly increasing}. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** inorder(t) is pairwise strictly increasing; member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t); t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)

**basisKind:** extensional-structural-definition

**basisScope:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**specializationNote:** Forget the strictly-increasing inorder proof, retaining the same empty/node constructors, labels and child positions. No claim inheritance; the additional invariant requires a linear order.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BinarySearchTree-member"></a>

### member

`urn:csabs:operation/BinarySearchTree-member`

**signature:** member : BST(A)×A→Prop

**description:** member(t,x) iff x occurs in inorder(t).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** member(t,x) iff x occurs in inorder(t).

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinarySearchTree-keys"></a>

### keys

`urn:csabs:operation/BinarySearchTree-keys`

**signature:** keys : BST(A)→FinSet(A)

**description:** Returns the inorder values as a set.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the inorder values as a set.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinarySearchTree-insert"></a>

### insert

`urn:csabs:operation/BinarySearchTree-insert`

**signature:** insert : BST(A)×A→𝒫(BST(A))

**description:** All well-formed t′ with keys(t′)=keys(t)∪{x}; shape unconstrained.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** All well-formed t′ with keys(t′)=keys(t)∪{x}; shape unconstrained.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BinarySearchTree-delete"></a>

### delete

`urn:csabs:operation/BinarySearchTree-delete`

**signature:** delete : BST(A)×A→𝒫(BST(A))

**description:** All well-formed t′ with keys(t′)=keys(t)∖{x}; shape unconstrained.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** All well-formed t′ with keys(t′)=keys(t)∖{x}; shape unconstrained.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BinarySearchTree-strict-order"></a>

### strict-order

`urn:csabs:axiom/BinarySearchTree-strict-order`

**statement:** Defining requirement: inorder(t) is pairwise strictly increasing

**formalStatement:** inorder(t) is pairwise strictly increasing

**assumptions:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BinarySearchTree-key-observation"></a>

### key-observation

`urn:csabs:axiom/BinarySearchTree-key-observation`

**statement:** Defining requirement: member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t)

**formalStatement:** member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t)

**assumptions:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BinarySearchTree-update-specification"></a>

### update-specification

`urn:csabs:axiom/BinarySearchTree-update-specification`

**statement:** Defining requirement: t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)

**formalStatement:** t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)

**assumptions:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-BinarySearchTree-unique-keys"></a>

### unique-keys

`urn:csabs:law/BinarySearchTree-unique-keys`

**statement:** No value occurs twice in inorder(t)

**formalStatement:** No value occurs twice in inorder(t)

**assumptions:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [strict-order](BinarySearchTree.md#node-urn-csabs-axiom-BinarySearchTree-strict-order)

**proofSketch:** Two equal occurrences would require x<x by strict-order, contradicting irreflexivity.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-BinarySearchTree-insert-membership"></a>

### insert-membership

`urn:csabs:theorem/BinarySearchTree-insert-membership`

**statement:** t′∈insert(t,x) ⇒ member(t′,x)

**formalStatement:** t′∈insert(t,x) ⇒ member(t′,x)

**assumptions:** Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [key-observation](BinarySearchTree.md#node-urn-csabs-axiom-BinarySearchTree-key-observation); [update-specification](BinarySearchTree.md#node-urn-csabs-axiom-BinarySearchTree-update-specification)

**proofSketch:** The inserted singleton is contained in the new key set; expand member.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Pat Morin: Open Data Structures, BinarySearchTree](https://opendatastructures.org/ods-python/6_2_BinarySearchTree_Unbala.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §6.2: search-tree ordering, search, insertion and removal

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BinarySearchTree",
    "type": "Concept",
    "shortForm": "BinarySearchTree",
    "fullName": "Strict binary search tree",
    "category": [
      "urn:csabs:category/tree-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite ordered binary tree whose inorder key sequence is strictly increasing under a fixed linear order.",
    "notation": "BST(A)={t∈BT(A) | inorder(t) strictly increasing}",
    "requiresConcept": [
      "urn:csabs:concept/BinaryTree",
      "urn:csabs:concept/TotalOrder",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/BinarySearchTree-member",
      "urn:csabs:operation/BinarySearchTree-keys",
      "urn:csabs:operation/BinarySearchTree-insert",
      "urn:csabs:operation/BinarySearchTree-delete"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BinarySearchTree-strict-order",
      "urn:csabs:axiom/BinarySearchTree-key-observation",
      "urn:csabs:axiom/BinarySearchTree-update-specification"
    ],
    "hasLaw": [
      "urn:csabs:law/BinarySearchTree-unique-keys"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BinarySearchTree-insert-membership"
    ],
    "axiomBasis": "inorder(t) is pairwise strictly increasing; member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t); t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/BinaryTree"
    ],
    "specializationNote": "Forget the strictly-increasing inorder proof, retaining the same empty/node constructors, labels and child positions. No claim inheritance; the additional invariant requires a linear order.",
    "leanFormulation": "structure BinarySearchTree (A : Type u) [LinearOrder A] where\n  tree : Catalog.BinaryTree A\n  ordered : (Catalog.BinaryTree.inorder tree).Pairwise (· < ·)",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.BinarySearchTree",
    "formulationScope": "model",
    "leanModelMapping": "BST(A)={t∈BT(A) | inorder(t) strictly increasing}. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "The selected carrier is {t∈BT(A) | inorder(t) is strictly increasing}, for a linear order A. Membership is x∈inorder(t); duplicate keys are excluded and the empty tree is permitted."
  },
  {
    "id": "urn:csabs:operation/BinarySearchTree-member",
    "type": "Operation",
    "name": "member",
    "signature": "member : BST(A)×A→Prop",
    "description": "member(t,x) iff x occurs in inorder(t).",
    "concept": "urn:csabs:concept/BinarySearchTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "member(t,x) iff x occurs in inorder(t).",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinarySearchTree-keys",
    "type": "Operation",
    "name": "keys",
    "signature": "keys : BST(A)→FinSet(A)",
    "description": "Returns the inorder values as a set.",
    "concept": "urn:csabs:concept/BinarySearchTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the inorder values as a set.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinarySearchTree-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : BST(A)×A→𝒫(BST(A))",
    "description": "All well-formed t′ with keys(t′)=keys(t)∪{x}; shape unconstrained.",
    "concept": "urn:csabs:concept/BinarySearchTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "All well-formed t′ with keys(t′)=keys(t)∪{x}; shape unconstrained.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BinarySearchTree-delete",
    "type": "Operation",
    "name": "delete",
    "signature": "delete : BST(A)×A→𝒫(BST(A))",
    "description": "All well-formed t′ with keys(t′)=keys(t)∖{x}; shape unconstrained.",
    "concept": "urn:csabs:concept/BinarySearchTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "All well-formed t′ with keys(t′)=keys(t)∖{x}; shape unconstrained.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinarySearchTree-strict-order",
    "type": "Axiom",
    "name": "strict-order",
    "statement": "Defining requirement: inorder(t) is pairwise strictly increasing",
    "formalStatement": "inorder(t) is pairwise strictly increasing",
    "assumptions": [
      "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinarySearchTree-key-observation",
    "type": "Axiom",
    "name": "key-observation",
    "statement": "Defining requirement: member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t)",
    "formalStatement": "member(t,x) ⇔ x∈keys(t) ⇔ x occurs in inorder(t)",
    "assumptions": [
      "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BinarySearchTree-update-specification",
    "type": "Axiom",
    "name": "update-specification",
    "statement": "Defining requirement: t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)",
    "formalStatement": "t′∈insert(t,x)⇔keys(t′)=keys(t)∪{x}; t′∈delete(t,x)⇔keys(t′)=keys(t)∖{x}, with all trees in BST(A)",
    "assumptions": [
      "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/BinarySearchTree-unique-keys",
    "type": "Law",
    "name": "unique-keys",
    "statement": "No value occurs twice in inorder(t)",
    "formalStatement": "No value occurs twice in inorder(t)",
    "assumptions": [
      "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BinarySearchTree-strict-order"
    ],
    "proofSketch": "Two equal occurrences would require x<x by strict-order, contradicting irreflexivity.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/BinarySearchTree-insert-membership",
    "type": "Theorem",
    "name": "insert-membership",
    "statement": "t′∈insert(t,x) ⇒ member(t′,x)",
    "formalStatement": "t′∈insert(t,x) ⇒ member(t′,x)",
    "assumptions": [
      "Set-valued key profile: duplicates excluded, empty tree allowed. Equality retains tree shape; different trees with identical keys can differ. No balancing or logarithmic bound. Insert/delete are invariant-preserving specifications and may admit several shapes.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BinarySearchTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/BinarySearchTree-key-observation",
      "urn:csabs:axiom/BinarySearchTree-update-specification"
    ],
    "proofSketch": "The inserted singleton is contained in the new key set; expand member.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-bst-core"
    ],
    "sourceLocator": "§6.2: search-tree ordering, search, insertion and removal",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
