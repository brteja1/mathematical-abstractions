# Mutex (non-reentrant mutual-exclusion lock)

An exclusive lock whose state records either no owner or exactly one owning process.

**Notation:** Mutex(P)=Option(P); owner=None | Some(p).

**Stable ID:** `urn:csabs:concept/Mutex`

**Categories:** Concurrency and distributed systems → Synchronization → Locks

**Kind:** Abstract data type

**Prerequisites:** [Lock with compatible access modes](Lock.md), [Option Type](OptionType.md)

**Specializes:** [Lock with compatible access modes](Lock.md)

**Related concepts:** [Safety Property](SafetyProperty.md), [Liveness Property](LivenessProperty.md)

## Backlinks

- [Lamport bakery lock protocol](LamportBakery.md) — `requiresConcept`

## Mathematical formulation

The selected non-reentrant mutex carrier is Option(P). Acquire(o,p,o′) ⇔ o=none∧o′=some(p); Release(o,p,o′) ⇔ o=some(p)∧o′=none. Only the owner may release; no scheduling policy is represented.

**Lean formulation** (in its source module context):

```lean
abbrev Mutex (P : Type u) := Option P
```

**Source:** [`Catalog.Mutex`](../lean/Catalog/Concurrency.lean); consulted 2026-11-12.

**Scope:** model

**Interpretation:** Option P with none unowned and some p owned. acquires/releases are guarded state relations; tryAcquire has exact non-spurious Boolean results. Equality is Option equality and process identity.

**Limits:** No blocking-call histories, fairness, recursive acquisition, crash recovery or memory fences. No compiled witnesses for the new graph claims.

Read with the linked module’s imports, namespaces, universes and section variables. Proof status requires a fresh Lean verification report; this formulation does not close historical bibliographic source gaps.

## Interface and scope

**axiomBasis:** Optional-owner carrier; initial None; acquire from None; release by owner; immediate try-acquire.

**basisKind:** operational-state-machine-definition

**basisScope:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**specializationNote:** Set M={exclusive} and C always false. Map None to the empty holder map and Some(p) to {p↦exclusive}; pairwise compatibility permits at most one holder. Acquire/release correspond under this bijection. Mutex rules are recorded directly, not inherited.

**verificationObligation:** Map process identity, equality, atomicity and memory visibility to the target model.; A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting.

**reviewStatus:** Editorial specification; model bindings and compiled claim witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Mutex-initial"></a>

### initial

`urn:csabs:operation/Mutex-initial`

**signature:** initial : Mutex(P)

**description:** Construct the unlocked state.

**precondition:** Fixed P.

**totality:** total on the stated precondition

**postcondition:** initial=None.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Mutex-acquire"></a>

### acquire

`urn:csabs:operation/Mutex-acquire`

**signature:** acquire : Mutex(P)×P ⇀ Mutex(P)

**description:** Grant exclusive ownership.

**precondition:** owner=None.

**totality:** total on the stated precondition

**postcondition:** acquire(None,p)=Some(p).

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Mutex-release"></a>

### release

`urn:csabs:operation/Mutex-release`

**signature:** release : Mutex(P)×P ⇀ Mutex(P)

**description:** Release exclusive ownership.

**precondition:** owner=Some(p).

**totality:** total on the stated precondition

**postcondition:** release(Some(p),p)=None.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Mutex-tryAcquire"></a>

### tryAcquire

`urn:csabs:operation/Mutex-tryAcquire`

**signature:** tryAcquire : Mutex(P)×P→Mutex(P)×Bool

**description:** Attempt an immediate exclusive grant.

**precondition:** Typed owner and process.

**totality:** total on the stated precondition

**postcondition:** tryAcquire(None,p)=(Some(p),true); tryAcquire(Some(q),p)=(Some(q),false).

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Mutex-owner"></a>

### owner

`urn:csabs:axiom/Mutex-owner`

**statement:** Mutex states are exactly the optional-owner values.

**formalStatement:** Mutex(P)=Option(P); holds(o,p) ⇔ o=Some(p); initial=None.

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Mutex-acquire"></a>

### acquire

`urn:csabs:axiom/Mutex-acquire`

**statement:** Acquire completes only from the unlocked state.

**formalStatement:** dom(acquire)={(None,p) | p∈P}; acquire(None,p)=Some(p).

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Mutex-release"></a>

### release

`urn:csabs:axiom/Mutex-release`

**statement:** Release is defined only for the owner.

