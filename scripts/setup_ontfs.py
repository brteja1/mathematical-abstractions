#!/usr/bin/env python3
"""Register/initialize ONTFS as a real submodule and pin its reviewed revision."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', '-C', str(cwd), *args], text=True).strip()


def main():
    lock = json.loads((ROOT / 'dependencies.lock.json').read_text())['ONTFS']
    try:
        top = Path(git('rev-parse', '--show-toplevel')).resolve()
    except subprocess.CalledProcessError:
        raise SystemExit('Cannot register a submodule: this workspace needs a valid, writable parent Git repository. No Git metadata was initialized or replaced.')
    if top != ROOT:
        raise SystemExit('Run in a standalone mathematical-abstractions Git checkout.')
    path = ROOT / lock['path']
    staged = git('ls-files', '--stage', '--', lock['path'])
    if staged and not staged.startswith('160000 '):
        raise SystemExit('Dependency path is tracked as ordinary files; refusing to replace it.')
    if staged:
        git('submodule', 'update', '--init', '--', lock['path'])
    else:
        git('submodule', 'add', '--name', 'ONTFS', lock['url'], lock['path'])
    if git('remote', 'get-url', 'origin', cwd=path) != lock['url']:
        raise SystemExit('ONTFS origin differs from dependencies.lock.json; refusing checkout.')
    if git('status', '--porcelain', cwd=path):
        raise SystemExit('ONTFS contains local changes; refusing to change its revision.')
    try:
        git('cat-file', '-e', lock['commit'] + '^{commit}', cwd=path)
    except subprocess.CalledProcessError:
        git('fetch', 'origin', lock['commit'], cwd=path)
    git('checkout', '--detach', lock['commit'], cwd=path)
    git('add', '--', '.gitmodules', lock['path'])
    if git('rev-parse', 'HEAD', cwd=path) != lock['commit']:
        raise SystemExit('ONTFS pin verification failed')
    entry = git('ls-files', '--stage', '--', lock['path'])
    if not entry.startswith('160000 ' + lock['commit'] + ' '):
        raise SystemExit('Parent gitlink pin verification failed')
    print('Registered ONTFS submodule at ' + lock['commit'])


if __name__ == '__main__':
    main()
