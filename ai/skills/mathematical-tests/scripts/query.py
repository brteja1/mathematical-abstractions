#!/usr/bin/env python3
"""Run the repository's bounded ONTFS test-context queries from any working directory."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'scripts'))
from test_context import main

if __name__ == '__main__':
    raise SystemExit(main())
