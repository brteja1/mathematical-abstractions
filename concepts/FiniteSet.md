# Finite set collection

An unordered finite subset of a fixed carrier, with extensional equality and no duplicate occurrences.

**Notation:** FinSet(A)={s⊆A : s is finite}

**Stable ID:** `urn:csabs:concept/FiniteSet`

**Categories:** Data structures → Sets and mappings, Set theory and foundations

**Kind:** Abstract data type

**Prerequisites:** [Set](Set.md)

**Specializes:** [Set](Set.md)

**Related concepts:** [Multiset](Multiset.md), [Finite sequence (List datatype)](Sequence.md)

## Backlinks

- [B-tree (balanced multiway search tree)](BTree.md) — `requiresConcept`
- [Strict binary search tree](BinarySearchTree.md) — `requiresConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `requiresConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `specializationOf`
- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `requiresConcept`
- [Finite typed entity-relationship instance](EntityRelationshipModel.md) — `requiresConcept`
- [Finitely supported probability distribution](FiniteDistribution.md) — `requiresConcept`
- [Finite carrier with exhaustive enumeration](FiniteType.md) — `requiresConcept`
- [Finite kinded generic parameter signature](GenericSignature.md) — `requiresConcept`
- [Finite simple undirected hypergraph](Hypergraph.md) — `requiresConcept`
- [Finite set-valued multimap](Multimap.md) — `requiresConcept`
- [Multiset](Multiset.md) — `relatedConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `requiresConcept`
- [Finite RDF 1.1 graph](RDFGraph.md) — `requiresConcept`
- [Set](Set.md) — `relatedConcept`
- [Finitely supported vector](SparseVector.md) — `requiresConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Collection states are finite subsets and equality is membership equality. Empty and insertion have set membership semantics.

**basisKind:** defined-structure

**basisScope:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**specializationNote:** Restrict the parent powerset carrier 𝒫(A) to its finite members. Membership, empty, union, intersection, difference and subset retain their set meanings and preserve this restriction. No complement in an infinite ambient carrier is included.

**verificationObligation:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FiniteSet-empty"></a>

### empty

`urn:csabs:operation/FiniteSet-empty`

**signature:** empty : FinSet(A)

**description:** Returns ∅.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns ∅.

<a id="node-urn-csabs-operation-FiniteSet-member"></a>

### member

`urn:csabs:operation/FiniteSet-member`

**signature:** member : A×FinSet(A)→Prop

**description:** Tests membership as a mathematical predicate.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Tests membership as a mathematical predicate.

<a id="node-urn-csabs-operation-FiniteSet-insert"></a>

### insert

`urn:csabs:operation/FiniteSet-insert`

**signature:** insert : FinSet(A)×A→FinSet(A)

**description:** Adds an element; an existing element is not duplicated.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Adds an element; an existing element is not duplicated.

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FiniteSet-carrier-extensionality"></a>

### carrier-extensionality

`urn:csabs:axiom/FiniteSet-carrier-extensionality`

**statement:** Collection states are finite subsets and equality is membership equality.

**description:** Collection states are finite subsets and equality is membership equality.

**formalStatement:** s∈FinSet(A) iff s⊆A ∧ s finite; s=t iff ∀x∈A:(x∈s ↔ x∈t)

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteSet-constructors"></a>

### constructors

`urn:csabs:axiom/FiniteSet-constructors`

**statement:** Empty and insertion have set membership semantics.

**description:** Empty and insertion have set membership semantics.

**formalStatement:** x∉empty; x∈insert(s,a) iff (x=a ∨ x∈s)

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FiniteSet-insert-commutation"></a>

### insert-commutation

`urn:csabs:law/FiniteSet-insert-commutation`

**statement:** Insertions commute.

**description:** Insertions commute.

**formalStatement:** insert(insert(s,a),b)=insert(insert(s,b),a)

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Both sides contain x exactly when x∈s or x=a or x=b. Membership extensionality identifies them.

**dependsOn:** [carrier-extensionality](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-carrier-extensionality); [constructors](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-constructors)

