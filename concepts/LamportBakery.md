# Lamport bakery lock protocol

A shared-memory mutual-exclusion protocol in which each process announces ticket selection, chooses a natural-number ticket and waits using lexicographic ticket/process priority.

**Notation:** P=Fin(N); choosing:P→Bool; number:P→ℕ; priority(i)=(number(i),i); pc and local scan state per process.

**Stable ID:** `urn:csabs:concept/LamportBakery`

**Categories:** Concurrency and distributed systems → Synchronization → Lock protocols

**Kind:** semantic-model

**Prerequisites:** [Action-labelled transition system with initial states](LabelledTransitionSystem.md), [Natural Number](NaturalNumber.md), [Total Order](TotalOrder.md), [Mutex (non-reentrant mutual-exclusion lock)](Mutex.md)

**Related concepts:** [Safety Property](SafetyProperty.md), [Liveness Property](LivenessProperty.md), [Sequential Consistency](SequentialConsistency.md)

## Interface and scope

**axiomBasis:** Explicit doorway, ticket scan, publication, ordered wait loop, critical-section entry and ticket-zero exit; reachable executions from zero initialization.

**basisKind:** operational-state-machine-definition

**basisScope:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**basisInstantiation:** This protocol is related to the Mutex contract rather than a structural specialization of its Option(P) carrier. A complete implementation refinement must map doorway/wait steps to internal actions and define ownership between successful entry and release; critical-section exclusion alone is not a full linearizability or memory-visibility proof.

**verificationObligation:** Map process identity, equality, atomicity and memory visibility to the target model.; A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting.; Keep the choosing handshake; selecting the minimum ticket without it is a different protocol.; Do not infer liveness from exclusion. For eventual entry, state fair scheduling, terminating doorway/exit and finite critical sections explicitly.; Lamport’s 1974 bakery algorithm is distinct from his fast mutual-exclusion and message-passing timestamp algorithms.

**reviewStatus:** Editorial specification; model bindings and compiled claim witnesses are separate.

**coverageStatus:** basis-reviewed

## Operations

<a id="node-urn-csabs-operation-LamportBakery-doorway"></a>

### doorway

`urn:csabs:operation/LamportBakery-doorway`

**signature:** doorway_i ⊆ State×State (multi-step protocol relation)

**description:** Announce selection, scan all ticket registers and publish a positive ticket.

**precondition:** i is outside with number[i]=0.

**totality:** Each read/write is a separate enabled transition; doorway is not one atomic operation.

**postcondition:** Set choosing[i]=true; read every number[j] into local scan data; set number[i]=1+max(observed tickets); set choosing[i]=false, in that program order.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LamportBakery-wait"></a>

### wait

`urn:csabs:operation/LamportBakery-wait`

**signature:** wait_i ⊆ State×State (guarded protocol-step relation)

**description:** Check each process in ID order.

**precondition:** i has published its current ticket.

**totality:** Reads and control steps are separate transitions; waiting may persist indefinitely.

**postcondition:** For each j≠i, first wait for choosing[j]=false; then wait until number[j]=0 or (number[i],i)<lex(number[j],j); advance only after both stages.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LamportBakery-enter"></a>

### enter

`urn:csabs:operation/LamportBakery-enter`

**signature:** enter_i : State ⇀ State

**description:** Move into the critical section.

**precondition:** i has completed both wait stages for every process in this attempt.

**totality:** total on the stated precondition

**postcondition:** pc[i]=critical; number[i] remains positive and unchanged.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-operation-LamportBakery-exit"></a>

### exit

`urn:csabs:operation/LamportBakery-exit`

**signature:** exit_i : State ⇀ State

**description:** Complete the critical section and relinquish the ticket.

**precondition:** pc[i]=critical or the subsequent exit phase.

**totality:** total on the stated precondition

**postcondition:** Write number[i]=0 before returning outside; choosing[i] is false.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

## Axioms and defining rules

<a id="node-urn-csabs-axiom-LamportBakery-memory-initialization"></a>

### memory-initialization

`urn:csabs:axiom/LamportBakery-memory-initialization`

**statement:** Executions start at zero and interleave the stated owner-written atomic register operations.

**formalStatement:** N∈ℕ; choosing[i]=false and number[i]=0 initially; pc[i]=outside; SC atomic reads/writes; only i writes slot i; all steps follow the protocol.

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LamportBakery-doorway"></a>

### doorway

`urn:csabs:axiom/LamportBakery-doorway`

**statement:** Ticket selection is enclosed by the choosing flag and uses individually read ticket values.

