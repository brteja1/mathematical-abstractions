# Deterministic finite automaton with total transition

A finite-state recognizer with exactly one next state for every state and input symbol.

**Notation:** M=(Q,Σ,δ,q₀,F); δ:Q×Σ→Q

**Stable ID:** `urn:csabs:concept/DFA`

**Categories:** Languages and computation, Behavior and transition systems

**Kind:** semantic-model

**Prerequisites:** [Formal language of finite words](FormalLanguage.md), [Total function](Function.md)

**Specializes:** [Nondeterministic finite automaton without epsilon moves](NFA.md)

**Related concepts:** [Regular language over a finite alphabet](RegularLanguage.md), [Nondeterministic finite automaton without epsilon moves](NFA.md)

## Backlinks

- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `relatedConcept`
- [Regular language over a finite alphabet](RegularLanguage.md) — `requiresConcept`
- [Deterministic one-tape Turing machine](TuringMachine.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: The transition function is total on a finite state set and alphabet. The extended transition consumes symbols successively.

**basisKind:** defined-structure

**basisScope:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**specializationNote:** Instantiate the NFA transition by singleton sets Δ(q,a)={δ(q,a)}. Singleton totality removes nondeterministic choices; start and acceptance data are unchanged. The underlying carriers are identified by this explicit encoding.

**verificationObligation:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DFA-run"></a>

### run

`urn:csabs:operation/DFA-run`

**signature:** δ̂ : Q×Σ*→Q

**description:** Returns the unique state reached after consuming the word.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the unique state reached after consuming the word.

<a id="node-urn-csabs-operation-DFA-accepts"></a>

### accepts

`urn:csabs:operation/DFA-accepts`

**signature:** accepts_M : Σ*→Bool

**description:** Tests membership of the final run state in F.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests membership of the final run state in F.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DFA-model"></a>

### model

`urn:csabs:axiom/DFA-model`

**statement:** The transition function is total on a finite state set and alphabet.

**description:** The transition function is total on a finite state set and alphabet.

**formalStatement:** Q finite ∧ Q≠∅; Σ finite; q₀∈Q; F⊆Q; δ:Q×Σ→Q

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Makes transition totality explicit; acceptance refers to the state reached after the entire word. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DFA-run"></a>

### run

`urn:csabs:axiom/DFA-run`

**statement:** The extended transition consumes symbols successively.

**description:** The extended transition consumes symbols successively.

**formalStatement:** δ̂(q,ε)=q; δ̂(q,wa)=δ(δ̂(q,w),a); accepts_M(w) iff δ̂(q₀,w)∈F

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Makes transition totality explicit; acceptance refers to the state reached after the entire word. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DFA-singleton-nfa-runs"></a>

### singleton-nfa-runs

`urn:csabs:law/DFA-singleton-nfa-runs`

**statement:** The singleton-transition NFA encoding has exactly the DFA run state after every word.

**description:** The singleton-transition NFA encoding has exactly the DFA run state after every word.

**formalStatement:** Δ(q,a)={δ(q,a)} ⇒ Δ̂({q},w)={δ̂(q,w)}

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on w. The base is the singleton start. The successor union over a singleton is the singleton transition of the unique current state.

**dependsOn:** [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run); [run](NFA.md#node-urn-csabs-axiom-NFA-run); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Theorems

<a id="node-urn-csabs-theorem-DFA-run-composition"></a>

### run-composition

`urn:csabs:theorem/DFA-run-composition`

**statement:** Running a concatenation is equivalent to running its two words in order.

**description:** Running a concatenation is equivalent to running its two words in order.

**formalStatement:** δ̂(q,uv)=δ̂(δ̂(q,u),v)

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant.

**ruleRole:** derived-result

**proofSketch:** Induct on the finite word v. The empty case uses the first equation; appending a symbol applies the step equation to the induction hypothesis.

**dependsOn:** [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-DFA-state-invariant"></a>

### state-invariant

`urn:csabs:theorem/DFA-state-invariant`

**statement:** A state predicate preserved by every input symbol holds after every finite word.

**description:** A state predicate preserved by every input symbol holds after every finite word.

**formalStatement:** P(q₀) ∧ (∀q,a:P(q)⇒P(δ(q,a))) ⇒ ∀w:P(δ̂(q₀,w))

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed. This is the deterministic singleton-transition instantiation of the NFA reachable-set invariant principle, with B={q:P(q)}; it does not assume automatic inheritance.

**provenanceKind:** derived

**proofSketch:** Induct on the input word. The empty word leaves q₀, and each appended symbol preserves P.

**dependsOn:** [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema); [reachable-set-invariant](NFA.md#node-urn-csabs-theorem-NFA-reachable-set-invariant); [singleton-nfa-runs](DFA.md#node-urn-csabs-law-DFA-singleton-nfa-runs)

<a id="node-urn-csabs-theorem-DFA-emptiness-reachability"></a>

### emptiness-reachability

`urn:csabs:theorem/DFA-emptiness-reachability`

**statement:** A DFA accepts some word exactly when an accepting state is reachable from its start.

**description:** A DFA accepts some word exactly when an accepting state is reachable from its start.

**formalStatement:** L(M)=∅ iff Reach(q₀)∩F=∅; Reach(q₀)={δ̂(q₀,w):w∈Σ*}

**assumptions:** Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Acceptance is exactly membership of a reached state in F. For decidability, search the finite directed graph with edges q→δ(q,a) from q₀; every discovered state has a witnessing word and every word run is covered. Empty alphabet leaves only q₀ reachable.

**dependsOn:** [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 7–8: finite automata, formal definition and computation

**sourceNote:** Makes transition totality explicit; acceptance refers to the state reached after the entire word.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DFA",
    "type": "Concept",
    "shortForm": "DFA",
    "fullName": "Deterministic finite automaton with total transition",
    "category": [
      "urn:csabs:category/languages-computation",
      "urn:csabs:category/behavior"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite-state recognizer with exactly one next state for every state and input symbol.",
    "notation": "M=(Q,Σ,δ,q₀,F); δ:Q×Σ→Q",
    "hasOperation": [
      "urn:csabs:operation/DFA-run",
      "urn:csabs:operation/DFA-accepts"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run"
    ],
    "hasLaw": [
      "urn:csabs:law/DFA-singleton-nfa-runs"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DFA-run-composition",
      "urn:csabs:theorem/DFA-state-invariant",
      "urn:csabs:theorem/DFA-emptiness-reachability"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FormalLanguage",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RegularLanguage",
      "urn:csabs:concept/NFA"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: The transition function is total on a finite state set and alphabet. The extended transition consumes symbols successively.",
    "basisKind": "defined-structure",
    "basisScope": "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages.",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Makes transition totality explicit; acceptance refers to the state reached after the entire word.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "specializationOf": [
      "urn:csabs:concept/NFA"
    ],
    "specializationNote": "Instantiate the NFA transition by singleton sets Δ(q,a)={δ(q,a)}. Singleton totality removes nondeterministic choices; start and acceptance data are unchanged. The underlying carriers are identified by this explicit encoding."
  },
  {
    "id": "urn:csabs:operation/DFA-run",
    "type": "Operation",
    "name": "run",
    "signature": "δ̂ : Q×Σ*→Q",
    "description": "Returns the unique state reached after consuming the word.",
    "concept": "urn:csabs:concept/DFA",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the unique state reached after consuming the word."
  },
  {
    "id": "urn:csabs:operation/DFA-accepts",
    "type": "Operation",
    "name": "accepts",
    "signature": "accepts_M : Σ*→Bool",
    "description": "Tests membership of the final run state in F.",
    "concept": "urn:csabs:concept/DFA",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests membership of the final run state in F."
  },
  {
    "id": "urn:csabs:axiom/DFA-model",
    "type": "Axiom",
    "name": "model",
    "statement": "The transition function is total on a finite state set and alphabet.",
    "description": "The transition function is total on a finite state set and alphabet.",
    "formalStatement": "Q finite ∧ Q≠∅; Σ finite; q₀∈Q; F⊆Q; δ:Q×Σ→Q",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Makes transition totality explicit; acceptance refers to the state reached after the entire word. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DFA-run",
    "type": "Axiom",
    "name": "run",
    "statement": "The extended transition consumes symbols successively.",
    "description": "The extended transition consumes symbols successively.",
    "formalStatement": "δ̂(q,ε)=q; δ̂(q,wa)=δ(δ̂(q,w),a); accepts_M(w) iff δ̂(q₀,w)∈F",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Makes transition totality explicit; acceptance refers to the state reached after the entire word. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DFA-singleton-nfa-runs",
    "type": "Law",
    "name": "singleton-nfa-runs",
    "statement": "The singleton-transition NFA encoding has exactly the DFA run state after every word.",
    "description": "The singleton-transition NFA encoding has exactly the DFA run state after every word.",
    "formalStatement": "Δ(q,a)={δ(q,a)} ⇒ Δ̂({q},w)={δ̂(q,w)}",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on w. The base is the singleton start. The successor union over a singleton is the singleton transition of the unique current state.",
    "dependsOn": [
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run",
      "urn:csabs:axiom/NFA-run",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/DFA-run-composition",
    "type": "Theorem",
    "name": "run-composition",
    "statement": "Running a concatenation is equivalent to running its two words in order.",
    "description": "Running a concatenation is equivalent to running its two words in order.",
    "formalStatement": "δ̂(q,uv)=δ̂(δ̂(q,u),v)",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Induct on the finite word v. The empty case uses the first equation; appending a symbol applies the step equation to the induction hypothesis.",
    "dependsOn": [
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/DFA-state-invariant",
    "type": "Theorem",
    "name": "state-invariant",
    "statement": "A state predicate preserved by every input symbol holds after every finite word.",
    "description": "A state predicate preserved by every input symbol holds after every finite word.",
    "formalStatement": "P(q₀) ∧ (∀q,a:P(q)⇒P(δ(q,a))) ⇒ ∀w:P(δ̂(q₀,w))",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed. This is the deterministic singleton-transition instantiation of the NFA reachable-set invariant principle, with B={q:P(q)}; it does not assume automatic inheritance.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on the input word. The empty word leaves q₀, and each appended symbol preserves P.",
    "dependsOn": [
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run",
      "urn:csabs:axiom/NaturalNumber-induction-schema",
      "urn:csabs:theorem/NFA-reachable-set-invariant",
      "urn:csabs:law/DFA-singleton-nfa-runs"
    ]
  },
  {
    "id": "urn:csabs:theorem/DFA-emptiness-reachability",
    "type": "Theorem",
    "name": "emptiness-reachability",
    "statement": "A DFA accepts some word exactly when an accepting state is reachable from its start.",
    "description": "A DFA accepts some word exactly when an accepting state is reachable from its start.",
    "formalStatement": "L(M)=∅ iff Reach(q₀)∩F=∅; Reach(q₀)={δ̂(q₀,w):w∈Σ*}",
    "assumptions": [
      "Q finite nonempty; Σ finite, possibly empty; q₀∈Q and F⊆Q. Empty word leaves the start state unchanged. Partial-transition devices require completion or a distinct variant. State and symbol equality is identity; machine equality is componentwise, not equality of accepted languages."
    ],
    "appliesTo": [
      "urn:csabs:concept/DFA"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 7–8: finite automata, formal definition and computation",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Acceptance is exactly membership of a reached state in F. For decidability, search the finite directed graph with edges q→δ(q,a) from q₀; every discovered state has a witnessing word and every word run is covered. Empty alphabet leaves only q₀ reachable.",
    "dependsOn": [
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run"
    ]
  }
]
```
<!-- graph-record:end -->
