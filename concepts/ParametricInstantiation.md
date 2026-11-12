# Contextual parametric declaration instantiation

A staged relation connecting a parameterized declaration and valid argument binding to substitution, declaration/body checks and an instance observation in a fixed language context.

**Notation:** Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ θ=bindNames(D,a) ∧ realizes(Γ,θ,D,I)

**Stable ID:** `urn:csabs:concept/ParametricInstantiation`

**Categories:** Programming-language semantics → Generic programming

**Kind:** semantic-model

**Prerequisites:** [Finite kinded generic parameter signature](GenericSignature.md), [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md), [Binary relation](Relation.md)

**Related concepts:** [Dependent function (Pi type)](DependentFunction.md), [Kinded partial template metafunction](TemplateMetafunction.md), [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md), [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md)

## Backlinks

- [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md) — `relatedConcept`
- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `requiresConcept`
- [Java generic inference constraints and resolution obligations](JavaTypeInference.md) — `relatedConcept`
- [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md) — `requiresConcept`

## Mathematical formulation

Inst(env,decl,args,value) ⇔ kindCorrect(signature(decl),args)∧admissible(env,decl,args)∧realizes(env,decl,zip(parameterNames,args),value). realizes is a supplied relation; determinism, hygienic substitution and language-specific phase semantics are not implicit.

**Lean formulation** (in its source module context):

```lean
structure ParametricInstantiation (Env Decl Name Kind Arg Instance : Type u) where
  signature : Decl → GenericSignature Name Kind Arg
  admissible : Env → Decl → List Arg → Prop
  realizes : Env → Decl → List (Name × Arg) → Instance → Prop
```

**Source:** [`Catalog.Generics.ParametricInstantiation`](../lean/Catalog/GenericProgramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Explicit signature, admissibility and realization relation with simultaneous name/argument zip. Instantiation remains a relation, allowing fresh/generative instance identities.

**Limits:** Actual syntax substitution, binder hygiene, language body semantics and realization/instance identity are supplied. A complete shared substitution calculus is not implemented.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I). bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.

**basisKind:** extensional-structural-definition

**basisScope:** Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ParametricInstantiation-substitute"></a>

### substitute

`urn:csabs:operation/ParametricInstantiation-substitute`

**signature:** substitute : Γ×Binding×Syntax⇀Syntax

**description:** Apply simultaneous declaration-identity substitution with language-specific binder hygiene and scope checking.

**precondition:** The supplied language substitution is defined for this syntax and binding.

**postcondition:** Apply simultaneous declaration-identity substitution with language-specific binder hygiene and scope checking.

**totality:** Partial language adapter; textual search/replace is not the specified operation.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ParametricInstantiation-instantiate"></a>

### instantiate

`urn:csabs:operation/ParametricInstantiation-instantiate`

**signature:** instantiate : Γ×Declaration×Args×Instance→Prop

**description:** Relate an instance only when signature kinds, full argument admissibility and the language realization relation all hold.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Relate an instance only when signature kinds, full argument admissibility and the language realization relation all hold.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ParametricInstantiation-instantiation-relation"></a>

### instantiation-relation

`urn:csabs:axiom/ParametricInstantiation-instantiation-relation`

**statement:** Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I).

**formalStatement:** Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I).

**assumptions:** Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-ParametricInstantiation-simultaneous-substitution"></a>

### simultaneous-substitution

`urn:csabs:axiom/ParametricInstantiation-simultaneous-substitution`

**statement:** bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.

**formalStatement:** bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.

**assumptions:** Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-ParametricInstantiation-inadmissible-no-instance"></a>

### inadmissible-no-instance

`urn:csabs:law/ParametricInstantiation-inadmissible-no-instance`

**statement:** ¬kindCorrect(sig(D),a) ∨ ¬admissible(Γ,D,a) ⇒ ¬∃I,Instantiate(Γ,D,a,I).

