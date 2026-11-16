# Sound abstract transfer and inductive dataflow facts

A concrete-to-abstract analysis interface whose abstract transfer overapproximates concrete successors; an inductive abstract state can justify a transformation guard.

**Notation:** post(γ(a))⊆γ(F♯(a)); Init⊆γ(a*) ∧ F♯(a*)⊑a*

**Stable ID:** `urn:csabs:concept/AbstractInterpretation`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Set](Set.md), [Join semilattice](JoinSemilattice.md), [Monotone Function](MonotoneFunction.md)

**Related concepts:** [Complete Lattice](CompleteLattice.md), [Fixed Point](FixedPoint.md), [Analysis validity across IR mutation](AnalysisPreservation.md)

## Backlinks

- [Conservative alias and Mod/Ref query contract](AliasAnalysis.md) — `requiresConcept`
- [Analysis validity across IR mutation](AnalysisPreservation.md) — `relatedConcept`
- [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md) — `relatedConcept`
- [Scoped induction recurrence and trip-count facts](ScalarRecurrence.md) — `relatedConcept`

## Mathematical formulation

A concrete-to-abstract analysis interface whose abstract transfer overapproximates concrete successors; an inductive abstract state can justify a transformation guard. post(γ(a))⊆γ(F♯(a)); Init⊆γ(a\*) ∧ F♯(a\*)⊑a\* C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.

**Lean formulation** (in its source module context):

```lean
structure AbstractInterpretation (C A : Type u) where
  gamma : A → Set C
  step : C → C → Prop
  transfer : A → A
  sound : ∀ a c d, c ∈ gamma a → step c d → d ∈ gamma (transfer a)
```

