# Duplicate-candidate audit

Run the offline, standard-library command from the repository root:

```sh
python3 scripts/audit_duplicates.py --limit 10
python3 scripts/audit_duplicates.py --changed urn:csabs:concept/SKOS --limit 10
python3 scripts/audit_duplicates.py --format markdown --limit 10 --output duplicate-audit.md
```

Default output is JSON on stdout. An explicit output file must be new; the command
does not overwrite files, create directories, change the graph or record reviews.
For automated classification and a shorter human-facing report, use the
[semantic triage experiment](TRIAGE.md). Its [pilot report](triage-pilot/report.md)
contains machine judgments on ten pairs and explicitly counts the unreviewed remainder.
Markdown record paths are relative to the catalog root, so keep exported Markdown
there when following its links. Thresholds are integers on a 0–10000 scale,
default 3000. The default row limit is 50. `--limit 0` still computes all counts.

The command compares concepts with concepts and claims with claims, including
different Axiom/Law/Theorem roles. Similar wording and shared interfaces can
produce high scores for mathematically distinct records. Treat the queue as
evidence for inspection; no pair is automatically merged or declared equivalent.
The initial weights are an experimental baseline without measured precision/recall.

## Incremental scope

`--changed` takes stable IDs, not filenames or Git refs, and may be repeated:

```sh
python3 scripts/audit_duplicates.py --changed urn:csabs:concept/SKOS --changed urn:csabs:concept/RDFGraph
```

Each affected subject is compared with its entire family. Changes to shared
operations, premises, sources and categories also select subjects whose explicit
review context reaches those records. The report declares inspected and
uninspected pair counts. It does not infer changes/deletions from Git or interpret
prerequisites as inherited axioms.

## Aliases and review receipts

`--aliases aliases.json` optionally supplies synonyms without changing the graph:

```json
{
  "schemaVersion": 1,
  "aliases": {
    "urn:csabs:concept/FiniteField": ["Galois field"]
  }
}
```

`--registry reviews.json` reads human review decisions. Create/edit this file
separately after comparing carriers, equality, operations and assumptions. Use the
canonical `pair` array and aligned `endpoints[*].fingerprint` values from a report
made with the aliases you intend to retain. Each entry has this structure (replace
the fingerprint placeholders with the actual 64-character hashes):

```json
{
  "schemaVersion": 1,
  "entries": [{
    "pair": ["urn:csabs:concept/PartialOrder", "urn:csabs:concept/TotalOrder"],
    "fingerprints": ["COPY_FIRST_ENDPOINT_HASH", "COPY_SECOND_ENDPOINT_HASH"],
    "profile": "DA-P1",
    "decision": "specialization",
    "specializedId": "urn:csabs:concept/TotalOrder",
    "generalId": "urn:csabs:concept/PartialOrder",
    "rationale": "The same carrier and relation with added comparability.",
    "reviewer": "YOUR_NAME",
    "reviewedAt": "2026-11-20T00:00:00Z",
    "mapping": {
      "carriers": "The same carrier A.",
      "equality": "Identity equality on A.",
      "operations": "The same binary order relation.",
      "assumptions": "TotalOrder additionally requires pairwise comparability."
    }
  }]
}
```

Supply the actual review time; the timestamp above illustrates the format. This
sample is not a receipt produced by the audit or a compiled mathematical proof.
The audit never modifies receipts. Unknown removed endpoints appear as orphaned
metadata; unknown changed IDs or alias IDs are errors.

Current `distinct`, `semantic_variant` and `specialization` decisions become quiet.
`--include-reviewed` includes them again. Current `same_meaning` decisions stay
actionable. Changed review contexts and older profiles reopen as stale, even below
the threshold, within the inspected scope. No review suppresses a third pair
through transitivity. `undecided` remains visible when the pair qualifies.

## Evidence, errors and limits

JSON contains exact component counts/weights, matched evidence, complete endpoint
records, directly linked operations/axioms/sources, field differences, fingerprints
and registry status. Counts are computed before row limiting; `truncated` means
additional queued pairs were not displayed. Mathematical source gaps and different
claim roles remain explicit. Source URLs are never fetched.

Exit 0 means a completed report, including reports with candidates. Exit 2 means
invalid inputs/options or a detected snapshot change. Exit 3 means I/O/resource
failure. No success report is emitted after a failed final input check. The command
captures/rechecks graph and validation-policy bytes without constructing an RDF
projection, lock files, caches or network requests. Input stability is assumed;
this is not a transactional filesystem snapshot against adversarial races.

The [contract](spec.md), [mapping](mapping.md) and [conformance review](conformance.md)
describe implementation obligations and tested limits. The earlier
[bounded reference model](check_model.py) remains separate from production tests:

```sh
python3 -B -m unittest discover -s tests -p test_audit_duplicates.py -v
python3 -B docs/duplicate-audit/check_model.py
```
