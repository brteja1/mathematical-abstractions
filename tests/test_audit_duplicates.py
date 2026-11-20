"""DA acceptance tests, with independent expected sets/arithmetic and fault injection.

Catalog mappings: FiniteSet has finite exact-ID/tuple/token equality; Relation is
not assumed transitive; TotalOrder instantiates integer/code-point rank keys.
These finite tests do not prove refinement or mathematical duplicate detection.
"""
from contextlib import redirect_stderr, redirect_stdout
import copy
import io
import itertools
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import audit_duplicates as audit

FS = 'urn:csabs:axiom/FiniteSet-carrier-extensionality'
ORDER = 'urn:csabs:axiom/TotalOrder-comparable'


def concept(name):
    ident = 'c:' + name
    provenance = {'source': ['s:test'], 'sourceLocator': 'synthetic fixture',
                  'sourceNote': 'Fixture only, not a catalog addition.', 'provenanceKind': 'adapted'}
    claim = lambda kind, prefix: dict(id=prefix + name, type=kind, name=prefix + name,
        statement='Statement ' + name, formalStatement='Formula ' + name, assumptions=['Carrier ' + name],
        appliesTo=[ident], reviewStatus='fixture', ruleRole='defining-rule', **provenance)
    return [dict(id=ident, type='Concept', shortForm=name, fullName=name, category=['cat:test'],
        kind='kind:test', definition='Definition ' + name, notation=name, axiomBasis='Basis ' + name,
        basisKind='defined-structure', basisScope='Scope ' + name, coverageStatus='fixture',
        hasOperation=['o:' + name], hasAxiom=['a:' + name], hasLaw=['l:' + name], hasTheorem=[], **provenance),
        dict(id='o:' + name, type='Operation', name='Operation ' + name, signature=name + '→' + name,
             description='Operation fixture', concept=ident, precondition='Defined ' + name,
             totality='total', outcome='Value ' + name),
        claim('Axiom', 'a:'), claim('Law', 'l:')]


def fixture(root, names=('A', 'B', 'C')):
    (root / 'concepts').mkdir(parents=True)
    (root / 'data').mkdir()
    shared = {'@context': {'id': '@id', 'type': '@type'}, '@graph': [
        {'id': 's:test', 'type': 'Source', 'label': 'Synthetic test fixture', 'path': 'fixture',
         'accessedOn': '2026-11-20', 'sourceRole': 'fixture'},
        {'id': 'cat:test', 'type': 'Category', 'label': 'Fixture'},
        {'id': 'kind:test', 'type': 'ConceptKind', 'label': 'Fixture'}]}
    (root / 'data/shared.json').write_text(json.dumps(shared))
    for name in names:
        write_page(root, name, concept(name))


def write_page(root, name, nodes):
    (root / 'concepts' / (name + '.md')).write_text(
        '<!-- graph-record:start -->\n```json\n' + json.dumps(nodes) + '\n```\n<!-- graph-record:end -->\n')


def receipt(engine, pair=('c:A', 'c:B'), decision='distinct'):
    return {'pair': list(pair), 'fingerprints': [engine.fingerprint(i) for i in pair],
            'profile': audit.PROFILE, 'decision': decision, 'rationale': 'Synthetic review',
            'reviewer': 'fixture', 'reviewedAt': '2026-11-20T00:00:00Z',
            'mapping': {k: 'Explicit fixture mapping' for k in ('carriers', 'equality', 'operations', 'assumptions')}}


class DuplicateAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        fixture(self.root)

    def engine(self, registry=None, aliases=None):
        def extra(role, data):
            if data is None:
                return None
            path = self.root / (role + '.json')
            path.write_text(json.dumps(data))
            return path
        return audit.Audit(audit.Snapshot(self.root, extra('aliases', aliases), extra('registry', registry)))

    def test_pair_universe_has_exact_members_and_cross_role_claims(self):
        """AC-02/O-02, FiniteSet-carrier-extensionality: compare exact expected membership."""
        report = self.engine().build_report(threshold=0, limit=100)
        expected = {p for ids in (['c:A', 'c:B', 'c:C'], ['a:A', 'a:B', 'a:C', 'l:A', 'l:B', 'l:C'])
                    for p in itertools.combinations(ids, 2)}
        self.assertEqual({tuple(c['pair']) for c in report['candidates']}, expected)
        self.assertEqual(report['scope']['totalPairCount'], 18)
        self.assertEqual(len(report['candidates']), 18)

    def test_empty_and_singleton_families(self):
        """AC-01/O-11, FiniteSet-constructors: empty carrier has no pair."""
        for path in (self.root / 'concepts').glob('*.md'):
            path.unlink()
        report = self.engine().build_report()
        self.assertEqual(report['counts']['qualifiedCount'], 0)
        self.assertEqual(report['scope']['totalPairCount'], 0)
        nodes = concept('A')
        nodes[0].update(hasOperation=[], noPrimitiveOperationsReason='fixture', hasAxiom=['a:A'], hasLaw=[], hasTheorem=['l:A'])
        nodes[3]['type'] = 'Theorem'
        write_page(self.root, 'A', [nodes[0], nodes[2], nodes[3]])
        report = self.engine().build_report(threshold=0, limit=10)
        self.assertEqual(report['scope']['totalPairCount'], 1)  # zero Concept pairs, one cross-role claim pair

    def test_incremental_matches_full_restriction_with_old_counterpart(self):
        """AC-03/O-03, Relation: pairs incident to affected subjects, not both changed."""
        engine = self.engine()
        full = engine.build_report(threshold=0, limit=100)
        partial = engine.build_report(changed=['c:A', 'c:A'], threshold=0, limit=100)
        expected = {tuple(c['pair']) for c in full['candidates'] if 'c:A' in c['pair'] or 'a:A' in c['pair'] or 'l:A' in c['pair']}
        self.assertEqual({tuple(c['pair']) for c in partial['candidates']}, expected)
        self.assertIn(('c:A', 'c:C'), expected)
        self.assertEqual(partial['scope']['inspectedPairCount'], len(expected))
        self.assertEqual(partial['scope']['requestedChangedIds'], ['c:A'])

    def test_closure_cycles_sources_and_local_invalidation(self):
        """AC-04/O-03, FiniteSet membership: visited set terminates; source edit affects dependents."""
        before = self.engine()
        fp = before.fingerprint('c:A')
        nodes = concept('B'); nodes[0]['definition'] += ' changed'
        write_page(self.root, 'B', nodes)
        self.assertEqual(self.engine().fingerprint('c:A'), fp)
        shared = json.loads((self.root / 'data/shared.json').read_text())
        shared['@graph'][0]['label'] += ' changed'
        (self.root / 'data/shared.json').write_text(json.dumps(shared))
        self.assertNotEqual(self.engine().fingerprint('c:A'), fp)
        for name, other in [('A', 'B'), ('B', 'A')]:
            nodes = concept(name); nodes[0]['requiresConcept'] = ['c:' + other]
            write_page(self.root, name, nodes)
        self.assertIn('c:B', self.engine().evidence_closure('c:A'))
        partial = self.engine().build_report(changed=['s:test'], threshold=0, limit=100)
        self.assertEqual(partial['scope']['uninspectedPairCount'], 0)

    def test_fingerprint_has_independent_canonical_payload(self):
        """AC-04/O-07, FiniteSet: exact context set; hash matches independently serialized closure."""
        import hashlib
        engine = self.engine()
        expected_ids = ['c:A', 'o:A', 'a:A', 'l:A', 's:test', 'cat:test', 'kind:test']
        payload = {'profile': 'DA-P1', 'context': engine.snapshot.doc['@context'],
                   'records': {i: engine.index[i] for i in expected_ids}, 'aliases': []}
        expected = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False,
                                           separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(engine.fingerprint('c:A'), expected)

    def test_normalization_preserves_operators_and_ignores_nontext(self):
        """AC-05/O-04, FiniteSet: expected token membership, with + and × distinct."""
        self.assertEqual(audit.normalize('  ＦＯＯ\tbar  '), 'foo bar')
        self.assertEqual(audit.tokens(['MyType + x×y', 42, None]), {'my', 'type', '+', 'x', '×', 'y'})
        self.assertEqual(audit.tokens([None, 3, False]), frozenset())

    def test_score_exact_fraction_and_empty_channels(self):
        """AC-06/O-05: hand oracle 10000/3 floors once to 3333; empty evidence scores 0."""
        engine = self.engine()
        # Supply abstract feature carriers directly to isolate arithmetic from extraction.
        engine.features['c:A'] = {k: frozenset({'one', 'left'}) for k in audit.CHANNELS}
        engine.features['c:B'] = {k: frozenset({'one', 'right'}) for k in audit.CHANNELS}
        self.assertEqual(engine.score_pair(('c:A', 'c:B'))[0], 3333)
        self.assertEqual(engine.score_pair(('c:B', 'c:A'))[0], 3333)
        engine.features['c:A'] = {k: frozenset() for k in audit.CHANNELS}
        engine.features['c:B'] = {k: frozenset() for k in audit.CHANNELS}
        self.assertEqual(engine.score_pair(('c:A', 'c:B'))[0], 0)
        self.assertEqual(engine.score_pair(('c:A', 'c:B'))[1]['name']['unionCount'], 0)

    def test_alias_and_cross_role_exact_statement_force_candidates(self):
        """AC-07/O-05: normalized aliases/statements trigger at max threshold without merging IDs."""
        aliases = {'schemaVersion': 1, 'aliases': {'c:B': ['  A  ', 'a']}}
        nodes = concept('B'); nodes[2]['formalStatement'] = 'Formula A'
        write_page(self.root, 'B', nodes)
        engine = self.engine(aliases=aliases)
        report = engine.build_report(threshold=10000, limit=100)
        pairs = {tuple(r['pair']): r for r in report['candidates']}
        self.assertIn('exact_name', pairs['c:A', 'c:B']['triggers'])
        self.assertIn('exact_statement', pairs['a:B', 'l:A']['triggers'])
        self.assertEqual(engine.aliases['c:B'], ['a'])

    def test_source_only_is_not_similarity_and_semantic_fields_remain_visible(self):
        """AC-08,17/O-09: sharing a citation cannot invent similarity; scope/proof roles survive."""
        engine = self.engine()
        for ident in engine.subjects:
            engine.names[ident] = set()
            engine.features[ident] = {k: frozenset() for k in audit.CHANNELS}
            if engine.index[ident]['type'] != 'Concept':
                engine.index[ident]['formalStatement'] = ident
        self.assertEqual(engine.build_report()['counts']['qualifiedCount'], 0)
        row = next(r for r in engine.build_report(threshold=0, limit=100)['candidates'] if r['pair'] == ['c:A', 'c:B'])
        self.assertEqual(row['endpoints'][0]['fields']['basisScope'], 'Scope A')
        self.assertIn('signature', row['endpoints'][0]['fields']['directOperations'][0])
        self.assertIn('assumptions', row['endpoints'][0]['fields']['directAxioms'][0])

    def test_all_receipt_states_and_below_threshold_forcing(self):
        """AC-09/O-07: every DA-14 row observed; old distinction cannot hide changed context."""
        initial = self.engine()
        for decision, state in [('same_meaning', 'confirmed_duplicate'), ('undecided', 'undecided'),
                                ('distinct', 'reviewed_distinct'), ('semantic_variant', 'reviewed_distinct')]:
            entry = receipt(initial, decision=decision)
            engine = self.engine(registry={'schemaVersion': 1, 'entries': [entry]})
            self.assertEqual(engine.classify_review(('c:A', 'c:B')), state)
            if decision == 'same_meaning':
                report = engine.build_report(threshold=10000, limit=100)
                self.assertTrue(any(r['pair'] == ['c:A', 'c:B'] for r in report['candidates']))
        entry = receipt(initial); entry['fingerprints'][0] = '0' * 64
        report = self.engine(registry={'schemaVersion': 1, 'entries': [entry]}).build_report(threshold=10000, limit=100)
        row = next(r for r in report['candidates'] if r['pair'] == ['c:A', 'c:B'])
        self.assertEqual(row['reviewState'], 'stale')
        self.assertIsNone(row['currentReview'])
        self.assertEqual(row['previousReview'], entry)
        self.assertIn('stale_review', row['triggers'])

    def test_review_suppression_is_pair_local_and_counts_partition(self):
        """AC-10,12/O-07, Relation: no transitive inference; finite sets partition qualified pairs."""
        initial = self.engine()
        entries = [receipt(initial, p) for p in [('c:A', 'c:B'), ('c:B', 'c:C')]]
        engine = self.engine(registry={'schemaVersion': 1, 'entries': entries})
        report = engine.build_report(threshold=0, limit=100)
        pairs = {tuple(c['pair']) for c in report['candidates']}
        self.assertNotIn(('c:A', 'c:B'), pairs)
        self.assertIn(('c:A', 'c:C'), pairs)
        self.assertEqual(report['counts']['hiddenReviewedCount'], 2)
        self.assertEqual(report['counts']['queueSize'] + 2, report['counts']['qualifiedCount'])
        self.assertEqual(sum(report['counts']['stateCounts'].values()), report['counts']['qualifiedCount'])
        included = engine.build_report(threshold=0, limit=100, include_reviewed=True)
        self.assertEqual(included['counts']['returnedCount'], 18)
        self.assertEqual(included['counts']['hiddenReviewedCount'], 0)

    def test_forced_receipts_respect_incremental_scope_and_orphans(self):
        """AC-10,13/O-07: confirmed unrelated pairs remain summary-only; removed endpoints are orphaned."""
        initial = self.engine()
        entry = receipt(initial, decision='same_meaning')
        orphan = copy.deepcopy(entry); orphan['pair'] = ['c:Missing', 'c:Removed']
        report = self.engine(registry={'schemaVersion': 1, 'entries': [entry, orphan]}).build_report(changed=['c:C'], threshold=10000)
        self.assertFalse(any(r['pair'] == ['c:A', 'c:B'] for r in report['candidates']))
        self.assertEqual(report['registrySummary'][0]['qualifies'], False)
        self.assertEqual(report['registrySummary'][1]['status'], 'orphaned')

    def test_order_ties_limit_zero_and_prefix(self):
        """AC-11/O-08, TotalOrder-comparable: exact lexicographic oracle for tied rank keys."""
        engine = self.engine()
        with patch.object(engine, 'score_pair', return_value=(7, {})):
            whole = engine.build_report(threshold=0, limit=100)
            zero = engine.build_report(threshold=0, limit=0)
            small = engine.build_report(threshold=0, limit=3)
        pairs = [r['pair'] for r in whole['candidates']]
        self.assertEqual(pairs, sorted(pairs))
        self.assertEqual(small['candidates'], whole['candidates'][:3])
        self.assertEqual(zero['counts']['queueSize'], 18)
        self.assertTrue(zero['truncated'])
        self.assertEqual(zero['candidates'], [])

    def test_invalid_inputs_fail_closed(self):
        """AC-13/O-01,06: schema-defined invalid inputs are rejected, not silently filtered."""
        engine = self.engine()
        for kwargs in ({'changed': ['missing']}, {'limit': -1}, {'threshold': 10001}, {'changed': []}):
            with self.assertRaises(audit.AuditError):
                engine.build_report(**kwargs)
        for aliases in ({'schemaVersion': True, 'aliases': {}}, {'schemaVersion': 1, 'aliases': {'a:A': ['x']}},
                        {'schemaVersion': 1, 'aliases': {'c:A': [' ']}}):
            with self.assertRaises(audit.AuditError):
                self.engine(aliases=aliases)
        with self.assertRaisesRegex(audit.AuditError, 'Duplicate JSON'):
            audit.strict_json('{"x": 1, "x": 2}')
        with self.assertRaises(audit.AuditError):
            audit.strict_json('{"x": NaN}')
        nodes = concept('A'); nodes[0]['requiresConcept'] = ['missing']
        write_page(self.root, 'A', nodes)
        with self.assertRaises(audit.AuditError):
            self.engine()

    def test_receipt_validation_and_specialization_direction(self):
        """AC-13/O-06: direction/type/timestamp/hash and duplicate-pair constraints are enforced."""
        initial = self.engine()
        good = receipt(initial, decision='specialization')
        good.update(specializedId='c:A', generalId='c:B')
        self.assertEqual(self.engine(registry={'schemaVersion': 1, 'entries': [good]}).classify_review(('c:A', 'c:B')), 'reviewed_distinct')
        for update in ({'pair': ['c:B', 'c:A']}, {'fingerprints': ['bad', 'bad']}, {'decision': 'merge'},
                       {'reviewedAt': '2026-11-20T00:00:00+00:99'}, {'generalId': 'c:A'}, {'mapping': {}}):
            bad = {**good, **update}
            with self.assertRaises(audit.AuditError):
                self.engine(registry={'schemaVersion': 1, 'entries': [bad]})
        with self.assertRaises(audit.AuditError):
            self.engine(registry={'schemaVersion': 1, 'entries': [good, good]})
        cross = receipt(initial, ('a:A', 'c:A'))
        with self.assertRaises(audit.AuditError):
            self.engine(registry={'schemaVersion': 1, 'entries': [cross]})

    def test_relocation_reproducibility_and_markdown_same_queue(self):
        """AC-14/O-09: relocating byte-identical inputs preserves JSON bytes; Markdown retains rows."""
        first = self.engine().build_report(limit=3)
        other = self.root / 'relocated'
        shutil.copytree(self.root / 'concepts', other / 'concepts')
        shutil.copytree(self.root / 'data', other / 'data')
        second = audit.Audit(audit.Snapshot(other)).build_report(limit=3)
        self.assertEqual(audit.render_json(first), audit.render_json(second))
        self.assertEqual(audit.render_json(first), audit.render_json(self.engine().build_report(limit=3)))
        markdown = audit.render_markdown(first)
        self.assertIn('Scope, assumptions, role and provenance', markdown)
        for row in first['candidates']:
            self.assertIn(str(row['score']), markdown)
            for ident in row['pair']:
                self.assertIn(ident, markdown)

    def test_snapshot_uses_captured_bytes_and_detects_membership_and_content_changes(self):
        """AC-16/O-01: captured records remain unchanged while final verification rejects edits."""
        snapshot = audit.Snapshot(self.root)
        nodes = concept('A'); nodes[0]['definition'] = 'Concurrent edit'
        write_page(self.root, 'A', nodes)
        self.assertEqual(snapshot.index['c:A']['definition'], 'Definition A')
        with self.assertRaisesRegex(audit.AuditError, 'changed'):
            snapshot.verify()
        snapshot = audit.Snapshot(self.root)
        write_page(self.root, 'D', concept('D'))
        with self.assertRaisesRegex(audit.AuditError, 'membership'):
            snapshot.verify()

    def test_alias_file_changes_invalidate_snapshot_and_endpoint_review(self):
        """AC-04,16/O-01,07: normalized alias evidence is fingerprinted and captured inputs rechecked."""
        old = self.engine()
        entry = receipt(old)
        aliases = {'schemaVersion': 1, 'aliases': {'c:A': ['NewName']}}
        new = self.engine(aliases=aliases, registry={'schemaVersion': 1, 'entries': [entry]})
        self.assertEqual(new.classify_review(('c:A', 'c:B')), 'stale')
        (self.root / 'aliases.json').write_text('{"schemaVersion": 1, "aliases": {}}')
        with self.assertRaisesRegex(audit.AuditError, 'changed'):
            new.snapshot.verify()

    def test_duplicate_graph_ids_and_keys_rejected_before_indexing(self):
        """AC-13/O-01: finite-map identity cannot overwrite conflicting records."""
        nodes = concept('A'); nodes.append(copy.deepcopy(nodes[2]))
        write_page(self.root, 'A', nodes)
        with self.assertRaisesRegex(audit.AuditError, 'Duplicate ID'):
            self.engine()
        write_page(self.root, 'A', concept('A'))
        path = self.root / 'data/shared.json'
        path.write_text(path.read_text().replace('"@context":', '"@context": {}, "@context":', 1))
        with self.assertRaisesRegex(audit.AuditError, 'Duplicate JSON key'):
            self.engine()

    def test_legacy_gap_and_unknown_fields_are_preserved_in_real_evidence(self):
        """AC-08,13/O-09: TotalOrder-comparable's legacy gap stays visible, with no invented source."""
        endpoint = audit.Audit(audit.Snapshot()).endpoint(ORDER)
        self.assertEqual(endpoint['fields']['provenanceStatus'], 'legacy-source-missing')
        self.assertNotIn('source', endpoint['fields'])
        self.assertEqual(endpoint['fields']['directSources'], [])

    def test_record_locators_use_real_generated_anchors_and_page_roots(self):
        """AC-08,14/O-09: actual Markdown locators exist, without invented Concept fragments."""
        engine = audit.Audit(audit.Snapshot())
        concept_endpoint = engine.endpoint('urn:csabs:concept/TotalOrder')
        self.assertIsNone(concept_endpoint['anchor'])
        claim_endpoint = engine.endpoint(ORDER)
        locations = [concept_endpoint, claim_endpoint, *claim_endpoint['evidenceRecords']]
        for loc in locations:
            path = audit.ROOT / loc['path']
            self.assertTrue(path.is_file())
            if loc['anchor'] is not None:
                self.assertIn('id="' + loc['anchor'] + '"', path.read_text())
        row = {'score': 1, 'pair': ['x', 'y'], 'reviewState': 'unreviewed', 'triggers': [],
               'differences': [], 'endpoints': [concept_endpoint]}
        report = {'scope': {}, 'counts': {}, 'truncated': False, 'inputs': {}, 'candidates': [row],
                  'registrySummary': [], 'limitations': []}
        self.assertIn('](concepts/TotalOrder.md)', audit.render_markdown(report))

    def test_output_rejects_existing_inputs_symlinks_and_protected_paths(self):
        """AC-15/O-10,12: forbidden outputs cannot modify input bytes."""
        snapshot = audit.Snapshot(self.root)
        paths = ['concepts/new.md', 'data/new.json', 'lean/new.txt', 'ontology/new.ttl',
                 'visualization/new.html', 'deps/new', '.git/new', 'docs/.hidden/file']
        for relative in paths:
            with self.assertRaises(audit.AuditError):
                audit.output_path(self.root / relative, snapshot)
        with self.assertRaises(audit.AuditError):
            audit.output_path(self.root / 'data/shared.json', snapshot)
        target = self.root / 'existing.txt'; target.write_text('preserve')
        with self.assertRaises(audit.AuditError):
            audit.output_path(target, snapshot)
        link = self.root / 'link'; link.symlink_to(self.root / 'absent')
        with self.assertRaises(audit.AuditError):
            audit.output_path(link, snapshot)
        parent = self.root / 'linked-directory'; parent.symlink_to(self.root / 'data', target_is_directory=True)
        with self.assertRaises(audit.AuditError):
            audit.output_path(parent / 'new.json', snapshot)
        self.assertEqual(target.read_text(), 'preserve')
        with self.assertRaises(FileExistsError):
            audit.emit('replace', target)

    def test_partial_output_cleanup_and_cleanup_failure_diagnostic(self):
        """AC-16/O-10: failed writes remove only the newly created file and report cleanup failures."""
        target = self.root / 'new.txt'
        def fail(handle, text):
            handle.write('partial')
            raise OSError('write fault')
        with patch.object(audit, 'write_report', side_effect=fail):
            with self.assertRaisesRegex(OSError, 'write fault'):
                audit.emit('report', target)
        self.assertFalse(target.exists())
        err = io.StringIO()
        with patch.object(audit, 'write_report', side_effect=fail), patch.object(Path, 'unlink', side_effect=OSError('cleanup fault')):
            with redirect_stderr(err), self.assertRaises(OSError):
                audit.emit('report', target)
        self.assertIn('cleanup failed', err.getvalue())
        self.assertEqual(target.read_text(), 'partial')

    def test_close_failure_cleanup_preserves_replacement_files(self):
        """AC-16/O-10: close failure cleans up; concurrent replacement is never unlinked."""
        target = self.root / 'close-fault.txt'
        real = target.open('x', encoding='utf-8')
        class CloseFailure:
            def fileno(self):
                return real.fileno()
            def __enter__(self):
                return real
            def __exit__(self, *args):
                real.close()
                raise OSError('close fault')
        with patch.object(Path, 'open', return_value=CloseFailure()), self.assertRaisesRegex(OSError, 'close fault'):
            audit.emit('report', target)
        self.assertFalse(target.exists())
        def replace(handle, text):
            target.unlink()
            target.write_text('someone else')
            raise OSError('write fault')
        err = io.StringIO()
        with patch.object(audit, 'write_report', side_effect=replace), redirect_stderr(err), self.assertRaises(OSError):
            audit.emit('report', target)
        self.assertEqual(target.read_text(), 'someone else')
        self.assertIn('replacement preserved', err.getvalue().lower())

    def test_main_exit_codes_output_and_final_check(self):
        """AC-13,15,16/O-10: successful output follows final verification; failures emit no success JSON."""
        def run(argv, side_effect=None):
            out, err = io.StringIO(), io.StringIO()
            # Capture the actual class before patching its global name.
            snapshot = audit.Snapshot(self.root)
            with patch.object(audit, 'Snapshot', return_value=snapshot), redirect_stdout(out), redirect_stderr(err):
                if side_effect:
                    with patch.object(snapshot, 'verify', side_effect=side_effect):
                        code = audit.main(argv)
                else:
                    code = audit.main(argv)
            return code, out.getvalue(), err.getvalue()
        code, out, _ = run(['--limit', '0'])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)['counts']['returnedCount'], 0)
        code, out, _ = run([], audit.AuditError('snapshot changed'))
        self.assertEqual((code, out), (2, ''))
        code, out, _ = run([], OSError('read failure'))
        self.assertEqual((code, out), (3, ''))
        target = self.root / 'report.json'
        code, out, _ = run(['--limit', '0', '--output', str(target)])
        self.assertEqual((code, out), (0, ''))
        self.assertEqual(json.loads(target.read_text())['schemaVersion'], 1)

    def test_real_entrypoint_readonly_without_bytecode_caches(self):
        """AC-15,17/O-12: subprocess hashes prove unchanged fixture tree except requested report."""
        # Relocated standard-library checkout exercises the actual main() ROOT path.
        (self.root / 'scripts').mkdir()
        for relative in audit.LOCAL_MODULES + audit.POLICY_FILES:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(audit.ROOT / relative, destination)
        before = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        result = subprocess.run([sys.executable, str(self.root / 'scripts/audit_duplicates.py'), '--limit', '1'],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['counts']['returnedCount'], 1)
        after = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        self.assertFalse(list(self.root.rglob('__pycache__')))


if __name__ == '__main__':
    unittest.main()
