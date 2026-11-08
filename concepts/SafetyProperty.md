# Safety Property

A property of infinite executions for which every violating trace has a finite prefix with no satisfying extension.

**Notation:** σ∉P ⇒ ∃finite prefix u of σ: ∀τ, uτ∉P

**Stable ID:** `urn:csabs:concept/SafetyProperty`

**Categories:** Concurrency and distributed systems → Correctness properties

**Kind:** principle

**Prerequisites:** [Transition System](TransitionSystem.md)

## Backlinks

- [Lamport bakery lock protocol](LamportBakery.md) — `relatedConcept`
- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `relatedConcept`
- [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A property of infinite executions for which every violating trace has a finite prefix with no satisfying extension. Governing rules: A safety property is defined relative to a stated trace alphabet by finite witnesses of every violation.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate carrier, equality, and stated semantic conventions before using this entry.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-SafetyProperty-basis-badPrefix"></a>

### badPrefix

`urn:csabs:operation/SafetyProperty-basis-badPrefix`

**signature:** badPrefix : Σ*×𝒫(Σ^ω)→Prop

**description:** States that the finite prefix has no satisfying infinite extension.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SafetyProperty-bad-prefix"></a>

### bad-prefix

`urn:csabs:axiom/SafetyProperty-bad-prefix`

**statement:** A safety property is defined relative to a stated trace alphabet by finite witnesses of every violation.

**formalStatement:** P⊆Σ^ω; σ∉P ⇒ ∃u prefix of σ:∀τ∈Σ^ω:uτ∉P

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-SafetyProperty-core"></a>

### law/SafetyProperty-core

`urn:csabs:law/SafetyProperty-core`

**statement:** Violations have finite bad-prefix witnesses.

**formalStatement:** Every σ∉P has a bad prefix

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [bad-prefix](SafetyProperty.md#node-urn-csabs-axiom-SafetyProperty-bad-prefix)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-SafetyProperty-intersection-closed"></a>

### intersection-closed

`urn:csabs:theorem/SafetyProperty-intersection-closed`

**statement:** An arbitrary intersection of safety properties over the same trace universe is safety.

**formalStatement:** ∀i:Safe(Pᵢ) ⇒ Safe(⋂ᵢPᵢ)

**proofSketch:** A trace outside the intersection violates one component; that component's bad prefix also refutes the intersection.

**assumptions:** The explicit basis, carriers, and side conditions stated for SafetyProperty apply.

**dependsOn:** [bad-prefix](SafetyProperty.md#node-urn-csabs-axiom-SafetyProperty-bad-prefix)

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
    "id": "urn:csabs:concept/SafetyProperty",
    "type": "Concept",
    "shortForm": "SafetyProperty",
    "fullName": "Safety Property",
    "category": [
      "urn:csabs:category/concurrency-properties"
    ],
    "kind": "urn:csabs:kind/principle",
    "definition": "A property of infinite executions for which every violating trace has a finite prefix with no satisfying extension.",
    "notation": "σ∉P ⇒ ∃finite prefix u of σ: ∀τ, uτ∉P",
    "hasOperation": [
      "urn:csabs:operation/SafetyProperty-basis-badPrefix"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SafetyProperty-bad-prefix"
    ],
    "hasLaw": [
      "urn:csabs:law/SafetyProperty-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SafetyProperty-intersection-closed"
    ],
    "requiresConcept": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate carrier, equality, and stated semantic conventions before using this entry.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A property of infinite executions for which every violating trace has a finite prefix with no satisfying extension. Governing rules: A safety property is defined relative to a stated trace alphabet by finite witnesses of every violation.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:operation/SafetyProperty-basis-badPrefix",
    "type": "Operation",
    "name": "badPrefix",
    "signature": "badPrefix : Σ*×𝒫(Σ^ω)→Prop",
    "description": "States that the finite prefix has no satisfying infinite extension.",
    "concept": "urn:csabs:concept/SafetyProperty"
  },
  {
    "id": "urn:csabs:axiom/SafetyProperty-bad-prefix",
    "type": "Axiom",
    "name": "bad-prefix",
    "statement": "A safety property is defined relative to a stated trace alphabet by finite witnesses of every violation.",
    "formalStatement": "P⊆Σ^ω; σ∉P ⇒ ∃u prefix of σ:∀τ∈Σ^ω:uτ∉P",
    "appliesTo": [
      "urn:csabs:concept/SafetyProperty"
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
    "id": "urn:csabs:law/SafetyProperty-core",
    "type": "Law",
    "statement": "Violations have finite bad-prefix witnesses.",
    "formalStatement": "Every σ∉P has a bad prefix",
    "appliesTo": [
      "urn:csabs:concept/SafetyProperty"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/SafetyProperty-bad-prefix"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/SafetyProperty-intersection-closed",
    "type": "Theorem",
    "name": "intersection-closed",
    "statement": "An arbitrary intersection of safety properties over the same trace universe is safety.",
    "formalStatement": "∀i:Safe(Pᵢ) ⇒ Safe(⋂ᵢPᵢ)",
    "proofSketch": "A trace outside the intersection violates one component; that component's bad prefix also refutes the intersection.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for SafetyProperty apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/SafetyProperty"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SafetyProperty-bad-prefix"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
