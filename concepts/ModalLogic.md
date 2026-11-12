# Classical propositional modal logic K

Classical propositional formulas extended by modalities interpreted over an arbitrary accessibility relation.

**Notation:** φ ::= p | ⊥ | ¬φ | (φ∧φ) | □φ; ◇φ := ¬□¬φ

**Stable ID:** `urn:csabs:concept/ModalLogic`

**Categories:** Logic and proof, Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Propositional Logic](PropositionalLogic.md), [Binary relation](Relation.md)

**Related concepts:** [Finite serial Kripke structure for model checking](KripkeStructure.md), [Predicate Logic](PredicateLogic.md), [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md)

## Backlinks

- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `relatedConcept`
- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `relatedConcept`
- [Propositional Logic](PropositionalLogic.md) — `relatedConcept`

## Mathematical formulation

For accessibility R⊆W×W and valuation v:W×AP→Prop, w⊨□φ ⇔ ∀t,R(w,t)⇒t⊨φ; atoms use v and ⊥,¬,∧ use their classical clauses. No reflexivity, transitivity or seriality is imposed on R by this evaluator.

**Lean formulation** (in its source module context):

```lean
def ModalLogic {AP : Type u} {W : Type v} (r : W → W → Prop)
    (valuation : W → AP → Prop) : ModalFormula AP → W → Prop
  | .atom p, s => valuation s p
  | .bottom, _ => False
  | .neg p, s => ¬ ModalLogic r valuation p s
  | .conj p q, s => ModalLogic r valuation p s ∧ ModalLogic r valuation q s
  | .box p, s => ∀ t, r s t → ModalLogic r valuation p t
```

