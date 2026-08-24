# DevOps and Operations

Practical guidance on development environment setup, testing, validation, builds, and operations for `python-project-template`.

---

## 1. Prerequisites and Environment

- **Python**: Python 3.10+
- **Git**: Git 2.30+ supporting worktrees (`git worktree`)
- **Shell**: PowerShell (Windows) or POSIX shell (Linux/macOS)

---

## 2. Setup and Development Workflows

### 2.1. One-Shot Bootstrap (PowerShell)
To initialize git, create the virtual environment, install in editable mode with dev tools, lint, run tests, and build:

```powershell
. .\setup.ps1
```

### 2.2. Manual Setup
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

### 2.3. Task Coordination Protocol
All active work follows the protocol defined in [Coordinating Work Guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/coordinating-work-guidelines.md):
1. **Claim**: Update `TODO.md` with `@owner` and `[~]`, commit, and push.
2. **Worktree**: Create an isolated worktree at `./work/Tnnnn-slug` on branch `task/Tnnnn-slug`.
3. **Execute**: Develop and document progress inside the worktree in `tasks/Tnnnn-slug.md`.
4. **Finalize**: Run validation checks, complete the task file, merge/integrate, clean up the worktree, and remove the task entry.

---

## 3. Testing and Code Quality

### 3.1. Running Tests
```bash
.venv\Scripts\python -m pytest
```

### 3.2. Linting and Formatting
```bash
.venv\Scripts\ruff check .
.venv\Scripts\ruff format --check .

# To automatically apply formatting and safe fixes:
.venv\Scripts\ruff check --fix .
.venv\Scripts\ruff format .
```

---

## 4. Build and Distribution

To build source distributions (`sdist`) and wheels (`bdist_wheel`):

```bash
python -m build
```

Built packages are written to `dist/` (or `bin/distributions/` if using `setup.ps1`).

---

## 5. Continuous Integration

The GitHub Actions workflow in `.github/workflows/ci.yml` runs on every push and pull request to validate:
- Python environment setup.
- Editable installation with dev dependencies.
- Code linting and formatting via `ruff`.
- Automated test suite execution via `pytest`.
- Package build via `build`.
