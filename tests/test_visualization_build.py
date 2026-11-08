"""The viewer bundles readable sources into a fresh, self-contained HTML file."""
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build_visualization import render
from markdown_graph import load_graph


class VisualizationBuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        self.template = ('<style>/*__STYLES__*/</style>'
                         '<script id="catalog-data" type="application/json">/*__CATALOG__*/null</script>'
                         '<script>/*__APP__*/</script>')
        (self.directory / 'template.html').write_text(self.template)
        (self.directory / 'styles.css').write_text('body { color: white; }\n')
        (self.directory / 'app.js').write_text('const bundled = true;\n')

    def test_assets_and_escaped_catalog_are_embedded(self):
        data = {'note': '</script><script>unsafe</script>\u2028\u2029'}
        page = render(data, self.directory)
        self.assertIn('body { color: white; }', page)
        self.assertIn('const bundled = true;', page)
        payload = re.search(r'type="application/json">(.*?)</script>', page, re.S)[1]
        self.assertNotIn('<', payload)
        self.assertNotIn('\u2028', payload)
        self.assertNotIn('\u2029', payload)
        self.assertEqual(json.loads(payload), data)

    def test_marker_like_content_is_not_reinterpreted(self):
        data = {'note': '/*__APP__*/ and /*__STYLES__*/'}
        page = render(data, self.directory)
        payload = re.search(r'type="application/json">(.*?)</script>', page, re.S)[1]
        self.assertEqual(json.loads(payload), data)

    def test_missing_or_duplicate_placeholders_are_rejected(self):
        for marker in ['/*__STYLES__*/', '/*__APP__*/', '/*__CATALOG__*/null']:
            for replacement in ['', marker * 2]:
                with self.subTest(marker=marker, replacement=replacement):
                    (self.directory / 'template.html').write_text(self.template.replace(marker, replacement))
                    with self.assertRaisesRegex(ValueError, 'exactly one viewer placeholder'):
                        render({}, self.directory)

    def test_generated_viewer_matches_all_current_sources(self):
        actual = (ROOT / 'visualization/index.html').read_text()
        self.assertEqual(actual, render(load_graph()))
        self.assertNotRegex(actual, r'<script\b[^>]*\bsrc=')
        self.assertNotRegex(actual, r'<link\b[^>]*\brel=[\'"]stylesheet')
        self.assertIn('function initialize()', actual)


if __name__ == '__main__':
    unittest.main()
