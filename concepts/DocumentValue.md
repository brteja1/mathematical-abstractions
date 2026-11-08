# Finite JSON document value (interoperable profile)

A finite recursive tagged value: null, Boolean, exact finite decimal, Unicode scalar string, ordered array, or finite unique-key object.

**Notation:** D=μX.(1+Bool+Dec+String+Seq(X)+Map(String,X)); Dec={m·10^e | m,e∈ℤ}

**Stable ID:** `urn:csabs:concept/DocumentValue`

**Categories:** Relational data modelling

**Kind:** Abstract data type

**Prerequisites:** [Two-valued Boolean type](BooleanType.md), [Exact rational number](RationalNumber.md), [Finite sequence (List datatype)](Sequence.md), [Map](Map.md), [Structural Induction](StructuralInduction.md)

## Interface and scope

**axiomBasis:** Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag; case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null; To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value; member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined

**basisKind:** extensional-structural-definition

**basisScope:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DocumentValue-construct"></a>

### construct

`urn:csabs:operation/DocumentValue-construct`

**signature:** null; boolean:Bool→D; number:Dec→D; string:String→D; array:Seq(D)→D; object:Map(String,D)→D

**description:** Six disjoint constructors; finite well-founded recursion only.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Six disjoint constructors; finite well-founded recursion only.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DocumentValue-member"></a>

### member

`urn:csabs:operation/DocumentValue-member`

**signature:** member : D×String⇀D

**description:** For object(o) only, returns o(k) when bound; absent/nonobject undefined.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** For object(o) only, returns o(k) when bound; absent/nonobject undefined.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DocumentValue-index"></a>

### index

`urn:csabs:operation/DocumentValue-index`

**signature:** index : D×ℕ⇀D

**description:** For array(xs) only, returns xs[i] when i<|xs|; otherwise undefined.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** For array(xs) only, returns xs[i] when i<|xs|; otherwise undefined.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DocumentValue-case"></a>

### case

`urn:csabs:operation/DocumentValue-case`

**signature:** case : (1→C)×(Bool→C)×(Dec→C)×(String→C)×(Seq(D)→C)×(Map(String,D)→C)×D→C

**description:** Selects the branch for the outer tag; all branches total on their domains.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Selects the branch for the outer tag; all branches total on their domains.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DocumentValue-tagged-constructors"></a>

### tagged-constructors

`urn:csabs:axiom/DocumentValue-tagged-constructors`

**statement:** Defining requirement: Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag

**formalStatement:** Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DocumentValue-case-beta"></a>

### case-beta

`urn:csabs:axiom/DocumentValue-case-beta`

**statement:** Defining requirement: case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null

**formalStatement:** case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DocumentValue-induction"></a>

### induction

`urn:csabs:axiom/DocumentValue-induction`

**statement:** Defining requirement: To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value

**formalStatement:** To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DocumentValue-lookup-equations"></a>

### lookup-equations

`urn:csabs:axiom/DocumentValue-lookup-equations`

**statement:** Defining requirement: member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined

**formalStatement:** member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DocumentValue-boolean-injective"></a>

### boolean-injective

`urn:csabs:law/DocumentValue-boolean-injective`

**statement:** boolean(a)=boolean(b) ⇔ a=b

