# DevOps and Operations

Practical guidance on development environment setup, testing, validation, builds, and operations for `python-project-template`.

---

## Prerequisites and Environment

- **Python**: Python 3.10+
- **Git**: Git 2.30+ supporting worktrees (`git worktree`)
- **Shell**: PowerShell (Windows) or POSIX shell (Linux/macOS)

---

## Setup and Development Workflows

### Initial Bootstrap (PowerShell)
To initialize git, create the virtual environment, install in editable mode with dev tools, lint, run tests, and build:

```powershell
. .\setup.ps1
```

### Manual Setup
```bash
# Create and activate virtual environment
python -m venv .venv

# Windows activation
.venv\Scripts\Activate.ps1

# Linux/macOS activation
source .venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### Task Coordination Protocol
All active work follows the protocol defined in [Coordinating Work Guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/coordinating-work-guidelines.md):
1. **Claim**: Fetch mainline, update `TODO.md` with `@owner` and `[~]`, commit, and push immediately (first fast-forward push wins).
2. **Isolate** (full tasks `Tnnnn` only): Create a worktree at `./work/Tnnnn-slug` on branch `task/Tnnnn-slug` with a task file at `tasks/Tnnnn-slug.md`. Adhoc tasks (`Annnn`) skip this and work directly in the primary checkout.
3. **Execute**: Develop and, for full tasks, document progress in the task file's Execution Log.
4. **Finalize**: Run validation checks, update `CHANGELOG.md`, remove the task entry from `TODO.md`, integrate in a single mainline commit, and clean up any worktree/branch.
5. **Review**: Satisfy the applicable tier before merging — PR approval, peer sign-off, solo-agent summary with human permission, or pre-authorized autonomous-loop integration.

---

## Testing and Code Quality

### Running Tests
```bash
.venv\Scripts\python -m pytest
```

### Linting and Formatting
```bash
.venv\Scripts\ruff check .
.venv\Scripts\ruff format --check .

# To automatically apply formatting and safe fixes:
.venv\Scripts\ruff check --fix .
.venv\Scripts\ruff format .
```

---

## Development and Maintenance Scripts

An optional root `scripts/` directory houses non-packaged development and maintenance tooling.
These standalone scripts remain separate from the installable package and automated test suites.
Projects such as `mail-utils` use this convention for bootstrap scripts, roundtrip testing, and migrations.

### Purpose and Scope
Use `scripts/` for operational tasks that support developers rather than packaged library users:
- Environment bootstrapping and dev setup automation.
- Specialized test harnesses and roundtrip verification suites.
- Adhoc data migrations, database maintenance, and repair utilities.
- Test fixture generation and synthetic benchmark data creation.
- Shared internal CLI utilities supporting standalone scripts.

### Script Conventions
Follow standard project conventions when adding tools under `scripts/`:
- Keep scripts standalone and executable directly with Python.
- Structure command-line interfaces around action-oriented subcommands.
- Standardize version and help output per cross-project [CLI guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/general-guidelines.md#cli).
- Return explicit exit codes indicating success or failure.
- Prefix non-executable shared modules with an underscore, such as `_cli_common.py`.
- Lint and format scripts with `ruff` alongside application code.

### Execution
Run scripts directly using the virtual environment interpreter:

```powershell
python scripts/<script-name>.py --help
```

---

## Build and Distribution

To build source distributions (`sdist`) and wheels (`bdist_wheel`):

```bash
python -m build
```

Built packages are written to `dist/` (or `bin/distributions/` if using `setup.ps1`).

---

## Release Process

Ongoing work accumulates under the top `CHANGELOG.md` heading while it carries a `-pre` SemVer suffix (e.g.
`## v1.3.1-pre`), which must always match `version` in `pyproject.toml` (the single source of truth) exactly,
`-pre` included.

1. Confirm the top `CHANGELOG.md` heading's version and `pyproject.toml`'s `version` already agree.
2. Freeze: replace the heading's `-pre` suffix with `[{{date}}]`, and drop `-pre` from `pyproject.toml`'s
   `version` so both again match exactly. In the same commit, add the next patch version's `## vX.Y.Z-pre`
   heading above it, but leave `pyproject.toml`'s `version` at the bare frozen version — bumping it to the next
   `-pre` now would make the following publish step publish the wrong version. Only bump `pyproject.toml` to the next
   `-pre` in the first real commit of the next dev cycle.
3. Perform a clean verification build:
   ```powershell
   .venv\Scripts\python -m pytest && .venv\Scripts\python -m build
   ```
4. Commit the changes and tag the release commit.
5. Publish a GitHub Release for the tag; `.github/workflows/publish.yml` builds distribution packages and attaches them to the release.

---

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/ci.yml` runs on every push and pull request to validate:
- Python environment setup.
- Editable installation with dev dependencies.
- Code linting and formatting via `ruff`.
- Automated test suite execution via `pytest`.
- Package build via `build`.

When a release is published on GitHub, `.github/workflows/publish.yml` triggers to build sdist and wheel packages and attach them as downloadable release assets.
