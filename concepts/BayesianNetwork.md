# Bayesian network (finite discrete variables)

A finite directed acyclic graph equipped with a nonempty finite value set per node and a normalized conditional probability table for every parent assignment, defining a joint law by their product.

**Notation:** G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v))

**Stable ID:** `urn:csabs:concept/BayesianNetwork`

**Categories:** Probability and stochastic models, Graph theory

**Kind:** semantic-model

**Prerequisites:** [Directed acyclic graph](DAG.md), [Probability space (normalized measure)](ProbabilitySpace.md), [Conditional probability given a positive-probability event](ConditionalProbability.md), [Random variable (measurable random element)](RandomVariable.md)

**Specializes:** [Directed acyclic graph](DAG.md)

## Mathematical formulation

For a finite DAG (V,E), finite nonempty value carriers X\_v and normalized conditional tables p\_v(x\_v|x\_pa(v)), the joint weight is p(x)=∏\_{v∈V}p\_v(x\_v|x\_pa(v)). The Lean interface stores the DAG and tables; joint normalization is not supplied as a registered proof witness.

**Lean formulation** (in its source module context):

```lean
structure BayesianNetwork (V : Type) [Fintype V] (Value : V → Type)
    [∀ v, Fintype (Value v)] [∀ v, Nonempty (Value v)] where
  dag : DAG V
  localLaw : ∀ v, ((p : {p // dag.edge p v}) → Value p.val) → PMF (Value v)
```

**Source:** [`Catalog.BayesianNetwork`](../lean/Catalog/Probability.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Finite DAG and nonempty finite variable carriers with normalized PMF conditional tables; joint defined by finite factorization.

**Limits:** Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite DAG, nonempty finite variable carriers, and nonnegative normalized local tables; joint factorization is a definition.

**basisKind:** defined-structure

**basisScope:** Exact finite joint evaluation, marginalization and positive-evidence conditioning. No causal or faithfulness assumption is imposed.

**specializationNote:** Forget variable value sets and conditional tables; retain the same finite vertex set and directed acyclic edge relation.

**verificationObligation:** Tables are specified even at parent assignments with probability zero; they are generative parameters, not uniquely determined observational ratios there.; An empty node set yields the singleton empty assignment with probability one. Graphical separation is sound; additional independences may occur.; Use the stated carriers and equality. Specialization does not automatically transfer operations or claims.

**reviewStatus:** editorial interface review; not machine-proved

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-BayesianNetwork-joint"></a>

### joint

`urn:csabs:operation/BayesianNetwork-joint`

**signature:** (∏_{v∈V}Val(v)) → [0,1]

**description:** Multiply the local conditional-table entries for a full assignment; empty product is one.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Multiply the local conditional-table entries for a full assignment; empty product is one.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-BayesianNetwork-marginal"></a>

### marginal

`urn:csabs:operation/BayesianNetwork-marginal`

**signature:** U⊆V, x_U ↦ ∑_{x_{V∖U}}p(x_V)

**description:** Sum out unrequested variables over their finite value sets.

**precondition:** Inputs belong to the stated domains.

**postcondition:** Sum out unrequested variables over their finite value sets.

**totality:** total on the stated domain

<a id="node-urn-csabs-operation-BayesianNetwork-posterior"></a>

### posterior

`urn:csabs:operation/BayesianNetwork-posterior`

**signature:** (A,e) ↦ p(A,e)/p(e)

**description:** Condition a query assignment on evidence by finite marginalization.

**precondition:** Query and evidence concern disjoint node sets; p(e)>0.

**postcondition:** Condition a query assignment on evidence by finite marginalization.

**totality:** partial; undefined for zero-probability evidence

## Axioms and defining rules

<a id="node-urn-csabs-axiom-BayesianNetwork-local-tables"></a>

### local-tables

`urn:csabs:axiom/BayesianNetwork-local-tables`

**statement:** Each node has a stochastic table for every assignment to its parents.

**formalStatement:** G is a finite DAG; ∀v,a:q_v(·∣a):Val(v)→[0,1], Val(v) finite nonempty, ∑_{b∈Val(v)}q_v(b∣a)=1

**assumptions:** G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v)); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Bayesian networks](https://ermongroup.github.io/cs228-notes/representation/directed/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Formal definition

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

<a id="node-urn-csabs-axiom-BayesianNetwork-factorization"></a>

### factorization

`urn:csabs:axiom/BayesianNetwork-factorization`

**statement:** The local tables define the joint mass by factorization over the DAG.

**formalStatement:** ∀x∈∏_vVal(v):p(x)=∏_{v∈V}q_v(x_v∣x_pa(v))

**assumptions:** G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v)); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial definition; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Bayesian networks](https://ermongroup.github.io/cs228-notes/representation/directed/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Probabilistic modeling with Bayesian networks; Formal definition

**sourceNote:** Defining constraint or equation adapted to the declared carriers and catalog notation.

**provenanceKind:** adapted

**ruleRole:** defining-rule

## Laws

No entries recorded. This does not assert absence of mathematical facts.

## Theorems

<a id="node-urn-csabs-theorem-BayesianNetwork-joint-normalization"></a>

### joint-normalization

`urn:csabs:theorem/BayesianNetwork-joint-normalization`

**statement:** The factored mass is a normalized joint probability distribution.

**formalStatement:** ∀x:p(x)≥0 and ∑_{x∈∏_vVal(v)}p(x)=1

**assumptions:** G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v)); Use the concept’s declared semantic conventions.

