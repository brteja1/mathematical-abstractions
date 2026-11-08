# Ordered collection without duplicates

A finite sequence with pairwise distinct elements; sequence position is part of equality.

**Notation:** OrdSet(A)={s∈Seq(A):∀i,j<|s|, sᵢ=sⱼ⇒i=j}

**Stable ID:** `urn:csabs:concept/OrderedSet`

**Categories:** Data structures → Sets and mappings, Data structures → Sequential collections

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Finite set collection](FiniteSet.md)

**Related concepts:** [Multiset](Multiset.md), [Map](Map.md)

## Backlinks

- [Multiset](Multiset.md) — `relatedConcept`
- [Finite sequence (List datatype)](Sequence.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: The carrier is the duplicate-free finite sequences, with positional equality. Fresh append preserves every old position and adds one new final position. Indexing is defined exactly at valid positions and returns the stored component.

**basisKind:** defined-structure

**basisScope:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**verificationObligation:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-OrderedSet-empty"></a>

### empty

`urn:csabs:operation/OrderedSet-empty`

**signature:** empty : OrdSet(A)

**description:** Returns the empty sequence.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the empty sequence.

<a id="node-urn-csabs-operation-OrderedSet-appendFresh"></a>

### appendFresh

`urn:csabs:operation/OrderedSet-appendFresh`

**signature:** appendFresh : OrdSet(A)×A ⇀ OrdSet(A)

**description:** Appends a previously absent element at the end.

**precondition:** a∉{sᵢ:0≤i<|s|}

**totality:** partial: defined exactly when the new element is absent

**postcondition:** Appends a previously absent element at the end.

<a id="node-urn-csabs-operation-OrderedSet-at"></a>

### at

`urn:csabs:operation/OrderedSet-at`

**signature:** at : OrdSet(A)×ℕ ⇀ A

**description:** Returns the element at a zero-based position.

**precondition:** 0≤i<|s|

**totality:** partial: defined exactly for valid indices

**postcondition:** Returns the element at a zero-based position.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-OrderedSet-carrier-equality"></a>

### carrier-equality

`urn:csabs:axiom/OrderedSet-carrier-equality`

**statement:** The carrier is the duplicate-free finite sequences, with positional equality.

**description:** The carrier is the duplicate-free finite sequences, with positional equality.

**formalStatement:** s∈OrdSet(A) iff s∈Seq(A) ∧ ∀i,j<|s|:(sᵢ=sⱼ⇒i=j); s=t iff |s|=|t| ∧ ∀i<|s|:sᵢ=tᵢ

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-OrderedSet-append-index"></a>

### append-index

`urn:csabs:axiom/OrderedSet-append-index`

**statement:** Fresh append preserves every old position and adds one new final position.

**description:** Fresh append preserves every old position and adds one new final position.

**formalStatement:** empty=[]; a∉elements(s)⇒(|appendFresh(s,a)|=|s|+1 ∧ (∀i<|s|:at(appendFresh(s,a),i)=sᵢ) ∧ at(appendFresh(s,a),|s|)=a)

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-OrderedSet-index-definedness"></a>

### index-definedness

`urn:csabs:axiom/OrderedSet-index-definedness`

**statement:** Indexing is defined exactly at valid positions and returns the stored component.

**description:** Indexing is defined exactly at valid positions and returns the stored component.

**formalStatement:** at(s,i) is defined iff 0≤i<|s|; when defined, at(s,i)=sᵢ

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** OCL 2.4 §§11.6.3, 11.7.3; adapted to zero-based indices and partiality

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-OrderedSet-fresh-append-injective"></a>

### fresh-append-injective

`urn:csabs:law/OrderedSet-fresh-append-injective`

**statement:** Equal fresh appends have equal prefixes and appended elements.

**description:** Equal fresh appends have equal prefixes and appended elements.

**formalStatement:** appendFresh(s,a)=appendFresh(t,b) ⇒ s=t ∧ a=b

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.; a∉elements(s) and b∉elements(t), so both sides are defined.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Lengths give |s|=|t|. Compare the last position to obtain a=b, then all earlier positions and positional extensionality to obtain s=t.

**dependsOn:** [carrier-equality](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-carrier-equality); [append-index](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-append-index); [index-definedness](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-index-definedness)

<a id="node-urn-csabs-law-OrderedSet-order-distinguishes"></a>

### order-distinguishes

`urn:csabs:law/OrderedSet-order-distinguishes`

**statement:** Two distinct elements in opposite orders yield distinct ordered collections.

**description:** Two distinct elements in opposite orders yield distinct ordered collections.

**formalStatement:** a≠b ⇒ appendFresh(appendFresh(empty,a),b) ≠ appendFresh(appendFresh(empty,b),a)

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Both constructions are defined by distinctness. Their zero-th components are a and b, so positional equality cannot hold.

**dependsOn:** [carrier-equality](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-carrier-equality); [append-index](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-append-index); [index-definedness](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-index-definedness)

## Theorems

<a id="node-urn-csabs-theorem-OrderedSet-fresh-closure"></a>

### fresh-closure

`urn:csabs:theorem/OrderedSet-fresh-closure`

**statement:** Fresh append preserves absence of duplicates.

**description:** Fresh append preserves absence of duplicates.

**formalStatement:** a∉elements(s) ∧ s∈OrdSet(A) ⇒ appendFresh(s,a)∈OrdSet(A)

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** derived-result

**proofSketch:** Two old positions are distinct by the carrier constraint. The new final position differs from every old value by freshness.

**dependsOn:** [carrier-equality](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-carrier-equality); [append-index](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-append-index)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-OrderedSet-fresh-append-induction"></a>

### fresh-append-induction

`urn:csabs:theorem/OrderedSet-fresh-append-induction`

**statement:** Prove a predicate on ordered unique collections by empty and fresh append cases.

**description:** Prove a predicate on ordered unique collections by empty and fresh append cases.

**formalStatement:** P(empty) ∧ (∀s,a∉elements(s):P(s)⇒P(appendFresh(s,a))) ⇒ ∀s∈OrdSet(A):P(s)

**assumptions:** Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on sequence length. A nonempty duplicate-free sequence splits uniquely into its initial segment and final element. The initial segment is duplicate-free and the final element is absent from it.

**dependsOn:** [carrier-equality](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-carrier-equality); [append-index](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-append-index); [index-definedness](OrderedSet.md#node-urn-csabs-axiom-OrderedSet-index-definedness); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [OMG Object Constraint Language 2.4: collection types](https://www.omg.org/spec/OCL/2.4/PDF); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§11.6.3, 11.7.1, 11.7.3

**sourceNote:** Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/OrderedSet",
    "type": "Concept",
    "shortForm": "OrderedSet",
    "fullName": "Ordered collection without duplicates",
    "category": [
      "urn:csabs:category/associative-collections",
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite sequence with pairwise distinct elements; sequence position is part of equality.",
    "notation": "OrdSet(A)={s∈Seq(A):∀i,j<|s|, sᵢ=sⱼ⇒i=j}",
    "hasOperation": [
      "urn:csabs:operation/OrderedSet-empty",
      "urn:csabs:operation/OrderedSet-appendFresh",
      "urn:csabs:operation/OrderedSet-at"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/OrderedSet-carrier-equality",
      "urn:csabs:axiom/OrderedSet-append-index",
      "urn:csabs:axiom/OrderedSet-index-definedness"
    ],
    "hasLaw": [
      "urn:csabs:law/OrderedSet-fresh-append-injective",
      "urn:csabs:law/OrderedSet-order-distinguishes"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/OrderedSet-fresh-closure",
      "urn:csabs:theorem/OrderedSet-fresh-append-induction"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/Map"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: The carrier is the duplicate-free finite sequences, with positional equality. Fresh append preserves every old position and adds one new final position. Indexing is defined exactly at valid positions and returns the stored component.",
    "basisKind": "defined-structure",
    "basisScope": "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ]
  },
  {
    "id": "urn:csabs:operation/OrderedSet-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : OrdSet(A)",
    "description": "Returns the empty sequence.",
    "concept": "urn:csabs:concept/OrderedSet",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the empty sequence."
  },
  {
    "id": "urn:csabs:operation/OrderedSet-appendFresh",
    "type": "Operation",
    "name": "appendFresh",
    "signature": "appendFresh : OrdSet(A)×A ⇀ OrdSet(A)",
    "description": "Appends a previously absent element at the end.",
    "concept": "urn:csabs:concept/OrderedSet",
    "precondition": "a∉{sᵢ:0≤i<|s|}",
    "totality": "partial: defined exactly when the new element is absent",
    "postcondition": "Appends a previously absent element at the end."
  },
  {
    "id": "urn:csabs:operation/OrderedSet-at",
    "type": "Operation",
    "name": "at",
    "signature": "at : OrdSet(A)×ℕ ⇀ A",
    "description": "Returns the element at a zero-based position.",
    "concept": "urn:csabs:concept/OrderedSet",
    "precondition": "0≤i<|s|",
    "totality": "partial: defined exactly for valid indices",
    "postcondition": "Returns the element at a zero-based position."
  },
  {
    "id": "urn:csabs:axiom/OrderedSet-carrier-equality",
    "type": "Axiom",
    "name": "carrier-equality",
    "statement": "The carrier is the duplicate-free finite sequences, with positional equality.",
    "description": "The carrier is the duplicate-free finite sequences, with positional equality.",
    "formalStatement": "s∈OrdSet(A) iff s∈Seq(A) ∧ ∀i,j<|s|:(sᵢ=sⱼ⇒i=j); s=t iff |s|=|t| ∧ ∀i<|s|:sᵢ=tᵢ",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/OrderedSet-append-index",
    "type": "Axiom",
    "name": "append-index",
    "statement": "Fresh append preserves every old position and adds one new final position.",
    "description": "Fresh append preserves every old position and adds one new final position.",
    "formalStatement": "empty=[]; a∉elements(s)⇒(|appendFresh(s,a)|=|s|+1 ∧ (∀i<|s|:at(appendFresh(s,a),i)=sᵢ) ∧ at(appendFresh(s,a),|s|)=a)",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Uses the ordered/no-duplicates distinction. To avoid ambiguous duplicate insertion and invalid/null propagation, appendFresh is explicitly partial and accepts only absent elements. This is an abstract mathematical variant, not the entire OCL library. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/OrderedSet-index-definedness",
    "type": "Axiom",
    "name": "index-definedness",
    "statement": "Indexing is defined exactly at valid positions and returns the stored component.",
    "description": "Indexing is defined exactly at valid positions and returns the stored component.",
    "formalStatement": "at(s,i) is defined iff 0≤i<|s|; when defined, at(s,i)=sᵢ",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "OCL 2.4 §§11.6.3, 11.7.3; adapted to zero-based indices and partiality",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/OrderedSet-fresh-append-injective",
    "type": "Law",
    "name": "fresh-append-injective",
    "statement": "Equal fresh appends have equal prefixes and appended elements.",
    "description": "Equal fresh appends have equal prefixes and appended elements.",
    "formalStatement": "appendFresh(s,a)=appendFresh(t,b) ⇒ s=t ∧ a=b",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs.",
      "a∉elements(s) and b∉elements(t), so both sides are defined."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Lengths give |s|=|t|. Compare the last position to obtain a=b, then all earlier positions and positional extensionality to obtain s=t.",
    "dependsOn": [
      "urn:csabs:axiom/OrderedSet-carrier-equality",
      "urn:csabs:axiom/OrderedSet-append-index",
      "urn:csabs:axiom/OrderedSet-index-definedness"
    ]
  },
  {
    "id": "urn:csabs:law/OrderedSet-order-distinguishes",
    "type": "Law",
    "name": "order-distinguishes",
    "statement": "Two distinct elements in opposite orders yield distinct ordered collections.",
    "description": "Two distinct elements in opposite orders yield distinct ordered collections.",
    "formalStatement": "a≠b ⇒ appendFresh(appendFresh(empty,a),b) ≠ appendFresh(appendFresh(empty,b),a)",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Both constructions are defined by distinctness. Their zero-th components are a and b, so positional equality cannot hold.",
    "dependsOn": [
      "urn:csabs:axiom/OrderedSet-carrier-equality",
      "urn:csabs:axiom/OrderedSet-append-index",
      "urn:csabs:axiom/OrderedSet-index-definedness"
    ]
  },
  {
    "id": "urn:csabs:theorem/OrderedSet-fresh-closure",
    "type": "Theorem",
    "name": "fresh-closure",
    "statement": "Fresh append preserves absence of duplicates.",
    "description": "Fresh append preserves absence of duplicates.",
    "formalStatement": "a∉elements(s) ∧ s∈OrdSet(A) ⇒ appendFresh(s,a)∈OrdSet(A)",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Two old positions are distinct by the carrier constraint. The new final position differs from every old value by freshness.",
    "dependsOn": [
      "urn:csabs:axiom/OrderedSet-carrier-equality",
      "urn:csabs:axiom/OrderedSet-append-index"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/OrderedSet-fresh-append-induction",
    "type": "Theorem",
    "name": "fresh-append-induction",
    "statement": "Prove a predicate on ordered unique collections by empty and fresh append cases.",
    "description": "Prove a predicate on ordered unique collections by empty and fresh append cases.",
    "formalStatement": "P(empty) ∧ (∀s,a∉elements(s):P(s)⇒P(appendFresh(s,a))) ⇒ ∀s∈OrdSet(A):P(s)",
    "assumptions": [
      "Identity equality on A; empty sequence allowed. No sorting order on A is assumed. This is related to Sequence rather than specializing its full concatenation algebra, which is not closed on duplicate-free inputs."
    ],
    "appliesTo": [
      "urn:csabs:concept/OrderedSet"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/omg-ocl24-collections"
    ],
    "sourceLocator": "§§11.6.3, 11.7.1, 11.7.3",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on sequence length. A nonempty duplicate-free sequence splits uniquely into its initial segment and final element. The initial segment is duplicate-free and the final element is absent from it.",
    "dependsOn": [
      "urn:csabs:axiom/OrderedSet-carrier-equality",
      "urn:csabs:axiom/OrderedSet-append-index",
      "urn:csabs:axiom/OrderedSet-index-definedness",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
