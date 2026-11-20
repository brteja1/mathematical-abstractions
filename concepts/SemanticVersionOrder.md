# Release precedence under Semantic Versioning 2.0.0

Total precedence preorder on parsed valid semantic versions; build metadata remains part of exact release identity but is ignored by precedence.

**Notation:** v=(major,minor,patch,pre,build); v≼w iff key(v)≤lex key(w)

**Stable ID:** `urn:csabs:concept/SemanticVersionOrder`

**Categories:** Order and fixed points

**Kind:** Relation

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Preorder](Preorder.md)

**Specializes:** [Preorder](Preorder.md)

**Related concepts:** [Total Order](TotalOrder.md)

## Mathematical formulation

Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.

**Lean formulation** (in its source module context):

```lean
structure SemanticVersionOrder where
  key : VersionKey
  build : List VersionText
```

**Source:** [`Catalog.SemanticVersionOrder`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.

**Limits:** Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Compare core major/minor/patch lexicographically. On a core tie compare prerelease: numeric IDs numerically, numeric before nonnumeric, nonnumeric by ASCII lexicographic order, proper list prefix first; absent prerelease is greatest. Ignore build metadata. These are defining comparison rules; reflexivity, transitivity and totality follow from the key construction.

**basisKind:** defined-structure

**basisScope:** Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included.

**specializationNote:** Carrier is the parsed release set and relation is key-projected precedence; retain explicit reflexivity and transitivity. Totality is an additional constraint. Antisymmetry holds only after identifying equal precedence keys.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SemanticVersionOrder-precedence"></a>

### precedence

`urn:csabs:operation/SemanticVersionOrder-precedence`

**signature:** le : SemVer×SemVer→Prop

**description:** Compare normalized parsed precedence keys, ignoring builds.

**precondition:** Both versions satisfy the parsed SemVer profile.

**postcondition:** True exactly when key(a)≤lex key(b).

**totality:** Total on the stated domain.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders

**sourceNote:** Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-SemanticVersionOrder-key"></a>

### precedence key

`urn:csabs:operation/SemanticVersionOrder-key`

**signature:** key : SemVer→VersionKey

**description:** Project major/minor/patch/prerelease.

**precondition:** Valid parsed semantic version.

**postcondition:** Build metadata is omitted; normal releases use the top prerelease sentinel.

**totality:** Total on the stated domain.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders

**sourceNote:** Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-SemanticVersionOrder-defining-profile"></a>

### defining profile

`urn:csabs:axiom/SemanticVersionOrder-defining-profile`

**statement:** Compare core major/minor/patch lexicographically. On a core tie compare prerelease: numeric IDs numerically, numeric before nonnumeric, nonnumeric by ASCII lexicographic order, proper list prefix first; absent prerelease is greatest. Ignore build metadata. These are defining comparison rules; reflexivity, transitivity and totality follow from the key construction.

**formalStatement:** Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.

**assumptions:** Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders

**sourceNote:** Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-SemanticVersionOrder-build-invariance"></a>

### build-invariance

`urn:csabs:law/SemanticVersionOrder-build-invariance`

**statement:** Both projected keys are k, so both inequalities are reflexivity.

**formalStatement:** ∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](SemanticVersionOrder.md#node-urn-csabs-axiom-SemanticVersionOrder-defining-profile)

**proofSketch:** Both projected keys are k, so both inequalities are reflexivity.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_build_invariance

**sourceNote:** Derived for the explicit selected model. Both projected keys are k, so both inequalities are reflexivity.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-SemanticVersionOrder-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/SemanticVersionOrder-model-satisfaction`

**statement:** The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.

**formalStatement:** (∀ a : Catalog.SemanticVersionOrder, Catalog.versionLE a a) ∧ (∀ a b c, Catalog.versionLE a b → Catalog.versionLE b c → Catalog.versionLE a c) ∧ (∀ a b, Catalog.versionLE a b ∨ Catalog.versionLE b a) ∧ (∀ a b, Catalog.versionLE a b → Catalog.versionLE b a → a.key = b.key)

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](SemanticVersionOrder.md#node-urn-csabs-axiom-SemanticVersionOrder-defining-profile)

**proofSketch:** The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_model_satisfaction

**sourceNote:** Derived for the explicit selected model. The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
(∀ a : Catalog.SemanticVersionOrder, Catalog.versionLE a a) ∧ (∀ a b c, Catalog.versionLE a b → Catalog.versionLE b c → Catalog.versionLE a c) ∧ (∀ a b, Catalog.versionLE a b ∨ Catalog.versionLE b a) ∧ (∀ a b, Catalog.versionLE a b → Catalog.versionLE b a → a.key = b.key)
```

**Source:** [`Catalog.version_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SemanticVersionOrder-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata."
}
```

<a id="node-urn-csabs-theorem-SemanticVersionOrder-build-invariance"></a>

### build-invariance

`urn:csabs:theorem/SemanticVersionOrder-build-invariance`

**statement:** Both projected keys are k, so both inequalities are reflexivity.

**formalStatement:** ∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](SemanticVersionOrder.md#node-urn-csabs-axiom-SemanticVersionOrder-defining-profile)

**proofSketch:** Both projected keys are k, so both inequalities are reflexivity.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_build_invariance

**sourceNote:** Derived for the explicit selected model. Both projected keys are k, so both inequalities are reflexivity.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩
```

**Source:** [`Catalog.version_build_invariance`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Both projected keys are k, so both inequalities are reflexivity.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/SemanticVersionOrder-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Both projected keys are k, so both inequalities are reflexivity."
}
```

## Concept provenance

- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html); citation: Specification §§2,9–11 and Backus–Naur grammar.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference
- [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders

**sourceNote:** Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SemanticVersionOrder",
    "type": "Concept",
    "shortForm": "SemanticVersionOrder",
    "fullName": "Release precedence under Semantic Versioning 2.0.0",
    "synonyms": [
      "SemVer precedence",
      "Semantic-version release order"
    ],
    "category": [
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "Total precedence preorder on parsed valid semantic versions; build metadata remains part of exact release identity but is ignored by precedence.",
    "notation": "v=(major,minor,patch,pre,build); v≼w iff key(v)≤lex key(w)",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Preorder"
    ],
    "relatedConcept": [
      "urn:csabs:concept/TotalOrder"
    ],
    "axiomBasis": "Compare core major/minor/patch lexicographically. On a core tie compare prerelease: numeric IDs numerically, numeric before nonnumeric, nonnumeric by ASCII lexicographic order, proper list prefix first; absent prerelease is greatest. Ignore build metadata. These are defining comparison rules; reflexivity, transitivity and totality follow from the key construction.",
    "basisKind": "defined-structure",
    "basisScope": "Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included.",
    "mathematicalFormulation": "Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/SemanticVersionOrder-precedence",
      "urn:csabs:operation/SemanticVersionOrder-key"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/SemanticVersionOrder-defining-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/SemanticVersionOrder-build-invariance"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/SemanticVersionOrder-model-satisfaction",
      "urn:csabs:theorem/SemanticVersionOrder-build-invariance"
    ],
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders",
    "sourceNote": "Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Preorder"
    ],
    "specializationNote": "Carrier is the parsed release set and relation is key-projected precedence; retain explicit reflexivity and transitivity. Totality is an additional constraint. Antisymmetry holds only after identifying equal precedence keys.",
    "leanFormulation": "structure SemanticVersionOrder where\n  key : VersionKey\n  build : List VersionText",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.SemanticVersionOrder",
    "formulationScope": "model",
    "leanModelMapping": "Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.",
    "leanModelLimitations": "Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/SemanticVersionOrder-precedence",
    "type": "Operation",
    "concept": "urn:csabs:concept/SemanticVersionOrder",
    "name": "precedence",
    "signature": "le : SemVer×SemVer→Prop",
    "description": "Compare normalized parsed precedence keys, ignoring builds.",
    "precondition": "Both versions satisfy the parsed SemVer profile.",
    "postcondition": "True exactly when key(a)≤lex key(b).",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders",
    "sourceNote": "Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/SemanticVersionOrder-key",
    "type": "Operation",
    "concept": "urn:csabs:concept/SemanticVersionOrder",
    "name": "precedence key",
    "signature": "key : SemVer→VersionKey",
    "description": "Project major/minor/patch/prerelease.",
    "precondition": "Valid parsed semantic version.",
    "postcondition": "Build metadata is omitted; normal releases use the top prerelease sentinel.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders",
    "sourceNote": "Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/SemanticVersionOrder-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Compare core major/minor/patch lexicographically. On a core tie compare prerelease: numeric IDs numerically, numeric before nonnumeric, nonnumeric by ASCII lexicographic order, proper list prefix first; absent prerelease is greatest. Ignore build metadata. These are defining comparison rules; reflexivity, transitivity and totality follow from the key construction.",
    "formalStatement": "Key=ℕ×lexℕ×lexℕ×lex WithTop(NonemptyList(ℕ⊕lex NonNumericASCIIWord)). SemVer=Key×List(ASCIIWord). v≼w ⇔ key(v)≤key(w). Key order is antisymmetric; the release relation is generally not antisymmetric because builds may differ.",
    "assumptions": [
      "Core fields are unbounded naturals serialized canonically without leading zeros. Prerelease is absent or a nonempty list of identifiers: numeric identifiers are naturals (canonical no-leading-zero decimal); nonnumeric identifiers are nonempty ASCII [0-9A-Za-z-] words containing a nondigit. Build identifiers are nonempty words over the same ASCII alphabet and may have leading zeros; absent build is []. Exact parsed release equality includes build metadata. No parser, coercion of invalid text, v-prefix, package-manager range syntax, time ordering, overflow or stability guarantee is included."
    ],
    "appliesTo": [
      "urn:csabs:concept/SemanticVersionOrder"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders",
    "sourceNote": "Adapts the normative parsed-version precedence rules to an exact mathematical key; deliberately preserves distinct build identities.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/SemanticVersionOrder-build-invariance",
    "type": "Law",
    "name": "build-invariance",
    "statement": "Both projected keys are k, so both inequalities are reflexivity.",
    "formalStatement": "∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/SemanticVersionOrder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SemanticVersionOrder-defining-profile"
    ],
    "proofSketch": "Both projected keys are k, so both inequalities are reflexivity.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_build_invariance",
    "sourceNote": "Derived for the explicit selected model. Both projected keys are k, so both inequalities are reflexivity.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/SemanticVersionOrder-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.",
    "formalStatement": "(∀ a : Catalog.SemanticVersionOrder, Catalog.versionLE a a) ∧ (∀ a b c, Catalog.versionLE a b → Catalog.versionLE b c → Catalog.versionLE a c) ∧ (∀ a b, Catalog.versionLE a b ∨ Catalog.versionLE b a) ∧ (∀ a b, Catalog.versionLE a b → Catalog.versionLE b a → a.key = b.key)",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/SemanticVersionOrder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SemanticVersionOrder-defining-profile"
    ],
    "proofSketch": "The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.",
    "provenanceKind": "derived",
    "leanFormulation": "(∀ a : Catalog.SemanticVersionOrder, Catalog.versionLE a a) ∧ (∀ a b c, Catalog.versionLE a b → Catalog.versionLE b c → Catalog.versionLE a c) ∧ (∀ a b, Catalog.versionLE a b ∨ Catalog.versionLE b a) ∧ (∀ a b, Catalog.versionLE a b → Catalog.versionLE b a → a.key = b.key)",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.version_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SemanticVersionOrder-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. The nested lexicographic linear order on parsed precedence keys supplies reflexivity, transitivity, comparability and key antisymmetry. Full release identity also contains build metadata.\"}"
  },
  {
    "id": "urn:csabs:theorem/SemanticVersionOrder-build-invariance",
    "type": "Theorem",
    "name": "build-invariance",
    "statement": "Both projected keys are k, so both inequalities are reflexivity.",
    "formalStatement": "∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/SemanticVersionOrder"
    ],
    "dependsOn": [
      "urn:csabs:axiom/SemanticVersionOrder-defining-profile"
    ],
    "proofSketch": "Both projected keys are k, so both inequalities are reflexivity.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-semver",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SemVer §§2,9–11, grammar; Mathlib List/Sum/Prod lexicographic orders; Catalog.version_build_invariance",
    "sourceNote": "Derived for the explicit selected model. Both projected keys are k, so both inequalities are reflexivity.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (k : Catalog.VersionKey) (a b : List Catalog.VersionText), Catalog.versionLE ⟨k, a⟩ ⟨k, b⟩ ∧ Catalog.versionLE ⟨k, b⟩ ⟨k, a⟩",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.version_build_invariance",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Both projected keys are k, so both inequalities are reflexivity.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/SemanticVersionOrder-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Both projected keys are k, so both inequalities are reflexivity.\"}"
  }
]
```
<!-- graph-record:end -->
