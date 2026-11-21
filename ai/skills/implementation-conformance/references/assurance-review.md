# Assurance review mode

Use the catalog and gap-handling policies in the parent [skill](../SKILL.md). Read the [shared ledger guide](../../spec-driven-development/references/assurance.md) when inspecting executable admission, freshness or proof-profile evidence.

Review normative sources and the evidence ledger, not only the implementation author's summary. Preserve review scope; a review request does not authorize repairs. Query catalog semantics independently and compare them with requirement, API and proof mappings.

Check both directions: every requirement and normative clause has implementation/evidence obligations, and every claimed guarantee has a source and applicable evidence. Challenge hidden domain restrictions, impossible preconditions, absent permitted outcomes, incomplete initial states, aliases, numeric semantics, nondeterminism, fairness and environment promises. Distinguish legitimate implementation choices from violations and unspecified behavior.

Inspect expected proof propositions, direct premise mappings and actual checked artifacts. Look for assumed target laws, weakened postconditions, a separate model substituted for source code, unsupported axioms, stale fingerprints, mutable dependencies, ignored failures and evidence-kind inflation. Read check output and rerun appropriate checks; a passed ledger only reports declared local evidence.

Use independent scenarios, small counterexamples and a realistic mutant where appropriate. Separate demonstrated defects, ambiguities, bounded results, unchecked obligations and trusted assumptions. Reviewer identity and receipt authenticity are outside the local gate's threat model. If review is performed by the implementation author or same agent, disclose that limitation; do not claim independent human review or spawn reviewers without authorization.

Deliver findings with clause/obligation IDs, source locators, reproduction commands and consequence. State exactly what assurance claim is supported, and block stronger claims until their missing evidence is resolved.
