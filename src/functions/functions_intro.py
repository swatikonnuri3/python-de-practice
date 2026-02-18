"""
Topic: Functions in Python
Author: Swati Konnuri
"""

def add(a, b):
    return a + b

def greet(name):
    print("Hello", name)

print("Sum:", add(10, 20))
greet("Swati")


def calculate_factorial(n):
    """
    Calculates factorial of a number
    """
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
fact = calculate_factorial(5)
print("Factorial:", fact)
