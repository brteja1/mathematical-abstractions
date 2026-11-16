# Scoped LLVM attribute, flag and metadata contract

An explicit semantic contract for instruction/callsite/function attributes and metadata, separating input assumptions, poison/UB consequences, ABI requirements and removable optimization hints.

**Notation:** Admitted(p,i)⇒Guarantees(p,i); infer/copy facts only with scope-valid entailment

**Stable ID:** `urn:csabs:concept/LLVMAttributeContract`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Hoare Triple](HoareTriple.md), [Call-boundary behavior and effect contract](CallEffectContract.md)

**Related concepts:** [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md), [LLVM fixed-width integer operations and flags](LLVMIntegerSemantics.md), [LLVM floating-point environment and rewrite permissions](LLVMFloatingPointSemantics.md), [Analysis validity across IR mutation](AnalysisPreservation.md)

## Backlinks

- [Call-boundary behavior and effect contract](CallEffectContract.md) — `relatedConcept`
- [Typed IR legalization with representation relation](DialectConversion.md) — `relatedConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `relatedConcept`

## Mathematical formulation

An explicit semantic contract for instruction/callsite/function attributes and metadata, separating input assumptions, poison/UB consequences, ABI requirements and removable optimization hints. Admitted(p,i)⇒Guarantees(p,i); infer/copy facts only with scope-valid entailment LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.

**Lean formulation** (in its source module context):

```lean
structure LLVMAttributeContract (Program Input : Type u) where
  admitted : Program → Input → Prop
  guarantees : Program → Input → Prop
  justified : ∀ p i, admitted p i → guarantees p i
