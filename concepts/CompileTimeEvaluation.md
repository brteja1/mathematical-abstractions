# Checked signed-integer constant-evaluation fragment

A pure partial evaluator for closed signed-integer literal, addition, multiplication and Boolean-conditional expressions, rejecting evaluated overflow and evaluating only the chosen conditional branch.

**Notation:** Expr ::= Lit(z) | Add(Expr,Expr) | Mul(Expr,Expr) | If(Bool,Expr,Expr); Rw=[−2^(w−1),2^(w−1)−1]; evalw:Expr⇀Rw

**Stable ID:** `urn:csabs:concept/CompileTimeEvaluation`

**Categories:** Programming-language semantics → Generic programming → Template metaprogramming

**Kind:** Function

**Prerequisites:** [Fixed-width signed integer](FixedWidthSignedInteger.md), [Partial function](PartialFunction.md)

**Related concepts:** [Kinded partial template metafunction](TemplateMetafunction.md), [Termination Variant](TerminationVariant.md)

## Backlinks

- [Kinded partial template metafunction](TemplateMetafunction.md) — `relatedConcept`
- [VHDL generic elaboration and static structural generation](VHDLGenericElaboration.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining rules: evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw. evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined. evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed.

**basisKind:** extensional-structural-definition

**basisScope:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.

**verificationObligation:** Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.; Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces.

**reviewStatus:** Editorial source/interface review; model bindings and compiled theorem witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-CompileTimeEvaluation-evaluate"></a>

### evaluate

`urn:csabs:operation/CompileTimeEvaluation-evaluate`

**signature:** evaluate : Width×Expr⇀Integer

**description:** Evaluate representable leaves; for Add/Mul evaluate both operands then require the exact integer result in Rw; for If evaluate only the selected branch.

**precondition:** w and every literal leaf meet the selected signed-type profile.

**postcondition:** Evaluate representable leaves; for Add/Mul evaluate both operands then require the exact integer result in Rw; for If evaluate only the selected branch.

**totality:** Partial when an evaluated arithmetic step is out of range; finite expression structure alone does not guarantee definedness.

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-CompileTimeEvaluation-in-range"></a>

### in-range

`urn:csabs:operation/CompileTimeEvaluation-in-range`

**signature:** inRange : Width×Integer→Prop

**description:** inRange(w,z) iff −2^(w−1)≤z≤2^(w−1)−1.

**precondition:** Typed inputs satisfying the selected profile.

**postcondition:** inRange(w,z) iff −2^(w−1)≤z≤2^(w−1)−1.

**totality:** Total mathematical operation on the stated inputs.

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CompileTimeEvaluation-literal-range"></a>

### literal-range

`urn:csabs:axiom/CompileTimeEvaluation-literal-range`

**statement:** evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw.

**formalStatement:** evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw.

**assumptions:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-CompileTimeEvaluation-checked-arithmetic"></a>

### checked-arithmetic

`urn:csabs:axiom/CompileTimeEvaluation-checked-arithmetic`

**statement:** evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined.

**formalStatement:** evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined.

**assumptions:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-CompileTimeEvaluation-selected-branch"></a>

### selected-branch

`urn:csabs:axiom/CompileTimeEvaluation-selected-branch`

**statement:** evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed.

**formalStatement:** evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed.

**assumptions:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-CompileTimeEvaluation-unchosen-overflow-irrelevant"></a>

### unchosen-overflow-irrelevant

`urn:csabs:law/CompileTimeEvaluation-unchosen-overflow-irrelevant`

**statement:** evalw(e)=v ⇒ evalw(If(true,e,f))=v even if evalw(f) is undefined due to overflow.

**formalStatement:** evalw(e)=v ⇒ evalw(If(true,e,f))=v even if evalw(f) is undefined due to overflow.

**assumptions:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [literal-range](CompileTimeEvaluation.md#node-urn-csabs-axiom-CompileTimeEvaluation-literal-range); [selected-branch](CompileTimeEvaluation.md#node-urn-csabs-axiom-CompileTimeEvaluation-selected-branch)

**proofSketch:** Use the true-branch equation; no evaluation of f is requested. The rule does not permit syntactically or type-invalid unchosen branches.

<a id="node-urn-csabs-law-CompileTimeEvaluation-overflow-is-not-wrapping"></a>

### overflow-is-not-wrapping

`urn:csabs:law/CompileTimeEvaluation-overflow-is-not-wrapping`

**statement:** evalw(e)=max(Rw) ∧ evalw(f)=1 ⇒ evalw(Add(e,f)) is undefined, not min(Rw).

**formalStatement:** evalw(e)=max(Rw) ∧ evalw(f)=1 ⇒ evalw(Add(e,f)) is undefined, not min(Rw).

**assumptions:** C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.; All variables use the typed carriers and fixed environments declared in this entry.

**reviewStatus:** Editorial mathematical statement; no compiled theorem witness asserted.

**notationLanguage:** informal mathematical Unicode

**source:** [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause; [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.

**provenanceKind:** derived

**dependsOn:** [literal-range](CompileTimeEvaluation.md#node-urn-csabs-axiom-CompileTimeEvaluation-literal-range); [checked-arithmetic](CompileTimeEvaluation.md#node-urn-csabs-axiom-CompileTimeEvaluation-checked-arithmetic)

**proofSketch:** The exact sum exceeds the maximum representable signed value, so the range premise for addition fails. No modulo rule applies to this signed profile.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [C++20 working draft N4861 [expr.const] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.const); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [expr.cond] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/expr.cond); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [basic.fundamental] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/basic.fundamental); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause
- [C++20 working draft N4861 [dcl.constexpr] (HTML rendering)](https://timsong-cpp.github.io/cppwp/n4861/dcl.constexpr); accessedOn: 2026-11-10; sourceRole: consulted-primary-working-draft-clause

**sourceLocator:** [expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]

**sourceNote:** Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CompileTimeEvaluation",
    "type": "Concept",
    "shortForm": "CompileTimeEvaluation",
    "fullName": "Checked signed-integer constant-evaluation fragment",
    "definition": "A pure partial evaluator for closed signed-integer literal, addition, multiplication and Boolean-conditional expressions, rejecting evaluated overflow and evaluating only the chosen conditional branch.",
    "notation": "Expr ::= Lit(z) | Add(Expr,Expr) | Mul(Expr,Expr) | If(Bool,Expr,Expr); Rw=[−2^(w−1),2^(w−1)−1]; evalw:Expr⇀Rw",
    "category": [
      "urn:csabs:category/template-metaprogramming"
    ],
    "kind": "urn:csabs:kind/function",
    "requiresConcept": [
      "urn:csabs:concept/FixedWidthSignedInteger",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TemplateMetafunction",
      "urn:csabs:concept/TerminationVariant"
    ],
    "hasOperation": [
      "urn:csabs:operation/CompileTimeEvaluation-evaluate",
      "urn:csabs:operation/CompileTimeEvaluation-in-range"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CompileTimeEvaluation-literal-range",
      "urn:csabs:axiom/CompileTimeEvaluation-checked-arithmetic",
      "urn:csabs:axiom/CompileTimeEvaluation-selected-branch"
    ],
    "hasLaw": [
      "urn:csabs:law/CompileTimeEvaluation-unchosen-overflow-irrelevant",
      "urn:csabs:law/CompileTimeEvaluation-overflow-is-not-wrapping"
    ],
    "hasTheorem": [],
    "basisKind": "extensional-structural-definition",
    "basisScope": "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; model bindings and compiled theorem witnesses are separate.",
    "verificationObligation": [
      "Use the stated C++20 N4861 profile and map types, argument equivalence, visibility, definedness and implementation limits explicitly.",
      "Do not infer an entire compiler semantics, decidability, universal termination or executable proof from these selected interfaces."
    ],
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted",
    "axiomBasis": "Selected defining rules: evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw. evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined. evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed."
  },
  {
    "id": "urn:csabs:operation/CompileTimeEvaluation-evaluate",
    "type": "Operation",
    "name": "evaluate",
    "signature": "evaluate : Width×Expr⇀Integer",
    "description": "Evaluate representable leaves; for Add/Mul evaluate both operands then require the exact integer result in Rw; for If evaluate only the selected branch.",
    "concept": "urn:csabs:concept/CompileTimeEvaluation",
    "precondition": "w and every literal leaf meet the selected signed-type profile.",
    "postcondition": "Evaluate representable leaves; for Add/Mul evaluate both operands then require the exact integer result in Rw; for If evaluate only the selected branch.",
    "totality": "Partial when an evaluated arithmetic step is out of range; finite expression structure alone does not guarantee definedness.",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/CompileTimeEvaluation-in-range",
    "type": "Operation",
    "name": "in-range",
    "signature": "inRange : Width×Integer→Prop",
    "description": "inRange(w,z) iff −2^(w−1)≤z≤2^(w−1)−1.",
    "concept": "urn:csabs:concept/CompileTimeEvaluation",
    "precondition": "Typed inputs satisfying the selected profile.",
    "postcondition": "inRange(w,z) iff −2^(w−1)≤z≤2^(w−1)−1.",
    "totality": "Total mathematical operation on the stated inputs.",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/CompileTimeEvaluation-literal-range",
    "type": "Axiom",
    "name": "literal-range",
    "statement": "evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw.",
    "formalStatement": "evalw(Lit(z))=z for z∈Rw; every defined evaluator result belongs to Rw.",
    "assumptions": [
      "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/CompileTimeEvaluation-checked-arithmetic",
    "type": "Axiom",
    "name": "checked-arithmetic",
    "statement": "evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined.",
    "formalStatement": "evalw(Add(e,f))=x+y iff evalw(e)=x, evalw(f)=y and x+y∈Rw; multiplication uses x·y with the same range requirement. An evaluated overflowing intermediate makes the enclosing arithmetic undefined.",
    "assumptions": [
      "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/CompileTimeEvaluation-selected-branch",
    "type": "Axiom",
    "name": "selected-branch",
    "statement": "evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed.",
    "formalStatement": "evalw(If(true,e,f))=evalw(e); evalw(If(false,e,f))=evalw(f), including equality of partial results; both branches are structurally well-formed.",
    "assumptions": [
      "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Defines a deliberately small evaluator using the cited integer range and evaluated-path rules. It is not the complete constexpr abstract machine; the C++ example records its compiler and uses actual int limits.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/CompileTimeEvaluation-unchosen-overflow-irrelevant",
    "type": "Law",
    "name": "unchosen-overflow-irrelevant",
    "statement": "evalw(e)=v ⇒ evalw(If(true,e,f))=v even if evalw(f) is undefined due to overflow.",
    "formalStatement": "evalw(e)=v ⇒ evalw(If(true,e,f))=v even if evalw(f) is undefined due to overflow.",
    "assumptions": [
      "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CompileTimeEvaluation-literal-range",
      "urn:csabs:axiom/CompileTimeEvaluation-selected-branch"
    ],
    "proofSketch": "Use the true-branch equation; no evaluation of f is requested. The rule does not permit syntactically or type-invalid unchosen branches."
  },
  {
    "id": "urn:csabs:law/CompileTimeEvaluation-overflow-is-not-wrapping",
    "type": "Law",
    "name": "overflow-is-not-wrapping",
    "statement": "evalw(e)=max(Rw) ∧ evalw(f)=1 ⇒ evalw(Add(e,f)) is undefined, not min(Rw).",
    "formalStatement": "evalw(e)=max(Rw) ∧ evalw(f)=1 ⇒ evalw(Add(e,f)) is undefined, not min(Rw).",
    "assumptions": [
      "C++20 N4861-inspired closed pure fragment. Fix a signed integer type of rank at least int and its implementation width w≥16; all arithmetic operands/results have that same type, avoiding mixed conversions/promotions. Literal leaves must be representable values of the chosen type; all branches must be structurally well-formed. Each evaluated addition/multiplication is checked in mathematical integers before range restriction; wrapping is not permitted. Only the selected conditional branch is evaluated. No pointers, allocation, mutable state, functions, recursion or full core-constant-expression classification is modeled. Compiler evaluation limits and required constant-expression contexts are additional obligations; constexpr alone does not force every invocation to occur at compile time. Mathematical partiality here is semantic invalidity for the selected fragment, not a classification of all compiler failures.",
      "All variables use the typed carriers and fixed environments declared in this entry."
    ],
    "appliesTo": [
      "urn:csabs:concept/CompileTimeEvaluation"
    ],
    "reviewStatus": "Editorial mathematical statement; no compiled theorem witness asserted.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cpp20-n4861-expr.const",
      "urn:csabs:source/cpp20-n4861-expr.cond",
      "urn:csabs:source/cpp20-n4861-basic.fundamental",
      "urn:csabs:source/cpp20-n4861-dcl.constexpr"
    ],
    "sourceLocator": "[expr.const] ¶5, implementation limits/undefined operations; [expr.cond] ¶1, selected operand; [basic.fundamental] ¶1–3; [dcl.constexpr]",
    "sourceNote": "Derived in the catalog from the explicitly linked premises in this selected profile; the consulted draft supplies the underlying language mechanisms, not an executable proof of this abstraction.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/CompileTimeEvaluation-literal-range",
      "urn:csabs:axiom/CompileTimeEvaluation-checked-arithmetic"
    ],
    "proofSketch": "The exact sum exceeds the maximum representable signed value, so the range premise for addition fails. No modulo rule applies to this signed profile."
  }
]
```
<!-- graph-record:end -->
