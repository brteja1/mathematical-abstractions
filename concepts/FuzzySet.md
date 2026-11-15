# Fuzzy set (unit-interval membership, min/max profile)

A total membership function from a fixed universe X into the real unit interval, with pointwise equality, order, min/max operations and standard complement. Degrees need not sum to one and do not denote probabilities.

**Notation:** F(X)=X→[0,1]; A≤B ⇔ ∀x, μ_A(x)≤μ_B(x).

**Stable ID:** `urn:csabs:concept/FuzzySet`

**Categories:** Logic and proof → Fuzzy logic

**Kind:** Mathematical structure

**Prerequisites:** [Exact real number](RealNumber.md), [Total function](Function.md)

**Specializes:** [Lattice](Lattice.md)

**Related concepts:** [Set](Set.md), [Boolean algebra](BooleanAlgebra.md)

## Backlinks

- [Triangular conorm (t-conorm)](TConorm.md) — `relatedConcept`
- [Triangular norm (t-norm)](TNorm.md) — `relatedConcept`

## Mathematical formulation

F(X)=X→[0,1]; A≤B ⇔ ∀x, μ\_A(x)≤μ\_B(x). X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**Lean formulation** (in its source module context):

```lean
abbrev FuzzySet (A : Type u) := A → FuzzyDegree
```

**Source:** [`Catalog.FuzzySet`](../lean/Catalog/FuzzyLogic.lean); consulted 2026-11-15.

**Scope:** model

