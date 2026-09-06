# Requirements

Functional and technical requirements for the `python-project-template` repository.

---

## High-Level Goals

- Provide a clean, modern template to start Python projects quickly using the standard `src/` layout.
- Include out-of-the-box support for testing (`pytest`), linting and formatting (`ruff`), packaging (`build`/`wheel`), and CI (`GitHub Actions`).
- Follow cross-project [Development Guidelines](https://github.com/gpellicciotta/dev-guidelines), including task coordination, documentation standards, and CLI conventions.
- Provide an automated scaffolding command (`myproject create <project-name>`) to clone and rename the template into a fresh, independent project with its own clean history and configuration.

---

## Functional Requirements

### Template Structure and Scaffolding
- Support the standard `src/{{package_name}}/` layout to avoid import conflicts during testing.
- Include a built-in `create` subcommand (`myproject create <project-name> [-o <output-dir>]`) that:
  - Validates and derives valid Python package names from project slugs.
  - Copies template files while excluding cache/build artifacts.
  - Rewrites placeholders (`template-project`, `python-template-project`, `myproject`, title) across documentation and configuration.
  - Initializes fresh `CHANGELOG.md` and `TODO.md` files and resets version to `0.0.1` in `pyproject.toml`.
  - Refuses to overwrite existing target directories.

### Command Line Interface (CLI)
- Provide an action-oriented, subcommand-based CLI:
  - `myproject help` / `-h` / `--help`: displays standardized multi-line help with usage, subcommands, options, and exit codes (supports `--verbose` for detailed usage).
  - `myproject version` / `--version`: outputs `{name} v{version} - {copyright}` and exits with code 0.
  - `myproject greet <name>`: sample business logic command demonstrating subcommands and arguments.
  - `myproject create <project-name>`: project scaffolding subcommand.
- Maintain consistent exit codes across all commands:
  - `0`: Success.
  - `1`: Application or command execution failure.
  - `2`: Invalid command-line arguments.

---

## Technical Requirements

- **Python Version**: Python >=3.10.
- **Packaging**: Standard `pyproject.toml` with `setuptools.build_meta` backend.
- **Code Quality**:
  - Code formatted and linted with `ruff` (132-character line length).
  - Editor settings configured via `.editorconfig` (4 spaces, UTF-8, LF line endings).
- **Testing**: Test suite run via `pytest` covering core logic, CLI subcommands, options, exit codes, and scaffolding behavior.
- **Portability**: Cross-platform support for Windows, Linux, and macOS.
- **Documentation**: All documentation written in US English and Markdown, adhering to [Markdown Guidelines](https://github.com/gpellicciotta/dev-guidelines/blob/main/guidelines/markdown-guidelines.md).
