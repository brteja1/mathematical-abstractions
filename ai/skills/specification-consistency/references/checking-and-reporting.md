# Checking methods and evidence

Use only the portions relevant to the chosen model. These are workflow instructions, not new catalog claims or proof witnesses.

## Backend selection

| Method | Evidence it can provide | Limits to report |
| --- | --- | --- |
| Exhaustive finite enumeration | A satisfying valuation, or exhaustion of the entire declared finite model space | Exponential growth; artificial finite restrictions may exclude valid models of the original specification |
| SAT/SMT | SAT model or UNSAT result for a supported encoding; a tracked core when available | Match mathematical versus machine arithmetic, quantifiers and solver theories; record `unknown`/timeout and unsupported constructs |
| Bounded model checking | Concrete trace or absence of a violation within stated bounds | A trace-length bound alone does not establish unbounded safety, liveness, realizability or inconsistency |
| Complete finite-state checking | Reachable states, bad traces/deadlocks, temporal checks supported by the backend | Initial states, stuttering, fairness, environment moves and acceptance conditions must match the specification |
| Lean | Compiled contradiction from named hypotheses, or a concrete model with proved requirements | A conditional theorem does not show assumptions are satisfiable; correspondence with the source specification remains a separate obligation |
| Manual derivation or sampled tests | Explained candidate conflict or concrete counterexample | Label a manual derivation as such; sampling cannot establish absence of conflicts |

Determine whether an abstraction preserves the conclusion being drawn. Restricting an infinite carrier to a small finite one may make a satisfiable specification look UNSAT. Failure to find a model within that restriction is not a general inconsistency result. Conversely, check that a reported model or counterexample actually represents permitted original behavior. Do not silently identify undefined operations with arbitrary total functions.

For a finite operation contract, enumerate each required input, enumerate its permitted outputs, and retain an input with no output as evidence of a coverage failure. If a precondition is imposed by the specification, check its nonemptiness and compatibility with required inputs before using it. If the contract permits explicit failure, include that failure outcome; do not assume success is required.

For SMT, track original clause IDs independently of solver-generated symbols. Document integer/rational/real versus bit-vector semantics, signedness, overflow, rounding, quantifier ranges, and any finite unrolling. Recheck an extracted core together with the fixed background. A core names constraints used in the encoded conflict; it need not be minimal or identify the only conflict.

For temporal specifications, check initial-state existence before universal path properties. State which executions count: finite versus infinite, deadlock handling, fairness and nondeterminism. A counterexample to a property on a proposed system disproves that system's conformance; it does not show that every possible implementation violates the specification. An unrealizability claim needs the appropriate environment/system quantifiers or strategy argument.

## Report shape

Scale the report to the review, but retain the following information:

```text
Scope: specification paths/revisions/hashes; clauses checked and omitted
Interpretation: carriers, equality, inputs/outputs, quantifiers, behavior conventions
Background: environment assumptions and whether they are satisfiable
Mapping: clause ID + source locator -> encoded constraint -> catalog IDs/premises
Method: tool/version, encoding path/hash, command, domain/trace bounds

Finding:
  Classification: demonstrated conflict / conditional conflict / ambiguity /
                  missing requirement / inconclusive
  Clauses and required scenario:
  Reason: derivation, no-output input, witness or trace
  Evidence: exact executed result and reproducible artifact
  Scope and translation limitations:
  Possible repair and its behavioral effect:
  Repair recheck: actual result, or explicitly not executed

Remaining coverage: unchecked clauses/scenarios and why
```

For a clean finite result, say “No conflict in the complete declared Boolean model” or “Every input in the declared finite domain has an allowed outcome,” as appropriate. For a bounded or sampled check, say exactly what was explored. Do not upgrade a local result to “the specification is consistent” without an appropriate model/completeness argument and justified translation.
