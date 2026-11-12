# Finite labelled property graph (single-valued profile)

A finite directed multigraph with a string label per vertex and edge and a finite string-keyed property map per element.

**Notation:** (V,E,s,t,label_V,label_E,prop_V,prop_E)

**Stable ID:** `urn:csabs:concept/PropertyGraph`

**Categories:** Relational data modelling

**Kind:** Abstract data type

**Prerequisites:** [Finite directed multigraph with edge identities](DirectedMultigraph.md), [Map](Map.md), [Finite sequence (List datatype)](Sequence.md)

**Specializes:** [Finite directed multigraph with edge identities](DirectedMultigraph.md)

## Backlinks

- [Finite RDF 1.1 graph](RDFGraph.md) — `relatedConcept`

## Mathematical formulation

The selected property graph is a finite edge-identity directed multigraph (V,E,s,t) with labels ℓ\_V:V→String, ℓ\_E:E→String and finite partial property maps p\_V:V→(String⇀Value), p\_E:E→(String⇀Value). Each vertex/edge has one label and each property key at most one value.

**Lean formulation** (in its source module context):

```lean
structure PropertyGraph (V : Type u) (E : Type v) (Value : Type w)
    [Fintype V] [Fintype E] extends DirectedMultigraph V E where
  vertexLabel : V → String
  edgeLabel : E → String
  vertexProperties : V → Catalog.Map String Value
  edgeProperties : E → Catalog.Map String Value
```

**Source:** [`Catalog.PropertyGraph`](../lean/Catalog/InformationData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** (V,E,s,t,label_V,label_E,prop_V,prop_E). Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** (V,E,s,t) is a finite directed multigraph retaining edge identities; label_V and label_E are total string-valued functions; Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None

**basisKind:** extensional-structural-definition

**basisScope:** Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.

**basisInstantiation:** DirectedMultigraph-endpoints applies explicitly to the same V,E,s,t; labels and property maps add independent fields on existing identities.

**specializationNote:** Forget labels and property maps, retaining the same V,E,s,t. Property values and label equality do not collapse edge identities.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-PropertyGraph-endpoints"></a>

### endpoints

`urn:csabs:operation/PropertyGraph-endpoints`

**signature:** source,target : E→V

**description:** Endpoint functions of underlying directed multigraph.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Endpoint functions of underlying directed multigraph.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-PropertyGraph-label"></a>

### label

`urn:csabs:operation/PropertyGraph-label`

**signature:** label_V:V→String; label_E:E→String

**description:** Each element has one label.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Each element has one label.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-PropertyGraph-property"></a>

### property

`urn:csabs:operation/PropertyGraph-property`

**signature:** property_V:V×String→Option(Value); property_E:E×String→Option(Value)

**description:** Read the finite property map at an element.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Read the finite property map at an element.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DirectedMultigraph-endpoints"></a>

### endpoints

`urn:csabs:axiom/DirectedMultigraph-endpoints`

**statement:** Defining requirement: V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))

**formalStatement:** V,E finite; s,t total from E to V; no injectivity constraint on e↦(s(e),t(e))

