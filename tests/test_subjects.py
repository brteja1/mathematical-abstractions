"""Subject containment stays distinct from mathematical specialization."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from markdown_graph import load_graph
from subjects import category_path, in_category


class SubjectNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = {n['id']: n for n in load_graph()['@graph']}

    def test_nested_memberships_include_ancestors(self):
        bakery = self.index['urn:csabs:concept/LamportBakery']
        self.assertTrue(in_category(self.index, bakery, 'concurrency'))
        self.assertTrue(in_category(self.index, bakery, 'synchronization'))
        self.assertTrue(in_category(self.index, bakery, 'urn:csabs:category/lock-protocols'))
        self.assertFalse(in_category(self.index, bakery, 'locks'))
        self.assertEqual(category_path(self.index, bakery['category'][0]), [
            'urn:csabs:category/concurrency', 'urn:csabs:category/synchronization',
            'urn:csabs:category/lock-protocols'])

    def test_secondary_memberships_survive(self):
        trie = self.index['urn:csabs:concept/Trie']
        for subject in ['data-structures', 'tree-structures', 'associative-collections']:
            self.assertTrue(in_category(self.index, trie, subject))

    def test_subject_group_is_not_a_specialization_parent(self):
        bakery = self.index['urn:csabs:concept/LamportBakery']
        self.assertFalse(bakery.get('specializationOf'))
        self.assertEqual(self.index['urn:csabs:concept/Mutex']['specializationOf'],
                         ['urn:csabs:concept/Lock'])

    def test_cli_parent_and_full_id_queries_agree(self):
        def query(category):
            result = subprocess.check_output([sys.executable, str(ROOT / 'scripts/catalog.py'),
                                             'list', '--category', category], text=True)
            return {n['shortForm'] for n in json.loads(result)}
        expected = {'Lock', 'Mutex', 'LamportBakery'}
        self.assertEqual(query('synchronization'), expected)
        self.assertEqual(query('urn:csabs:category/synchronization'), expected)

    @unittest.skipUnless(shutil.which('node'), 'Node.js needed for viewer layout checks')
    def test_relation_layout_handles_multiple_parents_and_cycles(self):
        template = (ROOT / 'visualization/app.js').read_text()
        algorithm = template.split('// layout-ranks:start')[1].split('// layout-ranks:end')[0]
        assertions = r'''
const assert=require('node:assert/strict');
const edge=(source,target)=>({source,target});
let ranks=relationLayers(['root','left','right','child','alone'],[
 edge('left','root'),edge('right','root'),edge('child','left'),edge('child','right')]);
assert.equal(ranks.get('root'),0);assert.equal(ranks.get('child'),2);
assert.equal(ranks.get('alone'),0);
ranks=relationLayers(['a','b','consumer'],[edge('a','b'),edge('b','a'),edge('consumer','a')]);
assert.equal(ranks.get('a'),ranks.get('b'));assert.equal(ranks.get('consumer'),ranks.get('a')+1);
assert.equal(relationLayers([],[]).size,0);
'''
        subprocess.run(['node', '-e', algorithm + assertions], check=True, capture_output=True, text=True)


if __name__ == '__main__':
    unittest.main()
