# Ordered substitution with immediate-context failure

A staged function-template deduction model that distinguishes immediate-context substitution failure from hard errors caused by required instantiation side effects.

**Notation:** Event=Continue⊎ImmediateInvalid⊎RequiredHardError; scan:Seq(Event)→Success⊎DeductionFailure⊎HardError; attempt(Γ,θ,syntax) emits ordered events and a substituted result on success

**Stable ID:** `urn:csabs:concept/TemplateSubstitution`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** semantic-model

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Free ranked term algebra with variables](TermAlgebra.md)

**Related concepts:** [Kinded partial template metafunction](TemplateMetafunction.md), [Normalized template constraints with atomic identity](TemplateConstraint.md)

## Backlinks

- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `relatedConcept`
- [Resolved generic argument binding with ordered defaults](GenericArgumentBinding.md) — `relatedConcept`
- [Normalized template constraints with atomic identity](TemplateConstraint.md) — `relatedConcept`
- [Kinded partial template metafunction](TemplateMetafunction.md) — `relatedConcept`
- [Ordered template packs and structural expansion](TemplateParameterPack.md) — `relatedConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `relatedConcept`

## Mathematical formulation

A supplied frontend maps (env,subst,syntax) to an ordered event list and optional artifact. scan([])=success; scan(continue::es)=scan(es); scan(immediateInvalid::es)=deductionFailure; scan(requiredHardError::es)=hardError. A success result requires an artifact. Lexical event generation and immediate-context classification are frontend obligations.

**Lean formulation** (in its source module context):

```lean
structure TemplateSubstitution (Env : Type u) (Subst : Type v)
    (Syntax : Type w) (Artifact : Type x) where
  frontend : Env → Subst → Syntax → List SubstitutionEvent × Option Artifact
  success_artifact : ∀ env subst term,
    scanSubstitution (frontend env subst term).1 = .success →
      (frontend env subst term).2.isSome
