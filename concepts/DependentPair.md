# Dependent pair (Sigma type)

A pair whose second component lies in a carrier selected by its first component.

**Notation:** Σa:A. B(a)

**Stable ID:** `urn:csabs:concept/DependentPair`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Product Type](ProductType.md)

## Backlinks

- [Product Type](ProductType.md) — `specializationOf`
- [Free ranked term algebra with variables](TermAlgebra.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** fst(pair(a,b))=a ∧ snd(pair(a,b))=b; elim_k(pair(a,b))=k(a,b); p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)

**basisKind:** extensional-structural-definition

**basisScope:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DependentPair-pair"></a>

### pair

`urn:csabs:operation/DependentPair-pair`

**signature:** pair : (a:A)→B(a)→Σa:A.B(a)

**description:** Constructs a dependent pair.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs a dependent pair.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DependentPair-first"></a>

### first

`urn:csabs:operation/DependentPair-first`

**signature:** fst : (Σa:A.B(a))→A

**description:** fst(pair(a,b))=a.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** fst(pair(a,b))=a.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DependentPair-second"></a>

### second

`urn:csabs:operation/DependentPair-second`

**signature:** snd : (p:Σa:A.B(a))→B(fst(p))

**description:** snd(pair(a,b))=b.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** snd(pair(a,b))=b.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DependentPair-eliminate"></a>

### eliminate

`urn:csabs:operation/DependentPair-eliminate`

**signature:** elim_k : (Σa:A.B(a))→C

**description:** For total k:(a:A)→B(a)→C, elim_k(pair(a,b))=k(a,b).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** For total k:(a:A)→B(a)→C, elim_k(pair(a,b))=k(a,b).

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DependentPair-projections"></a>

### projections

`urn:csabs:axiom/DependentPair-projections`

**statement:** Defining requirement: fst(pair(a,b))=a ∧ snd(pair(a,b))=b

**formalStatement:** fst(pair(a,b))=a ∧ snd(pair(a,b))=b

**assumptions:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DependentPair-elimination"></a>

### elimination

`urn:csabs:axiom/DependentPair-elimination`

**statement:** Defining requirement: elim_k(pair(a,b))=k(a,b)

**formalStatement:** elim_k(pair(a,b))=k(a,b)

**assumptions:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DependentPair-extensionality"></a>

### extensionality

`urn:csabs:axiom/DependentPair-extensionality`

**statement:** Defining requirement: p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)

**formalStatement:** p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)

**assumptions:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DependentPair-eta"></a>

### eta

`urn:csabs:law/DependentPair-eta`

**statement:** pair(fst(p),snd(p))=p

**formalStatement:** pair(fst(p),snd(p))=p

