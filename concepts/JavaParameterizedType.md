# Java bounded parameterized types and nominal subtyping

Java class/interface parameterizations checked for arity and capture-adjusted bounds, with member/supertype substitution and invariant exact type arguments.

**Notation:** C<T₁,…,Tₙ>; θ=[A₁:=S₁,…,Aₙ:=Sₙ] after capture; WF iff reference/wildcard arguments, correct arity and Sᵢ<:θ(B) for each declared bound B of Aᵢ

**Stable ID:** `urn:csabs:concept/JavaParameterizedType`

**Categories:** Programming-language semantics → Generic programming → Java generics

**Kind:** semantic-model

**Prerequisites:** [Finite kinded generic parameter signature](GenericSignature.md), [Contextual parametric declaration instantiation](ParametricInstantiation.md)

**Related concepts:** [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md), [Java type erasure and selected reifiability rules](JavaTypeErasure.md), [Java generic inference constraints and resolution obligations](JavaTypeInference.md), [Behavioral subtyping with explicit history constraints](BehavioralSubtyping.md)

## Backlinks

- [Finite kinded generic parameter signature](GenericSignature.md) — `relatedConcept`
- [Java type erasure and selected reifiability rules](JavaTypeErasure.md) — `requiresConcept`
- [Java generic inference constraints and resolution obligations](JavaTypeInference.md) — `requiresConcept`
- [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md) — `requiresConcept`
- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required. For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first. Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments.

**basisKind:** extensional-structural-definition

**basisScope:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JavaParameterizedType-well-formed"></a>

### well-formed

`urn:csabs:operation/JavaParameterizedType-well-formed`

**signature:** wellFormed : Γ×GenericDecl×Args→Prop

**description:** Check declaration validity, exact arity, permitted argument forms, capture conversion and every substituted parameter bound.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Check declaration validity, exact arity, permitted argument forms, capture conversion and every substituted parameter bound.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaParameterizedType-member-type"></a>

### member-type

`urn:csabs:operation/JavaParameterizedType-member-type`

**signature:** memberType : Γ×C<Args>×Member⇀Type

**description:** Substitute declaration parameters in the declared member type, applying capture where required for wildcard arguments.

**precondition:** The parameterization is well-formed and the selected member is present and accessible.

**postcondition:** Substitute declaration parameters in the declared member type, applying capture where required for wildcard arguments.

**totality:** Partial; no missing/inaccessible-member fallback.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaParameterizedType-direct-supertypes"></a>

### direct-supertypes

`urn:csabs:operation/JavaParameterizedType-direct-supertypes`

**signature:** directSupertypes : Γ×Type→𝒫(Type)

**description:** Use the JLS declared-supertype substitution and argument-containment rules, including raw/Object cases where required; subtype is their reflexive-transitive closure.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Use the JLS declared-supertype substitution and argument-containment rules, including raw/Object cases where required; subtype is their reflexive-transitive closure.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-JavaParameterizedType-bounded-well-formedness"></a>

### bounded-well-formedness

`urn:csabs:axiom/JavaParameterizedType-bounded-well-formedness`

**statement:** WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required.

**formalStatement:** WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required.

**assumptions:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaParameterizedType-member-substitution"></a>

### member-substitution

`urn:csabs:axiom/JavaParameterizedType-member-substitution`

**statement:** For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first.

**formalStatement:** For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first.

**assumptions:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaParameterizedType-nominal-supertype-rules"></a>

### nominal-supertype-rules

`urn:csabs:axiom/JavaParameterizedType-nominal-supertype-rules`

**statement:** Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments.

**formalStatement:** Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments.

**assumptions:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-JavaParameterizedType-member-argument-replacement"></a>

### member-argument-replacement

`urn:csabs:law/JavaParameterizedType-member-argument-replacement`

**statement:** If C<A> declares a member of type A and C<T> is well-formed with an exact argument, that member has type T.

**formalStatement:** If C<A> declares a member of type A and C<T> is well-formed with an exact argument, that member has type T.

