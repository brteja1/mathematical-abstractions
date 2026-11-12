# Finite RDF 1.1 dataset

One default RDF graph and a finite partial map from IRI-or-blank graph names to named RDF graphs.

**Notation:** Dataset=(G_default, N:(I⊎B)⇀fin RDFGraph)

**Stable ID:** `urn:csabs:concept/RDFDataset`

**Categories:** Relational data modelling

**Kind:** Abstract data type

**Prerequisites:** [Finite RDF 1.1 graph](RDFGraph.md), [Map](Map.md), [Option Type](OptionType.md)

## Mathematical formulation

A dataset is (G₀,N), G₀ an RDF graph and N a finite partial map (I+B)⇀Graph. A missing graph name differs from a present name mapped to the empty graph. Shared blank-node scope must be instantiated explicitly.

**Lean formulation** (in its source module context):

```lean
structure RDFDataset (I : Type u) (B : Type v) (L : Type w) where
  defaultGraph : RDFGraph I B L
  namedGraphs : Catalog.Map (I ⊕ B) (RDFGraph I B L)
```

**Source:** [`Catalog.RDFDataset`](../lean/Catalog/InformationData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Default Finset triple graph plus Catalog.Map (I⊕B) RDFGraph; blank scopes and validated term carriers are caller obligations. Dataset=(G_default, N:(I⊎B)⇀fin RDFGraph). Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph; D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n); default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)

**basisKind:** extensional-structural-definition

**basisScope:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RDFDataset-default"></a>

### default

`urn:csabs:operation/RDFDataset-default`

**signature:** default : Dataset→RDFGraph

**description:** Returns the one default graph.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the one default graph.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RDFDataset-named"></a>

### named

`urn:csabs:operation/RDFDataset-named`

**signature:** named : Dataset×(I⊎B)→Option(RDFGraph)

**description:** None if graph name absent; Some(G) if present, including G=∅.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** None if graph name absent; Some(G) if present, including G=∅.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RDFDataset-put-named"></a>

### put-named

`urn:csabs:operation/RDFDataset-put-named`

**signature:** putNamed : Dataset×(I⊎B)×RDFGraph→Dataset

**description:** Adds/overwrites just this named graph, preserving default.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Adds/overwrites just this named graph, preserving default.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RDFDataset-dataset-carrier"></a>

### dataset-carrier

`urn:csabs:axiom/RDFDataset-dataset-carrier`

**statement:** Defining requirement: Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph

**formalStatement:** Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph

**assumptions:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RDFDataset-equality"></a>

### equality

`urn:csabs:axiom/RDFDataset-equality`

**statement:** Defining requirement: D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n)

**formalStatement:** D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n)

**assumptions:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RDFDataset-put-equations"></a>

### put-equations

`urn:csabs:axiom/RDFDataset-put-equations`

**statement:** Defining requirement: default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)

**formalStatement:** default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)

**assumptions:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RDFDataset-read-after-put"></a>

### read-after-put

`urn:csabs:law/RDFDataset-read-after-put`

**statement:** named(putNamed(D,n,G),n)=Some(G)

**formalStatement:** named(putNamed(D,n,G),n)=Some(G)

