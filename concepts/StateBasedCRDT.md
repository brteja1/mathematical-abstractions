# State-based CRDT replication algebra

A join-semilattice state space with bottom and inflationary local updates, merged by join.

**Notation:** (S,≤,⊔,⊥,update)

**Stable ID:** `urn:csabs:concept/StateBasedCRDT`

**Categories:** Concurrency and distributed systems → Replication

**Kind:** semantic-model

**Prerequisites:** [Join semilattice](JoinSemilattice.md), [Partial Order](PartialOrder.md)

## Interface and scope

**axiomBasis:** (S,≤,⊔) is a join semilattice and ∀s,⊥≤s; ∀o,s, s≤update(o,s); merge(s,t)=s⊔t

**basisKind:** extensional-structural-definition

**basisScope:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-StateBasedCRDT-initial"></a>

### initial

`urn:csabs:operation/StateBasedCRDT-initial`

**signature:** initial : S

**description:** initial=⊥.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** initial=⊥.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StateBasedCRDT-update"></a>

### update

`urn:csabs:operation/StateBasedCRDT-update`

**signature:** update : Op×S→S

**description:** Local update satisfies s≤update(o,s).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** Local update satisfies s≤update(o,s).

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-StateBasedCRDT-merge"></a>

### merge

`urn:csabs:operation/StateBasedCRDT-merge`

**signature:** merge : S×S→S

**description:** merge(s,t)=s⊔t.

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** merge(s,t)=s⊔t.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-StateBasedCRDT-state-order"></a>

### state-order

`urn:csabs:axiom/StateBasedCRDT-state-order`

**statement:** Defining requirement: (S,≤,⊔) is a join semilattice and ∀s,⊥≤s

**formalStatement:** (S,≤,⊔) is a join semilattice and ∀s,⊥≤s

**assumptions:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-StateBasedCRDT-inflationary"></a>

### inflationary

`urn:csabs:axiom/StateBasedCRDT-inflationary`

**statement:** Defining requirement: ∀o,s, s≤update(o,s)

**formalStatement:** ∀o,s, s≤update(o,s)

**assumptions:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-StateBasedCRDT-merge-definition"></a>

### merge-definition

`urn:csabs:axiom/StateBasedCRDT-merge-definition`

**statement:** Defining requirement: merge(s,t)=s⊔t

**formalStatement:** merge(s,t)=s⊔t

**assumptions:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-StateBasedCRDT-merge-idempotent"></a>

### merge-idempotent

`urn:csabs:law/StateBasedCRDT-merge-idempotent`

**statement:** merge(s,s)=s

**formalStatement:** merge(s,s)=s

