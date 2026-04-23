#!/usr/bin/env python3
"""Unit tests for hello_hermes module."""

import pytest
from src.hello_hermes import calculate_average, fibonacci, factorial


class TestCalculateAverage:
    """Test cases for calculate_average function."""
    
    def test_average_positive_numbers(self):
        """Test average calculation with positive numbers."""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    def test_average_negative_numbers(self):
        """Test average calculation with negative numbers."""
        assert calculate_average([-1, -2, -3]) == -2.0
    
    def test_average_mixed_numbers(self):
        """Test average calculation with mixed positive and negative numbers."""
        assert calculate_average([-2, 0, 2]) == 0.0
    
    def test_average_single_number(self):
        """Test average calculation with single number."""
        assert calculate_average([42]) == 42.0
    
    def test_average_floats(self):
        """Test average calculation with floating point numbers."""
        assert abs(calculate_average([1.5, 2.5, 3.0]) - 2.333333) < 1e-6
    
    def test_average_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
            calculate_average([])


class TestFibonacci:
    """Test cases for fibonacci function."""
    
    def test_fibonacci_zero_terms(self):
        """Test Fibonacci sequence with zero terms."""
        assert fibonacci(0) == []
    
    def test_fibonacci_one_term(self):
        """Test Fibonacci sequence with one term."""
        assert fibonacci(1) == [0]
    
    def test_fibonacci_two_terms(self):
        """Test Fibonacci sequence with two terms."""
        assert fibonacci(2) == [0, 1]
    
    def test_fibonacci_five_terms(self):
        """Test Fibonacci sequence with five terms."""
        assert fibonacci(5) == [0, 1, 1, 2, 3]
    
    def test_fibonacci_ten_terms(self):
        """Test Fibonacci sequence with ten terms."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci(10) == expected
    
    def test_fibonacci_negative_input_raises_error(self):
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError, match="n must be non-negative"):
            fibonacci(-1)


class TestFactorial:
    """Test cases for factorial function."""
    
    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert factorial(0) == 1
    
    def test_factorial_one(self):
        """Test factorial of one."""
        assert factorial(1) == 1
    
    def test_factorial_five(self):
        """Test factorial of five."""
        assert factorial(5) == 120
    
    def test_factorial_ten(self):
        """Test factorial of ten."""
        assert factorial(10) == 3628800
    
    def test_factorial_negative_raises_error(self):
        """Test that negative input raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)