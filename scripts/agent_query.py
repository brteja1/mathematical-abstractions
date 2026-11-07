#!/usr/bin/env python3
"""Bounded JSON retrieval for proof planning and software test design, offline."""
import argparse
import json
from collections import deque
from markdown_graph import load_graph, SECTIONS, RELATIONS


def resolve(index, query):
    if query in index:
        return query
    matches = [n['id'] for n in index.values() if n.get('shortForm') == query]
    if len(matches) != 1:
        raise ValueError('Unknown or ambiguous ID: ' + query)
    return matches[0]


def traverse(index, seed, predicates, depth=1, limit=40, incoming=False):
    if depth < 0 or not 1 <= limit <= 1000:
        raise ValueError('Depth must be nonnegative; limit must be between 1 and 1000')
    seen = {seed}
    queue = deque([(seed, 0)])
    edges = []
    truncated = False
    while queue:
        ident, level = queue.popleft()
        if level >= depth:
            continue
        candidates = []
        for predicate in predicates:
            values = index[ident].get(predicate, [])
            if isinstance(values, str):
                values = [values]
            candidates.extend((ident, predicate, ref) for ref in values if ref in index)
            if incoming:
                candidates.extend((n['id'], predicate, ident) for n in index.values()
                                  if ident in ([n[predicate]] if isinstance(n.get(predicate), str) else n.get(predicate, [])))
        for source, predicate, target in sorted(set(candidates)):
            other = target if source == ident else source
            if other not in seen:
                if len(seen) >= limit:
                    truncated = True
                    continue
                seen.add(other)
                queue.append((other, level + 1))
            edge = {'source': source, 'predicate': predicate, 'target': target}
            if edge not in edges:
                edges.append(edge)
    return {'nodes': [index[ident] for ident in sorted(seen)], 'edges': edges,
            'truncated': truncated, 'depth': depth, 'limit': limit}


def dossier(index, seed, purpose, limit):
    predicates = list(SECTIONS) + ['requiresConcept', 'dependsOn', 'source']
    result = traverse(index, seed, predicates, depth=len(index), limit=limit)
    result['purpose'] = purpose
    result['concept'] = seed
    result['interpretation'] = 'Recorded prerequisites and derivation premises only. Truncation or missing catalog facts requires further retrieval; this is not an executable proof or a test oracle.'
    if purpose == 'proof':
        result['agentInstructions'] = [
            'Choose Lean or Coq and pin its version and library revision before writing executable syntax.',
            'Match carriers, equality, totality and conventions to the target library; check every assumption.',
            'Treat formalStatement as informal Unicode. Locate or prove each needed library lemma.',
            'Do not inherit claims automatically from specialization or prerequisites.',
            'Compile the resulting theorem with the chosen assistant; report unverified obligations and additional axioms.'
        ]
    else:
        result['agentInstructions'] = [
            'Map each abstract operation to the software API and document representation, equality and numeric semantics.',
            'Derive generators from carrier restrictions and preconditions; cover empty, singleton and boundary cases where allowed.',
            'Turn applicable equations into properties and model stateful operation sequences when needed.',
            'Test invalid inputs only against an explicit API error contract; do not evaluate undefined abstract operations.',
            'Separate exact mathematical laws from overflow, rounding, concurrency and nondeterminism conventions.',
            'Run properties against the implementation and report counterexamples. Passing tests do not establish a proof.'
        ]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    node = sub.add_parser('node'); node.add_argument('id')
    neighbors = sub.add_parser('neighbors'); neighbors.add_argument('id')
    neighbors.add_argument('--depth', type=int, default=1)
    neighbors.add_argument('--limit', type=int, default=40)
    neighbors.add_argument('--incoming', action='store_true')
    neighbors.add_argument('--relations', nargs='+', choices=list(RELATIONS)+['dependsOn', 'source']+list(SECTIONS), default=list(RELATIONS))
    task = sub.add_parser('dossier'); task.add_argument('id')
    task.add_argument('--purpose', choices=['proof', 'tests'], required=True)
    task.add_argument('--limit', type=int, default=80)
    args = parser.parse_args()
    try:
        doc = load_graph()
        index = {n['id']: n for n in doc['@graph']}
        seed = resolve(index, args.id)
        if args.command == 'node':
            result = index[seed]
        elif args.command == 'neighbors':
            result = traverse(index, seed, args.relations, args.depth, args.limit, args.incoming)
        else:
            if index[seed]['type'] != 'Concept':
                raise ValueError('A dossier requires a Concept ID or shortForm')
            result = dossier(index, seed, args.purpose, args.limit)
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
