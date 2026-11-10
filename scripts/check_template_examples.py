#!/usr/bin/env python3
"""Compile catalog-mapped C++20 examples, retaining scoped acceptance evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

from markdown_graph import load_graph
from lean import catalog_slice, digest

ROOT = Path(__file__).resolve().parents[1]
NEGATIVE_CASES = (
    'WRONG_KIND', 'AMBIGUITY', 'HARD_ERROR', 'CONSTRAINT_BODY',
    'ATOMIC_IDENTITY', 'PACK_LENGTH', 'EMPTY_FOLD', 'OVERFLOW',
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compiler', default='g++', help='C++ compiler executable')
    parser.add_argument('--output', type=Path, help='Optional JSON evidence path')
    args = parser.parse_args()
    compiler = shutil.which(args.compiler)
    if compiler is None:
        parser.error(f'Compiler not found: {args.compiler}')
    source = ROOT / 'examples/template_metaprogramming.cpp'
    version = subprocess.run([compiler, '--version'], text=True, capture_output=True, check=True, timeout=10)
    claim_ids = sorted(set(re.findall(r'urn:csabs:(?:axiom|law|theorem)/[A-Za-z0-9-]+', source.read_text())))
    index = {node['id']: node for node in load_graph()['@graph']}
    records = {}
    for claim_id in claim_ids:
        records.update(catalog_slice(index, claim_id))
    results = []
    for name in ('POSITIVE', *NEGATIVE_CASES):
        command = [compiler, '-std=c++20', '-pedantic-errors', '-Wall', '-Wextra', '-fsyntax-only']
        if name != 'POSITIVE':
            command.append('-DTMP_FAIL_' + name)
        command.append(str(source))
        try:
            completed = subprocess.run(command, text=True, capture_output=True, timeout=30)
        except subprocess.TimeoutExpired:
            results.append({'case': name, 'command': command, 'ok': False, 'result': 'timeout'})
            continue
        accepted = completed.returncode == 0
        diagnostic = completed.stderr.lower()
        tool_failure = completed.returncode < 0 or any(marker in diagnostic for marker in (
            'internal compiler error', 'please submit a bug report',
            'frontend command failed', 'template instantiation depth exceeds',
            'constexpr evaluation operation count exceeds', 'constexpr evaluation depth exceeds',
        ))
        results.append({'case': name, 'command': command, 'returncode': completed.returncode,
                        'ok': accepted if name == 'POSITIVE' else completed.returncode > 0 and not tool_failure,
                        'toolFailure': tool_failure,
                        'stdout': completed.stdout, 'stderr': completed.stderr})
        # A rejected baseline can make every negative look successful for an
        # unrelated reason; do not continue with that misleading experiment.
        if name == 'POSITIVE' and not accepted:
            break
    report = {'compiler': compiler, 'version': version.stdout.strip(), 'standard': 'c++20',
              'source': str(source.relative_to(ROOT)),
              'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'catalogClaimIds': claim_ids, 'catalogRecordsSha256': digest(records),
              'catalogRetrieval': 'authoritative Markdown via markdown_graph; selected interfaces, premises and sources',
              'scope': 'Selected examples only; compiler acceptance is not universal conformance or a Lean proof.',
              'ok': len(results) == 1 + len(NEGATIVE_CASES) and all(r['ok'] for r in results),
              'results': results}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'ok': report['ok'], 'cases': len(results),
                      'results': [{'case': r['case'], 'ok': r['ok']} for r in results]}, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
