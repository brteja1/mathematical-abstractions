# Finite fused sequence iterator

An immutable finite sequence cursor retaining its original sequence and a position from zero through length.

**Notation:** Iter(A)={(s,p) | s∈Seq(A), 0≤p≤|s|}

**Stable ID:** `urn:csabs:concept/FiniteIterator`

**Categories:** Data structures → Sequential collections

**Kind:** Abstract data type

**Prerequisites:** [Finite sequence (List datatype)](Sequence.md), [Option Type](OptionType.md), [Natural Number](NaturalNumber.md)

## Backlinks

- [Asymmetric coroutine with explicit resume/yield lifecycle](AsymmetricCoroutine.md) — `relatedConcept`

## Mathematical formulation

A cursor is (xs,p) with xs∈A\*,0≤p≤|xs|. next(xs,p)=(some(xs[p]),(xs,p+1)) when p<|xs|, and (none,(xs,p)) otherwise. Equality retains both xs and p.

**Lean formulation** (in its source module context):

```lean
structure FiniteIterator (A : Type u) where
  values : List A
  position : Fin (values.length + 1)
```

**Source:** [`Catalog.FiniteIterator`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Iter(A)={(s,p) | s∈Seq(A), 0≤p≤|s|}. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.

**Limits:** Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** 0≤p≤|s| for every (s,p)∈Iter(A); p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p)); remaining(s,p)=drop(p,s)

**basisKind:** extensional-structural-definition

**basisScope:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.

**verificationObligation:** Map carrier, equality, operation definedness and stated profile to the target API or proof context.; Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.; Model coverage does not establish every recorded claim or an implementation refinement.

**reviewStatus:** Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-FiniteIterator-start"></a>

### start

`urn:csabs:operation/FiniteIterator-start`

**signature:** start : Seq(A)→Iter(A)

**description:** start(s)=(s,0).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** start(s)=(s,0).

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteIterator-next"></a>

### next

`urn:csabs:operation/FiniteIterator-next`

**signature:** next : Iter(A)→Option(A)×Iter(A)

**description:** If p<|s| return (Some(s[p]),(s,p+1)); otherwise (None,(s,p)).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** If p<|s| return (Some(s[p]),(s,p+1)); otherwise (None,(s,p)).

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-FiniteIterator-remaining"></a>

### remaining

`urn:csabs:operation/FiniteIterator-remaining`

**signature:** remaining : Iter(A)→Seq(A)

**description:** remaining(s,p)=drop(p,s).

**precondition:** Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.

**totality:** Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.

**postcondition:** remaining(s,p)=drop(p,s).

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-FiniteIterator-cursor-range"></a>

### cursor-range

`urn:csabs:axiom/FiniteIterator-cursor-range`

**statement:** Defining requirement: 0≤p≤|s| for every (s,p)∈Iter(A)

**formalStatement:** 0≤p≤|s| for every (s,p)∈Iter(A)

**assumptions:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteIterator-next-equations"></a>

### next-equations

`urn:csabs:axiom/FiniteIterator-next-equations`

**statement:** Defining requirement: p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p))

**formalStatement:** p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p))

**assumptions:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-FiniteIterator-remaining-equation"></a>

### remaining-equation

`urn:csabs:axiom/FiniteIterator-remaining-equation`

**statement:** Defining requirement: remaining(s,p)=drop(p,s)

**formalStatement:** remaining(s,p)=drop(p,s)

**assumptions:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.; All variables range over the typed carriers in the notation and signatures.

**ruleRole:** defining-rule

**reviewStatus:** Editorial source/interface review; Lean model and individual proof evidence are separate.

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-FiniteIterator-fused-exhaustion"></a>

### fused-exhaustion

`urn:csabs:law/FiniteIterator-fused-exhaustion`

**statement:** next(i)=(None,j) ⇒ next(j)=(None,j)

**formalStatement:** next(i)=(None,j) ⇒ next(j)=(None,j)

