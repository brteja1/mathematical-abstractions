# Paired skill evaluations

This suite compares the same user task in fresh sessions **without repository skill instructions** and **with the selected skills**. Both arms have the same catalog, task inputs, tools and budget. This measures the added value of the skill instructions given catalog access; it does not measure the combined value of skills plus catalog versus a model with neither.

The protocol works with any AI agent that can read the task and use the required tools. Workspace instructions are explicit Markdown inputs; scoring does not depend on a vendor transcript format.

The prompts are realistic tasks with seeded pitfalls and controls. They request outcomes without prescribing the skill's reasoning steps. Evaluator-only [criteria](grader.md) identify correct results, false positives and evidence requirements. Do not give that file, other outputs or past-session memory to either evaluated session.

| Case | Primary skill | What the comparison probes |
| --- | --- | --- |
| [01](prompts/01-discovery.md) | abstraction-discovery | Broken reducer laws; preserving ordered diagnostic semantics |
| [02](prompts/02-consistency.md) | specification-consistency | Joint consistency versus required-input coverage |
| [03](prompts/03-implementation.md) | implementation-mapping | Implementing exact arithmetic, errors and representation choices |
| [04](prompts/04-conformance.md) | implementation-conformance | Incorrect mapping versus code defect; permitted tie choice |
| [05](prompts/05-tests.md) | mathematical-tests | Runnable tests and defect detection rather than test counts |
| [06](prompts/06-concurrency.md) | formal-model-checking | Split atomic actions, a concrete trace, safety versus liveness |
| [07](prompts/07-acquisition.md) | abstraction-acquisition | Reuse before invention, a concrete Lean model and resumed task |
| [08](prompts/08-proof-control.md) | abstraction-acquisition | Detecting circular proof evidence and conditional assumptions |
| [09](prompts/09-no-algebra-control.md) | abstraction-discovery | Avoiding unnecessary mathematical structure |
| [10](prompts/10-calendar-quality.md) | implementation-mapping, mathematical-tests, implementation-conformance | Persistent interval algorithms; code, spec and test quality |
| [11](prompts/11-scheduler-test-quality.md) | mathematical-tests | Stateful test efficacy against ten hidden faults and two correct representations |
| [12](prompts/12-quota-spec-quality.md) | specification-consistency, formal-model-checking | Implementable distributed specification, conflicts and lifecycle semantics |
| [13](prompts/13-requirements.md) | requirements-formalization | Intent, required scenarios and unresolved promises |
| [14](prompts/14-composition.md) | compositional-verification | Local guarantees versus a shared global invariant |
| [15](prompts/15-refinement.md) | implementation-refinement | Actual-source Lean proof and behavioral mutant |
| [16](prompts/16-maintenance.md) | spec-driven-development (maintenance workflow) | Input freshness and defect-detecting re-execution |
| [17](prompts/17-assurance.md) | implementation-conformance (assurance review mode) | Weak tests, unlinked proofs and stale claims |
| [18](prompts/18-lifecycle.md) | spec-driven-development | Specified implementation, evidence gate and maintenance |

## Prepare a pair

Run from this repository. The helper uses Python's standard library and does not invoke an agent or install dependencies:

```sh
python3 ai/evaluations/prepare.py --case 01 --out /tmp/skill-eval-01
```

It creates `without-skills/` and `with-skills/` with identical `TASK.md`, `WORKSPACE.md`, catalog snapshots and task fixtures. Each generated `prompt.txt` explicitly asks the agent to read the workspace instructions; automatic discovery of an agent-specific instruction filename is unnecessary. Only the treatment receives `catalog/ai/skills/` and instructions to read the selected entrypoints. All skills are copied there for cross-skill routing; selected entrypoints and input hashes are recorded in `manifest.json`.

Snapshots include authoritative graph files, tools, selected workflow documentation and Lean sources. Installed `.venv`, `deps/ONTFS` and `lean/.lake` runtimes are shared by symlink and must remain unchanged. These workspaces are not OS security boundaries. Use containers/read mounts for strict isolation. Run outside the source repository to avoid inherited repository instructions. Disable host skill registration and past-session memory for both arms; disclose unavoidable global instructions or tools. The helper cannot control host policy.

## Run with any agent

Start a fresh session in each arm directory and submit the entire `prompt.txt`. Use the same agent/model version, reasoning settings, permissions, network policy, tools and time/token budget in both arms. Do not inherit the preparing conversation. Exclude evaluator files and the other arm. Retain prompts, task artifacts, final replies, native transcripts, elapsed time, usage where available, errors and artifact hashes. Record resolved settings separately from requested aliases.

For an interactive agent, use its normal fresh-session interface. For automation, write a wrapper that accepts the prompt on stdin, runs in the current directory, and waits until the session finishes:

