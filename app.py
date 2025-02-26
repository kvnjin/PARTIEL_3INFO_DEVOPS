from app import add, multiply, divide, greet


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) is None


def test_greet():
    assert greet("") == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"


# Add two blank lines after the last function