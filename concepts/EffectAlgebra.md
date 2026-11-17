# Program side-effect algebra (total sequential effect-quantale profile)

A join semilattice of abstract program effects equipped with associative sequential composition, a no-effect identity and distributivity over alternatives.

**Notation:** (E,⊑,⊔,▷,ε); a⊑b ⇔ a⊔b=b; a▷(b⊔c)=(a▷b)⊔(a▷c).

**Stable ID:** `urn:csabs:concept/EffectAlgebra`

**Categories:** Programming-language semantics, Algebra, Order and fixed points

**Kind:** Mathematical structure

**Prerequisites:** [Join semilattice](JoinSemilattice.md), [Monoid](Monoid.md)

**Specializes:** [Join semilattice](JoinSemilattice.md), [Monoid](Monoid.md)

**Related concepts:** [Conservative resource effect summary](EffectSummary.md), [Relational method contract with write effects](MethodContract.md), [Call-boundary behavior and effect contract](CallEffectContract.md), [Exclusive finite-heap separation predicates](HeapSeparation.md)

## Backlinks

- [Observable behavior refinement (ObservationalRefinement)](BehaviorRefinement.md) — `relatedConcept`
- [Conservative resource effect summary](EffectSummary.md) — `relatedConcept`

## Mathematical formulation

(E,⊑,⊔,▷,ε); a⊑b ⇔ a⊔b=b; a▷(b⊔c)=(a▷b)⊔(a▷c). This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**Lean formulation** (in its source module context):

```lean
structure EffectAlgebra (E : Type u) where
  join : E → E → E
  sequence : E → E → E
  identity : E
  joinAssoc : ∀ a b c, join (join a b) c = join a (join b c)
  joinComm : ∀ a b, join a b = join b a
  joinIdem : ∀ a, join a a = a
  seqAssoc : ∀ a b c, sequence (sequence a b) c = sequence a (sequence b c)
  leftIdentity : ∀ a, sequence identity a = a
  rightIdentity : ∀ a, sequence a identity = a
  leftDistrib : ∀ a b c, sequence a (join b c) = join (sequence a b) (sequence a c)
  rightDistrib : ∀ a b c, sequence (join a b) c = join (sequence a c) (sequence b c)
```

**Source:** [`Catalog.Programs.EffectAlgebra`](../lean/Catalog/ProgramStructures.lean); consulted 2026-11-17.

**Scope:** model

**Interpretation:** Total join and sequence on E, sequential identity and explicit semilattice/monoid/distributivity fields; subeffect is join-induced ordering.

**Limits:** No interpretation of concrete program executions, effect-inference soundness, atomic effects, iteration, concurrency, or quantum-logical effects. No registered theorem witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Join associativity/commutativity/idempotence; sequential monoid; left and right distribution. No additive zero or annihilation assumption.

**basisKind:** extensional-structural-definition

**basisScope:** This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**specializationNote:** For JoinSemilattice retain E,⊑,⊔. For Monoid retain E,▷,ε. Join is not the sequential operation; distributivity relates the two. ε makes the carrier nonempty.

**verificationObligation:** Instantiate carrier, equality, operation definedness and semantic assumptions before application.; Typed links do not transfer axioms; retrieve explicit premises.

**reviewStatus:** Editorial mathematical interface review; Lean models and individual proof witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-EffectAlgebra-sequence"></a>

### sequence

`urn:csabs:operation/EffectAlgebra-sequence`

**signature:** ▷ : E×E → E

**description:** Compose effects in program evaluation order, first a then b.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Compose effects in program evaluation order, first a then b.

**totality:** Total on the displayed typed domain.

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EffectAlgebra-alternative"></a>

### alternative

`urn:csabs:operation/EffectAlgebra-alternative`

**signature:** ⊔ : E×E → E

**description:** Return the least conservative effect upper bound of either branch.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return the least conservative effect upper bound of either branch.

**totality:** Total on the displayed typed domain.

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EffectAlgebra-identity"></a>

### identity

`urn:csabs:operation/EffectAlgebra-identity`

