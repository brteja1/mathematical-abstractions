# Ordered template packs and structural expansion

Finite kind-indexed argument sequences with pointwise pack expansion, equal-length simultaneous expansion and explicit fold parenthesization.

**Notation:** Pack(K)=Seq(Arg_K); expand(f,[a₁,…,aₙ])=[f(a₁),…,f(aₙ)]; zipExpand(g,p,q) defined iff |p|=|q|; foldL/foldR preserve grouping

**Stable ID:** `urn:csabs:concept/TemplateParameterPack`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Function type](FunctionType.md)

**Specializes:** [Finite sequence (List datatype)](Sequence.md)

**Related concepts:** [Kinded partial template metafunction](TemplateMetafunction.md), [Ordered substitution with immediate-context failure](TemplateSubstitution.md)

## Interface and scope

**axiomBasis:** Selected defining rules: expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree. zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|. foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.

**specializationNote:** Fix a parameter kind K and instantiate Sequence element carrier with canonical arguments Arg_K. Retain sequence order, length, equality and empty case; add the expansion/fold-shape operations. This is a mathematical representation profile, not a runtime C++ container.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TemplateParameterPack-expand"></a>

### expand

`urn:csabs:operation/TemplateParameterPack-expand`

**signature:** expand : (A→B)×Pack(A)→Pack(B)

**description:** Apply the pattern once per corresponding element, retaining order and multiplicity.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** Apply the pattern once per corresponding element, retaining order and multiplicity.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateParameterPack-zip-expand"></a>

### zip-expand

`urn:csabs:operation/TemplateParameterPack-zip-expand`

**signature:** zipExpand : (A×B→C)×Pack(A)×Pack(B)⇀Pack(C)

**description:** Produce g(aᵢ,bᵢ) in order when lengths agree.

**precondition:** Both participating packs have the same length.

**postcondition:** Produce g(aᵢ,bᵢ) in order when lengths agree.

**totality:** Partial on unequal lengths; no truncation or Cartesian-product fallback.

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TemplateParameterPack-fold-shapes"></a>

### fold-shapes

`urn:csabs:operation/TemplateParameterPack-fold-shapes`

**signature:** foldL,foldR : Op×Expr×Pack(Expr)→Expr

**description:** foldL builds (((init op e₁) op e₂)…); foldR builds e₁ op (e₂ op (… op init)); empty binary folds return init.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** foldL builds (((init op e₁) op e₂)…); foldR builds e₁ op (e₂ op (… op init)); empty binary folds return init.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TemplateParameterPack-ordered-expansion"></a>

### ordered-expansion

`urn:csabs:axiom/TemplateParameterPack-ordered-expansion`

**statement:** expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree.

**formalStatement:** expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree.

**assumptions:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateParameterPack-simultaneous-expansion"></a>

### simultaneous-expansion

`urn:csabs:axiom/TemplateParameterPack-simultaneous-expansion`

**statement:** zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|.

**formalStatement:** zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|.

**assumptions:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-TemplateParameterPack-fold-parentheses"></a>

### fold-parentheses

`urn:csabs:axiom/TemplateParameterPack-fold-parentheses`

**statement:** foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases.

**formalStatement:** foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases.

**assumptions:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-TemplateParameterPack-expansion-length"></a>

### expansion-length

`urn:csabs:law/TemplateParameterPack-expansion-length`

**statement:** |expand(f,p)|=|p|, including p=[].

**formalStatement:** |expand(f,p)|=|p|, including p=[].

