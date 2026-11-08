# Finite ordered rose tree

A finite nonempty node-labelled rooted tree with an ordered finite list of children at every node.

**Notation:** Rose(A)=μX.(A×Seq(X)); node(a,children)

**Stable ID:** `urn:csabs:concept/RoseTree`

**Categories:** Data structures → Tree structures

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Structural Induction](StructuralInduction.md)

**Related concepts:** [Finite rooted undirected tree](RootedTree.md), [Finite ordered binary tree with node labels](BinaryTree.md)

## Backlinks

- [B-tree (balanced multiway search tree)](BTree.md) — `requiresConcept`
- [B-tree (balanced multiway search tree)](BTree.md) — `specializationOf`
- [Free ranked term algebra with variables](TermAlgebra.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** root(node(a,cs))=a ∧ children(node(a,cs))=cs; node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form; If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t); fold_k(node(a,cs))=k(a,map(fold_k,cs))

**basisKind:** extensional-structural-definition

**basisScope:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RoseTree-node"></a>

### node

`urn:csabs:operation/RoseTree-node`

**signature:** node : A×Seq(Rose(A))→Rose(A)

**description:** Constructs a labelled root with ordered children.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs a labelled root with ordered children.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RoseTree-root"></a>

### root

`urn:csabs:operation/RoseTree-root`

**signature:** root : Rose(A)→A

**description:** root(node(a,cs))=a.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** root(node(a,cs))=a.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RoseTree-children"></a>

### children

`urn:csabs:operation/RoseTree-children`

**signature:** children : Rose(A)→Seq(Rose(A))

**description:** children(node(a,cs))=cs.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** children(node(a,cs))=cs.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RoseTree-fold"></a>

### fold

`urn:csabs:operation/RoseTree-fold`

**signature:** fold_k : Rose(A)→B, k:A×Seq(B)→B

**description:** fold_k(node(a,cs))=k(a,map(fold_k,cs)).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** fold_k(node(a,cs))=k(a,map(fold_k,cs)).

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RoseTree-projections"></a>

### projections

`urn:csabs:axiom/RoseTree-projections`

**statement:** Defining requirement: root(node(a,cs))=a ∧ children(node(a,cs))=cs

**formalStatement:** root(node(a,cs))=a ∧ children(node(a,cs))=cs

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RoseTree-free-constructor"></a>

### free-constructor

`urn:csabs:axiom/RoseTree-free-constructor`

**statement:** Defining requirement: node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form

**formalStatement:** node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RoseTree-induction"></a>

### induction

`urn:csabs:axiom/RoseTree-induction`

**statement:** Defining requirement: If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t)

**formalStatement:** If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t)

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RoseTree-fold-equation"></a>

### fold-equation

`urn:csabs:axiom/RoseTree-fold-equation`

**statement:** Defining requirement: fold_k(node(a,cs))=k(a,map(fold_k,cs))

**formalStatement:** fold_k(node(a,cs))=k(a,map(fold_k,cs))

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RoseTree-eta"></a>

### eta

`urn:csabs:law/RoseTree-eta`

**statement:** node(root(t),children(t))=t

