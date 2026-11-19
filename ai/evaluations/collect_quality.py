#!/usr/bin/env python3
"""Archive completed hard runs and execute frozen evaluator checks, without model calls."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import shutil
import subprocess
import sys

from prepare import SUITE
from quality_checks import REFERENCE, calendar_evaluation, scheduler_evaluation

QUESTIONS = {
    '10': [
        'Where is an ID conflict checked, and what remains unchanged after failure?',
        'Why do adjacent intervals coalesce in occupied spans but not overlap for peak?',
        'Can two booking IDs share the same interval? Show the relevant code and spec.',
        'What would change to add a read-only occupied_length observer?',
        'For which inputs is merge associativity a valid guarantee?'],
    '11': [
        'Which test catches expiration exactly at the deadline?',
        'How does this suite avoid enforcing a particular tie order?',
        'What observation establishes that a rejected backwards-time call changes no state?',
        'Which tests establish that changes to either clone leave the other independent?',
        'How would you add another allowed tie-breaking strategy without rewriting the tests?'],
    '12': [
        'During a partition, which replica may accept which reservation IDs and amounts?',
        'What happens when a release is delivered before its reserve?',
        'What prevents a delayed old request from recreating released usage?',
        'Which original stakeholder promises change in the proposed contract?',
        'Which assumptions justify convergence, and which would justify a numerical deadline?'],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists(): parser.error('Output already exists; choose a fresh archive directory')
    plan = json.loads((args.run / 'plan.json').read_text())
    for relative, digest in plan['frozenEvaluatorHashes'].items():
        if hashlib.sha256((SUITE / relative).read_bytes()).hexdigest() != digest:
            parser.error('Frozen evaluator changed: ' + relative)
    if not all((args.run / ('case-' + item['case']) / item['arm'] / 'run.json').exists()
               for item in plan['schedule']):
        parser.error('Wait until all scheduled runs have finished')
    args.out.mkdir(parents=True)
    shutil.copy2(args.run / 'plan.json', args.out / 'plan.json')
    for relative in plan['frozenEvaluatorHashes']:
        target = args.out / 'frozen-evaluator' / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SUITE / relative, target)
    reference_target = args.out / 'frozen-evaluator/fixtures/scheduler_api.py'
    reference_target.parent.mkdir(parents=True, exist_ok=True)
    reference_target.write_text(REFERENCE)
    metrics = {}
    reader_key = {}
    rng = random.Random(915702)
    for case in ('10', '11', '12'):
        pair = args.run / ('case-' + case)
        target = args.out / ('case-' + case)
        target.mkdir()
        manifest = json.loads((pair / 'manifest.json').read_text())
        if case == '11' and hashlib.sha256(REFERENCE.encode()).hexdigest() != manifest['commonInputHashes']['scheduler_api.py']:
            parser.error('Scheduler reference changed after the model inputs were frozen')
        shutil.copy2(pair / 'manifest.json', target / 'manifest.json')
        labels = ['A', 'B']; rng.shuffle(labels)
        for arm, label in zip(('without-skills', 'with-skills'), labels):
            source = pair / arm
            dest = target / arm; dest.mkdir()
            for path in source.iterdir():
                if path.is_file() and not path.is_symlink(): shutil.copy2(path, dest / path.name)
            metadata_path = source / 'agent-metadata.json'
            metadata = json.loads(metadata_path.read_text()) if metadata_path.exists() else {}
            if not isinstance(metadata, dict):
                parser.error('Agent metadata must be a JSON object: ' + str(metadata_path))
            commands = metadata.get('commands')
            if commands is not None and (not isinstance(commands, list) or
                                         not all(isinstance(c, str) for c in commands)):
                parser.error('Agent metadata commands must be an array of strings')
            changed = [name for name, digest in manifest['commonInputHashes'].items()
                       if not (source / name).is_file() or
                       hashlib.sha256((source / name).read_bytes()).hexdigest() != digest]
            result = {'run': json.loads((source / 'run.json').read_text()),
                      'usage': metadata.get('usage'), 'agentMetadata': metadata, 'changedCommonInputs': changed,
                      'changedSkillInputs': [name for name, digest in manifest['skillInputHashes'].items()
                                             if arm == 'with-skills' and
                                             (not (source / 'catalog/ai/skills' / name).is_file() or
                                              hashlib.sha256((source / 'catalog/ai/skills' / name).read_bytes()).hexdigest() != digest)],
                      'completedCommands': len(commands) if commands is not None else None}
            if case == '10':
                result['independentContract'] = calendar_evaluation(source)
            elif case == '11':
                result['mutationEvaluation'] = scheduler_evaluation(source)
            if case in ('10', '12'):
                command = [sys.executable, '-B', '-m', 'unittest', '-v', 'test_calendar'] if case == '10' else [sys.executable, '-B', 'checks.py']
                try:
                    run = subprocess.run(command, cwd=source, text=True, capture_output=True, timeout=60)
                    result['generatedChecksRerun'] = {'command': command, 'exitCode': run.returncode,
                                                     'output': run.stdout + run.stderr}
                except subprocess.TimeoutExpired:
                    result['generatedChecksRerun'] = {'command': command, 'exitCode': None, 'output': 'timeout'}
            result['artifactHashes'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                        for p in sorted(dest.iterdir()) if p.is_file()}
            (dest / 'evaluation.json').write_text(json.dumps(result, indent=2) + '\n')
            metrics[case + '/' + arm] = result
            packet = args.out / 'human-reading' / ('case-' + case) / label
            packet.mkdir(parents=True)
            for name in ('TASK.md', 'spec.md', 'mapping.md', 'calendar_api.py', 'test_calendar.py',
                         'scheduler_api.py', 'test_scheduler.py', 'test-plan.md', 'checks.py'):
                if (dest / name).exists(): shutil.copy2(dest / name, packet / name)
            (packet / 'questions.md').write_text('# Comprehension tasks\n\n' + '\n'.join(
                str(i) + '. ' + question for i, question in enumerate(QUESTIONS[case], 1)) + '\n')
            (packet / 'responses.csv').write_text('reader,question,answer,file_and_lines,seconds,confidence_1_5,accuracy_evaluator_only\n')
            reader_key[case + '/' + label] = arm
    (args.out / 'metrics.json').write_text(json.dumps(metrics, indent=2) + '\n')
    (args.out / 'reader-key-evaluator-only.json').write_text(json.dumps(reader_key, indent=2) + '\n')
    (args.out / 'human-reading/README.md').write_text('''# Human comprehension trial — not yet performed

Choose one anonymous packet per case, read its TASK.md and relevant artifacts,
then answer questions.md. Record elapsed time, confidence and file/line evidence
in responses.csv. Leave accuracy to a reviewer using the contract. Do not read
the arm key, aggregate report or the other packet before submitting answers.
Use opposite packet orders across readers. A reader who sees both variants
learns from the first; disclose that effect. Labels conceal paths and metadata,
but content such as catalog references may still suggest the arm.

These packets are prepared materials, not measured human readability results.
The suite author's quality scores are editorial judgments, not a blind trial.
''')
    print(args.out)


if __name__ == '__main__':
    main()
