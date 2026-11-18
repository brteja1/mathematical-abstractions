#!/usr/bin/env python3
"""Run the three hard paired cases only with an explicit --execute request."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import random
import signal
import subprocess
import time

from prepare import ROOT, SUITE, prepare


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--effort', default='medium')
    parser.add_argument('--timeout', type=int, default=480)
    parser.add_argument('--seed', type=int, default=20261118)
    parser.add_argument('--execute', action='store_true', help='Authorize six model invocations')
    args = parser.parse_args()
    if not args.execute: parser.error('--execute is required; this run invokes a paid model')
    output = args.out.resolve()
    if output.exists() or output.is_relative_to(ROOT):
        parser.error('Choose a new output directory outside the source repository')
    output.mkdir(parents=True)
    rng = random.Random(args.seed)
    schedule = []
    for case in ('10', '11', '12'):
        prepare(case, output / ('case-' + case))
        arms = ['without-skills', 'with-skills']
        rng.shuffle(arms)
        schedule.extend({'case': case, 'arm': arm} for arm in arms)
    frozen = [SUITE / 'quality-rubric.md', SUITE / 'quality_checks.py',
              SUITE / 'run_quality.py', SUITE / 'prepare.py', SUITE / 'cases.json',
              *[SUITE / 'prompts' / name for name in
                ('10-calendar-quality.md', '11-scheduler-test-quality.md', '12-quota-spec-quality.md')]]
    plan = {'modelRequested': args.model, 'reasoningRequested': args.effort,
            'timeoutPerArmSeconds': args.timeout, 'seed': args.seed, 'schedule': schedule,
            'frozenEvaluatorHashes': {str(p.relative_to(SUITE)): hashlib.sha256(p.read_bytes()).hexdigest()
                                     for p in frozen},
            'cliVersion': subprocess.check_output(['codex', '--version'], text=True).strip(),
            'sourceStatus': subprocess.check_output(['git', 'status', '--short'], cwd=ROOT, text=True),
            'limits': ['One run per arm per task; exploratory, not statistical evidence.',
                       'Host context and runtime symlinks are not OS-isolated.',
                       'Model/reasoning are explicitly requested; backend revision may not be emitted.']}
    (output / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    for entry in schedule:
        workspace = output / ('case-' + entry['case']) / entry['arm']
        command = ['codex', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
                   '--sandbox', 'workspace-write', '--json', '--color', 'never',
                   '--model', args.model, '-c', 'model_reasoning_effort="' + args.effort + '"',
                   '--output-last-message', 'final-message.md', '-']
        print('START', entry['case'], entry['arm'], flush=True)
        start = time.monotonic()
        timed_out = False
        with (workspace / 'events.jsonl').open('w') as stdout, (workspace / 'stderr.txt').open('w') as stderr:
            process = subprocess.Popen(command, cwd=workspace, stdin=subprocess.PIPE,
                                       stdout=stdout, stderr=stderr, text=True, start_new_session=True)
            try:
                process.communicate((workspace / 'prompt.txt').read_text(), timeout=args.timeout)
            except subprocess.TimeoutExpired:
                timed_out = True
                os.killpg(process.pid, signal.SIGTERM)
                try: process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
        result = {**entry, 'command': command, 'elapsedSeconds': round(time.monotonic()-start, 2),
                  'exitCode': process.returncode, 'timedOut': timed_out}
        (workspace / 'run.json').write_text(json.dumps(result, indent=2) + '\n')
        print('FINISH', entry['case'], entry['arm'], result['exitCode'], result['elapsedSeconds'], flush=True)
        if process.returncode and not timed_out:
            print('Stopping on infrastructure/process failure; inspect stderr and events.', flush=True)
            return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
