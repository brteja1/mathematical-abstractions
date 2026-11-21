# Agent workflows

All repository skills require catalog abstractions retrieved through the query tools, with stable IDs and explicit semantic mappings. Do not open or search catalog storage or generated exports to retrieve facts. Report missing mathematics and blocked work before acquisition or dependent steps; see the [catalog-use policy](../ai/skills/mathematical-tests/references/catalog-use.md) for required report contents and explicit acquisition exceptions.

Use the graph as a retrieved specification and dependency map. Keep assumptions and source quality visible in the resulting work.

For controlled comparisons of these workflows, use the [paired skill evaluation suite](../ai/evaluations/README.md). Prepare fresh workspaces outside the repository, give both arms equal catalog/tool access, expose skill instructions only to the treatment, and keep the evaluator criteria and other outputs separate. Score task correctness, executable evidence, false positives, completion and cost; report actual runs separately from authored examples.

Hard cases additionally assess generated specification precision, code/test maintainability and reviewer readability using the suite's [quality rubric](../ai/evaluations/quality-rubric.md). Use independent contract checks and semantic mutation testing for behavior; prepare anonymous comprehension questions for human readers. Counts, length, and task completion do not establish artifact quality, and editorial readability reviews are not measured human comprehension.

## Specification-driven lifecycle and evidence admission

Use [spec-driven-development](../ai/skills/spec-driven-development/SKILL.md) to
coordinate an authorized lifecycle task. Its skills and supporting workflows cover
[requirements](../ai/skills/requirements-formalization/SKILL.md),
[composition](../ai/skills/compositional-verification/SKILL.md),
[actual-source refinement](../ai/skills/implementation-refinement/SKILL.md),
[change impact](../ai/skills/spec-driven-development/references/verification-maintenance.md) and
[assurance review](../ai/skills/implementation-conformance/references/assurance-review.md).
Keep task artifacts outside authoritative graph records and preserve source-to-clause-to-API links.

The [shared ledger guide](../ai/skills/spec-driven-development/references/assurance.md)
defines the schema and `scripts/assurance.py` commands. `check`/`impact` inspect
declared traceability and freshness; `run` explicitly executes a named check.
Missing, failed or stale required evidence, unresolved decisions and pending or
rejected requirement validation block admission. Tests, bounded exploration,
review and proof remain different kinds. Only the narrow `lean-source-v1`
profile currently admits proof evidence: source function and theorem share a
file, expected types are explicit, and the pinned compiler and transitive axiom
audit must pass. This does not establish native executable correspondence.

Run `make test-assurance` for the actual-source pilot and rejection regressions.
Reviewer identity, natural-language completeness and arbitrary external command
inputs remain outside the local gate. Neither fixture checks nor a passed ledger
measure comparative skill efficacy or universal software correctness.

## Missing abstractions and proofs

Problem-oriented AI skills route required mathematical gaps to [abstraction-acquisition](../ai/skills/abstraction-acquisition/SKILL.md). Search existing concepts and claims first, then reuse the pinned Lean/Mathlib or consult primary sources; construct a model when necessary. Prove that the selected interpretation satisfies its axiom basis and establish the additional claims needed by the problem. An assumed structure, a conditional theorem or one trivial instance alone does not establish required-input coverage or software refinement.

Prepare sourced definitions, semantic mappings and compiled, axiom-audited evidence before offering **Promote to catalog (default)** or **Keep with this task**. Wait for that choice unless already specified. Promotion preserves the source policy and existing witness schema: model-satisfaction results are Theorems linked to defining constraints, rather than bindings against Axiom IDs. Task-local artifacts retain their own exact inputs and compiler evidence without claiming catalog verification status. Resume the original task after retention and refresh queries after promotion. Unavailable proofs or sources remain explicit blockers; assumption-based continuation requires the user's choice and yields conditional conclusions.

The [acquisition guide](../ai/skills/abstraction-acquisition/references/acquisition.md) details sourcing, construction, persistence and recovery. The [watermark example](../ai/skills/abstraction-acquisition/references/watermark-example.md) provides a runnable Lean model-satisfaction proof and a downstream application, reusing an existing concept.

## Mathematical formulations and evidence

Concept records now expose readable `mathematicalFormulation`, selected `leanFormulation`, `formulationScope`, `leanModelMapping`/`leanModelLimitations`, and local `formulationSource`/`formulationLocator`. Registered witnesses expose their expected proposition and JSON-encoded `leanPremiseMapping`. The AI skills use the shared [formulation and Lean-evidence guide](../ai/skills/mathematical-tests/references/formulations.md) for these fields, source retrieval, module context and domain-specific omissions. Start with focused concept/operation records and match carriers, equality, guards and observations to the normative contract. Fetch axioms/laws for the current obligation and theorems only when their result or proof is needed; do not preload proof material or all linked claims.

