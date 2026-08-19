# Release Notes

All notes will be in reverse chronological order.

## 2026-08-19 v1.0.0
- First stable release. Published the repo to GitHub
  (https://github.com/gpellicciotta/python-project-template).
- Added a `docs/` folder (with a short explainer) so it exists from the start rather than only being
  documented as "created as needed".
- Fixed `setup.ps1`'s build step: the `dev` extra never included the `build` package, so `python -m build`
  always failed with "No module named build" despite the editable install succeeding.

## 2026-08-19 v0.1.0
- Added `myproject create <project-name> [-o <output-dir>]`, which scaffolds a new project as a renamed copy
  of this template (package rename, `pyproject.toml` name, and all `template-project` / `python-template-project`
  placeholder references), automating the manual steps previously described in the README.
- Restructured the CLI into subcommands: `help`, `version`, `greet <name>` (the previous top-level sample
  action), and `create`. **Breaking:** `myproject <name>` no longer greets directly — use `myproject greet <name>`.
- `__version__` is now read from installed package metadata instead of being hardcoded, so it can't drift
  from `pyproject.toml`'s `version`.
- Added `ruff` (lint + format check) as a dev-extra tool, wired into `setup.ps1` and CI, with a 132-character
  line length. Added a matching `.editorconfig` (4-space indent, spaces only, UTF-8, 132-char lines).
- Added the project's `LICENSE` file (MIT), matching the classifier already declared in `pyproject.toml`.
- Trimmed `[build-system].requires` to just `setuptools>=68` (removed `wheel` and `build`, neither of which
  is a build-backend dependency).
- Documented general development guidelines and the style guide in `CLAUDE.md`.
