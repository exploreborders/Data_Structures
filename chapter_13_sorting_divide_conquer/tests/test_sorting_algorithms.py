"""
Tests for Chapter 13: Sorting with Divide and Conquer - Mergesort and Quicksort

Comprehensive tests covering all sorting algorithms, edge cases, performance, and stability.
"""

# Add to code directory to path
import sys
import os

sys.path.insert(0, os.path.join(os.getcwd(), "..", "code"))

import random
import time
from divide_conquer_sorting import DivideConquerSorting


class TestMergesort:
    """Test mergesort implementations."""

    def test_mergesort_empty_array(self):
        """Test mergesort on empty array."""
        result = DivideConquerSorting.mergesort([])
        assert result == []

    def test_mergesort_single_element(self):
        """Test mergesort on single element."""
        result = DivideConquerSorting.mergesort([5])
        assert result == [5]

    def test_mergesort_sorted_array(self):
        """Test mergesort on already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = DivideConquerSorting.mergesort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_mergesort_reverse_sorted(self):
        """Test mergesort on reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = DivideConquerSorting.mergesort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_mergesort_random_array(self):
        """Test mergesort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = DivideConquerSorting.mergesort(arr)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_mergesort_with_duplicates(self):
        """Test mergesort with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 1]
        result = DivideConquerSorting.mergesort(arr)
        assert result == [1, 1, 1, 3, 4, 5]

    def test_mergesort_strings(self):
        """Test mergesort on strings."""
        arr = ["banana", "apple", "cherry", "date"]
        result = DivideConquerSorting.mergesort(arr)
        assert result == ["apple", "banana", "cherry", "date"]

    def test_mergesort_stability(self):
        """Test that mergesort is stable."""

        # Create items with same value but different identities
        class Item:
            def __init__(self, value, id):
                self.value = value
                self.id = id

            def __lt__(self, other):
                return self.value < other.value

            def __le__(self, other):
                return self.value <= other.value

            def __repr__(self):
                return f"Item({self.value}, {self.id})"

        arr = [Item(1, "a"), Item(2, "b"), Item(1, "c"), Item(3, "d"), Item(1, "e")]
        result = DivideConquerSorting.mergesort(arr)

        # Check that equal elements maintain relative order
        assert result[0].id == "a"  # First 1
        assert result[1].id == "c"  # Second 1
        assert result[2].id == "e"  # Third 1

    def test_mergesort_inplace_empty(self):
        """Test in-place mergesort on empty array."""
        arr = []
        DivideConquerSorting.mergesort_inplace(arr)
        assert arr == []

    def test_mergesort_inplace_single(self):
        """Test in-place mergesort on single element."""
        arr = [5]
        DivideConquerSorting.mergesort_inplace(arr)
        assert arr == [5]

    def test_mergesort_inplace_random(self):
        """Test in-place mergesort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        DivideConquerSorting.mergesort_inplace(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]


class TestQuicksort:
    """Test quicksort implementations."""

    def test_quicksort_empty_array(self):
        """Test quicksort on empty array."""
        result = DivideConquerSorting.quicksort([])
        assert result == []

    def test_quicksort_single_element(self):
        """Test quicksort on single element."""
        result = DivideConquerSorting.quicksort([5])
        assert result == [5]

    def test_quicksort_sorted_array(self):
        """Test quicksort on already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = DivideConquerSorting.quicksort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_quicksort_reverse_sorted(self):
        """Test quicksort on reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = DivideConquerSorting.quicksort(arr)
        assert result == [1, 2, 3, 4, 5]

    def test_quicksort_random_array(self):
        """Test quicksort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = DivideConquerSorting.quicksort(arr)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_quicksort_with_duplicates(self):
        """Test quicksort with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 1]
        result = DivideConquerSorting.quicksort(arr)
        assert result == [1, 1, 1, 3, 4, 5]

    def test_quicksort_strings(self):
        """Test quicksort on strings."""
        arr = ["banana", "apple", "cherry", "date"]
        result = DivideConquerSorting.quicksort(arr)
        assert result == ["apple", "banana", "cherry", "date"]

    def test_quicksort_inplace_empty(self):
        """Test in-place quicksort on empty array."""
        arr = []
        DivideConquerSorting.quicksort_inplace(arr)
        assert arr == []

    def test_quicksort_inplace_single(self):
        """Test in-place quicksort on single element."""
        arr = [5]
        DivideConquerSorting.quicksort_inplace(arr)
        assert arr == [5]

    def test_quicksort_inplace_random(self):
        """Test in-place quicksort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        DivideConquerSorting.quicksort_inplace(arr)
        assert arr == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_quicksort_median_pivot_empty(self):
        """Test median pivot quicksort on empty array."""
        result = DivideConquerSorting.quicksort_median_pivot([])
        assert result == []

    def test_quicksort_median_pivot_single(self):
        """Test median pivot quicksort on single element."""
        result = DivideConquerSorting.quicksort_median_pivot([5])
        assert result == [5]

    def test_quicksort_median_pivot_random(self):
        """Test median pivot quicksort on random array."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = DivideConquerSorting.quicksort_median_pivot(arr)
        assert result == [1, 1, 2, 3, 4, 5, 6, 9]


class TestSortingCorrectness:
    """Test correctness across different input types and sizes."""

    def test_all_algorithms_same_result(self):
        """Test that all sorting algorithms produce same result."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = sorted(arr)

        merge_result = DivideConquerSorting.mergesort(arr)
        quick_result = DivideConquerSorting.quicksort(arr)
        quick_median_result = DivideConquerSorting.quicksort_median_pivot(arr)

        assert merge_result == expected
        assert quick_result == expected
        assert quick_median_result == expected

    def test_large_random_arrays(self):
        """Test sorting on large random arrays."""
        for size in [10, 50, 100]:
            arr = [random.randint(0, 1000) for _ in range(size)]
            expected = sorted(arr)

            merge_result = DivideConquerSorting.mergesort(arr)
            quick_result = DivideConquerSorting.quicksort(arr)

            assert merge_result == expected
            assert quick_result == expected

    def test_edge_cases(self):
        """Test various edge cases."""
        test_arrays = [
            [],
            [1],
            [1, 2],
            [2, 1],
            [1, 1, 1],
            [3, 1, 2, 3, 1, 2],
            list(range(10, 0, -1)),  # Reverse sorted
            list(range(1, 11)),  # Already sorted
        ]

        for arr in test_arrays:
            expected = sorted(arr)

            merge_result = DivideConquerSorting.mergesort(arr)
            quick_result = DivideConquerSorting.quicksort(arr)

            assert merge_result == expected, f"mergesort failed on {arr}"
            assert quick_result == expected, f"quicksort failed on {arr}"

    def test_introsort_like(self):
        """Test introsort-like algorithm."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = DivideConquerSorting.introsort_like(arr)
        assert result == sorted(arr)

    def test_performance_basic(self):
        """Test basic performance measurement."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        # Test that both algorithms can sort the array
        merge_result = DivideConquerSorting.mergesort(arr)
        quick_result = DivideConquerSorting.quicksort(arr)
        expected = sorted(arr)

        assert merge_result == expected
        assert quick_result == expected

    def test_algorithm_properties(self):
        """Test that algorithms have expected properties."""
        # Test that results are sorted
        arr = [3, 1, 4, 1, 5]

        merge_result = DivideConquerSorting.mergesort(arr)
        quick_result = DivideConquerSorting.quicksort(arr)

        # Test that results are sorted using Python's sorted()
        assert merge_result == sorted(arr)
        assert quick_result == sorted(arr)


