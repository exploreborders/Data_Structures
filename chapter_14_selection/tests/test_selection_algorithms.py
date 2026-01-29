"""
Tests for Chapter 14: Selection - Finding Order Statistics

Comprehensive tests covering all selection algorithms, edge cases, and correctness verification.
"""

# Add to code directory to path
import sys
import os
import random
import time

# Add chapter code directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.join(current_dir, "..", "code")
sys.path.insert(0, code_dir)

from selection_algorithms import SelectionAlgorithms, SelectionAnalysis


class TestQuickselect:
    """Test quickselect implementations."""

    def test_quickselect_basic(self):
        """Test basic quickselect functionality."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_single_element(self):
        """Test quickselect on single element array."""
        arr = [42]
        result = SelectionAlgorithms.quickselect(arr, 0)
        assert result == 42

    def test_quickselect_two_elements(self):
        """Test quickselect on two element array."""
        arr = [5, 3]
        assert SelectionAlgorithms.quickselect(arr, 0) == 3
        assert SelectionAlgorithms.quickselect(arr, 1) == 5

    def test_quickselect_duplicates(self):
        """Test quickselect with duplicate elements."""
        arr = [3, 1, 4, 1, 5, 1, 9, 2, 6]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_reverse_sorted(self):
        """Test quickselect on reverse sorted array."""
        arr = [9, 6, 5, 4, 3, 2, 1]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_already_sorted(self):
        """Test quickselect on already sorted array."""
        arr = [1, 2, 3, 4, 5, 6, 9]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_strings(self):
        """Test quickselect on strings."""
        arr = ["banana", "apple", "cherry", "date"]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_iterative(self):
        """Test iterative quickselect."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect_iterative(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_random_pivot(self):
        """Test quickselect with random pivot."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect_random_pivot(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_large_array(self):
        """Test quickselect on large array."""
        arr = list(range(1000, 0, -1))  # Reverse sorted large array
        expected_sorted = sorted(arr)

        test_positions = [0, 99, 499, 900, 999]
        for k in test_positions:
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result == expected_sorted[k]

    def test_quickselect_error_handling(self):
        """Test error handling for invalid k values."""
        arr = [1, 2, 3, 4, 5]

        # k too small
        try:
            SelectionAlgorithms.quickselect(arr, -1)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        # k too large
        try:
            SelectionAlgorithms.quickselect(arr, 5)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        # Empty array
        try:
            SelectionAlgorithms.quickselect([], 0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

    def test_median_finding(self):
        """Test median finding."""
        # Odd length
        arr = [1, 3, 5, 7, 9]
        median = SelectionAlgorithms.find_median(arr)
        assert median == 5

        # Even length
        arr = [1, 3, 5, 7]
        median = SelectionAlgorithms.find_median(arr)
        assert median == 3  # Lower median

    def test_percentile_finding(self):
        """Test percentile finding."""
        arr = list(range(1, 101))  # 1 to 100

        assert SelectionAlgorithms.find_percentile(arr, 0) == 1  # 0th percentile
        assert SelectionAlgorithms.find_percentile(arr, 50) == 50  # Median
        assert SelectionAlgorithms.find_percentile(arr, 100) == 100  # 100th percentile

    def test_percentile_error_handling(self):
        """Test percentile error handling."""
        arr = [1, 2, 3]

        try:
            SelectionAlgorithms.find_percentile(arr, -1)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        try:
            SelectionAlgorithms.find_percentile(arr, 101)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        try:
            SelectionAlgorithms.find_percentile([], 50)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

    def test_select_top_k(self):
        """Test selecting top k elements."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        sorted_arr = sorted(arr)

        for k in range(1, len(arr) + 1):
            result = SelectionAlgorithms.select_top_k(arr, k)
            assert len(result) == k
            # All elements in result should be <= k-th smallest
            kth_smallest = sorted_arr[k - 1]
            assert all(x <= kth_smallest for x in result)

    def test_select_top_k_edge_cases(self):
        """Test select_top_k edge cases."""
        arr = [1, 2, 3, 4, 5]

        # k = 0
        result = SelectionAlgorithms.select_top_k(arr, 0)
        assert result == []

        # k >= len(arr)
        result = SelectionAlgorithms.select_top_k(arr, 10)
        assert result == arr

    def test_floating_point_arrays(self):
        """Test selection on floating point arrays."""
        arr = [3.14, 1.41, 2.71, 1.73, 0.58, 9.97, 2.65, 6]
        expected_sorted = sorted(arr)

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert abs(result - expected_sorted[k]) < 1e-10

    def test_custom_objects(self):
        """Test selection on custom comparable objects."""

        class Item:
            def __init__(self, value):
                self.value = value

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
                return f"Item({self.value})"

        arr = [Item(3), Item(1), Item(4), Item(1), Item(5)]
        expected_values = [1, 1, 3, 4, 5]

        for k in range(len(arr)):
            result = SelectionAlgorithms.quickselect(arr, k)
            assert result.value == expected_values[k]


