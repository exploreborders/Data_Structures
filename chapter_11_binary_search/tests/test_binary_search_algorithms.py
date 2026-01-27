"""
Tests for Chapter 11: Binary Search - Efficient Search Algorithms
"""

import unittest
import math
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from binary_search_algorithms import BinarySearch, BinarySearchApplications, AdvancedSearch


class TestBinarySearch(unittest.TestCase):
    """Test cases for basic binary search algorithms."""

    def setUp(self):
        """Set up test data."""
        self.sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.duplicate_array = [1, 3, 3, 3, 5, 5, 7, 9, 9, 9]

    def test_binary_search_iterative_found(self):
        """Test iterative binary search - element found."""
        for i, val in enumerate(self.sorted_array):
            with self.subTest(value=val):
                result = BinarySearch.binary_search_iterative(self.sorted_array, val)
                self.assertEqual(result, i)

    def test_binary_search_iterative_not_found(self):
        """Test iterative binary search - element not found."""
        not_found_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        for val in not_found_values:
            with self.subTest(value=val):
                result = BinarySearch.binary_search_iterative(self.sorted_array, val)
                self.assertEqual(result, -1)

    def test_binary_search_recursive_found(self):
        """Test recursive binary search - element found."""
        for i, val in enumerate(self.sorted_array):
            with self.subTest(value=val):
                result = BinarySearch.binary_search_recursive(self.sorted_array, val)
                self.assertEqual(result, i)

    def test_binary_search_recursive_not_found(self):
        """Test recursive binary search - element not found."""
        not_found_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        for val in not_found_values:
            with self.subTest(value=val):
                result = BinarySearch.binary_search_recursive(self.sorted_array, val)
                self.assertEqual(result, -1)

    def test_binary_search_edge_cases(self):
        """Test binary search edge cases."""
        # Empty array
        self.assertEqual(BinarySearch.binary_search_iterative([], 5), -1)
        self.assertEqual(BinarySearch.binary_search_recursive([], 5), -1)

        # Single element - found
        self.assertEqual(BinarySearch.binary_search_iterative([5], 5), 0)
        self.assertEqual(BinarySearch.binary_search_recursive([5], 5), 0)

        # Single element - not found
        self.assertEqual(BinarySearch.binary_search_iterative([5], 3), -1)
        self.assertEqual(BinarySearch.binary_search_recursive([5], 3), -1)

        # Two elements
        arr = [1, 3]
        self.assertEqual(BinarySearch.binary_search_iterative(arr, 1), 0)
        self.assertEqual(BinarySearch.binary_search_iterative(arr, 3), 1)
        self.assertEqual(BinarySearch.binary_search_iterative(arr, 2), -1)


