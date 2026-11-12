# Java type erasure and selected reifiability rules

A type translation removing generic arguments, erasing type variables through their leftmost bounds and recursively erasing arrays, with a distinct predicate for runtime-reifiable types.

**Notation:** |G<T>|=|G|; |T[]|=|T|[]; |X|=|leftmostBound(X)|; erasure is not an injective map

**Stable ID:** `urn:csabs:concept/JavaTypeErasure`

**Categories:** Programming-language semantics → Generic programming → Java generics

**Kind:** Function

**Prerequisites:** [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md), [Partial function](PartialFunction.md)

**Related concepts:** [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md), [Single-inheritance class table and dynamic dispatch](ClassTable.md)

## Backlinks

- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `relatedConcept`

## Mathematical formulation

The selected owner-free syntax has named C, C<args>, array(T), variable(X) and unbounded wildcard. With positive fuel, erase(C)=C; erase(C<args>)=C; erase(array(T))=array(erase(T)); erase(X)=erase(leftmostBound(X)). Recursive steps consume fuel, fuel 0 returns none and an unbounded wildcard returns none.

**Lean formulation** (in its source module context):

```lean
structure JavaTypeErasure (Class Var : Type u) where
  leftmostBound : Var → JavaErasureSyntax Class Var
```

**Source:** [`Catalog.Generics.JavaTypeErasure`](../lean/Catalog/GenericProgramming.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** Named/parameterized/array/variable type core, plus an unbounded wildcard marker used only inside arguments; fuel-bounded erasure discards argument lists and follows the supplied leftmost variable bound.

**Limits:** Nested-owner typing, reifiability and signature translation are not encoded; adequate fuel and terminating well-formed bound chains require justification. Fuel exhaustion does not establish invalidity. No JVM translation or erasure theorem witness.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining rules: |G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves. Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.

**basisKind:** extensional-structural-definition

**basisScope:** Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JavaTypeErasure-erase"></a>

### erase

`urn:csabs:operation/JavaTypeErasure-erase`

**signature:** erase : Γ×Type→ErasedType

**description:** Apply JLS erasure equations for parameterized, nested, array and type-variable cases, using the well-formed declaration environment.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Apply JLS erasure equations for parameterized, nested, array and type-variable cases, using the well-formed declaration environment.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaTypeErasure-reifiable"></a>

### reifiable

`urn:csabs:operation/JavaTypeErasure-reifiable`

**signature:** reifiable : Γ×Type→Prop

**description:** Apply JLS §4.7 independently of erasure, including its raw, wildcard, array and nested-type requirements.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Apply JLS §4.7 independently of erasure, including its raw, wildcard, array and nested-type requirements.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaTypeErasure-erase-signature"></a>

### erase-signature

`urn:csabs:operation/JavaTypeErasure-erase-signature`

**signature:** eraseSignature : Γ×MethodSignature→ErasedSignature

**description:** Retain the method name and erase formal parameter types; constructor/method type parameters and return types follow the JLS translation where specified.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Retain the method name and erase formal parameter types; constructor/method type parameters and return types follow the JLS translation where specified.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-JavaTypeErasure-erasure-equations"></a>

### erasure-equations

`urn:csabs:axiom/JavaTypeErasure-erasure-equations`

**statement:** |G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves.

**formalStatement:** |G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves.

**assumptions:** Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaTypeErasure-reifiability-distinct"></a>

### reifiability-distinct

`urn:csabs:axiom/JavaTypeErasure-reifiability-distinct`

**statement:** Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.

**formalStatement:** Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.

**assumptions:** Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-JavaTypeErasure-same-head-erasure"></a>

### same-head-erasure

`urn:csabs:law/JavaTypeErasure-same-head-erasure`

**statement:** For two well-formed parameterizations of the same generic declaration G, |G<A>|=|G<B>|, even if G<A>≠G<B>.

**formalStatement:** For two well-formed parameterizations of the same generic declaration G, |G<A>|=|G<B>|, even if G<A>≠G<B>.

**assumptions:** Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [erasure-equations](JavaTypeErasure.md#node-urn-csabs-axiom-JavaTypeErasure-erasure-equations)

**proofSketch:** Both erase to |G|. Source-level type identity and argument containment remain separate.

<a id="node-urn-csabs-law-JavaTypeErasure-array-erasure-commutes"></a>

### array-erasure-commutes

`urn:csabs:law/JavaTypeErasure-array-erasure-commutes`

**statement:** |G<A>[]|=|G|[].

**formalStatement:** |G<A>[]|=|G|[].

**assumptions:** Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [erasure-equations](JavaTypeErasure.md#node-urn-csabs-axiom-JavaTypeErasure-erasure-equations)

**proofSketch:** Apply the array equation and then the parameterized-type equation to its component.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types

**sourceNote:** Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JavaTypeErasure",
    "type": "Concept",
    "shortForm": "JavaTypeErasure",
    "fullName": "Java type erasure and selected reifiability rules",
    "definition": "A type translation removing generic arguments, erasing type variables through their leftmost bounds and recursively erasing arrays, with a distinct predicate for runtime-reifiable types.",
    "notation": "|G<T>|=|G|; |T[]|=|T|[]; |X|=|leftmostBound(X)|; erasure is not an injective map",
    "category": [
      "urn:csabs:category/java-generics"
    ],
    "kind": "urn:csabs:kind/function",
    "requiresConcept": [
      "urn:csabs:concept/JavaParameterizedType",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/JavaWildcardCapture",
      "urn:csabs:concept/ClassTable"
    ],
    "hasOperation": [
      "urn:csabs:operation/JavaTypeErasure-erase",
      "urn:csabs:operation/JavaTypeErasure-reifiable",
      "urn:csabs:operation/JavaTypeErasure-erase-signature"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/JavaTypeErasure-erasure-equations",
      "urn:csabs:axiom/JavaTypeErasure-reifiability-distinct"
    ],
    "hasLaw": [
      "urn:csabs:law/JavaTypeErasure-same-head-erasure",
      "urn:csabs:law/JavaTypeErasure-array-erasure-commutes"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: |G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves. Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.",
    "leanFormulation": "structure JavaTypeErasure (Class Var : Type u) where\n  leftmostBound : Var → JavaErasureSyntax Class Var",
    "formulationSource": "urn:csabs:source/local-lean-GenericProgramming",
    "formulationLocator": "Catalog.Generics.JavaTypeErasure",
    "formulationScope": "partial",
    "leanModelMapping": "Named/parameterized/array/variable type core, plus an unbounded wildcard marker used only inside arguments; fuel-bounded erasure discards argument lists and follows the supplied leftmost variable bound.",
    "leanModelLimitations": "Nested-owner typing, reifiability and signature translation are not encoded; adequate fuel and terminating well-formed bound chains require justification. Fuel exhaustion does not establish invalidity. No JVM translation or erasure theorem witness.",
    "mathematicalFormulation": "The selected owner-free syntax has named C, C<args>, array(T), variable(X) and unbounded wildcard. With positive fuel, erase(C)=C; erase(C<args>)=C; erase(array(T))=array(erase(T)); erase(X)=erase(leftmostBound(X)). Recursive steps consume fuel, fuel 0 returns none and an unbounded wildcard returns none."
  },
  {
    "id": "urn:csabs:operation/JavaTypeErasure-erase",
    "type": "Operation",
    "name": "erase",
    "signature": "erase : Γ×Type→ErasedType",
    "description": "Apply JLS erasure equations for parameterized, nested, array and type-variable cases, using the well-formed declaration environment.",
    "concept": "urn:csabs:concept/JavaTypeErasure",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Apply JLS erasure equations for parameterized, nested, array and type-variable cases, using the well-formed declaration environment.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaTypeErasure-reifiable",
    "type": "Operation",
    "name": "reifiable",
    "signature": "reifiable : Γ×Type→Prop",
    "description": "Apply JLS §4.7 independently of erasure, including its raw, wildcard, array and nested-type requirements.",
    "concept": "urn:csabs:concept/JavaTypeErasure",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Apply JLS §4.7 independently of erasure, including its raw, wildcard, array and nested-type requirements.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaTypeErasure-erase-signature",
    "type": "Operation",
    "name": "erase-signature",
    "signature": "eraseSignature : Γ×MethodSignature→ErasedSignature",
    "description": "Retain the method name and erase formal parameter types; constructor/method type parameters and return types follow the JLS translation where specified.",
    "concept": "urn:csabs:concept/JavaTypeErasure",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Retain the method name and erase formal parameter types; constructor/method type parameters and return types follow the JLS translation where specified.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JavaTypeErasure-erasure-equations",
    "type": "Axiom",
    "name": "erasure-equations",
    "statement": "|G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves.",
    "formalStatement": "|G<T>|=|G|; |T.C|=|T|.C; |T[]|=|T|[]; |X|=|leftmostBound(X)|; all other types erase to themselves.",
    "assumptions": [
      "Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeErasure"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaTypeErasure-reifiability-distinct",
    "type": "Axiom",
    "name": "reifiability-distinct",
    "statement": "Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.",
    "formalStatement": "Reifiable(T) is governed by JLS §4.7, not by the equation T=|T| alone: e.g. G<?> can be reifiable while G<String> is not for an ordinary generic G; owner/array conditions remain applicable.",
    "assumptions": [
      "Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeErasure"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Separates the erasure function and runtime type availability. Selected equations do not assert that all generic metadata disappears or that equal erasures imply equal source types.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/JavaTypeErasure-same-head-erasure",
    "type": "Law",
    "name": "same-head-erasure",
    "statement": "For two well-formed parameterizations of the same generic declaration G, |G<A>|=|G<B>|, even if G<A>≠G<B>.",
    "formalStatement": "For two well-formed parameterizations of the same generic declaration G, |G<A>|=|G<B>|, even if G<A>≠G<B>.",
    "assumptions": [
      "Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeErasure"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaTypeErasure-erasure-equations"
    ],
    "proofSketch": "Both erase to |G|. Source-level type identity and argument containment remain separate."
  },
  {
    "id": "urn:csabs:law/JavaTypeErasure-array-erasure-commutes",
    "type": "Law",
    "name": "array-erasure-commutes",
    "statement": "|G<A>[]|=|G|[].",
    "formalStatement": "|G<A>[]|=|G|[].",
    "assumptions": [
      "Java SE 25 JLS §§4.6–4.8 selected type/signature translation. The environment resolves well-formed nominal declarations, type-variable bounds and nested owners; the executable core model below omits owner-sensitive nested types. Erasure of a variable follows its leftmost bound, not an arbitrary intersection constituent. Well-formed environments have terminating bound erasure. Reifiability is separate from erasure: non-generic/raw types and suitable all-unbounded-wildcard parameterizations can be reifiable; arbitrary exact parameterizations generally are not. Erasure alone does not specify complete JVM translation, bridge methods, inserted casts, reflection signatures, heap-pollution safety or overload legality.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaTypeErasure"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §§4.6 Type Erasure,4.7 Reifiable Types,4.8 Raw Types",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaTypeErasure-erasure-equations"
    ],
    "proofSketch": "Apply the array equation and then the parameterized-type equation to its component."
  }
]
```
<!-- graph-record:end -->
