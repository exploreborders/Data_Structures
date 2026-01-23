#!/usr/bin/env python3
"""
Chapter 12: Sorting Algorithms - Interactive Examples

This script demonstrates sorting algorithms with performance comparisons,
visualizations, and interactive exploration of algorithm characteristics.
"""

import time
import random
import sys
import os
from typing import List, Dict, Any

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from sorting_algorithms import SortingAlgorithms, SortingAnalysis


def print_array(arr: List, max_elements: int = 20) -> None:
    """Print array with truncation for large arrays."""
    if len(arr) <= max_elements:
        print(f"[{', '.join(map(str, arr))}]")
    else:
        front = arr[:max_elements//2]
        back = arr[-(max_elements//2):]
        print(f"[{', '.join(map(str, front))}, ..., {', '.join(map(str, back))}]")


def demonstrate_basic_sorts():
    """Demonstrate basic sorting algorithms with step-by-step visualization."""
    print("BASIC SORTING ALGORITHMS DEMONSTRATION")
    print("=" * 50)

    # Sample array
    original = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {original}")
    print()

    algorithms = [
        ("Bubble Sort", SortingAlgorithms.bubble_sort, "O(n²) - Simple but inefficient"),
        ("Insertion Sort", SortingAlgorithms.insertion_sort, "O(n²) - Good for small/nearly sorted arrays"),
        ("Selection Sort", SortingAlgorithms.selection_sort, "O(n²) - Predictable but slow"),
    ]

    for name, sort_func, description in algorithms:
        print(f"{name}: {description}")
        arr_copy = original.copy()
        result, exec_time = SortingAnalysis.time_sorting_algorithm(sort_func, arr_copy)
        print("6.2f")
        print(f"  Result: {result}")
        print()


def demonstrate_efficient_sorts():
    """Demonstrate efficient O(n log n) sorting algorithms."""
    print("EFFICIENT SORTING ALGORITHMS")
    print("=" * 50)

    original = [64, 34, 25, 12, 22, 11, 90, 45, 72, 18]
    print(f"Original array: {original}")
    print()

    algorithms = [
        ("Quick Sort", SortingAlgorithms.quick_sort, "O(n log n) average - Fast and in-place"),
        ("Merge Sort", SortingAlgorithms.merge_sort, "O(n log n) worst case - Stable and predictable"),
        ("Heap Sort", SortingAlgorithms.heap_sort, "O(n log n) worst case - In-place, no extra space"),
    ]

    for name, sort_func, description in algorithms:
        print(f"{name}: {description}")
        arr_copy = original.copy()
        result, exec_time = SortingAnalysis.time_sorting_algorithm(sort_func, arr_copy)
        print("6.2f")
        print(f"  Result: {result}")
        print()


def demonstrate_non_comparison_sorts():
    """Demonstrate non-comparison sorting algorithms."""
    print("NON-COMPARISON SORTING ALGORITHMS")
    print("=" * 50)

    # Counting sort example
    print("Counting Sort - O(n + k) time")
    arr = [4, 2, 2, 8, 3, 3, 1]
    max_val = 8
    print(f"Original: {arr} (range 1-{max_val})")
    result = SortingAlgorithms.counting_sort(arr.copy(), max_val)
    print(f"Sorted:   {result}")
    print("  Perfect for small integer ranges!")
    print()

    # Radix sort example
    print("Radix Sort - O(n × d) time")
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original: {arr}")
    result = SortingAlgorithms.radix_sort(arr.copy())
    print(f"Sorted:   {result}")
    print("  Processes one digit at a time")
    print()

    # Bucket sort example
    print("Bucket Sort - O(n) average case")
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]
    print(f"Original: {[f'{x:.2f}' for x in arr]}")
    result = SortingAlgorithms.bucket_sort(arr.copy())
    print(f"Sorted:   {[f'{x:.2f}' for x in result]}")
    print("  Best for uniform distributions in [0,1)")
    print()


def performance_comparison():
    """Compare performance of different sorting algorithms."""
    print("PERFORMANCE COMPARISON")
    print("=" * 50)

    sizes = [100, 1000, 5000]

    # Define algorithms to test
    algorithms = [
        ("Bubble Sort", SortingAlgorithms.bubble_sort),
        ("Insertion Sort", SortingAlgorithms.insertion_sort),
        ("Selection Sort", SortingAlgorithms.selection_sort),
        ("Quick Sort", SortingAlgorithms.quick_sort),
        ("Merge Sort", SortingAlgorithms.merge_sort),
        ("Heap Sort", SortingAlgorithms.heap_sort),
        ("Timsort-like", SortingAlgorithms.timsort_like_sort),
    ]

    print("Array Size | Algorithm       | Time (seconds) | Status")
    print("-----------|-----------------|----------------|--------")

    for size in sizes:
        # Generate random data
        arr = SortingAnalysis.generate_test_data(size, "random")

        for name, sort_func in algorithms:
            try:
                result, exec_time = SortingAnalysis.time_sorting_algorithm(sort_func, arr.copy())

                # Check if result is sorted
                if SortingAnalysis.is_sorted(result):
                    status = "✓"
                else:
                    status = "✗ FAILED"

                print("9d")

                # For large arrays, skip slow algorithms after first failure
                if size >= 1000 and exec_time > 1.0 and name in ["Bubble Sort", "Selection Sort"]:
                    break

            except RecursionError:
                print("9d")
            except Exception as e:
                print("9d")

        print()


def analyze_algorithm_characteristics():
    """Analyze characteristics of different sorting algorithms."""
    print("ALGORITHM CHARACTERISTICS ANALYSIS")
    print("=" * 50)

    # Test data
    test_arrays = {
        "Random": SortingAnalysis.generate_test_data(20, "random"),
        "Sorted": SortingAnalysis.generate_test_data(20, "sorted"),
        "Reverse": SortingAnalysis.generate_test_data(20, "reverse"),
        "Nearly Sorted": SortingAnalysis.generate_test_data(20, "nearly_sorted"),
    }

    algorithms = [
        ("Bubble Sort", SortingAlgorithms.bubble_sort, "Adaptive"),
        ("Insertion Sort", SortingAlgorithms.insertion_sort, "Adaptive"),
        ("Selection Sort", SortingAlgorithms.selection_sort, "Not adaptive"),
        ("Quick Sort", SortingAlgorithms.quick_sort, "Not adaptive"),
        ("Merge Sort", SortingAlgorithms.merge_sort, "Not adaptive"),
    ]

    print("Algorithm       | Data Type      | Time (ms) | Best Case Performance")
    print("----------------|----------------|-----------|---------------------")

    for arr_name, arr in test_arrays.items():
        for name, sort_func, adaptive in algorithms:
            result, exec_time = SortingAnalysis.time_sorting_algorithm(sort_func, arr.copy())
            time_ms = exec_time * 1000

            # Determine if this shows best-case behavior for adaptive sorts
            best_case = ""
            if arr_name == "Sorted" and adaptive == "Adaptive":
                best_case = "★ Best case!"
            elif arr_name == "Reverse" and name == "Selection Sort":
                best_case = "★ Same performance"

            print("15")

        print()


def demonstrate_sorting_stability():
    """Demonstrate stability in sorting."""
    print("SORTING STABILITY DEMONSTRATION")
    print("=" * 50)

    class Student:
        def __init__(self, name: str, grade: int, original_pos: int):
            self.name = name
            self.grade = grade
            self.original_pos = original_pos

        def __lt__(self, other):
            return self.grade < other.grade

        def __repr__(self):
            return f"{self.name}(G{self.grade}, #{self.original_pos})"

    # Create students with same grade but different names
    students = [
        Student("Alice", 85, 1),
        Student("Bob", 92, 2),
        Student("Charlie", 85, 3),  # Same grade as Alice
        Student("David", 78, 4),
        Student("Eve", 85, 5),      # Same grade as Alice and Charlie
    ]

    print("Original students (note positions):")
    for student in students:
        print(f"  {student}")
    print()

    # Sort by grade (stable sort should preserve relative order)
    stable_sorted = SortingAlgorithms.merge_sort(students.copy())
    print("After stable sort (Merge Sort) - same grades maintain relative order:")
    for student in stable_sorted:
        print(f"  {student}")
    print()

    # Quick sort might not preserve order (unstable)
    unstable_sorted = SortingAlgorithms.quick_sort(students.copy())
    print("After unstable sort (Quick Sort) - order may change:")
    for student in unstable_sorted:
        print(f"  {student}")
    print()

    print("Stability matters when sorting by multiple criteria!")


def interactive_sort_explorer():
    """Interactive exploration of sorting algorithms."""
    print("INTERACTIVE SORT EXPLORER")
    print("=" * 50)

    algorithms = {
        "1": ("Bubble Sort", SortingAlgorithms.bubble_sort),
        "2": ("Insertion Sort", SortingAlgorithms.insertion_sort),
        "3": ("Selection Sort", SortingAlgorithms.selection_sort),
        "4": ("Quick Sort", SortingAlgorithms.quick_sort),
        "5": ("Merge Sort", SortingAlgorithms.merge_sort),
        "6": ("Heap Sort", SortingAlgorithms.heap_sort),
        "7": ("Counting Sort", SortingAlgorithms.counting_sort),
        "8": ("Radix Sort", SortingAlgorithms.radix_sort),
        "9": ("Bucket Sort", SortingAlgorithms.bucket_sort),
    }

    while True:
        print("\nAvailable algorithms:")
        for key, (name, _) in algorithms.items():
            print(f"  {key}. {name}")

        choice = input("\nChoose an algorithm (number or 'quit'): ").strip()

        if choice.lower() == 'quit':
            break

        if choice not in algorithms:
            print("Invalid choice. Try again.")
            continue

        name, sort_func = algorithms[choice]

        # Get array input
        while True:
            arr_input = input("Enter comma-separated numbers (or 'random' for random array): ").strip()

            if arr_input.lower() == 'random':
                arr = SortingAnalysis.generate_test_data(10, "random")
                break
            else:
                try:
                    arr = [int(x.strip()) for x in arr_input.split(',')]
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers separated by commas.")

        print(f"\nOriginal array: {arr}")

        # Handle special cases for non-comparison sorts
        if name == "Counting Sort":
            if not arr:
                max_val = 0
            else:
                max_val = max(arr)
            print(f"Using max value: {max_val}")
            result = SortingAlgorithms.counting_sort(arr.copy(), max_val)
        elif name == "Bucket Sort":
            # Convert to floats in [0,1) for bucket sort
            if not arr:
                result = []
            else:
                max_val = max(arr)
                float_arr = [x / (max_val + 1) for x in arr]
                result = SortingAlgorithms.bucket_sort(float_arr)
                # Convert back (approximately)
                result = [round(x * (max_val + 1)) for x in result]
        else:
            result = sort_func(arr.copy())

        print(f"Sorted array:   {result}")
        print(f"Is sorted:      {SortingAnalysis.is_sorted(result)}")


def main():
    """Run all demonstrations."""
    print("Chapter 12: Sorting Algorithms - Interactive Examples")
    print("This script demonstrates sorting concepts, performance, and characteristics.\n")

    demonstrate_basic_sorts()
    demonstrate_efficient_sorts()
    demonstrate_non_comparison_sorts()
    performance_comparison()
    analyze_algorithm_characteristics()
    demonstrate_sorting_stability()

    # Interactive demo
    response = input("\nWould you like to explore sorting algorithms interactively? (y/n): ").strip().lower()
    if response == 'y' or response == 'yes':
        interactive_sort_explorer()

    print("\n" + "=" * 60)
    print("SORTING ALGORITHMS KEY INSIGHTS:")
    print("=" * 60)
    print("1. Quadratic sorts: Simple but only for small datasets")
    print("2. O(n log n) sorts: The workhorses - Quick, Merge, Heap")
    print("3. Non-comparison sorts: Linear time for special cases")
    print("4. Stability matters: Preserving relative order of equals")
    print("5. Adaptivity helps: Better performance on nearly sorted data")
    print("6. No single 'best' sort: Choose based on constraints")
    print("\nMastering sorting algorithms is fundamental to efficient programming!")


if __name__ == '__main__':
    main()</content>
<parameter name="filePath">chapter_12_sorting_algorithms/examples/sorting_demo.py