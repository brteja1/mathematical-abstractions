# Kinded partial template metafunction

An environment-indexed partial function from finite, kind-correct template argument lists to a selected type or constant-value observation of a successful instantiation.

**Notation:** Arg=TypeArg(TypeId)⊎ValueArg(TypedConstant)⊎TemplateArg(TemplateId); F_Γ:Args⇀(TypeId⊎TypedConstant)

**Stable ID:** `urn:csabs:concept/TemplateMetafunction`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** Function

**Prerequisites:** [Partial function](PartialFunction.md), [Finite sequence (List datatype)](Sequence.md), [Sum Type](SumType.md)

**Specializes:** [Partial function](PartialFunction.md)

**Related concepts:** [Dependent function (Pi type)](DependentFunction.md), [Class template partial-specialization selection](TemplateSpecialization.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md), [Checked signed-integer constant-evaluation fragment](CompileTimeEvaluation.md)

## Backlinks

- [Checked signed-integer constant-evaluation fragment](CompileTimeEvaluation.md) — `relatedConcept`
- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `relatedConcept`
- [Finite kinded generic parameter signature](GenericSignature.md) — `relatedConcept`
- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `relatedConcept`
- [Ordered template packs and structural expansion](TemplateParameterPack.md) — `relatedConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `relatedConcept`
- [Ordered substitution with immediate-context failure](TemplateSubstitution.md) — `relatedConcept`
- [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md) — `relatedConcept`

## Mathematical formulation

A selected environment supplies kinded:Arg\*→Prop and apply:Arg\*→Option(Result), with apply(args)=some(r)⇒kinded(args). Composition is Option bind. This partial semantic observation does not decide all C++ instantiations or distinguish every cause of undefinedness.

**Lean formulation** (in its source module context):

```lean
structure TemplateMetafunction (Arg : Type u) (Result : Type v) where
  wellKinded : List Arg → Prop
  apply : List Arg → Option Result
  domain_kinded : ∀ args, (apply args).isSome → wellKinded args
