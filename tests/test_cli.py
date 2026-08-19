from myproject.cli import main


def test_help_exits_zero(capsys):
    assert main(["help"]) == 0
    assert "usage:" in capsys.readouterr().out


def test_no_args_shows_help(capsys):
    assert main([]) == 0
    assert "usage:" in capsys.readouterr().out


def test_version(capsys):
    assert main(["version"]) == 0
    assert capsys.readouterr().out.strip()


def test_greet(capsys):
    assert main(["greet", "Gio"]) == 0
    assert capsys.readouterr().out.strip() == "Hello, Gio"


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

    releases = (destination / "RELEASES.md").read_text(encoding="utf-8")
    assert "Initial release of the Sample App project." in releases
    assert "ruff" not in releases

    todo = (destination / "TODO.md").read_text(encoding="utf-8")
    assert "github.com/gpellicciotta" not in todo


def test_create_refuses_existing_destination(tmp_path):
    project_name = "dup-app"
    (tmp_path / project_name).mkdir()

    assert main(["create", project_name, "-o", str(tmp_path)]) == 1