**formalStatement:** outside→choosing[i]:=true→read number[0..N−1] individually→number[i]:=1+max(local reads)→choosing[i]:=false→wait; max(∅)=0.

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LamportBakery-wait-entry"></a>

### wait-entry

`urn:csabs:axiom/LamportBakery-wait-entry`

**statement:** A process enters only after its per-process two-stage waits.

**formalStatement:** For each j≠i in ID order: await choosing[j]=false; then await number[j]=0 ∨ (number[i],i)<lex(number[j],j); after the final j, enter critical.

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

<a id="node-urn-csabs-axiom-LamportBakery-ticket-stability-exit"></a>

### ticket-stability-exit

`urn:csabs:axiom/LamportBakery-ticket-stability-exit`

**statement:** A published ticket stays fixed until release and is cleared before another attempt.

**formalStatement:** From choosing[i]:=false through critical, number[i]>0 is unchanged; after critical set number[i]:=0 then return outside; no overlapping attempts by the same process.

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**ruleRole:** defining-rule

**reviewStatus:** Editorial defining requirement; not a machine-checked theorem.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

## Laws

<a id="node-urn-csabs-law-LamportBakery-critical-ticket-order"></a>

### critical-ticket-order

`urn:csabs:law/LamportBakery-critical-ticket-order`

**statement:** A process in the critical section precedes every other process with a published active ticket.