**signature:** ε : Unit → E

**description:** Return the sequential identity effect.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** Return the sequential identity effect.

**totality:** Total on the displayed typed domain.

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-EffectAlgebra-subeffect"></a>

### subeffect

`urn:csabs:operation/EffectAlgebra-subeffect`

**signature:** ⊑ : E×E → Prop

**description:** a⊑b iff a⊔b=b; b is an allowed conservative enlargement of a.

**precondition:** Arguments range over the stated typed carriers.

**postcondition:** a⊑b iff a⊔b=b; b is an allowed conservative enlargement of a.

**totality:** Total on the displayed typed domain.

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-EffectAlgebra-join-structure"></a>

### join-structure

`urn:csabs:axiom/EffectAlgebra-join-structure`

**description:** Defining rule for Program side-effect algebra (total sequential effect-quantale profile)

**statement:** ⊔ is associative, commutative and idempotent; a⊑b ⇔ a⊔b=b.

**formalStatement:** ⊔ is associative, commutative and idempotent; a⊑b ⇔ a⊔b=b.

**assumptions:** This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-EffectAlgebra-sequencing-monoid"></a>

### sequencing-monoid

`urn:csabs:axiom/EffectAlgebra-sequencing-monoid`

**description:** Defining rule for Program side-effect algebra (total sequential effect-quantale profile)

**statement:** (a▷b)▷c=a▷(b▷c); ε▷a=a=a▷ε.

**formalStatement:** (a▷b)▷c=a▷(b▷c); ε▷a=a=a▷ε.

**assumptions:** This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-EffectAlgebra-distributivity"></a>

### distributivity

`urn:csabs:axiom/EffectAlgebra-distributivity`

**description:** Defining rule for Program side-effect algebra (total sequential effect-quantale profile)

**statement:** a▷(b⊔c)=(a▷b)⊔(a▷c); (a⊔b)▷c=(a▷c)⊔(b▷c).

**formalStatement:** a▷(b⊔c)=(a▷b)⊔(a▷c); (a⊔b)▷c=(a▷c)⊔(b▷c).

**assumptions:** This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**ruleRole:** defining-rule

**reviewStatus:** Editorial statement; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-EffectAlgebra-sequencing-monotone"></a>

### sequencing-monotone

`urn:csabs:law/EffectAlgebra-sequencing-monotone`

**description:** a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.

**statement:** a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.

**formalStatement:** a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.

**assumptions:** This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.

