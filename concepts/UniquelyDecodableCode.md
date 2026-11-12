# Uniquely decodable binary source code

Symbol encoding whose concatenation extension is injective on finite source strings.

**Notation:** f:M→{0,1}⁺; f*:M*→{0,1}*

**Stable ID:** `urn:csabs:concept/UniquelyDecodableCode`

**Categories:** Information theory → Coding theory → Source coding

**Kind:** Mathematical structure

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Total function](Function.md)

## Backlinks

- [Prefix-free binary source code](PrefixFreeCode.md) — `requiresConcept`
- [Prefix-free binary source code](PrefixFreeCode.md) — `specializationOf`

## Mathematical formulation

A binary code f:M→{0,1}\* has positive word lengths and injective extension f\*:M\*→{0,1}\*, where f\* concatenates codewords. Thus f\*(s)=f\*(t)⇒s=t for every pair of finite message sequences.

**Lean formulation** (in its source module context):

```lean
abbrev UniquelyDecodableCode := Information.UniqueCode
```

**Source:** [`Catalog.UniquelyDecodableCode`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** M→List Bool with nonempty words and injective flatMap concatenation on List M; word equality.

**Limits:** Decoding inverse and expected-length operation omitted; no Kraft witness. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-UniquelyDecodableCode-extend"></a>

### extend

`urn:csabs:operation/UniquelyDecodableCode-extend`

**signature:** extend : Code(M)×M* → {0,1}*

**description:** Concatenate symbol codewords, mapping the empty message string to the empty bit string.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Concatenate symbol codewords, mapping the empty message string to the empty bit string.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-UniquelyDecodableCode-expected-length"></a>

### expected-length

`urn:csabs:operation/UniquelyDecodableCode-expected-length`

**signature:** L : Code(M)×Dist(M) → ℝ

**description:** L(f,p)=Σm p(m)|f(m)|, measured in bits per source symbol.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** L(f,p)=Σm p(m)|f(m)|, measured in bits per source symbol.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-UniquelyDecodableCode-unique-concatenation"></a>

### unique-concatenation

`urn:csabs:axiom/UniquelyDecodableCode-unique-concatenation`

**statement:** f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.

**formalStatement:** f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-UniquelyDecodableCode-kraft-mcmillan"></a>

### Kraft–McMillan theorem

`urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan`

**statement:** For every uniquely decodable binary code, Σm 2^(−|f(m)|)≤1. Conversely any finite assignment of positive integer lengths ℓm with Σm 2^(−ℓm)≤1 is realized by a prefix-free binary code.

**formalStatement:** For every uniquely decodable binary code, Σm 2^(−|f(m)|)≤1. Conversely any finite assignment of positive integer lengths ℓm with Σm 2^(−ℓm)≤1 is realized by a prefix-free binary code.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction.

**dependsOn:** [unique-concatenation](UniquelyDecodableCode.md#node-urn-csabs-axiom-UniquelyDecodableCode-unique-concatenation)

**proofSketch:** For necessity count distinct concatenations of r codewords by total bit length and let r grow (McMillan). For sufficiency allocate disjoint dyadic intervals of the requested lengths in a binary prefix tree.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 6.5

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-PrefixFreeCode-source-length"></a>

### Shannon expected-length bounds

`urn:csabs:theorem/PrefixFreeCode-source-length`

**statement:** For p(m)>0 on finite M, every uniquely decodable f has H(p)≤L(f,p). There exists a prefix-free f with L(f,p)≤H(p)+1; if |M|≥2 this can be strengthened to L(f,p)<H(p)+1.

**formalStatement:** For p(m)>0 on finite M, every uniquely decodable f has H(p)≤L(f,p). There exists a prefix-free f with L(f,p)≤H(p)+1; if |M|≥2 this can be strengthened to L(f,p)<H(p)+1.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.; p has full support on the chosen source alphabet; singleton source uses a positive one-bit word.

**dependsOn:** [Kraft–McMillan theorem](UniquelyDecodableCode.md#node-urn-csabs-theorem-UniquelyDecodableCode-kraft-mcmillan); [Gibbs inequality](RelativeEntropy.md#node-urn-csabs-theorem-RelativeEntropy-gibbs); [entropy-equation](ShannonEntropy.md#node-urn-csabs-axiom-ShannonEntropy-entropy-equation)

**proofSketch:** Normalize the Kraft weights and apply Gibbs for the lower bound. For |M|≥2 choose ℓm=ceil(−log₂p(m)) and apply Kraft; for a singleton choose a one-bit word.

**reviewStatus:** Editorial proof sketch; no registered Lean theorem witness.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** Theorem 6.6; positive-length singleton convention stated explicitly

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

## Concept provenance

- [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/UniquelyDecodableCode",
    "type": "Concept",
    "shortForm": "UniquelyDecodableCode",
    "fullName": "Uniquely decodable binary source code",
    "category": [
      "urn:csabs:category/source-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Symbol encoding whose concatenation extension is injective on finite source strings.",
    "notation": "f:M→{0,1}⁺; f*:M*→{0,1}*",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/UniquelyDecodableCode-extend",
      "urn:csabs:operation/UniquelyDecodableCode-expected-length"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/UniquelyDecodableCode-unique-concatenation"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan",
      "urn:csabs:theorem/PrefixFreeCode-source-length"
    ],
    "axiomBasis": "f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "leanFormulation": "abbrev UniquelyDecodableCode := Information.UniqueCode",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.UniquelyDecodableCode",
    "formulationScope": "partial",
    "leanModelMapping": "M→List Bool with nonempty words and injective flatMap concatenation on List M; word equality.",
    "leanModelLimitations": "Decoding inverse and expected-length operation omitted; no Kraft witness. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "A binary code f:M→{0,1}* has positive word lengths and injective extension f*:M*→{0,1}*, where f* concatenates codewords. Thus f*(s)=f*(t)⇒s=t for every pair of finite message sequences."
  },
  {
    "id": "urn:csabs:operation/UniquelyDecodableCode-extend",
    "type": "Operation",
    "name": "extend",
    "signature": "extend : Code(M)×M* → {0,1}*",
    "description": "Concatenate symbol codewords, mapping the empty message string to the empty bit string.",
    "concept": "urn:csabs:concept/UniquelyDecodableCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Concatenate symbol codewords, mapping the empty message string to the empty bit string.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/UniquelyDecodableCode-expected-length",
    "type": "Operation",
    "name": "expected-length",
    "signature": "L : Code(M)×Dist(M) → ℝ",
    "description": "L(f,p)=Σm p(m)|f(m)|, measured in bits per source symbol.",
    "concept": "urn:csabs:concept/UniquelyDecodableCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "L(f,p)=Σm p(m)|f(m)|, measured in bits per source symbol.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/UniquelyDecodableCode-unique-concatenation",
    "type": "Axiom",
    "name": "unique-concatenation",
    "statement": "f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.",
    "formalStatement": "f(m) is a nonempty finite bit word; f*([]) = []; f*(m::s)=f(m)++f*(s); f*(s)=f*(t) implies s=t.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction."
    ],
    "appliesTo": [
      "urn:csabs:concept/UniquelyDecodableCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definitions 6.1–6.3 and Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  }
]
```
<!-- graph-record:end -->