**Interpretation:** X→{r:ℝ // 0≤r ∧ r≤1}; function equality is extensional. The module supplies constants, min/max, complement and weak alphaCut. Empty X is allowed.

**Limits:** Exact carrier and selected operations only; no claim in this entry is registered as a compiled proof witness. No approximate membership or probabilistic interpretation.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Membership representation and extensionality; pointwise definitions of order, bounds, min/max and complement; weak alpha-cut rule.

**basisKind:** defined-structure

**basisScope:** The selected exact real profile and listed operations and results; no completeness claim.

**convention:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**specializationNote:** Instantiate Lattice carrier with X→[0,1], equality with pointwise equality, order pointwise, meet with pointwise min and join with pointwise max. Bounds are constant 0 and 1. Standard complement need not be a Boolean complement. Explicit rules below establish applicability.

**verificationObligation:** Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.; Specialization and prerequisites do not transfer claims automatically.

**reviewStatus:** Editorial mathematical review; Lean model coverage is separate from claim proof coverage.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FuzzySet-membership"></a>

### membership

`urn:csabs:operation/FuzzySet-membership`

**signature:** F(X) × X → [0,1]

**description:** Evaluate μ_A(x).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Evaluate μ_A(x).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-empty"></a>

### empty

`urn:csabs:operation/FuzzySet-empty`

**signature:** 1 → F(X)

**description:** Return the constant-zero membership function.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return the constant-zero membership function.

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-full"></a>

### full

`urn:csabs:operation/FuzzySet-full`

**signature:** 1 → F(X)

**description:** Return the constant-one membership function.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return the constant-one membership function.

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-intersection"></a>

### intersection

`urn:csabs:operation/FuzzySet-intersection`

**signature:** F(X)² → F(X)

**description:** Return μ(x)=min(μ_A(x),μ_B(x)).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return μ(x)=min(μ_A(x),μ_B(x)).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-union"></a>

### union

`urn:csabs:operation/FuzzySet-union`

**signature:** F(X)² → F(X)

**description:** Return μ(x)=max(μ_A(x),μ_B(x)).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return μ(x)=max(μ_A(x),μ_B(x)).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-complement"></a>

### complement

`urn:csabs:operation/FuzzySet-complement`

**signature:** F(X) → F(X)

**description:** Return μ(x)=1−μ_A(x).

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return μ(x)=1−μ_A(x).

**totality:** total on the stated typed domain

<a id="node-urn-csabs-operation-FuzzySet-alpha-cut"></a>

### alpha-cut

`urn:csabs:operation/FuzzySet-alpha-cut`

**signature:** F(X) × [0,1] → 𝒫(X)

**description:** Return the weak cut {x∈X: α≤μ_A(x)}. At α=0 the result is X, including zero-membership points; strong cuts use > and are a separate convention.

**precondition:** Arguments have the displayed types; all degree inputs are in the closed real unit interval.

**postcondition:** Return the weak cut {x∈X: α≤μ_A(x)}. At α=0 the result is X, including zero-membership points; strong cuts use > and are a separate convention.

**totality:** total on the stated typed domain

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FuzzySet-extensionality"></a>

### extensionality

`urn:csabs:axiom/FuzzySet-extensionality`

**statement:** Membership determines equality and containment.

**description:** Membership determines equality and containment.

**formalStatement:** A=B ⇔ ∀x∈X, μ_A(x)=μ_B(x); A≤B ⇔ ∀x∈X, μ_A(x)≤μ_B(x).

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §II p.340, equality and containment (2)

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-FuzzySet-pointwise-operations"></a>

### pointwise-operations

`urn:csabs:axiom/FuzzySet-pointwise-operations`

**statement:** Bounds, intersection, union and standard complement are defined pointwise.

**description:** Bounds, intersection, union and standard complement are defined pointwise.

**formalStatement:** μ_0(x)=0; μ_1(x)=1; μ_(A∩B)(x)=min(μ_A(x),μ_B(x)); μ_(A∪B)(x)=max(μ_A(x),μ_B(x)); μ_(¬A)(x)=1−μ_A(x).

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §II pp.340–341, (1), (3), (5)

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-FuzzySet-weak-cut"></a>

### weak-cut

`urn:csabs:axiom/FuzzySet-weak-cut`

**statement:** The selected alpha cut uses a non-strict threshold.

**description:** The selected alpha cut uses a non-strict threshold.

**formalStatement:** A_α={x∈X: μ_A(x)≥α}, α∈[0,1]; A_0=X.

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §V p.347, level sets (24); extended here to arbitrary X and α=0

**sourceNote:** Defining constraints adapted to the chosen typed interface.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

<a id="node-urn-csabs-law-FuzzySet-de-morgan"></a>

### de-morgan

`urn:csabs:law/FuzzySet-de-morgan`

**statement:** Standard complement interchanges min and max.

**description:** Standard complement interchanges min and max.

**formalStatement:** ¬(A∪B)=(¬A)∩(¬B); ¬(A∩B)=(¬A)∪(¬B); ¬¬A=A.

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §III p.342, (7)–(8)

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [extensionality](FuzzySet.md#node-urn-csabs-axiom-FuzzySet-extensionality); [pointwise-operations](FuzzySet.md#node-urn-csabs-axiom-FuzzySet-pointwise-operations)

**proofSketch:** At each point, u↦1−u reverses real order and is involutive; split u≤v and v≤u.

<a id="node-urn-csabs-law-FuzzySet-cut-antitone"></a>

### cut-antitone

`urn:csabs:law/FuzzySet-cut-antitone`

**statement:** Increasing the cut threshold can only remove points.

**description:** Increasing the cut threshold can only remove points.

**formalStatement:** 0≤α≤β≤1 ⇒ A_β⊆A_α.

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §V p.347, weak level-set definition (24)

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [weak-cut](FuzzySet.md#node-urn-csabs-axiom-FuzzySet-weak-cut)

**proofSketch:** If μ_A(x)≥β and β≥α, transitivity gives μ_A(x)≥α.

## Theorems

<a id="node-urn-csabs-theorem-FuzzySet-lattice-bounds"></a>

### lattice-bounds

`urn:csabs:theorem/FuzzySet-lattice-bounds`

**statement:** Min and max supply greatest lower and least upper bounds for pointwise order.

**description:** Min and max supply greatest lower and least upper bounds for pointwise order.

**formalStatement:** C≤A∩B ⇔ C≤A ∧ C≤B; A∪B≤C ⇔ A≤C ∧ B≤C; 0≤A≤1.

**assumptions:** X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.

**reviewStatus:** Editorial statement and derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §II pp.340–341, least/greatest bound arguments; §III p.343

**sourceNote:** Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.

**provenanceKind:** derived

**dependsOn:** [extensionality](FuzzySet.md#node-urn-csabs-axiom-FuzzySet-extensionality); [pointwise-operations](FuzzySet.md#node-urn-csabs-axiom-FuzzySet-pointwise-operations)

**proofSketch:** Evaluate at each x; real min is a greatest lower bound and real max a least upper bound; all memberships lie in [0,1].

## Concept provenance

- [L. A. Zadeh, Fuzzy Sets (1965)](https://people.eecs.berkeley.edu/~pister/publications/FamousPapers/Zadeh65FuzzySets.pdf); citation: Information and Control 8 (1965), 338–353. DOI: 10.1016/S0019-9958(65)90241-X.; accessedOn: 2026-11-15; sourceRole: Consulted original paper: membership, pointwise operations, lattice identities and level sets.

**sourceLocator:** §II pp.339–341; §III pp.342–343; §V level sets p.347, (24)

**sourceNote:** Adapted to exact real carriers and explicit catalog equality and definedness conventions.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FuzzySet",
    "type": "Concept",
    "shortForm": "FuzzySet",
    "fullName": "Fuzzy set (unit-interval membership, min/max profile)",
    "category": [
      "urn:csabs:category/fuzzy-logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "definition": "A total membership function from a fixed universe X into the real unit interval, with pointwise equality, order, min/max operations and standard complement. Degrees need not sum to one and do not denote probabilities.",
    "notation": "F(X)=X→[0,1]; A≤B ⇔ ∀x, μ_A(x)≤μ_B(x).",
    "mathematicalFormulation": "F(X)=X→[0,1]; A≤B ⇔ ∀x, μ_A(x)≤μ_B(x). X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.",
    "convention": "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required.",
    "hasOperation": [
      "urn:csabs:operation/FuzzySet-membership",
      "urn:csabs:operation/FuzzySet-empty",
      "urn:csabs:operation/FuzzySet-full",
      "urn:csabs:operation/FuzzySet-intersection",
      "urn:csabs:operation/FuzzySet-union",
      "urn:csabs:operation/FuzzySet-complement",
      "urn:csabs:operation/FuzzySet-alpha-cut"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FuzzySet-extensionality",
      "urn:csabs:axiom/FuzzySet-pointwise-operations",
      "urn:csabs:axiom/FuzzySet-weak-cut"
    ],
    "hasLaw": [
      "urn:csabs:law/FuzzySet-de-morgan",
      "urn:csabs:law/FuzzySet-cut-antitone"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FuzzySet-lattice-bounds"
    ],
    "axiomBasis": "Membership representation and extensionality; pointwise definitions of order, bounds, min/max and complement; weak alpha-cut rule.",
    "basisKind": "defined-structure",
    "basisScope": "The selected exact real profile and listed operations and results; no completeness claim.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical review; Lean model coverage is separate from claim proof coverage.",
    "verificationObligation": [
      "Map equality, carriers, degree bounds and exact arithmetic to the target API. Rounded operations require separate law checks.",
      "Specialization and prerequisites do not transfer claims automatically."
    ],
    "requiresConcept": [
      "urn:csabs:concept/RealNumber",
      "urn:csabs:concept/Function"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Set",
      "urn:csabs:concept/BooleanAlgebra"
    ],
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§II pp.339–341; §III pp.342–343; §V level sets p.347, (24)",
    "sourceNote": "Adapted to exact real carriers and explicit catalog equality and definedness conventions.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Lattice"
    ],
    "specializationNote": "Instantiate Lattice carrier with X→[0,1], equality with pointwise equality, order pointwise, meet with pointwise min and join with pointwise max. Bounds are constant 0 and 1. Standard complement need not be a Boolean complement. Explicit rules below establish applicability.",
    "leanFormulation": "abbrev FuzzySet (A : Type u) := A → FuzzyDegree",
    "formulationSource": "urn:csabs:source/local-lean-FuzzyLogic",
    "formulationLocator": "Catalog.FuzzySet",
    "formulationScope": "model",
    "leanModelMapping": "X→{r:ℝ // 0≤r ∧ r≤1}; function equality is extensional. The module supplies constants, min/max, complement and weak alphaCut. Empty X is allowed.",
    "leanModelLimitations": "Exact carrier and selected operations only; no claim in this entry is registered as a compiled proof witness. No approximate membership or probabilistic interpretation."
  },
  {
    "id": "urn:csabs:operation/FuzzySet-membership",
    "type": "Operation",
    "name": "membership",
    "signature": "F(X) × X → [0,1]",
    "description": "Evaluate μ_A(x).",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Evaluate μ_A(x).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-empty",
    "type": "Operation",
    "name": "empty",
    "signature": "1 → F(X)",
    "description": "Return the constant-zero membership function.",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return the constant-zero membership function.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-full",
    "type": "Operation",
    "name": "full",
    "signature": "1 → F(X)",
    "description": "Return the constant-one membership function.",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return the constant-one membership function.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-intersection",
    "type": "Operation",
    "name": "intersection",
    "signature": "F(X)² → F(X)",
    "description": "Return μ(x)=min(μ_A(x),μ_B(x)).",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return μ(x)=min(μ_A(x),μ_B(x)).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-union",
    "type": "Operation",
    "name": "union",
    "signature": "F(X)² → F(X)",
    "description": "Return μ(x)=max(μ_A(x),μ_B(x)).",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return μ(x)=max(μ_A(x),μ_B(x)).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-complement",
    "type": "Operation",
    "name": "complement",
    "signature": "F(X) → F(X)",
    "description": "Return μ(x)=1−μ_A(x).",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return μ(x)=1−μ_A(x).",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:operation/FuzzySet-alpha-cut",
    "type": "Operation",
    "name": "alpha-cut",
    "signature": "F(X) × [0,1] → 𝒫(X)",
    "description": "Return the weak cut {x∈X: α≤μ_A(x)}. At α=0 the result is X, including zero-membership points; strong cuts use > and are a separate convention.",
    "concept": "urn:csabs:concept/FuzzySet",
    "precondition": "Arguments have the displayed types; all degree inputs are in the closed real unit interval.",
    "postcondition": "Return the weak cut {x∈X: α≤μ_A(x)}. At α=0 the result is X, including zero-membership points; strong cuts use > and are a separate convention.",
    "totality": "total on the stated typed domain"
  },
  {
    "id": "urn:csabs:axiom/FuzzySet-extensionality",
    "type": "Axiom",
    "name": "extensionality",
    "statement": "Membership determines equality and containment.",
    "description": "Membership determines equality and containment.",
    "formalStatement": "A=B ⇔ ∀x∈X, μ_A(x)=μ_B(x); A≤B ⇔ ∀x∈X, μ_A(x)≤μ_B(x).",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§II p.340, equality and containment (2)",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/FuzzySet-pointwise-operations",
    "type": "Axiom",
    "name": "pointwise-operations",
    "statement": "Bounds, intersection, union and standard complement are defined pointwise.",
    "description": "Bounds, intersection, union and standard complement are defined pointwise.",
    "formalStatement": "μ_0(x)=0; μ_1(x)=1; μ_(A∩B)(x)=min(μ_A(x),μ_B(x)); μ_(A∪B)(x)=max(μ_A(x),μ_B(x)); μ_(¬A)(x)=1−μ_A(x).",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§II pp.340–341, (1), (3), (5)",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/FuzzySet-weak-cut",
    "type": "Axiom",
    "name": "weak-cut",
    "statement": "The selected alpha cut uses a non-strict threshold.",
    "description": "The selected alpha cut uses a non-strict threshold.",
    "formalStatement": "A_α={x∈X: μ_A(x)≥α}, α∈[0,1]; A_0=X.",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§V p.347, level sets (24); extended here to arbitrary X and α=0",
    "sourceNote": "Defining constraints adapted to the chosen typed interface.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:law/FuzzySet-de-morgan",
    "type": "Law",
    "name": "de-morgan",
    "statement": "Standard complement interchanges min and max.",
    "description": "Standard complement interchanges min and max.",
    "formalStatement": "¬(A∪B)=(¬A)∩(¬B); ¬(A∩B)=(¬A)∪(¬B); ¬¬A=A.",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§III p.342, (7)–(8)",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/FuzzySet-extensionality",
      "urn:csabs:axiom/FuzzySet-pointwise-operations"
    ],
    "proofSketch": "At each point, u↦1−u reverses real order and is involutive; split u≤v and v≤u."
  },
  {
    "id": "urn:csabs:law/FuzzySet-cut-antitone",
    "type": "Law",
    "name": "cut-antitone",
    "statement": "Increasing the cut threshold can only remove points.",
    "description": "Increasing the cut threshold can only remove points.",
    "formalStatement": "0≤α≤β≤1 ⇒ A_β⊆A_α.",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§V p.347, weak level-set definition (24)",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/FuzzySet-weak-cut"
    ],
    "proofSketch": "If μ_A(x)≥β and β≥α, transitivity gives μ_A(x)≥α."
  },
  {
    "id": "urn:csabs:theorem/FuzzySet-lattice-bounds",
    "type": "Theorem",
    "name": "lattice-bounds",
    "statement": "Min and max supply greatest lower and least upper bounds for pointwise order.",
    "description": "Min and max supply greatest lower and least upper bounds for pointwise order.",
    "formalStatement": "C≤A∩B ⇔ C≤A ∧ C≤B; A∪B≤C ⇔ A≤C ∧ B≤C; 0≤A≤1.",
    "assumptions": [
      "X is any fixed set, including the empty set. Equality is pointwise real equality. All operations are exact and total. Complement is 1−μ, meet is min and join is max. For X=∅ all membership functions coincide. No finite support or normalization is required."
    ],
    "appliesTo": [
      "urn:csabs:concept/FuzzySet"
    ],
    "reviewStatus": "Editorial statement and derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/zadeh-1965-fuzzy-sets"
    ],
    "sourceLocator": "§II pp.340–341, least/greatest bound arguments; §III p.343",
    "sourceNote": "Catalog derivation from the explicitly linked premises and elementary exact real arithmetic/order.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/FuzzySet-extensionality",
      "urn:csabs:axiom/FuzzySet-pointwise-operations"
    ],
    "proofSketch": "Evaluate at each x; real min is a greatest lower bound and real max a least upper bound; all memberships lie in [0,1]."
  }
]
```
<!-- graph-record:end -->
