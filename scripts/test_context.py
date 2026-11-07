#!/usr/bin/env python3
"""Bounded, freshness-checked ONTFS retrieval for abstraction-based test design."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

from markdown_graph import ROOT, load_graph
from ontology import CA, backend, input_digest

PREFIX = 'PREFIX ca: <' + CA + '>\n'
SECTIONS = {'operations': 'hasOperation', 'axioms': 'hasAxiom',
            'laws': 'hasLaw', 'theorems': 'hasTheorem'}
KINDS = {'axiom': 'Axiom', 'law': 'Law', 'theorem': 'Theorem'}
INTERPRETATION = ('Recorded mathematics, not a software contract or proof. Map carriers, '
                  'operations, equality, applicability and preconditions to the target API. '
                  'Prerequisites and specializations do not transfer axioms.')


def encode(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + '\n'


def bounded_page(records, total, offset, limit, max_chars, metadata):
    """Page atomic records. Never truncate mathematical text or its assumptions."""
    def envelope(selected):
        next_offset = offset + len(selected)
        more = next_offset < total
        return {**metadata, 'offset': offset, 'limit': limit, 'maxChars': max_chars,
                'total': total, 'returned': len(selected), 'records': selected,
                'truncated': more or bool(metadata.get('depthBoundary', {}).get('count')),
                'nextOffset': next_offset if more else None,
                'needsLargerBudget': False}

    selected = []
    for record in records[:limit]:
        candidate = envelope(selected + [record])
        if len(encode(candidate)) > max_chars:
            break
        selected.append(record)
    result = envelope(selected)
    if not selected and records:
        result['needsLargerBudget'] = True
        result['blockedRecord'] = records[0]['id']
        result['requiredChars'] = len(encode(envelope([records[0]])))
        result['hint'] = 'Increase --max-chars; records and mathematical statements are not clipped.'
    if len(encode(result)) > max_chars:
        raise ValueError('Response metadata exceeds --max-chars; increase the budget')
    return result


class TestContext:
    """Query IDs/typed edges through ONTFS, return lossless Markdown JSON records.

    The source graph is loaded internally for freshness and lossless arrays/types;
    it is never dumped into an agent's context. No inference or runtime mutation.
    """

    def __init__(self, directory=ROOT):
        import inspect
        expected_backend = ROOT / 'deps/ONTFS/ontfs/core.py'
        if not expected_backend.is_file():
            raise RuntimeError('Pinned ONTFS checkout is missing; run make submodules')
        OntFS = backend()
        if Path(inspect.getfile(OntFS)).resolve() != expected_backend.resolve():
            raise RuntimeError('ONTFS import is not from the pinned checkout; use a fresh Python process with this repository backend')
        from ontfs.storage import locked
        self.directory = Path(directory).resolve()
        target = self.directory / '.ontfs.ttl'
        marker = self.directory / '.ontfs.generated.json'
        if not target.is_file() or not marker.is_file():
            raise ValueError('ONTFS projection is missing. Run scripts/ontology.py build with the same --directory.')
        doc = load_graph()
        self.index = {node['id']: node for node in doc['@graph']}
        self.input_hash = input_digest(doc)
        # Load a consistent snapshot under the same lock used by the exporter.
        with locked(target):
            stamp = json.loads(marker.read_text())
            if not isinstance(stamp, dict):
                raise ValueError('ONTFS generation marker must be a JSON object')
            if stamp.get('inputSha256') != self.input_hash:
                raise ValueError('ONTFS projection is stale. Rebuild with scripts/ontology.py build before querying.')
            if hashlib.sha256(target.read_bytes()).hexdigest() != stamp.get('sha256'):
                raise ValueError('ONTFS projection has local edits. Preserve it and build a separate scratch projection; it will not be overwritten.')
            self.store = OntFS(str(self.directory))
            self.store.graph  # eagerly load this snapshot; no save/transaction

    @staticmethod
    def literal(value):
        from rdflib import Literal
        return Literal(value).n3()

    @staticmethod
    def iri(value):
        from rdflib import URIRef
        return URIRef(value).n3()

    def query(self, sparql):
        return list(self.store.graph.query_graph(PREFIX + sparql))

    def resolve(self, value, concept=False):
        if len(value) > 300:
            raise ValueError('Identifier is too long')
        term = self.literal(value)
        types = 'ca:Concept' if concept else 'ca:Concept ca:Operation ca:Axiom ca:Law ca:Theorem ca:Source'
        rows = self.query('SELECT DISTINCT ?id WHERE { VALUES ?type { ' + types + ' } '
                          '?id a ?type . OPTIONAL { ?id ca:shortForm ?name } '
                          'FILTER(STR(?id) = ' + term + ' || LCASE(STR(?name)) = LCASE(' + term + ')) } LIMIT 2')
        if len(rows) != 1 or str(rows[0][0]) not in self.index:
            raise ValueError('Unknown or ambiguous catalog ' + ('concept: ' if concept else 'ID: ') + value)
        return str(rows[0][0])

    def page(self, command, body, *, offset=0, limit=6, max_chars=12000,
             seed=None, compact=False, extra=None):
        if not 0 <= offset <= 10000 or not 1 <= limit <= 32 or not 2048 <= max_chars <= 40000:
            raise ValueError('Require offset 0..10000, limit 1..32, max-chars 2048..40000')
        total = int(self.query('SELECT (COUNT(DISTINCT ?id) AS ?n) WHERE { ' + body + ' }')[0][0])
        order = ('DESC(?id = ' + self.iri(seed) + ') ' if seed else '') + 'STR(?id)'
        rows = self.query('SELECT DISTINCT ?id WHERE { ' + body + ' } ORDER BY ' + order +
                          ' LIMIT ' + str(limit) + ' OFFSET ' + str(offset))
        records = []
        for row in rows:
            ident = str(row[0])
            if ident not in self.index:
                raise ValueError('ONTFS query returned a non-catalog record: ' + ident)
            record = self.index[ident]
            if compact:
                record = {key: record[key] for key in ('id', 'type', 'shortForm', 'fullName', 'category') if key in record}
            records.append(record)
        metadata = {'command': command, **(extra or {}), 'projectionInputSha256': self.input_hash,
                    'selectionBackend': 'ONTFS/SPARQL', 'interpretation': INTERPRETATION}
        return bounded_page(records, total, offset, limit, max_chars, metadata)

    def search(self, term, category=None, **bounds):
        if len(term) > 200 or (category and len(category) > 100):
            raise ValueError('Search term/category is too long')
        if not term.strip() and not category:
            raise ValueError('Supply a nonempty search term or --category')
        body = '?id a ca:Concept . '
        if term:
            body += ('{ { ?id ?field ?text . VALUES ?field { ca:shortForm ca:fullName ca:definition ca:notation ca:axiomBasis } } '
                     'UNION { ?id ca:hasOperation ?operation . ?operation ?field ?text . '
                     'VALUES ?field { ca:name ca:description ca:signature } } } '
                     'FILTER(CONTAINS(LCASE(STR(?text)), LCASE(' + self.literal(term) + '))) ')
        if category:
            body += ('?id ca:category ?category . FILTER(STR(?category) = ' + self.literal(category) +
                     ' || STRENDS(STR(?category), CONCAT("/", ' + self.literal(category) + '))) ')
        return self.page('search', body, compact=True, extra={'term': term, 'category': category}, **bounds)

    def node(self, value, **bounds):
        ident = self.resolve(value)
        return self.page('node', 'VALUES ?id { ' + self.iri(ident) + ' }', seed=ident, **bounds)

    def interface(self, value, sections=('operations', 'axioms'), **bounds):
        ident = self.resolve(value, concept=True)
        if not sections or any(s not in SECTIONS for s in sections):
            raise ValueError('Select operations, axioms, laws or theorems')
        relations = ' '.join('ca:' + SECTIONS[s] for s in sections)
        root = self.iri(ident)
        body = ('{ BIND(' + root + ' AS ?id) } UNION { ' + root + ' ?relation ?id . '
                'VALUES ?relation { ' + relations + ' } }')
        return self.page('interface', body, seed=ident,
                         extra={'concept': ident, 'sections': list(sections)}, **bounds)

    def claims(self, value, kind='law', **bounds):
        ident = self.resolve(value, concept=True)
        if kind not in KINDS:
            raise ValueError('Claim kind must be axiom, law or theorem')
        # Membership uses the concept's explicit typed edge, not inherited facts.
        rel = {'axiom': 'hasAxiom', 'law': 'hasLaw', 'theorem': 'hasTheorem'}[kind]
        body = self.iri(ident) + ' ca:' + rel + ' ?id . ?id a ca:' + KINDS[kind] + ' .'
        return self.page('claims', body, extra={'concept': ident, 'kind': kind}, **bounds)

    def premises(self, value, depth=1, **bounds):
        ident = self.resolve(value)
        if self.index[ident]['type'] not in {'Axiom', 'Law', 'Theorem', 'Operation'}:
            raise ValueError('Premises require a claim or operation ID')
        if not 0 <= depth <= 6:
            raise ValueError('Premise depth must be between 0 and 6')
        root = self.iri(ident)
        path = '/'.join(['ca:dependsOn?'] * depth)
        def reached(variable):
            return root + ' ' + path + ' ' + variable + ' .' if depth else 'BIND(' + root + ' AS ' + variable + ')'
        body = reached('?id')
        outside = ('FILTER NOT EXISTS { ' + reached('?id') + ' }' if depth else
                   'FILTER(?id != ' + root + ')')
        boundary = reached('?parent') + ' ?parent ca:dependsOn ?id . ' + outside
        count = int(self.query('SELECT (COUNT(DISTINCT ?id) AS ?n) WHERE { ' + boundary + ' }')[0][0])
        sample = [str(row[0]) for row in self.query('SELECT DISTINCT ?id WHERE { ' + boundary + ' } ORDER BY STR(?id) LIMIT 5')]
        return self.page('premises', body, seed=ident,
                         extra={'claim': ident, 'depth': depth,
                                'depthBoundary': {'count': count, 'sample': sample}}, **bounds)

    def sources(self, value, **bounds):
        ident = self.resolve(value)
        body = self.iri(ident) + ' ca:source ?id . ?id a ca:Source .'
        return self.page('sources', body, extra={'subject': ident, 'scope': 'direct citations only'}, **bounds)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT, help='Generated ONTFS projection directory')
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--limit', type=int, default=6)
    common.add_argument('--offset', type=int, default=0)
    common.add_argument('--max-chars', type=int, default=12000)
    sub = parser.add_subparsers(dest='command', required=True)
    search = sub.add_parser('search', parents=[common]); search.add_argument('term')
    search.add_argument('--category')
    for name in ('node', 'interface', 'claims', 'premises', 'sources'):
        command = sub.add_parser(name, parents=[common]); command.add_argument('id')
        if name == 'interface':
            command.add_argument('--sections', nargs='+', choices=list(SECTIONS), default=['operations', 'axioms'])
        elif name == 'claims':
            command.add_argument('--kind', choices=list(KINDS), default='law')
        elif name == 'premises':
            command.add_argument('--depth', type=int, default=1)
    args = parser.parse_args(argv)
    try:
        store = TestContext(args.directory)
        bounds = {'limit': args.limit, 'offset': args.offset, 'max_chars': args.max_chars}
        if args.command == 'search':
            result = store.search(args.term, args.category, **bounds)
        else:
            extra = {key: getattr(args, key) for key in ('sections', 'kind', 'depth') if hasattr(args, key)}
            result = getattr(store, args.command)(args.id, **extra, **bounds)
        sys.stdout.write(encode(result))
        return 2 if result['needsLargerBudget'] else 0
    except (ValueError, RuntimeError, ImportError, OSError) as exc:
        print('Test context error: ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
