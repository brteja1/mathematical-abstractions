# Finite serial Kripke structure for model checking

A finite transition system whose states carry propositional valuations, with at least one successor from each state.

**Notation:** K=(S,I,R,AP,L); R⊆S×S; L:S→𝒫(AP)

**Stable ID:** `urn:csabs:concept/KripkeStructure`

**Categories:** Behavior and transition systems, Logic and proof

**Kind:** semantic-model

**Prerequisites:** [Transition System](TransitionSystem.md), [Propositional Logic](PropositionalLogic.md)

**Specializes:** [Transition System](TransitionSystem.md)

**Related concepts:** [Classical propositional modal logic K](ModalLogic.md), [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md)

## Backlinks

- [Linear temporal logic on infinite discrete traces](LinearTemporalLogic.md) — `requiresConcept`
- [Classical propositional modal logic K](ModalLogic.md) — `relatedConcept`
- [Transition System](TransitionSystem.md) — `relatedConcept`

## Mathematical formulation

A Kripke structure is (S,I,R,L) with finite S, I⊆S, serial R⊆S×S satisfying ∀s∃t,R(s,t), and L:S→℘(AP). I may be empty; the label records atomic propositions true at each state.

**Lean formulation** (in its source module context):

```lean
structure KripkeStructure (S : Type u) (AP : Type v) [Fintype S] where
  initial : _root_.Set S
  next : S → S → Prop
  serial : ∀ s, ∃ t, next s t
  label : S → _root_.Set AP
```

