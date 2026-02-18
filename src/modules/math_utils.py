def add(a, b):
    """Returns sum of two numbers"""
    return a + b


def multiply(a, b):
    """Returns product of two numbers"""
    return a * b


def factorial(n):
    """Returns factorial of a number"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result