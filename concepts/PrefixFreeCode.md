# Prefix-free binary source code

Injective symbol code for which no distinct codeword is a prefix of another.

**Notation:** f:M→{0,1}⁺; f(a)≼f(b)⇒a=b

**Stable ID:** `urn:csabs:concept/PrefixFreeCode`

**Categories:** Information theory → Coding theory → Source coding

**Kind:** Mathematical structure

**Prerequisites:** [Uniquely decodable binary source code](UniquelyDecodableCode.md)

**Specializes:** [Uniquely decodable binary source code](UniquelyDecodableCode.md)

## Mathematical formulation

The selected binary code f:M→{0,1}\* has ∀m,f(m)≠ε and ∀a,b,f(a) is a prefix of f(b)⇒a=b. Empty codewords are explicitly excluded.

**Lean formulation** (in its source module context):

```lean
abbrev PrefixFreeCode := Information.PrefixCode
```

**Source:** [`Catalog.PrefixFreeCode`](../lean/Catalog/InformationTheory.lean); consulted 2026-11-12.

**Scope:** partial

**Interpretation:** M→List Bool with positive lengths and prefix implication forcing equal source symbols.

**Limits:** Parsing and correspondence to UniqueCode omitted; no unique-decoding theorem witness. These are model bindings, not proofs of the catalog theorems.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.

**basisKind:** extensional-structural-definition

**basisScope:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.

**specializationNote:** Use the same symbol-to-word map and concatenation extension; impose the prefix condition. Unique decoding follows by the explicitly linked theorem, not inheritance.

**verificationObligation:** Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.; Retrieve explicit premises; category and specialization links do not inherit claims.

**reviewStatus:** Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PrefixFreeCode-parse"></a>

### parse

`urn:csabs:operation/PrefixFreeCode-parse`

**signature:** parse : PrefixCode(M)×{0,1}* → Option(M*)

**description:** Return the unique complete symbol string if the bits are a concatenation of codewords; otherwise failure, including incomplete final words.

**precondition:** Inputs satisfy the concept profile.

**totality:** Total on the stated domain.

**postcondition:** Return the unique complete symbol string if the bits are a concatenation of codewords; otherwise failure, including incomplete final words.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.3, Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-PrefixFreeCode-prefix-condition"></a>

### prefix-condition

`urn:csabs:axiom/PrefixFreeCode-prefix-condition`

**statement:** f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.

**formalStatement:** f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.

**ruleRole:** defining-rule

**reviewStatus:** Sourced structural definition, not an independent foundational axiom.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.3, Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-PrefixFreeCode-unique-decoding"></a>

### Prefix-free codes are uniquely decodable

`urn:csabs:theorem/PrefixFreeCode-unique-decoding`

**statement:** f*(s)=f*(t) implies s=t.

**formalStatement:** f*(s)=f*(t) implies s=t.

**assumptions:** Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.