<a id="node-urn-csabs-law-FiniteSet-insert-absorption"></a>

### insert-absorption

`urn:csabs:law/FiniteSet-insert-absorption`

**statement:** Insertion is ineffective exactly when the element is already present.

**description:** Insertion is ineffective exactly when the element is already present.

**formalStatement:** insert(s,a)=s iff a∈s

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** If a is present, insertion has the same members; conversely a belongs to the inserted set, hence belongs to s if the sets are equal.

**dependsOn:** [carrier-extensionality](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-carrier-extensionality); [constructors](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-constructors)

## Theorems

<a id="node-urn-csabs-theorem-FiniteSet-insert-idempotence"></a>

### insert-idempotence

`urn:csabs:theorem/FiniteSet-insert-idempotence`

**statement:** Inserting the same element twice has the same effect as once.

**description:** Inserting the same element twice has the same effect as once.

**formalStatement:** insert(insert(s,a),a)=insert(s,a)

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** derived-result

**proofSketch:** For each x, the membership formula is x=a or x=a or x∈s; Boolean idempotence and extensionality conclude.

**dependsOn:** [carrier-extensionality](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-carrier-extensionality); [constructors](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-constructors)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-FiniteSet-finite-insertion-induction"></a>

### finite-insertion-induction

`urn:csabs:theorem/FiniteSet-finite-insertion-induction`

**statement:** A predicate closed under fresh insertion and true of empty holds for every finite set.

**description:** A predicate closed under fresh insertion and true of empty holds for every finite set.

**formalStatement:** P(∅) ∧ (∀s∈FinSet(A),a∉s:P(s)⇒P(insert(s,a))) ⇒ ∀s∈FinSet(A):P(s)

**assumptions:** A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.