**formalStatement:** boolean(a)=boolean(b) ⇔ a=b

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [tagged-constructors](DocumentValue.md#node-urn-csabs-axiom-DocumentValue-tagged-constructors)

**proofSketch:** Use injectivity of the Boolean payload constructor.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-DocumentValue-null-not-false"></a>

### null-not-false

`urn:csabs:theorem/DocumentValue-null-not-false`

**statement:** null≠boolean(false)

**formalStatement:** null≠boolean(false)

**assumptions:** Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [tagged-constructors](DocumentValue.md#node-urn-csabs-axiom-DocumentValue-tagged-constructors)

**proofSketch:** The null and Boolean constructors have different tags.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [RFC 8259: The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Theorem Proving in Lean 4, chapter 7: inductive types](https://lean-lang.org/theorem_proving_in_lean4/Inductive-Types/); accessedOn: 2026-11-07; sourceRole: inductive-constructor-and-elimination-principles

**sourceLocator:** §§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DocumentValue",
    "type": "Concept",
    "shortForm": "DocumentValue",
    "fullName": "Finite JSON document value (interoperable profile)",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite recursive tagged value: null, Boolean, exact finite decimal, Unicode scalar string, ordered array, or finite unique-key object.",
    "notation": "D=μX.(1+Bool+Dec+String+Seq(X)+Map(String,X)); Dec={m·10^e | m,e∈ℤ}",
    "requiresConcept": [
      "urn:csabs:concept/BooleanType",
      "urn:csabs:concept/RationalNumber",
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Map",
      "urn:csabs:concept/StructuralInduction"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DocumentValue-construct",
      "urn:csabs:operation/DocumentValue-member",
      "urn:csabs:operation/DocumentValue-index",
      "urn:csabs:operation/DocumentValue-case"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DocumentValue-tagged-constructors",
      "urn:csabs:axiom/DocumentValue-case-beta",
      "urn:csabs:axiom/DocumentValue-induction",
      "urn:csabs:axiom/DocumentValue-lookup-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/DocumentValue-boolean-injective"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DocumentValue-null-not-false"
    ],
    "axiomBasis": "Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag; case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null; To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value; member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DocumentValue-construct",
    "type": "Operation",
    "name": "construct",
    "signature": "null; boolean:Bool→D; number:Dec→D; string:String→D; array:Seq(D)→D; object:Map(String,D)→D",
    "description": "Six disjoint constructors; finite well-founded recursion only.",
    "concept": "urn:csabs:concept/DocumentValue",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Six disjoint constructors; finite well-founded recursion only.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DocumentValue-member",
    "type": "Operation",
    "name": "member",
    "signature": "member : D×String⇀D",
    "description": "For object(o) only, returns o(k) when bound; absent/nonobject undefined.",
    "concept": "urn:csabs:concept/DocumentValue",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "For object(o) only, returns o(k) when bound; absent/nonobject undefined.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DocumentValue-index",
    "type": "Operation",
    "name": "index",
    "signature": "index : D×ℕ⇀D",
    "description": "For array(xs) only, returns xs[i] when i<|xs|; otherwise undefined.",
    "concept": "urn:csabs:concept/DocumentValue",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "For array(xs) only, returns xs[i] when i<|xs|; otherwise undefined.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DocumentValue-case",
    "type": "Operation",
    "name": "case",
    "signature": "case : (1→C)×(Bool→C)×(Dec→C)×(String→C)×(Seq(D)→C)×(Map(String,D)→C)×D→C",
    "description": "Selects the branch for the outer tag; all branches total on their domains.",
    "concept": "urn:csabs:concept/DocumentValue",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Selects the branch for the outer tag; all branches total on their domains.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DocumentValue-tagged-constructors",
    "type": "Axiom",
    "name": "tagged-constructors",
    "statement": "Defining requirement: Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag",
    "formalStatement": "Distinct constructor tags are unequal; each constructor is injective in its semantic payload; every D has exactly one outer tag",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DocumentValue-case-beta",
    "type": "Axiom",
    "name": "case-beta",
    "statement": "Defining requirement: case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null",
    "formalStatement": "case(h₀,h_b,h_n,h_s,h_a,h_o,constructor_i(x))=h_i(x), using unit payload for null",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DocumentValue-induction",
    "type": "Axiom",
    "name": "induction",
    "statement": "Defining requirement: To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value",
    "formalStatement": "To prove P for all D, prove scalar/null cases and array/object cases assuming P for every immediate child value",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DocumentValue-lookup-equations",
    "type": "Axiom",
    "name": "lookup-equations",
    "statement": "Defining requirement: member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined",
    "formalStatement": "member(object(o),k)=o(k) when bound; index(array(xs),i)=xs[i] for i<|xs|; other cases undefined",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DocumentValue-boolean-injective",
    "type": "Law",
    "name": "boolean-injective",
    "statement": "boolean(a)=boolean(b) ⇔ a=b",
    "formalStatement": "boolean(a)=boolean(b) ⇔ a=b",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DocumentValue-tagged-constructors"
    ],
    "proofSketch": "Use injectivity of the Boolean payload constructor.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/DocumentValue-null-not-false",
    "type": "Theorem",
    "name": "null-not-false",
    "statement": "null≠boolean(false)",
    "formalStatement": "null≠boolean(false)",
    "assumptions": [
      "Chosen semantic profile, stricter than accepting every RFC syntax: object keys unique; strings scalar Unicode sequences; numbers exact finite decimal rationals, numeric spellings and negative zero identified by value. Objects unordered, arrays ordered. No duplicate-key policy, unpaired surrogates, reference cycles, NaN, infinity or parser/serializer claim.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DocumentValue"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DocumentValue-tagged-constructors"
    ],
    "proofSketch": "The null and Boolean constructors have different tags.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/json-values-core",
      "urn:csabs:source/lean4-inductive-types"
    ],
    "sourceLocator": "§§3–8.2: values, objects, arrays, numbers and Unicode interoperability; §§7.1, 7.5–7.6, 7.9: enumeration, recursive/nested inductives, constructors and recursors",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
