# Finite database relation under set semantics

A finite set of admissible named tuples over one schema; row order and duplicate occurrences have no meaning.

**Notation:** Rel(Σ)=FinSet(Tup(Σ)); π_V(r)={t|V:t∈r}

**Stable ID:** `urn:csabs:concept/DatabaseRelation`

**Categories:** Relational data modelling, Data structures

**Kind:** Abstract data type

**Prerequisites:** [Named relational schema with attribute domains](RelationalSchema.md), [Finite set collection](FiniteSet.md)

**Specializes:** [Finite set collection](FiniteSet.md)

**Related concepts:** [Binary relation](Relation.md), [Multiset](Multiset.md), [Functional dependency on a relational schema](FunctionalDependency.md)

## Backlinks

- [Functional dependency on a relational schema](FunctionalDependency.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** Selected defining presentation: Relations are finite tuple sets with extensional equality. Projection is the set image of tuple restriction. Union, selection and natural join are set operations on compatible tuple carriers.

**basisKind:** defined-structure

**basisScope:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**specializationNote:** Instantiate the parent element carrier A as Tup(Σ); relation values are finite subsets of that carrier. Set operations act only on relations with the same schema; projection changes the schema to its restriction.

**verificationObligation:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**reviewStatus:** editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DatabaseRelation-empty"></a>

### empty

`urn:csabs:operation/DatabaseRelation-empty`

**signature:** empty_Σ : Rel(Σ)

**description:** Returns the relation with no tuples.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Returns the relation with no tuples.

<a id="node-urn-csabs-operation-DatabaseRelation-insert"></a>

### insert

`urn:csabs:operation/DatabaseRelation-insert`

**signature:** insert : Rel(Σ)×Tup(Σ)→Rel(Σ)

**description:** Adds a row without adding a duplicate occurrence.

**precondition:** Arguments belong to the carriers in the signature.

**totality:** total mathematical operation on the stated domain

**postcondition:** Adds a row without adding a duplicate occurrence.

<a id="node-urn-csabs-operation-DatabaseRelation-project"></a>

### project

`urn:csabs:operation/DatabaseRelation-project`

**signature:** π_V : Rel(Σ)→Rel(Σ|V)

**description:** Restricts each tuple to V and removes duplicate resulting tuples.

**precondition:** V⊆U; Σ|V retains the corresponding domains.

**totality:** total mathematical operation on the stated domain

**postcondition:** Restricts each tuple to V and removes duplicate resulting tuples.

<a id="node-urn-csabs-operation-DatabaseRelation-union"></a>

### union

`urn:csabs:operation/DatabaseRelation-union`

**signature:** ∪ : Rel(Σ)×Rel(Σ)→Rel(Σ)

**description:** Returns all tuples present in either same-schema relation.

**precondition:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**postcondition:** Returns all tuples present in either same-schema relation.

**totality:** total mathematical operation on the stated domain

<a id="node-urn-csabs-operation-DatabaseRelation-select"></a>

### select

`urn:csabs:operation/DatabaseRelation-select`

**signature:** select : (Tup(Σ)→Prop)×Rel(Σ)→Rel(Σ)

**description:** Keeps exactly the rows satisfying the given total two-valued predicate.

**precondition:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**postcondition:** Keeps exactly the rows satisfying the given total two-valued predicate.

**totality:** total mathematical operation on the stated domain

<a id="node-urn-csabs-operation-DatabaseRelation-naturalJoin"></a>

### naturalJoin

`urn:csabs:operation/DatabaseRelation-naturalJoin`

**signature:** ⋈ : Rel(Σ_V)×Rel(Σ_W)→Rel(Σ_{V∪W})

**description:** Returns tuples whose restrictions occur in both operands.

**precondition:** Schemas have compatible domains on V∩W; output attributes are V∪W with those domains.

**postcondition:** Returns tuples whose restrictions occur in both operands.

**totality:** total mathematical operation on the stated domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DatabaseRelation-set-interface"></a>

### set-interface

`urn:csabs:axiom/DatabaseRelation-set-interface`

**statement:** Relations are finite tuple sets with extensional equality.

**description:** Relations are finite tuple sets with extensional equality.

**formalStatement:** r∈Rel(Σ) iff r⊆Tup(Σ) ∧ r finite; r=s iff ∀t∈Tup(Σ):(t∈r↔t∈s); empty_Σ=∅; insert(r,t)=r∪{t}

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DatabaseRelation-projection"></a>

### projection

`urn:csabs:axiom/DatabaseRelation-projection`

**statement:** Projection is the set image of tuple restriction.

**description:** Projection is the set image of tuple restriction.

**formalStatement:** π_V(r)={t|V:t∈r}, V⊆U

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Local notation specifies the chosen defining presentation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DatabaseRelation-relational-algebra"></a>

### relational-algebra

`urn:csabs:axiom/DatabaseRelation-relational-algebra`

**statement:** Union, selection and natural join are set operations on compatible tuple carriers.

**description:** Union, selection and natural join are set operations on compatible tuple carriers.

**formalStatement:** r∪s={t:t∈r∨t∈s}; select(P,r)={t∈r:P(t)}; r⋈s={t∈Tup(Σ_{V∪W}):t|V∈r ∧ t|W∈s}

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §3.3 set operations; §4.4 selection, named projection and natural join, pp. 57–58

**sourceNote:** Specifies additional equations for the selected abstract interface; local conventions are explicit.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DatabaseRelation-selection-composition"></a>

### selection-composition

`urn:csabs:law/DatabaseRelation-selection-composition`

**statement:** Successive selections combine their predicates.

**description:** Successive selections combine their predicates.

**formalStatement:** select(P,select(Q,r))=select(λt.P(t)∧Q(t),r)

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Both sides have exactly those rows of r for which P and Q hold; set extensionality concludes.

**dependsOn:** [set-interface](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-set-interface); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection); [relational-algebra](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-relational-algebra)

