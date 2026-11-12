# Finite database relation under bag semantics

A finite multiset of well-typed named tuples over a fixed relational schema.

**Notation:** BagRel(S)=Multiset(Tuple(S))

**Stable ID:** `urn:csabs:concept/BagRelation`

**Categories:** Relational data modelling

**Kind:** Abstract data type

**Prerequisites:** [Named relational schema with attribute domains](RelationalSchema.md), [Multiset](Multiset.md), [Finite database relation under set semantics](DatabaseRelation.md)

**Specializes:** [Multiset](Multiset.md)

## Mathematical formulation

For schema s, BagRelation(s)=Multiset(Π\_a D(a)). Equality compares each tuple's multiplicity and bag union adds multiplicities; row order is not observable.

**Lean formulation** (in its source module context):

```lean
abbrev BagRelation (s : RelationalSchema) := _root_.Multiset (Catalog.NamedTuple s)
```

**Source:** [`Catalog.BagRelation`](../lean/Catalog/InformationData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** BagRel(S)=Multiset(Tuple(S)). No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** count(R,t) has finite support in t; R=T iff ∀t,count(R,t)=count(T,t); count(unionAll(R,T),t)=count(R,t)+count(T,t); count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t); count(select_P(R),t)=count(R,t) if P(t), else 0

**basisKind:** extensional-structural-definition

**basisScope:** No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**specializationNote:** Instantiate Multiset at the dependent named-tuple carrier of S. unionAll is multiset additive union ⊎; count, empty, insert and remove keep their occurrence-count meanings. Projection and selection are additional typed operations. All reused axioms have explicit applicability; the hierarchy alone transfers no rule.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BagRelation-multiplicity"></a>

### multiplicity

`urn:csabs:operation/BagRelation-multiplicity`

**signature:** count : BagRel(S)×Tuple(S)→ℕ

**description:** Number of occurrences of a row.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Number of occurrences of a row.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BagRelation-union-all"></a>

### union-all

`urn:csabs:operation/BagRelation-union-all`

**signature:** unionAll : BagRel(S)²→BagRel(S)

**description:** Adds row multiplicities.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Adds row multiplicities.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BagRelation-project"></a>

### project

`urn:csabs:operation/BagRelation-project`

**signature:** project_X : BagRel(S)→BagRel(S|X), X⊆attrs(S)

**description:** Projection sums counts over original rows with the same restriction.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Projection sums counts over original rows with the same restriction.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-BagRelation-select"></a>

### select

`urn:csabs:operation/BagRelation-select`

**signature:** select_P : BagRel(S)→BagRel(S)

**description:** Keeps a row with its count iff the total two-valued predicate P holds.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Keeps a row with its count iff the total two-valued predicate P holds.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Multiset-finite-support"></a>

### finite-support

`urn:csabs:axiom/Multiset-finite-support`

**statement:** A bag is a natural multiplicity function with finite support.

**formalStatement:** Bag(A)={m:A→ℕ:support(m)={x:m(x)>0} is finite}

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Multiset-count-extensionality"></a>

### count-extensionality

`urn:csabs:axiom/Multiset-count-extensionality`

**statement:** Bags are equal exactly when multiplicities agree.

**formalStatement:** m=n iff ∀x:count(m,x)=count(n,x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-Multiset-operations"></a>

### operations

`urn:csabs:axiom/Multiset-operations`

**statement:** Insertion, removal, and union are defined pointwise.

**formalStatement:** count(empty,x)=0; count(insert(m,a),x)=count(m,x)+[x=a]; count(remove(m,a),x)=max(0,count(m,x)−[x=a]); count(m⊎n,x)=count(m,x)+count(n,x)

**assumptions:** All variables range over the carriers and semantic conventions specified in this concept.

**ruleRole:** defining-rule

**reviewStatus:** editorial-summary; not machine-proved

**notationLanguage:** informal mathematical Unicode

**provenanceStatus:** legacy-source-missing

<a id="node-urn-csabs-axiom-BagRelation-project-count"></a>

### project-count

`urn:csabs:axiom/BagRelation-project-count`

**statement:** Defining requirement: count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t)

**formalStatement:** count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t)

**assumptions:** No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-BagRelation-selection-count"></a>

### selection-count

`urn:csabs:axiom/BagRelation-selection-count`

**statement:** Defining requirement: count(select_P(R),t)=count(R,t) if P(t), else 0

**formalStatement:** count(select_P(R),t)=count(R,t) if P(t), else 0

**assumptions:** No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-BagRelation-union-commutative"></a>

### union-commutative

`urn:csabs:law/BagRelation-union-commutative`

**statement:** unionAll(R,T)=unionAll(T,R)

**formalStatement:** unionAll(R,T)=unionAll(T,R)

