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

**Next ID:** 0024

---

## Next Milestone

- [~] A0022 [owner: @claude] Standardize local build distribution output location between setup.ps1 and package build workflows.
- [ ] A0016 Add source directory to pytest pythonpath so tests run against source without prior editable installation.
- [ ] A0017 Declare license file and repository URLs in pyproject.toml and update project scaffolding to rewrite them.
- [ ] A0018 Provide a cross-platform Python bootstrap script to replace setup.ps1
- [ ] A0019 Refactor sample CLI to use hinolugi-support CLI helpers instead of duplicating custom argparse and help boilerplate.
- [ ] A0020 Modernize CI workflow with setup-python v5, explicit read permissions, and distribution artifact archiving.
- [ ] A0021 Add tool caches and coverage files to .gitignore and exclude logs and tool caches during scaffolding.

---

## Backlog

- [ ] A0023 Add scaffolded `scripts/bootstrap-dev-environment.py` and `scripts/deploy-to-production.py` per dev-guidelines' scripts-directory convention, as an example for projects derived from this template that deploy a service; may supersede/inform A0018.

