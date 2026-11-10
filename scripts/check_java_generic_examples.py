#!/usr/bin/env python3
"""Check selected Java generic examples with installed javac/java; retain evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from markdown_graph import load_graph
from lean import catalog_slice, digest

ROOT = Path(__file__).resolve().parents[1]
# Each snippet maps a concrete rejected construct to the recorded obligation.
CASES = {
    'bound': ('urn:csabs:law/JavaParameterizedType-failed-bound-rejected',
              'class Reject { GenericExamples.Box<String> invalid; }'),
    'invariance': ('urn:csabs:axiom/JavaParameterizedType-nominal-supertype-rules',
                   'class Reject { void bad(List<Integer> x) { List<Number> y = x; } }'),
    'extends-write': ('urn:csabs:axiom/JavaWildcardCapture-wildcard-bounds',
                      'class Reject { void bad(List<? extends Number> x) { x.add(Integer.valueOf(1)); } }'),
    'capture-mismatch': ('urn:csabs:axiom/JavaWildcardCapture-fresh-nonrecursive',
                         'class Reject { void bad(List<?> x) { x.set(0, x.get(0)); } }'),
    'erasure-clash': ('urn:csabs:operation/JavaTypeErasure-erase-signature',
                      'class Reject { void same(List<String> x) {} void same(List<Integer> x) {} }'),
    'target-conflict': ('urn:csabs:law/JavaTypeInference-failed-target-no-resolution',
                        'class Reject { List<String> invalid = GenericExamples.singleton(Integer.valueOf(1)); }'),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--release', default='21', help='javac --release target, default 21')
    parser.add_argument('--output', type=Path, help='Optional JSON evidence path')
    args = parser.parse_args()
    javac, java = shutil.which('javac'), shutil.which('java')
    if not javac or not java:
        parser.error('Installed javac and java executables are required')
    source_path = ROOT / 'examples/GenericExamples.java'
    source = source_path.read_text()
    version = subprocess.run([javac, '-version'], capture_output=True, text=True, check=True, timeout=10)
    records = {}
    index = {node['id']: node for node in load_graph()['@graph']}
    for claim, _ in CASES.values():
        records.update(catalog_slice(index, claim))
    results = []
    with tempfile.TemporaryDirectory(prefix='catalog-java-generics-') as directory:
        work = Path(directory)
        for name in ('positive', *CASES):
            text = source if name == 'positive' else source + '\n' + CASES[name][1] + '\n'
            path = work / 'GenericExamples.java'
            path.write_text(text)
            command = [javac, '--release', args.release, '-Xlint:all', '-Werror', '-d', directory, str(path)]
            try:
                completed = subprocess.run(command, capture_output=True, text=True, timeout=30)
            except subprocess.TimeoutExpired:
                results.append({'case': name, 'command': command, 'ok': False, 'result': 'timeout'})
                break
            accepted = completed.returncode == 0
            tool_failure = completed.returncode < 0 or any(marker in completed.stderr.lower() for marker in (
                'an exception has occurred in the compiler', 'java.lang.stackoverflowerror',
                'java.lang.outofmemoryerror', 'fatal error',
            ))
            result = {'case': name, 'command': command, 'returncode': completed.returncode,
                      'sourceSha256': hashlib.sha256(text.encode()).hexdigest(),
                      'ok': accepted if name == 'positive' else completed.returncode > 0 and not tool_failure,
                      'stdout': completed.stdout, 'stderr': completed.stderr}
            results.append(result)
            if name == 'positive':
                if not accepted:
                    break
                run_command = [java, '-cp', directory, 'GenericExamples']
                try:
                    run = subprocess.run(run_command, capture_output=True, text=True, timeout=10)
                    result['runtime'] = {'command': run_command, 'returncode': run.returncode,
                                         'stdout': run.stdout, 'stderr': run.stderr}
                    result['ok'] = run.returncode == 0
                except subprocess.TimeoutExpired:
                    result['runtime'] = {'command': run_command, 'result': 'timeout'}
                    result['ok'] = False
                if not result['ok']:
                    break
            else:
                result['catalogId'] = CASES[name][0]
    report = {'compiler': javac, 'version': (version.stdout + version.stderr).strip(),
              'release': args.release, 'referenceProfile': 'JLS SE25, selected established generic rules',
              'source': str(source_path.relative_to(ROOT)), 'catalogRecordsSha256': digest(records),
              'scope': 'Selected compiler/runtime cases only; not full JLS SE25 conformance or a Lean proof.',
              'ok': len(results) == len(CASES) + 1 and all(r['ok'] for r in results), 'results': results}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'ok': report['ok'], 'results': [{'case': r['case'], 'ok': r['ok']} for r in results]}, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
