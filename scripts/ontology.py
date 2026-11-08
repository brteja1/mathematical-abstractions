#!/usr/bin/env python3
"""Build and query the ONTFS projection of the authoritative Markdown graph."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from markdown_graph import ROOT, load_graph
from validate_graph import validate

CA = 'https://w3id.org/cs-abstractions/v1#'


def backend():
    path = ROOT / 'deps/ONTFS'
    if path.exists():
        lock = json.loads((ROOT / 'dependencies.lock.json').read_text())['ONTFS']
        try:
            head = subprocess.check_output(['git', '-C', str(path), 'rev-parse', 'HEAD'], text=True, stderr=subprocess.DEVNULL).strip()
        except subprocess.CalledProcessError:
            raise RuntimeError('ONTFS dependency is not initialized; run make')
        if head != lock['commit']:
            raise RuntimeError('ONTFS checkout does not match dependencies.lock.json')
        sys.path.insert(0, str(path))
    try:
        from ontfs.core import OntFS
    except ImportError as exc:
        raise RuntimeError('ONTFS is unavailable. Run make, then use the project virtual environment; see INSTALL.md.') from exc
    return OntFS


def build(directory):
    from rdflib import Graph, URIRef, Literal, RDF, RDFS, OWL
    OntFS = backend()
    from ontfs.storage import locked, atomic_write
    directory = Path(directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    doc = load_graph()
    errors = validate(doc)
    if errors:
        raise ValueError('; '.join(errors))
    data = Graph().parse(data=json.dumps(doc), format='json-ld')
    model = Graph().parse(ROOT / 'ontology/model.ttl', format='turtle')
    # Declare all imported predicates without changing their JSON-LD interpretation.
    # Some legacy metadata has heterogeneous literals, so no invented datatype ranges.
    for predicate in set(data.predicates()):
        if str(predicate).startswith(CA):
            if not list(model.objects(predicate, RDF.type)):
                model.add((predicate, RDF.type, RDF.Property))
    target = directory / '.ontfs.ttl'
    marker = directory / '.ontfs.generated.json'
    with locked(target):
        if target.exists():
            previous = json.loads(marker.read_text()) if marker.exists() else {}
            if hashlib.sha256(target.read_bytes()).hexdigest() != previous.get('sha256'):
                raise ValueError('ONTFS graph contains unexported edits or is not generated. Preserve it before rebuilding; use a separate --directory for experiments.')
        store = OntFS(str(directory))
        with store.graph.transaction():
            store.graph.graph = Graph()
            store.graph.graph.bind('ca', URIRef(CA))
            for graph in (data, model):
                for prefix, namespace in graph.namespaces():
                    store.graph.graph.bind(prefix, namespace)
                for triple in graph:
                    store.graph.graph.add(triple)
            for n in doc['@graph']:
                if n['type'] != 'Concept':
                    continue
                subject = URIRef(n['id'])
                page = ROOT / 'concepts' / (n['shortForm'] + '.md')
                file_uri = store.graph.resolve_uri(page.as_uri())
                store.graph.graph.add((subject, RDFS.label, Literal(n['fullName'])))
                store.graph.graph.add((subject, URIRef(CA + 'document'), file_uri))
                store.graph.graph.add((file_uri, RDF.type, URIRef(CA + 'Document')))
            store.graph.is_dirty = True
        shapes = directory / '.ontfs.shapes.ttl'
        atomic_write(shapes, (ROOT / 'ontology/shapes.ttl').read_text())
        atomic_write(marker, json.dumps({'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                                        'source': 'concepts/*.md and data/shared.json',
                                        'catalogNodes': len(doc['@graph']),
                                        'inputSha256': input_digest(doc)}, indent=2) + '\n')
    return {'path': str(target), 'catalogNodes': len(doc['@graph']), 'triples': len(store.graph.graph)}


def input_digest(doc):
    payload = json.dumps(doc, sort_keys=True, ensure_ascii=False).encode()
    for name in ['model.ttl', 'shapes.ttl']:
        payload += (ROOT / 'ontology' / name).read_bytes()
    return hashlib.sha256(payload).hexdigest()


def load_projection(directory):
    """Load an intact, fresh ONTFS snapshot without overwriting local experiments."""
    OntFS = backend()
    from ontfs.storage import locked
    directory = Path(directory).resolve()
    target = directory / '.ontfs.ttl'
    if not target.is_file():
        raise ValueError('ONTFS projection is missing; run make ontology')
    doc = load_graph()
    errors = validate(doc)
    if errors:
        raise ValueError('; '.join(errors))
    marker = directory / '.ontfs.generated.json'
    with locked(target):
        stamp = json.loads(marker.read_text()) if marker.is_file() else {}
        if not isinstance(stamp, dict) or stamp.get('inputSha256') != input_digest(doc):
            raise ValueError('ONTFS projection inputs changed; run make ontology')
        if hashlib.sha256(target.read_bytes()).hexdigest() != stamp.get('sha256'):
            raise ValueError('ONTFS projection has local edits; preserve it before rebuilding')
        shapes = directory / '.ontfs.shapes.ttl'
        if not shapes.is_file() or shapes.read_bytes() != (ROOT / 'ontology/shapes.ttl').read_bytes():
            raise ValueError('SHACL shapes are missing or modified; preserve local edits before rebuilding')
        store = OntFS(str(directory))
        store.graph  # eagerly load the graph under the exporter lock
    return store


def check(directory):
    store = load_projection(directory)
    result = store.validate()
    if not result['shapes_loaded']:
        raise ValueError('SHACL shapes are missing; run make ontology')
    count = int(list(store.graph.query_graph('SELECT (COUNT(?c) AS ?n) WHERE { ?c a <' + CA + 'Concept> }'))[0][0])
    result['concepts'] = count
    if count != sum(n['type'] == 'Concept' for n in load_graph()['@graph']):
        result['conforms'] = False
        result['error'] = 'ONTFS concept count differs from Markdown graph'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build'); sub.add_parser('check')
    ctx = sub.add_parser('context'); ctx.add_argument('id')
    ctx.add_argument('--depth', type=int, default=1); ctx.add_argument('--limit', type=int, default=30)
    query = sub.add_parser('query'); query.add_argument('file', type=Path)
    args = parser.parse_args()
    try:
        OntFS = backend()
        if args.command == 'build':
            result = build(args.directory)
        elif args.command == 'check':
            result = check(args.directory)
        else:
            if not (args.directory / '.ontfs.ttl').is_file():
                raise ValueError('Run make ontology before querying ONTFS')
            store = OntFS(str(args.directory))
            if args.command == 'context':
                result = store.context(args.id, depth=args.depth, limit=args.limit)
            else:
                resultset = store.graph.query_graph(args.file.read_text())
                if resultset.type != 'SELECT':
                    raise ValueError('This command supports SELECT queries')
                result = [{str(key): str(value) for key, value in row.asdict().items()} for row in resultset]
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return int(isinstance(result, dict) and result.get('conforms') is False)
    except (RuntimeError, ValueError, ImportError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    raise SystemExit(main())
