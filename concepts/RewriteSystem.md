# Abstract rewrite system

A carrier equipped with an arbitrary one-step reduction relation and its finite reflexive transitive closure.

**Notation:** (A,→); →* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b.

**Stable ID:** `urn:csabs:concept/RewriteSystem`

**Categories:** Programming-language semantics, Logic and proof

**Kind:** Mathematical structure

**Prerequisites:** [Binary relation](Relation.md)

**Specializes:** [Binary relation](Relation.md)

**Related concepts:** [Guarded contextual program rewrite](GuardedRewrite.md), [Free ranked term algebra with variables](TermAlgebra.md), [Termination Variant](TerminationVariant.md)

## Backlinks

- [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md) — `relatedConcept`
- [Guarded contextual program rewrite](GuardedRewrite.md) — `relatedConcept`

## Mathematical formulation

(A,→); →\* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b. A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.

**Lean formulation** (in its source module context):

```lean
structure RewriteSystem (A : Type u) where
  step : A → A → Prop
```

**Source:** [`Catalog.Programs.RewriteSystem`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** partial

**Interpretation:** Arbitrary step relation on A; reduces is Relation.ReflTransGen and normalForm excludes step successors.

**Limits:** No matching engine, term substitution/context closure, strategy, termination, confluence or refinement proof.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Arbitrary typed step relation; inductively generated finite closure; absence-of-successor normal-form definition.

**basisKind:** extensional-structural-definition

**basisScope:** A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.

**specializationNote:** Retain A and its binary step relation as Relation on A; the closure and normal-form predicates are defined from that relation.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-RewriteSystem-step"></a>

### step

`urn:csabs:operation/RewriteSystem-step`

**signature:** step : A → P(A)

**description:** step(a)={b | a→b}; the empty result means no reduction.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** step(a)={b | a→b}; the empty result means no reduction.

**totality:** Total set-valued relation; no computability requirement.

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RewriteSystem-reduces"></a>

### reduces

`urn:csabs:operation/RewriteSystem-reduces`

**signature:** reduces : A×A → Prop

**description:** reduces(a,b) iff a→*b by a finite sequence, possibly empty.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** reduces(a,b) iff a→*b by a finite sequence, possibly empty.

**totality:** Total on the displayed typed domain.

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RewriteSystem-normal-form"></a>

### normal-form

`urn:csabs:operation/RewriteSystem-normal-form`

**signature:** NF : A → Prop

**description:** NF(a) iff a has no one-step successor; normal forms need not coincide with semantic values.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** NF(a) iff a has no one-step successor; normal forms need not coincide with semantic values.

**totality:** Total on the displayed typed domain.

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-RewriteSystem-closure"></a>

### closure

`urn:csabs:axiom/RewriteSystem-closure`

**description:** Defining rule for Abstract rewrite system

**statement:** →* is the least relation with a→*a and (a→b ∧ b→*c ⇒ a→*c).

**formalStatement:** →* is the least relation with a→*a and (a→b ∧ b→*c ⇒ a→*c).

**assumptions:** A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-RewriteSystem-normal-forms"></a>

### normal-forms

`urn:csabs:axiom/RewriteSystem-normal-forms`

**description:** Defining rule for Abstract rewrite system

**statement:** NF(a) ⇔ ¬∃b∈A, a→b.

**formalStatement:** NF(a) ⇔ ¬∃b∈A, a→b.

**assumptions:** A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-RewriteSystem-closure-transitive"></a>

### closure-transitive

`urn:csabs:law/RewriteSystem-closure-transitive`

**description:** a→*b ∧ b→*c ⇒ a→*c.

**statement:** a→*b ∧ b→*c ⇒ a→*c.

**formalStatement:** a→*b ∧ b→*c ⇒ a→*c.

**assumptions:** A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.

**dependsOn:** [closure](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-closure)

**proofSketch:** Induct on the first finite derivation; the reflexive case uses the second derivation, and a leading step is prepended to the induction result.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Software Foundations, Programming Language Foundations: Smallstep](https://softwarefoundations.cis.upenn.edu/plf-current/Smallstep.html); accessedOn: 2026-11-17; sourceRole: consulted-author-formalization

**sourceLocator:** Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/RewriteSystem",
    "type": "Concept",
    "shortForm": "RewriteSystem",
    "fullName": "Abstract rewrite system",
    "definition": "A carrier equipped with an arbitrary one-step reduction relation and its finite reflexive transitive closure.",
    "notation": "(A,→); →* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b.",
    "category": [
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/logic"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.",
    "axiomBasis": "Arbitrary typed step relation; inductively generated finite closure; absence-of-successor normal-form definition.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "(A,→); →* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b. A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties.",
    "requiresConcept": [
      "urn:csabs:concept/Relation"
    ],
    "relatedConcept": [
      "urn:csabs:concept/GuardedRewrite",
      "urn:csabs:concept/TermAlgebra",
      "urn:csabs:concept/TerminationVariant"
    ],
    "hasOperation": [
      "urn:csabs:operation/RewriteSystem-step",
      "urn:csabs:operation/RewriteSystem-reduces",
      "urn:csabs:operation/RewriteSystem-normal-form"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RewriteSystem-closure",
      "urn:csabs:axiom/RewriteSystem-normal-forms"
    ],
    "hasLaw": [
      "urn:csabs:law/RewriteSystem-closure-transitive"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Relation"
    ],
    "specializationNote": "Retain A and its binary step relation as Relation on A; the closure and normal-form predicates are defined from that relation.",
    "leanFormulation": "structure RewriteSystem (A : Type u) where\n  step : A → A → Prop",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.RewriteSystem",
    "formulationScope": "partial",
    "leanModelMapping": "Arbitrary step relation on A; reduces is Relation.ReflTransGen and normalForm excludes step successors.",
    "leanModelLimitations": "No matching engine, term substitution/context closure, strategy, termination, confluence or refinement proof."
  },
  {
    "id": "urn:csabs:operation/RewriteSystem-step",
    "type": "Operation",
    "name": "step",
    "signature": "step : A → P(A)",
    "description": "step(a)={b | a→b}; the empty result means no reduction.",
    "concept": "urn:csabs:concept/RewriteSystem",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "step(a)={b | a→b}; the empty result means no reduction.",
    "totality": "Total set-valued relation; no computability requirement.",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RewriteSystem-reduces",
    "type": "Operation",
    "name": "reduces",
    "signature": "reduces : A×A → Prop",
    "description": "reduces(a,b) iff a→*b by a finite sequence, possibly empty.",
    "concept": "urn:csabs:concept/RewriteSystem",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "reduces(a,b) iff a→*b by a finite sequence, possibly empty.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RewriteSystem-normal-form",
    "type": "Operation",
    "name": "normal-form",
    "signature": "NF : A → Prop",
    "description": "NF(a) iff a has no one-step successor; normal forms need not coincide with semantic values.",
    "concept": "urn:csabs:concept/RewriteSystem",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "NF(a) iff a has no one-step successor; normal forms need not coincide with semantic values.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RewriteSystem-closure",
    "type": "Axiom",
    "name": "closure",
    "description": "Defining rule for Abstract rewrite system",
    "statement": "→* is the least relation with a→*a and (a→b ∧ b→*c ⇒ a→*c).",
    "formalStatement": "→* is the least relation with a→*a and (a→b ∧ b→*c ⇒ a→*c).",
    "assumptions": [
      "A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/RewriteSystem-normal-forms",
    "type": "Axiom",
    "name": "normal-forms",
    "description": "Defining rule for Abstract rewrite system",
    "statement": "NF(a) ⇔ ¬∃b∈A, a→b.",
    "formalStatement": "NF(a) ⇔ ¬∃b∈A, a→b.",
    "assumptions": [
      "A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/RewriteSystem-closure-transitive",
    "type": "Law",
    "name": "closure-transitive",
    "description": "a→*b ∧ b→*c ⇒ a→*c.",
    "statement": "a→*b ∧ b→*c ⇒ a→*c.",
    "formalStatement": "a→*b ∧ b→*c ⇒ a→*c.",
    "assumptions": [
      "A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-closure"
    ],
    "proofSketch": "Induct on the first finite derivation; the reflexive case uses the second derivation, and a leading step is prepended to the induction result.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/sf-smallstep-2026"
    ],
    "sourceLocator": "Smallstep: Normal Forms and Multi-Step Reduction (multi, multi_R, multi_trans).",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
