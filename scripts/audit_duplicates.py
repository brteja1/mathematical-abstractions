#!/usr/bin/env python3
"""Offline duplicate-candidate review queue. Contract: docs/duplicate-audit/spec.md.

No generated RDF, network, locks, caches, catalog edits or automatic merging.
"""
import sys
sys.dont_write_bytecode = True  # Before importing any repository module (DA-18).
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)  # DA-05 exact unbounded integer inputs.

import argparse
from collections import Counter
from datetime import datetime
from fractions import Fraction
import hashlib
import heapq
import itertools
import json
import os
from pathlib import Path
import platform
import re
import unicodedata
from urllib.parse import quote

from markdown_graph import ROOT, anchor, load_graph, read_records
from validate_graph import LINK_TYPES, validate

PROFILE = 'DA-P1'
VERSION = '0.1.0'
CHANNELS = ('name', 'description', 'interface', 'basis', 'context')
WEIGHTS = {'concept': (20, 20, 25, 25, 10), 'claim': (10, 35, 0, 40, 15)}
CLOSURE_LINKS = ('hasOperation', 'hasAxiom', 'hasLaw', 'hasTheorem', 'dependsOn',
                 'requiresConcept', 'appliesTo', 'source', 'category', 'kind', 'parentCategory')
SUBJECT_TYPES = {'Concept': 'concept', 'Axiom': 'claim', 'Law': 'claim', 'Theorem': 'claim'}
DECISIONS = {'same_meaning', 'specialization', 'semantic_variant', 'distinct', 'undecided'}
STATES = ('unreviewed', 'stale', 'confirmed_duplicate', 'undecided', 'reviewed_distinct')
LOCAL_MODULES = ('scripts/audit_duplicates.py', 'scripts/markdown_graph.py',
                 'scripts/subjects.py', 'scripts/validate_graph.py')
POLICY_FILES = ('provenance_legacy.json', 'data/import_manifest.json')
LIMITATIONS = [
    'Heuristic candidates are not mathematical equivalence, inconsistency or merge authorization.',
    'No candidate does not imply absence of duplication; semantic recall is incomplete.',
    'Review invalidation follows only the explicit DA-06 evidence-closure boundary.',
    'Existing legacy source gaps are retained, not repaired; citations are not re-consulted.',
    'No solver, compiled proof or automatic catalog/registry/Lean changes are performed.',
]


class AuditError(ValueError):
    """Invalid input, usage or observed snapshot change: exit 2."""


def canon(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(value):
    return hashlib.sha256(value).hexdigest()


def strict_json(text):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise AuditError('Duplicate JSON key: ' + key)
            result[key] = value
        return result

    def bad_constant(value):
        raise AuditError('Non-finite JSON constant: ' + value)
    return json.loads(text, object_pairs_hook=object_pairs, parse_constant=bad_constant)


def normalize(text):
    return ' '.join(unicodedata.normalize('NFKC', text).casefold().split())


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)


def tokens(values):
    result = set()
    for text in strings(values):
        split = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', text)
        result.update(re.findall(r'\w+|[^\w\s]', normalize(split), re.UNICODE))
    return frozenset(result)


def refs(record, keys):
    for key in keys:
        value = record.get(key, [])
        yield from value if isinstance(value, list) else [value]


def schema(condition, message):
    if not condition:
        raise AuditError(message)


