# Project context: mathematical abstractions catalog

## Purpose

Maintain a problem-agnostic knowledge graph of mathematical abstractions used to model and verify software. Cover mathematical abstractions across disciplines, including foundations, logic, algebra, order, probability, geometry, data structures, numeric types, programming semantics, and concurrency. Describe abstract behavior independently of particular software implementations. Grow the catalog with reusable concepts and precise mathematical interfaces.

## Retrieve only relevant context

`concepts/*.md` are authoritative concept records: edit their marked JSON blocks. `data/shared.json` holds the JSON-LD context, controlled vocabulary, and sources. Page prose/backlinks, `CONCEPTS.md`, the ONTFS projection, SPARQL coverage, and the HTML viewer are generated with `make build`. No monolithic `catalog.jsonld` file is stored or generated. Never edit generated prose or runtime RDF as the source of facts. Claims shared between concepts have one structured record; search by stable ID before moving or editing a claim. Use the local CLI to retrieve small slices instead of reading the whole graph into the agent context:

```sh
python3 scripts/catalog.py list --search TERM
python3 scripts/catalog.py list --category CATEGORY
python3 scripts/catalog.py get ID
python3 scripts/catalog.py get ID --sections operations axioms laws theorems
python3 scripts/catalog.py get ID --sections dependencies sources
```

The default `get` returns a concise concept record. Expand only sections relevant to the current problem; follow prerequisites explicitly. `requiresConcept` guides retrieval and is not an automatic inheritance rule. `dependsOn` connects claims to their derivation premises. Use README.md for storage and workflow, docs/IMPORTED_SCHEMA.md for the inherited schema and SPARQL examples, CONCEPTS.md for the complete page index, CATALOG.md for the imported roadmap, and COVERAGE.md for per-concept coverage. Do not infer mathematical completeness from counts or coverage labels.

## Entry requirements

- Before adding a concept or axiom, search existing entries by name, synonyms, notation, and mathematical meaning, and inspect likely matches. Reuse or extend an existing entry when it expresses the same concept or claim; do not create duplicates under different names. Give genuinely distinct variants explicit assumptions and links to related entries.
- Organize concepts into a hierarchy where mathematically appropriate, using explicit typed links for specialization or other supported relationships. Record axiom applicability and relationships explicitly; hierarchy and prerequisites do not automatically imply inheritance of axioms.
- Review existing concepts for appropriate hierarchy refinements as well as new additions. Prefer linking existing entries over creating new ones; preserve stable meanings and IDs, and explain the carrier/operation instantiation for each specialization. Do not confuse specialization with prerequisites, representations, or constructions.
- Preserve stable node IDs and unique concept short forms. Record full name, category, concept kind, descriptive definition, mathematical notation, and typed links to operations and claims.
- Each operation records its name, mathematical signature, description, and relevant domains, preconditions, outcomes, and definedness. If a proof principle has no primitive operations, explain that explicitly.
- Record the chosen `axiomBasis`, `basisKind`, and `basisScope`. Include constructor/eliminator rules, beta/eta equations, uniqueness/extensionality, or algebraic/relational constraints as appropriate.
- Give axioms, laws, and theorems separate identities, descriptions, formal statements, assumptions, and applicability links. Distinguish definitions, foundational axioms, structure laws, and derived results using their types and `ruleRole`. Never fill an axiom list with arbitrary theorems to satisfy a count.
- Record derived results and meaningful proof sketches with explicit `dependsOn` links. Informal mathematical notation and editorial sketches are not executable theories or machine-checked proofs.
- Make equality, carrier ranges, empty cases, totality, overflow, rounding, nondeterminism, and concurrency assumptions explicit. Different semantic conventions require explicit variants or instantiation instructions.

## Mandatory source provenance for additions

Every new Concept, Axiom, Law, or Theorem must link directly to one or more real Source nodes with `source`. Record `sourceLocator` (section, definition, theorem, or page), `sourceNote` (what was taken or changed), and `provenanceKind` (`direct`, `adapted`, or `derived`). Consult the actual source before citing it; a discovery index, nearby concept's reference, or unverified URL is not evidence for a specific claim. Derived claims must identify their supporting premises with `dependsOn` and explain the derivation.

A new Source needs a title (`label`), `url`, `path`, or full bibliographic `citation`, an actual consultation date (`accessedOn`, YYYY-MM-DD), and `sourceRole`. Never invent citations or retrospectively assert consultation dates. Attach citations when adding data, not as later cleanup.

