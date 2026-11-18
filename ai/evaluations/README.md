# Paired skill evaluations

This suite compares the same user task in fresh sessions **without repository skill instructions** and **with the selected skills**. Both arms have the same catalog, task inputs, tools and budget. This measures the added value of the skill instructions given catalog access; it does not measure the combined value of skills plus catalog versus a model with neither.

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

## Harder quality evaluations

Cases 10–12 evaluate the artifacts beyond task completion. The evaluator-only [quality rubric](quality-rubric.md) separates behavioral correctness, test defect detection, specification precision, code maintainability, test maintainability and reviewer readability. Human comprehension requires actual readers; anonymous packets and questions support that trial without claiming human results before it occurs.

The [independent checks](quality_checks.py) validate case 10 against 18 contract scenarios, including seeded mixed histories. Case 11 runs each generated test suite against two correct implementations (including an opaque state type with different tie behavior) and ten prevalidated semantic mutants. Behavioral failures detect defects; import or syntax failures are invalid evidence. Validate the evaluator fixtures before running models:

```sh
python3 ai/evaluations/quality_checks.py --case self-test --out /tmp/scheduler-oracle-validation.json
```

The [hard-case runner](run_quality.py) freezes evaluator and prompt hashes, prepares all pairs before generation, randomizes arm order with a recorded seed, sets the same explicit model/reasoning request, and saves separate task artifacts and final replies. It starts six paid model sessions only with `--execute`:

```sh
python3 ai/evaluations/run_quality.py --out /tmp/skill-quality-run \
  --model MODEL --effort medium --timeout 480 --execute
```

Use a model available in your environment. One pair per hard case broadens task coverage but still does not measure run-to-run variation. Report dimension-level differences and concrete examples rather than declaring one arm universally better.

## Prepare a pair

Run from this repository. The helper uses Python's standard library and does not call a model, install dependencies or change the source catalog:

```sh
python3 ai/evaluations/prepare.py --case 01 --out /tmp/skill-eval-01
```

It creates `without-skills/` and `with-skills/`, each with identical `TASK.md`, neutral workspace instructions, a catalog snapshot and a generated `prompt.txt`. Only the treatment includes `catalog/ai/skills/` and instructions to read the selected entrypoints. Copying all skills to that arm permits ordinary cross-skill routing; loaded entrypoints are recorded in `manifest.json`.

Snapshots include authoritative graph files, tools, selected workflow documentation and Lean sources. If installed, `.venv`, `deps/ONTFS` and `lean/.lake` are shared by symlink for both arms; these runtimes must remain unchanged. These are convenient workspaces, **not OS security boundaries**. Use separate containers/read mounts for strict isolation. Do not run inside this repository: its `AGENTS.md` already exposes the skills. Disable repository skill registration and prior-session memory in the baseline host; record any unavoidable host/global instructions or tools as possible contamination. The helper cannot control host policy.

## Run and retain evidence

Start a fresh session for each generated prompt, using its arm directory as the working directory. Use the same model/version, reasoning setting, tool permissions, network policy and time/token budget. Do not inherit this conversation. Record the model's actual resolved settings rather than assuming a requested alias was honored. Exclude evaluator files and the other arm's directory. Allow both arms equal catalog access; only treatment receives the skill files. Retain prompts, final answers, tool transcripts, elapsed time, token usage if available, errors and artifact hashes.

For a CLI supporting these options, one manual invocation is:

```sh
cd /tmp/skill-eval-01/without-skills
codex exec --ignore-user-config --ephemeral --skip-git-repo-check \
  --sandbox workspace-write --json --output-last-message final-message.md - \
  < prompt.txt > events.jsonl 2> stderr.txt
```

Repeat in the treatment directory with identical settings. Keep `final-message.md` distinct from the task's `answer.md`: the CLI writes its final reply after the model's task artifacts and would otherwise overwrite the review. Check your installed CLI's help; tool availability is a host property. This command may use a paid model. The helper itself never starts runs. Stop on authentication/network/tool blockers and record them; do not count an infrastructure failure as a skill failure.

For a first pilot use case 01 with a 5-minute wall-clock cap per arm, sequentially. For repeated evaluation use at least three independent runs per case, randomize arm order, and counterbalance it across repeats. Record the run order before reading answers. A single pair is exploratory and cannot establish a general efficacy improvement.

Case 07 preselects task-local retention to keep its two budgets comparable. To evaluate the post-verification choice separately, remove that sentence in **both** prompts and script the same user response when the choice appears; record turn counts and time waiting separately. Do not score an appropriate clarification as a failure.

## Score and compare

After both sessions finish, assign anonymous output labels and score with [grader.md](grader.md), preferably using an independent reviewer unaware of the arm. Report correctness, missed defects, false positives, runnable evidence, task completion and cost separately. Stable catalog IDs and workflow compliance are useful process diagnostics, not correctness bonuses unavailable to the baseline. Do not substitute verbosity, test counts, code coverage or a Lean structure declaration for task success.

Record scores in a CSV file outside the repository; leave unmeasured fields blank. A failed/unperformed check is not a passing result. For case 05 run the generated tests against the known-good implementation and semantic mutants described in the grader; count killed mutants only when the failure is an assertion about behavior, not an import/syntax error. Retain counterexamples, failing seeds and commands. For case 07 require actual Lean compilation and axiom audits in both arms before awarding verified proof credit.

Keep actual reports outside the repository with raw evidence and limitations. Separate authored examples, evaluator fixture checks and actual independently generated model outputs. Publishing a prompt suite or validating its fixtures does not demonstrate that skills improve results.
