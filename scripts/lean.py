#!/usr/bin/env python3
"""Check catalog bindings, compile Lean witnesses, and report fresh evidence."""
import argparse
import copy
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

from markdown_graph import ROOT, load_graph

LEAN = ROOT / 'lean'
MANIFEST = LEAN / 'bindings.json'
REPORT = LEAN / 'verification.json'
SYMBOL = re.compile(r'[A-Za-z_][A-Za-z_0-9]*(?:\.[A-Za-z_][A-Za-z_0-9]*)*\Z')
ALLOWED_AXIOMS = {'propext', 'Quot.sound', 'Classical.choice'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


def catalog_slice(index, ident):
    """Freeze explicit interfaces and premises; never infer axiom inheritance."""
    pending, seen = [ident], set()
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        node = index[current]
        for key in ('dependsOn', 'appliesTo', 'hasOperation', 'hasAxiom', 'source'):
            pending.extend(node.get(key, []))
    return {key: index[key] for key in sorted(seen)}


def catalog_hash(index, ident):
    return digest(catalog_slice(index, ident))


def refresh_bindings(manifest, index, identifiers=()):
    """Refresh reviewed hashes; reject unrelated metadata errors before writing."""
    candidate = copy.deepcopy(manifest)
    bindings = candidate['bindings']
    selected = set()
    for ident in identifiers:
        if ident not in index:
            ident = next((i for i, n in index.items() if n.get('shortForm') == ident), ident)
        if ident not in bindings or ident not in index:
            raise ValueError('No Lean binding registered for ' + ident)
        selected.add(ident)
    if not identifiers:
        selected = set(bindings)
    changes = []
    # Validate all metadata against current hashes, so unselected stale hashes
    # do not prevent a targeted refresh. No other errors are suppressed.
    for ident, binding in bindings.items():
        if ident not in index:
            continue
        current = catalog_hash(index, ident)
        if ident in selected and binding.get('catalogHash') != current:
            changes.append({'id': ident, 'oldHash': binding.get('catalogHash'),
                            'catalogHash': current})
        binding['catalogHash'] = current
    errors = validate(candidate, index)
    if errors:
        raise ValueError('\n'.join(errors))
    result = copy.deepcopy(manifest)
    for change in changes:
        result['bindings'][change['id']]['catalogHash'] = change['catalogHash']
    return result, changes


def validate(manifest, index):
    errors = []
    from lean_formulations import formulation_errors
    errors.extend(formulation_errors(manifest, index, ROOT))
    if manifest.get('schemaVersion') != 1:
        errors.append('Unsupported Lean binding schema version')
    if manifest.get('toolchain') != (LEAN / 'lean-toolchain').read_text().strip():
        errors.append('Toolchain differs from binding manifest')
    lock = json.loads((LEAN / 'lake-manifest.json').read_text())
    packages = {p['name']: p for p in lock['packages']}
    if manifest.get('mathlibRevision') != packages['mathlib']['rev']:
        errors.append('Mathlib revision differs from Lake lock')
    config = (LEAN / 'lakefile.toml').read_text()
    if packages['mathlib']['rev'] not in config:
        errors.append('lakefile.toml must pin Mathlib to the locked commit')
    bindings = manifest.get('bindings', {})
    concepts = {i for i, n in index.items() if n['type'] == 'Concept'}
    missing = concepts - bindings.keys()
    if missing:
        errors.append('Concepts without a Lean model: ' + ', '.join(sorted(missing)))
    for ident, binding in bindings.items():
        node = index.get(ident)
        if node is None:
            errors.append('Unknown catalog ID: ' + ident)
            continue
        kind = binding.get('kind')
        if kind not in {'model', 'witness'}:
            errors.append(ident + ': unknown binding kind')
        if kind == 'model' and node['type'] != 'Concept':
            errors.append(ident + ': model must bind a Concept')
        if kind == 'witness' and node['type'] not in {'Law', 'Theorem'}:
            errors.append(ident + ': witness must bind a Law or Theorem')
        if not SYMBOL.fullmatch(binding.get('symbol', '')):
            errors.append(ident + ': invalid declaration name')
        module = binding.get('module', '')
        if not SYMBOL.fullmatch(module) or module.split('.')[0] != 'Catalog':
            errors.append(ident + ': invalid local module')
        elif not (LEAN / (module.replace('.', '/') + '.lean')).is_file():
            errors.append(ident + ': module file is missing')
        for key in ('mapping', 'limitations'):
            if not isinstance(binding.get(key), str) or not binding[key].strip():
                errors.append(ident + ': missing ' + key)
        if binding.get('catalogHash') != catalog_hash(index, ident):
            errors.append(ident + ': catalog interface or premises changed; review mapping and update catalogHash')
        if kind == 'model' and binding.get('scope') not in {'model', 'partial'}:
            errors.append(ident + ': model scope must be model or partial')
        if kind == 'witness':
            if not binding.get('expectedType'):
                errors.append(ident + ': missing independently reviewed expectedType')
            premises = binding.get('premiseMapping', {})
            if set(premises) != set(node.get('dependsOn', [])) or not all(premises.values()):
                errors.append(ident + ': each explicit dependsOn premise requires a mapping')
            allowed = binding.get('allowedAxioms', [])
            if not isinstance(allowed, list) or not set(allowed) <= ALLOWED_AXIOMS:
                errors.append(ident + ': only standard Lean foundational axioms may be allowed')
    return errors


def inputs_digest():
    paths = sorted([*LEAN.glob('*.lean'), *(LEAN / 'Catalog').rglob('*.lean')])
    paths += [MANIFEST, LEAN / 'lakefile.toml', LEAN / 'lake-manifest.json',
              LEAN / 'lean-toolchain', ROOT / 'scripts/lean.py', ROOT / 'scripts/lean_formulations.py']
    return digest({'files': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in paths}, 'catalog': load_graph()})


