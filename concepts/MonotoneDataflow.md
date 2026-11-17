# Monotone dataflow framework (forward join profile)

A finite dependency graph with complete-lattice facts, boundary facts and monotone edge transfer functions, interpreted as a system of dataflow equations.

**Notation:** F(x)(v)=b(v) ⊔ ⋁{f(u,v)(x(u)) | E(u,v)}; x*=lfp(F).

**Stable ID:** `urn:csabs:concept/MonotoneDataflow`

**Categories:** Programming-language semantics → Compiler transformations, Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Complete Lattice](CompleteLattice.md), [Monotone Function](MonotoneFunction.md)

**Related concepts:** [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md), [Control-flow graph (single entry, single exit)](ControlFlowGraph.md), [Integer interval abstract domain (empty and unbounded intervals)](IntervalDomain.md), [Fixed Point](FixedPoint.md)

## Backlinks

- [Sound abstract transfer and inductive dataflow facts](AbstractInterpretation.md) — `relatedConcept`
- [Integer interval abstract domain (empty and unbounded intervals)](IntervalDomain.md) — `relatedConcept`

## Mathematical formulation

F(x)(v)=b(v) ⊔ ⋁{f(u,v)(x(u)) | E(u,v)}; x\*=lfp(F). V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**Lean formulation** (in its source module context):

```lean
structure MonotoneDataflow (V : Type u) (L : Type v) [Fintype V] [CompleteLattice L] where
  edge : V → V → Prop
  boundary : V → L
  transfer : V → V → L → L
  monotone : ∀ u v, edge u v → Monotone (transfer u v)
```