**reviewStatus:** editorial derivation; not machine-proved

**notationLanguage:** informal mathematical Unicode

**source:** [Stanford CS228 notes: Bayesian networks](https://ermongroup.github.io/cs228-notes/representation/directed/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Normalization paragraph following Formal definition

**sourceNote:** Derived from the linked local premises; proof sketch gives the adaptation.

**provenanceKind:** derived

**dependsOn:** [local-tables](BayesianNetwork.md#node-urn-csabs-axiom-BayesianNetwork-local-tables); [factorization](BayesianNetwork.md#node-urn-csabs-axiom-BayesianNetwork-factorization); [joint](BayesianNetwork.md#node-urn-csabs-operation-BayesianNetwork-joint); [marginal](BayesianNetwork.md#node-urn-csabs-operation-BayesianNetwork-marginal)

**proofSketch:** Products are nonnegative. Sum in reverse topological order, eliminating a sink variable using its table normalization, and repeat. The empty graph leaves the empty product one.

## Concept provenance

- [Stanford CS228 notes: Bayesian networks](https://ermongroup.github.io/cs228-notes/representation/directed/); accessedOn: 2026-11-07; sourceRole: primary mathematical reference

**sourceLocator:** Formal definition; normalization discussion; Independencies described by directed graphs

**sourceNote:** Interface adapted to the catalog notation and explicitly restricted to the stated scope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/BayesianNetwork",
    "type": "Concept",
    "shortForm": "BayesianNetwork",
    "fullName": "Bayesian network (finite discrete variables)",
    "category": [
      "urn:csabs:category/probability",
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A finite directed acyclic graph equipped with a nonempty finite value set per node and a normalized conditional probability table for every parent assignment, defining a joint law by their product.",
    "notation": "G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v))",
    "hasOperation": [
      "urn:csabs:operation/BayesianNetwork-joint",
      "urn:csabs:operation/BayesianNetwork-marginal",
      "urn:csabs:operation/BayesianNetwork-posterior"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/BayesianNetwork-local-tables",
      "urn:csabs:axiom/BayesianNetwork-factorization"
    ],
    "hasLaw": [],
    "hasTheorem": [
      "urn:csabs:theorem/BayesianNetwork-joint-normalization"
    ],
    "axiomBasis": "Finite DAG, nonempty finite variable carriers, and nonnegative normalized local tables; joint factorization is a definition.",
    "basisKind": "defined-structure",
    "basisScope": "Exact finite joint evaluation, marginalization and positive-evidence conditioning. No causal or faithfulness assumption is imposed.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "editorial interface review; not machine-proved",
    "requiresConcept": [
      "urn:csabs:concept/DAG",
      "urn:csabs:concept/ProbabilitySpace",
      "urn:csabs:concept/ConditionalProbability",
      "urn:csabs:concept/RandomVariable"
    ],
    "verificationObligation": [
      "Tables are specified even at parent assignments with probability zero; they are generative parameters, not uniquely determined observational ratios there.",
      "An empty node set yields the singleton empty assignment with probability one. Graphical separation is sound; additional independences may occur.",
      "Use the stated carriers and equality. Specialization does not automatically transfer operations or claims."
    ],
    "source": [
      "urn:csabs:source/cs228-bayesian-networks"
    ],
    "sourceLocator": "Formal definition; normalization discussion; Independencies described by directed graphs",
    "sourceNote": "Interface adapted to the catalog notation and explicitly restricted to the stated scope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DAG"
    ],
    "specializationNote": "Forget variable value sets and conditional tables; retain the same finite vertex set and directed acyclic edge relation.",
    "leanFormulation": "structure BayesianNetwork (V : Type) [Fintype V] (Value : V → Type)\n    [∀ v, Fintype (Value v)] [∀ v, Nonempty (Value v)] where\n  dag : DAG V\n  localLaw : ∀ v, ((p : {p // dag.edge p v}) → Value p.val) → PMF (Value v)",
    "formulationSource": "urn:csabs:source/local-lean-Probability",
    "formulationLocator": "Catalog.BayesianNetwork",
    "formulationScope": "model",
    "leanModelMapping": "Finite DAG and nonempty finite variable carriers with normalized PMF conditional tables; joint defined by finite factorization.",
    "leanModelLimitations": "Selected carrier/interface interpretation only. No blanket witness for all recorded operations, axioms, laws or theorems; consult binders and individual witness mappings.",
    "mathematicalFormulation": "For a finite DAG (V,E), finite nonempty value carriers X_v and normalized conditional tables p_v(x_v|x_pa(v)), the joint weight is p(x)=∏_{v∈V}p_v(x_v|x_pa(v)). The Lean interface stores the DAG and tables; joint normalization is not supplied as a registered proof witness."
  },
  {
    "id": "urn:csabs:operation/BayesianNetwork-joint",
    "type": "Operation",
    "name": "joint",
    "signature": "(∏_{v∈V}Val(v)) → [0,1]",
    "description": "Multiply the local conditional-table entries for a full assignment; empty product is one.",
    "concept": "urn:csabs:concept/BayesianNetwork",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Multiply the local conditional-table entries for a full assignment; empty product is one.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/BayesianNetwork-marginal",
    "type": "Operation",
    "name": "marginal",
    "signature": "U⊆V, x_U ↦ ∑_{x_{V∖U}}p(x_V)",
    "description": "Sum out unrequested variables over their finite value sets.",
    "concept": "urn:csabs:concept/BayesianNetwork",
    "precondition": "Inputs belong to the stated domains.",
    "postcondition": "Sum out unrequested variables over their finite value sets.",
    "totality": "total on the stated domain"
  },
  {
    "id": "urn:csabs:operation/BayesianNetwork-posterior",
    "type": "Operation",
    "name": "posterior",
    "signature": "(A,e) ↦ p(A,e)/p(e)",
    "description": "Condition a query assignment on evidence by finite marginalization.",
    "concept": "urn:csabs:concept/BayesianNetwork",
    "precondition": "Query and evidence concern disjoint node sets; p(e)>0.",
    "postcondition": "Condition a query assignment on evidence by finite marginalization.",
    "totality": "partial; undefined for zero-probability evidence"
  },
  {
    "id": "urn:csabs:axiom/BayesianNetwork-local-tables",
    "type": "Axiom",
    "name": "local-tables",
    "statement": "Each node has a stochastic table for every assignment to its parents.",
    "formalStatement": "G is a finite DAG; ∀v,a:q_v(·∣a):Val(v)→[0,1], Val(v) finite nonempty, ∑_{b∈Val(v)}q_v(b∣a)=1",
    "appliesTo": [
      "urn:csabs:concept/BayesianNetwork"
    ],
    "assumptions": [
      "G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v))",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-bayesian-networks"
    ],
    "sourceLocator": "Formal definition",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:axiom/BayesianNetwork-factorization",
    "type": "Axiom",
    "name": "factorization",
    "statement": "The local tables define the joint mass by factorization over the DAG.",
    "formalStatement": "∀x∈∏_vVal(v):p(x)=∏_{v∈V}q_v(x_v∣x_pa(v))",
    "appliesTo": [
      "urn:csabs:concept/BayesianNetwork"
    ],
    "assumptions": [
      "G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v))",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial definition; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-bayesian-networks"
    ],
    "sourceLocator": "Probabilistic modeling with Bayesian networks; Formal definition",
    "sourceNote": "Defining constraint or equation adapted to the declared carriers and catalog notation.",
    "provenanceKind": "adapted",
    "ruleRole": "defining-rule"
  },
  {
    "id": "urn:csabs:theorem/BayesianNetwork-joint-normalization",
    "type": "Theorem",
    "name": "joint-normalization",
    "statement": "The factored mass is a normalized joint probability distribution.",
    "formalStatement": "∀x:p(x)≥0 and ∑_{x∈∏_vVal(v)}p(x)=1",
    "appliesTo": [
      "urn:csabs:concept/BayesianNetwork"
    ],
    "assumptions": [
      "G=(V,E) a finite DAG; p(x_V)=∏_{v∈V}q_v(x_v∣x_pa(v))",
      "Use the concept’s declared semantic conventions."
    ],
    "reviewStatus": "editorial derivation; not machine-proved",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/cs228-bayesian-networks"
    ],
    "sourceLocator": "Normalization paragraph following Formal definition",
    "sourceNote": "Derived from the linked local premises; proof sketch gives the adaptation.",
    "provenanceKind": "derived",
    "dependsOn": [
      "urn:csabs:axiom/BayesianNetwork-local-tables",
      "urn:csabs:axiom/BayesianNetwork-factorization",
      "urn:csabs:operation/BayesianNetwork-joint",
      "urn:csabs:operation/BayesianNetwork-marginal"
    ],
    "proofSketch": "Products are nonnegative. Sum in reverse topological order, eliminating a sink variable using its table normalization, and repeat. The empty graph leaves the empty product one."
  }
]
```
<!-- graph-record:end -->
