# Automated semantic triage

Start with the [readable pilot report](triage-pilot/report.md). This assistant
reviewed ten high-scoring pairs: five distinct laws and five format-specific
variants. There were no duplicate-consolidation proposals in that subset.
Another 5,528 actionable candidates were not selected or semantically reviewed.
These are machine proposals, not human receipts or independent accuracy evidence.

The pipeline reuses the audit's DA-P1 selector and stores source capsules once per
record/fingerprint, immutable review results once per packet/reviewer/version,
and a short Markdown report. No model service is silently chosen and no graph
records are edited. Rules provide evidence hints; they do not decide equivalence.

## Prepare an experiment

From the repository root:

```sh
python3 scripts/triage_duplicates.py prepare --workspace /tmp/catalog-triage --limit 50
```

This ranks all audit candidates but selects 50 for semantic review. Pass `--all`
instead of `--limit` to select the complete actionable queue. Preparation performs
no AI calls. `--threshold`, `--aliases` and `--registry` use the existing audit
semantics; current human-reviewed distinctions are excluded from the actionable
queue. The plan declares the full, selected and unselected counts.

Use a new/empty directory. Later commands recognize its tool marker and can
resume the same experiment. Keep normal user documents and human receipt files
outside that directory. Authoritative graph directories and symlink workspaces
are rejected. Re-run prepare after source, policy or code changes; previous
content-addressed evidence remains available, with reuse only for identical
packet/reviewer contexts.

## Review using this assistant

Export source packets to review without labels or earlier judgments:

```sh
python3 scripts/triage_duplicates.py export --workspace /tmp/catalog-triage --reviewer-id current-assistant --reviewer-version YOUR_SESSION_VERSION --reviewer-kind assistant-session --budget 10
```

The command prints the exported JSON path relative to the workspace. Ask the
assistant to review those requests and return this bundle structure:

```json
{
  "schemaVersion": 1,
  "reviews": [{
    "pair": ["FIRST_ID", "SECOND_ID"],
    "packetKey": "COPY_PACKET_KEY",
    "result": {
      "decision": "distinct",
      "rationale": "Explain the mathematical distinction.",
      "mapping": {
        "carriers": "Explicit carrier comparison.",
        "equality": "Explicit equality comparison.",
        "operations": "Explicit operation correspondence or difference.",
        "assumptions": "Explicit assumptions and definedness."
      },
      "differences": ["Decisive difference."],
      "missingContext": [],
      "evidence": [
        {"recordId": "FIRST_ID", "field": "formalStatement", "quote": "EXACT_NONEMPTY_QUOTE"},
        {"recordId": "SECOND_ID", "field": "formalStatement", "quote": "EXACT_NONEMPTY_QUOTE"}
      ]
    }
  }]
}
```

Allowed decisions: same_meaning, specialization, semantic_variant, distinct,
insufficient_evidence. Evidence must quote real packet fields and cover both
endpoints; definitions can be quoted for Concept records. This checks citation
existence, not correctness of the interpretation. Preserve real model identity
and version when available; otherwise record that they are unavailable. Do not
invent a version or identify assistant output as a human decision.

```sh
python3 scripts/triage_duplicates.py import --workspace /tmp/catalog-triage --reviewer-id current-assistant --reviewer-version YOUR_SESSION_VERSION --reviewer-kind assistant-session --reviews /tmp/reviews.json
python3 scripts/triage_duplicates.py report --workspace /tmp/catalog-triage
```

Open `/tmp/catalog-triage/report.md`. Duplicate proposals and unresolved cases
appear first; suggested distinctions are in an expandable table. Every group is
counted, including failures, pending reviews and unselected candidates. The
machine evidence stays in `proposals.json` and immutable cache objects. Repeated
identical imports are idempotent; contradictory results require a new version.

## Unattended batches

A configured, trusted model adapter makes one model request from stdin and writes
one protocol result to stdout. Pass its executable argv as JSON, without a shell:

```sh
python3 scripts/triage_duplicates.py review --workspace /tmp/catalog-triage --reviewer-id YOUR_MODEL --reviewer-version YOUR_PINNED_VERSION --review-command '["/absolute/path/to/model-adapter"]' --budget 20 --timeout 45 --max-input-chars 40000
```

Repeat to resume; already valid results are reused. Budgets bound attempted pairs,
including failures. Oversized inputs, invalid citations, adapter errors and
timeouts remain failed/unresolved and retryable. Context is never silently cut
to fit. The adapter must use an approved local/remote backend and its own model
configuration; this repository does not install or select a service. It is a
trusted program, not a filesystem security sandbox. Subprocess output is checked
after capture; the pipeline makes no adversarial memory/resource guarantee.

For same-meaning proposals, use a different declared reviewer ID/version with
`--stage independent`. Only those proposals are selected for the second stage;
the reviewer receives original records, not the first verdict. Disagreements,
missing context and failed second reviews stay visible. Declared identities do
not prove statistical independence. Even agreement never authorizes a merge.

## Calibration before automatic suppression

DT-1 does **not** automatically quiet audit entries or write human review receipts.
Suggested distinctions are merely collapsed in the human report. An optional
evaluation file keeps labels separate from model inputs:

```json
{
  "schemaVersion": 1,
  "labeler": {"id": "YOUR_REVIEWER", "independence": "DESCRIBE_HOW_LABELS_WERE_REVIEWED"},
  "cases": [{"pair": ["FIRST_ID", "SECOND_ID"], "expectedDecision": "distinct"}]
}
```

```sh
python3 scripts/triage_duplicates.py evaluate --workspace /tmp/catalog-triage --labels /tmp/independent-labels.json
```

`evaluation.json` reports coverage, exact classification agreement, retain/duplicate
precision and a confusion table with explicit denominators. Missing predictions
are not counted as correct. Synthetic fixture tests and labels written by the
reviewing assistant are not independent detector-accuracy evidence. Calibration
metadata is a declared provenance claim, not something the software can authenticate.
A later, independently evaluated policy would be needed to enable auto-quieting.

## Tests and retained evidence

```sh
python3 -B -m unittest discover -s tests -p test_triage_duplicates.py -v
make test
```

See [triage-spec.md](triage-spec.md) for DT-01–DT-12 and API obligations,
[triage-conformance.md](triage-conformance.md) for inspected/tested scope, and
[triage-evidence.json](triage-evidence.json) for actual results and hashes.
The original audit experiment's reports remain historical evidence; the latest
triage run records the shared pair-selector integration and current code hashes.
