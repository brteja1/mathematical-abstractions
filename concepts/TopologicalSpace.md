# Topological space (topology on a carrier)

A set X with a family τ of open subsets containing X and closed under arbitrary unions and binary intersections.

**Notation:** (X,τ); τ⊆𝒫(X)

**Stable ID:** `urn:csabs:concept/TopologicalSpace`

**Categories:** Topology

**Kind:** Mathematical structure

**Prerequisites:** [Set](Set.md), [Power set](PowerSet.md)

**Related concepts:** [Measurable space (sigma-algebra on a carrier)](MeasurableSpace.md), [Closure Operator](ClosureOperator.md)

## Backlinks

- [Topological manifold (fixed dimension, without boundary)](Manifold.md) — `requiresConcept`
- [Topological manifold (fixed dimension, without boundary)](Manifold.md) — `specializationOf`

## Mathematical formulation

A topology τ⊆℘(M) contains ∅ and M, is closed under arbitrary unions and finite intersections. Equality compares the collections of open sets; no separation or countability axiom is implicit.

**Lean formulation** (in its source module context):

```lean
abbrev TopologicalSpace (M : Type*) := _root_.TopologicalSpace M
```

**Source:** [`Catalog.TopologicalSpace`](../lean/Catalog/Topology.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib TopologicalSpace with arbitrary-union and finite-intersection open-set axioms.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** The whole carrier is open, arbitrary unions of opens are open, and binary intersections of opens are open.

**basisKind:** defined-structure

**basisScope:** Open and closed sets, interior and closure. Separation and countability are additional constraints.

**verificationObligation:** The empty carrier is allowed. No metric, Hausdorff property or countable basis is assumed. A topology need not be closed under complement.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TopologicalSpace-interior"></a>

### interior

`urn:csabs:operation/TopologicalSpace-interior`

**signature:** 𝒫(X) → 𝒫(X); A ↦ ⋃{U∈τ:U⊆A}

**description:** Return the largest open subset of A.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Return the largest open subset of A.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-TopologicalSpace-closure"></a>

### closure

`urn:csabs:operation/TopologicalSpace-closure`

**signature:** 𝒫(X) → 𝒫(X); A ↦ ⋂{C⊆X:A⊆C and X∖C∈τ}

**description:** Return the smallest closed superset of A.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Return the smallest closed superset of A.

**totality:** total on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TopologicalSpace-whole-open"></a>

### whole-open

`urn:csabs:axiom/TopologicalSpace-whole-open`

**statement:** The whole carrier is open.

**formalStatement:** X∈τ

**assumptions:** (X,τ); τ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TopologicalSpace.isOpen_univ

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-TopologicalSpace-open-unions"></a>

### open-unions

`urn:csabs:axiom/TopologicalSpace-open-unions`

**statement:** Arbitrary unions of open sets are open.

**formalStatement:** 𝒰⊆τ ⇒ ⋃𝒰∈τ

**assumptions:** (X,τ); τ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TopologicalSpace.isOpen_sUnion

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-TopologicalSpace-open-intersection"></a>

### open-intersection

`urn:csabs:axiom/TopologicalSpace-open-intersection`

**statement:** Binary intersections of open sets are open.

**formalStatement:** U,V∈τ ⇒ U∩V∈τ

**assumptions:** (X,τ); τ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TopologicalSpace.isOpen_inter

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-TopologicalSpace-closed-definition"></a>

### closed-definition

`urn:csabs:axiom/TopologicalSpace-closed-definition`

**statement:** A set is closed exactly when its complement is open.

**formalStatement:** C⊆X is closed ⇔ X∖C∈τ

**assumptions:** (X,τ); τ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** IsClosed

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** definition

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-TopologicalSpace-closure-operator"></a>

### closure-operator

`urn:csabs:theorem/TopologicalSpace-closure-operator`

**statement:** Topological closure is an extensive, monotone and idempotent operator on the power set.

**formalStatement:** A⊆cl(A); A⊆B ⇒ cl(A)⊆cl(B); cl(cl(A))=cl(A)

**assumptions:** (X,τ); τ⊆𝒫(X); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** closure (intersection of closed supersets)

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [closure](TopologicalSpace.md#node-urn-csabs-operation-TopologicalSpace-closure); [whole-open](TopologicalSpace.md#node-urn-csabs-axiom-TopologicalSpace-whole-open); [open-unions](TopologicalSpace.md#node-urn-csabs-axiom-TopologicalSpace-open-unions); [closed-definition](TopologicalSpace.md#node-urn-csabs-axiom-TopologicalSpace-closed-definition)

**proofSketch:** Closed sets are closed under arbitrary intersections by complementing open unions. Thus the intersection defining cl(A) is a closed superset of A. Its leastness gives monotonicity and idempotence. The full carrier is closed since the empty union is open.

## Concept provenance

- [Mathlib: Basic definitions about topological spaces](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** TopologicalSpace; IsOpen; interior; closure

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TopologicalSpace",
    "type": "Concept",
    "shortForm": "TopologicalSpace",
    "fullName": "Topological space (topology on a carrier)",
    "category": [
      "urn:csabs:category/topology"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A set X with a family τ of open subsets containing X and closed under arbitrary unions and binary intersections.",
    "notation": "(X,τ); τ⊆𝒫(X)",
    "hasOperation": [
      "urn:csabs:operation/TopologicalSpace-interior",
      "urn:csabs:operation/TopologicalSpace-closure"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TopologicalSpace-whole-open",
      "urn:csabs:axiom/TopologicalSpace-open-unions",
      "urn:csabs:axiom/TopologicalSpace-open-intersection",
      "urn:csabs:axiom/TopologicalSpace-closed-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/TopologicalSpace-closure-operator"
    ],
    "axiomBasis": "The whole carrier is open, arbitrary unions of opens are open, and binary intersections of opens are open.",
    "basisKind": "defined-structure",
    "basisScope": "Open and closed sets, interior and closure. Separation and countability are additional constraints.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/PowerSet"
    ],
    "verificationObligation": [
      "The empty carrier is allowed. No metric, Hausdorff property or countable basis is assumed. A topology need not be closed under complement.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "TopologicalSpace; IsOpen; interior; closure",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "relatedConcept": [
      "urn:csabs:concept/MeasurableSpace",
      "urn:csabs:concept/ClosureOperator"
    ],
    "leanFormulation": "abbrev TopologicalSpace (M : Type*) := _root_.TopologicalSpace M",
    "formulationSource": "urn:csabs:source/local-lean-Topology",
    "formulationLocator": "Catalog.TopologicalSpace",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib TopologicalSpace with arbitrary-union and finite-intersection open-set axioms.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A topology τ⊆℘(M) contains ∅ and M, is closed under arbitrary unions and finite intersections. Equality compares the collections of open sets; no separation or countability axiom is implicit."
  },
  {
    "id": "urn:csabs:operation/TopologicalSpace-interior",
    "type": "Operation",
    "name": "interior",
    "signature": "𝒫(X) → 𝒫(X); A ↦ ⋃{U∈τ:U⊆A}",
    "description": "Return the largest open subset of A.",
    "concept": "urn:csabs:concept/TopologicalSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Return the largest open subset of A.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/TopologicalSpace-closure",
    "type": "Operation",
    "name": "closure",
    "signature": "𝒫(X) → 𝒫(X); A ↦ ⋂{C⊆X:A⊆C and X∖C∈τ}",
    "description": "Return the smallest closed superset of A.",
    "concept": "urn:csabs:concept/TopologicalSpace",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Return the smallest closed superset of A.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/TopologicalSpace-whole-open",
    "type": "Axiom",
    "name": "whole-open",
    "statement": "The whole carrier is open.",
    "formalStatement": "X∈τ",
    "appliesTo": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "assumptions": [
      "(X,τ); τ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "TopologicalSpace.isOpen_univ",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/TopologicalSpace-open-unions",
    "type": "Axiom",
    "name": "open-unions",
    "statement": "Arbitrary unions of open sets are open.",
    "formalStatement": "𝒰⊆τ ⇒ ⋃𝒰∈τ",
    "appliesTo": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "assumptions": [
      "(X,τ); τ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "TopologicalSpace.isOpen_sUnion",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/TopologicalSpace-open-intersection",
    "type": "Axiom",
    "name": "open-intersection",
    "statement": "Binary intersections of open sets are open.",
    "formalStatement": "U,V∈τ ⇒ U∩V∈τ",
    "appliesTo": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "assumptions": [
      "(X,τ); τ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "TopologicalSpace.isOpen_inter",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/TopologicalSpace-closed-definition",
    "type": "Axiom",
    "name": "closed-definition",
    "statement": "A set is closed exactly when its complement is open.",
    "formalStatement": "C⊆X is closed ⇔ X∖C∈τ",
    "appliesTo": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "assumptions": [
      "(X,τ); τ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "IsClosed",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "definition"
  },
  {
    "id": "urn:csabs:theorem/TopologicalSpace-closure-operator",
    "type": "Theorem",
    "name": "closure-operator",
    "statement": "Topological closure is an extensive, monotone and idempotent operator on the power set.",
    "formalStatement": "A⊆cl(A); A⊆B ⇒ cl(A)⊆cl(B); cl(cl(A))=cl(A)",
    "appliesTo": [
      "urn:csabs:concept/TopologicalSpace"
    ],
    "assumptions": [
      "(X,τ); τ⊆𝒫(X)",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-topology-defs"
    ],
    "sourceLocator": "closure (intersection of closed supersets)",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:operation/TopologicalSpace-closure",
      "urn:csabs:axiom/TopologicalSpace-whole-open",
      "urn:csabs:axiom/TopologicalSpace-open-unions",
      "urn:csabs:axiom/TopologicalSpace-closed-definition"
    ],
    "proofSketch": "Closed sets are closed under arbitrary intersections by complementing open unions. Thus the intersection defining cl(A) is a closed superset of A. Its leastness gives monotonicity and idempotence. The full carrier is closed since the empty union is open."
  }
]
```
<!-- graph-record:end -->