The bounded helper's `sources ID` keeps mathematical citations as its default; `sources ID --kind formulation` retrieves the separate local Lean sources. Interfaces default to operations only; `node` and `interface` default to focused fields. Use `--view lean` for a needed typed interpretation, or `--view full` for a complete-record audit. Retained assumptions and partial-model limits are not shortened. Search includes readable mathematical formulations. Check budget and pagination flags when the additional formulas make records larger. A stated proposition or a model binding is distinct from a verified witness; inspect current `scripts/lean.py get ID` output before relying on compiled evidence. Local sources and compiled proofs do not repair independent citation gaps.

## Proof construction with Lean or Coq

For a group identity, first retrieve the exact group interface:

```sh
python3 scripts/catalog.py get Group --sections operations
python3 scripts/agent_query.py node urn:csabs:theorem/Group-inverse-product --view lean
```

Read the target theorem's `formalStatement`, `assumptions`, `appliesTo`, `dependsOn`, `reviewStatus`, and provenance. Follow each needed premise by ID with `agent_query.py node ID`. Use a dossier only when the task needs that broader dependency package; it expands linked claims beyond the focused defaults. If it reports `truncated: true`, retrieve needed missing premises separately rather than increasing context without a reason.

Before translating into an assistant, write an explicit mapping:

| Catalog requirement | Formalization obligation |
| --- | --- |
| Carrier, operations, equality | Choose corresponding types, functions and equality relation. |
| Axiom basis and conventions | Check the actual imported library structure and available instances. |
| Assumptions and prerequisites | Introduce hypotheses explicitly; do not infer them from graph proximity. |
| Claim dependencies | Locate matching library lemmas or prove the intermediate statements. |
| Unicode statement and proof sketch | Translate into assistant syntax; neither field supplies checked code. |
| Source gaps or editorial review | Report limitations; a citation does not establish a compiled proof. |

Pin the assistant version and library revision in the formalization project. Run Lean or Coq on the resulting file and retain compiler output. State any extra assumptions such as classical logic, choice or function extensionality; the extensional set-like catalog convention does not automatically justify these inside an intensional type theory. Do not use an unproved placeholder as evidence of completion.

The implemented Lean project is [`lean/`](../lean/README.md). Its `lean/bindings.json` manifest is keyed by stable concept/claim IDs and records pinned versions, declarations/modules, carrier/operation/assumption and premise mappings, expected types, scope, limitations and catalog fingerprints. The Markdown formulation fields expose the selected declarations/propositions and mappings; metadata checks reject drift from the Lean sources and bindings. Use `python3 scripts/lean.py get ID` to retrieve a binding, `make check-lean` for metadata checks, and `make test-lean` for actual compilation, axiom auditing and negative compiler tests. Only fresh `lean/verification.json` evidence supports a verified witness; a model or registered binding alone does not. Hash mismatches require review before updating fingerprints. Partial models have explicit remaining obligations in the Lean manifest and guide. Keep readable mathematics usable independently of Lean and preserve its bibliographic provenance.

## Software test design

Prefer bounded retrieval when designing tests from selected catalog claims.

