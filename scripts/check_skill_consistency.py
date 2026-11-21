#!/usr/bin/env python3
"""Check reviewed skill sources and a deliberately finite shared-policy encoding."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = 'ai/skill-consistency/contract.json'


def skill_sources(root):
    return {str(p.relative_to(root)) for p in (root / 'ai/skills').rglob('*.md')}


def evaluate(expr, valuation):
    """Total classical Boolean semantics for the validated finite AST."""
    if type(expr) is bool:
        return expr
    if isinstance(expr, str):
        return valuation[expr]
    op, terms = next(iter(expr.items()))
    if op == 'not':
        return not evaluate(terms, valuation)
    values = [evaluate(term, valuation) for term in terms]
    if op == 'and':
        return all(values)
    if op == 'or':
        return any(values)
    if op == 'implies':
        return not values[0] or values[1]
    return values[0] == values[1]  # iff


def validate_expr(expr, atoms):
    if type(expr) is bool:
        return
    if isinstance(expr, str) and expr in atoms:
        return
    if not isinstance(expr, dict) or len(expr) != 1:
        raise ValueError(f'invalid policy expression: {expr!r}')
    op, terms = next(iter(expr.items()))
    if op == 'not':
        validate_expr(terms, atoms)
        return
    if op not in ('and', 'or', 'implies', 'iff') or not isinstance(terms, list):
        raise ValueError(f'invalid policy operator: {op}')
    if (op in ('implies', 'iff') and len(terms) != 2) or not terms:
        raise ValueError(f'invalid arity: {op}')
    for term in terms:
        validate_expr(term, atoms)


def valuations(names):
    for bits in itertools.product((False, True), repeat=len(names)):
        yield dict(zip(names, bits))


def check_policy(contract):
    inputs, outputs = contract['inputs'], contract['outputs']
    atoms = inputs + outputs
    if (not inputs or not outputs or len(atoms) != len(set(atoms))
            or len(atoms) > 18 or not all(isinstance(n, str) for n in atoms)):
        raise ValueError('policy requires distinct named atoms, at most 18 in total')
    rules = contract['rules']
    if not rules or len({r['id'] for r in rules}) != len(rules):
        raise ValueError('policy rules must have unique IDs and be nonempty')
    for rule in rules:
        validate_expr(rule['formula'], atoms)
        if not rule['clauses'] or not set(rule['clauses']) <= set(contract['clauses']):
            raise ValueError(f"unmapped rule: {rule['id']}")
    errors, models = [], {}
    for given in valuations(inputs):
        key = tuple(given.values())
        models[key] = [out for out in valuations(outputs)
                       if all(evaluate(r['formula'], given | out) for r in rules)]
        if not models[key]:
            errors.append(f'no permitted outcome for required input {given}')
    scenarios = contract['scenarios']
    if not scenarios or len({s['id'] for s in scenarios}) != len(scenarios):
        raise ValueError('scenarios must be nonempty with unique IDs')
    for scenario in scenarios:
        given, expect = scenario['inputs'], scenario['expect']
        if (set(given) != set(inputs) or not expect or not set(expect) <= set(outputs)
                or any(type(v) is not bool for v in [*given.values(), *expect.values()])):
            raise ValueError(f"invalid scenario: {scenario['id']}")
        allow = scenario.get('allow', {})
        if not set(allow) <= set(outputs) or any(type(v) is not bool for v in allow.values()):
            raise ValueError(f"invalid permitted outcome: {scenario['id']}")
        outcomes = models[tuple(given[n] for n in inputs)]
        if not outcomes or any(any(out[n] != value for n, value in expect.items())
                               for out in outcomes):
            errors.append(f"scenario not entailed: {scenario['id']}")
        if allow and not any(all(out[n] == v for n, v in allow.items()) for out in outcomes):
            errors.append(f"required outcome unavailable: {scenario['id']}")
    return errors, {'inputContexts': len(models),
                    'valuations': 2 ** len(atoms),
                    'satisfyingValuations': sum(map(len, models.values())),
                    'scenarios': len(scenarios)}


def check_repository(root=ROOT, contract=None):
    root = Path(root).resolve()
    if contract is None:
        contract = json.loads((root / CONTRACT).read_text())
    errors = []
    actual = {p.parent.name for p in (root / 'ai/skills').glob('*/SKILL.md')}
    if actual != set(contract['skills']):
        errors.append('skill inventory differs from reviewed contract')
    sources = skill_sources(root) | {'AGENTS.md'}
    if sources != set(contract['sourceHashes']):
        errors.append('normative source inventory differs from reviewed contract')
    texts = {}
    for relative in sources:
        path = root / relative
        if not path.is_file():
            errors.append(f'missing source: {relative}')
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != contract['sourceHashes'].get(relative):
            errors.append(f'review stale: {relative}')
        texts[relative] = data.decode()
        if path.name == 'SKILL.md':
            header = texts[relative].split('---', 2)
            if len(header) < 3 or not re.search(r'^name: ' + re.escape(path.parent.name) + r'$', header[1], re.M) or not re.search(r'^description: .+', header[1], re.M):
                errors.append(f'invalid skill frontmatter: {relative}')
        prose = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', texts[relative], flags=re.M | re.S)
        for destination in re.findall(r'\[[^\]\n]+\]\(([^)\s]+)\)', prose):
            dest = urlsplit(destination.strip('<>'))
            if dest.scheme or not dest.path:
                continue
            target = (path.parent / unquote(dest.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'broken local link: {relative} -> {destination}')
    for cid, clause in contract['clauses'].items():
        if clause['quote'] not in texts.get(clause['source'], ''):
            errors.append(f'clause anchor missing: {cid}')
    connected = set()
    for handoff in contract['handoffs']:
        if (handoff['from'] not in actual or handoff['to'] not in actual
                or not handoff['artifact'] or handoff['clause'] not in contract['clauses']):
            errors.append(f'invalid handoff: {handoff}')
        connected.update((handoff['from'], handoff['to']))
    if connected != actual:
        errors.append('skill missing from reviewed handoff graph')
    policy_errors, summary = check_policy(contract)
    errors.extend(policy_errors)
    return {'ok': not errors, 'errors': errors, 'skills': len(actual),
            'sourceFiles': len(sources), 'handoffs': len(contract['handoffs']), **summary}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        result = check_repository(args.root)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result = {'ok': False, 'errors': [f'invalid consistency contract: {exc}']}
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
