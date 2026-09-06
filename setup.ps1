# Open PowerShell in project root

# Start the project under version control if it isn't already
if (-not (Test-Path .git)) {
    git init
}

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install the project in editable mode with the dev extra (pytest, ruff, build).
# Editable install is the main dev loop: code changes are picked up immediately,
# no rebuild/reinstall needed.
python -m pip install --upgrade pip
pip install -e ".[dev]"

# Lint
ruff check .
ruff format --check .

# Run unit tests
pytest -q

# Build sdist + wheel (optional - only needed when producing a distributable
# artifact, e.g. to hand someone a .whl or publish to a package index).
# Uses the same ./dist/ output location as a plain `python -m build` and CI.
if (Test-Path ./dist) {
    Remove-Item -Recurse -Force ./dist
}
python -m build
