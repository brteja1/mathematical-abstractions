# Typed-edge schema with incidence cardinalities

A schema assigning each edge kind one source vertex type and one target vertex type, plus lower and optional upper incoming/outgoing incidence bounds, with an explicit graph conformance predicate.

**Notation:** s:K→T; t:K→T; ℓout,ℓin:K→ℕ; uout,uin:K→Option(ℕ)

**Stable ID:** `urn:csabs:concept/TypedEdgeSchema`

**Categories:** Relational data modelling

**Kind:** semantic-model

**Prerequisites:** [Finite directed multigraph with edge identities](DirectedMultigraph.md), [Finite carrier with exhaustive enumeration](FiniteType.md)

**Related concepts:** [Finite labelled property graph (single-valued profile)](PropertyGraph.md), [Finite typed entity-relationship instance](EntityRelationshipModel.md)

## Mathematical formulation

G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds. Utility profile: Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.

**Lean formulation** (in its source module context):

```lean
structure TypedEdgeSchema (T K : Type) where
  sourceType : K → T
  targetType : K → T
  outMin : K → Nat
  outMax : K → Option Nat
  inMin : K → Nat
  inMax : K → Option Nat
```

**Source:** [`Catalog.TypedEdgeSchema`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** model

**Interpretation:** G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds.

**Limits:** Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Conformance requires endpoint type agreement for every edge and lower≤incident-edge-count≤upper for each applicable vertex/kind and direction. A loop contributes once to each direction. Upper bound None imposes no upper constraint. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

**basisKind:** defined-structure

**basisScope:** Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints.

**verificationObligation:** Map exact carriers, equality, totality and the explicit profile conventions before use.; Model and theorem evidence does not establish a concrete software implementation refinement.

**reviewStatus:** Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-TypedEdgeSchema-conforms"></a>

### schema conformance

`urn:csabs:operation/TypedEdgeSchema-conforms`

**signature:** conforms : Schema(T,K)×TypedGraph(V,E,T,K)→Prop

**description:** Check total endpoint typing and all applicable per-vertex incidence bounds.

**precondition:** Finite graph, explicit edge identities; consistent kind carriers and maps.

**postcondition:** True iff endpoint laws and incoming/outgoing lower and upper bounds hold. This predicate does not assert existence of any conforming graph.

**totality:** Total on the stated domain.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality

**sourceNote:** Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TypedEdgeSchema-incidence"></a>

### incidence count

`urn:csabs:operation/TypedEdgeSchema-incidence`

**signature:** countOut,countIn : TypedGraph×V×K→ℕ

**description:** Count finite edge identities with the selected kind and endpoint.

**precondition:** Finite E; exact identity equality.

**postcondition:** Parallel edges count separately; a loop contributes one to each direction. Isolated applicable vertices have count zero.

**totality:** Total on the stated domain.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality

**sourceNote:** Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-TypedEdgeSchema-subtype-conforms"></a>

### subtype-conforms

`urn:csabs:operation/TypedEdgeSchema-subtype-conforms`

**signature:** subtypeConforms : Preorder(T)×Schema(T,K)×TypedGraph(V,E,T,K)→Prop

**description:** Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-TypedEdgeSchema-defining-profile"></a>

### defining profile

`urn:csabs:axiom/TypedEdgeSchema-defining-profile`

**statement:** Conformance requires endpoint type agreement for every edge and lower≤incident-edge-count≤upper for each applicable vertex/kind and direction. A loop contributes once to each direction. Upper bound None imposes no upper constraint.

**formalStatement:** G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds.

**assumptions:** Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints.

**ruleRole:** defining-rule

**reviewStatus:** Structure constraints; satisfaction is established separately for the selected model.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality

**sourceNote:** Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-TypedEdgeSchema-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/TypedEdgeSchema-utility-profile`

**statement:** Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.

**formalStatement:** subtypeConforms : Preorder(T)×Schema(T,K)×TypedGraph(V,E,T,K)→Prop: Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-TypedEdgeSchema-bound-relaxation"></a>

### bound-relaxation

`urn:csabs:law/TypedEdgeSchema-bound-relaxation`

**statement:** Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**formalStatement:** ∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-defining-profile)

**proofSketch:** Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**reviewStatus:** Derived mathematical law; separately registered theorem supplies explicit proof evidence.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.bounds_relax

**sourceNote:** Derived for the explicit selected model. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**provenanceKind:** derived

**ruleRole:** derived-law

## Theorems

<a id="node-urn-csabs-theorem-TypedEdgeSchema-model-satisfaction"></a>

### model-satisfaction

`urn:csabs:theorem/TypedEdgeSchema-model-satisfaction`

**statement:** A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.

**formalStatement:** Catalog.schemaConforms Catalog.unitSchema Catalog.unitGraph

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-defining-profile)

**proofSketch:** A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.schema_model_satisfaction

**sourceNote:** Derived for the explicit selected model. A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
Catalog.schemaConforms Catalog.unitSchema Catalog.unitGraph
```

**Source:** [`Catalog.schema_model_satisfaction`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds."
}
```

<a id="node-urn-csabs-theorem-TypedEdgeSchema-bound-relaxation"></a>

### bound-relaxation

`urn:csabs:theorem/TypedEdgeSchema-bound-relaxation`

**statement:** Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**formalStatement:** ∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'

**assumptions:** Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality.

**dependsOn:** [defining profile](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-defining-profile)

**proofSketch:** Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**reviewStatus:** Separately registered Lean witness; require fresh compiler and axiom audit for verified status.

**source:** [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference; Catalog release, sequence, transducer, schema, date and extension models and witnesses; path: lean/Catalog/ReleaseSequenceModels.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-proof

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.bounds_relax

**sourceNote:** Derived for the explicit selected model. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'
```

**Source:** [`Catalog.bounds_relax`](../lean/Catalog/ReleaseSequenceModels.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.

**Limits:** Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-defining-profile": "Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded."
}
```

<a id="node-urn-csabs-theorem-TypedEdgeSchema-subtype-exact-recovery"></a>

### subtype-exact-recovery

`urn:csabs:theorem/TypedEdgeSchema-subtype-exact-recovery`

**statement:** Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.

**formalStatement:** Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.

**proofSketch:** Unfold both definitions; endpoint and eligible-bound predicates coincide.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_exact

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.

**Lean formulation** (in its source module context):

```lean
∀ {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : Catalog.TypedEdgeSchema T K) (g : Catalog.TypedEdgeGraph V E T K), Catalog.subtypeSchemaConforms Eq s g ↔ Catalog.schemaConforms s g
```

**Source:** [`Catalog.subtype_exact`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-TypedEdgeSchema-subtype-model-satisfaction"></a>

### subtype-model-satisfaction

`urn:csabs:theorem/TypedEdgeSchema-subtype-model-satisfaction`

**statement:** The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.

**formalStatement:** The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.

**proofSketch:** Recover the existing concrete exact-type satisfaction theorem.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-utility-profile); [defining profile](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-defining-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_model

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.

**Lean formulation** (in its source module context):

```lean
Catalog.subtypeSchemaConforms Eq Catalog.unitSchema Catalog.unitGraph
```

**Source:** [`Catalog.subtype_model`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The original one-vertex, one-edge schema model also satisfies the equality-subtype profile. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-defining-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/TypedEdgeSchema-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-TypedEdgeSchema-proper-subtype-model"></a>

### proper-subtype-model

`urn:csabs:theorem/TypedEdgeSchema-proper-subtype-model`

**statement:** A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.

**formalStatement:** A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.

**proofSketch:** Evaluate concrete endpoints, preorder comparisons and incidence bounds; endpoint equality 0=1 is false.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_strict_model

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.

**Lean formulation** (in its source module context):

```lean
Catalog.subtypeSchemaConforms (· ≤ ·) Catalog.subtypeExampleSchema Catalog.subtypeExampleGraph ∧
    ¬ Catalog.schemaConforms Catalog.subtypeExampleSchema Catalog.subtypeExampleGraph
```

**Source:** [`Catalog.subtype_strict_model`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-TypedEdgeSchema-set-endpoint-singleton-recovery"></a>

### set-endpoint-singleton-recovery

`urn:csabs:theorem/TypedEdgeSchema-set-endpoint-singleton-recovery`

**statement:** Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.

**formalStatement:** Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.

**assumptions:** Exactly the displayed Lean binders and the explicit profile definitions.

**dependsOn:** [defining profile](TypedEdgeSchema.md#node-urn-csabs-axiom-TypedEdgeSchema-defining-profile)

**source:** Constructed information, prefix, replacement and endpoint-set models over pinned Mathlib; citation: Constructed models; primitives consulted in pinned Mathlib Data/Finset/Sort.lean length_sort, Data/List/TakeDrop.lean take_of_length_le, list map composition and Set membership. Independent mathematical primitive provenance: utility-mathlib-pinned.; path: lean/Catalog/ExtensionProfiles.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-derived-proof; [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Catalog.setSchema_singleton; pinned Mathlib finite-list, finite-set and relation primitives

**sourceNote:** Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.

**provenanceKind:** derived

**proofSketch:** Use the concrete definitions and the compiled proof in the cited local module.

**reviewStatus:** Selected model proof; verification requires fresh compiler and axiom audit.

#### Mathematical formulation

Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.

**Lean formulation** (in its source module context):

```lean
∀ {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]
    (s : Catalog.TypedEdgeSchema T K) (g : Catalog.TypedEdgeGraph V E T K), Catalog.setSchemaConforms (Catalog.singletonSchema s) g ↔ Catalog.schemaConforms s g
```

**Source:** [`Catalog.setSchema_singleton`](../lean/Catalog/ExtensionProfiles.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile. Exact equality and typed carriers are those displayed in the Lean proposition.

**Limits:** Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/TypedEdgeSchema-defining-profile": "Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed."
}
```

## Concept provenance

- [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/); citation: W3C Recommendation 20 July 2017, §§4.1,4.2.1–4.2.2,4.7.3: class/node constraints, minCount/maxCount and property paths.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference
- [Pinned Mathlib list and lexicographic order constructions and linear-order extension](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); citation: Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679: Data/Finset/Card.lean Finset.card; Data/List/TakeDrop.lean dropSlice_eq and length_dropSlice; Data/List/Lex.lean linearOrder; Order/Sum/Order.lean Sum.Lex; Order/Prod/Lex/Basic.lean Prod.Lex; Order/Extension/Linear.lean extend_partialOrder and toLinearExtension. Apache-2.0.; accessedOn: 2026-11-20; sourceRole: consulted-definition-and-theorem-reference

**sourceLocator:** SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality

**sourceNote:** Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/TypedEdgeSchema",
    "type": "Concept",
    "shortForm": "TypedEdgeSchema",
    "fullName": "Typed-edge schema with incidence cardinalities",
    "synonyms": [
      "Edge-type incidence schema",
      "Typed multigraph cardinality schema"
    ],
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A schema assigning each edge kind one source vertex type and one target vertex type, plus lower and optional upper incoming/outgoing incidence bounds, with an explicit graph conformance predicate.",
    "notation": "s:K→T; t:K→T; ℓout,ℓin:K→ℕ; uout,uin:K→Option(ℕ)",
    "requiresConcept": [
      "urn:csabs:concept/DirectedMultigraph",
      "urn:csabs:concept/FiniteType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PropertyGraph",
      "urn:csabs:concept/EntityRelationshipModel"
    ],
    "axiomBasis": "Conformance requires endpoint type agreement for every edge and lower≤incident-edge-count≤upper for each applicable vertex/kind and direction. A loop contributes once to each direction. Upper bound None imposes no upper constraint. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "basisKind": "defined-structure",
    "basisScope": "Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints.",
    "mathematicalFormulation": "G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds. Utility profile: Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Sourced model with separately registered Lean satisfaction and derived witnesses; verification requires fresh audit evidence.",
    "verificationObligation": [
      "Map exact carriers, equality, totality and the explicit profile conventions before use.",
      "Model and theorem evidence does not establish a concrete software implementation refinement."
    ],
    "hasOperation": [
      "urn:csabs:operation/TypedEdgeSchema-conforms",
      "urn:csabs:operation/TypedEdgeSchema-incidence",
      "urn:csabs:operation/TypedEdgeSchema-subtype-conforms"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile",
      "urn:csabs:axiom/TypedEdgeSchema-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/TypedEdgeSchema-bound-relaxation"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/TypedEdgeSchema-model-satisfaction",
      "urn:csabs:theorem/TypedEdgeSchema-bound-relaxation",
      "urn:csabs:theorem/TypedEdgeSchema-subtype-exact-recovery",
      "urn:csabs:theorem/TypedEdgeSchema-subtype-model-satisfaction",
      "urn:csabs:theorem/TypedEdgeSchema-proper-subtype-model",
      "urn:csabs:theorem/TypedEdgeSchema-set-endpoint-singleton-recovery"
    ],
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality",
    "sourceNote": "Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure TypedEdgeSchema (T K : Type) where\n  sourceType : K → T\n  targetType : K → T\n  outMin : K → Nat\n  outMax : K → Option Nat\n  inMin : K → Nat\n  inMax : K → Option Nat",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.TypedEdgeSchema",
    "formulationScope": "model",
    "leanModelMapping": "G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds.",
    "leanModelLimitations": "Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints. Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit."
  },
  {
    "id": "urn:csabs:operation/TypedEdgeSchema-conforms",
    "type": "Operation",
    "concept": "urn:csabs:concept/TypedEdgeSchema",
    "name": "schema conformance",
    "signature": "conforms : Schema(T,K)×TypedGraph(V,E,T,K)→Prop",
    "description": "Check total endpoint typing and all applicable per-vertex incidence bounds.",
    "precondition": "Finite graph, explicit edge identities; consistent kind carriers and maps.",
    "postcondition": "True iff endpoint laws and incoming/outgoing lower and upper bounds hold. This predicate does not assert existence of any conforming graph.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality",
    "sourceNote": "Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TypedEdgeSchema-incidence",
    "type": "Operation",
    "concept": "urn:csabs:concept/TypedEdgeSchema",
    "name": "incidence count",
    "signature": "countOut,countIn : TypedGraph×V×K→ℕ",
    "description": "Count finite edge identities with the selected kind and endpoint.",
    "precondition": "Finite E; exact identity equality.",
    "postcondition": "Parallel edges count separately; a loop contributes one to each direction. Isolated applicable vertices have count zero.",
    "totality": "Total on the stated domain.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality",
    "sourceNote": "Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/TypedEdgeSchema-subtype-conforms",
    "type": "Operation",
    "concept": "urn:csabs:concept/TypedEdgeSchema",
    "name": "subtype-conforms",
    "signature": "subtypeConforms : Preorder(T)×Schema(T,K)×TypedGraph(V,E,T,K)→Prop",
    "description": "Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TypedEdgeSchema-defining-profile",
    "type": "Axiom",
    "name": "defining profile",
    "statement": "Conformance requires endpoint type agreement for every edge and lower≤incident-edge-count≤upper for each applicable vertex/kind and direction. A loop contributes once to each direction. Upper bound None imposes no upper constraint.",
    "formalStatement": "G=(V,E,src,dst,τV,τE). Endpoint laws: τV(src e)=s(τE e), τV(dst e)=t(τE e). cout(v,k)=|{e∈E | src e=v ∧ τE e=k}|; cin analogously. Conforms iff endpoints agree and applicable counts satisfy bounds.",
    "assumptions": [
      "Finite graph vertex and edge identity sets V,E, and finite vertex/edge kind sets T,K in the intended finite-schema profile. Types and endpoint maps are total; every vertex/edge has exactly one kind. Loops and parallel edge identities are allowed. For each k count edges of that kind incident to each vertex of the required endpoint type; zero counts and isolated vertices are checked. Bounds count edge identities, not distinct targets, pairs, or SHACL value nodes. None means no upper bound; inclusive min/max. Inconsistent bounds and schemas with no conforming graph are representable and not asserted satisfiable. The Lean predicate generalizes to arbitrary V,T,K with finite E. Empty kinds require compatible empty graphs; no inheritance, subtyping, attributes or global connectivity constraints."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Structure constraints; satisfaction is established separately for the selected model.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality",
    "sourceNote": "Constructed adaptation of type and inclusive cardinality constraints. SHACL property paths count distinct value nodes; this profile deliberately counts multigraph edge identities, so it is not a SHACL equivalence.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/TypedEdgeSchema-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.",
    "formalStatement": "subtypeConforms : Preorder(T)×Schema(T,K)×TypedGraph(V,E,T,K)→Prop: Optional profile: actual endpoint type ≤ declared endpoint type. For every vertex and edge kind, outgoing/incoming incidence bounds apply when actual vertex type ≤ that kind’s corresponding declared endpoint type. Count each edge identity once, including parallel edges. Overlapping type eligibility imposes each applicable constraint. Exact profile is recovered with ≤ defined as equality; no inheritance is silently added to the original conformance predicate.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/TypedEdgeSchema-bound-relaxation",
    "type": "Law",
    "name": "bound-relaxation",
    "statement": "Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "formalStatement": "∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile"
    ],
    "proofSketch": "Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "reviewStatus": "Derived mathematical law; separately registered theorem supplies explicit proof evidence.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.bounds_relax",
    "sourceNote": "Derived for the explicit selected model. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "provenanceKind": "derived",
    "ruleRole": "derived-law"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-model-satisfaction",
    "type": "Theorem",
    "name": "model-satisfaction",
    "statement": "A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.",
    "formalStatement": "Catalog.schemaConforms Catalog.unitSchema Catalog.unitGraph",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile"
    ],
    "proofSketch": "A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.schema_model_satisfaction",
    "sourceNote": "Derived for the explicit selected model. A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.schemaConforms Catalog.unitSchema Catalog.unitGraph",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.schema_model_satisfaction",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. A finite one-vertex one-edge loop has correctly typed endpoints and exactly one incoming and outgoing edge; it realizes positive lower and upper bounds.\"}"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-bound-relaxation",
    "type": "Theorem",
    "name": "bound-relaxation",
    "statement": "Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "formalStatement": "∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'",
    "assumptions": [
      "Exactly the typed binders and explicit preconditions of the formal statement; selected profile carrier and equality."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile"
    ],
    "proofSketch": "Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "reviewStatus": "Separately registered Lean witness; require fresh compiler and axiom audit for verified status.",
    "source": [
      "urn:csabs:source/seven-shacl",
      "urn:csabs:source/seven-mathlib",
      "urn:csabs:source/seven-lean-models"
    ],
    "sourceLocator": "SHACL §§4.1,4.2.1–4.2.2,4.7.3; Mathlib Finset cardinality; Catalog.bounds_relax",
    "sourceNote": "Derived for the explicit selected model. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (n lo lo' : Nat) (hi hi' : Option Nat), lo' ≤ lo → (∀ h' ∈ hi', ∃ h ∈ hi, h ≤ h') → Catalog.withinBounds n lo hi → Catalog.withinBounds n lo' hi'",
    "formulationSource": "urn:csabs:source/seven-lean-models",
    "formulationLocator": "Catalog.bounds_relax",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.",
    "leanModelLimitations": "Exact selected mathematical profile; no parser, implementation refinement or blanket theorem transfer. Read individual binders, carrier constraints and source adaptation notes. Witness verification requires a fresh compiler/axiom audit.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-defining-profile\": \"Proved constraint for the specified concrete interpretation or structural recursion; not a hypothesis asserting its own satisfaction. Use transitivity for the lowered minimum and for each enlarged finite maximum; none denotes unbounded.\"}"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-subtype-exact-recovery",
    "type": "Theorem",
    "name": "subtype-exact-recovery",
    "statement": "Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.",
    "formalStatement": "Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.",
    "mathematicalFormulation": "Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds.",
    "proofSketch": "Unfold both definitions; endpoint and eligible-bound predicates coincide.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_exact",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]\n    (s : Catalog.TypedEdgeSchema T K) (g : Catalog.TypedEdgeGraph V E T K), Catalog.subtypeSchemaConforms Eq s g ↔ Catalog.schemaConforms s g",
    "leanModelMapping": "Subtype-qualified conformance with equality as the subtype preorder is exactly the original exact-type conformance predicate, including incidence bounds. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.subtype_exact"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-subtype-model-satisfaction",
    "type": "Theorem",
    "name": "subtype-model-satisfaction",
    "statement": "The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.",
    "formalStatement": "The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.",
    "mathematicalFormulation": "The original one-vertex, one-edge schema model also satisfies the equality-subtype profile.",
    "proofSketch": "Recover the existing concrete exact-type satisfaction theorem.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-utility-profile",
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_model",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.subtypeSchemaConforms Eq Catalog.unitSchema Catalog.unitGraph",
    "leanModelMapping": "The original one-vertex, one-edge schema model also satisfies the equality-subtype profile. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-defining-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/TypedEdgeSchema-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.subtype_model"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-proper-subtype-model",
    "type": "Theorem",
    "name": "proper-subtype-model",
    "statement": "A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.",
    "formalStatement": "A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.",
    "mathematicalFormulation": "A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails.",
    "proofSketch": "Evaluate concrete endpoints, preorder comparisons and incidence bounds; endpoint equality 0=1 is false.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: reflexive/transitive relations; Data/Finset/Filter.lean: incidence counting; constructed subtype-qualified endpoint profile; Catalog.subtype_strict_model",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "Catalog.subtypeSchemaConforms (· ≤ ·) Catalog.subtypeExampleSchema Catalog.subtypeExampleGraph ∧\n    ¬ Catalog.schemaConforms Catalog.subtypeExampleSchema Catalog.subtypeExampleGraph",
    "leanModelMapping": "A graph whose endpoint types are 0 conforms to declarations of type 1 under the Fin 2 ≤ preorder with zero lower/unbounded upper incidence bounds, while exact-type conformance fails. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.subtype_strict_model"
  },
  {
    "id": "urn:csabs:theorem/TypedEdgeSchema-set-endpoint-singleton-recovery",
    "type": "Theorem",
    "name": "set-endpoint-singleton-recovery",
    "statement": "Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.",
    "formalStatement": "Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.",
    "mathematicalFormulation": "Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile.",
    "assumptions": [
      "Exactly the displayed Lean binders and the explicit profile definitions."
    ],
    "appliesTo": [
      "urn:csabs:concept/TypedEdgeSchema"
    ],
    "dependsOn": [
      "urn:csabs:axiom/TypedEdgeSchema-defining-profile"
    ],
    "source": [
      "urn:csabs:source/extension-profiles-2026-11-20",
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Catalog.setSchema_singleton; pinned Mathlib finite-list, finite-set and relation primitives",
    "sourceNote": "Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.",
    "provenanceKind": "derived",
    "proofSketch": "Use the concrete definitions and the compiled proof in the cited local module.",
    "leanFormulation": "∀ {V E T K : Type} [Fintype E] [DecidableEq V] [DecidableEq K]\n    (s : Catalog.TypedEdgeSchema T K) (g : Catalog.TypedEdgeGraph V E T K), Catalog.setSchemaConforms (Catalog.singletonSchema s) g ↔ Catalog.schemaConforms s g",
    "leanModelMapping": "Optional EndpointSetSchema assigns sourceTypes(k),targetTypes(k)⊆T. Each edge endpoint must belong to its declared set. Incidence bounds apply at every vertex whose type belongs to the corresponding set, counting edge identities once per kind. Empty sets reject edges of that kind; overlapping eligible kinds impose each constraint. Singleton sets recover exact conformance, including bounds. The bounds carrier reuses TypedEdgeSchema; its sourceType/targetType fields are ignored in this profile. Exact equality and typed carriers are those displayed in the Lean proposition.",
    "leanModelLimitations": "Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/TypedEdgeSchema-defining-profile\": \"Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/extension-profiles-2026-11-20",
    "formulationLocator": "Catalog.setSchema_singleton",
    "reviewStatus": "Selected model proof; verification requires fresh compiler and axiom audit."
  }
]
```
<!-- graph-record:end -->