**assumptions:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [cursor-range](FiniteIterator.md#node-urn-csabs-axiom-FiniteIterator-cursor-range); [next-equations](FiniteIterator.md#node-urn-csabs-axiom-FiniteIterator-next-equations)

**proofSketch:** None can arise only at p=length; next keeps that same state.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

#### Mathematical formulation

**Lean formulation** (in its source module context):

```lean
∀ {A : Type} (it j : Catalog.FiniteIterator A), it.next = (none, j) → j.next = (none, j)
```

**Source:** [`Catalog.CoreDataProofs.iterator_fused`](../lean/Catalog/CoreData.lean); consulted 2026-11-12.

**Scope:** registered-witness-type

**Interpretation:** FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile.

**Limits:** Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

**Direct premise mapping:**

```json
{
  "urn:csabs:axiom/FiniteIterator-cursor-range": "Interpreted premise: 0≤p≤|s| for every (s,p)∈Iter(A). FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile.",
  "urn:csabs:axiom/FiniteIterator-next-equations": "Interpreted premise: p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p)). FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile."
}
```

## Theorems

<a id="node-urn-csabs-theorem-FiniteIterator-finite-consumption"></a>

### finite-consumption

`urn:csabs:theorem/FiniteIterator-finite-consumption`

**statement:** From (s,p), exactly |s|-p successful next steps precede permanent None

**formalStatement:** From (s,p), exactly |s|-p successful next steps precede permanent None

**assumptions:** State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.; Typed mathematical equality and the stated defining requirements.

**dependsOn:** [cursor-range](FiniteIterator.md#node-urn-csabs-axiom-FiniteIterator-cursor-range); [next-equations](FiniteIterator.md#node-urn-csabs-axiom-FiniteIterator-next-equations)

**proofSketch:** Induct on |s|-p; each successful step increases p by one, and the zero case is exhaustion.

**reviewStatus:** Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.

**source:** [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference; [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.

**provenanceKind:** derived

## Concept provenance

- [Rust standard library: FusedIterator](https://doc.rust-lang.org/std/iter/trait.FusedIterator.html); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference
- [Mathlib pinned definitions: Data/Stream/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Data/Stream/Defs.lean); accessedOn: 2026-11-07; sourceRole: consulted-definition-and-interface-reference

**sourceLocator:** FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec

**sourceNote:** Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/FiniteIterator",
    "type": "Concept",
    "shortForm": "FiniteIterator",
    "fullName": "Finite fused sequence iterator",
    "category": [
      "urn:csabs:category/sequential-collections"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "definition": "An immutable finite sequence cursor retaining its original sequence and a position from zero through length.",
    "notation": "Iter(A)={(s,p) | s∈Seq(A), 0≤p≤|s|}",
    "requiresConcept": [
      "urn:csabs:concept/Sequence",
      "urn:csabs:concept/OptionType",
      "urn:csabs:concept/NaturalNumber"
    ],
    "relatedConcept": [],
    "hasOperation": [
      "urn:csabs:operation/FiniteIterator-start",
      "urn:csabs:operation/FiniteIterator-next",
      "urn:csabs:operation/FiniteIterator-remaining"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/FiniteIterator-cursor-range",
      "urn:csabs:axiom/FiniteIterator-next-equations",
      "urn:csabs:axiom/FiniteIterator-remaining-equation"
    ],
    "hasLaw": [
      "urn:csabs:law/FiniteIterator-fused-exhaustion"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/FiniteIterator-finite-consumption"
    ],
    "axiomBasis": "0≤p≤|s| for every (s,p)∈Iter(A); p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p)); remaining(s,p)=drop(p,s)",
    "basisKind": "extensional-structural-definition",
    "basisScope": "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
    "coverageStatus": "basis-reviewed",
    "verificationObligation": [
      "Map carrier, equality, operation definedness and stated profile to the target API or proof context.",
      "Prerequisites and hierarchy links do not transfer axioms; retrieve explicit premises.",
      "Model coverage does not establish every recorded claim or an implementation refinement."
    ],
    "reviewStatus": "Editorial source/interface review with a Lean carrier binding; individual witnesses recorded separately.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted",
    "leanFormulation": "structure FiniteIterator (A : Type u) where\n  values : List A\n  position : Fin (values.length + 1)",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.FiniteIterator",
    "formulationScope": "model",
    "leanModelMapping": "Iter(A)={(s,p) | s∈Seq(A), 0≤p≤|s|}. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
    "leanModelLimitations": "Compiled carrier and selected interface interpretation. Some catalog operations are specified mathematically rather than wrapped as Lean declarations; no blanket proof of claims, algorithms, parsing, liveness or complexity. See individual witnesses.",
    "mathematicalFormulation": "A cursor is (xs,p) with xs∈A*,0≤p≤|xs|. next(xs,p)=(some(xs[p]),(xs,p+1)) when p<|xs|, and (none,(xs,p)) otherwise. Equality retains both xs and p."
  },
  {
    "id": "urn:csabs:operation/FiniteIterator-start",
    "type": "Operation",
    "name": "start",
    "signature": "start : Seq(A)→Iter(A)",
    "description": "start(s)=(s,0).",
    "concept": "urn:csabs:concept/FiniteIterator",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "start(s)=(s,0).",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteIterator-next",
    "type": "Operation",
    "name": "next",
    "signature": "next : Iter(A)→Option(A)×Iter(A)",
    "description": "If p<|s| return (Some(s[p]),(s,p+1)); otherwise (None,(s,p)).",
    "concept": "urn:csabs:concept/FiniteIterator",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "If p<|s| return (Some(s[p]),(s,p+1)); otherwise (None,(s,p)).",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/FiniteIterator-remaining",
    "type": "Operation",
    "name": "remaining",
    "signature": "remaining : Iter(A)→Seq(A)",
    "description": "remaining(s,p)=drop(p,s).",
    "concept": "urn:csabs:concept/FiniteIterator",
    "precondition": "Inputs have the stated types and satisfy the restrictions in the signature and basisScope. State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
    "totality": "Partial on the explicitly restricted cases; otherwise total mathematical operation. Set-valued outcomes specify allowed nondeterminism, not a chosen algorithm.",
    "postcondition": "remaining(s,p)=drop(p,s).",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteIterator-cursor-range",
    "type": "Axiom",
    "name": "cursor-range",
    "statement": "Defining requirement: 0≤p≤|s| for every (s,p)∈Iter(A)",
    "formalStatement": "0≤p≤|s| for every (s,p)∈Iter(A)",
    "assumptions": [
      "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteIterator"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteIterator-next-equations",
    "type": "Axiom",
    "name": "next-equations",
    "statement": "Defining requirement: p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p))",
    "formalStatement": "p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p))",
    "assumptions": [
      "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteIterator"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/FiniteIterator-remaining-equation",
    "type": "Axiom",
    "name": "remaining-equation",
    "statement": "Defining requirement: remaining(s,p)=drop(p,s)",
    "formalStatement": "remaining(s,p)=drop(p,s)",
    "assumptions": [
      "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
      "All variables range over the typed carriers in the notation and signatures."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteIterator"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial source/interface review; Lean model and individual proof evidence are separate.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Adapted to the explicitly stated finite, typed and equality conventions of this entry. Additional profile restrictions and operation specifications are catalog choices, not claims about every implementation.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/FiniteIterator-fused-exhaustion",
    "type": "Law",
    "name": "fused-exhaustion",
    "statement": "next(i)=(None,j) ⇒ next(j)=(None,j)",
    "formalStatement": "next(i)=(None,j) ⇒ next(j)=(None,j)",
    "assumptions": [
      "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteIterator"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteIterator-cursor-range",
      "urn:csabs:axiom/FiniteIterator-next-equations"
    ],
    "proofSketch": "None can arise only at p=length; next keeps that same state.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived",
    "leanFormulation": "∀ {A : Type} (it j : Catalog.FiniteIterator A), it.next = (none, j) → j.next = (none, j)",
    "formulationSource": "urn:csabs:source/local-lean-CoreData",
    "formulationLocator": "Catalog.CoreDataProofs.iterator_fused",
    "formulationScope": "registered-witness-type",
    "leanModelMapping": "FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile.",
    "leanModelLimitations": "Only the displayed proposition for this explicit interpretation. No proof of all catalog claims or of a software implementation; informal/formal correspondence remains reviewed metadata.",
    "leanPremiseMapping": "{\"urn:csabs:axiom/FiniteIterator-cursor-range\": \"Interpreted premise: 0≤p≤|s| for every (s,p)∈Iter(A). FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile.\", \"urn:csabs:axiom/FiniteIterator-next-equations\": \"Interpreted premise: p<|s| ⇒ next(s,p)=(Some(s[p]),(s,p+1)); p=|s| ⇒ next(s,p)=(None,(s,p)). FiniteIterator is List A plus a Fin(length+1) cursor; next returns an Option payload and new immutable cursor. None occurs only at exhaustion and preserves the cursor; list and position equality match the graph profile.\"}"
  },
  {
    "id": "urn:csabs:theorem/FiniteIterator-finite-consumption",
    "type": "Theorem",
    "name": "finite-consumption",
    "statement": "From (s,p), exactly |s|-p successful next steps precede permanent None",
    "formalStatement": "From (s,p), exactly |s|-p successful next steps precede permanent None",
    "assumptions": [
      "State equality retains original s and p, even when remaining suffixes agree. Finite pure fused profile; generic effectful or resumable iterators require another model. None is exhaustion, not a payload.",
      "Typed mathematical equality and the stated defining requirements."
    ],
    "appliesTo": [
      "urn:csabs:concept/FiniteIterator"
    ],
    "dependsOn": [
      "urn:csabs:axiom/FiniteIterator-cursor-range",
      "urn:csabs:axiom/FiniteIterator-next-equations"
    ],
    "proofSketch": "Induct on |s|-p; each successful step increases p by one, and the zero case is exhaustion.",
    "reviewStatus": "Editorial derivation; a compiled Lean witness is asserted only by a fresh individual binding verification report.",
    "source": [
      "urn:csabs:source/rust-fused-core",
      "urn:csabs:source/mathlib-stream-core"
    ],
    "sourceLocator": "FusedIterator contract: all subsequent next results remain None after exhaustion; Stream', cons, get, head, tail, map and corec",
    "sourceNote": "Catalog derivation from the explicitly linked premises; source supplies the selected underlying interface. No executable proof is implied.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
