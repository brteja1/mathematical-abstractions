#!/usr/bin/env python3
"""Validate and render the versioned LLVM IR pass obligation inventory.

The manifest records registration coverage, not implementation correctness.
Optional --llvm-root compares the complete pinned source registry to the snapshot.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from markdown_graph import ROOT, load_graph

MANIFEST = ROOT / 'data/llvm/pass_obligations_21.1.8.json'
REPORT = ROOT / 'docs/LLVM_PASS_COVERAGE.md'
MACRO = r'(?:MODULE|CGSCC|FUNCTION|LOOP|LOOPNEST)_PASS(?:_WITH_PARAMS)?'
REGISTRATION = re.compile(r'^(' + MACRO + r')\s*\(\s*"([^"\n]+)"', re.M)
INVOCATION = re.compile(r'^([A-Z][A-Z_]*PASS[A-Z_]*)\s*\(', re.M)


def parse_registry(text):
    """Read literal registrations only; reject newly introduced macro shapes."""
    unsupported = [m[1] for m in INVOCATION.finditer(text)
                   if not re.fullmatch(MACRO, m[1])]
    if unsupported:
        raise ValueError('Unsupported pass registration macros: ' + ', '.join(unsupported))
    matches = list(REGISTRATION.finditer(text))
    invocations = list(INVOCATION.finditer(text))
    if len(matches) != len(invocations):
        raise ValueError('Nonliteral or unparsed pass registration; review the parser')
    entries = [{'kind': m[1], 'name': m[2],
                'line': text.count('\n', 0, m.start()) + 1} for m in matches]
    keys = [(e['kind'], e['name']) for e in entries]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate macro/name registration')
    if not entries:
        raise ValueError('Empty pass registry')
    return entries


def validate(manifest, index, registry_text=None):
    errors = []
    if manifest.get('schemaVersion') != 1 or manifest.get('llvmVersion') != '21.1.8':
        errors.append('Unsupported manifest version')
    if manifest.get('sourcePath') != 'llvm/lib/Passes/PassRegistry.def':
        errors.append('Unexpected registry path')
    if not re.fullmatch(r'[0-9a-f]{64}', manifest.get('sourceSha256', '')):
        errors.append('Missing registry content hash')
    if index.get(manifest.get('source'), {}).get('type') != 'Source':
        errors.append('Missing direct registry Source node')
    families = manifest.get('families', {})
    entries = manifest.get('entries', [])
    if not families or not entries:
        errors.append('Empty inventory or family mapping')
    keys = [(e.get('kind'), e.get('name')) for e in entries]
    if len(keys) != len(set(keys)):
        errors.append('Duplicate inventory macro/name')
    used = set()
    for e in entries:
        family = families.get(e.get('family'))
        if family is None:
            errors.append('Unmapped pass: ' + str(e.get('name')))
            continue
        used.add(e['family'])
        expected = 'obligation-mapped' if family.get('kind') == 'transform' else family.get('kind')
        if e.get('status') != expected:
            errors.append('Invalid evidence status: ' + str(e.get('name')))
        if not re.fullmatch(MACRO, e.get('kind', '')) or not e.get('name'):
            errors.append('Invalid registration: ' + str(e))
        if not isinstance(e.get('line'), int) or e['line'] <= 0:
            errors.append('Missing source locator: ' + str(e.get('name')))
    for key, family in families.items():
        if family.get('kind') not in {'transform', 'pipeline', 'utility'}:
            errors.append('Unknown family kind: ' + key)
        if not family.get('description') or not family.get('obligations') or not family.get('evidence'):
            errors.append('Missing contract/evidence scope: ' + key)
        if not family.get('concepts'):
            errors.append('Missing concepts: ' + key)
        for ident in family.get('concepts', []):
            if index.get(ident, {}).get('type') != 'Concept':
                errors.append('Unknown concept in ' + key + ': ' + ident)
    if used != set(families):
        errors.append('Unused family mappings: ' + ', '.join(sorted(set(families) - used)))
    if registry_text is not None:
        try:
            actual = parse_registry(registry_text)
            expected = [{k: e[k] for k in ('kind', 'name', 'line')} for e in entries]
            if actual != expected:
                actual_keys = {(e['kind'], e['name']) for e in actual}
                expected_keys = set(keys)
                errors.append('Registry drift: missing mappings=' + str(sorted(actual_keys - expected_keys)) +
                              '; obsolete mappings=' + str(sorted(expected_keys - actual_keys)) +
                              '; source order/line locators must also match')
            if hashlib.sha256(registry_text.encode()).hexdigest() != manifest.get('sourceSha256'):
                errors.append('Registry content hash differs from the consulted snapshot')
        except ValueError as exc:
            errors.append(str(exc))
    return errors


def render(manifest, index):
    counts = Counter(e['status'] for e in manifest['entries'])
    lines = [
        '# LLVM 21.1.8 pass obligation inventory', '',
        'Generated from [the mapping manifest](../data/llvm/pass_obligations_21.1.8.json) with',
        '`python3 scripts/llvm_transform_coverage.py --write`. Edit the manifest to change mappings.', '',
        manifest['scope'], '', manifest['evidence'], '',
        f"Consulted {manifest['consultedOn']}; registry SHA-256 `{manifest['sourceSha256']}`.", '',
        f"The snapshot contains **{len(manifest['entries'])} registrations** in **{len(manifest['families'])} families**:", '',
        *[f'- {value} {key} entries.' for key, value in sorted(counts.items())], '',
        'Counts are registration coverage, not counts of distinct algorithms, semantic completeness or verified passes.',
        'Parameterized registrations count once; their possible options and pipeline expansions are not enumerated.', '',
        'Every transforming entry also needs [behavior refinement](../concepts/BehaviorRefinement.md),',
        '[guarded rewriting](../concepts/GuardedRewrite.md), output well-formedness and',
        '[analysis preservation](../concepts/AnalysisPreservation.md), where applicable.', '',
        '## Family contracts', '',
    ]
    for key, family in manifest['families'].items():
        lines += [f"### {family['description']}", '', f"Family `{key}`; kind `{family['kind']}`.", '']
        concepts = []
        for ident in family['concepts']:
            name = index[ident]['shortForm']
            concepts.append(f'[{name}](../concepts/{name}.md)')
        lines += [', '.join(concepts) + '.', '']
        lines += [f'- {obligation}' for obligation in family['obligations']]
        lines += ['', 'Registrations: ' + ', '.join(
            f"`{e['kind']}:{e['name']}`" for e in manifest['entries'] if e['family'] == key) + '.', '']
    lines += ['## Complete registration index', '',
              'Source: [LLVM 21.1.8 PassRegistry.def](https://github.com/llvm/llvm-project/blob/llvmorg-21.1.8/llvm/lib/Passes/PassRegistry.def).', '',
              '| Macro | Pass spelling | Family | Source line |', '| --- | --- | --- | --- |']
    lines += [f"| `{e['kind']}` | `{e['name']}` | `{e['family']}` | {e['line']} |" for e in manifest['entries']]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--llvm-root', type=Path, help='Compare against this LLVM source checkout')
    parser.add_argument('--write', action='store_true', help='Regenerate the report after validation')
    parser.add_argument('--check', action='store_true', help='Reject a stale generated report')
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text())
    index = {n['id']: n for n in load_graph()['@graph']}
    registry = ((args.llvm_root / manifest['sourcePath']).read_bytes().decode('utf-8')
                if args.llvm_root else None)
    errors = validate(manifest, index, registry)
    if errors:
        parser.exit(1, '\n'.join(errors) + '\n')
    expected = render(manifest, index)
    if args.write:
        REPORT.write_text(expected)
    if args.check and (not REPORT.exists() or REPORT.read_text() != expected):
        parser.exit(1, 'Stale LLVM pass coverage report; run with --write\n')
    print(json.dumps({'registrations': len(manifest['entries']),
                      'families': len(manifest['families']),
                      'statuses': dict(Counter(e['status'] for e in manifest['entries'])),
                      'sourceCompared': registry is not None,
                      'evidence': 'obligation mapping, not verified pass correctness'}, indent=2))


if __name__ == '__main__':
    main()