class TestBinarySearchVariants(unittest.TestCase):
    """Test cases for binary search variants."""

    def setUp(self):
        """Set up test data."""
        self.duplicate_array = [1, 3, 3, 3, 5, 5, 7, 9, 9, 9]
        self.unique_array = [1, 3, 5, 7, 9, 11, 13, 15]

    def test_find_first_occurrence(self):
        """Test finding first occurrence of duplicates."""
        # Test with duplicates
        self.assertEqual(BinarySearch.find_first_occurrence(self.duplicate_array, 3), 1)
        self.assertEqual(BinarySearch.find_first_occurrence(self.duplicate_array, 5), 4)
        self.assertEqual(BinarySearch.find_first_occurrence(self.duplicate_array, 9), 7)

        # Test with unique values
        self.assertEqual(BinarySearch.find_first_occurrence(self.unique_array, 5), 2)
        self.assertEqual(BinarySearch.find_first_occurrence(self.unique_array, 1), 0)

        # Test not found
        self.assertEqual(BinarySearch.find_first_occurrence(self.duplicate_array, 4), -1)
        self.assertEqual(BinarySearch.find_first_occurrence(self.unique_array, 10), -1)

    def test_find_last_occurrence(self):
        """Test finding last occurrence of duplicates."""
        # Test with duplicates
        self.assertEqual(BinarySearch.find_last_occurrence(self.duplicate_array, 3), 3)
        self.assertEqual(BinarySearch.find_last_occurrence(self.duplicate_array, 5), 5)
        self.assertEqual(BinarySearch.find_last_occurrence(self.duplicate_array, 9), 9)

        # Test with unique values
        self.assertEqual(BinarySearch.find_last_occurrence(self.unique_array, 5), 2)
        self.assertEqual(BinarySearch.find_last_occurrence(self.unique_array, 15), 7)

        # Test not found
        self.assertEqual(BinarySearch.find_last_occurrence(self.duplicate_array, 4), -1)
        self.assertEqual(BinarySearch.find_last_occurrence(self.unique_array, 10), -1)

    def test_lower_bound(self):
        """Test lower bound (insertion point)."""
        arr = [1, 3, 5, 7, 9]

        # Test existing elements
        self.assertEqual(BinarySearch.lower_bound(arr, 1), 0)
        self.assertEqual(BinarySearch.lower_bound(arr, 3), 1)
        self.assertEqual(BinarySearch.lower_bound(arr, 5), 2)
        self.assertEqual(BinarySearch.lower_bound(arr, 9), 4)

        # Test non-existing elements
        self.assertEqual(BinarySearch.lower_bound(arr, 0), 0)  # Insert at beginning
        self.assertEqual(BinarySearch.lower_bound(arr, 2), 1)  # Insert between 1 and 3
        self.assertEqual(BinarySearch.lower_bound(arr, 4), 2)  # Insert between 3 and 5
        self.assertEqual(BinarySearch.lower_bound(arr, 6), 3)  # Insert between 5 and 7
        self.assertEqual(BinarySearch.lower_bound(arr, 8), 4)  # Insert between 7 and 9
        self.assertEqual(BinarySearch.lower_bound(arr, 10), 5) # Insert at end

    def test_upper_bound(self):
        """Test upper bound."""
        arr = [1, 3, 5, 7, 9]

        # Test existing elements
        self.assertEqual(BinarySearch.upper_bound(arr, 1), 1)
        self.assertEqual(BinarySearch.upper_bound(arr, 3), 2)
        self.assertEqual(BinarySearch.upper_bound(arr, 5), 3)
        self.assertEqual(BinarySearch.upper_bound(arr, 7), 4)
        self.assertEqual(BinarySearch.upper_bound(arr, 9), 5)

        # Test non-existing elements
        self.assertEqual(BinarySearch.upper_bound(arr, 0), 0)
        self.assertEqual(BinarySearch.upper_bound(arr, 2), 1)
        self.assertEqual(BinarySearch.upper_bound(arr, 4), 2)
        self.assertEqual(BinarySearch.upper_bound(arr, 6), 3)
        self.assertEqual(BinarySearch.upper_bound(arr, 8), 4)
        self.assertEqual(BinarySearch.upper_bound(arr, 10), 5)

    def test_count_occurrences(self):
        """Test counting occurrences."""
        # Test with duplicates
        self.assertEqual(BinarySearch.count_occurrences(self.duplicate_array, 3), 3)
        self.assertEqual(BinarySearch.count_occurrences(self.duplicate_array, 5), 2)
        self.assertEqual(BinarySearch.count_occurrences(self.duplicate_array, 9), 3)

        # Test with unique values
        self.assertEqual(BinarySearch.count_occurrences(self.unique_array, 5), 1)
        self.assertEqual(BinarySearch.count_occurrences(self.unique_array, 1), 1)

        # Test not found
        self.assertEqual(BinarySearch.count_occurrences(self.duplicate_array, 4), 0)
        self.assertEqual(BinarySearch.count_occurrences(self.unique_array, 10), 0)


