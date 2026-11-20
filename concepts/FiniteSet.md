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

- [BM25 score model (positive-IDF, normalized single-field profile)](BM25.md) — `requiresConcept`
- [SQLite FTS5-style BM25 phrase and weighted-column profile](BM25FTS5.md) — `requiresConcept`
- [B-tree (balanced multiway search tree)](BTree.md) — `requiresConcept`
- [Strict binary search tree](BinarySearchTree.md) — `requiresConcept`
- [Finite block code (Hamming profile)](BlockCode.md) — `requiresConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `requiresConcept`
- [Finite database relation under set semantics](DatabaseRelation.md) — `specializationOf`
- [Finite unique-hit decision table](DecisionTable.md) — `requiresConcept`
- [Definition/instantiation lookup for dependent calls](DependentNameLookup.md) — `requiresConcept`
- [Finite typed entity-relationship instance](EntityRelationshipModel.md) — `requiresConcept`
- [Finitely supported probability distribution](FiniteDistribution.md) — `requiresConcept`
- [Finite carrier with exhaustive enumeration](FiniteType.md) — `requiresConcept`
- [Finite kinded generic parameter signature](GenericSignature.md) — `requiresConcept`
- [Hamming space (finite fixed-length words)](HammingSpace.md) — `requiresConcept`
- [Finite simple undirected hypergraph](Hypergraph.md) — `requiresConcept`
- [Empirical mode set (all observed frequency maximizers)](Mode.md) — `requiresConcept`
- [Finite set-valued multimap](Multimap.md) — `requiresConcept`
- [Multiset](Multiset.md) — `relatedConcept`
- [Ordered collection without duplicates](OrderedSet.md) — `requiresConcept`
- [Finite RDF 1.1 graph](RDFGraph.md) — `requiresConcept`
- [Finite score-ranked retrieval](RankedRetrieval.md) — `requiresConcept`
- [Set](Set.md) — `relatedConcept`
- [Finitely supported vector](SparseVector.md) — `requiresConcept`
- [Class template partial-specialization selection](TemplateSpecialization.md) — `requiresConcept`
- [Finite verdict-label coverage](VerdictCoverage.md) — `requiresConcept`

## Mathematical formulation

FinSet(A)={S⊆A | S is finite}; S=T ⇔ ∀x, x∈S↔x∈T. insert(S,x)=S∪{x}; erase(S,x)=S∖{x}. The empty set is included; repeated insertion has no multiplicity. Utility profile: s∪t={x | x∈s ∨ x∈t}; s∩t={x | x∈s ∧ x∈t}; s∖t={x | x∈s ∧ x∉t}; s⊆t iff every member of s belongs to t; empty s is allowed.; filter(p,s)={x∈s | p(x)}; exact predicate semantics.; The number of distinct elements; |∅|=0; arbitrary-precision natural result.

**Lean formulation** (in its source module context):

```lean
abbrev FiniteSet (A : Type u) := Finset A
```

**Source:** [`Catalog.FiniteSet`](../lean/Catalog/DataStructures.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Finset A, quotient-based finite sets with extensional equality.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: Collection states are finite subsets and equality is membership equality. Empty and insertion have set membership semantics. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

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

<a id="node-urn-csabs-operation-FiniteSet-union"></a>

### union

`urn:csabs:operation/FiniteSet-union`

**signature:** union : FinSet(A)²→FinSet(A)

**description:** s∪t={x | x∈s ∨ x∈t}

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** s∪t={x | x∈s ∨ x∈t}

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteSet-intersection"></a>

### intersection

`urn:csabs:operation/FiniteSet-intersection`

**signature:** intersection : FinSet(A)²→FinSet(A)

**description:** s∩t={x | x∈s ∧ x∈t}

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** s∩t={x | x∈s ∧ x∈t}

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteSet-difference"></a>

### difference

`urn:csabs:operation/FiniteSet-difference`

**signature:** difference : FinSet(A)²→FinSet(A)

**description:** s∖t={x | x∈s ∧ x∉t}

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** s∖t={x | x∈s ∧ x∉t}

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteSet-subset"></a>

### subset

`urn:csabs:operation/FiniteSet-subset`

**signature:** subset : FinSet(A)²→Prop

**description:** s⊆t iff every member of s belongs to t; empty s is allowed.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** s⊆t iff every member of s belongs to t; empty s is allowed.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteSet-filter"></a>

### filter

`urn:csabs:operation/FiniteSet-filter`

**signature:** filter : (A→Prop)×FinSet(A)→FinSet(A)

**description:** filter(p,s)={x∈s | p(x)}; exact predicate semantics.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** filter(p,s)={x∈s | p(x)}; exact predicate semantics.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteSet-cardinality"></a>

### cardinality

`urn:csabs:operation/FiniteSet-cardinality`

**signature:** cardinality : FinSet(A)→ℕ

**description:** The number of distinct elements; |∅|=0; arbitrary-precision natural result.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** The number of distinct elements; |∅|=0; arbitrary-precision natural result.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

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

<a id="node-urn-csabs-axiom-FiniteSet-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/FiniteSet-utility-profile`

