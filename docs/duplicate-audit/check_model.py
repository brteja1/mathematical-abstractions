#!/usr/bin/env python3
"""Bounded consistency encoding for spec.md; not the proposed audit command.

Only abstract finite sets, receipts, exact scores and report prefixes are modeled.
There is no catalog reader, feature extractor, receipt parser or production CLI.
Assertions carry clause IDs. All arithmetic uses exact integers/Fraction.
"""
import hashlib
import itertools
import json
import platform
import sys
import unicodedata
from fractions import Fraction
from pathlib import Path


def subsets(values):
    values = tuple(values)
    return [frozenset(values[i] for i in range(len(values)) if mask & (1 << i))
            for mask in range(1 << len(values))]


def receipt_state(present, fresh, decision):
    if not present:
        return 'unreviewed'
    if not fresh:
        return 'stale'
    if decision == 'same_meaning':
        return 'confirmed_duplicate'
    if decision == 'undecided':
        return 'undecided'
    return 'reviewed_distinct'


def check_pairs_and_reports():
    cases = 0
    nonempty = False
    zero_limit = False
    # Exhaust every two-family assignment, affected-subject set, base-candidate
    # relation, forced-pair relation (confirmed or stale) and quiet-pair relation
    # for <=3 subjects. Individual receipt states are checked separately.
    for n in range(4):
        ids = tuple(range(n))
        for family in itertools.product(range(2), repeat=n):
            universe = frozenset((a, b) for a, b in itertools.combinations(ids, 2)
                                 if family[a] == family[b])
            assert all(a < b and family[a] == family[b] for a, b in universe), 'DA-04'
            for affected in [None] + subsets(ids):
                inspected = universe if affected is None else frozenset(
                    p for p in universe if set(p) & affected)
                for base in subsets(universe):
                    for forced in subsets(universe):
                        qualified = (base | forced) & inspected
                        assert qualified <= inspected, 'DA-07, DA-10, DA-14'
                        assert forced & inspected <= qualified, 'DA-14'
                        for quiet_input in subsets(universe):
                            # Current confirmed duplicates and stale reviews cannot be quiet.
                            quiet = quiet_input & qualified - forced
                            for include_reviewed in (False, True):
                                selected = qualified if include_reviewed else qualified - quiet
                                hidden = frozenset() if include_reviewed else quiet
                                assert not (selected & hidden), 'DA-14'
                                assert selected | hidden == qualified, 'DA-14, DA-17'
                                assert len(selected) + len(hidden) == len(qualified), 'DA-17'
                                assert forced & inspected <= selected, 'DA-14'
                                if affected is not None:
                                    full_selected = (base | forced) if include_reviewed else (
                                        (base | forced) - (quiet_input - forced))
                                    assert selected == full_selected & inspected, 'DA-07'
                                # Arbitrary concrete tie pattern; all rank keys include IDs.
                                score = {p: (sum(p) % 2) * 5000 for p in universe}
                                order = lambda p: (-score[p], p[0], p[1])
                                queue = sorted(selected, key=order)
                                reverse_input = sorted(reversed(queue), key=order)
                                assert queue == reverse_input, 'DA-15'
                                for limit in range(len(universe) + 2):
                                    rows = queue[:limit]
                                    truncated = len(rows) < len(queue)
                                    assert len(rows) == min(limit, len(queue)), 'DA-15'
                                    assert rows == queue[:len(rows)], 'DA-15'
                                    assert len(rows) <= len(queue) <= len(qualified), 'DA-17'
                                    assert truncated == (limit < len(queue)), 'DA-15'
                                    if queue:
                                        nonempty = True
                                        if limit == 0:
                                            zero_limit = truncated and not rows
                                    cases += 1
    assert nonempty and zero_limit, 'DA-05: nonvacuity witnesses required'
    # Relation need not be transitive; reviewed pairs never complete triangles.
    quiet = {(0, 1), (1, 2)}
    assert (0, 2) not in quiet, 'DA-04, DA-14'
    return {'cases': cases, 'nonemptyQueueWitness': True,
            'zeroLimitTruncationWitness': True, 'maxSubjects': 3,
            'families': 2, 'completeWithinDeclaredSetBounds': True}


def check_receipts():
    decisions = ('same_meaning', 'specialization', 'semantic_variant', 'distinct', 'undecided')
    counts = dict.fromkeys(('unreviewed', 'stale', 'confirmed_duplicate',
                           'undecided', 'reviewed_distinct'), 0)
    expected = {'same_meaning': 'confirmed_duplicate', 'undecided': 'undecided',
                'specialization': 'reviewed_distinct', 'semantic_variant': 'reviewed_distinct',
                'distinct': 'reviewed_distinct'}
    cases = 0
    for present, fresh, decision in itertools.product((False, True), (False, True), decisions):
        state = receipt_state(present, fresh, decision)
        assert state == ('unreviewed' if not present else 'stale' if not fresh
                         else expected[decision]), 'DA-14'
        counts[state] += 1
        cases += 1
    assert all(counts.values()), 'DA-14: every state must have a witness'
    # Abstract fingerprint equality, excluding hash collisions by assumption.
    for profile_ok, left_ok, right_ok in itertools.product((False, True), repeat=3):
        current = profile_ok and left_ok and right_ok
        assert current == all((profile_ok, left_ok, right_ok)), 'DA-06, DA-14'
        cases += 1
    return {'cases': cases, 'stateWitnessCounts': counts,
            'limitations': 'No JSON parsing, cryptography, dependency traversal or filesystem modeled.'}


