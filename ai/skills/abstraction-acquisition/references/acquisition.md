# Acquisition, proof and retention

Read the section relevant to the current gap. The catalog root is four levels above this reference directory. Existing [retrieval guidance](../../mathematical-tests/references/retrieval.md), [formulation guidance](../../mathematical-tests/references/formulations.md), and the [Lean guide](../../../../lean/README.md) remain authoritative for those interfaces.

## Identify the missing obligation

Retain a short task record: original request, selected catalog IDs, required operations/inputs, gap, semantic mapping, evidence and pending work. Search names, synonyms, notation and mathematical meaning using `scripts/catalog.py list --search TERM`; retrieve likely concepts' operations and relevant claims, then `scripts/agent_query.py node ID` for specific records. A zero-result keyword search is insufficient to establish absence. An ONTFS failure is a backend problem, not a mathematical gap; authoritative Markdown queries remain available.

Distinguish these cases:

| Gap | Action |
| --- | --- |
| Existing abstraction and sufficient evidence | Reuse it and return immediately; no acquisition or retention prompt. |
| Existing abstraction, missing operation/model/proof | Extend that interface or add the needed witness; preserve concept identity. |
| Existing concept expresses a different convention | State the mismatch; use a justified explicit variant or another abstraction. |
| Genuinely missing abstraction | Acquire a definition or construct one from existing sourced primitives. |
| Structural refactoring without mathematical laws | Return to abstraction discovery; do not invent algebraic structure. |

## Select and consult sources

1. Search installed sources at the pinned Lean/Mathlib revision first. Inspect actual declarations and imports, including their hypotheses and semantics; a theorem name or generated index alone is insufficient. Record the repository, revision, file and declaration.
2. Consult original papers, standards, textbooks or official maintained libraries for the selected mathematical definition and claims. Check authorship/version and precise sections or theorem numbers. A search result, an adjacent entry's citation or a plausible URL is not consultation.
3. Download only needed documents or source files into task scratch space. Record origin, revision or content hash, actual consultation date, locator and what is reused/adapted. Check licensing/attribution before copying code or text. Consulted mathematical sources and executable Lean formulation sources serve separate roles.
4. Review external Lean code as proof source, including transitive imports and axioms; do not execute downloaded setup scripts. Use libraries already compatible with the pinned environment or adapt the relevant proof locally. An acquisition request does not authorize changing Lean/Mathlib/ONTFS pins or silently adding unpinned dependencies.

For a constructed abstraction, cite consulted sources for its primitives and assumptions; label the composition and its claims as derived and explain the derivation. Do not imply the source states the newly designed abstraction. New graph Concepts, Axioms, Laws and Theorems each need direct Source links, `sourceLocator`, `sourceNote`, and `provenanceKind`. New Sources need a title, URL/path/full citation, actual `accessedOn`, and `sourceRole`. Preserve legacy gaps; never add candidates to the legacy baseline. If provenance cannot be supplied, retain the candidate locally and report the blocker.

## Build the interpretation and prove model satisfaction

Record carrier ranges, equality, operation signatures, preconditions/outcomes, empty cases and totality. Include relevant numeric, nondeterministic, concurrency and fairness conventions. Select the basis explicitly; do not prove only convenient laws while claiming a stronger abstraction. Limit the scope of a partial model to the part actually covered by proofs.

Translate each selected axiom into a predicate on the chosen carrier and operations. Build an actual inhabitant of the model structure, or prove the conjunction of those predicates for specified operations. Defining a structure with law fields alone merely assumes those laws. A generic theorem under `[Group G]`, for example, is reusable evidence about groups but does not construct a group for the task's carrier.

Model satisfaction is relative to Lean's foundations and any explicitly parameterized background assumptions. Do not attempt to prove foundational axioms, absolute consistency, or universal semantic soundness merely from a model binding. If a rule system has semantics and a soundness theorem is needed, state and prove that theorem separately; one model is not that metatheorem.

Prove additional task-required claims from explicit premises. Preserve equality, quantifiers and definedness when reviewing expected types independently of proof bodies. Check that assumptions have realizations supporting the task's required inputs and outcomes. Empty or singleton carriers can be mathematically valid but cannot justify a task needing distinct states. Assuming the desired conclusion, or a false premise, is not evidence for unconditional application.

## Compile and audit

Use the pinned `lean/` environment; inspect its toolchain and Lake locks. Keep drafts beside the task or in scratch space until ready. Do not add drafts to `Catalog.lean` or mutate installed dependencies. Check dependency cleanliness/revisions with the existing `scripts/lean.py` dependency checks before relying on them.

