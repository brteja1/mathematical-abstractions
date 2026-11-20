# Duplicate audit implementation review

Scope: DA-01–DA-18, mapping O-01–O-12, implementation version 0.1.0 / DA-P1.
The user authorized implementation after the specification stage. The original
context.json is a historical baseline; current hashes and executed results are
retained in [implementation-evidence.json](implementation-evidence.json).

## Result and interpretation

The command implements the specified offline review queue, including aliases,
explicit changed-ID scope, exact scoring, review receipts, deterministic output,
final input checks and exclusive report creation. No remaining contract violation
was identified in this review. This is code inspection and finite test evidence,
not a universal refinement proof or evidence of mathematical detector accuracy.

The [sample report](sample-report.json) is from a full current-catalog run with
`--limit 10`: 828,150 eligible pairs inspected, 5,538 qualified, ten displayed,
and `truncated=true`. No review receipts or external aliases were supplied.
These are candidate counts, not confirmed duplicate counts. The highest-scoring
pair compares CRDT merge idempotence with commutativity: its related wording does
not make these the same law. DA-P1 remains an uncalibrated experimental baseline.

The sample's source-file and tool hashes were checked against the current files
before retention. Graph records and existing SKOS work remain unchanged by the
implementation. The shared loader/validator changes only add optional captured
input hooks; their ordinary disk-loading behavior is retained and regression-tested.

## Obligation-to-evidence review

Tests live in [test_audit_duplicates.py](../../tests/test_audit_duplicates.py).
Each test names its acceptance/obligation IDs and the catalog interpretation it
uses. All finite sets use exact ID/tuple/token equality; rank order is exact
integer then Unicode code-point order. Citation gaps in Relation and the selected
TotalOrder claim remain visible and are not closed by tests.

| Obligations | Code/evidence | Assessment and limits |
| --- | --- | --- |
| O-01 | Snapshot capture, shared loader captured-text path, validator captured-policy reader; invalid graph/key/ID and snapshot-change tests | Supported by inspection and synthetic fixtures; no filesystem transaction against adversarial change-and-restore races |
| O-02 | sorted same-family combinations; exact independent 18-pair expected set with cross-role claims | No self/reversed/cross-family/duplicate pairs in tested domain; distinct names/IDs are not merged |
| O-03 | visited-set closure; incremental/full restriction, cycle, shared-source and unchanged-counterpart tests | Explicit DA-06 closure only; no inferred semantic dependency or Git deletion analysis |
| O-04 | normalize/tokens/extract_features; Unicode width/case, camel-case, operator and nontext tests | Current Python/Unicode environment; no alpha-equivalence or symbolic algebra |
| O-05 | exact Fraction arithmetic; independently calculated 3333 score, empty-channel zero, reversed-pair symmetry and max-threshold triggers | Exact arithmetic in tested cases; weights not validated for ranking quality |
| O-06 | strict JSON/schema readers; aliases, every receipt state, direction/type/date/hash and duplicate-pair errors | Invalid inputs fail closed; orphan receipts remain metadata |
| O-07 | independent canonical fingerprint payload; premise/source/alias invalidation, unrelated-record stability, stale/confirmed forcing and no transitive suppression | SHA-256 collision resistance assumed; explicit closure scope and full-record conservative invalidation |
| O-08 | nsmallest exact rank key; tied-score independent lexicographic oracle, prefix and zero-limit tests | Every pair consumed for counts, including limit zero; retained detailed candidate payloads bounded by limit |
| O-09 | full endpoint/direct evidence, exact field differences; relocated byte-identical JSON and Markdown queue tests; real legacy-gap observation | All requested fields retained; human mathematical correspondence review still required |
| O-10 | CLI, output policy, exclusive creation and emission; real subprocess, exit-code, symlink/protected-path, write/close/cleanup/replacement tests | No overwrite or successful report after observed input change; tests cover selected faults, not all possible OS failures/interleavings |
| O-11 | empty catalog, singleton-family, unknown selector and resource error contracts | Finite fixtures plus inspection; no fixed performance or arbitrary-input termination proof |
| O-12 | whole-program inspection and relocated subprocess before/after byte-tree comparison without -B | No source/registry mutation, bytecode cache, RDF/backend calls, network client, merge or ID retirement in the audited command |

## Findings repaired during implementation

* A heap selection with limit zero would not consume a lazy input iterator.
  The implementation explicitly consumes it so qualification and scope counts
  remain complete even when no rows are requested.
* Reading files again inside the shared loader/validator would defeat captured
  input semantics. Optional snapshot hooks now parse the captured graph and
  preflight-policy bytes. Policy hashes are reported as validationInputs.
* Endpoint links alone were insufficient to retain operation preconditions and
  axiom assumptions. Full directly linked operation/axiom/source records are
  included in the endpoint evidence.
* Output failure handling must include close failures and avoid unlinking a
  replacement created by another process. Cleanup checks the originally opened
  file's device/inode identity before unlinking; cleanup failures are diagnosed.
* Timestamp parsers may normalize malformed offset minutes. Explicit RFC3339
  field bounds are checked before date/time parsing.
* Concept pages do not generate node-ID fragments. Report locators now use page
  roots for Concepts and shared data, and the actual stable fragments for claims
  and operations; a real-catalog regression checks that those fragments exist.

These repairs preserve DA-P1's specified scoring and review behavior. The main
specification's status was updated to implementation contract, and existing
DA-03/18 policy-capture obligations were made explicit; no requirement was weakened
to fit the implementation.

## Reverse traceability and limits

The implementation's additional mechanisms serve explicit obligations: no-bytecode
mode and exact-integer input handling (DA-05/18), canonical serialization and tool
hashes (DA-06/17), complete direct evidence (DA-11), lazy endpoint construction and
bounded heap retention without pair dropping (DA-05/15), and inode-aware cleanup
(DA-18). No additional scoring channel, learned model, transitive candidate
clustering, automatic registry editing, remote lookup or graph migration was added.

The production audit does not depend on ONTFS or Lean. The mathematical-tests skill
used bounded ONTFS queries only to select test rationale records; source assumptions
and legacy gaps are preserved. No compiled catalog witness is relied upon.

Future work requiring separate evaluation includes precision/recall against
independently reviewed pairs, scaling measurements, alternative scoring profiles
and consolidation/retirement workflows. The current contract assumes stable local
inputs and sufficient resources, and does not guarantee transactional safety
against adversarial filesystem races. Finite fault injection does not establish
conformance for every possible I/O failure.

## Reproduction

```sh
python3 -B -m unittest discover -s tests -p test_audit_duplicates.py -v
make test
python3 -B docs/duplicate-audit/check_model.py
python3 scripts/audit_duplicates.py --limit 10
```

The reference model remains a separate bounded specification check; its evidence
does not substitute for production tests. The implementation evidence records
actual command outcomes, file hashes and the dated sample's scope. Hashes are
reproducibility metadata, not cryptographic attestations or proof certificates.