Use the repository-local [`mathematical-tests` skill](../ai/skills/mathematical-tests/SKILL.md) for the complete test-design workflow. Its bounded ONTFS helper avoids expanding a full dossier when only a few interface records or selected claims are needed:

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search stack --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Stack --sections operations --limit 6 --max-chars 8000
```

For a push/pop test property, retrieve `node urn:csabs:law/stack-push-pop` after selecting that obligation. Fetch a theorem only when the rationale needs its result; a scoped claim search is for discovery of a needed property, not a routine preload. Fetch Lean evidence only when relying on a formal interpretation or proof.

The projection must match current Markdown and have no local edits. Respect `nextOffset`, `needsLargerBudget` and `depthBoundary`; only fetch omitted records needed for the selected property. See the skill's retrieval reference for setup and scratch projections. The original standard-library CLI remains useful when ONTFS is unavailable, but it is a different retrieval backend and should be disclosed as such:

```sh
python3 scripts/catalog.py get Stack --sections operations
python3 scripts/agent_query.py node urn:csabs:law/stack-push-pop
```

Map the catalog carrier and operations to the real API. Check whether the interface is mutable, persistent, bounded, concurrent or exception-raising. An equation about an abstract stack needs an observation function when the software stores additional internal state.

For each applicable recorded law, produce a test plan with its claim ID, assumptions, input generator, operation sequence and expected observation. Generate only inputs that satisfy the law's preconditions. Include empty and singleton states where defined, plus boundary values and representative operation sequences. Test invalid-input behavior using the software's explicit error contract. Use a reference model for stateful properties and keep counterexamples and random seeds.

For arithmetic, retrieve the correct concept: exact integers, fixed-width unsigned integers, modular arithmetic, and floating-point numbers have different laws. Do not transplant exact associativity into rounded arithmetic or assume an overflow policy. For concurrency, specify scheduling, nondeterminism and the chosen equivalence or observation model before constructing an oracle.

Run the resulting tests against the actual implementation. Cite the claim IDs and representation assumptions in the test report. A finite set of passing examples or generated cases is not a proof of a universal law.

## Specification consistency

Use the repository-local [specification-consistency skill](../ai/skills/specification-consistency/SKILL.md) to review conflicting requirements and impossible contracts. It guides clause-to-catalog mappings, joint satisfiability, required input coverage and nonvacuity, backend selection, conflict diagnosis and evidence reporting. It includes a runnable exhaustive Boolean example and reuses the existing catalog and bounded ONTFS retrieval tools.

Invoke it by asking an agent to read that skill and check a named specification, for example: “Use `ai/skills/specification-consistency/SKILL.md` to review `path/to/spec.md`; report conflicting clause IDs, required scenarios, runnable evidence and any unchecked obligations.” The folder alone does not register the skill with every agent host.

Keep specification assumptions distinct from catalog laws and agent-added modeling assumptions. Structural validation does not establish satisfiability. A satisfying instance does not ensure every required input has an outcome, and a counterexample to one implementation does not establish specification unrealizability. Report the check's precise scope and preserve normative documents unless edits are requested.

## Implementation mapping and conformance

For code generated from a catalog-based specification, use [implementation-mapping](../ai/skills/implementation-mapping/SKILL.md) to record clause-to-API obligations before implementing them. Keep the [mapping](../ai/skills/implementation-mapping/assets/implementation-map.md) beside the target software with source versions, carriers, equality/observations, representation relation/invariants, required domains, errors and unresolved decisions. Mapping-only tasks do not imply code generation; an explicit implementation request authorizes work on resolved obligations without another routine approval step.

Use [implementation-conformance](../ai/skills/implementation-conformance/SKILL.md) to review the mapping against normative clauses and code against the mapped obligations. Preserve obligation IDs across implementation, tests and findings. Distinguish mapping defects, implementation defects, ambiguities and unchecked obligations; retain commands, results, versions and counterexample traces. Use specification-consistency for requirement conflicts and mathematical-tests for derived tests. The [stack example](../ai/skills/implementation-mapping/references/stack-example.md) illustrates the complete connection without an ONTFS runtime requirement.

## Abstraction discovery

Use the repository-local [abstraction-discovery skill](../ai/skills/abstraction-discovery/SKILL.md) to analyze unannotated code, data structures, or APIs and discover their underlying mathematical abstractions. It guides signature classification (e.g., binary reducers to `Monoid`, comparisons to `TotalOrder`, state reconciliations to `JoinSemilattice`), candidate catalog queries, and algebraic law evaluation.

Invoke it by asking: "Use `ai/skills/abstraction-discovery/SKILL.md` to inspect `path/to/code.py`; discover candidate mathematical abstractions, report broken algebraic laws or missing identity/invariants, and propose principled refactorings."

The [discovery guide](../ai/skills/abstraction-discovery/references/discovery-guide.md) outlines common code anti-patterns (such as non-associative parallel reductions, missing neutral elements, and non-transitive comparators). The [metrics aggregator example](../ai/skills/abstraction-discovery/references/metrics-example.md) demonstrates how testing monoid laws reveals subtle aggregation bugs and guides refactoring to a sound algebraic structure.

## Formal model checking

Use the repository-local [formal-model-checking skill](../ai/skills/formal-model-checking/SKILL.md) to model and verify concurrent protocols, state machines, and distributed algorithms against catalog concepts such as `Lock`, `Mutex`, `LabelledTransitionSystem`, and `LinearTemporalLogic`. It guides the formulation of state variables, atomic transition relations (`Init` and `Next`), safety invariants (e.g., mutual exclusion, type invariants), and liveness obligations (e.g., starvation freedom under weak/strong fairness).

Invoke it by asking: "Use `ai/skills/formal-model-checking/SKILL.md` to model `path/to/protocol.md` with TLA+ or Alloy; verify mutual exclusion and deadlock freedom against catalog concept `Lock`, and report any counterexample traces."

The [backend selection guide](../ai/skills/formal-model-checking/references/backend-selection.md) compares TLA+, Alloy, and Z3, and explains state-space reduction techniques (such as symmetry sets and data abstraction). The [mutex TLA+ example](../ai/skills/formal-model-checking/references/mutex-tla-example.md) includes a complete Ticket Lock specification and an executable Python state-space explorer demonstrating invariant checking and counterexample generation.

## Other uses

Use `neighbors` for educational prerequisite navigation and impact analysis. Incoming edges identify explicit dependents; they are not evidence that every possible dependent has been recorded. Use the catalog CLI or ONTFS projection for cross-disciplinary queries; external RDF tools can read the generated ONTFS Turtle projection. Edit concept Markdown records rather than the projection. `specializationOf` means an explicitly described interface specialization, while `requiresConcept` is a retrieval prerequisite and `dependsOn` connects a claim to derivation premises.

Commands default to bounded slices or explicitly chosen sections. They do not perform symbolic theorem search, semantic equivalence checking, natural-language question answering, or automatic reasoning over inheritance. An AI agent interprets the retrieved records and verifies the result in the chosen downstream tool.
