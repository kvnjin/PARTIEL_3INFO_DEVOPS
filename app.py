def add(a, b):
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    return None


def greet(name):
    if name == "":
        return "Hello, World!"
    return "Hello, " + name
