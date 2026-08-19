from myproject.core import greet


def test_greet():
    assert greet("Gio") == "Hello, Gio"
