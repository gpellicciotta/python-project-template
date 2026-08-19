# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

<Fill in: what this project does, who/what it's for (personal tool, library, service, ...), and any hard
invariants that must not be silently changed — e.g. "read-only, never sends/writes", "no network calls",
"single-user, no auth". State them as deliberate design decisions, not just current behavior, so a future
change doesn't casually cross them.>

## Commands

All commands use the project's venv (`.venv`, created via `python -m venv .venv` — or run `. .\setup.ps1` for a
one-shot bootstrap: creates the venv, installs editable + dev extras, runs tests, builds sdist/wheel).

- Install in editable mode, with the `dev` extra (pytest): `.venv\Scripts\pip install -e ".[dev]"`
  (drop `[dev]` if you only need to run the app, not the tests)
- Run the test suite: `.venv\Scripts\python -m pytest`
- <Add the project's actual run command(s) here, e.g. `python -m mypackage.cli <command>`, or
  `mypackage <command>` once installed — see `pyproject.toml`'s `[project.scripts]`.>

Dependencies are declared once, in `pyproject.toml` — there is no separate `requirements.txt` to keep in sync.

## Architecture

<Describe the modules/packages and what each one owns — one paragraph per module is usually enough. Name it,
state its one job, and flag anything a future change needs to respect (e.g. "the only place that parses X",
"must stay pure/dependency-free so it's testable without live credentials").>

## Development Guidelines

These apply to every project scaffolded from this template, not just this one:

- Use semver (`MAJOR.MINOR.PATCH`); this project and its descendants start pre-1.0 (`0.x.y`), so breaking
  changes are still expected but must be called out explicitly in `RELEASES.md` rather than reading as routine.
- Favour simplicity over ingenuity. Keep things as simple as possible for what's actually needed today — don't
  design for hypothetical future requirements.
- Minimize third-party dependencies. Reach for the standard library first; add a dependency only when it earns
  its ongoing maintenance cost.
- Make it easy to get started: a clone + `. .\setup.ps1` (or the three commands under Commands above) should be
  enough to get a working venv, passing tests, and a build — no undocumented setup steps.
- Use the same tools and techniques the rest of the Python ecosystem is using (src-layout, `pyproject.toml`,
  pytest, ruff, GitHub Actions) unless there's a concrete reason to deviate — and if you deviate, say why in
  this file rather than leaving it implicit.

## Conventions

- `RELEASES.md` (top-level) tracks version history: bump `pyproject.toml`'s `version` for every user-facing
  change and add a matching dated entry to `RELEASES.md` with the same version number. This project is pre-1.0
  (`0.x.y`), so call out breaking changes explicitly in the entry rather than letting them read as a routine
  addition.
- `TODO.md` (top-level) is the prioritized backlog. When a TODO item is implemented, remove it and add the
  corresponding `RELEASES.md` entry instead of leaving both.
- `RELEASES.md` and `TODO.md` live at the repo root, not under `docs/`, for visibility. Other documentation
  (design notes, detailed plans, investigation write-ups) belongs under `docs/` instead.
- Keep `README.md`'s setup/usage/layout sections in sync with the code as it evolves — treat drift there as a
  bug, not a documentation nice-to-have.
- Style guide: spaces for indentation (never tabs), 4-space indent width, 132-character line length, UTF-8
  everywhere. Enforced by `.editorconfig` (editor-level) and `ruff` (`pyproject.toml`'s `[tool.ruff]`, run via
  `ruff check .` / `ruff format --check .`, wired into `setup.ps1` and CI) — don't let either drift from these
  numbers.
- The package's `__version__` (`src/myproject/__init__.py`) is read from installed package metadata
  (`importlib.metadata.version(...)`) rather than hardcoded, so `pyproject.toml`'s `version` stays the single
  source of truth.
- <Add project-specific invariants/conventions here as they emerge — things a future change must not casually
  break.>
