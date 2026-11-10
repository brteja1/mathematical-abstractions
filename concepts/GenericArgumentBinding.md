# Resolved generic argument binding with ordered defaults

Completion of resolved parameter slots from supplied actual arguments or permitted defaults, retaining declaration order and detecting missing or wrong-kind arguments.

**Notation:** actual:Fin(n)→Option(Arg); default:(i,prefix)⇀Arg; bindΣ(actual,default):Option(Seq(Arg)); slots traversed i=0,…,n−1

**Stable ID:** `urn:csabs:concept/GenericArgumentBinding`

**Categories:** Programming-language semantics → Generic programming

**Kind:** semantic-model

**Prerequisites:** [Finite kinded generic parameter signature](GenericSignature.md), [Option Type](OptionType.md)

**Related concepts:** [Contextual parametric declaration instantiation](ParametricInstantiation.md), [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md)

## Backlinks

- [Finite kinded generic parameter signature](GenericSignature.md) — `relatedConcept`
- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `requiresConcept`
- [VHDL generic interfaces and whole-formal association](VHDLGenericInterface.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots. complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface.

**basisKind:** extensional-structural-definition

**basisScope:** Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GenericArgumentBinding-bind"></a>

### bind

`urn:csabs:operation/GenericArgumentBinding-bind`

**signature:** bind : Signature×ActualSlots×Defaults→Option(Seq(Arg))

**description:** For each declared slot, use an explicit actual if present, otherwise evaluate its permitted default; fail on absence or wrong kind and append a valid selected argument in declaration order.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** For each declared slot, use an explicit actual if present, otherwise evaluate its permitted default; fail on absence or wrong kind and append a valid selected argument in declaration order.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GenericArgumentBinding-complete"></a>

### complete

`urn:csabs:operation/GenericArgumentBinding-complete`

**signature:** complete : Signature×ActualSlots×Defaults→Prop

**description:** complete iff bind returns Some(args); this does not check body validity or full language-specific bounds.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** complete iff bind returns Some(args); this does not check body validity or full language-specific bounds.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GenericArgumentBinding-binding-step"></a>

### binding-step

`urn:csabs:axiom/GenericArgumentBinding-binding-step`

**statement:** Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots.

**formalStatement:** Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots.

**assumptions:** Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-GenericArgumentBinding-binding-definedness"></a>

### binding-definedness

`urn:csabs:axiom/GenericArgumentBinding-binding-definedness`

**statement:** complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface.

**formalStatement:** complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface.

**assumptions:** Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-GenericArgumentBinding-successful-binding-kinded"></a>

### successful-binding-kinded

`urn:csabs:law/GenericArgumentBinding-successful-binding-kinded`

**statement:** bindΣ(A,D)=Some(a) ⇒ kindCorrect(Σ,a).

**formalStatement:** bindΣ(A,D)=Some(a) ⇒ kindCorrect(Σ,a).

**assumptions:** Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [binding-step](GenericArgumentBinding.md#node-urn-csabs-axiom-GenericArgumentBinding-binding-step); [kind-correctness](GenericSignature.md#node-urn-csabs-axiom-GenericSignature-kind-correctness)

**proofSketch:** Each step appends exactly one argument of the corresponding kind; induction over the finite signature yields the exact final length and all per-slot checks.

<a id="node-urn-csabs-law-GenericArgumentBinding-explicit-actual-precedence"></a>

### explicit-actual-precedence

`urn:csabs:law/GenericArgumentBinding-explicit-actual-precedence`

**statement:** A(i)=Some(x) in a reached slot ⇒ the selected argument is x and default(i,prefix) is not evaluated.

**formalStatement:** A(i)=Some(x) in a reached slot ⇒ the selected argument is x and default(i,prefix) is not evaluated.

**assumptions:** Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [binding-step](GenericArgumentBinding.md#node-urn-csabs-axiom-GenericArgumentBinding-binding-step)

**proofSketch:** Use the explicit-actual branch of the step rule, which precedes default evaluation; later checks may still reject x.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [IEEE Std 1076-2019: VHDL Language Reference Manual, generic interfaces, staticness and elaboration](https://www.0x04.net/~mwk/vstd/ieee-1076-2019.pdf); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [C++20 working draft N4861 [temp.arg] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.arg); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]

**sourceNote:** Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GenericArgumentBinding",
    "type": "Concept",
    "shortForm": "GenericArgumentBinding",
    "fullName": "Resolved generic argument binding with ordered defaults",
    "definition": "Completion of resolved parameter slots from supplied actual arguments or permitted defaults, retaining declaration order and detecting missing or wrong-kind arguments.",
    "notation": "actual:Fin(n)→Option(Arg); default:(i,prefix)⇀Arg; bindΣ(actual,default):Option(Seq(Arg)); slots traversed i=0,…,n−1",
    "category": [
      "urn:csabs:category/generic-programming"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/GenericSignature",
      "urn:csabs:concept/OptionType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ParametricInstantiation",
      "urn:csabs:concept/VHDLGenericInterface",
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "hasOperation": [
      "urn:csabs:operation/GenericArgumentBinding-bind",
      "urn:csabs:operation/GenericArgumentBinding-complete"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GenericArgumentBinding-binding-step",
      "urn:csabs:axiom/GenericArgumentBinding-binding-definedness"
    ],
    "hasLaw": [
      "urn:csabs:law/GenericArgumentBinding-successful-binding-kinded",
      "urn:csabs:law/GenericArgumentBinding-explicit-actual-precedence"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.",
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
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots. complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface."
  },
  {
    "id": "urn:csabs:operation/GenericArgumentBinding-bind",
    "type": "Operation",
    "name": "bind",
    "signature": "bind : Signature×ActualSlots×Defaults→Option(Seq(Arg))",
    "description": "For each declared slot, use an explicit actual if present, otherwise evaluate its permitted default; fail on absence or wrong kind and append a valid selected argument in declaration order.",
    "concept": "urn:csabs:concept/GenericArgumentBinding",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "For each declared slot, use an explicit actual if present, otherwise evaluate its permitted default; fail on absence or wrong kind and append a valid selected argument in declaration order.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GenericArgumentBinding-complete",
    "type": "Operation",
    "name": "complete",
    "signature": "complete : Signature×ActualSlots×Defaults→Prop",
    "description": "complete iff bind returns Some(args); this does not check body validity or full language-specific bounds.",
    "concept": "urn:csabs:concept/GenericArgumentBinding",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "complete iff bind returns Some(args); this does not check body validity or full language-specific bounds.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GenericArgumentBinding-binding-step",
    "type": "Axiom",
    "name": "binding-step",
    "statement": "Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots.",
    "formalStatement": "Starting with prefix=[], for each slot i choose actual(i) when present, otherwise default(i,prefix); fail if absent or wrong kind, else append the selected argument. Return the complete list after all slots.",
    "assumptions": [
      "Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericArgumentBinding"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/GenericArgumentBinding-binding-definedness",
    "type": "Axiom",
    "name": "binding-definedness",
    "statement": "complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface.",
    "formalStatement": "complete(Σ,A,D) ⇔ ∃a, bindΣ(A,D)=Some(a); preprocessing rejects unknown/duplicate formal associations before applying this interface.",
    "assumptions": [
      "Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericArgumentBinding"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Introduces a deterministic completion interface after language association has resolved slots. Prefix-dependent defaults are an explicit common subprofile, not the full generic association semantics of every language.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/GenericArgumentBinding-successful-binding-kinded",
    "type": "Law",
    "name": "successful-binding-kinded",
    "statement": "bindΣ(A,D)=Some(a) ⇒ kindCorrect(Σ,a).",
    "formalStatement": "bindΣ(A,D)=Some(a) ⇒ kindCorrect(Σ,a).",
    "assumptions": [
      "Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericArgumentBinding"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GenericArgumentBinding-binding-step",
      "urn:csabs:axiom/GenericSignature-kind-correctness"
    ],
    "proofSketch": "Each step appends exactly one argument of the corresponding kind; induction over the finite signature yields the exact final length and all per-slot checks."
  },
  {
    "id": "urn:csabs:law/GenericArgumentBinding-explicit-actual-precedence",
    "type": "Law",
    "name": "explicit-actual-precedence",
    "statement": "A(i)=Some(x) in a reached slot ⇒ the selected argument is x and default(i,prefix) is not evaluated.",
    "formalStatement": "A(i)=Some(x) in a reached slot ⇒ the selected argument is x and default(i,prefix) is not evaluated.",
    "assumptions": [
      "Shared fixed-arity binding profile after language-specific positional/named matching, duplicate/unknown-name checks, inference and any pack normalization. Explicit actuals here are already resolved arguments; defaults are supplied partial functions of the allowed preceding bindings and fixed environment. This is a selected ordered-default profile, not a rule that every language supports defaults, named arguments or arbitrary default dependencies. Java uses no type-parameter defaults; inferred arguments are supplied by its inference phase. Full simultaneous bounds are checked after binding. Failure means no complete binding, not a promise of rollback or a particular diagnostic.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/GenericArgumentBinding"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-vhdl2019",
      "urn:csabs:source/cpp20-n4861-temp.arg"
    ],
    "sourceLocator": "JLS §4.5 well-formed parameterizations; IEEE 1076-2019 §§6.5.7,14.3.3; N4861 [temp.arg]",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/GenericArgumentBinding-binding-step"
    ],
    "proofSketch": "Use the explicit-actual branch of the step rule, which precedes default evaluation; later checks may still reject x."
  }
]
```
<!-- graph-record:end -->
