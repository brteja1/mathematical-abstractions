# Typed IR legalization with representation relation

A partial relation between source and target IRs, with explicit target legality, potentially one-to-many type conversion and a separate semantic representation relation.

**Notation:** convert(s,t); Legal(t); typeConvert:SType→P(List TType); Rep(s,t)

**Stable ID:** `urn:csabs:concept/DialectConversion`

**Categories:** Programming-language semantics → Compiler transformations

**Kind:** semantic-model

**Prerequisites:** [Typed static single assignment with scoped uses](SSAForm.md), [Observable behavior refinement](BehaviorRefinement.md)

**Related concepts:** [Guarded contextual program rewrite](GuardedRewrite.md), [Partial function](PartialFunction.md), [Target-indexed storage and ABI layout](DataLayout.md), [Observable state representation relation](StateRepresentation.md), [Call-boundary behavior and effect contract](CallEffectContract.md), [Scoped LLVM attribute, flag and metadata contract](LLVMAttributeContract.md)

## Backlinks

- [Typed static single assignment with scoped uses](SSAForm.md) — `relatedConcept`
- [Observable state representation relation](StateRepresentation.md) — `relatedConcept`
- [Per-instance transformation validation](TranslationValidation.md) — `relatedConcept`

## Mathematical formulation

A partial relation between source and target IRs, with explicit target legality, potentially one-to-many type conversion and a separate semantic representation relation. convert(s,t); Legal(t); typeConvert:SType→P(List TType); Rep(s,t) Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.

**Lean formulation** (in its source module context):

```lean
structure DialectConversion (S T STy TTy : Type u) where
  convert : S → T → Prop
  legal : T → Prop
  typeConvert : STy → List TTy → Prop
  represents : S → T → Prop
```

**Source:** [`Catalog.Transforms.DialectConversion`](../lean/Catalog/CompilerTransforms.lean); consulted 2026-11-16.

**Scope:** partial

**Interpretation:** Raw convert/legality/typeConvert/represents relations, with one-to-many type lists.

**Limits:** No conversion driver, materialization implementation, ABI model or proof connecting legality to semantics; full/partial/analysis policies remain client predicates.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.; CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.

**basisKind:** relational-structural-definition

**basisScope:** Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.

**verificationObligation:** Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.; No conversion driver, materialization implementation, ABI model or proof connecting legality to semantics; full/partial/analysis policies remain client predicates.

**reviewStatus:** Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DialectConversion-convert"></a>

### convert

`urn:csabs:operation/DialectConversion-convert`

**signature:** convert : SIR→P(TIR)

**description:** Produce a target according to the selected full or partial legalization policy.

**precondition:** Source well formed, mode, legality and conversion patterns fixed.

**postcondition:** Produce a target according to the selected full or partial legalization policy.

**totality:** Partial/nondeterministic relation.

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DialectConversion-convert-type"></a>

### convert-type

`urn:csabs:operation/DialectConversion-convert-type`

**signature:** convertType : SType→P(List TType)

**description:** Return permitted target type sequences, including the empty sequence for erasure.

**precondition:** Dialect and target profile fixed.

**postcondition:** Return permitted target type sequences, including the empty sequence for erasure.

**totality:** Partial; unsupported distinct from successful erasure.

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DialectConversion-represents"></a>

### represents

`urn:csabs:operation/DialectConversion-represents`

**signature:** represents : SIR×TIR→Prop

**description:** State correspondence under explicit representation and semantic adapters.

**precondition:** Memory/layout/ABI and materialization semantics specified.

**postcondition:** State correspondence under explicit representation and semantic adapters.

**totality:** Total mathematical predicate.

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DialectConversion-full-legality"></a>

### full-legality

`urn:csabs:axiom/DialectConversion-full-legality`

**description:** Defining obligation for Typed IR legalization with representation relation

**statement:** Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.

**formalStatement:** Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.

**assumptions:** Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

<a id="node-urn-csabs-axiom-DialectConversion-semantic-obligation"></a>

### semantic-obligation

`urn:csabs:axiom/DialectConversion-semantic-obligation`

**description:** Defining obligation for Typed IR legalization with representation relation

**statement:** CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.

**formalStatement:** CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.

