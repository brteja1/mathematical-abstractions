# Nondeterministic finite automaton without epsilon moves

A finite-state word recognizer that may choose any of a set of successors for each input symbol.

**Notation:** M=(Q,Σ,Δ,q₀,F); Δ:Q×Σ→𝒫(Q)

**Stable ID:** `urn:csabs:concept/NFA`

**Categories:** Languages and computation, Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Formal language of finite words](FormalLanguage.md), [Power set](PowerSet.md)

**Specializes:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md)

**Related concepts:** [Deterministic finite automaton with total transition](DFA.md), [Regular language over a finite alphabet](RegularLanguage.md)

## Backlinks

- [Deterministic finite automaton with total transition](DFA.md) — `relatedConcept`
- [Deterministic finite automaton with total transition](DFA.md) — `specializationOf`
- [Action-labelled transition system with initial states](LabelledTransitionSystem.md) — `relatedConcept`
- [Regular language over a finite alphabet](RegularLanguage.md) — `relatedConcept`

## Mathematical formulation

For finite A,Q, an NFA has δ:Q×A→℘(Q), one initial q₀ and accepting F⊆Q. A word is accepted iff some δ-path from q₀ ends in F. This selected transition type has no ε-moves.

**Lean formulation** (in its source module context):

```lean
structure NFA (A : Type u) (Q : Type v) [Fintype A] [Fintype Q]
    extends _root_.NFA A Q where
  single_initial : ∃ q, start = {q}
```