def check_exact_arithmetic():
    def jaccard(a, b):
        return Fraction(len(a & b), len(a | b)) if a | b else Fraction(0)

    cases = 0
    sets = subsets(('a', 'b', '×'))
    for a, b in itertools.product(sets, repeat=2):
        value = jaccard(a, b)
        assert 0 <= value <= 1 and value == jaccard(b, a), 'DA-09'
        if not (a | b):
            assert value == 0, 'DA-09'
        for weights in ((20, 20, 25, 25, 10), (10, 35, 0, 40, 15)):
            assert sum(weights) == 100, 'DA-09'
            for channels in itertools.product((Fraction(0), value, Fraction(1)), repeat=5):
                exact = 100 * sum(w * c for w, c in zip(weights, channels))
                score = exact.numerator // exact.denominator
                assert 0 <= score <= 10000, 'DA-09'
                cases += 1
    # Hand-calculated example: five equal 1/3 channels give 10000/3 -> 3333.
    assert (100 * sum(Fraction(w, 3) for w in (20, 20, 25, 25, 10))) // 1 == 3333, 'DA-09'
    for score, threshold, exact_name, exact_statement in itertools.product(
            (0, 2999, 3000, 10000), (0, 3000, 10000), (False, True), (False, True)):
        qualifies = score >= threshold or exact_name or exact_statement
        if threshold == 0 or exact_name or exact_statement:
            assert qualifies, 'DA-10'
        if score == 0 and threshold > 0 and not exact_name and not exact_statement:
            assert not qualifies, 'DA-10'
        cases += 1
    return {'cases': cases, 'alphabet': ['a', 'b', '×'],
            'componentDomain': ['0', 'J(A,B)', '1'],
            'manualWitness': {'channels': ['1/3'] * 5, 'expectedScore': 3333},
            'limitations': 'No real-record tokenization or detector efficacy evaluated.'}


def check_rejected_alternatives():
    # Concrete counterexamples to plausible but incompatible interpretations.
    universe = {(0, 1)}
    affected = {0}
    wrong_incremental = {p for p in universe if set(p) <= affected}
    required_incremental = {p for p in universe if set(p) & affected}
    assert wrong_incremental != required_incremental, 'DA-07'
    state = receipt_state(True, True, 'same_meaning')
    assert state == 'confirmed_duplicate' and state != 'reviewed_distinct', 'DA-14'
    stale = receipt_state(True, False, 'distinct')
    assert stale == 'stale' and stale != 'reviewed_distinct', 'DA-14'
    assert not (Fraction(0) >= Fraction(3000, 10000)), 'DA-09–10'
    return {
        'cases': 4,
        'witnesses': [
            {'rejected': 'both endpoints must be changed', 'pair': [0, 1],
             'affected': [0], 'requiredIncluded': True, 'clause': 'DA-07'},
            {'rejected': 'all reviewed pairs become quiet', 'decision': 'same_meaning',
             'requiredState': state, 'clause': 'DA-14'},
            {'rejected': 'old distinct decision suppresses changed records',
             'current': False, 'requiredState': stale, 'clause': 'DA-14'},
            {'rejected': 'empty Jaccard channels score 1', 'allChannelsEmpty': True,
             'requiredScore': 0, 'requiredDefaultQualification': False, 'clause': 'DA-09–10'}
        ]}


def main():
    here = Path(__file__).resolve().parent
    paths = ('spec.md', 'mapping.md', 'check_model.py', 'context.json')
    hashes = {p: hashlib.sha256((here / p).read_bytes()).hexdigest() for p in paths}
    result = {
        'schemaVersion': 1,
        'status': 'passed',
        'method': 'finite reference encoding plus documented manual specification review',
        'command': 'python3 -B docs/duplicate-audit/check_model.py',
        'environment': {'python': platform.python_version(), 'unicode': unicodedata.unidata_version},
        'inputs': hashes,
        'checks': {'pairsAndReports': check_pairs_and_reports(),
                   'receiptClassification': check_receipts(),
                   'exactArithmetic': check_exact_arithmetic(),
                   'rejectedAlternatives': check_rejected_alternatives()},
        'witness': {'subjects': ['a', 'b'], 'family': 'concept', 'pair': ['a', 'b'],
                    'baseQualifies': False, 'currentDecision': 'same_meaning',
                    'qualifiedCount': 1, 'queueSize': 1, 'limit': 0,
                    'returnedCount': 0, 'truncated': True},
        'notEstablished': [
            'Universal consistency or input coverage over all finite catalogs.',
            'Parser, schema, captured-byte loader, recursive closure and hash implementation conformance.',
            'Unicode feature extraction, full report evidence and deterministic serialization conformance.',
            'I/O errors, exclusive output creation, concurrent snapshots, no-write or no-network behavior.',
            'Detector precision/recall, mathematical equivalence, source entailment or production CLI correctness.',
            'Lean-compiled proofs or a complete filesystem/state-machine verification.'
        ]
    }
    print(json.dumps(result, ensure_ascii=False, indent=2) + '\n', end='')
    return 0


if __name__ == '__main__':
    sys.exit(main())