`provenance_legacy.json` freezes historical citation gaps and existing citation metadata. Do not add IDs to this baseline to bypass the rule. Existing missing citations are explicitly marked `provenanceStatus: legacy-source-missing`; remove that marker and its baseline entry only after verifying and attaching actual evidence. `make test` enforces source requirements for new entries and prevents removal of existing sources. Validation checks citation structure, not whether the cited reference entails the mathematics.

## Validation and generated artifacts

After editing Markdown graph records or shared data, run `make build`, then `make test`. Also run `make test-rdf` to validate the fresh ONTFS projection with SHACL and SPARQL. Full builds install the backend automatically; report dependency blockers honestly. These check graph structure, sources, ownership, typed references, derivation cycles, and RDF/SPARQL access, not mathematical truth. Use `make coverage` for the queryable coverage summary.

Regenerate the derived artifacts after changing the graph:

```sh
make build
```

Subject navigation uses Category `parentCategory` links separately from concept `specializationOf`. See docs/HIERARCHY.md. Category searches include descendants; preserve multiple memberships. Keep the viewer’s Subjects, Specializations and Dependencies views distinct and cycle-safe for prerequisite links.

The standalone radial viewer is `visualization/index.html`. Edit `visualization/template.html` (page shell), `visualization/styles.css` (styles), and `visualization/app.js` (graph behavior), then rebuild rather than editing the generated HTML. The builder inlines these sources and the catalog into one offline page. It embeds the canonical graph, colors subject arcs, places concept nodes on an inner ring, and highlights incoming/outgoing links on hover or selection. Preserve search, relationship filters, keyboard selection, and concept details. Normal graph retrieval and `make markdown` viewer generation use Python's standard library; full builds, coverage and RDF checks use ONTFS.

Project requirements belong in this file so future agents discover them at workspace entry. Keep it concise; put detailed mathematics in the graph and detailed usage in README.md. Preserve the mandatory source policy when updating this context.

## Agent task retrieval and formalization

Use `python3 scripts/agent_query.py node ID` to fetch any claim or operation, `neighbors ID --incoming --depth 1 --limit 40` for bounded typed links, or `dossier SHORT_FORM --purpose proof|tests --limit 80` for a task context. Check `truncated` and retrieve omitted premises explicitly. See docs/AGENT_WORKFLOWS.md. Reads load authoritative Markdown, so a stale export does not silently change retrieval.

Before using a claim in Lean/Coq, map equality, carriers, assumptions and library versions explicitly. A Unicode statement, graph edge, or editorial proof sketch is not a compiled theorem. Do not claim verified proofs without running the chosen proof assistant. For software tests, map abstraction operations to the target API and honor definedness, preconditions, numeric semantics and nondeterminism. Tests do not prove universal claims.

Keep imported stable IDs and context despite the broader repository name. `data/import_manifest.json` records original node hashes, context, and the initial provenance baseline; do not alter it to conceal import loss or bypass provenance. `python3 scripts/audit_import.py` reports differences. Importing citation metadata does not mean sources were consulted again.

## AI test-design skill

All four AI skills share `ai/skills/mathematical-tests/references/formulations.md` for readable/Lean formulations, source separation, partial interfaces and witness evidence. The bounded helper searches readable formulations; `sources ID --kind formulation` follows local Lean sources, while default citation queries keep their existing mathematical-provenance meaning.

Retrieve context progressively: focused concept/operation records first; axioms/laws for the current obligation; theorems only when their results or proofs are needed. Interfaces default to operations only. `--view lean` opts into typed excerpts and `--view full` into complete records; ordinary retrieval keeps semantic conditions and partial-model limits without preloading claim lists or proof text. Read only relevant skill-reference sections, and expand premises, sources or prerequisites only to resolve a task need.

For software tests derived from this catalog, use `ai/skills/mathematical-tests/SKILL.md`. Its `scripts/query.py` entrypoint wraps `scripts/test_context.py`: bounded ONTFS/SPARQL search, interfaces, claims, premises and direct sources with record/character budgets and explicit pagination/depth boundaries. It requires a fresh, unmodified generated projection and the pinned backend; it never overwrites runtime graphs or inherits axioms. Keep API/carrier/equality/precondition mappings and source gaps explicit. Run `make test-ai` with ONTFS dependencies installed after changing the retrieval tooling or skill. Normal catalog queries remain dependency-free.

## AI specification-consistency skill