**Source:** [`Catalog.Transforms.AbstractInterpretation`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Concretization, concrete step and abstract transfer with a one-step soundness field.

**Limits:** Partial sound-transfer interface: no abstract order, join, fixpoint solver, widening or reachability induction implementation. Does not certify an LLVM/MLIR analysis implementation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀a, post(γ(a))⊆γ(F♯(a)).; Reachable is the least subset of C containing Init and closed under the concrete successor relation.

**basisKind:** relational-structural-definition

**basisScope:** C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Partial sound-transfer interface: no abstract order, join, fixpoint solver, widening or reachability induction implementation. Does not certify an LLVM/MLIR analysis implementation.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-AbstractInterpretation-transfer"></a>

### transfer

`urn:csabs:operation/AbstractInterpretation-transfer`

**signature:** transfer : A→A

**description:** Overapproximate successors of every represented concrete state.

**precondition:** Sound abstraction of the selected concrete step.

**postcondition:** Overapproximate successors of every represented concrete state.

**totality:** Total mathematical transfer.

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AbstractInterpretation-concretize"></a>

### concretize

`urn:csabs:operation/AbstractInterpretation-concretize`

**signature:** γ : A→P(C)

**description:** Interpret abstract facts as sets of possible states.

**precondition:** Carrier and order direction fixed.

**postcondition:** Interpret abstract facts as sets of possible states.

**totality:** Total function.

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-AbstractInterpretation-join"></a>

### join

`urn:csabs:operation/AbstractInterpretation-join`

**signature:** join : A×A→A

**description:** Compute an abstract upper bound encompassing both concretizations.

**precondition:** Chosen semilattice laws and monotone γ.

**postcondition:** Compute an abstract upper bound encompassing both concretizations.

**totality:** Total operation.

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-AbstractInterpretation-transfer-soundness"></a>

### transfer-soundness

`urn:csabs:axiom/AbstractInterpretation-transfer-soundness`

**description:** Defining obligation for Sound abstract transfer and inductive dataflow facts

**statement:** ∀a, post(γ(a))⊆γ(F♯(a)).

**formalStatement:** ∀a, post(γ(a))⊆γ(F♯(a)).

**assumptions:** C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-AbstractInterpretation-inductive-definition"></a>

### inductive-definition

`urn:csabs:axiom/AbstractInterpretation-inductive-definition`

**description:** Defining obligation for Sound abstract transfer and inductive dataflow facts

**statement:** Reachable is the least subset of C containing Init and closed under the concrete successor relation.

**formalStatement:** Reachable is the least subset of C containing Init and closed under the concrete successor relation.

**assumptions:** C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-AbstractInterpretation-abstract-postfixpoint-invariant"></a>

### abstract-postfixpoint-invariant

`urn:csabs:law/AbstractInterpretation-abstract-postfixpoint-invariant`

**description:** Derived consequence within the selected semantic profile.

**statement:** If γ is monotone, F♯(a*)⊑a*, Init⊆γ(a*) and transfer is sound, then Reachable⊆γ(a*).

**formalStatement:** If γ is monotone, F♯(a*)⊑a*, Init⊆γ(a*) and transfer is sound, then Reachable⊆γ(a*).

**assumptions:** C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.

**dependsOn:** [transfer-soundness](AbstractInterpretation.md#node-urn-csabs-axiom-AbstractInterpretation-transfer-soundness); [inductive-definition](AbstractInterpretation.md#node-urn-csabs-axiom-AbstractInterpretation-inductive-definition)

**proofSketch:** Sound transfer and monotonicity give post(γ(a*))⊆γ(F♯(a*))⊆γ(a*). Induct on finite concrete reachability from Init; the base is initialization and the step uses closure.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Data Flow Analysis tutorial (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/Tutorials/DataFlowAnalysis.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/AbstractInterpretation",
    "type": "Concept",
    "shortForm": "AbstractInterpretation",
    "fullName": "Sound abstract transfer and inductive dataflow facts",
    "definition": "A concrete-to-abstract analysis interface whose abstract transfer overapproximates concrete successors; an inductive abstract state can justify a transformation guard.",
    "notation": "post(γ(a))⊆γ(F♯(a)); Init⊆γ(a*) ∧ F♯(a*)⊑a*",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/JoinSemilattice",
      "urn:csabs:concept/MonotoneFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/CompleteLattice",
      "urn:csabs:concept/FixedPoint",
      "urn:csabs:concept/AnalysisPreservation"
    ],
    "hasOperation": [
      "urn:csabs:operation/AbstractInterpretation-transfer",
      "urn:csabs:operation/AbstractInterpretation-concretize",
      "urn:csabs:operation/AbstractInterpretation-join"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/AbstractInterpretation-transfer-soundness",
      "urn:csabs:axiom/AbstractInterpretation-inductive-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/AbstractInterpretation-abstract-postfixpoint-invariant"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.",
    "axiomBasis": "∀a, post(γ(a))⊆γ(F♯(a)).; Reachable is the least subset of C containing Init and closed under the concrete successor relation.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Partial sound-transfer interface: no abstract order, join, fixpoint solver, widening or reachability induction implementation. Does not certify an LLVM/MLIR analysis implementation."
    ],
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A concrete-to-abstract analysis interface whose abstract transfer overapproximates concrete successors; an inductive abstract state can justify a transformation guard. post(γ(a))⊆γ(F♯(a)); Init⊆γ(a*) ∧ F♯(a*)⊑a* C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite.",
    "leanFormulation": "structure AbstractInterpretation (C A : Type u) where\n  gamma : A → Set C\n  step : C → C → Prop\n  transfer : A → A\n  sound : ∀ a c d, c ∈ gamma a → step c d → d ∈ gamma (transfer a)",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.AbstractInterpretation",
    "formulationScope": "partial",
    "leanModelMapping": "Concretization, concrete step and abstract transfer with a one-step soundness field.",
    "leanModelLimitations": "Partial sound-transfer interface: no abstract order, join, fixpoint solver, widening or reachability induction implementation. Does not certify an LLVM/MLIR analysis implementation."
  },
  {
    "id": "urn:csabs:operation/AbstractInterpretation-transfer",
    "type": "Operation",
    "name": "transfer",
    "signature": "transfer : A→A",
    "description": "Overapproximate successors of every represented concrete state.",
    "concept": "urn:csabs:concept/AbstractInterpretation",
    "precondition": "Sound abstraction of the selected concrete step.",
    "postcondition": "Overapproximate successors of every represented concrete state.",
    "totality": "Total mathematical transfer.",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AbstractInterpretation-concretize",
    "type": "Operation",
    "name": "concretize",
    "signature": "γ : A→P(C)",
    "description": "Interpret abstract facts as sets of possible states.",
    "concept": "urn:csabs:concept/AbstractInterpretation",
    "precondition": "Carrier and order direction fixed.",
    "postcondition": "Interpret abstract facts as sets of possible states.",
    "totality": "Total function.",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/AbstractInterpretation-join",
    "type": "Operation",
    "name": "join",
    "signature": "join : A×A→A",
    "description": "Compute an abstract upper bound encompassing both concretizations.",
    "concept": "urn:csabs:concept/AbstractInterpretation",
    "precondition": "Chosen semilattice laws and monotone γ.",
    "postcondition": "Compute an abstract upper bound encompassing both concretizations.",
    "totality": "Total operation.",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/AbstractInterpretation-transfer-soundness",
    "type": "Axiom",
    "name": "transfer-soundness",
    "description": "Defining obligation for Sound abstract transfer and inductive dataflow facts",
    "statement": "∀a, post(γ(a))⊆γ(F♯(a)).",
    "formalStatement": "∀a, post(γ(a))⊆γ(F♯(a)).",
    "assumptions": [
      "C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite."
    ],
    "appliesTo": [
      "urn:csabs:concept/AbstractInterpretation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/AbstractInterpretation-inductive-definition",
    "type": "Axiom",
    "name": "inductive-definition",
    "description": "Defining obligation for Sound abstract transfer and inductive dataflow facts",
    "statement": "Reachable is the least subset of C containing Init and closed under the concrete successor relation.",
    "formalStatement": "Reachable is the least subset of C containing Init and closed under the concrete successor relation.",
    "assumptions": [
      "C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite."
    ],
    "appliesTo": [
      "urn:csabs:concept/AbstractInterpretation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/AbstractInterpretation-abstract-postfixpoint-invariant",
    "type": "Law",
    "name": "abstract-postfixpoint-invariant",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "If γ is monotone, F♯(a*)⊑a*, Init⊆γ(a*) and transfer is sound, then Reachable⊆γ(a*).",
    "formalStatement": "If γ is monotone, F♯(a*)⊑a*, Init⊆γ(a*) and transfer is sound, then Reachable⊆γ(a*).",
    "assumptions": [
      "C is a concrete state carrier, A an abstract ordered carrier, γ:A→P(C) monotone and F♯ sound. Bottom represents impossible/uninitialized only after its semantic interpretation is established; framework uninitialized solver state is not automatically semantic unreachability. Top permits all states. Join overapproximates union. Finite-height/ascending-chain assumptions or a justified widening are required for termination; monotonicity alone does not imply finite convergence. A sound analysis may be imprecise and refuse a valid rewrite."
    ],
    "appliesTo": [
      "urn:csabs:concept/AbstractInterpretation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/AbstractInterpretation-transfer-soundness",
      "urn:csabs:axiom/AbstractInterpretation-inductive-definition"
    ],
    "proofSketch": "Sound transfer and monotonicity give post(γ(a*))⊆γ(F♯(a*))⊆γ(a*). Induct on finite concrete reachability from Init; the base is initialization and the step uses closure.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-dataflow"
    ],
    "sourceLocator": "Data Flow Analysis tutorial: Forward Dataflow Analysis, Lattices, ForwardDataflowAnalysis Driver",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