**assumptions:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [ordered-expansion](TemplateParameterPack.md#node-urn-csabs-axiom-TemplateParameterPack-ordered-expansion)

**proofSketch:** Induct on the sequence: empty expansion has length zero and each cons contributes exactly one result.

<a id="node-urn-csabs-law-TemplateParameterPack-zip-not-product"></a>

### zip-not-product

`urn:csabs:law/TemplateParameterPack-zip-not-product`

**statement:** |p|=|q|=n ⇒ |zipExpand(g,p,q)|=n, even if n>1; an empty pair of packs expands to [].

**formalStatement:** |p|=|q|=n ⇒ |zipExpand(g,p,q)|=n, even if n>1; an empty pair of packs expands to [].

**assumptions:** C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [simultaneous-expansion](TemplateParameterPack.md#node-urn-csabs-axiom-TemplateParameterPack-simultaneous-expansion)

**proofSketch:** Use the defining length equation; each index contributes one result, not n pairings.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [temp.variadic] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/temp.variadic); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms

**sourceNote:** Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TemplateParameterPack",
    "type": "Concept",
    "shortForm": "TemplateParameterPack",
    "fullName": "Ordered template packs and structural expansion",
    "definition": "Finite kind-indexed argument sequences with pointwise pack expansion, equal-length simultaneous expansion and explicit fold parenthesization.",
    "notation": "Pack(K)=Seq(Arg_K); expand(f,[a₁,…,aₙ])=[f(a₁),…,f(aₙ)]; zipExpand(g,p,q) defined iff |p|=|q|; foldL/foldR preserve grouping",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/FunctionType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/TemplateSubstitution"
    ],
    "hasOperation": [
      "urn:csabs:operation/TemplateParameterPack-expand",
      "urn:csabs:operation/TemplateParameterPack-zip-expand",
      "urn:csabs:operation/TemplateParameterPack-fold-shapes"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TemplateParameterPack-ordered-expansion",
      "urn:csabs:axiom/TemplateParameterPack-simultaneous-expansion",
      "urn:csabs:axiom/TemplateParameterPack-fold-parentheses"
    ],
    "hasLaw": [
      "urn:csabs:law/TemplateParameterPack-expansion-length",
      "urn:csabs:law/TemplateParameterPack-zip-not-product"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Sequence"
    ],
    "specializationNote": "Fix a parameter kind K and instantiate Sequence element carrier with canonical arguments Arg_K. Retain sequence order, length, equality and empty case; add the expansion/fold-shape operations. This is a mathematical representation profile, not a runtime C++ container.",
    "axiomBasis": "Selected defining rules: expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree. zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|. foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases."
  },
  {
    "id": "urn:csabs:operation/TemplateParameterPack-expand",
    "type": "Operation",
    "name": "expand",
    "signature": "expand : (A→B)×Pack(A)→Pack(B)",
    "description": "Apply the pattern once per corresponding element, retaining order and multiplicity.",
    "concept": "urn:csabs:concept/TemplateParameterPack",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "Apply the pattern once per corresponding element, retaining order and multiplicity.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateParameterPack-zip-expand",
    "type": "Operation",
    "name": "zip-expand",
    "signature": "zipExpand : (A×B→C)×Pack(A)×Pack(B)⇀Pack(C)",
    "description": "Produce g(aᵢ,bᵢ) in order when lengths agree.",
    "concept": "urn:csabs:concept/TemplateParameterPack",
    "precondition": "Both participating packs have the same length.",
    "postcondition": "Produce g(aᵢ,bᵢ) in order when lengths agree.",
    "totality": "Partial on unequal lengths; no truncation or Cartesian-product fallback.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TemplateParameterPack-fold-shapes",
    "type": "Operation",
    "name": "fold-shapes",
    "signature": "foldL,foldR : Op×Expr×Pack(Expr)→Expr",
    "description": "foldL builds (((init op e₁) op e₂)…); foldR builds e₁ op (e₂ op (… op init)); empty binary folds return init.",
    "concept": "urn:csabs:concept/TemplateParameterPack",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "foldL builds (((init op e₁) op e₂)…); foldR builds e₁ op (e₂ op (… op init)); empty binary folds return init.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TemplateParameterPack-ordered-expansion",
    "type": "Axiom",
    "name": "ordered-expansion",
    "statement": "expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree.",
    "formalStatement": "expand(f,[])=[]; expand(f,x::xs)=f(x)::expand(f,xs); packs are equal iff lengths and corresponding canonical arguments agree.",
    "assumptions": [
      "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateParameterPack"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateParameterPack-simultaneous-expansion",
    "type": "Axiom",
    "name": "simultaneous-expansion",
    "statement": "zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|.",
    "formalStatement": "zipExpand(g,p,q) is defined iff |p|=|q|; its i-th element is g(pᵢ,qᵢ), and its length is |p|.",
    "assumptions": [
      "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateParameterPack"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/TemplateParameterPack-fold-parentheses",
    "type": "Axiom",
    "name": "fold-parentheses",
    "statement": "foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases.",
    "formalStatement": "foldL(op,z,[])=z; foldL(op,z,x::xs)=foldL(op,Node(op,z,x),xs); foldR(op,z,[])=z; foldR(op,z,x::xs)=Node(op,x,foldR(op,z,xs)). Empty unary folds are limited to the specified &&, || and comma cases.",
    "assumptions": [
      "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateParameterPack"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Reuses finite sequences as the pack carrier and gives a pure ordered expansion interface. Type/value/template kinds are supplied per instantiation; C++ evaluation sequencing is not inferred from list order.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/TemplateParameterPack-expansion-length",
    "type": "Law",
    "name": "expansion-length",
    "statement": "|expand(f,p)|=|p|, including p=[].",
    "formalStatement": "|expand(f,p)|=|p|, including p=[].",
    "assumptions": [
      "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateParameterPack"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateParameterPack-ordered-expansion"
    ],
    "proofSketch": "Induct on the sequence: empty expansion has length zero and each cons contributes exactly one result."
  },
  {
    "id": "urn:csabs:law/TemplateParameterPack-zip-not-product",
    "type": "Law",
    "name": "zip-not-product",
    "statement": "|p|=|q|=n ⇒ |zipExpand(g,p,q)|=n, even if n>1; an empty pair of packs expands to [].",
    "formalStatement": "|p|=|q|=n ⇒ |zipExpand(g,p,q)|=n, even if n>1; an empty pair of packs expands to [].",
    "assumptions": [
      "C++20 N4861 pure list-result abstraction after deduction and kind checking. Argument order and duplicates are observable. A simultaneous expansion zips corresponding elements, not a Cartesian product; this profile has two participating packs, with generalization explicit. The pattern supplied here is total on its selected carrier; actual invalid pattern instantiations need TemplateSubstitution/TemplateConstraint treatment. Generated expression shape is distinct from operand evaluation order. Nested expansions, overloads/effects of fold operators and context-specific grammar are not modeled. Empty unary fold identities exist only for && (true), || (false) and comma (void()), per the source; no empty + identity is invented.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/TemplateParameterPack"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-temp.variadic"
    ],
    "sourceLocator": "[temp.variadic] ¶1, ¶7–10: pack expansion, simultaneous lengths, zero length and fold forms",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/TemplateParameterPack-simultaneous-expansion"
    ],
    "proofSketch": "Use the defining length equation; each index contributes one result, not n pairings."
  }
]
```
<!-- graph-record:end -->
