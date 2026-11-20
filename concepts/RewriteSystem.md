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

(A,→); →\* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b. A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties. Utility profile: For every a→\*b and a→\*c there exists d with b→\*d and c→\*d; global confluence, not merely local one-step confluence.; The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.

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

**axiomBasis:** Arbitrary typed step relation; inductively generated finite closure; absence-of-successor normal-form definition. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.

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

<a id="node-urn-csabs-operation-RewriteSystem-confluence"></a>

### confluence

`urn:csabs:operation/RewriteSystem-confluence`

**signature:** confluent : RewriteSystem(A)→Prop

**description:** For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RewriteSystem-termination"></a>

### termination

`urn:csabs:operation/RewriteSystem-termination`

**signature:** terminating : RewriteSystem(A)→Prop

**description:** The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-RewriteSystem-unique-normal-form"></a>

### unique-normal-form

`urn:csabs:operation/RewriteSystem-unique-normal-form`

**signature:** normalFormOf : ConvergentRewriteSystem(A)×A→A

**description:** With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.

**precondition:** Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.

**postcondition:** With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.

**totality:** Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-axiom-RewriteSystem-utility-profile"></a>

### Explicit utility operation definitions

`urn:csabs:axiom/RewriteSystem-utility-profile`

**statement:** For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.; The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.

**formalStatement:** confluent : RewriteSystem(A)→Prop: For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.; terminating : RewriteSystem(A)→Prop: The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; normalFormOf : ConvergentRewriteSystem(A)×A→A: With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.

**assumptions:** Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics.

**ruleRole:** defining-rule

**reviewStatus:** Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments

**sourceNote:** Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.

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

<a id="node-urn-csabs-theorem-RewriteSystem-normal-form-closure-equality"></a>

### normal-form-closure-equality

`urn:csabs:theorem/RewriteSystem-normal-form-closure-equality`

**statement:** If a is a normal form and a→*b then a=b.

**formalStatement:** If a is a normal form and a→*b then a=b.

**proofSketch:** A nonempty path would have a first outgoing step, contradicting normality.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-utility-profile); [closure](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-closure); [normal-forms](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-normal-forms)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.normalForm_reduces_eq

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

If a is a normal form and a→\*b then a=b.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A) (a b : A)
    (_ha : r.normalForm a) (_hab : r.reduces a b), a = b
```

**Source:** [`Catalog.Programs.normalForm_reduces_eq`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** If a is a normal form and a→*b then a=b. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-closure": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RewriteSystem-normal-forms": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RewriteSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-confluent-normal-form-uniqueness"></a>

### confluent-normal-form-uniqueness

`urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness`

**statement:** Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.

**formalStatement:** Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.

**proofSketch:** Join the two reducts by confluence; a normal form reduces only to itself.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-utility-profile); [normal-form-closure-equality](RewriteSystem.md#node-urn-csabs-theorem-RewriteSystem-normal-form-closure-equality)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.confluent_unique_normalForm

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)
    (_hc : Catalog.Programs.confluent r) (a b c : A) (_hab : r.reduces a b) (_hac : r.reduces a c)
    (_hb : r.normalForm b) (_hc' : r.normalForm c), b = c
```

**Source:** [`Catalog.Programs.confluent_unique_normalForm`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/RewriteSystem-normal-form-closure-equality": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-termination-normal-form-existence"></a>

### termination-normal-form-existence

`urn:csabs:theorem/RewriteSystem-termination-normal-form-existence`

**statement:** Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.

**formalStatement:** Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.

**proofSketch:** Well-founded induction: stop if normal; otherwise take one step and prepend it to the inductively obtained path.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-utility-profile); [closure](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-closure); [normal-forms](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-normal-forms)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.terminating_normalForm

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)
    (_ht : Catalog.Programs.terminating r) (a : A), ∃ b, r.reduces a b ∧ r.normalForm b
