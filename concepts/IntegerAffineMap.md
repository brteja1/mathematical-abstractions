# Integer quasi-affine index map

A finite tuple of exact integer expressions over separately bound dimensions and symbols, allowing addition, constant multiplication and floor/ceiling division or modulo by positive constants.

**Notation:** (d∈ℤⁿ,s∈ℤᵏ)↦(e₁(d,s),…,eₘ(d,s)); 0≤x mod c<c for c>0

**Stable ID:** `urn:csabs:concept/IntegerAffineMap`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** Function

**Prerequisites:** [Mathematical integers](Integer.md), [Total function](Function.md)

**Specializes:** [Total function](Function.md)

**Related concepts:** [Finite rectangular matrix over a field](Matrix.md), [Memory dependence and legal loop rescheduling](LoopDependence.md), [Modular Integer](ModularInteger.md)

## Backlinks

- [Target-indexed storage and ABI layout](DataLayout.md) — `relatedConcept`
- [Memory dependence and legal loop rescheduling](LoopDependence.md) — `requiresConcept`
- [Guarded loop event-domain correspondence](LoopIterationMapping.md) — `relatedConcept`

## Mathematical formulation

A finite tuple of exact integer expressions over separately bound dimensions and symbols, allowing addition, constant multiplication and floor/ceiling division or modulo by positive constants. (d∈ℤⁿ,s∈ℤᵏ)↦(e₁(d,s),…,eₘ(d,s)); 0≤x mod c<c for c>0 Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.

**Lean formulation** (in its source module context):

```lean
abbrev IntegerAffineMap (dimensions symbols results : Nat) :=
  Fin results → AffineExpr (dimensions + symbols)
```

