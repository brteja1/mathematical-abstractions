# Catalog use and gap handling

This policy applies to all repository skills. Query tooling is the agent's interface to catalog facts; authoritative storage is not an alternate retrieval interface. Use focused records and selected claims, preserve assumptions and provenance gaps, and resolve necessary pagination or omitted premises before relying on a result. A successful search alone is not a semantic mapping.

## Retrieve before relying

Locate the catalog root three levels above the skill directory. Use `scripts/catalog.py list --search TERM` for names, synonyms and mathematical meaning, `get ID --sections operations` for the interface, and `scripts/agent_query.py node ID` for selected operations/claims. Use the bounded ONTFS helper for SPARQL retrieval; see [retrieval.md](retrieval.md). Use `scripts/lean.py get ID` for current binding/evidence status. Record actual commands, selected stable IDs and carrier/equality/operation/assumption mappings with the task artifacts. Do not bypass these tools by reading or searching catalog storage or generated exports directly, even for a single concept.

Skill examples and candidate tables do not establish that a concept or claim exists or applies. Retrieve each mathematical abstraction and law actually used. Target-specific requirements remain normative; using the catalog does not authorize importing stronger laws or forcing a mismatched abstraction onto the software. Structural findings that assert no mathematical abstraction or law can be reported without inventing one.

## Report before proceeding

Before acquiring missing mathematics or generating dependent models, proofs, implementation, tests or recommendations, send the user a clear gap report containing:

- The required abstraction, operation, semantic convention or proof obligation.
- The tool queries performed, candidate IDs inspected and missing or incompatible results.
- The dependent work that is blocked and the proposed resolution.

Search alternative names and meanings and inspect plausible candidates before declaring a gap. An empty keyword result, truncated response, missing citation or partial Lean interface does not by itself establish a missing concept. Report backend/setup failure separately; do not describe it as absence and do not inspect catalog files to bypass it. Where the active skill permits dependency-free retrieval, use the standard-library catalog/agent CLI and disclose that backend. Otherwise resolve setup or report the blocker.

After the report, follow [abstraction-acquisition](../../abstraction-acquisition/SKILL.md) to reuse, source or construct and verify the missing mathematics. Reporting the gap does not itself require an acknowledgment before authorized acquisition work. Keep the original task's dependent work stopped until a suitable catalog entry is retrieved, or the acquisition workflow's verification and explicit retention choice have completed. Catalog promotion is the default recommendation; task-local retention requires the user's explicit choice and must stay visibly separate from catalog entries. An already explicit session choice remains effective. Conditional continuation with unverified assumptions also requires an explicit user choice and conditional labeling. Never silently treat external, task-local or assumed mathematics as catalog-backed evidence.

Independent work may continue after the gap report if it does not rely on the missing mathematics. Preserve the pending obligations and resume them with an explicit semantic mapping once resolved.

## Authorized maintenance

For an authorized catalog edit or promotion, first locate and inspect existing records through the query tools, then open only the authoritative files needed to make that edit. This editing exception does not permit directory exploration as a retrieval shortcut. Rebuild and validate as required by `AGENTS.md`; ordinary consumers never edit generated graphs to make a query succeed.