**assumptions:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [member-substitution](JavaParameterizedType.md#node-urn-csabs-axiom-JavaParameterizedType-member-substitution)

**proofSketch:** Instantiate the simultaneous member-substitution equation on the single parameter occurrence.

<a id="node-urn-csabs-law-JavaParameterizedType-failed-bound-rejected"></a>

### failed-bound-rejected

`urn:csabs:law/JavaParameterizedType-failed-bound-rejected`

**statement:** After capture, some required Sᵢ is not a subtype of its substituted bound ⇒ C<T> is not well-formed.

**formalStatement:** After capture, some required Sᵢ is not a subtype of its substituted bound ⇒ C<T> is not well-formed.

**assumptions:** Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [bounded-well-formedness](JavaParameterizedType.md#node-urn-csabs-axiom-JavaParameterizedType-bounded-well-formedness)

**proofSketch:** A required bound conjunct fails. This says nothing about a different inferred or explicitly supplied argument list.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds

**sourceNote:** Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JavaParameterizedType",
    "type": "Concept",
    "shortForm": "JavaParameterizedType",
    "fullName": "Java bounded parameterized types and nominal subtyping",
    "definition": "Java class/interface parameterizations checked for arity and capture-adjusted bounds, with member/supertype substitution and invariant exact type arguments.",
    "notation": "C<T₁,…,Tₙ>; θ=[A₁:=S₁,…,Aₙ:=Sₙ] after capture; WF iff reference/wildcard arguments, correct arity and Sᵢ<:θ(B) for each declared bound B of Aᵢ",
    "category": [
      "urn:csabs:category/java-generics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/GenericSignature",
      "urn:csabs:concept/ParametricInstantiation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/JavaWildcardCapture",
      "urn:csabs:concept/JavaTypeErasure",
      "urn:csabs:concept/JavaTypeInference",
      "urn:csabs:concept/BehavioralSubtyping"
    ],
    "hasOperation": [
      "urn:csabs:operation/JavaParameterizedType-well-formed",
      "urn:csabs:operation/JavaParameterizedType-member-type",
      "urn:csabs:operation/JavaParameterizedType-direct-supertypes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/JavaParameterizedType-bounded-well-formedness",
      "urn:csabs:axiom/JavaParameterizedType-member-substitution",
      "urn:csabs:axiom/JavaParameterizedType-nominal-supertype-rules"
    ],
    "hasLaw": [
      "urn:csabs:law/JavaParameterizedType-member-argument-replacement",
      "urn:csabs:law/JavaParameterizedType-failed-bound-rejected"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required. For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first. Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments."
  },
  {
    "id": "urn:csabs:operation/JavaParameterizedType-well-formed",
    "type": "Operation",
    "name": "well-formed",
    "signature": "wellFormed : Γ×GenericDecl×Args→Prop",
    "description": "Check declaration validity, exact arity, permitted argument forms, capture conversion and every substituted parameter bound.",
    "concept": "urn:csabs:concept/JavaParameterizedType",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Check declaration validity, exact arity, permitted argument forms, capture conversion and every substituted parameter bound.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaParameterizedType-member-type",
    "type": "Operation",
    "name": "member-type",
    "signature": "memberType : Γ×C<Args>×Member⇀Type",
    "description": "Substitute declaration parameters in the declared member type, applying capture where required for wildcard arguments.",
    "concept": "urn:csabs:concept/JavaParameterizedType",
    "precondition": "The parameterization is well-formed and the selected member is present and accessible.",
    "postcondition": "Substitute declaration parameters in the declared member type, applying capture where required for wildcard arguments.",
    "totality": "Partial; no missing/inaccessible-member fallback.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaParameterizedType-direct-supertypes",
    "type": "Operation",
    "name": "direct-supertypes",
    "signature": "directSupertypes : Γ×Type→𝒫(Type)",
    "description": "Use the JLS declared-supertype substitution and argument-containment rules, including raw/Object cases where required; subtype is their reflexive-transitive closure.",
    "concept": "urn:csabs:concept/JavaParameterizedType",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Use the JLS declared-supertype substitution and argument-containment rules, including raw/Object cases where required; subtype is their reflexive-transitive closure.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JavaParameterizedType-bounded-well-formedness",
    "type": "Axiom",
    "name": "bounded-well-formedness",
    "statement": "WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required.",
    "formalStatement": "WF(C<T>) requires the correct number of reference/wildcard arguments and, after capture to S with θ=[A:=S], Sᵢ<:θ(B) for each declared bound B of Aᵢ; declaration well-formedness is also required.",
    "assumptions": [
      "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaParameterizedType"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaParameterizedType-member-substitution",
    "type": "Axiom",
    "name": "member-substitution",
    "statement": "For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first.",
    "formalStatement": "For a well-formed exact-argument C<T> and selected declared member with type U, its instantiated type is U[A:=T]; wildcard access uses capture first.",
    "assumptions": [
      "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaParameterizedType"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaParameterizedType-nominal-supertype-rules",
    "type": "Axiom",
    "name": "nominal-supertype-rules",
    "statement": "Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments.",
    "formalStatement": "Declared generic superclass/interface types are substituted simultaneously; same-head wildcard argument containment follows JLS §4.5.1. S<:T alone does not imply C<S><:C<T> for exact arguments.",
    "assumptions": [
      "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaParameterizedType"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Records well-formedness and selected nominal/member substitution rules; Java nominal subtyping is not itself behavioral subtyping or C++ partial specialization.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/JavaParameterizedType-member-argument-replacement",
    "type": "Law",
    "name": "member-argument-replacement",
    "statement": "If C<A> declares a member of type A and C<T> is well-formed with an exact argument, that member has type T.",
    "formalStatement": "If C<A> declares a member of type A and C<T> is well-formed with an exact argument, that member has type T.",
    "assumptions": [
      "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaParameterizedType"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaParameterizedType-member-substitution"
    ],
    "proofSketch": "Instantiate the simultaneous member-substitution equation on the single parameter occurrence."
  },
  {
    "id": "urn:csabs:law/JavaParameterizedType-failed-bound-rejected",
    "type": "Law",
    "name": "failed-bound-rejected",
    "statement": "After capture, some required Sᵢ is not a subtype of its substituted bound ⇒ C<T> is not well-formed.",
    "formalStatement": "After capture, some required Sᵢ is not a subtype of its substituted bound ⇒ C<T> is not well-formed.",
    "assumptions": [
      "Java SE 25 JLS selected generic class/interface profile. Type arguments are reference types or wildcards; primitives require a separate boxing conversion and are not direct type arguments. Bounds may be recursive/F-bounded and are substituted simultaneously. Type/declaration equality is nominal identity. Member types and declared generic supertypes use substitution; same-head argument containment uses wildcard rules, not covariance of exact arguments. Raw types and erasure are distinct views, not interchangeable parameterizations. Full member lookup, nested-owner typing, annotations, all array/null rules and a complete subtype decision procedure are outside this interface; adapters must honor the cited JLS rules.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaParameterizedType"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types",
      "urn:csabs:source/generics-jls25-capture"
    ],
    "sourceLocator": "JLS §§4.4,4.5–4.5.2,4.10–4.10.2; §5.1.10 for capture-adjusted bounds",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaParameterizedType-bounded-well-formedness"
    ],
    "proofSketch": "A required bound conjunct fails. This says nothing about a different inferred or explicitly supplied argument list."
  }
]
```
<!-- graph-record:end -->
