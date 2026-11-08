#!/usr/bin/env python3
"""Query ONTFS/SPARQL for catalog coverage and render its Markdown report."""
import argparse
import json
from pathlib import Path

from markdown_graph import ROOT
from ontology import CA, load_projection

RELATIONS = {'operations': 'hasOperation', 'axioms': 'hasAxiom',
             'laws': 'hasLaw', 'theorems': 'hasTheorem',
             'dependencies': 'requiresConcept', 'sources': 'source'}
PREFIX = 'PREFIX ca: <' + CA + '>\n'


def coverage(directory=ROOT):
    store = load_projection(directory)
    entries = {}
    rows = store.graph.query_graph(PREFIX + '''
        SELECT ?concept ?shortForm ?status ?basis ?kind ?scope WHERE {
          ?concept a ca:Concept ; ca:shortForm ?shortForm .
          OPTIONAL { ?concept ca:coverageStatus ?status }
          OPTIONAL { ?concept ca:axiomBasis ?basis }
          OPTIONAL { ?concept ca:basisKind ?kind }
          OPTIONAL { ?concept ca:basisScope ?scope }
        } ORDER BY ?shortForm''')
    for row in rows:
        values = row.asdict()
        entries[str(row.concept)] = {
            'shortForm': str(row.shortForm),
            'coverageStatus': str(values.get('status', 'unspecified')),
            'documentedAxiomBasis': bool(str(values.get('basis', ''))),
            'basisKind': str(values.get('kind', '')),
            'basisScope': str(values.get('scope', '')),
            **dict.fromkeys(RELATIONS, 0)}
    # Count each edge family separately, avoiding cross-products between claims.
    predicates = ' '.join('ca:' + name for name in RELATIONS.values())
    sections = {CA + name: section for section, name in RELATIONS.items()}
    rows = store.graph.query_graph(PREFIX + '''
        SELECT ?concept ?relation (COUNT(DISTINCT ?item) AS ?count) WHERE {
          VALUES ?relation { ''' + predicates + ''' }
          ?concept a ca:Concept ; ?relation ?item .
        } GROUP BY ?concept ?relation''')
    for row in rows:
        entries[str(row.concept)][sections[str(row.relation)]] = int(row.asdict()['count'])
    ordered = sorted(entries.values(), key=lambda n: n['shortForm'])
    missing = [n['shortForm'] for n in ordered if not n['documentedAxiomBasis']]
    return {'concepts': len(ordered),
            'withDocumentedAxiomBasis': len(ordered) - len(missing),
            'withoutDocumentedAxiomBasis': missing,
            'conceptsWithoutRecordedAxioms': [n['shortForm'] for n in ordered if not n['axioms']],
            'entries': ordered,
            'interpretation': 'Counts describe recorded interfaces, not mathematical completeness or machine-checked proofs.'}


def render(report):
    lines = ['# Catalog basis coverage', '',
             'Generated from the ONTFS projection with SPARQL by `make coverage-report`. Counts describe recorded interfaces, not machine-checked proofs or an enumeration of every consequence.', '',
             '| Concept | Operations | Defining rules | Laws | Theorems | Basis kind |',
             '| --- | ---: | ---: | ---: | ---: | --- |']
    for n in report['entries']:
        counts = [str(n[key]) for key in ['operations', 'axioms', 'laws', 'theorems']]
        lines.append('| ' + n['shortForm'] + ' | ' + ' | '.join(counts) + ' | ' + n['basisKind'] + ' |')
    lines += ['', f"{report['withDocumentedAxiomBasis']} of {report['concepts']} current entries document their basis. "
              'PigeonholePrinciple and StructuralInduction introduce theorem/proof schemas rather than primitive value operations; this is explicitly recorded.', '',
              'Use `ruleRole` to distinguish foundational axioms, structure constraints, and defining equations. Use `basisScope` for interface boundaries. Alternate language policies, intensional equality, IEEE payload/trap details, and formal proof artifacts require further formalization.']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true', help='Print queried coverage as JSON')
    parser.add_argument('--check', action='store_true', help='Reject a stale COVERAGE.md without writing it')
    args = parser.parse_args()
    try:
        report = coverage(args.directory)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            text = render(report)
            target = ROOT / 'COVERAGE.md'
            if args.check:
                if not target.is_file() or target.read_text() != text:
                    raise ValueError('Stale COVERAGE.md; run make coverage-report')
            else:
                target.write_text(text)
    except (RuntimeError, ValueError, ImportError) as exc:
        parser.error(str(exc))


if __name__ == '__main__':
    main()
