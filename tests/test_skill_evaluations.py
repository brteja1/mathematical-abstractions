"""Keep paired evaluation inputs equal and evaluator answers out of model workspaces."""
import importlib.util
import json
import contextlib
import io
import sys
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('prepare_skill_evaluation', ROOT / 'ai/evaluations/prepare.py')
PREPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PREPARE)


class SkillEvaluationTests(unittest.TestCase):
    def test_cases_cover_all_skills_with_real_prompts(self):
        cases = json.loads((PREPARE.SUITE / 'cases.json').read_text())
        self.assertEqual(len({c['id'] for c in cases}), len(cases))
        skills = set()
        for case in cases:
            self.assertTrue((PREPARE.SUITE / case['prompt']).is_file())
            for destination, source in case.get('fixtures', {}).items():
                self.assertEqual(Path(destination).name, destination)
                self.assertTrue((PREPARE.SUITE / source).is_file())
            for skill in case['skills']:
                self.assertTrue((ROOT / 'ai/skills' / skill / 'SKILL.md').is_file())
                skills.add(skill)
        self.assertEqual(skills, {p.name for p in (ROOT / 'ai/skills').iterdir()
                                 if (p / 'SKILL.md').is_file()})

    def test_prepared_pair_has_identical_common_inputs_and_no_answer_keys(self):
        # A tiny snapshot verifies isolation mechanics without copying runtimes.
        def snapshot(destination):
            destination.mkdir()
            (destination / 'reference.txt').write_text('same mathematical reference\n')
            return {}

        with tempfile.TemporaryDirectory() as temp, patch.object(PREPARE, 'snapshot', snapshot):
            output = PREPARE.prepare('11', Path(temp) / 'pair')
            manifest = json.loads((output / 'manifest.json').read_text())
            baseline, treatment = output / 'without-skills', output / 'with-skills'
            for relative, digest in manifest['commonInputHashes'].items():
                for arm in (baseline, treatment):
                    self.assertEqual(PREPARE.hashes(arm)[relative], digest)
            self.assertFalse((baseline / 'catalog/ai/skills').exists())
            self.assertTrue((treatment / 'catalog/ai/skills/abstraction-discovery/SKILL.md').exists())
            for arm in (baseline, treatment):
                self.assertFalse((arm / 'grader.md').exists())
                self.assertFalse((arm / 'quality-rubric.md').exists())
                self.assertFalse((arm / 'quality_checks.py').exists())
                self.assertFalse((arm / 'results').exists())
                self.assertFalse((arm / 'AGENTS.md').exists())
                self.assertTrue((arm / 'WORKSPACE.md').is_file())
                self.assertIn('WORKSPACE.md', (arm / 'prompt.txt').read_text())
                self.assertEqual((arm / 'scheduler_api.py').read_bytes(),
                                 (PREPARE.SUITE / 'fixtures/scheduler_api.py').read_bytes())
            with self.assertRaisesRegex(ValueError, 'already exists'):
                PREPARE.prepare('01', output)

    def test_unknown_case_and_source_tree_destination_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown case'):
            PREPARE.prepare('missing', Path('/tmp/unused-skill-eval'))
        with self.assertRaisesRegex(ValueError, 'outside the source repository'):
            PREPARE.prepare('01', ROOT / 'ai/evaluations/should-not-be-created')

    def test_snapshot_preserves_projection_metadata_and_shapes(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / 'source'; source.mkdir()
            for name in ('concepts', 'data', 'scripts', 'lean', 'ontology', 'visualization', 'docs'):
                (source / name).mkdir()
            (source / 'docs/AGENT_WORKFLOWS.md').write_text('not a common model input')
            names = ('.ontfs.ttl', '.ontfs.generated.json', '.ontfs.shapes.ttl')
            for name in names: (source / name).write_text('fixture ' + name)
            destination = Path(temp) / 'snapshot'
            with patch.object(PREPARE, 'ROOT', source): PREPARE.snapshot(destination)
            for name in names:
                self.assertEqual((destination / name).read_bytes(), (source / name).read_bytes())
            self.assertFalse((destination / 'docs/AGENT_WORKFLOWS.md').exists())



    def test_generic_runner_and_collector_without_vendor_transcripts(self):
        # Real child processes exercise stdin, cwd, argv and optional metadata.
        with patch.object(sys, 'path', [str(PREPARE.SUITE), *sys.path]):
            import run_quality
            import collect_quality

        def tiny_snapshot(destination):
            destination.mkdir()
            (destination / 'reference.txt').write_text('reference')
            return {}

        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            wrapper = base / 'agent.py'
            wrapper.write_text("""import json, pathlib, sys
prompt = sys.stdin.read()
assert 'WORKSPACE.md' in prompt
assert pathlib.Path('TASK.md').is_file()
assert sys.argv[1:] == ['test-model', 'low']
pathlib.Path('answer.md').write_text('fake task artifact')
if pathlib.Path('catalog/ai/skills').exists():
    pathlib.Path('agent-metadata.json').write_text(json.dumps({
        'usage': {'outputTokens': 7}, 'commands': ['python3 check.py']}))
print('plain text output, not JSON')
""")
            config = base / 'agent.json'
            config.write_text(json.dumps({'agent': 'local-test', 'version': '1',
                'command': [sys.executable, str(wrapper), '{model}', '{effort}']}))
            output = base / 'run'
            argv = ['run_quality.py', '--out', str(output), '--agent-config', str(config),
                    '--model', 'test-model', '--effort', 'low', '--execute']
            with patch.object(sys, 'argv', argv), patch.object(PREPARE, 'snapshot', tiny_snapshot), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(run_quality.main(), 0)
            plan = json.loads((output / 'plan.json').read_text())
            self.assertEqual(len(plan['schedule']), 6)
            self.assertEqual(plan['agentConfig']['agent'], 'local-test')
            for item in plan['schedule']:
                arm = output / ('case-' + item['case']) / item['arm']
                self.assertEqual(json.loads((arm / 'run.json').read_text())['exitCode'], 0)
                self.assertFalse((arm / 'events.jsonl').exists())
                self.assertIn('plain text', (arm / 'stdout.txt').read_text())
            archive = base / 'archive'
            with patch.object(sys, 'argv', ['collect_quality.py', '--run', str(output), '--out', str(archive)]), patch.object(collect_quality, 'calendar_evaluation', return_value={}), patch.object(collect_quality, 'scheduler_evaluation', return_value={}), patch.object(collect_quality.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, '', '')), contextlib.redirect_stdout(io.StringIO()):
                collect_quality.main()
            metrics = json.loads((archive / 'metrics.json').read_text())
            for case in ('10', '11', '12'):
                baseline = metrics[case + '/without-skills']
                guided = metrics[case + '/with-skills']
                self.assertIsNone(baseline['usage'])
                self.assertIsNone(baseline['completedCommands'])
                self.assertEqual(guided['usage']['outputTokens'], 7)
                self.assertEqual(guided['completedCommands'], 1)
                self.assertEqual(guided['changedCommonInputs'], [])

    def test_runner_requires_explicit_execution_and_valid_configuration(self):
        with patch.object(sys, 'path', [str(PREPARE.SUITE), *sys.path]):
            import run_quality
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            config = base / 'agent.json'
            output = base / 'run'
            argv = ['run_quality.py', '--out', str(output), '--agent-config', str(config), '--model', 'test']
            for content, execute in [({'agent': 'test', 'command': ['unused']}, False),
                                     ({'agent': 'test', 'command': ['{unknown}']}, True),
                                     ({'agent': 'test', 'command': 'shell command'}, True),
                                     ([], True)]:
                config.write_text(json.dumps(content))
                with patch.object(sys, 'argv', argv + (['--execute'] if execute else [])), contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as exc:
                        run_quality.main()
                    self.assertEqual(exc.exception.code, 2)
                self.assertFalse(output.exists())

if __name__ == '__main__':
    unittest.main()
