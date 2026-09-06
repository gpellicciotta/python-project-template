# TODO

An overview of all tasks and their planning.

> Tasks are listed by milestone.  
> See [coordinating work guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/coordinating-work-guidelines.md) for the full coordination protocol.

> Notation:
> - ID: 
>   - `Tnnnn`: full task with `tasks/` file and branch/worktree
>   - `Annnn`: adhoc task with TODO.md line only
> - Status: 
>   - `[ ]` available
>   - `[~]` active / in progress
>   - `[!]` blocked 
>   - `[?]` needs-review
> - Metadata: `[label: value]` immediately following the task ID (e.g. `[owner: name]`, `[needs: Tnnnn]`, `[continue-after: YYYY-MM-DD]`, `[blocked: reason]`).
> - Description: Natural-language sentence ($\le 20$ words once a task file exists; longer/multi-line permitted initially). Slugs are never used in TODO.md.

**Next ID:** 0016

---

## Next Milestone

- [~] A0008 [owner: @gemini] Scaffold a tracked `tasks/` directory (placeholder file) so new projects start with the location coordinating-work-guidelines.md requires for full-task files.
- [ ] A0009 Fix `scaffold.py`'s `_reset_pyproject_version` to reset to a `-pre` version (e.g. `0.0.1-pre`) so scaffolded projects start compliant with the versioning guideline instead of needing a later fix-up.
- [ ] A0010 Standardize on setuptools as the build backend (already used by the template and mail-utils) and add an explicit `[tool.ruff.lint] select = ["E4", "E7", "E9", "F"]` to the template's pyproject.toml, pinning ruff's current default rule set; file a follow-up adhoc task in hinolugi-support.python's own TODO.md to migrate it from hatchling to setuptools for consistency.
- [ ] A0011 Document an optional `scripts/` convention for non-packaged dev/maintenance tooling, as used in mail-utils, in `docs/devops.md`.
- [ ] A0012 [needs: A0011] [needs: A0010] [needs: A0009] [needs: A0008] Make a new v1.3.0 release
- [ ] T0013 [needs: A0012] Review the Python projects hinolugi-support.python and mail-utils and document structural differences from this project: look at it as if these projects should have been started from this project, yet keeping in mind that this is a generic template project: we don't want to include things that are only relevant for 1 particular project. For each major topic, make a separate TODO in the backlog and mark it for review by @gio.

---

## Backlog

*(Currently no tasks)*