class Snapshot:
    """DA-03/18 captured graph and policy bytes; verify again before emission."""

    def __init__(self, root=ROOT, aliases=None, registry=None):
        self.root = Path(root).resolve()
        self.paths = self.graph_paths()
        self.raw = {p: p.read_bytes() for p in self.paths}
        self.explicit = {}
        for role, path in (('aliases', aliases), ('registry', registry)):
            if path is not None:
                path = Path(path).resolve()
                self.explicit[role] = (path, path.read_bytes())
        self.policy = {ROOT / p: (ROOT / p).read_bytes() for p in POLICY_FILES}
        self.tool = {ROOT / p: (ROOT / p).read_bytes() for p in LOCAL_MODULES}
        try:
            decoded = {p: raw.decode('utf-8') for p, raw in self.raw.items()}
            # Reject duplicate keys/non-finite values before the shared loader parses.
            from markdown_graph import BLOCK
            for path, text in decoded.items():
                if path.suffix == '.json':
                    strict_json(text)
                else:
                    for block in BLOCK.findall(text):
                        strict_json(block)
            self.doc = load_graph(self.root, captured=decoded)
            errors = validate(self.doc, read_text=lambda p: self.policy[p].decode('utf-8'))
            if errors:
                raise AuditError('Invalid catalog:\n' + '\n'.join(errors))
            self.index = {n['id']: n for n in self.doc['@graph']}
            self.owners = {n['id']: 'data/shared.json' for n in self.doc['@graph']}
            for path, text in decoded.items():
                if path.suffix == '.md':
                    for node in read_records(path, text=text):
                        self.owners[node['id']] = path.relative_to(self.root).as_posix()
            self.extra = {role: strict_json(raw.decode('utf-8'))
                          for role, (_, raw) in self.explicit.items()}
        except (ValueError, TypeError, KeyError, AttributeError, UnicodeError) as exc:
            raise AuditError(str(exc)) from exc

    def graph_paths(self):
        return tuple(sorted([self.root / 'data/shared.json',
                             *(self.root / 'concepts').glob('*.md')]))

    def verify(self):
        if self.paths != self.graph_paths():
            raise AuditError('Catalog file membership changed during audit')
        captured = list(self.raw.items()) + list(self.policy.items()) + list(self.tool.items())
        captured += list(self.explicit.values())
        for path, raw in captured:
            try:
                current = path.read_bytes()
            except FileNotFoundError as exc:
                raise AuditError('Input disappeared during audit: ' + path.name) from exc
            if digest(current) != digest(raw):
                raise AuditError('Input changed during audit: ' + path.name)

    def metadata(self):
        return {
            'catalogDigest': digest(canon({'context': self.doc['@context'], 'records': self.index})),
            'manifest': [{'path': p.relative_to(self.root).as_posix(), 'sha256': digest(raw)}
                         for p, raw in sorted(self.raw.items())],
            'aliasesHash': digest(self.explicit['aliases'][1]) if 'aliases' in self.explicit else None,
            'registryHash': digest(self.explicit['registry'][1]) if 'registry' in self.explicit else None,
            'commandVersion': VERSION,
            'toolSources': {p.relative_to(ROOT).as_posix(): digest(raw) for p, raw in self.tool.items()},
            'validationInputs': {p.relative_to(ROOT).as_posix(): digest(raw) for p, raw in self.policy.items()},
            'pythonVersion': platform.python_version(), 'unicodeVersion': unicodedata.unidata_version,
        }


def read_aliases(data, index):
    if data is None:
        return {}
    schema(isinstance(data, dict) and type(data.get('schemaVersion')) is int
           and data['schemaVersion'] == 1 and isinstance(data.get('aliases'), dict), 'Invalid alias schema')
    result = {}
    for ident, values in data['aliases'].items():
        schema(ident in index and index[ident]['type'] == 'Concept', 'Alias ID must be a current Concept: ' + ident)
        schema(isinstance(values, list) and all(isinstance(v, str) and normalize(v) for v in values),
               'Aliases must be nonempty strings: ' + ident)
        result[ident] = sorted({normalize(v) for v in values})
    return result


def valid_timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(
            r'\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})', value):
        return False
    if int(value[11:13]) > 23 or int(value[14:16]) > 59 or int(value[17:19]) > 60:
        return False
    if value[-1] not in 'Zz' and (int(value[-5:-3]) > 23 or int(value[-2:]) > 59):
        return False
    # datetime cannot represent RFC3339 leap-second :60; validate that case with :59.
    parsed = value[:17] + ('59' if value[17:19] == '60' else value[17:19]) + value[19:]
    try:
        datetime.fromisoformat(parsed.upper().replace('Z', '+00:00'))
    except ValueError:
        return False
    return True


