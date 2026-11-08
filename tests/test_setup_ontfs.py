"""Exercise dependency initialization against local Git repositories."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import setup_ontfs


class SetupOntfsTests(unittest.TestCase):
    def git(self, directory, *args):
        return subprocess.check_output(
            ['git', '-C', str(directory), '-c', 'protocol.file.allow=always',
             '-c', 'user.name=Setup Test', '-c', 'user.email=setup@example.invalid',
             *args], text=True, stderr=subprocess.PIPE).strip()

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name)
        upstream = base / 'upstream'
        upstream.mkdir()
        self.git(upstream, 'init')
        (upstream / 'module.py').write_text('value = 1\n')
        self.git(upstream, 'add', '.')
        self.git(upstream, 'commit', '-m', 'initial dependency')
        self.revision = self.git(upstream, 'rev-parse', 'HEAD')
        self.root = base / 'catalog'
        self.root.mkdir()
        self.git(self.root, 'init')
        self.git(self.root, 'submodule', 'add', str(upstream), 'deps/ONTFS')
        self.dependency = self.root / 'deps/ONTFS'
        self.lock = {'path': 'deps/ONTFS', 'url': str(upstream), 'commit': self.revision}
        (self.root / 'dependencies.lock.json').write_text(json.dumps({'ONTFS': self.lock}))
        self.index = self.git(self.root, 'ls-files', '--stage')
        self.addCleanup(patch.stopall)
        patch.object(setup_ontfs, 'ROOT', self.root).start()
        # git()'s default argument was bound when the module was imported.
        original = setup_ontfs.git
        patch.object(setup_ontfs, 'git',
                     side_effect=lambda *args, cwd=None: original(*args, cwd=cwd or self.root)).start()
        patch.dict(os.environ, {'GIT_ALLOW_PROTOCOL': 'file'}).start()

    def test_reuses_expected_revision_without_touching_local_edits_or_index(self):
        module = self.dependency / 'module.py'
        module.write_text('local work\n')
        setup_ontfs.main()
        self.assertEqual(module.read_text(), 'local work\n')
        self.assertEqual(self.git(self.root, 'ls-files', '--stage'), self.index)

    def test_initializes_missing_dependency_without_staging(self):
        self.git(self.root, 'submodule', 'deinit', '-f', '--', 'deps/ONTFS')
        setup_ontfs.main()
        self.assertEqual(self.git(self.dependency, 'rev-parse', 'HEAD'), self.revision)
        self.assertEqual(self.git(self.root, 'ls-files', '--stage'), self.index)

    def test_refuses_to_switch_modified_dependency(self):
        self.git(self.dependency, 'commit', '--allow-empty', '-m', 'local revision')
        (self.dependency / 'module.py').write_text('uncommitted work\n')
        head = self.git(self.dependency, 'rev-parse', 'HEAD')
        with self.assertRaisesRegex(SystemExit, 'local changes'):
            setup_ontfs.main()
        self.assertEqual(self.git(self.dependency, 'rev-parse', 'HEAD'), head)
        self.assertEqual(self.git(self.root, 'ls-files', '--stage'), self.index)

    def test_refuses_inconsistent_registration(self):
        self.lock['commit'] = '0' * 40
        (self.root / 'dependencies.lock.json').write_text(json.dumps({'ONTFS': self.lock}))
        with self.assertRaisesRegex(SystemExit, 'Git index'):
            setup_ontfs.main()
        self.assertEqual(self.git(self.root, 'ls-files', '--stage'), self.index)
