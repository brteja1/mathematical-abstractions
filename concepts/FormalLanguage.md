# Formal language of finite words

An arbitrary set of finite words over a fixed finite alphabet. The set of words may itself be infinite.

**Notation:** Σ* = ⋃_{n≥0}Σⁿ; L⊆Σ*; ε∈Σ⁰

**Stable ID:** `urn:csabs:concept/FormalLanguage`

**Categories:** Languages and computation

**Kind:** Mathematical structure

**Prerequisites:** [Set](Set.md), [Finite sequence (List datatype)](Sequence.md)

**Specializes:** [Set](Set.md)

**Related concepts:** [Monoid](Monoid.md), [Regular language over a finite alphabet](RegularLanguage.md), [Context-free grammar of finite words](ContextFreeGrammar.md)

## Backlinks

- [Context-free grammar of finite words](ContextFreeGrammar.md) — `requiresConcept`
- [Deterministic finite automaton with total transition](DFA.md) — `requiresConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `requiresConcept`
- [Regular language over a finite alphabet](RegularLanguage.md) — `requiresConcept`
- [Regular language over a finite alphabet](RegularLanguage.md) — `specializationOf`
- [Finite sequence (List datatype)](Sequence.md) — `relatedConcept`
- [Set](Set.md) — `relatedConcept`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `relatedConcept`
- [Deterministic one-tape Turing machine](TuringMachine.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Languages are subsets of finite words. Concatenation and star use word concatenation and include the zero-factor word. Language union has ordinary word membership semantics.

**basisKind:** defined-structure

**basisScope:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**specializationNote:** Use Σ* as the parent element universe. Language union/intersection/difference and subset have set meanings; concatenation and star are additional operations on sets of words, not sequence concatenation on individual words.

**verificationObligation:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FormalLanguage-contains"></a>

### contains

`urn:csabs:operation/FormalLanguage-contains`

**signature:** contains : Lang(Σ)×Σ*→Prop

**description:** Tests word membership semantically.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests word membership semantically.

<a id="node-urn-csabs-operation-FormalLanguage-concatenate"></a>

### concatenate

`urn:csabs:operation/FormalLanguage-concatenate`

**signature:** · : Lang(Σ)×Lang(Σ)→Lang(Σ)

**description:** Forms all concatenations of one word from each operand.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Forms all concatenations of one word from each operand.

<a id="node-urn-csabs-operation-FormalLanguage-star"></a>

### star

`urn:csabs:operation/FormalLanguage-star`

**signature:** * : Lang(Σ)→Lang(Σ)

**description:** Forms concatenations of any finite number of operand words, including zero.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Forms concatenations of any finite number of operand words, including zero.

<a id="node-urn-csabs-operation-FormalLanguage-union"></a>

### union

`urn:csabs:operation/FormalLanguage-union`

**signature:** ∪ : Lang(Σ)×Lang(Σ)→Lang(Σ)

**description:** Returns set union over the fixed word universe.

**precondition:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**postcondition:** Returns set union over the fixed word universe.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FormalLanguage-language-equality"></a>

### language-equality

`urn:csabs:axiom/FormalLanguage-language-equality`

**statement:** Languages are subsets of finite words.

**description:** Languages are subsets of finite words.

**formalStatement:** Lang(Σ)=𝒫(Σ*); L=M iff ∀w∈Σ*:(w∈L↔w∈M); ε is the unique length-zero word

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Uses finite words and distinguishes ∅ from {ε}; operations have set semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FormalLanguage-language-operations"></a>

### language-operations

`urn:csabs:axiom/FormalLanguage-language-operations`

**statement:** Concatenation and star use word concatenation and include the zero-factor word.

**description:** Concatenation and star use word concatenation and include the zero-factor word.

**formalStatement:** LM={uv:u∈L,v∈M}; L⁰={ε}; Lⁿ⁺¹=LⁿL; L*=⋃_{n≥0}Lⁿ

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Uses finite words and distinguishes ∅ from {ε}; operations have set semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FormalLanguage-union-membership"></a>

### union-membership

`urn:csabs:axiom/FormalLanguage-union-membership`

**statement:** Language union has ordinary word membership semantics.

**description:** Language union has ordinary word membership semantics.

**formalStatement:** w∈L∪M iff w∈L∨w∈M

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, slide 10: regular language operations

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FormalLanguage-concatenation-monoid"></a>

### concatenation-monoid

`urn:csabs:law/FormalLanguage-concatenation-monoid`

**statement:** Language concatenation is associative with singleton empty-word identity.

**description:** Language concatenation is associative with singleton empty-word identity.

**formalStatement:** (LM)N=L(MN); {ε}L=L=L{ε}

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Membership in either association has three word factors. Word associativity rebrackets their concatenation; the empty word is a left and right word identity.

**dependsOn:** [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [union-membership](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-union-membership); [urn:csabs:law/sequence-concat-associative](Sequence.md#node-urn-csabs-law-sequence-concat-associative); [urn:csabs:law/sequence-empty-identity](Sequence.md#node-urn-csabs-law-sequence-empty-identity)

<a id="node-urn-csabs-law-FormalLanguage-distributivity-annihilation"></a>

### distributivity-annihilation

`urn:csabs:law/FormalLanguage-distributivity-annihilation`

**statement:** Language concatenation distributes over union and is annihilated by the empty language.

**description:** Language concatenation distributes over union and is annihilated by the empty language.

**formalStatement:** L(M∪N)=LM∪LN; (L∪M)N=LN∪MN; ∅L=∅=L∅

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Split the chosen word factor according to its union membership. A factor cannot be chosen from ∅, so the empty-factor products contain no words.

**dependsOn:** [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [union-membership](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-union-membership)

## Theorems

<a id="node-urn-csabs-theorem-FormalLanguage-empty-star"></a>

### empty-star

`urn:csabs:theorem/FormalLanguage-empty-star`

**statement:** The star of the empty language is the singleton empty word.

**description:** The star of the empty language is the singleton empty word.

**formalStatement:** ∅*={ε}

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** derived-result

**proofSketch:** The zero-factor case contributes ε. No positive-length list of factors can be chosen from ∅, so every other power is empty.

**dependsOn:** [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FormalLanguage-star-induction"></a>

### star-induction

`urn:csabs:theorem/FormalLanguage-star-induction`

**statement:** A language containing the empty word and closed under appending L contains L star.

**description:** A language containing the empty word and closed under appending L contains L star.

**formalStatement:** ε∈K ∧ KL⊆K ⇒ L*⊆K

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on the finite number of L factors. The zero-factor word belongs to K. Appending an L factor to a product already in K stays in K by KL⊆K. Union over all finite powers concludes.

**dependsOn:** [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [union-membership](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-union-membership); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema); [concatenation-monoid](FormalLanguage.md#node-urn-csabs-law-FormalLanguage-concatenation-monoid)

<a id="node-urn-csabs-theorem-FormalLanguage-star-idempotence"></a>

### star-idempotence

`urn:csabs:theorem/FormalLanguage-star-idempotence`

**statement:** Taking star twice yields the same language.

**description:** Taking star twice yields the same language.

**formalStatement:** (L*)*=L*

**assumptions:** Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** A finite concatenation of finite lists of L factors flattens to a finite list of L factors, giving the forward inclusion. Every L-star word is one factor in the outer star, giving the reverse inclusion.

**dependsOn:** [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality); [language-operations](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-operations); [union-membership](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-union-membership); [concatenation-monoid](FormalLanguage.md#node-urn-csabs-law-FormalLanguage-concatenation-monoid)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8 and 10: strings, languages, regular operations

**sourceNote:** Uses finite words and distinguishes ∅ from {ε}; operations have set semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FormalLanguage",
    "type": "Concept",
    "shortForm": "FormalLanguage",
    "fullName": "Formal language of finite words",
    "category": [
      "urn:csabs:category/languages-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "An arbitrary set of finite words over a fixed finite alphabet. The set of words may itself be infinite.",
    "notation": "Σ* = ⋃_{n≥0}Σⁿ; L⊆Σ*; ε∈Σ⁰",
    "hasOperation": [
      "urn:csabs:operation/FormalLanguage-contains",
      "urn:csabs:operation/FormalLanguage-concatenate",
      "urn:csabs:operation/FormalLanguage-star",
      "urn:csabs:operation/FormalLanguage-union"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership"
    ],
    "hasLaw": [
      "urn:csabs:law/FormalLanguage-concatenation-monoid",
      "urn:csabs:law/FormalLanguage-distributivity-annihilation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FormalLanguage-empty-star",
      "urn:csabs:theorem/FormalLanguage-star-induction",
      "urn:csabs:theorem/FormalLanguage-star-idempotence"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Monoid",
      "urn:csabs:concept/RegularLanguage",
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Languages are subsets of finite words. Concatenation and star use word concatenation and include the zero-factor word. Language union has ordinary word membership semantics.",
    "basisKind": "defined-structure",
    "basisScope": "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Uses finite words and distinguishes ∅ from {ε}; operations have set semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "specializationOf": [
      "urn:csabs:concept/Set"
    ],
    "specializationNote": "Use Σ* as the parent element universe. Language union/intersection/difference and subset have set meanings; concatenation and star are additional operations on sets of words, not sequence concatenation on individual words."
  },
  {
    "id": "urn:csabs:operation/FormalLanguage-contains",
    "type": "Operation",
    "name": "contains",
    "signature": "contains : Lang(Σ)×Σ*→Prop",
    "description": "Tests word membership semantically.",
    "concept": "urn:csabs:concept/FormalLanguage",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests word membership semantically."
  },
  {
    "id": "urn:csabs:operation/FormalLanguage-concatenate",
    "type": "Operation",
    "name": "concatenate",
    "signature": "· : Lang(Σ)×Lang(Σ)→Lang(Σ)",
    "description": "Forms all concatenations of one word from each operand.",
    "concept": "urn:csabs:concept/FormalLanguage",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Forms all concatenations of one word from each operand."
  },
  {
    "id": "urn:csabs:operation/FormalLanguage-star",
    "type": "Operation",
    "name": "star",
    "signature": "* : Lang(Σ)→Lang(Σ)",
    "description": "Forms concatenations of any finite number of operand words, including zero.",
    "concept": "urn:csabs:concept/FormalLanguage",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Forms concatenations of any finite number of operand words, including zero."
  },
  {
    "id": "urn:csabs:operation/FormalLanguage-union",
    "type": "Operation",
    "name": "union",
    "signature": "∪ : Lang(Σ)×Lang(Σ)→Lang(Σ)",
    "description": "Returns set union over the fixed word universe.",
    "concept": "urn:csabs:concept/FormalLanguage",
    "precondition": "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable.",
    "postcondition": "Returns set union over the fixed word universe.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/FormalLanguage-language-equality",
    "type": "Axiom",
    "name": "language-equality",
    "statement": "Languages are subsets of finite words.",
    "description": "Languages are subsets of finite words.",
    "formalStatement": "Lang(Σ)=𝒫(Σ*); L=M iff ∀w∈Σ*:(w∈L↔w∈M); ε is the unique length-zero word",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Uses finite words and distinguishes ∅ from {ε}; operations have set semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FormalLanguage-language-operations",
    "type": "Axiom",
    "name": "language-operations",
    "statement": "Concatenation and star use word concatenation and include the zero-factor word.",
    "description": "Concatenation and star use word concatenation and include the zero-factor word.",
    "formalStatement": "LM={uv:u∈L,v∈M}; L⁰={ε}; Lⁿ⁺¹=LⁿL; L*=⋃_{n≥0}Lⁿ",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Uses finite words and distinguishes ∅ from {ε}; operations have set semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FormalLanguage-union-membership",
    "type": "Axiom",
    "name": "union-membership",
    "statement": "Language union has ordinary word membership semantics.",
    "description": "Language union has ordinary word membership semantics.",
    "formalStatement": "w∈L∪M iff w∈L∨w∈M",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Lecture 1, slide 10: regular language operations",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FormalLanguage-concatenation-monoid",
    "type": "Law",
    "name": "concatenation-monoid",
    "statement": "Language concatenation is associative with singleton empty-word identity.",
    "description": "Language concatenation is associative with singleton empty-word identity.",
    "formalStatement": "(LM)N=L(MN); {ε}L=L=L{ε}",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Membership in either association has three word factors. Word associativity rebrackets their concatenation; the empty word is a left and right word identity.",
    "dependsOn": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership",
      "urn:csabs:law/sequence-concat-associative",
      "urn:csabs:law/sequence-empty-identity"
    ]
  },
  {
    "id": "urn:csabs:law/FormalLanguage-distributivity-annihilation",
    "type": "Law",
    "name": "distributivity-annihilation",
    "statement": "Language concatenation distributes over union and is annihilated by the empty language.",
    "description": "Language concatenation distributes over union and is annihilated by the empty language.",
    "formalStatement": "L(M∪N)=LM∪LN; (L∪M)N=LN∪MN; ∅L=∅=L∅",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Split the chosen word factor according to its union membership. A factor cannot be chosen from ∅, so the empty-factor products contain no words.",
    "dependsOn": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership"
    ]
  },
  {
    "id": "urn:csabs:theorem/FormalLanguage-empty-star",
    "type": "Theorem",
    "name": "empty-star",
    "statement": "The star of the empty language is the singleton empty word.",
    "description": "The star of the empty language is the singleton empty word.",
    "formalStatement": "∅*={ε}",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "The zero-factor case contributes ε. No positive-length list of factors can be chosen from ∅, so every other power is empty.",
    "dependsOn": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FormalLanguage-star-induction",
    "type": "Theorem",
    "name": "star-induction",
    "statement": "A language containing the empty word and closed under appending L contains L star.",
    "description": "A language containing the empty word and closed under appending L contains L star.",
    "formalStatement": "ε∈K ∧ KL⊆K ⇒ L*⊆K",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on the finite number of L factors. The zero-factor word belongs to K. Appending an L factor to a product already in K stays in K by KL⊆K. Union over all finite powers concludes.",
    "dependsOn": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership",
      "urn:csabs:axiom/NaturalNumber-induction-schema",
      "urn:csabs:law/FormalLanguage-concatenation-monoid"
    ]
  },
  {
    "id": "urn:csabs:theorem/FormalLanguage-star-idempotence",
    "type": "Theorem",
    "name": "star-idempotence",
    "statement": "Taking star twice yields the same language.",
    "description": "Taking star twice yields the same language.",
    "formalStatement": "(L*)*=L*",
    "assumptions": [
      "Σ is finite and may be empty. Word equality is positional and language equality is extensional. Membership is a predicate; arbitrary language membership is not promised decidable."
    ],
    "appliesTo": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8 and 10: strings, languages, regular operations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "A finite concatenation of finite lists of L factors flattens to a finite list of L factors, giving the forward inclusion. Every L-star word is one factor in the outer star, giving the reverse inclusion.",
    "dependsOn": [
      "urn:csabs:axiom/FormalLanguage-language-equality",
      "urn:csabs:axiom/FormalLanguage-language-operations",
      "urn:csabs:axiom/FormalLanguage-union-membership",
      "urn:csabs:law/FormalLanguage-concatenation-monoid"
    ]
  }
]
```
<!-- graph-record:end -->
