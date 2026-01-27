#!/usr/bin/env python3
"""
Examples demonstrating Chapter 5 running time analysis concepts.
Run this script to see timing comparisons and complexity analysis.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from chapter_05_running_time_analysis.code.complexity_analysis import *


def timing_comparison_demo():
    """Demonstrate timing different algorithms for the same problem."""
    print("=== Timing Comparison: Summing First k Numbers ===\n")

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"Summing first {size} numbers:")

        # O(k²) - Quadratic (very slow)
        try:
            result1, time1, _, _ = time_function(sum_first_k_quadratic, size, n_runs=3)
            print(".6f")
        except:
            print(f"  O(k²) method: Too slow for size {size}")

        # O(k) - Linear
        result2, time2, _, _ = time_function(sum_first_k_linear, size, n_runs=3)
        print(".6f")

        # O(1) - Constant
        result3, time3, _, _ = time_function(sum_first_k_constant, size, n_runs=3)
        print(".6f")

        # Verify all give same result
        assert result2 == result3, "Linear and constant should give same result"
        if "result1" in locals():
            assert result1 == result2, "All methods should give same result"

        print(".1f")
        print()


def complexity_analysis_demo():
    """Demonstrate operation counting and complexity analysis."""
    print("=== Complexity Analysis: Search Algorithms ===\n")

    analyzer = ComplexityAnalyzer()

    # Create test data
    sizes = [10, 100, 1000]

    for size in sizes:
        # Create array and pick target in middle
        arr = list(range(size))
        target = size // 2

        print(f"Array size: {size}, searching for: {target}")

        # Linear search
        index1, ops1 = analyzer.analyze_linear_search(arr, target)
        print(f"  Linear search: {ops1} operations")

        # Binary search (need sorted array)
        sorted_arr = sorted(arr)
        index2, ops2 = analyzer.analyze_binary_search(sorted_arr, target)
        print(f"  Binary search: {ops2} operations")

        # Calculate ratios
        if ops1 > 0:
            ratio = ops1 / ops2 if ops2 > 0 else float("inf")
            print(".1f")

        print()


def big_o_growth_demo():
    """Demonstrate Big-O growth rates with actual measurements."""
    print("=== Big-O Growth Demonstration ===\n")

    analyzer = BigOAnalyzer()
    sizes = [10, 20, 50, 100]

    print("Measuring actual execution times for different complexities:")
    print("(Times shown in microseconds for easier comparison)")
    print()

    results = analyzer.measure_complexities(sizes)

    # Show results in a table-like format
    print("Input Size | O(1)     | O(log n) | O(n)     | O(n²)")
    print("-----------|----------|----------|----------|----------")

    for i, size in enumerate(sizes):
        o1_time = results.get("O(1)", [])[i][1] * 1_000_000  # Convert to microseconds
        olog_time = results.get("O(log n)", [])[i][1] * 1_000_000
        on_time = results.get("O(n)", [])[i][1] * 1_000_000
        on2_time = results.get("O(n²)", [])[i][1] * 1_000_000

        print("5d")
    print()

    # Explain the growth patterns
    print("Growth Analysis:")
    print("- O(1): Time stays roughly constant")
    print("- O(log n): Time increases very slowly")
    print("- O(n): Time increases proportionally to input size")
    print("- O(n²): Time increases much faster (squares of input size)")
    print()


def data_structure_complexity_demo():
    """Demonstrate complexity of different data structure operations."""
    print("=== Data Structure Operation Complexity ===\n")

    analyzer = ComplexityAnalyzer()

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"Operations on data structures of size {size}:")

        # List operations
        list_results = analyzer.analyze_list_operations(size)
        print("  List operations:")
        print(f"    Index access: {list_results['index_access']} ops (O(1))")
        print(f"    Sum all: {list_results['sum_all']} ops (O(n))")
        print(f"    Membership: {list_results['membership']} ops (O(n))")

        # Dict operations
        dict_results = analyzer.analyze_dict_operations(size)
        print("  Dict operations:")
        print(f"    Key access: {dict_results['key_access']} ops (O(1) avg)")
        print(f"    Key insert: {dict_results['key_insert']} ops (O(1) avg)")
        print(f"    Membership: {dict_results['membership']} ops (O(1) avg)")

        print()


def practical_algorithm_selection():
    """Show how to choose algorithms based on problem constraints."""
    print("=== Practical Algorithm Selection Guide ===\n")

    print("Problem Size Guidelines:")
    print("• n ≤ 10: Any algorithm works fine")
    print("• n ≤ 1,000: O(n²) might be acceptable")
    print("• n ≤ 100,000: Prefer O(n log n)")
    print("• n > 100,000: Must use O(n) or better")
    print()

    print("Common Algorithm Choices:")
    print("• Small datasets (n < 50): Insertion sort O(n²)")
    print("• Medium datasets (n < 10,000): Quicksort O(n log n)")
    print("• Large datasets: Merge sort O(n log n) - guaranteed performance")
    print("• Nearly sorted data: Timsort O(n log n) - hybrid approach")
    print()

    print("Data Structure Choices:")
    print("• Fast lookups needed: Dictionary O(1) average")
    print("• Ordered data required: List with sorting O(n log n)")
    print("• Unique items only: Set for automatic deduplication")
    print("• LIFO operations: Stack for push/pop")
    print("• FIFO operations: Queue for enqueue/dequeue")
    print()


def performance_optimization_tips():
    """Show practical performance optimization techniques."""
    print("=== Performance Optimization Tips ===\n")

    print("1. Algorithm Improvement:")
    print("   - Replace O(n²) with O(n log n) for sorting")
    print("   - Use hash tables instead of linear search")
    print("   - Cache expensive computations")
    print()

    print("2. Data Structure Selection:")
    print("   - Use dict for O(1) lookups instead of list O(n)")
    print("   - Use set for O(1) membership instead of list O(n)")
    print("   - Choose the right data structure for your access patterns")
    print()

    print("3. Code-Level Optimizations:")
    print("   - Avoid unnecessary work in loops")
    print("   - Use built-in functions (sum, max, sorted)")
    print("   - Pre-compute values when possible")
    print()

    print("4. Big-O vs Practical Performance:")
    print("   - O(1000n) might be faster than O(n²) for small n")
    print("   - Consider constant factors and memory usage")
    print("   - Profile before optimizing!")
    print()


if __name__ == "__main__":
    print("=== Chapter 5: Running Time Analysis Examples ===\n")

    # Run all demonstrations
    timing_comparison_demo()
    complexity_analysis_demo()
    big_o_growth_demo()
    data_structure_complexity_demo()
    practical_algorithm_selection()
    performance_optimization_tips()

    print("=== Key Takeaways ===")
    print("• Big-O describes growth rate, not absolute speed")
    print("• Focus on dominant terms (ignore constants and lower terms)")
    print("• Worst case matters for reliability")
    print("• Choose algorithms based on expected input sizes")
    print("• Right algorithm can make orders of magnitude difference")
    print("• Profile and measure - don't guess about performance!")