**ruleRole:** proof-principle

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces; [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset.induction_on; Finset.mem_insert; finite subset definition

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Induct on a finite enumeration without duplicates. Delete its final element to obtain a smaller finite set; the original is recovered by a fresh insertion. Membership extensionality makes the proof independent of enumeration order.

**dependsOn:** [carrier-extensionality](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-carrier-extensionality); [constructors](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-constructors); [induction-schema](NaturalNumber.md#node-urn-csabs-axiom-NaturalNumber-induction-schema)

## Concept provenance

- [Mathlib: finite sets, membership and extensionality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Defs.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces
- [Mathlib: finite-set insertion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Insert.html); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** Finset definition; Finset.ext_iff; Finset.mem_insert

**sourceNote:** Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FiniteSet",
    "type": "Concept",
    "shortForm": "FiniteSet",
    "fullName": "Finite set collection",
    "category": [
      "urn:csabs:category/associative-collections",
      "urn:csabs:category/foundations"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "An unordered finite subset of a fixed carrier, with extensional equality and no duplicate occurrences.",
    "notation": "FinSet(A)={s⊆A : s is finite}",
    "hasOperation": [
      "urn:csabs:operation/FiniteSet-empty",
      "urn:csabs:operation/FiniteSet-member",
      "urn:csabs:operation/FiniteSet-insert"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors"
    ],
    "hasLaw": [
      "urn:csabs:law/FiniteSet-insert-commutation",
      "urn:csabs:law/FiniteSet-insert-absorption"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteSet-insert-idempotence",
      "urn:csabs:theorem/FiniteSet-finite-insertion-induction"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/Sequence"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Collection states are finite subsets and equality is membership equality. Empty and insertion have set membership semantics.",
    "basisKind": "defined-structure",
    "basisScope": "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality.",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "specializationOf": [
      "urn:csabs:concept/Set"
    ],
    "specializationNote": "Restrict the parent powerset carrier 𝒫(A) to its finite members. Membership, empty, union, intersection, difference and subset retain their set meanings and preserve this restriction. No complement in an infinite ambient carrier is included."
  },
  {
    "id": "urn:csabs:operation/FiniteSet-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty : FinSet(A)",
    "description": "Returns ∅.",
    "concept": "urn:csabs:concept/FiniteSet",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns ∅."
  },
  {
    "id": "urn:csabs:operation/FiniteSet-member",
    "type": "Operation",
    "name": "member",
    "signature": "member : A×FinSet(A)→Prop",
    "description": "Tests membership as a mathematical predicate.",
    "concept": "urn:csabs:concept/FiniteSet",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Tests membership as a mathematical predicate."
  },
  {
    "id": "urn:csabs:operation/FiniteSet-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : FinSet(A)×A→FinSet(A)",
    "description": "Adds an element; an existing element is not duplicated.",
    "concept": "urn:csabs:concept/FiniteSet",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Adds an element; an existing element is not duplicated."
  },
  {
    "id": "urn:csabs:axiom/FiniteSet-carrier-extensionality",
    "type": "Axiom",
    "name": "carrier-extensionality",
    "statement": "Collection states are finite subsets and equality is membership equality.",
    "description": "Collection states are finite subsets and equality is membership equality.",
    "formalStatement": "s∈FinSet(A) iff s⊆A ∧ s finite; s=t iff ∀x∈A:(x∈s ↔ x∈t)",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteSet-constructors",
    "type": "Axiom",
    "name": "constructors",
    "statement": "Empty and insertion have set membership semantics.",
    "description": "Empty and insertion have set membership semantics.",
    "formalStatement": "x∉empty; x∈insert(s,a) iff (x=a ∨ x∈s)",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Abstracts the finite-subset interface from Finset; no Lean representation or computability guarantee is assumed. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FiniteSet-insert-commutation",
    "type": "Law",
    "name": "insert-commutation",
    "statement": "Insertions commute.",
    "description": "Insertions commute.",
    "formalStatement": "insert(insert(s,a),b)=insert(insert(s,b),a)",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Both sides contain x exactly when x∈s or x=a or x=b. Membership extensionality identifies them.",
    "dependsOn": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors"
    ]
  },
  {
    "id": "urn:csabs:law/FiniteSet-insert-absorption",
    "type": "Law",
    "name": "insert-absorption",
    "statement": "Insertion is ineffective exactly when the element is already present.",
    "description": "Insertion is ineffective exactly when the element is already present.",
    "formalStatement": "insert(s,a)=s iff a∈s",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "If a is present, insertion has the same members; conversely a belongs to the inserted set, hence belongs to s if the sets are equal.",
    "dependsOn": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors"
    ]
  },
  {
    "id": "urn:csabs:theorem/FiniteSet-insert-idempotence",
    "type": "Theorem",
    "name": "insert-idempotence",
    "statement": "Inserting the same element twice has the same effect as once.",
    "description": "Inserting the same element twice has the same effect as once.",
    "formalStatement": "insert(insert(s,a),a)=insert(s,a)",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "For each x, the membership formula is x=a or x=a or x∈s; Boolean idempotence and extensionality conclude.",
    "dependsOn": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset definition; Finset.ext_iff; Finset.mem_insert",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/FiniteSet-finite-insertion-induction",
    "type": "Theorem",
    "name": "finite-insertion-induction",
    "statement": "A predicate closed under fresh insertion and true of empty holds for every finite set.",
    "description": "A predicate closed under fresh insertion and true of empty holds for every finite set.",
    "formalStatement": "P(∅) ∧ (∀s∈FinSet(A),a∉s:P(s)⇒P(insert(s,a))) ⇒ ∀s∈FinSet(A):P(s)",
    "assumptions": [
      "A is any set with identity equality. Empty collections are allowed; membership is a mathematical predicate. Executable membership/insertion additionally require a way to decide equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "proof-principle",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/mathlib-finset-defs",
      "urn:csabs:source/mathlib-finset-insert"
    ],
    "sourceLocator": "Finset.induction_on; Finset.mem_insert; finite subset definition",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Induct on a finite enumeration without duplicates. Delete its final element to obtain a smaller finite set; the original is recovered by a fresh insertion. Membership extensionality makes the proof independent of enumeration order.",
    "dependsOn": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors",
      "urn:csabs:axiom/NaturalNumber-induction-schema"
    ]
  }
]
```
<!-- graph-record:end -->
