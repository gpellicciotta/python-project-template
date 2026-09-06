from myproject import __version__
from myproject.cli import main


def test_help_exits_zero(capsys):
    assert main(["help"]) == 0
    out = capsys.readouterr().out
    assert "myproject v" in out
    assert "Usage:" in out
    assert "Exit codes:" in out


def test_help_flags(capsys):
    assert main(["-h"]) == 0
    assert "Usage:" in capsys.readouterr().out

    assert main(["--help"]) == 0
    assert "Usage:" in capsys.readouterr().out


def test_help_verbose(capsys):
    assert main(["help", "--verbose"]) == 0
    out = capsys.readouterr().out
    assert "Actions:" in out
    assert "Options:" in out
    assert "Exit codes:" in out


def test_no_args_shows_help(capsys):
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "Usage:" in out
    assert "Exit codes:" in out


def test_version_action_and_flag(capsys):
    assert main(["version"]) == 0
    out = capsys.readouterr().out.strip()
    assert out == f"myproject v{__version__} - Copyright (c) 2026 Giovanni Pellicciotta"

    assert main(["--version"]) == 0
    out = capsys.readouterr().out.strip()
    assert out == f"myproject v{__version__} - Copyright (c) 2026 Giovanni Pellicciotta"


def test_greet(capsys):
    assert main(["greet", "Gio"]) == 0
    assert capsys.readouterr().out.strip() == "Hello, Gio"

    assert main(["greet"]) == 0
    assert capsys.readouterr().out.strip() == "Hello, wereld"

    assert main(["greet", "Gio", "--verbose"]) == 0
    out = capsys.readouterr().out
    assert "Greeting target: Gio" in out
    assert "Hello, Gio" in out


def test_create_scaffolds_renamed_project(tmp_path):
    project_name = "sample-app"
    assert main(["create", project_name, "-o", str(tmp_path)]) == 0

    destination = tmp_path / project_name
    assert destination.is_dir()
    assert (destination / "src" / "sample_app" / "cli.py").is_file()
    assert [p.name for p in (destination / "src").iterdir() if p.is_dir()] == ["sample_app"]

    pyproject = (destination / "pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "sample-app"' in pyproject
    assert 'version = "0.0.1"' in pyproject
    assert 'sample_app = "sample_app.cli:main"' in pyproject

    readme = (destination / "README.md").read_text(encoding="utf-8")
    assert "Sample App" in readme

    license_file = destination / "LICENSE.md"
    assert license_file.is_file()

    changelog = (destination / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "Initial scaffold of the Sample App project." in changelog
    assert "## v0.0.1-pre" in changelog
    assert "in development" not in changelog
    assert "ruff" not in changelog

    todo = (destination / "TODO.md").read_text(encoding="utf-8")
    assert "**Next ID:** 0001" in todo
    assert "## Next Milestone" in todo
    assert "## Backlog" in todo

    assert (destination / "docs" / "requirements.md").is_file()
    assert (destination / "docs" / "devops.md").is_file()
    assert (destination / "docs" / "index.md").is_file()
    assert (destination / "docs" / "specs" / ".gitkeep").is_file()
    assert (destination / "docs" / "adrs" / ".gitkeep").is_file()
    assert (destination / "docs" / "issues" / ".gitkeep").is_file()
    assert (destination / "tasks" / ".gitkeep").is_file()
    assert [p.name for p in (destination / "tasks").iterdir()] == [".gitkeep"]
    assert (destination / ".github" / "workflows" / "publish.yml").is_file()
    assert "Installing from a release" in readme


def test_create_refuses_existing_destination(tmp_path):
    project_name = "dup-app"
    (tmp_path / project_name).mkdir()

    assert main(["create", project_name, "-o", str(tmp_path)]) == 1


def test_create_missing_project_name(capsys):
    assert main(["create"]) == 2
    assert "error:" in capsys.readouterr().err


def test_invalid_args():
    assert main(["--invalid-option"]) == 2
