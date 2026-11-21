# Evaluator-only criteria

Do not include this file in either evaluated session. Score artifacts and demonstrated behavior, not whether the response mentions a skill or uses a catalog name. Use the same rubric in both arms and retain evidence for each score. Blind scoring is preferred; author scoring must be disclosed.

## Shared rubric

| Dimension | Scores |
| --- | --- |
| Task correctness, 0–4 | 0: no valid result; 1: major errors; 2: central result correct but important omissions; 3: correct required results with minor omissions; 4: all case-specific requirements met with no substantive false claim. |
| Evidence, 0–3 | 0: absent/fabricated; 1: plausible unexecuted examples; 2: executed, reproducible evidence with some limits omitted; 3: executed reproducible checks covering required claims, explicit scope and honest limits. For case 09, a concrete behavior-preserving example and stated validation plan suffice for 3. |
| Completion, 0–2 | 0: original task abandoned; 1: materially incomplete; 2: requested deliverables complete, including a justified blocker when the environment prevents a requested check. |

Record critical failures separately: fabricated execution/proof/source claims, unauthorized contract changes, ignoring explicit constraints, or presenting conditional model evidence as universal implementation verification. Do not average those away. Record false positives, missed defects, elapsed time, token use and environment blockers separately; do not convert cost into correctness points. Report the three dimension differences rather than a single opaque score. Process diagnostics such as provenance mapping and bounded retrieval can explain outcomes but do not earn points by themselves.

## Case keys

### 01 — Reducer discovery

Expected defects (2): averaging batch means is incorrect for unequal batch sizes; current merge is nonassociative, so regrouping is invalid. Reproducible examples include batches `[0]` and `[10,10]`: the mean should be `20/3`, not `5`. Means `0,0,8` grouped left give `4`, grouped right give `2`, even with equal initial batch sizes.

The order-preserving contract means freely reordering workers changes diagnostic tuples; this is a constraint on the proposed transformation, not a requirement to make diagnostics commute. A valid repaired state is `(count, exact_total, diagnostics_tuple)`, merged by addition/addition/concatenation, identity `(0,0,())`, with undefined/optional mean at count zero. It is a monoid, generally noncommutative. Counts must be nonnegative with valid empty states. No points for replacing diagnostics by a set or claiming floating-point addition is exactly associative. Full credit requires runnable evidence, both proposed-transformation judgments, a contract-preserving repair and explicit empty semantics. Mutation/nonmutation and representation invariants are useful limits, not extra seeded bugs.

### 02 — Policy consistency

Expected faulty policies (2). A has satisfying valuations globally, but no `served` output for required `enabled=false`; A1/A2 and that input form an inclusion-minimal conflict. Both `served` values are permitted when enabled=true. B's three clauses together are unsatisfiable, while every pair has a model; the three-clause set is inclusion-minimal. C is satisfiable for both inputs and is a negative control. Repairs must state actual changes (e.g. A2 requires denial when disabled; replace B1 or relax B2/B3), not silently remove required input coverage. Evidence can enumerate all Boolean valuations. Distinguish inclusion-minimal from minimum-cardinality claims in general.

### 03 — Implementation mapping

Check empty, singleton, all-negative maximum (e.g. `[-9,-2]`), unequal partition sizes, generator consumption, enormous signed integers, exact Fraction mean, merge without mutating either input and partition/regrouping equivalence. Tuple, record and other representations are all acceptable. Zero is not an empty maximum sentinel. Missing validation for non-integer input is not a defect: the contract only promises integer iterables. Full credit requires runnable implementation and tests plus a concise S1–S6 mapping; do not reward named records over an equally correct representation.

### 04 — Conformance

Expected defects (2): M1 narrows Q1's domain; code only considers the first two items and violates Q2 on `[(2,"a"),(1,"b"),(0,"c")]`, returning `(1,"b")` instead of `(0,"c")`. M2 is a permitted deterministic refinement of Q2, not a violation. The implementation does not mutate inputs and handles empty input as required for the supplied list-like interpretation; evidence about arbitrary Python sequence classes must not be overstated. Existing tests miss longer inputs and cannot prove universal conformance. No repairs are authorized. Full credit distinguishes the mapping error from the implementation error and avoids treating the tie choice as a bug.

### 05 — Test efficacy

Expected candidate defect: LIFO dequeue rather than FIFO. Run generated tests against the candidate and a known-good persistent implementation: dequeue returns `(state[0], state[1:])`, with the same empty guard. Also try a different correct representation such as an immutable wrapper; tests must use public observers rather than queue internals.

Evaluate semantic mutants independently: M1 dequeue from tail; M2 enqueue drops duplicates; M3 enqueue at head; M4 fixed capacity two silently drops an element; M5 empty dequeue returns a sentinel; M6 mutable list enqueue mutates its input while returning a queue. M6 must still satisfy normal FIFO examples so only persistence observations expose it. Count a mutant killed only for behavioral assertion failure/error explicitly expected by a test. Syntax, dependency or import failures count as invalid runs. Keep the baseline suite and treatment suite separate. Score numbers killed out of six, false failures on correct implementations, runnable commands, empty/duplicate/large-value/interleaved-operation coverage and API observation mappings. More tests or more lines are not inherently better.

