# Agent workflows

Use the graph as a retrieved specification and dependency map. Keep assumptions and source quality visible in the resulting work.

## Proof construction with Lean or Coq

For a group identity, first retrieve the exact group interface:

```sh
python3 scripts/catalog.py get Group --sections operations axioms laws theorems
python3 scripts/agent_query.py dossier Group --purpose proof --limit 100
```

Read the target theorem's `formalStatement`, `assumptions`, `appliesTo`, `dependsOn`, `reviewStatus`, and provenance. Follow each needed premise by ID with `agent_query.py node ID`. If a dossier reports `truncated: true`, retrieve missing premises separately or increase the limit (maximum 1000).

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

The implemented Lean project is [`lean/`](../lean/README.md). Its separate `lean/bindings.json` manifest is keyed by stable concept/claim IDs and records pinned versions, declarations/modules, carrier/operation/assumption and premise mappings, expected types, scope, limitations and catalog fingerprints. Use `python3 scripts/lean.py get ID` to retrieve a binding, `make check-lean` for metadata checks, and `make test-lean` for actual compilation, axiom auditing and negative compiler tests. Only fresh `lean/verification.json` evidence supports a verified witness; a model or registered binding alone does not. Hash mismatches require review before updating fingerprints. The 13 partial models have explicit remaining obligations. Add bindings to the JSON-LD context only through a reviewed schema change; keep informal mathematics usable independently of Lean.

## Software test design

Prefer bounded retrieval when designing tests from selected catalog claims.

Use the repository-local [`mathematical-tests` skill](../ai/skills/mathematical-tests/SKILL.md) for the complete test-design workflow. Its bounded ONTFS helper avoids expanding a full dossier when only a few interface records or selected claims are needed:

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search stack --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Stack --sections operations axioms --limit 6 --max-chars 8000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py claims Stack --kind law --limit 3 --max-chars 6000
```

The projection must match current Markdown and have no local edits. Respect `nextOffset`, `needsLargerBudget` and `depthBoundary`; only fetch omitted records needed for the selected property. See the skill's retrieval reference for setup and scratch projections. The original standard-library CLI remains useful when ONTFS is unavailable, but it is a different retrieval backend and should be disclosed as such:

```sh
python3 scripts/catalog.py get Stack --sections operations axioms laws theorems dependencies
python3 scripts/agent_query.py dossier Stack --purpose tests --limit 100
```

Map the catalog carrier and operations to the real API. Check whether the interface is mutable, persistent, bounded, concurrent or exception-raising. An equation about an abstract stack needs an observation function when the software stores additional internal state.

For each applicable recorded law, produce a test plan with its claim ID, assumptions, input generator, operation sequence and expected observation. Generate only inputs that satisfy the law's preconditions. Include empty and singleton states where defined, plus boundary values and representative operation sequences. Test invalid-input behavior using the software's explicit error contract. Use a reference model for stateful properties and keep counterexamples and random seeds.

For arithmetic, retrieve the correct concept: exact integers, fixed-width unsigned integers, modular arithmetic, and floating-point numbers have different laws. Do not transplant exact associativity into rounded arithmetic or assume an overflow policy. For concurrency, specify scheduling, nondeterminism and the chosen equivalence or observation model before constructing an oracle.

Run the resulting tests against the actual implementation. Cite the claim IDs and representation assumptions in the test report. A finite set of passing examples or generated cases is not a proof of a universal law.

## Specification consistency

Use the repository-local [specification-consistency skill](../ai/skills/specification-consistency/SKILL.md) to review conflicting requirements and impossible contracts. It guides clause-to-catalog mappings, joint satisfiability, required input coverage and nonvacuity, backend selection, conflict diagnosis and evidence reporting. It includes a runnable exhaustive Boolean example and reuses the existing catalog and bounded ONTFS retrieval tools.

Invoke it by asking an agent to read that skill and check a named specification, for example: “Use `ai/skills/specification-consistency/SKILL.md` to review `path/to/spec.md`; report conflicting clause IDs, required scenarios, runnable evidence and any unchecked obligations.” The folder alone does not register the skill with every agent host.

Keep specification assumptions distinct from catalog laws and agent-added modeling assumptions. Structural validation does not establish satisfiability. A satisfying instance does not ensure every required input has an outcome, and a counterexample to one implementation does not establish specification unrealizability. Report the check's precise scope and preserve normative documents unless edits are requested.

## Other uses

Use `neighbors` for educational prerequisite navigation and impact analysis. Incoming edges identify explicit dependents; they are not evidence that every possible dependent has been recorded. Use the catalog CLI or ONTFS projection for cross-disciplinary queries; external RDF tools can read the generated ONTFS Turtle projection. Edit concept Markdown records rather than the projection. `specializationOf` means an explicitly described interface specialization, while `requiresConcept` is a retrieval prerequisite and `dependsOn` connects a claim to derivation premises.

Commands default to bounded slices or explicitly chosen sections. They do not perform symbolic theorem search, semantic equivalence checking, natural-language question answering, or automatic reasoning over inheritance. An AI agent interprets the retrieved records and verifies the result in the chosen downstream tool.
