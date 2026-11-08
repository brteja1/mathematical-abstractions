#!/usr/bin/env python3
"""Bundle the page shell, local assets, and catalog into one offline viewer."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VISUALIZATION = ROOT / 'visualization'


def render(data, directory=VISUALIZATION):
    """Inline trusted source assets and escaped catalog JSON without dependencies."""
    template = (directory / 'template.html').read_text()
    payload = (json.dumps(data, ensure_ascii=False)
               .replace('<', '\\u003c')
               .replace('\u2028', '\\u2028')
               .replace('\u2029', '\\u2029'))
    replacements = {
        '/*__STYLES__*/': (directory / 'styles.css').read_text().rstrip(),
        '/*__APP__*/': (directory / 'app.js').read_text().rstrip(),
        '/*__CATALOG__*/null': payload,
    }
    for marker in replacements:
        if template.count(marker) != 1:
            raise ValueError('Expected exactly one viewer placeholder: ' + marker)
    # One substitution pass prevents marker-like text inside assets or data from
    # being interpreted as a second placeholder.
    pattern = '|'.join(re.escape(marker) for marker in replacements)
    return re.sub(pattern, lambda match: replacements[match[0]], template)


def build():
    from markdown_graph import load_graph
    from validate_graph import validate

    data = load_graph()
    errors = validate(data)
    if errors:
        raise ValueError('Invalid graph: ' + '; '.join(errors))
    target = VISUALIZATION / 'index.html'
    target.write_text(render(data))
    print(target)


if __name__ == '__main__':
    build()
