# Binary relation

A relation from A to B is a set of ordered pairs with first component in A and second in B; properties such as reflexivity or transitivity are optional constraints.

**Notation:** R ⊆ A × B; a R b iff (a,b) ∈ R.

**Stable ID:** `urn:csabs:concept/Relation`

**Categories:** Set theory and foundations

**Kind:** Relation

**Related concepts:** [Set](Set.md), [Cartesian product](CartesianProduct.md), [Equivalence relation](EquivalenceRelation.md)

## Backlinks

- [Finite database relation under set semantics](DatabaseRelation.md) — `relatedConcept`
- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `requiresConcept`
- [Directed Graph](DirectedGraph.md) — `requiresConcept`
- [Equivalence relation](EquivalenceRelation.md) — `relatedConcept`
- [Hoare Triple](HoareTriple.md) — `requiresConcept`
- [Java generic inference constraints and resolution obligations](JavaTypeInference.md) — `requiresConcept`
- [Java wildcard capture with fresh bounded variables](JavaWildcardCapture.md) — `requiresConcept`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `requiresConcept`
- [Linearizability](Linearizability.md) — `requiresConcept`
- [Lock with compatible access modes](Lock.md) — `requiresConcept`
- [Relational method contract with write effects](MethodContract.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `requiresConcept`
- [Finite set-valued multimap](Multimap.md) — `requiresConcept`
- [Contextual parametric declaration instantiation](ParametricInstantiation.md) — `requiresConcept`
- [Partial function](PartialFunction.md) — `requiresConcept`
- [Partial function](PartialFunction.md) — `specializationOf`
- [Preorder](Preorder.md) — `requiresConcept`
- [Preorder](Preorder.md) — `specializationOf`
- [Sequential Consistency](SequentialConsistency.md) — `requiresConcept`
- [Set](Set.md) — `relatedConcept`
- [Simulation](Simulation.md) — `specializationOf`
- [Transition System](TransitionSystem.md) — `requiresConcept`
- [Well Founded Relation](WellFoundedRelation.md) — `requiresConcept`
- [Well Founded Relation](WellFoundedRelation.md) — `specializationOf`

## Mathematical formulation

Rel(A,B)=A→B→Prop, equivalently ℘(A×B). R=S ⇔ ∀a∈A ∀b∈B, R(a,b)↔S(a,b). No totality, functionality or nonemptiness is imposed.

**Lean formulation** (in its source module context):

```lean
abbrev Relation (A : Type u) (B : Type v) := A → B → Prop
```

**Source:** [`Catalog.Relation`](../lean/Catalog/Foundations.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** A -> B -> Prop; relational composition is existential over the middle carrier.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected presentation: A relation from A to B is a set of ordered pairs with first component in A and second in B; properties such as reflexivity or transitivity are optional constraints. Governing rules: A relation is a subset of its typed Cartesian product. Inverse reverses the ordered pairs. Relational composition existentially joins over the middle carrier.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-relation-inverse"></a>

### inverse relation

`urn:csabs:operation/relation-inverse`

**signature:** R⁻¹ = {(b,a) | (a,b)∈R}

**description:** Reverses each ordered pair.

<a id="node-urn-csabs-operation-relation-composition"></a>

### relation composition

`urn:csabs:operation/relation-composition`

**signature:** S∘R = {(a,c) | ∃b: aRb ∧ bSc}

**description:** Relates an input to an output when an intermediate element connects them.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Relation-typing"></a>

### typing

`urn:csabs:axiom/Relation-typing`

**statement:** A relation is a subset of its typed Cartesian product.

**formalStatement:** R⊆A×B; R(a,b) iff (a,b)∈R

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Relation-inverse-definition"></a>

### inverse-definition

`urn:csabs:axiom/Relation-inverse-definition`

**statement:** Inverse reverses the ordered pairs.

**formalStatement:** (b,a)∈R⁻¹ iff (a,b)∈R

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Relation-composition-definition"></a>

### composition-definition

`urn:csabs:axiom/Relation-composition-definition`

**statement:** Relational composition existentially joins over the middle carrier.

**formalStatement:** (a,c)∈S∘R iff ∃b∈B: (a,b)∈R ∧ (b,c)∈S

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-Relation-inverse-involution"></a>

### inverse-involution

`urn:csabs:theorem/Relation-inverse-involution`

**statement:** Reversing a relation twice recovers it.

**formalStatement:** (R⁻¹)⁻¹=R

**proofSketch:** Unfold inverse membership twice and apply set extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Relation apply.

**dependsOn:** [typing](Relation.md#node-urn-csabs-axiom-Relation-typing); [inverse-definition](Relation.md#node-urn-csabs-axiom-Relation-inverse-definition); [composition-definition](Relation.md#node-urn-csabs-axiom-Relation-composition-definition)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-Relation-composition-associativity"></a>

### composition-associativity

`urn:csabs:theorem/Relation-composition-associativity`

**statement:** Typed relation composition is associative.

**formalStatement:** T∘(S∘R)=(T∘S)∘R

**proofSketch:** Expand membership on both sides into two existentially quantified intermediate elements; the formulas coincide.

**assumptions:** The explicit basis, carriers, and side conditions stated for Relation apply.

**dependsOn:** [typing](Relation.md#node-urn-csabs-axiom-Relation-typing); [inverse-definition](Relation.md#node-urn-csabs-axiom-Relation-inverse-definition); [composition-definition](Relation.md#node-urn-csabs-axiom-Relation-composition-definition)

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
    "id": "urn:csabs:concept/Relation",
    "type": "Concept",
    "shortForm": "Relation",
    "fullName": "Binary relation",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A relation from A to B is a set of ordered pairs with first component in A and second in B; properties such as reflexivity or transitivity are optional constraints.",
    "notation": "R ⊆ A × B; a R b iff (a,b) ∈ R.",
    "hasOperation": [
      "urn:csabs:operation/relation-inverse",
      "urn:csabs:operation/relation-composition"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Relation-typing",
      "urn:csabs:axiom/Relation-inverse-definition",
      "urn:csabs:axiom/Relation-composition-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/Relation-inverse-involution",
      "urn:csabs:theorem/Relation-composition-associativity"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/CartesianProduct",
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A relation from A to B is a set of ordered pairs with first component in A and second in B; properties such as reflexivity or transitivity are optional constraints. Governing rules: A relation is a subset of its typed Cartesian product. Inverse reverses the ordered pairs. Relational composition existentially joins over the middle carrier.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "leanFormulation": "abbrev Relation (A : Type u) (B : Type v) := A → B → Prop",
    "formulationSource": "urn:csabs:source/local-lean-Foundations",
    "formulationLocator": "Catalog.Relation",
    "formulationScope": "model",
    "leanModelMapping": "A -> B -> Prop; relational composition is existential over the middle carrier.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "Rel(A,B)=A→B→Prop, equivalently ℘(A×B). R=S ⇔ ∀a∈A ∀b∈B, R(a,b)↔S(a,b). No totality, functionality or nonemptiness is imposed."
  },
  {
    "id": "urn:csabs:operation/relation-inverse",
    "type": "Operation",
    "name": "inverse relation",
    "signature": "R⁻¹ = {(b,a) | (a,b)∈R}",
    "description": "Reverses each ordered pair.",
    "concept": "urn:csabs:concept/Relation"
  },
  {
    "id": "urn:csabs:operation/relation-composition",
    "type": "Operation",
    "name": "relation composition",
    "signature": "S∘R = {(a,c) | ∃b: aRb ∧ bSc}",
    "description": "Relates an input to an output when an intermediate element connects them.",
    "concept": "urn:csabs:concept/Relation"
  },
  {
    "id": "urn:csabs:axiom/Relation-typing",
    "type": "Axiom",
    "name": "typing",
    "statement": "A relation is a subset of its typed Cartesian product.",
    "formalStatement": "R⊆A×B; R(a,b) iff (a,b)∈R",
    "appliesTo": [
      "urn:csabs:concept/Relation"
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
    "id": "urn:csabs:axiom/Relation-inverse-definition",
    "type": "Axiom",
    "name": "inverse-definition",
    "statement": "Inverse reverses the ordered pairs.",
    "formalStatement": "(b,a)∈R⁻¹ iff (a,b)∈R",
    "appliesTo": [
      "urn:csabs:concept/Relation"
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
    "id": "urn:csabs:axiom/Relation-composition-definition",
    "type": "Axiom",
    "name": "composition-definition",
    "statement": "Relational composition existentially joins over the middle carrier.",
    "formalStatement": "(a,c)∈S∘R iff ∃b∈B: (a,b)∈R ∧ (b,c)∈S",
    "appliesTo": [
      "urn:csabs:concept/Relation"
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
    "id": "urn:csabs:theorem/Relation-inverse-involution",
    "type": "Theorem",
    "name": "inverse-involution",
    "statement": "Reversing a relation twice recovers it.",
    "formalStatement": "(R⁻¹)⁻¹=R",
    "proofSketch": "Unfold inverse membership twice and apply set extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Relation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Relation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Relation-typing",
      "urn:csabs:axiom/Relation-inverse-definition",
      "urn:csabs:axiom/Relation-composition-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Relation-composition-associativity",
    "type": "Theorem",
    "name": "composition-associativity",
    "statement": "Typed relation composition is associative.",
    "formalStatement": "T∘(S∘R)=(T∘S)∘R",
    "proofSketch": "Expand membership on both sides into two existentially quantified intermediate elements; the formulas coincide.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Relation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Relation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Relation-typing",
      "urn:csabs:axiom/Relation-inverse-definition",
      "urn:csabs:axiom/Relation-composition-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