def read_registry(data, index):
    if data is None:
        return {}
    schema(isinstance(data, dict) and type(data.get('schemaVersion')) is int
           and data['schemaVersion'] == 1 and isinstance(data.get('entries'), list), 'Invalid registry schema')
    result = {}
    for receipt in data['entries']:
        schema(isinstance(receipt, dict), 'Receipt must be an object')
        pair = receipt.get('pair')
        schema(isinstance(pair, list) and len(pair) == 2 and all(isinstance(x, str) and x for x in pair)
               and pair[0] < pair[1], 'Receipt pair must contain two canonical, distinct IDs')
        pair = tuple(pair)
        schema(pair not in result, 'Duplicate registry pair: ' + str(pair))
        hashes = receipt.get('fingerprints')
        schema(isinstance(hashes, list) and len(hashes) == 2 and all(
            isinstance(h, str) and re.fullmatch('[0-9a-f]{64}', h) for h in hashes), 'Invalid receipt fingerprints')
        for key in ('profile', 'decision', 'rationale', 'reviewer'):
            schema(isinstance(receipt.get(key), str) and receipt[key].strip(), 'Invalid receipt ' + key)
        schema(receipt['decision'] in DECISIONS, 'Unknown review decision')
        schema(valid_timestamp(receipt.get('reviewedAt')), 'Invalid RFC3339 reviewedAt')
        mapping = receipt.get('mapping')
        schema(isinstance(mapping, dict) and all(isinstance(mapping.get(k), str) and mapping[k].strip()
               for k in ('carriers', 'equality', 'operations', 'assumptions')), 'Incomplete semantic mapping')
        existing = [index[x]['type'] for x in pair if x in index]
        schema(all(t in SUBJECT_TYPES for t in existing), 'Receipt endpoints must be eligible subjects')
        if len(existing) == 2:
            schema(SUBJECT_TYPES[existing[0]] == SUBJECT_TYPES[existing[1]], 'Cross-family receipt')
        if receipt['decision'] == 'specialization':
            schema(all(t == 'Concept' for t in existing), 'Specialization receipt requires Concepts')
            schema(isinstance(receipt.get('specializedId'), str) and isinstance(receipt.get('generalId'), str)
                   and receipt['specializedId'] != receipt['generalId']
                   and {receipt['specializedId'], receipt['generalId']} == set(pair), 'Invalid specialization direction')
        result[pair] = receipt
    return result


