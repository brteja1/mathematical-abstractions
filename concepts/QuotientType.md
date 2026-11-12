# Quotient by an equivalence relation

Equivalence classes of values under a fixed equivalence relation, with elimination restricted to invariant functions.

**Notation:** A/≈; [a]∈A/≈

**Stable ID:** `urn:csabs:concept/QuotientType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Equivalence relation](EquivalenceRelation.md)

## Mathematical formulation

For an equivalence relation ≈ on A, A/≈ has classes [a] with [a]=[b] iff a≈b. A map f:A→B descends to the quotient only if a≈b⇒f(a)=f(b).

**Lean formulation** (in its source module context):

```lean
abbrev QuotientType (A : Type u) (r : Setoid A) := Quotient r
```

**Source:** [`Catalog.QuotientType`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Quotient r for a Setoid r on A; Quotient.mk/lift require invariant maps. A/≈; [a]∈A/≈. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** [a]=[b] ⇔ a≈b; ∀q:A/≈, ∃a:A, q=[a]; If f respects ≈, lift(f)([a])=f(a)

**basisKind:** extensional-structural-definition

**basisScope:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-QuotientType-class"></a>

### class

`urn:csabs:operation/QuotientType-class`

**signature:** class : A→A/≈

**description:** Maps a to [a].

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Maps a to [a].

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-QuotientType-lift"></a>

### lift

`urn:csabs:operation/QuotientType-lift`

**signature:** lift : {f:A→B | ∀a≈b, f(a)=f(b)}→(A/≈→B)

**description:** lift(f)([a])=f(a); invariant f only.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** lift(f)([a])=f(a); invariant f only.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-QuotientType-class-equality"></a>

### class-equality

`urn:csabs:axiom/QuotientType-class-equality`

**statement:** Defining requirement: [a]=[b] ⇔ a≈b

**formalStatement:** [a]=[b] ⇔ a≈b

**assumptions:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-QuotientType-surjective"></a>

### surjective

`urn:csabs:axiom/QuotientType-surjective`

**statement:** Defining requirement: ∀q:A/≈, ∃a:A, q=[a]

**formalStatement:** ∀q:A/≈, ∃a:A, q=[a]

**assumptions:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-QuotientType-lift-beta"></a>

### lift-beta

`urn:csabs:axiom/QuotientType-lift-beta`

**statement:** Defining requirement: If f respects ≈, lift(f)([a])=f(a)

**formalStatement:** If f respects ≈, lift(f)([a])=f(a)

**assumptions:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-QuotientType-lift-unique"></a>

### lift-unique

`urn:csabs:law/QuotientType-lift-unique`

**statement:** (∀a, g([a])=f(a)) ⇒ g=lift(f), for invariant f

**formalStatement:** (∀a, g([a])=f(a)) ⇒ g=lift(f), for invariant f

**assumptions:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [surjective](QuotientType.md#node-urn-csabs-axiom-QuotientType-surjective); [lift-beta](QuotientType.md#node-urn-csabs-axiom-QuotientType-lift-beta)

**proofSketch:** Choose a representative of each q by surjectivity, apply beta, and use function extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-QuotientType-equality-quotient"></a>

### equality-quotient

`urn:csabs:theorem/QuotientType-equality-quotient`

**statement:** If a≈b ⇔ a=b, then A/≈ ≅ A

**formalStatement:** If a≈b ⇔ a=b, then A/≈ ≅ A

**assumptions:** ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [class-equality](QuotientType.md#node-urn-csabs-axiom-QuotientType-class-equality); [surjective](QuotientType.md#node-urn-csabs-axiom-QuotientType-surjective); [lift-beta](QuotientType.md#node-urn-csabs-axiom-QuotientType-lift-beta)

**proofSketch:** The identity respects ≈; its lift and class map are inverse using beta and surjectivity.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/QuotientType",
    "type": "Concept",
    "shortForm": "QuotientType",
    "fullName": "Quotient by an equivalence relation",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "Equivalence classes of values under a fixed equivalence relation, with elimination restricted to invariant functions.",
    "notation": "A/≈; [a]∈A/≈",
    "requiresConcept": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/QuotientType-class",
      "urn:csabs:operation/QuotientType-lift"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/QuotientType-class-equality",
      "urn:csabs:axiom/QuotientType-surjective",
      "urn:csabs:axiom/QuotientType-lift-beta"
    ],
    "hasLaw": [
      "urn:csabs:law/QuotientType-lift-unique"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/QuotientType-equality-quotient"
    ],
    "axiomBasis": "[a]=[b] ⇔ a≈b; ∀q:A/≈, ∃a:A, q=[a]; If f respects ≈, lift(f)([a])=f(a)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev QuotientType (A : Type u) (r : Setoid A) := Quotient r",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.QuotientType",
    "formulationScope": "model",
    "leanModelMapping": "Quotient r for a Setoid r on A; Quotient.mk/lift require invariant maps. A/≈; [a]∈A/≈. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "For an equivalence relation ≈ on A, A/≈ has classes [a] with [a]=[b] iff a≈b. A map f:A→B descends to the quotient only if a≈b⇒f(a)=f(b)."
  },
  {
    "id": "urn:csabs:operation/QuotientType-class",
    "type": "Operation",
    "name": "class",
    "signature": "class : A→A/≈",
    "description": "Maps a to [a].",
    "concept": "urn:csabs:concept/QuotientType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Maps a to [a].",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/QuotientType-lift",
    "type": "Operation",
    "name": "lift",
    "signature": "lift : {f:A→B | ∀a≈b, f(a)=f(b)}→(A/≈→B)",
    "description": "lift(f)([a])=f(a); invariant f only.",
    "concept": "urn:csabs:concept/QuotientType",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. ≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "lift(f)([a])=f(a); invariant f only.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/QuotientType-class-equality",
    "type": "Axiom",
    "name": "class-equality",
    "statement": "Defining requirement: [a]=[b] ⇔ a≈b",
    "formalStatement": "[a]=[b] ⇔ a≈b",
    "assumptions": [
      "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/QuotientType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/QuotientType-surjective",
    "type": "Axiom",
    "name": "surjective",
    "statement": "Defining requirement: ∀q:A/≈, ∃a:A, q=[a]",
    "formalStatement": "∀q:A/≈, ∃a:A, q=[a]",
    "assumptions": [
      "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/QuotientType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/QuotientType-lift-beta",
    "type": "Axiom",
    "name": "lift-beta",
    "statement": "Defining requirement: If f respects ≈, lift(f)([a])=f(a)",
    "formalStatement": "If f respects ≈, lift(f)([a])=f(a)",
    "assumptions": [
      "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/QuotientType"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/QuotientType-lift-unique",
    "type": "Law",
    "name": "lift-unique",
    "statement": "(∀a, g([a])=f(a)) ⇒ g=lift(f), for invariant f",
    "formalStatement": "(∀a, g([a])=f(a)) ⇒ g=lift(f), for invariant f",
    "assumptions": [
      "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/QuotientType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/QuotientType-surjective",
      "urn:csabs:axiom/QuotientType-lift-beta"
    ],
    "proofSketch": "Choose a representative of each q by surjectivity, apply beta, and use function extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/QuotientType-equality-quotient",
    "type": "Theorem",
    "name": "equality-quotient",
    "statement": "If a≈b ⇔ a=b, then A/≈ ≅ A",
    "formalStatement": "If a≈b ⇔ a=b, then A/≈ ≅ A",
    "assumptions": [
      "≈ must be reflexive, symmetric and transitive. No canonical representative or computable equality is promised. Equality is class equality, not equality of representatives.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/QuotientType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/QuotientType-class-equality",
      "urn:csabs:axiom/QuotientType-surjective",
      "urn:csabs:axiom/QuotientType-lift-beta"
    ],
    "proofSketch": "The identity respects ≈; its lift and class map are inverse using beta and surjectivity.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
