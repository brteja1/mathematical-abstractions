---
name: specification-consistency
description: Find conflicting requirements, impossible operation contracts, and vacuous specifications using the mathematical abstractions catalog, explicit semantic mappings, and executable checks. Use for specification review; implementation testing is a separate workflow.
---

# Specification consistency

Review whether a specification's requirements can hold together under its intended semantics. Deliver traceable findings and executable evidence where feasible. Catalog validation, SHACL success, source citations, and Lean model bindings alone do not establish specification consistency.

## Establish the specification and its interpretation

Read the target project's instructions and the relevant specification versions. Preserve clause IDs or assign local IDs with file/section/line locators and exact excerpts. Distinguish normative requirements, definitions, examples, environment assumptions, required inputs/scenarios, and optional behavior. Do not silently resolve precedence between documents.

Record carriers, equality/observations, operations and before/after states, quantifier scope, preconditions, allowed outcomes, and definedness. Resolve relevant numeric ranges, units, overflow/rounding, empty cases, errors, termination, concurrency, and fairness. Separate user requirements from assumptions introduced by the agent. Ambiguous interpretations get separate conditional analyses; an ambiguity or omitted guarantee is not itself a contradiction.

Ask for missing information only when it blocks the interpretation; continue with independent checks. Do not strengthen preconditions, exclude required scenarios, or invent priorities to make the specification pass.

## Retrieve applicable mathematics

Resolve `<catalog>` to the checkout containing this skill, independently of the target working directory. Read its `AGENTS.md` and use absolute paths for commands from another repository. These standard-library commands read authoritative Markdown without requiring ONTFS:

```sh
python3 <catalog>/scripts/catalog.py list --search propositional
python3 <catalog>/scripts/catalog.py get PropositionalLogic --sections operations
```

Search by mathematical meaning and synonyms. Start with the selected concept and operations. Fetch axioms/laws for constraints actually used in the encoding, and a theorem only when the check needs its result or proof. Fetch premises to justify those uses and sources when checking provenance; do not preload them for every candidate. Use a bounded `dossier CONCEPT --purpose proof --limit 80` only when that larger context is needed; check `truncated` and retrieve omitted premises explicitly. Preserve source gaps and distinguish informal statements from compiled witnesses. Neither `requiresConcept` nor `specializationOf` transfers axioms.

Use focused readable formulations, scope and limitations to identify carriers, guards and quantifiers. Retrieve `--view lean` and the relevant part of the [formulation guide](../mathematical-tests/references/formulations.md) only when constructing or reusing a formal encoding/proof. A `def ... : Prop` states a target and structure fields impose hypotheses; neither shows satisfiability. Check inhabited inputs and nonvacuity separately. Omitted partial-model behavior remains unchecked.

For ONTFS/SPARQL retrieval, reuse the existing bounded helper rather than creating another graph export:

```sh
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py search hoare --limit 4 --max-chars 4000
<catalog>/.venv/bin/python <catalog>/ai/skills/mathematical-tests/scripts/query.py interface HoareTriple --sections operations --limit 6 --max-chars 8000
```

Read [the shared retrieval reference](../mathematical-tests/references/retrieval.md) for setup, source/premise queries and scratch projections. Respect `nextOffset`, `depthBoundary` and `needsLargerBudget`; projection and source hashes must match. Preserve modified runtime graphs. If using the dependency-free commands instead, disclose that backend choice. A query returning no matching claim is not evidence of consistency.

Map each selected catalog operation/claim ID to the specification's symbols and assumptions. Use only applicable laws; a useful abstraction is not an additional product requirement. Route by the actual semantics:

| Specification | Candidate catalog concepts | Check to construct |
| --- | --- | --- |
| Boolean rules | PropositionalFormula, PropositionalLogic | Joint satisfiability and required scenarios |
| Quantified objects/relations | PredicateLogic | Explicit structures, quantifiers and domain restrictions |
| Operation contracts | HoareTriple, WeakestPrecondition | Permitted outcomes for each required input; termination separately |
| Stateful or temporal behavior | TransitionSystem, KripkeStructure, LinearTemporalLogic | Initial states, reachability, invariant preservation, deadlock and progress obligations |
| Numeric requirements | Appropriate exact, bounded or floating-point concept | Range, units, rounding and overflow compatibility |

## Construct the right obligations

Check environment assumptions and required domains for satisfiability first. If those already conflict, distinguish that failure from a conflict introduced by a requirement.

Joint satisfiability asks whether some model satisfies the conjunction of all selected clauses. Pairwise checks are insufficient. Also check **input coverage**: for an operation relation `R(i,o)` and required domain `D`, require `∀i∈D, ∃o, R(i,o)` when the contract promises an outcome for every such input. A single satisfying input/output pair does not establish this. Check required scenarios individually; do not conjoin mutually exclusive scenarios as if they were one execution. Preserve shared implementation choices across scenarios when checking one implementation can support them all.

Check that preconditions and initial states are inhabited where required. Partial-correctness Hoare triples may hold when no execution terminates; they do not imply implementability or termination. For stateful specifications, distinguish an unreachable bad state from an impossible required transition. For reactive systems, distinguish the existence of one permitted trace from a strategy that meets requirements against all permitted environment behavior. Include scheduler/fairness assumptions when checking progress.

Read [references/checking-and-reporting.md](references/checking-and-reporting.md) when choosing a backend or writing findings. For a complete dependency-free demonstration, read and run [references/boolean-example.md](references/boolean-example.md).

## Execute and diagnose

Choose exhaustive enumeration for genuinely finite domains, an installed SAT/SMT or model-checking backend for a supported encoding, or the pinned Lean project for explicit proof obligations. Keep the encoding and commands in the requested output location or a scratch directory, separate from authoritative graph records. Do not use `eval` on specification text. Inspect the generated encoding against the clause mapping before trusting its result.

Run the check. Retain tool/version, specification and encoding hashes, bounds, assumptions, commands, results, and a witness, trace, conflicting set or derivation. An unavailable tool, timeout, `unknown`, or incomplete search is inconclusive. Inspect SAT witnesses against the original clauses; recheck conflicting sets and their assumptions. An UNSAT result diagnoses the encoding; report an original-specification inconsistency only to the extent the translation is justified.

When practical, shrink a conflict by removing clauses and rechecking. Call it inclusion-minimal only after every single-clause removal is satisfiable with the background fixed; this does not establish minimum cardinality. Include indispensable background assumptions and required scenarios in the finding, even if the backend omits them from its core. Check the full selected set, not only the easiest clauses.

## Deliver evidence and preserve scope

Lead with findings and their scope. For each finding, give clause IDs/locators, the interpretation, catalog IDs and semantic mapping, the conflict or failing input, reproducible evidence, and limitations. Distinguish demonstrated conflicts, conditional conflicts, ambiguities, missing requirements, and inconclusive checks. A finite search with no conflict supports only its stated domain/bound unless a completeness argument applies.

Propose concrete repairs with the behavior each repair changes; do not edit normative requirements without authorization. Recheck a proposed repair before claiming it resolves the conflict. Keep specification findings outside catalog records unless catalog maintenance is requested. New graph claims still require consulted sources and the repository's full build/validation workflow. For Lean, follow `lean/README.md`; prove contradictions from explicit hypotheses without global axioms or `sorry`, and require fresh compilation before claiming a proof. A proof conditional on inconsistent hypotheses does not establish that those hypotheses have a model.

This skill lives in the requested `ai/skills/` location. Agents can read it explicitly; automatic discovery depends on the host's skill configuration. Keep it attached to this checkout so its infrastructure links resolve.