**assumptions:** Empty carriers permitted when endpoint functions exist: V empty forces E empty. Loops and parallel edges allowed. Equality retains carriers, edge identities and endpoints; not equality up to graph isomorphism.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Pat Morin: Open Data Structures, Graphs](https://opendatastructures.org/ods-python/12_Graphs.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints; Chapter 12: directed edges and paths; adapted to distinct edge identities and weights

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropertyGraph-labels"></a>

### labels

`urn:csabs:axiom/PropertyGraph-labels`

**statement:** Defining requirement: label_V and label_E are total string-valued functions

**formalStatement:** label_V and label_E are total string-valued functions

**assumptions:** Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-PropertyGraph-properties"></a>

### properties

`urn:csabs:axiom/PropertyGraph-properties`

**statement:** Defining requirement: Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None

**formalStatement:** Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None

**assumptions:** Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-PropertyGraph-missing-property"></a>

### missing-property

`urn:csabs:law/PropertyGraph-missing-property`

**statement:** k∉dom(prop_V(v)) ⇒ property_V(v,k)=None

**formalStatement:** k∉dom(prop_V(v)) ⇒ property_V(v,k)=None

**assumptions:** Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [properties](PropertyGraph.md#node-urn-csabs-axiom-PropertyGraph-properties)

**proofSketch:** Expand finite partial-map domain and lookup; the edge case is identical.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-PropertyGraph-parallel-edge-distinction"></a>

### parallel-edge-distinction

`urn:csabs:theorem/PropertyGraph-parallel-edge-distinction`

**statement:** There exists a PropertyGraph with distinct edges e,f having equal sources and targets but different edge labels.

**formalStatement:** There exists a PropertyGraph with distinct edges e,f having equal sources and targets but different edge labels.

**assumptions:** Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.; Typed mathematical equality and the stated defining requirements.; The existential construction chooses the finite carriers; every property map may be empty for any Value carrier.

**dependsOn:** [endpoints](DirectedMultigraph.md#node-urn-csabs-axiom-DirectedMultigraph-endpoints); [labels](PropertyGraph.md#node-urn-csabs-axiom-PropertyGraph-labels); [properties](PropertyGraph.md#node-urn-csabs-axiom-PropertyGraph-properties)

**proofSketch:** Take V={v}, E={e,f} with e≠f; both endpoints of both edges are v. Give labels "a" and "b" to e and f and empty property maps to every element. All invariants hold.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Apache TinkerPop reference: graph structure](https://tinkerpop.apache.org/docs/current/reference/#graph-structure); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Combinatorics/Quiver/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/PropertyGraph",
    "type": "Concept",
    "shortForm": "PropertyGraph",
    "fullName": "Finite labelled property graph (single-valued profile)",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite directed multigraph with a string label per vertex and edge and a finite string-keyed property map per element.",
    "notation": "(V,E,s,t,label_V,label_E,prop_V,prop_E)",
    "requiresConcept": [
      "urn:csabs:concept/DirectedMultigraph",
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Sequence"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/PropertyGraph-endpoints",
      "urn:csabs:operation/PropertyGraph-label",
      "urn:csabs:operation/PropertyGraph-property"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DirectedMultigraph-endpoints",
      "urn:csabs:axiom/PropertyGraph-labels",
      "urn:csabs:axiom/PropertyGraph-properties"
    ],
    "hasLaw": [
      "urn:csabs:law/PropertyGraph-missing-property"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/PropertyGraph-parallel-edge-distinction"
    ],
    "axiomBasis": "(V,E,s,t) is a finite directed multigraph retaining edge identities; label_V and label_E are total string-valued functions; Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DirectedMultigraph"
    ],
    "specializationNote": "Forget labels and property maps, retaining the same V,E,s,t. Property values and label equality do not collapse edge identities.",
    "basisInstantiation": "DirectedMultigraph-endpoints applies explicitly to the same V,E,s,t; labels and property maps add independent fields on existing identities.",
    "leanFormulation": "structure PropertyGraph (V : Type u) (E : Type v) (Value : Type w)\n    [Fintype V] [Fintype E] extends DirectedMultigraph V E where\n  vertexLabel : V → String\n  edgeLabel : E → String\n  vertexProperties : V → Catalog.Map String Value\n  edgeProperties : E → Catalog.Map String Value",
    "formulationSource": "urn:csabs:source/local-lean-InformationData",
    "formulationLocator": "Catalog.PropertyGraph",
    "formulationScope": "model",
    "leanModelMapping": "(V,E,s,t,label_V,label_E,prop_V,prop_E). Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "The selected property graph is a finite edge-identity directed multigraph (V,E,s,t) with labels ℓ_V:V→String, ℓ_E:E→String and finite partial property maps p_V:V→(String⇀Value), p_E:E→(String⇀Value). Each vertex/edge has one label and each property key at most one value."
  },
  {
    "id": "urn:csabs:operation/PropertyGraph-endpoints",
    "type": "Operation",
    "name": "endpoints",
    "signature": "source,target : E→V",
    "description": "Endpoint functions of underlying directed multigraph.",
    "concept": "urn:csabs:concept/PropertyGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Endpoint functions of underlying directed multigraph.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PropertyGraph-label",
    "type": "Operation",
    "name": "label",
    "signature": "label_V:V→String; label_E:E→String",
    "description": "Each element has one label.",
    "concept": "urn:csabs:concept/PropertyGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Each element has one label.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/PropertyGraph-property",
    "type": "Operation",
    "name": "property",
    "signature": "property_V:V×String→Option(Value); property_E:E×String→Option(Value)",
    "description": "Read the finite property map at an element.",
    "concept": "urn:csabs:concept/PropertyGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Read the finite property map at an element.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropertyGraph-labels",
    "type": "Axiom",
    "name": "labels",
    "statement": "Defining requirement: label_V and label_E are total string-valued functions",
    "formalStatement": "label_V and label_E are total string-valued functions",
    "assumptions": [
      "Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropertyGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/PropertyGraph-properties",
    "type": "Axiom",
    "name": "properties",
    "statement": "Defining requirement: Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None",
    "formalStatement": "Every element has a finite partial string→Value map; property reads return its lookup; absent keys return None",
    "assumptions": [
      "Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropertyGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/PropertyGraph-missing-property",
    "type": "Law",
    "name": "missing-property",
    "statement": "k∉dom(prop_V(v)) ⇒ property_V(v,k)=None",
    "formalStatement": "k∉dom(prop_V(v)) ⇒ property_V(v,k)=None",
    "assumptions": [
      "Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropertyGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/PropertyGraph-properties"
    ],
    "proofSketch": "Expand finite partial-map domain and lookup; the edge case is identical.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/PropertyGraph-parallel-edge-distinction",
    "type": "Theorem",
    "name": "parallel-edge-distinction",
    "statement": "There exists a PropertyGraph with distinct edges e,f having equal sources and targets but different edge labels.",
    "formalStatement": "There exists a PropertyGraph with distinct edges e,f having equal sources and targets but different edge labels.",
    "assumptions": [
      "Separate vertex/edge identities; loops and parallel edges allowed. Fixed property-value carrier Value; absence differs from a stored null-like Value. Selected single-label, single-valued property profile; TinkerPop multi/meta-properties require an extension. No automatic relationship-to-RDF encoding or schema constraint.",
      "Typed mathematical equality and the stated defining requirements.",
      "The existential construction chooses the finite carriers; every property map may be empty for any Value carrier."
    ],
    "appliesTo": [
      "urn:csabs:concept/PropertyGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DirectedMultigraph-endpoints",
      "urn:csabs:axiom/PropertyGraph-labels",
      "urn:csabs:axiom/PropertyGraph-properties"
    ],
    "proofSketch": "Take V={v}, E={e,f} with e≠f; both endpoints of both edges are v. Give labels \"a\" and \"b\" to e and f and empty property maps to every element. All invariants hold.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/tinkerpop-lpg-core",
      "urn:csabs:source/mathlib-quiver-core"
    ],
    "sourceLocator": "Introduction: primary structure components and The Graph Structure; single-valued profile selected here; Quiver: typed arrows for each ordered vertex pair; distinct arrows may have the same endpoints",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
