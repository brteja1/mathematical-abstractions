# Mathematical Abstractions

A local, linked Markdown knowledge graph for mathematical modeling across disciplines, proof planning, and software test design. It imports **all 106 concepts and 998 nodes** from `/linuxdev/ai_research/cs_data_abstractions`, preserving every graph field, stable ID, source record, and historical provenance gap.

Start with the [concept index](CONCEPTS.md), open the [interactive radial atlas](visualization/index.html) in a browser, or query individual records with Python. The viewer works offline and includes the reference project's category arcs, progressive specialization hierarchy, search, typed relationship filters, details, keyboard selection, pan and zoom. Each concept's details link to its Markdown page.

The imported graph covers 19 categories, including algebra, logic, order, probability, topology, geometry, linear algebra, computation, databases, software semantics, and concurrency. This is a starting collection, not exhaustive coverage of mathematics or every discipline.

## Browse online

The interactive atlas is published at **https://brteja1.github.io/mathematical-abstractions/** using GitHub Pages. Concept links in the hosted viewer open the corresponding Markdown records on GitHub; local copies retain relative links for offline use.

In the repository's **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The [Pages workflow](.github/workflows/pages.yml) rebuilds and validates the catalog, then deploys the standalone viewer on every push to `main`. It can also be started manually from **Actions → Deploy visualization to GitHub Pages → Run workflow**. Deployment progress and the published URL appear in the workflow run. Only the viewer is included in the Pages artifact; the optional ONTFS backend is not needed for hosting.

## Storage and fields

| Location | Role |
| --- | --- |
| [`concepts/`](concepts/) | One editable Markdown file per concept, with typed links, backlinks, readable operations/claims, and an authoritative marked JSON record block. |
| [`data/shared.json`](data/shared.json) | Authoritative JSON-LD context, categories, concept kinds, vocabulary and shared sources. |
| [`catalog.jsonld`](catalog.jsonld) | Generated interoperable JSON-LD export for RDF/SPARQL tools. |
| [`CONCEPTS.md`](CONCEPTS.md) | Generated complete concept index. |
| [`COVERAGE.md`](COVERAGE.md) | Generated counts and basis coverage, not a completeness certificate. |
| [`visualization/template.html`](visualization/template.html) | Editable viewer template; `index.html` is generated. |
| [`provenance_legacy.json`](provenance_legacy.json) | Imported historical citation baseline. New entries cannot use its exemptions. |
| [`data/import_manifest.json`](data/import_manifest.json) | Original per-node hashes, context and baseline for import audit. |

Concepts retain `shortForm`, `fullName`, `category`, `kind`, `definition`, `notation`, `axiomBasis`, `basisKind`, `basisScope`, and all optional fields from the original. Operations retain signatures, ownership, preconditions, outcomes and definedness. Axioms, laws and theorems remain individually identified, with assumptions, applicability, provenance and derivation dependencies. Prerequisites, specializations and related concepts remain distinct typed edges.

See [the inherited schema and SPARQL examples](docs/IMPORTED_SCHEMA.md) for the complete reference documentation. That document is an imported historical description: its JSON-LD-authority instructions are superseded by this repository's Markdown workflow. The [imported roadmap](CATALOG.md) provides additional mathematical context; the generated index is the current page inventory. Original URNs and vocabulary namespace are preserved for compatibility.

## Query from AI agents

Python 3 and the standard library are sufficient; no service, credentials, embedding model or network is needed.

```sh
python3 scripts/catalog.py list --search group
python3 scripts/catalog.py list --category probability
python3 scripts/catalog.py get Group --sections operations axioms laws theorems sources
python3 scripts/agent_query.py neighbors Group --incoming --depth 1 --limit 40
python3 scripts/agent_query.py dossier Group --purpose proof --limit 80
python3 scripts/agent_query.py dossier Stack --purpose tests --limit 80
python3 scripts/agent_query.py node urn:csabs:concept/Group
```

Commands emit JSON. Retrieval reads current Markdown records directly. `get` expands only requested sections; `node` fetches any stable concept/claim/operation/source ID. `neighbors` supports chosen edge types and incoming edges. A `dossier` traverses interfaces, prerequisites, sources and derivation premises within an explicit node limit, reports truncation, and includes task instructions. Retrieve omitted premises before relying on a truncated result.

The graph can help an agent select definitions, assemble proof obligations, find premises, and derive test properties. Its Unicode statements and sketches are **not executable Lean/Coq theories**. No proof-assistant bridge, general proof generator, or automatic arbitrary-code test generator is claimed. [Agent workflows](docs/AGENT_WORKFLOWS.md) explain how to connect the retrieved specifications to those tools and other uses.

## Maintain and extend

