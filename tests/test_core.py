from myproject.core import greet


def test_greet():
    assert greet("Gio") == "Hallo, Gio"