class Audit:
    """Pure catalog interpretation, with lazy review closures and fingerprints."""

    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.index = snapshot.index
        self.aliases = read_aliases(snapshot.extra.get('aliases'), self.index)
        self.registry = read_registry(snapshot.extra.get('registry'), self.index)
        self.subjects = sorted(i for i, n in self.index.items() if n['type'] in SUBJECT_TYPES)
        self.features = {i: self.extract_features(i) for i in self.subjects}
        self.names = {i: self.exact_names(i) for i in self.subjects}
        self._closures = {}
        self._fingerprints = {}

    def evidence_closure(self, ident):
        if ident not in self._closures:
            pending, seen = [ident], set()
            while pending:
                node = pending.pop()
                if node not in seen:
                    seen.add(node)
                    pending.extend(refs(self.index[node], CLOSURE_LINKS))
            self._closures[ident] = frozenset(seen)
        return self._closures[ident]

    def fingerprint(self, ident):
        if ident not in self._fingerprints:
            payload = {'profile': PROFILE, 'context': self.snapshot.doc['@context'],
                       'records': {i: self.index[i] for i in self.evidence_closure(ident)},
                       'aliases': self.aliases.get(ident, [])}
            self._fingerprints[ident] = digest(canon(payload))
        return self._fingerprints[ident]

    def exact_names(self, ident):
        n = self.index[ident]
        names = ([n.get('shortForm'), n.get('fullName'), *self.aliases.get(ident, [])]
                 if n['type'] == 'Concept' else [n.get('name')])
        return {normalize(v) for v in names if isinstance(v, str) and normalize(v)}

    def extract_features(self, ident):
        n = self.index[ident]
        if n['type'] == 'Concept':
            name = [n.get('shortForm'), n.get('fullName'), *self.aliases.get(ident, [])]
            description = [n.get('definition'), n.get('mathematicalFormulation')]
            interface = [[self.index[x].get(k) for k in ('name', 'signature', 'precondition', 'totality', 'outcome', 'postcondition')]
                         for x in n.get('hasOperation', [])]
            basis = [n.get(k) for k in ('axiomBasis', 'basisKind', 'basisScope')]
            basis += [[self.index[x].get(k) for k in ('formalStatement', 'assumptions', 'ruleRole')]
                      for x in n.get('hasAxiom', [])]
            context = refs(n, ('category', 'kind', 'requiresConcept'))
        else:
            name, description, interface = [n.get('name')], [n.get('statement'), n.get('description')], []
            basis = [n.get(k) for k in ('formalStatement', 'assumptions', 'ruleRole')]
            context = refs(n, ('appliesTo', 'dependsOn'))
        return dict(zip(CHANNELS, (tokens(name), tokens(description), tokens(interface), tokens(basis), frozenset(context))))

    def score_pair(self, pair):
        a, b = pair
        family = SUBJECT_TYPES[self.index[a]['type']]
        components, total = {}, Fraction(0)
        for channel, weight in zip(CHANNELS, WEIGHTS[family]):
            left, right = self.features[a][channel], self.features[b][channel]
            intersection = len(left & right)
            union = len(left) + len(right) - intersection
            components[channel] = {'intersectionCount': intersection, 'unionCount': union, 'weight': weight}
            total += Fraction(weight * intersection, union or 1)
        return (100 * total.numerator) // total.denominator, components

    def classify_review(self, pair):
        receipt = self.registry.get(pair)
        if receipt is None:
            return 'unreviewed'
        if (receipt['profile'] != PROFILE or
                receipt['fingerprints'] != [self.fingerprint(i) for i in pair]):
            return 'stale'
        if receipt['decision'] == 'same_meaning':
            return 'confirmed_duplicate'
        if receipt['decision'] == 'undecided':
            return 'undecided'
        return 'reviewed_distinct'

    def location(self, ident):
        path = self.snapshot.owners[ident]
        # Concept records occupy their page root; only operations/claims have
        # generated node anchors. Shared vocabulary lives in one JSON document.
        fragment = None if path == 'data/shared.json' or self.index[ident]['type'] == 'Concept' else anchor(ident)
        return {'id': ident, 'path': path, 'anchor': fragment}

    def endpoint(self, ident):
        node = self.index[ident]
        # Retain full records, rather than risk dropping a semantic qualifier.
        fields = dict(node)
        if ident in self.aliases:
            fields['aliases'] = self.aliases[ident]
        direct = sorted(set(refs(node, LINK_TYPES)))
        evidence = [self.location(target) for target in direct]
        # Source records are inline as well as linked, including consultation metadata.
        fields['directSources'] = [self.index[s] for s in sorted(set(node.get('source', [])))]
        if node['type'] == 'Concept':
            fields['directOperations'] = [self.index[s] for s in sorted(set(node.get('hasOperation', [])))]
            fields['directAxioms'] = [self.index[s] for s in sorted(set(node.get('hasAxiom', [])))]
        return {**self.location(ident), 'type': node['type'], 'fingerprint': self.fingerprint(ident),
                'fields': fields, 'evidenceRecords': evidence}

    def candidate(self, summary):
        score, a, b, state, triggers = summary
        endpoints = [self.endpoint(a), self.endpoint(b)]
        _, components = self.score_pair((a, b))
        left, right = (e['fields'] for e in endpoints)
        differences = [k for k in sorted(left.keys() | right.keys())
                       if k not in left or k not in right or canon(left[k]) != canon(right[k])]
        receipt = self.registry.get((a, b))
        return {'pair': [a, b], 'family': SUBJECT_TYPES[self.index[a]['type']], 'score': score,
                'components': components, 'triggers': sorted(triggers),
                'matches': {k: sorted(self.features[a][k] & self.features[b][k]) for k in CHANNELS},
                'matchedNames': sorted(self.names[a] & self.names[b]), 'endpoints': endpoints,
                'differences': differences, 'reviewState': state,
                'currentReview': receipt if state not in ('stale', 'unreviewed') else None,
                'previousReview': receipt if state == 'stale' else None}

    def iter_scored_pairs(self, affected, threshold=3000):
        """Stream qualified pair summaries for the audit and downstream triage.

        Keeps DA-P1 scoring/receipt semantics in one place, without building
        large endpoint payloads for every candidate.
        """
        for family in ('concept', 'claim'):
            ids = [i for i in self.subjects if SUBJECT_TYPES[self.index[i]['type']] == family]
            for a, b in itertools.combinations(ids, 2):
                if a not in affected and b not in affected:
                    continue
                score, _ = self.score_pair((a, b))
                triggers = []
                if score >= threshold:
                    triggers.append('threshold')
                if self.names[a] & self.names[b]:
                    triggers.append('exact_name')
                if family == 'claim':
                    x, y = (self.index[i].get('formalStatement') for i in (a, b))
                    if isinstance(x, str) and isinstance(y, str) and normalize(x) and normalize(x) == normalize(y):
                        triggers.append('exact_statement')
                state = self.classify_review((a, b))
                if state == 'confirmed_duplicate':
                    triggers.append('confirmed_review')
                elif state == 'stale':
                    triggers.append('stale_review')
                if triggers:
                    yield score, a, b, state, triggers

    def build_report(self, *, changed=None, threshold=3000, limit=50, include_reviewed=False):
        schema(type(threshold) is int and 0 <= threshold <= 10000, 'threshold must be 0..10000')
        schema(type(limit) is int and limit >= 0, 'limit must be nonnegative')
        requested = sorted(set(changed or []))
        schema(changed is None or bool(requested), 'changed must have at least one ID')
        schema(all(i in self.index for i in requested), 'Unknown changed ID')
        affected = (set(self.subjects) if changed is None else
                    {i for i in self.subjects if self.evidence_closure(i).intersection(requested)})
        families = [[i for i in self.subjects if SUBJECT_TYPES[self.index[i]['type']] == f]
                    for f in ('concept', 'claim')]
        total_pairs = sum(len(ids) * (len(ids) - 1) // 2 for ids in families)
        inspected = sum(len(ids) * (len(ids) - 1) // 2 -
                        sum(i not in affected for i in ids) * (sum(i not in affected for i in ids) - 1) // 2
                        for ids in families)
        counts = Counter({state: 0 for state in STATES})
        registry_qualifies = set()
        queue_size = 0

        def summaries():
            nonlocal queue_size
            for score, a, b, state, triggers in self.iter_scored_pairs(affected, threshold):
                counts[state] += 1
                if (a, b) in self.registry:
                    registry_qualifies.add((a, b))
                if state == 'reviewed_distinct' and not include_reviewed:
                    continue
                queue_size += 1
                yield (score, a, b, state, triggers)

        # nsmallest(0, ...) does not consume its input. DA-15 still requires counts.
        stream = summaries()
        if limit:
            top = heapq.nsmallest(limit, stream, key=lambda row: (-row[0], row[1], row[2]))
        else:
            for _ in stream:
                pass
            top = []
        receipts = []
        for pair, receipt in sorted(self.registry.items()):
            orphan = any(i not in self.index for i in pair)
            state = None if orphan else self.classify_review(pair)
            receipts.append({'pair': list(pair), 'status': 'orphaned' if orphan else 'stale' if state == 'stale' else 'current',
                             'decision': receipt['decision'],
                             'inInspectedUniverse': not orphan and any(i in affected for i in pair),
                             'qualifies': pair in registry_qualifies})
        return {'schemaVersion': 1, 'profile': PROFILE, 'semantics': 'heuristic-candidates-not-equivalence',
                'inputs': self.snapshot.metadata(),
                'scope': {'mode': 'full' if changed is None else 'incremental', 'requestedChangedIds': requested,
                          'affectedSubjectIds': sorted(affected), 'threshold': threshold, 'limit': limit,
                          'includeReviewed': include_reviewed, 'inspectedPairCount': inspected,
                          'totalPairCount': total_pairs, 'uninspectedPairCount': total_pairs - inspected},
                'counts': {'qualifiedCount': sum(counts.values()), 'stateCounts': dict(counts),
                           'hiddenReviewedCount': counts['reviewed_distinct'] if not include_reviewed else 0,
                           'queueSize': queue_size, 'returnedCount': len(top)},
                'truncated': len(top) < queue_size, 'candidates': [self.candidate(row) for row in top],
                'registrySummary': receipts, 'limitations': LIMITATIONS}


def render_json(report):
    return json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + '\n'


def render_markdown(report):
    def inline(value):
        return str(value).replace('`', '\\`').replace('|', '\\|').replace('\n', ' ')
    lines = ['# Duplicate-candidate audit', '',
             'Heuristic review candidates; no mathematical equivalence or merge authorization.', '',
             '## Scope and counts', '', '```json', render_json({
                 'scope': report['scope'], 'counts': report['counts'], 'truncated': report['truncated'],
                 'inputs': report['inputs']}).rstrip(), '```', '']
    if report['truncated']:
        lines += ['**Truncated: additional queued pairs are not displayed.**', '']
    lines += ['## Candidates', '']
    for row in report['candidates']:
        lines += [f"### {row['score']} / 10000 — {row['reviewState']}", '',
                  'Pair: ' + ' / '.join('`' + inline(i) + '`' for i in row['pair']), '',
                  'Triggers: ' + ', '.join(row['triggers']) + '.', '',
                  'Textual field differences: ' + ', '.join(row['differences']) + '.', '']
        for endpoint in row['endpoints']:
            target = quote(endpoint['path'], safe='/')
            if endpoint['anchor'] is not None:
                target += '#' + endpoint['anchor']
            fields = endpoint['fields']
            lines += [f"[{inline(endpoint['id'])}]({target}) — {endpoint['type']}", '',
                      '**Scope, assumptions, role and provenance (unknown when absent):**', '',
                      '```json', render_json({k: fields[k] for k in (
                          'basisScope', 'assumptions', 'verificationObligation', 'ruleRole', 'reviewStatus',
                          'provenanceStatus', 'source', 'sourceLocator', 'sourceNote', 'directSources') if k in fields}).rstrip(),
                      '```', '']
        # Complete candidate payload also preserves all evidence/receipt state in Markdown.
        lines += ['<details><summary>Full candidate evidence</summary>', '', '```json',
                  render_json(row).rstrip(), '```', '', '</details>', '']
    lines += ['## Registry', '', '```json', render_json(report['registrySummary']).rstrip(), '```', '',
              '## Limitations', '', *['- ' + text for text in report['limitations']], '']
    return '\n'.join(lines)


def output_path(path, snapshot):
    """DA-18 rejects protected locations before exclusive file creation."""
    original = Path(path).absolute()
    schema(not original.is_symlink(), 'Output cannot be a symlink')
    target = original.resolve()
    protected = {'concepts', 'data', 'lean', 'ontology', 'visualization', 'deps', '.git'}
    for candidate in (Path(os.path.abspath(original)), target):
        if candidate.is_relative_to(snapshot.root):
            parts = candidate.relative_to(snapshot.root).parts
            schema(not (parts and parts[0] in protected) and not any(p.startswith('.') for p in parts),
                   'Output is in a protected catalog location')
    inputs = set(snapshot.raw) | set(snapshot.policy) | set(snapshot.tool)
    inputs.update(p for p, _ in snapshot.explicit.values())
    schema(target not in {p.resolve() for p in inputs}, 'Output aliases an input')
    schema(not target.exists(), 'Output already exists')
    return target


def write_report(handle, text):
    """One write boundary, also used for deterministic I/O-failure injection."""
    handle.write(text)
    handle.flush()


def emit(text, target=None):
    if target is None:
        sys.stdout.write(text)
        sys.stdout.flush()
        return
    # x mode is the final race-safe no-overwrite check; never remove someone else's file.
    handle = target.open('x', encoding='utf-8', newline='\n')
    created = os.fstat(handle.fileno())
    try:
        with handle:
            write_report(handle, text)
    except BaseException:
        try:
            current = target.lstat()
            if (current.st_dev, current.st_ino) != (created.st_dev, created.st_ino):
                raise OSError('Partial report path was replaced; replacement preserved')
            target.unlink()
        except OSError as cleanup:
            print('Audit output cleanup failed: ' + str(cleanup), file=sys.stderr)
        raise


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--changed', nargs='+', action='extend')
    cli.add_argument('--aliases', type=Path)
    cli.add_argument('--registry', type=Path)
    cli.add_argument('--threshold', type=int, default=3000)
    cli.add_argument('--limit', type=int, default=50)
    cli.add_argument('--include-reviewed', action='store_true')
    cli.add_argument('--format', choices=('json', 'markdown'), default='json')
    cli.add_argument('--output', type=Path)
    return cli


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        schema(0 <= args.threshold <= 10000 and args.limit >= 0, 'threshold must be 0..10000 and limit nonnegative')
        snapshot = Snapshot(aliases=args.aliases, registry=args.registry)
        target = output_path(args.output, snapshot) if args.output is not None else None
        report = Audit(snapshot).build_report(changed=args.changed, threshold=args.threshold,
                                            limit=args.limit, include_reviewed=args.include_reviewed)
        text = render_json(report) if args.format == 'json' else render_markdown(report)
        snapshot.verify()
        emit(text, target)
    except (ValueError, TypeError, KeyError, UnicodeError) as exc:
        print('Audit input error: ' + str(exc), file=sys.stderr)
        return 2
    except (OSError, MemoryError, OverflowError, RecursionError) as exc:
        print('Audit I/O or resource error: ' + str(exc), file=sys.stderr)
        return 3
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