```

**Source:** [`Catalog.Programs.terminating_normalForm`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Termination implies every term has a reachable normal form. Confluence is not needed for existence alone. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-closure": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RewriteSystem-normal-forms": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:axiom/RewriteSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-convergent-unique-normal-form"></a>

### convergent-unique-normal-form

`urn:csabs:theorem/RewriteSystem-convergent-unique-normal-form`

**statement:** Termination plus confluence implies every term has exactly one reachable normal form.

**formalStatement:** Termination plus confluence implies every term has exactly one reachable normal form.

**proofSketch:** Combine existence from termination with uniqueness from confluence.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-utility-profile); [termination-normal-form-existence](RewriteSystem.md#node-urn-csabs-theorem-RewriteSystem-termination-normal-form-existence); [confluent-normal-form-uniqueness](RewriteSystem.md#node-urn-csabs-theorem-RewriteSystem-confluent-normal-form-uniqueness)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.convergent_unique_normalForm

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

Termination plus confluence implies every term has exactly one reachable normal form.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)
    (_ht : Catalog.Programs.terminating r) (_hc : Catalog.Programs.confluent r) (a : A), ∃! b, r.reduces a b ∧ r.normalForm b
```

**Source:** [`Catalog.Programs.convergent_unique_normalForm`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Termination plus confluence implies every term has exactly one reachable normal form. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.",
  "urn:csabs:theorem/RewriteSystem-termination-normal-form-existence": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-convergent-model-satisfaction"></a>

### convergent-model-satisfaction

`urn:csabs:theorem/RewriteSystem-convergent-model-satisfaction`

**statement:** The empty-step rewrite system on any carrier is terminating and confluent.

**formalStatement:** The empty-step rewrite system on any carrier is terminating and confluent.

**proofSketch:** Every state is accessible without predecessors; the only closure paths are identities. This model is nonvacuously inhabited whenever its carrier is inhabited.

**assumptions:** Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles.

**dependsOn:** [Explicit utility operation definitions](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-utility-profile)

**reviewStatus:** Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.

**source:** [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.; Catalog ReachabilityUtilities Lean formulations and proofs; path: lean/Catalog/ReachabilityUtilities.lean; accessedOn: 2026-11-20; sourceRole: Local formulation and derived-proof evidence. Independent mathematical provenance is linked separately.

**sourceLocator:** Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.rewrite_model

**sourceNote:** Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.

**provenanceKind:** derived

#### Mathematical formulation

The empty-step rewrite system on any carrier is terminating and confluent.

**Lean formulation** (in its source module context):

```lean
∀ (A : Type u), Catalog.Programs.terminating (Catalog.Programs.emptyRewrite A) ∧ Catalog.Programs.confluent (Catalog.Programs.emptyRewrite A)
```

**Source:** [`Catalog.Programs.rewrite_model`](../lean/Catalog/ReachabilityUtilities.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** The empty-step rewrite system on any carrier is terminating and confluent. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.

**Limits:** Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-utility-profile": "Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-singleton-replace-all-idempotence"></a>

### singleton-replace-all-idempotence

`urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence`

**statement:** For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.

**formalStatement:** For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.

**assumptions:** Exactly the displayed Lean binders and the explicit profile definitions.

**dependsOn:** [closure](RewriteSystem.md#node-urn-csabs-axiom-RewriteSystem-closure)

**source:** Constructed information, prefix, replacement and endpoint-set models over pinned Mathlib; citation: Constructed models; primitives consulted in pinned Mathlib Data/Finset/Sort.lean length_sort, Data/List/TakeDrop.lean take_of_length_le, list map composition and Set membership. Independent mathematical primitive provenance: utility-mathlib-pinned.; path: lean/Catalog/ExtensionProfiles.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-derived-proof; [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Catalog.replaceSymbol_idempotent; pinned Mathlib finite-list, finite-set and relation primitives

**sourceNote:** Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.

**provenanceKind:** derived

**proofSketch:** Use the concrete definitions and the compiled proof in the cited local module.

**reviewStatus:** Selected model proof; verification requires fresh compiler and axiom audit.

#### Mathematical formulation

For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (a b : A) (xs : List A), Catalog.replaceSymbol a b (Catalog.replaceSymbol a b xs) = Catalog.replaceSymbol a b xs
```

**Source:** [`Catalog.replaceSymbol_idempotent`](../lean/Catalog/ExtensionProfiles.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed. Exact equality and typed carriers are those displayed in the Lean proposition.

**Limits:** Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/RewriteSystem-closure": "Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-singleton-replace-all-correspondence"></a>

### singleton-replace-all-correspondence

`urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence`

**statement:** Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.

**formalStatement:** Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.

**assumptions:** Exactly the displayed Lean binders and the explicit profile definitions.

**dependsOn:** [leftmost non-overlapping replace all](Sequence.md#node-urn-csabs-operation-Sequence-edit-replace-all)

**source:** Constructed information, prefix, replacement and endpoint-set models over pinned Mathlib; citation: Constructed models; primitives consulted in pinned Mathlib Data/Finset/Sort.lean length_sort, Data/List/TakeDrop.lean take_of_length_le, list map composition and Set membership. Independent mathematical primitive provenance: utility-mathlib-pinned.; path: lean/Catalog/ExtensionProfiles.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-derived-proof; [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Catalog.replaceSymbol_eq_replaceAll; pinned Mathlib finite-list, finite-set and relation primitives

**sourceNote:** Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.

**provenanceKind:** derived

**proofSketch:** Use the concrete definitions and the compiled proof in the cited local module.

**reviewStatus:** Selected model proof; verification requires fresh compiler and axiom audit.

#### Mathematical formulation

Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (a b : A) (xs : List A), Catalog.replaceSymbol a b xs = Catalog.replaceAll [a] (by simp) [b] xs
```

**Source:** [`Catalog.replaceSymbol_eq_replaceAll`](../lean/Catalog/ExtensionProfiles.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list. Exact equality and typed carriers are those displayed in the Lean proposition.

**Limits:** Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:operation/Sequence-edit-replace-all": "Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed."
}
```

<a id="node-urn-csabs-theorem-RewriteSystem-singleton-replace-all-confluence"></a>

### singleton-replace-all-confluence

`urn:csabs:theorem/RewriteSystem-singleton-replace-all-confluence`

**statement:** Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.

**formalStatement:** Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.

**assumptions:** Exactly the displayed Lean binders and the explicit profile definitions.

**dependsOn:** [singleton-replace-all-idempotence](RewriteSystem.md#node-urn-csabs-theorem-RewriteSystem-singleton-replace-all-idempotence); [singleton-replace-all-correspondence](RewriteSystem.md#node-urn-csabs-theorem-RewriteSystem-singleton-replace-all-correspondence)

**source:** Constructed information, prefix, replacement and endpoint-set models over pinned Mathlib; citation: Constructed models; primitives consulted in pinned Mathlib Data/Finset/Sort.lean length_sort, Data/List/TakeDrop.lean take_of_length_le, list map composition and Set membership. Independent mathematical primitive provenance: utility-mathlib-pinned.; path: lean/Catalog/ExtensionProfiles.lean; accessedOn: 2026-11-20; sourceRole: local-lean-formulation-and-derived-proof; [Mathlib finite collection, relation, order and graph sources, pinned revision 56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib); path: lean/.lake/packages/mathlib/Mathlib; accessedOn: 2026-11-20; sourceRole: Consulted primary library definitions and proofs for the primitive operations and constructed utility profiles.

**sourceLocator:** Catalog.symbolRewrite_confluent; pinned Mathlib finite-list, finite-set and relation primitives

**sourceNote:** Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.

**provenanceKind:** derived

**proofSketch:** Use the concrete definitions and the compiled proof in the cited local module.

**reviewStatus:** Selected model proof; verification requires fresh compiler and axiom audit.

#### Mathematical formulation

Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.

**Lean formulation** (in its source module context):

```lean
∀ {A : Type u} [DecidableEq A] (a b : A), Catalog.Programs.confluent (Catalog.symbolRewrite a b)
```

**Source:** [`Catalog.symbolRewrite_confluent`](../lean/Catalog/ExtensionProfiles.lean); consulted 2026-11-20.

**Scope:** registered-witness-type

**Interpretation:** Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting. Exact equality and typed carriers are those displayed in the Lean proposition.

**Limits:** Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence": "Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.",
  "urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence": "Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed."
}
```

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
    "axiomBasis": "Arbitrary typed step relation; inductively generated finite closure; absence-of-successor normal-form definition. Utility definitions are recorded separately; optional bottom, subtype and goal-relative conventions are conditional and do not strengthen the base carrier.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "(A,→); →* = finite reflexive transitive closure of →; NF(a) ⇔ ¬∃b,a→b. A may be empty; equality is carrier equality. One-step reduction may be nondeterministic, cyclic, nonterminating or infinitely branching; no effective decision procedure is assumed. This is abstract rewriting; substitution/context closure for term rewriting is an additional instantiation on TermAlgebra. Termination, confluence, semantic refinement and a normalization strategy are independent properties. Utility profile: For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.; The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.",
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
      "urn:csabs:operation/RewriteSystem-normal-form",
      "urn:csabs:operation/RewriteSystem-confluence",
      "urn:csabs:operation/RewriteSystem-termination",
      "urn:csabs:operation/RewriteSystem-unique-normal-form"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/RewriteSystem-closure",
      "urn:csabs:axiom/RewriteSystem-normal-forms",
      "urn:csabs:axiom/RewriteSystem-utility-profile"
    ],
    "hasLaw": [
      "urn:csabs:law/RewriteSystem-closure-transitive"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/RewriteSystem-normal-form-closure-equality",
      "urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness",
      "urn:csabs:theorem/RewriteSystem-termination-normal-form-existence",
      "urn:csabs:theorem/RewriteSystem-convergent-unique-normal-form",
      "urn:csabs:theorem/RewriteSystem-convergent-model-satisfaction",
      "urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence",
      "urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence",
      "urn:csabs:theorem/RewriteSystem-singleton-replace-all-confluence"
    ],
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
    "id": "urn:csabs:operation/RewriteSystem-confluence",
    "type": "Operation",
    "concept": "urn:csabs:concept/RewriteSystem",
    "name": "confluence",
    "signature": "confluent : RewriteSystem(A)→Prop",
    "description": "For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RewriteSystem-termination",
    "type": "Operation",
    "concept": "urn:csabs:concept/RewriteSystem",
    "name": "termination",
    "signature": "terminating : RewriteSystem(A)→Prop",
    "description": "The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/RewriteSystem-unique-normal-form",
    "type": "Operation",
    "concept": "urn:csabs:concept/RewriteSystem",
    "name": "unique-normal-form",
    "signature": "normalFormOf : ConvergentRewriteSystem(A)×A→A",
    "description": "With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.",
    "precondition": "Stated carrier and optional-profile assumptions; executable equality/predicates require decision procedures.",
    "postcondition": "With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.",
    "totality": "Mathematical totality on the stated domain; no runtime resource or floating-point guarantee.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
    "id": "urn:csabs:axiom/RewriteSystem-utility-profile",
    "type": "Axiom",
    "name": "Explicit utility operation definitions",
    "statement": "For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.; The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.",
    "formalStatement": "confluent : RewriteSystem(A)→Prop: For every a→*b and a→*c there exists d with b→*d and c→*d; global confluence, not merely local one-step confluence.; terminating : RewriteSystem(A)→Prop: The converse step relation is well-founded, excluding infinite forward reduction chains in the classical model; no fixed global step bound is asserted.; normalFormOf : ConvergentRewriteSystem(A)×A→A: With both termination and confluence, choose the unique reachable normal form; no effective reduction strategy or complexity bound is asserted.",
    "assumptions": [
      "Base concept conventions remain unchanged. Optional profiles apply only under their explicitly stated additional hypotheses; identity equality, finite inputs and exact mathematics."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Definitions of a selected extension, not new foundational axioms; individual model and result witnesses are separate.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments",
    "sourceNote": "Adapts consulted primitives to this explicitly defined mathematical profile; no claim that the source states the entire constructed composition.",
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
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-normal-form-closure-equality",
    "type": "Theorem",
    "name": "normal-form-closure-equality",
    "statement": "If a is a normal form and a→*b then a=b.",
    "formalStatement": "If a is a normal form and a→*b then a=b.",
    "mathematicalFormulation": "If a is a normal form and a→*b then a=b.",
    "proofSketch": "A nonempty path would have a first outgoing step, contradicting normality.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-utility-profile",
      "urn:csabs:axiom/RewriteSystem-closure",
      "urn:csabs:axiom/RewriteSystem-normal-forms"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.normalForm_reduces_eq",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A) (a b : A)\n    (_ha : r.normalForm a) (_hab : r.reduces a b), a = b",
    "leanModelMapping": "If a is a normal form and a→*b then a=b. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-closure\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RewriteSystem-normal-forms\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RewriteSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.normalForm_reduces_eq"
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness",
    "type": "Theorem",
    "name": "confluent-normal-form-uniqueness",
    "statement": "Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.",
    "formalStatement": "Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.",
    "mathematicalFormulation": "Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone.",
    "proofSketch": "Join the two reducts by confluence; a normal form reduces only to itself.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-utility-profile",
      "urn:csabs:theorem/RewriteSystem-normal-form-closure-equality"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.confluent_unique_normalForm",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)\n    (_hc : Catalog.Programs.confluent r) (a b c : A) (_hab : r.reduces a b) (_hac : r.reduces a c)\n    (_hb : r.normalForm b) (_hc' : r.normalForm c), b = c",
    "leanModelMapping": "Confluence implies any two reachable normal forms from the same term are equal. Termination is not needed for uniqueness alone. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/RewriteSystem-normal-form-closure-equality\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.confluent_unique_normalForm"
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-termination-normal-form-existence",
    "type": "Theorem",
    "name": "termination-normal-form-existence",
    "statement": "Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.",
    "formalStatement": "Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.",
    "mathematicalFormulation": "Termination implies every term has a reachable normal form. Confluence is not needed for existence alone.",
    "proofSketch": "Well-founded induction: stop if normal; otherwise take one step and prepend it to the inductively obtained path.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-utility-profile",
      "urn:csabs:axiom/RewriteSystem-closure",
      "urn:csabs:axiom/RewriteSystem-normal-forms"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.terminating_normalForm",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)\n    (_ht : Catalog.Programs.terminating r) (a : A), ∃ b, r.reduces a b ∧ r.normalForm b",
    "leanModelMapping": "Termination implies every term has a reachable normal form. Confluence is not needed for existence alone. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-closure\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RewriteSystem-normal-forms\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:axiom/RewriteSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.terminating_normalForm"
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-convergent-unique-normal-form",
    "type": "Theorem",
    "name": "convergent-unique-normal-form",
    "statement": "Termination plus confluence implies every term has exactly one reachable normal form.",
    "formalStatement": "Termination plus confluence implies every term has exactly one reachable normal form.",
    "mathematicalFormulation": "Termination plus confluence implies every term has exactly one reachable normal form.",
    "proofSketch": "Combine existence from termination with uniqueness from confluence.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-utility-profile",
      "urn:csabs:theorem/RewriteSystem-termination-normal-form-existence",
      "urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.convergent_unique_normalForm",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type u} (r : Catalog.Programs.RewriteSystem A)\n    (_ht : Catalog.Programs.terminating r) (_hc : Catalog.Programs.confluent r) (a : A), ∃! b, r.reduces a b ∧ r.normalForm b",
    "leanModelMapping": "Termination plus confluence implies every term has exactly one reachable normal form. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/RewriteSystem-confluent-normal-form-uniqueness\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\", \"urn:csabs:theorem/RewriteSystem-termination-normal-form-existence\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.convergent_unique_normalForm"
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-convergent-model-satisfaction",
    "type": "Theorem",
    "name": "convergent-model-satisfaction",
    "statement": "The empty-step rewrite system on any carrier is terminating and confluent.",
    "formalStatement": "The empty-step rewrite system on any carrier is terminating and confluent.",
    "mathematicalFormulation": "The empty-step rewrite system on any carrier is terminating and confluent.",
    "proofSketch": "Every state is accessible without predecessors; the only closure paths are identities. This model is nonvacuously inhabited whenever its carrier is inhabited.",
    "assumptions": [
      "Exactly the carrier, equality and explicit hypotheses in leanFormulation; see the base and utility profiles."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-utility-profile"
    ],
    "reviewStatus": "Compiled local proof and axiom audit; catalog verification status requires a fresh verification report.",
    "source": [
      "urn:csabs:source/utility-mathlib-pinned",
      "urn:csabs:source/utility-lean-ReachabilityUtilities"
    ],
    "sourceLocator": "Logic/Relation.lean: ReflTransGen, Join, church_rosser; well-founded induction; constructed existence and uniqueness arguments; Catalog.Programs.rewrite_model",
    "sourceNote": "Derived from the explicit linked premises using the separately recorded Lean proof; primitives are adapted to the displayed carriers and conventions.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ (A : Type u), Catalog.Programs.terminating (Catalog.Programs.emptyRewrite A) ∧ Catalog.Programs.confluent (Catalog.Programs.emptyRewrite A)",
    "leanModelMapping": "The empty-step rewrite system on any carrier is terminating and confluent. Carrier/equality mapping is exactly the typed Lean binders; operations are the named concrete definitions in the formulation module. Defining equations and structural consequences are proved, not postulated.",
    "leanModelLimitations": "Proves the displayed proposition in the selected exact mathematical model. Optional hypotheses remain explicit. No software refinement, tokenizer correctness, floating-point equivalence or blanket proof coverage.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-utility-profile\": \"Defining premise interpreted by the named concrete operations and typed structural assumptions; the displayed theorem proves the stated consequence under exactly its binders.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/utility-lean-ReachabilityUtilities",
    "formulationLocator": "Catalog.Programs.rewrite_model"
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence",
    "type": "Theorem",
    "name": "singleton-replace-all-idempotence",
    "statement": "For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.",
    "formalStatement": "For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.",
    "mathematicalFormulation": "For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed.",
    "assumptions": [
      "Exactly the displayed Lean binders and the explicit profile definitions."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:axiom/RewriteSystem-closure"
    ],
    "source": [
      "urn:csabs:source/extension-profiles-2026-11-20",
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Catalog.replaceSymbol_idempotent; pinned Mathlib finite-list, finite-set and relation primitives",
    "sourceNote": "Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.",
    "provenanceKind": "derived",
    "proofSketch": "Use the concrete definitions and the compiled proof in the cited local module.",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (a b : A) (xs : List A), Catalog.replaceSymbol a b (Catalog.replaceSymbol a b xs) = Catalog.replaceSymbol a b xs",
    "leanModelMapping": "For singleton pattern [a] and singleton replacement [b], the leftmost replace-all map R is idempotent: R(R(xs))=R(xs), including a=b. No arbitrary-pattern idempotence is claimed. Exact equality and typed carriers are those displayed in the Lean proposition.",
    "leanModelLimitations": "Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/RewriteSystem-closure\": \"Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/extension-profiles-2026-11-20",
    "formulationLocator": "Catalog.replaceSymbol_idempotent",
    "reviewStatus": "Selected model proof; verification requires fresh compiler and axiom audit."
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence",
    "type": "Theorem",
    "name": "singleton-replace-all-correspondence",
    "statement": "Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.",
    "formalStatement": "Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.",
    "mathematicalFormulation": "Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list.",
    "assumptions": [
      "Exactly the displayed Lean binders and the explicit profile definitions."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:operation/Sequence-edit-replace-all"
    ],
    "source": [
      "urn:csabs:source/extension-profiles-2026-11-20",
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Catalog.replaceSymbol_eq_replaceAll; pinned Mathlib finite-list, finite-set and relation primitives",
    "sourceNote": "Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.",
    "provenanceKind": "derived",
    "proofSketch": "Use the concrete definitions and the compiled proof in the cited local module.",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (a b : A) (xs : List A), Catalog.replaceSymbol a b xs = Catalog.replaceAll [a] (by simp) [b] xs",
    "leanModelMapping": "Pointwise symbol replacement equals the existing Sequence.replaceAll [a] [b] operation on every finite list. Exact equality and typed carriers are those displayed in the Lean proposition.",
    "leanModelLimitations": "Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.",
    "leanPremiseMapping": "{\"urn:csabs:operation/Sequence-edit-replace-all\": \"Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/extension-profiles-2026-11-20",
    "formulationLocator": "Catalog.replaceSymbol_eq_replaceAll",
    "reviewStatus": "Selected model proof; verification requires fresh compiler and axiom audit."
  },
  {
    "id": "urn:csabs:theorem/RewriteSystem-singleton-replace-all-confluence",
    "type": "Theorem",
    "name": "singleton-replace-all-confluence",
    "statement": "Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.",
    "formalStatement": "Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.",
    "mathematicalFormulation": "Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting.",
    "assumptions": [
      "Exactly the displayed Lean binders and the explicit profile definitions."
    ],
    "appliesTo": [
      "urn:csabs:concept/RewriteSystem"
    ],
    "dependsOn": [
      "urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence",
      "urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence"
    ],
    "source": [
      "urn:csabs:source/extension-profiles-2026-11-20",
      "urn:csabs:source/utility-mathlib-pinned"
    ],
    "sourceLocator": "Catalog.symbolRewrite_confluent; pinned Mathlib finite-list, finite-set and relation primitives",
    "sourceNote": "Constructed and proved in the local module from the directly linked primitive definitions; not attributed verbatim to Mathlib.",
    "provenanceKind": "derived",
    "proofSketch": "Use the concrete definitions and the compiled proof in the cited local module.",
    "leanFormulation": "∀ {A : Type u} [DecidableEq A] (a b : A), Catalog.Programs.confluent (Catalog.symbolRewrite a b)",
    "leanModelMapping": "Define xs→ys iff ys=replaceAll([a],[b],xs) and ys≠xs. This full-pass rewrite relation is confluent: every pair of reachable reducts joins at their common normalized replacement result. This is not arbitrary-position substring rewriting. Exact equality and typed carriers are those displayed in the Lean proposition.",
    "leanModelLimitations": "Selected mathematical profile only; singleton replacement does not establish arbitrary substring replacement confluence. Set endpoint declarations use disjunctive membership; no automatic subtype closure.",
    "leanPremiseMapping": "{\"urn:csabs:theorem/RewriteSystem-singleton-replace-all-correspondence\": \"Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.\", \"urn:csabs:theorem/RewriteSystem-singleton-replace-all-idempotence\": \"Interpret the linked definitions on the explicit carriers in the witness; no target law is assumed.\"}",
    "formulationScope": "registered-witness-type",
    "formulationSource": "urn:csabs:source/extension-profiles-2026-11-20",
    "formulationLocator": "Catalog.symbolRewrite_confluent",
    "reviewStatus": "Selected model proof; verification requires fresh compiler and axiom audit."
  }
]
```
<!-- graph-record:end -->
