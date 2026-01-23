"""
Tests for Chapter 9: Recursion - Basic Recursive Functions
"""

import unittest
import sys
import os

# Add the code directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from recursive_functions import (
    factorial,
    fibonacci,
    fibonacci_memoized,
    sum_list_recursive,
    reverse_list_recursive,
    binary_search_recursive,
    power,
    gcd,
    count_elements_recursive
)


class TestFactorial(unittest.TestCase):
    """Test cases for factorial function."""

    def test_factorial_zero(self):
        """Test factorial of 0."""
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        """Test factorial of positive numbers."""
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative_raises_error(self):
        """Test that factorial raises error for negative input."""
        with self.assertRaises(ValueError):
            factorial(-1)


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci functions."""

    def test_fibonacci_base_cases(self):
        """Test fibonacci base cases."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_sequence(self):
        """Test fibonacci sequence values."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected_value)

    def test_fibonacci_negative_raises_error(self):
        """Test that fibonacci raises error for negative input."""
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_memoized(self):
        """Test memoized fibonacci matches regular fibonacci."""
        for n in range(15):  # Test reasonable values to avoid exponential time
            with self.subTest(n=n):
                self.assertEqual(fibonacci_memoized(n), fibonacci(n))

    def test_fibonacci_memoized_large(self):
        """Test memoized fibonacci can handle larger values efficiently."""
        # This would be very slow without memoization
        result = fibonacci_memoized(35)
        self.assertEqual(result, 9227465)


class TestSumListRecursive(unittest.TestCase):
    """Test cases for sum_list_recursive function."""

    def test_sum_empty_list(self):
        """Test sum of empty list."""
        self.assertEqual(sum_list_recursive([]), 0)

    def test_sum_single_element(self):
        """Test sum of single element list."""
        self.assertEqual(sum_list_recursive([5]), 5)

    def test_sum_multiple_elements(self):
        """Test sum of multiple elements."""
        self.assertEqual(sum_list_recursive([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list_recursive([10, -5, 3]), 8)

    def test_sum_floats(self):
        """Test sum with floating point numbers."""
        self.assertAlmostEqual(sum_list_recursive([1.5, 2.5, 3.0]), 7.0)


class TestReverseListRecursive(unittest.TestCase):
    """Test cases for reverse_list_recursive function."""

    def test_reverse_empty_list(self):
        """Test reverse of empty list."""
        self.assertEqual(reverse_list_recursive([]), [])

    def test_reverse_single_element(self):
        """Test reverse of single element list."""
        self.assertEqual(reverse_list_recursive([1]), [1])

    def test_reverse_multiple_elements(self):
        """Test reverse of multiple elements."""
        self.assertEqual(reverse_list_recursive([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list_recursive(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_reverse_preserves_original(self):
        """Test that original list is not modified."""
        original = [1, 2, 3]
        result = reverse_list_recursive(original)
        self.assertEqual(original, [1, 2, 3])  # Original unchanged
        self.assertEqual(result, [3, 2, 1])     # Result is reversed


class TestBinarySearchRecursive(unittest.TestCase):
    """Test cases for binary_search_recursive function."""

    def test_search_empty_list(self):
        """Test search in empty list."""
        self.assertEqual(binary_search_recursive([], 5), -1)

    def test_search_single_element_found(self):
        """Test search single element - found."""
        self.assertEqual(binary_search_recursive([5], 5), 0)

    def test_search_single_element_not_found(self):
        """Test search single element - not found."""
        self.assertEqual(binary_search_recursive([5], 3), -1)

    def test_search_multiple_elements(self):
        """Test search in larger sorted lists."""
        arr = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(binary_search_recursive(arr, 5), 2)
        self.assertEqual(binary_search_recursive(arr, 1), 0)
        self.assertEqual(binary_search_recursive(arr, 13), 6)
        self.assertEqual(binary_search_recursive(arr, 4), -1)
        self.assertEqual(binary_search_recursive(arr, 15), -1)

    def test_search_with_duplicates(self):
        """Test search when element appears multiple times."""
        arr = [1, 3, 3, 3, 7, 9]
        # Should return one valid index (implementation dependent which one)
        index = binary_search_recursive(arr, 3)
        self.assertIn(index, [1, 2, 3])


class TestPower(unittest.TestCase):
    """Test cases for power function."""

    def test_power_zero_exponent(self):
        """Test power with exponent 0."""
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 0), 1)  # 0^0 is typically defined as 1

    def test_power_positive_exponent(self):
        """Test power with positive exponents."""
        self.assertEqual(power(2, 1), 2)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(5, 3), 125)

    def test_power_base_one(self):
        """Test power with base 1."""
        self.assertEqual(power(1, 10), 1)

    def test_power_base_zero(self):
        """Test power with base 0."""
        self.assertEqual(power(0, 5), 0)

    def test_power_negative_exponent_raises_error(self):
        """Test that power raises error for negative exponent."""
        with self.assertRaises(ValueError):
            power(2, -1)


class TestGCD(unittest.TestCase):
    """Test cases for gcd function."""

    def test_gcd_basic(self):
        """Test basic GCD calculations."""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 75), 25)
        self.assertEqual(gcd(17, 13), 1)  # Coprime
        self.assertEqual(gcd(24, 24), 24)  # Same number

    def test_gcd_with_zero(self):
        """Test GCD with zero."""
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 15), 15)


class TestCountElementsRecursive(unittest.TestCase):
    """Test cases for count_elements_recursive function."""

    def test_count_empty_list(self):
        """Test count of empty list."""
        self.assertEqual(count_elements_recursive([]), 0)

    def test_count_single_element(self):
        """Test count of single element list."""
        self.assertEqual(count_elements_recursive([1]), 1)

    def test_count_multiple_elements(self):
        """Test count of multiple elements."""
        self.assertEqual(count_elements_recursive([1, 2, 3, 4]), 4)
        self.assertEqual(count_elements_recursive(['a', 'b', 'c']), 3)

    def test_count_with_nested_lists(self):
        """Test that nested lists count as single elements."""
        self.assertEqual(count_elements_recursive([[1, 2], [3, 4]]), 2)


if __name__ == '__main__':
    unittest.main()</content>
<parameter name="filePath">chapter_9_recursion/tests/test_recursive_functions.py