"""Keep paired evaluation inputs equal and evaluator answers out of model workspaces."""
import importlib.util
import json
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


if __name__ == '__main__':
    unittest.main()