**statement:** s∪t={x | x∈s ∨ x∈t}; s∩t={x | x∈s ∧ x∈t}; s∖t={x | x∈s ∧ x∉t}; s⊆t iff every member of s belongs to t; empty s is allowed.; filter(p,s)={x∈s | p(x)}; exact predicate semantics.; The number of distinct elements; |∅|=0; arbitrary-precision natural result.

**formalStatement:** union : FinSet(A)²→FinSet(A): s∪t={x | x∈s ∨ x∈t}; intersection : FinSet(A)²→FinSet(A): s∩t={x | x∈s ∧ x∈t}; difference : FinSet(A)²→FinSet(A): s∖t={x | x∈s ∧ x∉t}; subset : FinSet(A)²→Prop: s⊆t iff every member of s belongs to t; empty s is allowed.; filter : (A→Prop)×FinSet(A)→FinSet(A): filter(p,s)={x∈s | p(x)}; exact predicate semantics.; cardinality : FinSet(A)→ℕ: The number of distinct elements; |∅|=0; arbitrary-precision natural result.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-theorem-FiniteSet-utility-membership-cardinality"></a>

### utility-membership-cardinality

`urn:csabs:theorem/FiniteSet-utility-membership-cardinality`

**statement:** Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.

**formalStatement:** Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.

