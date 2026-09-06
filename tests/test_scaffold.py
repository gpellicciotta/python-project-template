from myproject.scaffold import _ignore


def test_ignore_excludes_logs_and_tool_caches():
    names = ["logs", ".pytest_cache", ".ruff_cache", ".mypy_cache", "src", "pyproject.toml"]
    assert _ignore(".", names) == {"logs", ".pytest_cache", ".ruff_cache", ".mypy_cache"}


def test_ignore_excludes_coverage_files():
    names = [".coverage", ".coverage.host.12345", "htmlcov", "README.md"]
    assert _ignore(".", names) == {".coverage", ".coverage.host.12345", "htmlcov"}
