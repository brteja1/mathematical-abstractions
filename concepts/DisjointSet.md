# Union Find (disjoint-set union with representatives)

The Union Find (UnionFind, disjoint-set union, DSU) abstract data structure: a finite universe partition represented by an idempotent choice of representative for each element, supporting find, connected and union.

**Notation:** D_n={r:Fin(n)→Fin(n) | r(r(x))=r(x)}

**Stable ID:** `urn:csabs:concept/DisjointSet`

**Categories:** Data structures → Connectivity structures

**Kind:** Abstract data type

**Prerequisites:** [Partition of a set](Partition.md), [Equivalence relation](EquivalenceRelation.md), [Finite carrier with exhaustive enumeration](FiniteType.md)

## Mathematical formulation

On Fin(n), a disjoint-set value is r:Fin(n)→Fin(n) satisfying r(r(x))=r(x). connected(x,y) ⇔ r(x)=r(y). A union replaces both affected classes' representatives by one of their two old representatives.

**Lean formulation** (in its source module context):

```lean
structure DisjointSet (n : Nat) where
  representative : Fin n → Fin n
  idempotent : ∀ x, representative (representative x) = representative x
```

**Source:** [`Catalog.DisjointSet`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** D_n={r:Fin(n)→Fin(n) | r(r(x))=r(x)}. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** ∀x, r(r(x))=r(x); connected(r,x,y) ⇔ r(x)=r(y); r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)

**basisKind:** extensional-structural-definition

**basisScope:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-DisjointSet-initial"></a>

### initial

`urn:csabs:operation/DisjointSet-initial`

**signature:** initial_n : D_n

**description:** initial_n(x)=x.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** initial_n(x)=x.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DisjointSet-find"></a>

### find

`urn:csabs:operation/DisjointSet-find`

**signature:** find : D_n×Fin(n)→Fin(n)

**description:** find(r,x)=r(x).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** find(r,x)=r(x).

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DisjointSet-connected"></a>

### connected

`urn:csabs:operation/DisjointSet-connected`

**signature:** connected : D_n×Fin(n)²→Prop

**description:** connected(r,x,y) iff r(x)=r(y).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** connected(r,x,y) iff r(x)=r(y).

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-DisjointSet-union"></a>

### union

`urn:csabs:operation/DisjointSet-union`

**signature:** union : D_n×Fin(n)²→𝒫(D_n)

**description:** Choose c∈{r(a),r(b)}; r′(x)=c when r(x)∈{r(a),r(b)}, else r(x).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Choose c∈{r(a),r(b)}; r′(x)=c when r(x)∈{r(a),r(b)}, else r(x).

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-DisjointSet-representative"></a>

### representative

`urn:csabs:axiom/DisjointSet-representative`

**statement:** Defining requirement: ∀x, r(r(x))=r(x)

**formalStatement:** ∀x, r(r(x))=r(x)

**assumptions:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DisjointSet-connectivity"></a>

### connectivity

`urn:csabs:axiom/DisjointSet-connectivity`

**statement:** Defining requirement: connected(r,x,y) ⇔ r(x)=r(y)

**formalStatement:** connected(r,x,y) ⇔ r(x)=r(y)

**assumptions:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-DisjointSet-union-definition"></a>

### union-definition

`urn:csabs:axiom/DisjointSet-union-definition`

**statement:** Defining requirement: r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)

**formalStatement:** r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)

**assumptions:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-DisjointSet-find-idempotent"></a>

### find-idempotent

`urn:csabs:law/DisjointSet-find-idempotent`

**statement:** find(r,find(r,x))=find(r,x)

**formalStatement:** find(r,find(r,x))=find(r,x)