**assumptions:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [projections](DependentPair.md#node-urn-csabs-axiom-DependentPair-projections); [extensionality](DependentPair.md#node-urn-csabs-axiom-DependentPair-extensionality)

**proofSketch:** Apply dependent-pair extensionality, using reflexive index equality and the projection equations.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-DependentPair-constant-family"></a>

### constant-family

`urn:csabs:theorem/DependentPair-constant-family`

**statement:** If B(a)=C for every a, Σa:A.B(a) ≅ A×C

**formalStatement:** If B(a)=C for every a, Σa:A.B(a) ≅ A×C

**assumptions:** B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [projections](DependentPair.md#node-urn-csabs-axiom-DependentPair-projections); [extensionality](DependentPair.md#node-urn-csabs-axiom-DependentPair-extensionality)

**proofSketch:** Map both components identically; projection equations and eta establish the inverse laws.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Data/Sigma/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Sigma/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DependentPair",
    "type": "Concept",
    "shortForm": "DependentPair",
    "fullName": "Dependent pair (Sigma type)",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A pair whose second component lies in a carrier selected by its first component.",
    "notation": "Σa:A. B(a)",
    "requiresConcept": [
      "urn:csabs:concept/ProductType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DependentPair-pair",
      "urn:csabs:operation/DependentPair-first",
      "urn:csabs:operation/DependentPair-second",
      "urn:csabs:operation/DependentPair-eliminate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DependentPair-projections",
      "urn:csabs:axiom/DependentPair-elimination",
      "urn:csabs:axiom/DependentPair-extensionality"
    ],
    "hasLaw": [
      "urn:csabs:law/DependentPair-eta"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DependentPair-constant-family"
    ],
    "axiomBasis": "fst(pair(a,b))=a ∧ snd(pair(a,b))=b; elim_k(pair(a,b))=k(a,b); p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentPair-pair",
    "type": "Operation",
    "name": "pair",
    "signature": "pair : (a:A)→B(a)→Σa:A.B(a)",
    "description": "Constructs a dependent pair.",
    "concept": "urn:csabs:concept/DependentPair",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs a dependent pair.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentPair-first",
    "type": "Operation",
    "name": "first",
    "signature": "fst : (Σa:A.B(a))→A",
    "description": "fst(pair(a,b))=a.",
    "concept": "urn:csabs:concept/DependentPair",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "fst(pair(a,b))=a.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentPair-second",
    "type": "Operation",
    "name": "second",
    "signature": "snd : (p:Σa:A.B(a))→B(fst(p))",
    "description": "snd(pair(a,b))=b.",
    "concept": "urn:csabs:concept/DependentPair",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "snd(pair(a,b))=b.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentPair-eliminate",
    "type": "Operation",
    "name": "eliminate",
    "signature": "elim_k : (Σa:A.B(a))→C",
    "description": "For total k:(a:A)→B(a)→C, elim_k(pair(a,b))=k(a,b).",
    "concept": "urn:csabs:concept/DependentPair",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "For total k:(a:A)→B(a)→C, elim_k(pair(a,b))=k(a,b).",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentPair-projections",
    "type": "Axiom",
    "name": "projections",
    "statement": "Defining requirement: fst(pair(a,b))=a ∧ snd(pair(a,b))=b",
    "formalStatement": "fst(pair(a,b))=a ∧ snd(pair(a,b))=b",
    "assumptions": [
      "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentPair"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentPair-elimination",
    "type": "Axiom",
    "name": "elimination",
    "statement": "Defining requirement: elim_k(pair(a,b))=k(a,b)",
    "formalStatement": "elim_k(pair(a,b))=k(a,b)",
    "assumptions": [
      "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentPair"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentPair-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Defining requirement: p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)",
    "formalStatement": "p=q ⇔ ∃h:fst(p)=fst(q), transport_B(h,snd(p))=snd(q)",
    "assumptions": [
      "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentPair"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DependentPair-eta",
    "type": "Law",
    "name": "eta",
    "statement": "pair(fst(p),snd(p))=p",
    "formalStatement": "pair(fst(p),snd(p))=p",
    "assumptions": [
      "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentPair"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DependentPair-projections",
      "urn:csabs:axiom/DependentPair-extensionality"
    ],
    "proofSketch": "Apply dependent-pair extensionality, using reflexive index equality and the projection equations.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/DependentPair-constant-family",
    "type": "Theorem",
    "name": "constant-family",
    "statement": "If B(a)=C for every a, Σa:A.B(a) ≅ A×C",
    "formalStatement": "If B(a)=C for every a, Σa:A.B(a) ≅ A×C",
    "assumptions": [
      "B:A→Type is a family of set-like carriers. Equality of second components across equal indices uses transport. A and fibers may be empty; no decidable equality assumed.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentPair"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DependentPair-projections",
      "urn:csabs:axiom/DependentPair-extensionality"
    ],
    "proofSketch": "Map both components identically; projection equations and eta establish the inverse laws.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/mathlib-sigma-core"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; Sigma.mk.inj_iff, Sigma.eta, Sigma.eq",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
