#!/usr/bin/env python3
"""Bounded, dependency-free retrieval of catalog nodes; optional RDF validation."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINKS = {'category','kind','specializationOf','relatedConcept','hasOperation','hasAxiom','hasLaw','hasTheorem','appliesTo','source','concept','requiresConcept','dependsOn'}
SECTIONS = {'operations':'hasOperation','axioms':'hasAxiom','laws':'hasLaw','theorems':'hasTheorem','dependencies':'requiresConcept','sources':'source'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file',type=Path,default=None)
    sub=parser.add_subparsers(dest='command',required=True)
    ls=sub.add_parser('list'); ls.add_argument('--category'); ls.add_argument('--search',default='')
    get=sub.add_parser('get'); get.add_argument('id'); get.add_argument('--sections',nargs='*',choices=list(SECTIONS),default=[])
    sub.add_parser('coverage', help='Report recorded claims and whether an axiom basis is documented')
    check=sub.add_parser('check'); check.add_argument('--rdf',action='store_true')
    args=parser.parse_args()
    from markdown_graph import load_graph
    doc=json.loads(args.file.read_text()) if args.file else load_graph(); graph=doc['@graph']; index={n['id']:n for n in graph}
    concepts=[n for n in graph if n.get('type')=='Concept']
    if args.command=='list':
        result=[{k:n[k] for k in ['shortForm','fullName','category','kind']} for n in concepts
                if (not args.category or any(c.endswith('/'+args.category) for c in n['category']))
                and args.search.casefold() in (json.dumps(n,ensure_ascii=False)).casefold()]
    elif args.command=='coverage':
        result={'concepts':len(concepts),
                'withDocumentedAxiomBasis':sum(bool(n.get('axiomBasis')) for n in concepts),
                'withoutDocumentedAxiomBasis':[n['shortForm'] for n in concepts if not n.get('axiomBasis')],
                'conceptsWithoutRecordedAxioms':[n['shortForm'] for n in concepts if not n.get('hasAxiom')],
                'entries':[{ 'shortForm':n['shortForm'], 'coverageStatus':n.get('coverageStatus','unspecified'),
                             'documentedAxiomBasis':bool(n.get('axiomBasis')),
                             **{section:len(n.get(link,[])) for section,link in SECTIONS.items()}}
                            for n in sorted(concepts,key=lambda n:n['shortForm'])],
                'interpretation':'Counts describe recorded material, not mathematical completeness. Axioms depend on a chosen presentation; a concept may be defined from others without introducing new axioms.'}
    elif args.command=='get':
        matches=[n for n in concepts if n['shortForm']==args.id or n['id']==args.id]
        if not matches: parser.error('Unknown concept: '+args.id)
        n=matches[0]
        result={k:v for k,v in n.items() if k not in set(SECTIONS.values())}
        for section in args.sections:
            result[section]=[index[x] for x in n.get(SECTIONS[section],[])]
    else:
        from validate_graph import validate
        errors=validate(doc)
        result={'concepts':len(concepts),'nodes':len(graph),'errors':errors}
        if args.rdf:
            try:
                from rdflib import Graph
            except ImportError:parser.error('--rdf requires rdflib')
            rdf=Graph().parse(data=json.dumps(doc),format='json-ld')
            vocab=doc['@context']['@vocab']
            count=list(rdf.query('SELECT (COUNT(?x) AS ?n) WHERE {?x a <'+vocab+'Concept>}'))[0][0]
            result['rdfTriples']=len(rdf); result['rdfConcepts']=int(count)
            if int(count)!=len(concepts):errors.append('RDF concept count mismatch')
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return bool(errors)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