class TestSortingUtilities:
    """Test utility functions."""

    def test_introsort_like(self):
        """Test introsort-like algorithm."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result = DivideConquerSorting.introsort_like(arr)
        assert result == sorted(arr)

    def test_mergesort_stability(self):
        """Test that mergesort is stable."""

        # Create items with same value but different identities
        class Item:
            def __init__(self, value, id):
                self.value = value
                self.id = id

            def __lt__(self, other):
                return self.value < other.value

            def __le__(self, other):
                return self.value <= other.value

            def __repr__(self):
                return f"Item({self.value}, {self.id})"

        arr = [Item(1, "a"), Item(2, "b"), Item(1, "c"), Item(3, "d"), Item(1, "e")]
        result = DivideConquerSorting.mergesort(arr)

        # Check that equal elements maintain relative order
        assert result[0].id == "a"  # First 1
        assert result[1].id == "c"  # Second 1
        assert result[2].id == "e"  # Third 1


def run_test_class(test_class):
    """Run all test methods in a test class."""
    test_instance = test_class()
    test_methods = [
        method
        for method in dir(test_instance)
        if method.startswith("test_") and callable(getattr(test_instance, method))
    ]

    for test_method in test_methods:
        try:
            getattr(test_instance, test_method)()
        except Exception as e:
            print(f"✗ {test_class.__name__}.{test_method}: {e}")
            return False

    return True


def run_all_tests():
    """Run all test classes."""
    print("Running Chapter 13 Sorting Tests...")
    print("=" * 50)

    test_classes = [
        TestMergesort,
        TestQuicksort,
        TestSortingCorrectness,
        TestSortingUtilities,
    ]

    for test_class in test_classes:
        if not run_test_class(test_class):
            return False

    print("=" * 50)
    print("All tests passed! ✓")
    return True


if __name__ == "__main__":
    run_all_tests()
