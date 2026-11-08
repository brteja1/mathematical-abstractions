"""Measured wrapping and collision priorities for the standalone atlas."""
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which('node'), 'Node.js needed for label geometry checks')
class ViewerLabelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        template = (ROOT / 'visualization/app.js').read_text()
        cls.algorithm = template.split('// label-geometry:start')[1].split('// label-geometry:end')[0]

    def run_js(self, assertions):
        subprocess.run(['node', '-e', self.algorithm + '\n' + assertions],
                       check=True, capture_output=True, text=True)

    def test_wrapping_uses_measurements_and_retains_names(self):
        self.run_js(r'''
const assert=require('node:assert/strict'),measure=s=>s.length*8;
assert.deepEqual(wrapLabel('Mutex',80,measure),['Mutex']);
assert.deepEqual(wrapLabel('SequentialConsistency',96,measure),['Sequential','Consistency']);
assert.deepEqual(wrapLabel('finite sequence',80,measure),['finite','sequence']);
let lines=wrapLabel('VeryLongUnbrokenIdentifierWithMoreWords',64,measure);
assert.equal(lines.join(''),'VeryLongUnbrokenIdentifierWithMoreWords');assert.ok(lines.every(s=>measure(s)<=64));
const variable=s=>[...s].reduce((sum,c)=>sum+(c==='W'?20:3),0);
assert.deepEqual(wrapLabel('WWii',26,variable),['W','Wii']);
assert.equal(wrapLabel('FirstOrderNaturalDeduction',180,measure).join(''),'FirstOrderNaturalDeduction');
const long='LongConceptName'.repeat(10);const complete=wrapLabel(long,64,measure);assert.equal(complete.join(''),long);assert.ok(complete.length>3);
''')

    def test_placement_is_deterministic_for_input_order(self):
        self.run_js(r'''
const assert=require('node:assert/strict');
const bounds={left:-Infinity,right:Infinity,top:-Infinity,bottom:Infinity};
const item=id=>({id,priority:10,placements:[{dx:0,dy:0,rect:{left:0,right:100,top:0,bottom:20}}]});
assert.deepEqual(placeLabels([item('b'),item('a')]).map(n=>n.id),['a']);
assert.deepEqual(placeLabels([item('a'),item('b')]).map(n=>n.id),['a']);
''')

    def test_selected_label_wins_and_alternatives_avoid_collisions(self):
        self.run_js(r'''
const assert=require('node:assert/strict');
const rect=(left,top,right,bottom)=>({left,top,right,bottom});
const box=rect(20,20,80,40),bounds=rect(0,0,150,150);
const normal={id:'normal',priority:10,placements:[{rect:box,dx:0,dy:0}]};
const selected={id:'selected',priority:400,placements:[{rect:box,dx:0,dy:0}]};
assert.deepEqual(placeLabels([normal,selected]).map(n=>n.id),['selected']);
const movable={...normal,placements:[...normal.placements,{rect:rect(20,50,80,70),dx:0,dy:30}]};
const accepted=placeLabels([movable,selected]);
assert.equal(accepted.length,2);assert.equal(accepted[1].dy,30);
assert.ok(!labelOverlap(accepted[0].rect,accepted[1].rect));
assert.equal(placeLabels([selected],[box]).length,0);
assert.equal(placeLabels([selected]).length,1);
assert.deepEqual(placeLabels([]),[]);
''')


if __name__ == '__main__':
    unittest.main()