**assumptions:** No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-support](Multiset.md#node-urn-csabs-axiom-Multiset-finite-support); [count-extensionality](Multiset.md#node-urn-csabs-axiom-Multiset-count-extensionality); [operations](Multiset.md#node-urn-csabs-axiom-Multiset-operations)

**proofSketch:** Row counts agree by natural addition commutativity; use bag extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {s : Catalog.RelationalSchema} (r t : Catalog.BagRelation s), r + t = t + r
```

**Source:** [`Catalog.InformationDataProofs.bag_union_commutes`](../lean/Catalog/InformationData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/Multiset-count-extensionality": "Interpreted premise: m=n iff ∀x:count(m,x)=count(n,x). NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.",
  "urn:csabs:axiom/Multiset-finite-support": "Interpreted premise: Bag(A)={m:A→ℕ:support(m)={x:m(x)>0} is finite}. NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.",
  "urn:csabs:axiom/Multiset-operations": "Interpreted premise: count(empty,x)=0; count(insert(m,a),x)=count(m,x)+[x=a]; count(remove(m,a),x)=max(0,count(m,x)−[x=a]); count(m⊎n,x)=count(m,x)+count(n,x). NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law."
}
```

## Theorems

<a id="node-urn-csabs-theorem-BagRelation-projection-cardinality"></a>

### projection-cardinality

`urn:csabs:theorem/BagRelation-projection-cardinality`

**statement:** |project_X(R)|=|R|, counting multiplicities

**formalStatement:** |project_X(R)|=|R|, counting multiplicities

**assumptions:** No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [finite-support](Multiset.md#node-urn-csabs-axiom-Multiset-finite-support); [count-extensionality](Multiset.md#node-urn-csabs-axiom-Multiset-count-extensionality); [project-count](BagRelation.md#node-urn-csabs-axiom-BagRelation-project-count)

**proofSketch:** Each original occurrence contributes exactly once to its restricted row; regroup the finite sum by the projection fibers.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Mathlib pinned definitions: Data/Multiset/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Multiset/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Multiset as lists modulo permutation; count, addition, cardinality

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BagRelation",
    "type": "Concept",
    "shortForm": "BagRelation",
    "fullName": "Finite database relation under bag semantics",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite multiset of well-typed named tuples over a fixed relational schema.",
    "notation": "BagRel(S)=Multiset(Tuple(S))",
    "requiresConcept": [
      "urn:csabs:concept/RelationalSchema",
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/DatabaseRelation"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/BagRelation-multiplicity",
      "urn:csabs:operation/BagRelation-union-all",
      "urn:csabs:operation/BagRelation-project",
      "urn:csabs:operation/BagRelation-select"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/Multiset-operations",
      "urn:csabs:axiom/BagRelation-project-count",
      "urn:csabs:axiom/BagRelation-selection-count"
    ],
    "hasLaw": [
      "urn:csabs:law/BagRelation-union-commutative"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/BagRelation-projection-cardinality"
    ],
    "axiomBasis": "count(R,t) has finite support in t; R=T iff ∀t,count(R,t)=count(T,t); count(unionAll(R,T),t)=count(R,t)+count(T,t); count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t); count(select_P(R),t)=count(R,t) if P(t), else 0",
    "basisKind": "extensional-structural-definition",
    "basisScope": "No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Multiset"
    ],
    "specializationNote": "Instantiate Multiset at the dependent named-tuple carrier of S. unionAll is multiset additive union ⊎; count, empty, insert and remove keep their occurrence-count meanings. Projection and selection are additional typed operations. All reused axioms have explicit applicability; the hierarchy alone transfers no rule.",
    "leanFormulation": "abbrev BagRelation (s : RelationalSchema) := _root_.Multiset (Catalog.NamedTuple s)",
    "formulationSource": "urn:csabs:source/local-lean-InformationData",
    "formulationLocator": "Catalog.BagRelation",
    "formulationScope": "model",
    "leanModelMapping": "BagRel(S)=Multiset(Tuple(S)). No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "For schema s, BagRelation(s)=Multiset(Π_a D(a)). Equality compares each tuple's multiplicity and bag union adds multiplicities; row order is not observable."
  },
  {
    "id": "urn:csabs:operation/BagRelation-multiplicity",
    "type": "Operation",
    "name": "multiplicity",
    "signature": "count : BagRel(S)×Tuple(S)→ℕ",
    "description": "Number of occurrences of a row.",
    "concept": "urn:csabs:concept/BagRelation",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Number of occurrences of a row.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BagRelation-union-all",
    "type": "Operation",
    "name": "union-all",
    "signature": "unionAll : BagRel(S)²→BagRel(S)",
    "description": "Adds row multiplicities.",
    "concept": "urn:csabs:concept/BagRelation",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Adds row multiplicities.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BagRelation-project",
    "type": "Operation",
    "name": "project",
    "signature": "project_X : BagRel(S)→BagRel(S|X), X⊆attrs(S)",
    "description": "Projection sums counts over original rows with the same restriction.",
    "concept": "urn:csabs:concept/BagRelation",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Projection sums counts over original rows with the same restriction.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/BagRelation-select",
    "type": "Operation",
    "name": "select",
    "signature": "select_P : BagRel(S)→BagRel(S)",
    "description": "Keeps a row with its count iff the total two-valued predicate P holds.",
    "concept": "urn:csabs:concept/BagRelation",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Keeps a row with its count iff the total two-valued predicate P holds.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Multiset-finite-support",
    "type": "Axiom",
    "name": "finite-support",
    "statement": "A bag is a natural multiplicity function with finite support.",
    "formalStatement": "Bag(A)={m:A→ℕ:support(m)={x:m(x)>0} is finite}",
    "appliesTo": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/BagRelation"
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
    "id": "urn:csabs:axiom/Multiset-count-extensionality",
    "type": "Axiom",
    "name": "count-extensionality",
    "statement": "Bags are equal exactly when multiplicities agree.",
    "formalStatement": "m=n iff ∀x:count(m,x)=count(n,x)",
    "appliesTo": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/BagRelation"
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
    "id": "urn:csabs:axiom/Multiset-operations",
    "type": "Axiom",
    "name": "operations",
    "statement": "Insertion, removal, and union are defined pointwise.",
    "formalStatement": "count(empty,x)=0; count(insert(m,a),x)=count(m,x)+[x=a]; count(remove(m,a),x)=max(0,count(m,x)−[x=a]); count(m⊎n,x)=count(m,x)+count(n,x)",
    "appliesTo": [
      "urn:csabs:concept/Multiset",
      "urn:csabs:concept/BagRelation"
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
    "id": "urn:csabs:axiom/BagRelation-project-count",
    "type": "Axiom",
    "name": "project-count",
    "statement": "Defining requirement: count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t)",
    "formalStatement": "count(project_X(R),u)=Σ{t∈supp(R) | t|X=u}count(R,t)",
    "assumptions": [
      "No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BagRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/BagRelation-selection-count",
    "type": "Axiom",
    "name": "selection-count",
    "statement": "Defining requirement: count(select_P(R),t)=count(R,t) if P(t), else 0",
    "formalStatement": "count(select_P(R),t)=count(R,t) if P(t), else 0",
    "assumptions": [
      "No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/BagRelation"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/BagRelation-union-commutative",
    "type": "Law",
    "name": "union-commutative",
    "statement": "unionAll(R,T)=unionAll(T,R)",
    "formalStatement": "unionAll(R,T)=unionAll(T,R)",
    "assumptions": [
      "No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BagRelation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/Multiset-operations"
    ],
    "proofSketch": "Row counts agree by natural addition commutativity; use bag extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {s : Catalog.RelationalSchema} (r t : Catalog.BagRelation s), r + t = t + r",
    "formulationSource": "urn:csabs:source/local-lean-InformationData",
    "formulationLocator": "Catalog.InformationDataProofs.bag_union_commutes",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/Multiset-count-extensionality\": \"Interpreted premise: m=n iff ∀x:count(m,x)=count(n,x). NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.\", \"urn:csabs:axiom/Multiset-finite-support\": \"Interpreted premise: Bag(A)={m:A→ℕ:support(m)={x:m(x)>0} is finite}. NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.\", \"urn:csabs:axiom/Multiset-operations\": \"Interpreted premise: count(empty,x)=0; count(insert(m,a),x)=count(m,x)+[x=a]; count(remove(m,a),x)=max(0,count(m,x)−[x=a]); count(m⊎n,x)=count(m,x)+count(n,x). NamedTuple s is the dependent tuple carrier; BagRelation is Multiset of tuples, modulo row permutation. + means occurrence-additive unionAll, not max union; add_comm is the multiset additive law.\"}"
  },
  {
    "id": "urn:csabs:theorem/BagRelation-projection-cardinality",
    "type": "Theorem",
    "name": "projection-cardinality",
    "statement": "|project_X(R)|=|R|, counting multiplicities",
    "formalStatement": "|project_X(R)|=|R|, counting multiplicities",
    "assumptions": [
      "No tuple ordering; equal rows retain natural-number multiplicity. No SQL NULL, three-valued predicates, ordering or aggregation overflow. Schema fixed; projection adds multiplicities when distinct rows collapse.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/BagRelation"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Multiset-finite-support",
      "urn:csabs:axiom/Multiset-count-extensionality",
      "urn:csabs:axiom/BagRelation-project-count"
    ],
    "proofSketch": "Each original occurrence contributes exactly once to its restricted row; regroup the finite sum by the projection fibers.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/mathlib-bag-core"
    ],
    "sourceLocator": "Multiset as lists modulo permutation; count, addition, cardinality",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
