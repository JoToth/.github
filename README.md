# JoToth community defaults

This public `.github` repository provides shared community guidance for JoToth repositories and defines an auditable standard.

## Shared policies

- [Code of Conduct](CODE_OF_CONDUCT.md) — adapted directly from `JoToth/workers` (text supplied by the maintainer).
- [Contributing](CONTRIBUTING.md) — shared rules adapted from `JoToth/workers`; workers-only commands are deliberately not imposed on other repositories.
- [Community Standards](COMMUNITY_STANDARDS.md) — audit criteria and scoring.

GitHub can use supported default community health files from this public repository when a repository under the same owner does not define its own. Local files **override**, rather than merge with, shared defaults. Templates in `templates/` require manual customization.

For projects requiring local build, test, cleanup or examples instructions, use a repository-local `CONTRIBUTING.md` that links to the shared policy and the project's verified development guide. Otherwise, rely on the inherited default and make the project's README independently useful.

## Status and next steps

The CoC and shared contribution guidance are populated. **This is not yet a 100% compliant repository**: reporting needs a verified private contact channel, `SECURITY.md` and `SUPPORT.md` remain drafts in `templates/`, and licensing requires an explicit maintainer decision. Verify the GitHub default-file behavior after publishing.

See [bootstrap guide](docs/BOOTSTRAP.md) and [audit checklist](docs/AUDIT_CHECKLIST.md). Run `python3 scripts/audit_structure.py` for a limited structural check.