```

**Source:** [`Catalog.TMP.TemplateMetafunction`](../lean/Catalog/TemplateMetaprogramming.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Kind-correct List Arg to Option Result in a fixed environment; TemplateArgument supplies disjoint type/value/template tags; partial composition is explicit. Instantiate carriers with canonical argument identities and result observations.

**Limits:** The function is a mathematical interpretation, not a decision procedure for compilation, equivalence, instantiation termination or compiler limits. Apply only after target-environment and canonical-argument mapping.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result. If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree. dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.

**specializationNote:** Instantiate ambient A with canonical finite template argument lists and B with the tagged type/value observation carrier. Definedness includes successful required instantiation in fixed Γ. Retain partial application and extensional partial composition; no total dependent-function or runtime-function interpretation is implied.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TemplateMetafunction-well-kinded"></a>

### well-kinded

`urn:csabs:operation/TemplateMetafunction-well-kinded`

**signature:** wellKinded : Γ×Params×Args→Prop

**description:** Check the fixed parameter/argument kind, arity and pack correspondence; non-type conversion and template-template compatibility are part of this supplied relation.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Check the fixed parameter/argument kind, arity and pack correspondence; non-type conversion and template-template compatibility are part of this supplied relation.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateMetafunction-apply"></a>

### apply

`urn:csabs:operation/TemplateMetafunction-apply`

**signature:** apply : F_Γ×Args⇀MetaResult

**description:** Return the selected type or constant observation exactly on dom(F_Γ).

**precondition:** Arguments belong to the defined domain of the fixed observed metafunction.

**postcondition:** Return the selected type or constant observation exactly on dom(F_Γ).

**totality:** Partial; undefined inputs do not yield a fallback type or value.

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateMetafunction-compose"></a>

### compose

`urn:csabs:operation/TemplateMetafunction-compose`

**signature:** compose : (A⇀B)×(B⇀C)→(A⇀C)

**description:** For compatible observation/argument carriers, (G∘F)(a) is defined exactly when F(a) and then G(F(a)) are defined. Bridging a result into another template argument list must be explicit.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** For compatible observation/argument carriers, (G∘F)(a) is defined exactly when F(a) and then G(F(a)) are defined. Bridging a result into another template argument list must be explicit.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TemplateMetafunction-kind-and-domain"></a>

### kind-and-domain

`urn:csabs:axiom/TemplateMetafunction-kind-and-domain`

**statement:** a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result.

**formalStatement:** a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result.

**assumptions:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateMetafunction-canonical-arguments"></a>

### canonical-arguments

`urn:csabs:axiom/TemplateMetafunction-canonical-arguments`

**statement:** If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree.

**formalStatement:** If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree.

**assumptions:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateMetafunction-partial-composition"></a>

### partial-composition

`urn:csabs:axiom/TemplateMetafunction-partial-composition`

**statement:** dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.

**formalStatement:** dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.

**assumptions:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-TemplateMetafunction-equivalent-argument-observation"></a>

### equivalent-argument-observation

`urn:csabs:law/TemplateMetafunction-equivalent-argument-observation`

**statement:** a∈dom(F_Γ) ∧ a≡Γb ⇒ b∈dom(F_Γ) ∧ F_Γ(a)=F_Γ(b).

**formalStatement:** a∈dom(F_Γ) ∧ a≡Γb ⇒ b∈dom(F_Γ) ∧ F_Γ(a)=F_Γ(b).

**assumptions:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [kind-and-domain](TemplateMetafunction.md#node-urn-csabs-axiom-TemplateMetafunction-kind-and-domain); [canonical-arguments](TemplateMetafunction.md#node-urn-csabs-axiom-TemplateMetafunction-canonical-arguments)

**proofSketch:** Apply canonical-argument domain invariance and output congruence. The fixed Γ condition excludes changes to visibility or selected result members.

<a id="node-urn-csabs-law-TemplateMetafunction-undefined-composition"></a>

### undefined-composition

`urn:csabs:law/TemplateMetafunction-undefined-composition`

**statement:** a∉dom(F) ∨ (a∈dom(F) ∧ F(a)∉dom(G)) ⇒ a∉dom(G∘F).

**formalStatement:** a∉dom(F) ∨ (a∈dom(F) ∧ F(a)∉dom(G)) ⇒ a∉dom(G∘F).

**assumptions:** C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [partial-composition](TemplateMetafunction.md#node-urn-csabs-axiom-TemplateMetafunction-partial-composition)

**proofSketch:** Negate the conjunction characterizing the composition domain; no value is manufactured for an undefined stage.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.type] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.type); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [temp.inst] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.inst); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation

**sourceNote:** Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TemplateMetafunction",
    "type": "Concept",
    "shortForm": "TemplateMetafunction",
    "fullName": "Kinded partial template metafunction",
    "definition": "An environment-indexed partial function from finite, kind-correct template argument lists to a selected type or constant-value observation of a successful instantiation.",
    "notation": "Arg=TypeArg(TypeId)⊎ValueArg(TypedConstant)⊎TemplateArg(TemplateId); F_Γ:Args⇀(TypeId⊎TypedConstant)",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/function",
    "requiresConcept": [
      "urn:csabs:concept/PartialFunction",
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/SumType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DependentFunction",
      "urn:csabs:concept/TemplateSpecialization",
      "urn:csabs:concept/TemplateSubstitution",
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "hasOperation": [
      "urn:csabs:operation/TemplateMetafunction-well-kinded",
      "urn:csabs:operation/TemplateMetafunction-apply",
      "urn:csabs:operation/TemplateMetafunction-compose"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TemplateMetafunction-kind-and-domain",
      "urn:csabs:axiom/TemplateMetafunction-canonical-arguments",
      "urn:csabs:axiom/TemplateMetafunction-partial-composition"
    ],
    "hasLaw": [
      "urn:csabs:law/TemplateMetafunction-equivalent-argument-observation",
      "urn:csabs:law/TemplateMetafunction-undefined-composition"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/PartialFunction"
    ],
    "specializationNote": "Instantiate ambient A with canonical finite template argument lists and B with the tagged type/value observation carrier. Definedness includes successful required instantiation in fixed Γ. Retain partial application and extensional partial composition; no total dependent-function or runtime-function interpretation is implied.",
    "axiomBasis": "Selected defining rules: a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result. If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree. dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.",
    "leanFormulation": "structure TemplateMetafunction (Arg : Type u) (Result : Type v) where\n  wellKinded : List Arg → Prop\n  apply : List Arg → Option Result\n  domain_kinded : ∀ args, (apply args).isSome → wellKinded args",
    "formulationSource": "urn:csabs:source/local-lean-TemplateMetaprogramming",
    "formulationLocator": "Catalog.TMP.TemplateMetafunction",
    "formulationScope": "model",
    "leanModelMapping": "Kind-correct List Arg to Option Result in a fixed environment; TemplateArgument supplies disjoint type/value/template tags; partial composition is explicit. Instantiate carriers with canonical argument identities and result observations.",
    "leanModelLimitations": "The function is a mathematical interpretation, not a decision procedure for compilation, equivalence, instantiation termination or compiler limits. Apply only after target-environment and canonical-argument mapping.",
    "mathematicalFormulation": "A selected environment supplies kinded:Arg*→Prop and apply:Arg*→Option(Result), with apply(args)=some(r)⇒kinded(args). Composition is Option bind. This partial semantic observation does not decide all C++ instantiations or distinguish every cause of undefinedness."
  },
  {
    "id": "urn:csabs:operation/TemplateMetafunction-well-kinded",
    "type": "Operation",
    "name": "well-kinded",
    "signature": "wellKinded : Γ×Params×Args→Prop",
    "description": "Check the fixed parameter/argument kind, arity and pack correspondence; non-type conversion and template-template compatibility are part of this supplied relation.",
    "concept": "urn:csabs:concept/TemplateMetafunction",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Check the fixed parameter/argument kind, arity and pack correspondence; non-type conversion and template-template compatibility are part of this supplied relation.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateMetafunction-apply",
    "type": "Operation",
    "name": "apply",
    "signature": "apply : F_Γ×Args⇀MetaResult",
    "description": "Return the selected type or constant observation exactly on dom(F_Γ).",
    "concept": "urn:csabs:concept/TemplateMetafunction",
    "precondition": "Arguments belong to the defined domain of the fixed observed metafunction.",
    "postcondition": "Return the selected type or constant observation exactly on dom(F_Γ).",
    "totality": "Partial; undefined inputs do not yield a fallback type or value.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateMetafunction-compose",
    "type": "Operation",
    "name": "compose",
    "signature": "compose : (A⇀B)×(B⇀C)→(A⇀C)",
    "description": "For compatible observation/argument carriers, (G∘F)(a) is defined exactly when F(a) and then G(F(a)) are defined. Bridging a result into another template argument list must be explicit.",
    "concept": "urn:csabs:concept/TemplateMetafunction",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "For compatible observation/argument carriers, (G∘F)(a) is defined exactly when F(a) and then G(F(a)) are defined. Bridging a result into another template argument list must be explicit.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TemplateMetafunction-kind-and-domain",
    "type": "Axiom",
    "name": "kind-and-domain",
    "statement": "a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result.",
    "formalStatement": "a∈dom(F_Γ) ⇒ wellKinded(Γ,params(F),a); each a∈dom(F_Γ) has exactly one observed result.",
    "assumptions": [
      "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateMetafunction-canonical-arguments",
    "type": "Axiom",
    "name": "canonical-arguments",
    "statement": "If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree.",
    "formalStatement": "If a and b represent the same canonical template arguments in fixed Γ, then a∈dom(F_Γ) ⇔ b∈dom(F_Γ), and their defined observed results agree.",
    "assumptions": [
      "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateMetafunction-partial-composition",
    "type": "Axiom",
    "name": "partial-composition",
    "statement": "dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.",
    "formalStatement": "dom(G∘F)={a∈dom(F) | F(a)∈dom(G)}; (G∘F)(a)=G(F(a)) there; F=G iff their domains and all defined observations agree.",
    "assumptions": [
      "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Models a fixed observed type/member value as a partial map. Kind tags and environmental indexing are catalog abstractions; full non-type argument equivalence and instantiation rules remain explicit adapter obligations.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/TemplateMetafunction-equivalent-argument-observation",
    "type": "Law",
    "name": "equivalent-argument-observation",
    "statement": "a∈dom(F_Γ) ∧ a≡Γb ⇒ b∈dom(F_Γ) ∧ F_Γ(a)=F_Γ(b).",
    "formalStatement": "a∈dom(F_Γ) ∧ a≡Γb ⇒ b∈dom(F_Γ) ∧ F_Γ(a)=F_Γ(b).",
    "assumptions": [
      "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateMetafunction-kind-and-domain",
      "urn:csabs:axiom/TemplateMetafunction-canonical-arguments"
    ],
    "proofSketch": "Apply canonical-argument domain invariance and output congruence. The fixed Γ condition excludes changes to visibility or selected result members."
  },
  {
    "id": "urn:csabs:law/TemplateMetafunction-undefined-composition",
    "type": "Law",
    "name": "undefined-composition",
    "statement": "a∉dom(F) ∨ (a∈dom(F) ∧ F(a)∉dom(G)) ⇒ a∉dom(G∘F).",
    "formalStatement": "a∉dom(F) ∨ (a∈dom(F) ∧ F(a)∉dom(G)) ⇒ a∉dom(G∘F).",
    "assumptions": [
      "C++20 N4861-inspired observation profile, not every C++ template as a first-class function. Γ fixes declarations, visibility, instantiation point and selected result member. Type/template identities and converted non-type argument equivalence are resolved before applying F; spelling equality is insufficient. Correct parameter kinds, arity, constraints, selected specialization and required instantiations determine the domain. Invalid, ambiguous or nonterminating instantiations have no result here; their diagnostics belong to other entries. Compiler resource exhaustion is not identified with mathematical nontermination. Metafunction equality is extensional in both domain and result; equal observed results need not identify template entities.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateMetafunction"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.arg",
      "urn:csabs:source/cpp20-n4861-temp.type",
      "urn:csabs:source/cpp20-n4861-temp.inst"
    ],
    "sourceLocator": "[temp.arg] ¶1; [temp.type] ¶1–2; [temp.inst], contexts requiring instantiation",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateMetafunction-partial-composition"
    ],
    "proofSketch": "Negate the conjunction characterizing the composition domain; no value is manufactured for an undefined stage."
  }
]
```
<!-- graph-record:end -->
