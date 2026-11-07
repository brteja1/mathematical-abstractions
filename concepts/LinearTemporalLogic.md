# Linear temporal logic on infinite discrete traces

Classical temporal formulas evaluated along an infinite sequence of propositional valuations, with next and strong until.

**Notation:** φ ::= p | ⊥ | ¬φ | (φ∧φ) | Xφ | (φ U φ); σ:ℕ→𝒫(AP)

**Stable ID:** `urn:csabs:concept/LinearTemporalLogic`

**Categories:** Logic and proof, Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Propositional Logic](PropositionalLogic.md), [Finite serial Kripke structure for model checking](KripkeStructure.md)

**Related concepts:** [Safety Property](SafetyProperty.md), [Liveness Property](LivenessProperty.md), [Classical propositional modal logic K](ModalLogic.md)

## Backlinks

- [Finite serial Kripke structure for model checking](KripkeStructure.md) — `relatedConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `relatedConcept`
- [Propositional Logic](PropositionalLogic.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Atoms and Boolean connectives are evaluated at the current position. Next advances one position; strong until requires a finite future witness. Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.

**basisKind:** defined-structure

**basisScope:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**verificationObligation:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LinearTemporalLogic-satisfies"></a>

### satisfies

`urn:csabs:operation/LinearTemporalLogic-satisfies`

**signature:** ⊨ : (ℕ→𝒫(AP))×ℕ×LTLFormula→Prop

**description:** Evaluates a temporal formula at a position on an infinite trace.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Evaluates a temporal formula at a position on an infinite trace.

<a id="node-urn-csabs-operation-LinearTemporalLogic-modelSatisfies"></a>

### modelSatisfies

`urn:csabs:operation/LinearTemporalLogic-modelSatisfies`

**signature:** ⊨_K : KripkeStructure×LTLFormula→Prop

**description:** Requires the formula to hold at time zero along every initial path.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Requires the formula to hold at time zero along every initial path.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LinearTemporalLogic-state-connectives"></a>

### state-connectives

`urn:csabs:axiom/LinearTemporalLogic-state-connectives`

**statement:** Atoms and Boolean connectives are evaluated at the current position.

**description:** Atoms and Boolean connectives are evaluated at the current position.

**formalStatement:** σ,i⊨p iff p∈σ(i); σ,i⊭⊥; σ,i⊨¬φ iff not(σ,i⊨φ); σ,i⊨φ∧ψ iff σ,i⊨φ and σ,i⊨ψ

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LinearTemporalLogic-next-until"></a>

### next-until

`urn:csabs:axiom/LinearTemporalLogic-next-until`

**statement:** Next advances one position; strong until requires a finite future witness.

**description:** Next advances one position; strong until requires a finite future witness.

**formalStatement:** σ,i⊨Xφ iff σ,i+1⊨φ; σ,i⊨φ U ψ iff ∃j≥i:(σ,j⊨ψ ∧ ∀k:(i≤k<j⇒σ,k⊨φ))

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models"></a>

### derived-modalities-and-models

`urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models`

**statement:** Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.

**description:** Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.

**formalStatement:** ⊤:=¬⊥; Fφ:=⊤ U φ; Gφ:=¬F¬φ; K⊨φ iff ∀π∈Paths(K):trace(π),0⊨φ

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-LinearTemporalLogic-next-boolean-laws"></a>

### next-boolean-laws

`urn:csabs:law/LinearTemporalLogic-next-boolean-laws`

**statement:** On infinite traces, next commutes with negation and conjunction.

**description:** On infinite traces, next commutes with negation and conjunction.

**formalStatement:** X¬φ ≡ ¬Xφ; X(φ∧ψ) ≡ Xφ∧Xψ

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** All occurrences evaluate at the same next index i+1. Infinite-trace definedness guarantees that this position exists; apply the Boolean clauses there.

**dependsOn:** [state-connectives](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-state-connectives); [next-until](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-next-until); [derived-modalities-and-models](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models)

<a id="node-urn-csabs-law-LinearTemporalLogic-eventually-always-unfold"></a>

### eventually-always-unfold

`urn:csabs:law/LinearTemporalLogic-eventually-always-unfold`

**statement:** Eventually and always admit one-step unfolding.

**description:** Eventually and always admit one-step unfolding.

**formalStatement:** Fφ ≡ φ∨XFφ; Gφ ≡ φ∧XGφ

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Eventually has a witness at the current position or a later one. Always requires truth now and at every position in the next suffix. Derive both by the until and defined-modality clauses.

**dependsOn:** [state-connectives](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-state-connectives); [next-until](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-next-until); [derived-modalities-and-models](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models); [until-unfolding](LinearTemporalLogic.md#node-urn-csabs-theorem-LinearTemporalLogic-until-unfolding)

## Theorems

<a id="node-urn-csabs-theorem-LinearTemporalLogic-until-unfolding"></a>

### until-unfolding

`urn:csabs:theorem/LinearTemporalLogic-until-unfolding`

**statement:** Strong until obeys its one-step unfolding law.

**description:** Strong until obeys its one-step unfolding law.

**formalStatement:** φ U ψ ≡ ψ ∨ (φ ∧ X(φ U ψ))

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** derived-result

**proofSketch:** Split a witness j≥i into j=i and j>i. In the latter case φ holds at i and the same witness works from i+1. Conversely a witness at i or one for the next suffix supplies the until witness. This law alone does not distinguish strong from weak until; the existential definition does.

**dependsOn:** [state-connectives](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-state-connectives); [next-until](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-next-until); [derived-modalities-and-models](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-LinearTemporalLogic-always-invariant-rule"></a>

### always-invariant-rule

`urn:csabs:theorem/LinearTemporalLogic-always-invariant-rule`

**statement:** Truth initially and persistent truth imply always truth along the trace.

**description:** Truth initially and persistent truth imply always truth along the trace.

**formalStatement:** σ,0⊨φ ∧ σ,0⊨G(φ→Xφ) ⇒ σ,0⊨Gφ

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.; φ→ψ is classical implication, defined from negation and conjunction. No fairness premise is used.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on i. The premise supplies φ at i=0. At every i, the always implication transfers φ at i to φ at i+1. The always semantics then quantifies over all positions.

**dependsOn:** [state-connectives](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-state-connectives); [next-until](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-next-until); [derived-modalities-and-models](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

<a id="node-urn-csabs-theorem-LinearTemporalLogic-until-least-fixedpoint"></a>

### until-least-fixedpoint

`urn:csabs:theorem/LinearTemporalLogic-until-least-fixedpoint`

**statement:** Strong until is the least solution of its position-set unfolding equation.

**description:** Strong until is the least solution of its position-set unfolding equation.

**formalStatement:** {i:σ,i⊨φ U ψ}=μZ.[B∪(A∩Pre(Z))]; A={i:σ,i⊨φ}; B={i:σ,i⊨ψ}; Pre(Z)={i:i+1∈Z}

**assumptions:** Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Let Z₀=∅ and Zₙ₊₁=B∪(A∩Pre(Zₙ)). Inductively Zₙ contains exactly positions with an until witness fewer than n steps away. Their union is the existential strong-until set and is fixed. Every prefixed point contains all Zₙ by induction, hence contains their union. Thus the solution is least, unlike weak-until solutions allowed by unfolding alone.

**dependsOn:** [state-connectives](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-state-connectives); [next-until](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-next-until); [derived-modalities-and-models](LinearTemporalLogic.md#node-urn-csabs-axiom-LinearTemporalLogic-derived-modalities-and-models); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [Ruben Martins: CMU 15-414 (2024), Lecture 21, Linear Temporal Logic](https://www.cs.cmu.edu/~15414/s24/lectures/21-ltl.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3, Definitions 2–3, pp. L21.3–L21.4

**sourceNote:** Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LinearTemporalLogic",
    "type": "Concept",
    "shortForm": "LinearTemporalLogic",
    "fullName": "Linear temporal logic on infinite discrete traces",
    "category": [
      "urn:csabs:category/logic",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Classical temporal formulas evaluated along an infinite sequence of propositional valuations, with next and strong until.",
    "notation": "φ ::= p | ⊥ | ¬φ | (φ∧φ) | Xφ | (φ U φ); σ:ℕ→𝒫(AP)",
    "hasOperation": [
      "urn:csabs:operation/LinearTemporalLogic-satisfies",
      "urn:csabs:operation/LinearTemporalLogic-modelSatisfies"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models"
    ],
    "hasLaw": [
      "urn:csabs:law/LinearTemporalLogic-next-boolean-laws",
      "urn:csabs:law/LinearTemporalLogic-eventually-always-unfold"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LinearTemporalLogic-until-unfolding",
      "urn:csabs:theorem/LinearTemporalLogic-always-invariant-rule",
      "urn:csabs:theorem/LinearTemporalLogic-until-least-fixedpoint"
    ],
    "requiresConcept": [
      "urn:csabs:concept/PropositionalLogic",
      "urn:csabs:concept/KripkeStructure"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SafetyProperty",
      "urn:csabs:concept/LivenessProperty",
      "urn:csabs:concept/ModalLogic"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Atoms and Boolean connectives are evaluated at the current position. Next advances one position; strong until requires a finite future witness. Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.",
    "basisKind": "defined-structure",
    "basisScope": "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ]
  },
  {
    "id": "urn:csabs:operation/LinearTemporalLogic-satisfies",
    "type": "Operation",
    "name": "satisfies",
    "signature": "⊨ : (ℕ→𝒫(AP))×ℕ×LTLFormula→Prop",
    "description": "Evaluates a temporal formula at a position on an infinite trace.",
    "concept": "urn:csabs:concept/LinearTemporalLogic",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Evaluates a temporal formula at a position on an infinite trace."
  },
  {
    "id": "urn:csabs:operation/LinearTemporalLogic-modelSatisfies",
    "type": "Operation",
    "name": "modelSatisfies",
    "signature": "⊨_K : KripkeStructure×LTLFormula→Prop",
    "description": "Requires the formula to hold at time zero along every initial path.",
    "concept": "urn:csabs:concept/LinearTemporalLogic",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Requires the formula to hold at time zero along every initial path."
  },
  {
    "id": "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
    "type": "Axiom",
    "name": "state-connectives",
    "statement": "Atoms and Boolean connectives are evaluated at the current position.",
    "description": "Atoms and Boolean connectives are evaluated at the current position.",
    "formalStatement": "σ,i⊨p iff p∈σ(i); σ,i⊭⊥; σ,i⊨¬φ iff not(σ,i⊨φ); σ,i⊨φ∧ψ iff σ,i⊨φ and σ,i⊨ψ",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LinearTemporalLogic-next-until",
    "type": "Axiom",
    "name": "next-until",
    "statement": "Next advances one position; strong until requires a finite future witness.",
    "description": "Next advances one position; strong until requires a finite future witness.",
    "formalStatement": "σ,i⊨Xφ iff σ,i+1⊨φ; σ,i⊨φ U ψ iff ∃j≥i:(σ,j⊨ψ ∧ ∀k:(i≤k<j⇒σ,k⊨φ))",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models",
    "type": "Axiom",
    "name": "derived-modalities-and-models",
    "statement": "Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.",
    "description": "Eventually and always abbreviate until and negation; system satisfaction ranges over initial paths.",
    "formalStatement": "⊤:=¬⊥; Fφ:=⊤ U φ; Gφ:=¬F¬φ; K⊨φ iff ∀π∈Paths(K):trace(π),0⊨φ",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Restricts the source trace semantics to infinite discrete traces, so every suffix exists. Uses strong until including a witness at the current position; F and G are defined operators. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/LinearTemporalLogic-next-boolean-laws",
    "type": "Law",
    "name": "next-boolean-laws",
    "statement": "On infinite traces, next commutes with negation and conjunction.",
    "description": "On infinite traces, next commutes with negation and conjunction.",
    "formalStatement": "X¬φ ≡ ¬Xφ; X(φ∧ψ) ≡ Xφ∧Xψ",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "All occurrences evaluate at the same next index i+1. Infinite-trace definedness guarantees that this position exists; apply the Boolean clauses there.",
    "dependsOn": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models"
    ]
  },
  {
    "id": "urn:csabs:law/LinearTemporalLogic-eventually-always-unfold",
    "type": "Law",
    "name": "eventually-always-unfold",
    "statement": "Eventually and always admit one-step unfolding.",
    "description": "Eventually and always admit one-step unfolding.",
    "formalStatement": "Fφ ≡ φ∨XFφ; Gφ ≡ φ∧XGφ",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Eventually has a witness at the current position or a later one. Always requires truth now and at every position in the next suffix. Derive both by the until and defined-modality clauses.",
    "dependsOn": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models",
      "urn:csabs:theorem/LinearTemporalLogic-until-unfolding"
    ]
  },
  {
    "id": "urn:csabs:theorem/LinearTemporalLogic-until-unfolding",
    "type": "Theorem",
    "name": "until-unfolding",
    "statement": "Strong until obeys its one-step unfolding law.",
    "description": "Strong until obeys its one-step unfolding law.",
    "formalStatement": "φ U ψ ≡ ψ ∨ (φ ∧ X(φ U ψ))",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Split a witness j≥i into j=i and j>i. In the latter case φ holds at i and the same witness works from i+1. Conversely a witness at i or one for the next suffix supplies the until witness. This law alone does not distinguish strong from weak until; the existential definition does.",
    "dependsOn": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/LinearTemporalLogic-always-invariant-rule",
    "type": "Theorem",
    "name": "always-invariant-rule",
    "statement": "Truth initially and persistent truth imply always truth along the trace.",
    "description": "Truth initially and persistent truth imply always truth along the trace.",
    "formalStatement": "σ,0⊨φ ∧ σ,0⊨G(φ→Xφ) ⇒ σ,0⊨Gφ",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised.",
      "φ→ψ is classical implication, defined from negation and conjunction. No fairness premise is used."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on i. The premise supplies φ at i=0. At every i, the always implication transfers φ at i to φ at i+1. The always semantics then quantifies over all positions.",
    "dependsOn": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/LinearTemporalLogic-until-least-fixedpoint",
    "type": "Theorem",
    "name": "until-least-fixedpoint",
    "statement": "Strong until is the least solution of its position-set unfolding equation.",
    "description": "Strong until is the least solution of its position-set unfolding equation.",
    "formalStatement": "{i:σ,i⊨φ U ψ}=μZ.[B∪(A∩Pre(Z))]; A={i:σ,i⊨φ}; B={i:σ,i⊨ψ}; Pre(Z)={i:i+1∈Z}",
    "assumptions": [
      "Positions i∈ℕ. All traces are infinite; no finite-trace or termination semantics, fairness or probabilistic assumption is implicit. When interpreted on a Kripke structure, satisfaction is universal over its initial paths. No generic evaluation algorithm for arbitrary trace representations is promised."
    ],
    "appliesTo": [
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/martins-ltl"
    ],
    "sourceLocator": "§3, Definitions 2–3, pp. L21.3–L21.4",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Let Z₀=∅ and Zₙ₊₁=B∪(A∩Pre(Zₙ)). Inductively Zₙ contains exactly positions with an until witness fewer than n steps away. Their union is the existential strong-until set and is fixed. Every prefixed point contains all Zₙ by induction, hence contains their union. Thus the solution is least, unlike weak-until solutions allowed by unfolding alone.",
    "dependsOn": [
      "urn:csabs:axiom/LinearTemporalLogic-state-connectives",
      "urn:csabs:axiom/LinearTemporalLogic-next-until",
      "urn:csabs:axiom/LinearTemporalLogic-derived-modalities-and-models",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
