---
name: mathematical-tests
description: Create runnable software tests from the mathematical abstractions catalog, using bounded ONTFS queries to select applicable concepts, operations, axioms and laws and map them to the target API.
---

# Tests from mathematical abstractions

Use this skill when mathematical interfaces can guide tests for software code: collections, numeric operations, transformations, state machines, relations, or concurrent behavior. Produce tests in the target software's existing harness, with a reviewable mapping from catalog claims to its actual contract.

## Mandatory catalog use

Use catalog abstractions as the mathematical basis for this workflow. Before relying on an abstraction, query it through the repository tooling and record the selected stable concept/operation/claim IDs and their semantic mapping. Names and examples in this skill are search hints, not retrieved evidence; do not substitute remembered or invented definitions or laws.

Retrieve catalog content only through `scripts/catalog.py`, `scripts/agent_query.py`, or `ai/skills/mathematical-tests/scripts/query.py` (and `scripts/lean.py get ID` for binding evidence). Do not directly open, browse, grep, glob, or parse `concepts/`, `data/shared.json`, generated catalog pages, embedded viewer data, or runtime RDF to obtain catalog facts. The tools may read those files internally. Reading instructions, target code, consulted external sources and selected Lean source declarations is separate from catalog retrieval. Direct record edits are allowed only for authorized catalog maintenance or promotion, after tool-based discovery.

If the required abstraction or applicable operation, law or proof cannot be found, **report the gap to the user before acquisition or any further dependent step**: name the need, list queries and closest matches, explain what is missing or incompatible, and identify blocked work. Resolve synonyms, relevant candidates and necessary truncated results first; distinguish unavailable tooling from absent mathematics. Do not silently fall back to general knowledge or continue on unsupported assumptions. Follow the [shared catalog-use policy](../mathematical-tests/references/catalog-use.md) for gap handling and the acquisition exceptions; read it when a gap or retrieval blocker occurs.

## Read the software before selecting mathematics

Read the target repository's instructions, relevant code, public contract and nearby tests. Establish the input/output carriers, state changes, observation/equality function, error behavior and applicable numeric or concurrency conventions. Select concepts by behavior rather than matching class names. A method called `add` does not by itself imply a group or exact arithmetic.

## Retrieve small slices through ONTFS

The catalog dependency is located relative to this skill file's directory: starting from `<skill_dir>` (the directory containing this `SKILL.md`), the catalog root is three levels up at `<skill_dir>/../../..`. This relative structure works from git checkouts or unzipped source archives alike.

Verify catalog availability before querying:

```sh
python3 <skill_dir>/../../../scripts/catalog.py check
```

Prefer `<skill_dir>/../../../.venv/bin/python` when installed, otherwise a Python with the catalog's ONTFS dependencies. Setup and query details are in [references/retrieval.md](references/retrieval.md); read it if the backend is unavailable or pagination needs explanation.

```sh
python3 <skill_dir>/scripts/query.py search queue --limit 4 --max-chars 4000
python3 <skill_dir>/scripts/query.py interface Queue --sections operations --limit 6 --max-chars 8000
```

Search returns candidate names and IDs, not a test specification. Start with the selected concept and relevant operations. Fetch a selected axiom/law only when it supplies a test property or resolves applicability; fetch a theorem only when the test rationale needs that result. For example, use `node urn:csabs:law/queue-fifo` for a FIFO obligation, then `premises ... --depth 1` only when its derivation or assumptions need checking. A scoped `claims` query can discover a needed property; do not load every claim by default. Follow prerequisites only for missing definitions and sources only when checking provenance. Concept specializations never silently transfer axioms.

The default focused view keeps readable formulations, preconditions, assumptions and partial-model limits, while omitting unselected claim links, Lean excerpts and proof sketches. Use it for ordinary test design. Retrieve `--view lean` and the relevant part of the [formulation guide](references/formulations.md) only when typed interpretation or witness reuse affects the task; request `--view full` only for a complete-record audit. A local Lean source does not close a citation gap or establish the software's behavior.

