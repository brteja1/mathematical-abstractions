# Control-flow graph (single entry, single exit)

A finite directed graph with distinct boundary nodes entry and exit, the unique source and sink respectively; internal nodes represent control locations.

**Notation:** G=(V,E,s,t); s≠t; pred(v)=∅ ⇔ v=s; succ(v)=∅ ⇔ v=t.

**Stable ID:** `urn:csabs:concept/ControlFlowGraph`

**Categories:** Graph theory, Programming-language semantics → Compiler transformations

**Kind:** Mathematical structure

**Prerequisites:** [Directed Graph](DirectedGraph.md)

**Specializes:** [Directed Graph](DirectedGraph.md)

**Related concepts:** [Reachability-qualified control-flow dominance](Dominance.md), [CFG refinement with path correspondence and progress](ControlFlowRefinement.md), [Normal, exceptional and nonlocal control outcomes](ExceptionalControlFlow.md)

## Backlinks

- [CFG refinement with path correspondence and progress](ControlFlowRefinement.md) — `relatedConcept`
- [Reachability-qualified control-flow dominance](Dominance.md) — `relatedConcept`
- [Monotone dataflow framework (forward join profile)](MonotoneDataflow.md) — `relatedConcept`

## Mathematical formulation

G=(V,E,s,t); s≠t; pred(v)=∅ ⇔ v=s; succ(v)=∅ ⇔ v=t. V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.

**Lean formulation** (in its source module context):

```lean
structure ControlFlowGraph (V : Type u) [Fintype V] where
  edge : V → V → Prop
  entry : V
  exit : V
  distinct : entry ≠ exit
  uniqueSource : ∀ v, (¬ ∃ u, edge u v) ↔ v = entry
  uniqueSink : ∀ v, (¬ ∃ w, edge v w) ↔ v = exit
```

