# Model Checking Backend Selection Guide

This guide helps agents choose the appropriate formal verification engine, configure model scopes, and manage state-space explosion when verifying systems against catalog abstractions.

---

## Backend Comparison Matrix

| Verification Engine | Primary Strength | Best For | Typical Catalog Concepts |
| :--- | :--- | :--- | :--- |
| **TLA+ / PlusCal** | Interleaving concurrency & temporal progress | Distributed protocols, consensus, locking, race conditions, deadlock freedom | `urn:csabs:concept/Lock`<br>`urn:csabs:concept/Mutex`<br>`urn:csabs:concept/LamportBakery`<br>`urn:csabs:concept/LinearTemporalLogic` |
| **Alloy** | Relational structures & multi-entity constraints | Object graph invariants, role-based access control (RBAC), database schemas, pointer structures | `urn:csabs:concept/Relation`<br>`urn:csabs:concept/Partition`<br>`urn:csabs:concept/PropertyGraph` |
| **Z3 / SMT-LIB** | Decidable theories & arithmetic optimization | Numeric bounds, bitvector manipulation, buffer sizing, bounded model unrolling | `urn:csabs:concept/ModularInteger`<br>`urn:csabs:concept/RealNumber`<br>`urn:csabs:concept/MinPlusSemiring` |

---

## 1. TLA+ & PlusCal

TLA+ (Temporal Logic of Actions) models systems as discrete state transitions. PlusCal is a pseudo-code algorithm language that translates directly into TLA+.

### When to Choose TLA+
* The problem involves **interleaved concurrent execution** across multiple processes or threads.
* You need to verify **temporal liveness properties** such as:
  * Starvation freedom: A process requesting a resource eventually acquires it ($P \rightsquigarrow Q$).
  * Eventual consistency: Replicas eventually agree on state after quiescent periods.
* You need an automated exhaustive trace explorer (TLC) that delivers exact line-by-line counterexample states.

### Key Considerations
* **Fairness:** Specify Weak Fairness ($WF_v(A)$) or Strong Fairness ($SF_v(A)$) on actions. Without fairness assumptions, TLC will find trivial "stuttering" counterexamples where a thread simply stops taking steps.
* **Granularity of Actions:** In PlusCal, each label defines an atomic step. Placing multiple reads and writes under a single label hides potential race conditions that exist in real CPU/memory architectures.

---

## 2. Alloy

Alloy is based on first-order relational logic with transitive closure, solved via boolean satisfiability (SAT / Kodkod).

### When to Choose Alloy
* The problem involves **structural relationships**, graph topologies, or pointer networks (e.g., file system structures, DAG invariants, multi-tenant isolation).
* You want to verify that an invariant holds across all possible structural shapes within a small bounded scope.
* Dynamic execution can be modeled as ordering relations between events or clock ticks.

### Key Considerations
* **Small Scope Hypothesis:** If a relational assertion has a counterexample, it almost always has a small counterexample (e.g., $\le 3$ to $5$ nodes per signature).
* **Transitive Closure:** Alloy's `^` (transitive closure) and `*` (reflexive transitive closure) make reachability and acyclicity checks straightforward.

---

## 3. Z3 & SMT-LIB

Z3 is an efficient Satisfiability Modulo Theories (SMT) solver supporting arithmetic, bitvectors, arrays, and uninterpreted functions.

### When to Choose Z3
* The system involves **numeric invariants, bounded integer calculations, bitwise operations, or resource allocation limits**.
* You need **bounded model checking (BMC)**: unrolling a transition system $k$ steps ($I(s_0) \land T(s_0, s_1) \land \dots \land T(s_{k-1}, s_k) \land \neg P(s_k)$) to find reachability violations.
* The system can be expressed as a constraint satisfaction problem.

---

## Managing State-Space Explosion

Exhaustive model checking faces exponential state-space growth with increasing variables and processes. Apply these techniques:

1. **Minimize Process Count:** Start checking with 2 processes, then expand to 3. Two processes expose most race conditions; three expose complex multi-party deadlocks and token passing issues.
2. **Use Symmetry Sets in TLC:**
   In TLA+, declare process sets as symmetric:
   ```tla
   SYMMETRIC Permutations(Processes)
   ```
   TLC prunes isomorphic states where process IDs are merely permuted, reducing the state space by up to $N!$.
3. **Data Abstraction:** Replace continuous variables or unbounded counters with finite equivalence classes. For example, instead of tracking exact queue contents, track `QueueState \in {"Empty", "Single", "Full"}`.
4. **Constrain Message Channels:** Restrict message buffers to small finite bounds (e.g., capacity 2 or 3) and unroll loops with small step bounds.
