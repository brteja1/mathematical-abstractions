---
name: abstraction-acquisition
description: Fill a mathematical abstraction or proof gap encountered during a problem by reusing trusted sources or constructing a model, checking the required properties in Lean, choosing catalog or task-local retention, and returning to the original task.
---

# Acquire and verify a missing abstraction

Use this workflow when a task needs an abstraction, operation, axiom interpretation or proof that the catalog does not supply. Acquire only the mathematics needed for that task. An existing interface with a missing proof is not a missing concept, and code duplication alone need not represent a mathematical structure.

The catalog root is three levels above this skill directory, including in extracted archives. Read the target project's instructions and retain the original task, required inputs and pending obligations before starting.

## Mandatory catalog use

Read and maintain the [catalog lookup log](../mathematical-tests/references/catalog-lookup-log.md) whenever querying the catalog. Record actual commands, retrieved IDs, target mappings and misses; cover every semantic domain touched, including preserved or copied flags/attributes. Keep indexed rationales for substantive decisions, consistency arguments and tests, linked to requirements, lookups and validation evidence. Deliver the task-local log and carry it through skill handoffs. Read every fetched claim in full using `--view full`; resolve all fetch truncation before relying on results. Never pipe a claim or concept fetch through `head`, `tail` or `cut`. Deliver derivations, consistency arguments and linked evidence under `mathematical-abstractions-formal-reasoning/`; maintain its project memory note and persistent agent-context routing for subsequent modifications.

Use catalog abstractions as the mathematical basis for this workflow. Before relying on an abstraction, query it through the repository tooling and record the selected stable concept/operation/claim IDs and their semantic mapping. Names and examples in this skill are search hints, not retrieved evidence; do not substitute remembered or invented definitions or laws.

Retrieve catalog content only through `scripts/catalog.py`, `scripts/agent_query.py`, or `ai/skills/mathematical-tests/scripts/query.py` (and `scripts/lean.py get ID` for binding evidence). Do not directly open, browse, grep, glob, or parse `concepts/`, `data/shared.json`, generated catalog pages, embedded viewer data, or runtime RDF to obtain catalog facts. The tools may read those files internally. Reading instructions, target code, consulted external sources and selected Lean source declarations is separate from catalog retrieval. Direct record edits are allowed only for authorized catalog maintenance or promotion, after tool-based discovery.

If the required abstraction or applicable operation, law or proof cannot be found, **report the gap to the user before acquisition or any further dependent step**: name the need, list queries and closest matches, explain what is missing or incompatible, and identify blocked work. Resolve synonyms, relevant candidates and all truncated fetches first; distinguish unavailable tooling from absent mathematics. Do not silently fall back to general knowledge or continue on unsupported assumptions. Follow the [shared catalog-use policy](../mathematical-tests/references/catalog-use.md) for gap handling and the acquisition exceptions; read it when a gap or retrieval blocker occurs.

## Establish the gap and acquire evidence

Search the catalog by meaning, synonyms, notation and operation signatures; inspect likely matches and selected claims with the bounded tools. Follow necessary premises and resolve all fetch truncation. Reuse stable IDs and extend existing entries when appropriate. Neither prerequisites nor specialization links transfer axioms.

Read [references/acquisition.md](references/acquisition.md) for source selection, construction, proof checks and persistence. Prefer the pinned Lean/Mathlib declarations, then consulted primary papers, standards, textbooks or official formal libraries. Download only relevant material, retain its locator/revision and license, and review it before reuse. Keep dependency pins unchanged. A trusted publisher or repository is a starting point, not proof that a source entails the selected statement.

Specify carriers, equality, operations, definedness, selected axiom basis and the task's additional claims. Construct a model satisfying every axiom in that basis and prove the additional claims used by the task. Explicitly check required input coverage and nonvacuity. Importing an interface, assuming its laws as fields, or proving an implication from inconsistent hypotheses does not establish model satisfaction. Absolute consistency and foundational axioms are not proof targets for this workflow.

Compile with the pinned environment and audit the actual theorem declarations and transitive axiom dependencies. No `sorry`, fabricated axioms, assumed target results or silent hypothesis strengthening. Reuse the existing catalog witness mechanism for promoted proofs; task-local proofs use the same audit command without claiming catalog registration. See the [worked example](references/watermark-example.md).

## Choose retention and return to the problem

Prepare sourced definitions, semantic mappings, proofs, compiler/audit output and proposed catalog changes before presenting the retention choice. After verification, offer **Promote to catalog (default)** or **Keep with this task**. Wait for the selection; the default is a recommendation, not consent. Honor an explicit choice already made in the session without asking again. This choice is required by this workflow; name this skill when asking it.

For promotion, maintain the authoritative Markdown JSON, direct provenance, hierarchy, formulations and model/witness bindings, then run the repository's graph and Lean checks. Keep Axioms as assumptions/defining constraints; register concrete model-satisfaction results as separate Theorems with explicit mappings to those axioms. For task-local retention, keep artifacts beside the problem and identify reused graph IDs separately from local claim IDs.

Resume the original skill and task using a versioned mapping from the acquired operations and proved propositions to its inputs, API or specification. Refresh task queries after promotion against a fresh projection. Mathematical model satisfaction does not prove implementation refinement, runtime behavior or model-checker translation correctness.

If a trusted source, model or proof is unavailable, identify the exact unsupported obligation and continue independent work. Offer an alternative abstraction, a revised requirement, or conditional continuation with explicit unverified assumptions. Continue on assumptions only after the user chooses that option; keep conditional results separate from verified evidence. Do not promote an unverified candidate under this workflow or loop indefinitely on an unavailable dependency.

## Lifecycle evidence integration

For an authorized end-to-end assurance task, use [spec-driven-development](../spec-driven-development/SKILL.md) and its [shared ledger guide](../spec-driven-development/references/assurance.md). Preserve requirement/obligation IDs, exact inputs and evidence kinds. A model proof, finite test, review receipt and actual-source refinement prove different things; required missing or stale evidence blocks admission. This integration does not expand the user's requested scope.