**Source:** [`Catalog.Transforms.IntegerAffineMap`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Finite tuple of positive-divisor expression syntax over Fin(dimensions+symbols); function interpretation needs an evaluator.

**Limits:** Lean encodes syntax and divisor positivity only; evaluation/composition, symbol validity, Presburger solving and index-to-machine arithmetic correspondence are not implemented.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.; ∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.

**basisKind:** relational-structural-definition

**basisScope:** Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.

**specializationNote:** Instantiate the parent carrier and operation as follows: Finite tuple of positive-divisor expression syntax over Fin(dimensions+symbols); function interpretation needs an evaluator.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean encodes syntax and divisor positivity only; evaluation/composition, symbol validity, Presburger solving and index-to-machine arithmetic correspondence are not implemented.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-IntegerAffineMap-evaluate"></a>

### evaluate

`urn:csabs:operation/IntegerAffineMap-evaluate`

**signature:** evaluate : Map(n,k,m)×ℤⁿ×ℤᵏ→ℤᵐ

**description:** Evaluate all expressions with exact Euclidean floor/ceiling/modulo semantics.

**precondition:** Arity, dimension/symbol binding and positive divisors valid.

**postcondition:** Evaluate all expressions with exact Euclidean floor/ceiling/modulo semantics.

**totality:** Total on well-formed maps.

**source:** [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IntegerAffineMap-compose"></a>

### compose

`urn:csabs:operation/IntegerAffineMap-compose`

**signature:** compose : Map(n,k,m)×Map(m,k,r)→Map(n,k,r)

**description:** Substitute dimension expressions, consistently renaming/shared-binding symbols.

**precondition:** Symbol environments agree or are explicitly merged.

**postcondition:** Substitute dimension expressions, consistently renaming/shared-binding symbols.

**totality:** Total after arity and binding alignment.

**source:** [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-IntegerAffineMap-expression-grammar"></a>

### expression-grammar

`urn:csabs:axiom/IntegerAffineMap-expression-grammar`

**description:** Defining obligation for Integer quasi-affine index map

**statement:** e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.

**formalStatement:** e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.

**assumptions:** Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-IntegerAffineMap-euclidean-division"></a>

### euclidean-division

`urn:csabs:axiom/IntegerAffineMap-euclidean-division`

**description:** Defining obligation for Integer quasi-affine index map

**statement:** ∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.

**formalStatement:** ∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.

**assumptions:** Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-IntegerAffineMap-modulo-constant-range"></a>

### modulo-constant-range

`urn:csabs:law/IntegerAffineMap-modulo-constant-range`

**description:** Derived consequence within the selected semantic profile.

**statement:** For a well-formed modulo expression e mod c with positive literal c, every evaluated result belongs to {0,…,c−1}, including negative values of e.

**formalStatement:** For a well-formed modulo expression e mod c with positive literal c, every evaluated result belongs to {0,…,c−1}, including negative values of e.

**assumptions:** Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.

**dependsOn:** [euclidean-division](IntegerAffineMap.md#node-urn-csabs-axiom-IntegerAffineMap-euclidean-division)

**proofSketch:** Instantiate the remainder bounds with the exact integer value of e. A nonnegative integer strictly below positive c is at most c−1.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Affine dialect (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Dialects/Affine.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Dialects/Affine.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/IntegerAffineMap",
    "type": "Concept",
    "shortForm": "IntegerAffineMap",
    "fullName": "Integer quasi-affine index map",
    "definition": "A finite tuple of exact integer expressions over separately bound dimensions and symbols, allowing addition, constant multiplication and floor/ceiling division or modulo by positive constants.",
    "notation": "(d∈ℤⁿ,s∈ℤᵏ)↦(e₁(d,s),…,eₘ(d,s)); 0≤x mod c<c for c>0",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/function",
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Matrix",
      "urn:csabs:concept/LoopDependence",
      "urn:csabs:concept/ModularInteger"
    ],
    "hasOperation": [
      "urn:csabs:operation/IntegerAffineMap-evaluate",
      "urn:csabs:operation/IntegerAffineMap-compose"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/IntegerAffineMap-expression-grammar",
      "urn:csabs:axiom/IntegerAffineMap-euclidean-division"
    ],
    "hasLaw": [
      "urn:csabs:law/IntegerAffineMap-modulo-constant-range"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.",
    "axiomBasis": "e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.; ∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean encodes syntax and divisor positivity only; evaluation/composition, symbol validity, Presburger solving and index-to-machine arithmetic correspondence are not implemented."
    ],
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Function"
    ],
    "specializationNote": "Instantiate the parent carrier and operation as follows: Finite tuple of positive-divisor expression syntax over Fin(dimensions+symbols); function interpretation needs an evaluator.",
    "mathematicalFormulation": "A finite tuple of exact integer expressions over separately bound dimensions and symbols, allowing addition, constant multiplication and floor/ceiling division or modulo by positive constants. (d∈ℤⁿ,s∈ℤᵏ)↦(e₁(d,s),…,eₘ(d,s)); 0≤x mod c<c for c>0 Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap.",
    "leanFormulation": "abbrev IntegerAffineMap (dimensions symbols results : Nat) :=\n  Fin results → AffineExpr (dimensions + symbols)",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.IntegerAffineMap",
    "formulationScope": "partial",
    "leanModelMapping": "Finite tuple of positive-divisor expression syntax over Fin(dimensions+symbols); function interpretation needs an evaluator.",
    "leanModelLimitations": "Lean encodes syntax and divisor positivity only; evaluation/composition, symbol validity, Presburger solving and index-to-machine arithmetic correspondence are not implemented."
  },
  {
    "id": "urn:csabs:operation/IntegerAffineMap-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "evaluate : Map(n,k,m)×ℤⁿ×ℤᵏ→ℤᵐ",
    "description": "Evaluate all expressions with exact Euclidean floor/ceiling/modulo semantics.",
    "concept": "urn:csabs:concept/IntegerAffineMap",
    "precondition": "Arity, dimension/symbol binding and positive divisors valid.",
    "postcondition": "Evaluate all expressions with exact Euclidean floor/ceiling/modulo semantics.",
    "totality": "Total on well-formed maps.",
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IntegerAffineMap-compose",
    "type": "Operation",
    "name": "compose",
    "signature": "compose : Map(n,k,m)×Map(m,k,r)→Map(n,k,r)",
    "description": "Substitute dimension expressions, consistently renaming/shared-binding symbols.",
    "concept": "urn:csabs:concept/IntegerAffineMap",
    "precondition": "Symbol environments agree or are explicitly merged.",
    "postcondition": "Substitute dimension expressions, consistently renaming/shared-binding symbols.",
    "totality": "Total after arity and binding alignment.",
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/IntegerAffineMap-expression-grammar",
    "type": "Axiom",
    "name": "expression-grammar",
    "description": "Defining obligation for Integer quasi-affine index map",
    "statement": "e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.",
    "formalStatement": "e ::= dᵢ | sⱼ | c | e+e | c·e | floor(e/c⁺) | ceil(e/c⁺) | e mod c⁺, with c∈ℤ,c⁺>0.",
    "assumptions": [
      "Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntegerAffineMap"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/IntegerAffineMap-euclidean-division",
    "type": "Axiom",
    "name": "euclidean-division",
    "description": "Defining obligation for Integer quasi-affine index map",
    "statement": "∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.",
    "formalStatement": "∀x∈ℤ,c>0, x=c·floor(x/c)+(x mod c) ∧ 0≤x mod c<c.",
    "assumptions": [
      "Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntegerAffineMap"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/IntegerAffineMap-modulo-constant-range",
    "type": "Law",
    "name": "modulo-constant-range",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "For a well-formed modulo expression e mod c with positive literal c, every evaluated result belongs to {0,…,c−1}, including negative values of e.",
    "formalStatement": "For a well-formed modulo expression e mod c with positive literal c, every evaluated result belongs to {0,…,c−1}, including negative values of e.",
    "assumptions": [
      "Exact mathematical integers; dimensions and symbols have distinct binding/validity rules in MLIR. Empty input/result tuples are allowed. Multiplication is by literal integer constants; divisors are positive constants. Semi-affine symbolic products/divisors are outside this profile. Modulo is nonnegative, including negative dividends (the local documentation phrase positive results is normalized to include zero). MLIR index lowering has target-dependent width: correspondence to exact arithmetic needs range/no-overflow proof. This extends ordinary affine maps with quasi-affine operations and therefore is not a specialization of LinearMap."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntegerAffineMap"
    ],
    "dependsOn": [
      "urn:csabs:axiom/IntegerAffineMap-euclidean-division"
    ],
    "proofSketch": "Instantiate the remainder bounds with the exact integer value of e. A nonnegative integer strictly below positive c is at most c−1.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-affine"
    ],
    "sourceLocator": "Affine dialect: Dimensions and Symbols, Affine Expressions, Affine Maps, Integer Sets",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