**dependsOn:** [join-structure](EffectAlgebra.md#node-urn-csabs-axiom-EffectAlgebra-join-structure); [distributivity](EffectAlgebra.md#node-urn-csabs-axiom-EffectAlgebra-distributivity)

**proofSketch:** If a⊔b=b, distribution gives (a▷c)⊔(b▷c)=(a⊔b)▷c=b▷c. Similarly c⊑d implies b▷c⊑b▷d. The join-induced order is transitive.

**reviewStatus:** Editorial derivation; no registered Lean proof witness.

**notationLanguage:** informal mathematical Unicode

**source:** [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Derived from the linked premises by the supplied editorial proof sketch.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Sky Wilshaw and Graham Hutton: A Compositional Semantics for Explicit Naming (Functional Pearl)](https://people.cs.nott.ac.uk/pszgmh/explicit-naming.pdf); accessedOn: 2026-11-17; sourceRole: consulted-primary-research

**sourceLocator:** §3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.

**sourceNote:** Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/EffectAlgebra",
    "type": "Concept",
    "shortForm": "EffectAlgebra",
    "fullName": "Program side-effect algebra (total sequential effect-quantale profile)",
    "definition": "A join semilattice of abstract program effects equipped with associative sequential composition, a no-effect identity and distributivity over alternatives.",
    "notation": "(E,⊑,⊔,▷,ε); a⊑b ⇔ a⊔b=b; a▷(b⊔c)=(a▷b)⊔(a▷c).",
    "category": [
      "urn:csabs:category/programming-semantics",
      "urn:csabs:category/algebra",
      "urn:csabs:category/order"
    ],
    "kind": "urn:csabs:kind/mathematical-structure",
    "basisKind": "extensional-structural-definition",
    "basisScope": "This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.",
    "axiomBasis": "Join associativity/commutativity/idempotence; sequential monoid; left and right distribution. No additive zero or annihilation assumption.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial mathematical interface review; Lean models and individual proof witnesses are separate.",
    "verificationObligation": [
      "Instantiate carrier, equality, operation definedness and semantic assumptions before application.",
      "Typed links do not transfer axioms; retrieve explicit premises."
    ],
    "mathematicalFormulation": "(E,⊑,⊔,▷,ε); a⊑b ⇔ a⊔b=b; a▷(b⊔c)=(a▷b)⊔(a▷c). This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency.",
    "requiresConcept": [
      "urn:csabs:concept/JoinSemilattice",
      "urn:csabs:concept/Monoid"
    ],
    "relatedConcept": [
      "urn:csabs:concept/EffectSummary",
      "urn:csabs:concept/MethodContract",
      "urn:csabs:concept/CallEffectContract",
      "urn:csabs:concept/HeapSeparation"
    ],
    "hasOperation": [
      "urn:csabs:operation/EffectAlgebra-sequence",
      "urn:csabs:operation/EffectAlgebra-alternative",
      "urn:csabs:operation/EffectAlgebra-identity",
      "urn:csabs:operation/EffectAlgebra-subeffect"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/EffectAlgebra-join-structure",
      "urn:csabs:axiom/EffectAlgebra-sequencing-monoid",
      "urn:csabs:axiom/EffectAlgebra-distributivity"
    ],
    "hasLaw": [
      "urn:csabs:law/EffectAlgebra-sequencing-monotone"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/JoinSemilattice",
      "urn:csabs:concept/Monoid"
    ],
    "specializationNote": "For JoinSemilattice retain E,⊑,⊔. For Monoid retain E,▷,ε. Join is not the sequential operation; distributivity relates the two. ε makes the carrier nonempty.",
    "leanFormulation": "structure EffectAlgebra (E : Type u) where\n  join : E → E → E\n  sequence : E → E → E\n  identity : E\n  joinAssoc : ∀ a b c, join (join a b) c = join a (join b c)\n  joinComm : ∀ a b, join a b = join b a\n  joinIdem : ∀ a, join a a = a\n  seqAssoc : ∀ a b c, sequence (sequence a b) c = sequence a (sequence b c)\n  leftIdentity : ∀ a, sequence identity a = a\n  rightIdentity : ∀ a, sequence a identity = a\n  leftDistrib : ∀ a b c, sequence a (join b c) = join (sequence a b) (sequence a c)\n  rightDistrib : ∀ a b c, sequence (join a b) c = join (sequence a c) (sequence b c)",
    "formulationSource": "urn:csabs:source/local-lean-ProgramStructures",
    "formulationLocator": "Catalog.Programs.EffectAlgebra",
    "formulationScope": "model",
    "leanModelMapping": "Total join and sequence on E, sequential identity and explicit semilattice/monoid/distributivity fields; subeffect is join-induced ordering.",
    "leanModelLimitations": "No interpretation of concrete program executions, effect-inference soundness, atomic effects, iteration, concurrency, or quantum-logical effects. No registered theorem witnesses."
  },
  {
    "id": "urn:csabs:operation/EffectAlgebra-sequence",
    "type": "Operation",
    "name": "sequence",
    "signature": "▷ : E×E → E",
    "description": "Compose effects in program evaluation order, first a then b.",
    "concept": "urn:csabs:concept/EffectAlgebra",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Compose effects in program evaluation order, first a then b.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EffectAlgebra-alternative",
    "type": "Operation",
    "name": "alternative",
    "signature": "⊔ : E×E → E",
    "description": "Return the least conservative effect upper bound of either branch.",
    "concept": "urn:csabs:concept/EffectAlgebra",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return the least conservative effect upper bound of either branch.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EffectAlgebra-identity",
    "type": "Operation",
    "name": "identity",
    "signature": "ε : Unit → E",
    "description": "Return the sequential identity effect.",
    "concept": "urn:csabs:concept/EffectAlgebra",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "Return the sequential identity effect.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/EffectAlgebra-subeffect",
    "type": "Operation",
    "name": "subeffect",
    "signature": "⊑ : E×E → Prop",
    "description": "a⊑b iff a⊔b=b; b is an allowed conservative enlargement of a.",
    "concept": "urn:csabs:concept/EffectAlgebra",
    "precondition": "Arguments range over the stated typed carriers.",
    "postcondition": "a⊑b iff a⊔b=b; b is an allowed conservative enlargement of a.",
    "totality": "Total on the displayed typed domain.",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EffectAlgebra-join-structure",
    "type": "Axiom",
    "name": "join-structure",
    "description": "Defining rule for Program side-effect algebra (total sequential effect-quantale profile)",
    "statement": "⊔ is associative, commutative and idempotent; a⊑b ⇔ a⊔b=b.",
    "formalStatement": "⊔ is associative, commutative and idempotent; a⊑b ⇔ a⊔b=b.",
    "assumptions": [
      "This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectAlgebra"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EffectAlgebra-sequencing-monoid",
    "type": "Axiom",
    "name": "sequencing-monoid",
    "description": "Defining rule for Program side-effect algebra (total sequential effect-quantale profile)",
    "statement": "(a▷b)▷c=a▷(b▷c); ε▷a=a=a▷ε.",
    "formalStatement": "(a▷b)▷c=a▷(b▷c); ε▷a=a=a▷ε.",
    "assumptions": [
      "This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectAlgebra"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/EffectAlgebra-distributivity",
    "type": "Axiom",
    "name": "distributivity",
    "description": "Defining rule for Program side-effect algebra (total sequential effect-quantale profile)",
    "statement": "a▷(b⊔c)=(a▷b)⊔(a▷c); (a⊔b)▷c=(a▷c)⊔(b▷c).",
    "formalStatement": "a▷(b⊔c)=(a▷b)⊔(a▷c); (a⊔b)▷c=(a▷c)⊔(b▷c).",
    "assumptions": [
      "This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectAlgebra"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial statement; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Adapted to the explicitly stated catalog profile, carriers, equality and definedness; additional restrictions are identified in basisScope.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/EffectAlgebra-sequencing-monotone",
    "type": "Law",
    "name": "sequencing-monotone",
    "description": "a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.",
    "statement": "a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.",
    "formalStatement": "a⊑b ∧ c⊑d ⇒ a▷c ⊑ b▷d.",
    "assumptions": [
      "This is an algebra of program side effects, not the quantum-logical partial-sum effect algebra. Selected total effect-quantale profile: join and sequencing total, equality carrier equality, sequencing generally noncommutative. ε is sequential no-effect, not necessarily least; no bottom, top, iteration, parallel composition or cancellation is required. Partial protocol-effect algebras need a distinct definedness-aware variant. To model reads, writes, allocation, freeing, I/O or exceptions, supply atomic effects and a sound interpretation; algebraic laws alone do not justify reordering, speculation or concurrency."
    ],
    "appliesTo": [
      "urn:csabs:concept/EffectAlgebra"
    ],
    "dependsOn": [
      "urn:csabs:axiom/EffectAlgebra-join-structure",
      "urn:csabs:axiom/EffectAlgebra-distributivity"
    ],
    "proofSketch": "If a⊔b=b, distribution gives (a▷c)⊔(b▷c)=(a⊔b)▷c=b▷c. Similarly c⊑d implies b▷c⊑b▷d. The join-induced order is transitive.",
    "reviewStatus": "Editorial derivation; no registered Lean proof witness.",
    "notationLanguage": "informal mathematical Unicode",
    "source": [
      "urn:csabs:source/wilshaw-hutton-explicit-naming"
    ],
    "sourceLocator": "§3.3 name-effect sequencing; §3.4 Definition 3.8, p.12; adapted by restricting both operations to be total.",
    "sourceNote": "Derived from the linked premises by the supplied editorial proof sketch.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
