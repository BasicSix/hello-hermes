#!/usr/bin/env python3
"""
Hello Hermes - A simple Python module demonstrating Hermes agent capabilities.
"""

import math
from typing import List, Union


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of integers or floats
        
    Returns:
        The arithmetic mean as a float
        
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def fibonacci(n: int) -> List[int]:
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n: Number of terms to generate
        
    Returns:
        List containing the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[:n]


def factorial(n: int) -> int:
    """
    Calculate factorial of n (n!).
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


if __name__ == "__main__":
    # Example usage
    print("Hello Hermes!")
    print(f"Average of [1, 2, 3, 4, 5]: {calculate_average([1, 2, 3, 4, 5])}")
    print(f"Fibonacci(8): {fibonacci(8)}")
    print(f"Factorial(5): {factorial(5)}")