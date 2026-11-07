# Finite RDF 1.1 graph

A finite set of RDF triples with disjoint IRI, blank-node and literal sorts and RDF position restrictions.

**Notation:** G⊆fin (I⊎B)×I×(I⊎B⊎L)

**Stable ID:** `urn:csabs:concept/RDFGraph`

**Categories:** Relational data modelling

**Kind:** Abstract data type

**Prerequisites:** [Finite set collection](FiniteSet.md), [Product Type](ProductType.md), [Sum Type](SumType.md)

**Related concepts:** [Finite labelled property graph (single-valued profile)](PropertyGraph.md)

## Backlinks

- [Finite RDF 1.1 dataset](RDFDataset.md) — `requiresConcept`

## Interface and scope

**axiomBasis:** I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L; G is a finite set of position-correct triples; equality is triple-set equality; u∈insert(G,t) ⇔ u=t ∨ u∈G; G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H

**basisKind:** extensional-structural-definition

**basisScope:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RDFGraph-triple"></a>

### triple

`urn:csabs:operation/RDFGraph-triple`

**signature:** triple : (I⊎B)×I×(I⊎B⊎L)→Triple

**description:** Constructs a position-correct triple.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Constructs a position-correct triple.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RDFGraph-insert"></a>

### insert

`urn:csabs:operation/RDFGraph-insert`

**signature:** insert : RDFGraph×Triple→RDFGraph

**description:** Set insertion of a triple.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Set insertion of a triple.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RDFGraph-contains"></a>

### contains

`urn:csabs:operation/RDFGraph-contains`

**signature:** contains : RDFGraph×Triple→Prop

**description:** Triple membership.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Triple membership.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RDFGraph-isomorphic"></a>

### isomorphic

`urn:csabs:operation/RDFGraph-isomorphic`

**signature:** isomorphic : RDFGraph²→Prop

**description:** A bijection on occurring blank nodes, fixing IRIs/literals, maps one triple set exactly onto the other.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** A bijection on occurring blank nodes, fixing IRIs/literals, maps one triple set exactly onto the other.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RDFGraph-term-sorts"></a>

### term-sorts

`urn:csabs:axiom/RDFGraph-term-sorts`

**statement:** Defining requirement: I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L

**formalStatement:** I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RDFGraph-set-graph"></a>

### set-graph

`urn:csabs:axiom/RDFGraph-set-graph`

**statement:** Defining requirement: G is a finite set of position-correct triples; equality is triple-set equality

**formalStatement:** G is a finite set of position-correct triples; equality is triple-set equality

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RDFGraph-insertion"></a>

### insertion

`urn:csabs:axiom/RDFGraph-insertion`

**statement:** Defining requirement: u∈insert(G,t) ⇔ u=t ∨ u∈G

**formalStatement:** u∈insert(G,t) ⇔ u=t ∨ u∈G

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RDFGraph-isomorphism"></a>

### isomorphism

`urn:csabs:axiom/RDFGraph-isomorphism`

**statement:** Defining requirement: G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H

**formalStatement:** G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RDFGraph-insert-idempotent"></a>

### insert-idempotent

`urn:csabs:law/RDFGraph-insert-idempotent`

**statement:** insert(insert(G,t),t)=insert(G,t)