<a id="node-urn-csabs-law-DatabaseRelation-projection-union"></a>

### projection-union

`urn:csabs:law/DatabaseRelation-projection-union`

**statement:** Projection distributes over same-schema union.

**description:** Projection distributes over same-schema union.

**formalStatement:** π_V(r∪s)=π_V(r)∪π_V(s)

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.; r and s have schema Σ and V⊆U.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** A projected tuple has a source row in r or s, and conversely either source supplies membership in the projected union.

**dependsOn:** [set-interface](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-set-interface); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection); [relational-algebra](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-relational-algebra)

## Theorems

<a id="node-urn-csabs-theorem-DatabaseRelation-projection-composition"></a>

### projection-composition

`urn:csabs:theorem/DatabaseRelation-projection-composition`

**statement:** Nested projections discard no more information than direct restriction to the final attributes.

**description:** Nested projections discard no more information than direct restriction to the final attributes.

**formalStatement:** W⊆V⊆U ⇒ π_W(π_V(r))=π_W(r)

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** derived-result

**proofSketch:** Function restriction composes: (t|V)|W=t|W. Taking the two set images gives identical members.

**dependsOn:** [set-interface](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-set-interface); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection)

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.

**provenanceKind:** derived

<a id="node-urn-csabs-theorem-DatabaseRelation-fd-lossless-decomposition"></a>

### fd-lossless-decomposition

`urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition`

**statement:** An FD gives a lossless decomposition into two projections.

**description:** An FD gives a lossless decomposition into two projections.

**formalStatement:** r⊨X→Y ∧ Z=U∖(X∪Y) ⇒ r=π_{X∪Y}(r) ⋈ π_{X∪Z}(r)

**assumptions:** Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.

**ruleRole:** derived-result

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §8.2, Proposition 8.2.2, p. 164; §4.4 natural join

**sourceNote:** Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.

**provenanceKind:** derived

**proofSketch:** Every original row yields compatible projections. Conversely a joined row combines projections of s,t∈r agreeing on X. The FD forces agreement on Y, so the joined row equals t on all U and belongs to r.