```sh
cd /tmp/skill-eval-01/without-skills
/path/to/agent-wrapper < prompt.txt > stdout.txt 2> stderr.txt
```

Configure session isolation, instruction loading, permissions and transcript export using your agent's supported options. Repeat in the treatment directory with identical settings. Save the final reply separately from requested task files such as `answer.md`. Stop on authentication/network/tool blockers and disclose them; infrastructure failures are not skill failures.

For an initial pilot, use case 01 with a five-minute cap per arm. For repeated evaluations, use at least three independent runs per case, randomize arm order and counterbalance across repeats. Record the order before reading answers. One pair is exploratory evidence. Case 07 preselects task-local retention to keep budgets comparable; to evaluate the post-verification choice, remove that sentence in both prompts and supply the same user response. Record clarification turns and waiting time separately.

## Automated hard-case runs

Cases 10–12 evaluate code, tests and specifications beyond task completion. The evaluator-only [quality rubric](quality-rubric.md) separates correctness, defect detection, specification precision, maintainability and readability. Human comprehension requires actual readers; prepared packets alone are not measured human results.

Validate the [independent checks](quality_checks.py) before running agents. Case 10 has 18 contract scenarios and seeded histories; case 11 uses two correct implementations and ten semantic mutants. Import/syntax failures do not count as behavioral defect detection.

```sh
python3 ai/evaluations/quality_checks.py --case self-test --out /tmp/scheduler-oracle-validation.json
```

The [runner](run_quality.py) prepares all pairs before generation, freezes evaluator/prompt hashes and records randomized arm order. Supply an external agent configuration:

```json
{
  "agent": "your-agent-name",
  "version": "installed-version",
  "command": ["/absolute/path/to/agent-wrapper", "--model", "{model}", "--effort", "{effort}"]
}
```

The command is an argv array executed without a shell. Only `{model}` and `{effort}` are substituted; escape literal braces as `{{` and `}}`. Omit unsupported reasoning arguments and disclose that limitation. Record other host settings in the configuration, which is archived; keep credentials out. Model/reasoning labels are requests, not verified resolved settings.

```sh
python3 ai/evaluations/run_quality.py --out /tmp/skill-quality-run \
  --agent-config /path/to/agent.json --model MODEL --effort medium \
  --timeout 480 --execute
```

Only `--execute` permits the six agent invocations, which may incur charges. Each receives `prompt.txt` on stdin and the arm directory as its working directory. The runner saves `stdout.txt`, `stderr.txt` and `run.json`; wrappers may retain native transcripts and `final-message.md`. Launch/process failures stop the schedule; timeouts are recorded. A zero exit code does not establish task completion or successful tool access.

After all runs finish, [collect artifacts](collect_quality.py) and execute the frozen checks:

```sh
python3 ai/evaluations/collect_quality.py --run /tmp/skill-quality-run \
  --out /tmp/skill-quality-archive
```

Collection does not parse native transcripts. An optional `agent-metadata.json` in each arm may contain reported resolved settings, usage counters with units, and completed command strings:

```json
{
  "resolvedSettings": {"model": "reported-model-version", "reasoning": "medium"},
  "usage": {"inputTokens": 123, "outputTokens": 45},
  "commands": ["python3 -m unittest -v"]
}
```

Omit unavailable fields: missing usage and command counts remain unknown, not zero. Metadata is reported evidence, not independently verified identity or instruction compliance. Collection works without it or a structured transcript. Preserve native transcripts for audit where available.

## Score and compare

Assign anonymous labels and score using [grader.md](grader.md), preferably with an independent reviewer unaware of the arm. Report correctness, missed defects, false positives, runnable evidence, task completion and cost separately. Catalog IDs and workflow compliance are process diagnostics, not correctness bonuses. Do not substitute verbosity, test counts, coverage or structure declarations for task success. Compare skill arms within the same agent/model configuration; report cross-agent differences separately.

Record scores in a CSV file outside the repository; leave unmeasured fields blank. For case 05, run tests against the known-good implementation and semantic mutants described in the grader; only behavioral assertion failures count as killed mutants. Retain counterexamples, seeds and commands. For case 07 require Lean compilation and axiom audits in both arms before awarding verified proof credit.

Keep reports outside the repository with raw evidence and limitations. Distinguish authored examples, fixture validation and independently generated agent outputs. Publishing prompts or validating fixtures does not demonstrate skill efficacy. Report dimension-level differences and concrete examples; one pair per hard case does not measure run-to-run variation.

Cases 13–18 cover requirements, composition, actual-source refinement, evidence
maintenance, assurance review and lifecycle delivery. Their prompts and evaluator
criteria are provided; adding them is not a measured skill-efficacy result.
