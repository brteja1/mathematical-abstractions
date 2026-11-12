# Vector space over a field

An additive abelian group V equipped with scalar multiplication by a specified field F satisfying scalar associativity, identity and both distributive laws.

**Notation:** V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V

**Stable ID:** `urn:csabs:concept/VectorSpace`

**Categories:** Algebra → Linear and multilinear algebra, Algebra

**Kind:** Mathematical structure

**Prerequisites:** [Field](Field.md), [Group](Group.md)

**Specializes:** [Group](Group.md)

## Backlinks

- [Euclidean dual of a finite-field linear code](DualCode.md) — `requiresConcept`
- [Euclidean lattice (discrete integer-span lattice)](EuclideanLattice.md) — `requiresConcept`
- [Linear block code over a finite field](LinearBlockCode.md) — `requiresConcept`
- [Linear map](LinearMap.md) — `requiresConcept`
- [Finite rectangular matrix over a field](Matrix.md) — `requiresConcept`
- [Finitely supported vector](SparseVector.md) — `requiresConcept`
- [Finitely supported vector](SparseVector.md) — `specializationOf`
- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `requiresConcept`
- [Tensor of specified valence on a finite-dimensional vector space](Tensor.md) — `specializationOf`
- [Tensor product of vector spaces](TensorProduct.md) — `requiresConcept`
- [Tensor product of vector spaces](TensorProduct.md) — `specializationOf`

## Mathematical formulation

Over a field F, V is an abelian additive group with scalar multiplication F×V→V satisfying a(u+v)=au+av, (a+b)v=av+bv, (ab)v=a(bv), and 1v=v. The zero vector space is permitted.

**Lean formulation** (in its source module context):

```lean
abbrev VectorSpace (F : Type u) (V : Type v) [_root_.Field F]
    [AddCommGroup V] := Module F V
```

