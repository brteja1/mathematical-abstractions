# Discovery pilot — 2026-11-18

Both runs solved the reducer task. This single paired pilot showed **no correctness improvement from the skill**. The guided review added useful detail about not recovering valid totals from already-corrupted merged reports, but both outputs found the required defects and preserved the diagnostic contract.

| Observation | Without skills | With skills |
| --- | --- | --- |
| Required reducer defects found | 2/2 | 2/2 |
| Incorrect weighting / broken associativity | Both identified with executable witnesses | Both identified with executable witnesses |
| Arbitrary reordering rejected | Yes; ordered diagnostics preserved | Yes; order and duplicate diagnostics preserved |
| Corrected structure and empty semantics | Noncommutative monoid; exact sum/count; empty mean `None` | Same |
| Task correctness | 4/4 | 4/4 |
| Reproducible evidence | 3/3 | 3/3 |
| Completion | 2/2 | 2/2 |
| Substantive false positives / critical failures | 0 / none | 0 / none |
| Generated checks independently rerun | Pass | Pass |
| Wall time including CLI startup | 63.39 s | 61.08 s |
| Completed shell commands | 8 | 10 |
| Reported input tokens, cumulative | 133,779 | 129,546 |
| Reported cached input tokens | 119,424 | 92,032 |
| Reported output tokens | 1,940 | 2,360 |
| Repository skill files visibly read | 0 | 3 |

The two defect counts cover incorrect weighting and nonassociativity. Diagnostic order is an explicit contract constraint, not an additional defect in the original concatenation. Each generated script demonstrated counterexamples and exercised the suggested repair; these scripts do not universally prove implementation correctness.

## Inspect the actual outputs

- Without skills: [authored review](without-skills/review.md), [checks](without-skills/checks.py), [check rerun](without-skills/checks-rerun.txt), [raw events](without-skills/events.jsonl).
- With skills: [authored review](with-skills/review.md), [checks](with-skills/checks.py), [check rerun](with-skills/checks-rerun.txt), [raw events](with-skills/events.jsonl).
- [Manifest and input hashes](manifest.json), [run metadata and artifact hashes](metadata.json), [score rows](scores.csv).

The baseline used catalog queries without reading repository skill files. The treatment first read `abstraction-discovery/SKILL.md`, then its discovery and metrics references, and queried the catalog. Both selected the appropriate noncommutative structure. Skill-reference terminology or stable IDs were not used as correctness bonuses.

Reproduce the generated checks independently from the repository root:

```sh
python3 ai/evaluations/results/2026-11-18-01-discovery/without-skills/checks.py
python3 ai/evaluations/results/2026-11-18-01-discovery/with-skills/checks.py
```

## Controls and limitations

The runs were fresh ephemeral Codex CLI 0.169.0 sessions, baseline first, then treatment, with the same command, default model/reasoning request, workspace-write sandbox and 300-second timeout. Both had identical common task/catalog inputs, verified unchanged after execution. Only treatment had the repository skill files. Installed runtimes were linked equally. The original repository contained uncommitted work, so the manifest hashes, rather than the Git revision alone, identify evaluated inputs.

The actual resolved model ID and reasoning setting were **not emitted by the captured JSON stream**. They are recorded as unknown defaults, not asserted to be confirmed identical model versions. User configuration was ignored, but global/host instructions and shared runtimes were not fully isolated. This is an exploratory skill-exposure comparison, not a tightly controlled model benchmark.

The suite author graded the outputs after seeing arm labels; grading was not blind or independent. There was one run per arm and one task, with no confidence interval or randomized order. The small time difference is not evidence of speed improvement. Input-token totals include repeated context across turns, and cache use differed substantially; no monetary-cost or efficiency conclusion follows from these token counts.

The first baseline launch failed before model startup because the outer sandbox made app-server state read-only. Both successful runs used approved outer escalation while retaining their own workspace-write sandbox. That failed startup is excluded from task time and scores. Both generated scripts originally ran in commands followed by `git status`, which failed because the prepared directories are not Git repositories; the scripts themselves passed and were rerun independently with exit code zero.

An evidence-collection error set the CLI final-message path to `answer.md`, which overwrote each model's substantive review with its closing reply. The exact original reviews were recovered from their completed shell-command heredocs in the preserved JSONL transcripts and saved as `review.md`; the closing replies are retained as `final-message.md`. No review text was authored or repaired by the evaluator. The documented invocation now writes the closing reply to a separate file. A stronger replication should use that corrected invocation, explicit recorded model/version settings, randomized order and blind scoring across the remaining cases.
