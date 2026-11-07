# Finite rooted undirected tree

A finite nonempty simple undirected connected acyclic graph with a distinguished vertex as root.

**Notation:** (V,E,r), r∈V; (V,E) a Tree

**Stable ID:** `urn:csabs:concept/RootedTree`

**Categories:** Graph theory

**Kind:** Abstract data type

**Prerequisites:** [Tree](Tree.md)

**Specializes:** [Tree](Tree.md)

## Backlinks

- [Finite ordered rose tree](RoseTree.md) — `relatedConcept`

## Interface and scope

**axiomBasis:** V finite; r∈V; (V,E) is simple, undirected, connected and acyclic; For v≠r, parent(v) is the next vertex on the unique simple path v→r; depth(v) is the edge length of the unique simple path v→r, including length 0 at r

**basisKind:** extensional-structural-definition

**basisScope:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.

**specializationNote:** Forget r and retain the same finite nonempty simple graph. Adding a root does not add child ordering or a binary-tree empty constructor.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RootedTree-root"></a>

### root

`urn:csabs:operation/RootedTree-root`

**signature:** root : RootedTree(V)→V

**description:** Returns distinguished vertex r.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns distinguished vertex r.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RootedTree-parent"></a>

### parent

`urn:csabs:operation/RootedTree-parent`

**signature:** parent : RootedTree(V)×(V∖{r})→V

**description:** Returns the neighbor of v on the unique simple path from v to r.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Returns the neighbor of v on the unique simple path from v to r.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RootedTree-depth"></a>

### depth

`urn:csabs:operation/RootedTree-depth`

**signature:** depth : RootedTree(V)×V→ℕ

**description:** Number of edges on the unique simple path to r.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Number of edges on the unique simple path to r.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RootedTree-tree-carrier"></a>

### tree-carrier

`urn:csabs:axiom/RootedTree-tree-carrier`

**statement:** Defining requirement: V finite; r∈V; (V,E) is simple, undirected, connected and acyclic

**formalStatement:** V finite; r∈V; (V,E) is simple, undirected, connected and acyclic

**assumptions:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RootedTree-parent-definition"></a>

### parent-definition

`urn:csabs:axiom/RootedTree-parent-definition`

**statement:** Defining requirement: For v≠r, parent(v) is the next vertex on the unique simple path v→r

**formalStatement:** For v≠r, parent(v) is the next vertex on the unique simple path v→r

**assumptions:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RootedTree-depth-definition"></a>

### depth-definition

`urn:csabs:axiom/RootedTree-depth-definition`

**statement:** Defining requirement: depth(v) is the edge length of the unique simple path v→r, including length 0 at r

**formalStatement:** depth(v) is the edge length of the unique simple path v→r, including length 0 at r

**assumptions:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RootedTree-root-depth"></a>

### root-depth

`urn:csabs:law/RootedTree-root-depth`

**statement:** depth(r)=0

**formalStatement:** depth(r)=0

