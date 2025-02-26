def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    """Multiplie deux nombres."""
    return x * y


def divide(x, y):
    """Divise deux nombres si le diviseur n'est pas zéro."""
    beta = 0
    if y != 0:
        return x / y
    return None

def greet(name):
    """Retourne un message de salutation."""
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name
