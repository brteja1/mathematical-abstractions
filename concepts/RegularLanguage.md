# Regular language over a finite alphabet

A language recognized by some deterministic finite automaton over the same alphabet.

**Notation:** Reg(Σ)={L⊆Σ*:∃DFA M over Σ,L=L(M)}

**Stable ID:** `urn:csabs:concept/RegularLanguage`

**Categories:** Languages and computation

**Kind:** Mathematical structure

**Prerequisites:** [Formal language of finite words](FormalLanguage.md), [Deterministic finite automaton with total transition](DFA.md)

**Specializes:** [Formal language of finite words](FormalLanguage.md)

**Related concepts:** [Nondeterministic finite automaton without epsilon moves](NFA.md), [Context-free grammar of finite words](ContextFreeGrammar.md)

## Backlinks

- [Context-free grammar of finite words](ContextFreeGrammar.md) — `relatedConcept`
- [Deterministic finite automaton with total transition](DFA.md) — `relatedConcept`
- [Formal language of finite words](FormalLanguage.md) — `relatedConcept`
- [Nondeterministic finite automaton without epsilon moves](NFA.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Regularity means the existence of a DFA recognizing exactly the language.

**basisKind:** defined-structure

**basisScope:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**specializationNote:** Restrict the parent carrier Lang(Σ) to languages with a DFA witness. Word membership and extensional language equality are unchanged. Closure of particular operations must be proved explicitly.

**verificationObligation:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RegularLanguage-union"></a>

### union

`urn:csabs:operation/RegularLanguage-union`

**signature:** ∪ : Reg(Σ)×Reg(Σ)→Reg(Σ)

**description:** Uses ordinary language union; regular closure is justified by the product construction.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Uses ordinary language union; regular closure is justified by the product construction.

<a id="node-urn-csabs-operation-RegularLanguage-intersection"></a>

### intersection

`urn:csabs:operation/RegularLanguage-intersection`

**signature:** ∩ : Reg(Σ)×Reg(Σ)→Reg(Σ)

**description:** Returns language intersection, using a product DFA witness.

**precondition:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**postcondition:** Returns language intersection, using a product DFA witness.

**totality:** total mathematical operation on the stated domain

<a id="node-urn-csabs-operation-RegularLanguage-complement"></a>

### complement

`urn:csabs:operation/RegularLanguage-complement`

**signature:** complement_Σ : Reg(Σ)→Reg(Σ)

**description:** Returns Σ* minus the language; total DFA transition is essential to the witness construction.

**precondition:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**postcondition:** Returns Σ* minus the language; total DFA transition is essential to the witness construction.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RegularLanguage-dfa-witness"></a>

### dfa-witness

`urn:csabs:axiom/RegularLanguage-dfa-witness`

**statement:** Regularity means the existence of a DFA recognizing exactly the language.

**description:** Regularity means the existence of a DFA recognizing exactly the language.

**formalStatement:** L∈Reg(Σ) iff ∃M∈DFA(Σ):∀w∈Σ*:(w∈L↔accepts(M,w))

**assumptions:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8–11: definition of regularity and product construction

**sourceNote:** Uses existence of a DFA as the defining basis; closure is a derived result, not a substitute definition. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RegularLanguage-double-complement"></a>

### double-complement

`urn:csabs:law/RegularLanguage-double-complement`

**statement:** Complementing a regular language twice restores it.

**description:** Complementing a regular language twice restores it.

**formalStatement:** complement_Σ(complement_Σ(L))=L

**assumptions:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8–11: definition of regularity and product construction

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Boolean closure ensures both complements stay in Reg(Σ); ordinary set membership double negation gives extensional equality.

**dependsOn:** [dfa-witness](RegularLanguage.md#node-urn-csabs-axiom-RegularLanguage-dfa-witness); [boolean-closure](RegularLanguage.md#node-urn-csabs-theorem-RegularLanguage-boolean-closure); [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality)

## Theorems

<a id="node-urn-csabs-theorem-RegularLanguage-union-closure"></a>

### union-closure

`urn:csabs:theorem/RegularLanguage-union-closure`

**statement:** The union of two regular languages is regular.

**description:** The union of two regular languages is regular.

**formalStatement:** L₁,L₂∈Reg(Σ)⇒L₁∪L₂∈Reg(Σ)

**assumptions:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**ruleRole:** derived-result

**proofSketch:** Given DFA witnesses, use states Q₁×Q₂, componentwise transition, start (q₁,q₂), and accepting pairs with at least one accepting component. Induction on the word shows each component matches its witness run.

**dependsOn:** [dfa-witness](RegularLanguage.md#node-urn-csabs-axiom-RegularLanguage-dfa-witness); [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8–11: definition of regularity and product construction

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-RegularLanguage-boolean-closure"></a>

### boolean-closure

`urn:csabs:theorem/RegularLanguage-boolean-closure`

**statement:** Regular languages are closed under intersection and fixed-alphabet complement.

**description:** Regular languages are closed under intersection and fixed-alphabet complement.

**formalStatement:** L,M∈Reg(Σ) ⇒ L∩M∈Reg(Σ) ∧ (Σ*∖L)∈Reg(Σ)

**assumptions:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Lecture 1, DFA semantics and product construction, slides 7–11; derived accepting-set variants

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** For intersection, use componentwise product DFA states and accepting pairs in F_L×F_M. For complement, keep the total DFA and replace F by Q∖F. Every finite word has exactly one final state, so acceptance is negated.

**dependsOn:** [dfa-witness](RegularLanguage.md#node-urn-csabs-axiom-RegularLanguage-dfa-witness); [model](DFA.md#node-urn-csabs-axiom-DFA-model); [run](DFA.md#node-urn-csabs-axiom-DFA-run); [run-composition](DFA.md#node-urn-csabs-theorem-DFA-run-composition)

<a id="node-urn-csabs-theorem-RegularLanguage-extensional-transfer"></a>

### extensional-transfer

`urn:csabs:theorem/RegularLanguage-extensional-transfer`

**statement:** A language equal to a regular language is regular with the same witness.

**description:** A language equal to a regular language is regular with the same witness.

**formalStatement:** L=M ∧ L∈Reg(Σ) ⇒ M∈Reg(Σ)

**assumptions:** Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8–11: definition of regularity and product construction

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** A DFA accepting exactly L accepts exactly M by extensional equality. Reuse that witness.

**dependsOn:** [dfa-witness](RegularLanguage.md#node-urn-csabs-axiom-RegularLanguage-dfa-witness); [language-equality](FormalLanguage.md#node-urn-csabs-axiom-FormalLanguage-language-equality)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/b4d9bf1573dccea21bee82cfba4224d4_MIT18_404f20_lec1.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slides 8–11: definition of regularity and product construction

**sourceNote:** Uses existence of a DFA as the defining basis; closure is a derived result, not a substitute definition.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RegularLanguage",
    "type": "Concept",
    "shortForm": "RegularLanguage",
    "fullName": "Regular language over a finite alphabet",
    "category": [
      "urn:csabs:category/languages-computation"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A language recognized by some deterministic finite automaton over the same alphabet.",
    "notation": "Reg(Σ)={L⊆Σ*:∃DFA M over Σ,L=L(M)}",
    "hasOperation": [
      "urn:csabs:operation/RegularLanguage-union",
      "urn:csabs:operation/RegularLanguage-intersection",
      "urn:csabs:operation/RegularLanguage-complement"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RegularLanguage-dfa-witness"
    ],
    "hasLaw": [
      "urn:csabs:law/RegularLanguage-double-complement"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RegularLanguage-union-closure",
      "urn:csabs:theorem/RegularLanguage-boolean-closure",
      "urn:csabs:theorem/RegularLanguage-extensional-transfer"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FormalLanguage",
      "urn:csabs:concept/DFA"
    ],
    "relatedConcept": [
      "urn:csabs:concept/NFA",
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Regularity means the existence of a DFA recognizing exactly the language.",
    "basisKind": "defined-structure",
    "basisScope": "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8–11: definition of regularity and product construction",
    "sourceNote": "Uses existence of a DFA as the defining basis; closure is a derived result, not a substitute definition.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "specializationOf": [
      "urn:csabs:concept/FormalLanguage"
    ],
    "specializationNote": "Restrict the parent carrier Lang(Σ) to languages with a DFA witness. Word membership and extensional language equality are unchanged. Closure of particular operations must be proved explicitly."
  },
  {
    "id": "urn:csabs:operation/RegularLanguage-union",
    "type": "Operation",
    "name": "union",
    "signature": "∪ : Reg(Σ)×Reg(Σ)→Reg(Σ)",
    "description": "Uses ordinary language union; regular closure is justified by the product construction.",
    "concept": "urn:csabs:concept/RegularLanguage",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Uses ordinary language union; regular closure is justified by the product construction."
  },
  {
    "id": "urn:csabs:operation/RegularLanguage-intersection",
    "type": "Operation",
    "name": "intersection",
    "signature": "∩ : Reg(Σ)×Reg(Σ)→Reg(Σ)",
    "description": "Returns language intersection, using a product DFA witness.",
    "concept": "urn:csabs:concept/RegularLanguage",
    "precondition": "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.",
    "postcondition": "Returns language intersection, using a product DFA witness.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:operation/RegularLanguage-complement",
    "type": "Operation",
    "name": "complement",
    "signature": "complement_Σ : Reg(Σ)→Reg(Σ)",
    "description": "Returns Σ* minus the language; total DFA transition is essential to the witness construction.",
    "concept": "urn:csabs:concept/RegularLanguage",
    "precondition": "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular.",
    "postcondition": "Returns Σ* minus the language; total DFA transition is essential to the witness construction.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/RegularLanguage-dfa-witness",
    "type": "Axiom",
    "name": "dfa-witness",
    "statement": "Regularity means the existence of a DFA recognizing exactly the language.",
    "description": "Regularity means the existence of a DFA recognizing exactly the language.",
    "formalStatement": "L∈Reg(Σ) iff ∃M∈DFA(Σ):∀w∈Σ*:(w∈L↔accepts(M,w))",
    "assumptions": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8–11: definition of regularity and product construction",
    "sourceNote": "Uses existence of a DFA as the defining basis; closure is a derived result, not a substitute definition. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RegularLanguage-double-complement",
    "type": "Law",
    "name": "double-complement",
    "statement": "Complementing a regular language twice restores it.",
    "description": "Complementing a regular language twice restores it.",
    "formalStatement": "complement_Σ(complement_Σ(L))=L",
    "assumptions": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8–11: definition of regularity and product construction",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Boolean closure ensures both complements stay in Reg(Σ); ordinary set membership double negation gives extensional equality.",
    "dependsOn": [
      "urn:csabs:axiom/RegularLanguage-dfa-witness",
      "urn:csabs:theorem/RegularLanguage-boolean-closure",
      "urn:csabs:axiom/FormalLanguage-language-equality"
    ]
  },
  {
    "id": "urn:csabs:theorem/RegularLanguage-union-closure",
    "type": "Theorem",
    "name": "union-closure",
    "statement": "The union of two regular languages is regular.",
    "description": "The union of two regular languages is regular.",
    "formalStatement": "L₁,L₂∈Reg(Σ)⇒L₁∪L₂∈Reg(Σ)",
    "assumptions": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Given DFA witnesses, use states Q₁×Q₂, componentwise transition, start (q₁,q₂), and accepting pairs with at least one accepting component. Induction on the word shows each component matches its witness run.",
    "dependsOn": [
      "urn:csabs:axiom/RegularLanguage-dfa-witness",
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8–11: definition of regularity and product construction",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RegularLanguage-boolean-closure",
    "type": "Theorem",
    "name": "boolean-closure",
    "statement": "Regular languages are closed under intersection and fixed-alphabet complement.",
    "description": "Regular languages are closed under intersection and fixed-alphabet complement.",
    "formalStatement": "L,M∈Reg(Σ) ⇒ L∩M∈Reg(Σ) ∧ (Σ*∖L)∈Reg(Σ)",
    "assumptions": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Lecture 1, DFA semantics and product construction, slides 7–11; derived accepting-set variants",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "For intersection, use componentwise product DFA states and accepting pairs in F_L×F_M. For complement, keep the total DFA and replace F by Q∖F. Every finite word has exactly one final state, so acceptance is negated.",
    "dependsOn": [
      "urn:csabs:axiom/RegularLanguage-dfa-witness",
      "urn:csabs:axiom/DFA-model",
      "urn:csabs:axiom/DFA-run",
      "urn:csabs:theorem/DFA-run-composition"
    ]
  },
  {
    "id": "urn:csabs:theorem/RegularLanguage-extensional-transfer",
    "type": "Theorem",
    "name": "extensional-transfer",
    "statement": "A language equal to a regular language is regular with the same witness.",
    "description": "A language equal to a regular language is regular with the same witness.",
    "formalStatement": "L=M ∧ L∈Reg(Σ) ⇒ M∈Reg(Σ)",
    "assumptions": [
      "Finite fixed alphabet; finite words including ε. Automaton witnesses are representations rather than languages themselves. An empty language and a singleton empty word are both regular."
    ],
    "appliesTo": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-automata"
    ],
    "sourceLocator": "Slides 8–11: definition of regularity and product construction",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "A DFA accepting exactly L accepts exactly M by extensional equality. Reuse that witness.",
    "dependsOn": [
      "urn:csabs:axiom/RegularLanguage-dfa-witness",
      "urn:csabs:axiom/FormalLanguage-language-equality"
    ]
  }
]
```
<!-- graph-record:end -->
