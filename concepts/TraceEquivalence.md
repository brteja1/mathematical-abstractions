# Strong finite partial-trace equivalence

Two states of one fixed labelled transition system are equivalent when their sets of finite observable action traces are equal.

**Notation:** s≡tr t iff Tr(s)=Tr(t)

**Stable ID:** `urn:csabs:concept/TraceEquivalence`

**Categories:** Behavior and transition systems, Concurrency and distributed systems

**Kind:** Relation

**Prerequisites:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Equivalence relation](EquivalenceRelation.md)

**Specializes:** [Equivalence relation](EquivalenceRelation.md)

**Related concepts:** [Bisimulation](Bisimulation.md), [Formal language of finite words](FormalLanguage.md)

## Backlinks

- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Equivalence is equality of the entire finite partial-trace sets.

**basisKind:** defined-structure

**basisScope:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**specializationNote:** Use the fixed LTS state set S as the parent carrier and equality of trace sets as its binary relation. Reflexivity, symmetry and transitivity are recorded below as a derived result, not inherited from prerequisites.

**verificationObligation:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TraceEquivalence-equivalent"></a>

### equivalent

`urn:csabs:operation/TraceEquivalence-equivalent`

**signature:** ≡tr : S×S→Prop

**description:** Compares trace sets semantically; no general decision algorithm for arbitrary infinite LTSs is asserted.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Compares trace sets semantically; no general decision algorithm for arbitrary infinite LTSs is asserted.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TraceEquivalence-trace-equality"></a>

### trace-equality

`urn:csabs:axiom/TraceEquivalence-trace-equality`

**statement:** Equivalence is equality of the entire finite partial-trace sets.

**description:** Equivalence is equality of the entire finite partial-trace sets.

**formalStatement:** s≡tr t iff ∀w∈Act*:(w∈Tr(s)↔w∈Tr(t))

**assumptions:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Selects strong finite partial traces; does not hide τ, require successful termination, or compare infinite traces. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-TraceEquivalence-residual-trace-equality"></a>

### residual-trace-equality

`urn:csabs:law/TraceEquivalence-residual-trace-equality`

**statement:** Trace-equivalent states have the same residual trace language after any given action.

**description:** Trace-equivalent states have the same residual trace language after any given action.

**formalStatement:** s≡tr t ⇒ ⋃_{s —a→ s′}Tr(s′)=⋃_{t —a→ t′}Tr(t′)

**assumptions:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** A word belongs to either union exactly when the same word prefixed by a is a trace of its source. Trace equivalence identifies these prefixed memberships.

