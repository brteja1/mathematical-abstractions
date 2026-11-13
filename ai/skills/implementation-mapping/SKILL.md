---
name: implementation-mapping
description: Map specifications modeled with the mathematical abstractions catalog to concrete software types, APIs, state representations and implementation obligations. Use before generating or changing code from a catalog-based specification.
---

# Map a model to software

Produce a versioned implementation mapping beside the target software. The mapping connects normative specification clauses and selected catalog records to concrete behavior; it is not a replacement specification or a proof. Generate code only when requested by the task, using the resolved mapping.

## Establish the contract

Read the target repository's instructions, specification, existing API and nearby tests. Preserve clause IDs and locators; assign local IDs when absent. Record document revisions or content hashes. Separate normative requirements, catalog definitions, environment assumptions, agent proposals and unresolved choices. Existing code is evidence about implementation, not authority to weaken a requirement.

If a mapping already exists, update it rather than creating a competing interpretation. Use [assets/implementation-map.md](assets/implementation-map.md) as a starting point when none exists; adapt its detail to the component. Store completed mappings in the target project, outside this catalog's authoritative records. Preserve the normative text unless specification changes are requested.

## Retrieve the selected semantics

The catalog dependency is located relative to this skill file's directory: starting from `<skill_dir>` (the directory containing this `SKILL.md`), the catalog root is three levels up at `<skill_dir>/../../..`. This relative structure is preserved whether cloned or extracted from an archive or zip without requiring git.

First verify catalog availability with Python's standard library:

```sh
python3 <skill_dir>/../../../scripts/catalog.py check
```

Then query concepts and operations using standard-library commands:

```sh
python3 <skill_dir>/../../../scripts/catalog.py list --search stack
python3 <skill_dir>/../../../scripts/catalog.py get Stack --sections operations
```

Search by behavior and synonyms. Start with the selected concept and relevant operations. Retrieve an axiom or law only to resolve a current interface obligation; fetch a theorem only when a required result or proof needs it. Follow premises only to check applicability or a derivation, and sources when checking provenance. Do not prefetch all claims or a prerequisite closure. For bounded ONTFS retrieval, use the existing [retrieval helper and guide](../mathematical-tests/references/retrieval.md). Disclose the backend used. Respect pagination, truncation and depth boundaries; retrieve necessary omitted premises. Do not overwrite modified projections. Prerequisites and specialization links do not transfer axioms.

Record selected stable IDs and source-file hashes or a catalog revision plus relevant dirty-file hashes. Preserve source locators, citation gaps and review status. A graph edge, Unicode equation or Lean binding is not evidence that the software conforms.

Use the focused `mathematicalFormulation`, scope and limitations to map the contract. Load `--view lean` and the relevant part of the [formulation guide](../mathematical-tests/references/formulations.md) only when a typed interpretation or witness is needed; `--view full` is for a required complete-record audit. Record only relied-on equations and evidence. A partial interface leaves explicit obligations; it does not authorize narrowing the product contract.

## Define the concrete interpretation

For each selected operation, map all of the following that affect its behavior:

- Abstract carriers to language types, admissible values, units and numeric ranges.
- Abstract equality to an explicit observation/equivalence, including identity, aliasing and mutable before/after state where relevant.
- Concrete state to abstract state through an abstraction function or relation, with a representation invariant and initial states.
- Constructors, updates and observers to API symbols, argument/result order, preconditions, allowed outcomes, errors and failure-state guarantees.
- Totality/termination, allocation or capacity limits, overflow/rounding, nondeterminism and concurrency guarantees where relevant.

An operation refinement obligation is: related valid initial states and a permitted input lead to outcomes allowed by the abstract contract, and successful concrete states remain related and valid. Account for permitted failures explicitly. Termination and progress require separate obligations when promised. For nondeterministic operations, all possible implementation outcomes must be permitted; implementing every permitted outcome is not generally required. Concurrent operations require a history/observation model rather than just sequential equations.

Write traceable obligations with local IDs and acceptance evidence. Include constructor establishment, invariant preservation, operation simulation, definedness and required input coverage as applicable. Mark each choice as required, justified design choice, or unresolved; do not describe proposed semantics as approved requirements. Read [references/stack-example.md](references/stack-example.md) for a total-operation/capacity mismatch and a worked mapping.

## Handle mismatches and generate within scope

Do not silently narrow a required input domain, change equality, add failure outcomes, strengthen preconditions or import extra catalog laws. Explain a mismatch and its behavioral alternatives. Ask only when a consequential unresolved choice blocks dependent work; continue independent mapping and implementation. Ordinary representation choices consistent with the contract do not require an approval round.

If requirements appear inconsistent, use the existing [specification-consistency skill](../specification-consistency/SKILL.md) for that analysis. A missing decision is not itself a contradiction.

When code generation is requested, use the target project's language, conventions and dependencies. Implement resolved obligations, including error paths and observers, and retain obligation-to-symbol links in the mapping. Do not add catalog/ONTFS runtime dependencies unless the software actually requires them. A partial implementation must identify remaining obligations; do not present it as complete.

## Deliver and check

Deliver the mapping, unresolved decisions and, when requested, code and relevant execution results. Use [mathematical-tests](../mathematical-tests/SKILL.md) for derived tests and [implementation-conformance](../implementation-conformance/SKILL.md) for comparison against the mapping. Run appropriate target checks for code changes. Mapping alone does not require installing a solver or running this catalog's full build.

Distinguish static inspection, tests, bounded exploration and compiled proofs. Formal proof of the abstract model does not establish its relation to this implementation. Skills in `ai/skills/` can be read explicitly; automatic discovery depends on the agent host.