**formalStatement:** ¬kindCorrect(sig(D),a) ∨ ¬admissible(Γ,D,a) ⇒ ¬∃I,Instantiate(Γ,D,a,I).

**assumptions:** Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [instantiation-relation](ParametricInstantiation.md#node-urn-csabs-axiom-ParametricInstantiation-instantiation-relation)

**proofSketch:** Every realization requires both conjuncts, so either failed prerequisite excludes all related instances.

<a id="node-urn-csabs-law-ParametricInstantiation-instance-projection"></a>

### instance-projection

`urn:csabs:law/ParametricInstantiation-instance-projection`

**statement:** Instantiate(Γ,D,a,I) ⇒ realizes(Γ,bindNames(D,a),D,I).

**formalStatement:** Instantiate(Γ,D,a,I) ⇒ realizes(Γ,bindNames(D,a),D,I).

**assumptions:** Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [instantiation-relation](ParametricInstantiation.md#node-urn-csabs-axiom-ParametricInstantiation-instantiation-relation); [simultaneous-substitution](ParametricInstantiation.md#node-urn-csabs-axiom-ParametricInstantiation-simultaneous-substitution)

**proofSketch:** Project the realization conjunct using the explicit simultaneous binding; no uniqueness or runtime code-generation consequence follows.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]

**sourceNote:** Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ParametricInstantiation",
    "type": "Concept",
    "shortForm": "ParametricInstantiation",
    "fullName": "Contextual parametric declaration instantiation",
    "definition": "A staged relation connecting a parameterized declaration and valid argument binding to substitution, declaration/body checks and an instance observation in a fixed language context.",
    "notation": "Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ θ=bindNames(D,a) ∧ realizes(Γ,θ,D,I)",
    "category": [
      "urn:csabs:category/generic-programming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/GenericSignature",
      "urn:csabs:concept/GenericArgumentBinding",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DependentFunction",
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/JavaParameterizedType",
      "urn:csabs:concept/VHDLGenericElaboration"
    ],
    "hasOperation": [
      "urn:csabs:operation/ParametricInstantiation-substitute",
      "urn:csabs:operation/ParametricInstantiation-instantiate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ParametricInstantiation-instantiation-relation",
      "urn:csabs:axiom/ParametricInstantiation-simultaneous-substitution"
    ],
    "hasLaw": [
      "urn:csabs:law/ParametricInstantiation-inadmissible-no-instance",
      "urn:csabs:law/ParametricInstantiation-instance-projection"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I). bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.",
    "leanFormulation": "structure ParametricInstantiation (Env Decl Name Kind Arg Instance : Type u) where\n  signature : Decl → GenericSignature Name Kind Arg\n  admissible : Env → Decl → List Arg → Prop\n  realizes : Env → Decl → List (Name × Arg) → Instance → Prop",
    "formulationSource": "urn:csabs:source/local-lean-GenericProgramming",
    "formulationLocator": "Catalog.Generics.ParametricInstantiation",
    "formulationScope": "partial",
    "leanModelMapping": "Explicit signature, admissibility and realization relation with simultaneous name/argument zip. Instantiation remains a relation, allowing fresh/generative instance identities.",
    "leanModelLimitations": "Actual syntax substitution, binder hygiene, language body semantics and realization/instance identity are supplied. A complete shared substitution calculus is not implemented.",
    "mathematicalFormulation": "Inst(env,decl,args,value) ⇔ kindCorrect(signature(decl),args)∧admissible(env,decl,args)∧realizes(env,decl,zip(parameterNames,args),value). realizes is a supplied relation; determinism, hygienic substitution and language-specific phase semantics are not implicit."
  },
  {
    "id": "urn:csabs:operation/ParametricInstantiation-substitute",
    "type": "Operation",
    "name": "substitute",
    "signature": "substitute : Γ×Binding×Syntax⇀Syntax",
    "description": "Apply simultaneous declaration-identity substitution with language-specific binder hygiene and scope checking.",
    "concept": "urn:csabs:concept/ParametricInstantiation",
    "precondition": "The supplied language substitution is defined for this syntax and binding.",
    "postcondition": "Apply simultaneous declaration-identity substitution with language-specific binder hygiene and scope checking.",
    "totality": "Partial language adapter; textual search/replace is not the specified operation.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ParametricInstantiation-instantiate",
    "type": "Operation",
    "name": "instantiate",
    "signature": "instantiate : Γ×Declaration×Args×Instance→Prop",
    "description": "Relate an instance only when signature kinds, full argument admissibility and the language realization relation all hold.",
    "concept": "urn:csabs:concept/ParametricInstantiation",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Relate an instance only when signature kinds, full argument admissibility and the language realization relation all hold.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ParametricInstantiation-instantiation-relation",
    "type": "Axiom",
    "name": "instantiation-relation",
    "statement": "Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I).",
    "formalStatement": "Instantiate(Γ,D,a,I) ⇔ kindCorrect(sig(D),a) ∧ admissible(Γ,D,a) ∧ realizes(Γ,bindNames(D,a),D,I).",
    "assumptions": [
      "Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParametricInstantiation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/ParametricInstantiation-simultaneous-substitution",
    "type": "Axiom",
    "name": "simultaneous-substitution",
    "statement": "bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.",
    "formalStatement": "bindNames(D,a) maps each declared parameter identity pᵢ to aᵢ simultaneously; substitution respects the selected language binding/scoping rules, not textual name coincidence.",
    "assumptions": [
      "Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParametricInstantiation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Defines a common staging relation with explicit language adapters. It does not identify Java parameterization, C++ observation and VHDL elaboration with the same instance representation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/ParametricInstantiation-inadmissible-no-instance",
    "type": "Law",
    "name": "inadmissible-no-instance",
    "statement": "¬kindCorrect(sig(D),a) ∨ ¬admissible(Γ,D,a) ⇒ ¬∃I,Instantiate(Γ,D,a,I).",
    "formalStatement": "¬kindCorrect(sig(D),a) ∨ ¬admissible(Γ,D,a) ⇒ ¬∃I,Instantiate(Γ,D,a,I).",
    "assumptions": [
      "Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParametricInstantiation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ParametricInstantiation-instantiation-relation"
    ],
    "proofSketch": "Every realization requires both conjuncts, so either failed prerequisite excludes all related instances."
  },
  {
    "id": "urn:csabs:law/ParametricInstantiation-instance-projection",
    "type": "Law",
    "name": "instance-projection",
    "statement": "Instantiate(Γ,D,a,I) ⇒ realizes(Γ,bindNames(D,a),D,I).",
    "formalStatement": "Instantiate(Γ,D,a,I) ⇒ realizes(Γ,bindNames(D,a),D,I).",
    "assumptions": [
      "Shared relational profile. BindNames is simultaneous substitution on declaration-local parameter identities; a supplied hygienic substitution operation handles binders and scope. Admissible includes full bounds and language checks and may refer to all arguments, including recursive/F-bounds. Realizes supplies the language-specific type, declaration or elaborated-instance semantics and any required phases. The relation need not be functional or total: different capture or generative instance identities may yield distinct results. Equality/observations and any equivalence modulo fresh names must be explicit. No shared specialization, erasure, SFINAE, runtime representation or hardware-generation rule is assumed.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/ParametricInstantiation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §§4.5,4.5.2,4.10.2; IEEE 1076-2019 §§6.5.7,14.3,14.4.2.10; N4861 [temp.arg]",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/ParametricInstantiation-instantiation-relation",
      "urn:csabs:axiom/ParametricInstantiation-simultaneous-substitution"
    ],
    "proofSketch": "Project the realization conjunct using the explicit simultaneous binding; no uniqueness or runtime code-generation consequence follows."
  }
]
```
<!-- graph-record:end -->