**dependsOn:** [prefix-condition](PrefixFreeCode.md#node-urn-csabs-axiom-PrefixFreeCode-prefix-condition)

**proofSketch:** Compare the first two codewords in a nonempty common encoding; one must prefix the other, hence their symbols agree. Cancel that prefix and induct on the remaining source strings.

**reviewStatus:** Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.

**source:** [Yury Polyanskiy, MIT 6.441 (2016), Chapter 6: Variable-length lossless compression](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/67d8e68cd8fda55366e3f9f0a9465c17_MIT6_441S16_chapter_6.pdf); accessedOn: 2026-11-11; sourceRole: consulted author lecture notes; mathematical definitions and theorem statements

**sourceLocator:** §6.4 Definition 6.3, Theorems 6.5–6.6

**sourceNote:** Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (M : Type) (f : Catalog.Information.PrefixCode M), Function.Injective (fun s : List M => s.flatMap f.word)
```

**Source:** [`Catalog.Information.Verified.prefixUnique`](../lean/Catalog/InformationTheoryStatements.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite exact profile. f*(s)=f*(t) implies s=t. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.

**Limits:** Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/PrefixFreeCode-prefix-condition": "Explicit premise: f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom."
}
```

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

**sourceLocator:** §6.4 Definition 6.3, Theorems 6.5–6.6

**sourceNote:** Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PrefixFreeCode",
    "type": "Concept",
    "shortForm": "PrefixFreeCode",
    "fullName": "Prefix-free binary source code",
    "category": [
      "urn:csabs:category/source-coding"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "Injective symbol code for which no distinct codeword is a prefix of another.",
    "notation": "f:M→{0,1}⁺; f(a)≼f(b)⇒a=b",
    "requiresConcept": [
      "urn:csabs:concept/UniquelyDecodableCode"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/PrefixFreeCode-parse"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/PrefixFreeCode-prefix-condition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/PrefixFreeCode-unique-decoding",
      "urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan",
      "urn:csabs:theorem/PrefixFreeCode-source-length"
    ],
    "axiomBasis": "f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean models are explicitly scoped and theorem sketches are not compiled proofs.",
    "verificationObligation": [
      "Map alphabets, exact arithmetic, equality, logarithm base, channel model and error criterion before use.",
      "Retrieve explicit premises; category and specialization links do not inherit claims."
    ],
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definition 6.3, Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/UniquelyDecodableCode"
    ],
    "specializationNote": "Use the same symbol-to-word map and concatenation extension; impose the prefix condition. Unique decoding follows by the explicitly linked theorem, not inheritance.",
    "leanFormulation": "abbrev PrefixFreeCode := Information.PrefixCode",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheory",
    "formulationLocator": "Catalog.PrefixFreeCode",
    "formulationScope": "partial",
    "leanModelMapping": "M→List Bool with positive lengths and prefix implication forcing equal source symbols.",
    "leanModelLimitations": "Parsing and correspondence to UniqueCode omitted; no unique-decoding theorem witness. These are model bindings, not proofs of the catalog theorems.",
    "mathematicalFormulation": "The selected binary code f:M→{0,1}* has ∀m,f(m)≠ε and ∀a,b,f(a) is a prefix of f(b)⇒a=b. Empty codewords are explicitly excluded."
  },
  {
    "id": "urn:csabs:operation/PrefixFreeCode-parse",
    "type": "Operation",
    "name": "parse",
    "signature": "parse : PrefixCode(M)×{0,1}* → Option(M*)",
    "description": "Return the unique complete symbol string if the bits are a concatenation of codewords; otherwise failure, including incomplete final words.",
    "concept": "urn:csabs:concept/PrefixFreeCode",
    "precondition": "Inputs satisfy the concept profile.",
    "totality": "Total on the stated domain.",
    "postcondition": "Return the unique complete symbol string if the bits are a concatenation of codewords; otherwise failure, including incomplete final words.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definition 6.3, Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PrefixFreeCode-prefix-condition",
    "type": "Axiom",
    "name": "prefix-condition",
    "statement": "f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.",
    "formalStatement": "f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits."
    ],
    "appliesTo": [
      "urn:csabs:concept/PrefixFreeCode"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Sourced structural definition, not an independent foundational axiom.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definition 6.3, Theorems 6.5–6.6",
    "sourceNote": "Finite exact profile adapted from the cited definitions/results; restrictions and conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:theorem/PrefixFreeCode-unique-decoding",
    "type": "Theorem",
    "name": "Prefix-free codes are uniquely decodable",
    "statement": "f*(s)=f*(t) implies s=t.",
    "formalStatement": "f*(s)=f*(t) implies s=t.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits."
    ],
    "appliesTo": [
      "urn:csabs:concept/PrefixFreeCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PrefixFreeCode-prefix-condition"
    ],
    "proofSketch": "Compare the first two codewords in a nonempty common encoding; one must prefix the other, hence their symbols agree. Cancel that prefix and induct on the remaining source strings.",
    "reviewStatus": "Editorial statement-to-Lean correspondence review; a full-claim witness is registered separately in lean/bindings.json. Consult a fresh verification report for compiler and axiom-audit evidence.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "§6.4 Definition 6.3, Theorems 6.5–6.6",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (M : Type) (f : Catalog.Information.PrefixCode M), Function.Injective (fun s : List M => s.flatMap f.word)",
    "formulationSource": "urn:csabs:source/local-lean-InformationTheoryStatements",
    "formulationLocator": "Catalog.Information.Verified.prefixUnique",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite exact profile. f*(s)=f*(t) implies s=t. The compiled Targets proposition supplies explicit carriers and hypotheses; the independently expanded expected type is retained here. Nat minima are used only under nontrivial-code assumptions; source and channel blocks use positive lengths.",
    "leanModelLimitations": "Witness proves the entire expanded expected type; correspondence to the informal statement is a reviewed mapping. This does not prove other catalog targets or an implementation refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/PrefixFreeCode-prefix-condition\": \"Explicit premise: f(m) is nonempty and (f(a) is a prefix of f(b) ⇒ a=b); parse is the partial inverse of concatenation, returning failure outside its image. Implemented by the normalized finite-law, exact finite-field, prefix-word or Hamming definitions and proved helper lemmas in InformationTheoryProofs/Statements; not introduced as a global axiom.\"}"
  },
  {
    "id": "urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan",
    "type": "Theorem",
    "name": "Kraft–McMillan theorem",
    "statement": "For every uniquely decodable binary code, Σm 2^(−|f(m)|)≤1. Conversely any finite assignment of positive integer lengths ℓm with Σm 2^(−ℓm)≤1 is realized by a prefix-free binary code.",
    "formalStatement": "For every uniquely decodable binary code, Σm 2^(−|f(m)|)≤1. Conversely any finite assignment of positive integer lengths ℓm with Σm 2^(−ℓm)≤1 is realized by a prefix-free binary code.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. M finite nonempty; codewords have positive integer lengths; source sequences concatenate without external delimiters. Equality is word equality. This is lossless source coding, not channel error correction."
    ],
    "appliesTo": [
      "urn:csabs:concept/UniquelyDecodableCode",
      "urn:csabs:concept/PrefixFreeCode"
    ],
    "dependsOn": [
      "urn:csabs:axiom/UniquelyDecodableCode-unique-concatenation"
    ],
    "proofSketch": "For necessity count distinct concatenations of r codewords by total bit length and let r grow (McMillan). For sufficiency allocate disjoint dyadic intervals of the requested lengths in a binary prefix tree.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "Theorem 6.5",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PrefixFreeCode-source-length",
    "type": "Theorem",
    "name": "Shannon expected-length bounds",
    "statement": "For p(m)>0 on finite M, every uniquely decodable f has H(p)≤L(f,p). There exists a prefix-free f with L(f,p)≤H(p)+1; if |M|≥2 this can be strengthened to L(f,p)<H(p)+1.",
    "formalStatement": "For p(m)>0 on finite M, every uniquely decodable f has H(p)≤L(f,p). There exists a prefix-free f with L(f,p)≤H(p)+1; if |M|≥2 this can be strengthened to L(f,p)<H(p)+1.",
    "assumptions": [
      "Finite nonempty alphabets; normalized exact real masses; log means log₂; 0 log₂ 0=0. Equality of distributions is pointwise; no floating-point rounding. Positive lengths; M finite nonempty; prefix includes equality. Streaming concatenation uses exact bits.",
      "p has full support on the chosen source alphabet; singleton source uses a positive one-bit word."
    ],
    "appliesTo": [
      "urn:csabs:concept/PrefixFreeCode",
      "urn:csabs:concept/UniquelyDecodableCode"
    ],
    "dependsOn": [
      "urn:csabs:theorem/UniquelyDecodableCode-kraft-mcmillan",
      "urn:csabs:theorem/RelativeEntropy-gibbs",
      "urn:csabs:axiom/ShannonEntropy-entropy-equation"
    ],
    "proofSketch": "Normalize the Kraft weights and apply Gibbs for the lower bound. For |M|≥2 choose ℓm=ceil(−log₂p(m)) and apply Kraft; for a singleton choose a one-bit word.",
    "reviewStatus": "Editorial proof sketch; no registered Lean theorem witness.",
    "source": [
      "urn:csabs:source/mit-information-6"
    ],
    "sourceLocator": "Theorem 6.6; positive-length singleton convention stated explicitly",
    "sourceNote": "Editorial derivation from the linked premises using the cited argument; no machine-checked witness is asserted.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
