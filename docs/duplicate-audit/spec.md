# Duplicate-candidate audit command: formal specification

Version: 0.1. Status: experimental implementation contract, 2026-11-20.
Implementation: [scripts/audit_duplicates.py](../../scripts/audit_duplicates.py).
See the [usage guide](README.md) and [conformance review](conformance.md).

## Authority and scope

**DA-01 — Purpose.** Given the authoritative catalog, return a reproducible,
ranked review queue of potentially overlapping concepts and claims. Candidate
means “inspect these records together”; it does not assert mathematical
equivalence, inconsistency, redundancy or permission to merge.

The user requested a specification first and then authorized its implementation.
This contract's profile, flags, threshold, receipt format and lifecycle are the
adopted experimental design. Existing
AGENTS.md source, identity and graph-maintenance requirements remain applicable.
Examples are informative; numbered DA clauses and their definitions are normative
within this version. No catalog addition or dependency update is required.

**DA-02 — Boundary.** Version 0.1 is an offline, deterministic, standard-library
audit over authoritative Markdown JSON blocks and `data/shared.json`. It includes
concepts and Axiom/Law/Theorem records; operations supply evidence but are not
independently audited subjects. It neither runs a solver nor fetches sources,
uses embeddings/LLMs, proves semantic equivalence, edits records/receipts,
selects canonical IDs, redirects IDs, repairs provenance, nor changes Lean bindings.
Absence of candidates is not evidence of absence of duplication. No precision,
recall or calibrated-probability guarantee is made for this initial heuristic.

## Carriers and equality

**DA-03 — Input.** A snapshot G is a finite map from stable Unicode ID strings to
authoritative JSON records, together with the context and a source-file ownership
map. Read it with the repository Markdown loader and validate the entire graph
with the existing preflight validator. Structural/provenance failures prevent a
successful audit; frozen, explicitly marked legacy source gaps remain permissible
and must be exposed as evidence. Generated prose, coverage, viewer, Turtle and
Lean verification reports are not mathematical input authorities.

Let C be the Concept IDs and H the Axiom/Law/Theorem IDs in G. Eligible subjects
U=C∪H have family f(x)=concept or claim respectively. ID equality is exact string
identity; textual normalization never changes identity or coalesces records.
Semantic equality between mathematical abstractions is deliberately undefined
by this program. Source, role, scope and proof-status differences remain visible.

**DA-04 — Pairs.** Order IDs lexicographically by Unicode code points. Define
`pair(a,b)=(min(a,b),max(a,b))` only for distinct IDs of the same family. Its JSON
identity is the two-element ID array, not a concatenation with a delimiter.
The full universe is E={pair(a,b) | a,b∈U, a≠b, f(a)=f(b)}. Axiom/Law/Theorem
cross-type pairs are eligible, with the different proof roles displayed. Distinct
families are never compared. Each pair occurs at most once; no transitive closure
of candidate similarity is taken.

**DA-05 — Empty cases and resources.** Zero/one-subject families give empty pair
sets and a successful empty report. Counts and scores use exact, unbounded
integers/rationals; no machine overflow, NaN or floating-point tie policy exists.
Every finite valid input has a mathematical outcome. Successful termination is
required when sufficient memory, disk, CPU time and functioning I/O are supplied;
there is no fixed latency guarantee. Exhaustive comparison is permitted. No pair
may be dropped silently to meet a resource budget. Resource failure is an error.

## Evidence closure and incremental selection

**DA-06 — Closure and fingerprints.** For each x∈U, D(x) is the least visited-set
closure starting at x and following these explicit outgoing record links:
`hasOperation`, `hasAxiom`, `hasLaw`, `hasTheorem`, `dependsOn`, `requiresConcept`,
`appliesTo`, `source`, `category`, `kind`, `parentCategory`. Traverse list and
scalar links as declared by the graph schema. Cycles terminate by visited IDs;
links provide context, not inherited axioms. Do not follow `relatedConcept`,
`specializationOf` or `formulationSource` transitively; their stored values are
still fingerprinted as part of each included record. Changes to records outside
D(x) do not invalidate x's review context. This is a declared dependency scope,
not a guarantee to discover every semantic dependency.

