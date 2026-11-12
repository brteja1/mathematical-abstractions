# Partial function

A function defined on a specified subset of an ambient input set, with no value specified outside that subset.

**Notation:** f : D → B with D ⊆ A, written f : A ⇀ B.

**Stable ID:** `urn:csabs:concept/PartialFunction`

**Categories:** Set theory and foundations, Programming-language semantics

**Kind:** Function

**Prerequisites:** [Total function](Function.md), [Binary relation](Relation.md)

**Specializes:** [Binary relation](Relation.md)

## Backlinks

- [Single-inheritance class table and dynamic dispatch](ClassTable.md) — `requiresConcept`
- [Checked signed-integer constant-evaluation fragment](CompileTimeEvaluation.md) — `requiresConcept`
- [Total function](Function.md) — `relatedConcept`
- [Total function](Function.md) — `specializationOf`
- [Java type erasure and selected reifiability rules](JavaTypeErasure.md) — `requiresConcept`
- [Topological manifold (fixed dimension, without boundary)](Manifold.md) — `requiresConcept`
- [Map](Map.md) — `requiresConcept`
- [Map](Map.md) — `specializationOf`
- [Kinded partial template metafunction](TemplateMetafunction.md) — `requiresConcept`
- [Kinded partial template metafunction](TemplateMetafunction.md) — `specializationOf`
- [Deterministic one-tape Turing machine](TuringMachine.md) — `requiresConcept`

## Mathematical formulation

A⇀B is represented by A→Option(B). dom(f)={a | ∃b, f(a)=some(b)}. Composition returns none if either stage is undefined; otherwise (g∘f)(a)=some(c) when f(a)=some(b) and g(b)=some(c).

**Lean formulation** (in its source module context):

```lean
abbrev PartialFunction (A : Type u) (B : Type v) := A → Option B
```