**Source:** [`Catalog.KripkeStructure`](../lean/Catalog/Graphs.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Finite state type, initial set, serial transition relation and propositional labels.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: A finite state model has propositional labels and a total next-state relation in the serial sense. Executions start in an initial state and follow the relation indefinitely.

**basisKind:** defined-structure

**basisScope:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**specializationNote:** Keep the parent states S, initials I and next-state relation R. Add finite-state and seriality restrictions and a state labelling L. Labels describe states rather than actions; do not identify this with an action-labelled LTS without a specified conversion.

**verificationObligation:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-KripkeStructure-successors"></a>

### successors

`urn:csabs:operation/KripkeStructure-successors`

**signature:** succ_K : S→𝒫(S)

**description:** Returns the finite nonempty successor set.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the finite nonempty successor set.

<a id="node-urn-csabs-operation-KripkeStructure-label"></a>

### label

`urn:csabs:operation/KripkeStructure-label`

**signature:** L : S→𝒫(AP)

**description:** Returns the atoms true in the given state.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the atoms true in the given state.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-KripkeStructure-serial-labelled-model"></a>

### serial-labelled-model

`urn:csabs:axiom/KripkeStructure-serial-labelled-model`

**statement:** A finite state model has propositional labels and a total next-state relation in the serial sense.

**description:** A finite state model has propositional labels and a total next-state relation in the serial sense.

**formalStatement:** S finite ∧ S≠∅; ∅≠I⊆S; AP finite; L:S→𝒫(AP); R⊆S×S; ∀s∈S:∃t∈S:sRt; succ_K(s)={t:sRt}

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-KripkeStructure-infinite-paths"></a>

### infinite-paths

`urn:csabs:axiom/KripkeStructure-infinite-paths`

**statement:** Executions start in an initial state and follow the relation indefinitely.

**description:** Executions start in an initial state and follow the relation indefinitely.

**formalStatement:** Paths(K)={π:ℕ→S:π(0)∈I ∧ ∀i:π(i)Rπ(i+1)}; trace(π)(i)=L(π(i))

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-KripkeStructure-path-tail"></a>

### path-tail

`urn:csabs:law/KripkeStructure-path-tail`

**statement:** Dropping the first state preserves the step condition of an infinite path.

**description:** Dropping the first state preserves the step condition of an infinite path.

**formalStatement:** π∈Paths(K) ⇒ ∀i≥0:π(i+1)Rπ(i+2); tail(π)(i)=π(i+1)

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Reindex the defining step condition. The tail starts at π(1), which need not be initial; thus it is not asserted to belong to Paths(K) with the original I.

**dependsOn:** [infinite-paths](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-infinite-paths)

## Theorems

<a id="node-urn-csabs-theorem-KripkeStructure-initial-path-existence"></a>

### initial-path-existence

`urn:csabs:theorem/KripkeStructure-initial-path-existence`

**statement:** Every initial state has an infinite path.

**description:** Every initial state has an infinite path.

**formalStatement:** ∀s∈I:∃π∈Paths(K):π(0)=s

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** derived-result

**proofSketch:** Fix an enumeration of finite S and choose the first successor of each state; seriality ensures it exists. Iterate this function from s by natural-number recursion.

**dependsOn:** [serial-labelled-model](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-serial-labelled-model); [infinite-paths](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-infinite-paths)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-KripkeStructure-reachable-invariant-principle"></a>

### reachable-invariant-principle

`urn:csabs:theorem/KripkeStructure-reachable-invariant-principle`

**statement:** An inductive state invariant holds at every position on every initial path.

**description:** An inductive state invariant holds at every position on every initial path.

**formalStatement:** I⊆B⊆S ∧ (∀s∈B,t:sRt⇒t∈B) ⇒ ∀π∈Paths(K),i∈ℕ:π(i)∈B

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** The path starts in I⊆B. Induct on the position and use preservation along its next R edge.

**dependsOn:** [serial-labelled-model](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-serial-labelled-model); [infinite-paths](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-infinite-paths); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

<a id="node-urn-csabs-theorem-KripkeStructure-lasso-path-existence"></a>

### lasso-path-existence

`urn:csabs:theorem/KripkeStructure-lasso-path-existence`

**statement:** Every initial state of a finite serial Kripke structure has an ultimately periodic path.

**description:** Every initial state of a finite serial Kripke structure has an ultimately periodic path.

**formalStatement:** ∀s∈I:∃π∈Paths(K),m≥0,p≥1:π(0)=s ∧ ∀i≥m:π(i+p)=π(i)

**assumptions:** S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Choose one successor of each state and iterate from s. Among |S|+1 visited states one repeats. Since the chosen successor is a function, all later states repeat with that cycle period. This constructs one lasso path; it does not assert that every nondeterministic path is ultimately periodic.

**dependsOn:** [serial-labelled-model](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-serial-labelled-model); [infinite-paths](KripkeStructure.md#node-urn-csabs-axiom-KripkeStructure-infinite-paths); [initial-path-existence](KripkeStructure.md#node-urn-csabs-theorem-KripkeStructure-initial-path-existence)

## Concept provenance

- [E. M. Clarke et al.: Model Checking and the State Explosion Problem](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Model%20Checking%20and%20the%20State%20Explosion%20Problem.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §2, Definition 1 and infinite paths, p. 3

**sourceNote:** Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/KripkeStructure",
    "type": "Concept",
    "shortForm": "KripkeStructure",
    "fullName": "Finite serial Kripke structure for model checking",
    "category": [
      "urn:csabs:category/behavior",
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite transition system whose states carry propositional valuations, with at least one successor from each state.",
    "notation": "K=(S,I,R,AP,L); R⊆S×S; L:S→𝒫(AP)",
    "hasOperation": [
      "urn:csabs:operation/KripkeStructure-successors",
      "urn:csabs:operation/KripkeStructure-label"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/KripkeStructure-serial-labelled-model",
      "urn:csabs:axiom/KripkeStructure-infinite-paths"
    ],
    "hasLaw": [
      "urn:csabs:law/KripkeStructure-path-tail"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/KripkeStructure-initial-path-existence",
      "urn:csabs:theorem/KripkeStructure-reachable-invariant-principle",
      "urn:csabs:theorem/KripkeStructure-lasso-path-existence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/TransitionSystem",
      "urn:csabs:concept/PropositionalLogic"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ModalLogic",
      "urn:csabs:concept/LinearTemporalLogic"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: A finite state model has propositional labels and a total next-state relation in the serial sense. Executions start in an initial state and follow the relation indefinitely.",
    "basisKind": "defined-structure",
    "basisScope": "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties.",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "specializationOf": [
      "urn:csabs:concept/TransitionSystem"
    ],
    "specializationNote": "Keep the parent states S, initials I and next-state relation R. Add finite-state and seriality restrictions and a state labelling L. Labels describe states rather than actions; do not identify this with an action-labelled LTS without a specified conversion.",
    "leanFormulation": "structure KripkeStructure (S : Type u) (AP : Type v) [Fintype S] where\n  initial : _root_.Set S\n  next : S → S → Prop\n  serial : ∀ s, ∃ t, next s t\n  label : S → _root_.Set AP",
    "formulationSource": "urn:csabs:source/local-lean-Graphs",
    "formulationLocator": "Catalog.KripkeStructure",
    "formulationScope": "model",
    "leanModelMapping": "Finite state type, initial set, serial transition relation and propositional labels.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "A Kripke structure is (S,I,R,L) with finite S, I⊆S, serial R⊆S×S satisfying ∀s∃t,R(s,t), and L:S→℘(AP). I may be empty; the label records atomic propositions true at each state."
  },
  {
    "id": "urn:csabs:operation/KripkeStructure-successors",
    "type": "Operation",
    "name": "successors",
    "signature": "succ_K : S→𝒫(S)",
    "description": "Returns the finite nonempty successor set.",
    "concept": "urn:csabs:concept/KripkeStructure",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the finite nonempty successor set."
  },
  {
    "id": "urn:csabs:operation/KripkeStructure-label",
    "type": "Operation",
    "name": "label",
    "signature": "L : S→𝒫(AP)",
    "description": "Returns the atoms true in the given state.",
    "concept": "urn:csabs:concept/KripkeStructure",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the atoms true in the given state."
  },
  {
    "id": "urn:csabs:axiom/KripkeStructure-serial-labelled-model",
    "type": "Axiom",
    "name": "serial-labelled-model",
    "statement": "A finite state model has propositional labels and a total next-state relation in the serial sense.",
    "description": "A finite state model has propositional labels and a total next-state relation in the serial sense.",
    "formalStatement": "S finite ∧ S≠∅; ∅≠I⊆S; AP finite; L:S→𝒫(AP); R⊆S×S; ∀s∈S:∃t∈S:sRt; succ_K(s)={t:sRt}",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/KripkeStructure-infinite-paths",
    "type": "Axiom",
    "name": "infinite-paths",
    "statement": "Executions start in an initial state and follow the relation indefinitely.",
    "description": "Executions start in an initial state and follow the relation indefinitely.",
    "formalStatement": "Paths(K)={π:ℕ→S:π(0)∈I ∧ ∀i:π(i)Rπ(i+1)}; trace(π)(i)=L(π(i))",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Adapts the finite serial model in Definition 1. Requires nonempty states and initial states and finite AP explicitly; valuations are sets of true atoms. These restrictions define the chosen variant, not every Kripke model.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/KripkeStructure-path-tail",
    "type": "Law",
    "name": "path-tail",
    "statement": "Dropping the first state preserves the step condition of an infinite path.",
    "description": "Dropping the first state preserves the step condition of an infinite path.",
    "formalStatement": "π∈Paths(K) ⇒ ∀i≥0:π(i+1)Rπ(i+2); tail(π)(i)=π(i+1)",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Reindex the defining step condition. The tail starts at π(1), which need not be initial; thus it is not asserted to belong to Paths(K) with the original I.",
    "dependsOn": [
      "urn:csabs:axiom/KripkeStructure-infinite-paths"
    ]
  },
  {
    "id": "urn:csabs:theorem/KripkeStructure-initial-path-existence",
    "type": "Theorem",
    "name": "initial-path-existence",
    "statement": "Every initial state has an infinite path.",
    "description": "Every initial state has an infinite path.",
    "formalStatement": "∀s∈I:∃π∈Paths(K):π(0)=s",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Fix an enumeration of finite S and choose the first successor of each state; seriality ensures it exists. Iterate this function from s by natural-number recursion.",
    "dependsOn": [
      "urn:csabs:axiom/KripkeStructure-serial-labelled-model",
      "urn:csabs:axiom/KripkeStructure-infinite-paths"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/KripkeStructure-reachable-invariant-principle",
    "type": "Theorem",
    "name": "reachable-invariant-principle",
    "statement": "An inductive state invariant holds at every position on every initial path.",
    "description": "An inductive state invariant holds at every position on every initial path.",
    "formalStatement": "I⊆B⊆S ∧ (∀s∈B,t:sRt⇒t∈B) ⇒ ∀π∈Paths(K),i∈ℕ:π(i)∈B",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "The path starts in I⊆B. Induct on the position and use preservation along its next R edge.",
    "dependsOn": [
      "urn:csabs:axiom/KripkeStructure-serial-labelled-model",
      "urn:csabs:axiom/KripkeStructure-infinite-paths",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/KripkeStructure-lasso-path-existence",
    "type": "Theorem",
    "name": "lasso-path-existence",
    "statement": "Every initial state of a finite serial Kripke structure has an ultimately periodic path.",
    "description": "Every initial state of a finite serial Kripke structure has an ultimately periodic path.",
    "formalStatement": "∀s∈I:∃π∈Paths(K),m≥0,p≥1:π(0)=s ∧ ∀i≥m:π(i+p)=π(i)",
    "assumptions": [
      "S finite nonempty; I⊆S nonempty; AP finite; ∀s∈S:∃t:sRt. Infinite executions use ℕ-indexed paths. Deadlocks require an explicit completion such as a self-loop; such completion may affect next-step properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/KripkeStructure"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/clarke-state-explosion"
    ],
    "sourceLocator": "§2, Definition 1 and infinite paths, p. 3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Choose one successor of each state and iterate from s. Among |S|+1 visited states one repeats. Since the chosen successor is a function, all later states repeat with that cycle period. This constructs one lasso path; it does not assert that every nondeterministic path is ultimately periodic.",
    "dependsOn": [
      "urn:csabs:axiom/KripkeStructure-serial-labelled-model",
      "urn:csabs:axiom/KripkeStructure-infinite-paths",
      "urn:csabs:theorem/KripkeStructure-initial-path-existence"
    ]
  }
]
```
<!-- graph-record:end -->