**assumptions:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [state-order](StateBasedCRDT.md#node-urn-csabs-axiom-StateBasedCRDT-state-order); [merge-definition](StateBasedCRDT.md#node-urn-csabs-axiom-StateBasedCRDT-merge-definition)

**proofSketch:** By join leastness s⊔s=s; expand merge.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-StateBasedCRDT-merge-commutative"></a>

### merge-commutative

`urn:csabs:theorem/StateBasedCRDT-merge-commutative`

**statement:** merge(s,t)=merge(t,s)

**formalStatement:** merge(s,t)=merge(t,s)

**assumptions:** Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [state-order](StateBasedCRDT.md#node-urn-csabs-axiom-StateBasedCRDT-state-order); [merge-definition](StateBasedCRDT.md#node-urn-csabs-axiom-StateBasedCRDT-merge-definition)

**proofSketch:** Both orders compute the same least upper bound by antisymmetry.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Preguiça, Baquero and Shapiro: Conflict-free Replicated Data Types (2018)](https://arxiv.org/pdf/1805.06358); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Order/Defs/Lattice.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Order/Defs/Lattice.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/StateBasedCRDT",
    "type": "Concept",
    "shortForm": "StateBasedCRDT",
    "fullName": "State-based CRDT replication algebra",
    "category": [
      "urn:csabs:category/replication"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "definition": "A join-semilattice state space with bottom and inflationary local updates, merged by join.",
    "notation": "(S,≤,⊔,⊥,update)",
    "requiresConcept": [
      "urn:csabs:concept/JoinSemilattice",
      "urn:csabs:concept/PartialOrder"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/StateBasedCRDT-initial",
      "urn:csabs:operation/StateBasedCRDT-update",
      "urn:csabs:operation/StateBasedCRDT-merge"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/StateBasedCRDT-state-order",
      "urn:csabs:axiom/StateBasedCRDT-inflationary",
      "urn:csabs:axiom/StateBasedCRDT-merge-definition"
    ],
    "hasLaw": [
      "urn:csabs:law/StateBasedCRDT-merge-idempotent"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/StateBasedCRDT-merge-commutative"
    ],
    "axiomBasis": "(S,≤,⊔) is a join semilattice and ∀s,⊥≤s; ∀o,s, s≤update(o,s); merge(s,t)=s⊔t",
    "basisKind": "extensional-structural-definition",
    "basisScope": "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StateBasedCRDT-initial",
    "type": "Operation",
    "name": "initial",
    "signature": "initial : S",
    "description": "initial=⊥.",
    "concept": "urn:csabs:concept/StateBasedCRDT",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "initial=⊥.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StateBasedCRDT-update",
    "type": "Operation",
    "name": "update",
    "signature": "update : Op×S→S",
    "description": "Local update satisfies s≤update(o,s).",
    "concept": "urn:csabs:concept/StateBasedCRDT",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "Local update satisfies s≤update(o,s).",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/StateBasedCRDT-merge",
    "type": "Operation",
    "name": "merge",
    "signature": "merge : S×S→S",
    "description": "merge(s,t)=s⊔t.",
    "concept": "urn:csabs:concept/StateBasedCRDT",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "merge(s,t)=s⊔t.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StateBasedCRDT-state-order",
    "type": "Axiom",
    "name": "state-order",
    "statement": "Defining requirement: (S,≤,⊔) is a join semilattice and ∀s,⊥≤s",
    "formalStatement": "(S,≤,⊔) is a join semilattice and ∀s,⊥≤s",
    "assumptions": [
      "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateBasedCRDT"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StateBasedCRDT-inflationary",
    "type": "Axiom",
    "name": "inflationary",
    "statement": "Defining requirement: ∀o,s, s≤update(o,s)",
    "formalStatement": "∀o,s, s≤update(o,s)",
    "assumptions": [
      "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateBasedCRDT"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/StateBasedCRDT-merge-definition",
    "type": "Axiom",
    "name": "merge-definition",
    "statement": "Defining requirement: merge(s,t)=s⊔t",
    "formalStatement": "merge(s,t)=s⊔t",
    "assumptions": [
      "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateBasedCRDT"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/StateBasedCRDT-merge-idempotent",
    "type": "Law",
    "name": "merge-idempotent",
    "statement": "merge(s,s)=s",
    "formalStatement": "merge(s,s)=s",
    "assumptions": [
      "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateBasedCRDT"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StateBasedCRDT-state-order",
      "urn:csabs:axiom/StateBasedCRDT-merge-definition"
    ],
    "proofSketch": "By join leastness s⊔s=s; expand merge.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/StateBasedCRDT-merge-commutative",
    "type": "Theorem",
    "name": "merge-commutative",
    "statement": "merge(s,t)=merge(t,s)",
    "formalStatement": "merge(s,t)=merge(t,s)",
    "assumptions": [
      "Pure state-based algebra only. Updates need not commute or be order preserving beyond inflation. Eventual convergence requires delivery assumptions outside this record; no loss-free transport, liveness or Byzantine tolerance is asserted.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/StateBasedCRDT"
    ],
    "dependsOn": [
      "urn:csabs:axiom/StateBasedCRDT-state-order",
      "urn:csabs:axiom/StateBasedCRDT-merge-definition"
    ],
    "proofSketch": "Both orders compute the same least upper bound by antisymmetry.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/crdt-state-core",
      "urn:csabs:source/mathlib-join-core"
    ],
    "sourceLocator": "Synchronization Model, pp. 6–7: state-based join semilattice, inflationary update and join merge; SemilatticeSup: PartialOrder, le_sup_left, le_sup_right, sup_le",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