**Source:** [`Catalog.PartialFunction`](../lean/Catalog/Foundations.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** A -> Option B; none means undefined, some b means the unique defined value; totalized representation of a partial map.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A function defined on a specified subset of an ambient input set, with no value specified outside that subset. Governing rules: Every input in the defined domain has exactly one output; inputs outside it have no specified output. A partial function is a single-valued relation whose defined domain is part of its meaning. Partial maps are equal exactly when their domains and values agree. A partial composition is defined only where both stages are defined.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use the graph R⊆A×B of the partial function, retaining ambient domain and codomain; single-valuedness is the additional constraint.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-partial-function-application"></a>

### partial application

`urn:csabs:operation/partial-function-application`

**signature:** f : A ⇀ B; apply_f : D → B, where D=dom(f)⊆A

**description:** Returns a value only for inputs in the defined domain D.

**precondition:** input ∈ D

**totality:** partial on ambient input carrier A

<a id="node-urn-csabs-operation-partial-function-composition"></a>

### partial composition

`urn:csabs:operation/partial-function-composition`

**signature:** (g∘f)(x)=g(f(x)) when x∈dom(f) and f(x)∈dom(g)

**description:** Composition is defined only when both component applications are defined.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-partial-functionality"></a>

### partial-functionality

`urn:csabs:axiom/partial-functionality`

**statement:** Every input in the defined domain has exactly one output; inputs outside it have no specified output.

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**formalStatement:** Every input in the defined domain has exactly one output; inputs outside it have no specified output.

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialFunction-graph"></a>

### graph

`urn:csabs:axiom/PartialFunction-graph`

**statement:** A partial function is a single-valued relation whose defined domain is part of its meaning.

**formalStatement:** R⊆A×B; (a,b)∈R ∧ (a,c)∈R ⇒ b=c; dom(R)={a∈A:∃b∈B:(a,b)∈R}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialFunction-extensionality"></a>

### extensionality

`urn:csabs:axiom/PartialFunction-extensionality`

**statement:** Partial maps are equal exactly when their domains and values agree.

**formalStatement:** f=g iff dom(f)=dom(g) ∧ ∀a∈dom(f):f(a)=g(a)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-PartialFunction-compose-domain"></a>

### compose-domain

`urn:csabs:axiom/PartialFunction-compose-domain`

**statement:** A partial composition is defined only where both stages are defined.

**formalStatement:** dom(g∘f)={a∈dom(f):f(a)∈dom(g)}; (g∘f)(a)=g(f(a)) on this domain

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-PartialFunction-composition-associativity"></a>

### composition-associativity

`urn:csabs:theorem/PartialFunction-composition-associativity`

**statement:** Partial composition is associative with equality of both defined domains and values.

**formalStatement:** h∘(g∘f)=(h∘g)∘f

**proofSketch:** Both sides are defined exactly when f(x), g(f(x)), and h(g(f(x))) are defined, and then agree.

**assumptions:** The explicit basis, carriers, and side conditions stated for PartialFunction apply.

**dependsOn:** [partial-functionality](PartialFunction.md#node-urn-csabs-axiom-partial-functionality); [graph](PartialFunction.md#node-urn-csabs-axiom-PartialFunction-graph); [extensionality](PartialFunction.md#node-urn-csabs-axiom-PartialFunction-extensionality); [compose-domain](PartialFunction.md#node-urn-csabs-axiom-PartialFunction-compose-domain)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PartialFunction",
    "type": "Concept",
    "shortForm": "PartialFunction",
    "fullName": "Partial function",
    "category": [
      "urn:csabs:category/foundations",
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "A function defined on a specified subset of an ambient input set, with no value specified outside that subset.",
    "notation": "f : D → B with D ⊆ A, written f : A ⇀ B.",
    "hasOperation": [
      "urn:csabs:operation/partial-function-application",
      "urn:csabs:operation/partial-function-composition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/partial-functionality",
      "urn:csabs:axiom/PartialFunction-graph",
      "urn:csabs:axiom/PartialFunction-extensionality",
      "urn:csabs:axiom/PartialFunction-compose-domain"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/PartialFunction-composition-associativity"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/Relation"
    ],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A function defined on a specified subset of an ambient input set, with no value specified outside that subset. Governing rules: Every input in the defined domain has exactly one output; inputs outside it have no specified output. A partial function is a single-valued relation whose defined domain is part of its meaning. Partial maps are equal exactly when their domains and values agree. A partial composition is defined only where both stages are defined.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Use the graph R⊆A×B of the partial function, retaining ambient domain and codomain; single-valuedness is the additional constraint.",
    "leanFormulation": "abbrev PartialFunction (A : Type u) (B : Type v) := A → Option B",
    "formulationSource": "urn:csabs:source/local-lean-Foundations",
    "formulationLocator": "Catalog.PartialFunction",
    "formulationScope": "model",
    "leanModelMapping": "A -> Option B; none means undefined, some b means the unique defined value; totalized representation of a partial map.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A⇀B is represented by A→Option(B). dom(f)={a | ∃b, f(a)=some(b)}. Composition returns none if either stage is undefined; otherwise (g∘f)(a)=some(c) when f(a)=some(b) and g(b)=some(c)."
  },
  {
    "id": "urn:csabs:operation/partial-function-application",
    "type": "Operation",
    "name": "partial application",
    "signature": "f : A ⇀ B; apply_f : D → B, where D=dom(f)⊆A",
    "description": "Returns a value only for inputs in the defined domain D.",
    "precondition": "input ∈ D",
    "totality": "partial on ambient input carrier A",
    "concept": "urn:csabs:concept/PartialFunction"
  },
  {
    "id": "urn:csabs:operation/partial-function-composition",
    "type": "Operation",
    "name": "partial composition",
    "signature": "(g∘f)(x)=g(f(x)) when x∈dom(f) and f(x)∈dom(g)",
    "description": "Composition is defined only when both component applications are defined.",
    "concept": "urn:csabs:concept/PartialFunction"
  },
  {
    "id": "urn:csabs:axiom/partial-functionality",
    "type": "Axiom",
    "statement": "Every input in the defined domain has exactly one output; inputs outside it have no specified output.",
    "appliesTo": [
      "urn:csabs:concept/PartialFunction"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "partial-functionality",
    "formalStatement": "Every input in the defined domain has exactly one output; inputs outside it have no specified output.",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/PartialFunction-graph",
    "type": "Axiom",
    "name": "graph",
    "statement": "A partial function is a single-valued relation whose defined domain is part of its meaning.",
    "formalStatement": "R⊆A×B; (a,b)∈R ∧ (a,c)∈R ⇒ b=c; dom(R)={a∈A:∃b∈B:(a,b)∈R}",
    "appliesTo": [
      "urn:csabs:concept/PartialFunction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/PartialFunction-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Partial maps are equal exactly when their domains and values agree.",
    "formalStatement": "f=g iff dom(f)=dom(g) ∧ ∀a∈dom(f):f(a)=g(a)",
    "appliesTo": [
      "urn:csabs:concept/PartialFunction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/PartialFunction-compose-domain",
    "type": "Axiom",
    "name": "compose-domain",
    "statement": "A partial composition is defined only where both stages are defined.",
    "formalStatement": "dom(g∘f)={a∈dom(f):f(a)∈dom(g)}; (g∘f)(a)=g(f(a)) on this domain",
    "appliesTo": [
      "urn:csabs:concept/PartialFunction"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/PartialFunction-composition-associativity",
    "type": "Theorem",
    "name": "composition-associativity",
    "statement": "Partial composition is associative with equality of both defined domains and values.",
    "formalStatement": "h∘(g∘f)=(h∘g)∘f",
    "proofSketch": "Both sides are defined exactly when f(x), g(f(x)), and h(g(f(x))) are defined, and then agree.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for PartialFunction apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/PartialFunction"
    ],
    "dependsOn": [
      "urn:csabs:axiom/partial-functionality",
      "urn:csabs:axiom/PartialFunction-graph",
      "urn:csabs:axiom/PartialFunction-extensionality",
      "urn:csabs:axiom/PartialFunction-compose-domain"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
