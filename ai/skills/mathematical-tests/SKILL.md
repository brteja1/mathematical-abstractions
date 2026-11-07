---
name: mathematical-tests
description: Create runnable software tests from the mathematical abstractions catalog, using bounded ONTFS queries to select applicable concepts, operations, axioms and laws and map them to the target API.
---

# Tests from mathematical abstractions

Use this skill when mathematical interfaces can guide tests for software code: collections, numeric operations, transformations, state machines, relations, or concurrent behavior. Produce tests in the target software's existing harness, with a reviewable mapping from catalog claims to its actual contract.

## Read the software before selecting mathematics

Read the target repository's instructions, relevant code, public contract and nearby tests. Establish the input/output carriers, state changes, observation/equality function, error behavior and applicable numeric or concurrency conventions. Select concepts by behavior rather than matching class names. A method called `add` does not by itself imply a group or exact arithmetic.

## Retrieve small slices through ONTFS

Resolve this skill's actual directory and use absolute paths when working in another software repository. `<catalog>` is the checkout containing this skill; `<skill>` is this directory. Prefer `<catalog>/.venv/bin/python` when installed, otherwise a Python with the catalog's ONTFS dependencies. Setup and query details are in [references/retrieval.md](references/retrieval.md); read it if the backend is unavailable or pagination needs explanation.

```sh
python3 <skill>/scripts/query.py search queue --limit 4 --max-chars 4000
python3 <skill>/scripts/query.py interface Queue --sections operations axioms --limit 6 --max-chars 8000
python3 <skill>/scripts/query.py claims Queue --kind law --limit 3 --max-chars 6000
python3 <skill>/scripts/query.py node urn:csabs:law/queue-fifo --max-chars 6000
python3 <skill>/scripts/query.py premises urn:csabs:law/queue-fifo --depth 1 --limit 6 --max-chars 8000
```

Search returns candidate names and IDs, not a test specification. Retrieve the chosen interface and only the claims relevant to the behavior under test. Prefer a selected `node` over a broad dossier. Follow `requiresConcept` when its definitions are needed and `dependsOn` for the selected claim's premises. Concept specializations never silently transfer axioms. Retrieve direct source records with `sources ID` when evidence quality matters.

The wrapper uses ONTFS/SPARQL for selection and typed links, checks the generated projection against current Markdown, and returns lossless source records. Python may load the catalog internally; the agent receives only the bounded response. Do not dump `catalog.jsonld`, runtime Turtle, every concept page or an unrestricted SPARQL result into context. A stale/modified projection is an error, not permission to query it or overwrite local experiments.

Read `truncated`, `nextOffset`, `depthBoundary` and `needsLargerBudget`. Fetch another page only when its omitted records are needed. Follow a relevant missing premise by ID, or deepen that premise query. A response with `needsLargerBudget: true` made no progress: increase the character budget for that node rather than repeating its offset. Never treat a clipped page, unresolved premise, empty section or absent citation as mathematical completeness.

## Translate claims into test obligations

For each selected axiom/law/theorem, record the stable ID, its assumptions and definedness, the code operations implementing it, the observation/equality used, and any representation or semantic differences. Map **every operation used in the property**, including constructors, observers and partial results. If multiple methods mutate the same object, model before/after states explicitly.

Use a small table or comments alongside the tests. Do not invent a software guarantee because the graph records a stronger mathematical abstraction. If the target contract does not satisfy a premise, choose a better abstraction, restrict the test's domain with justification, or defer that property and explain the mismatch. Contradictory catalog wording or unclear code contracts require resolution before treating the disputed statement as an oracle.

Read the relevant parts of [references/test-design.md](references/test-design.md) for stateful, numeric, nondeterministic or concurrent APIs. Use only the branches that apply.

## Implement and run meaningful tests

Use the existing framework. Choose examples, generated properties, metamorphic relations or model-based operation sequences according to the contract and failure modes. An independent simple reference model is useful when a direct expected-result oracle is unavailable. Reuse an installed property-testing library where appropriate; seeded generated loops also work without a new dependency.

Generate valid inputs under the selected claim's preconditions and exercise meaningful empty, singleton, boundary and composition cases. Test invalid inputs against the **software's** documented error contract, not an arbitrary extension of an undefined mathematical operation. Avoid implementation-mirroring checks or properties that pass vacuously; exercise generators/preconditions with nonempty valid domains. Preserve a failing seed, input or operation sequence and use shrinking/minimization when available.

Run the relevant tests and required target checks. Report the actual commands/results and any blockers. Failing tests may expose either a code defect or a bad abstraction mapping: distinguish them using the contract and counterexample before changing production code. A request for tests alone does not authorize changing behavior to satisfy an inapplicable law.

## Keep evidence explicit

Preserve source locators and `provenanceStatus` for claims used in a test rationale. Legacy citation gaps are not repaired by a passing test. A Lean witness, when relevant, can support the mapped mathematical proposition: inspect it with `<catalog>/scripts/lean.py get ID` and require fresh verification evidence before calling it compiled. It does not prove that the target implementation refines that model.

Deliver the test files, chosen concept/claim IDs and API mapping, tested preconditions/edge cases, execution evidence and any deferred properties. Tests provide finite evidence; do not report universal mathematical or implementation proofs. Catalog edits, proof promotion and ONTFS proposals are separate work from generating tests.