1. Search names, synonyms, notation and meaning before adding a concept or claim. Reuse existing records when appropriate; keep distinct semantic variants explicit.
2. Edit the marked JSON array at the bottom of the relevant concept page. Keep the Concept and its operation/claim records together; shared claims have exactly one stored record and may be referenced from multiple concepts. Do not duplicate their IDs. To add a page, use the same block markers and filename equal to `shortForm`.
3. Add new sources and vocabulary to `data/shared.json` as needed. Every new Concept/Axiom/Law/Theorem requires direct consulted sources, `sourceLocator`, `sourceNote` and `provenanceKind`. Derived claims need `dependsOn`. Record actual source consultation dates. Importing metadata is not fresh source verification.
4. Record carriers, equality, empty cases, totality, overflow, rounding, nondeterminism and concurrency assumptions as relevant. Explain specialization mappings; never infer automatic axiom inheritance.
5. Run the build and checks:

```sh
make build
make test
make test-rdf  # optional: requires rdflib
python3 scripts/audit_import.py
```

`make build` validates authoritative records, regenerates readable page bodies and backlinks, exports JSON-LD, and rebuilds coverage and the offline viewer. Changes to generated prose alone are overwritten; `make test` rejects stale Markdown projections/exports and viewer data. Claims shared by pages are stored once in the first linked page by shortForm sort order after building. Find the marked record by stable ID to edit it.

The checks preserve and extend the imported safeguards: unique IDs and short forms; typed, resolved links; operation ownership and claim applicability; required bases, assumptions and formal statements; acyclic derivation and specialization edges; mandatory new-entry provenance; and a non-expanding historical citation baseline. Tests also check local page links, anchors, bounded retrieval, generated data synchronization, and presence of imported IDs. `audit_import.py` reports original, changed, missing and added nodes, so deliberate later edits remain visible.

Validation checks structure and citation metadata. It does not establish mathematical truth, source entailment, formal consistency, or proof completeness. Historical source gaps remain disclosed. Use [AGENTS.md](AGENTS.md) as the entry instructions for future agents.

## AI skill for abstraction-based tests

[`ai/skills/mathematical-tests/SKILL.md`](ai/skills/mathematical-tests/SKILL.md) guides agents from a software API to applicable mathematical concepts, axioms and laws, then to runnable tests. It covers API/operation mappings, definedness, numeric policies, nondeterminism and evidence limitations. Agents should read the skill explicitly or register this directory using their host's skill-discovery mechanism.

Its Python helper uses the pinned ONTFS projection for compact searches and selected interfaces, claims, premises and direct citations. Responses have hard record/character budgets, pagination and depth-boundary flags; complete mathematical records are preserved. Stale or locally edited runtime graphs are rejected. After the [ONTFS setup](docs/ONTOLOGY.md):

```sh
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py search queue --limit 4 --max-chars 4000
.venv/bin/python ai/skills/mathematical-tests/scripts/query.py interface Queue --limit 6 --max-chars 8000
make PYTHON=.venv/bin/python test-ai
```

The helper works from other repositories via its absolute path. See the skill's [retrieval guide](ai/skills/mathematical-tests/references/retrieval.md) for setup, source freshness, pagination and exact limits. No full graph dump or embedding service is needed.

## Lean formalization

The [`lean/`](lean/README.md) Lake project provides models or explicitly partial interfaces for all 106 catalog concepts, with pinned Lean/Mathlib versions and 17 compiled law/theorem witnesses. A separate [`bindings.json`](lean/bindings.json) links stable catalog IDs to declarations, expected types, premise mappings and limitations. `make test-lean` compiles and audits witnesses, rejects admitted or fabricated proofs, and records fresh compiler evidence. Model coverage does not mean every catalog claim has been proved. See the [formalization guide](lean/README.md) for setup, coverage and adding a new theorem.

## ONTFS ontology backend

The ontology is modeled in [`ontology/model.ttl`](ontology/model.ttl), with [`SHACL shapes`](ontology/shapes.ttl), an ONTFS exporter and bounded context/SPARQL access. ONTFS is configured as the submodule dependency `deps/ONTFS`, pinned to `05f166cd3ba37f13984b2746ddbbe56de24d8113` in [`dependencies.lock.json`](dependencies.lock.json). See [setup status and ontology workflow](docs/ONTOLOGY.md).

```sh
make submodules
make deps-ontology
make PYTHON=.venv/bin/python ontology test-ontology
.venv/bin/python scripts/ontology.py context urn:csabs:concept/Group --limit 30
.venv/bin/python scripts/ontology.py query ontology/prerequisites.rq
```

ONTFS is registered as a submodule at the locked commit. After cloning this repository, run `make submodules`, then `make deps-ontology` to install the ontology backend into the project virtual environment.
