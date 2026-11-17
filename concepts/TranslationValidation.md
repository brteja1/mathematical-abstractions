# Per-instance transformation validation

An instance checker for a concrete source/target pair against a stated refinement obligation, retaining semantic scope, bounds and distinct proved, counterexample and unknown outcomes.

**Notation:** check(s,t)∈{proved,counterexample,unknown}; proved⇒Obligation(s,t)

**Stable ID:** `urn:csabs:concept/TranslationValidation`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md)

**Related concepts:** [Typed IR legalization with representation relation](DialectConversion.md), [Guarded contextual program rewrite](GuardedRewrite.md)

## Mathematical formulation

An instance checker for a concrete source/target pair against a stated refinement obligation, retaining semantic scope, bounds and distinct proved, counterexample and unknown outcomes. check(s,t)∈{proved,counterexample,unknown}; proved⇒Obligation(s,t) The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.

**Lean formulation** (in its source module context):

```lean
structure TranslationValidation (P : Type u) where
  obligation : P → P → Prop
  check : P → P → ValidationVerdict
  acceptedSound : ∀ s t, check s t = .proved → obligation s t
```

**Source:** [`Catalog.Transforms.TranslationValidation`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Three-way verdict and acceptedSound law for a supplied obligation; bounds are part of that obligation.

**Limits:** No SMT encoder, solver integration or validation of a concrete pass. Counterexample replay and scope metadata are external. A supplied soundness hypothesis is not proof that Alive2 implements this interface.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** check(s,t,scope)=proved ⇒ Obligation(scope,s,t).; A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.

**basisKind:** relational-structural-definition

**basisScope:** The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No SMT encoder, solver integration or validation of a concrete pass. Counterexample replay and scope metadata are external. A supplied soundness hypothesis is not proof that Alive2 implements this interface.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TranslationValidation-validate"></a>

### validate

`urn:csabs:operation/TranslationValidation-validate`

**signature:** validate : Program×Program×Scope→Verdict

**description:** Check a fixed pair; return evidence scoped to the actual encoded obligation.

**precondition:** Well-formed inputs and supported semantic subset.

**postcondition:** Check a fixed pair; return evidence scoped to the actual encoded obligation.

**totality:** Total reporting protocol; solver timeout maps to unknown.

**source:** [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation; [Lopes et al., Alive2: Bounded Translation Validation for LLVM (author abstract)](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21); accessedOn: 2026-11-16; sourceRole: consulted-primary-author-abstract

**sourceLocator:** Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TranslationValidation-accepted-soundness"></a>

### accepted-soundness

`urn:csabs:axiom/TranslationValidation-accepted-soundness`

**description:** Defining obligation for Per-instance transformation validation

**statement:** check(s,t,scope)=proved ⇒ Obligation(scope,s,t).

**formalStatement:** check(s,t,scope)=proved ⇒ Obligation(scope,s,t).

**assumptions:** The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation; [Lopes et al., Alive2: Bounded Translation Validation for LLVM (author abstract)](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21); accessedOn: 2026-11-16; sourceRole: consulted-primary-author-abstract

**sourceLocator:** Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-TranslationValidation-bounded-scope"></a>

### bounded-scope

`urn:csabs:axiom/TranslationValidation-bounded-scope`

**description:** Defining obligation for Per-instance transformation validation

**statement:** A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.

**formalStatement:** A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.

**assumptions:** The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation; [Lopes et al., Alive2: Bounded Translation Validation for LLVM (author abstract)](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21); accessedOn: 2026-11-16; sourceRole: consulted-primary-author-abstract

**sourceLocator:** Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-TranslationValidation-accepted-pipeline"></a>

### accepted-pipeline

`urn:csabs:law/TranslationValidation-accepted-pipeline`

**description:** Derived consequence within the selected semantic profile.

**statement:** If two accepted checks establish S ⊒ M and M ⊒ T as their actual unbounded obligations under identical semantics and input assumptions, then S ⊒ T.

**formalStatement:** If two accepted checks establish S ⊒ M and M ⊒ T as their actual unbounded obligations under identical semantics and input assumptions, then S ⊒ T.

**assumptions:** The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.

**dependsOn:** [accepted-soundness](TranslationValidation.md#node-urn-csabs-axiom-TranslationValidation-accepted-soundness); [transitive](BehaviorRefinement.md#node-urn-csabs-law-BehaviorRefinement-transitive)

**proofSketch:** Extract both obligations from sound acceptance and compose inclusions. Bounded or incompatible obligations do not meet the stated assumptions.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation; [Lopes et al., Alive2: Bounded Translation Validation for LLVM (author abstract)](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21); accessedOn: 2026-11-16; sourceRole: consulted-primary-author-abstract

**sourceLocator:** Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Alive2 official README](https://github.com/AliveToolkit/alive2/blob/master/README.md); accessedOn: 2026-11-16; sourceRole: consulted-primary-tool-documentation
- [Lopes et al., Alive2: Bounded Translation Validation for LLVM (author abstract)](https://web.ist.utl.pt/nuno.lopes/pubs.php?id=alive2-pldi21); accessedOn: 2026-11-16; sourceRole: consulted-primary-author-abstract

**sourceLocator:** Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TranslationValidation",
    "type": "Concept",
    "shortForm": "TranslationValidation",
    "fullName": "Per-instance transformation validation",
    "definition": "An instance checker for a concrete source/target pair against a stated refinement obligation, retaining semantic scope, bounds and distinct proved, counterexample and unknown outcomes.",
    "notation": "check(s,t)∈{proved,counterexample,unknown}; proved⇒Obligation(s,t)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DialectConversion",
      "urn:csabs:concept/GuardedRewrite"
    ],
    "hasOperation": [
      "urn:csabs:operation/TranslationValidation-validate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TranslationValidation-accepted-soundness",
      "urn:csabs:axiom/TranslationValidation-bounded-scope"
    ],
    "hasLaw": [
      "urn:csabs:law/TranslationValidation-accepted-pipeline"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.",
    "axiomBasis": "check(s,t,scope)=proved ⇒ Obligation(scope,s,t).; A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No SMT encoder, solver integration or validation of a concrete pass. Counterexample replay and scope metadata are external. A supplied soundness hypothesis is not proof that Alive2 implements this interface."
    ],
    "source": [
      "urn:csabs:source/compiler-alive",
      "urn:csabs:source/compiler-alive-paper-abstract"
    ],
    "sourceLocator": "Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An instance checker for a concrete source/target pair against a stated refinement obligation, retaining semantic scope, bounds and distinct proved, counterexample and unknown outcomes. check(s,t)∈{proved,counterexample,unknown}; proved⇒Obligation(s,t) The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision.",
    "leanFormulation": "structure TranslationValidation (P : Type u) where\n  obligation : P → P → Prop\n  check : P → P → ValidationVerdict\n  acceptedSound : ∀ s t, check s t = .proved → obligation s t",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.TranslationValidation",
    "formulationScope": "partial",
    "leanModelMapping": "Three-way verdict and acceptedSound law for a supplied obligation; bounds are part of that obligation.",
    "leanModelLimitations": "No SMT encoder, solver integration or validation of a concrete pass. Counterexample replay and scope metadata are external. A supplied soundness hypothesis is not proof that Alive2 implements this interface."
  },
  {
    "id": "urn:csabs:operation/TranslationValidation-validate",
    "type": "Operation",
    "name": "validate",
    "signature": "validate : Program×Program×Scope→Verdict",
    "description": "Check a fixed pair; return evidence scoped to the actual encoded obligation.",
    "concept": "urn:csabs:concept/TranslationValidation",
    "precondition": "Well-formed inputs and supported semantic subset.",
    "postcondition": "Check a fixed pair; return evidence scoped to the actual encoded obligation.",
    "totality": "Total reporting protocol; solver timeout maps to unknown.",
    "source": [
      "urn:csabs:source/compiler-alive",
      "urn:csabs:source/compiler-alive-paper-abstract"
    ],
    "sourceLocator": "Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TranslationValidation-accepted-soundness",
    "type": "Axiom",
    "name": "accepted-soundness",
    "description": "Defining obligation for Per-instance transformation validation",
    "statement": "check(s,t,scope)=proved ⇒ Obligation(scope,s,t).",
    "formalStatement": "check(s,t,scope)=proved ⇒ Obligation(scope,s,t).",
    "assumptions": [
      "The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision."
    ],
    "appliesTo": [
      "urn:csabs:concept/TranslationValidation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alive",
      "urn:csabs:source/compiler-alive-paper-abstract"
    ],
    "sourceLocator": "Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/TranslationValidation-bounded-scope",
    "type": "Axiom",
    "name": "bounded-scope",
    "description": "Defining obligation for Per-instance transformation validation",
    "statement": "A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.",
    "formalStatement": "A bounded obligation quantifies only over admitted bounded executions; its acceptance does not establish unbounded refinement.",
    "assumptions": [
      "The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision."
    ],
    "appliesTo": [
      "urn:csabs:concept/TranslationValidation"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alive",
      "urn:csabs:source/compiler-alive-paper-abstract"
    ],
    "sourceLocator": "Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/TranslationValidation-accepted-pipeline",
    "type": "Law",
    "name": "accepted-pipeline",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "If two accepted checks establish S ⊒ M and M ⊒ T as their actual unbounded obligations under identical semantics and input assumptions, then S ⊒ T.",
    "formalStatement": "If two accepted checks establish S ⊒ M and M ⊒ T as their actual unbounded obligations under identical semantics and input assumptions, then S ⊒ T.",
    "assumptions": [
      "The obligation records exact input pair, preconditions, semantic version, target layout, observation mapping and any loop/resource bound. A bounded proof is a proof of its bounded obligation only; a timeout or unsupported construct is unknown. A counterexample needs replay/interpretation under the same semantics and assumptions. Interprocedural transformations are outside the documented Alive2 support scope. No claim that current Alive2 master builds against LLVM 21.1.8 without a compatible revision."
    ],
    "appliesTo": [
      "urn:csabs:concept/TranslationValidation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TranslationValidation-accepted-soundness",
      "urn:csabs:law/BehaviorRefinement-transitive"
    ],
    "proofSketch": "Extract both obligations from sound acceptance and compose inclusions. Bounded or incompatible obligations do not meet the stated assumptions.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-alive",
      "urn:csabs:source/compiler-alive-paper-abstract"
    ],
    "sourceLocator": "Alive2 README: standalone translation validation, WARNING, build compatibility; author abstract: loop-unrolling bounds and missed bugs",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
