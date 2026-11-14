# Coroutines and cooperative execution

The catalog now has two complementary models:

- [AsymmetricCoroutine](../concepts/AsymmetricCoroutine.md) models one
  computation and a fixed direct caller, including saved continuation state,
  input on resume, yielded output, normal return and uncaught failure.
- [CooperativeScheduler](../concepts/CooperativeScheduler.md) composes a fixed
  finite pool of these computations on one logical thread, with explicit
  dispatch, waiting and wakeup.

Both specialize [LabelledTransitionSystem](../concepts/LabelledTransitionSystem.md)
using explicit state, action and initial-state instantiations. The scheduler
requires coroutine models; it is not itself a subtype of one coroutine.
The subject category is **Programming-language semantics → Coroutines and
cooperative execution**, with additional membership in concurrency's behavioral
models. Category membership does not transfer axioms.

## Single-coroutine lifecycle

The continuation carrier `K` includes all retained local data and control state.
It may encode a stack, but the model does not select a stackful or stackless
representation. `I`, `O`, `R` and `E` are distinct input, yield, return and error
carriers. Even if their concrete representations coincide, their event tags
do not. Equality preserves phase and payload.

| Phase | Permitted next action | Next phase |
| --- | --- | --- |
| Created | `Resume(input)` | Running with input incorporated into the entry state |
| Suspended | `Resume(input)` | Running with input incorporated into the saved state |
| Running | `Internal` | Running |
| Running | `Yield(output)` | Suspended with the chosen saved continuation |
| Running | `Return(result)` | Returned |
| Running | `Raise(error)` | Failed |
| Returned / Failed | None in this lifecycle relation | No successor |

Creation is dormant. A yield transfers control back to the direct caller;
resuming a Running coroutine has no successor. An invalid action is not a
successful lifecycle step; runtime-specific error responses need an adapter.
The general body relations may be nondeterministic, stuck or internally
divergent. Nothing requires a running computation to reach a yield.

`resumeOutcomes` collects **finite** segments of the form
`Resume(input) · Internal* · Boundary`, where `Boundary` is a yield, return or
failure. It specifies allowed observations, not a terminating implementation
of `resume`. An empty outcome set does not distinguish invalid resume,
deadlock and divergence. An outcome may coexist with an infinite alternative.
Internal labels are retained in the parent LTS; no weak equivalence or hiding
is silently introduced.

## Pool scheduling and waiting

The scheduler stores a task-state map `c`, an optional active owner and a
waiting set `W`. Initially all tasks are Created, the owner is absent and `W`
is empty. The task type is finite; an empty pool is permitted.

An idle scheduler may dispatch any nonwaiting Created or Suspended task.
The selected task alone takes body steps until it releases the owner slot:

- `Yield(output)` suspends it and leaves it immediately eligible for dispatch.
- `Wait(output)` suspends it and adds it to `W`.
- `Return(result)` or `Raise(error)` records a terminal state.

`Wake(task)` removes a task from `W`; it does not resume the task. Wake can
arrive while another task is active and does not preempt that task. A later
dispatch supplies the resumed input. There is no implicit input mailbox.
The adapter chooses whether a local yield denotes Yield or Wait; this
classification is part of the scheduler interface, not inferred from a value.

For example, with two initially dormant tasks, this is an allowed shape of
trace if their supplied body relations support the matching local events:

```text
Dispatch(A, start)
Wait(read-request)        # A is suspended and waiting; owner becomes idle
Dispatch(B, start)
Internal                 # only B advances
Wake(A)                  # A becomes eligible; B still owns execution
Yield(b-output)           # B suspends; owner becomes idle
Dispatch(A, read-result)  # A receives the completed input
Return(a-result)
```

Dispatching A before Wake(A), or dispatching A while B is still active, is
disabled. The recorded invariant theorem derives the single-owner property
and suspended waiting states by induction over finite executions. Its registered
Lean witness proves this invariant for the supplied operational model, with
explicit premise mappings and separately checked compiler evidence.

The scheduler has no fairness axiom. If B can keep taking an internal
self-loop, a ready A can remain unexecuted forever. Even a fair dispatch
policy cannot preempt such an active B under these rules. Progress requires
additional assumptions about body handoffs and scheduling; a wakeup also
needs an external event-delivery assumption. An all-waiting pool need not
ever receive one.

## Runtime and nearby-concept mappings