class TestBinarySearchApplications(unittest.TestCase):
    """Test cases for binary search applications."""

    def test_square_root_binary_search(self):
        """Test square root calculation using binary search."""
        test_cases = [
            (0, 0),
            (1, 1),
            (4, 2),
            (9, 3),
            (16, 4),
            (25, 5),
            (2, math.sqrt(2)),
            (3, math.sqrt(3)),
            (10, math.sqrt(10))
        ]

        for x, expected in test_cases:
            with self.subTest(x=x):
                result = BinarySearchApplications.square_root_binary_search(x)
                self.assertAlmostEqual(result, expected, places=5)

        # Test negative input
        with self.assertRaises(ValueError):
            BinarySearchApplications.square_root_binary_search(-1)

    def test_find_peak_element(self):
        """Test finding peak elements."""
        # Single peak
        self.assertEqual(BinarySearchApplications.find_peak_element([1, 3, 2, 1]), 1)

        # Peak at end
        self.assertEqual(BinarySearchApplications.find_peak_element([1, 2, 3, 4]), 3)

        # Peak at beginning
        self.assertEqual(BinarySearchApplications.find_peak_element([4, 3, 2, 1]), 0)

        # Multiple peaks (any valid peak)
        arr = [1, 3, 2, 4, 1]
        peak = BinarySearchApplications.find_peak_element(arr)
        self.assertIn(peak, [1, 3])  # Either index 1 or 3 is valid

        # Single element
        self.assertEqual(BinarySearchApplications.find_peak_element([5]), 0)

        # Two elements
        self.assertEqual(BinarySearchApplications.find_peak_element([1, 2]), 1)
        self.assertEqual(BinarySearchApplications.find_peak_element([2, 1]), 0)

    def test_search_rotated_array(self):
        """Test searching in rotated sorted arrays."""
        # Standard rotated array
        arr = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 0), 4)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 4), 0)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 2), 6)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 3), -1)

        # Not rotated (already sorted)
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 1), 0)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 5), 4)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 0), -1)

        # Rotated by one position
        arr = [5, 1, 2, 3, 4]
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 5), 0)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 1), 1)
        self.assertEqual(BinarySearchApplications.search_rotated_array(arr, 4), 4)

    def test_find_minimum_in_rotated_array(self):
        """Test finding minimum in rotated sorted arrays."""
        # Standard rotated array
        self.assertEqual(BinarySearchApplications.find_minimum_in_rotated_array([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(BinarySearchApplications.find_minimum_in_rotated_array([3, 4, 5, 1, 2]), 1)

        # Not rotated
        self.assertEqual(BinarySearchApplications.find_minimum_in_rotated_array([1, 2, 3, 4, 5]), 1)

        # Rotated by one position
        self.assertEqual(BinarySearchApplications.find_minimum_in_rotated_array([5, 1, 2, 3, 4]), 1)

        # All elements same
        self.assertEqual(BinarySearchApplications.find_minimum_in_rotated_array([3, 3, 3, 3]), 3)


class TestAdvancedSearch(unittest.TestCase):
    """Test cases for advanced search algorithms."""

    def setUp(self):
        """Set up test data."""
        self.sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

    def test_exponential_search(self):
        """Test exponential search."""
        # Test found elements
        for i, val in enumerate(self.sorted_array):
            with self.subTest(value=val):
                result = AdvancedSearch.exponential_search(self.sorted_array, val)
                self.assertEqual(result, i)

        # Test not found elements
        not_found = [0, 2, 4, 6, 8, 10, 30]
        for val in not_found:
            with self.subTest(value=val):
                result = AdvancedSearch.exponential_search(self.sorted_array, val)
                self.assertEqual(result, -1)

    def test_interpolation_search(self):
        """Test interpolation search."""
        # For uniformly distributed data, interpolation search should work well
        uniform_array = list(range(1, 101))  # 1, 2, 3, ..., 100

        # Test some values
        test_values = [1, 25, 50, 75, 100]
        for val in test_values:
            with self.subTest(value=val):
                result = AdvancedSearch.interpolation_search(uniform_array, val)
                self.assertEqual(result, val - 1)  # 0-based indexing

        # Test not found
        self.assertEqual(AdvancedSearch.interpolation_search(uniform_array, 0), -1)
        self.assertEqual(AdvancedSearch.interpolation_search(uniform_array, 101), -1)

    def test_ternary_search(self):
        """Test ternary search."""
        # Test found elements
        for i, val in enumerate(self.sorted_array):
            with self.subTest(value=val):
                result = AdvancedSearch.ternary_search(self.sorted_array, val)
                self.assertEqual(result, i)

        # Test not found elements
        not_found = [0, 2, 4, 6, 8, 10, 30]
        for val in not_found:
            with self.subTest(value=val):
                result = AdvancedSearch.ternary_search(self.sorted_array, val)
                self.assertEqual(result, -1)

    def test_empty_arrays(self):
        """Test all search algorithms with empty arrays."""
        algorithms = [
            BinarySearch.binary_search_iterative,
            BinarySearch.binary_search_recursive,
            BinarySearch.find_first_occurrence,
            BinarySearch.find_last_occurrence,
            AdvancedSearch.exponential_search,
            AdvancedSearch.ternary_search,
        ]

        for algo in algorithms:
            with self.subTest(algorithm=algo.__name__):
                self.assertEqual(algo([], 5), -1)


if __name__ == '__main__':
    unittest.main()
