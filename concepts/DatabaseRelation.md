# Finite database relation under set semantics

A finite set of admissible named tuples over one schema; row order and duplicate occurrences have no meaning.

**Notation:** Rel(Σ)=FinSet(Tup(Σ)); π_V(r)={t|V:t∈r}

**Stable ID:** `urn:csabs:concept/DatabaseRelation`

**Categories:** Relational data modelling, Data structures → Sets and mappings

**Kind:** Abstract data type

**Prerequisites:** [Named relational schema with attribute domains](RelationalSchema.md), [Finite set collection](FiniteSet.md)

**Specializes:** [Finite set collection](FiniteSet.md)

**Related concepts:** [Binary relation](Relation.md), [Multiset](Multiset.md), [Functional dependency on a relational schema](FunctionalDependency.md)

## Backlinks

- [Finite database relation under bag semantics](BagRelation.md) — `requiresConcept`
- [Functional dependency on a relational schema](FunctionalDependency.md) — `requiresConcept`

## Mathematical formulation

For schema (Attr,D), Tuple=Π\_a D(a) and Relation=FinSet(Tuple). Tuple equality is pointwise; duplicate rows collapse and a relation may be empty.

**Lean formulation** (in its source module context):

```lean
abbrev DatabaseRelation (s : RelationalSchema) := Finset (NamedTuple s)
```