**Source:** [`Catalog.ModalLogic`](../lean/Catalog/Logic.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Modal K formulas evaluated on arbitrary accessibility relations; box quantifies all successors, including vacuous dead ends.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: Atoms and connectives have classical truth conditions at each world. Box quantifies universally over accessible successors; diamond is its classical dual.

**basisKind:** defined-structure

**basisScope:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**verificationObligation:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ModalLogic-satisfies"></a>

### satisfies

`urn:csabs:operation/ModalLogic-satisfies`

**signature:** ⊨ : Model×World×ModalFormula→Prop

**description:** Evaluates truth in a model at a world; models may be infinite.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Evaluates truth in a model at a world; models may be infinite.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ModalLogic-boolean-semantics"></a>

### boolean-semantics

`urn:csabs:axiom/ModalLogic-boolean-semantics`

**statement:** Atoms and connectives have classical truth conditions at each world.

**description:** Atoms and connectives have classical truth conditions at each world.

**formalStatement:** M,w⊨p iff w∈V(p); M,w⊭⊥; M,w⊨¬φ iff not(M,w⊨φ); M,w⊨φ∧ψ iff M,w⊨φ and M,w⊨ψ

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ModalLogic-box-semantics"></a>

### box-semantics

`urn:csabs:axiom/ModalLogic-box-semantics`

**statement:** Box quantifies universally over accessible successors; diamond is its classical dual.

**description:** Box quantifies universally over accessible successors; diamond is its classical dual.

**formalStatement:** M,w⊨□φ iff ∀v:(wRv⇒M,v⊨φ); ◇φ:=¬□¬φ

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ModalLogic-box-conjunction"></a>

### box-conjunction

`urn:csabs:law/ModalLogic-box-conjunction`

**statement:** Box preserves finite conjunction.

**description:** Box preserves finite conjunction.

**formalStatement:** □(φ∧ψ) ≡ □φ∧□ψ

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** At each accessible world the conjunction holds exactly when both components hold. Universal quantification distributes over conjunction, including the vacuous dead-end case.

**dependsOn:** [boolean-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-boolean-semantics); [box-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-box-semantics)

<a id="node-urn-csabs-law-ModalLogic-diamond-existential"></a>

### diamond-existential

`urn:csabs:law/ModalLogic-diamond-existential`

**statement:** Diamond means that at least one accessible world satisfies its argument.

**description:** Diamond means that at least one accessible world satisfies its argument.

**formalStatement:** M,w⊨◇φ iff ∃v:(wRv ∧ M,v⊨φ)

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Expand ◇φ as ¬□¬φ, apply the box clause and classical quantifier duality. At a dead end no witness exists.

**dependsOn:** [boolean-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-boolean-semantics); [box-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-box-semantics)

## Theorems

<a id="node-urn-csabs-theorem-ModalLogic-distribution-K"></a>

### distribution-K

`urn:csabs:theorem/ModalLogic-distribution-K`

**statement:** Box distributes over implication in the K axiom scheme.

**description:** Box distributes over implication in the K axiom scheme.

**formalStatement:** M,w⊨□(φ→ψ)→(□φ→□ψ), where φ→ψ:=¬(φ∧¬ψ)

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.

**ruleRole:** derived-result

**proofSketch:** Assume both boxed premises. At every accessible world, implication and its antecedent hold, hence ψ holds by classical semantics. Thus □ψ holds; with no successors the same universal statement is vacuous.

**dependsOn:** [boolean-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-boolean-semantics); [box-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-box-semantics)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-ModalLogic-necessitation-validity"></a>

### necessitation-validity

`urn:csabs:theorem/ModalLogic-necessitation-validity`

**statement:** A globally valid formula remains valid when boxed.

**description:** A globally valid formula remains valid when boxed.

**formalStatement:** [∀M,w:M,w⊨φ] ⇒ [∀M,w:M,w⊨□φ]

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.; Validity is across all models and all worlds; the premise is not a local hypothesis M,w⊨φ.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Every accessible world in any model satisfies a globally valid φ, so the universal box condition holds. Truth at one particular world is not enough.

**dependsOn:** [boolean-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-boolean-semantics); [box-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-box-semantics)

<a id="node-urn-csabs-theorem-ModalLogic-formula-structural-induction"></a>

### formula-structural-induction

`urn:csabs:theorem/ModalLogic-formula-structural-induction`

**statement:** Prove a predicate on modal formula syntax by atom, falsity and constructor cases.

**description:** Prove a predicate on modal formula syntax by atom, falsity and constructor cases.

**formalStatement:** [∀p:P(p)] ∧ P(⊥) ∧ [∀φ:P(φ)⇒P(¬φ)] ∧ [∀φ,ψ:P(φ)∧P(ψ)⇒P(φ∧ψ)] ∧ [∀φ:P(φ)⇒P(□φ)] ⇒ ∀φ:P(φ)

**assumptions:** Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.; The syntax is φ ::= p | ⊥ | ¬φ | (φ∧φ) | □φ as recorded in the concept; semantic equivalence does not identify syntax trees.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Modal formulas are finite expressions built by exactly these constructors. Induct on syntax-tree height; every immediate subformula is shorter.

**dependsOn:** [boolean-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-boolean-semantics); [box-semantics](ModalLogic.md#node-urn-csabs-axiom-ModalLogic-box-semantics); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [Andre Platzer: CMU 15-816 (2010), Lecture 18, Model Checking](https://www.cs.cmu.edu/~fp/courses/15816-s10/lectures/18-modck.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, pp. L18.3–L18.4: modal satisfaction and truth sets

**sourceNote:** Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ModalLogic",
    "type": "Concept",
    "shortForm": "ModalLogic",
    "fullName": "Classical propositional modal logic K",
    "category": [
      "urn:csabs:category/logic",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Classical propositional formulas extended by modalities interpreted over an arbitrary accessibility relation.",
    "notation": "φ ::= p | ⊥ | ¬φ | (φ∧φ) | □φ; ◇φ := ¬□¬φ",
    "hasOperation": [
      "urn:csabs:operation/ModalLogic-satisfies"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics"
    ],
    "hasLaw": [
      "urn:csabs:law/ModalLogic-box-conjunction",
      "urn:csabs:law/ModalLogic-diamond-existential"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ModalLogic-distribution-K",
      "urn:csabs:theorem/ModalLogic-necessitation-validity",
      "urn:csabs:theorem/ModalLogic-formula-structural-induction"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PropositionalLogic",
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/KripkeStructure",
      "urn:csabs:concept/PredicateLogic",
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Atoms and connectives have classical truth conditions at each world. Box quantifies universally over accessible successors; diamond is its classical dual.",
    "basisKind": "defined-structure",
    "basisScope": "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "leanFormulation": "def ModalLogic {AP : Type u} {W : Type v} (r : W → W → Prop)\n    (valuation : W → AP → Prop) : ModalFormula AP → W → Prop\n  | .atom p, s => valuation s p\n  | .bottom, _ => False\n  | .neg p, s => ¬ ModalLogic r valuation p s\n  | .conj p q, s => ModalLogic r valuation p s ∧ ModalLogic r valuation q s\n  | .box p, s => ∀ t, r s t → ModalLogic r valuation p t",
    "formulationSource": "urn:csabs:source/local-lean-Logic",
    "formulationLocator": "Catalog.ModalLogic",
    "formulationScope": "model",
    "leanModelMapping": "Modal K formulas evaluated on arbitrary accessibility relations; box quantifies all successors, including vacuous dead ends.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For accessibility R⊆W×W and valuation v:W×AP→Prop, w⊨□φ ⇔ ∀t,R(w,t)⇒t⊨φ; atoms use v and ⊥,¬,∧ use their classical clauses. No reflexivity, transitivity or seriality is imposed on R by this evaluator."
  },
  {
    "id": "urn:csabs:operation/ModalLogic-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "⊨ : Model×World×ModalFormula→Prop",
    "description": "Evaluates truth in a model at a world; models may be infinite.",
    "concept": "urn:csabs:concept/ModalLogic",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Evaluates truth in a model at a world; models may be infinite."
  },
  {
    "id": "urn:csabs:axiom/ModalLogic-boolean-semantics",
    "type": "Axiom",
    "name": "boolean-semantics",
    "statement": "Atoms and connectives have classical truth conditions at each world.",
    "description": "Atoms and connectives have classical truth conditions at each world.",
    "formalStatement": "M,w⊨p iff w∈V(p); M,w⊭⊥; M,w⊨¬φ iff not(M,w⊨φ); M,w⊨φ∧ψ iff M,w⊨φ and M,w⊨ψ",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ModalLogic-box-semantics",
    "type": "Axiom",
    "name": "box-semantics",
    "statement": "Box quantifies universally over accessible successors; diamond is its classical dual.",
    "description": "Box quantifies universally over accessible successors; diamond is its classical dual.",
    "formalStatement": "M,w⊨□φ iff ∀v:(wRv⇒M,v⊨φ); ◇φ:=¬□¬φ",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Uses the one-modality arbitrary-frame fragment of the source discussion. No reflexivity, transitivity, seriality, proof calculus or completeness theorem is added. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ModalLogic-box-conjunction",
    "type": "Law",
    "name": "box-conjunction",
    "statement": "Box preserves finite conjunction.",
    "description": "Box preserves finite conjunction.",
    "formalStatement": "□(φ∧ψ) ≡ □φ∧□ψ",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "At each accessible world the conjunction holds exactly when both components hold. Universal quantification distributes over conjunction, including the vacuous dead-end case.",
    "dependsOn": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics"
    ]
  },
  {
    "id": "urn:csabs:law/ModalLogic-diamond-existential",
    "type": "Law",
    "name": "diamond-existential",
    "statement": "Diamond means that at least one accessible world satisfies its argument.",
    "description": "Diamond means that at least one accessible world satisfies its argument.",
    "formalStatement": "M,w⊨◇φ iff ∃v:(wRv ∧ M,v⊨φ)",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Expand ◇φ as ¬□¬φ, apply the box clause and classical quantifier duality. At a dead end no witness exists.",
    "dependsOn": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics"
    ]
  },
  {
    "id": "urn:csabs:theorem/ModalLogic-distribution-K",
    "type": "Theorem",
    "name": "distribution-K",
    "statement": "Box distributes over implication in the K axiom scheme.",
    "description": "Box distributes over implication in the K axiom scheme.",
    "formalStatement": "M,w⊨□(φ→ψ)→(□φ→□ψ), where φ→ψ:=¬(φ∧¬ψ)",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Assume both boxed premises. At every accessible world, implication and its antecedent hold, hence ψ holds by classical semantics. Thus □ψ holds; with no successors the same universal statement is vacuous.",
    "dependsOn": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/ModalLogic-necessitation-validity",
    "type": "Theorem",
    "name": "necessitation-validity",
    "statement": "A globally valid formula remains valid when boxed.",
    "description": "A globally valid formula remains valid when boxed.",
    "formalStatement": "[∀M,w:M,w⊨φ] ⇒ [∀M,w:M,w⊨□φ]",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.",
      "Validity is across all models and all worlds; the premise is not a local hypothesis M,w⊨φ."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Every accessible world in any model satisfies a globally valid φ, so the universal box condition holds. Truth at one particular world is not enough.",
    "dependsOn": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics"
    ]
  },
  {
    "id": "urn:csabs:theorem/ModalLogic-formula-structural-induction",
    "type": "Theorem",
    "name": "formula-structural-induction",
    "statement": "Prove a predicate on modal formula syntax by atom, falsity and constructor cases.",
    "description": "Prove a predicate on modal formula syntax by atom, falsity and constructor cases.",
    "formalStatement": "[∀p:P(p)] ∧ P(⊥) ∧ [∀φ:P(φ)⇒P(¬φ)] ∧ [∀φ,ψ:P(φ)∧P(ψ)⇒P(φ∧ψ)] ∧ [∀φ:P(φ)⇒P(□φ)] ⇒ ∀φ:P(φ)",
    "assumptions": [
      "Frames have nonempty W, R⊆W×W, and V:Atoms→𝒫(W). Dead ends are permitted: □φ is vacuously true there and ◇φ false. Formula syntax equality is distinct from semantic equivalence.",
      "The syntax is φ ::= p | ⊥ | ¬φ | (φ∧φ) | □φ as recorded in the concept; semantic equivalence does not identify syntax trees."
    ],
    "appliesTo": [
      "urn:csabs:concept/ModalLogic"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/platzer-modal-modelchecking"
    ],
    "sourceLocator": "§2, pp. L18.3–L18.4: modal satisfaction and truth sets",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Modal formulas are finite expressions built by exactly these constructors. Induct on syntax-tree height; every immediate subformula is shorter.",
    "dependsOn": [
      "urn:csabs:axiom/ModalLogic-boolean-semantics",
      "urn:csabs:axiom/ModalLogic-box-semantics",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