**dependsOn:** [trace-equality](TraceEquivalence.md#node-urn-csabs-axiom-TraceEquivalence-trace-equality); [trace-first-step](LabelledTransitionSystem.md#node-urn-csabs-law-LabelledTransitionSystem-trace-first-step)

## Theorems

<a id="node-urn-csabs-theorem-TraceEquivalence-equivalence-laws"></a>

### equivalence-laws

`urn:csabs:theorem/TraceEquivalence-equivalence-laws`

**statement:** Trace equivalence is reflexive, symmetric and transitive.

**description:** Trace equivalence is reflexive, symmetric and transitive.

**formalStatement:** s≡tr s; s≡tr t⇒t≡tr s; s≡tr t ∧ t≡tr u⇒s≡tr u

**assumptions:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**ruleRole:** derived-result

**proofSketch:** Pointwise equivalence of membership predicates has these three properties, or equivalently use equality of trace sets.

**dependsOn:** [trace-equality](TraceEquivalence.md#node-urn-csabs-axiom-TraceEquivalence-trace-equality); [finite-paths](LabelledTransitionSystem.md#node-urn-csabs-axiom-LabelledTransitionSystem-finite-paths)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-TraceEquivalence-deterministic-successor-matching"></a>

### deterministic-successor-matching

`urn:csabs:theorem/TraceEquivalence-deterministic-successor-matching`

**statement:** Under action determinism, trace-equivalent states match steps to trace-equivalent successors.

**description:** Under action determinism, trace-equivalent states match steps to trace-equivalent successors.

**formalStatement:** s≡tr t ∧ s —a→ s′ ⇒ ∃t′:(t —a→ t′ ∧ s′≡tr t′), with the symmetric statement as well

**assumptions:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.; Action determinism: for each state x and action a, there is at most one a-successor. Without it the conclusion can fail; no state labels or termination predicates are compared.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** The one-letter trace a of s must also be a trace of t, so an a-successor exists. Determinism makes each residual union a single successor trace set; residual equality identifies these sets. Symmetry gives the reverse matching condition.

**dependsOn:** [trace-equality](TraceEquivalence.md#node-urn-csabs-axiom-TraceEquivalence-trace-equality); [residual-trace-equality](TraceEquivalence.md#node-urn-csabs-law-TraceEquivalence-residual-trace-equality); [trace-first-step](LabelledTransitionSystem.md#node-urn-csabs-law-LabelledTransitionSystem-trace-first-step)

<a id="node-urn-csabs-theorem-TraceEquivalence-finite-observation-substitution"></a>

### finite-observation-substitution

`urn:csabs:theorem/TraceEquivalence-finite-observation-substitution`

**statement:** Trace equivalence permits substitution in any property determined solely by the finite trace language.

**description:** Trace equivalence permits substitution in any property determined solely by the finite trace language.

**formalStatement:** s≡tr t ⇒ H(Tr(s))=H(Tr(t)), for every mathematical function H:𝒫(Act*)→B

**assumptions:** One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Trace equality supplies identical arguments to the same function. This is a substitution principle for finite-trace observations; it does not extend to branching, fairness or divergence-sensitive observations.

**dependsOn:** [trace-equality](TraceEquivalence.md#node-urn-csabs-axiom-TraceEquivalence-trace-equality)

## Concept provenance

- [Rob van Glabbeek: Modelling Concurrent Systems (2024), course notes](https://homepages.inf.ed.ac.uk/rvangla/MCS/notes.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time

**sourceNote:** Selects strong finite partial traces; does not hide τ, require successful termination, or compare infinite traces.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TraceEquivalence",
    "type": "Concept",
    "shortForm": "TraceEquivalence",
    "fullName": "Strong finite partial-trace equivalence",
    "category": [
      "urn:csabs:category/behavior",
      "urn:csabs:category/concurrency"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "Two states of one fixed labelled transition system are equivalent when their sets of finite observable action traces are equal.",
    "notation": "s≡tr t iff Tr(s)=Tr(t)",
    "hasOperation": [
      "urn:csabs:operation/TraceEquivalence-equivalent"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TraceEquivalence-trace-equality"
    ],
    "hasLaw": [
      "urn:csabs:law/TraceEquivalence-residual-trace-equality"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TraceEquivalence-equivalence-laws",
      "urn:csabs:theorem/TraceEquivalence-deterministic-successor-matching",
      "urn:csabs:theorem/TraceEquivalence-finite-observation-substitution"
    ],
    "requiresConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Bisimulation",
      "urn:csabs:concept/FormalLanguage"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Equivalence is equality of the entire finite partial-trace sets.",
    "basisKind": "defined-structure",
    "basisScope": "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Selects strong finite partial traces; does not hide τ, require successful termination, or compare infinite traces.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions."
    ],
    "specializationOf": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "specializationNote": "Use the fixed LTS state set S as the parent carrier and equality of trace sets as its binary relation. Reflexivity, symmetry and transitivity are recorded below as a derived result, not inherited from prerequisites."
  },
  {
    "id": "urn:csabs:operation/TraceEquivalence-equivalent",
    "type": "Operation",
    "name": "equivalent",
    "signature": "≡tr : S×S→Prop",
    "description": "Compares trace sets semantically; no general decision algorithm for arbitrary infinite LTSs is asserted.",
    "concept": "urn:csabs:concept/TraceEquivalence",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Compares trace sets semantically; no general decision algorithm for arbitrary infinite LTSs is asserted."
  },
  {
    "id": "urn:csabs:axiom/TraceEquivalence-trace-equality",
    "type": "Axiom",
    "name": "trace-equality",
    "statement": "Equivalence is equality of the entire finite partial-trace sets.",
    "description": "Equivalence is equality of the entire finite partial-trace sets.",
    "formalStatement": "s≡tr t iff ∀w∈Act*:(w∈Tr(s)↔w∈Tr(t))",
    "assumptions": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions."
    ],
    "appliesTo": [
      "urn:csabs:concept/TraceEquivalence"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Selects strong finite partial traces; does not hide τ, require successful termination, or compare infinite traces. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/TraceEquivalence-residual-trace-equality",
    "type": "Law",
    "name": "residual-trace-equality",
    "statement": "Trace-equivalent states have the same residual trace language after any given action.",
    "description": "Trace-equivalent states have the same residual trace language after any given action.",
    "formalStatement": "s≡tr t ⇒ ⋃_{s —a→ s′}Tr(s′)=⋃_{t —a→ t′}Tr(t′)",
    "assumptions": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions."
    ],
    "appliesTo": [
      "urn:csabs:concept/TraceEquivalence"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "A word belongs to either union exactly when the same word prefixed by a is a trace of its source. Trace equivalence identifies these prefixed memberships.",
    "dependsOn": [
      "urn:csabs:axiom/TraceEquivalence-trace-equality",
      "urn:csabs:law/LabelledTransitionSystem-trace-first-step"
    ]
  },
  {
    "id": "urn:csabs:theorem/TraceEquivalence-equivalence-laws",
    "type": "Theorem",
    "name": "equivalence-laws",
    "statement": "Trace equivalence is reflexive, symmetric and transitive.",
    "description": "Trace equivalence is reflexive, symmetric and transitive.",
    "formalStatement": "s≡tr s; s≡tr t⇒t≡tr s; s≡tr t ∧ t≡tr u⇒s≡tr u",
    "assumptions": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions."
    ],
    "appliesTo": [
      "urn:csabs:concept/TraceEquivalence"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Pointwise equivalence of membership predicates has these three properties, or equivalently use equality of trace sets.",
    "dependsOn": [
      "urn:csabs:axiom/TraceEquivalence-trace-equality",
      "urn:csabs:axiom/LabelledTransitionSystem-finite-paths"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/TraceEquivalence-deterministic-successor-matching",
    "type": "Theorem",
    "name": "deterministic-successor-matching",
    "statement": "Under action determinism, trace-equivalent states match steps to trace-equivalent successors.",
    "description": "Under action determinism, trace-equivalent states match steps to trace-equivalent successors.",
    "formalStatement": "s≡tr t ∧ s —a→ s′ ⇒ ∃t′:(t —a→ t′ ∧ s′≡tr t′), with the symmetric statement as well",
    "assumptions": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions.",
      "Action determinism: for each state x and action a, there is at most one a-successor. Without it the conclusion can fail; no state labels or termination predicates are compared."
    ],
    "appliesTo": [
      "urn:csabs:concept/TraceEquivalence"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "The one-letter trace a of s must also be a trace of t, so an a-successor exists. Determinism makes each residual union a single successor trace set; residual equality identifies these sets. Symmetry gives the reverse matching condition.",
    "dependsOn": [
      "urn:csabs:axiom/TraceEquivalence-trace-equality",
      "urn:csabs:law/TraceEquivalence-residual-trace-equality",
      "urn:csabs:law/LabelledTransitionSystem-trace-first-step"
    ]
  },
  {
    "id": "urn:csabs:theorem/TraceEquivalence-finite-observation-substitution",
    "type": "Theorem",
    "name": "finite-observation-substitution",
    "statement": "Trace equivalence permits substitution in any property determined solely by the finite trace language.",
    "description": "Trace equivalence permits substitution in any property determined solely by the finite trace language.",
    "formalStatement": "s≡tr t ⇒ H(Tr(s))=H(Tr(t)), for every mathematical function H:𝒫(Act*)→B",
    "assumptions": [
      "One fixed LTS with identity-equal actions; compare all finite prefixes from each state. Equality of trace sets can forget deadlock, branching and divergence distinctions."
    ],
    "appliesTo": [
      "urn:csabs:concept/TraceEquivalence"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/vanglabbeek-mcs"
    ],
    "sourceLocator": "Lecture 2: strong finitary partial trace equivalence; Lecture 3: linear versus branching time",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Trace equality supplies identical arguments to the same function. This is a substitution principle for finite-trace observations; it does not extend to branching, fairness or divergence-sensitive observations.",
    "dependsOn": [
      "urn:csabs:axiom/TraceEquivalence-trace-equality"
    ]
  }
]
```
<!-- graph-record:end -->
