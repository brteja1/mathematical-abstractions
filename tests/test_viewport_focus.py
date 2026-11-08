"""Shared viewport framing for graph and right-pane selections."""
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('node'), 'Node.js needed for camera checks')
class ViewportFocusTests(unittest.TestCase):
    def test_selection_bounds_padding_backoff_and_empty_case(self):
        template = (ROOT / 'visualization/app.js').read_text()
        algorithm = template.split('// selection-camera:start')[1].split('// selection-camera:end')[0]
        assertions = r'''
const assert=require('node:assert/strict');
assert.equal(selectionCamera([],3000,1.25,7),null);
assert.deepEqual(selectionCamera([{x:100,y:200,width:20,height:20}],3000,1,0),{x:110,y:210,span:180});
const boxes=[{x:100,y:200,width:20,height:20},{x:200,y:300,width:20,height:20}];
assert.deepEqual(selectionCamera(boxes,3000,1,0),{x:160,y:260,span:186});
assert.equal(selectionCamera(boxes,3000,1.25,7).span,186*1.25**7);
assert.equal(selectionCamera([{x:-500,y:-500,width:1000,height:1000}],3000,1.25,7).span,3000);
'''
        result = subprocess.run(['node', '-e', algorithm + assertions], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