**assumptions:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [representative](DisjointSet.md#node-urn-csabs-axiom-DisjointSet-representative)

**proofSketch:** Expand find; this is the representative invariant.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {n : Nat} (d : Catalog.DisjointSet n) (x : Fin n), d.representative (d.representative x) = d.representative x
```

**Source:** [`Catalog.StructuredDataProofs.disjoint_set_find_idempotent`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** Finite universe is Fin n; find is the representative function. Its idempotence is the structure invariant, with no assumed parent-pointer implementation.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DisjointSet-representative": "Interpreted premise: ∀x, r(r(x))=r(x). Finite universe is Fin n; find is the representative function. Its idempotence is the structure invariant, with no assumed parent-pointer implementation."
}
```

## Theorems

<a id="node-urn-csabs-theorem-DisjointSet-connected-symmetric"></a>

### connected-symmetric

`urn:csabs:theorem/DisjointSet-connected-symmetric`

**statement:** connected(r,x,y) ⇒ connected(r,y,x)

**formalStatement:** connected(r,x,y) ⇒ connected(r,y,x)

**assumptions:** Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [connectivity](DisjointSet.md#node-urn-csabs-axiom-DisjointSet-connectivity)

**proofSketch:** Expand connectivity and apply symmetry of equality.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {n : Nat} (d : Catalog.DisjointSet n) (x y : Fin n), d.connected x y → d.connected y x
```

**Source:** [`Catalog.StructuredDataProofs.disjoint_set_connected_symmetric`](../lean/Catalog/StructuredData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** connected means equality of representative outputs in Fin n. Symmetry follows from equality symmetry; no representative selection policy is needed.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/DisjointSet-connectivity": "Interpreted premise: connected(r,x,y) ⇔ r(x)=r(y). connected means equality of representative outputs in Fin n. Symmetry follows from equality symmetry; no representative selection policy is needed."
}
```

## Concept provenance

- [Sedgewick and Wayne: algs4 UF API](https://javadoc.io/static/edu.princeton.cs/algs4/1.0.4/edu/princeton/cs/algs4/UF.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Class contract: sites, components, representative, find, union and connected

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation. Union Find and disjoint-sets synonymy reconfirmed from the UF class contract on 2026-11-08; stable ID and representative semantics are preserved.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/DisjointSet",
    "type": "Concept",
    "shortForm": "DisjointSet",
    "fullName": "Union Find (disjoint-set union with representatives)",
    "category": [
      "urn:csabs:category/connectivity-structures"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "The Union Find (UnionFind, disjoint-set union, DSU) abstract data structure: a finite universe partition represented by an idempotent choice of representative for each element, supporting find, connected and union.",
    "notation": "D_n={r:Fin(n)→Fin(n) | r(r(x))=r(x)}",
    "requiresConcept": [
      "urn:csabs:concept/Partition",
      "urn:csabs:concept/EquivalenceRelation",
      "urn:csabs:concept/FiniteType"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/DisjointSet-initial",
      "urn:csabs:operation/DisjointSet-find",
      "urn:csabs:operation/DisjointSet-connected",
      "urn:csabs:operation/DisjointSet-union"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/DisjointSet-representative",
      "urn:csabs:axiom/DisjointSet-connectivity",
      "urn:csabs:axiom/DisjointSet-union-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/DisjointSet-find-idempotent"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/DisjointSet-connected-symmetric"
    ],
    "axiomBasis": "∀x, r(r(x))=r(x); connected(r,x,y) ⇔ r(x)=r(y); r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation. Union Find and disjoint-sets synonymy reconfirmed from the UF class contract on 2026-11-08; stable ID and representative semantics are preserved.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure DisjointSet (n : Nat) where\n  representative : Fin n → Fin n\n  idempotent : ∀ x, representative (representative x) = representative x",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.DisjointSet",
    "formulationScope": "model",
    "leanModelMapping": "D_n={r:Fin(n)→Fin(n) | r(r(x))=r(x)}. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "On Fin(n), a disjoint-set value is r:Fin(n)→Fin(n) satisfying r(r(x))=r(x). connected(x,y) ⇔ r(x)=r(y). A union replaces both affected classes' representatives by one of their two old representatives."
  },
  {
    "id": "urn:csabs:operation/DisjointSet-initial",
    "type": "Operation",
    "name": "initial",
    "signature": "initial_n : D_n",
    "description": "initial_n(x)=x.",
    "concept": "urn:csabs:concept/DisjointSet",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "initial_n(x)=x.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DisjointSet-find",
    "type": "Operation",
    "name": "find",
    "signature": "find : D_n×Fin(n)→Fin(n)",
    "description": "find(r,x)=r(x).",
    "concept": "urn:csabs:concept/DisjointSet",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "find(r,x)=r(x).",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DisjointSet-connected",
    "type": "Operation",
    "name": "connected",
    "signature": "connected : D_n×Fin(n)²→Prop",
    "description": "connected(r,x,y) iff r(x)=r(y).",
    "concept": "urn:csabs:concept/DisjointSet",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "connected(r,x,y) iff r(x)=r(y).",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/DisjointSet-union",
    "type": "Operation",
    "name": "union",
    "signature": "union : D_n×Fin(n)²→𝒫(D_n)",
    "description": "Choose c∈{r(a),r(b)}; r′(x)=c when r(x)∈{r(a),r(b)}, else r(x).",
    "concept": "urn:csabs:concept/DisjointSet",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Choose c∈{r(a),r(b)}; r′(x)=c when r(x)∈{r(a),r(b)}, else r(x).",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DisjointSet-representative",
    "type": "Axiom",
    "name": "representative",
    "statement": "Defining requirement: ∀x, r(r(x))=r(x)",
    "formalStatement": "∀x, r(r(x))=r(x)",
    "assumptions": [
      "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DisjointSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DisjointSet-connectivity",
    "type": "Axiom",
    "name": "connectivity",
    "statement": "Defining requirement: connected(r,x,y) ⇔ r(x)=r(y)",
    "formalStatement": "connected(r,x,y) ⇔ r(x)=r(y)",
    "assumptions": [
      "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DisjointSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/DisjointSet-union-definition",
    "type": "Axiom",
    "name": "union-definition",
    "statement": "Defining requirement: r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)",
    "formalStatement": "r′∈union(r,a,b) ⇔ ∃c∈{r(a),r(b)}, ∀x, r′(x)=if r(x)∈{r(a),r(b)} then c else r(x)",
    "assumptions": [
      "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/DisjointSet"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/DisjointSet-find-idempotent",
    "type": "Law",
    "name": "find-idempotent",
    "statement": "find(r,find(r,x))=find(r,x)",
    "formalStatement": "find(r,find(r,x))=find(r,x)",
    "assumptions": [
      "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DisjointSet"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DisjointSet-representative"
    ],
    "proofSketch": "Expand find; this is the representative invariant.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {n : Nat} (d : Catalog.DisjointSet n) (x : Fin n), d.representative (d.representative x) = d.representative x",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.StructuredDataProofs.disjoint_set_find_idempotent",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "Finite universe is Fin n; find is the representative function. Its idempotence is the structure invariant, with no assumed parent-pointer implementation.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DisjointSet-representative\": \"Interpreted premise: ∀x, r(r(x))=r(x). Finite universe is Fin n; find is the representative function. Its idempotence is the structure invariant, with no assumed parent-pointer implementation.\"}"
  },
  {
    "id": "urn:csabs:theorem/DisjointSet-connected-symmetric",
    "type": "Theorem",
    "name": "connected-symmetric",
    "statement": "connected(r,x,y) ⇒ connected(r,y,x)",
    "formalStatement": "connected(r,x,y) ⇒ connected(r,y,x)",
    "assumptions": [
      "Fixed universe {0,…,n-1}, including n=0. Representative identity observable; union may choose either previous root. No path compression/rank representation or complexity bound. Equality is equality of representative maps.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/DisjointSet"
    ],
    "dependsOn": [
      "urn:csabs:axiom/DisjointSet-connectivity"
    ],
    "proofSketch": "Expand connectivity and apply symmetry of equality.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/algs4-uf-core"
    ],
    "sourceLocator": "Class contract: sites, components, representative, find, union and connected",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {n : Nat} (d : Catalog.DisjointSet n) (x y : Fin n), d.connected x y → d.connected y x",
    "formulationSource": "urn:csabs:source/local-lean-StructuredData",
    "formulationLocator": "Catalog.StructuredDataProofs.disjoint_set_connected_symmetric",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "connected means equality of representative outputs in Fin n. Symmetry follows from equality symmetry; no representative selection policy is needed.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/DisjointSet-connectivity\": \"Interpreted premise: connected(r,x,y) ⇔ r(x)=r(y). connected means equality of representative outputs in Fin n. Symmetry follows from equality symmetry; no representative selection policy is needed.\"}"
  }
]
```
<!-- graph-record:end -->
