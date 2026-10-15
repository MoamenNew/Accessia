#!/usr/bin/env python3
"""Lightweight repository sanity checks, NOT a comprehensive security audit."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = [
    'AGENTS.md', 'CLAUDE.md', 'START_HERE.md',
    'docs/OPERATING_RULES.md', 'docs/PROJECT_BRIEF.md',
    'docs/PRODUCT_SPEC.md', 'docs/ARCHITECTURE.md',
    'docs/SECURITY.md', 'docs/BUILD_LOG.md',
    'prompts/01_UNDERSTAND_IDEA.txt', 'prompts/02_BUILD_MVP.txt',
    'prompts/03_TEST_AND_SECURITY.txt', 'prompts/04_HANDOFF.txt',
]
missing = [name for name in REQUIRED if not (ROOT / name).exists()]
if missing:
    print('FAIL: Missing required files:', ', '.join(missing))
    sys.exit(1)

# Scan newly authored application/source/config files only; avoid false matches
# from explanatory documentation or this script itself.
source_ext = {'.py', '.js', '.jsx', '.ts', '.tsx', '.json', '.yaml', '.yml'}
patterns = [
    ('Private key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
    ('OpenAI-style key', re.compile(r'\bsk-[A-Za-z0-9_-]{22,}\b')),
    ('GitHub token', re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{25,}\b')),
]
findings = []
for file in ROOT.rglob('*'):
    if not file.is_file():
        continue
    rel = file.relative_to(ROOT)
    if any(part in {'.git', 'node_modules', '.venv', 'dist', 'build'} for part in rel.parts):
        continue
    if file.name == '.env' or (file.name.startswith('.env.') and file.name != '.env.example'):
        findings.append(f'{rel}: environment file must not be committed')
    if file.suffix not in source_ext or file == pathlib.Path(__file__):
        continue
    try:
        data = file.read_text(encoding='utf-8')
    except (UnicodeError, OSError):
        continue
    for label, pattern in patterns:
        if pattern.search(data):
            findings.append(f'{rel}: possible {label}')
if findings:
    print('FAIL: Potential sensitive content detected:')
    print('\n'.join(findings))
    sys.exit(1)
print('PASS: required starter files exist; no obvious credential patterns found in scanned source files.')
print('NOTE: This does NOT verify application security, dependencies, auth, or live behavior.')
