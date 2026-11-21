---
name: compositional-verification
description: Verify that component contracts and their connections imply a system contract, with explicit interference, compatibility and progress obligations.
---

# Compositional Verification

Identify the system boundary, components, shared state, call/event interfaces and scheduler/environment. Retrieve relevant catalog interfaces before choosing a composition rule. Component proofs alone do not establish system behavior.

Write each component's assumptions and guarantees and the system obligations. Map actual carriers, equality, observations, initial states, ownership and operation ordering across boundaries. Establish initial feasibility, wiring/type compatibility, invariant preservation, discharge of each component assumption, and absence of circular assume-guarantee reasoning. An obligation cycle is rejected by the ledger; a legitimate cyclic system needs a separately proved induction/fixed-point rule rather than a circular evidence graph.

Treat interference, shared mutable state, resource exhaustion and error propagation explicitly. Sequential postcondition/precondition matching requires frame and alias conditions; asynchronous composition requires history/message semantics. Component safety does not establish global deadlock freedom, liveness, fairness or timing. Keep each as a separate obligation and use formal-model-checking where appropriate.

Encode dependency edges from a system obligation to every relied-on component obligation. Run interface checks and bounded adverse interleavings when useful; obtain a composition theorem for universal claims. No general composition or frame-rule backend is supplied by this skill. Report missing rules before acquisition or dependent work. Deliver connection mappings, discharged assumptions, evidence and remaining system obligations.

## Catalog and evidence discipline

Read the [shared lifecycle and ledger guide](../spec-driven-development/references/assurance.md) for the executable contract, commands, pilot and limits. Reuse existing target mappings; do not create competing specifications.

Retrieve mathematical facts only through `python3 <catalog>/scripts/catalog.py list --search TERM`, focused `get` sections, `scripts/agent_query.py node ID` or the bounded mathematical-tests helper. Here `<catalog>` is three directories above this skill directory. Follow necessary premises explicitly and resolve truncation. Do not browse catalog storage or generated exports for facts. Prerequisites and hierarchy confer no axioms or proof evidence.

Report required mathematical gaps before acquisition or dependent steps, including searched queries, candidates, mismatch and blocked work. Follow [catalog-use](../mathematical-tests/references/catalog-use.md) and [abstraction-acquisition](../abstraction-acquisition/SKILL.md). A retrieval/backend failure is a tooling blocker: resolve setup first and use a fallback only when the active skill permits it; do not treat it as absent mathematics. Do not silently continue on unsupported assumptions. Preserve provenance and pinned dependencies. Read the [formulation guide](../mathematical-tests/references/formulations.md) only when typed correspondence or witness evidence is needed.
