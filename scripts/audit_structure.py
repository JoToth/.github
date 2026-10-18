#!/usr/bin/env python3
"""Check the JoToth community scaffold. This is NOT a live GitHub compliance score."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "COMMUNITY_STANDARDS.md",
    "SECURITY.md", "SUPPORT.md", "LICENSE", "docs/BOOTSTRAP.md", "docs/AUDIT_CHECKLIST.md",
    "docs/DECISIONS_REQUIRED.md", ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml", ".github/PULL_REQUEST_TEMPLATE.md",
]
errors = []
for name in required:
    exists = (root / name).is_file()
    print(f"{'PASS' if exists else 'FAIL'} required: {name}")
    if not exists:
        errors.append(f"Missing required file: {name}")

# Local Markdown links only. External links and anchor resolution are outside this check.
link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
for path in root.rglob('*.md'):
    if 'templates' in path.relative_to(root).parts:
        continue  # drafts can intentionally contain placeholders
    body = path.read_text(encoding='utf-8')
    for target in link_re.findall(body):
        target = target.split('#', 1)[0].split('?', 1)[0]
        if not target or re.match(r'^[a-z][a-z0-9+.-]*:', target, re.I) or target.startswith('//'):
            continue
        if not (path.parent / target).exists():
            errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")

# Basic YAML parse if PyYAML is installed; otherwise warn, never pretend validated.
forms = list((root / '.github' / 'ISSUE_TEMPLATE').glob('*.yml'))
try:
    import yaml
except ImportError:
    print('WARN YAML syntax not validated (install PyYAML to enable)')
else:
    for path in forms:
        try:
            data = yaml.safe_load(path.read_text(encoding='utf-8'))
            if not isinstance(data, dict) or not data.get('name') or not data.get('description'):
                errors.append(f'Incomplete issue form metadata: {path.relative_to(root)}')
        except yaml.YAMLError as exc:
            errors.append(f'Invalid YAML: {path.relative_to(root)}: {exc}')

if (root / 'LICENSE').exists():
    print('PASS license file present (owner approval not machine-verifiable)')
print('PENDING verified private conduct/security reporting channel and live GitHub settings')
for error in errors:
    print('FAIL', error)
if errors:
    sys.exit(1)
print('PASS local scaffold and checked local links; NOT a 100% community compliance claim')