```

**Source:** [`Catalog.TMP.TemplateSubstitution`](../lean/Catalog/TemplateMetaprogramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Ordered Continue/ImmediateInvalid/RequiredHardError events with a stopping scan; a supplied frontend connects environment, substitution and syntax to events and a successful artifact.

**Limits:** Actual syntactic substitution, lexical event generation, access checking and immediate-context/side-effect classification remain frontend obligations. IFNDR cases are excluded. No complete C++ deduction algorithm or SFINAE theorem is registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError. Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TemplateSubstitution-attempt"></a>

### attempt

`urn:csabs:operation/TemplateSubstitution-attempt`

**signature:** attempt : Γ×Substitution×Syntax→Attempt

**description:** Apply the supplied substitution frontend in lexical order; success includes a substituted artifact, failure includes the reached event classification.

**precondition:** Syntax and substitution are in the selected well-formed deduction profile.

**postcondition:** Apply the supplied substitution frontend in lexical order; success includes a substituted artifact, failure includes the reached event classification.

**totality:** Classifier on the selected frontend observations; unsupported/IFNDR cases require separate reporting.

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateSubstitution-scan"></a>

### scan

`urn:csabs:operation/TemplateSubstitution-scan`

**signature:** scan : Seq(Event)→Status

**description:** Skip Continue events, stop at the first ImmediateInvalid or RequiredHardError, and return Success only if the finite sequence ends.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Skip Continue events, stop at the first ImmediateInvalid or RequiredHardError, and return Success only if the finite sequence ends.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateSubstitution-retain"></a>

### retain

`urn:csabs:operation/TemplateSubstitution-retain`

**signature:** retain : Status→Prop

**description:** retain(status) iff status=Success; HardError aborts the required program check rather than behaving as a rejected candidate.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** retain(status) iff status=Success; HardError aborts the required program check rather than behaving as a rejected candidate.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TemplateSubstitution-lexical-scan"></a>

### lexical-scan

`urn:csabs:axiom/TemplateSubstitution-lexical-scan`

**statement:** scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError.

**formalStatement:** scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError.

**assumptions:** C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateSubstitution-context-classification"></a>

### context-classification

`urn:csabs:axiom/TemplateSubstitution-context-classification`

**statement:** Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.

**formalStatement:** Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.

**assumptions:** C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-TemplateSubstitution-early-failure-stops"></a>

### early-failure-stops

`urn:csabs:law/TemplateSubstitution-early-failure-stops`

**statement:** scan(Continueⁿ ++ [ImmediateInvalid] ++ es)=DeductionFailure, even if es contains RequiredHardError.

**formalStatement:** scan(Continueⁿ ++ [ImmediateInvalid] ++ es)=DeductionFailure, even if es contains RequiredHardError.

**assumptions:** C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [lexical-scan](TemplateSubstitution.md#node-urn-csabs-axiom-TemplateSubstitution-lexical-scan)

**proofSketch:** Induct over the Continue prefix, then apply the stopping equation; the later event is not reached.

<a id="node-urn-csabs-law-TemplateSubstitution-hard-error-is-not-sfinae"></a>

### hard-error-is-not-sfinae

`urn:csabs:law/TemplateSubstitution-hard-error-is-not-sfinae`

**statement:** scan(Continueⁿ ++ [RequiredHardError] ++ es)=HardError.

**formalStatement:** scan(Continueⁿ ++ [RequiredHardError] ++ es)=HardError.

**assumptions:** C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [lexical-scan](TemplateSubstitution.md#node-urn-csabs-axiom-TemplateSubstitution-lexical-scan); [context-classification](TemplateSubstitution.md#node-urn-csabs-axiom-TemplateSubstitution-context-classification)

**proofSketch:** Remove the successful prefix and use the hard-error branch. The context classifier prevents treating a required side-effect error as ordinary candidate rejection.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.deduct] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.deduct); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects

**sourceNote:** Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TemplateSubstitution",
    "type": "Concept",
    "shortForm": "TemplateSubstitution",
    "fullName": "Ordered substitution with immediate-context failure",
    "definition": "A staged function-template deduction model that distinguishes immediate-context substitution failure from hard errors caused by required instantiation side effects.",
    "notation": "Event=Continue⊎ImmediateInvalid⊎RequiredHardError; scan:Seq(Event)→Success⊎DeductionFailure⊎HardError; attempt(Γ,θ,syntax) emits ordered events and a substituted result on success",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/TermAlgebra"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/TemplateConstraint"
    ],
    "hasOperation": [
      "urn:csabs:operation/TemplateSubstitution-attempt",
      "urn:csabs:operation/TemplateSubstitution-scan",
      "urn:csabs:operation/TemplateSubstitution-retain"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TemplateSubstitution-lexical-scan",
      "urn:csabs:axiom/TemplateSubstitution-context-classification"
    ],
    "hasLaw": [
      "urn:csabs:law/TemplateSubstitution-early-failure-stops",
      "urn:csabs:law/TemplateSubstitution-hard-error-is-not-sfinae"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError. Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.",
    "leanFormulation": "structure TemplateSubstitution (Env : Type u) (Subst : Type v)\n    (Syntax : Type w) (Artifact : Type x) where\n  frontend : Env → Subst → Syntax → List SubstitutionEvent × Option Artifact\n  success_artifact : ∀ env subst term,\n    scanSubstitution (frontend env subst term).1 = .success →\n      (frontend env subst term).2.isSome",
    "formulationSource": "urn:csabs:source/local-lean-TemplateMetaprogramming",
    "formulationLocator": "Catalog.TMP.TemplateSubstitution",
    "formulationScope": "partial",
    "leanModelMapping": "Ordered Continue/ImmediateInvalid/RequiredHardError events with a stopping scan; a supplied frontend connects environment, substitution and syntax to events and a successful artifact.",
    "leanModelLimitations": "Actual syntactic substitution, lexical event generation, access checking and immediate-context/side-effect classification remain frontend obligations. IFNDR cases are excluded. No complete C++ deduction algorithm or SFINAE theorem is registered.",
    "mathematicalFormulation": "A supplied frontend maps (env,subst,syntax) to an ordered event list and optional artifact. scan([])=success; scan(continue::es)=scan(es); scan(immediateInvalid::es)=deductionFailure; scan(requiredHardError::es)=hardError. A success result requires an artifact. Lexical event generation and immediate-context classification are frontend obligations."
  },
  {
    "id": "urn:csabs:operation/TemplateSubstitution-attempt",
    "type": "Operation",
    "name": "attempt",
    "signature": "attempt : Γ×Substitution×Syntax→Attempt",
    "description": "Apply the supplied substitution frontend in lexical order; success includes a substituted artifact, failure includes the reached event classification.",
    "concept": "urn:csabs:concept/TemplateSubstitution",
    "precondition": "Syntax and substitution are in the selected well-formed deduction profile.",
    "postcondition": "Apply the supplied substitution frontend in lexical order; success includes a substituted artifact, failure includes the reached event classification.",
    "totality": "Classifier on the selected frontend observations; unsupported/IFNDR cases require separate reporting.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateSubstitution-scan",
    "type": "Operation",
    "name": "scan",
    "signature": "scan : Seq(Event)→Status",
    "description": "Skip Continue events, stop at the first ImmediateInvalid or RequiredHardError, and return Success only if the finite sequence ends.",
    "concept": "urn:csabs:concept/TemplateSubstitution",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Skip Continue events, stop at the first ImmediateInvalid or RequiredHardError, and return Success only if the finite sequence ends.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateSubstitution-retain",
    "type": "Operation",
    "name": "retain",
    "signature": "retain : Status→Prop",
    "description": "retain(status) iff status=Success; HardError aborts the required program check rather than behaving as a rejected candidate.",
    "concept": "urn:csabs:concept/TemplateSubstitution",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "retain(status) iff status=Success; HardError aborts the required program check rather than behaving as a rejected candidate.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TemplateSubstitution-lexical-scan",
    "type": "Axiom",
    "name": "lexical-scan",
    "statement": "scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError.",
    "formalStatement": "scan([])=Success; scan(Continue::es)=scan(es); scan(ImmediateInvalid::es)=DeductionFailure; scan(RequiredHardError::es)=HardError.",
    "assumptions": [
      "C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateSubstitution-context-classification",
    "type": "Axiom",
    "name": "context-classification",
    "statement": "Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.",
    "formalStatement": "Invalidity in the specified immediate context maps to ImmediateInvalid; an actually required diagnostic error in an instantiated side effect maps to RequiredHardError, not ImmediateInvalid.",
    "assumptions": [
      "C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Separates a supplied C++ substitution frontend from a small ordered event semantics. It is not a complete deduction algorithm, universal error-catching mechanism or inference of context from textual nesting.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/TemplateSubstitution-early-failure-stops",
    "type": "Law",
    "name": "early-failure-stops",
    "statement": "scan(Continueⁿ ++ [ImmediateInvalid] ++ es)=DeductionFailure, even if es contains RequiredHardError.",
    "formalStatement": "scan(Continueⁿ ++ [ImmediateInvalid] ++ es)=DeductionFailure, even if es contains RequiredHardError.",
    "assumptions": [
      "C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateSubstitution-lexical-scan"
    ],
    "proofSketch": "Induct over the Continue prefix, then apply the stopping equation; the later event is not reached."
  },
  {
    "id": "urn:csabs:law/TemplateSubstitution-hard-error-is-not-sfinae",
    "type": "Law",
    "name": "hard-error-is-not-sfinae",
    "statement": "scan(Continueⁿ ++ [RequiredHardError] ++ es)=HardError.",
    "formalStatement": "scan(Continueⁿ ++ [RequiredHardError] ++ es)=HardError.",
    "assumptions": [
      "C++20 N4861 function-template deduction profile. A front end supplies syntactic replacement, lexical order, access checking and the immediate-context/side-effect classification. Only checks actually reached are processed. Immediate invalidity means an invalid type/expression in a permitted immediate context for which the substituted construct would require a diagnostic. Required instantiation side effects can be hard errors; function bodies and lambda bodies are not made immediate merely by surrounding unevaluated syntax. Ill-formed-no-diagnostic-required cases, prior syntax errors and unrelated declaration errors are outside this outcome model. DeductionFailure discards this candidate; it does not guarantee another viable overload.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.deduct"
    ],
    "sourceLocator": "[temp.deduct] ¶7–9, lexical substitution order, immediate context and instantiation effects",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateSubstitution-lexical-scan",
      "urn:csabs:axiom/TemplateSubstitution-context-classification"
    ],
    "proofSketch": "Remove the successful prefix and use the hard-error branch. The context classifier prevents treating a required side-effect error as ordinary candidate rejection."
  }
]
```
<!-- graph-record:end -->
