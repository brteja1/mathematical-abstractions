#!/usr/bin/env python3
"""Bundle the canonical catalog into a dependency-free radial graph viewer."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def build():
    from markdown_graph import load_graph
    from validate_graph import validate
    data = load_graph()
    errors = validate(data)
    if errors:
        raise ValueError('Invalid graph: ' + '; '.join(errors))
    template = (ROOT / 'visualization' / 'template.html').read_text()
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    target = ROOT / 'visualization' / 'index.html'
    target.write_text(template.replace('/*__CATALOG__*/null', payload))
    print(target)

if __name__ == '__main__':
    build()
