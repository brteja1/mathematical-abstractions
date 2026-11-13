---
name: abstraction-discovery
description: Inspect unannotated software, data structures, and APIs to discover candidate mathematical abstractions, identify hidden assumptions and broken algebraic laws, and recommend principled refactorings.
---

# Discover mathematical abstractions in software

Inspect existing software components, algorithms, and data structures to uncover their underlying mathematical abstractions. Identify implicit invariants, detect violated algebraic laws, and recommend principled refactorings grounded in the catalog.

## Inspect code before querying the catalog

Read the target implementation, type definitions, method signatures, error paths, and nearby tests. Analyze concrete behavior rather than relying on class or variable names:

- **Signatures and Arity**: Identify binary combination operations `(A, A) -> A`, binary relations `(A, A) -> Bool`, state transitions `(State, Event) -> State`, partial projections, and observers.
- **Identity Elements and Defaults**: Check how empty, zero, or initial cases are initialized and whether an explicit neutral value exists.
- **State Mutation and Observability**: Determine whether objects are persistent, mutable in-place, or stateful; define what constitutes observable equality for results.
- **Error and Edge Handling**: Check boundary conditions, null/empty collections, numeric overflow, rounding, and partiality.

Do not assume a method named `combine` is associative or that a `compare` function forms a total order. Unannotated code often implements an incomplete or subtly broken abstraction.

## Retrieve candidate abstractions progressively

Resolve `<catalog>` to the checkout containing this skill. Read its `AGENTS.md` and retrieve candidate concepts using standard-library commands or the bounded ONTFS helper:

```sh
python3 <catalog>/scripts/catalog.py list --search monoid
python3 <catalog>/scripts/catalog.py get Monoid --sections operations axioms laws
```

Search by operational behavior and mathematical role:

| Operational Pattern | Candidate Catalog Concepts | Key Governing Laws to Check |
| --- | --- | --- |
| Binary reduction / folding `(A, A) -> A` | `Semigroup`, `Monoid`, `Group` | Associativity (`Monoid-associative`), identity (`monoid-identity`), invertibility |
| State reconciliation / CRDT merge | `JoinSemilattice`, `StateBasedCRDT` | Idempotence, commutativity, associativity, monotonicity |
| Comparison / Sorting / Priority | `Preorder`, `PartialOrder`, `TotalOrder` | Reflexivity, transitivity, antisymmetry, totality |
| State transitions / Protocols | `LabelledTransitionSystem`, `KripkeStructure` | Determinism, reachability, enabled actions, deadlocks |
| Set / Map / Collection indexing | `Set`, `Multiset`, `Sequence`, `Multimap` | Extensionality, membership, duplicate handling, ordering |
| Resource / Access management | `Lock`, `Mutex` | Mutual exclusion, compatible holders, release ownership |

Start with focused concept and operation records. Retrieve axioms and laws only for candidate invariants under test. Do not preload complete claim closures or full dossiers.

## Test algebraic laws and detect violations

Evaluate candidate laws against the code's actual semantics. Use static analysis, symbolic evaluation, or lightweight property tests to probe for broken assumptions:

1. **Associativity `(x · y) · z == x · (y · z)`**: Check whether batching, parallel reduction, or tree folding alters outcomes. Common violations include floating-point arithmetic, list concatenation with order-dependent deduplication, and stateful side-effects during combination.
2. **Identity `e · x == x · e == x`**: Test whether an empty input or default value acts as a true two-sided identity. Common violations include methods that crash on empty collections, allocate distinct sentinel wrappers, or mutate state on identity combinations.
3. **Commutativity `x · y == y · x`**: Check whether evaluation order affects concurrent merges or stream aggregations.
4. **Idempotence `x · x == x`**: Test retry loops, caching, and state-synchronization methods.
5. **Transitivity and Comparators**: Verify that ordering functions satisfy transitivity. Inconsistent comparator implementations (e.g., subtracting integers prone to overflow, or incomplete tie-breaking) frequently cause sort or heap corruption.

When a law is violated, construct a minimal concrete counterexample showing the inputs, the expected mathematical outcome, and the actual software behavior.

Read [references/discovery-guide.md](references/discovery-guide.md) for detailed mapping tables and code smells, and [references/metrics-example.md](references/metrics-example.md) for a worked example on telemetry aggregation.

## Deliver the discovery report and refactoring plan

Produce a structured report detailing:

- **Target Component**: File, class, function, or API locator.
- **Discovered Abstraction**: Matching catalog concepts with stable IDs (`urn:csabs:concept/...`).
- **Carrier & Operation Mapping**: Concrete types and methods mapped to catalog carriers and signatures.
- **Law Assessment**: Table of checked laws (associativity, identity, commutativity, etc.), marked as satisfied, conditionally satisfied, or violated.
- **Counterexamples**: Explicit inputs that trigger law violations or unexpected edge behavior.
- **Refactoring Recommendations**: Specific architectural changes to align the software with the sound abstraction (e.g., introducing an explicit identity element, adjusting floating-point aggregation, or making merge operations idempotent).

Connect the discovery findings to downstream skills:
- Use [implementation-mapping](../implementation-mapping/SKILL.md) to formalize the updated API contract.
- Use [implementation-conformance](../implementation-conformance/SKILL.md) to review refactored code against the revised obligations.
- Use [mathematical-tests](../mathematical-tests/SKILL.md) to generate regression property tests based on discovered laws.