For a task-local proof file, import `Catalog.Audit` and use `#catalog_witness Qualified.theoremName` on **every** satisfaction and downstream theorem relied upon. This checks theorem declarations and rejects transitive nonstandard axioms, including `sorryAx`; compile with warnings as errors. Add explicit `example : EXPECTED_TYPE := @Qualified.theoremName` checks after reviewing the types. For an imported module, follow the verifier's `import all` pattern so audit sees theorem bodies rather than opaque facades. The [worked example](watermark-example.md) contains executable commands.

Retain commands, exit codes, compiler output, actual audited axioms, Lean version, locked and installed dependency revisions, input hashes, exact propositions, mappings and limitations. Verify the sources and locks have not changed during the run. Only `{propext, Quot.sound, Classical.choice}` are allowed foundational names by the existing audit; record which each proof uses. Task-local evidence is valid only for those recorded inputs and is not `lean/verification.json` or a catalog `verificationFresh` result. Recompile after relevant changes. A compilation failure, missing audit result, unavailable toolchain or stale report leaves the proof unverified.

## Offer retention after verification

Present the prepared model, sources, proved properties, remaining limits and proposed promotion scope, then ask:

> The abstraction and required proofs are ready. Retain them by promoting to the catalog (default), or keep them with this task?

Wait for selection unless the user already chose retention explicitly. No reply does not select the default. Explain that this choice comes from [the acquisition skill](../SKILL.md). Do not ask about retention when an existing abstraction/evidence can simply be reused.

**Promote to catalog:** recheck duplicate IDs and hierarchy; edit only authoritative marked records and shared source data. Keep defining Axiom records intact. Add a separately named model-satisfaction Theorem with a proposition about the concrete interpretation, direct `dependsOn` links to the selected constraints and a mapping that explains these are *proved obligations*, not hypotheses postulating their own satisfaction. Additional derived claims need their own premise mappings. Consulted mathematical provenance remains separate from local formulation evidence. Supply readable and Lean formulations and model/witness bindings with reviewed expected types, limitations and fingerprints. Do not refresh unrelated hashes or alter baseline/import manifests.

Run `make build`, `make test`, `make test-rdf`, `make check-lean`, and `make test-lean`. Inspect individual promoted witnesses with `scripts/lean.py get ID`, requiring fresh evidence. Preserve modified runtime graphs and dependency edits; report build blockers rather than overwrite them. Catalog promotion is complete only when required checks pass. If it is blocked, retain prepared artifacts and continue using already checked task-local proofs where their mapping permits, stating that promotion remains incomplete.

**Keep with this task:** retain sourced definitions, local IDs, Lean files, independently reviewed expected propositions, premise/API mappings and compilation/audit evidence in the target project's agreed artifact location. Catalog edits and catalog witness registration are unnecessary. If the task is exploratory, use scratch space and report its path. Do not fabricate global graph IDs for local claims.

## Resume or report a blocker

Restore the original task and its pending obligations. Map proved results to specification clauses, API operations or model-checker formulas; record input scope and conditional assumptions. After promotion, retrieve the new stable IDs from authoritative records or a freshly rebuilt, unmodified projection. Resume the originating skill's implementation, review, test design or model checking; do not stop at delivering an abstraction.

When a required source or proof cannot be obtained, report the exact gap and attempted evidence, and continue independent work. Offer another abstraction, a requirement change, or explicit conditional continuation. Only the user's affirmative choice authorizes assumption-based continuation. Label affected conclusions conditional/unchecked, keep them outside verified evidence, and do not promote the unverified candidate under this workflow. Do not weaken the original requirement or advertise model satisfaction as software refinement.

## Workflow acceptance scenarios

Use these scenarios when reviewing changes to this workflow; compiler tests check proof behavior, not an agent's interpretation of instructions.

| Scenario | Required outcome |
| --- | --- |
| Existing abstraction and suitable fresh witness | Reuse the IDs and resume; no new concept or persistence prompt. |
| Existing abstraction, missing concrete satisfaction proof | Keep concept identity, prove the concrete model's constraints, then offer retention. |
| Exact compatible declaration in pinned Mathlib | Inspect its assumptions/source and instantiate it; do not download or upgrade a library unnecessarily. |
| Genuinely absent abstraction, sourced primitives available | Derive a definition with explicit basis and provenance, construct a model, and prove required claims. |
| Bounded/rounded API proposed for an exact unbounded model | Report the mapping mismatch; do not transfer the theorem until justified. |
| Required proof fails or source is inaccessible | Continue independent work and offer alternatives; conditional continuation needs an explicit user choice. |
| Verified artifacts, user chooses promotion | Add sourced records and bindings, validate, refresh queries, and resume the original task. |
| Verified artifacts, user chooses local retention | Keep local IDs and compilation/audit evidence with the problem; leave graph records unchanged and resume. |
| Retention prompt unanswered | Keep prepared artifacts pending; do not treat the default as consent. |
