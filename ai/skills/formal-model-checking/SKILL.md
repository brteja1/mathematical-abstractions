---
name: formal-model-checking
description: Formulate and verify stateful, concurrent, or distributed system specifications against catalog abstractions using automated model checkers (TLA+, PlusCal, Alloy, Z3). Use to find deadlocks, race conditions, and safety violations before or alongside implementation.
---

# Formal model checking from mathematical abstractions

Model and verify concurrent protocols, state machines, and distributed algorithms using formal model checkers. Ground models in the mathematical abstractions catalog to exhaustively check safety, liveness, and structural invariants before writing or approving code.

## Establish the protocol and concurrency contract

Read the target system's design, protocol specification, state transitions, and concurrency assumptions:

- **State Variables & Domains**: Identify process sets, state enumerations, buffers, queues, counters, and message channels.
- **Atomic Actions**: Determine the exact granularity of state transitions (what steps are atomic vs. interruptible). A step in code that looks like a single line (e.g., `count++`) is typically multiple read-modify-write actions at the model level.
- **Environment & Scheduling Assumptions**: Record fairness constraints (weak vs. strong fairness on actions), network reliability (lossless, reordering, duplicate messages), and failure modes (crash-stop, crash-recovery).
- **Safety vs. Liveness Goals**: Distinguish "nothing bad happens" invariants (e.g., mutual exclusion, no buffer overflow) from "something good eventually happens" temporal progress (e.g., starvation freedom, eventual consistency, deadlock freedom).

Do not assume sequential consistency or atomic execution across multi-statement methods without explicit locking or memory barrier semantics.

## Retrieve applicable catalog abstractions

Resolve `<catalog>` to the checkout containing this skill. Read its `AGENTS.md` and retrieve candidate concepts using standard-library commands or the bounded ONTFS helper:

```sh
python3 <catalog>/scripts/catalog.py list --search transition
python3 <catalog>/scripts/catalog.py get LabelledTransitionSystem --sections operations axioms laws
```

Select concepts based on the system's operational model:

| System Domain | Candidate Catalog Concepts | Key Verification Axioms & Laws |
| --- | --- | --- |
| Mutual exclusion / Locking | `Lock`, `Mutex`, `LamportBakery` | `urn:csabs:axiom/Lock-compatible-holders`<br>`urn:csabs:axiom/Mutex-acquire`<br>`urn:csabs:law/Lock-grant-preserves-compatibility` |
| Stateful transitions / Protocols | `LabelledTransitionSystem`, `KripkeStructure` | Action-labelled transitions, initial states, reachability |
| Temporal properties / Liveness | `LinearTemporalLogic` | Invariance `□P`, eventuality `◇P`, leads-to `P ↝ Q` |
| Shared queues / Buffers | `Queue` | FIFO order (`urn:csabs:law/queue-fifo`), empty guard |
| Distributed state reconciliation | `JoinSemilattice`, `StateBasedCRDT` | Monotonic growth, join commutativity and associativity |

Retrieve focused records for the chosen concept. Use the formal statements and assumptions in the catalog records to formulate the model's transition relations and invariant predicates.

## Select the verification backend

Route by the nature of the verification task:

1. **TLA+ / PlusCal**: Ideal for concurrent protocols, message-passing distributed systems, and temporal logic (LTL) properties involving fairness and deadlock checks.
2. **Alloy**: Ideal for rich relational data structures, object graph invariants, multi-tenant permission models, and structural reachability.
3. **Z3 / SMT-LIB**: Ideal for arithmetic bounds, bitvector constraints, resource scheduling, and bounded unrolling of transition systems.

Read [references/backend-selection.md](references/backend-selection.md) for backend comparison, scoping strategies, and state-explosion mitigations.

## Formulate the model and obligations

Structure the model with explicit state, transitions, and properties:

1. **Initial State (`Init`)**: Specify valid starting conditions for all variables.
2. **Next-State Relation (`Next`)**: Decompose the transition relation into atomic actions:
   $$\text{Next} \triangleq \text{Action}_1 \lor \text{Action}_2 \lor \dots \lor \text{Action}_n$$
3. **Safety Invariants**: Formulate predicates that must hold in every reachable state:
   - Type invariants (`TypeOK`): All state variables stay within declared carrier sets.
   - Domain invariants: E.g., Mutual exclusion:
     $$\forall p, q \in \text{Processes} : (\text{state}[p] = \text{"Critical"} \land \text{state}[q] = \text{"Critical"}) \implies p = q$$
4. **Liveness & Progress Obligations**: Formulate temporal properties under declared fairness:
   - Starvation freedom: $\forall p \in \text{Processes} : (\text{state}[p] = \text{"Waiting"}) \rightsquigarrow (\text{state}[p] = \text{"Critical"})$.
   - Deadlock freedom: At least one non-stuttering action remains enabled while active processes remain.

Read [references/mutex-tla-example.md](references/mutex-tla-example.md) for a worked example modeling a mutual-exclusion protocol with TLA+ and a runnable Python state-space explorer.

## Execute checks and diagnose counterexamples

Run the model checker with bounded parameters (e.g., 2–3 processes, buffer depth 2–4) to avoid combinatorial state explosion while exercising all interleavings:

- **Invariant Violations**: The checker produces a minimal execution trace from `Init` to the violating state. Map each step in the trace back to the concrete code action that caused the invariant breach.
- **Liveness / Cycle Violations**: The checker produces a lasso-shaped trace (a prefix leading to a stuttering loop). Inspect which process was starved and which action failed to take steps under the assumed fairness.
- **Deadlock Traces**: Identify the cycle of dependencies (e.g., circular waiting on locks or channels).

## Deliver the model-checking report

Deliver a comprehensive report containing:
- **Formal Specification**: The complete TLA+, Alloy, or Z3 model file.
- **Catalog Grounding**: Stable catalog IDs for concepts, axioms, and laws cited.
- **Configuration & Bounds**: Process counts, queue depths, and fairness assumptions tested.
- **Verification Outcomes**: Total distinct states explored, reachable states, and properties verified.
- **Counterexample Traces**: If a property failed, provide the exact sequence of states and interleavings, along with root-cause analysis.
- **Remediation**: Recommended protocol adjustments, memory barriers, or locking changes to ensure safety and liveness.

Connect with downstream skills:
- Use [implementation-mapping](../implementation-mapping/SKILL.md) to formalize the checked atomic actions into concrete code methods.
- Use [implementation-conformance](../implementation-conformance/SKILL.md) to verify that real threads or actors do not reorder the validated protocol steps.