```

**Source:** [`Catalog.LLVM.LLVMAttributeContract`](../lean/Catalog/LLVMTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Admitted-input and guarantee predicates with a justified entailment field.

**Limits:** No parser/classification of actual LLVM attributes, flags or metadata, no inference engine, and no ABI/bundle implementation. Client entailment is a hypothesis, not an Attributor proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.; Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.

**basisKind:** relational-structural-definition

**basisScope:** LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No parser/classification of actual LLVM attributes, flags or metadata, no inference engine, and no ABI/bundle implementation. Client entailment is a hypothesis, not an Attributor proof.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LLVMAttributeContract-entails"></a>

### entails

`urn:csabs:operation/LLVMAttributeContract-entails`

**signature:** entails : Facts×ScopedContract→Prop

**description:** Prove the exact attribute/metadata fact at its new attachment point.

**precondition:** Definedness, path, lifetime, ABI and semantic version mapped.

**postcondition:** Prove the exact attribute/metadata fact at its new attachment point.

**totality:** Semantic entailment; generally undecidable.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LLVMAttributeContract-transfer"></a>

### transfer

`urn:csabs:operation/LLVMAttributeContract-transfer`

**signature:** transfer : OldAttachment×Mutation⇀NewAttachment

**description:** Retain only justified facts and required semantic bundles.

**precondition:** Each fact classified by its documented consequences and scope.

**postcondition:** Retain only justified facts and required semantic bundles.

**totality:** Partial; unsupported transfer drops only legally droppable information.

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LLVMAttributeContract-justified-guarantee"></a>

### justified-guarantee

`urn:csabs:axiom/LLVMAttributeContract-justified-guarantee`

**description:** Defining obligation for Scoped LLVM attribute, flag and metadata contract

**statement:** For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.

**formalStatement:** For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.

**assumptions:** LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

<a id="node-urn-csabs-axiom-LLVMAttributeContract-bundle-distinction"></a>

### bundle-distinction

`urn:csabs:axiom/LLVMAttributeContract-bundle-distinction`

**description:** Defining obligation for Scoped LLVM attribute, flag and metadata contract

**statement:** Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.

**formalStatement:** Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.

**assumptions:** LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-LLVMAttributeContract-invalid-strengthening"></a>

### invalid-strengthening

`urn:csabs:law/LLVMAttributeContract-invalid-strengthening`

**description:** Derived consequence in the stated profile.

**statement:** Adding a guarantee G when an admitted execution violates G does not satisfy the justified-guarantee obligation.

**formalStatement:** Adding a guarantee G when an admitted execution violates G does not satisfy the justified-guarantee obligation.

**assumptions:** LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.

**dependsOn:** [justified-guarantee](LLVMAttributeContract.md#node-urn-csabs-axiom-LLVMAttributeContract-justified-guarantee)

**proofSketch:** Instantiate the universal entailment with the violating execution to obtain a contradiction. The concrete poison/UB consequence depends on G.

**notationLanguage:** informal mathematical Unicode

**source:** [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.

**provenanceKind:** derived

**reviewStatus:** Editorial sourced mathematical obligation; no registered compiled witness.

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [LLVM Language Reference (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/docs/LangRef.rst); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/llvm/docs/LangRef.rst; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses

**sourceNote:** Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LLVMAttributeContract",
    "type": "Concept",
    "shortForm": "LLVMAttributeContract",
    "fullName": "Scoped LLVM attribute, flag and metadata contract",
    "definition": "An explicit semantic contract for instruction/callsite/function attributes and metadata, separating input assumptions, poison/UB consequences, ABI requirements and removable optimization hints.",
    "notation": "Admitted(p,i)⇒Guarantees(p,i); infer/copy facts only with scope-valid entailment",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/HoareTriple",
      "urn:csabs:concept/CallEffectContract"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AbstractInterpretation",
      "urn:csabs:concept/LLVMIntegerSemantics",
      "urn:csabs:concept/LLVMFloatingPointSemantics",
      "urn:csabs:concept/AnalysisPreservation"
    ],
    "hasOperation": [
      "urn:csabs:operation/LLVMAttributeContract-entails",
      "urn:csabs:operation/LLVMAttributeContract-transfer"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LLVMAttributeContract-justified-guarantee",
      "urn:csabs:axiom/LLVMAttributeContract-bundle-distinction"
    ],
    "hasLaw": [
      "urn:csabs:law/LLVMAttributeContract-invalid-strengthening"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.",
    "axiomBasis": "For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.; Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No parser/classification of actual LLVM attributes, flags or metadata, no inference engine, and no ABI/bundle implementation. Client entailment is a hypothesis, not an Attributor proof."
    ],
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "An explicit semantic contract for instruction/callsite/function attributes and metadata, separating input assumptions, poison/UB consequences, ABI requirements and removable optimization hints. Admitted(p,i)⇒Guarantees(p,i); infer/copy facts only with scope-valid entailment LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata.",
    "leanFormulation": "structure LLVMAttributeContract (Program Input : Type u) where\n  admitted : Program → Input → Prop\n  guarantees : Program → Input → Prop\n  justified : ∀ p i, admitted p i → guarantees p i",
    "formulationSource": "urn:csabs:source/compiler-llvm-lean",
    "formulationLocator": "Catalog.LLVM.LLVMAttributeContract",
    "formulationScope": "partial",
    "leanModelMapping": "Admitted-input and guarantee predicates with a justified entailment field.",
    "leanModelLimitations": "No parser/classification of actual LLVM attributes, flags or metadata, no inference engine, and no ABI/bundle implementation. Client entailment is a hypothesis, not an Attributor proof."
  },
  {
    "id": "urn:csabs:operation/LLVMAttributeContract-entails",
    "type": "Operation",
    "name": "entails",
    "signature": "entails : Facts×ScopedContract→Prop",
    "description": "Prove the exact attribute/metadata fact at its new attachment point.",
    "concept": "urn:csabs:concept/LLVMAttributeContract",
    "precondition": "Definedness, path, lifetime, ABI and semantic version mapped.",
    "postcondition": "Prove the exact attribute/metadata fact at its new attachment point.",
    "totality": "Semantic entailment; generally undecidable.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LLVMAttributeContract-transfer",
    "type": "Operation",
    "name": "transfer",
    "signature": "transfer : OldAttachment×Mutation⇀NewAttachment",
    "description": "Retain only justified facts and required semantic bundles.",
    "concept": "urn:csabs:concept/LLVMAttributeContract",
    "precondition": "Each fact classified by its documented consequences and scope.",
    "postcondition": "Retain only justified facts and required semantic bundles.",
    "totality": "Partial; unsupported transfer drops only legally droppable information.",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LLVMAttributeContract-justified-guarantee",
    "type": "Axiom",
    "name": "justified-guarantee",
    "description": "Defining obligation for Scoped LLVM attribute, flag and metadata contract",
    "statement": "For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.",
    "formalStatement": "For each inferred/copied guarantee, every admitted input/execution at the attachment point must satisfy the exact scoped contract.",
    "assumptions": [
      "LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMAttributeContract"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/LLVMAttributeContract-bundle-distinction",
    "type": "Axiom",
    "name": "bundle-distinction",
    "description": "Defining obligation for Scoped LLVM attribute, flag and metadata contract",
    "statement": "Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.",
    "formalStatement": "Operand bundles can affect escape, memory, control and runtime state; they cannot be treated as arbitrary removable metadata.",
    "assumptions": [
      "LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMAttributeContract"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Adapted Scoped LLVM attribute, flag and metadata contract from LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses. The catalog chooses the stated carrier and proof obligations; it does not claim that the reference proves an LLVM pass implementation satisfies them.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/LLVMAttributeContract-invalid-strengthening",
    "type": "Law",
    "name": "invalid-strengthening",
    "description": "Derived consequence in the stated profile.",
    "statement": "Adding a guarantee G when an admitted execution violates G does not satisfy the justified-guarantee obligation.",
    "formalStatement": "Adding a guarantee G when an admitted execution violates G does not satisfy the justified-guarantee obligation.",
    "assumptions": [
      "LLVM 21.1.8 exact attachment point and validity scope fixed. Attribute kinds differ: ABI constraints, input promises, poison-generating conditions, UB conditions, optimization permissions and hints are not interchangeable. Adding or strengthening a promise needs evidence for all admitted executions; moving/copying facts requires continued dominance/lifetime/context validity. Operand bundles are semantic, not freely droppable metadata; unknown bundles conservatively escape/read/write as specified. Debug-only metadata has a separate preservation contract when debugging is in scope. No generic drop-all rule covers ABI attributes, convergence/deopt bundles or all metadata."
    ],
    "appliesTo": [
      "urn:csabs:concept/LLVMAttributeContract"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LLVMAttributeContract-justified-guarantee"
    ],
    "proofSketch": "Instantiate the universal entailment with the violating execution to obtain a contradiction. The concrete poison/UB consequence depends on G.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-llvm"
    ],
    "sourceLocator": "LangRef: Parameter Attributes, Function Attributes, Metadata, Operand Bundles; memory, noundef, nonnull, dereferenceable, align, range, invariant and noalias clauses",
    "sourceNote": "Catalog derivation from the explicit dependsOn premises; the cited source motivates the interface, not this exact editorial theorem name.",
    "provenanceKind": "derived",
    "reviewStatus": "Editorial sourced mathematical obligation; no registered compiled witness."
  }
]
```
<!-- graph-record:end -->
