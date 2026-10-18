#!/usr/bin/env python3
"""Minimal local scaffold check; not a substitute for GitHub Community Standards."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["README.md", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "COMMUNITY_STANDARDS.md", "docs/BOOTSTRAP.md", "docs/AUDIT_CHECKLIST.md", ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/PULL_REQUEST_TEMPLATE.md"]
missing = [name for name in required if not (root / name).is_file()]
for name in required:
    print(("FAIL" if name in missing else "PASS") + " " + name)
for name in ["CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md", "LICENSE"]:
    print(("PRESENT " if (root / name).is_file() else "PENDING ") + name)
if missing:
    raise SystemExit(1)
print("Scaffold structural check passed; community policy activation remains manual.")
