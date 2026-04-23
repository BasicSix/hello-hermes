#!/usr/bin/env python3
"""
Hello Hermes - A simple Python module demonstrating Hermes agent capabilities.
"""

import math
from typing import List, Union


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.
    
    This function computes the arithmetic mean by summing all elements
    and dividing by the count. It's useful for basic statistical calculations
    and data analysis tasks.
    
    Args:
        numbers: List of integers or floats to calculate average for
        
    Returns:
        The arithmetic mean as a float
        
    Raises:
        ValueError: If the input list is empty (no valid average)
        
    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10, 20, 30])
        20.0
        
    Time Complexity: O(n) where n is the length of the input list
    Space Complexity: O(1) - only uses constant extra space
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def fibonacci(n: int) -> List[int]:
    """
    Generate Fibonacci sequence up to n terms.
    
    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, starting from 0 and 1. This sequence appears
    frequently in nature and has applications in computer science algorithms.
    
    Args:
        n: Number of terms to generate (must be non-negative)
        
    Returns:
        List containing the first n Fibonacci numbers in order
        
    Raises:
        ValueError: If n is negative (no Fibonacci numbers defined for negative indices)
        
    Examples:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
        
    Time Complexity: O(n) - generates each term once
    Space Complexity: O(n) - stores all n terms in memory
    
    Note:
        The sequence starts with F(0)=0, F(1)=1, so fibonacci(1) returns [0]
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
    Calculate factorial of n (n! = n × (n-1) × ... × 2 × 1).
    
    The factorial function is fundamental in combinatorics, probability theory,
    and algorithm analysis. It represents the number of ways to arrange n distinct
    items in a sequence.
    
    Args:
        n: Non-negative integer to calculate factorial for
        
    Returns:
        Factorial of n as an integer
        
    Raises:
        ValueError: If n is negative (factorial undefined for negative numbers)
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        
    Time Complexity: O(n) - multiplies n numbers together
    Space Complexity: O(1) - iterative implementation uses constant space
    
    Special Cases:
        - factorial(0) = 1 (by mathematical convention)
        - factorial(1) = 1
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