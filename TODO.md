# TODO

Shared task index for planned, active, and blocked work.
See [Coordinating Work Guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/coordinating-work-guidelines.md) for protocol details.

**Next ID:** 0012

## Next Milestone

*(Currently no tasks)*

## Backlog

- [ ] A0005 [owner: @gio] Add a starter logging module implementing CLAUDE.md's Logging section (severity tags, file+stdout split, start/end messages), mirroring hinolugi-support.python's `logging.py` so downstream projects stop reimplementing it.
- [ ] A0006 [owner: @gio] Add a release/publish GitHub Actions workflow (trigger on `release: published`, build sdist/wheel, upload to the release) plus a README "installing from a release" section, mirroring hinolugi-support.python's `publish.yml`.
- [ ] A0007 [owner: @gio] Scaffold `docs/specs/`, `docs/adrs/`, and `docs/issues/` placeholders and link them from `docs/index.md`; dev-guidelines mandates them but the template's docs/index.md doesn't mention any of the three.
- [ ] A0008 [owner: @gio] Scaffold a tracked `tasks/` directory (placeholder file) so new projects start with the location coordinating-work-guidelines.md requires for full-task files.
- [ ] A0009 [owner: @gio] Fix `scaffold.py`'s `_reset_pyproject_version` to reset to a `-pre` version (e.g. `0.0.1-pre`) so scaffolded projects start compliant with the versioning guideline instead of needing a later fix-up.
- [ ] A0010 [owner: @gio] Decide whether to standardize the build backend (setuptools vs. hatchling) and a default `[tool.ruff.lint] select` list across template-derived projects; hinolugi-support.python diverges from the template on both.
- [ ] A0011 [owner: @gio] Decide whether to document an optional `scripts/` convention for non-packaged dev/maintenance tooling, as used in mail-utils, in `docs/devops.md`.