**formalStatement:** dom(release)={(Some(p),p) | p∈P}; release(Some(p),p)=None.

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Mutex-try-result"></a>

### try-result

`urn:csabs:axiom/Mutex-try-result`

**statement:** Try-acquire succeeds exactly when unlocked.

**formalStatement:** tryAcquire(None,p)=(Some(p),true); tryAcquire(Some(q),p)=(Some(q),false).

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Mutex-acquire-release"></a>

### acquire-release

`urn:csabs:law/Mutex-acquire-release`

**statement:** Releasing after a successful acquisition restores the unlocked state.

**formalStatement:** release(acquire(None,p),p)=None

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**dependsOn:** [acquire](Mutex.md#node-urn-csabs-axiom-Mutex-acquire); [release](Mutex.md#node-urn-csabs-axiom-Mutex-release)

**proofSketch:** Substitute the acquisition equation into owner-only release.

**reviewStatus:** Editorial derivation; no compiled witness registered.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Derived from the linked premises under the stated profile; proof sketch is editorial.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-Mutex-exclusive-owner"></a>

### exclusive-owner

`urn:csabs:theorem/Mutex-exclusive-owner`

**statement:** Two holders of the same mutex are the same process.

**formalStatement:** holds(o,p) ∧ holds(o,q) ⇒ p=q

**assumptions:** Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.

**dependsOn:** [owner](Mutex.md#node-urn-csabs-axiom-Mutex-owner)

**proofSketch:** Both holdings identify o with Some(p) and Some(q); injectivity of Some gives p=q.

**reviewStatus:** Editorial derivation; no compiled witness registered.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Derived from the linked premises under the stated profile; proof sketch is editorial.

**provenanceKind:** derived

## Concept provenance

- [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract

**sourceLocator:** Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations

**sourceNote:** Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Mutex",
    "type": "Concept",
    "shortForm": "Mutex",
    "fullName": "Mutex (non-reentrant mutual-exclusion lock)",
    "definition": "An exclusive lock whose state records either no owner or exactly one owning process.",
    "notation": "Mutex(P)=Option(P); owner=None | Some(p).",
    "category": [
      "urn:csabs:category/locks"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "requiresConcept": [
      "urn:csabs:concept/Lock",
      "urn:csabs:concept/OptionType"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SafetyProperty",
      "urn:csabs:concept/LivenessProperty"
    ],
    "axiomBasis": "Optional-owner carrier; initial None; acquire from None; release by owner; immediate try-acquire.",
    "basisKind": "operational-state-machine-definition",
    "basisScope": "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; model bindings and compiled claim witnesses are separate.",
    "verificationObligation": [
      "Map process identity, equality, atomicity and memory visibility to the target model.",
      "A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting."
    ],
    "hasOperation": [
      "urn:csabs:operation/Mutex-initial",
      "urn:csabs:operation/Mutex-acquire",
      "urn:csabs:operation/Mutex-release",
      "urn:csabs:operation/Mutex-tryAcquire"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Mutex-owner",
      "urn:csabs:axiom/Mutex-acquire",
      "urn:csabs:axiom/Mutex-release",
      "urn:csabs:axiom/Mutex-try-result"
    ],
    "hasLaw": [
      "urn:csabs:law/Mutex-acquire-release"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/Mutex-exclusive-owner"
    ],
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted",
    "specializationOf": [
      "urn:csabs:concept/Lock"
    ],
    "specializationNote": "Set M={exclusive} and C always false. Map None to the empty holder map and Some(p) to {p↦exclusive}; pairwise compatibility permits at most one holder. Acquire/release correspond under this bijection. Mutex rules are recorded directly, not inherited.",
    "leanFormulation": "abbrev Mutex (P : Type u) := Option P",
    "formulationSource": "urn:csabs:source/local-lean-Concurrency",
    "formulationLocator": "Catalog.Mutex",
    "formulationScope": "model",
    "leanModelMapping": "Option P with none unowned and some p owned. acquires/releases are guarded state relations; tryAcquire has exact non-spurious Boolean results. Equality is Option equality and process identity.",
    "leanModelLimitations": "No blocking-call histories, fairness, recursive acquisition, crash recovery or memory fences. No compiled witnesses for the new graph claims.",
    "mathematicalFormulation": "The selected non-reentrant mutex carrier is Option(P). Acquire(o,p,o′) ⇔ o=none∧o′=some(p); Release(o,p,o′) ⇔ o=some(p)∧o′=none. Only the owner may release; no scheduling policy is represented."
  },
  {
    "id": "urn:csabs:operation/Mutex-initial",
    "type": "Operation",
    "name": "initial",
    "signature": "initial : Mutex(P)",
    "description": "Construct the unlocked state.",
    "precondition": "Fixed P.",
    "totality": "total on the stated precondition",
    "postcondition": "initial=None.",
    "concept": "urn:csabs:concept/Mutex",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Mutex-acquire",
    "type": "Operation",
    "name": "acquire",
    "signature": "acquire : Mutex(P)×P ⇀ Mutex(P)",
    "description": "Grant exclusive ownership.",
    "precondition": "owner=None.",
    "totality": "total on the stated precondition",
    "postcondition": "acquire(None,p)=Some(p).",
    "concept": "urn:csabs:concept/Mutex",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Mutex-release",
    "type": "Operation",
    "name": "release",
    "signature": "release : Mutex(P)×P ⇀ Mutex(P)",
    "description": "Release exclusive ownership.",
    "precondition": "owner=Some(p).",
    "totality": "total on the stated precondition",
    "postcondition": "release(Some(p),p)=None.",
    "concept": "urn:csabs:concept/Mutex",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Mutex-tryAcquire",
    "type": "Operation",
    "name": "tryAcquire",
    "signature": "tryAcquire : Mutex(P)×P→Mutex(P)×Bool",
    "description": "Attempt an immediate exclusive grant.",
    "precondition": "Typed owner and process.",
    "totality": "total on the stated precondition",
    "postcondition": "tryAcquire(None,p)=(Some(p),true); tryAcquire(Some(q),p)=(Some(q),false).",
    "concept": "urn:csabs:concept/Mutex",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Mutex-owner",
    "type": "Axiom",
    "name": "owner",
    "statement": "Mutex states are exactly the optional-owner values.",
    "formalStatement": "Mutex(P)=Option(P); holds(o,p) ⇔ o=Some(p); initial=None.",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Mutex-acquire",
    "type": "Axiom",
    "name": "acquire",
    "statement": "Acquire completes only from the unlocked state.",
    "formalStatement": "dom(acquire)={(None,p) | p∈P}; acquire(None,p)=Some(p).",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Mutex-release",
    "type": "Axiom",
    "name": "release",
    "statement": "Release is defined only for the owner.",
    "formalStatement": "dom(release)={(Some(p),p) | p∈P}; release(Some(p),p)=None.",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Mutex-try-result",
    "type": "Axiom",
    "name": "try-result",
    "statement": "Try-acquire succeeds exactly when unlocked.",
    "formalStatement": "tryAcquire(None,p)=(Some(p),true); tryAcquire(Some(q),p)=(Some(q),false).",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Selected owner-tracked non-reentrant exclusive profile. Blocking calls are represented by successful completion steps; invalid release and self-acquire are outside the partial-operation domain.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Mutex-acquire-release",
    "type": "Law",
    "name": "acquire-release",
    "statement": "Releasing after a successful acquisition restores the unlocked state.",
    "formalStatement": "release(acquire(None,p),p)=None",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Mutex-acquire",
      "urn:csabs:axiom/Mutex-release"
    ],
    "proofSketch": "Substitute the acquisition equation into owner-only release.",
    "reviewStatus": "Editorial derivation; no compiled witness registered.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Derived from the linked premises under the stated profile; proof sketch is editorial.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/Mutex-exclusive-owner",
    "type": "Theorem",
    "name": "exclusive-owner",
    "statement": "Two holders of the same mutex are the same process.",
    "formalStatement": "holds(o,p) ∧ holds(o,q) ⇒ p=q",
    "assumptions": [
      "Process identity uses equality; P may be empty. Initially unowned. Successful acquire/release steps are atomic; acquire requires no owner, release requires the caller to own the mutex. Self-acquire is disabled; wrong-owner release is undefined. No recursion, timeout, robust-owner recovery, fairness or implicit memory fences. Clients must access the protected critical section only while owning the mutex."
    ],
    "appliesTo": [
      "urn:csabs:concept/Mutex"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Mutex-owner"
    ],
    "proofSketch": "Both holdings identify o with Some(p) and Some(q); injectivity of Some gives p=q.",
    "reviewStatus": "Editorial derivation; no compiled witness registered.",
    "source": [
      "urn:csabs:source/java-lock-contract"
    ],
    "sourceLocator": "Lock: exclusive access, non-reentrant usage, lock/tryLock/unlock and implementation considerations",
    "sourceNote": "Derived from the linked premises under the stated profile; proof sketch is editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
