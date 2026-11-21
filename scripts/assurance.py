#!/usr/bin/env python3
"""Check a task-local obligation ledger; execute checks only with `run`."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

CATALOG = Path(__file__).resolve().parents[1]
KINDS = {'test', 'bounded', 'review', 'proof'}
MAPPING = {'carrier', 'equality', 'operations', 'assumptions', 'scope', 'limitations'}
IGNORED = {'.git', '.assurance', '__pycache__', '.venv', '.lake'}
SYMBOL = re.compile(r'[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*\Z')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(root, path):
    if not isinstance(path, str) or not path or Path(path).is_absolute():
        raise ValueError('Expected a relative project path')
    result = (root / path).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('Path escapes project: ' + path)
    return result


def catalog_record(ident):
    result = subprocess.run([sys.executable, str(CATALOG / 'scripts/agent_query.py'),
                             'node', ident, '--view', 'full'], capture_output=True, text=True)
    if result.returncode:
        raise ValueError('Catalog retrieval failed for ' + ident + ': ' + result.stderr.strip())
    record = json.loads(result.stdout)
    if record['id'] != ident:
        raise ValueError('Use a stable catalog ID: ' + ident)
    return record


def indexed(records, label):
    if not isinstance(records, list) or any(not isinstance(r, dict) for r in records):
        raise ValueError(label + ' must be a list of records')
    result = {}
    for record in records:
        ident = record.get('id')
        if not isinstance(ident, str) or not ident or ident in result:
            raise ValueError('Missing or duplicate ' + label + ' ID')
        result[ident] = record
    return result


def text_fields(record, fields, label):
    if not isinstance(record, dict):
        raise ValueError(label + ': expected a record')
    for key in fields:
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError(label + ': nonempty ' + key + ' required')


def refs(values, index, label, nonempty=False):
    if (not isinstance(values, list) or (nonempty and not values)
            or any(not isinstance(v, str) or v not in index for v in values)
            or len(values) != len(set(values))):
        raise ValueError('Invalid ' + label + ' references')


def validate(doc, root):
    """Validate traceability before checking evidence; never execute task commands."""
    if not isinstance(doc, dict) or doc.get('schemaVersion') != 1:
        raise ValueError('Expected assurance schemaVersion 1')
    text_fields(doc, ['name'], 'ledger')
    if type(doc.get('dependencyGraphComplete')) is not bool:
        raise ValueError('dependencyGraphComplete must be Boolean')
    if not isinstance(doc.get('decisions'), list):
        raise ValueError('decisions must be a list; unresolved decisions block admission')
    artifacts = indexed(doc.get('artifacts'), 'artifact')
    requirements = indexed(doc.get('requirements'), 'requirement')
    obligations = indexed(doc.get('obligations'), 'obligation')
    if not artifacts or not requirements or not obligations:
        raise ValueError('Artifacts, requirements and obligations must be nonempty')
    paths = set()
    for item in artifacts.values():
        text_fields(item, ['path', 'role'], item['id'])
        path = local(root, item['path'])
        if path in paths or any(p in IGNORED for p in Path(item['path']).parts):
            raise ValueError('Duplicate or ignored artifact path: ' + item['path'])
        if not path.is_file():
            raise ValueError('Missing artifact: ' + item['path'])
        paths.add(path)
        if item['role'] not in {'requirement', 'specification', 'implementation', 'checker',
                                 'toolchain', 'environment', 'release'}:
            raise ValueError('Unknown artifact role: ' + item['role'])
    for item in requirements.values():
        text_fields(item, ['statement', 'origin', 'source', 'locator'], item['id'])
        if item['origin'] not in {'human', 'external', 'derived', 'proposal'}:
            raise ValueError('Unknown requirement origin')
        refs([item['source']], artifacts, 'requirement source')
        review = item.get('validation', {})
        text_fields(review, ['reviewer', 'rationale', 'status'], item['id'] + ' validation')
        if review['status'] not in {'pending', 'accepted', 'rejected'}:
            raise ValueError('Unknown requirement validation status')
    used_requirements, used_artifacts = set(), set()
    for item in obligations.values():
        ident = item['id']
        text_fields(item, ['statement'], ident)
        refs(item.get('requirements'), requirements, 'obligation requirement', True)
        refs(item.get('artifacts'), artifacts, 'obligation artifact', True)
        refs(item.get('dependsOn'), obligations, 'obligation dependency')
        used_requirements.update(item['requirements'])
        used_artifacts.update(item['artifacts'])
        kinds = item.get('evidenceRequired')
        refs(kinds, KINDS, 'evidence kind', True)
        if not isinstance(item.get('assumptions'), list) or any(
                not isinstance(a, str) or not a.strip() for a in item['assumptions']):
            raise ValueError(ident + ': assumptions must be an explicit list')
        mappings = item.get('catalog')
        if not isinstance(mappings, list) or not mappings:
            raise ValueError(ident + ': catalog mappings required')
        for mapping in mappings:
            text_fields(mapping, ['id'], ident + ' catalog')
            if not mapping['id'].startswith('urn:csabs:'):
                raise ValueError('Use stable catalog IDs')
            text_fields(mapping.get('mapping', {}), MAPPING, ident + ' mapping')
        checks = indexed(item.get('checks'), ident + ' check')
        if not set(kinds) <= {c.get('kind') for c in checks.values()}:
            raise ValueError(ident + ': missing required check kind')
        for check in checks.values():
            text_fields(check, ['kind', 'scope'], ident + ' check')
            if check['kind'] not in KINDS:
                raise ValueError('Unknown evidence kind')
            if check['kind'] == 'proof':
                if check.get('profile') != 'lean-source-v1':
                    raise ValueError('Proof requires supported lean-source-v1 profile')
                text_fields(check, ['source', 'symbol', 'expectedType', 'typeReviewer'], ident)
                if check['source'] not in item['artifacts'] or not SYMBOL.fullmatch(check['symbol']):
                    raise ValueError('Proof source must be an obligation artifact; symbol must be qualified')
                if '\n' in check['expectedType'] or '\r' in check['expectedType']:
                    raise ValueError('expectedType must be a single Lean term line')
            else:
                argv = check.get('argv')
                if not isinstance(argv, list) or not argv or any(
                        not isinstance(a, str) or not a for a in argv):
                    raise ValueError('Checks require a nonempty argv list')
                # A successful review command checks a receipt, not reviewer identity.
                if check['kind'] == 'review':
                    text_fields(check, ['reviewer', 'rationale'], ident + ' review')
    if used_requirements != set(requirements):
        raise ValueError('Orphan requirements: ' + ', '.join(sorted(set(requirements) - used_requirements)))
    normative = {a['id'] for a in artifacts.values()
                 if a['role'] in {'requirement', 'specification', 'implementation', 'release'}}
    if not normative <= used_artifacts:
        raise ValueError('Unmapped normative artifacts: ' + ', '.join(sorted(normative - used_artifacts)))
    for ident in obligations:
        closure(obligations, ident)
    return artifacts, requirements, obligations


def closure(obligations, ident, active=None):
    active = set() if active is None else active
    if ident in active:
        raise ValueError('Obligation dependency cycle at ' + ident)
    result = {ident}
    for dep in obligations[ident]['dependsOn']:
        result.update(closure(obligations, dep, active | {ident}))
    return result


def inventory(root, ledger):
    result = []
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED)
        for name in dirs + files:
            path = Path(directory) / name
            if path == ledger:
                continue
            relative = path.relative_to(root)
            if path.is_symlink():
                raise ValueError('Project inventory cannot contain symlinks: ' + str(relative))
            if path.is_file():
                result.append(str(relative))
    return sorted(result)


def snapshot(doc, root, ledger, ident, retrieve=None):
    retrieve = catalog_record if retrieve is None else retrieve
    artifacts, requirements, obligations = validate(doc, root)
    selected = closure(obligations, ident) if doc['dependencyGraphComplete'] else set(obligations)
    needed = {a for i in selected for a in obligations[i]['artifacts']}
    needed.update(r['source'] for r in requirements.values())
    needed.update(a['id'] for a in artifacts.values() if a['role'] in {'toolchain', 'environment'})
    # Unmapped helper/configuration files also invalidate conservatively.
    mapped_paths = {a['path'] for a in artifacts.values()}
    files = inventory(root, ledger)
    hashes = {a: file_hash(local(root, artifacts[a]['path'])) for a in sorted(needed)}
    extra = {p: file_hash(local(root, p)) for p in files if p not in mapped_paths}
    records = {}
    for i in selected:
        for mapping in obligations[i]['catalog']:
            key = mapping['id']
            if key not in records:
                records[key] = retrieve(key)
    # Premises used by a claim must be listed explicitly as mappings; no inheritance.
    for key, record in records.items():
        missing = set(record.get('dependsOn', [])) - records.keys()
        if missing:
            raise ValueError('Map required premises for ' + key + ': ' + ', '.join(sorted(missing)))
    check = {'name': doc['name'], 'dependencyGraphComplete': doc['dependencyGraphComplete'],
             'decisions': doc['decisions'], 'requirements': requirements,
             'obligations': {i: obligations[i] for i in sorted(selected)},
             'artifacts': {a: artifacts[a] for a in sorted(needed)}}
    return {'contract': digest(check), 'artifacts': hashes, 'inventory': files,
            'unmappedInputs': extra, 'catalog': {k: digest(v) for k, v in records.items()},
            'gate': file_hash(Path(__file__))}


def process(argv, cwd, timeout):
    try:
        result = subprocess.run(argv, cwd=cwd, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=timeout)
        return result.returncode, result.stdout
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout or b''
        return 124, (output.decode(errors='replace') if isinstance(output, bytes) else output) + '\nTIMEOUT\n'


def executable(argv, root):
    found = shutil.which(argv[0], path=None)
    if '/' in argv[0]:
        found = str((root / argv[0]).resolve())
    if not found or not Path(found).is_file():
        raise ValueError('Missing executable: ' + argv[0])
    return {'path': str(Path(found).resolve()), 'sha256': file_hash(Path(found))}


def lean_context():
    # Reuse the pinned project's installed-package and local-edit audit.
    import lean
    lean.check_dependencies()
    paths = ['lean/lean-toolchain', 'lean/lake-manifest.json', 'lean/lakefile.toml']
    paths += [str(p.relative_to(CATALOG)) for p in sorted((CATALOG / 'lean/Catalog').rglob('*.lean'))]
    context = {p: file_hash(CATALOG / p) for p in paths}
    code, version = process(['lake', 'env', 'lean', '--version'], CATALOG / 'lean', 30)
    pin = (CATALOG / 'lean/lean-toolchain').read_text().strip().split(':v')[-1]
    if code or 'version ' + pin + ',' not in version:
        raise ValueError('Running Lean version differs from the pinned toolchain')
    code, binary = process(['lake', 'env', 'which', 'lean'], CATALOG / 'lean', 30)
    if code:
        raise ValueError('Cannot resolve pinned Lean executable')
    context['leanExecutable'] = file_hash(Path(binary.strip()))
    context['version'] = version.strip()
    return context


def run_check(doc, root, ledger, ident, check_id, timeout=120):
    artifacts, _, obligations = validate(doc, root)
    check = indexed(obligations[ident]['checks'], 'check')[check_id]
    before = snapshot(doc, root, ledger, ident)
    context = lean_context() if check['kind'] == 'proof' else None
    argv = ['lake', 'env', 'lean'] if context is not None else check['argv']
    binary = executable(argv, CATALOG / 'lean' if context is not None else root)
    if context is None:
        code, output = process(argv, root, timeout)
    else:
        code, output = process(['lake', 'build', 'Catalog.Audit'], CATALOG / 'lean', timeout)
        if code == 0:
            source = local(root, artifacts[check['source']]['path']).read_text()
            wrapper = ('import Catalog.Audit\n' + source + '\nset_option warningAsError true\n'
                       + 'example : (' + check['expectedType'] + ') := @' + check['symbol'] + '\n'
                       + '#catalog_witness ' + check['symbol'] + '\n')
            with tempfile.TemporaryDirectory(prefix='assurance-lean-') as temp:
                target = Path(temp) / 'Check.lean'
                target.write_text(wrapper)
                code, compiled = process(['lake', 'env', 'lean', '-DwarningAsError=true', str(target)],
                                         CATALOG / 'lean', timeout)
                output += compiled
            marker = r'^CATALOG_WITNESS ' + re.escape(check['symbol']) + r' \| *(.*)$'
            match = re.search(marker, output, re.MULTILINE)
            if code == 0 and (not match or not set(filter(None, match[1].strip().split(',')))
                              <= {'propext', 'Quot.sound', 'Classical.choice'}):
                code, output = 1, output + '\nMissing or invalid transitive axiom audit\n'
    after = snapshot(json.loads(ledger.read_text()), root, ledger, ident)
    if before != after or (context is not None and context != lean_context()):
        code, output = 1, output + '\nInputs changed during verification\n'
    report = {'schemaVersion': 1, 'obligation': ident, 'check': check_id, 'kind': check['kind'],
              'scope': check['scope'], 'inputs': before, 'executable': binary,
              'leanContext': context, 'exitCode': code, 'output': output,
              'checkedAt': datetime.now(timezone.utc).isoformat()}
    destination = root / '.assurance' / (digest([ident, check_id]) + '.json')
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


def assess(doc, root, ledger):
    _, requirements, obligations = validate(doc, root)
    blockers = []
    if doc['decisions']:
        blockers.append('Unresolved decisions')
    blockers += ['Requirement validation pending/rejected: ' + r['id'] for r in requirements.values()
                 if r['validation']['status'] != 'accepted']
    rows = []
    for ident, obligation in obligations.items():
        current = snapshot(doc, root, ledger, ident)
        for check in obligation['checks']:
            path = root / '.assurance' / (digest([ident, check['id']]) + '.json')
            status = 'missing'
            if path.exists():
                report = json.loads(path.read_text())
                if not isinstance(report, dict):
                    raise ValueError('Evidence report must be a record: ' + str(path))
                expected_binary = executable(['lake'] if check['kind'] == 'proof' else check['argv'], root)
                if (report.get('inputs') != current or report.get('executable') != expected_binary
                        or report.get('obligation') != ident or report.get('check') != check['id']
                        or report.get('kind') != check['kind']
                        or report.get('leanContext') != (lean_context() if check['kind'] == 'proof' else None)):
                    status = 'stale'
                else:
                    status = 'passed' if type(report.get('exitCode')) is int and report['exitCode'] == 0 else 'failed'
            rows.append({'obligation': ident, 'check': check['id'], 'kind': check['kind'],
                         'scope': check['scope'], 'status': status})
            if status != 'passed':
                blockers.append(ident + '/' + check['id'] + ': ' + status)
    return {'admitted': not blockers, 'blockers': blockers, 'checks': rows,
            'interpretation': 'Local evidence admission only. Mapping adequacy, reviewer identity, '
                              'check soundness and execution-platform assumptions require independent review. '
                              'Reports are not authenticated certificates.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('check', 'impact', 'run'):
        p = sub.add_parser(name)
        p.add_argument('ledger', type=Path)
        if name == 'run':
            p.add_argument('obligation')
            p.add_argument('check_id')
            p.add_argument('--timeout', type=int, default=120)
    sub.add_parser('catalog-fingerprint').add_argument('id')
    args = parser.parse_args()
    try:
        if args.command == 'catalog-fingerprint':
            record = catalog_record(args.id)
            result = {'id': record['id'], 'digest': digest(record), 'dependsOn': record.get('dependsOn', [])}
            code = 0
        else:
            ledger = args.ledger.resolve()
            doc = json.loads(ledger.read_text())
            if args.command == 'run':
                if args.timeout <= 0:
                    raise ValueError('timeout must be positive')
                result = run_check(doc, ledger.parent, ledger, args.obligation, args.check_id, args.timeout)
                code = 0 if result['exitCode'] == 0 else 1
            else:
                result = assess(doc, ledger.parent, ledger)
                code = 0 if result['admitted'] else 1
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({'admitted': False, 'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
