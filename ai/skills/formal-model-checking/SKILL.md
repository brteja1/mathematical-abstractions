---
name: formal-model-checking
description: Formulate and verify stateful, concurrent, or distributed system specifications against catalog abstractions using automated model checkers (TLA+, PlusCal, Alloy, Z3). Use to find deadlocks, race conditions, and safety violations before or alongside implementation.
---

# Formal model checking from mathematical abstractions

Model and verify concurrent protocols, state machines, and distributed algorithms using formal model checkers. Ground models in the mathematical abstractions catalog to exhaustively check safety, liveness, and structural invariants before writing or approving code.

## Mandatory catalog use

Use catalog abstractions as the mathematical basis for this workflow. Before relying on an abstraction, query it through the repository tooling and record the selected stable concept/operation/claim IDs and their semantic mapping. Names and examples in this skill are search hints, not retrieved evidence; do not substitute remembered or invented definitions or laws.

Retrieve catalog content only through `scripts/catalog.py`, `scripts/agent_query.py`, or `ai/skills/mathematical-tests/scripts/query.py` (and `scripts/lean.py get ID` for binding evidence). Do not directly open, browse, grep, glob, or parse `concepts/`, `data/shared.json`, generated catalog pages, embedded viewer data, or runtime RDF to obtain catalog facts. The tools may read those files internally. Reading instructions, target code, consulted external sources and selected Lean source declarations is separate from catalog retrieval. Direct record edits are allowed only for authorized catalog maintenance or promotion, after tool-based discovery.

If the required abstraction or applicable operation, law or proof cannot be found, **report the gap to the user before acquisition or any further dependent step**: name the need, list queries and closest matches, explain what is missing or incompatible, and identify blocked work. Resolve synonyms, relevant candidates and necessary truncated results first; distinguish unavailable tooling from absent mathematics. Do not silently fall back to general knowledge or continue on unsupported assumptions. Follow the [shared catalog-use policy](../mathematical-tests/references/catalog-use.md) for gap handling and the acquisition exceptions; read it when a gap or retrieval blocker occurs.

## Establish the protocol and concurrency contract

Read the target system's design, protocol specification, state transitions, and concurrency assumptions:

- **State Variables & Domains**: Identify process sets, state enumerations, buffers, queues, counters, and message channels.
- **Atomic Actions**: Determine the exact granularity of state transitions (what steps are atomic vs. interruptible). A step in code that looks like a single line (e.g., `count++`) is typically multiple read-modify-write actions at the model level.
- **Environment & Scheduling Assumptions**: Record fairness constraints (weak vs. strong fairness on actions), network reliability (lossless, reordering, duplicate messages), and failure modes (crash-stop, crash-recovery).
- **Safety vs. Liveness Goals**: Distinguish "nothing bad happens" invariants (e.g., mutual exclusion, no buffer overflow) from "something good eventually happens" temporal progress (e.g., starvation freedom, eventual consistency, deadlock freedom).

Do not assume sequential consistency or atomic execution across multi-statement methods without explicit locking or memory barrier semantics.

## Retrieve applicable catalog abstractions

The catalog dependency is located relative to this skill file's directory: starting from `<skill_dir>` (the directory containing this `SKILL.md`), the catalog root is three levels up at `<skill_dir>/../../..`. This relative structure is preserved whether cloned or extracted from an archive or zip without requiring git.

First verify catalog availability with Python's standard library:

```sh
python3 <skill_dir>/../../../scripts/catalog.py check
```

Retrieve candidate concepts using standard-library commands:

```sh
python3 <skill_dir>/../../../scripts/catalog.py list --search transition
python3 <skill_dir>/../../../scripts/catalog.py get LabelledTransitionSystem --sections operations axioms laws
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

## Fill a required mathematical gap

After reporting a required catalog gap under the mandatory policy above, use [abstraction-acquisition](../abstraction-acquisition/SKILL.md). Search for reusable entries first, acquire or construct only the missing mathematics, and compile/audit the required Lean model and claims. After verification, offer catalog promotion (default) or task-local retention and wait for the user's choice unless already specified. Then resume this workflow with the explicit semantic mapping. Unverified assumptions require an explicit user choice for conditional continuation.

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

Run the model checker with bounded parameters (e.g., 2–3 processes, buffer depth 2–4) and report exactly which model states/interleavings were explored and whether exploration completed:

- **Invariant Violations**: Retain the returned trace from `Init` to the violating state. Claim minimality only if the backend/configuration establishes it. Map model steps to concrete code where correspondence has been justified.
- **Liveness / Cycle Violations**: Retain the backend witness, which may be a prefix followed by a repeating cycle; the cycle need not be stuttering. Inspect progress, enabled actions and the declared fairness assumptions.
- **Deadlock Traces**: Identify why no permitted progress action is enabled; circular waiting is one possible cause, not a required shape.

## Deliver the model-checking report

Deliver a comprehensive report containing:
- **Formal Specification**: The complete TLA+, Alloy, or Z3 model file.
- **Catalog Grounding**: Stable catalog IDs for concepts, axioms, and laws cited.
- **Configuration & Bounds**: Process counts, queue depths, and fairness assumptions tested.
- **Verification Outcomes**: Total distinct states explored, reachable states, and properties verified.
- **Counterexample Traces**: If a property failed, provide the exact sequence of states and interleavings, along with root-cause analysis.
- **Remediation**: Proposed protocol, memory-ordering or locking changes, with the obligations and checks needed before claiming safety or liveness.

Connect with downstream skills:
- Use [implementation-mapping](../implementation-mapping/SKILL.md) to formalize the checked atomic actions into concrete code methods.
- Use [implementation-conformance](../implementation-conformance/SKILL.md) to assess the implementation-to-model correspondence, including atomicity, scheduling and memory ordering. Report unchecked runtime behavior; a model check alone does not verify real thread execution.

## Lifecycle evidence integration

For an authorized end-to-end assurance task, use [spec-driven-development](../spec-driven-development/SKILL.md) and its [shared ledger guide](../spec-driven-development/references/assurance.md). Preserve requirement/obligation IDs, exact inputs and evidence kinds. A model proof, finite test, review receipt and actual-source refinement prove different things; required missing or stale evidence blocks admission. This integration does not expand the user's requested scope.