| Target | Required interpretation / remaining work |
| --- | --- |
| Lua coroutines | First resume may pass arguments to the body; later inputs become yield results. Tuple-valued carriers can model multiple arguments. Nested coroutine callers, non-yieldable C boundaries, close and cleanup are omitted. |
| Python generator coroutines | Map a generator's saved execution state to K. Creation needs `next()` or `send(None)` priming; arbitrary initial input in the general model needs a wrapper. Invalid reentry raises a Python exception instead of taking a lifecycle step. Map yielded values, `StopIteration.value` and uncaught exceptions separately. |
| Python pull generators | A unit input can model `next()`. An adapter may answer repeated exhaustion queries without creating a new body transition. Effectful, infinite or failing generators are not the catalog's pure finite sequence cursor. |
| asyncio-style tasks | Map actual suspension to Wait and completion delivery to Wake, then dispatch. A syntactic `await` can complete immediately and need not yield to another task. The fixed-pool model omits event readiness storage, future identity, cancellation and dynamic tasks. |
| FiniteIterator | Its fixed finite sequence and cursor give a different carrier and equality. A coroutine needs separate purity, finiteness and observation mappings before using iterator properties. It is related, not automatically a specialization. |
| Mutex / HappensBefore | These express access or ordering constraints. Cooperative ownership alone neither supplies a memory model nor makes logical operations spanning suspension atomic. |

The chosen profile omits cancellation, exception injection, cleanup/finalizers,
delegation (`yield from`), symmetric coroutine transfer, nested resume stacks,
dynamic tasks, shared mutable memory and parallel execution. Each needs
explicit state and rules rather than an assumed interpretation of these models.

## Sources and Lean evidence

The structured records link directly to the consulted
[Lua 5.4 reference, §§2.6 and 6.2](https://www.lua.org/manual/5.4/manual.html#2.6),
[Python 3.13 yield and generator methods, §6.2.9](https://docs.python.org/3.13/reference/expressions.html#yield-expressions),
and [Python 3.13 cooperative Task documentation](https://docs.python.org/3.13/library/asyncio-task.html#task-object).
Consultation date: 2026-11-14. The entries are explicit adaptations, not claims
to be complete runtime specifications. Derived claims identify their premises
and explain the argument; they are not attributed as numbered source theorems.

[`lean/Catalog/Coroutines.lean`](../lean/Catalog/Coroutines.lean) supplies tagged
states/actions, body relations, exact transition rules, finite resume outcomes,
pool state, eligibility, and the scheduler's operational rules. The bindings
and formulation excerpts are maintained with the graph. Body semantics and
runtime correspondence remain instantiation obligations. Two local Lean
examples check terminal and reentry exclusions.

[`lean/Catalog/CoroutineProofs.lean`](../lean/Catalog/CoroutineProofs.lean)
contains three separately registered theorem witnesses:

| Graph theorem | Lean declaration | What the expected proposition establishes |
| --- | --- | --- |
| `AsymmetricCoroutine-successive-resumes-require-yield` | `Catalog.CoroutineProofs.successive_resumes_require_yield` | Any two resume positions in a finite labelled path from creation have a yield in the intervening word. This also covers the consecutive-resume case. |
| `CooperativeScheduler-reachable-owner-invariant` | `Catalog.CoroutineProofs.reachable_owner_invariant` | Every state finitely reachable from the initial pool satisfies both owner and waiting invariants; preservation covers every action. |
| `CooperativeScheduler-cooperation-does-not-imply-progress` | `Catalog.CoroutineProofs.cooperation_does_not_imply_progress` | Given the stated reachable valid state and local self-loop, constructs a constant infinite sequence of permitted internal steps with the other task always runnable and never running. |

The third witness retains reachability, validity, distinct tasks, ownership,
readiness and the internal self-loop as explicit hypotheses. It does not assume
the desired result or introduce a global axiom. A concrete two-task pool in the
proof module demonstrates that these hypotheses can be satisfied. The first
witness splits finite paths and rules out resume after a segment with no yield;
the second uses initialization, per-action preservation and reachability
induction.

Each binding records an independently reviewed expected type, all direct
`dependsOn` premise mappings, structural carrier/equality interpretation and a
current catalog fingerprint. The readable proof sketches and independent
mathematical provenance remain alongside these bindings. Registration is
metadata; only fresh `lean/verification.json` from `make test-lean` supports
compiler-verified status. These witnesses prove the mapped abstract
propositions, not conformance of Lua, Python or a generated implementation.

After changes, run `make build`, `make test`, `make test-rdf`,
`make check-lean` and `make test-lean`. Structural/RDF checks and model
compilation have different scopes; neither establishes complete runtime
conformance or automatically proves the graph's derived claims.
