# JoToth Community Standards

This public `.github` repository hosts shared community health defaults for repositories owned by JoToth. GitHub uses eligible default files when the target repository has no local counterpart. Local policies take precedence; they do not merge automatically.

## Community files

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Support](SUPPORT.md)
- [Community audit standard](COMMUNITY_STANDARDS.md)
- [License](LICENSE) — proposed MIT; confirm owner approval before publication

## Repository-specific rules

Build presets, test commands, examples, dependencies and cleanup instructions must be verified in each repository. Use the [repository contributing template](templates/REPOSITORY_CONTRIBUTING.md) when a local `CONTRIBUTING.md` is necessary; link back to shared rules explicitly. Do not assume that a link to a local document in a centrally inherited Markdown file resolves in the target repository.

## Validation

Run `python3 scripts/audit_structure.py` for local structural and link checks. This cannot verify GitHub settings or prove full compliance. See the [audit checklist](docs/AUDIT_CHECKLIST.md) and [publication checklist](docs/DECISIONS_REQUIRED.md).

## License

This repository is licensed under the [BSD 3-Clause License](LICENSE) (`BSD-3-Clause`). Individual JoToth repositories must declare their own licenses.
