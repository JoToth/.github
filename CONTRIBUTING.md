# Contributing

Thanks for contributing to JoToth projects. This document describes shared expectations for contributors. For repository-specific build, test, examples and cleanup commands, consult the target repository's README and development documentation. **Do not assume that every repository provides the same CMake presets or scripts.**

## Development rules

- Keep generated files out of the source tree.
- For CMake-based projects, route build, documentation, coverage, benchmark, and test outputs into `${CMAKE_BINARY_DIR}` where applicable.
- When adding a new target that generates files, make sure generated artifacts participate in cleanup where practical.
- Follow the existing code style and conventions in the project. Keep formatting consistent with surrounding code.
- Run relevant tests before submitting changes. New features should include tests where applicable.

## Recommended workflow

Follow the repository's verified configuration, build and test instructions. If it provides CMake presets, use the documented presets; names such as `dev` and `tests` are **not universal**.

## Branching strategy

Use feature branches to implement new capabilities. Branches that are no longer maintained for over 180 days may be deleted by maintainers.

## Commits

### Cleaning before commit

Remove generated build artifacts using the cleanup procedure documented by the target repository. `cmake -P tools/prune.cmake` and `clean-all` are **workers-specific examples**, not shared commands.

### Think before commit

- Instead of large commits, use small commits that implement the feature step by step.
- Each commit must leave the branch in a working state. Commits must not introduce broken or incomplete changes.
- It is the committer's responsibility to choose appropriate commit messages.
- Commit messages must be clear and descriptive.
- The title should summarize the change and include the feature or component affected. The body should explain what was changed and why.

    Example:
    ```text
    build: improve cleanup of generated files

    Ensures generated artifacts are removed by the documented cleanup workflow.
    ```

- Please be respectful in all interactions. Abusive, offensive, or inappropriate language will not be tolerated and may result in removal of contributions or access restrictions. See [Code of Conduct](CODE_OF_CONDUCT.md).

## Submitting changes

- Fork the repository and create a feature branch.
- Submit a pull request with a clear description of the changes. Pull requests should be focused, well-described, and limited in scope.
- Link related issues when applicable.

## Notes for new build tooling

When adding coverage, documentation, release, or benchmarking logic to a CMake project:

- Prefer `${CMAKE_BINARY_DIR}` for outputs.
- Register build-tree artifacts with native `clean` where possible.
- Keep the repository's documented cleanup workflow able to remove generated artifacts that could leak into the source tree.
- Update `.gitignore` and documentation when new generated artifacts appear.