**Source:** [`Catalog.Programs.ControlFlowGraph`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** model

**Interpretation:** Finite vertex carrier; directed relation, distinct entry/exit and explicit unique-source/sink conditions.

**Limits:** No normalization algorithm, path enumeration, or proof of the recorded maximal-path law; boundary structure does not imply termination.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Finite directed carrier; distinct unique source and sink; finite-path reflexive transitive closure.

**basisKind:** extensional-structural-definition

**basisScope:** V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.

**specializationNote:** Forget s,t and the finite boundary constraints; keep the same V and E as the directed edge relation.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-ControlFlowGraph-predecessors"></a>

### predecessors

`urn:csabs:operation/ControlFlowGraph-predecessors`

**signature:** pred : V → P(V)

**description:** pred(v)={u∈V | E(u,v)}.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** pred(v)={u∈V | E(u,v)}.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ControlFlowGraph-successors"></a>

### successors

`urn:csabs:operation/ControlFlowGraph-successors`

**signature:** succ : V → P(V)

**description:** succ(v)={w∈V | E(v,w)}.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** succ(v)={w∈V | E(v,w)}.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-ControlFlowGraph-reachable"></a>

### reachable

`urn:csabs:operation/ControlFlowGraph-reachable`

**signature:** reach : V×V → Bool

**description:** reach(u,v) iff a finite E-path exists, including the zero-edge path.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** reach(u,v) iff a finite E-path exists, including the zero-edge path.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-ControlFlowGraph-boundaries"></a>

### boundaries

`urn:csabs:axiom/ControlFlowGraph-boundaries`

**description:** Defining rule for Control-flow graph (single entry, single exit)

**statement:** V finite; s,t∈V; s≠t; ∀v, pred(v)=∅ ⇔ v=s, and succ(v)=∅ ⇔ v=t.

**formalStatement:** V finite; s,t∈V; s≠t; ∀v, pred(v)=∅ ⇔ v=s, and succ(v)=∅ ⇔ v=t.

**assumptions:** V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-ControlFlowGraph-paths"></a>

### paths

`urn:csabs:axiom/ControlFlowGraph-paths`

**description:** Defining rule for Control-flow graph (single entry, single exit)

**statement:** E* is the least relation containing identity and closed under prepending one E edge; reach(u,v) ⇔ E*(u,v).

**formalStatement:** E* is the least relation containing identity and closed under prepending one E edge; reach(u,v) ⇔ E*(u,v).

**assumptions:** V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-ControlFlowGraph-finite-maximal-path-exits"></a>

### finite-maximal-path-exits

`urn:csabs:law/ControlFlowGraph-finite-maximal-path-exits`

**description:** Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.

**statement:** Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.

**formalStatement:** Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.

**assumptions:** V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.

**dependsOn:** [boundaries](ControlFlowGraph.md#node-urn-csabs-axiom-ControlFlowGraph-boundaries); [paths](ControlFlowGraph.md#node-urn-csabs-axiom-ControlFlowGraph-paths)

**proofSketch:** If the last node v were not t, the unique-sink rule supplies a successor and extends the path, contradicting maximality. Infinite paths have no last node.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/ControlFlowGraph",
    "type": "Concept",
    "shortForm": "ControlFlowGraph",
    "fullName": "Control-flow graph (single entry, single exit)",
    "definition": "A finite directed graph with distinct boundary nodes entry and exit, the unique source and sink respectively; internal nodes represent control locations.",
    "notation": "G=(V,E,s,t); s≠t; pred(v)=∅ ⇔ v=s; succ(v)=∅ ⇔ v=t.",
    "category": [
      "urn:csabs:category/graphs",
      "urn:csabs:category/compiler-transformations"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.",
    "axiomBasis": "Finite directed carrier; distinct unique source and sink; finite-path reflexive transitive closure.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "G=(V,E,s,t); s≠t; pred(v)=∅ ⇔ v=s; succ(v)=∅ ⇔ v=t. V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance.",
    "requiresConcept": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "relatedConcept": [
      "urn:csabs:concept/Dominance",
      "urn:csabs:concept/ControlFlowRefinement",
      "urn:csabs:concept/ExceptionalControlFlow"
    ],
    "hasOperation": [
      "urn:csabs:operation/ControlFlowGraph-predecessors",
      "urn:csabs:operation/ControlFlowGraph-successors",
      "urn:csabs:operation/ControlFlowGraph-reachable"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/ControlFlowGraph-boundaries",
      "urn:csabs:axiom/ControlFlowGraph-paths"
    ],
    "hasLaw": [
      "urn:csabs:law/ControlFlowGraph-finite-maximal-path-exits"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/DirectedGraph"
    ],
    "specializationNote": "Forget s,t and the finite boundary constraints; keep the same V and E as the directed edge relation.",
    "leanFormulation": "structure ControlFlowGraph (V : Type u) [Fintype V] where\n  edge : V → V → Prop\n  entry : V\n  exit : V\n  distinct : entry ≠ exit\n  uniqueSource : ∀ v, (¬ ∃ u, edge u v) ↔ v = entry\n  uniqueSink : ∀ v, (¬ ∃ w, edge v w) ↔ v = exit",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.ControlFlowGraph",
    "formulationScope": "model",
    "leanModelMapping": "Finite vertex carrier; directed relation, distinct entry/exit and explicit unique-source/sink conditions.",
    "leanModelLimitations": "No normalization algorithm, path enumeration, or proof of the recorded maximal-path law; boundary structure does not imply termination."
  },
  {
    "id": "urn:csabs:operation/ControlFlowGraph-predecessors",
    "type": "Operation",
    "name": "predecessors",
    "signature": "pred : V → P(V)",
    "description": "pred(v)={u∈V | E(u,v)}.",
    "concept": "urn:csabs:concept/ControlFlowGraph",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "pred(v)={u∈V | E(u,v)}.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ControlFlowGraph-successors",
    "type": "Operation",
    "name": "successors",
    "signature": "succ : V → P(V)",
    "description": "succ(v)={w∈V | E(v,w)}.",
    "concept": "urn:csabs:concept/ControlFlowGraph",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "succ(v)={w∈V | E(v,w)}.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/ControlFlowGraph-reachable",
    "type": "Operation",
    "name": "reachable",
    "signature": "reach : V×V → Bool",
    "description": "reach(u,v) iff a finite E-path exists, including the zero-edge path.",
    "concept": "urn:csabs:concept/ControlFlowGraph",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "reach(u,v) iff a finite E-path exists, including the zero-edge path.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ControlFlowGraph-boundaries",
    "type": "Axiom",
    "name": "boundaries",
    "description": "Defining rule for Control-flow graph (single entry, single exit)",
    "statement": "V finite; s,t∈V; s≠t; ∀v, pred(v)=∅ ⇔ v=s, and succ(v)=∅ ⇔ v=t.",
    "formalStatement": "V finite; s,t∈V; s≠t; ∀v, pred(v)=∅ ⇔ v=s, and succ(v)=∅ ⇔ v=t.",
    "assumptions": [
      "V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/ControlFlowGraph-paths",
    "type": "Axiom",
    "name": "paths",
    "description": "Defining rule for Control-flow graph (single entry, single exit)",
    "statement": "E* is the least relation containing identity and closed under prepending one E edge; reach(u,v) ⇔ E*(u,v).",
    "formalStatement": "E* is the least relation containing identity and closed under prepending one E edge; reach(u,v) ⇔ E*(u,v).",
    "assumptions": [
      "V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowGraph"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/ControlFlowGraph-finite-maximal-path-exits",
    "type": "Law",
    "name": "finite-maximal-path-exits",
    "description": "Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.",
    "statement": "Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.",
    "formalStatement": "Every finite path from s that cannot be extended ends at t. This does not imply all executions terminate.",
    "assumptions": [
      "V is finite with exact vertex equality; E⊆V×V collapses parallel edges and may contain internal self-loops. Entry and exit are distinct synthetic boundary nodes. Unreachable internal cycles and an unreachable exit are allowed. Infinite paths may avoid exit, and not every node need reach exit. Multiple returns are normalized to the exit; exceptional/nonlocal exits require explicit normalization. This is a whole-graph boundary convention, not a SESE region defined by dominance/postdominance."
    ],
    "appliesTo": [
      "urn:csabs:concept/ControlFlowGraph"
    ],
    "dependsOn": [
      "urn:csabs:axiom/ControlFlowGraph-boundaries",
      "urn:csabs:axiom/ControlFlowGraph-paths"
    ],
    "proofSketch": "If the last node v were not t, the unique-sink rule supplies a successor and extends the path, contradicting maximality. Infinite paths have no last node.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§2.5, pp.16–17; adapted with finite carrier, distinct boundaries and unique source/sink rules.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