**Source:** [`Catalog.NFA`](../lean/Catalog/Languages.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Mathlib NFA restricted to a singleton start set; finite alphabet and states, no epsilon transitions.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: States and alphabet are finite and each step returns an arbitrary subset of states. Runs propagate all choices; acceptance needs at least one accepting endpoint.

**basisKind:** defined-structure

**basisScope:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**specializationNote:** Set S=Q, Act=Σ, I={q₀} and q —a→ r iff r∈Δ(q,a). F is extra acceptance data; the LTS trace set alone does not encode the accepted language.

**verificationObligation:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-NFA-runSet"></a>

### runSet

`urn:csabs:operation/NFA-runSet`

**signature:** Δ̂ : 𝒫(Q)×Σ*→𝒫(Q)

**description:** Propagates a set of possible states through a whole finite word.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Propagates a set of possible states through a whole finite word.

<a id="node-urn-csabs-operation-NFA-accepts"></a>

### accepts

`urn:csabs:operation/NFA-accepts`

**signature:** accepts_M : Σ*→Bool

**description:** Returns true exactly when some whole-word run ends in F.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns true exactly when some whole-word run ends in F.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-NFA-model"></a>

### model

`urn:csabs:axiom/NFA-model`

**statement:** States and alphabet are finite and each step returns an arbitrary subset of states.

**description:** States and alphabet are finite and each step returns an arbitrary subset of states.

**formalStatement:** Q finite ∧ Q≠∅; Σ finite; q₀∈Q; F⊆Q; Δ:Q×Σ→𝒫(Q)

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-NFA-run"></a>

### run

`urn:csabs:axiom/NFA-run`

**statement:** Runs propagate all choices; acceptance needs at least one accepting endpoint.

**description:** Runs propagate all choices; acceptance needs at least one accepting endpoint.

**formalStatement:** Δ̂(P,ε)=P; Δ̂(P,wa)=⋃_{q∈Δ̂(P,w)}Δ(q,a); accepts_M(w) iff Δ̂({q₀},w)∩F≠∅

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-NFA-run-union"></a>

### run-union

`urn:csabs:law/NFA-run-union`

**statement:** Set runs preserve arbitrary unions of starting states.

**description:** Set runs preserve arbitrary unions of starting states.

**formalStatement:** Δ̂(⋃_{j∈J}P_j,w)=⋃_{j∈J}Δ̂(P_j,w)

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on w. The empty word preserves the union. For a final symbol, distribute the successor union over the induction-hypothesis union. The empty family shows that ∅ remains a sink.

**dependsOn:** [model](NFA.md#node-urn-csabs-axiom-NFA-model); [run](NFA.md#node-urn-csabs-axiom-NFA-run); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

<a id="node-urn-csabs-law-NFA-run-composition"></a>

### run-composition

`urn:csabs:law/NFA-run-composition`

**statement:** Set runs compose across concatenated words.

**description:** Set runs compose across concatenated words.

**formalStatement:** Δ̂(P,uv)=Δ̂(Δ̂(P,u),v)

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on v with the empty-word and final-symbol run equations.

**dependsOn:** [model](NFA.md#node-urn-csabs-axiom-NFA-model); [run](NFA.md#node-urn-csabs-axiom-NFA-run); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Theorems

<a id="node-urn-csabs-theorem-NFA-subset-construction"></a>

### subset-construction

`urn:csabs:theorem/NFA-subset-construction`

**statement:** Every epsilon-free NFA has a language-equivalent DFA.

**description:** Every epsilon-free NFA has a language-equivalent DFA.

**formalStatement:** ∃D∈DFA(Σ):∀w:accepts_D(w)↔accepts_M(w)

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word.

**ruleRole:** derived-result

**proofSketch:** Use state set 𝒫(Q), start {q₀}, transition P↦⋃_{q∈P}Δ(q,a), accepting subsets intersecting F. Induction on w identifies the DFA state with Δ̂({q₀},w); 𝒫(Q) is finite and includes ∅ as a sink.

**dependsOn:** [model](NFA.md#node-urn-csabs-axiom-NFA-model); [run](NFA.md#node-urn-csabs-axiom-NFA-run); [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-NFA-reachable-set-invariant"></a>

### reachable-set-invariant

`urn:csabs:theorem/NFA-reachable-set-invariant`

**statement:** An invariant closed under all symbol successors contains every set-run endpoint.

**description:** An invariant closed under all symbol successors contains every set-run endpoint.

**formalStatement:** q₀∈B⊆Q ∧ (∀q∈B,a∈Σ:Δ(q,a)⊆B) ⇒ ∀w∈Σ*:Δ̂({q₀},w)⊆B

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** The start set is contained in B. Induct on word length; each successor set of a state already in B remains within B. Union over possible current states preserves the inclusion.

**dependsOn:** [model](NFA.md#node-urn-csabs-axiom-NFA-model); [run](NFA.md#node-urn-csabs-axiom-NFA-run); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/d741901d23b4522588e267177c77d10d_MIT18_404f20_lec2.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 4–6: NFA definition and subset-construction equivalence

**sourceNote:** Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/NFA",
    "type": "Concept",
    "shortForm": "NFA",
    "fullName": "Nondeterministic finite automaton without epsilon moves",
    "category": [
      "urn:csabs:category/languages-computation",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite-state word recognizer that may choose any of a set of successors for each input symbol.",
    "notation": "M=(Q,Σ,Δ,q₀,F); Δ:Q×Σ→𝒫(Q)",
    "hasOperation": [
      "urn:csabs:operation/NFA-runSet",
      "urn:csabs:operation/NFA-accepts"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/NFA-model",
      "urn:csabs:axiom/NFA-run"
    ],
    "hasLaw": [
      "urn:csabs:law/NFA-run-union",
      "urn:csabs:law/NFA-run-composition"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/NFA-subset-construction",
      "urn:csabs:theorem/NFA-reachable-set-invariant"
    ],
    "requiresConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/FormalLanguage",
      "urn:csabs:concept/PowerSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/DFA",
      "urn:csabs:concept/RegularLanguage"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: States and alphabet are finite and each step returns an arbitrary subset of states. Runs propagate all choices; acceptance needs at least one accepting endpoint.",
    "basisKind": "defined-structure",
    "basisScope": "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "specializationOf": [
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "specializationNote": "Set S=Q, Act=Σ, I={q₀} and q —a→ r iff r∈Δ(q,a). F is extra acceptance data; the LTS trace set alone does not encode the accepted language.",
    "leanFormulation": "structure NFA (A : Type u) (Q : Type v) [Fintype A] [Fintype Q]\n    extends _root_.NFA A Q where\n  single_initial : ∃ q, start = {q}",
    "formulationSource": "urn:csabs:source/local-lean-Languages",
    "formulationLocator": "Catalog.NFA",
    "formulationScope": "model",
    "leanModelMapping": "Mathlib NFA restricted to a singleton start set; finite alphabet and states, no epsilon transitions.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For finite A,Q, an NFA has δ:Q×A→℘(Q), one initial q₀ and accepting F⊆Q. A word is accepted iff some δ-path from q₀ ends in F. This selected transition type has no ε-moves."
  },
  {
    "id": "urn:csabs:operation/NFA-runSet",
    "type": "Operation",
    "name": "runSet",
    "signature": "Δ̂ : 𝒫(Q)×Σ*→𝒫(Q)",
    "description": "Propagates a set of possible states through a whole finite word.",
    "concept": "urn:csabs:concept/NFA",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Propagates a set of possible states through a whole finite word."
  },
  {
    "id": "urn:csabs:operation/NFA-accepts",
    "type": "Operation",
    "name": "accepts",
    "signature": "accepts_M : Σ*→Bool",
    "description": "Returns true exactly when some whole-word run ends in F.",
    "concept": "urn:csabs:concept/NFA",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns true exactly when some whole-word run ends in F."
  },
  {
    "id": "urn:csabs:axiom/NFA-model",
    "type": "Axiom",
    "name": "model",
    "statement": "States and alphabet are finite and each step returns an arbitrary subset of states.",
    "description": "States and alphabet are finite and each step returns an arbitrary subset of states.",
    "formalStatement": "Q finite ∧ Q≠∅; Σ finite; q₀∈Q; F⊆Q; Δ:Q×Σ→𝒫(Q)",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/NFA-run",
    "type": "Axiom",
    "name": "run",
    "statement": "Runs propagate all choices; acceptance needs at least one accepting endpoint.",
    "description": "Runs propagate all choices; acceptance needs at least one accepting endpoint.",
    "formalStatement": "Δ̂(P,ε)=P; Δ̂(P,wa)=⋃_{q∈Δ̂(P,w)}Δ(q,a); accepts_M(w) iff Δ̂({q₀},w)∩F≠∅",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Restricts the source epsilon-NFA model to Δ(q,ε)=∅. Acceptance is existential over paths, not universal. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/NFA-run-union",
    "type": "Law",
    "name": "run-union",
    "statement": "Set runs preserve arbitrary unions of starting states.",
    "description": "Set runs preserve arbitrary unions of starting states.",
    "formalStatement": "Δ̂(⋃_{j∈J}P_j,w)=⋃_{j∈J}Δ̂(P_j,w)",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on w. The empty word preserves the union. For a final symbol, distribute the successor union over the induction-hypothesis union. The empty family shows that ∅ remains a sink.",
    "dependsOn": [
      "urn:csabs:axiom/NFA-model",
      "urn:csabs:axiom/NFA-run",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:law/NFA-run-composition",
    "type": "Law",
    "name": "run-composition",
    "statement": "Set runs compose across concatenated words.",
    "description": "Set runs compose across concatenated words.",
    "formalStatement": "Δ̂(P,uv)=Δ̂(Δ̂(P,u),v)",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on v with the empty-word and final-symbol run equations.",
    "dependsOn": [
      "urn:csabs:axiom/NFA-model",
      "urn:csabs:axiom/NFA-run",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/NFA-subset-construction",
    "type": "Theorem",
    "name": "subset-construction",
    "statement": "Every epsilon-free NFA has a language-equivalent DFA.",
    "description": "Every epsilon-free NFA has a language-equivalent DFA.",
    "formalStatement": "∃D∈DFA(Σ):∀w:accepts_D(w)↔accepts_M(w)",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Use state set 𝒫(Q), start {q₀}, transition P↦⋃_{q∈P}Δ(q,a), accepting subsets intersecting F. Induction on w identifies the DFA state with Δ̂({q₀},w); 𝒫(Q) is finite and includes ∅ as a sink.",
    "dependsOn": [
      "urn:csabs:axiom/NFA-model",
      "urn:csabs:axiom/NFA-run",
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/NFA-reachable-set-invariant",
    "type": "Theorem",
    "name": "reachable-set-invariant",
    "statement": "An invariant closed under all symbol successors contains every set-run endpoint.",
    "description": "An invariant closed under all symbol successors contains every set-run endpoint.",
    "formalStatement": "q₀∈B⊆Q ∧ (∀q∈B,a∈Σ:Δ(q,a)⊆B) ⇒ ∀w∈Σ*:Δ̂({q₀},w)⊆B",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. No epsilon moves. A missing move is an empty successor set; a run must consume the whole finite word. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/NFA"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-nondeterminism"
    ],
    "sourceLocator": "Slides 4–6: NFA definition and subset-construction equivalence",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "The start set is contained in B. Induct on word length; each successor set of a state already in B remains within B. Union over possible current states preserves the inclusion.",
    "dependsOn": [
      "urn:csabs:axiom/NFA-model",
      "urn:csabs:axiom/NFA-run",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
