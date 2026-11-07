# Boolean algebra

A bounded distributive complemented lattice, equivalently an algebra satisfying an appropriate Boolean equational basis.

**Notation:** (B, ∨, ∧, ¬, 0, 1), with bounded distributive lattice laws and x∨¬x=1, x∧¬x=0.

**Stable ID:** `urn:csabs:concept/BooleanAlgebra`

**Categories:** Logic and proof, Algebra

**Kind:** Mathematical structure

**Specializes:** [Lattice](Lattice.md)

**Related concepts:** [Set](Set.md)

## Backlinks

- [Two-valued Boolean type](BooleanType.md) — `specializationOf`
- [Propositional Logic](PropositionalLogic.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Equational Boolean algebra on a nonempty carrier with join, meet, complement, bottom, and top. Includes lattice laws, bounds, distributivity, and complements; the trivial algebra is allowed.

**basisKind:** axiomatic-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Use the same meet and join and the induced order x≤y iff x∧y=x; boundedness, distributivity and complement are additional structure.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-boolean-join"></a>

### join

`urn:csabs:operation/boolean-join`

**signature:** ∨ : B×B→B

**description:** Least upper bound in the Boolean lattice; logical disjunction in the two-valued model.

<a id="node-urn-csabs-operation-boolean-meet"></a>

### meet

`urn:csabs:operation/boolean-meet`

**signature:** ∧ : B×B→B

**description:** Greatest lower bound in the Boolean lattice; logical conjunction in the two-valued model.

<a id="node-urn-csabs-operation-boolean-complement"></a>

### complement

`urn:csabs:operation/boolean-complement`

**signature:** ¬ : B→B

**description:** Maps each element to its lattice complement.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-boolean-bounded-distributive-complemented"></a>

### boolean-bounded-distributive-complemented

`urn:csabs:axiom/boolean-bounded-distributive-complemented`

**statement:** The lattice is bounded and distributive and each element has a complement.

**formalStatement:** x∨0=x; x∧1=x; x∨(y∧z)=(x∨y)∧(x∨z); x∨¬x=1; x∧¬x=0

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-closure"></a>

### closure

`urn:csabs:axiom/BooleanAlgebra-closure`

**statement:** All operations are total on the carrier.

**formalStatement:** 0,1∈B; ∨,∧:B×B→B; ¬:B→B

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-commutativity"></a>

### commutativity

`urn:csabs:axiom/BooleanAlgebra-commutativity`

**statement:** Join and meet commute.

**formalStatement:** x∨y=y∨x; x∧y=y∧x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-associativity"></a>

### associativity

`urn:csabs:axiom/BooleanAlgebra-associativity`

**statement:** Join and meet associate.

**formalStatement:** (x∨y)∨z=x∨(y∨z); (x∧y)∧z=x∧(y∧z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-absorption"></a>

### absorption

`urn:csabs:axiom/BooleanAlgebra-absorption`

**statement:** The lattice operations absorb each other.

**formalStatement:** x∨(x∧y)=x; x∧(x∨y)=x

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-bounds"></a>

### bounds

`urn:csabs:axiom/BooleanAlgebra-bounds`

**statement:** Zero and one are bounds.

**formalStatement:** x∨0=x; x∧1=x; x∨1=1; x∧0=0

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-distributivity"></a>

### distributivity

`urn:csabs:axiom/BooleanAlgebra-distributivity`

**statement:** Each lattice operation distributes over the other.

**formalStatement:** x∧(y∨z)=(x∧y)∨(x∧z); x∨(y∧z)=(x∨y)∧(x∨z)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BooleanAlgebra-complements"></a>

### complements

`urn:csabs:axiom/BooleanAlgebra-complements`

**statement:** Complement meets to zero and joins to one.

**formalStatement:** x∧¬x=0; x∨¬x=1

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-de-morgan"></a>

### law/de-morgan

`urn:csabs:law/de-morgan`

**statement:** Complement interchanges join and meet.

**formalStatement:** ¬(x∨y)=¬x∧¬y; ¬(x∧y)=¬x∨¬y

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [boolean-bounded-distributive-complemented](BooleanAlgebra.md#node-urn-csabs-axiom-boolean-bounded-distributive-complemented); [closure](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-closure); [commutativity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-commutativity); [associativity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-associativity); [absorption](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-absorption); [bounds](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-bounds); [distributivity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-distributivity); [complements](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-complements)

**assumptions:** Use the explicit mathematical bases and typed carriers of the linked concepts.

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-BooleanAlgebra-double-complement"></a>

### double-complement

`urn:csabs:theorem/BooleanAlgebra-double-complement`

**statement:** Complementation is involutive.

**formalStatement:** ¬¬x=x

**proofSketch:** Both x and ¬¬x complement ¬x; distributivity gives uniqueness of complements.

**assumptions:** The explicit basis, carriers, and side conditions stated for BooleanAlgebra apply.

**dependsOn:** [boolean-bounded-distributive-complemented](BooleanAlgebra.md#node-urn-csabs-axiom-boolean-bounded-distributive-complemented); [closure](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-closure); [commutativity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-commutativity); [associativity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-associativity); [absorption](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-absorption); [bounds](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-bounds); [distributivity](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-distributivity); [complements](BooleanAlgebra.md#node-urn-csabs-axiom-BooleanAlgebra-complements)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

Historical source gap retained; see `provenanceStatus` and the frozen baseline.

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BooleanAlgebra",
    "type": "Concept",
    "shortForm": "BooleanAlgebra",
    "fullName": "Boolean algebra",
    "category": [
      "urn:csabs:category/logic",
      "urn:csabs:category/algebra"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A bounded distributive complemented lattice, equivalently an algebra satisfying an appropriate Boolean equational basis.",
    "notation": "(B, ∨, ∧, ¬, 0, 1), with bounded distributive lattice laws and x∨¬x=1, x∧¬x=0.",
    "hasOperation": [
      "urn:csabs:operation/boolean-join",
      "urn:csabs:operation/boolean-meet",
      "urn:csabs:operation/boolean-complement"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/boolean-bounded-distributive-complemented",
      "urn:csabs:axiom/BooleanAlgebra-closure",
      "urn:csabs:axiom/BooleanAlgebra-commutativity",
      "urn:csabs:axiom/BooleanAlgebra-associativity",
      "urn:csabs:axiom/BooleanAlgebra-absorption",
      "urn:csabs:axiom/BooleanAlgebra-bounds",
      "urn:csabs:axiom/BooleanAlgebra-distributivity",
      "urn:csabs:axiom/BooleanAlgebra-complements"
    ],
    "hasLaw": [
      "urn:csabs:law/de-morgan"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BooleanAlgebra-double-complement"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Set"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Equational Boolean algebra on a nonempty carrier with join, meet, complement, bottom, and top. Includes lattice laws, bounds, distributivity, and complements; the trivial algebra is allowed.",
    "basisKind": "axiomatic-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Lattice"
    ],
    "specializationNote": "Use the same meet and join and the induced order x≤y iff x∧y=x; boundedness, distributivity and complement are additional structure."
  },
  {
    "id": "urn:csabs:operation/boolean-join",
    "type": "Operation",
    "name": "join",
    "signature": "∨ : B×B→B",
    "description": "Least upper bound in the Boolean lattice; logical disjunction in the two-valued model.",
    "concept": "urn:csabs:concept/BooleanAlgebra"
  },
  {
    "id": "urn:csabs:operation/boolean-meet",
    "type": "Operation",
    "name": "meet",
    "signature": "∧ : B×B→B",
    "description": "Greatest lower bound in the Boolean lattice; logical conjunction in the two-valued model.",
    "concept": "urn:csabs:concept/BooleanAlgebra"
  },
  {
    "id": "urn:csabs:operation/boolean-complement",
    "type": "Operation",
    "name": "complement",
    "signature": "¬ : B→B",
    "description": "Maps each element to its lattice complement.",
    "concept": "urn:csabs:concept/BooleanAlgebra"
  },
  {
    "id": "urn:csabs:axiom/boolean-bounded-distributive-complemented",
    "type": "Axiom",
    "statement": "The lattice is bounded and distributive and each element has a complement.",
    "formalStatement": "x∨0=x; x∧1=x; x∨(y∧z)=(x∨y)∧(x∨z); x∨¬x=1; x∧¬x=0",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "boolean-bounded-distributive-complemented",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/BooleanAlgebra-closure",
    "type": "Axiom",
    "name": "closure",
    "statement": "All operations are total on the carrier.",
    "formalStatement": "0,1∈B; ∨,∧:B×B→B; ¬:B→B",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-commutativity",
    "type": "Axiom",
    "name": "commutativity",
    "statement": "Join and meet commute.",
    "formalStatement": "x∨y=y∨x; x∧y=y∧x",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-associativity",
    "type": "Axiom",
    "name": "associativity",
    "statement": "Join and meet associate.",
    "formalStatement": "(x∨y)∨z=x∨(y∨z); (x∧y)∧z=x∧(y∧z)",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-absorption",
    "type": "Axiom",
    "name": "absorption",
    "statement": "The lattice operations absorb each other.",
    "formalStatement": "x∨(x∧y)=x; x∧(x∨y)=x",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-bounds",
    "type": "Axiom",
    "name": "bounds",
    "statement": "Zero and one are bounds.",
    "formalStatement": "x∨0=x; x∧1=x; x∨1=1; x∧0=0",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-distributivity",
    "type": "Axiom",
    "name": "distributivity",
    "statement": "Each lattice operation distributes over the other.",
    "formalStatement": "x∧(y∨z)=(x∧y)∨(x∧z); x∨(y∧z)=(x∨y)∧(x∨z)",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:axiom/BooleanAlgebra-complements",
    "type": "Axiom",
    "name": "complements",
    "statement": "Complement meets to zero and joins to one.",
    "formalStatement": "x∧¬x=0; x∨¬x=1",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
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
    "id": "urn:csabs:law/de-morgan",
    "type": "Law",
    "statement": "Complement interchanges join and meet.",
    "formalStatement": "¬(x∨y)=¬x∧¬y; ¬(x∧y)=¬x∨¬y",
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/boolean-bounded-distributive-complemented",
      "urn:csabs:axiom/BooleanAlgebra-closure",
      "urn:csabs:axiom/BooleanAlgebra-commutativity",
      "urn:csabs:axiom/BooleanAlgebra-associativity",
      "urn:csabs:axiom/BooleanAlgebra-absorption",
      "urn:csabs:axiom/BooleanAlgebra-bounds",
      "urn:csabs:axiom/BooleanAlgebra-distributivity",
      "urn:csabs:axiom/BooleanAlgebra-complements"
    ],
    "assumptions": [
      "Use the explicit mathematical bases and typed carriers of the linked concepts."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/BooleanAlgebra-double-complement",
    "type": "Theorem",
    "name": "double-complement",
    "statement": "Complementation is involutive.",
    "formalStatement": "¬¬x=x",
    "proofSketch": "Both x and ¬¬x complement ¬x; distributivity gives uniqueness of complements.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for BooleanAlgebra apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "dependsOn": [
      "urn:csabs:axiom/boolean-bounded-distributive-complemented",
      "urn:csabs:axiom/BooleanAlgebra-closure",
      "urn:csabs:axiom/BooleanAlgebra-commutativity",
      "urn:csabs:axiom/BooleanAlgebra-associativity",
      "urn:csabs:axiom/BooleanAlgebra-absorption",
      "urn:csabs:axiom/BooleanAlgebra-bounds",
      "urn:csabs:axiom/BooleanAlgebra-distributivity",
      "urn:csabs:axiom/BooleanAlgebra-complements"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