class TestPartitionSchemes:
    """Test partition scheme implementations."""

    def test_lomuto_partition(self):
        """Test Lomuto partition scheme."""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()

        pivot_idx = SelectionAlgorithms._partition_lomuto(arr, 0, len(arr) - 1, 0)
        pivot_value = arr[pivot_idx]

        # Pivot should be in correct position
        assert all(x <= pivot_value for x in arr[:pivot_idx])
        assert all(x >= pivot_value for x in arr[pivot_idx:])

        # All original elements should still be present
        assert sorted(arr) == sorted(original)

    def test_hoare_partition(self):
        """Test Hoare partition scheme."""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()

        pivot_idx = SelectionAlgorithms._partition_hoare(arr, 0, len(arr) - 1)
        pivot_value = arr[pivot_idx]

        # Elements before pivot should be <= pivot, after pivot should be >= pivot
        for i in range(len(arr)):
            if i <= pivot_idx:
                assert arr[i] <= pivot_value
            else:
                assert arr[i] >= pivot_value

        # All original elements should still be present
        assert sorted(arr) == sorted(original)


class TestPivotSelection:
    """Test pivot selection strategies."""

    def test_median_of_three(self):
        """Test median-of-three pivot selection."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        # Test on various subarrays
        for end in range(3, len(arr)):
            subarr = arr[:end]
            if len(subarr) >= 3:
                pivot_idx = SelectionAlgorithms._choose_pivot_median_of_three(
                    subarr, 0, len(subarr) - 1
                )

                # Pivot index should be valid
                assert 0 <= pivot_idx < len(subarr)

    def test_median_of_three_small_array(self):
        """Test median-of-three on small arrays."""
        # Two elements
        arr = [3, 1]
        pivot_idx = SelectionAlgorithms._choose_pivot_median_of_three(arr, 0, 1)
        assert 0 <= pivot_idx <= 1

        # Three elements
        arr = [3, 1, 2]
        pivot_idx = SelectionAlgorithms._choose_pivot_median_of_three(arr, 0, 2)
        assert 0 <= pivot_idx <= 2

    def test_random_pivot(self):
        """Test random pivot selection."""
        arr = [3, 1, 4, 1, 5]

        # Test multiple times to ensure randomness
        indices = set()
        for _ in range(20):
            pivot_idx = SelectionAlgorithms._choose_pivot_random(arr, 0, len(arr) - 1)
            assert 0 <= pivot_idx < len(arr)
            indices.add(pivot_idx)

        # Should get variety
        assert len(indices) > 1


class TestSelectionAnalysis:
    """Test analysis and utility functions."""

    def test_benchmark_algorithms(self):
        """Test benchmarking function."""
        arr = list(range(100))
        k = 50

        results = SelectionAnalysis.benchmark_selection_algorithms(arr, k, num_trials=3)
        required_algorithms = [
            "quickselect",
            "quickselect_iterative",
            "quickselect_random",
        ]

        for algo in required_algorithms:
            assert algo in results
            assert "avg_time" in results[algo]
            assert "result" in results[algo]
            assert results[algo]["result"] == 50  # k-th element in range(100)

    def test_analyze_pivot_quality(self):
        """Test pivot quality analysis."""
        arr = list(range(100))
        k = 50

        results = SelectionAnalysis.analyze_pivot_quality(arr, k, num_trials=10)

        # Check that both strategies were tested
        assert len(results) > 0

        # Check timing information exists for tested strategies
        for strategy in results:
            if "avg_time" in results[strategy]:
                assert "min_time" in results[strategy]
                assert "max_time" in results[strategy]

    def test_correctness_testing(self):
        """Test correctness verification."""
        arr = list(range(10))
        k = 5

        # Test that function runs without error
        result = SelectionAnalysis.test_correctness(arr, k)
        assert isinstance(result, bool)


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
    print("Running Chapter 14 Selection Tests...")
    print("=" * 50)

    test_classes = [
        TestQuickselect,
        TestPartitionSchemes,
        TestPivotSelection,
        TestSelectionAnalysis,
    ]

    for test_class in test_classes:
        if not run_test_class(test_class):
            return False

    print("=" * 50)
    print("All tests passed! ✓")
    return True


if __name__ == "__main__":
    run_all_tests()