**formalStatement:** node(root(t),children(t))=t

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [projections](RoseTree.md#node-urn-csabs-axiom-RoseTree-projections); [free-constructor](RoseTree.md#node-urn-csabs-axiom-RoseTree-free-constructor)

**proofSketch:** Decompose t as a node and apply both projection equations.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-RoseTree-fold-unique"></a>

### fold-unique

`urn:csabs:theorem/RoseTree-fold-unique`

**statement:** If f(node(a,cs))=k(a,map(f,cs)), then f=fold_k

**formalStatement:** If f(node(a,cs))=k(a,map(f,cs)), then f=fold_k

**assumptions:** No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [induction](RoseTree.md#node-urn-csabs-axiom-RoseTree-induction); [fold-equation](RoseTree.md#node-urn-csabs-axiom-RoseTree-fold-equation)

**proofSketch:** Structural induction identifies all child results, then the node result; apply function extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles; [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles
- [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RoseTree",
    "type": "Concept",
    "shortForm": "RoseTree",
    "fullName": "Finite ordered rose tree",
    "category": [
      "urn:csabs:category/tree-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite nonempty node-labelled rooted tree with an ordered finite list of children at every node.",
    "notation": "Rose(A)=μX.(A×Seq(X)); node(a,children)",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/StructuralInduction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RootedTree",
      "urn:csabs:concept/BinaryTree"
    ],
    "hasOperation": [
      "urn:csabs:operation/RoseTree-node",
      "urn:csabs:operation/RoseTree-root",
      "urn:csabs:operation/RoseTree-children",
      "urn:csabs:operation/RoseTree-fold"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RoseTree-projections",
      "urn:csabs:axiom/RoseTree-free-constructor",
      "urn:csabs:axiom/RoseTree-induction",
      "urn:csabs:axiom/RoseTree-fold-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/RoseTree-eta"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RoseTree-fold-unique"
    ],
    "axiomBasis": "root(node(a,cs))=a ∧ children(node(a,cs))=cs; node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form; If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t); fold_k(node(a,cs))=k(a,map(fold_k,cs))",
    "basisKind": "extensional-structural-definition",
    "basisScope": "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RoseTree-node",
    "type": "Operation",
    "name": "node",
    "signature": "node : A×Seq(Rose(A))→Rose(A)",
    "description": "Constructs a labelled root with ordered children.",
    "concept": "urn:csabs:concept/RoseTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs a labelled root with ordered children.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RoseTree-root",
    "type": "Operation",
    "name": "root",
    "signature": "root : Rose(A)→A",
    "description": "root(node(a,cs))=a.",
    "concept": "urn:csabs:concept/RoseTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "root(node(a,cs))=a.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RoseTree-children",
    "type": "Operation",
    "name": "children",
    "signature": "children : Rose(A)→Seq(Rose(A))",
    "description": "children(node(a,cs))=cs.",
    "concept": "urn:csabs:concept/RoseTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "children(node(a,cs))=cs.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RoseTree-fold",
    "type": "Operation",
    "name": "fold",
    "signature": "fold_k : Rose(A)→B, k:A×Seq(B)→B",
    "description": "fold_k(node(a,cs))=k(a,map(fold_k,cs)).",
    "concept": "urn:csabs:concept/RoseTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "fold_k(node(a,cs))=k(a,map(fold_k,cs)).",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RoseTree-projections",
    "type": "Axiom",
    "name": "projections",
    "statement": "Defining requirement: root(node(a,cs))=a ∧ children(node(a,cs))=cs",
    "formalStatement": "root(node(a,cs))=a ∧ children(node(a,cs))=cs",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RoseTree-free-constructor",
    "type": "Axiom",
    "name": "free-constructor",
    "statement": "Defining requirement: node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form",
    "formalStatement": "node(a,cs)=node(b,ds) ⇔ a=b ∧ cs=ds; every tree has this form",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RoseTree-induction",
    "type": "Axiom",
    "name": "induction",
    "statement": "Defining requirement: If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t)",
    "formalStatement": "If ∀a,cs, (∀t∈cs,P(t))⇒P(node(a,cs)), then ∀t,P(t)",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RoseTree-fold-equation",
    "type": "Axiom",
    "name": "fold-equation",
    "statement": "Defining requirement: fold_k(node(a,cs))=k(a,map(fold_k,cs))",
    "formalStatement": "fold_k(node(a,cs))=k(a,map(fold_k,cs))",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RoseTree-eta",
    "type": "Law",
    "name": "eta",
    "statement": "node(root(t),children(t))=t",
    "formalStatement": "node(root(t),children(t))=t",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RoseTree-projections",
      "urn:csabs:axiom/RoseTree-free-constructor"
    ],
    "proofSketch": "Decompose t as a node and apply both projection equations.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RoseTree-fold-unique",
    "type": "Theorem",
    "name": "fold-unique",
    "statement": "If f(node(a,cs))=k(a,map(f,cs)), then f=fold_k",
    "formalStatement": "If f(node(a,cs))=k(a,map(f,cs)), then f=fold_k",
    "assumptions": [
      "No empty tree constructor; a leaf is node(a,[]). Child order, shape and repeated label occurrences are observable; no pointer sharing/cycles/infinite branches. If A is empty there are no values.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RoseTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RoseTree-induction",
      "urn:csabs:axiom/RoseTree-fold-equation"
    ],
    "proofSketch": "Structural induction identifies all child results, then the node result; apply function extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-inductive-types",
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "§§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors; Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