**formalStatement:** For reachable s: pc[i]=critical ∧ j≠i ∧ j is in bakery ⇒ (number[i],i)<lex(number[j],j); in bakery means from clearing choosing after publication until starting ticket-zero exit.

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**dependsOn:** [memory-initialization](LamportBakery.md#node-urn-csabs-axiom-LamportBakery-memory-initialization); [doorway](LamportBakery.md#node-urn-csabs-axiom-LamportBakery-doorway); [wait-entry](LamportBakery.md#node-urn-csabs-axiom-LamportBakery-wait-entry); [ticket-stability-exit](LamportBakery.md#node-urn-csabs-axiom-LamportBakery-ticket-stability-exit)

**proofSketch:** Follow source Assertion 2. Consider i’s successful choosing[j] read. If j’s current doorway starts later, i’s stable ticket is among j’s scan reads, so j gets a larger ticket. Otherwise j finished publishing before that choosing read; i’s subsequent successful ticket test establishes lexicographic priority. The choosing handshake rules out a partially published current ticket.

**reviewStatus:** Editorial derivation; no compiled witness registered.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Derived from the linked premises under the stated profile; proof sketch is editorial.

**provenanceKind:** derived

## Theorems

<a id="node-urn-csabs-theorem-LamportBakery-mutual-exclusion"></a>

### mutual-exclusion

`urn:csabs:theorem/LamportBakery-mutual-exclusion`

**statement:** Reachable executions contain at most one process in the critical section.

**formalStatement:** Reachable(s) ∧ pc[i]=critical ∧ pc[j]=critical ⇒ i=j

**assumptions:** Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.

**dependsOn:** [critical-ticket-order](LamportBakery.md#node-urn-csabs-law-LamportBakery-critical-ticket-order)

**proofSketch:** If i≠j, each is in the bakery, so the priority law gives both priority(i)<priority(j) and priority(j)<priority(i), contradicting the strict lexicographic order.

**reviewStatus:** Editorial derivation; no compiled witness registered.

**source:** [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Derived from the linked premises under the stated profile; proof sketch is editorial.

**provenanceKind:** derived

## Concept provenance

- [Leslie Lamport: A New Solution of Dijkstra’s Concurrent Programming Problem (1974)](https://lamport.azurewebsites.net/pubs/bakery.pdf); accessedOn: 2026-11-08; sourceRole: algorithm-and-correctness-proof

**sourceLocator:** pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks

**sourceNote:** Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.

**provenanceKind:** adapted

## Structured record

Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.

<!-- graph-record:start -->
```json
[
  {
    "id": "urn:csabs:concept/LamportBakery",
    "type": "Concept",
    "shortForm": "LamportBakery",
    "fullName": "Lamport bakery lock protocol",
    "definition": "A shared-memory mutual-exclusion protocol in which each process announces ticket selection, chooses a natural-number ticket and waits using lexicographic ticket/process priority.",
    "notation": "P=Fin(N); choosing:P→Bool; number:P→ℕ; priority(i)=(number(i),i); pc and local scan state per process.",
    "category": [
      "urn:csabs:category/lock-protocols"
    ],
    "kind": "urn:csabs:kind/semantic-model",
    "requiresConcept": [
      "urn:csabs:concept/LabelledTransitionSystem",
      "urn:csabs:concept/NaturalNumber",
      "urn:csabs:concept/TotalOrder",
      "urn:csabs:concept/Mutex"
    ],
    "relatedConcept": [
      "urn:csabs:concept/SafetyProperty",
      "urn:csabs:concept/LivenessProperty",
      "urn:csabs:concept/SequentialConsistency"
    ],
    "axiomBasis": "Explicit doorway, ticket scan, publication, ordered wait loop, critical-section entry and ticket-zero exit; reachable executions from zero initialization.",
    "basisKind": "operational-state-machine-definition",
    "basisScope": "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound.",
    "coverageStatus": "basis-reviewed",
    "reviewStatus": "Editorial specification; model bindings and compiled claim witnesses are separate.",
    "verificationObligation": [
      "Map process identity, equality, atomicity and memory visibility to the target model.",
      "A state invariant does not imply deadlock freedom, starvation freedom or bounded waiting.",
      "Keep the choosing handshake; selecting the minimum ticket without it is a different protocol.",
      "Do not infer liveness from exclusion. For eventual entry, state fair scheduling, terminating doorway/exit and finite critical sections explicitly.",
      "Lamport’s 1974 bakery algorithm is distinct from his fast mutual-exclusion and message-passing timestamp algorithms."
    ],
    "hasOperation": [
      "urn:csabs:operation/LamportBakery-doorway",
      "urn:csabs:operation/LamportBakery-wait",
      "urn:csabs:operation/LamportBakery-enter",
      "urn:csabs:operation/LamportBakery-exit"
    ],
    "hasAxiom": [
      "urn:csabs:axiom/LamportBakery-memory-initialization",
      "urn:csabs:axiom/LamportBakery-doorway",
      "urn:csabs:axiom/LamportBakery-wait-entry",
      "urn:csabs:axiom/LamportBakery-ticket-stability-exit"
    ],
    "hasLaw": [
      "urn:csabs:law/LamportBakery-critical-ticket-order"
    ],
    "hasTheorem": [
      "urn:csabs:theorem/LamportBakery-mutual-exclusion"
    ],
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted",
    "basisInstantiation": "This protocol is related to the Mutex contract rather than a structural specialization of its Option(P) carrier. A complete implementation refinement must map doorway/wait steps to internal actions and define ownership between successful entry and release; critical-section exclusion alone is not a full linearizability or memory-visibility proof."
  },
  {
    "id": "urn:csabs:operation/LamportBakery-doorway",
    "type": "Operation",
    "name": "doorway",
    "signature": "doorway_i ⊆ State×State (multi-step protocol relation)",
    "description": "Announce selection, scan all ticket registers and publish a positive ticket.",
    "precondition": "i is outside with number[i]=0.",
    "totality": "Each read/write is a separate enabled transition; doorway is not one atomic operation.",
    "postcondition": "Set choosing[i]=true; read every number[j] into local scan data; set number[i]=1+max(observed tickets); set choosing[i]=false, in that program order.",
    "concept": "urn:csabs:concept/LamportBakery",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LamportBakery-wait",
    "type": "Operation",
    "name": "wait",
    "signature": "wait_i ⊆ State×State (guarded protocol-step relation)",
    "description": "Check each process in ID order.",
    "precondition": "i has published its current ticket.",
    "totality": "Reads and control steps are separate transitions; waiting may persist indefinitely.",
    "postcondition": "For each j≠i, first wait for choosing[j]=false; then wait until number[j]=0 or (number[i],i)<lex(number[j],j); advance only after both stages.",
    "concept": "urn:csabs:concept/LamportBakery",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LamportBakery-enter",
    "type": "Operation",
    "name": "enter",
    "signature": "enter_i : State ⇀ State",
    "description": "Move into the critical section.",
    "precondition": "i has completed both wait stages for every process in this attempt.",
    "totality": "total on the stated precondition",
    "postcondition": "pc[i]=critical; number[i] remains positive and unchanged.",
    "concept": "urn:csabs:concept/LamportBakery",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:operation/LamportBakery-exit",
    "type": "Operation",
    "name": "exit",
    "signature": "exit_i : State ⇀ State",
    "description": "Complete the critical section and relinquish the ticket.",
    "precondition": "pc[i]=critical or the subsequent exit phase.",
    "totality": "total on the stated precondition",
    "postcondition": "Write number[i]=0 before returning outside; choosing[i] is false.",
    "concept": "urn:csabs:concept/LamportBakery",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LamportBakery-memory-initialization",
    "type": "Axiom",
    "name": "memory-initialization",
    "statement": "Executions start at zero and interleave the stated owner-written atomic register operations.",
    "formalStatement": "N∈ℕ; choosing[i]=false and number[i]=0 initially; pc[i]=outside; SC atomic reads/writes; only i writes slot i; all steps follow the protocol.",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LamportBakery-doorway",
    "type": "Axiom",
    "name": "doorway",
    "statement": "Ticket selection is enclosed by the choosing flag and uses individually read ticket values.",
    "formalStatement": "outside→choosing[i]:=true→read number[0..N−1] individually→number[i]:=1+max(local reads)→choosing[i]:=false→wait; max(∅)=0.",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LamportBakery-wait-entry",
    "type": "Axiom",
    "name": "wait-entry",
    "statement": "A process enters only after its per-process two-stage waits.",
    "formalStatement": "For each j≠i in ID order: await choosing[j]=false; then await number[j]=0 ∨ (number[i],i)<lex(number[j],j); after the final j, enter critical.",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:axiom/LamportBakery-ticket-stability-exit",
    "type": "Axiom",
    "name": "ticket-stability-exit",
    "statement": "A published ticket stays fixed until release and is cleared before another attempt.",
    "formalStatement": "From choosing[i]:=false through critical, number[i]>0 is unchanged; after critical set number[i]:=0 then return outside; no overlapping attempts by the same process.",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "ruleRole": "defining-rule",
    "reviewStatus": "Editorial defining requirement; not a machine-checked theorem.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Failure-free sequentially consistent atomic-register restriction of the source algorithm. Max scans read locations individually; this entry does not assert the original stronger overlapping-read or failure-recovery guarantee.",
    "provenanceKind": "adapted"
  },
  {
    "id": "urn:csabs:law/LamportBakery-critical-ticket-order",
    "type": "Law",
    "name": "critical-ticket-order",
    "statement": "A process in the critical section precedes every other process with a published active ticket.",
    "formalStatement": "For reachable s: pc[i]=critical ∧ j≠i ∧ j is in bakery ⇒ (number[i],i)<lex(number[j],j); in bakery means from clearing choosing after publication until starting ticket-zero exit.",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "dependsOn": [
      "urn:csabs:axiom/LamportBakery-memory-initialization",
      "urn:csabs:axiom/LamportBakery-doorway",
      "urn:csabs:axiom/LamportBakery-wait-entry",
      "urn:csabs:axiom/LamportBakery-ticket-stability-exit"
    ],
    "proofSketch": "Follow source Assertion 2. Consider i’s successful choosing[j] read. If j’s current doorway starts later, i’s stable ticket is among j’s scan reads, so j gets a larger ticket. Otherwise j finished publishing before that choosing read; i’s subsequent successful ticket test establishes lexicographic priority. The choosing handshake rules out a partially published current ticket.",
    "reviewStatus": "Editorial derivation; no compiled witness registered.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Derived from the linked premises under the stated profile; proof sketch is editorial.",
    "provenanceKind": "derived"
  },
  {
    "id": "urn:csabs:theorem/LamportBakery-mutual-exclusion",
    "type": "Theorem",
    "name": "mutual-exclusion",
    "statement": "Reachable executions contain at most one process in the critical section.",
    "formalStatement": "Reachable(s) ∧ pc[i]=critical ∧ pc[j]=critical ⇒ i=j",
    "assumptions": [
      "Fixed finite N, including N=0; unique ordered process IDs. Initially all flags false, tickets zero and processes outside. Only process i writes choosing[i] and number[i]. Each register read/write is atomic and sequentially consistent; max is a sequence of reads, not an atomic snapshot. Tickets use unbounded naturals. Processes do not crash or cancel; tickets stay fixed from publication through the critical section. Control states and local scan results are part of state, and equality includes them. Safety needs no scheduling fairness. Progress additionally needs scheduling/finite-section hypotheses. No claim about plain non-atomic C/C++ accesses or bounded-ticket wraparound."
    ],
    "appliesTo": [
      "urn:csabs:concept/LamportBakery"
    ],
    "dependsOn": [
      "urn:csabs:law/LamportBakery-critical-ticket-order"
    ],
    "proofSketch": "If i≠j, each is in the bakery, so the priority law gives both priority(i)<priority(j) and priority(j)<priority(i), contradicting the strict lexicographic order.",
    "reviewStatus": "Editorial derivation; no compiled witness registered.",
    "source": [
      "urn:csabs:source/lamport-bakery-1974"
    ],
    "sourceLocator": "pp. 454–455: The Algorithm (L1–L3), Proof of Correctness Assertions 1–3, Further Remarks",
    "sourceNote": "Derived from the linked premises under the stated profile; proof sketch is editorial.",
    "provenanceKind": "derived"
  }
]
```
<!-- graph-record:end -->
