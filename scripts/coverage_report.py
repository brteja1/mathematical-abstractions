#!/usr/bin/env python3
"""Write a reproducible human-readable overview of catalog basis coverage."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def build():
    graph=json.loads((ROOT/'catalog.jsonld').read_text())['@graph']
    concepts=sorted((n for n in graph if n.get('type')=='Concept'),key=lambda n:n['shortForm'])
    lines=['# Catalog basis coverage','',
           'Generated from `catalog.jsonld` by `make coverage-report`. Counts describe recorded interfaces, not machine-checked proofs or an enumeration of every consequence.','',
           '| Concept | Operations | Defining rules | Laws | Theorems | Basis kind |',
           '| --- | ---: | ---: | ---: | ---: | --- |']
    for n in concepts:
        counts=[str(len(n[k])) for k in ['hasOperation','hasAxiom','hasLaw','hasTheorem']]
        lines.append('| '+n['shortForm']+' | '+' | '.join(counts)+' | '+n['basisKind']+' |')
    lines+=['', 'All '+str(len(concepts))+' current entries document their basis and scope. PigeonholePrinciple and StructuralInduction introduce theorem/proof schemas rather than primitive value operations; this is explicitly recorded.', '',
            'Use `ruleRole` to distinguish foundational axioms, structure constraints, and defining equations. Use `basisScope` for interface boundaries. Alternate language policies, intensional equality, IEEE payload/trap details, and formal proof artifacts require further formalization.']
    (ROOT/'COVERAGE.md').write_text('\n'.join(lines)+'\n')

if __name__=='__main__':build()
