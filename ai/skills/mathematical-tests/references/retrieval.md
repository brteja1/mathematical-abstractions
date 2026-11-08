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

All commands produce JSON and accept `--limit`, `--offset`, and `--max-chars` after the subcommand. Defaults are 6 records, offset 0, and 12,000 Unicode characters including JSON formatting. Limits are 1–32 records and 2,048–40,000 characters. Character limits approximate context use; they are not tokenizer measurements.

| Command | Purpose |
| --- | --- |
| `search TERM --category CATEGORY` | Compact concept candidates by substring of name, definition, notation, basis, or linked operation name/description/signature; category is optional. Try semantic synonyms as separate searches. Use `search '' --category data-structures` for a bounded category listing. |
| `interface CONCEPT --sections operations axioms` | The concept record and only explicitly linked records in the selected sections; root appears first. `laws` and `theorems` are optional sections. |
| `claims CONCEPT --kind law` | Only explicitly linked axioms, laws or theorems of the chosen kind. |
| `node ID` | One complete canonical JSON record, including assumptions, applicability, provenance and dependency IDs where recorded. Short forms resolve concepts; other record types need stable IDs. |
| `premises CLAIM --depth 1` | Claim/operation plus explicit `dependsOn` premises up to that depth; no inheritance or unrelated prerequisite closure. Depth range 0–6. |
| `sources ID` | Direct Source records only. A concept citation does not become a direct citation for its laws. |

Pagination is stable while the projection inputs stay unchanged. `projectionInputSha256` identifies that snapshot. Start again if it changes while composing a rationale.

- `total` is the number of records selected by this command within its stated sections/depth, not all mathematical consequences.
- `returned` counts complete records actually included. Large records may reduce it below `limit`.
- `nextOffset` continues the selected record page; preserve all other query options.
- `truncated` is true when records remain on another page **or** explicit dependencies exist beyond the requested premise depth.
- `depthBoundary.count` and its bounded `sample` identify deeper unexpanded premises. `nextOffset: null` does not negate a nonempty depth boundary. Follow needed IDs or increase the relevant depth.
- `needsLargerBudget: true` and exit code 2 mean the next atomic record cannot fit. `blockedRecord` and `requiredChars` identify the obstruction. No statement or assumption was shortened; raise `--max-chars` rather than looping unchanged.
- Exit code 1 reports unavailable dependencies, unknown IDs, unsafe bounds, or stale/modified projection errors.

ONTFS selects records using fixed SELECT queries with safely encoded literals. Returned records come from the matching authoritative Markdown JSON, preserving arrays and datatypes rather than flattening RDF into ambiguous strings. No embeddings, hosted service or graph mutation is needed.
