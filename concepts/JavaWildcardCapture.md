# Java wildcard capture with fresh bounded variables

A nonrecursive conversion of wildcard arguments in one parameterized type to fresh bounded type variables, enabling a typed name for an unknown argument.

**Notation:** capture(G<T₁,…,Tₙ>)=G<S₁,…,Sₙ>; Uᵢ′=Uᵢ[A:=S]; ?:nullType≤Sᵢ≤Uᵢ′; ? extends B:nullType≤Sᵢ≤glb(B,Uᵢ′); ? super B:B≤Sᵢ≤Uᵢ′

**Stable ID:** `urn:csabs:concept/JavaWildcardCapture`

**Categories:** Programming-language semantics → Generic programming → Java generics

**Kind:** semantic-model

**Prerequisites:** [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md), [Binary relation](Relation.md)

**Related concepts:** [Java generic inference constraints and resolution obligations](JavaTypeInference.md), [Predicate-restricted subtype](Subtype.md)

## Backlinks

- [Java bounded parameterized types and nominal subtyping](JavaParameterizedType.md) — `relatedConcept`
- [Java type erasure and selected reifiability rules](JavaTypeErasure.md) — `relatedConcept`
- [Java generic inference constraints and resolution obligations](JavaTypeInference.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T. Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action.

**basisKind:** extensional-structural-definition

**basisScope:** Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.

**verificationObligation:** Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.; Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance.

**reviewStatus:** Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-JavaWildcardCapture-capture"></a>

### capture

`urn:csabs:operation/JavaWildcardCapture-capture`

**signature:** capture : Γ×ParameterizedType×CapturedType×FreshBounds→Prop

**description:** Relate a capture result using one fresh variable per wildcard and the stipulated simultaneous bounds; reject invalid intersections.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Relate a capture result using one fresh variable per wildcard and the stipulated simultaneous bounds; reject invalid intersections.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-JavaWildcardCapture-bounds"></a>

### bounds

`urn:csabs:operation/JavaWildcardCapture-bounds`

**signature:** bounds : CapturedVariable→(LowerType×UpperType)

**description:** Return the lower and upper bounds attached to this particular fresh variable, not a replacement of it by either bound.

**precondition:** Inputs satisfy the selected typed profile.

**postcondition:** Return the lower and upper bounds attached to this particular fresh variable, not a replacement of it by either bound.

**totality:** Total mathematical operation on the stated carrier.

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-JavaWildcardCapture-wildcard-bounds"></a>

### wildcard-bounds

`urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds`

**statement:** For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T.

**formalStatement:** For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T.

**assumptions:** Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-JavaWildcardCapture-fresh-nonrecursive"></a>

### fresh-nonrecursive

`urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive`

**statement:** Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action.

**formalStatement:** Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action.

**assumptions:** Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-JavaWildcardCapture-exact-capture-identity"></a>

### exact-capture-identity

`urn:csabs:law/JavaWildcardCapture-exact-capture-identity`

**statement:** A parameterized type with only exact type arguments is unchanged by capture.

**formalStatement:** A parameterized type with only exact type arguments is unchanged by capture.

**assumptions:** Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [wildcard-bounds](JavaWildcardCapture.md#node-urn-csabs-axiom-JavaWildcardCapture-wildcard-bounds); [fresh-nonrecursive](JavaWildcardCapture.md#node-urn-csabs-axiom-JavaWildcardCapture-fresh-nonrecursive)

**proofSketch:** Each slot takes the exact-argument branch; no wildcard fresh variables or nested recursive conversions are introduced.

<a id="node-urn-csabs-law-JavaWildcardCapture-super-capture-lower-bound"></a>

### super-capture-lower-bound

`urn:csabs:law/JavaWildcardCapture-super-capture-lower-bound`

**statement:** Capturing G<? super B> yields a fresh S with lower bound B and substituted declared upper bound θ(U), rather than replacing S by θ(U).

**formalStatement:** Capturing G<? super B> yields a fresh S with lower bound B and substituted declared upper bound θ(U), rather than replacing S by θ(U).

**assumptions:** Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.; Variables have the explicitly declared typed carriers.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification; [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.

**provenanceKind:** derived

**dependsOn:** [wildcard-bounds](JavaWildcardCapture.md#node-urn-csabs-axiom-JavaWildcardCapture-wildcard-bounds); [fresh-nonrecursive](JavaWildcardCapture.md#node-urn-csabs-axiom-JavaWildcardCapture-fresh-nonrecursive)

**proofSketch:** Use the super-wildcard branch and freshness. The two bounds constrain S; neither identifies the unknown type with a bound.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java Language Specification, Java SE 25, §5.1.10: Capture Conversion](https://docs.oracle.com/javase/specs/jls/se25/html/jls-5.html#jls-5.1.10); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification
- [Java Language Specification, Java SE 25, §§4.4–4.10: generic types, erasure and subtyping](https://docs.oracle.com/javase/specs/jls/se25/html/jls-4.html); accessedOn: 2026-11-10; sourceRole: consulted-primary-language-specification

**sourceLocator:** JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds

**sourceNote:** Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/JavaWildcardCapture",
    "type": "Concept",
    "shortForm": "JavaWildcardCapture",
    "fullName": "Java wildcard capture with fresh bounded variables",
    "definition": "A nonrecursive conversion of wildcard arguments in one parameterized type to fresh bounded type variables, enabling a typed name for an unknown argument.",
    "notation": "capture(G<T₁,…,Tₙ>)=G<S₁,…,Sₙ>; Uᵢ′=Uᵢ[A:=S]; ?:nullType≤Sᵢ≤Uᵢ′; ? extends B:nullType≤Sᵢ≤glb(B,Uᵢ′); ? super B:B≤Sᵢ≤Uᵢ′",
    "category": [
      "urn:csabs:category/java-generics"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/JavaParameterizedType",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/JavaTypeInference",
      "urn:csabs:concept/Subtype"
    ],
    "hasOperation": [
      "urn:csabs:operation/JavaWildcardCapture-capture",
      "urn:csabs:operation/JavaWildcardCapture-bounds"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds",
      "urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive"
    ],
    "hasLaw": [
      "urn:csabs:law/JavaWildcardCapture-exact-capture-identity",
      "urn:csabs:law/JavaWildcardCapture-super-capture-lower-bound"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; selected Lean interpretations are separate from theorem witnesses.",
    "verificationObligation": [
      "Map language edition, carriers, identity, binding, substitution and phase-specific definedness explicitly.",
      "Shared profiles do not transfer language rules; structural validation and model compilation do not prove language conformance."
    ],
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T. Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action."
  },
  {
    "id": "urn:csabs:operation/JavaWildcardCapture-capture",
    "type": "Operation",
    "name": "capture",
    "signature": "capture : Γ×ParameterizedType×CapturedType×FreshBounds→Prop",
    "description": "Relate a capture result using one fresh variable per wildcard and the stipulated simultaneous bounds; reject invalid intersections.",
    "concept": "urn:csabs:concept/JavaWildcardCapture",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Relate a capture result using one fresh variable per wildcard and the stipulated simultaneous bounds; reject invalid intersections.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/JavaWildcardCapture-bounds",
    "type": "Operation",
    "name": "bounds",
    "signature": "bounds : CapturedVariable→(LowerType×UpperType)",
    "description": "Return the lower and upper bounds attached to this particular fresh variable, not a replacement of it by either bound.",
    "concept": "urn:csabs:concept/JavaWildcardCapture",
    "precondition": "Inputs satisfy the selected typed profile.",
    "postcondition": "Return the lower and upper bounds attached to this particular fresh variable, not a replacement of it by either bound.",
    "totality": "Total mathematical operation on the stated carrier.",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds",
    "type": "Axiom",
    "name": "wildcard-bounds",
    "statement": "For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T.",
    "formalStatement": "For θ=[A:=S], capture of ? has lower nullType and upper θ(U); ? extends B has lower nullType and upper glb(B,θ(U)); ? super B has lower B and upper θ(U); exact T yields S=T.",
    "assumptions": [
      "Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaWildcardCapture"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive",
    "type": "Axiom",
    "name": "fresh-nonrecursive",
    "statement": "Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action.",
    "formalStatement": "Each captured wildcard gets a distinct fresh type variable; capture applies to the arguments at this parameterized-type level only and introduces no runtime action.",
    "assumptions": [
      "Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaWildcardCapture"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Treats capture as a fresh-name relation with explicit upper/lower bounds; preserves the distinction between upper-bound knowledge and exact element type.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/JavaWildcardCapture-exact-capture-identity",
    "type": "Law",
    "name": "exact-capture-identity",
    "statement": "A parameterized type with only exact type arguments is unchanged by capture.",
    "formalStatement": "A parameterized type with only exact type arguments is unchanged by capture.",
    "assumptions": [
      "Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaWildcardCapture"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds",
      "urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive"
    ],
    "proofSketch": "Each slot takes the exact-argument branch; no wildcard fresh variables or nested recursive conversions are introduced."
  },
  {
    "id": "urn:csabs:law/JavaWildcardCapture-super-capture-lower-bound",
    "type": "Law",
    "name": "super-capture-lower-bound",
    "statement": "Capturing G<? super B> yields a fresh S with lower bound B and substituted declared upper bound θ(U), rather than replacing S by θ(U).",
    "formalStatement": "Capturing G<? super B> yields a fresh S with lower bound B and substituted declared upper bound θ(U), rather than replacing S by θ(U).",
    "assumptions": [
      "Java SE 25 JLS §5.1.10 profile on well-formed parameterized inputs. Each wildcard gets a distinct fresh identity, disjoint from the surrounding type variables. The lower bound nullType is the language null type, not a runtime null object. Bounds are simultaneous and glb is a well-formed intersection satisfying the JLS class compatibility checks. Exact type arguments are unchanged; capture is not recursively applied inside nested arguments. Separate capture applications need not yield identical fresh types. Comparing capture schemes modulo consistent renaming is an editorial observation, not Java equality of independently captured variables. No runtime conversion or ability to write an arbitrary value of the upper bound is implied.",
      "Variables have the explicitly declared typed carriers."
    ],
    "appliesTo": [
      "urn:csabs:concept/JavaWildcardCapture"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/generics-jls25-capture",
      "urn:csabs:source/generics-jls25-types"
    ],
    "sourceLocator": "JLS §5.1.10 capture clauses, nonrecursive application and absence of runtime action; §§4.4–4.5 for bounds",
    "sourceNote": "Catalog derivation from the linked premises in the explicitly selected abstraction. The consulted language clauses motivate the interface; this is not a claim that the entire language semantics is formalized.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds",
      "urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive"
    ],
    "proofSketch": "Use the super-wildcard branch and freshness. The two bounds constrain S; neither identifies the unknown type with a bound."
  }
]
```
<!-- graph-record:end -->
