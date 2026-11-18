#!/usr/bin/env python3
"""Prepare matched evaluation workspaces without invoking a model."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


SUITE = Path(__file__).resolve().parent
ROOT = SUITE.parents[1]
COMMON = """This is an isolated evaluation task. Work only in this workspace.
Read TASK.md and complete it, writing the requested outputs here. The catalog
at catalog/ is available as mathematical reference in both evaluation arms.
Use python3 catalog/scripts/catalog.py for focused queries. The pinned Lean
project is catalog/lean/; available installed runtimes are linked into the
snapshot. Do not change shared runtime directories or the source repository.
Do not read outside this workspace, use past-session memory, inspect evaluator
answer keys, or consult another run. Report tool blockers honestly. Follow the
task's contract and preserve its requested scope. Do not invoke other agents.
"""
NEUTRAL = """# Evaluation workspace

Complete TASK.md using this workspace. Keep generated task artifacts here.
Catalog records and linked installed runtimes are reference inputs; do not
modify them. Do not read other evaluation runs or evaluator answer keys.
"""


def hashes(directory):
    """Hash copied regular inputs; runtime links are recorded separately."""
    return {str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob('*')) if p.is_file() and
            not any(parent.is_symlink() for parent in (p, *p.parents))}


def snapshot(destination):
    destination.mkdir()
    ignore = shutil.ignore_patterns('__pycache__', '*.pyc', '.lake', 'verification.json')
    for name in ('concepts', 'data', 'scripts', 'lean', 'ontology', 'visualization', 'docs'):
        shutil.copytree(ROOT / name, destination / name, ignore=ignore)
    # Agent instructions and examples that route to skills are not common inputs.
    (destination / 'docs/AGENT_WORKFLOWS.md').unlink()
    for name in ('provenance_legacy.json', 'dependencies.lock.json', 'Makefile',
                 'requirements-ontology.txt', 'INSTALL.md', '.ontfs.ttl'):
        if (ROOT / name).exists():
            shutil.copy2(ROOT / name, destination / name)
    links = {}
    for name in ('.venv', 'deps/ONTFS', 'lean/.lake'):
        source = ROOT / name
        if source.exists():
            target = destination / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(source, target_is_directory=True)
            links[name] = str(source)
    return links


def prepare(case_id, output):
    cases = json.loads((SUITE / 'cases.json').read_text())
    case = next((c for c in cases if c['id'] == case_id), None)
    if case is None:
        raise ValueError('Unknown case: ' + case_id)
    output = output.resolve()
    if output.exists():
        raise ValueError('Output already exists; choose a new directory: ' + str(output))
    if output.is_relative_to(ROOT):
        raise ValueError('Prepare outside the source repository to avoid inherited instructions')
    output.parent.mkdir(parents=True, exist_ok=True)
    task = (SUITE / case['prompt']).read_text()
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True,
                              capture_output=True, check=True).stdout.strip()
    # Stage both arms before making them visible; never overwrite an existing run.
    with tempfile.TemporaryDirectory(prefix='skill-eval-', dir=output.parent) as temp:
        staging = Path(temp) / 'pair'
        staging.mkdir()
        baseline = staging / 'without-skills'
        treatment = staging / 'with-skills'
        baseline.mkdir()
        runtime_links = snapshot(baseline / 'catalog')
        (baseline / 'TASK.md').write_text(task)
        (baseline / 'AGENTS.md').write_text(NEUTRAL)
        for name, source in case.get('fixtures', {}).items():
            if Path(name).name != name:
                raise ValueError('Fixture destination must be a filename: ' + name)
            shutil.copy2(SUITE / source, baseline / name)
        common_hashes = hashes(baseline)
        shutil.copytree(baseline, treatment, symlinks=True)
        shutil.copytree(ROOT / 'ai/skills', treatment / 'catalog/ai/skills',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        guided = '\nRead these skill entrypoints before completing the same task:\n'
        guided += ''.join('- catalog/ai/skills/' + name + '/SKILL.md\n' for name in case['skills'])
        (baseline / 'prompt.txt').write_text(COMMON + '\nComplete TASK.md without repository skill instructions.\n')
        (treatment / 'prompt.txt').write_text(COMMON + guided)
        manifest = {'case': case_id, 'sourceRevision': revision,
                    'comparison': 'skill instructions given equal catalog access',
                    'entrypoints': case['skills'], 'commonInputHashes': common_hashes,
                    'runtimeLinks': runtime_links,
                    'skillInputHashes': hashes(treatment / 'catalog/ai/skills'),
                    'promptHashes': {arm.name: hashlib.sha256((arm / 'prompt.txt').read_bytes()).hexdigest()
                                     for arm in (baseline, treatment)},
                    'limitations': ['Runtime symlinks and host instructions are not isolated by this helper.',
                                    'Record model/settings, tool access and catalog dirty state separately.']}
        (staging / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        staging.rename(output)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', required=True, help='Case ID, e.g. 01')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(prepare(args.case, args.out))
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