**proofSketch:** Instantiate finite-set membership lemmas and the inclusion-exclusion identity.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-utility-profile); [carrier-extensionality](FiniteSet.md#node-urn-csabs-axiom-FiniteSet-carrier-extensionality)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog CollectionUtilities Lean formulations and proofs; path: lean/Catalog/CollectionUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership; Catalog.finiteSet_utilities

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (s t : Finset A)
    (p : A → Prop) [DecidablePred p] (x : A), (x ∈ s ∪ t ↔ x ∈ s ∨ x ∈ t) ∧
    (x ∈ s ∩ t ↔ x ∈ s ∧ x ∈ t) ∧
    (x ∈ s \ t ↔ x ∈ s ∧ x ∉ t) ∧
    (s ⊆ t ↔ ∀ a ∈ s, a ∈ t) ∧
    (x ∈ s.filter p ↔ x ∈ s ∧ p x) ∧
    (s ∪ t).card + (s ∩ t).card = s.card + t.card
```

**Source:** [`Catalog.finiteSet_utilities`](../lean/Catalog/CollectionUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FiniteSet-carrier-extensionality": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/FiniteSet-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

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
      "urn:csabs:operation/FiniteSet-insert",
      "urn:csabs:operation/FiniteSet-union",
      "urn:csabs:operation/FiniteSet-intersection",
      "urn:csabs:operation/FiniteSet-difference",
      "urn:csabs:operation/FiniteSet-subset",
      "urn:csabs:operation/FiniteSet-filter",
      "urn:csabs:operation/FiniteSet-cardinality"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FiniteSet-carrier-extensionality",
      "urn:csabs:axiom/FiniteSet-constructors",
      "urn:csabs:axiom/FiniteSet-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/FiniteSet-insert-commutation",
      "urn:csabs:law/FiniteSet-insert-absorption"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteSet-insert-idempotence",
      "urn:csabs:theorem/FiniteSet-finite-insertion-induction",
      "urn:csabs:theorem/FiniteSet-utility-membership-cardinality"
    ],
    "requiresConcept": [
      "urn:csabs:concept/Set"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/Sequence"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Collection states are finite subsets and equality is membership equality. Empty and insertion have set membership semantics. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
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
    "specializationNote": "Restrict the parent powerset carrier 𝒫(A) to its finite members. Membership, empty, union, intersection, difference and subset retain their set meanings and preserve this restriction. No complement in an infinite ambient carrier is included.",
    "leanFormulation": "abbrev FiniteSet (A : Type u) := Finset A",
    "formulationSource": "urn:csabs:source/local-lean-DataStructures",
    "formulationLocator": "Catalog.FiniteSet",
    "formulationScope": "model",
    "leanModelMapping": "Finset A, quotient-based finite sets with extensional equality.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "FinSet(A)={S⊆A | S is finite}; S=T ⇔ ∀x, x∈S↔x∈T. insert(S,x)=S∪{x}; erase(S,x)=S∖{x}. The empty set is included; repeated insertion has no multiplicity. Utility profile: s∪t={x | x∈s ∨ x∈t}; s∩t={x | x∈s ∧ x∈t}; s∖t={x | x∈s ∧ x∉t}; s⊆t iff every member of s belongs to t; empty s is allowed.; filter(p,s)={x∈s | p(x)}; exact predicate semantics.; The number of distinct elements; |∅|=0; arbitrary-precision natural result."
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
    "id": "urn:csabs:operation/FiniteSet-union",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "union",
    "signature": "union : FinSet(A)²→FinSet(A)",
    "description": "s∪t={x | x∈s ∨ x∈t}",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "s∪t={x | x∈s ∨ x∈t}",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteSet-intersection",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "intersection",
    "signature": "intersection : FinSet(A)²→FinSet(A)",
    "description": "s∩t={x | x∈s ∧ x∈t}",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "s∩t={x | x∈s ∧ x∈t}",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteSet-difference",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "difference",
    "signature": "difference : FinSet(A)²→FinSet(A)",
    "description": "s∖t={x | x∈s ∧ x∉t}",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "s∖t={x | x∈s ∧ x∉t}",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteSet-subset",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "subset",
    "signature": "subset : FinSet(A)²→Prop",
    "description": "s⊆t iff every member of s belongs to t; empty s is allowed.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "s⊆t iff every member of s belongs to t; empty s is allowed.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteSet-filter",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "filter",
    "signature": "filter : (A→Prop)×FinSet(A)→FinSet(A)",
    "description": "filter(p,s)={x∈s | p(x)}; exact predicate semantics.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "filter(p,s)={x∈s | p(x)}; exact predicate semantics.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteSet-cardinality",
    "type": "Operation",
    "concept": "urn:csabs:concept/FiniteSet",
    "name": "cardinality",
    "signature": "cardinality : FinSet(A)→ℕ",
    "description": "The number of distinct elements; |∅|=0; arbitrary-precision natural result.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "The number of distinct elements; |∅|=0; arbitrary-precision natural result.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
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
    "id": "urn:csabs:axiom/FiniteSet-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "s∪t={x | x∈s ∨ x∈t}; s∩t={x | x∈s ∧ x∈t}; s∖t={x | x∈s ∧ x∉t}; s⊆t iff every member of s belongs to t; empty s is allowed.; filter(p,s)={x∈s | p(x)}; exact predicate semantics.; The number of distinct elements; |∅|=0; arbitrary-precision natural result.",
    "formalStatement": "union : FinSet(A)²→FinSet(A): s∪t={x | x∈s ∨ x∈t}; intersection : FinSet(A)²→FinSet(A): s∩t={x | x∈s ∧ x∈t}; difference : FinSet(A)²→FinSet(A): s∖t={x | x∈s ∧ x∉t}; subset : FinSet(A)²→Prop: s⊆t iff every member of s belongs to t; empty s is allowed.; filter : (A→Prop)×FinSet(A)→FinSet(A): filter(p,s)={x∈s | p(x)}; exact predicate semantics.; cardinality : FinSet(A)→ℕ: The number of distinct elements; |∅|=0; arbitrary-precision natural result.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
  },
  {
    "id": "urn:csabs:theorem/FiniteSet-utility-membership-cardinality",
    "type": "Theorem",
    "name": "utility-membership-cardinality",
    "statement": "Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.",
    "formalStatement": "Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.",
    "mathematicalFormulation": "Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|.",
    "proofSketch": "Instantiate finite-set membership lemmas and the inclusion-exclusion identity.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteSet"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteSet-utility-profile",
      "urn:csabs:axiom/FiniteSet-carrier-extensionality"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-CollectionUtilities"
    ],
    "sourceLocator": "Data/Finset/Filter.lean: mem_filter; Data/Finset/Card.lean: card_union_add_card_inter; Data/Finset/Basic.lean: union, inter, sdiff membership; Catalog.finiteSet_utilities",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (s t : Finset A)\n    (p : A → Prop) [DecidablePred p] (x : A), (x ∈ s ∪ t ↔ x ∈ s ∨ x ∈ t) ∧\n    (x ∈ s ∩ t ↔ x ∈ s ∧ x ∈ t) ∧\n    (x ∈ s \\ t ↔ x ∈ s ∧ x ∉ t) ∧\n    (s ⊆ t ↔ ∀ a ∈ s, a ∈ t) ∧\n    (x ∈ s.filter p ↔ x ∈ s ∧ p x) ∧\n    (s ∪ t).card + (s ∩ t).card = s.card + t.card",
    "leanModelMapping": "Union, intersection, difference, subset and filter have their displayed membership semantics, and |s∪t|+|s∩t|=|s|+|t|. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FiniteSet-carrier-extensionality\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/FiniteSet-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-CollectionUtilities",
    "formulationLocator": "Catalog.finiteSet_utilities"
  }
]
```
<!-- graph-record:end -->
