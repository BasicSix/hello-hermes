"""
Utility functions for hello-hermes project
"""

def calculate_average(numbers):
    """Calculate average of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        float: Average value

    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms.

    Args:
        n: Number of terms to generate

    Returns:
        list: Fibonacci sequence

    Example:
        >>> fibonacci(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    while len(sequence) < n:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

def factorial(n):
    """Calculate factorial of n.

    Args:
        n: Non-negative integer

    Returns:
        int: Factorial result

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result