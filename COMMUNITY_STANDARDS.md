# JoToth Community Standards — v0.2 (draft)

## Scoring rules

For each applicable requirement use **PASS**, **PARTIAL**, **FAIL**, or **N/A**. Record evidence links and rationale for N/A. Score = PASS / (PASS + PARTIAL + FAIL) × 100; PARTIAL does not count as passed. Report GitHub Community, JoToth Policy and Engineering separately; do not claim a GitHub-generated score from this local calculation.

## A. GitHub Community Standards

| ID | Check | Applicability |
| --- | --- | --- |
| GH-01 | Useful repository description | All |
| GH-02 | Accurate README and onboarding | All |
| GH-03 | Code of Conduct (local or effective GitHub default) | Community-facing repos |
| GH-04 | Contributing guidance (local or effective default) | Accepting contributions |
| GH-05 | Explicit license decision and appropriate license file | Distributable code/content |
| GH-06 | Security reporting policy (local or effective default) | All applicable repos |
| GH-07 | Issue templates / forms (local or effective default) | Issues enabled |
| GH-08 | Pull request template (local or effective default) | PRs enabled |
| GH-09 | Effective support / contact guidance | Community-facing repos |

GitHub's actual Community Standards insights remain the authoritative product UI; this table is an audit-oriented checklist and may include JoToth additions. Also review GitHub's issue/reporting settings where applicable.

## B. JoToth policy

| ID | Check |
| --- | --- |
| JT-01 | CoC matches the maintainer-supplied workers baseline; private reporting channel reviewed |
| JT-02 | Shared contribution rules reflect workers baseline without imposing workers-only commands |
| JT-03 | No workers-only paths, examples, names or commands survive in other repositories |
| JT-04 | Project-specific build/test/examples instructions are verified against repository contents |
| JT-05 | Links and contacts are correct; no unresolved placeholders |
| JT-06 | Changes to shared policies have a review and propagation plan |

## C. Engineering (only where applicable)

| ID | Check |
| --- | --- |
| ENG-01 | C++ standard and supported compilers documented (C++20 where required) |
| ENG-02 | Target-based CMake usage and reproducible configure/build commands |
| ENG-03 | Build, test, install and examples instructions match actual targets |
| ENG-04 | CI exercises supported build/test matrix |
| ENG-05 | API, usage examples and release/versioning documented as relevant |
| ENG-06 | Package/export/install semantics checked for libraries |

## Audit policy

- Check repository source, not merely presence of filenames.
- Cite exact paths and line ranges in findings.
- Prioritize Critical / High / Medium / Low.
- Audit this `.github` repository against sections A and B, and apply section C only if engineering artifacts are introduced.
- Never mark a draft template as an active policy.
