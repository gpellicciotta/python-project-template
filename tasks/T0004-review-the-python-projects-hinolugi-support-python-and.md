---
id: T0004
owner: "@claude"
needs: []
branch: task/T0004-review-the-python-projects-hinolugi-support-python-and
worktree: ./work/T0004-review-the-python-projects-hinolugi-support-python-and
status: completed
started: 2026-09-06
ended: 2026-09-06
---

# T0004: Review hinolugi-support.python and mail-utils for template gaps

## Goals

Compare this template's structure against hinolugi-support.python and mail-utils, as if both were scaffolded
from it, to surface generic conventions worth adopting here. Exclude anything specific to one project's domain.
File each finding as a separate backlog item for @gio to review.

## Task Execution Steps

- [x] **[Read]**      Inventory top-level layout, docs/, .github/, src/ across all three projects.
- [x] **[Read]**      Compare pyproject.toml, .gitignore, README, and CHANGELOG conventions across all three.
- [x] **[Decide]**    Select generic, template-worthy differences, excluding project-specific domain logic.
- [x] **[Doc]**       File one backlog TODO per major topic, owned by @gio, in TODO.md.

## Execution Log

- [2026-09-06] **[Read]** Compared directory layouts, CI workflows, pyproject.toml, .gitignore, and
  README/CHANGELOG conventions across all three projects.
  - hinolugi-support.python ships `logging.py` and a `publish.yml` release workflow; template has neither.
  - Both downstream projects populate `tasks/`; the template's `tasks/` dir isn't tracked at all.
  - Neither downstream project's `docs/` scaffolds the `specs/`/`adrs/`/`issues/` subdirectories that
    dev-guidelines mandates.
  - `scaffold.py` resets `pyproject.toml`'s version to `"0.0.1"` (no `-pre`), and mail-utils still carries the
    superseded `[in development]` CHANGELOG tag instead of the current `-pre` heading convention.
  - hinolugi-support.python uses hatchling + a narrow `[tool.ruff.lint] select` list; template and mail-utils
    use setuptools with ruff defaults.
  - mail-utils has a `scripts/` dir for non-packaged dev/maintenance tooling with no equivalent template
    convention.
- [2026-09-06] **[Decide]** Chose 7 generic topics (logging module, release workflow, docs subdirectories,
  tasks/ scaffold, `-pre` version fix, build-backend/lint decision, scripts/ convention). Excluded mail-utils'
  Gmail/PST-specific modules and hinolugi's `transport.py` (an HTTP client, not template-generic).
- [2026-09-06] **[Doc]** Filed A0005-A0011 in TODO.md's Backlog, each `[owner: @gio]`, pending his review before
  any implementation.
- [2026-09-06] **[Verify]** Ran `pytest -q` in the worktree (no source changes made); suite passes.
- [2026-09-06] **[Complete]** Review finished; findings filed as seven backlog TODOs for @gio, no source
  changes needed in this task. CHANGELOG.md left untouched — backlog/administrative grooming is explicitly
  excluded from release notes.
