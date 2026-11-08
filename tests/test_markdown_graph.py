"""Regression tests for lossless storage, linked Markdown and bounded retrieval."""
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from markdown_graph import ROOT, load_graph, outputs, read_records, BLOCK
from agent_query import traverse, dossier, resolve
from validate_graph import validate


class MarkdownGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = load_graph()
        cls.index = {n['id']: n for n in cls.doc['@graph']}

    def test_generated_projection_matches_records(self):
        for path, text in outputs(self.doc).items():
            self.assertEqual(path.read_text(), text, path.name)

    def test_build_does_not_emit_monolithic_jsonld_catalog(self):
        self.assertNotIn(ROOT / 'catalog.jsonld', outputs(self.doc))

    def test_imported_ids_remain_present(self):
        manifest = json.loads((ROOT / 'data/import_manifest.json').read_text())
        self.assertTrue(set(manifest['nodeHashes']) <= set(self.index))
        # New vocabulary may extend the context without changing any imported term.
        for term, definition in manifest['context'].items():
            self.assertEqual(definition, self.doc['@context'].get(term), term)

    def test_markdown_links_resolve(self):
        for page in (ROOT / 'concepts').glob('*.md'):
            prose = page.read_text().split('<!-- graph-record:start -->')[0]
            for filename, fragment in re.findall(r'\]\(([A-Za-z0-9_-]+\.md)(#[^)]*)?\)', prose):
                target = page.parent / filename
                self.assertTrue(target.is_file(), f'{page}: {filename}')
                if fragment:
                    self.assertIn(f'id="{fragment[1:]}"', target.read_text())

    def test_filename_must_match_concept(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'Wrong.md'
            path.write_text((ROOT / 'concepts/Group.md').read_text())
            with self.assertRaisesRegex(ValueError, 'filename'):
                read_records(path)

    def test_duplicate_record_blocks_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'Group.md'
            text = (ROOT / 'concepts/Group.md').read_text()
            path.write_text(text + BLOCK.search(text)[0])
            with self.assertRaisesRegex(ValueError, 'exactly one'):
                read_records(path)

    def test_bounded_traversal_reports_truncation(self):
        seed = resolve(self.index, 'Group')
        result = traverse(self.index, seed, ['requiresConcept'], depth=5, limit=1)
        self.assertEqual(len(result['nodes']), 1)
        self.assertTrue(result['truncated'])

    def test_incoming_edges_preserve_direction(self):
        seed = resolve(self.index, 'Monoid')
        group = resolve(self.index, 'Group')
        result = traverse(self.index, seed, ['specializationOf'], incoming=True)
        self.assertIn({'source': group, 'predicate': 'specializationOf', 'target': seed}, result['edges'])

    def test_dossier_includes_claim_premises_and_sources(self):
        seed = resolve(self.index, 'Group')
        result = dossier(self.index, seed, 'proof', 1000)
        self.assertFalse(result['truncated'])
        ids = {n['id'] for n in result['nodes']}
        for node in result['nodes']:
            for key in ['dependsOn', 'source']:
                self.assertTrue(set(node.get(key, [])) <= ids)
        self.assertIn('not an executable proof', result['interpretation'])

    def test_viewer_embeds_current_graph(self):
        text = (ROOT / 'visualization/index.html').read_text()
        payload = re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>', text, re.S)[1]
        self.assertEqual(json.loads(payload), self.doc)
        self.assertIn('Open Markdown concept page', text)


if __name__ == '__main__':
    unittest.main()