**assumptions:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [tree-carrier](RootedTree.md#node-urn-csabs-axiom-RootedTree-tree-carrier); [depth-definition](RootedTree.md#node-urn-csabs-axiom-RootedTree-depth-definition)

**proofSketch:** The simple path from r to itself is empty, so has edge length zero.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-RootedTree-parent-depth"></a>

### parent-depth

`urn:csabs:theorem/RootedTree-parent-depth`

**statement:** v≠r ⇒ depth(parent(v))+1=depth(v)

**formalStatement:** v≠r ⇒ depth(parent(v))+1=depth(v)

**assumptions:** Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [tree-carrier](RootedTree.md#node-urn-csabs-axiom-RootedTree-tree-carrier); [parent-definition](RootedTree.md#node-urn-csabs-axiom-RootedTree-parent-definition); [depth-definition](RootedTree.md#node-urn-csabs-axiom-RootedTree-depth-definition)

**proofSketch:** The unique path v→r starts with v→parent(v); its tail is the unique path parent(v)→r. Count edges.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Pat Morin: Open Data Structures, Binary Trees](https://opendatastructures.org/ods-python/6_Binary_Trees.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Chapter 6: root, parent, children and path to root; generalized here beyond binary branching

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RootedTree",
    "type": "Concept",
    "shortForm": "RootedTree",
    "fullName": "Finite rooted undirected tree",
    "category": [
      "urn:csabs:category/graphs"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "A finite nonempty simple undirected connected acyclic graph with a distinguished vertex as root.",
    "notation": "(V,E,r), r∈V; (V,E) a Tree",
    "requiresConcept": [
      "urn:csabs:concept/Tree"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/RootedTree-root",
      "urn:csabs:operation/RootedTree-parent",
      "urn:csabs:operation/RootedTree-depth"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RootedTree-tree-carrier",
      "urn:csabs:axiom/RootedTree-parent-definition",
      "urn:csabs:axiom/RootedTree-depth-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/RootedTree-root-depth"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RootedTree-parent-depth"
    ],
    "axiomBasis": "V finite; r∈V; (V,E) is simple, undirected, connected and acyclic; For v≠r, parent(v) is the next vertex on the unique simple path v→r; depth(v) is the edge length of the unique simple path v→r, including length 0 at r",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Tree"
    ],
    "specializationNote": "Forget r and retain the same finite nonempty simple graph. Adding a root does not add child ordering or a binary-tree empty constructor."
  },
  {
    "id": "urn:csabs:operation/RootedTree-root",
    "type": "Operation",
    "name": "root",
    "signature": "root : RootedTree(V)→V",
    "description": "Returns distinguished vertex r.",
    "concept": "urn:csabs:concept/RootedTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns distinguished vertex r.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RootedTree-parent",
    "type": "Operation",
    "name": "parent",
    "signature": "parent : RootedTree(V)×(V∖{r})→V",
    "description": "Returns the neighbor of v on the unique simple path from v to r.",
    "concept": "urn:csabs:concept/RootedTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Returns the neighbor of v on the unique simple path from v to r.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RootedTree-depth",
    "type": "Operation",
    "name": "depth",
    "signature": "depth : RootedTree(V)×V→ℕ",
    "description": "Number of edges on the unique simple path to r.",
    "concept": "urn:csabs:concept/RootedTree",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Number of edges on the unique simple path to r.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RootedTree-tree-carrier",
    "type": "Axiom",
    "name": "tree-carrier",
    "statement": "Defining requirement: V finite; r∈V; (V,E) is simple, undirected, connected and acyclic",
    "formalStatement": "V finite; r∈V; (V,E) is simple, undirected, connected and acyclic",
    "assumptions": [
      "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RootedTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RootedTree-parent-definition",
    "type": "Axiom",
    "name": "parent-definition",
    "statement": "Defining requirement: For v≠r, parent(v) is the next vertex on the unique simple path v→r",
    "formalStatement": "For v≠r, parent(v) is the next vertex on the unique simple path v→r",
    "assumptions": [
      "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RootedTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RootedTree-depth-definition",
    "type": "Axiom",
    "name": "depth-definition",
    "statement": "Defining requirement: depth(v) is the edge length of the unique simple path v→r, including length 0 at r",
    "formalStatement": "depth(v) is the edge length of the unique simple path v→r, including length 0 at r",
    "assumptions": [
      "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/RootedTree"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RootedTree-root-depth",
    "type": "Law",
    "name": "root-depth",
    "statement": "depth(r)=0",
    "formalStatement": "depth(r)=0",
    "assumptions": [
      "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RootedTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RootedTree-tree-carrier",
      "urn:csabs:axiom/RootedTree-depth-definition"
    ],
    "proofSketch": "The simple path from r to itself is empty, so has edge length zero.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/RootedTree-parent-depth",
    "type": "Theorem",
    "name": "parent-depth",
    "statement": "v≠r ⇒ depth(parent(v))+1=depth(v)",
    "formalStatement": "v≠r ⇒ depth(parent(v))+1=depth(v)",
    "assumptions": [
      "Vertex identities retained; child order and labels not built in. Single-vertex tree valid. Parent of root undefined. No empty rooted tree, binary branching constraint or pointer representation.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/RootedTree"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RootedTree-tree-carrier",
      "urn:csabs:axiom/RootedTree-parent-definition",
      "urn:csabs:axiom/RootedTree-depth-definition"
    ],
    "proofSketch": "The unique path v→r starts with v→parent(v); its tail is the unique path parent(v)→r. Count edges.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/ods-trees-core"
    ],
    "sourceLocator": "Chapter 6: root, parent, children and path to root; generalized here beyond binary branching",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