**assumptions:** Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.

**ruleRole:** defining-rule

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

**reviewStatus:** Editorial mathematical statement and derivation; no registered compiled witness.

## Laws

<a id="node-urn-csabs-law-DialectConversion-illegal-full-result-rejected"></a>

### illegal-full-result-rejected

`urn:csabs:law/DialectConversion-illegal-full-result-rejected`

**description:** Derived consequence within the selected semantic profile.

**statement:** A target with an operation rejected by the full-conversion target policy, after recursive-legality overrides, cannot be the result of successful full conversion.

**formalStatement:** A target with an operation rejected by the full-conversion target policy, after recursive-legality overrides, cannot be the result of successful full conversion.

**assumptions:** Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.

**dependsOn:** [full-legality](DialectConversion.md#node-urn-csabs-axiom-DialectConversion-full-legality)

**proofSketch:** Contraposition of the full-legality condition. Partial-conversion acceptance has a different policy.

**reviewStatus:** Editorial mathematical derivation; no registered compiled witness.

**notationLanguage:** informal mathematical Unicode

**source:** [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [MLIR Dialect Conversion (LLVM 21.1.8)](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/mlir/docs/DialectConversion.md); path: /linuxdev/ai_research/llvm/sources/llvm-project-llvmorg-21.1.8/mlir/docs/DialectConversion.md; accessedOn: 2026-11-16; sourceRole: consulted-primary-versioned-specification

**sourceLocator:** Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion

**sourceNote:** Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DialectConversion",
    "type": "Concept",
    "shortForm": "DialectConversion",
    "fullName": "Typed IR legalization with representation relation",
    "definition": "A partial relation between source and target IRs, with explicit target legality, potentially one-to-many type conversion and a separate semantic representation relation.",
    "notation": "convert(s,t); Legal(t); typeConvert:SType→P(List TType); Rep(s,t)",
    "category": [
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/SSAForm",
      "urn:csabs:concept/BehaviorRefinement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/GuardedRewrite",
      "urn:csabs:concept/PartialFunction",
      "urn:csabs:concept/DataLayout",
      "urn:csabs:concept/StateRepresentation",
      "urn:csabs:concept/CallEffectContract",
      "urn:csabs:concept/LLVMAttributeContract"
    ],
    "hasOperation": [
      "urn:csabs:operation/DialectConversion-convert",
      "urn:csabs:operation/DialectConversion-convert-type",
      "urn:csabs:operation/DialectConversion-represents"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DialectConversion-full-legality",
      "urn:csabs:axiom/DialectConversion-semantic-obligation"
    ],
    "hasLaw": [
      "urn:csabs:law/DialectConversion-illegal-full-result-rejected"
    ],
    "hasTheorem": [],
    "basisKind": "relational-structural-definition",
    "basisScope": "Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.",
    "axiomBasis": "Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.; CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial source/interface review; no concrete LLVM or MLIR pass correctness asserted.",
    "verificationObligation": [
      "Instantiate LLVM/MLIR edition, dialect, target data layout, carriers, equality, preconditions and observable behavior before using these obligations.",
      "No conversion driver, materialization implementation, ABI model or proof connecting legality to semantics; full/partial/analysis policies remain client predicates."
    ],
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "mathematicalFormulation": "A partial relation between source and target IRs, with explicit target legality, potentially one-to-many type conversion and a separate semantic representation relation. convert(s,t); Legal(t); typeConvert:SType→P(List TType); Rep(s,t) Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification.",
    "leanFormulation": "structure DialectConversion (S T STy TTy : Type u) where\n  convert : S → T → Prop\n  legal : T → Prop\n  typeConvert : STy → List TTy → Prop\n  represents : S → T → Prop",
    "formulationSource": "urn:csabs:source/compiler-lean",
    "formulationLocator": "Catalog.Transforms.DialectConversion",
    "formulationScope": "partial",
    "leanModelMapping": "Raw convert/legality/typeConvert/represents relations, with one-to-many type lists.",
    "leanModelLimitations": "No conversion driver, materialization implementation, ABI model or proof connecting legality to semantics; full/partial/analysis policies remain client predicates."
  },
  {
    "id": "urn:csabs:operation/DialectConversion-convert",
    "type": "Operation",
    "name": "convert",
    "signature": "convert : SIR→P(TIR)",
    "description": "Produce a target according to the selected full or partial legalization policy.",
    "concept": "urn:csabs:concept/DialectConversion",
    "precondition": "Source well formed, mode, legality and conversion patterns fixed.",
    "postcondition": "Produce a target according to the selected full or partial legalization policy.",
    "totality": "Partial/nondeterministic relation.",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DialectConversion-convert-type",
    "type": "Operation",
    "name": "convert-type",
    "signature": "convertType : SType→P(List TType)",
    "description": "Return permitted target type sequences, including the empty sequence for erasure.",
    "concept": "urn:csabs:concept/DialectConversion",
    "precondition": "Dialect and target profile fixed.",
    "postcondition": "Return permitted target type sequences, including the empty sequence for erasure.",
    "totality": "Partial; unsupported distinct from successful erasure.",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DialectConversion-represents",
    "type": "Operation",
    "name": "represents",
    "signature": "represents : SIR×TIR→Prop",
    "description": "State correspondence under explicit representation and semantic adapters.",
    "concept": "urn:csabs:concept/DialectConversion",
    "precondition": "Memory/layout/ABI and materialization semantics specified.",
    "postcondition": "State correspondence under explicit representation and semantic adapters.",
    "totality": "Total mathematical predicate.",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DialectConversion-full-legality",
    "type": "Axiom",
    "name": "full-legality",
    "description": "Defining obligation for Typed IR legalization with representation relation",
    "statement": "Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.",
    "formalStatement": "Successful full conversion ⇒ all target operations are legal under the target policy, including explicit recursive-legality rules.",
    "assumptions": [
      "Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification."
    ],
    "appliesTo": [
      "urn:csabs:concept/DialectConversion"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:axiom/DialectConversion-semantic-obligation",
    "type": "Axiom",
    "name": "semantic-obligation",
    "description": "Defining obligation for Typed IR legalization with representation relation",
    "statement": "CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.",
    "formalStatement": "CorrectConversion(s,t) ⇒ WellFormed(t) ∧ Rep(s,t) ∧ adaptedBeh(t)⊆Beh(s); legalization success alone supplies no semantic inclusion.",
    "assumptions": [
      "Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification."
    ],
    "appliesTo": [
      "urn:csabs:concept/DialectConversion"
    ],
    "ruleRole": "defining-rule",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Adapted into a reusable mathematical interface from the cited sections. The chosen carriers and restrictions are stated explicitly; this is not a complete compiler semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "Editorial mathematical statement and derivation; no registered compiled witness."
  },
  {
    "id": "urn:csabs:law/DialectConversion-illegal-full-result-rejected",
    "type": "Law",
    "name": "illegal-full-result-rejected",
    "description": "Derived consequence within the selected semantic profile.",
    "statement": "A target with an operation rejected by the full-conversion target policy, after recursive-legality overrides, cannot be the result of successful full conversion.",
    "formalStatement": "A target with an operation rejected by the full-conversion target policy, after recursive-legality overrides, cannot be the result of successful full conversion.",
    "assumptions": [
      "Legality is a client predicate on operations/types/attributes. Full, partial and analysis conversion have different structural success conditions, including recursively legal regions. Type conversion may erase, preserve or expand a source type into zero, one or many target types; values, block arguments, call signatures and materializations require coherent mappings. A legal IR is not automatically semantically equivalent. Cross-language correctness uses an explicit input/output representation and observation adapter; materialization operations themselves require semantic justification."
    ],
    "appliesTo": [
      "urn:csabs:concept/DialectConversion"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DialectConversion-full-legality"
    ],
    "proofSketch": "Contraposition of the full-legality condition. Partial-conversion acceptance has a different policy.",
    "reviewStatus": "Editorial mathematical derivation; no registered compiled witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/compiler-conversion"
    ],
    "sourceLocator": "Dialect Conversion: Modes of Conversion, Conversion Target, Recursive Legality, Type Conversion",
    "sourceNote": "Derived from the explicit dependsOn premises under the stated assumptions; exact claim and proof sketch are editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
