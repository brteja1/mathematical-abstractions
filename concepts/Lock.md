# Lock with compatible access modes

A synchronization contract for one resource, represented by a finite partial map from processes to access modes; distinct holders must have compatible modes.

**Notation:** L(P,M,C)={H:P⇀fin M | ∀p≠q in dom(H), C(H(p),H(q))}; C symmetric.

**Stable ID:** `urn:csabs:concept/Lock`

**Categories:** Concurrency and distributed systems → Synchronization → Locks

**Kind:** Abstract data type

**Prerequisites:** [Map](Map.md), [Binary relation](Relation.md), [Action-labelled transition system with initial states](LabelledTransitionSystem.md)

**Related concepts:** [Happens Before](HappensBefore.md), [Linearizability](Linearizability.md)

## Backlinks

- [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md) — `requiresConcept`
- [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md) — `specializationOf`

## Interface and scope

**axiomBasis:** Compatible-holder invariant, empty initialization, enabled acquisition, owner-only release and exact try-acquire outcomes.

**basisKind:** operational-state-machine-definition

**basisScope:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**basisInstantiation:** Exclusive lock: M={exclusive}, C always false. Shared/exclusive lock: M={read,write}, C(a,b) iff a=b=read. These are parameter instantiations, not inherited axioms.

**verificationObligation:** Map process identity, equality, atomicity and memory visibility to the target model.; A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting.

**reviewStatus:** Editorial specification; model bindings and compiled claim witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-Lock-initial"></a>

### initial

`urn:csabs:operation/Lock-initial`

**signature:** initial : L(P,M,C)

**description:** Create a lock with no holders.

**precondition:** Fixed P,M,C.

**totality:** total on the stated precondition

**postcondition:** initial=∅.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Lock-canAcquire"></a>

### canAcquire

`urn:csabs:operation/Lock-canAcquire`

**signature:** canAcquire : L×P×M→Bool

**description:** Test compatibility with all current holders.

**precondition:** Typed valid state.

**totality:** total on the stated precondition

**postcondition:** canAcquire(H,p,m) ⇔ p∉dom(H) ∧ ∀q∈dom(H), C(m,H(q)).

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Lock-acquire"></a>

### acquire

`urn:csabs:operation/Lock-acquire`

**signature:** acquire : L×P×M ⇀ L

**description:** Complete an acquisition when enabled.

**precondition:** canAcquire(H,p,m).

**totality:** total on the stated precondition

**postcondition:** acquire(H,p,m)=H[p↦m].

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Lock-release"></a>

### release

`urn:csabs:operation/Lock-release`

**signature:** release : L×P ⇀ L

**description:** Release the calling process’s holding.

**precondition:** p∈dom(H).

**totality:** total on the stated precondition

**postcondition:** release(H,p)=H restricted to P∖{p}.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-Lock-tryAcquire"></a>

### tryAcquire

`urn:csabs:operation/Lock-tryAcquire`

**signature:** tryAcquire : L×P×M→L×Bool

**description:** Attempt acquisition without waiting.

**precondition:** Typed valid state.

**totality:** total on the stated precondition

**postcondition:** Returns (H[p↦m],true) iff canAcquire(H,p,m), otherwise (H,false). No spurious failure in this profile.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-Lock-compatible-holders"></a>

### compatible-holders

`urn:csabs:axiom/Lock-compatible-holders`

**statement:** Legal states contain only pairwise compatible distinct holders.

**formalStatement:** H has finite domain; C is symmetric; ∀p≠q∈dom(H), C(H(p),H(q)).

**assumptions:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Lock-grant"></a>

### grant

`urn:csabs:axiom/Lock-grant`

**statement:** Acquisition adds precisely an enabled holding.

**formalStatement:** canAcquire(H,p,m) ⇔ p∉dom(H) ∧ ∀q∈dom(H), C(m,H(q)); dom(acquire)={(H,p,m) | canAcquire(H,p,m)}; acquire(H,p,m)=H[p↦m].

**assumptions:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Lock-release"></a>

### release

`urn:csabs:axiom/Lock-release`

**statement:** Only a holder can release, leaving other holders unchanged.

**formalStatement:** dom(release)={(H,p) | p∈dom(H)}; release(H,p)=H|_(P∖{p}); initial=∅.

**assumptions:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-Lock-try-result"></a>

### try-result

`urn:csabs:axiom/Lock-try-result`

