# Bootstrap and adoption

The maintainer supplied the original `workers` Code of Conduct and Contributing text. Root `CODE_OF_CONDUCT.md` preserves the supplied CoC. Root `CONTRIBUTING.md` adapts its shared rules, removing the assumption that every project has `dev` / `tests` presets, `tools/prune.cmake`, or `clean-all`.

## Before publishing

1. Confirm the reporting path for confidential CoC reports. The current wording says to contact maintainers but does not provide a specific private channel.
2. Decide the license for `.github` and ensure each code repository has its own appropriate license.
3. Review and activate `SECURITY.md` and `SUPPORT.md` from `templates/` only after verifying the real reporting and support channels.
4. Confirm the common rules apply to every JoToth repository, especially CMake-only rules for non-CMake projects.
5. Test default-file inheritance in a repository without local overrides; verify issue and PR template behavior.
6. Where project-specific contribution instructions are necessary, use `templates/REPOSITORY_CONTRIBUTING.md`, adapt every command, and link back to the central rules.
7. Audit `.github` itself using `COMMUNITY_STANDARDS.md` and `docs/AUDIT_CHECKLIST.md`.

Do not treat template files as active policies. GitHub does not dynamically substitute a repository's name or paths into central Markdown links.
