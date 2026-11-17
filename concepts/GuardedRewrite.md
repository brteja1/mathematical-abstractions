# Guarded contextual program rewrite

A conditional rewrite relation with a match guard, well-formedness obligations and semantic refinement in every admitted enclosing context.

**Notation:** G(s) ∧ s↝t ⇒ WF(t) ∧ ∀C∈Adm(s,t), Beh(C[t])⊆Beh(C[s])

**Stable ID:** `urn:csabs:concept/GuardedRewrite`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md), [Partial function](PartialFunction.md)

**Related concepts:** [Free ranked term algebra with variables](TermAlgebra.md), [Termination Variant](TerminationVariant.md), [Typed static single assignment with scoped uses](SSAForm.md), [Conservative resource effect summary](EffectSummary.md), [CFG refinement with path correspondence and progress](ControlFlowRefinement.md), [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md), [Abstract rewrite system](RewriteSystem.md)

## Backlinks

- [Typed IR legalization with representation relation](DialectConversion.md) — `relatedConcept`
- [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md) — `relatedConcept`
- [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md) — `relatedConcept`
- [Abstract rewrite system](RewriteSystem.md) — `relatedConcept`
- [Per-instance transformation validation](TranslationValidation.md) — `relatedConcept`

## Mathematical formulation

A conditional rewrite relation with a match guard, well-formedness obligations and semantic refinement in every admitted enclosing context. G(s) ∧ s↝t ⇒ WF(t) ∧ ∀C∈Adm(s,t), Beh(C[t])⊆Beh(C[s]) Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.

**Lean formulation** (in its source module context):

```lean
structure GuardedRewrite (P : Type u) where
  guard : P → Prop
  rewrite : P → P → Prop
  wellFormed : P → Prop
```

**Source:** [`Catalog.Transforms.GuardedRewrite`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Raw guard/rewrite/wellFormed predicates on fragments; contextual semantics must be supplied separately.

**Limits:** Lean carrier does not enforce contextual soundness or match transactions. No matching algorithm, capture avoidance, termination or confluence proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].; match(s)=none ⇒ IR_after=IR_before.

**basisKind:** relational-structural-definition

**basisScope:** Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; Lean carrier does not enforce contextual soundness or match transactions. No matching algorithm, capture avoidance, termination or confluence proof.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-GuardedRewrite-match"></a>

### match

`urn:csabs:operation/GuardedRewrite-match`

**signature:** match : Fragment→Option Substitution

**description:** Produce bindings satisfying the guard, or no match.

**precondition:** Well-formed fragment.

**postcondition:** Produce bindings satisfying the guard, or no match.

**totality:** Partial result represented by Option.

**source:** [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-GuardedRewrite-rewrite"></a>

### rewrite

`urn:csabs:operation/GuardedRewrite-rewrite`

**signature:** rewrite : Fragment→P(Fragment)

**description:** Relate a matched source to permitted targets preserving interface, scope and observations in admitted contexts.

**precondition:** Guard, typing, dominance, effects and definedness obligations established.

**postcondition:** Relate a matched source to permitted targets preserving interface, scope and observations in admitted contexts.

**totality:** Relation may be empty or nondeterministic.

**source:** [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-GuardedRewrite-contextual-soundness"></a>

### contextual-soundness

`urn:csabs:axiom/GuardedRewrite-contextual-soundness`

**description:** Defining obligation for Guarded contextual program rewrite

**statement:** G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].

**formalStatement:** G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].

**assumptions:** Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-GuardedRewrite-failed-match"></a>

### failed-match

`urn:csabs:axiom/GuardedRewrite-failed-match`

**description:** Defining obligation for Guarded contextual program rewrite

**statement:** match(s)=none ⇒ IR_after=IR_before.

**formalStatement:** match(s)=none ⇒ IR_after=IR_before.

**assumptions:** Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-GuardedRewrite-composed-rewrite"></a>

### composed-rewrite

`urn:csabs:law/GuardedRewrite-composed-rewrite`

**description:** Derived consequence within the selected semantic profile.

**statement:** If two guarded rewrites preserve well-formedness and contextual refinement in the same admitted enclosing context C, then C[s] ⊒ C[u] for s↝t↝u.

**formalStatement:** If two guarded rewrites preserve well-formedness and contextual refinement in the same admitted enclosing context C, then C[s] ⊒ C[u] for s↝t↝u.

**assumptions:** Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.

