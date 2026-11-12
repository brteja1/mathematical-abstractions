"""Read declaration excerpts from this project's deliberately formatted Lean modules.

This is a source locator, not a Lean parser or proof checker. Excerpts retain the
module's imports, namespace, universe and section-variable context by reference.
"""
import re
import json
from pathlib import Path

COMMAND = re.compile(r'^(?:(?:noncomputable|private|protected) )*(abbrev|def|structure|class|inductive|theorem) ([\w.]+)')
BOUNDARY = re.compile(r'^(?:namespace |end(?: |$)|section(?: |$)|variable |universe |open |(?:noncomputable )?instance\b|/[-*]|--)')


def declarations(path):
    lines = Path(path).read_text().splitlines()
    namespaces = []
    result = {}
    comment = False
    for i, line in enumerate(lines):
        if line.startswith('/-'):
            comment = '-/' not in line
            continue
        if comment:
            if '-/' in line:
                comment = False
            continue
        if line.startswith('namespace '):
            namespaces.append(line.split()[1])
        elif line.startswith('end') and namespaces:
            # Named sections also end with `end`; they do not pop a namespace.
            name = line[3:].strip()
            if name == namespaces[-1] or (not name):
                namespaces.pop()
        match = COMMAND.match(line)
        if not match:
            continue
        symbol = '.'.join(namespaces + [match[2]])
        stop = i + 1
        while stop < len(lines) and not COMMAND.match(lines[stop]) and not BOUNDARY.match(lines[stop]):
            stop += 1
        result[symbol] = ('\n'.join(lines[i:stop]).rstrip(), i + 1)
    return result


def locate(root, module, symbol, seen=None):
    """Follow local imports when a binding re-exports a declaration."""
    seen = set() if seen is None else seen
    if module in seen:
        return None
    seen.add(module)
    path = root / 'lean' / (module.replace('.', '/') + '.lean')
    found = declarations(path).get(symbol)
    if found:
        return path, found[0], found[1]
    for imported in re.findall(r'^(?:public )?import (Catalog[\w.]*)', path.read_text(), re.M):
        result = locate(root, imported, symbol, seen)
        if result:
            return result
    return None


def formulation_errors(manifest, index, root):
    errors = []
    for ident, binding in manifest['bindings'].items():
        node = index.get(ident, {})
        if not node:
            continue
        if 'leanFormulation' not in node:
            errors.append(ident + ': missing Lean formulation')
            continue
        module = binding.get('module', '')
        if not re.fullmatch(r'Catalog(?:\.[A-Za-z_][A-Za-z_0-9]*)+', module):
            continue  # The main manifest validator reports malformed bindings.
        if binding['kind'] == 'witness' and 'expectedType' not in binding:
            continue
        if not (root / 'lean' / (module.replace('.', '/') + '.lean')).is_file():
            continue
        declaration = locate(root, module, binding.get('symbol', ''))
        if not declaration:
            errors.append(ident + ': formulation declaration is missing')
            continue
        path, code, _ = declaration
        if binding['kind'] == 'witness':
            path, code, _ = witness_formulation(root, binding)
        expected = code
        if node['leanFormulation'] != expected:
            errors.append(ident + ': Lean formulation is stale; review against its source')
        if node.get('leanModelMapping') != binding['mapping'] or node.get('leanModelLimitations') != binding['limitations']:
            errors.append(ident + ': formulation mapping or limitations differ from Lean binding')
        if binding['kind'] == 'witness' and node.get('leanPremiseMapping') != json.dumps(binding.get('premiseMapping', {}), ensure_ascii=False, sort_keys=True):
            errors.append(ident + ': formulation premise mapping differs from Lean binding')
        if node.get('formulationScope') != binding.get('scope', 'registered-witness-type'):
            errors.append(ident + ': formulation scope differs from Lean binding')
        source = index.get(node.get('formulationSource'), {})
        if source.get('path') != str(path.relative_to(root)) or node.get('formulationLocator') != binding['symbol']:
            errors.append(ident + ': formulation source/locator differs from Lean binding')
    return errors


def witness_formulation(root, binding):
    expected = binding['expectedType']
    # Expand a named proposition rather than showing an opaque target alias.
    if re.fullmatch(r'Catalog[\w.]+', expected):
        found = locate(root, binding['module'], expected)
        if found:
            return found
    path, _, line = locate(root, binding['module'], binding['symbol'])
    return path, expected, line
