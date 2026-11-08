#!/usr/bin/env python3
"""Check always-visible labels and navigation in Chrome/Chromium after make markdown.

Usage: python3 scripts/check_viewer_labels.py [--screenshots /tmp/atlas-labels]
No Python packages or downloaded browser drivers are required.
"""
import argparse
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    browser = next((shutil.which(n) for n in ('google-chrome', 'chromium', 'chromium-browser')
                    if shutil.which(n)), None)
    if not browser:
        raise SystemExit('Chrome or Chromium must be installed locally.')
    page = (ROOT / 'visualization/index.html').read_text()
    checks = (ROOT / 'tests/viewer_label_checks.js').read_text()
    if args.screenshots:
        args.screenshots.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='atlas-label-check-') as tmp:
        directory = Path(tmp)
        for width, scenario in [(1600, 'overview'), (1600, 'dense'), (1600, 'nested'), (1100, 'selected'), (600, 'dense')]:
            capture = '<script>window.viewerErrors=[];window.addEventListener("error",e=>window.viewerErrors.push(e.message));window.labelScenario=' + json.dumps(scenario) + ';</script>'
            target = directory / 'viewer.html'
            target.write_text(page.replace('<script>\n', capture + '<script>\n', 1).replace('</body>', '<script>' + checks + '</script></body>'))
            command = [browser, '--headless', '--disable-gpu', '--no-first-run',
                       '--no-default-browser-check', '--force-device-scale-factor=1',
                       '--user-data-dir=' + str(directory / 'profile'),
                       f'--window-size={width},1150', '--dump-dom', '--timeout=15000', '--virtual-time-budget=1500']
            if args.screenshots:
                command.append('--screenshot=' + str(args.screenshots.resolve() / f'{width}-{scenario}.png'))
            result = subprocess.run(command + [target.as_uri()], capture_output=True, text=True, timeout=45)
            report = re.search(r'<pre id="label-report"[^>]*>(.*?)</pre>', result.stdout, re.S)
            if result.returncode or not report:
                raise SystemExit(f'Browser failed ({width}, {scenario}): {result.stderr[-1600:]}')
            parsed = json.loads(html.unescape(report[1]))
            print(json.dumps({'scenario': scenario, **parsed}), flush=True)
            if not parsed['ok']:
                return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