`canon(v)` is UTF-8 JSON with sorted object keys, `ensure_ascii=False`, separators
`,` and `:`, and no NaN/Infinity. Array order is retained. This conservatively
invalidates receipts after array reorderings; it never equates reordered ASTs.
Let A_x be the alias list for x, sorted and deduplicated by normalized text, and
empty for claims. The fingerprint is SHA-256(canon({profile: "DA-P1", context:
G's JSON-LD context, records: {i:G[i] for i∈D(x)}, aliases:A_x})). Digest equality
is a practical change detector under the SHA-256 collision-resistance assumption,
not a mathematical proof of equality. There is no substitution of fingerprints
for the record IDs or for a reviewer's semantic analysis.

**DA-07 — Selection.** With no `--changed`, inspect E. With one or more changed
IDs Δ, every ID must exist in G, but may be an operation, source or category.
Define affected subjects V={x∈U | D(x)∩Δ≠∅}; inspect
E_Δ={p∈E | an endpoint of p lies in V}. Duplicate changed arguments collapse by
ID. The other endpoint ranges over the entire family, not just Δ. A deleted ID
is an error; detecting deletions or inferring changes from Git is outside 0.1.
Report requested IDs, V, inspected and uninspected pair counts. Selection is not
a statement that uninspected pairs were checked.

## Detection profile DA-P1

**DA-08 — Normalization.** For exact textual comparison, N(s) is NFKC Unicode
normalization followed by casefold and replacement of each nonempty whitespace
run with one ASCII space, then stripping leading/trailing space. Empty N(s)
never triggers exact-match evidence. For tokenization, first insert a space at
each ASCII lowercase-or-digit to uppercase boundary (`(?<=[a-z0-9])(?=[A-Z])`),
then apply N and Python's Unicode regular expression `\w+|[^\w\s]`; retain the
result as a set of tokens. Mathematical and punctuation symbols are retained.
No stemming, alpha-renaming, stop-word filtering, rewriting or unit conversion
occurs. Pin and report Python and Unicode database versions: identical inputs
are reproducible within that environment/profile, not across unpinned Unicode
implementations. Null/missing optional fields contribute nothing; required fields
remain subject to graph validation. Non-string data are not coerced to prose.

**DA-09 — Features.** Union tokens from string leaves of the listed fields,
recursing through arrays/objects in those fields. For context, use sets of exact
stable IDs rather than word tokens. Only directly linked operations/axioms below
are used for scoring; the larger D(x) is for review context and invalidation.

| Channel | Concepts | Claims | Concept/claim weight |
| --- | --- | --- | --- |
| name | shortForm, fullName and external aliases | name | 20 / 10 |
| description | definition, mathematicalFormulation | statement, description | 20 / 35 |
| interface | directly linked operation name, signature, precondition, totality, outcome, postcondition | empty | 25 / 0 |
| basis | axiomBasis, basisKind, basisScope and directly linked axiom formalStatement, assumptions, ruleRole | formalStatement, assumptions, ruleRole | 25 / 40 |
| context | direct category, kind, requiresConcept IDs | direct appliesTo, dependsOn IDs | 10 / 15 |

For finite sets, J(A,B)=|A∩B|/|A∪B| if the union is nonempty and 0 otherwise.
Both empty does not count as similarity. For endpoint family f with weights w,
score(p)=floor(100·Σ_k w_fk J(F_k(a),F_k(b)))∈[0,10000]. Missing channels are
not reweighted. Store each component as exact intersection/union counts and its
weight; a zero union has value 0/1. Compute the final floor only once.

**DA-10 — Candidate relation.** T is an integer threshold in [0,10000], default
3000. Define exact-name evidence when the sets of nonempty normalized names
(shortForm/fullName/aliases for concepts; name for claims) intersect. Define
exact-statement evidence only for claims with equal nonempty normalized
formalStatement. A pair qualifies iff score≥T OR exact-name OR exact-statement.
Threshold 0 intentionally admits every inspected pair, including zero evidence.
At any other threshold, sharing only a source, subject or prerequisite never
independently forces qualification. Source IDs are not a scoring channel.

**DA-11 — Explanations.** Every candidate includes score components, triggers,
matched names, matched tokens/IDs per channel (sorted), both endpoint types,
source record paths and stable node anchors. Include direct source IDs, locators,
provenanceStatus and reviewStatus, without inventing source consultation.
Include each endpoint's unabridged relevant fields from DA-09 plus assumptions,
verificationObligation, source metadata, all typed outgoing links and endpoint
fingerprints. List directly referenced evidence records with ID/path/anchor;
retain missing fields as absent/unknown. Present an exact-field difference list
using canon equality. A textual difference is not a demonstrated semantic
conflict, and matching wording does not establish equivalent carriers or laws.
The JSON report carries complete evidence; Markdown may link to these full
records but may not omit the scope/assumption/role/provenance warnings.

## Review receipts and lifecycle

**DA-12 — Optional aliases.** `--aliases PATH` reads JSON `{schemaVersion:1,
aliases:{conceptID:[string,…]}}`. IDs must denote current Concepts; reject
unknown/claim IDs, non-string/empty-normalized aliases and duplicate JSON keys.
Normalize/deduplicate aliases for comparison, retaining their normalized sorted
list for fingerprints. No alias file means the empty map. This external input
tests synonym support without adding a new authoritative graph field.

**DA-13 — Optional registry.** `--registry PATH` reads `{schemaVersion:1,
entries:[receipt,…]}`. Each receipt has `pair`, `fingerprints` (two hashes aligned
to canonical pair order), `profile` (nonempty string), `decision`, `rationale`,
`reviewer`, `reviewedAt` (RFC3339 timestamp), and `mapping` with nonempty strings
for `carriers`, `equality`, `operations`, `assumptions`. Decisions are
`same_meaning`, `specialization`, `semantic_variant`, `distinct`, `undecided`.
Specialization is allowed only for concepts and additionally has `specializedId`
and `generalId`, distinct and exactly the endpoints. The mapping records what
was compared, not a proof. `same_meaning` is a human conclusion, not an audit
inference or an instruction to consolidate.

Reject malformed receipts, self/uncanonical pairs, invalid hash syntax, duplicate
pair entries, unknown decision values, duplicate JSON keys and unsupported registry
schema versions. Receipts for removed endpoints are retained as `orphaned` metadata
and never suppress candidates. A receipt for a present cross-family pair is an
error. An older profile is valid input but cannot be current.

**DA-14 — Freshness.** A receipt is current iff both endpoints exist, its profile
is DA-P1 and both stored fingerprints match the recomputed values. For an extant
candidate, assign exactly one state:

| Condition | State | Actionable by default? |
| --- | --- | --- |
| no receipt | unreviewed | yes |
| receipt exists but is not current | stale | yes |
| current same_meaning | confirmed_duplicate | yes |
| current undecided | undecided | yes |
| current specialization, semantic_variant or distinct | reviewed_distinct | no |

Preserve previous decisions on stale rows, explicitly marked historical; do not
use them as current mathematical findings. Without `--include-reviewed`, omit
only reviewed_distinct candidates from the queue, while counting them. With that
flag, include them. Receipts never cause edits, determine candidate scores, or
suppress an unreviewed third pair through a shared endpoint. Current
confirmed_duplicate receipts and stale receipts for extant eligible pairs force
qualification even below T, within the inspected universe. This keeps known
duplicates actionable and reopens changed review contexts. Other receipts do
not force qualification; report their status in a separate registry summary
even when their pair is below threshold or outside incremental selection.

## Report and command boundary

**DA-15 — Ranking and bounds.** Sort the selected queue by
`(-score, firstID, secondID)` using exact integers and code-point ID ordering.
No environment-dependent locale or unstable tie order. `--limit L` is a global
nonnegative integer, default 50; retain exactly the first min(L,queueSize) rows.
Compute all counts before limiting. `truncated` iff returnedCount<queueSize.
An empty displayed queue with a positive queueSize is never described as clean.
Changing L does not change qualification, score, review states or total counts.

**DA-16 — CLI.** The entrypoint is:

```text
python3 scripts/audit_duplicates.py
  [--changed ID ...] [--aliases PATH] [--registry PATH]
  [--threshold T] [--limit L] [--include-reviewed]
  [--format json|markdown] [--output PATH]
```

`--changed` accepts one or more IDs and may repeat; omitted means full scope.
No positional arguments, Git dependency or automatic filesystem scan beyond the
catalog input manifest. Format defaults to JSON. Success is exit 0 even when
candidates exist; parse/validation/usage/snapshot errors are exit 2 and I/O or
resource errors exit 3, with no success report. Keyboard interruption follows
the host's interruption convention and cannot be reported as success.

**DA-17 — Machine output.** A successful JSON report has schemaVersion=1,
profile=DA-P1, `semantics="heuristic-candidates-not-equivalence"`, and:

* `inputs`: catalog digest, sorted relative-path/byte-hash manifest, alias/registry
  byte hashes or null, command version and local executed-module source hashes
  (including loader/validator helpers), Python and Unicode versions;
* `scope`: mode, requested changed IDs, affected subject IDs, threshold, limit,
  includeReviewed, inspected/total/uninspected pair counts;
* `counts`: qualifiedCount (after the DA-14 forced-candidate rule), stateCounts
  partitioning qualifiedCount, hiddenReviewedCount, queueSize, returnedCount;
* `truncated`, `candidates`: the ranked prefix with evidence and review states;
* `registrySummary`: every receipt in canonical pair order with current/stale/
  orphaned status, decision, inInspectedUniverse and qualifies flags;
* `limitations`: heuristic detection, incomplete semantic recall, dependency-scope
  boundary, retained legacy gaps, and absence of proof/merge authorization.

All object keys use deterministic serialization; unordered arrays are sorted by
their declared identity, and original record arrays preserve order. JSON is
UTF-8, two-space indented, ensure_ascii=False, with one trailing newline. Do not
include wall-clock timestamps, absolute checkout paths or runtime durations in
the report. Identical byte inputs/options/tool environment yield identical bytes.
Markdown presents the same scope, counts, ordering, receipt states and warnings,
with relative record links and a clear truncation notice.

For each candidate, the exact JSON keys are `pair`, `family`, `score`,
`components` (channel → {intersectionCount, unionCount, weight}), `triggers`
(a sorted subset of `threshold`, `exact_name`, `exact_statement`,
`confirmed_review`, `stale_review`), `matches` (channel → sorted token/ID array), `matchedNames`,
`endpoints` (two aligned objects), `differences` (sorted field-name array),
`reviewState`, `currentReview` (receipt or null), and `previousReview` (stale
receipt or null). Endpoint objects have `id`, `type`, `path`, `anchor`,
`fingerprint`, `fields` (all DA-11 relevant fields) and `evidenceRecords`
(sorted {id,path,anchor} objects for direct references). Shared data nodes and
Concept page roots use `anchor=null`; operations/claims use the existing generated
node anchors. Missing fields stay absent, while a present null remains null.
Differences compare the union of endpoint `fields` keys, distinguishing absent
from null. stateCounts has exactly the five DA-14 state keys, including zeros.
The qualified relation is DA-10's relation union the current confirmed-review
and stale-review pairs, restricted to the inspected universe. The five trigger predicates are
reported independently, even if several hold. A stale receipt has currentReview
null and previousReview set; an absent receipt has both null.

The catalog digest is SHA-256(canon({context: G's context, records:G})). Report
paths are relative to the catalog root. External alias/registry paths are
represented only by their role and byte hash. registrySummary rows use `pair`,
`status`, `decision`, `inInspectedUniverse`, `qualifies`; qualifies is false
outside the inspected universe or for an orphan. Candidate JSON and Markdown
are two renderings of one result, not separately computed queues.

**DA-18 — Side effects and concurrent input.** By default emit the complete
report to stdout only. `--output` emits it to a new regular file, never overwrites
an existing path, and is rejected inside concepts/, data/, lean/, ontology/,
visualization/, deps/, .git/ or any hidden path beneath the catalog root. Resolve
symlinks before checking; reject a symlink output target. Also reject any input
path, existing directory or alias of an input. No report file is created before
all reads, validation, computation and the final input check succeed. Its parent
directory must already exist; creating directories is outside the contract. Exclusive
creation must fail if another process creates the target first. On output write
failure, best-effort remove only the newly created partial report; document any
cleanup failure. stdout transport failure can leave partial bytes; exit 3 makes
them unusable as a successful report.

The manifest covers concepts/*.md and data/shared.json plus explicit alias and
registry files. Parse the captured bytes, not a later independent reread.
Preflight policy files `provenance_legacy.json` and `data/import_manifest.json`
are also captured and rechecked, and identified as `inputs.validationInputs`;
the shared validator reads those captured policy bytes.
Immediately before emitting, verify file membership and byte hashes again; any
detected change aborts with exit 2. The environment must keep inputs stable
during capture and final verification; there is no filesystem transaction or
protection against an adversarial change-and-restore race. Do not create lock
files, bytecode caches, runtime graphs, generated pages, registry updates or
network activity. Incidental interpreter caches must be disabled by the entrypoint.

## Acceptance obligations

These are implementation obligations; executed evidence is in the
[conformance review](conformance.md). This table alone is not a test result.

| ID | Clauses | Required observation |
| --- | --- | --- |
| AC-01 | DA-03–05 | Empty/singleton families succeed with zero pairs; distinct IDs survive equal wording |
| AC-02 | DA-04 | Permuting records cannot create self, reversed or repeated pairs; all claim-type combinations included |
| AC-03 | DA-06–07 | Incremental run equals full run restricted by closure intersection, including an unchanged counterpart |
| AC-04 | DA-06 | Shared premise/source edit invalidates dependent receipts; unrelated record edit does not; cyclic traversal terminates |
| AC-05 | DA-08 | Case/space variants normalize; absent tags/assumptions are not invented; operator tokens such as + and × remain distinct |
| AC-06 | DA-09 | Empty unions give zero; component arithmetic is exact; independent hand-calculated fractions yield the expected final floor |
| AC-07 | DA-10 | Exact alias/name/claim-statement triggers work at T=10000; T=0 includes every inspected pair |
| AC-08 | DA-10–11 | Shared source alone does not qualify at default T; scope/role differences remain visible despite high scores |
| AC-09 | DA-12–14 | Every receipt-state row exercised; stale distinct and current confirmed duplicates remain actionable even below threshold within the inspected universe |
| AC-10 | DA-14 | Receipts for (a,b),(b,c) never suppress (a,c); confirmed below-threshold pairs forced only inside inspected universe |
| AC-11 | DA-15 | Tied scores use IDs; limit 0 exposes positive queueSize/truncation; increasing limit extends a prefix |
| AC-12 | DA-17 | State counts partition qualified pairs; hidden+queue=qualified; returned≤queue; no claims of semantic completeness |
| AC-13 | DA-03,12–13,16 | Invalid graph/selector/registry/options fail closed; explicit legacy gaps remain visible; removed-endpoint receipts are orphaned |
| AC-14 | DA-17 | Byte-identical reruns and relocated checkout outputs in the same tool environment; Markdown and JSON queue agree |
| AC-15 | DA-18 | Hash-tree before/after unchanged except requested new report; no overwrite, input alias, symlink or forbidden-directory writes |
| AC-16 | DA-18 | Injected mid-read/final-check changes abort; exclusive-create and write/cleanup failures follow the error contract |
| AC-17 | DA-01–02 | No automatic merge/identity inference even for identical normalized statements or confirmed receipts |

## Specification consistency evidence

[mapping.md](mapping.md) maps clauses to existing catalog abstractions and future
implementation obligations. [check_model.py](check_model.py) is a standalone
bounded reference encoding for the specification, not the audit CLI. It checks
pair/selection/report partitions, receipt cases, rank prefixes and exact arithmetic
on explicitly finite domains. [evidence.json](evidence.json) retains hashes,
environment, bounds and execution results. Those finite checks do not establish
universal consistency, detector efficacy, I/O safety, or future conformance.
All DA clauses received manual review; unchecked operational obligations remain
listed in the evidence. No Lean theorem or solver proof is claimed.

## Experiment follow-up

After implementation, evaluate ranking on independently reviewed catalog pairs:
known synonyms/equivalent presentations, genuine specializations, semantic variants
and unrelated controls. Keep labels outside scoring inputs; report adjudication
rules, precision among reviewed top-k pairs, missed labeled duplicates and runtime
on the dated snapshot. Tune a new versioned profile from measured results rather
than describing DA-P1's weights as mathematically justified. Automatic consolidation
and ID migration require their own contract and authorization.
