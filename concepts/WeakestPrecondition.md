# Weakest Precondition

For a command and postcondition, the weakest predicate ensuring termination and the postcondition for every allowed execution.

**Notation:** wp(C,Q)(s): all executions of C from s terminate and satisfy Q

**Stable ID:** `urn:csabs:concept/WeakestPrecondition`

**Categories:** Programming-language semantics

**Kind:** Function

**Prerequisites:** [Hoare Triple](HoareTriple.md)

## Mathematical formulation

For a supplied total-command interface C and postcondition Q, wp(C,Q)(s) ⇔ allTerminateNormally\_C(s) ∧ ∀t,normal\_C(s,t)⇒Q(t). The interface also requires allTerminateNormally\_C(s)⇒∃t,normal\_C(s,t); correspondence to actual executions is an instantiation obligation.

**Lean formulation** (in its source module context):

```lean
def WeakestPrecondition {S : Type u} (C : TotalCommand S) (Q : S → Prop) (s : S) : Prop :=
  C.allTerminateNormally s ∧ ∀ t, C.normal s t → Q t
```

**Source:** [`Catalog.WeakestPrecondition`](../lean/Catalog/Semantics.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** All-normal-termination predicate plus universal postcondition over normal outcomes; execution/scheduler semantics must substantiate the supplied predicate.

**Limits:** Operational all-executions termination/no-fault semantics is supplied by clients, not derived from a concrete command language.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: For a command and postcondition, the weakest predicate ensuring termination and the postcondition for every allowed execution. Governing rules: The weakest precondition requires termination without faults and Q for every execution, not just the terminating ones.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Total correctness requires termination of all nondeterministic executions; specify scheduler assumptions.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-WeakestPrecondition-wp"></a>

### wp

`urn:csabs:operation/WeakestPrecondition-wp`

**signature:** wp : Command×Predicate→Predicate

**description:** Computes the total-correctness precondition, including termination of every allowed execution.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-WeakestPrecondition-total-correctness"></a>

### total-correctness

`urn:csabs:axiom/WeakestPrecondition-total-correctness`

**statement:** The weakest precondition requires termination without faults and Q for every execution, not just the terminating ones.

**formalStatement:** wp(C,Q)(s) iff AllExecutionsTerminateNormally(C,s) ∧ ∀t:Exec_C(s,t)⇒Q(t)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-WeakestPrecondition-core"></a>

### law/WeakestPrecondition-core

`urn:csabs:law/WeakestPrecondition-core`

**statement:** Weakest preconditions compose in reverse command order.

**formalStatement:** wp(C;D,Q)=wp(C,wp(D,Q))

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [total-correctness](WeakestPrecondition.md#node-urn-csabs-axiom-WeakestPrecondition-total-correctness)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-WeakestPrecondition-post-monotonicity"></a>

### post-monotonicity

`urn:csabs:theorem/WeakestPrecondition-post-monotonicity`

**statement:** Weakest preconditions are monotone in their postcondition.

**formalStatement:** Q⇒R ⇒ wp(C,Q)⇒wp(C,R)

**proofSketch:** Termination is unchanged and each final Q-state also satisfies R.

**assumptions:** The explicit basis, carriers, and side conditions stated for WeakestPrecondition apply.

**dependsOn:** [total-correctness](WeakestPrecondition.md#node-urn-csabs-axiom-WeakestPrecondition-total-correctness)

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
    "id": "urn:csabs:concept/WeakestPrecondition",
    "type": "Concept",
    "shortForm": "WeakestPrecondition",
    "fullName": "Weakest Precondition",
    "category": [
      "urn:csabs:category/programming-semantics"
    ],
    "kind": "urn:csabs:kind/function",
    "definition": "For a command and postcondition, the weakest predicate ensuring termination and the postcondition for every allowed execution.",
    "notation": "wp(C,Q)(s): all executions of C from s terminate and satisfy Q",
    "hasOperation": [
      "urn:csabs:operation/WeakestPrecondition-wp"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/WeakestPrecondition-total-correctness"
    ],
    "hasLaw": [
      "urn:csabs:law/WeakestPrecondition-core"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/WeakestPrecondition-post-monotonicity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/HoareTriple"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Total correctness requires termination of all nondeterministic executions; specify scheduler assumptions.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: For a command and postcondition, the weakest predicate ensuring termination and the postcondition for every allowed execution. Governing rules: The weakest precondition requires termination without faults and Q for every execution, not just the terminating ones.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "def WeakestPrecondition {S : Type u} (C : TotalCommand S) (Q : S → Prop) (s : S) : Prop :=\n  C.allTerminateNormally s ∧ ∀ t, C.normal s t → Q t",
    "formulationSource": "urn:csabs:source/local-lean-Semantics",
    "formulationLocator": "Catalog.WeakestPrecondition",
    "formulationScope": "partial",
    "leanModelMapping": "All-normal-termination predicate plus universal postcondition over normal outcomes; execution/scheduler semantics must substantiate the supplied predicate.",
    "leanModelLimitations": "Operational all-executions termination/no-fault semantics is supplied by clients, not derived from a concrete command language.",
    "mathematicalFormulation": "For a supplied total-command interface C and postcondition Q, wp(C,Q)(s) ⇔ allTerminateNormally_C(s) ∧ ∀t,normal_C(s,t)⇒Q(t). The interface also requires allTerminateNormally_C(s)⇒∃t,normal_C(s,t); correspondence to actual executions is an instantiation obligation."
  },
  {
    "id": "urn:csabs:operation/WeakestPrecondition-wp",
    "type": "Operation",
    "name": "wp",
    "signature": "wp : Command×Predicate→Predicate",
    "description": "Computes the total-correctness precondition, including termination of every allowed execution.",
    "concept": "urn:csabs:concept/WeakestPrecondition"
  },
  {
    "id": "urn:csabs:axiom/WeakestPrecondition-total-correctness",
    "type": "Axiom",
    "name": "total-correctness",
    "statement": "The weakest precondition requires termination without faults and Q for every execution, not just the terminating ones.",
    "formalStatement": "wp(C,Q)(s) iff AllExecutionsTerminateNormally(C,s) ∧ ∀t:Exec_C(s,t)⇒Q(t)",
    "appliesTo": [
      "urn:csabs:concept/WeakestPrecondition"
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
    "id": "urn:csabs:law/WeakestPrecondition-core",
    "type": "Law",
    "statement": "Weakest preconditions compose in reverse command order.",
    "formalStatement": "wp(C;D,Q)=wp(C,wp(D,Q))",
    "appliesTo": [
      "urn:csabs:concept/WeakestPrecondition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/WeakestPrecondition-total-correctness"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/WeakestPrecondition-post-monotonicity",
    "type": "Theorem",
    "name": "post-monotonicity",
    "statement": "Weakest preconditions are monotone in their postcondition.",
    "formalStatement": "Q⇒R ⇒ wp(C,Q)⇒wp(C,R)",
    "proofSketch": "Termination is unchanged and each final Q-state also satisfies R.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for WeakestPrecondition apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/WeakestPrecondition"
    ],
    "dependsOn": [
      "urn:csabs:axiom/WeakestPrecondition-total-correctness"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
