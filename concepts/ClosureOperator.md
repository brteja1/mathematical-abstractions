# Closure Operator

An extensive, monotone, idempotent self-map on a partially ordered set.

**Notation:** c:L→L; x≤c(x); x≤y⇒c(x)≤c(y); c(c(x))=c(x)

**Stable ID:** `urn:csabs:concept/ClosureOperator`

**Categories:** Order and fixed points

**Kind:** Function

**Prerequisites:** [Partial Order](PartialOrder.md)

**Specializes:** [Monotone Function](MonotoneFunction.md)

## Backlinks

- [Functional dependency on a relational schema](FunctionalDependency.md) — `relatedConcept`
- [Topological space (topology on a carrier)](TopologicalSpace.md) — `relatedConcept`

## Mathematical formulation

For a partial order A, c:A→A is a closure operator iff (∀x,x≤c(x)), (∀x,y,x≤y⇒c(x)≤c(y)), and (∀x,c(c(x))=c(x)).

**Lean formulation** (in its source module context):

```lean
abbrev ClosureOperator (A : Type u) [_root_.PartialOrder A] := _root_.ClosureOperator A
```

**Source:** [`Catalog.ClosureOperator`](../lean/Catalog/Order.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib ClosureOperator on an explicitly supplied PartialOrder.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: An extensive, monotone, idempotent self-map on a partially ordered set. Governing rules: Closure lies above its input. Closure preserves the partial order. Applying closure twice equals applying it once.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use the same poset for domain and codomain and the same map; extensivity and idempotence are additional constraints.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-ClosureOperator-closure"></a>

### closure

`urn:csabs:operation/ClosureOperator-closure`

**signature:** c : L→L

**description:** Returns the closed approximation of its argument.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ClosureOperator-extensive"></a>

### extensive

`urn:csabs:axiom/ClosureOperator-extensive`

**statement:** Closure lies above its input.

**formalStatement:** x≤c(x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-ClosureOperator-monotone"></a>

### monotone

`urn:csabs:axiom/ClosureOperator-monotone`

**statement:** Closure preserves the partial order.

**formalStatement:** x≤y ⇒ c(x)≤c(y)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-ClosureOperator-idempotent"></a>

### idempotent

`urn:csabs:axiom/ClosureOperator-idempotent`

**statement:** Applying closure twice equals applying it once.

**formalStatement:** c(c(x))=c(x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-ClosureOperator-core"></a>

### law/ClosureOperator-core

`urn:csabs:law/ClosureOperator-core`

**statement:** Every output is a fixed point.

**formalStatement:** ∀x: c(x)∈Fix(c)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**proofSketch:** Idempotence c(c(x))=c(x) directly states that c(x) is fixed.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [extensive](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-extensive); [monotone](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-monotone); [idempotent](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-idempotent)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-ClosureOperator-least-closed-upper-bound"></a>

### least-closed-upper-bound

`urn:csabs:theorem/ClosureOperator-least-closed-upper-bound`

**statement:** Closure is the least closed element above its argument.

**formalStatement:** x≤y ∧ c(y)=y ⇒ c(x)≤y

**proofSketch:** Monotonicity gives c(x)≤c(y); replace c(y) with y.

**assumptions:** The explicit basis, carriers, and side conditions stated for ClosureOperator apply.

**dependsOn:** [extensive](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-extensive); [monotone](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-monotone); [idempotent](ClosureOperator.md#node-urn-csabs-axiom-ClosureOperator-idempotent)

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
    "id": "urn:csabs:concept/ClosureOperator",
    "type": "Concept",
    "shortForm": "ClosureOperator",
    "fullName": "Closure Operator",
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "An extensive, monotone, idempotent self-map on a partially ordered set.",
    "notation": "c:L→L; x≤c(x); x≤y⇒c(x)≤c(y); c(c(x))=c(x)",
    "hasOperation": [
      "urn:csabs:operation/ClosureOperator-closure"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ClosureOperator-extensive",
      "urn:csabs:axiom/ClosureOperator-monotone",
      "urn:csabs:axiom/ClosureOperator-idempotent"
    ],
    "hasLaw": [
      "urn:csabs:law/ClosureOperator-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ClosureOperator-least-closed-upper-bound"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PartialOrder"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: An extensive, monotone, idempotent self-map on a partially ordered set. Governing rules: Closure lies above its input. Closure preserves the partial order. Applying closure twice equals applying it once.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/MonotoneFunction"
    ],
    "specializationNote": "Use the same poset for domain and codomain and the same map; extensivity and idempotence are additional constraints.",
    "leanFormulation": "abbrev ClosureOperator (A : Type u) [_root_.PartialOrder A] := _root_.ClosureOperator A",
    "formulationSource": "urn:csabs:source/local-lean-Order",
    "formulationLocator": "Catalog.ClosureOperator",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib ClosureOperator on an explicitly supplied PartialOrder.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For a partial order A, c:A→A is a closure operator iff (∀x,x≤c(x)), (∀x,y,x≤y⇒c(x)≤c(y)), and (∀x,c(c(x))=c(x))."
  },
  {
    "id": "urn:csabs:operation/ClosureOperator-closure",
    "type": "Operation",
    "name": "closure",
    "signature": "c : L→L",
    "description": "Returns the closed approximation of its argument.",
    "concept": "urn:csabs:concept/ClosureOperator"
  },
  {
    "id": "urn:csabs:axiom/ClosureOperator-extensive",
    "type": "Axiom",
    "name": "extensive",
    "statement": "Closure lies above its input.",
    "formalStatement": "x≤c(x)",
    "appliesTo": [
      "urn:csabs:concept/ClosureOperator"
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
    "id": "urn:csabs:axiom/ClosureOperator-monotone",
    "type": "Axiom",
    "name": "monotone",
    "statement": "Closure preserves the partial order.",
    "formalStatement": "x≤y ⇒ c(x)≤c(y)",
    "appliesTo": [
      "urn:csabs:concept/ClosureOperator"
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
    "id": "urn:csabs:axiom/ClosureOperator-idempotent",
    "type": "Axiom",
    "name": "idempotent",
    "statement": "Applying closure twice equals applying it once.",
    "formalStatement": "c(c(x))=c(x)",
    "appliesTo": [
      "urn:csabs:concept/ClosureOperator"
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
    "id": "urn:csabs:law/ClosureOperator-core",
    "type": "Law",
    "statement": "Every output is a fixed point.",
    "formalStatement": "∀x: c(x)∈Fix(c)",
    "appliesTo": [
      "urn:csabs:concept/ClosureOperator"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "proofSketch": "Idempotence c(c(x))=c(x) directly states that c(x) is fixed.",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/ClosureOperator-extensive",
      "urn:csabs:axiom/ClosureOperator-monotone",
      "urn:csabs:axiom/ClosureOperator-idempotent"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/ClosureOperator-least-closed-upper-bound",
    "type": "Theorem",
    "name": "least-closed-upper-bound",
    "statement": "Closure is the least closed element above its argument.",
    "formalStatement": "x≤y ∧ c(y)=y ⇒ c(x)≤y",
    "proofSketch": "Monotonicity gives c(x)≤c(y); replace c(y) with y.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for ClosureOperator apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/ClosureOperator"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ClosureOperator-extensive",
      "urn:csabs:axiom/ClosureOperator-monotone",
      "urn:csabs:axiom/ClosureOperator-idempotent"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
