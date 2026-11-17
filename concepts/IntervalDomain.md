# Integer interval abstract domain (empty and unbounded intervals)

The complete lattice of order-convex subsets of the mathematical integers, including the empty set, ordered by inclusion.

**Notation:** Iℤ={⊥} ∪ {[l,u]∩ℤ | l∈ℤ∪{−∞}, u∈ℤ∪{+∞}, l≤u}; γ(I)=I; I⊑J ⇔ I⊆J.

**Stable ID:** `urn:csabs:concept/IntervalDomain`

**Categories:** Data structures → Intervals, Order and fixed points, Programming-language semantics → Compiler transformations

**Kind:** Mathematical structure

**Prerequisites:** [Mathematical integers](Integer.md), [Set](Set.md)

**Specializes:** [Complete Lattice](CompleteLattice.md)

**Related concepts:** [Nonempty bounded closed interval](ClosedInterval.md), [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md), [Monotone dataflow framework (forward join profile)](MonotoneDataflow.md)

## Backlinks

- [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md) — `relatedConcept`
- [Nonempty bounded closed interval](ClosedInterval.md) — `relatedConcept`
- [Monotone dataflow framework (forward join profile)](MonotoneDataflow.md) — `relatedConcept`

## Mathematical formulation

Iℤ={⊥} ∪ {[l,u]∩ℤ | l∈ℤ∪{−∞}, u∈ℤ∪{+∞}, l≤u}; γ(I)=I; I⊑J ⇔ I⊆J. Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**Lean formulation** (in its source module context):

```lean
def IntervalDomain :=
  {s : Set Int // ∀ a ∈ s, ∀ b ∈ s, ∀ c : Int, a ≤ c → c ≤ b → c ∈ s}
```