**statement:** Try-acquire returns immediate success exactly when enabled.

**formalStatement:** tryAcquire(H,p,m)=if canAcquire(H,p,m) then (H[p↦m],true) else (H,false).

**assumptions:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-Lock-grant-preserves-compatibility"></a>

### grant-preserves-compatibility

`urn:csabs:law/Lock-grant-preserves-compatibility`

**statement:** An enabled grant preserves the compatible-holder invariant.

**formalStatement:** H∈L ∧ canAcquire(H,p,m) ⇒ H[p↦m]∈L

**assumptions:** Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.

**dependsOn:** [compatible-holders](Lock.md#node-urn-csabs-axiom-Lock-compatible-holders); [grant](Lock.md#node-urn-csabs-axiom-Lock-grant)

**proofSketch:** Existing holder pairs remain compatible. New pairs use the grant guard and symmetry of C; adding one element preserves finite support.

**reviewStatus:** Editorial derivation; no compiled witness registered.

**source:** [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract; [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Derived from the linked premises under the stated profile; proof sketch is editorial.

**provenanceKind:** derived

## Theorems

No entries recorded. This does not assert absence of mathematical facts.

## Concept provenance

- [Java SE 25 Lock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/Lock.html); accessedOn: 2026-11-08; sourceRole: interface-contract
- [Java SE 25 ReadWriteLock interface](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReadWriteLock.html); accessedOn: 2026-11-08; sourceRole: shared-exclusive-mode-and-policy-reference

**sourceLocator:** Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices

**sourceNote:** Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/Lock",
    "type": "Concept",
    "shortForm": "Lock",
    "fullName": "Lock with compatible access modes",
    "definition": "A synchronization contract for one resource, represented by a finite partial map from processes to access modes; distinct holders must have compatible modes.",
    "notation": "L(P,M,C)={H:P⇀fin M | ∀p≠q in dom(H), C(H(p),H(q))}; C symmetric.",
    "category": [
      "urn:csabs:category/locks"
    ],
    "kind": "urn:csabs:kind/abstract-data-type",
    "requiresConcept": [
      "urn:csabs:concept/Map",
      "urn:csabs:concept/Relation",
      "urn:csabs:concept/LabelledTransitionSystem"
    ],
    "relatedConcept": [
      "urn:csabs:concept/HappensBefore",
      "urn:csabs:concept/Linearizability"
    ],
    "axiomBasis": "Compatible-holder invariant, empty initialization, enabled acquisition, owner-only release and exact try-acquire outcomes.",
    "basisKind": "operational-state-machine-definition",
    "basisScope": "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; model bindings and compiled claim witnesses are separate.",
    "verificationObligation": [
      "Map process identity, equality, atomicity and memory visibility to the target model.",
      "A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting."
    ],
    "hasOperation": [
      "urn:csabs:operation/Lock-initial",
      "urn:csabs:operation/Lock-canAcquire",
      "urn:csabs:operation/Lock-acquire",
      "urn:csabs:operation/Lock-release",
      "urn:csabs:operation/Lock-tryAcquire"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/Lock-compatible-holders",
      "urn:csabs:axiom/Lock-grant",
      "urn:csabs:axiom/Lock-release",
      "urn:csabs:axiom/Lock-try-result"
    ],
    "hasLaw": [
      "urn:csabs:law/Lock-grant-preserves-compatibility"
    ],
    "hasTheorem": [],
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted",
    "basisInstantiation": "Exclusive lock: M={exclusive}, C always false. Shared/exclusive lock: M={read,write}, C(a,b) iff a=b=read. These are parameter instantiations, not inherited axioms."
  },
  {
    "id": "urn:csabs:operation/Lock-initial",
    "type": "Operation",
    "name": "initial",
    "signature": "initial : L(P,M,C)",
    "description": "Create a lock with no holders.",
    "precondition": "Fixed P,M,C.",
    "totality": "total on the stated precondition",
    "postcondition": "initial=∅.",
    "concept": "urn:csabs:concept/Lock",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Lock-canAcquire",
    "type": "Operation",
    "name": "canAcquire",
    "signature": "canAcquire : L×P×M→Bool",
    "description": "Test compatibility with all current holders.",
    "precondition": "Typed valid state.",
    "totality": "total on the stated precondition",
    "postcondition": "canAcquire(H,p,m) ⇔ p∉dom(H) ∧ ∀q∈dom(H), C(m,H(q)).",
    "concept": "urn:csabs:concept/Lock",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Lock-acquire",
    "type": "Operation",
    "name": "acquire",
    "signature": "acquire : L×P×M ⇀ L",
    "description": "Complete an acquisition when enabled.",
    "precondition": "canAcquire(H,p,m).",
    "totality": "total on the stated precondition",
    "postcondition": "acquire(H,p,m)=H[p↦m].",
    "concept": "urn:csabs:concept/Lock",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Lock-release",
    "type": "Operation",
    "name": "release",
    "signature": "release : L×P ⇀ L",
    "description": "Release the calling process’s holding.",
    "precondition": "p∈dom(H).",
    "totality": "total on the stated precondition",
    "postcondition": "release(H,p)=H restricted to P∖{p}.",
    "concept": "urn:csabs:concept/Lock",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/Lock-tryAcquire",
    "type": "Operation",
    "name": "tryAcquire",
    "signature": "tryAcquire : L×P×M→L×Bool",
    "description": "Attempt acquisition without waiting.",
    "precondition": "Typed valid state.",
    "totality": "total on the stated precondition",
    "postcondition": "Returns (H[p↦m],true) iff canAcquire(H,p,m), otherwise (H,false). No spurious failure in this profile.",
    "concept": "urn:csabs:concept/Lock",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Lock-compatible-holders",
    "type": "Axiom",
    "name": "compatible-holders",
    "statement": "Legal states contain only pairwise compatible distinct holders.",
    "formalStatement": "H has finite domain; C is symmetric; ∀p≠q∈dom(H), C(H(p),H(q)).",
    "assumptions": [
      "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lock"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Lock-grant",
    "type": "Axiom",
    "name": "grant",
    "statement": "Acquisition adds precisely an enabled holding.",
    "formalStatement": "canAcquire(H,p,m) ⇔ p∉dom(H) ∧ ∀q∈dom(H), C(m,H(q)); dom(acquire)={(H,p,m) | canAcquire(H,p,m)}; acquire(H,p,m)=H[p↦m].",
    "assumptions": [
      "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lock"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Lock-release",
    "type": "Axiom",
    "name": "release",
    "statement": "Only a holder can release, leaving other holders unchanged.",
    "formalStatement": "dom(release)={(H,p) | p∈dom(H)}; release(H,p)=H|_(P∖{p}); initial=∅.",
    "assumptions": [
      "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lock"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/Lock-try-result",
    "type": "Axiom",
    "name": "try-result",
    "statement": "Try-acquire returns immediate success exactly when enabled.",
    "formalStatement": "tryAcquire(H,p,m)=if canAcquire(H,p,m) then (H[p↦m],true) else (H,false).",
    "assumptions": [
      "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lock"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Catalog abstraction of ownership and symmetric mode compatibility, with one holding per process. Java supplies interface examples; this is not the complete Java memory or exception contract.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/Lock-grant-preserves-compatibility",
    "type": "Law",
    "name": "grant-preserves-compatibility",
    "statement": "An enabled grant preserves the compatible-holder invariant.",
    "formalStatement": "H∈L ∧ canAcquire(H,p,m) ⇒ H[p↦m]∈L",
    "assumptions": [
      "Process identities and modes use equality. Empty P and empty M are allowed. Fixed symmetric compatibility relation C; one holding per process, without recursion, conversion or upgrade. Atomic state transitions describe completed grants and releases. An unavailable blocking acquire has no completed transition; waiting queues and scheduling are outside this state. No automatic fairness, timeout, crash recovery or memory-visibility contract."
    ],
    "appliesTo": [
      "urn:csabs:concept/Lock"
    ],
    "dependsOn": [
      "urn:csabs:axiom/Lock-compatible-holders",
      "urn:csabs:axiom/Lock-grant"
    ],
    "proofSketch": "Existing holder pairs remain compatible. New pairs use the grant guard and symmetry of C; adding one element preserves finite support.",
    "reviewStatus": "Editorial derivation; no compiled witness registered.",
    "source": [
      "urn:csabs:source/java-lock-contract",
      "urn:csabs:source/java-rwlock-contract"
    ],
    "sourceLocator": "Lock: class description, lock, tryLock, unlock; ReadWriteLock: description and policy choices",
    "sourceNote": "Derived from the linked premises under the stated profile; proof sketch is editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