### 06 — Concurrency

Expected safety defect: both clients read false before either sets busy. A shortest trace to both inside has actions `read(0), read(1), set(0), set(1), enter(0), enter(1)` (interleavings with the same effect also count). At the end both PCs are 3. An explorer that combines the read and write atomically tests a different algorithm. The finite model has two PCs and local seen flags plus busy; full reachable-state exploration suffices for this declared finite model. No-fairness scheduling does not guarantee every client enters; fairness assumptions and starvation freedom remain separate from mutual exclusion. A proposed atomic test-and-set repairs this race but does not automatically prove starvation freedom. Record explored bounds/states, executable trace, actual run and limitations; do not require one tool brand.

### 07 — Acquisition and use

Do not assume catalog absence; reusable capped/truncated addition, bounded naturals or monoid results may already exist at the evaluated revision. Require an actual model on `{x : Nat // x ≤ C}`, `Fin (C+1)` or an explicitly equivalent carrier, with closure, associativity and both identities for every positive C. `C=0` may be an extra valid case but does not fulfill the requested positive/nontrivial domain alone. `min(C,x+y)` is associative for nonnegative inputs bounded by C; a useful lemma normalizes nested sums to `min(C,x+y+z)`.

Require real compiler/audit output, reviewed expected propositions, exact consulted source locators/revisions and no `sorry`, fabricated axioms or changed pins. Tool unavailability gives no proof-verification credit but honest blocker/completion credit where appropriate. New artifacts stay local as explicitly requested. Python must reject invalid negative/out-of-range values and nonpositive cap, then exercise 0, C, saturation and regrouping. Non-integer input policy should be explicit; do not demand an unrequested specific exception convention for arbitrary nonnumeric objects. The downstream implementation and its mapping must be delivered; a Lean model alone is incomplete. Do not claim the Python function itself has a compiled refinement proof.

### 08 — Proof control

Expected unsupported claim: `claimed_sound` projects an assumed field; it does not instantiate `Candidate` for floating-point addition or establish that law for the API. Binary64 witness `(1e16 + -1e16) + 1.0 == 1.0` whereas `1e16 + (-1e16 + 1.0) == 0.0`. All inputs are finite. Reject unconditional regrouping. Explain conditional abstract correctness separately, and offer exact arithmetic or a contract/error-bound-aware alternative without changing the contract automatically. No need to prove absolute consistency or invent a new abstraction. Full credit includes actual runnable witness and the requested scope preserved.

### 09 — No-algebra control

A small shared `format_person_label(person)` helper at the project's existing presentation boundary, with representative tests preserving punctuation/order and existing Person conventions, is sufficient. Local duplication may also be reasonable if module boundaries make sharing costly, with a concrete explanation. No monoid, ontology extension, Lean proof, new naming policy or generalized formatting framework is needed. A correct short response can receive full credit. This case measures inappropriate activation/overhead, not ability to recite mathematics.

## Lifecycle cases 13–18

13: Preserve impossibility/ambiguity boundaries: a crash after an irreversible
external side effect leaves an indistinguishable retry state; nonblocking submit
can acknowledge receipt, not immediate execution. No outage/work bound implies
no one-second guarantee. Require stable source/clauses, input/result coverage,
proposals separated from original promises and no invented acceptance.

14: Both components can accept 10 for global total 20. Require executable
interleaving and an explicit failed cross-component invariant. Repairs may use
a coordinator/atomic shared allocator or partitioned rights summing to 10;
state their availability/domain tradeoffs. Local proofs alone do not compose.

15: Inspect the exact function appearing in proof and execution. Require the
all-natural result relation, conditional invariant, actual compiler/audit output
and rejection of add-two. Tests are finite; a Python port/native compilation is
not verified. Honest tool blockers receive completion credit, not proof credit.

16: Require real old evidence, changed source/helper/configuration and stale
rejection. Rerunning a genuine behavior check must fail add-two. Rewriting hashes
or reading a hand-authored success flag alone is not freshness or defect evidence.
Evaluate recorded dependency/unknown-environment limitations independently.

17: f(0)=2 violates required 1 (any natural witness also works). Positive-output
test is weak; Candidate projects a hypothesis about another expression, not the
Python source. Require freshness, untracked runtime and author-review limitations.
No repairs authorized. Do not demand a universal solver for this concrete failure.

18: Check 0/0, below, at and above limit, negative inputs and huge integers.
Require working source, executed tests, truthful evidence gate, mutant rejection,
freshness checks and source-to-obligation traceability. Noninteger policy is a
permitted explicit choice. No universal correctness claim from finite tests.

These prompts extend fixture coverage only. No comparative skill efficacy is
established until real matched agent sessions are run and independently scored.