**Source:** [`Catalog.DatabaseRelation`](../lean/Catalog/Database.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Finset of dependent named tuples, set semantics and extensional equality; projection/join algorithms remain to be exposed.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Selected defining presentation: Relations are finite tuple sets with extensional equality. Projection is the set image of tuple restriction. Union, selection and natural join are set operations on compatible tuple carriers. The added Codd basis defines intersection, difference, expanded product, total-predicate theta join and observed-candidate division by the linked membership equations.

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

<a id="node-urn-csabs-operation-DatabaseRelation-intersection"></a>

### intersection

`urn:csabs:operation/DatabaseRelation-intersection`

**signature:** ∩ : Rel(Σ)×Rel(Σ)→Rel(Σ)

**description:** Rows occurring in both same-schema operands.

**precondition:** Same schema, or explicitly domain-preserving alignment to one common schema.

**postcondition:** t∈r∩s iff t∈r ∧ t∈s

**totality:** total mathematical operation on the stated compatible carriers

<a id="node-urn-csabs-operation-DatabaseRelation-difference"></a>

### difference

`urn:csabs:operation/DatabaseRelation-difference`

**signature:** − : Rel(Σ)×Rel(Σ)→Rel(Σ)

**description:** Rows in the first operand but not the second.

**precondition:** Same schema, or explicitly domain-preserving alignment to one common schema.

**postcondition:** t∈r−s iff t∈r ∧ t∉s

**totality:** total mathematical operation on the stated compatible carriers

<a id="node-urn-csabs-operation-DatabaseRelation-cartesianProduct"></a>

### cartesianProduct

`urn:csabs:operation/DatabaseRelation-cartesianProduct`

**signature:** × : Rel(Σ_X)×Rel(Σ_Y)→Rel(Σ_{X∪Y})

**description:** Expanded Cartesian product concatenating disjoint named tuple blocks.

**precondition:** X∩Y=∅; output retains the domains of both blocks. Rename colliding attributes first.

**postcondition:** t∈r×s iff t|X∈r ∧ t|Y∈s; an empty operand yields empty.

**totality:** total mathematical operation on the stated compatible carriers

<a id="node-urn-csabs-operation-DatabaseRelation-thetaJoin"></a>

### thetaJoin

`urn:csabs:operation/DatabaseRelation-thetaJoin`

**signature:** ⋈_P : Rel(Σ_X)×Rel(Σ_Y)→Rel(Σ_{X∪Y})

**description:** Product restricted by a total two-valued predicate, including comparable-attribute theta comparisons.

**precondition:** X∩Y=∅; P:Tup(Σ_{X∪Y})→Prop; comparisons are defined on all operand pairs.

**postcondition:** r⋈_P s=select(P,r×s). Both input blocks remain in the output; equijoin does not automatically remove a column.

**totality:** total mathematical operation on the stated compatible carriers

<a id="node-urn-csabs-operation-DatabaseRelation-divide"></a>

### divide

`urn:csabs:operation/DatabaseRelation-divide`

**signature:** ÷ : Rel(Σ_{X∪Y})×Rel(Σ_Y)→Rel(Σ_X)

**description:** Observed X-tuples paired in the dividend with every tuple of the divisor.

**precondition:** X∩Y=∅; divisor schema matches the Y block, with identical domains and equality.

**postcondition:** R÷S={x∈π_X(R):∀y∈S,x⊕y∈R}. Empty S gives π_X(R); empty R gives empty even if S is empty.

**totality:** total mathematical operation on the stated compatible carriers

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

<a id="node-urn-csabs-axiom-DatabaseRelation-codd-set-operations"></a>

### codd-set-operations

`urn:csabs:axiom/DatabaseRelation-codd-set-operations`

**statement:** Intersection, difference and expanded product use finite set membership.

**description:** Intersection, difference and expanded product use finite set membership.

**formalStatement:** t∈r∩s ⇔ t∈r∧t∈s; t∈r−s ⇔ t∈r∧t∉s; t∈r×s ⇔ t|X∈r∧t|Y∈s

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** defining-rule

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §2.3.1, printed pp.7–8

**sourceNote:** Adapts Codd’s union-compatible positional relations to identical named schemas, with disjoint attribute blocks for expanded product.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DatabaseRelation-codd-theta-join"></a>

### codd-theta-join

`urn:csabs:axiom/DatabaseRelation-codd-theta-join`

**statement:** Theta join is selection over expanded product.

**description:** Theta join is selection over expanded product.

**formalStatement:** r⋈_P s=select(P,r×s); t∈r⋈_P s ⇔ t|X∈r∧t|Y∈s∧P(t)

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** defining-rule

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §2.3.3, printed p.10; §2.3.5, printed p.13

**sourceNote:** Generalizes Codd’s defined true/false comparisons to an arbitrary total two-valued predicate; keeps both blocks, unlike natural join.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DatabaseRelation-codd-division"></a>

### codd-division

`urn:csabs:axiom/DatabaseRelation-codd-division`

**statement:** Division universally checks the divisor, restricted to observed candidates.

**description:** Division universally checks the divisor, restricted to observed candidates.

**formalStatement:** R÷S={x∈π_X(R):∀y∈S,x⊕y∈R}

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** defining-rule

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §2.3.4, printed pp.11–12

**sourceNote:** Uses the observed-candidate restriction in Codd’s division. Adapts complementary positional coordinates to disjoint named blocks. No extension to all possible domain tuples when S is empty.

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

<a id="node-urn-csabs-law-DatabaseRelation-division-empty"></a>

### division-empty

`urn:csabs:law/DatabaseRelation-division-empty`

**statement:** Empty divisor returns observed projection; empty dividend returns empty.

**description:** Empty divisor returns observed projection; empty dividend returns empty.

**formalStatement:** R÷∅=π_X(R); ∅÷S=∅, including S=∅

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** derived-result

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §2.3.4, printed pp.11–12

**sourceNote:** The empty-dividend case is explicitly discussed by Codd; the empty-divisor case follows from the same definition.

**provenanceKind:** derived

**dependsOn:** [codd-division](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-division)

**proofSketch:** With no divisor tuple, the universal test is vacuous. With no dividend tuple, the candidate projection is empty.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} {B : Type v} (r : Finset (A × B)) (s : Finset B), Catalog.RelationalAlgebra.divide r (∅ : Finset B) = Catalog.RelationalAlgebra.projectLeft r ∧ Catalog.RelationalAlgebra.divide (∅ : Finset (A × B)) s = ∅
```

**Source:** [`Catalog.RelationalAlgebra.division_empty`](../lean/Catalog/RelationalAlgebra.lean); consulted 2026-11-27.

**Scope:** registered-witness-type

**Interpretation:** A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.

**Limits:** Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DatabaseRelation-codd-division": "Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality."
}
```

<a id="node-urn-csabs-law-DatabaseRelation-division-elimination"></a>

### division-elimination

`urn:csabs:law/DatabaseRelation-division-elimination`

**statement:** Division is definable using projection, product and difference.