def run(args):
    result = subprocess.run(args, cwd=LEAN, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    if result.returncode:
        raise ValueError('Command failed: ' + ' '.join(args) + '\n' + result.stdout)
    return result.stdout


def check_dependencies():
    lock = json.loads((LEAN / 'lake-manifest.json').read_text())
    for package in lock['packages']:
        if package['type'] != 'git':
            raise ValueError('Only pinned Git dependencies are supported')
        directory = LEAN / lock['packagesDir'] / package['name']
        actual = run(['git', '-C', str(directory), 'rev-parse', 'HEAD']).strip()
        if actual != package['rev']:
            raise ValueError('Installed dependency revision differs from lock: ' + package['name'])
        dirty = run(['git', '-C', str(directory), 'status', '--porcelain', '--untracked-files=normal'])
        if dirty.strip():
            raise ValueError('Installed dependency has local changes: ' + package['name'])


def audit_source(bindings):
    # `import all` retains theorem bodies for ConstantInfo inspection under
    # Lean's module system; an ordinary import may expose only an opaque facade.
    modules = sorted({b['module'] for b in bindings.values()})
    lines = ['module', 'import Catalog', 'import Catalog.Audit']
    lines += ['import all ' + module for module in modules]
    lines += ['set_option warningAsError true', 'universe u v w x']
    for ident, binding in sorted(bindings.items()):
        symbol = binding['symbol']
        if binding['kind'] == 'model':
            lines.append('#catalog_model ' + symbol)
        else:
            lines += ['-- ' + ident,
                      'example : ' + binding['expectedType'] + ' := @' + symbol,
                      '#catalog_witness ' + symbol]
    return '\n'.join(lines) + '\n'


def verify(manifest):
    REPORT.unlink(missing_ok=True)
    before = inputs_digest()
    check_dependencies()
    version = run(['lake', 'env', 'lean', '--version']).strip()
    if 'version ' + manifest['toolchain'].split(':v')[-1] + ',' not in version:
        raise ValueError('Running Lean version differs from the pinned toolchain')
    build_output = run(['lake', 'build'])
    target = LEAN / '.lake' / 'CatalogAudit.lean'
    target.write_text(audit_source(manifest['bindings']))
    audit_output = run(['lake', 'env', 'lean', str(target)])
    witnesses = {}
    for ident, binding in manifest['bindings'].items():
        if binding['kind'] != 'witness':
            continue
        pattern = r'^CATALOG_WITNESS ' + re.escape(binding['symbol']) + r' \| *(.*)$'
        match = re.search(pattern, audit_output, re.MULTILINE)
        if not match:
            raise ValueError('Missing compiler audit output for ' + ident)
        axioms = sorted(a for a in match[1].strip().split(',') if a)
        if not set(axioms) <= set(binding['allowedAxioms']):
            raise ValueError('Witness exceeds its declared foundational axioms: ' + ident)
        witnesses[ident] = {'symbol': binding['symbol'], 'axioms': axioms}
    for binding in manifest['bindings'].values():
        if binding['kind'] == 'model' and 'CATALOG_MODEL ' + binding['symbol'] + '\n' not in audit_output:
            raise ValueError('Missing compiled model: ' + binding['symbol'])
    after = inputs_digest()
    check_dependencies()
    if before != after:
        raise ValueError('Lean inputs changed during verification; run again')
    report = {'schemaVersion': 1, 'verifiedAt': datetime.now(timezone.utc).isoformat(),
              'inputsDigest': after, 'toolchain': manifest['toolchain'],
              'mathlibRevision': manifest['mathlibRevision'], 'compiler': version,
              'modelsChecked': sum(b['kind'] == 'model' for b in manifest['bindings'].values()),
              'witnesses': witnesses,
              'commands': ['lake build', 'lake env lean .lake/CatalogAudit.lean'],
              'compilerOutput': build_output + audit_output,
              'interpretation': 'Compiled proofs of the mapped Lean propositions. Natural-language correspondence still requires review; models are not proofs of every catalog claim.'}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return report


def fresh_report():
    if REPORT.exists():
        report = json.loads(REPORT.read_text())
        if report.get('inputsDigest') == inputs_digest():
            try:
                check_dependencies()
                return report
            except (ValueError, OSError):
                return None
    return None


def summary(manifest, index):
    models = [b for b in manifest['bindings'].values() if b['kind'] == 'model']
    scopes = Counter(b['scope'] for b in models)
    report = fresh_report()
    return {'concepts': len(models), 'modelScopes': dict(scopes),
            'registeredWitnesses': sum(b['kind'] == 'witness' for b in manifest['bindings'].values()),
            'verifiedWitnesses': len(report['witnesses']) if report else 0,
            'verificationFresh': report is not None,
            'unboundLawsAndTheorems': sum(n['type'] in {'Law', 'Theorem'} and i not in manifest['bindings']
                                        for i, n in index.items()),
            'interpretation': 'Model coverage does not imply all operations, laws or theorems have been formalized.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('check', 'verify', 'coverage'):
        sub.add_parser(name)
    sub.add_parser('get').add_argument('id')
    sub.add_parser('fingerprint').add_argument('id')
    refresh = sub.add_parser('refresh-bindings', help='Refresh catalogHash after reviewing Lean mappings')
    refresh.add_argument('ids', nargs='*', help='Stable IDs or concept short forms; default: all bindings')
    refresh.add_argument('--dry-run', action='store_true', help='List changes without writing')
    args = parser.parse_args()
    try:
        manifest = json.loads(MANIFEST.read_text())
        index = {n['id']: n for n in load_graph()['@graph']}
        if args.command == 'refresh-bindings':
            updated, changes = refresh_bindings(manifest, index, args.ids)
            if changes and not args.dry_run:
                MANIFEST.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + '\n')
            print(json.dumps({'dryRun': args.dry_run, 'changes': changes,
                              'verification': 'Run make check-lean and make test-lean after refreshing.'}, indent=2))
            return 0
        if args.command == 'fingerprint':
            ident = args.id
            if ident not in index:
                ident = next((i for i, n in index.items() if n.get('shortForm') == ident), ident)
            if ident not in index:
                raise ValueError('Unknown catalog ID: ' + ident)
            print(json.dumps({'id': ident, 'catalogHash': catalog_hash(index, ident),
                              'dependsOn': index[ident].get('dependsOn', [])}, indent=2))
            return 0
        errors = validate(manifest, index)
        if errors:
            raise ValueError('\n'.join(errors))
        if args.command == 'verify':
            verify(manifest)
        result = summary(manifest, index)
        if args.command == 'get':
            ident = args.id
            if ident not in index:
                ident = next((i for i, n in index.items() if n.get('shortForm') == ident), ident)
            binding = manifest['bindings'].get(ident)
            if binding is None:
                raise ValueError('No Lean binding registered for ' + ident)
            report = fresh_report()
            evidence = report.get('witnesses', {}).get(ident) if report else None
            result = {'id': ident, **binding, 'verificationFresh': report is not None,
                      'witnessEvidence': evidence}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
