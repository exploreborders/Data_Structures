#!/usr/bin/env python3
"""
Chapter 11: Binary Search - Interactive Examples

This script demonstrates binary search algorithms with step-by-step visualizations
and performance comparisons with other search methods.
"""

import time
import sys
import os
from typing import List

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from binary_search_algorithms import (
    BinarySearch,
    BinarySearchApplications,
    AdvancedSearch,
)


def time_function(func, *args, **kwargs):
    """Time a function execution."""
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start


def linear_search(arr: List[int], target: int) -> int:
    """Simple linear search for comparison."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def visualize_binary_search():
    """Step-by-step visualization of binary search."""
    print("BINARY SEARCH VISUALIZATION")
    print("=" * 50)

    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11

    print(f"Array: {arr}")
    print(f"Target: {target}")
    print()

    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = left + (right - left) // 2

        print(f"Step {steps}:")
        print(f"  Search range: arr[{left}:{right + 1}] = {arr[left : right + 1]}")
        print(f"  Mid index: {mid}, Mid value: {arr[mid]}")

        if arr[mid] == target:
            print(f"  ✓ Found {target} at index {mid}!")
            return mid
        elif arr[mid] < target:
            print(f"  {arr[mid]} < {target}, search right half")
            left = mid + 1
        else:
            print(f"  {arr[mid]} > {target}, search left half")
            right = mid - 1

        print(f"  New range: [{left}, {right}]")
        print()

    print(f"✗ {target} not found in array")
    return -1


def demonstrate_variants():
    """Demonstrate binary search variants."""
    print("\nBINARY SEARCH VARIANTS")
    print("=" * 50)

    arr = [1, 3, 3, 3, 5, 5, 7, 9, 9, 9]
    target = 3

    print(f"Array with duplicates: {arr}")
    print(f"Target: {target}")
    print()

    # Standard binary search (returns one occurrence)
    standard = BinarySearch.binary_search_iterative(arr, target)
    print(f"Standard binary search: index {standard}")

    # First occurrence
    first = BinarySearch.find_first_occurrence(arr, target)
    print(f"First occurrence: index {first}")

    # Last occurrence
    last = BinarySearch.find_last_occurrence(arr, target)
    print(f"Last occurrence: index {last}")

    # Count occurrences
    count = BinarySearch.count_occurrences(arr, target)
    print(f"Total occurrences: {count}")

    # Bounds
    lower = BinarySearch.lower_bound(arr, target)
    upper = BinarySearch.upper_bound(arr, target)
    print(f"Lower bound (insertion point): index {lower}")
    print(f"Upper bound: index {upper}")

    print(f"\nRange of {target}s: indices {first} to {last}")


def demonstrate_applications():
    """Demonstrate binary search applications."""
    print("\nBINARY SEARCH APPLICATIONS")
    print("=" * 50)

    # Square root calculation
    print("1. Square Root Calculation:")
    for x in [4, 9, 16, 25, 2]:
        sqrt_result = BinarySearchApplications.square_root_binary_search(x)
        actual = x**0.5
        error = abs(sqrt_result - actual)
        print(
            f"  sqrt({x}) ≈ {sqrt_result:.1f} (actual: {actual:.1f}, error: {error:.1f})"
        )
    # Peak finding
    print("\n2. Peak Finding:")
    arrays = [[1, 3, 2, 1], [1, 2, 3, 4, 3], [5, 4, 3, 2, 1]]

    for arr in arrays:
        peak_idx = BinarySearchApplications.find_peak_element(arr)
        print(f"  Array: {arr} → Peak at index {peak_idx} (value: {arr[peak_idx]})")

    # Rotated array search
    print("\n3. Search in Rotated Sorted Array:")
    rotated = [4, 5, 6, 7, 0, 1, 2]
    targets = [0, 4, 2, 3]

    print(f"  Rotated array: {rotated}")
    for target in targets:
        idx = BinarySearchApplications.search_rotated_array(rotated, target)
        result = f"found at index {idx}" if idx != -1 else "not found"
        print(f"    Search for {target}: {result}")


def performance_comparison():
    """Compare performance of different search algorithms."""
    print("\nPERFORMANCE COMPARISON")
    print("=" * 50)

    # Create test data of different sizes
    sizes = [1000, 10000, 100000]
    target = -1  # Not found case (worst for binary search)

    print("Array Size | Linear Search | Binary Search | Speedup")
    print("-----------|---------------|---------------|--------")

    for size in sizes:
        # Create sorted array
        arr = list(range(size))

        # Time linear search
        _, linear_time = time_function(linear_search, arr, target)

        # Time binary search
        _, binary_time = time_function(
            BinarySearch.binary_search_iterative, arr, target
        )

        # Calculate speedup
        speedup = linear_time / binary_time if binary_time > 0 else float("inf")

        print("6d")

    print(
        "\nNote: Binary search requires sorted data. The 'sort once, search many times'"
    )
    print("      principle makes binary search extremely valuable in practice.")


def demonstrate_advanced_search():
    """Demonstrate advanced search algorithms."""
    print("\nADVANCED SEARCH ALGORITHMS")
    print("=" * 50)

    # Test data
    arr = list(range(1, 1001))  # 1 to 1000
    targets = [1, 250, 500, 750, 1000, 1500]  # Mix of found and not found

    algorithms = [
        ("Binary Search", BinarySearch.binary_search_iterative),
        ("Exponential Search", AdvancedSearch.exponential_search),
        ("Interpolation Search", AdvancedSearch.interpolation_search),
        ("Ternary Search", AdvancedSearch.ternary_search),
    ]

    print("Algorithm Performance (searching in array of size 1000):")
    print("Target | Binary | Exponential | Interpolation | Ternary")
    print("-------|--------|-------------|---------------|--------")

    for target in targets:
        results = []
        for name, algo in algorithms:
            _, exec_time = time_function(algo, arr, target)
            results.append("6.4f")

        print(f"{target:6d} | {' | '.join(results)}")

    print("\nKey Insights:")
    print("- Binary search: Always O(log n), predictable performance")
    print("- Exponential search: Good when array size unknown")
    print("- Interpolation search: Excellent for uniform distributions")
    print("- Ternary search: Useful for 3-way optimization problems")


def interactive_search_demo():
    """Interactive demonstration of binary search."""
    print("\nINTERACTIVE BINARY SEARCH DEMO")
    print("=" * 50)

    # Create a sample array
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(f"Sample sorted array: {arr}")
    print("This array contains even numbers from 2 to 20.")

    while True:
        try:
            target = input(
                "\nEnter a number to search for (or 'quit' to exit): "
            ).strip()

            if target.lower() == "quit":
                break

            target = int(target)

            # Perform binary search
            result = BinarySearch.binary_search_iterative(arr, target)

            if result != -1:
                print(f"✓ Found {target} at index {result}")
            else:
                # Find insertion point
                insert_pos = BinarySearch.lower_bound(arr, target)
                print(f"✗ {target} not found")
                print(f"  Could be inserted at index {insert_pos}")

                # Show neighbors
                if insert_pos > 0:
                    print(
                        f"  Between {arr[insert_pos - 1]} (index {insert_pos - 1}) and ",
                        end="",
                    )
                if insert_pos < len(arr):
                    print(f"{arr[insert_pos]} (index {insert_pos})")
                else:
                    print("the end of the array")

        except ValueError:
            print("Please enter a valid number or 'quit'")


def main():
    """Run all demonstrations."""
    print("Chapter 11: Binary Search - Interactive Examples")
    print("This script demonstrates binary search concepts and applications.\n")

    visualize_binary_search()
    demonstrate_variants()
    demonstrate_applications()
    performance_comparison()
    demonstrate_advanced_search()

    # Interactive demo (only if user wants it)
    response = (
        input("\nWould you like to try an interactive binary search demo? (y/n): ")
        .strip()
        .lower()
    )
    if response == "y" or response == "yes":
        interactive_search_demo()

    print("\n" + "=" * 60)
    print("BINARY SEARCH KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Divide and conquer: Eliminate half the search space each step")
    print("2. Requires sorted data: O(n log n) sort enables O(log n) searches")
    print("3. O(log n) time complexity: Scales excellently to large datasets")
    print("4. Multiple variants: First/last occurrence, bounds, applications")
    print("5. Beyond arrays: Square root, peaks, rotated arrays, optimization")
    print(
        "\nBinary search is a fundamental algorithm that every programmer should master!"
    )


if __name__ == "__main__":
    main()