**assumptions:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [put-equations](RDFDataset.md#node-urn-csabs-axiom-RDFDataset-put-equations)

**proofSketch:** Use the equal-name branch of put-equations.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [W3C RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** §§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-RDFDataset-empty-not-absent"></a>

### empty-not-absent

`urn:csabs:theorem/RDFDataset-empty-not-absent`

**statement:** named(D,n)=Some(∅) ⇒ named(D,n)≠None

**formalStatement:** named(D,n)=Some(∅) ⇒ named(D,n)≠None

**assumptions:** Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [dataset-carrier](RDFDataset.md#node-urn-csabs-axiom-RDFDataset-dataset-carrier)

**proofSketch:** Some and None are distinct option constructors, so a present empty graph remains observable.

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
    "id": "urn:csabs:concept/RDFDataset",
    "type": "Concept",
    "shortForm": "RDFDataset",
    "fullName": "Finite RDF 1.1 dataset",
    "category": [
      "urn:csabs:category/data-modelling"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "One default RDF graph and a finite partial map from IRI-or-blank graph names to named RDF graphs.",
    "notation": "Dataset=(G_default, N:(I⊎B)⇀fin RDFGraph)",
    "requiresConcept": [
      "urn:csabs:concept/RDFGraph",
      "urn:csabs:concept/Map",
      "urn:csabs:concept/OptionType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/RDFDataset-default",
      "urn:csabs:operation/RDFDataset-named",
      "urn:csabs:operation/RDFDataset-put-named"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RDFDataset-dataset-carrier",
      "urn:csabs:axiom/RDFDataset-equality",
      "urn:csabs:axiom/RDFDataset-put-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/RDFDataset-read-after-put"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RDFDataset-empty-not-absent"
    ],
    "axiomBasis": "Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph; D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n); default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
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
    "provenanceKind": "adapted",
    "leanFormulation": "structure RDFDataset (I : Type u) (B : Type v) (L : Type w) where\n  defaultGraph : RDFGraph I B L\n  namedGraphs : Catalog.Map (I ⊕ B) (RDFGraph I B L)",
    "formulationSource": "urn:csabs:source/local-lean-InformationData",
    "formulationLocator": "Catalog.RDFDataset",
    "formulationScope": "model",
    "leanModelMapping": "Default Finset triple graph plus Catalog.Map (I⊕B) RDFGraph; blank scopes and validated term carriers are caller obligations. Dataset=(G_default, N:(I⊎B)⇀fin RDFGraph). Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A dataset is (G₀,N), G₀ an RDF graph and N a finite partial map (I+B)⇀Graph. A missing graph name differs from a present name mapped to the empty graph. Shared blank-node scope must be instantiated explicitly."
  },
  {
    "id": "urn:csabs:operation/RDFDataset-default",
    "type": "Operation",
    "name": "default",
    "signature": "default : Dataset→RDFGraph",
    "description": "Returns the one default graph.",
    "concept": "urn:csabs:concept/RDFDataset",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the one default graph.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFDataset-named",
    "type": "Operation",
    "name": "named",
    "signature": "named : Dataset×(I⊎B)→Option(RDFGraph)",
    "description": "None if graph name absent; Some(G) if present, including G=∅.",
    "concept": "urn:csabs:concept/RDFDataset",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "None if graph name absent; Some(G) if present, including G=∅.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RDFDataset-put-named",
    "type": "Operation",
    "name": "put-named",
    "signature": "putNamed : Dataset×(I⊎B)×RDFGraph→Dataset",
    "description": "Adds/overwrites just this named graph, preserving default.",
    "concept": "urn:csabs:concept/RDFDataset",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Adds/overwrites just this named graph, preserving default.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RDFDataset-dataset-carrier",
    "type": "Axiom",
    "name": "dataset-carrier",
    "statement": "Defining requirement: Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph",
    "formalStatement": "Exactly one default graph; named graphs are a finite partial map with names in I⊎B and values RDFGraph",
    "assumptions": [
      "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFDataset"
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
    "id": "urn:csabs:axiom/RDFDataset-equality",
    "type": "Axiom",
    "name": "equality",
    "statement": "Defining requirement: D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n)",
    "formalStatement": "D=E ⇔ default(D)=default(E) ∧ ∀n,named(D,n)=named(E,n)",
    "assumptions": [
      "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFDataset"
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
    "id": "urn:csabs:axiom/RDFDataset-put-equations",
    "type": "Axiom",
    "name": "put-equations",
    "statement": "Defining requirement: default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)",
    "formalStatement": "default(putNamed(D,n,G))=default(D); named(putNamed(D,n,G),m)=Some(G) if m=n, else named(D,m)",
    "assumptions": [
      "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFDataset"
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
    "id": "urn:csabs:law/RDFDataset-read-after-put",
    "type": "Law",
    "name": "read-after-put",
    "statement": "named(putNamed(D,n,G),n)=Some(G)",
    "formalStatement": "named(putNamed(D,n,G),n)=Some(G)",
    "assumptions": [
      "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFDataset"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RDFDataset-put-equations"
    ],
    "proofSketch": "Use the equal-name branch of put-equations.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/w3c-rdf11-core"
    ],
    "sourceLocator": "§§3–4: RDF triples, IRIs, literals, blank nodes, graph isomorphism and datasets",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RDFDataset-empty-not-absent",
    "type": "Theorem",
    "name": "empty-not-absent",
    "statement": "named(D,n)=Some(∅) ⇒ named(D,n)≠None",
    "formalStatement": "named(D,n)=Some(∅) ⇒ named(D,n)≠None",
    "assumptions": [
      "Graph names unique; no literal names. Blank identities share an explicit dataset scope and may occur in multiple graphs. Default graph is not assumed to be the union of named graphs. Absent graph differs from present empty graph. Dataset equality retains names and blank identities; no entailment or dataset-canonicalization claim.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RDFDataset"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RDFDataset-dataset-carrier"
    ],
    "proofSketch": "Some and None are distinct option constructors, so a present empty graph remains observable.",
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
