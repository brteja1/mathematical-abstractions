# Task-local assurance ledger

Use one ledger beside the target artifacts, in a dedicated project directory.
Do not place it at the catalog root: inventory includes all project files.
This is a local, cooperative evidence tool, not an authenticated certification
system or a sandbox for untrusted commands. A passed gate means the declared
checks passed for the recorded inputs. Reviewers still assess contract adequacy,
nonvacuity, semantic mappings and the soundness/scope of checks.

## Runnable profile

From the catalog root, with its existing pinned Lean dependencies installed:

```sh
python3 scripts/assurance.py check examples/assurance-counter/ledger.json
python3 scripts/assurance.py run examples/assurance-counter/ledger.json O1 lean
python3 scripts/assurance.py run examples/assurance-counter/ledger.json O1 examples
python3 scripts/assurance.py run examples/assurance-counter/ledger.json O2 lean
python3 scripts/assurance.py run examples/assurance-counter/ledger.json O2 examples
python3 scripts/assurance.py check examples/assurance-counter/ledger.json
python3 scripts/assurance.py impact examples/assurance-counter/ledger.json
make test-assurance
```

The first check reports missing evidence and exits 1. `run` is the only command
that executes task-supplied argv. It uses no shell, writes a JSON report under
`.assurance/`, and replaces an earlier result for the same obligation/check.
`check` and `impact` report missing, stale, failed or passed checks without running
them; they may inspect the pinned toolchain and Git dependency state. `impact`
uses the same conservative admission calculation as `check`. It does not infer
semantic dependency edges or explain changed lines. CLI exit codes are 0 for
admission/success, 1 for blocking evidence/failure, 2 for invalid data/tooling.

The pilot proves properties of the actual pure Lean function and independently
executes it for 208 inputs. It establishes neither a Python port nor native
compiler/runtime correctness. Its validation/type-review receipts explicitly
name the implementing agent: they do not assert independent stakeholder review.
No graph claims are added or promoted. Read the pilot spec for the exact domain.

## Schema version 1

The [example ledger](../../../../examples/assurance-counter/ledger.json) is a
complete copyable template. Paths resolve relative to its directory; absolute
paths and escapes are rejected. Symlinks in the project inventory are rejected.

- `schemaVersion: 1`, nonempty `name`, Boolean `dependencyGraphComplete` and
  `decisions` (list of unresolved decisions; any entry blocks admission).
- `artifacts`: records with unique `id`, relative `path` and `role` from
  requirement, specification, implementation, checker, toolchain, environment,
  release. Every file must exist. Every normative artifact must be mapped.
- `requirements`: unique `id`, `statement`, `origin` (human, external, derived,
  proposal), source artifact ID, `locator`, and `validation` containing status
  (pending, accepted, rejected), reviewer and rationale. Every requirement must
  have an obligation. Accepted proposal review is not stakeholder acceptance.
- `obligations`: unique `id`, statement, nonempty requirement/artifact ID lists,
  explicit `dependsOn` obligation IDs (acyclic), explicit string `assumptions`,
  nonempty `catalog` mappings, `evidenceRequired` kinds and uniquely named checks.
  Each catalog mapping uses a stable `urn:csabs:` ID and a `mapping` object with
  nonempty carrier, equality, operations, assumptions, scope and limitations.
  Relied-on claim `dependsOn` premises need explicit mappings. No inheritance.
- Every check has `id`, `kind` (test, bounded, review, proof) and `scope`.
  Nonproof checks specify nonempty `argv` string lists. Review also names reviewer
  and rationale; a successful command only validates a receipt, not identity.
  Every declared check must pass, including extra kinds beyond evidenceRequired.
- Proof checks require `profile: lean-source-v1`, source artifact ID, qualified
  theorem `symbol`, single-line Lean `expectedType` term and `typeReviewer`.
  Arbitrary argv cannot be classified as proof. Other proof backends are
  unsupported and require a deliberate new profile, not an evidence-kind change.

The schema checks references and coverage of *declared* records. It cannot know
whether an engineer omitted a natural-language requirement or labeled a normative
file as a checker. Reverse traceability remains a review obligation.

## Proof boundary

The runner prepends Catalog.Audit to the selected Lean source, checks
`example : (expectedType) := @symbol`, and audits that symbol as an actual theorem.
It builds the pinned audit module, checks installed package revisions and local
edits, checks the running Lean version, and permits only propext, Quot.sound and
Classical.choice transitively. `sorryAx` and postulated target theorems fail.
The expected proposition must refer to the actual implementation and express
its full required domain; compiler success does not establish this correspondence.
The runner hashes Lean source/configuration, executable, audit sources and pins.
It does not change pins, create catalog proof bindings, or assert equivalence
between source and native binaries. Put function and theorem in one self-contained
source; this first profile does not support an arbitrary project module graph.

## Freshness and impact

Each report captures exact selected catalog record hashes through agent_query,
contract metadata, artifacts, executable and gate hashes, project inventory and
unmapped helper/config file content. Changes during execution fail the run.
With dependencyGraphComplete true, an obligation includes its transitive premise
obligations and their artifacts; false selects all obligations. Requirement
sources and declared environment/toolchain files are always global. Adding or
removing a project file invalidates all evidence. Editing an unrelated mapped
artifact can preserve independent evidence only with a declared complete graph.

Ignored directories are .git, .assurance, __pycache__, .venv and .lake. They are
not places to hide task inputs. Arbitrary external files, network responses,
subprocess toolchains and environment variables are not automatically discovered.
Freeze relevant external state in declared environment/toolchain files, retain
versions and assumptions, or leave admission blocked with an unresolved decision.
Do not claim reproducibility across untracked execution environments. Hashing an
executable does not freeze every interpreter module or operating-system input.
Reports are mutable local receipts and are not resistant to malicious fabrication.

On each contract/code/toolchain change: update traceability, run impact, inspect
reverse dependencies and assumptions, rerun affected checks, then check admission.
Retain failed output and distinguish tests, bounded exploration, review and proof.
Full universal correctness, stakeholder intent validation, composition rules and
deployment guarantees are not supplied by ledger validation.
