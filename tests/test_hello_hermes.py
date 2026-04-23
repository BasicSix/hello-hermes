"""
Unit tests for hello-hermes project
"""

import pytest
from hello_hermes.utils import calculate_average, fibonacci, factorial


class TestCalculateAverage:
    """Test cases for calculate_average function"""

    def test_average_basic(self):
        """Test basic average calculation"""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0

    def test_average_empty_list(self):
        """Test empty list returns 0.0"""
        assert calculate_average([]) == 0.0

    def test_average_single_element(self):
        """Test single element list"""
        assert calculate_average([5]) == 5.0

    def test_average_negative_numbers(self):
        """Test negative numbers"""
        assert calculate_average([-1, -2, -3, -4, -5]) == -3.0

    def test_average_mixed_signs(self):
        """Test mixed positive and negative numbers"""
        assert calculate_average([-2, 0, 2]) == 0.0


class TestFibonacci:
    """Test cases for fibonacci function"""

    def test_fibonacci_empty(self):
        """Test empty sequence"""
        assert fibonacci(0) == []

    def test_fibonacci_single(self):
        """Test single element"""
        assert fibonacci(1) == [0]

    def test_fibonacci_two_elements(self):
        """Test two elements"""
        assert fibonacci(2) == [0, 1]

    def test_fibonacci_seven(self):
        """Test seven elements"""
        expected = [0, 1, 1, 2, 3, 5, 8]
        assert fibonacci(7) == expected

    def test_fibonacci_ten(self):
        """Test ten elements"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci(10) == expected


class TestFactorial:
    """Test cases for factorial function"""

    def test_factorial_zero(self):
        """Test factorial of zero"""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one"""
        assert factorial(1) == 1

    def test_factorial_five(self):
        """Test factorial of five"""
        assert factorial(5) == 120

    def test_factorial_ten(self):
        """Test factorial of ten"""
        assert factorial(10) == 3628800

    def test_factorial_negative_error(self):
        """Test that negative number raises ValueError"""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)

    def test_factorial_large_number(self):
        """Test factorial of large number"""
        assert factorial(20) == 2432902008176640000