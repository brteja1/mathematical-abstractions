#!/usr/bin/env python3
"""Read authoritative Markdown records and build deterministic linked projections."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCK = re.compile(r'<!-- graph-record:start -->\n```json\n(.*?)\n```\n<!-- graph-record:end -->', re.S)
RELATIONS = {'requiresConcept': 'Prerequisites', 'specializationOf': 'Specializes', 'relatedConcept': 'Related concepts'}
SECTIONS = {'hasOperation': 'Operations', 'hasAxiom': 'Axioms and defining rules', 'hasLaw': 'Laws', 'hasTheorem': 'Theorems'}


def read_records(path):
    matches = BLOCK.findall(path.read_text())
    if len(matches) != 1:
        raise ValueError(f'{path}: expected exactly one graph-record JSON block')
    nodes = json.loads(matches[0])
    if not isinstance(nodes, list) or not all(isinstance(n, dict) for n in nodes):
        raise ValueError(f'{path}: graph record must be an array of objects')
    concepts = [n for n in nodes if n.get('type') == 'Concept']
    if len(concepts) != 1 or path.stem != concepts[0].get('shortForm'):
        raise ValueError(f'{path}: filename must match its sole Concept shortForm')
    if any(n.get('type') not in {'Concept', 'Operation', 'Axiom', 'Law', 'Theorem'} for n in nodes):
        raise ValueError(f'{path}: shared vocabulary and sources belong in data/shared.json')
    concept = concepts[0]
    owned = {ref for key in SECTIONS for ref in concept.get(key, [])}
    if not {n.get('id') for n in nodes if n is not concept} <= owned:
        raise ValueError(f'{path}: record contains an operation or claim not linked by its concept')
    return nodes


def load_graph(root=ROOT):
    shared = json.loads((root / 'data/shared.json').read_text())
    if any(n.get('type') in {'Concept', 'Operation', 'Axiom', 'Law', 'Theorem'} for n in shared['@graph']):
        raise ValueError('Concepts and their interfaces must be stored in concepts/*.md')
    nodes = list(shared['@graph'])
    for path in sorted((root / 'concepts').glob('*.md')):
        nodes.extend(read_records(path))
    return {'@context': shared['@context'], '@graph': sorted(nodes, key=lambda n: n['id'])}


def link(ident, index):
    n = index[ident]
    if n.get('type') == 'Concept':
        return f"[{n['fullName']}]({n['shortForm']}.md)"
    owner = n.get('concept') or next(iter(n.get('appliesTo', [])), None)
    label = n.get('name', n.get('label', ident))
    if owner in index and index[owner].get('type') == 'Concept':
        return f"[{label}]({index[owner]['shortForm']}.md#{anchor(ident)})"
    return label


def anchor(ident):
    return 'node-' + re.sub('[^a-zA-Z0-9_-]', '-', ident)


def value_text(value):
    if isinstance(value, list):
        return '; '.join(value_text(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def render(nodes, index):
    c = next(n for n in nodes if n['type'] == 'Concept')
    lines = [f"# {c['fullName']}", '', c['definition'], '', f"**Notation:** {c['notation']}", '',
             f"**Stable ID:** `{c['id']}`", '',
             '**Categories:** ' + ', '.join(index[x]['label'] for x in c['category']), '',
             f"**Kind:** {index[c['kind']]['label']}", '']
    for field, title in RELATIONS.items():
        if c.get(field):
            lines += [f"**{title}:** " + ', '.join(link(x, index) for x in c[field]), '']
    incoming = [(n, field) for n in index.values() if n.get('type') == 'Concept'
                for field in RELATIONS if c['id'] in n.get(field, [])]
    if incoming:
        lines += ['## Backlinks', '']
        lines += [f"- {link(n['id'], index)} — `{field}`" for n, field in sorted(incoming, key=lambda pair:(pair[0]['shortForm'],pair[1]))]
        lines += ['']
    lines += ['## Interface and scope', '']
    for key in ['axiomBasis', 'basisKind', 'basisScope', 'basisInstantiation', 'convention', 'specializationNote', 'noPrimitiveOperationsReason', 'verificationObligation', 'reviewStatus', 'coverageStatus', 'provenanceStatus']:
        if key in c:
            lines += [f'**{key}:** {value_text(c[key])}', '']
    for field, title in SECTIONS.items():
        lines += [f'## {title}', '']
        if not c[field]:
            lines += ['No entries recorded. This does not assert absence of mathematical facts.', '']
        for ident in c[field]:
            n = index[ident]
            lines += [f'<a id="{anchor(ident)}"></a>', '', f"### {n.get('name', ident.rsplit(':',1)[-1])}", '', f"`{ident}`", '']
            for key, value in n.items():
                if key in {'id', 'type', 'name', 'concept', 'appliesTo'}:
                    continue
                if key == 'source':
                    text = '; '.join(source_text(index[x]) for x in value)
                elif key == 'dependsOn':
                    text = '; '.join(link(x, index) for x in value)
                else:
                    text = value_text(value)
                lines += [f'**{key}:** {text}', '']
    lines += ['## Concept provenance', '']
    for ident in c.get('source', []):
        lines += ['- ' + source_text(index[ident])]
    if not c.get('source'):
        lines += ['Historical source gap retained; see `provenanceStatus` and the frozen baseline.']
    for key in ['sourceLocator', 'sourceNote', 'provenanceKind']:
        if key in c:
            lines += ['', f'**{key}:** {value_text(c[key])}']
    lines += ['', '## Structured record', '',
              'Edit this JSON block to change graph facts, then run `make build`. The prose and links above are generated from it.', '',
              '<!-- graph-record:start -->', '```json', json.dumps(nodes, ensure_ascii=False, indent=2), '```', '<!-- graph-record:end -->', '']
    return '\n'.join(lines)


def source_text(source):
    label = source['label']
    url = source.get('url')
    text = f'[{label}]({url})' if url else label
    for key in ['citation', 'path', 'accessedOn', 'sourceRole', 'license', 'licenseUrl']:
        if source.get(key):
            text += f'; {key}: {value_text(source[key])}'
    return text


def outputs(doc):
    index = {n['id']: n for n in doc['@graph']}
    result = {}
    concepts = sorted((n for n in index.values() if n['type'] == 'Concept'), key=lambda n:n['shortForm'])
    overview = ['# Mathematical abstractions', '', 'Each linked page contains the definition, assumptions, operations, claims, provenance, typed relationships, and backlinks.', '',
                '| Concept | Categories |', '| --- | --- |']
    assigned = set()
    for c in concepts:
        refs = list(dict.fromkeys(ref for key in SECTIONS for ref in c[key] if ref not in assigned))
        nodes = [c] + [index[ref] for ref in refs]
        assigned.update(refs)
        result[ROOT / 'concepts' / (c['shortForm'] + '.md')] = render(nodes, index)
        overview.append(f"| [{c['fullName']}](concepts/{c['shortForm']}.md) | " + ', '.join(index[x]['label'] for x in c['category']) + ' |')
    result[ROOT / 'CONCEPTS.md'] = '\n'.join(overview) + '\n'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    from validate_graph import validate
    doc = load_graph()
    errors = validate(doc)
    if errors:
        raise SystemExit('\n'.join(errors))
    stale = []
    for path, content in outputs(doc).items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content)
    if stale:
        raise SystemExit('Stale generated content; run make build: ' + ', '.join(stale))
    print(f"Markdown graph {'checked' if args.check else 'built'}: {sum(n['type']=='Concept' for n in doc['@graph'])} concepts, {len(doc['@graph'])} nodes")


if __name__ == '__main__':
    main()