**description:** Division is definable using projection, product and difference.

**formalStatement:** R÷S=π_X(R)−π_X((π_X(R)×S)−R)

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** derived-result

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §2.3.4, printed p.12, displayed elimination formula

**sourceNote:** Adapts the displayed division elimination to named disjoint blocks, retaining observed candidates.

**provenanceKind:** derived

**dependsOn:** [codd-set-operations](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-set-operations); [codd-division](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-division); [projection](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-projection)

**proofSketch:** An observed x is removed exactly when some y∈S has x⊕y missing from R. Its survival is therefore the universal division condition.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} {B : Type v} (r : Finset (A × B)) (s : Finset B), Catalog.RelationalAlgebra.divide r s = Catalog.RelationalAlgebra.difference (Catalog.RelationalAlgebra.projectLeft r) (Catalog.RelationalAlgebra.projectLeft (Catalog.RelationalAlgebra.difference (Catalog.RelationalAlgebra.product (Catalog.RelationalAlgebra.projectLeft r) s) r))
```

**Source:** [`Catalog.RelationalAlgebra.division_elimination`](../lean/Catalog/RelationalAlgebra.lean); consulted 2026-11-27.

**Scope:** registered-witness-type

**Interpretation:** A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.

**Limits:** Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DatabaseRelation-codd-division": "Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.",
  "urn:csabs:axiom/DatabaseRelation-codd-set-operations": "Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.",
  "urn:csabs:axiom/DatabaseRelation-projection": "Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality."
}
```

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

<a id="node-urn-csabs-theorem-DatabaseRelation-codd-model-satisfaction"></a>

### codd-model-satisfaction

`urn:csabs:theorem/DatabaseRelation-codd-model-satisfaction`

**statement:** A finite-set tuple-block interpretation satisfies the added Codd operation basis.

**description:** A finite-set tuple-block interpretation satisfies the added Codd operation basis.

**formalStatement:** For arbitrary tuple carriers A=Tup(X), B=Tup(Y), finite-set intersection, difference, product, predicate filtering and observed-projection division satisfy DatabaseRelation-codd-set-operations, DatabaseRelation-codd-theta-join and DatabaseRelation-codd-division.

**assumptions:** Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted.

**ruleRole:** derived-result

**reviewStatus:** editorial formulation; compiler evidence is scoped to the registered Lean mapping

**notationLanguage:** informal mathematical Unicode

