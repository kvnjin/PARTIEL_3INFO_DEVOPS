def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(4, 2) == 2


def test_greet():
    assert greet("Alice") == "Hello, Alice"
    assert greet("") == "Hello, World!"