**Source:** [`Catalog.Programs.MonotoneDataflow`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** partial

**Interpretation:** Finite graph, complete lattice, boundary facts and edge-qualified monotone transfers. The step declaration uses suprema for the forward join equations.

**Limits:** No concretization soundness proof, solver, convergence proof or registered least-solution witness.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Complete fact lattice, pointwise product, total monotone edge transfers and explicit boundary-join equations.

**basisKind:** extensional-structural-definition

**basisScope:** V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-MonotoneDataflow-transfer"></a>

### transfer

`urn:csabs:operation/MonotoneDataflow-transfer`

**signature:** f : E → (L → L)

**description:** Apply the selected monotone edge transfer; node transfers can be assigned to all outgoing edges.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Apply the selected monotone edge transfer; node transfers can be assigned to all outgoing edges.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MonotoneDataflow-step"></a>

### step

`urn:csabs:operation/MonotoneDataflow-step`

**signature:** F : (V→L) → (V→L)

**description:** Evaluate all displayed equations simultaneously, preserving boundary contributions.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Evaluate all displayed equations simultaneously, preserving boundary contributions.

**totality:** Total on the displayed typed domain.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-MonotoneDataflow-least-solution"></a>

### least-solution

`urn:csabs:operation/MonotoneDataflow-least-solution`

**signature:** solve : Framework → (V→L)

**description:** Return the mathematical least fixed point of F; no finite-time algorithm is implied.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return the mathematical least fixed point of F; no finite-time algorithm is implied.

**totality:** Total mathematical operator, not a promised terminating implementation.

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-MonotoneDataflow-fact-lattice"></a>

### fact-lattice

`urn:csabs:axiom/MonotoneDataflow-fact-lattice`

**description:** Defining rule for Monotone dataflow framework (forward join profile)

**statement:** L is a complete lattice; V→L has pointwise order and pointwise arbitrary suprema and infima.

**formalStatement:** L is a complete lattice; V→L has pointwise order and pointwise arbitrary suprema and infima.

**assumptions:** V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-MonotoneDataflow-transfer-monotonicity"></a>

### transfer-monotonicity

`urn:csabs:axiom/MonotoneDataflow-transfer-monotonicity`

**description:** Defining rule for Monotone dataflow framework (forward join profile)

**statement:** For every (u,v)∈E, a⊑b ⇒ f(u,v)(a)⊑f(u,v)(b).

**formalStatement:** For every (u,v)∈E, a⊑b ⇒ f(u,v)(a)⊑f(u,v)(b).

**assumptions:** V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-MonotoneDataflow-equations"></a>

### equations

`urn:csabs:axiom/MonotoneDataflow-equations`

**description:** Defining rule for Monotone dataflow framework (forward join profile)

**statement:** F(x)(v)=b(v)⊔⋁{f(u,v)(x(u)) | (u,v)∈E}; a solution satisfies F(x)=x.

**formalStatement:** F(x)(v)=b(v)⊔⋁{f(u,v)(x(u)) | (u,v)∈E}; a solution satisfies F(x)=x.

**assumptions:** V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-MonotoneDataflow-least-solution"></a>

### least-solution

`urn:csabs:law/MonotoneDataflow-least-solution`

**description:** F has a unique least fixed point, also the least x satisfying F(x)⊑x.

**statement:** F has a unique least fixed point, also the least x satisfying F(x)⊑x.

**formalStatement:** F has a unique least fixed point, also the least x satisfying F(x)⊑x.

**assumptions:** V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.

**dependsOn:** [fact-lattice](MonotoneDataflow.md#node-urn-csabs-axiom-MonotoneDataflow-fact-lattice); [transfer-monotonicity](MonotoneDataflow.md#node-urn-csabs-axiom-MonotoneDataflow-transfer-monotonicity); [equations](MonotoneDataflow.md#node-urn-csabs-axiom-MonotoneDataflow-equations)

**proofSketch:** Monotonicity of each transfer and of suprema makes F monotone. Let P={x | F(x)⊑x} and m=inf P. For each p∈P, F(m)⊑F(p)⊑p, so F(m)⊑m. Then F(F(m))⊑F(m), so F(m)∈P and m⊑F(m). Antisymmetry gives equality, and m is below every pre-fixed point.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Anders Møller and Michael I. Schwartzbach: Static Program Analysis (15 October 2026)](https://cs.au.dk/~amoeller/spa/spa.pdf); accessedOn: 2026-11-17; sourceRole: consulted-author-textbook

**sourceLocator:** §4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/MonotoneDataflow",
    "type": "Concept",
    "shortForm": "MonotoneDataflow",
    "fullName": "Monotone dataflow framework (forward join profile)",
    "definition": "A finite dependency graph with complete-lattice facts, boundary facts and monotone edge transfer functions, interpreted as a system of dataflow equations.",
    "notation": "F(x)(v)=b(v) ⊔ ⋁{f(u,v)(x(u)) | E(u,v)}; x*=lfp(F).",
    "category": [
      "urn:csabs:category/compiler-transformations",
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.",
    "axiomBasis": "Complete fact lattice, pointwise product, total monotone edge transfers and explicit boundary-join equations.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "F(x)(v)=b(v) ⊔ ⋁{f(u,v)(x(u)) | E(u,v)}; x*=lfp(F). V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption.",
    "requiresConcept": [
      "urn:csabs:concept/CompleteLattice",
      "urn:csabs:concept/MonotoneFunction"
    ],
    "relatedConcept": [
      "urn:csabs:concept/AbstractInterpretation",
      "urn:csabs:concept/ControlFlowGraph",
      "urn:csabs:concept/IntervalDomain",
      "urn:csabs:concept/FixedPoint"
    ],
    "hasOperation": [
      "urn:csabs:operation/MonotoneDataflow-transfer",
      "urn:csabs:operation/MonotoneDataflow-step",
      "urn:csabs:operation/MonotoneDataflow-least-solution"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/MonotoneDataflow-fact-lattice",
      "urn:csabs:axiom/MonotoneDataflow-transfer-monotonicity",
      "urn:csabs:axiom/MonotoneDataflow-equations"
    ],
    "hasLaw": [
      "urn:csabs:law/MonotoneDataflow-least-solution"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure MonotoneDataflow (V : Type u) (L : Type v) [Fintype V] [CompleteLattice L] where\n  edge : V → V → Prop\n  boundary : V → L\n  transfer : V → V → L → L\n  monotone : ∀ u v, edge u v → Monotone (transfer u v)",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.MonotoneDataflow",
    "formulationScope": "partial",
    "leanModelMapping": "Finite graph, complete lattice, boundary facts and edge-qualified monotone transfers. The step declaration uses suprema for the forward join equations.",
    "leanModelLimitations": "No concretization soundness proof, solver, convergence proof or registered least-solution witness."
  },
  {
    "id": "urn:csabs:operation/MonotoneDataflow-transfer",
    "type": "Operation",
    "name": "transfer",
    "signature": "f : E → (L → L)",
    "description": "Apply the selected monotone edge transfer; node transfers can be assigned to all outgoing edges.",
    "concept": "urn:csabs:concept/MonotoneDataflow",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Apply the selected monotone edge transfer; node transfers can be assigned to all outgoing edges.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MonotoneDataflow-step",
    "type": "Operation",
    "name": "step",
    "signature": "F : (V→L) → (V→L)",
    "description": "Evaluate all displayed equations simultaneously, preserving boundary contributions.",
    "concept": "urn:csabs:concept/MonotoneDataflow",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Evaluate all displayed equations simultaneously, preserving boundary contributions.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/MonotoneDataflow-least-solution",
    "type": "Operation",
    "name": "least-solution",
    "signature": "solve : Framework → (V→L)",
    "description": "Return the mathematical least fixed point of F; no finite-time algorithm is implied.",
    "concept": "urn:csabs:concept/MonotoneDataflow",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return the mathematical least fixed point of F; no finite-time algorithm is implied.",
    "totality": "Total mathematical operator, not a promised terminating implementation.",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MonotoneDataflow-fact-lattice",
    "type": "Axiom",
    "name": "fact-lattice",
    "description": "Defining rule for Monotone dataflow framework (forward join profile)",
    "statement": "L is a complete lattice; V→L has pointwise order and pointwise arbitrary suprema and infima.",
    "formalStatement": "L is a complete lattice; V→L has pointwise order and pointwise arbitrary suprema and infima.",
    "assumptions": [
      "V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption."
    ],
    "appliesTo": [
      "urn:csabs:concept/MonotoneDataflow"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MonotoneDataflow-transfer-monotonicity",
    "type": "Axiom",
    "name": "transfer-monotonicity",
    "description": "Defining rule for Monotone dataflow framework (forward join profile)",
    "statement": "For every (u,v)∈E, a⊑b ⇒ f(u,v)(a)⊑f(u,v)(b).",
    "formalStatement": "For every (u,v)∈E, a⊑b ⇒ f(u,v)(a)⊑f(u,v)(b).",
    "assumptions": [
      "V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption."
    ],
    "appliesTo": [
      "urn:csabs:concept/MonotoneDataflow"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/MonotoneDataflow-equations",
    "type": "Axiom",
    "name": "equations",
    "description": "Defining rule for Monotone dataflow framework (forward join profile)",
    "statement": "F(x)(v)=b(v)⊔⋁{f(u,v)(x(u)) | (u,v)∈E}; a solution satisfies F(x)=x.",
    "formalStatement": "F(x)(v)=b(v)⊔⋁{f(u,v)(x(u)) | (u,v)∈E}; a solution satisfies F(x)=x.",
    "assumptions": [
      "V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption."
    ],
    "appliesTo": [
      "urn:csabs:concept/MonotoneDataflow"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/MonotoneDataflow-least-solution",
    "type": "Law",
    "name": "least-solution",
    "description": "F has a unique least fixed point, also the least x satisfying F(x)⊑x.",
    "statement": "F has a unique least fixed point, also the least x satisfying F(x)⊑x.",
    "formalStatement": "F has a unique least fixed point, also the least x satisfying F(x)⊑x.",
    "assumptions": [
      "V finite (possibly empty); L a complete lattice ordered by increasing information allowance, equality the lattice carrier equality. b:V→L and every edge transfer f(u,v):L→L is total and monotone. Facts x:V→L have pointwise order. Empty predecessor join is ⊥. The generic equations need not be semantically sound without a concretization proof. Finite convergence requires finite height or another convergence condition; widening may yield a nonleast inductive result. Must analyses use an explicit dual order; backward analyses reverse dependencies. No distributivity or MOP=MFP assumption."
    ],
    "appliesTo": [
      "urn:csabs:concept/MonotoneDataflow"
    ],
    "dependsOn": [
      "urn:csabs:axiom/MonotoneDataflow-fact-lattice",
      "urn:csabs:axiom/MonotoneDataflow-transfer-monotonicity",
      "urn:csabs:axiom/MonotoneDataflow-equations"
    ],
    "proofSketch": "Monotonicity of each transfer and of suprema makes F monotone. Let P={x | F(x)⊑x} and m=inf P. For each p∈P, F(m)⊑F(p)⊑p, so F(m)⊑m. Then F(F(m))⊑F(m), so F(m)∈P and m⊑F(m). Antisymmetry gives equality, and m is below every pre-fixed point.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/moller-schwartzbach-spa-2026"
    ],
    "sourceLocator": "§4.4, Chapter 5 introductory definition, §§5.3,5.8,6.1; least-solution theorem on pp.81–82.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
