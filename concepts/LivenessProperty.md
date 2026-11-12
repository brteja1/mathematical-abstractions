# Liveness Property

A trace property for which every finite prefix has at least one infinite extension satisfying the property.

**Notation:** ∀finite u ∃infinite τ: uτ∈P

**Stable ID:** `urn:csabs:concept/LivenessProperty`

**Categories:** Concurrency and distributed systems → Correctness properties

**Kind:** principle

**Prerequisites:** [Transition System](TransitionSystem.md)

## Backlinks

- [Lamport bakery lock protocol](LamportBakery.md) — `relatedConcept`
- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `relatedConcept`
- [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md) — `relatedConcept`

## Mathematical formulation

For P⊆A^ℕ, Liveness(P) ⇔ ∀w∈A\*,∃α∈P,∀i<|w|,α(i)=w\_i. Every finite word has a satisfying infinite extension; no scheduler or fairness assumption is built into P.

**Lean formulation** (in its source module context):

```lean
def LivenessProperty {A : Type u} (P : (Nat → A) → Prop) : Prop :=
  ∀ word : List A, ∃ trace, extendsPrefix word trace ∧ P trace
```

**Source:** [`Catalog.LivenessProperty`](../lean/Catalog/Semantics.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Each finite List prefix admits a satisfying infinite trace; empty-alphabet cases stay explicit in types.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A trace property for which every finite prefix has at least one infinite extension satisfying the property. Governing rules: A liveness property allows some satisfying extension of every finite word over the stated alphabet.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-LivenessProperty-basis-extendible"></a>

### extendible

`urn:csabs:operation/LivenessProperty-basis-extendible`

**signature:** extendible : Σ*×𝒫(Σ^ω)→Prop

**description:** States that at least one satisfying infinite extension exists.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LivenessProperty-extendibility"></a>

### extendibility

`urn:csabs:axiom/LivenessProperty-extendibility`

**statement:** A liveness property allows some satisfying extension of every finite word over the stated alphabet.

**formalStatement:** P⊆Σ^ω; ∀u∈Σ*:∃τ∈Σ^ω:uτ∈P

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-LivenessProperty-core"></a>

### law/LivenessProperty-core

`urn:csabs:law/LivenessProperty-core`

**statement:** No finite prefix alone refutes a liveness property.

**formalStatement:** ∀u: u is extendible to P

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [extendibility](LivenessProperty.md#node-urn-csabs-axiom-LivenessProperty-extendibility)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-LivenessProperty-union-closed"></a>

### union-closed

`urn:csabs:theorem/LivenessProperty-union-closed`

**statement:** A nonempty union of liveness properties over one trace universe is liveness.

**formalStatement:** J≠∅ ∧ ∀j∈J:Live(Pⱼ) ⇒ Live(⋃ⱼPⱼ)

**proofSketch:** Choose one component; each finite prefix has a satisfying extension in that component and hence in the union.

**assumptions:** The explicit basis, carriers, and side conditions stated for LivenessProperty apply.

**dependsOn:** [extendibility](LivenessProperty.md#node-urn-csabs-axiom-LivenessProperty-extendibility)

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
    "id": "urn:csabs:concept/LivenessProperty",
    "type": "Concept",
    "shortForm": "LivenessProperty",
    "fullName": "Liveness Property",
    "category": [
      "urn:csabs:category/concurrency-properties"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "A trace property for which every finite prefix has at least one infinite extension satisfying the property.",
    "notation": "∀finite u ∃infinite τ: uτ∈P",
    "hasOperation": [
      "urn:csabs:operation/LivenessProperty-basis-extendible"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LivenessProperty-extendibility"
    ],
    "hasLaw": [
      "urn:csabs:law/LivenessProperty-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LivenessProperty-union-closed"
    ],
    "requiresConcept": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A trace property for which every finite prefix has at least one infinite extension satisfying the property. Governing rules: A liveness property allows some satisfying extension of every finite word over the stated alphabet.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "def LivenessProperty {A : Type u} (P : (Nat → A) → Prop) : Prop :=\n  ∀ word : List A, ∃ trace, extendsPrefix word trace ∧ P trace",
    "formulationSource": "urn:csabs:source/local-lean-Semantics",
    "formulationLocator": "Catalog.LivenessProperty",
    "formulationScope": "model",
    "leanModelMapping": "Each finite List prefix admits a satisfying infinite trace; empty-alphabet cases stay explicit in types.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For P⊆A^ℕ, Liveness(P) ⇔ ∀w∈A*,∃α∈P,∀i<|w|,α(i)=w_i. Every finite word has a satisfying infinite extension; no scheduler or fairness assumption is built into P."
  },
  {
    "id": "urn:csabs:operation/LivenessProperty-basis-extendible",
    "type": "Operation",
    "name": "extendible",
    "signature": "extendible : Σ*×𝒫(Σ^ω)→Prop",
    "description": "States that at least one satisfying infinite extension exists.",
    "concept": "urn:csabs:concept/LivenessProperty"
  },
  {
    "id": "urn:csabs:axiom/LivenessProperty-extendibility",
    "type": "Axiom",
    "name": "extendibility",
    "statement": "A liveness property allows some satisfying extension of every finite word over the stated alphabet.",
    "formalStatement": "P⊆Σ^ω; ∀u∈Σ*:∃τ∈Σ^ω:uτ∈P",
    "appliesTo": [
      "urn:csabs:concept/LivenessProperty"
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
    "id": "urn:csabs:law/LivenessProperty-core",
    "type": "Law",
    "statement": "No finite prefix alone refutes a liveness property.",
    "formalStatement": "∀u: u is extendible to P",
    "appliesTo": [
      "urn:csabs:concept/LivenessProperty"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/LivenessProperty-extendibility"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/LivenessProperty-union-closed",
    "type": "Theorem",
    "name": "union-closed",
    "statement": "A nonempty union of liveness properties over one trace universe is liveness.",
    "formalStatement": "J≠∅ ∧ ∀j∈J:Live(Pⱼ) ⇒ Live(⋃ⱼPⱼ)",
    "proofSketch": "Choose one component; each finite prefix has a satisfying extension in that component and hence in the union.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for LivenessProperty apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/LivenessProperty"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LivenessProperty-extendibility"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
