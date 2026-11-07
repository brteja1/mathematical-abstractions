# Dependent function (Pi type)

A total function choosing a value in B(a) at each input a.

**Notation:** Πa:A. B(a)

**Stable ID:** `urn:csabs:concept/DependentFunction`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Function type](FunctionType.md)

## Backlinks

- [Finite typed entity-relationship instance](EntityRelationshipModel.md) — `requiresConcept`
- [Function type](FunctionType.md) — `specializationOf`
- [Free ranked term algebra with variables](TermAlgebra.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** (λa.t(a))(x)=t(x); f=g ⇔ ∀a:A, f(a)=g(a)

**basisKind:** extensional-structural-definition

**basisScope:** Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DependentFunction-abstract"></a>

### abstract

`urn:csabs:operation/DependentFunction-abstract`

**signature:** lambda : ((a:A)↦t(a):B(a))→Πa:A.B(a)

**description:** Forms a function from a typed expression.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Forms a function from a typed expression.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DependentFunction-apply"></a>

### apply

`urn:csabs:operation/DependentFunction-apply`

**signature:** apply : (Πa:A.B(a))→(a:A)→B(a)

**description:** Applies a dependent function.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Applies a dependent function.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DependentFunction-beta"></a>

### beta

`urn:csabs:axiom/DependentFunction-beta`

**statement:** Defining requirement: (λa.t(a))(x)=t(x)

**formalStatement:** (λa.t(a))(x)=t(x)

**assumptions:** Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DependentFunction-extensionality"></a>

### extensionality

`urn:csabs:axiom/DependentFunction-extensionality`

**statement:** Defining requirement: f=g ⇔ ∀a:A, f(a)=g(a)

**formalStatement:** f=g ⇔ ∀a:A, f(a)=g(a)

**assumptions:** Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DependentFunction-eta"></a>

### eta

`urn:csabs:law/DependentFunction-eta`

**statement:** (λa.f(a))=f

**formalStatement:** (λa.f(a))=f

**assumptions:** Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [beta](DependentFunction.md#node-urn-csabs-axiom-DependentFunction-beta); [extensionality](DependentFunction.md#node-urn-csabs-axiom-DependentFunction-extensionality)

**proofSketch:** Every application agrees by beta; use extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-DependentFunction-empty-domain"></a>

### empty-domain

`urn:csabs:theorem/DependentFunction-empty-domain`

**statement:** If A is empty, any f,g:Πa:A.B(a) satisfy f=g

**formalStatement:** If A is empty, any f,g:Πa:A.B(a) satisfy f=g

**assumptions:** Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [extensionality](DependentFunction.md#node-urn-csabs-axiom-DependentFunction-extensionality)

**proofSketch:** The pointwise obligation is vacuous; extensionality gives equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Theorem Proving in Lean 4: Dependent Type Theory](https://lean-lang.org/theorem_proving_in_lean4/Dependent-Type-Theory/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Theorem Proving in Lean 4: Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DependentFunction",
    "type": "Concept",
    "shortForm": "DependentFunction",
    "fullName": "Dependent function (Pi type)",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "A total function choosing a value in B(a) at each input a.",
    "notation": "Πa:A. B(a)",
    "requiresConcept": [
      "urn:csabs:concept/FunctionType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DependentFunction-abstract",
      "urn:csabs:operation/DependentFunction-apply"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DependentFunction-beta",
      "urn:csabs:axiom/DependentFunction-extensionality"
    ],
    "hasLaw": [
      "urn:csabs:law/DependentFunction-eta"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DependentFunction-empty-domain"
    ],
    "axiomBasis": "(λa.t(a))(x)=t(x); f=g ⇔ ∀a:A, f(a)=g(a)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentFunction-abstract",
    "type": "Operation",
    "name": "abstract",
    "signature": "lambda : ((a:A)↦t(a):B(a))→Πa:A.B(a)",
    "description": "Forms a function from a typed expression.",
    "concept": "urn:csabs:concept/DependentFunction",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Forms a function from a typed expression.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DependentFunction-apply",
    "type": "Operation",
    "name": "apply",
    "signature": "apply : (Πa:A.B(a))→(a:A)→B(a)",
    "description": "Applies a dependent function.",
    "concept": "urn:csabs:concept/DependentFunction",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Applies a dependent function.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentFunction-beta",
    "type": "Axiom",
    "name": "beta",
    "statement": "Defining requirement: (λa.t(a))(x)=t(x)",
    "formalStatement": "(λa.t(a))(x)=t(x)",
    "assumptions": [
      "Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentFunction"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DependentFunction-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Defining requirement: f=g ⇔ ∀a:A, f(a)=g(a)",
    "formalStatement": "f=g ⇔ ∀a:A, f(a)=g(a)",
    "assumptions": [
      "Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentFunction"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DependentFunction-eta",
    "type": "Law",
    "name": "eta",
    "statement": "(λa.f(a))=f",
    "formalStatement": "(λa.f(a))=f",
    "assumptions": [
      "Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentFunction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DependentFunction-beta",
      "urn:csabs:axiom/DependentFunction-extensionality"
    ],
    "proofSketch": "Every application agrees by beta; use extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/DependentFunction-empty-domain",
    "type": "Theorem",
    "name": "empty-domain",
    "statement": "If A is empty, any f,g:Πa:A.B(a) satisfy f=g",
    "formalStatement": "If A is empty, any f,g:Πa:A.B(a) satisfy f=g",
    "assumptions": [
      "Extensional equality: f=g iff all typed applications agree. No effects, divergence or partiality. Empty A gives one function; some empty fibers may prevent inhabitants.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DependentFunction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DependentFunction-extensionality"
    ],
    "proofSketch": "The pointwise obligation is vacuous; extensionality gives equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/lean4-dependent-types",
      "urn:csabs:source/lean4-quotients"
    ],
    "sourceLocator": "§§2.3, 2.8: abstraction, application, Pi and Sigma types; §§12.3–12.4: function extensionality and quotients of setoids",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
