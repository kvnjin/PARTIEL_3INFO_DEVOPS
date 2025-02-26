def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y


def greet(name):
    # GREET FUNCTION
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name

