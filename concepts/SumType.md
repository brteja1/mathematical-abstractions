# Sum Type

The tagged disjoint union of A and B: each value is exactly a left-tagged A value or a right-tagged B value, eliminated by exhaustive case analysis.

**Notation:** A+B = ({L}×A) ∪ ({R}×B), L≠R; inl(a)=(L,a), inr(b)=(R,b).

**Stable ID:** `urn:csabs:concept/SumType`

**Categories:** Types and semantics

**Kind:** Numeric data type

**Prerequisites:** [Set](Set.md), [Function type](FunctionType.md), [Empty type](EmptyType.md), [Unit type](UnitType.md)

## Backlinks

- [Checked Integer](CheckedInteger.md) — `requiresConcept`
- [Option Type](OptionType.md) — `requiresConcept`
- [Option Type](OptionType.md) — `specializationOf`
- [Finite RDF 1.1 graph](RDFGraph.md) — `requiresConcept`
- [Free ranked term algebra with variables](TermAlgebra.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.

**basisKind:** extensional-type-theory

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Instantiate type parameters and operation domains.; Function equality here is extensional; translating to intensional type theory may require function extensionality.; Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.; Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-SumType-injectLeft"></a>

### injectLeft

`urn:csabs:operation/SumType-injectLeft`

**signature:** inl : A→A+B

**description:** Constructs a left-tagged value.

<a id="node-urn-csabs-operation-SumType-injectRight"></a>

### injectRight

`urn:csabs:operation/SumType-injectRight`

**signature:** inr : B→A+B

**description:** Constructs a right-tagged value.

<a id="node-urn-csabs-operation-sum-case"></a>

### case

`urn:csabs:operation/sum-case`

**signature:** case : (A→C)×(B→C)×(A+B)→C

**description:** Eliminates a sum by applying the branch corresponding to its constructor. Write [f,g](s)=case(f,g,s).

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-sum-map"></a>

### mapSum

`urn:csabs:operation/sum-map`

**signature:** mapSum : (A→C)×(B→D)→(A+B→C+D)

**description:** Maps each payload using the matching function and preserves the left/right tag.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-sum-swap"></a>

### swap

`urn:csabs:operation/sum-swap`

**signature:** swap : A+B→B+A

**description:** Exchanges the tags without changing payloads.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

<a id="node-urn-csabs-operation-sum-associate"></a>

### associate

`urn:csabs:operation/sum-associate`

**signature:** assoc : (A+B)+C→A+(B+C)

**description:** Rebrackets the three alternatives while preserving which alternative and payload were present.

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

## Axioms and defining rules

<a id="node-urn-csabs-axiom-case-inl"></a>

### case-inl

`urn:csabs:axiom/case-inl`

**statement:** Case analysis on a left injection evaluates the left branch.

**formalStatement:** ∀f:A→C,g:B→C,a:A: case(f,g,inl(a))=f(a)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case](SumType.md#node-urn-csabs-operation-sum-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-case-inr"></a>

### case-inr

`urn:csabs:axiom/case-inr`

**statement:** Case analysis on a right injection evaluates the right branch.

**formalStatement:** ∀f:A→C,g:B→C,b:B: case(f,g,inr(b))=g(b)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case](SumType.md#node-urn-csabs-operation-sum-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-sum-eta"></a>

### sum-eta

`urn:csabs:axiom/sum-eta`

**statement:** Every function out of a sum is determined by its two constructor branches.

**formalStatement:** ∀h:A+B→C: h=case(h∘inl,h∘inr)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case](SumType.md#node-urn-csabs-operation-sum-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-map-sum-definition"></a>

### map-sum-definition

`urn:csabs:axiom/map-sum-definition`

**statement:** Sum mapping is case analysis followed by the corresponding target injection.

**formalStatement:** mapSum(f,g)=case(inl∘f,inr∘g)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [mapSum](SumType.md#node-urn-csabs-operation-sum-map); [case](SumType.md#node-urn-csabs-operation-sum-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-sum-swap-definition"></a>

### sum-swap-definition

`urn:csabs:axiom/sum-swap-definition`

**statement:** Swap exchanges the injections.

**formalStatement:** swap=case(inr,inl)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [swap](SumType.md#node-urn-csabs-operation-sum-swap); [case](SumType.md#node-urn-csabs-operation-sum-case)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

<a id="node-urn-csabs-axiom-sum-associate-definition"></a>

### sum-associate-definition

`urn:csabs:axiom/sum-associate-definition`

**statement:** Associating a sum preserves its three alternatives.

**formalStatement:** assoc(inl(inl(a)))=inl(a); assoc(inl(inr(b)))=inr(inl(b)); assoc(inr(c))=inr(inr(c))

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [associate](SumType.md#node-urn-csabs-operation-sum-associate)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

## Laws

<a id="node-urn-csabs-law-SumType-core"></a>

### law/SumType-core

`urn:csabs:law/SumType-core`

**statement:** The two injections have disjoint images.

**formalStatement:** ∀a,b: inl(a)≠inr(b)

**reviewStatus:** editorial-summary; not machine-proved

**assumptions:** Use the carrier and semantic convention in the linked concept definition.

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [injections-disjoint](SumType.md#node-urn-csabs-theorem-injections-disjoint); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-sum-case-identity"></a>

### sum-case-identity

`urn:csabs:law/sum-case-identity`

**statement:** Eliminating a sum with its own constructors recovers the original value.

**formalStatement:** case(inl,inr)=id_(A+B)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Both sides agree on each constructor, so eta gives equality.

<a id="node-urn-csabs-law-sum-map-inl"></a>

### sum-map-inl

`urn:csabs:law/sum-map-inl`

**statement:** Mapping a left injection changes only its payload.

**formalStatement:** mapSum(f,g)(inl(a))=inl(f(a))

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Unfold mapSum and apply case-inl.

<a id="node-urn-csabs-law-sum-map-inr"></a>

### sum-map-inr

`urn:csabs:law/sum-map-inr`

**statement:** Mapping a right injection changes only its payload.

**formalStatement:** mapSum(f,g)(inr(b))=inr(g(b))

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Unfold mapSum and apply case-inr.

<a id="node-urn-csabs-law-sum-map-identity"></a>

### sum-map-identity

`urn:csabs:law/sum-map-identity`

**statement:** Mapping both identity functions gives the identity on the sum.

**formalStatement:** mapSum(id_A,id_B)=id_(A+B)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Check both constructors and apply eta.

<a id="node-urn-csabs-law-sum-map-composition"></a>

### sum-map-composition

`urn:csabs:law/sum-map-composition`

**statement:** Sum mapping preserves composition of branch maps.

**formalStatement:** mapSum(f₂,g₂)∘mapSum(f₁,g₁)=mapSum(f₂∘f₁,g₂∘g₁)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Both sides send a left payload to inl(f₂(f₁(a))) and a right payload to inr(g₂(g₁(b))); apply eta.

<a id="node-urn-csabs-law-sum-case-fusion"></a>

### sum-case-fusion

`urn:csabs:law/sum-case-fusion`

**statement:** Postcomposition distributes through case analysis.

**formalStatement:** k∘case(f,g)=case(k∘f,k∘g)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Both sides agree on inl and inr, then eta applies.

## Theorems

<a id="node-urn-csabs-theorem-coproduct-universal"></a>

### coproduct-universal

`urn:csabs:theorem/coproduct-universal`

**statement:** For any two branch functions, there exists exactly one function out of the sum with those branches.

**formalStatement:** ∀f:A→C,g:B→C ∃!h:A+B→C: h∘inl=f ∧ h∘inr=g

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Existence: h=case(f,g), using the two computation equations. Uniqueness: eta rewrites any candidate h as case(h∘inl,h∘inr)=case(f,g).

<a id="node-urn-csabs-theorem-injections-disjoint"></a>

### injections-disjoint

`urn:csabs:theorem/injections-disjoint`

**statement:** The left and right injections have disjoint images.

**formalStatement:** ∀a:A,b:B: inl(a)≠inr(b)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.; Boolean values false and true are distinct.

**dependsOn:** [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Case into Bool, returning false for the left branch and true for the right. Equality of the inputs would imply false=true.

<a id="node-urn-csabs-theorem-injections-injective"></a>

### injections-injective

`urn:csabs:theorem/injections-injective`

**statement:** Each injection preserves and reflects equality of its payloads.

**formalStatement:** inl(a)=inl(a′) iff a=a′; inr(b)=inr(b′) iff b=b′

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** For a fixed left value a, case(id_A, λb.a) recovers each left payload; use it on the proposed equality. The right proof is symmetric. The reverse implications follow by congruence.

<a id="node-urn-csabs-theorem-sum-swap-involution"></a>

### sum-swap-involution

`urn:csabs:theorem/sum-swap-involution`

**statement:** Swapping a sum twice returns its original value.

**formalStatement:** swap_(B,A)∘swap_(A,B)=id_(A+B)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** Check each constructor and apply eta.

<a id="node-urn-csabs-theorem-sum-finite-cardinality"></a>

### sum-finite-cardinality

`urn:csabs:theorem/sum-finite-cardinality`

**statement:** The size of a finite tagged sum is the sum of the sizes.

**formalStatement:** card(A+B)=card(A)+card(B)

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.; A and B are finite.

**dependsOn:** [injections-disjoint](SumType.md#node-urn-csabs-theorem-injections-disjoint); [injections-injective](SumType.md#node-urn-csabs-theorem-injections-injective); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** The two injective images partition the sum; add their finite cardinalities.

<a id="node-urn-csabs-theorem-sum-empty-identity"></a>

### sum-empty-identity

`urn:csabs:theorem/sum-empty-identity`

**statement:** A sum with an empty summand is isomorphic to its other summand.

**formalStatement:** 0+A ≅ A; A+0 ≅ A

**assumptions:** Extensional total set-like types; all displayed functions total and correctly typed.

**dependsOn:** [absurd-unique](EmptyType.md#node-urn-csabs-axiom-absurd-unique); [case-inl](SumType.md#node-urn-csabs-axiom-case-inl); [case-inr](SumType.md#node-urn-csabs-axiom-case-inr); [sum-eta](SumType.md#node-urn-csabs-axiom-sum-eta); [map-sum-definition](SumType.md#node-urn-csabs-axiom-map-sum-definition); [sum-swap-definition](SumType.md#node-urn-csabs-axiom-sum-swap-definition); [sum-associate-definition](SumType.md#node-urn-csabs-axiom-sum-associate-definition)

**source:** [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**proofSketch:** For 0+A use case(absurd_A,id_A) and inr. Their composites are identities by the beta equations, empty uniqueness, and eta; the other side is symmetric.

## Concept provenance

- [Steve Awodey: Notes on Type Theory](https://awodey.github.io/typetheory/notes/typetheory.pdf); sourceRole: reference
- [Lean reference: sum types](https://lean-lang.org/doc/reference/latest/Basic-Types/Sum-Types/); sourceRole: reference

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/SumType",
    "type": "Concept",
    "shortForm": "SumType",
    "fullName": "Sum Type",
    "category": [
      "urn:csabs:category/types"
    ],
    "kind": "urn:csabs:kind/data-type",
    "definition": "The tagged disjoint union of A and B: each value is exactly a left-tagged A value or a right-tagged B value, eliminated by exhaustive case analysis.",
    "notation": "A+B = ({L}×A) ∪ ({R}×B), L≠R; inl(a)=(L,a), inr(b)=(R,b).",
    "hasOperation": [
      "urn:csabs:operation/SumType-injectLeft",
      "urn:csabs:operation/SumType-injectRight",
      "urn:csabs:operation/sum-case",
      "urn:csabs:operation/sum-map",
      "urn:csabs:operation/sum-swap",
      "urn:csabs:operation/sum-associate"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/SumType-core",
      "urn:csabs:law/sum-case-identity",
      "urn:csabs:law/sum-map-inl",
      "urn:csabs:law/sum-map-inr",
      "urn:csabs:law/sum-map-identity",
      "urn:csabs:law/sum-map-composition",
      "urn:csabs:law/sum-case-fusion"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/coproduct-universal",
      "urn:csabs:theorem/injections-disjoint",
      "urn:csabs:theorem/injections-injective",
      "urn:csabs:theorem/sum-swap-involution",
      "urn:csabs:theorem/sum-finite-cardinality",
      "urn:csabs:theorem/sum-empty-identity"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/FunctionType",
      "urn:csabs:concept/EmptyType",
      "urn:csabs:concept/UnitType"
    ],
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Instantiate type parameters and operation domains.",
      "Function equality here is extensional; translating to intensional type theory may require function extensionality.",
      "Account separately for nontermination, exceptions, mutation, or untagged representation in concrete software.",
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Extensional total set-like types: constructor/eliminator beta and eta equations; operation-definition equations where specified. Equality of functions is pointwise; no divergence, effects, or bottom values.",
    "source": [
      "urn:csabs:source/awodey-types",
      "urn:csabs:source/lean-sum"
    ],
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "basisKind": "extensional-type-theory"
  },
  {
    "id": "urn:csabs:operation/SumType-injectLeft",
    "type": "Operation",
    "name": "injectLeft",
    "signature": "inl : A→A+B",
    "description": "Constructs a left-tagged value.",
    "concept": "urn:csabs:concept/SumType"
  },
  {
    "id": "urn:csabs:operation/SumType-injectRight",
    "type": "Operation",
    "name": "injectRight",
    "signature": "inr : B→A+B",
    "description": "Constructs a right-tagged value.",
    "concept": "urn:csabs:concept/SumType"
  },
  {
    "id": "urn:csabs:operation/sum-case",
    "type": "Operation",
    "name": "case",
    "signature": "case : (A→C)×(B→C)×(A+B)→C",
    "description": "Eliminates a sum by applying the branch corresponding to its constructor. Write [f,g](s)=case(f,g,s).",
    "concept": "urn:csabs:concept/SumType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/sum-map",
    "type": "Operation",
    "name": "mapSum",
    "signature": "mapSum : (A→C)×(B→D)→(A+B→C+D)",
    "description": "Maps each payload using the matching function and preserves the left/right tag.",
    "concept": "urn:csabs:concept/SumType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/sum-swap",
    "type": "Operation",
    "name": "swap",
    "signature": "swap : A+B→B+A",
    "description": "Exchanges the tags without changing payloads.",
    "concept": "urn:csabs:concept/SumType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:operation/sum-associate",
    "type": "Operation",
    "name": "associate",
    "signature": "assoc : (A+B)+C→A+(B+C)",
    "description": "Rebrackets the three alternatives while preserving which alternative and payload were present.",
    "concept": "urn:csabs:concept/SumType",
    "source": [
      "urn:csabs:source/awodey-types"
    ]
  },
  {
    "id": "urn:csabs:axiom/case-inl",
    "type": "Axiom",
    "name": "case-inl",
    "statement": "Case analysis on a left injection evaluates the left branch.",
    "formalStatement": "∀f:A→C,g:B→C,a:A: case(f,g,inl(a))=f(a)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/case-inr",
    "type": "Axiom",
    "name": "case-inr",
    "statement": "Case analysis on a right injection evaluates the right branch.",
    "formalStatement": "∀f:A→C,g:B→C,b:B: case(f,g,inr(b))=g(b)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/sum-eta",
    "type": "Axiom",
    "name": "sum-eta",
    "statement": "Every function out of a sum is determined by its two constructor branches.",
    "formalStatement": "∀h:A+B→C: h=case(h∘inl,h∘inr)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/map-sum-definition",
    "type": "Axiom",
    "name": "map-sum-definition",
    "statement": "Sum mapping is case analysis followed by the corresponding target injection.",
    "formalStatement": "mapSum(f,g)=case(inl∘f,inr∘g)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-map",
      "urn:csabs:operation/sum-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/sum-swap-definition",
    "type": "Axiom",
    "name": "sum-swap-definition",
    "statement": "Swap exchanges the injections.",
    "formalStatement": "swap=case(inr,inl)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-swap",
      "urn:csabs:operation/sum-case"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:axiom/sum-associate-definition",
    "type": "Axiom",
    "name": "sum-associate-definition",
    "statement": "Associating a sum preserves its three alternatives.",
    "formalStatement": "assoc(inl(inl(a)))=inl(a); assoc(inl(inr(b)))=inr(inl(b)); assoc(inr(c))=inr(inr(c))",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:operation/sum-associate"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law"
  },
  {
    "id": "urn:csabs:law/SumType-core",
    "type": "Law",
    "statement": "The two injections have disjoint images.",
    "formalStatement": "∀a,b: inl(a)≠inr(b)",
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "assumptions": [
      "Use the carrier and semantic convention in the linked concept definition."
    ],
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:theorem/injections-disjoint",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/sum-case-identity",
    "type": "Law",
    "name": "sum-case-identity",
    "statement": "Eliminating a sum with its own constructors recovers the original value.",
    "formalStatement": "case(inl,inr)=id_(A+B)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Both sides agree on each constructor, so eta gives equality."
  },
  {
    "id": "urn:csabs:law/sum-map-inl",
    "type": "Law",
    "name": "sum-map-inl",
    "statement": "Mapping a left injection changes only its payload.",
    "formalStatement": "mapSum(f,g)(inl(a))=inl(f(a))",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Unfold mapSum and apply case-inl."
  },
  {
    "id": "urn:csabs:law/sum-map-inr",
    "type": "Law",
    "name": "sum-map-inr",
    "statement": "Mapping a right injection changes only its payload.",
    "formalStatement": "mapSum(f,g)(inr(b))=inr(g(b))",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Unfold mapSum and apply case-inr."
  },
  {
    "id": "urn:csabs:law/sum-map-identity",
    "type": "Law",
    "name": "sum-map-identity",
    "statement": "Mapping both identity functions gives the identity on the sum.",
    "formalStatement": "mapSum(id_A,id_B)=id_(A+B)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Check both constructors and apply eta."
  },
  {
    "id": "urn:csabs:law/sum-map-composition",
    "type": "Law",
    "name": "sum-map-composition",
    "statement": "Sum mapping preserves composition of branch maps.",
    "formalStatement": "mapSum(f₂,g₂)∘mapSum(f₁,g₁)=mapSum(f₂∘f₁,g₂∘g₁)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Both sides send a left payload to inl(f₂(f₁(a))) and a right payload to inr(g₂(g₁(b))); apply eta."
  },
  {
    "id": "urn:csabs:law/sum-case-fusion",
    "type": "Law",
    "name": "sum-case-fusion",
    "statement": "Postcomposition distributes through case analysis.",
    "formalStatement": "k∘case(f,g)=case(k∘f,k∘g)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Both sides agree on inl and inr, then eta applies."
  },
  {
    "id": "urn:csabs:theorem/coproduct-universal",
    "type": "Theorem",
    "name": "coproduct-universal",
    "statement": "For any two branch functions, there exists exactly one function out of the sum with those branches.",
    "formalStatement": "∀f:A→C,g:B→C ∃!h:A+B→C: h∘inl=f ∧ h∘inr=g",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Existence: h=case(f,g), using the two computation equations. Uniqueness: eta rewrites any candidate h as case(h∘inl,h∘inr)=case(f,g)."
  },
  {
    "id": "urn:csabs:theorem/injections-disjoint",
    "type": "Theorem",
    "name": "injections-disjoint",
    "statement": "The left and right injections have disjoint images.",
    "formalStatement": "∀a:A,b:B: inl(a)≠inr(b)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed.",
      "Boolean values false and true are distinct."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Case into Bool, returning false for the left branch and true for the right. Equality of the inputs would imply false=true."
  },
  {
    "id": "urn:csabs:theorem/injections-injective",
    "type": "Theorem",
    "name": "injections-injective",
    "statement": "Each injection preserves and reflects equality of its payloads.",
    "formalStatement": "inl(a)=inl(a′) iff a=a′; inr(b)=inr(b′) iff b=b′",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "For a fixed left value a, case(id_A, λb.a) recovers each left payload; use it on the proposed equality. The right proof is symmetric. The reverse implications follow by congruence."
  },
  {
    "id": "urn:csabs:theorem/sum-swap-involution",
    "type": "Theorem",
    "name": "sum-swap-involution",
    "statement": "Swapping a sum twice returns its original value.",
    "formalStatement": "swap_(B,A)∘swap_(A,B)=id_(A+B)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "Check each constructor and apply eta."
  },
  {
    "id": "urn:csabs:theorem/sum-finite-cardinality",
    "type": "Theorem",
    "name": "sum-finite-cardinality",
    "statement": "The size of a finite tagged sum is the sum of the sizes.",
    "formalStatement": "card(A+B)=card(A)+card(B)",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed.",
      "A and B are finite."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:theorem/injections-disjoint",
      "urn:csabs:theorem/injections-injective",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "The two injective images partition the sum; add their finite cardinalities."
  },
  {
    "id": "urn:csabs:theorem/sum-empty-identity",
    "type": "Theorem",
    "name": "sum-empty-identity",
    "statement": "A sum with an empty summand is isomorphic to its other summand.",
    "formalStatement": "0+A ≅ A; A+0 ≅ A",
    "assumptions": [
      "Extensional total set-like types; all displayed functions total and correctly typed."
    ],
    "appliesTo": [
      "urn:csabs:concept/SumType"
    ],
    "dependsOn": [
      "urn:csabs:axiom/absurd-unique",
      "urn:csabs:axiom/case-inl",
      "urn:csabs:axiom/case-inr",
      "urn:csabs:axiom/sum-eta",
      "urn:csabs:axiom/map-sum-definition",
      "urn:csabs:axiom/sum-swap-definition",
      "urn:csabs:axiom/sum-associate-definition"
    ],
    "source": [
      "urn:csabs:source/awodey-types"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "proofSketch": "For 0+A use case(absurd_A,id_A) and inr. Their composites are identities by the beta equations, empty uniqueness, and eta; the other side is symmetric."
  }
]
```
<!-- graph-record:end -->