**Source:** [`Catalog.VectorSpace`](../lean/Catalog/Algebra.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Module F V with Field F and AddCommGroup V explicit; field and additive structure are parameters, not inferred from graph edges.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The additive structure is an abelian Group; scalar action satisfies (ab)v=a(bv), 1v=v, a(u+v)=au+av and (a+b)v=av+bv.

**basisKind:** defined-structure

**basisScope:** Algebraic vector spaces over arbitrary commutative fields, with total exact operations; no topology or norm is implicit.

**basisInstantiation:** Instantiate Group using multiplication x*y := x+y, identity 0_V and inverse −x on V. Require commutativity of this additive reduct, then impose the stated field-action axioms.

**specializationNote:** Retain (V,+,0_V,−) as the underlying additive group; forget the scalar action. The additive group is additionally commutative.

**verificationObligation:** V contains 0_V and may be the zero-dimensional one-element space, never the empty set. F is a nontrivial field. No finite-dimensionality is assumed unless a claim requires it.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-VectorSpace-add"></a>

### add

`urn:csabs:operation/VectorSpace-add`

**signature:** V×V → V

**description:** Add vectors in the same vector space.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Add vectors in the same vector space.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-VectorSpace-negate"></a>

### negate

`urn:csabs:operation/VectorSpace-negate`

**signature:** V → V

**description:** Take the additive inverse.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Take the additive inverse.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-VectorSpace-scale"></a>

### scale

`urn:csabs:operation/VectorSpace-scale`

**signature:** F×V → V

**description:** Multiply a vector by a scalar in its specified field.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Multiply a vector by a scalar in its specified field.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-VectorSpace-additive-structure"></a>

### additive-structure

`urn:csabs:axiom/VectorSpace-additive-structure`

**statement:** The named additive reduct is a commutative group.

**formalStatement:** (V,+,0_V,−) is a Group and ∀u,v∈V:u+v=v+u

**assumptions:** V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: semimodule and module axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Axler Definition 1.20; Module over a field

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-VectorSpace-scalar-action"></a>

### scalar-action

`urn:csabs:axiom/VectorSpace-scalar-action`

**statement:** Scalar multiplication is an associative unital action.

**formalStatement:** ∀a,b∈F,v∈V:(ab)v=a(bv) and 1_Fv=v

**assumptions:** V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: semimodule and module axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Axler Definition 1.20; Module

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-VectorSpace-distributivity"></a>

### distributivity

`urn:csabs:axiom/VectorSpace-distributivity`

**statement:** Scalar multiplication distributes over both additions.

**formalStatement:** ∀a,b∈F,u,v∈V:a(u+v)=au+av and (a+b)v=av+bv

**assumptions:** V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: semimodule and module axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Axler Definition 1.20; Module

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-VectorSpace-zero-scalar"></a>

### zero-scalar

`urn:csabs:theorem/VectorSpace-zero-scalar`

**statement:** Zero scalar annihilates every vector and every scalar annihilates the zero vector.

**formalStatement:** ∀a∈F,v∈V:0_Fv=0_V and a0_V=0_V

**assumptions:** V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V; Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/; [Mathlib: semimodule and module axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Axler §1B, elementary vector-space properties

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [additive-structure](VectorSpace.md#node-urn-csabs-axiom-VectorSpace-additive-structure); [distributivity](VectorSpace.md#node-urn-csabs-axiom-VectorSpace-distributivity); [scale](VectorSpace.md#node-urn-csabs-operation-VectorSpace-scale)

**proofSketch:** The scalar distributivity identity 0v=(0+0)v=0v+0v yields 0v=0_V by group cancellation. Similarly a0_V=a(0_V+0_V)=a0_V+a0_V.

## Concept provenance

- [Sheldon Axler, Linear Algebra Done Right, fourth edition (consulted revision dated 30 October 2026)](https://linear.axler.net/LADR4e.pdf); accessedOn: 2026-11-07; sourceRole: primary mathematical reference; license: CC BY-NC 4.0; licenseUrl: https://creativecommons.org/licenses/by-nc/4.0/
- [Mathlib: semimodule and module axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Axler §1B, Definition 1.20; Mathlib Module (specialized to a field)

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/VectorSpace",
    "type": "Concept",
    "shortForm": "VectorSpace",
    "fullName": "Vector space over a field",
    "category": [
      "urn:csabs:category/linear-algebra",
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An additive abelian group V equipped with scalar multiplication by a specified field F satisfying scalar associativity, identity and both distributive laws.",
    "notation": "V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V",
    "hasOperation": [
      "urn:csabs:operation/VectorSpace-add",
      "urn:csabs:operation/VectorSpace-negate",
      "urn:csabs:operation/VectorSpace-scale"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/VectorSpace-additive-structure",
      "urn:csabs:axiom/VectorSpace-scalar-action",
      "urn:csabs:axiom/VectorSpace-distributivity"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/VectorSpace-zero-scalar"
    ],
    "axiomBasis": "The additive structure is an abelian Group; scalar action satisfies (ab)v=a(bv), 1v=v, a(u+v)=au+av and (a+b)v=av+bv.",
    "basisKind": "defined-structure",
    "basisScope": "Algebraic vector spaces over arbitrary commutative fields, with total exact operations; no topology or norm is implicit.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Field",
      "urn:csabs:concept/Group"
    ],
    "verificationObligation": [
      "V contains 0_V and may be the zero-dimensional one-element space, never the empty set. F is a nontrivial field. No finite-dimensionality is assumed unless a claim requires it.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-module-defs"
    ],
    "sourceLocator": "Axler §1B, Definition 1.20; Mathlib Module (specialized to a field)",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Group"
    ],
    "specializationNote": "Retain (V,+,0_V,−) as the underlying additive group; forget the scalar action. The additive group is additionally commutative.",
    "basisInstantiation": "Instantiate Group using multiplication x*y := x+y, identity 0_V and inverse −x on V. Require commutativity of this additive reduct, then impose the stated field-action axioms.",
    "leanFormulation": "abbrev VectorSpace (F : Type u) (V : Type v) [_root_.Field F]\n    [AddCommGroup V] := Module F V",
    "formulationSource": "urn:csabs:source/local-lean-Algebra",
    "formulationLocator": "Catalog.VectorSpace",
    "formulationScope": "model",
    "leanModelMapping": "Module F V with Field F and AddCommGroup V explicit; field and additive structure are parameters, not inferred from graph edges.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Over a field F, V is an abelian additive group with scalar multiplication F×V→V satisfying a(u+v)=au+av, (a+b)v=av+bv, (ab)v=a(bv), and 1v=v. The zero vector space is permitted."
  },
  {
    "id": "urn:csabs:operation/VectorSpace-add",
    "type": "Operation",
    "name": "add",
    "signature": "V×V → V",
    "description": "Add vectors in the same vector space.",
    "concept": "urn:csabs:concept/VectorSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Add vectors in the same vector space.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/VectorSpace-negate",
    "type": "Operation",
    "name": "negate",
    "signature": "V → V",
    "description": "Take the additive inverse.",
    "concept": "urn:csabs:concept/VectorSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Take the additive inverse.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/VectorSpace-scale",
    "type": "Operation",
    "name": "scale",
    "signature": "F×V → V",
    "description": "Multiply a vector by a scalar in its specified field.",
    "concept": "urn:csabs:concept/VectorSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Multiply a vector by a scalar in its specified field.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/VectorSpace-additive-structure",
    "type": "Axiom",
    "name": "additive-structure",
    "statement": "The named additive reduct is a commutative group.",
    "formalStatement": "(V,+,0_V,−) is a Group and ∀u,v∈V:u+v=v+u",
    "appliesTo": [
      "urn:csabs:concept/VectorSpace"
    ],
    "assumptions": [
      "V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-module-defs"
    ],
    "sourceLocator": "Axler Definition 1.20; Module over a field",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/VectorSpace-scalar-action",
    "type": "Axiom",
    "name": "scalar-action",
    "statement": "Scalar multiplication is an associative unital action.",
    "formalStatement": "∀a,b∈F,v∈V:(ab)v=a(bv) and 1_Fv=v",
    "appliesTo": [
      "urn:csabs:concept/VectorSpace"
    ],
    "assumptions": [
      "V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-module-defs"
    ],
    "sourceLocator": "Axler Definition 1.20; Module",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/VectorSpace-distributivity",
    "type": "Axiom",
    "name": "distributivity",
    "statement": "Scalar multiplication distributes over both additions.",
    "formalStatement": "∀a,b∈F,u,v∈V:a(u+v)=au+av and (a+b)v=av+bv",
    "appliesTo": [
      "urn:csabs:concept/VectorSpace"
    ],
    "assumptions": [
      "V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-module-defs"
    ],
    "sourceLocator": "Axler Definition 1.20; Module",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:theorem/VectorSpace-zero-scalar",
    "type": "Theorem",
    "name": "zero-scalar",
    "statement": "Zero scalar annihilates every vector and every scalar annihilates the zero vector.",
    "formalStatement": "∀a∈F,v∈V:0_Fv=0_V and a0_V=0_V",
    "appliesTo": [
      "urn:csabs:concept/VectorSpace"
    ],
    "assumptions": [
      "V over field F; +:V²→V; 0_V∈V; −:V→V; ·:F×V→V",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/axler-ladr4",
      "urn:csabs:source/mathlib-module-defs"
    ],
    "sourceLocator": "Axler §1B, elementary vector-space properties",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/VectorSpace-additive-structure",
      "urn:csabs:axiom/VectorSpace-distributivity",
      "urn:csabs:operation/VectorSpace-scale"
    ],
    "proofSketch": "The scalar distributivity identity 0v=(0+0)v=0v+0v yields 0v=0_V by group cancellation. Similarly a0_V=a(0_V+0_V)=a0_V+a0_V."
  }
]
```
<!-- graph-record:end -->