For conflicts within or between specifications, use `ai/skills/specification-consistency/SKILL.md`. Map clause IDs and source locators to explicit carriers, operations, assumptions and catalog claims; check required inputs and nonvacuity as well as joint satisfiability. Retain executable evidence and distinguish demonstrated conflicts from ambiguities, bounded results and inconclusive checks. Catalog/SHACL validation is structural, not a semantic consistency decision. Keep findings and trial encodings outside authoritative graph records unless catalog edits are requested.

## AI implementation skills

For translating catalog-based specifications into software, use `ai/skills/implementation-mapping/SKILL.md`; retain a versioned clause/catalog-to-API mapping beside the target software, including representation, equality, definedness and unresolved semantic choices. For code review against that contract, use `ai/skills/implementation-conformance/SKILL.md`. Check the mapping against normative clauses as well as code against obligations; distinguish defects, ambiguities and unchecked behavior. Reuse existing retrieval, consistency and test-design workflows. Keep implementation artifacts outside authoritative graph records and distinguish test evidence from refinement proofs.

## AI abstraction-discovery skill

For analyzing unannotated code, data structures or APIs, use `ai/skills/abstraction-discovery/SKILL.md`. Map concrete operations and signatures to candidate catalog concepts (e.g., reducers to `Monoid`, comparisons to `TotalOrder`, state merges to `JoinSemilattice`); test whether governing algebraic laws (associativity, identity, transitivity, commutativity) hold; construct reproducible counterexamples for broken laws; and formulate principled refactoring recommendations.

## AI formal-model-checking skill

For formal verification of concurrent protocols, state machines and distributed algorithms, use `ai/skills/formal-model-checking/SKILL.md`. Map system state and transitions to catalog concepts like `Lock`, `Mutex`, `LabelledTransitionSystem` and `LinearTemporalLogic`; encode states, atomic actions, safety invariants and liveness obligations under fairness into TLA+, Alloy or Z3; and diagnose counterexample traces to isolate concurrency bugs before implementation.

## Lean models and proof witnesses

Maintain each concept's readable `mathematicalFormulation` and selected `leanFormulation` in its Markdown record, with `formulationSource`, `formulationLocator`, scope, mapping and limitations. Registered witnesses also expose their expected proposition and direct premise mapping. `make check-lean` rejects drift between these excerpts and the current Lean sources/bindings; local formulation sources do not replace independent mathematical provenance.

`lean/` is the pinned Lean/Mathlib Lake project; see `lean/README.md`. Keep a model binding for every concept in `lean/bindings.json`, keyed by stable graph ID, and disclose partial interfaces. Model coverage is not proof coverage. Witnesses require an independently reviewed Lean expected type, explicit carrier/equality/operation/assumption and `dependsOn` premise mappings, and current catalog fingerprints. Use structure laws/hypotheses rather than introducing global axioms for target results. Run `make check-lean` and `make test-lean` after relevant changes; only fresh compiler/axiom-audit evidence in ignored `lean/verification.json` supports a verified witness. Never accept `sorry`, fabricated axioms, or stale evidence, or silently relabel graph claims as machine-proved. Preserve source provenance separately; a compiled proof does not establish informal-statement correspondence or close citation gaps. CI retains verification reports as artifacts. Do not change Lean/Mathlib pins without an explicit dependency update request.

## ONTFS ontology dependency

ONTFS is cloned and registered as a Git submodule at `deps/ONTFS`, pinned by `dependencies.lock.json` to `05f166cd3ba37f13984b2746ddbbe56de24d8113`. Default `make` initializes/verifies the dependency, installs it in `.venv`, and builds the catalog and ontology; repeat builds reuse the installed environment. See INSTALL.md for setup and docs/ONTOLOGY.md for the model. Setup must not stage Git changes or overwrite local dependency edits. `make markdown` remains a dependency-free catalog/viewer build. Full builds validate through ONTFS SHACL and derive coverage with SPARQL; retain Python preflight checks before RDF conversion. Do not advance the pin without an explicit dependency update request.

`ontology/model.ttl` and `ontology/shapes.ttl` define the ontology and SHACL layer. With the dependency installed, run `make PYTHON=.venv/bin/python ontology test-ontology`. The `.ontfs.ttl` runtime is a generated projection; Markdown remains authoritative. Never transfer axioms through OWL inference on concept links. Keep experiments/proposals in a scratch graph, promote reviewed facts into Markdown, and run all catalog checks before rebuilding. Do not overwrite modified runtime graphs or edit the upstream submodule as part of ordinary concept maintenance.
