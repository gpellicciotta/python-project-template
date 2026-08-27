# TODO

Shared task index for planned, active, and blocked work.
See [Coordinating Work Guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/coordinating-work-guidelines.md) for protocol details.

**Next ID:** 0003

## Next Milestone

### Backlog

- [ ] A0002 Scope pytest to tests/ so it doesn't collide with sibling task worktrees under work/
      Running `pytest` from the repo root recurses into any active task's worktree under `work/` too
      (per coordinating-work-guidelines.md's `./work/Tnnnn-slug` convention), and since a worktree's
      `tests/*.py` share module names with the primary checkout's own `tests/*.py` (no `__init__.py`
      package markers), pytest's default import mode raises "import file mismatch" collection errors
      instead of running anything - this reproduces on every project generated from this template as
      soon as two task worktrees coexist. Found and fixed in mail-utils (a project generated from this
      template) via `[tool.pytest.ini_options]` `testpaths = ["tests"]` in `pyproject.toml`; port the
      same fix here so new projects don't inherit the bug.
- [ ] A0001 Reconcile the minimum supported Python version between requires-python and CI
      pyproject.toml's `requires-python` says `>=3.10` and docs/devops.md says "Python 3.10+" (the two
      agree with each other), but .github/workflows/ci.yml only ever runs the single job against Python
      3.11 - so 3.10 is formally allowed but never actually verified by CI. Found incidentally while
      auditing mail-utils (a project generated from this template) for the same issue - mail-utils had the
      extra wrinkle of its own docs saying "3.11+", which was the actual bug fixed there; this template
      doesn't have that wrinkle, just the CI-vs-requires-python gap. Since every project generated from
      this template inherits it, worth deciding here once: either add a 3.10 job to the CI matrix, or
      raise requires-python to match what CI actually verifies.