**dependsOn:** [set-interface](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-set-interface); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection); [relational-algebra](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-relational-algebra); [satisfaction](FunctionalDependency.md#node-urn-csabs-axiom-FunctionalDependency-satisfaction)

## Concept provenance

- [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57

**sourceNote:** Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DatabaseRelation",
    "type": "Concept",
    "shortForm": "DatabaseRelation",
    "fullName": "Finite database relation under set semantics",
    "category": [
      "urn:csabs:category/data-modelling",
      "urn:csabs:category/data-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite set of admissible named tuples over one schema; row order and duplicate occurrences have no meaning.",
    "notation": "Rel(Σ)=FinSet(Tup(Σ)); π_V(r)={t|V:t∈r}",
    "hasOperation": [
      "urn:csabs:operation/DatabaseRelation-empty",
      "urn:csabs:operation/DatabaseRelation-insert",
      "urn:csabs:operation/DatabaseRelation-project",
      "urn:csabs:operation/DatabaseRelation-union",
      "urn:csabs:operation/DatabaseRelation-select",
      "urn:csabs:operation/DatabaseRelation-naturalJoin"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection",
      "urn:csabs:axiom/DatabaseRelation-relational-algebra"
    ],
    "hasLaw": [
      "urn:csabs:law/DatabaseRelation-selection-composition",
      "urn:csabs:law/DatabaseRelation-projection-union"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DatabaseRelation-projection-composition",
      "urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition"
    ],
    "requiresConcept": [
      "urn:csabs:concept/RelationalSchema",
      "urn:csabs:concept/FiniteSet"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/FunctionalDependency"
    ],
    "coverageStatus": "basis-reviewed",
    "axiomBasis": "Selected defining presentation: Relations are finite tuple sets with extensional equality. Projection is the set image of tuple restriction. Union, selection and natural join are set operations on compatible tuple carriers.",
    "basisKind": "defined-structure",
    "basisScope": "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "specializationOf": [
      "urn:csabs:concept/FiniteSet"
    ],
    "specializationNote": "Instantiate the parent element carrier A as Tup(Σ); relation values are finite subsets of that carrier. Set operations act only on relations with the same schema; projection changes the schema to its restriction."
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "empty_Σ : Rel(Σ)",
    "description": "Returns the relation with no tuples.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Returns the relation with no tuples."
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : Rel(Σ)×Tup(Σ)→Rel(Σ)",
    "description": "Adds a row without adding a duplicate occurrence.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Arguments belong to the carriers in the signature.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Adds a row without adding a duplicate occurrence."
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-project",
    "type": "Operation",
    "name": "project",
    "signature": "π_V : Rel(Σ)→Rel(Σ|V)",
    "description": "Restricts each tuple to V and removes duplicate resulting tuples.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "V⊆U; Σ|V retains the corresponding domains.",
    "totality": "total mathematical operation on the stated domain",
    "postcondition": "Restricts each tuple to V and removes duplicate resulting tuples."
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-union",
    "type": "Operation",
    "name": "union",
    "signature": "∪ : Rel(Σ)×Rel(Σ)→Rel(Σ)",
    "description": "Returns all tuples present in either same-schema relation.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.",
    "postcondition": "Returns all tuples present in either same-schema relation.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-select",
    "type": "Operation",
    "name": "select",
    "signature": "select : (Tup(Σ)→Prop)×Rel(Σ)→Rel(Σ)",
    "description": "Keeps exactly the rows satisfying the given total two-valued predicate.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.",
    "postcondition": "Keeps exactly the rows satisfying the given total two-valued predicate.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-naturalJoin",
    "type": "Operation",
    "name": "naturalJoin",
    "signature": "⋈ : Rel(Σ_V)×Rel(Σ_W)→Rel(Σ_{V∪W})",
    "description": "Returns tuples whose restrictions occur in both operands.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Schemas have compatible domains on V∩W; output attributes are V∪W with those domains.",
    "postcondition": "Returns tuples whose restrictions occur in both operands.",
    "totality": "total mathematical operation on the stated domain"
  },
  {
    "id": "urn:csabs:axiom/DatabaseRelation-set-interface",
    "type": "Axiom",
    "name": "set-interface",
    "statement": "Relations are finite tuple sets with extensional equality.",
    "description": "Relations are finite tuple sets with extensional equality.",
    "formalStatement": "r∈Rel(Σ) iff r⊆Tup(Σ) ∧ r finite; r=s iff ∀t∈Tup(Σ):(t∈r↔t∈s); empty_Σ=∅; insert(r,t)=r∪{t}",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DatabaseRelation-projection",
    "type": "Axiom",
    "name": "projection",
    "statement": "Projection is the set image of tuple restriction.",
    "description": "Projection is the set image of tuple restriction.",
    "formalStatement": "π_V(r)={t|V:t∈r}, V⊆U",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Local notation specifies the chosen defining presentation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DatabaseRelation-relational-algebra",
    "type": "Axiom",
    "name": "relational-algebra",
    "statement": "Union, selection and natural join are set operations on compatible tuple carriers.",
    "description": "Union, selection and natural join are set operations on compatible tuple carriers.",
    "formalStatement": "r∪s={t:t∈r∨t∈s}; select(P,r)={t∈r:P(t)}; r⋈s={t∈Tup(Σ_{V∪W}):t|V∈r ∧ t|W∈s}",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§3.3 set operations; §4.4 selection, named projection and natural join, pp. 57–58",
    "sourceNote": "Specifies additional equations for the selected abstract interface; local conventions are explicit.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DatabaseRelation-selection-composition",
    "type": "Law",
    "name": "selection-composition",
    "statement": "Successive selections combine their predicates.",
    "description": "Successive selections combine their predicates.",
    "formalStatement": "select(P,select(Q,r))=select(λt.P(t)∧Q(t),r)",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Both sides have exactly those rows of r for which P and Q hold; set extensionality concludes.",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection",
      "urn:csabs:axiom/DatabaseRelation-relational-algebra"
    ]
  },
  {
    "id": "urn:csabs:law/DatabaseRelation-projection-union",
    "type": "Law",
    "name": "projection-union",
    "statement": "Projection distributes over same-schema union.",
    "description": "Projection distributes over same-schema union.",
    "formalStatement": "π_V(r∪s)=π_V(r)∪π_V(s)",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.",
      "r and s have schema Σ and V⊆U."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "A projected tuple has a source row in r or s, and conversely either source supplies membership in the projected union.",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection",
      "urn:csabs:axiom/DatabaseRelation-relational-algebra"
    ]
  },
  {
    "id": "urn:csabs:theorem/DatabaseRelation-projection-composition",
    "type": "Theorem",
    "name": "projection-composition",
    "statement": "Nested projections discard no more information than direct restriction to the final attributes.",
    "description": "Nested projections discard no more information than direct restriction to the final attributes.",
    "formalStatement": "W⊆V⊆U ⇒ π_W(π_V(r))=π_W(r)",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "proofSketch": "Function restriction composes: (t|V)|W=t|W. Taking the two set images gives identical members.",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection"
    ],
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57",
    "sourceNote": "Editorial derivation from the linked defining rules and operations, using the consulted source presentation; not attributed as a numbered source theorem.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition",
    "type": "Theorem",
    "name": "fd-lossless-decomposition",
    "statement": "An FD gives a lossless decomposition into two projections.",
    "description": "An FD gives a lossless decomposition into two projections.",
    "formalStatement": "r⊨X→Y ∧ Z=U∖(X∪Y) ⇒ r=π_{X∪Y}(r) ⋈ π_{X∪Z}(r)",
    "assumptions": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation",
      "urn:csabs:concept/FunctionalDependency"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial-summary; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/ahv-database-model"
    ],
    "sourceLocator": "§8.2, Proposition 8.2.2, p. 164; §4.4 natural join",
    "sourceNote": "Editorial consequence of the linked defining rules and premises in the consulted presentation. The proof sketch below explains the derivation; no machine-checked proof or numbered source theorem is claimed.",
    "provenanceKind": "derived",
    "proofSketch": "Every original row yields compatible projections. Conversely a joined row combines projections of s,t∈r agreeing on X. The FD forces agreement on Y, so the joined row equals t on all U and belongs to r.",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection",
      "urn:csabs:axiom/DatabaseRelation-relational-algebra",
      "urn:csabs:axiom/FunctionalDependency-satisfaction"
    ]
  }
]
```
<!-- graph-record:end -->
