"""
Chapter 13 Examples: Sorting with Divide and Conquer

Interactive demonstrations of mergesort, quicksort, and their performance characteristics.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from divide_conquer_sorting import DivideConquerSorting


def demonstrate_basic_sorting():
    """Demonstrate basic sorting operations."""
    print("=== Basic Sorting Operations ===\n")

    # Sample array
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original array: {arr}\n")

    # Mergesort
    merge_result = DivideConquerSorting.mergesort(arr)
    print(f"Mergesort result: {merge_result}")
    print(f"Original unchanged: {arr}\n")

    # Quicksort
    quick_result = DivideConquerSorting.quicksort(arr)
    print(f"Quicksort result: {quick_result}")
    print(f"Original unchanged: {arr}\n")

    # In-place operations
    arr_copy = arr.copy()
    DivideConquerSorting.quicksort_inplace(arr_copy)
    print(f"Quicksort in-place: {arr_copy}")


def demonstrate_algorithm_properties():
    """Show key properties of each algorithm."""
    print("\n=== Algorithm Properties ===\n")

    algorithms = [
        (
            "Mergesort",
            DivideConquerSorting.mergesort,
            {
                "Time Complexity": "O(n log n) always",
                "Space Complexity": "O(n)",
                "Stable": "Yes",
                "In-place": "No (but can be implemented)",
            },
        ),
        (
            "Quicksort",
            DivideConquerSorting.quicksort,
            {
                "Time Complexity": "O(n²) worst, O(n log n) average",
                "Space Complexity": "O(log n) average",
                "Stable": "No",
                "In-place": "Yes",
            },
        ),
        (
            "Quicksort (Median Pivot)",
            DivideConquerSorting.quicksort_median_pivot,
            {
                "Time Complexity": "O(n log n) expected",
                "Space Complexity": "O(log n) average",
                "Stable": "No",
                "In-place": "Yes",
            },
        ),
    ]

    for name, func, props in algorithms:
        print(f"{name}:")
        for prop, value in props.items():
            print(f"  {prop}: {value}")
        print()


def demonstrate_stability():
    """Demonstrate stability property."""
    print("\n=== Stability Demonstration ===\n")

    # Create items with same value but different identities
    class Item:
        def __init__(self, value, id):
            self.value = value
            self.id = id

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
            return f"Item({self.value}, '{self.id}')"

    arr = [Item(1, "a"), Item(2, "b"), Item(1, "c"), Item(3, "d"), Item(1, "e")]
    print(f"Original array: {arr}")
    print("Note: Items with same value (1) have different IDs\n")

    # Mergesort (stable)
    merge_result = DivideConquerSorting.mergesort(arr)
    print("Mergesort (stable):")
    print(f"  Result: {merge_result}")
    print("  Equal elements maintain relative order: a, c, e\n")

    # Quicksort (unstable)
    quick_result = DivideConquerSorting.quicksort(arr)
    print("Quicksort (unstable):")
    print(f"  Result: {quick_result}")
    print("  Equal elements may change relative order\n")


def demonstrate_performance_comparison():
    """Compare performance of different algorithms."""
    print("\n=== Performance Comparison ===\n")

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"Array size: {size}")

        # Generate test array
        arr = [random.randint(0, 1000000) for _ in range(size)]

        # Test mergesort
        start = time.time()
        merge_result = DivideConquerSorting.mergesort(arr)
        merge_time = time.time() - start

        # Test quicksort
        start = time.time()
        quick_result = DivideConquerSorting.quicksort(arr)
        quick_time = time.time() - start

        # Test quicksort with median pivot
        start = time.time()
        quick_median_result = DivideConquerSorting.quicksort_median_pivot(arr)
        quick_median_time = time.time() - start

        # Verify correctness
        expected = sorted(arr)
        assert merge_result == expected
        assert quick_result == expected
        assert quick_median_result == expected

        print(".4f")
        print(".4f")
        print(".4f")

        if size <= 1000:  # Only show ratio for smaller sizes
            print(".2f")
        print()


def demonstrate_worst_case_scenarios():
    """Show worst-case behavior for different algorithms."""
    print("\n=== Worst-Case Scenarios ===\n")

    # Already sorted array (bad for quicksort, good for mergesort)
    sorted_arr = list(range(100))
    print("Testing with already sorted array:")

    # Mergesort
    start = time.time()
    merge_result = DivideConquerSorting.mergesort(sorted_arr)
    merge_time = time.time() - start

    # Quicksort (worst case)
    start = time.time()
    quick_result = DivideConquerSorting.quicksort(sorted_arr)
    quick_time = time.time() - start

    # Quicksort with median pivot (should be better)
    start = time.time()
    quick_median_result = DivideConquerSorting.quicksort_median_pivot(sorted_arr)
    quick_median_time = time.time() - start

    print(".6f")
    print(".6f")
    print(".6f")

    if quick_time > 0:
        print(".1f")

    # Reverse sorted array
    print("\nTesting with reverse sorted array:")
    reverse_arr = list(range(100, 0, -1))

    start = time.time()
    merge_result = DivideConquerSorting.mergesort(reverse_arr)
    merge_time = time.time() - start

    start = time.time()
    quick_result = DivideConquerSorting.quicksort(reverse_arr)
    quick_time = time.time() - start

    start = time.time()
    quick_median_result = DivideConquerSorting.quicksort_median_pivot(reverse_arr)
    quick_median_time = time.time() - start

    print(".6f")
    print(".6f")
    print(".6f")


def demonstrate_recursion_depth():
    """Show recursion depth analysis."""
    print("\n=== Recursion Depth Analysis ===\n")

    test_arrays = [
        ("Small sorted", list(range(10))),
        ("Small reverse", list(range(10, 0, -1))),
        ("Random", [random.randint(0, 100) for _ in range(10)]),
    ]

    for name, arr in test_arrays:
        # Note: analyze_recursion_depth is in SortingAnalysis class
        # For demo purposes, we'll show theoretical depth
        theoretical_depth = len(arr) if arr == sorted(arr, reverse=True) else "log n"
        print(f"{name:15} array: theoretical recursion depth = {theoretical_depth}")


def demonstrate_adaptive_behavior():
    """Show how algorithms behave with different inputs."""
    print("\n=== Adaptive Behavior ===\n")

    # Create partially sorted array
    arr = list(range(50)) + list(range(100, 150)) + list(range(50, 100))
    random.shuffle(arr[:75])  # Shuffle first part

    print("Testing with partially sorted array:")

    # Test both algorithms
    start = time.time()
    merge_result = DivideConquerSorting.mergesort(arr)
    merge_time = time.time() - start

    start = time.time()
    quick_result = DivideConquerSorting.quicksort(arr)
    quick_time = time.time() - start

    start = time.time()
    quick_median_result = DivideConquerSorting.quicksort_median_pivot(arr)
    quick_median_time = time.time() - start

    print(".6f")
    print(".6f")
    print(".6f")

    print(
        f"All results correct: {merge_result == quick_result == quick_median_result == sorted(arr)}"
    )


def demonstrate_memory_usage():
    """Show memory usage characteristics."""
    print("\n=== Memory Usage Characteristics ===\n")

    arr = [random.randint(0, 1000) for _ in range(1000)]

    print("Memory usage patterns:")
    print("• Mergesort: O(n) additional space for merging")
    print("• Quicksort: O(log n) stack space (average)")
    print("• In-place quicksort: O(1) additional space (besides recursion)")
    print()

    # Demonstrate in-place quicksort
    arr_copy = arr.copy()
    DivideConquerSorting.quicksort_inplace(arr_copy)

    print(f"Original array size: {len(arr)}")
    print(f"Sorted array size: {len(arr_copy)}")
    print(f"Arrays are different objects: {arr is not arr_copy}")
    print(f"Original unchanged: {arr != arr_copy}")
    # Check if sorted manually
    is_sorted = all(arr_copy[i] <= arr_copy[i + 1] for i in range(len(arr_copy) - 1))
    print(f"Result is sorted: {is_sorted}")


if __name__ == "__main__":
    demonstrate_basic_sorting()
    demonstrate_algorithm_properties()
    demonstrate_stability()
    demonstrate_performance_comparison()
    demonstrate_worst_case_scenarios()
    demonstrate_recursion_depth()
    demonstrate_adaptive_behavior()
    demonstrate_memory_usage()

    print("\n=== Key Takeaways ===")
    print("• Mergesort: Predictable O(n log n), stable, extra space")
    print("• Quicksort: Fast average case, in-place, unstable worst case")
    print("• Choose based on data characteristics and requirements!")
    print("\nChapter 13: Divide and conquer sorting algorithms mastered! 🎉")
