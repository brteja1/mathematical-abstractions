---
name: abstraction-acquisition
description: Fill a mathematical abstraction or proof gap encountered during a problem by reusing trusted sources or constructing a model, checking the required properties in Lean, choosing catalog or task-local retention, and returning to the original task.
---

# Acquire and verify a missing abstraction

Use this workflow when a task needs an abstraction, operation, axiom interpretation or proof that the catalog does not supply. Acquire only the mathematics needed for that task. An existing interface with a missing proof is not a missing concept, and code duplication alone need not represent a mathematical structure.

The catalog root is three levels above this skill directory, including in extracted archives. Read the target project's instructions and retain the original task, required inputs and pending obligations before starting.

## Establish the gap and acquire evidence

Search the catalog by meaning, synonyms, notation and operation signatures; inspect likely matches and selected claims with the bounded tools. Follow necessary premises and resolve truncation. Reuse stable IDs and extend existing entries when appropriate. Neither prerequisites nor specialization links transfer axioms.

Read [references/acquisition.md](references/acquisition.md) for source selection, construction, proof checks and persistence. Prefer the pinned Lean/Mathlib declarations, then consulted primary papers, standards, textbooks or official formal libraries. Download only relevant material, retain its locator/revision and license, and review it before reuse. Keep dependency pins unchanged. A trusted publisher or repository is a starting point, not proof that a source entails the selected statement.

Specify carriers, equality, operations, definedness, selected axiom basis and the task's additional claims. Construct a model satisfying every axiom in that basis and prove the additional claims used by the task. Explicitly check required input coverage and nonvacuity. Importing an interface, assuming its laws as fields, or proving an implication from inconsistent hypotheses does not establish model satisfaction. Absolute consistency and foundational axioms are not proof targets for this workflow.

Compile with the pinned environment and audit the actual theorem declarations and transitive axiom dependencies. No `sorry`, fabricated axioms, assumed target results or silent hypothesis strengthening. Reuse the existing catalog witness mechanism for promoted proofs; task-local proofs use the same audit command without claiming catalog registration. See the [worked example](references/watermark-example.md).

## Choose retention and return to the problem

Prepare sourced definitions, semantic mappings, proofs, compiler/audit output and proposed catalog changes before presenting the retention choice. After verification, offer **Promote to catalog (default)** or **Keep with this task**. Wait for the selection; the default is a recommendation, not consent. Honor an explicit choice already made in the session without asking again. This choice is required by this workflow; name this skill when asking it.

For promotion, maintain the authoritative Markdown JSON, direct provenance, hierarchy, formulations and model/witness bindings, then run the repository's graph and Lean checks. Keep Axioms as assumptions/defining constraints; register concrete model-satisfaction results as separate Theorems with explicit mappings to those axioms. For task-local retention, keep artifacts beside the problem and identify reused graph IDs separately from local claim IDs.

Resume the original skill and task using a versioned mapping from the acquired operations and proved propositions to its inputs, API or specification. Refresh task queries after promotion against a fresh projection. Mathematical model satisfaction does not prove implementation refinement, runtime behavior or model-checker translation correctness.

If a trusted source, model or proof is unavailable, identify the exact unsupported obligation and continue independent work. Offer an alternative abstraction, a revised requirement, or conditional continuation with explicit unverified assumptions. Continue on assumptions only after the user chooses that option; keep conditional results separate from verified evidence. Do not promote an unverified candidate under this workflow or loop indefinitely on an unavailable dependency.