**source:** [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §§2.3.1,2.3.3–2.3.5, printed pp.7–13

**sourceNote:** Locally constructed model-satisfaction result, derived from the consulted definitions. Codd does not state a Lean theorem.

**provenanceKind:** derived

**dependsOn:** [codd-set-operations](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-set-operations); [codd-theta-join](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-theta-join); [codd-division](DatabaseRelation.md#node-urn-csabs-axiom-DatabaseRelation-codd-division)

**proofSketch:** Instantiate relation carriers with Finset A, Finset B and Finset(A×B). Finset membership, filtering and image give the five equations; Finset guarantees finiteness. A×B models whole tuple-block concatenation, not two atomic SQL columns.

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} {B : Type v} (r t : Finset A) (s : Finset B) (q : Finset (A × B)) (p : A × B → Prop) (x : A) (y : B), (x ∈ Catalog.RelationalAlgebra.intersection r t ↔ x ∈ r ∧ x ∈ t) ∧ (x ∈ Catalog.RelationalAlgebra.difference r t ↔ x ∈ r ∧ x ∉ t) ∧ ((x, y) ∈ Catalog.RelationalAlgebra.product r s ↔ x ∈ r ∧ y ∈ s) ∧ ((x, y) ∈ Catalog.RelationalAlgebra.thetaJoin p r s ↔ x ∈ r ∧ y ∈ s ∧ p (x, y)) ∧ (x ∈ Catalog.RelationalAlgebra.divide q s ↔ x ∈ Catalog.RelationalAlgebra.projectLeft q ∧ ∀ z ∈ s, (x, z) ∈ q)
```

**Source:** [`Catalog.RelationalAlgebra.model_satisfaction`](../lean/Catalog/RelationalAlgebra.lean); consulted 2026-11-27.

**Scope:** registered-witness-type

**Interpretation:** A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.

**Limits:** Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DatabaseRelation-codd-division": "This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction.",
  "urn:csabs:axiom/DatabaseRelation-codd-set-operations": "This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction.",
  "urn:csabs:axiom/DatabaseRelation-codd-theta-join": "This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction."
}
```

## Concept provenance

- [Abiteboul, Hull and Vianu: Foundations of Databases (1995), author-hosted book](https://webdam.di.ens.fr/Alice/pdfs/all.pdf); accessedOn: 2026-11-07; sourceRole: primary reference for selected mathematical interfaces
- [E. F. Codd, Relational Completeness of Data Base Sublanguages (1972)](https://db.dobo.sk/wp-content/uploads/2015/11/Codd_1972_Relational_Completeness.pdf); citation: E. F. Codd. Relational Completeness of Data Base Sublanguages. IBM Research Report RJ987, March 6, 1972.; accessedOn: 2026-11-27; sourceRole: primary mathematical definitions

**sourceLocator:** §§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57; Codd1972 §§2.3.1–2.3.5, printed pp.7–13

**sourceNote:** Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Codd operations use disjoint named attribute blocks and total predicates. Codd1972 empty positional projection lists mean identity (§2.3.2); here projection onto no attributes retains the existing empty-tuple image convention. This is an explicit named-schema adaptation, not an exact positional transcription.

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
      "urn:csabs:category/associative-collections"
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
      "urn:csabs:operation/DatabaseRelation-naturalJoin",
      "urn:csabs:operation/DatabaseRelation-intersection",
      "urn:csabs:operation/DatabaseRelation-difference",
      "urn:csabs:operation/DatabaseRelation-cartesianProduct",
      "urn:csabs:operation/DatabaseRelation-thetaJoin",
      "urn:csabs:operation/DatabaseRelation-divide"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DatabaseRelation-set-interface",
      "urn:csabs:axiom/DatabaseRelation-projection",
      "urn:csabs:axiom/DatabaseRelation-relational-algebra",
      "urn:csabs:axiom/DatabaseRelation-codd-set-operations",
      "urn:csabs:axiom/DatabaseRelation-codd-theta-join",
      "urn:csabs:axiom/DatabaseRelation-codd-division"
    ],
    "hasLaw": [
      "urn:csabs:law/DatabaseRelation-selection-composition",
      "urn:csabs:law/DatabaseRelation-projection-union",
      "urn:csabs:law/DatabaseRelation-division-empty",
      "urn:csabs:law/DatabaseRelation-division-elimination"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DatabaseRelation-projection-composition",
      "urn:csabs:theorem/DatabaseRelation-fd-lossless-decomposition",
      "urn:csabs:theorem/DatabaseRelation-codd-model-satisfaction"
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
    "axiomBasis": "Selected defining presentation: Relations are finite tuple sets with extensional equality. Projection is the set image of tuple restriction. Union, selection and natural join are set operations on compatible tuple carriers. The added Codd basis defines intersection, difference, expanded product, total-predicate theta join and observed-candidate division by the linked membership equations.",
    "basisKind": "defined-structure",
    "basisScope": "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants.",
    "source": [
      "urn:csabs:source/ahv-database-model",
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§§3.2–3.3, pp. 32–33; §4.4, named projection, p. 57; Codd1972 §§2.3.1–2.3.5, printed pp.7–13",
    "sourceNote": "Uses finite named relations. Projection is the image under restriction, with set rather than bag semantics. Codd operations use disjoint named attribute blocks and total predicates. Codd1972 empty positional projection lists mean identity (§2.3.2); here projection onto no attributes retains the existing empty-tuple image convention. This is an explicit named-schema adaptation, not an exact positional transcription.",
    "provenanceKind": "adapted",
    "reviewStatus": "editorial review of defining basis and selected laws, theorems and proof principles; no machine-checked proof",
    "verificationObligation": [
      "Schema Σ=(R,U,D) is fixed; V⊆U. Row equality is componentwise identity. Empty relations and zero-attribute relations are allowed. SQL bags and NULL need separate variants."
    ],
    "specializationOf": [
      "urn:csabs:concept/FiniteSet"
    ],
    "specializationNote": "Instantiate the parent element carrier A as Tup(Σ); relation values are finite subsets of that carrier. Set operations act only on relations with the same schema; projection changes the schema to its restriction.",
    "leanFormulation": "abbrev DatabaseRelation (s : RelationalSchema) := Finset (NamedTuple s)",
    "formulationSource": "urn:csabs:source/local-lean-Database",
    "formulationLocator": "Catalog.DatabaseRelation",
    "formulationScope": "model",
    "leanModelMapping": "Finset of dependent named tuples, set semantics and extensional equality; projection/join algorithms remain to be exposed.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For schema (Attr,D), Tuple=Π_a D(a) and Relation=FinSet(Tuple). Tuple equality is pointwise; duplicate rows collapse and a relation may be empty.",
    "synonyms": [
      "Codd-style finite set relation"
    ]
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
    "id": "urn:csabs:operation/DatabaseRelation-intersection",
    "type": "Operation",
    "name": "intersection",
    "signature": "∩ : Rel(Σ)×Rel(Σ)→Rel(Σ)",
    "description": "Rows occurring in both same-schema operands.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Same schema, or explicitly domain-preserving alignment to one common schema.",
    "postcondition": "t∈r∩s iff t∈r ∧ t∈s",
    "totality": "total mathematical operation on the stated compatible carriers"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-difference",
    "type": "Operation",
    "name": "difference",
    "signature": "− : Rel(Σ)×Rel(Σ)→Rel(Σ)",
    "description": "Rows in the first operand but not the second.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "Same schema, or explicitly domain-preserving alignment to one common schema.",
    "postcondition": "t∈r−s iff t∈r ∧ t∉s",
    "totality": "total mathematical operation on the stated compatible carriers"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-cartesianProduct",
    "type": "Operation",
    "name": "cartesianProduct",
    "signature": "× : Rel(Σ_X)×Rel(Σ_Y)→Rel(Σ_{X∪Y})",
    "description": "Expanded Cartesian product concatenating disjoint named tuple blocks.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "X∩Y=∅; output retains the domains of both blocks. Rename colliding attributes first.",
    "postcondition": "t∈r×s iff t|X∈r ∧ t|Y∈s; an empty operand yields empty.",
    "totality": "total mathematical operation on the stated compatible carriers"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-thetaJoin",
    "type": "Operation",
    "name": "thetaJoin",
    "signature": "⋈_P : Rel(Σ_X)×Rel(Σ_Y)→Rel(Σ_{X∪Y})",
    "description": "Product restricted by a total two-valued predicate, including comparable-attribute theta comparisons.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "X∩Y=∅; P:Tup(Σ_{X∪Y})→Prop; comparisons are defined on all operand pairs.",
    "postcondition": "r⋈_P s=select(P,r×s). Both input blocks remain in the output; equijoin does not automatically remove a column.",
    "totality": "total mathematical operation on the stated compatible carriers"
  },
  {
    "id": "urn:csabs:operation/DatabaseRelation-divide",
    "type": "Operation",
    "name": "divide",
    "signature": "÷ : Rel(Σ_{X∪Y})×Rel(Σ_Y)→Rel(Σ_X)",
    "description": "Observed X-tuples paired in the dividend with every tuple of the divisor.",
    "concept": "urn:csabs:concept/DatabaseRelation",
    "precondition": "X∩Y=∅; divisor schema matches the Y block, with identical domains and equality.",
    "postcondition": "R÷S={x∈π_X(R):∀y∈S,x⊕y∈R}. Empty S gives π_X(R); empty R gives empty even if S is empty.",
    "totality": "total mathematical operation on the stated compatible carriers"
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
    "id": "urn:csabs:axiom/DatabaseRelation-codd-set-operations",
    "type": "Axiom",
    "name": "codd-set-operations",
    "statement": "Intersection, difference and expanded product use finite set membership.",
    "description": "Intersection, difference and expanded product use finite set membership.",
    "formalStatement": "t∈r∩s ⇔ t∈r∧t∈s; t∈r−s ⇔ t∈r∧t∉s; t∈r×s ⇔ t|X∈r∧t|Y∈s",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§2.3.1, printed pp.7–8",
    "sourceNote": "Adapts Codd’s union-compatible positional relations to identical named schemas, with disjoint attribute blocks for expanded product.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DatabaseRelation-codd-theta-join",
    "type": "Axiom",
    "name": "codd-theta-join",
    "statement": "Theta join is selection over expanded product.",
    "description": "Theta join is selection over expanded product.",
    "formalStatement": "r⋈_P s=select(P,r×s); t∈r⋈_P s ⇔ t|X∈r∧t|Y∈s∧P(t)",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§2.3.3, printed p.10; §2.3.5, printed p.13",
    "sourceNote": "Generalizes Codd’s defined true/false comparisons to an arbitrary total two-valued predicate; keeps both blocks, unlike natural join.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DatabaseRelation-codd-division",
    "type": "Axiom",
    "name": "codd-division",
    "statement": "Division universally checks the divisor, restricted to observed candidates.",
    "description": "Division universally checks the divisor, restricted to observed candidates.",
    "formalStatement": "R÷S={x∈π_X(R):∀y∈S,x⊕y∈R}",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§2.3.4, printed pp.11–12",
    "sourceNote": "Uses the observed-candidate restriction in Codd’s division. Adapts complementary positional coordinates to disjoint named blocks. No extension to all possible domain tuples when S is empty.",
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
    "id": "urn:csabs:law/DatabaseRelation-division-empty",
    "type": "Law",
    "name": "division-empty",
    "statement": "Empty divisor returns observed projection; empty dividend returns empty.",
    "description": "Empty divisor returns observed projection; empty dividend returns empty.",
    "formalStatement": "R÷∅=π_X(R); ∅÷S=∅, including S=∅",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§2.3.4, printed pp.11–12",
    "sourceNote": "The empty-dividend case is explicitly discussed by Codd; the empty-divisor case follows from the same definition.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-codd-division"
    ],
    "proofSketch": "With no divisor tuple, the universal test is vacuous. With no dividend tuple, the candidate projection is empty.",
    "leanFormulation": "∀ {A : Type u} {B : Type v} (r : Finset (A × B)) (s : Finset B), Catalog.RelationalAlgebra.divide r (∅ : Finset B) = Catalog.RelationalAlgebra.projectLeft r ∧ Catalog.RelationalAlgebra.divide (∅ : Finset (A × B)) s = ∅",
    "formulationSource": "urn:csabs:source/local-lean-RelationalAlgebra",
    "formulationLocator": "Catalog.RelationalAlgebra.division_empty",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.",
    "leanModelLimitations": "Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DatabaseRelation-codd-division\": \"Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.\"}"
  },
  {
    "id": "urn:csabs:law/DatabaseRelation-division-elimination",
    "type": "Law",
    "name": "division-elimination",
    "statement": "Division is definable using projection, product and difference.",
    "description": "Division is definable using projection, product and difference.",
    "formalStatement": "R÷S=π_X(R)−π_X((π_X(R)×S)−R)",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§2.3.4, printed p.12, displayed elimination formula",
    "sourceNote": "Adapts the displayed division elimination to named disjoint blocks, retaining observed candidates.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-codd-set-operations",
      "urn:csabs:axiom/DatabaseRelation-codd-division",
      "urn:csabs:axiom/DatabaseRelation-projection"
    ],
    "proofSketch": "An observed x is removed exactly when some y∈S has x⊕y missing from R. Its survival is therefore the universal division condition.",
    "leanFormulation": "∀ {A : Type u} {B : Type v} (r : Finset (A × B)) (s : Finset B), Catalog.RelationalAlgebra.divide r s = Catalog.RelationalAlgebra.difference (Catalog.RelationalAlgebra.projectLeft r) (Catalog.RelationalAlgebra.projectLeft (Catalog.RelationalAlgebra.difference (Catalog.RelationalAlgebra.product (Catalog.RelationalAlgebra.projectLeft r) s) r))",
    "formulationSource": "urn:csabs:source/local-lean-RelationalAlgebra",
    "formulationLocator": "Catalog.RelationalAlgebra.division_elimination",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.",
    "leanModelLimitations": "Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DatabaseRelation-codd-division\": \"Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.\", \"urn:csabs:axiom/DatabaseRelation-codd-set-operations\": \"Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.\", \"urn:csabs:axiom/DatabaseRelation-projection\": \"Use the stated finite-set membership/image interpretation of this premise; the conclusion follows by membership extensionality.\"}"
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
  },
  {
    "id": "urn:csabs:theorem/DatabaseRelation-codd-model-satisfaction",
    "type": "Theorem",
    "name": "codd-model-satisfaction",
    "statement": "A finite-set tuple-block interpretation satisfies the added Codd operation basis.",
    "description": "A finite-set tuple-block interpretation satisfies the added Codd operation basis.",
    "formalStatement": "For arbitrary tuple carriers A=Tup(X), B=Tup(Y), finite-set intersection, difference, product, predicate filtering and observed-projection division satisfy DatabaseRelation-codd-set-operations, DatabaseRelation-codd-theta-join and DatabaseRelation-codd-division.",
    "assumptions": [
      "Finite named tuple sets; componentwise identity equality; no NULL, duplicates or row order. Attribute blocks X and Y are disjoint, with fixed domains; rename collisions before use. P is total and two-valued. Empty relations and zero-attribute blocks are admitted."
    ],
    "appliesTo": [
      "urn:csabs:concept/DatabaseRelation"
    ],
    "ruleRole": "derived-result",
    "reviewStatus": "editorial formulation; compiler evidence is scoped to the registered Lean mapping",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/codd-1972-relational-completeness"
    ],
    "sourceLocator": "§§2.3.1,2.3.3–2.3.5, printed pp.7–13",
    "sourceNote": "Locally constructed model-satisfaction result, derived from the consulted definitions. Codd does not state a Lean theorem.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/DatabaseRelation-codd-set-operations",
      "urn:csabs:axiom/DatabaseRelation-codd-theta-join",
      "urn:csabs:axiom/DatabaseRelation-codd-division"
    ],
    "proofSketch": "Instantiate relation carriers with Finset A, Finset B and Finset(A×B). Finset membership, filtering and image give the five equations; Finset guarantees finiteness. A×B models whole tuple-block concatenation, not two atomic SQL columns.",
    "leanFormulation": "∀ {A : Type u} {B : Type v} (r t : Finset A) (s : Finset B) (q : Finset (A × B)) (p : A × B → Prop) (x : A) (y : B), (x ∈ Catalog.RelationalAlgebra.intersection r t ↔ x ∈ r ∧ x ∈ t) ∧ (x ∈ Catalog.RelationalAlgebra.difference r t ↔ x ∈ r ∧ x ∉ t) ∧ ((x, y) ∈ Catalog.RelationalAlgebra.product r s ↔ x ∈ r ∧ y ∈ s) ∧ ((x, y) ∈ Catalog.RelationalAlgebra.thetaJoin p r s ↔ x ∈ r ∧ y ∈ s ∧ p (x, y)) ∧ (x ∈ Catalog.RelationalAlgebra.divide q s ↔ x ∈ Catalog.RelationalAlgebra.projectLeft q ∧ ∀ z ∈ s, (x, z) ∈ q)",
    "formulationSource": "urn:csabs:source/local-lean-RelationalAlgebra",
    "formulationLocator": "Catalog.RelationalAlgebra.model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "A and B are whole tuples on disjoint named attribute blocks X,Y; A×B represents their concatenation via restriction/gluing. Finset gives finite relations and identity equality. projectLeft is tuple restriction image. Predicates are total two-valued propositions. All empty relations and Unit carriers for zero-attribute blocks are allowed.",
    "leanModelLimitations": "Partial tuple-block model of the added operation basis, not a proof of every legacy DatabaseRelation claim or a schema transport implementation. Requires disjoint attributes and compatible domains. Classical noncomputable operations; no SQL bags, NULL, outer joins, ordering, aggregation or query engine refinement.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DatabaseRelation-codd-division\": \"This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction.\", \"urn:csabs:axiom/DatabaseRelation-codd-set-operations\": \"This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction.\", \"urn:csabs:axiom/DatabaseRelation-codd-theta-join\": \"This defining equation is a proved obligation of the concrete finite-set interpretation, not a hypothesis assuming its own satisfaction.\"}"
  }
]
```
<!-- graph-record:end -->
