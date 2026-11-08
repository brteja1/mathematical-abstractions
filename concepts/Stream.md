# Infinite discrete stream

A total natural-indexed family of values with pointwise observations and productive head/tail decomposition.

**Notation:** Stream(A)=ℕ→A

**Stable ID:** `urn:csabs:concept/Stream`

**Categories:** Data structures → Sequential collections

**Kind:** Abstract data type

**Prerequisites:** [Total function](Function.md), [Natural Number](NaturalNumber.md), [Finite sequence (List datatype)](Sequence.md)

## Interface and scope

**axiomBasis:** head(cons(a,s))=a ∧ tail(cons(a,s))=s; s=t ⇔ ∀n:ℕ, s(n)=t(n); map(f,s)(n)=f(s(n))

**basisKind:** extensional-structural-definition

**basisScope:** Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.

**basisInstantiation:** Instantiate total Function at domain ℕ and codomain A; reuse Function-extensionality explicitly at this instance. Stream map/cons/head/tail are the displayed natural-indexed operations.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Stream-cons"></a>

### cons

`urn:csabs:operation/Stream-cons`

**signature:** cons : A×Stream(A)→Stream(A)

**description:** cons(a,s)(0)=a; cons(a,s)(n+1)=s(n).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** cons(a,s)(0)=a; cons(a,s)(n+1)=s(n).

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Stream-head"></a>

### head

`urn:csabs:operation/Stream-head`

**signature:** head : Stream(A)→A

**description:** head(s)=s(0).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** head(s)=s(0).

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Stream-tail"></a>

### tail

`urn:csabs:operation/Stream-tail`

**signature:** tail : Stream(A)→Stream(A)

**description:** tail(s)(n)=s(n+1).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** tail(s)(n)=s(n+1).

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Stream-map"></a>

### map

`urn:csabs:operation/Stream-map`

**signature:** map : (A→B)×Stream(A)→Stream(B)

**description:** map(f,s)(n)=f(s(n)).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** map(f,s)(n)=f(s(n)).

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Stream-observations"></a>

### observations

`urn:csabs:axiom/Stream-observations`

**statement:** Defining requirement: head(cons(a,s))=a ∧ tail(cons(a,s))=s

**formalStatement:** head(cons(a,s))=a ∧ tail(cons(a,s))=s

**assumptions:** Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Function-extensionality"></a>

### extensionality

`urn:csabs:axiom/Function-extensionality`

**statement:** Typed functions are equal if they agree on every input.

**formalStatement:** f,g:A→B; f=g iff ∀a∈A: f(a)=g(a)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Stream-map-equation"></a>

### map-equation

`urn:csabs:axiom/Stream-map-equation`

**statement:** Defining requirement: map(f,s)(n)=f(s(n))

**formalStatement:** map(f,s)(n)=f(s(n))

**assumptions:** Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Stream-map-identity"></a>

### map-identity

`urn:csabs:law/Stream-map-identity`

**statement:** map(id,s)=s

**formalStatement:** map(id,s)=s

**assumptions:** Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [map-equation](Stream.md#node-urn-csabs-axiom-Stream-map-equation)

**proofSketch:** Each natural-indexed observation is unchanged; apply pointwise equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-Stream-map-composition"></a>

### map-composition

`urn:csabs:theorem/Stream-map-composition`

**statement:** map(g,map(f,s))=map(g∘f,s)

**formalStatement:** map(g,map(f,s))=map(g∘f,s)

**assumptions:** Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [extensionality](Function.md#node-urn-csabs-axiom-Function-extensionality); [map-equation](Stream.md#node-urn-csabs-axiom-Stream-map-equation)

**proofSketch:** Expand the observation at n on both sides and use pointwise equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Stream",
    "type": "Concept",
    "shortForm": "Stream",
    "fullName": "Infinite discrete stream",
    "category": [
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A total natural-indexed family of values with pointwise observations and productive head/tail decomposition.",
    "notation": "Stream(A)=ℕ→A",
    "requiresConcept": [
      "urn:csabs:concept/Function",
      "urn:csabs:concept/NaturalNumber",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/Stream-cons",
      "urn:csabs:operation/Stream-head",
      "urn:csabs:operation/Stream-tail",
      "urn:csabs:operation/Stream-map"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Stream-observations",
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Stream-map-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/Stream-map-identity"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Stream-map-composition"
    ],
    "axiomBasis": "head(cons(a,s))=a ∧ tail(cons(a,s))=s; s=t ⇔ ∀n:ℕ, s(n)=t(n); map(f,s)(n)=f(s(n))",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "basisInstantiation": "Instantiate total Function at domain ℕ and codomain A; reuse Function-extensionality explicitly at this instance. Stream map/cons/head/tail are the displayed natural-indexed operations."
  },
  {
    "id": "urn:csabs:operation/Stream-cons",
    "type": "Operation",
    "name": "cons",
    "signature": "cons : A×Stream(A)→Stream(A)",
    "description": "cons(a,s)(0)=a; cons(a,s)(n+1)=s(n).",
    "concept": "urn:csabs:concept/Stream",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "cons(a,s)(0)=a; cons(a,s)(n+1)=s(n).",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Stream-head",
    "type": "Operation",
    "name": "head",
    "signature": "head : Stream(A)→A",
    "description": "head(s)=s(0).",
    "concept": "urn:csabs:concept/Stream",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "head(s)=s(0).",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Stream-tail",
    "type": "Operation",
    "name": "tail",
    "signature": "tail : Stream(A)→Stream(A)",
    "description": "tail(s)(n)=s(n+1).",
    "concept": "urn:csabs:concept/Stream",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "tail(s)(n)=s(n+1).",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Stream-map",
    "type": "Operation",
    "name": "map",
    "signature": "map : (A→B)×Stream(A)→Stream(B)",
    "description": "map(f,s)(n)=f(s(n)).",
    "concept": "urn:csabs:concept/Stream",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "map(f,s)(n)=f(s(n)).",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Stream-observations",
    "type": "Axiom",
    "name": "observations",
    "statement": "Defining requirement: head(cons(a,s))=a ∧ tail(cons(a,s))=s",
    "formalStatement": "head(cons(a,s))=a ∧ tail(cons(a,s))=s",
    "assumptions": [
      "Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Stream"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Stream-map-equation",
    "type": "Axiom",
    "name": "map-equation",
    "statement": "Defining requirement: map(f,s)(n)=f(s(n))",
    "formalStatement": "map(f,s)(n)=f(s(n))",
    "assumptions": [
      "Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/Stream"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Stream-map-identity",
    "type": "Law",
    "name": "map-identity",
    "statement": "map(id,s)=s",
    "formalStatement": "map(id,s)=s",
    "assumptions": [
      "Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Stream"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Stream-map-equation"
    ],
    "proofSketch": "Each natural-indexed observation is unchanged; apply pointwise equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/Stream-map-composition",
    "type": "Theorem",
    "name": "map-composition",
    "statement": "map(g,map(f,s))=map(g∘f,s)",
    "formalStatement": "map(g,map(f,s))=map(g∘f,s)",
    "assumptions": [
      "Infinite streams only; there is no end marker. Equality is pointwise at all natural indices. No effects, time-of-arrival, fairness or termination of arbitrary filters is assumed. Stream(∅) is empty.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/Stream"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Function-extensionality",
      "urn:csabs:axiom/Stream-map-equation"
    ],
    "proofSketch": "Expand the observation at n on both sides and use pointwise equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
