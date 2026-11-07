# Finitely supported vector

A vector indexed by I whose coordinates in a field F vanish outside a finite set.

**Notation:** F^{(I)}={v:I→F | supp(v) finite}

**Stable ID:** `urn:csabs:concept/SparseVector`

**Categories:** Linear and multilinear algebra

**Kind:** Abstract data type

**Prerequisites:** [Vector space over a field](VectorSpace.md), [Finite set collection](FiniteSet.md)

**Specializes:** [Vector space over a field](VectorSpace.md)

## Backlinks

- [Finitely supported probability distribution](FiniteDistribution.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** supp(v)={i | v(i)≠0} is finite; (v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i); v=w ⇔ ∀i:I,v(i)=w(i)

**basisKind:** extensional-structural-definition

**basisScope:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.

**specializationNote:** Instantiate VectorSpace with carrier I→₀F and pointwise addition/scalar multiplication over F; finite supports are preserved by union containment.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SparseVector-coordinate"></a>

### coordinate

`urn:csabs:operation/SparseVector-coordinate`

**signature:** coordinate : F^{(I)}×I→F

**description:** coordinate(v,i)=v(i), zero outside support.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** coordinate(v,i)=v(i), zero outside support.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SparseVector-support"></a>

### support

`urn:csabs:operation/SparseVector-support`

**signature:** support : F^{(I)}→FinSet(I)

**description:** supp(v)={i | v(i)≠0}.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** supp(v)={i | v(i)≠0}.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SparseVector-add"></a>

### add

`urn:csabs:operation/SparseVector-add`

**signature:** add : F^{(I)}×F^{(I)}→F^{(I)}

**description:** (v+w)(i)=v(i)+w(i).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (v+w)(i)=v(i)+w(i).

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SparseVector-scale"></a>

### scale

`urn:csabs:operation/SparseVector-scale`

**signature:** scale : F×F^{(I)}→F^{(I)}

**description:** (a·v)(i)=a·v(i).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** (a·v)(i)=a·v(i).

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SparseVector-finite-support"></a>

### finite-support

`urn:csabs:axiom/SparseVector-finite-support`

**statement:** Defining requirement: supp(v)={i | v(i)≠0} is finite

**formalStatement:** supp(v)={i | v(i)≠0} is finite

**assumptions:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-SparseVector-pointwise-arithmetic"></a>

### pointwise-arithmetic

`urn:csabs:axiom/SparseVector-pointwise-arithmetic`

**statement:** Defining requirement: (v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i)

**formalStatement:** (v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i)

**assumptions:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-SparseVector-extensionality"></a>

### extensionality

`urn:csabs:axiom/SparseVector-extensionality`

**statement:** Defining requirement: v=w ⇔ ∀i:I,v(i)=w(i)

**formalStatement:** v=w ⇔ ∀i:I,v(i)=w(i)

**assumptions:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-SparseVector-support-addition"></a>

### support-addition

`urn:csabs:law/SparseVector-support-addition`

**statement:** supp(v+w)⊆supp(v)∪supp(w)

**formalStatement:** supp(v+w)⊆supp(v)∪supp(w)

**assumptions:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-support](SparseVector.md#node-urn-csabs-axiom-SparseVector-finite-support); [pointwise-arithmetic](SparseVector.md#node-urn-csabs-axiom-SparseVector-pointwise-arithmetic)

**proofSketch:** Outside the union both coordinates vanish, hence so does their sum.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-SparseVector-zero-scale"></a>

### zero-scale

`urn:csabs:theorem/SparseVector-zero-scale`

**statement:** 0·v=0

**formalStatement:** 0·v=0

**assumptions:** I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [pointwise-arithmetic](SparseVector.md#node-urn-csabs-axiom-SparseVector-pointwise-arithmetic); [extensionality](SparseVector.md#node-urn-csabs-axiom-SparseVector-extensionality)

**proofSketch:** Every coordinate equals 0·v(i)=0 in the field; apply extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Data/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: LinearAlgebra/Finsupp/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/LinearAlgebra/Finsupp/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SparseVector",
    "type": "Concept",
    "shortForm": "SparseVector",
    "fullName": "Finitely supported vector",
    "category": [
      "urn:csabs:category/linear-algebra"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A vector indexed by I whose coordinates in a field F vanish outside a finite set.",
    "notation": "F^{(I)}={v:I→F | supp(v) finite}",
    "requiresConcept": [
      "urn:csabs:concept/VectorSpace",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/SparseVector-coordinate",
      "urn:csabs:operation/SparseVector-support",
      "urn:csabs:operation/SparseVector-add",
      "urn:csabs:operation/SparseVector-scale"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SparseVector-finite-support",
      "urn:csabs:axiom/SparseVector-pointwise-arithmetic",
      "urn:csabs:axiom/SparseVector-extensionality"
    ],
    "hasLaw": [
      "urn:csabs:law/SparseVector-support-addition"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SparseVector-zero-scale"
    ],
    "axiomBasis": "supp(v)={i | v(i)≠0} is finite; (v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i); v=w ⇔ ∀i:I,v(i)=w(i)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/VectorSpace"
    ],
    "specializationNote": "Instantiate VectorSpace with carrier I→₀F and pointwise addition/scalar multiplication over F; finite supports are preserved by union containment."
  },
  {
    "id": "urn:csabs:operation/SparseVector-coordinate",
    "type": "Operation",
    "name": "coordinate",
    "signature": "coordinate : F^{(I)}×I→F",
    "description": "coordinate(v,i)=v(i), zero outside support.",
    "concept": "urn:csabs:concept/SparseVector",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "coordinate(v,i)=v(i), zero outside support.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SparseVector-support",
    "type": "Operation",
    "name": "support",
    "signature": "support : F^{(I)}→FinSet(I)",
    "description": "supp(v)={i | v(i)≠0}.",
    "concept": "urn:csabs:concept/SparseVector",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "supp(v)={i | v(i)≠0}.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SparseVector-add",
    "type": "Operation",
    "name": "add",
    "signature": "add : F^{(I)}×F^{(I)}→F^{(I)}",
    "description": "(v+w)(i)=v(i)+w(i).",
    "concept": "urn:csabs:concept/SparseVector",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(v+w)(i)=v(i)+w(i).",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SparseVector-scale",
    "type": "Operation",
    "name": "scale",
    "signature": "scale : F×F^{(I)}→F^{(I)}",
    "description": "(a·v)(i)=a·v(i).",
    "concept": "urn:csabs:concept/SparseVector",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "(a·v)(i)=a·v(i).",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SparseVector-finite-support",
    "type": "Axiom",
    "name": "finite-support",
    "statement": "Defining requirement: supp(v)={i | v(i)≠0} is finite",
    "formalStatement": "supp(v)={i | v(i)≠0} is finite",
    "assumptions": [
      "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/SparseVector"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SparseVector-pointwise-arithmetic",
    "type": "Axiom",
    "name": "pointwise-arithmetic",
    "statement": "Defining requirement: (v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i)",
    "formalStatement": "(v+w)(i)=v(i)+w(i); (a·v)(i)=a·v(i)",
    "assumptions": [
      "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/SparseVector"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SparseVector-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Defining requirement: v=w ⇔ ∀i:I,v(i)=w(i)",
    "formalStatement": "v=w ⇔ ∀i:I,v(i)=w(i)",
    "assumptions": [
      "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/SparseVector"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/SparseVector-support-addition",
    "type": "Law",
    "name": "support-addition",
    "statement": "supp(v+w)⊆supp(v)∪supp(w)",
    "formalStatement": "supp(v+w)⊆supp(v)∪supp(w)",
    "assumptions": [
      "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/SparseVector"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SparseVector-finite-support",
      "urn:csabs:axiom/SparseVector-pointwise-arithmetic"
    ],
    "proofSketch": "Outside the union both coordinates vanish, hence so does their sum.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/SparseVector-zero-scale",
    "type": "Theorem",
    "name": "zero-scale",
    "statement": "0·v=0",
    "formalStatement": "0·v=0",
    "assumptions": [
      "I may be infinite, F is a field. Zero is implicit outside support; stored explicit zeros have no distinct mathematical identity. Exact scalar operations; no numerical pruning tolerance.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/SparseVector"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SparseVector-pointwise-arithmetic",
      "urn:csabs:axiom/SparseVector-extensionality"
    ],
    "proofSketch": "Every coordinate equals 0·v(i)=0 in the field; apply extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-finsupp-core",
      "urn:csabs:source/mathlib-sparse-module-core"
    ],
    "sourceLocator": "Finsupp finite support carrier and extensional evaluation; Finsupp module structure and linearEquivFunOnFinite",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
