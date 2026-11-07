# Cartesian product

The set of ordered pairs whose first and second components come from the respective factor sets.

**Notation:** A × B = {(a,b) | a∈A ∧ b∈B}.

**Stable ID:** `urn:csabs:concept/CartesianProduct`

**Categories:** Set theory and foundations

**Kind:** Mathematical construction

## Backlinks

- [Total function](Function.md) — `relatedConcept`
- [Product Type](ProductType.md) — `requiresConcept`
- [Binary relation](Relation.md) — `relatedConcept`
- [Named relational schema with attribute domains](RelationalSchema.md) — `requiresConcept`
- [Set](Set.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: The set of ordered pairs whose first and second components come from the respective factor sets. Governing rules: Ordered pairs are equal exactly when both components agree. The product contains exactly the pairs of elements of the two factors. Projections recover the two components.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-product-projection-first"></a>

### first projection

`urn:csabs:operation/product-projection-first`

**signature:** π₁ : A×B → A

**description:** Returns the first component of an ordered pair.

<a id="node-urn-csabs-operation-product-projection-second"></a>

### second projection

`urn:csabs:operation/product-projection-second`

**signature:** π₂ : A×B → B

**description:** Returns the second component of an ordered pair.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-CartesianProduct-pair-equality"></a>

### pair-equality

`urn:csabs:axiom/CartesianProduct-pair-equality`

**statement:** Ordered pairs are equal exactly when both components agree.

**formalStatement:** (a,b)=(a′,b′) iff a=a′ ∧ b=b′

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-CartesianProduct-membership"></a>

### membership

`urn:csabs:axiom/CartesianProduct-membership`

**statement:** The product contains exactly the pairs of elements of the two factors.

**formalStatement:** p∈A×B iff ∃a∈A,b∈B:p=(a,b)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-CartesianProduct-projection"></a>

### projection

`urn:csabs:axiom/CartesianProduct-projection`

**statement:** Projections recover the two components.

**formalStatement:** π₁(a,b)=a; π₂(a,b)=b; (π₁(p),π₂(p))=p for p∈A×B

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-product-membership"></a>

### law/product-membership

`urn:csabs:law/product-membership`

**statement:** A pair belongs to a Cartesian product iff both components belong to their corresponding factors.

**formalStatement:** (a,b)∈A×B ↔ (a∈A∧b∈B)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [pair-equality](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-pair-equality); [membership](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-membership); [projection](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-projection)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-finite-product-cardinality"></a>

### theorem/finite-product-cardinality

`urn:csabs:theorem/finite-product-cardinality`

**statement:** The cardinality of the product of finite sets is the product of their cardinalities.

**formalStatement:** |A×B|=|A|·|B|

**assumptions:** A and B finite

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [pair-equality](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-pair-equality); [membership](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-membership); [projection](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-projection)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-CartesianProduct-product-extensionality"></a>

### product-extensionality

`urn:csabs:theorem/CartesianProduct-product-extensionality`

**statement:** Pairs are reconstructed from projections.

**formalStatement:** p=q iff π₁(p)=π₁(q) ∧ π₂(p)=π₂(q)

**proofSketch:** Use reconstruction and componentwise equality of pairs.

**assumptions:** The explicit basis, carriers, and side conditions stated for CartesianProduct apply.

**dependsOn:** [pair-equality](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-pair-equality); [membership](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-membership); [projection](CartesianProduct.md#node-urn-csabs-axiom-CartesianProduct-projection)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [Mathematical structure (Wikipedia)](https://en.wikipedia.org/wiki/Mathematical_structure); sourceRole: discovery

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/CartesianProduct",
    "type": "Concept",
    "shortForm": "CartesianProduct",
    "fullName": "Cartesian product",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/construction",
    "definition": "The set of ordered pairs whose first and second components come from the respective factor sets.",
    "notation": "A × B = {(a,b) | a∈A ∧ b∈B}.",
    "hasOperation": [
      "urn:csabs:operation/product-projection-first",
      "urn:csabs:operation/product-projection-second"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/CartesianProduct-pair-equality",
      "urn:csabs:axiom/CartesianProduct-membership",
      "urn:csabs:axiom/CartesianProduct-projection"
    ],
    "hasLaw": [
      "urn:csabs:law/product-membership"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/finite-product-cardinality",
      "urn:csabs:theorem/CartesianProduct-product-extensionality"
    ],
    "source": [
      "urn:csabs:source/wikipedia-math-structure"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: The set of ordered pairs whose first and second components come from the respective factor sets. Governing rules: Ordered pairs are equal exactly when both components agree. The product contains exactly the pairs of elements of the two factors. Projections recover the two components.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/product-projection-first",
    "type": "Operation",
    "name": "first projection",
    "signature": "π₁ : A×B → A",
    "description": "Returns the first component of an ordered pair.",
    "concept": "urn:csabs:concept/CartesianProduct"
  },
  {
    "id": "urn:csabs:operation/product-projection-second",
    "type": "Operation",
    "name": "second projection",
    "signature": "π₂ : A×B → B",
    "description": "Returns the second component of an ordered pair.",
    "concept": "urn:csabs:concept/CartesianProduct"
  },
  {
    "id": "urn:csabs:axiom/CartesianProduct-pair-equality",
    "type": "Axiom",
    "name": "pair-equality",
    "statement": "Ordered pairs are equal exactly when both components agree.",
    "formalStatement": "(a,b)=(a′,b′) iff a=a′ ∧ b=b′",
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/CartesianProduct-membership",
    "type": "Axiom",
    "name": "membership",
    "statement": "The product contains exactly the pairs of elements of the two factors.",
    "formalStatement": "p∈A×B iff ∃a∈A,b∈B:p=(a,b)",
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/CartesianProduct-projection",
    "type": "Axiom",
    "name": "projection",
    "statement": "Projections recover the two components.",
    "formalStatement": "π₁(a,b)=a; π₂(a,b)=b; (π₁(p),π₂(p))=p for p∈A×B",
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "assumptions": [
      "All variables range over the carriers and semantic conventions specified in this concept."
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/product-membership",
    "type": "Law",
    "statement": "A pair belongs to a Cartesian product iff both components belong to their corresponding factors.",
    "formalStatement": "(a,b)∈A×B ↔ (a∈A∧b∈B)",
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/CartesianProduct-pair-equality",
      "urn:csabs:axiom/CartesianProduct-membership",
      "urn:csabs:axiom/CartesianProduct-projection"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/finite-product-cardinality",
    "type": "Theorem",
    "statement": "The cardinality of the product of finite sets is the product of their cardinalities.",
    "formalStatement": "|A×B|=|A|·|B|",
    "assumptions": [
      "A and B finite"
    ],
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/CartesianProduct-pair-equality",
      "urn:csabs:axiom/CartesianProduct-membership",
      "urn:csabs:axiom/CartesianProduct-projection"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/CartesianProduct-product-extensionality",
    "type": "Theorem",
    "name": "product-extensionality",
    "statement": "Pairs are reconstructed from projections.",
    "formalStatement": "p=q iff π₁(p)=π₁(q) ∧ π₂(p)=π₂(q)",
    "proofSketch": "Use reconstruction and componentwise equality of pairs.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for CartesianProduct apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/CartesianProduct"
    ],
    "dependsOn": [
      "urn:csabs:axiom/CartesianProduct-pair-equality",
      "urn:csabs:axiom/CartesianProduct-membership",
      "urn:csabs:axiom/CartesianProduct-projection"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
