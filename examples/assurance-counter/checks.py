#!/usr/bin/env python3
"""Independent finite oracle over results from the actual Lean source."""
from pathlib import Path
import subprocess
import sys

project = Path(__file__).resolve().parent
catalog = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else project.parents[1]
result = subprocess.run(['lake', 'env', 'lean', '--run', str(project / 'Counter.lean')],
                        cwd=catalog / 'lean', capture_output=True, text=True, timeout=90)
if result.returncode:
    raise SystemExit(result.stdout + result.stderr)
rows = [tuple(map(int, line.split(','))) for line in result.stdout.splitlines()]
assert len(rows) == 13 * 16, 'missing or duplicate outputs'
assert {(limit, n) for limit, n, _ in rows} == {(limit, n) for limit in range(13) for n in range(16)}
for limit, n, actual in rows:
    expected = n if n >= limit else n + 1
    assert actual == expected, (limit, n, actual, expected)
    if n <= limit:
        assert actual <= limit, (limit, n, actual)
print('208 actual-source examples matched the independent oracle (R1/R2).')
