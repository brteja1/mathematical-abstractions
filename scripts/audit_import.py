#!/usr/bin/env python3
"""Report imported node changes without treating later reviewed edits as corruption."""
import hashlib
import json
from markdown_graph import ROOT, load_graph


def main():
    manifest = json.loads((ROOT / 'data/import_manifest.json').read_text())
    doc = load_graph()
    hashes = {n['id']: hashlib.sha256(json.dumps(n, sort_keys=True, ensure_ascii=False).encode()).hexdigest() for n in doc['@graph']}
    original = manifest['nodeHashes']
    result = {'importedNodes': len(original), 'currentNodes': len(hashes),
              'unchanged': sum(hashes.get(k) == v for k, v in original.items()),
              'changed': sorted(k for k, v in original.items() if k in hashes and hashes[k] != v),
              'missing': sorted(set(original) - set(hashes)),
              'added': sorted(set(hashes) - set(original)),
              'contextUnchanged': doc['@context'] == manifest['context'],
              'contextPreserved': all(doc['@context'].get(k) == v for k, v in manifest['context'].items()),
              'addedContextTerms': sorted(set(doc['@context']) - set(manifest['context']))}
    print(json.dumps(result, indent=2))
    return bool(result['missing'] or not result['contextPreserved'])


if __name__ == '__main__':
    raise SystemExit(main())