**dependsOn:** [contextual-soundness](GuardedRewrite.md#node-urn-csabs-axiom-GuardedRewrite-contextual-soundness); [transitive](BehaviorRefinement.md#node-urn-csabs-law-BehaviorRefinement-transitive)

**proofSketch:** Apply contextual soundness to each enabled rewrite, then transitivity at each fixed admitted context; require both guards and context-admissibility conditions.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification; [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Pattern Rewriting (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/PatternRewriter.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/PatternRewriter.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification
- [LLVM IR Undefined Behavior Manual (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/UndefinedBehavior.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/GuardedRewrite",
    "type": "Concept",
    "shortForm": "GuardedRewrite",
    "fullName": "Guarded contextual program rewrite",
    "definition": "A conditional rewrite relation with a match guard, well-formedness obligations and semantic refinement in every admitted enclosing context.",
    "notation": "G(s) ∧ s↝t ⇒ WF(t) ∧ ∀C∈Adm(s,t), Beh(C[t])⊆Beh(C[s])",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/BehaviorRefinement",
      "urn:csabs:concept/PartialFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TermAlgebra",
      "urn:csabs:concept/TerminationVariant",
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/EffectSummary",
      "urn:csabs:concept/ControlFlowRefinement",
      "urn:csabs:concept/LLVMAttributeContract",
      "urn:csabs:concept/RewriteSystem"
    ],
    "hasOperation": [
      "urn:csabs:operation/GuardedRewrite-match",
      "urn:csabs:operation/GuardedRewrite-rewrite"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/GuardedRewrite-contextual-soundness",
      "urn:csabs:axiom/GuardedRewrite-failed-match"
    ],
    "hasLaw": [
      "urn:csabs:law/GuardedRewrite-composed-rewrite"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.",
    "axiomBasis": "G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].; match(s)=none ⇒ IR_after=IR_before.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "Lean carrier does not enforce contextual soundness or match transactions. No matching algorithm, capture avoidance, termination or confluence proof."
    ],
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A conditional rewrite relation with a match guard, well-formedness obligations and semantic refinement in every admitted enclosing context. G(s) ∧ s↝t ⇒ WF(t) ∧ ∀C∈Adm(s,t), Beh(C[t])⊆Beh(C[s]) Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof.",
    "leanFormulation": "structure GuardedRewrite (P : Type u) where\n  guard : P → Prop\n  rewrite : P → P → Prop\n  wellFormed : P → Prop",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.GuardedRewrite",
    "formulationScope": "partial",
    "leanModelMapping": "Raw guard/rewrite/wellFormed predicates on fragments; contextual semantics must be supplied separately.",
    "leanModelLimitations": "Lean carrier does not enforce contextual soundness or match transactions. No matching algorithm, capture avoidance, termination or confluence proof."
  },
  {
    "id": "urn:csabs:operation/GuardedRewrite-match",
    "type": "Operation",
    "name": "match",
    "signature": "match : Fragment→Option Substitution",
    "description": "Produce bindings satisfying the guard, or no match.",
    "concept": "urn:csabs:concept/GuardedRewrite",
    "precondition": "Well-formed fragment.",
    "postcondition": "Produce bindings satisfying the guard, or no match.",
    "totality": "Partial result represented by Option.",
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/GuardedRewrite-rewrite",
    "type": "Operation",
    "name": "rewrite",
    "signature": "rewrite : Fragment→P(Fragment)",
    "description": "Relate a matched source to permitted targets preserving interface, scope and observations in admitted contexts.",
    "concept": "urn:csabs:concept/GuardedRewrite",
    "precondition": "Guard, typing, dominance, effects and definedness obligations established.",
    "postcondition": "Relate a matched source to permitted targets preserving interface, scope and observations in admitted contexts.",
    "totality": "Relation may be empty or nondeterministic.",
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/GuardedRewrite-contextual-soundness",
    "type": "Axiom",
    "name": "contextual-soundness",
    "description": "Defining obligation for Guarded contextual program rewrite",
    "statement": "G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].",
    "formalStatement": "G(s) ∧ rewrite(s,t) ∧ WF(s) ⇒ WF(t) ∧ ∀C∈Adm(s,t), C[s] ⊒ C[t].",
    "assumptions": [
      "Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof."
    ],
    "appliesTo": [
      "urn:csabs:concept/GuardedRewrite"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/GuardedRewrite-failed-match",
    "type": "Axiom",
    "name": "failed-match",
    "description": "Defining obligation for Guarded contextual program rewrite",
    "statement": "match(s)=none ⇒ IR_after=IR_before.",
    "formalStatement": "match(s)=none ⇒ IR_after=IR_before.",
    "assumptions": [
      "Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof."
    ],
    "appliesTo": [
      "urn:csabs:concept/GuardedRewrite"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/GuardedRewrite-composed-rewrite",
    "type": "Law",
    "name": "composed-rewrite",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "If two guarded rewrites preserve well-formedness and contextual refinement in the same admitted enclosing context C, then C[s] ⊒ C[u] for s↝t↝u.",
    "formalStatement": "If two guarded rewrites preserve well-formedness and contextual refinement in the same admitted enclosing context C, then C[s] ⊒ C[u] for s↝t↝u.",
    "assumptions": [
      "Programs/IR fragments have binders, types and free operands. Adm contains well-typed contexts satisfying explicit interface and representation conditions. A local expression identity alone supplies no context closure. Failed matching leaves IR unchanged. Driver termination and confluence are independent obligations; bounded rewrite recursion is a client assertion, not a proof."
    ],
    "appliesTo": [
      "urn:csabs:concept/GuardedRewrite"
    ],
    "dependsOn": [
      "urn:csabs:axiom/GuardedRewrite-contextual-soundness",
      "urn:csabs:law/BehaviorRefinement-transitive"
    ],
    "proofSketch": "Apply contextual soundness to each enabled rewrite, then transitivity at each fixed admitted context; require both guards and context-admissibility conditions.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-patterns",
      "urn:csabs:source/compiler-ub"
    ],
    "sourceLocator": "PatternRewriter: matchAndRewrite, Restrictions, Application Recursion, Greedy Pattern Rewrite Driver; UB Manual: speculative division example",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