The wrapper uses ONTFS/SPARQL for selection and typed links, checks the generated projection against current Markdown, and returns the requested field view without shortening retained mathematical conditions. Python may load the catalog internally; the agent receives only the bounded response. Do not dump runtime Turtle, every concept page or an unrestricted SPARQL result into context. A stale/modified projection is an error, not permission to query it or overwrite local experiments.

Read `truncated`, `nextOffset`, `depthBoundary` and `needsLargerBudget`. Fetch another page only when its omitted records are needed. Follow a relevant missing premise by ID, or deepen that premise query. A response with `needsLargerBudget: true` made no progress: increase the character budget for that node rather than repeating its offset. Never treat a clipped page, unresolved premise, empty section or absent citation as mathematical completeness.

## Fill a required mathematical gap

After reporting a required catalog gap under the mandatory policy above, use [abstraction-acquisition](../abstraction-acquisition/SKILL.md). Search for reusable entries first, acquire or construct only the missing mathematics, and compile/audit the required Lean model and claims. After verification, offer catalog promotion (default) or task-local retention and wait for the user's choice unless already specified. Then resume this workflow with the explicit semantic mapping. Unverified assumptions require an explicit user choice for conditional continuation.

## Translate claims into test obligations

For each selected axiom/law/theorem, record the stable ID, its assumptions and definedness, the code operations implementing it, the observation/equality used, and any representation or semantic differences. Map **every operation used in the property**, including constructors, observers and partial results. If multiple methods mutate the same object, model before/after states explicitly.

Use a small table or comments alongside the tests. Do not invent a software guarantee because the graph records a stronger mathematical abstraction. If the target contract does not satisfy a premise, choose a better abstraction, restrict the test's domain with justification, or defer that property and explain the mismatch. Contradictory catalog wording or unclear code contracts require resolution before treating the disputed statement as an oracle.

Read the relevant parts of [references/test-design.md](references/test-design.md) for stateful, numeric, nondeterministic or concurrent APIs. Use only the branches that apply.

## Implement and run meaningful tests

Use the existing framework. Choose examples, generated properties, metamorphic relations or model-based operation sequences according to the contract and failure modes. An independent simple reference model is useful when a direct expected-result oracle is unavailable. Reuse an installed property-testing library where appropriate; seeded generated loops also work without a new dependency.

Generate valid inputs under the selected claim's preconditions and exercise meaningful empty, singleton, boundary and composition cases. Test invalid inputs against the **software's** documented error contract, not an arbitrary extension of an undefined mathematical operation. Avoid implementation-mirroring checks or properties that pass vacuously; exercise generators/preconditions with nonempty valid domains. Preserve a failing seed, input or operation sequence and use shrinking/minimization when available.

Run the relevant tests and required target checks. Report the actual commands/results and any blockers. Failing tests may expose either a code defect or a bad abstraction mapping: distinguish them using the contract and counterexample before changing production code. A request for tests alone does not authorize changing behavior to satisfy an inapplicable law.

## Keep evidence explicit

Preserve source locators and `provenanceStatus` for claims used in a test rationale. Legacy citation gaps are not repaired by a passing test. A Lean witness, when relevant, can support the mapped mathematical proposition: inspect it with `<skill_dir>/../../../scripts/lean.py get ID` and require fresh verification evidence before calling it compiled. It does not prove that the target implementation refines that model.

Deliver the test files, chosen concept/claim IDs and API mapping, tested preconditions/edge cases, execution evidence and any deferred properties. Tests provide finite evidence; do not report universal mathematical or implementation proofs. Keep test artifacts outside authoritative graph records. For a required mathematical gap, the acquisition workflow handles optional catalog promotion before test design resumes.

## Lifecycle evidence integration

For an authorized end-to-end assurance task, use [spec-driven-development](../spec-driven-development/SKILL.md) and its [shared ledger guide](../spec-driven-development/references/assurance.md). Preserve requirement/obligation IDs, exact inputs and evidence kinds. A model proof, finite test, review receipt and actual-source refinement prove different things; required missing or stale evidence blocks admission. This integration does not expand the user's requested scope.
