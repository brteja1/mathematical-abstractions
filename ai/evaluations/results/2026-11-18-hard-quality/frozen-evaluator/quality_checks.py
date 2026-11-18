#!/usr/bin/env python3
"""Evaluator-only contract and mutation checks. Never copy into model workspaces."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

SUITE = Path(__file__).resolve().parent
REFERENCE = (SUITE / 'fixtures/scheduler_api.py').read_text()

ALTERNATIVE = '''class State:
    __slots__ = ('time', 'rows')
    def __init__(self, time=0, rows=()):
        self.time, self.rows = time, tuple(rows)

def new(): return State()
def _step(s, now):
    if now < s.time: raise ValueError('backwards')
    s.rows = tuple(row for row in s.rows if row[2] > now)
    s.time = now
def put(s, job_id, priority, expires_at, now):
    _step(s, now)
    s.rows = tuple(row for row in s.rows if row[0] != job_id)
    if expires_at > now: s.rows += ((job_id, priority, expires_at),)
def take(s, now):
    _step(s, now)
    if not s.rows: raise KeyError('empty')
    priority = min(row[1] for row in s.rows)
    row = max((row for row in s.rows if row[1] == priority), key=lambda row: row[0])
    s.rows = tuple(other for other in s.rows if other[0] != row[0])
    return row
def snapshot(s, now):
    _step(s, now)
    return tuple(sorted(s.rows, key=lambda row: row[0]))
def clone(s): return State(s.time, s.rows)
'''


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Fixture mutation anchor must occur once: ' + old)
    return text.replace(old, new)


def mutants():
    anchor = "    state['jobs'].pop(job_id, None)"
    return {
        'expiry_boundary': replace_once(REFERENCE, 'if row[2] > now', 'if row[2] >= now'),
        'maximum_priority': replace_once(REFERENCE, 'row = min(', 'row = max('),
        'ignore_live_replacement': replace_once(REFERENCE, anchor,
            "    if expires_at > now and job_id in state['jobs']:\n        return\n" + anchor),
        'ignore_expired_replacement': replace_once(REFERENCE, anchor,
            '    if expires_at <= now:\n        return\n' + anchor),
        'allow_backwards': replace_once(REFERENCE, "if now < state['clock']:", 'if False:'),
        'mutate_on_rejection': replace_once(REFERENCE, "        raise ValueError('time cannot move backwards')",
            "        state['jobs'].clear()\n        raise ValueError('time cannot move backwards')"),
        'clone_clock_reset': replace_once(REFERENCE, "return {'clock': state['clock'],", "return {'clock': 0,"),
        'clone_alias': replace_once(REFERENCE,
            "return {'clock': state['clock'], 'jobs': state['jobs'].copy()}", 'return state'),
        'unsorted_snapshot': replace_once(REFERENCE, "return tuple(state['jobs'][key] for key in sorted(state['jobs']))",
            "return tuple(state['jobs'].values())"),
        'drop_on_equal_time': replace_once(REFERENCE, "    state['clock'] = now",
            "    if now == state['clock']:\n        state['jobs'].clear()\n    state['clock'] = now"),
    }


SCHEDULER_ORACLE = '''import unittest
import scheduler_api as api

class SchedulerContract(unittest.TestCase):
    def test_expiry_boundary(self):
        s=api.new(); api.put(s,'a',0,5,0)
        self.assertEqual(api.snapshot(s,5),())
    def test_minimum_priority(self):
        s=api.new(); api.put(s,'a',-5,10,0); api.put(s,'b',4,10,0)
        self.assertEqual(api.take(s,1),('a',-5,10))
    def test_live_replacement(self):
        s=api.new(); api.put(s,'a',3,10,0); api.put(s,'a',-2,20,1)
        self.assertEqual(api.snapshot(s,1),(('a',-2,20),))
    def test_expired_replacement(self):
        s=api.new(); api.put(s,'a',3,10,0); api.put(s,'a',8,1,1)
        self.assertEqual(api.snapshot(s,1),())
    def test_backwards_rejected(self):
        s=api.new(); api.snapshot(s,5)
        with self.assertRaises(ValueError): api.snapshot(s,4)
    def test_rejection_preserves_jobs(self):
        s=api.new(); api.put(s,'a',3,10,5)
        with self.assertRaises(ValueError): api.put(s,'b',0,20,4)
        self.assertEqual(api.snapshot(s,5),(('a',3,10),))
    def test_clone_clock(self):
        s=api.new(); api.snapshot(s,5); t=api.clone(s)
        with self.assertRaises(ValueError): api.snapshot(t,4)
    def test_clone_independence(self):
        s=api.new(); api.put(s,'a',0,10,0); t=api.clone(s)
        api.put(t,'b',1,20,1)
        self.assertEqual(api.snapshot(s,1),(('a',0,10),))
    def test_sorted_snapshot(self):
        s=api.new(); api.put(s,'z',0,10,0); api.put(s,'a',1,10,0)
        self.assertEqual(api.snapshot(s,0),(('a',1,10),('z',0,10)))
    def test_equal_time(self):
        s=api.new(); api.put(s,'a',0,10,0)
        self.assertEqual(api.snapshot(s,0),(('a',0,10),))
'''

CALENDAR_ORACLE = '''import unittest
import random
import calendar_api as api

class CalendarContract(unittest.TestCase):
    def test_empty(self):
        s=api.empty(); self.assertEqual(api.bookings(s),()); self.assertEqual(api.peak(s),0)
        self.assertEqual(api.occupied(s,-10,10),())
    def test_replay(self):
        s=api.reserve(api.empty(),'a',1,5)
        self.assertEqual(api.bookings(api.reserve(s,'a',1,5)),(('a',1,5),))
    def test_conflict_persistence(self):
        s=api.reserve(api.empty(),'a',1,5)
        with self.assertRaises(ValueError): api.reserve(s,'a',1,6)
        self.assertEqual(api.bookings(s),(('a',1,5),))
    def test_invalid_interval(self):
        s=api.empty()
        for a,b in ((0,0),(3,1)):
            with self.assertRaises(ValueError): api.reserve(s,'x',a,b)
        self.assertEqual(api.bookings(s),())
    def test_persistence(self):
        old=api.reserve(api.empty(),'a',0,4); new=api.reserve(old,'b',2,8)
        self.assertEqual(api.bookings(old),(('a',0,4),)); self.assertEqual(api.peak(new),2)
    def test_sorted_rows(self):
        s=api.reserve(api.reserve(api.empty(),'z',0,2),'a',1,3)
        self.assertEqual(api.bookings(s),(('a',1,3),('z',0,2)))
    def test_duplicate_interval_distinct_ids(self):
        s=api.reserve(api.reserve(api.empty(),'a',0,5),'b',0,5)
        self.assertEqual(api.peak(s),2); self.assertEqual(api.occupied(s,0,5),((0,5),))
    def test_compatible_merge(self):
        a=api.reserve(api.empty(),'a',0,2); b=api.reserve(api.empty(),'b',1,4)
        c=api.merge(a,b)
        self.assertEqual(api.bookings(c),(('a',0,2),('b',1,4)))
        self.assertEqual(api.bookings(a),(('a',0,2),)); self.assertEqual(api.bookings(b),(('b',1,4),))
    def test_merge_replay(self):
        s=api.reserve(api.empty(),'a',0,2)
        self.assertEqual(api.bookings(api.merge(s,s)),api.bookings(s))
        self.assertEqual(api.peak(api.merge(s,s)),1)
    def test_merge_conflict(self):
        a=api.reserve(api.empty(),'a',0,2); b=api.reserve(api.empty(),'a',0,3)
        with self.assertRaises(ValueError): api.merge(a,b)
        self.assertEqual(api.bookings(a),(('a',0,2),)); self.assertEqual(api.bookings(b),(('a',0,3),))
    def test_peak_adjacency(self):
        s=api.reserve(api.reserve(api.empty(),'a',0,5),'b',5,10)
        self.assertEqual(api.peak(s),1); self.assertEqual(api.occupied(s,0,10),((0,10),))
    def test_peak_nested(self):
        s=api.reserve(api.reserve(api.reserve(api.empty(),'a',-4,8),'b',0,4),'c',0,4)
        self.assertEqual(api.peak(s),3)
    def test_clip(self):
        s=api.reserve(api.reserve(api.empty(),'a',-10,3),'b',5,20)
        self.assertEqual(api.occupied(s,0,8),((0,3),(5,8)))
    def test_gaps(self):
        s=api.reserve(api.reserve(api.empty(),'a',0,2),'b',3,5)
        self.assertEqual(api.occupied(s,-1,6),((0,2),(3,5)))
    def test_window_edges(self):
        s=api.reserve(api.empty(),'a',0,5)
        self.assertEqual(api.occupied(s,5,6),()); self.assertEqual(api.occupied(s,-1,0),())
        self.assertEqual(api.occupied(s,2,2),())
        with self.assertRaises(ValueError): api.occupied(s,4,3)
    def test_huge_signed(self):
        big=10**100
        s=api.reserve(api.reserve(api.empty(),'a',-big,-big+1),'b',big,big+1)
        self.assertEqual(api.occupied(s,-big,big+1),((-big,-big+1),(big,big+1)))
        self.assertEqual(api.peak(s),1)
    def test_merge_laws_on_compatible_inputs(self):
        a=api.reserve(api.empty(),'a',0,3); b=api.reserve(api.empty(),'b',2,4)
        c=api.reserve(api.empty(),'c',3,5); e=api.empty()
        observe=api.bookings
        self.assertEqual(observe(api.merge(api.merge(a,b),c)),observe(api.merge(a,api.merge(b,c))))
        self.assertEqual(observe(api.merge(a,b)),observe(api.merge(b,a)))
        self.assertEqual(observe(api.merge(a,e)),observe(a)); self.assertEqual(observe(api.merge(e,a)),observe(a))
    def test_seeded_small_histories_independent_point_oracle(self):
        rng=random.Random(57031); s=api.empty(); model={}; retained=[]
        for index in range(70):
            retained.append((s,api.bookings(s)))
            start=rng.randrange(-6,6); end=rng.randrange(start+1,8)
            key='job'+str(index); s=api.reserve(s,key,start,end); model[key]=(start,end)
            self.assertEqual(api.bookings(s),tuple((k,*v) for k,v in sorted(model.items())))
            self.assertEqual(api.peak(s),max(sum(a<=t<b for a,b in model.values()) for t in range(-6,8)))
            cells=[t for t in range(-3,5) if any(a<=t<b for a,b in model.values())]
            spans=[]
            for t in cells:
                if spans and spans[-1][1]==t:spans[-1]=(spans[-1][0],t+1)
                else:spans.append((t,t+1))
            self.assertEqual(api.occupied(s,-3,5),tuple(spans))
        for old,rows in retained:self.assertEqual(api.bookings(old),rows)
'''


def run_tests(directory, module):
    try:
        result = subprocess.run([sys.executable, '-B', '-m', 'unittest', '-v', module],
                                cwd=directory, text=True, capture_output=True, timeout=60)
        text = result.stdout + result.stderr
        counts = re.search(r'Ran (\d+) tests?', text)
        failures = re.search(r'failures=(\d+)', text)
        errors = re.search(r'errors=(\d+)', text)
        skipped = re.search(r'skipped=(\d+)', text)
        return {'exitCode': result.returncode, 'tests': int(counts[1]) if counts else 0,
                'failures': int(failures[1]) if failures else 0,
                'errors': int(errors[1]) if errors else 0,
                'skipped': int(skipped[1]) if skipped else 0, 'output': text}
    except subprocess.TimeoutExpired:
        return {'exitCode': None, 'tests': 0, 'failures': 0, 'errors': 0,
                'skipped': 0, 'output': 'Evaluator timeout after 60 seconds'}


def scheduler_evaluation(workspace, oracle=False):
    rows = {}
    for name, source in {'correct_dictionary': REFERENCE, 'correct_opaque_reverse_ties': ALTERNATIVE,
                         **mutants()}.items():
        with tempfile.TemporaryDirectory(prefix='scheduler-grading-') as temp:
            directory = Path(temp)
            if not oracle:
                for p in workspace.glob('*.py'):
                    if p.name != 'scheduler_api.py': shutil.copy2(p, directory / p.name)
            (directory / 'scheduler_api.py').write_text(source)
            if oracle: (directory / 'test_scheduler.py').write_text(SCHEDULER_ORACLE)
            result = run_tests(directory, 'test_scheduler')
            result['behavioralKill'] = (result['exitCode'] == 1 and result['failures'] > 0 and result['errors'] == 0)
            rows[name] = result
    return rows


def calendar_evaluation(workspace):
    with tempfile.TemporaryDirectory(prefix='calendar-grading-') as temp:
        directory = Path(temp)
        for p in workspace.glob('*.py'): shutil.copy2(p, directory / p.name)
        (directory / '_contract_checks.py').write_text(CALENDAR_ORACLE)
        return run_tests(directory, '_contract_checks')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', choices=('10', '11', 'self-test'), required=True)
    parser.add_argument('--workspace', type=Path)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if args.case == 'self-test':
        result = scheduler_evaluation(Path('.'), oracle=True)
        assert all(result[name]['exitCode'] == 0 and result[name]['tests'] == 10
                   for name in ('correct_dictionary', 'correct_opaque_reverse_ties'))
        assert all(result[name]['behavioralKill'] for name in mutants())
    else:
        if args.workspace is None: parser.error('--workspace is required')
        result = calendar_evaluation(args.workspace) if args.case == '10' else scheduler_evaluation(args.workspace)
    text = json.dumps(result, indent=2) + '\n'
    if args.out: args.out.write_text(text)
    else: print(text)


if __name__ == '__main__':
    main()
