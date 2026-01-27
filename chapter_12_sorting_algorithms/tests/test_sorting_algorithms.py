"""
Tests for Chapter 12: Sorting Algorithms - Comprehensive Implementation
"""

import unittest
import random
from typing import List

# Add the code directory to the path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from sorting_algorithms import SortingAlgorithms, SortingAnalysis


class TestSortingAlgorithms(unittest.TestCase):
    """Test cases for all sorting algorithms."""

    def setUp(self):
        """Set up test data."""
        self.small_array = [3, 1, 4, 1, 5]
        self.sorted_small = [1, 1, 3, 4, 5]
        self.duplicate_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        self.sorted_duplicate = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
        self.empty_array = []
        self.single_element = [42]
        self.two_elements = [2, 1]
        self.sorted_two = [1, 2]

    def _test_sorting_algorithm(self, sort_func, arr, expected, *args, **kwargs):
        """Helper to test a sorting algorithm."""
        arr_copy = arr.copy()
        if args or kwargs:
            result = sort_func(arr_copy, *args, **kwargs)
        else:
            result = sort_func(arr_copy)

        # Check if result is sorted
        self.assertTrue(SortingAnalysis.is_sorted(result))

        # Check if result matches expected
        self.assertEqual(result, expected)

        # For in-place sorts, check original array was modified
        if sort_func in [SortingAlgorithms.bubble_sort, SortingAlgorithms.insertion_sort,
                        SortingAlgorithms.selection_sort, SortingAlgorithms.quick_sort,
                        SortingAlgorithms.heap_sort, SortingAlgorithms.timsort_like_sort]:
            self.assertEqual(arr_copy, expected)
        # For merge sort, check new array was returned
        elif sort_func == SortingAlgorithms.merge_sort:
            self.assertIsNot(arr_copy, result)

    def test_bubble_sort(self):
        """Test bubble sort."""
        self._test_sorting_algorithm(SortingAlgorithms.bubble_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.bubble_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.bubble_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.bubble_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.bubble_sort, self.two_elements, self.sorted_two)

    def test_insertion_sort(self):
        """Test insertion sort."""
        self._test_sorting_algorithm(SortingAlgorithms.insertion_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.insertion_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.insertion_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.insertion_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.insertion_sort, self.two_elements, self.sorted_two)

    def test_selection_sort(self):
        """Test selection sort."""
        self._test_sorting_algorithm(SortingAlgorithms.selection_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.selection_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.selection_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.selection_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.selection_sort, self.two_elements, self.sorted_two)

    def test_quick_sort(self):
        """Test quick sort."""
        self._test_sorting_algorithm(SortingAlgorithms.quick_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.quick_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.quick_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.quick_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.quick_sort, self.two_elements, self.sorted_two)

    def test_merge_sort(self):
        """Test merge sort."""
        self._test_sorting_algorithm(SortingAlgorithms.merge_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.merge_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.merge_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.merge_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.merge_sort, self.two_elements, self.sorted_two)

    def test_heap_sort(self):
        """Test heap sort."""
        self._test_sorting_algorithm(SortingAlgorithms.heap_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.heap_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.heap_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.heap_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.heap_sort, self.two_elements, self.sorted_two)

    def test_counting_sort(self):
        """Test counting sort."""
        # Test with small range
        arr = [3, 1, 4, 1, 5]
        expected = [1, 1, 3, 4, 5]
        self._test_sorting_algorithm(SortingAlgorithms.counting_sort, arr, expected, 5)

        # Test with duplicates
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
        self._test_sorting_algorithm(SortingAlgorithms.counting_sort, arr, expected, 9)

        # Test empty array
        self._test_sorting_algorithm(SortingAlgorithms.counting_sort, [], [], 0)

        # Test single element
        self._test_sorting_algorithm(SortingAlgorithms.counting_sort, [5], [5], 5)

    def test_radix_sort(self):
        """Test radix sort."""
        # Test basic case
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        expected = [2, 24, 45, 66, 75, 90, 170, 802]
        self._test_sorting_algorithm(SortingAlgorithms.radix_sort, arr, expected)

        # Test with duplicates
        arr = [100, 10, 1, 100, 10]
        expected = [1, 10, 10, 100, 100]
        self._test_sorting_algorithm(SortingAlgorithms.radix_sort, arr, expected)

        # Test empty array
        self._test_sorting_algorithm(SortingAlgorithms.radix_sort, [], [])

        # Test single element
        self._test_sorting_algorithm(SortingAlgorithms.radix_sort, [42], [42])

    def test_bucket_sort(self):
        """Test bucket sort."""
        # Test with floats in [0, 1)
        arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
        arr_copy = arr.copy()
        result = SortingAlgorithms.bucket_sort(arr_copy)
        self.assertTrue(SortingAnalysis.is_sorted(result))

        # Test empty array
        self.assertEqual(SortingAlgorithms.bucket_sort([]), [])

        # Test single element
        self.assertEqual(SortingAlgorithms.bucket_sort([0.5]), [0.5])

    def test_timsort_like_sort(self):
        """Test timsort-like algorithm."""
        self._test_sorting_algorithm(SortingAlgorithms.timsort_like_sort, self.small_array, self.sorted_small)
        self._test_sorting_algorithm(SortingAlgorithms.timsort_like_sort, self.duplicate_array, self.sorted_duplicate)
        self._test_sorting_algorithm(SortingAlgorithms.timsort_like_sort, self.empty_array, [])
        self._test_sorting_algorithm(SortingAlgorithms.timsort_like_sort, self.single_element, [42])
        self._test_sorting_algorithm(SortingAlgorithms.timsort_like_sort, self.two_elements, self.sorted_two)

    def test_stability_check(self):
        """Test stability of sorting algorithms."""
        # Create array with duplicate values but different original positions
        class Item:
            def __init__(self, value, index):
                self.value = value
                self.index = index
            def __lt__(self, other):
                return self.value < other.value
            def __le__(self, other):
                return self.value <= other.value
            def __gt__(self, other):
                return self.value > other.value
            def __ge__(self, other):
                return self.value >= other.value
            def __eq__(self, other):
                return self.value == other.value
            def __repr__(self):
                return f"Item({self.value}, {self.index})"

        # Merge sort should be stable
        items = [Item(3, 1), Item(1, 2), Item(3, 3), Item(1, 4)]
        result = SortingAlgorithms.merge_sort(items)
        # Check that items with value 1 maintain relative order
        self.assertEqual(result[0].index, 2)  # First 1 should be original index 2
        self.assertEqual(result[1].index, 4)  # Second 1 should be original index 4

    def test_large_arrays(self):
        """Test sorting algorithms with larger arrays."""
        # Generate larger test array
        large_array = SortingAnalysis.generate_test_data(1000, "random")
        expected = sorted(large_array)

        # Test a few key algorithms on larger data
        result = SortingAlgorithms.merge_sort(large_array.copy())
        self.assertEqual(result, expected)

        result = SortingAlgorithms.quick_sort(large_array.copy())
        self.assertEqual(result, expected)

        result = SortingAlgorithms.heap_sort(large_array.copy())
        self.assertEqual(result, expected)

    def test_different_distributions(self):
        """Test sorting with different data distributions."""
        size = 100

        # Test each distribution
        for dist in ["random", "sorted", "reverse", "nearly_sorted"]:
            arr = SortingAnalysis.generate_test_data(size, dist)

            # Test merge sort (always works)
            result = SortingAlgorithms.merge_sort(arr.copy())
            self.assertTrue(SortingAnalysis.is_sorted(result))

            # Test quick sort
            result = SortingAlgorithms.quick_sort(arr.copy())
            self.assertTrue(SortingAnalysis.is_sorted(result))

    def test_performance_analysis(self):
        """Test performance analysis tools."""
        arr = [3, 1, 4, 1, 5]

        # Test timing function
        result, exec_time = SortingAnalysis.time_sorting_algorithm(
            SortingAlgorithms.bubble_sort, arr)
        self.assertTrue(SortingAnalysis.is_sorted(result))
        self.assertIsInstance(exec_time, float)
        self.assertGreaterEqual(exec_time, 0)

        # Test sorted check
        self.assertTrue(SortingAnalysis.is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(SortingAnalysis.is_sorted([1, 3, 2, 4, 5]))

    def test_data_generation(self):
        """Test data generation functions."""
        # Test different distributions
        random_data = SortingAnalysis.generate_test_data(10, "random")
        self.assertEqual(len(random_data), 10)

        sorted_data = SortingAnalysis.generate_test_data(10, "sorted")
        self.assertEqual(sorted_data, list(range(10)))

        reverse_data = SortingAnalysis.generate_test_data(10, "reverse")
        self.assertEqual(reverse_data, list(range(9, -1, -1)))

        nearly_sorted = SortingAnalysis.generate_test_data(100, "nearly_sorted")
        self.assertEqual(len(nearly_sorted), 100)
        # Should be mostly sorted but not perfectly
        self.assertNotEqual(nearly_sorted, sorted(nearly_sorted))


if __name__ == '__main__':
    unittest.main()
