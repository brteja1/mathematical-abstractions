# Mapping mathematical claims to executable tests

Read only the relevant cases. Retrieve the actual catalog records before selecting properties; examples below are design choices, not new catalog claims.

## Mapping record

A test rationale should make these links reviewable, using the target repository's preferred format:

| Item | Record |
| --- | --- |
| Scope | Target file/symbol and public contract being exercised |
| Mathematical basis | Stable concept, operation and selected claim IDs; source/provenance gaps |
| Formulation and scope | Relevant readable equation and partial-model omissions; typed interpretation, module/symbol and witness type/premises only if relied on |
| Carrier and representation | Valid software values, mathematical observation/model and equality |
| API correspondence | Constructors, operations and observers used in the claim; mutation, return order and exceptions |
| Applicability | Each claim assumption, definedness condition, numeric policy and concurrency assumption |
| Test obligation | Executable property/oracle and justified input domain |
| Evidence | Framework command, result, seed/counterexample and deferred obligations |

For example, a mutable `push` returning `None` can refine a mathematical state-returning push only through a before/after observation. A pop result may use a different tuple order. Copying the equation without those mappings tests the wrong interface.

Fetch claims only for properties actually selected; a theorem is unnecessary when a definition or operation contract already determines the oracle. If typed interpretation or proof reuse is needed, use the relevant section of [formulations.md](formulations.md) to distinguish a definition, a structure hypothesis, a stated proposition and a currently compiled witness. `leanPremiseMapping` is JSON-encoded data, not an instruction to assume all its premises hold in the software. Map each premise actually used to the target contract and assertion. A partial-model omission stays deferred unless an independent contract/model supplies it.

## Collections and stateful APIs

For stacks, queues, maps and sequences, compare operation histories against a simple independent state model using only the mapped public observations. Generate sequences that include construction, insertion/update, observation and removal. Preserve old expected states separately when the implementation mutates in place. Include duplicates, empty/singleton transitions, repeated updates, and values that stress the contract's equality policy.

A state machine can generate `pop` only when the model is nonempty. Test empty-pop exceptions or sentinel results separately if the software specifies them. Avoid teaching a model an undefined outcome merely to make it run.

Check laws across implementations only after confirming their conventions: a bounded queue, expiring map or duplicate-free ordered collection has constraints absent from a generic unbounded sequence model. A set's extensional equality does not require iteration order; an ordered set's positional equality does.

## Numeric types and equality

Identify exact integers, wrapping integers, checked/saturating arithmetic, or a particular floating-point format before retrieving laws. Record width, overflow/underflow, division convention, rounding, NaNs, signed zeros and flags where applicable.

Generate representable operands and any needed nonzero divisors. Compute reference arithmetic independently in an exact domain before applying the specified wrapping/checking/clamping/rounding policy. Restrict an exact-arithmetic property to representable intermediate results only when that restriction matches the documented contract and the selected claim. Exercise the boundary policy separately.

Do not assert exact associativity on floating-point addition by borrowing a real-number or ring law. If the software contract calls for approximation, define a justified error relation or exact correctly rounded oracle. A tolerance is not automatically transitive and cannot silently replace mathematical equality in every algebraic law. Tiny hand-picked inputs that never exercise rounding/overflow give little evidence for the actual numeric contract.

## Nondeterminism and concurrency

For priority queues with equal keys, test that extraction selects an allowed minimal item and preserves the correct residual multiset. Do not require a tie order unless the software promises it. For other nondeterministic APIs, test membership in allowed outcomes and invariants across outcomes rather than one arbitrary exact sequence.

Concurrency tests need an explicit history/event model, completion treatment, object specification and scheduler assumptions. Distinguish program-order preservation from real-time preservation; the Linearizability and SequentialConsistency catalog entries are not interchangeable. A finite stress run does not establish liveness, fairness, termination, or linearizability for every execution. Use an installed history checker or bounded state exploration when its model fits, and state the explored bound. Synchronize relevant interleavings rather than relying only on sleeps.

## Information, coding and cryptographic interfaces

For information/coding APIs, preserve probability normalization, logarithm base, zero-mass and infinity conventions, word length and decoder domains. For cryptography and lattice APIs, map algorithm/encoding/validation requirements independently of abstract permutations, exponent maps, norm relations or normalized error laws. Functional examples can test the promised operations, but do not establish cryptographic security, hardness, a sampling experiment or a coding theorem. Retrieve only the relevant domain records and the shared formulation guide's domain distinctions.

## Compositions, predicates and metamorphic tests

For transformations or functions, an operation-preserving composition law can be useful when no simple expected-result oracle exists. Map domains/codomains and intermediate definedness; check side effects, exceptions and nondeterministic outputs before treating an API as a pure total function.

For relations, orderings or predicates, generate cases that reach each precondition. A conditional property that nearly always rejects its input can pass while testing nothing. Track accepted examples, use constructive generators when possible, and minimize failures into reproducible witnesses. Do not infer antisymmetry from an equality policy the software does not implement.

A metamorphic property is evidence for that relationship, not a complete implementation oracle. Combine it with independent examples or a reference model where the contract permits, so a degenerate implementation such as a constant output cannot pass every test.