**Source:** [`Catalog.Programs.IntervalDomain`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** partial

**Interpretation:** Subtype of Set Int satisfying integer order-convexity; equality is extensional set equality. Empty, singleton and unbounded sets are representable.

**Limits:** No Lean lattice instance, hull, abstract arithmetic or widening implementation; carrier model only. No proof witnesses registered.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Order-convex integer subsets; hull abstraction and identity concretization; arbitrary intersection/hull joins; lifted addition.

**basisKind:** extensional-structural-definition

**basisScope:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**specializationNote:** Carrier Iℤ with inclusion; arbitrary meet is intersection (empty-family meet ℤ), arbitrary join is the least integer interval containing the union (empty-family join ∅). No axioms transfer through this edge.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-IntervalDomain-abstract"></a>

### abstract

`urn:csabs:operation/IntervalDomain-abstract`

**signature:** α : P(ℤ) → Iℤ

**description:** Return the least interval containing S; α(∅)=⊥; unbounded sets use infinite bounds.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return the least interval containing S; α(∅)=⊥; unbounded sets use infinite bounds.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IntervalDomain-concretize"></a>

### concretize

`urn:csabs:operation/IntervalDomain-concretize`

**signature:** γ : Iℤ → P(ℤ)

**description:** Return exactly the represented integer set.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return exactly the represented integer set.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IntervalDomain-join"></a>

### join

`urn:csabs:operation/IntervalDomain-join`

**signature:** ⊔ : Iℤ×Iℤ → Iℤ

**description:** I⊔J=α(γ(I)∪γ(J)); gaps between disjoint operands are filled.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** I⊔J=α(γ(I)∪γ(J)); gaps between disjoint operands are filled.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IntervalDomain-meet"></a>

### meet

`urn:csabs:operation/IntervalDomain-meet`

**signature:** ⊓ : Iℤ×Iℤ → Iℤ

**description:** I⊓J=I∩J, including ⊥ for disjoint intervals.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** I⊓J=I∩J, including ⊥ for disjoint intervals.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-IntervalDomain-add"></a>

### add

`urn:csabs:operation/IntervalDomain-add`

**signature:** +♯ : Iℤ×Iℤ → Iℤ

**description:** I+♯J=α({x+y | x∈γ(I), y∈γ(J)}); bottom is absorbing. Avoid undefined extended arithmetic by this set definition.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** I+♯J=α({x+y | x∈γ(I), y∈γ(J)}); bottom is absorbing. Avoid undefined extended arithmetic by this set definition.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-IntervalDomain-convex-carrier"></a>

### convex-carrier

`urn:csabs:axiom/IntervalDomain-convex-carrier`

**description:** Defining rule for Integer interval abstract domain (empty and unbounded intervals)

**statement:** I∈Iℤ ⇔ I⊆ℤ ∧ ∀a,b∈I, ∀c∈ℤ, a≤c≤b ⇒ c∈I; I=J ⇔ γ(I)=γ(J).

**formalStatement:** I∈Iℤ ⇔ I⊆ℤ ∧ ∀a,b∈I, ∀c∈ℤ, a≤c≤b ⇒ c∈I; I=J ⇔ γ(I)=γ(J).

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-IntervalDomain-hull"></a>

### hull

`urn:csabs:axiom/IntervalDomain-hull`

**description:** Defining rule for Integer interval abstract domain (empty and unbounded intervals)

**statement:** α(S) is the intersection of all integer intervals containing S; γ(I)=I. In particular S⊆α(S), and S⊆I ⇒ α(S)⊆I.

**formalStatement:** α(S) is the intersection of all integer intervals containing S; γ(I)=I. In particular S⊆α(S), and S⊆I ⇒ α(S)⊆I.

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-IntervalDomain-lattice-operations"></a>

### lattice-operations

`urn:csabs:axiom/IntervalDomain-lattice-operations`

**description:** Defining rule for Integer interval abstract domain (empty and unbounded intervals)

**statement:** ⊥=∅; ⊤=ℤ; ⋀K=⋂K (⋂∅=ℤ); ⋁K=α(⋃K), with ⋁∅=⊥.

**formalStatement:** ⊥=∅; ⊤=ℤ; ⋀K=⋂K (⋂∅=ℤ); ⋁K=α(⋃K), with ⋁∅=⊥.

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-IntervalDomain-abstract-addition"></a>

### abstract-addition

`urn:csabs:axiom/IntervalDomain-abstract-addition`

**description:** Defining rule for Integer interval abstract domain (empty and unbounded intervals)

**statement:** I+♯J=α({x+y | x∈γ(I), y∈γ(J)}).

**formalStatement:** I+♯J=α({x+y | x∈γ(I), y∈γ(J)}).

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-IntervalDomain-hull-adjunction"></a>

### hull-adjunction

`urn:csabs:law/IntervalDomain-hull-adjunction`

**description:** α(S)⊑I ⇔ S⊆γ(I).

**statement:** α(S)⊑I ⇔ S⊆γ(I).

**formalStatement:** α(S)⊑I ⇔ S⊆γ(I).

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**dependsOn:** [convex-carrier](IntervalDomain.md#node-urn-csabs-axiom-IntervalDomain-convex-carrier); [hull](IntervalDomain.md#node-urn-csabs-axiom-IntervalDomain-hull)

**proofSketch:** The forward implication uses S⊆α(S). Conversely I is among the intervals containing S, so their intersection α(S) is contained in I.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

<a id="node-urn-csabs-law-IntervalDomain-addition-sound"></a>

### addition-sound

`urn:csabs:law/IntervalDomain-addition-sound`

**description:** {x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).

**statement:** {x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).

**formalStatement:** {x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).

**assumptions:** Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.

**dependsOn:** [hull](IntervalDomain.md#node-urn-csabs-axiom-IntervalDomain-hull); [abstract-addition](IntervalDomain.md#node-urn-csabs-axiom-IntervalDomain-abstract-addition)

**proofSketch:** Apply the hull upper-bound rule to the concrete result set and unfold the definition of +♯.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/IntervalDomain",
    "type": "Concept",
    "shortForm": "IntervalDomain",
    "fullName": "Integer interval abstract domain (empty and unbounded intervals)",
    "definition": "The complete lattice of order-convex subsets of the mathematical integers, including the empty set, ordered by inclusion.",
    "notation": "Iℤ={⊥} ∪ {[l,u]∩ℤ | l∈ℤ∪{−∞}, u∈ℤ∪{+∞}, l≤u}; γ(I)=I; I⊑J ⇔ I⊆J.",
    "category": [
      "urn:csabs:category/interval-structures",
      "urn:csabs:category/order",
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.",
    "axiomBasis": "Order-convex integer subsets; hull abstraction and identity concretization; arbitrary intersection/hull joins; lifted addition.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "Iℤ={⊥} ∪ {[l,u]∩ℤ | l∈ℤ∪{−∞}, u∈ℤ∪{+∞}, l≤u}; γ(I)=I; I⊑J ⇔ I⊆J. Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist.",
    "requiresConcept": [
      "urn:csabs:concept/MathematicalInteger",
      "urn:csabs:concept/Set"
    ],
    "relatedConcept": [
      "urn:csabs:concept/ClosedInterval",
      "urn:csabs:concept/AbstractInterpretation",
      "urn:csabs:concept/MonotoneDataflow"
    ],
    "hasOperation": [
      "urn:csabs:operation/IntervalDomain-abstract",
      "urn:csabs:operation/IntervalDomain-concretize",
      "urn:csabs:operation/IntervalDomain-join",
      "urn:csabs:operation/IntervalDomain-meet",
      "urn:csabs:operation/IntervalDomain-add"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/IntervalDomain-convex-carrier",
      "urn:csabs:axiom/IntervalDomain-hull",
      "urn:csabs:axiom/IntervalDomain-lattice-operations",
      "urn:csabs:axiom/IntervalDomain-abstract-addition"
    ],
    "hasLaw": [
      "urn:csabs:law/IntervalDomain-hull-adjunction",
      "urn:csabs:law/IntervalDomain-addition-sound"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/CompleteLattice"
    ],
    "specializationNote": "Carrier Iℤ with inclusion; arbitrary meet is intersection (empty-family meet ℤ), arbitrary join is the least integer interval containing the union (empty-family join ∅). No axioms transfer through this edge.",
    "leanFormulation": "def IntervalDomain :=\n  {s : Set Int // ∀ a ∈ s, ∀ b ∈ s, ∀ c : Int, a ≤ c → c ≤ b → c ∈ s}",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.IntervalDomain",
    "formulationScope": "partial",
    "leanModelMapping": "Subtype of Set Int satisfying integer order-convexity; equality is extensional set equality. Empty, singleton and unbounded sets are representable.",
    "leanModelLimitations": "No Lean lattice instance, hull, abstract arithmetic or widening implementation; carrier model only. No proof witnesses registered."
  },
  {
    "id": "urn:csabs:operation/IntervalDomain-abstract",
    "type": "Operation",
    "name": "abstract",
    "signature": "α : P(ℤ) → Iℤ",
    "description": "Return the least interval containing S; α(∅)=⊥; unbounded sets use infinite bounds.",
    "concept": "urn:csabs:concept/IntervalDomain",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return the least interval containing S; α(∅)=⊥; unbounded sets use infinite bounds.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IntervalDomain-concretize",
    "type": "Operation",
    "name": "concretize",
    "signature": "γ : Iℤ → P(ℤ)",
    "description": "Return exactly the represented integer set.",
    "concept": "urn:csabs:concept/IntervalDomain",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return exactly the represented integer set.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IntervalDomain-join",
    "type": "Operation",
    "name": "join",
    "signature": "⊔ : Iℤ×Iℤ → Iℤ",
    "description": "I⊔J=α(γ(I)∪γ(J)); gaps between disjoint operands are filled.",
    "concept": "urn:csabs:concept/IntervalDomain",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "I⊔J=α(γ(I)∪γ(J)); gaps between disjoint operands are filled.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IntervalDomain-meet",
    "type": "Operation",
    "name": "meet",
    "signature": "⊓ : Iℤ×Iℤ → Iℤ",
    "description": "I⊓J=I∩J, including ⊥ for disjoint intervals.",
    "concept": "urn:csabs:concept/IntervalDomain",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "I⊓J=I∩J, including ⊥ for disjoint intervals.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/IntervalDomain-add",
    "type": "Operation",
    "name": "add",
    "signature": "+♯ : Iℤ×Iℤ → Iℤ",
    "description": "I+♯J=α({x+y | x∈γ(I), y∈γ(J)}); bottom is absorbing. Avoid undefined extended arithmetic by this set definition.",
    "concept": "urn:csabs:concept/IntervalDomain",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "I+♯J=α({x+y | x∈γ(I), y∈γ(J)}); bottom is absorbing. Avoid undefined extended arithmetic by this set definition.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/IntervalDomain-convex-carrier",
    "type": "Axiom",
    "name": "convex-carrier",
    "description": "Defining rule for Integer interval abstract domain (empty and unbounded intervals)",
    "statement": "I∈Iℤ ⇔ I⊆ℤ ∧ ∀a,b∈I, ∀c∈ℤ, a≤c≤b ⇒ c∈I; I=J ⇔ γ(I)=γ(J).",
    "formalStatement": "I∈Iℤ ⇔ I⊆ℤ ∧ ∀a,b∈I, ∀c∈ℤ, a≤c≤b ⇒ c∈I; I=J ⇔ γ(I)=γ(J).",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/IntervalDomain-hull",
    "type": "Axiom",
    "name": "hull",
    "description": "Defining rule for Integer interval abstract domain (empty and unbounded intervals)",
    "statement": "α(S) is the intersection of all integer intervals containing S; γ(I)=I. In particular S⊆α(S), and S⊆I ⇒ α(S)⊆I.",
    "formalStatement": "α(S) is the intersection of all integer intervals containing S; γ(I)=I. In particular S⊆α(S), and S⊆I ⇒ α(S)⊆I.",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/IntervalDomain-lattice-operations",
    "type": "Axiom",
    "name": "lattice-operations",
    "description": "Defining rule for Integer interval abstract domain (empty and unbounded intervals)",
    "statement": "⊥=∅; ⊤=ℤ; ⋀K=⋂K (⋂∅=ℤ); ⋁K=α(⋃K), with ⋁∅=⊥.",
    "formalStatement": "⊥=∅; ⊤=ℤ; ⋀K=⋂K (⋂∅=ℤ); ⋁K=α(⋃K), with ⋁∅=⊥.",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/IntervalDomain-abstract-addition",
    "type": "Axiom",
    "name": "abstract-addition",
    "description": "Defining rule for Integer interval abstract domain (empty and unbounded intervals)",
    "statement": "I+♯J=α({x+y | x∈γ(I), y∈γ(J)}).",
    "formalStatement": "I+♯J=α({x+y | x∈γ(I), y∈γ(J)}).",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/IntervalDomain-hull-adjunction",
    "type": "Law",
    "name": "hull-adjunction",
    "description": "α(S)⊑I ⇔ S⊆γ(I).",
    "statement": "α(S)⊑I ⇔ S⊆γ(I).",
    "formalStatement": "α(S)⊑I ⇔ S⊆γ(I).",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "dependsOn": [
      "urn:csabs:axiom/IntervalDomain-convex-carrier",
      "urn:csabs:axiom/IntervalDomain-hull"
    ],
    "proofSketch": "The forward implication uses S⊆α(S). Conversely I is among the intervals containing S, so their intersection α(S) is contained in I.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:law/IntervalDomain-addition-sound",
    "type": "Law",
    "name": "addition-sound",
    "description": "{x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).",
    "statement": "{x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).",
    "formalStatement": "{x+y | x∈γ(I), y∈γ(J)} ⊆ γ(I+♯J).",
    "assumptions": [
      "Exact unbounded integers with extensional set equality; infinite endpoints are bounds, not integer values. All empty encodings are the single ⊥; ⊤=ℤ. Singleton and one-sided unbounded intervals are valid. Join is convex hull, not generally set union; meet is intersection. Arithmetic here is mathematical integer addition with no overflow or rounding. Machine wrapping, poison, NaN and floating-point rounding need separate models. This extends rather than specializes ClosedInterval, whose carrier excludes emptiness and unboundedness. Infinite ascending chains exist."
    ],
    "appliesTo": [
      "urn:csabs:concept/IntervalDomain"
    ],
    "dependsOn": [
      "urn:csabs:axiom/IntervalDomain-hull",
      "urn:csabs:axiom/IntervalDomain-abstract-addition"
    ],
    "proofSketch": "Apply the hull upper-bound rule to the concrete result set and unfold the definition of +♯.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§6.1 pp.79–81, lattice, inclusion order, lifted empty value and abstract operator formula; §6.2 for convergence limitations.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
