"""Validate evaluator fixtures before using them to judge generated artifacts."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('quality_checks', ROOT / 'ai/evaluations/quality_checks.py')
QUALITY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(QUALITY)

CALENDAR_REFERENCE = '''def empty(): return {}
def reserve(s, key, a, b):
    if a>=b or (key in s and s[key]!=(a,b)): raise ValueError('conflict or invalid interval')
    return dict(s, **{key:(a,b)})
def merge(a,b):
    out=dict(a)
    for key,(start,end) in b.items(): out=reserve(out,key,start,end)
    return out
def bookings(s): return tuple((key,*span) for key,span in sorted(s.items()))
def occupied(s,lo,hi):
    if lo>hi: raise ValueError('reversed window')
    spans=sorted((max(lo,a),min(hi,b)) for a,b in s.values() if max(lo,a)<min(hi,b))
    result=[]
    for a,b in spans:
        if result and a<=result[-1][1]: result[-1]=(result[-1][0],max(b,result[-1][1]))
        else: result.append((a,b))
    return tuple(result)
def peak(s):
    return max((sum(start<=point<end for start,end in s.values())
                for point in {a for a,b in s.values()}),default=0)
'''


class QualityEvaluatorTests(unittest.TestCase):
    def test_scheduler_oracle_accepts_two_representations_and_rejects_all_mutants(self):
        rows = QUALITY.scheduler_evaluation(Path('.'), oracle=True)
        for name in ('correct_dictionary', 'correct_opaque_reverse_ties'):
            self.assertEqual(rows[name]['exitCode'], 0, rows[name]['output'])
            self.assertEqual(rows[name]['tests'], 10)
        self.assertEqual(len(QUALITY.mutants()), 10)
        for name in QUALITY.mutants():
            self.assertTrue(rows[name]['behavioralKill'], (name, rows[name]['output']))

    def test_calendar_oracle_accepts_simple_reference(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / 'calendar_api.py').write_text(CALENDAR_REFERENCE)
            result = QUALITY.calendar_evaluation(workspace)
            self.assertEqual(result['tests'], 18)
            self.assertEqual(result['exitCode'], 0, result['output'])

    def test_calendar_oracle_detects_inclusive_endpoint_bug(self):
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / 'calendar_api.py').write_text(CALENDAR_REFERENCE.replace('start<=point<end', 'start<=point<=end'))
            result = QUALITY.calendar_evaluation(workspace)
            self.assertEqual(result['exitCode'], 1)
            self.assertGreater(result['failures'], 0)
            self.assertEqual(result['errors'], 0)

    def test_real_assertion_failure_is_not_discarded_when_another_test_errors(self):
        suite = '''import unittest
import scheduler_api as api
class CloneTests(unittest.TestCase):
    def pair(self):
        s=api.new(); api.put(s,'a',1,20,0)
        c=api.clone(s); api.put(c,'b',2,30,5)
        return s,c
    def test_clone_jobs(self):
        s,c=self.pair()
        self.assertEqual(api.snapshot(s,5),(('a',1,20),))
    def test_clone_clock(self):
        s,c=self.pair()
        self.assertEqual(api.snapshot(s,0),(('a',1,20),))
'''
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            (workspace / 'test_scheduler.py').write_text(suite)
            rows = QUALITY.scheduler_evaluation(workspace)
        for name in ('correct_dictionary', 'correct_opaque_reverse_ties'):
            self.assertEqual(rows[name]['exitCode'], 0)
        self.assertGreater(rows['clone_alias']['failures'], 0)
        self.assertGreater(rows['clone_alias']['errors'], 0)
        self.assertFalse(rows['clone_alias']['cleanRunFlag'])
        self.assertTrue(rows['clone_alias']['behavioralKill'])


if __name__ == '__main__':
    unittest.main()
