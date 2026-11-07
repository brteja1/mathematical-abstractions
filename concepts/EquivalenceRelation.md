# Equivalence relation

A homogeneous relation that is reflexive, symmetric, and transitive.

**Notation:** ~ ⊆ A×A; ∀a:a~a; a~b⇒b~a; (a~b∧b~c)⇒a~c.

**Stable ID:** `urn:csabs:concept/EquivalenceRelation`

**Categories:** Set theory and foundations

**Kind:** Relation

**Specializes:** [Preorder](Preorder.md)

**Related concepts:** [Binary relation](Relation.md), [Partition of a set](Partition.md)

## Backlinks

- [Binary relation](Relation.md) — `relatedConcept`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `requiresConcept`
- [Strong finite partial-trace equivalence](TraceEquivalence.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Selected presentation: A homogeneous relation that is reflexive, symmetric, and transitive. Governing rules: Every element is related to itself. Related pairs remain related when reversed. Relatedness composes transitively. The class of an element comprises all elements equivalent to it.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**specializationNote:** Keep the same homogeneous relation and carrier; reflexivity and transitivity give a preorder, with symmetry as an additional constraint.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

**provenanceStatus:** legacy-source-missing

## Operations

<a id="node-urn-csabs-operation-EquivalenceRelation-basis-class"></a>

### class

`urn:csabs:operation/EquivalenceRelation-basis-class`

**signature:** class : A→𝒫(A)

**description:** Returns the equivalence class [a]={x∈A:x~a}.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-equivalence-reflexive"></a>

### equivalence-reflexive

`urn:csabs:axiom/equivalence-reflexive`

**statement:** Every element is related to itself.

**formalStatement:** ∀a∈A: a~a

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-equivalence-symmetric"></a>

### equivalence-symmetric

`urn:csabs:axiom/equivalence-symmetric`

**statement:** Related pairs remain related when reversed.

**formalStatement:** ∀a,b∈A: a~b⇒b~a

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-equivalence-transitive"></a>

### equivalence-transitive

`urn:csabs:axiom/equivalence-transitive`

**statement:** Relatedness composes transitively.

**formalStatement:** ∀a,b,c∈A: (a~b∧b~c)⇒a~c

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-EquivalenceRelation-class-definition"></a>

### class-definition

`urn:csabs:axiom/EquivalenceRelation-class-definition`

**statement:** The class of an element comprises all elements equivalent to it.

**formalStatement:** [a]={x∈A:x~a}; A/~={[a]:a∈A}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-equivalence-partition-correspondence"></a>

### theorem/equivalence-partition-correspondence

`urn:csabs:theorem/equivalence-partition-correspondence`

**statement:** Equivalence relations on A correspond bijectively to partitions of A by their equivalence classes.

**assumptions:** underlying carrier A fixed

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [equivalence-reflexive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-reflexive); [equivalence-symmetric](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-symmetric); [equivalence-transitive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-transitive); [class-definition](EquivalenceRelation.md#node-urn-csabs-axiom-EquivalenceRelation-class-definition); [partition-cover](Partition.md#node-urn-csabs-axiom-partition-cover); [partition-disjoint](Partition.md#node-urn-csabs-axiom-partition-disjoint); [blocks](Partition.md#node-urn-csabs-axiom-Partition-blocks)

**formalStatement:** Equiv(A) ≅ Partitions(A); R↦{[a]_R:a∈A}; Π↦{(a,b):∃B∈Π:a∈B∧b∈B}

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-theorem-EquivalenceRelation-equal-classes"></a>

### equal-classes

`urn:csabs:theorem/EquivalenceRelation-equal-classes`

**statement:** Equivalent elements determine the same equivalence class and conversely.

**formalStatement:** [a]=[b] iff a~b, for a,b∈A

**proofSketch:** Use symmetry and transitivity for forward inclusions; reflexivity places a in its own class.

**assumptions:** The explicit basis, carriers, and side conditions stated for EquivalenceRelation apply.

**dependsOn:** [equivalence-reflexive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-reflexive); [equivalence-symmetric](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-symmetric); [equivalence-transitive](EquivalenceRelation.md#node-urn-csabs-axiom-equivalence-transitive); [class-definition](EquivalenceRelation.md#node-urn-csabs-axiom-EquivalenceRelation-class-definition)

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
    "id": "urn:csabs:concept/EquivalenceRelation",
    "type": "Concept",
    "shortForm": "EquivalenceRelation",
    "fullName": "Equivalence relation",
    "category": [
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/relation",
    "definition": "A homogeneous relation that is reflexive, symmetric, and transitive.",
    "notation": "~ ⊆ A×A; ∀a:a~a; a~b⇒b~a; (a~b∧b~c)⇒a~c.",
    "hasOperation": [
      "urn:csabs:operation/EquivalenceRelation-basis-class"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/equivalence-reflexive",
      "urn:csabs:axiom/equivalence-symmetric",
      "urn:csabs:axiom/equivalence-transitive",
      "urn:csabs:axiom/EquivalenceRelation-class-definition"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/equivalence-partition-correspondence",
      "urn:csabs:theorem/EquivalenceRelation-equal-classes"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/Partition"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A homogeneous relation that is reflexive, symmetric, and transitive. Governing rules: Every element is related to itself. Related pairs remain related when reversed. Relatedness composes transitively. The class of an element comprises all elements equivalent to it.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof",
    "provenanceStatus": "legacy-source-missing",
    "specializationOf": [
      "urn:csabs:concept/Preorder"
    ],
    "specializationNote": "Keep the same homogeneous relation and carrier; reflexivity and transitivity give a preorder, with symmetry as an additional constraint."
  },
  {
    "id": "urn:csabs:operation/EquivalenceRelation-basis-class",
    "type": "Operation",
    "name": "class",
    "signature": "class : A→𝒫(A)",
    "description": "Returns the equivalence class [a]={x∈A:x~a}.",
    "concept": "urn:csabs:concept/EquivalenceRelation"
  },
  {
    "id": "urn:csabs:axiom/equivalence-reflexive",
    "type": "Axiom",
    "statement": "Every element is related to itself.",
    "formalStatement": "∀a∈A: a~a",
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "equivalence-reflexive",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/equivalence-symmetric",
    "type": "Axiom",
    "statement": "Related pairs remain related when reversed.",
    "formalStatement": "∀a,b∈A: a~b⇒b~a",
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "equivalence-symmetric",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/equivalence-transitive",
    "type": "Axiom",
    "statement": "Relatedness composes transitively.",
    "formalStatement": "∀a,b,c∈A: (a~b∧b~c)⇒a~c",
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "equivalence-transitive",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/EquivalenceRelation-class-definition",
    "type": "Axiom",
    "name": "class-definition",
    "statement": "The class of an element comprises all elements equivalent to it.",
    "formalStatement": "[a]={x∈A:x~a}; A/~={[a]:a∈A}",
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation"
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
    "id": "urn:csabs:theorem/equivalence-partition-correspondence",
    "type": "Theorem",
    "statement": "Equivalence relations on A correspond bijectively to partitions of A by their equivalence classes.",
    "assumptions": [
      "underlying carrier A fixed"
    ],
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation",
      "urn:csabs:concept/Partition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/equivalence-reflexive",
      "urn:csabs:axiom/equivalence-symmetric",
      "urn:csabs:axiom/equivalence-transitive",
      "urn:csabs:axiom/EquivalenceRelation-class-definition",
      "urn:csabs:axiom/partition-cover",
      "urn:csabs:axiom/partition-disjoint",
      "urn:csabs:axiom/Partition-blocks"
    ],
    "formalStatement": "Equiv(A) ≅ Partitions(A); R↦{[a]_R:a∈A}; Π↦{(a,b):∃B∈Π:a∈B∧b∈B}",
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/EquivalenceRelation-equal-classes",
    "type": "Theorem",
    "name": "equal-classes",
    "statement": "Equivalent elements determine the same equivalence class and conversely.",
    "formalStatement": "[a]=[b] iff a~b, for a,b∈A",
    "proofSketch": "Use symmetry and transitivity for forward inclusions; reflexivity places a in its own class.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for EquivalenceRelation apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/EquivalenceRelation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/equivalence-reflexive",
      "urn:csabs:axiom/equivalence-symmetric",
      "urn:csabs:axiom/equivalence-transitive",
      "urn:csabs:axiom/EquivalenceRelation-class-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
