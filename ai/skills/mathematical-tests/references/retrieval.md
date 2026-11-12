# Bounded catalog retrieval

The checkout containing this skill is the catalog root. The helper locates it relative to its own resolved path, so invocation from another repository or through a symlink works. Keep the skill linked to this checkout rather than copying only `SKILL.md`; the helper depends on the pinned backend and `scripts/` here. The skill is stored at the user-requested `ai/skills/` location; agents can read it explicitly. Automatic discovery depends on the host agent's skill configuration, not on this folder name alone.

## Setup

Normal catalog commands require only Python. This skill's queries deliberately require ONTFS and RDF support. From the catalog root:

```sh
make
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search stack --limit 4
```

Use the project virtual environment; do not install into an externally managed system Python. Respect the locked ONTFS revision. `make` reuses an initialized dependency at the expected revision without changing its files, and refuses to switch revisions when local edits are present. Consult [INSTALL.md](../../../../INSTALL.md) for dependency recovery rather than discarding local changes.

Projection queries are read-only. If `.ontfs.ttl` is missing or stale, the ordinary exporter can rebuild a clean generated projection. If it contains unexported edits, preserve it and build a separate directory:

```sh
.venv/bin/python scripts/ontology.py --directory /tmp/catalog-test-context build
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py --directory /tmp/catalog-test-context search stack --limit 4
```

Use the same `--directory` for subsequent queries. Neither the helper nor the skill silently refreshes, overwrites, imports an edited runtime graph into Markdown, or performs OWL inference. Python dependencies can be available outside `.venv`; the important checks are the pinned checkout and matching projection/source hashes.

## Commands

Start with compact search results, then the selected concept and relevant operations. Fetch an axiom/law only for the current obligation; fetch a theorem only when its result or proof is needed. Premises, sources and prerequisite definitions are fetched to resolve a specific missing condition or justification, not as a routine closure. Full dossiers and whole concept pages are not the default context.

All commands produce JSON and accept `--limit`, `--offset`, `--max-chars` and `--view` after the subcommand. Defaults are 6 records, offset 0, 12,000 Unicode characters and the `focused` field view. Limits are 1–32 records and 2,048–40,000 characters. Character limits approximate context use; they are not tokenizer measurements.

| View | When to request it |
| --- | --- |
| `focused` (default) | Readable mathematics, complete retained conditions/assumptions, applicability, source-gap metadata and partial-model limits. Omits unselected interface-link lists, Lean excerpts/mappings and proof sketches. |
| `lean` | A selected record's typed formulation, mapping and direct premise mapping when formal translation or witness reuse requires them. Still omits unrelated interface links and proof sketches. |
| `full` | The complete authoritative record for an explicit audit or a needed proof sketch. This does not recursively fetch linked claims. |

Search always returns compact candidate summaries regardless of view. View selection controls fields, while section/kind/ID selection controls which records are fetched. No view clips retained equations, preconditions or assumptions to fit a budget.

| Command | Purpose |
| --- | --- |
| `search TERM --category CATEGORY` | Compact concept candidates by substring of name, definition, notation, basis, readable mathematical formulation, or linked operation name/description/signature; category is optional. Try semantic synonyms as separate searches. Use `search '' --category data-structures` for a bounded category listing. |
| `interface CONCEPT --sections operations` | The concept and explicitly linked operations; root appears first. Operations are the only default section. Request `axioms`, `laws` or `theorems` only for a current obligation. Prefer a known operation ID via `node` over the whole operation list when possible. |
| `claims CONCEPT --kind law` | Only explicitly linked axioms, laws or theorems of the chosen kind. |
| `node ID` | One record in the selected view, preserving assumptions, applicability, provenance and dependency IDs where recorded. Short forms resolve concepts; other record types need stable IDs. `--view full` retrieves the complete canonical record. |
| `premises CLAIM --depth 1` | Claim/operation plus explicit `dependsOn` premises up to that depth; no inheritance or unrelated prerequisite closure. Depth range 0–6. |
| `sources ID --kind citation` | Direct mathematical citations through `source` only; this is the default. A concept citation does not become a direct citation for its laws. |
| `sources ID --kind formulation` | Direct local Lean sources through `formulationSource` only. These describe a formal interpretation, independently of citation gaps or proof status. |

Read [formulations.md](formulations.md) only when field interpretation, typed correspondence or witness evidence is needed. `--view lean` exposes Lean declarations and JSON-encoded premise mappings; `scripts/lean.py get ID` checks the selected binding and evidence. A registered proposition is not proof evidence just because retrieval succeeded. The dependency-free `catalog.py get` and `agent_query.py node` commands also default to `focused` and accept `--view lean|full`.

Pagination is stable while the projection inputs and selection/view options stay unchanged. `projectionInputSha256` identifies that snapshot. Start again if it changes while composing a rationale. The response's `view` identifies a focused/Lean/full field selection or a search summary; omitted fields do not mean missing catalog facts.

- `total` is the number of records selected by this command within its stated sections/depth, not all mathematical consequences.
- `returned` counts complete records actually included. Large records may reduce it below `limit`.
- `nextOffset` continues the selected record page; preserve all other query options.
- `truncated` is true when records remain on another page **or** explicit dependencies exist beyond the requested premise depth.
- `depthBoundary.count` and its bounded `sample` identify deeper unexpanded premises. `nextOffset: null` does not negate a nonempty depth boundary. Follow needed IDs or increase the relevant depth.
- `needsLargerBudget: true` and exit code 2 mean the next atomic record cannot fit. `blockedRecord` and `requiredChars` identify the obstruction. No statement or assumption was shortened; raise `--max-chars` rather than looping unchanged.
- Exit code 1 reports unavailable dependencies, unknown IDs, unsafe bounds, or stale/modified projection errors.

ONTFS selects records using fixed SELECT queries with safely encoded literals. Returned fields come from the matching authoritative Markdown JSON, preserving arrays and datatypes rather than flattening RDF into ambiguous strings. `--view full` is lossless for the entire selected record; focused views omit known optional field groups while retaining semantic conditions. No embeddings, hosted service or graph mutation is needed.
