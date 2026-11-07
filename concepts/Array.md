# Fixed-length array

A finite indexed collection with one value per valid index; mutable variants are modeled by state-changing update operations.

**Notation:** A : Index(n) → V; store(A,i,v)[j] = if i=j then v else A[j].

**Stable ID:** `urn:csabs:concept/Array`

**Categories:** Data structures

**Kind:** Abstract data type

**Related concepts:** [Finite sequence](Sequence.md)

## Backlinks

- [Finite rectangular matrix over a field](Matrix.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** Selected presentation: A finite indexed collection with one value per valid index; mutable variants are modeled by state-changing update operations. Governing rules: Lookup and update are specified only for valid indices unless the ADT contract defines another behavior. An array of a fixed length is exactly a total map on that length's indices. Arrays of the same length and value carrier are equal when all indexed values agree. Store changes exactly one valid position and preserves the length.

**basisKind:** defined-structure

**basisScope:** Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.

**verificationObligation:** Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant.

**reviewStatus:** editorial basis review; no machine-checked mathematical proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-array-select"></a>

### select

`urn:csabs:operation/array-select`

**signature:** select : Array×Index(n)→V

**description:** Reads the value at a valid index.

**precondition:** 0 ≤ i < n

<a id="node-urn-csabs-operation-array-store"></a>

### store

`urn:csabs:operation/array-store`

**signature:** store : Array×Index(n)×V→Array

**description:** Returns the array with index i updated to v and all other indices preserved.

**precondition:** 0 ≤ i < n

## Axioms and defining rules

<a id="node-urn-csabs-axiom-array-valid-index"></a>

### array-valid-index

`urn:csabs:axiom/array-valid-index`

**statement:** Lookup and update are specified only for valid indices unless the ADT contract defines another behavior.

**formalStatement:** 0≤i<n

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**ruleRole:** structure-law

**assumptions:** Use the linked concept’s explicit basis and carrier conventions.

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Array-carrier"></a>

### carrier

`urn:csabs:axiom/Array-carrier`

**statement:** An array of a fixed length is exactly a total map on that length's indices.

**formalStatement:** Array(n,V)=V^Index(n); Index(n)={i∈ℕ:i<n}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Array-extensionality"></a>

### extensionality

`urn:csabs:axiom/Array-extensionality`

**statement:** Arrays of the same length and value carrier are equal when all indexed values agree.

**formalStatement:** A=B iff ∀i∈Index(n):select(A,i)=select(B,i)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Array-store-definition"></a>

### store-definition

`urn:csabs:axiom/Array-store-definition`

**statement:** Store changes exactly one valid position and preserves the length.

**formalStatement:** select(store(A,i,v),j)=if j=i then v else select(A,j); i,j∈Index(n)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Laws

<a id="node-urn-csabs-law-array-read-after-write-same"></a>

### law/array-read-after-write-same

`urn:csabs:law/array-read-after-write-same`

**statement:** Reading the index most recently written returns the written value.

**formalStatement:** select(store(A,i,v),i)=v

**assumptions:** i is valid

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [array-valid-index](Array.md#node-urn-csabs-axiom-array-valid-index); [carrier](Array.md#node-urn-csabs-axiom-Array-carrier); [extensionality](Array.md#node-urn-csabs-axiom-Array-extensionality); [store-definition](Array.md#node-urn-csabs-axiom-Array-store-definition)

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-law-array-read-after-write-other"></a>

### law/array-read-after-write-other

`urn:csabs:law/array-read-after-write-other`

**statement:** Writing one index preserves the value at every different index.

**formalStatement:** i≠j ⇒ select(store(A,i,v),j)=select(A,j)

**assumptions:** i and j are valid

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**dependsOn:** [array-valid-index](Array.md#node-urn-csabs-axiom-array-valid-index); [carrier](Array.md#node-urn-csabs-axiom-Array-carrier); [extensionality](Array.md#node-urn-csabs-axiom-Array-extensionality); [store-definition](Array.md#node-urn-csabs-axiom-Array-store-definition)

**provenanceStatus:** legacy-source-missing

## Theorems

<a id="node-urn-csabs-theorem-Array-update-overwrite"></a>

### update-overwrite

`urn:csabs:theorem/Array-update-overwrite`

**statement:** Two writes to the same valid index retain only the last value.

**formalStatement:** store(store(A,i,v),i,w)=store(A,i,w)

**proofSketch:** Read each valid index; the two store equations give identical values; apply array extensionality.

**assumptions:** The explicit basis, carriers, and side conditions stated for Array apply.

**dependsOn:** [array-valid-index](Array.md#node-urn-csabs-axiom-array-valid-index); [carrier](Array.md#node-urn-csabs-axiom-Array-carrier); [extensionality](Array.md#node-urn-csabs-axiom-Array-extensionality); [store-definition](Array.md#node-urn-csabs-axiom-Array-store-definition)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

## Concept provenance

- [List of data structures (Wikipedia)](https://en.wikipedia.org/wiki/List_of_data_structures); sourceRole: discovery

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Array",
    "type": "Concept",
    "shortForm": "Array",
    "fullName": "Fixed-length array",
    "category": [
      "urn:csabs:category/data-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite indexed collection with one value per valid index; mutable variants are modeled by state-changing update operations.",
    "notation": "A : Index(n) → V; store(A,i,v)[j] = if i=j then v else A[j].",
    "source": [
      "urn:csabs:source/wikipedia-data-structures"
    ],
    "hasOperation": [
      "urn:csabs:operation/array-select",
      "urn:csabs:operation/array-store"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/array-valid-index",
      "urn:csabs:axiom/Array-carrier",
      "urn:csabs:axiom/Array-extensionality",
      "urn:csabs:axiom/Array-store-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/array-read-after-write-same",
      "urn:csabs:law/array-read-after-write-other"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Array-update-overwrite"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Sequence"
    ],
    "coverageStatus": "basis-reviewed",
    "requiresConcept": [],
    "verificationObligation": [
      "Use the stated carriers, equality, domain restrictions and semantic conventions; alternative conventions require an explicit variant."
    ],
    "axiomBasis": "Selected presentation: A finite indexed collection with one value per valid index; mutable variants are modeled by state-changing update operations. Governing rules: Lookup and update are specified only for valid indices unless the ADT contract defines another behavior. An array of a fixed length is exactly a total map on that length's indices. Arrays of the same length and value carrier are equal when all indexed values agree. Store changes exactly one valid position and preserves the length.",
    "basisKind": "defined-structure",
    "basisScope": "Defining interface and selected derived results for the operations listed in this entry. Not an enumeration of all consequences or all alternative foundations.",
    "reviewStatus": "editorial basis review; no machine-checked mathematical proof"
  },
  {
    "id": "urn:csabs:operation/array-select",
    "type": "Operation",
    "name": "select",
    "signature": "select : Array×Index(n)→V",
    "description": "Reads the value at a valid index.",
    "precondition": "0 ≤ i < n",
    "concept": "urn:csabs:concept/Array"
  },
  {
    "id": "urn:csabs:operation/array-store",
    "type": "Operation",
    "name": "store",
    "signature": "store : Array×Index(n)×V→Array",
    "description": "Returns the array with index i updated to v and all other indices preserved.",
    "precondition": "0 ≤ i < n",
    "concept": "urn:csabs:concept/Array"
  },
  {
    "id": "urn:csabs:axiom/array-valid-index",
    "type": "Axiom",
    "statement": "Lookup and update are specified only for valid indices unless the ADT contract defines another behavior.",
    "formalStatement": "0≤i<n",
    "appliesTo": [
      "urn:csabs:concept/Array"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "ruleRole": "structure-law",
    "name": "array-valid-index",
    "assumptions": [
      "Use the linked concept’s explicit basis and carrier conventions."
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:axiom/Array-carrier",
    "type": "Axiom",
    "name": "carrier",
    "statement": "An array of a fixed length is exactly a total map on that length's indices.",
    "formalStatement": "Array(n,V)=V^Index(n); Index(n)={i∈ℕ:i<n}",
    "appliesTo": [
      "urn:csabs:concept/Array"
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
    "id": "urn:csabs:axiom/Array-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Arrays of the same length and value carrier are equal when all indexed values agree.",
    "formalStatement": "A=B iff ∀i∈Index(n):select(A,i)=select(B,i)",
    "appliesTo": [
      "urn:csabs:concept/Array"
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
    "id": "urn:csabs:axiom/Array-store-definition",
    "type": "Axiom",
    "name": "store-definition",
    "statement": "Store changes exactly one valid position and preserves the length.",
    "formalStatement": "select(store(A,i,v),j)=if j=i then v else select(A,j); i,j∈Index(n)",
    "appliesTo": [
      "urn:csabs:concept/Array"
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
    "id": "urn:csabs:law/array-read-after-write-same",
    "type": "Law",
    "statement": "Reading the index most recently written returns the written value.",
    "formalStatement": "select(store(A,i,v),i)=v",
    "assumptions": [
      "i is valid"
    ],
    "appliesTo": [
      "urn:csabs:concept/Array"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/array-valid-index",
      "urn:csabs:axiom/Array-carrier",
      "urn:csabs:axiom/Array-extensionality",
      "urn:csabs:axiom/Array-store-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:law/array-read-after-write-other",
    "type": "Law",
    "statement": "Writing one index preserves the value at every different index.",
    "formalStatement": "i≠j ⇒ select(store(A,i,v),j)=select(A,j)",
    "assumptions": [
      "i and j are valid"
    ],
    "appliesTo": [
      "urn:csabs:concept/Array"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "dependsOn": [
      "urn:csabs:axiom/array-valid-index",
      "urn:csabs:axiom/Array-carrier",
      "urn:csabs:axiom/Array-extensionality",
      "urn:csabs:axiom/Array-store-definition"
    ],
    "provenanceStatus": "legacy-source-missing"
  },
  {
    "id": "urn:csabs:theorem/Array-update-overwrite",
    "type": "Theorem",
    "name": "update-overwrite",
    "statement": "Two writes to the same valid index retain only the last value.",
    "formalStatement": "store(store(A,i,v),i,w)=store(A,i,w)",
    "proofSketch": "Read each valid index; the two store equations give identical values; apply array extensionality.",
    "assumptions": [
      "The explicit basis, carriers, and side conditions stated for Array apply."
    ],
    "appliesTo": [
      "urn:csabs:concept/Array"
    ],
    "dependsOn": [
      "urn:csabs:axiom/array-valid-index",
      "urn:csabs:axiom/Array-carrier",
      "urn:csabs:axiom/Array-extensionality",
      "urn:csabs:axiom/Array-store-definition"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "provenanceStatus": "legacy-source-missing"
  }
]
```
<!-- graph-record:end -->