**formalStatement:** insert(insert(G,t),t)=insert(G,t)

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [set-graph](RDFGraph.md#node-urn-csabs-axiom-RDFGraph-set-graph); [insertion](RDFGraph.md#node-urn-csabs-axiom-RDFGraph-insertion)

**proofSketch:** Triple membership on both sides is the same disjunction; apply set extensionality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-RDFGraph-iri-not-blank"></a>

### iri-not-blank

`urn:csabs:theorem/RDFGraph-iri-not-blank`

**statement:** For i∈I,b∈B, iri(i)≠blank(b)

**formalStatement:** For i∈I,b∈B, iri(i)≠blank(b)

**assumptions:** IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [term-sorts](RDFGraph.md#node-urn-csabs-axiom-RDFGraph-term-sorts)

**proofSketch:** IRI and blank nodes have disjoint tags even when printable labels look alike.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RDFGraph",
    "type": "Concept",
    "shortForm": "RDFGraph",
    "fullName": "Finite RDF 1.1 graph",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite set of RDF triples with disjoint IRI, blank-node and literal sorts and RDF position restrictions.",
    "notation": "G⊆fin (I⊎B)×I×(I⊎B⊎L)",
    "requiresConcept": [
      "urn:csabs:concept/FiniteSet",
      "urn:csabs:concept/ProductType",
      "urn:csabs:concept/SumType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/PropertyGraph"
    ],
    "hasOperation": [
      "urn:csabs:operation/RDFGraph-triple",
      "urn:csabs:operation/RDFGraph-insert",
      "urn:csabs:operation/RDFGraph-contains",
      "urn:csabs:operation/RDFGraph-isomorphic"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RDFGraph-term-sorts",
      "urn:csabs:axiom/RDFGraph-set-graph",
      "urn:csabs:axiom/RDFGraph-insertion",
      "urn:csabs:axiom/RDFGraph-isomorphism"
    ],
    "hasLaw": [
      "urn:csabs:law/RDFGraph-insert-idempotent"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RDFGraph-iri-not-blank"
    ],
    "axiomBasis": "I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L; G is a finite set of position-correct triples; equality is triple-set equality; u∈insert(G,t) ⇔ u=t ∨ u∈G; G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H",
    "basisKind": "extensional-structural-definition",
    "basisScope": "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFGraph-triple",
    "type": "Operation",
    "name": "triple",
    "signature": "triple : (I⊎B)×I×(I⊎B⊎L)→Triple",
    "description": "Constructs a position-correct triple.",
    "concept": "urn:csabs:concept/RDFGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Constructs a position-correct triple.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFGraph-insert",
    "type": "Operation",
    "name": "insert",
    "signature": "insert : RDFGraph×Triple→RDFGraph",
    "description": "Set insertion of a triple.",
    "concept": "urn:csabs:concept/RDFGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Set insertion of a triple.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFGraph-contains",
    "type": "Operation",
    "name": "contains",
    "signature": "contains : RDFGraph×Triple→Prop",
    "description": "Triple membership.",
    "concept": "urn:csabs:concept/RDFGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Triple membership.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFGraph-isomorphic",
    "type": "Operation",
    "name": "isomorphic",
    "signature": "isomorphic : RDFGraph²→Prop",
    "description": "A bijection on occurring blank nodes, fixing IRIs/literals, maps one triple set exactly onto the other.",
    "concept": "urn:csabs:concept/RDFGraph",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "A bijection on occurring blank nodes, fixing IRIs/literals, maps one triple set exactly onto the other.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RDFGraph-term-sorts",
    "type": "Axiom",
    "name": "term-sorts",
    "statement": "Defining requirement: I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L",
    "formalStatement": "I,B,L are pairwise disjoint tagged sorts; subject∈I⊎B, predicate∈I, object∈I⊎B⊎L",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RDFGraph-set-graph",
    "type": "Axiom",
    "name": "set-graph",
    "statement": "Defining requirement: G is a finite set of position-correct triples; equality is triple-set equality",
    "formalStatement": "G is a finite set of position-correct triples; equality is triple-set equality",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RDFGraph-insertion",
    "type": "Axiom",
    "name": "insertion",
    "statement": "Defining requirement: u∈insert(G,t) ⇔ u=t ∨ u∈G",
    "formalStatement": "u∈insert(G,t) ⇔ u=t ∨ u∈G",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RDFGraph-isomorphism",
    "type": "Axiom",
    "name": "isomorphism",
    "statement": "Defining requirement: G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H",
    "formalStatement": "G≅H iff a bijection on their occurring blank nodes, fixing I and L, maps exactly G onto H",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RDFGraph-insert-idempotent",
    "type": "Law",
    "name": "insert-idempotent",
    "statement": "insert(insert(G,t),t)=insert(G,t)",
    "formalStatement": "insert(insert(G,t),t)=insert(G,t)",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RDFGraph-set-graph",
      "urn:csabs:axiom/RDFGraph-insertion"
    ],
    "proofSketch": "Triple membership on both sides is the same disjunction; apply set extensionality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RDFGraph-iri-not-blank",
    "type": "Theorem",
    "name": "iri-not-blank",
    "statement": "For i∈I,b∈B, iri(i)≠blank(b)",
    "formalStatement": "For i∈I,b∈B, iri(i)≠blank(b)",
    "assumptions": [
      "IRIs are validated absolute IRIs compared by exact string; blank identities have explicit scope. Literals retain lexical form, datatype IRI and language tag where required by RDF 1.1. Term equality, not datatype-value equality. Literal subjects and blank predicates excluded. Graph equality is literal triple-set equality; isomorphism under blank-node renaming is a separate relation. No entailment or IRI normalization. Finite submodel of the standard.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RDFGraph-term-sorts"
    ],
    "proofSketch": "IRI and blank nodes have disjoint tags even when printable labels look alike.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
