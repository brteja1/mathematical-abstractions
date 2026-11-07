# Context-free grammar of finite words

Finite productions replace one nonterminal by a finite word of terminals and nonterminals; generated terminal words define the language.

**Notation:** G=(V,Σ,P,S); P⊆V×(V∪Σ)* finite; L(G)={w∈Σ*:S⇒*w}

**Stable ID:** `urn:csabs:concept/ContextFreeGrammar`

**Categories:** Languages and computation

**Kind:** semantic-model

**Prerequisites:** [Formal language of finite words](FormalLanguage.md), [Transition System](TransitionSystem.md)

**Related concepts:** [Regular language over a finite alphabet](RegularLanguage.md)

## Backlinks

- [Formal language of finite words](FormalLanguage.md) — `relatedConcept`
- [Regular language over a finite alphabet](RegularLanguage.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Each rule has a single nonterminal left side and a finite string right side. Rules act inside any context; generation uses reflexive transitive closure.

**basisKind:** defined-structure

**basisScope:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**verificationObligation:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ContextFreeGrammar-deriveOne"></a>

### deriveOne

`urn:csabs:operation/ContextFreeGrammar-deriveOne`

**signature:** ⇒_G : (V∪Σ)*×(V∪Σ)*→Prop

**description:** Relates sentential forms differing by one production application.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Relates sentential forms differing by one production application.

<a id="node-urn-csabs-operation-ContextFreeGrammar-generates"></a>

### generates

`urn:csabs:operation/ContextFreeGrammar-generates`

**signature:** generates_G : Σ*→Prop

**description:** Holds for terminal words reached by a finite derivation; not a promise that arbitrary derivation search terminates.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Holds for terminal words reached by a finite derivation; not a promise that arbitrary derivation search terminates.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ContextFreeGrammar-productions"></a>

### productions

`urn:csabs:axiom/ContextFreeGrammar-productions`

**statement:** Each rule has a single nonterminal left side and a finite string right side.

**description:** Each rule has a single nonterminal left side and a finite string right side.

**formalStatement:** V∩Σ=∅; V,Σ,P finite; S∈V; P⊆V×(V∪Σ)*

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Uses unrestricted context-free right-hand sides, including ε, and finite derivations. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ContextFreeGrammar-derivations"></a>

### derivations

`urn:csabs:axiom/ContextFreeGrammar-derivations`

**statement:** Rules act inside any context; generation uses reflexive transitive closure.

**description:** Rules act inside any context; generation uses reflexive transitive closure.

**formalStatement:** x⇒y iff ∃u,v∈(V∪Σ)*, A∈V, α∈(V∪Σ)*: x=uAv ∧ y=uαv ∧ (A,α)∈P; ⇒* is finite reflexive transitive closure of ⇒; w∈L(G) iff w∈Σ* ∧ S⇒*w

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Uses unrestricted context-free right-hand sides, including ε, and finite derivations. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ContextFreeGrammar-context-closure"></a>

### context-closure

`urn:csabs:law/ContextFreeGrammar-context-closure`

**statement:** A finite derivation can be placed inside any unchanged left and right contexts.

**description:** A finite derivation can be placed inside any unchanged left and right contexts.

**formalStatement:** x⇒*y ⇒ uxv⇒*uyv

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on the number of derivation steps. Zero steps preserve the contexts. Each one-step replacement remains a legal replacement when prefixed by u and suffixed by v.

**dependsOn:** [productions](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-productions); [derivations](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-derivations); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Theorems

<a id="node-urn-csabs-theorem-ContextFreeGrammar-empty-derivation"></a>

### empty-derivation

`urn:csabs:theorem/ContextFreeGrammar-empty-derivation`

**statement:** An explicit start-to-empty production makes the empty word part of the language.

**description:** An explicit start-to-empty production makes the empty word part of the language.

**formalStatement:** (S,ε)∈P⇒ε∈L(G)

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** derived-result

**proofSketch:** Apply the production in the empty left and right contexts. One step is a finite derivation and ε is a terminal word.

**dependsOn:** [productions](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-productions); [derivations](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-derivations)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-ContextFreeGrammar-derivation-induction"></a>

### derivation-induction

`urn:csabs:theorem/ContextFreeGrammar-derivation-induction`

**statement:** A predicate holding at a chosen initial sentential form and preserved by one-step derivation holds at every form derivable from it.

**description:** A predicate holding at a chosen initial sentential form and preserved by one-step derivation holds at every form derivable from it.

**formalStatement:** P(x₀) ∧ (∀x,y:P(x)∧x⇒y⇒P(y)) ⇒ ∀z:(x₀⇒*z⇒P(z))

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on the finite derivation length, using reflexivity for the zero-step case and preservation for the last production application.

**dependsOn:** [productions](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-productions); [derivations](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-derivations); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

<a id="node-urn-csabs-theorem-ContextFreeGrammar-rule-monotonicity"></a>

### rule-monotonicity

`urn:csabs:theorem/ContextFreeGrammar-rule-monotonicity`

**statement:** Adding productions over the same symbol sets cannot remove generated words.

**description:** Adding productions over the same symbol sets cannot remove generated words.

**formalStatement:** P_G⊆P_H ∧ V_G=V_H ∧ Σ_G=Σ_H ∧ S_G=S_H ⇒ L(G)⊆L(H)

**assumptions:** V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Every G production step is an H step. Reuse any finite G derivation of a terminal word as an H derivation.

**dependsOn:** [productions](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-productions); [derivations](ContextFreeGrammar.md#node-urn-csabs-axiom-ContextFreeGrammar-derivations)

## Concept provenance

- [Michael Sipser: MIT 18.404J (Fall 2020), Lecture 4](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/a22fce6f6824c53dbb79a0da786966a6_MIT18_404f20_lec4.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Slide 3: CFG formal definition and derivations

**sourceNote:** Uses unrestricted context-free right-hand sides, including ε, and finite derivations.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ContextFreeGrammar",
    "type": "Concept",
    "shortForm": "ContextFreeGrammar",
    "fullName": "Context-free grammar of finite words",
    "category": [
      "urn:csabs:category/languages-computation"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "Finite productions replace one nonterminal by a finite word of terminals and nonterminals; generated terminal words define the language.",
    "notation": "G=(V,Σ,P,S); P⊆V×(V∪Σ)* finite; L(G)={w∈Σ*:S⇒*w}",
    "hasOperation": [
      "urn:csabs:operation/ContextFreeGrammar-deriveOne",
      "urn:csabs:operation/ContextFreeGrammar-generates"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ContextFreeGrammar-productions",
      "urn:csabs:axiom/ContextFreeGrammar-derivations"
    ],
    "hasLaw": [
      "urn:csabs:law/ContextFreeGrammar-context-closure"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/ContextFreeGrammar-empty-derivation",
      "urn:csabs:theorem/ContextFreeGrammar-derivation-induction",
      "urn:csabs:theorem/ContextFreeGrammar-rule-monotonicity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/FormalLanguage",
      "urn:csabs:concept/TransitionSystem"
    ],
    "relatedConcept": [
      "urn:csabs:concept/RegularLanguage"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Each rule has a single nonterminal left side and a finite string right side. Rules act inside any context; generation uses reflexive transitive closure.",
    "basisKind": "defined-structure",
    "basisScope": "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed.",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Uses unrestricted context-free right-hand sides, including ε, and finite derivations.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ]
  },
  {
    "id": "urn:csabs:operation/ContextFreeGrammar-deriveOne",
    "type": "Operation",
    "name": "deriveOne",
    "signature": "⇒_G : (V∪Σ)*×(V∪Σ)*→Prop",
    "description": "Relates sentential forms differing by one production application.",
    "concept": "urn:csabs:concept/ContextFreeGrammar",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Relates sentential forms differing by one production application."
  },
  {
    "id": "urn:csabs:operation/ContextFreeGrammar-generates",
    "type": "Operation",
    "name": "generates",
    "signature": "generates_G : Σ*→Prop",
    "description": "Holds for terminal words reached by a finite derivation; not a promise that arbitrary derivation search terminates.",
    "concept": "urn:csabs:concept/ContextFreeGrammar",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Holds for terminal words reached by a finite derivation; not a promise that arbitrary derivation search terminates."
  },
  {
    "id": "urn:csabs:axiom/ContextFreeGrammar-productions",
    "type": "Axiom",
    "name": "productions",
    "statement": "Each rule has a single nonterminal left side and a finite string right side.",
    "description": "Each rule has a single nonterminal left side and a finite string right side.",
    "formalStatement": "V∩Σ=∅; V,Σ,P finite; S∈V; P⊆V×(V∪Σ)*",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Uses unrestricted context-free right-hand sides, including ε, and finite derivations. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ContextFreeGrammar-derivations",
    "type": "Axiom",
    "name": "derivations",
    "statement": "Rules act inside any context; generation uses reflexive transitive closure.",
    "description": "Rules act inside any context; generation uses reflexive transitive closure.",
    "formalStatement": "x⇒y iff ∃u,v∈(V∪Σ)*, A∈V, α∈(V∪Σ)*: x=uAv ∧ y=uαv ∧ (A,α)∈P; ⇒* is finite reflexive transitive closure of ⇒; w∈L(G) iff w∈Σ* ∧ S⇒*w",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Uses unrestricted context-free right-hand sides, including ε, and finite derivations. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ContextFreeGrammar-context-closure",
    "type": "Law",
    "name": "context-closure",
    "statement": "A finite derivation can be placed inside any unchanged left and right contexts.",
    "description": "A finite derivation can be placed inside any unchanged left and right contexts.",
    "formalStatement": "x⇒*y ⇒ uxv⇒*uyv",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on the number of derivation steps. Zero steps preserve the contexts. Each one-step replacement remains a legal replacement when prefixed by u and suffixed by v.",
    "dependsOn": [
      "urn:csabs:axiom/ContextFreeGrammar-productions",
      "urn:csabs:axiom/ContextFreeGrammar-derivations",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/ContextFreeGrammar-empty-derivation",
    "type": "Theorem",
    "name": "empty-derivation",
    "statement": "An explicit start-to-empty production makes the empty word part of the language.",
    "description": "An explicit start-to-empty production makes the empty word part of the language.",
    "formalStatement": "(S,ε)∈P⇒ε∈L(G)",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Apply the production in the empty left and right contexts. One step is a finite derivation and ε is a terminal word.",
    "dependsOn": [
      "urn:csabs:axiom/ContextFreeGrammar-productions",
      "urn:csabs:axiom/ContextFreeGrammar-derivations"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/ContextFreeGrammar-derivation-induction",
    "type": "Theorem",
    "name": "derivation-induction",
    "statement": "A predicate holding at a chosen initial sentential form and preserved by one-step derivation holds at every form derivable from it.",
    "description": "A predicate holding at a chosen initial sentential form and preserved by one-step derivation holds at every form derivable from it.",
    "formalStatement": "P(x₀) ∧ (∀x,y:P(x)∧x⇒y⇒P(y)) ⇒ ∀z:(x₀⇒*z⇒P(z))",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on the finite derivation length, using reflexivity for the zero-step case and preservation for the last production application.",
    "dependsOn": [
      "urn:csabs:axiom/ContextFreeGrammar-productions",
      "urn:csabs:axiom/ContextFreeGrammar-derivations",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  },
  {
    "id": "urn:csabs:theorem/ContextFreeGrammar-rule-monotonicity",
    "type": "Theorem",
    "name": "rule-monotonicity",
    "statement": "Adding productions over the same symbol sets cannot remove generated words.",
    "description": "Adding productions over the same symbol sets cannot remove generated words.",
    "formalStatement": "P_G⊆P_H ∧ V_G=V_H ∧ Σ_G=Σ_H ∧ S_G=S_H ⇒ L(G)⊆L(H)",
    "assumptions": [
      "V and Σ finite and disjoint; S∈V. Empty productions, ambiguity, left recursion and nonproductive grammars are allowed. No parsing strategy or unique derivation is assumed."
    ],
    "appliesTo": [
      "urn:csabs:concept/ContextFreeGrammar"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sipser-cfg"
    ],
    "sourceLocator": "Slide 3: CFG formal definition and derivations",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Every G production step is an H step. Reuse any finite G derivation of a terminal word as an H derivation.",
    "dependsOn": [
      "urn:csabs:axiom/ContextFreeGrammar-productions",
      "urn:csabs:axiom/ContextFreeGrammar-derivations"
    ]
  }
]
```
<!-- graph-record:end -->
