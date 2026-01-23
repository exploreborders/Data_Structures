"""
Chapter 5: Running Time Analysis - Algorithm Efficiency Analysis

This module demonstrates techniques for analyzing algorithm performance:
- Timing functions and measuring actual runtime
- Counting operations and modeling complexity
- Big-O analysis and asymptotic complexity
- Comparing algorithm efficiency
"""

import time
import timeit
import random
import math


# 5.1 Timing Programs
def time_function(func, *args, n_runs=5):
    """
    Time a function's execution multiple times and return average.

    Args:
        func: Function to time
        *args: Arguments to pass to function
        n_runs: Number of timing runs for averaging

    Returns:
        tuple: (result, average_time, min_time, max_time)
    """
    times = []

    for _ in range(n_runs):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)

    return result, avg_time, min_time, max_time


def timing_example():
    """Demonstrate timing different approaches to summing numbers."""
    n = 10000

    # Method 1: Loop
    def sum_loop(n):
        total = 0
        for i in range(n + 1):
            total += i
        return total

    # Method 2: Formula
    def sum_formula(n):
        return n * (n + 1) // 2

    print("Timing comparison for summing first", n, "numbers:")
    print()

    # Time loop method
    result1, avg1, min1, max1 = time_function(sum_loop, n)
    print(
        f"Loop method:     {result1} (avg: {avg1:.6f}s, min: {min1:.6f}s, max: {max1:.6f}s)"
    )

    # Time formula method
    result2, avg2, min2, max2 = time_function(sum_formula, n)
    print(
        f"Formula method:  {result2} (avg: {avg2:.6f}s, min: {min2:.6f}s, max: {max2:.6f}s)"
    )

    print(".2f")
    print()


# 5.2 Example: Adding the first k numbers
def sum_first_k_quadratic(k):
    """
    O(k²) example: nested loops doing redundant work.
    NOT an efficient way to sum - just demonstrates complexity.
    """
    total = 0
    for i in range(k + 1):
        for j in range(k + 1):  # Redundant inner loop
            if j == i:
                total += i
    return total


# For a true O(k²) example, let's create a different function
def sum_first_k_quadratic_example(k):
    """
    O(k²) example: nested loops doing redundant work.
    NOT an efficient way to sum - just demonstrates complexity.
    """
    total = 0
    for i in range(k + 1):
        for j in range(k + 1):  # Redundant work
            if j == i:
                total += i
    return total


def sum_first_k_linear(k):
    """Sum first k numbers using O(k) approach."""
    total = 0
    for i in range(k + 1):
        total += i
    return total


def sum_first_k_constant(k):
    """Sum first k numbers using O(1) formula."""
    return k * (k + 1) // 2


# 5.3 Modeling the Running Time
class ComplexityAnalyzer:
    """Analyze and compare algorithm complexities."""

    def __init__(self):
        self.operations_count = 0

    def reset_counter(self):
        """Reset the operations counter."""
        self.operations_count = 0

    def count_operation(self):
        """Increment the operations counter."""
        self.operations_count += 1

    def analyze_linear_search(self, arr, target):
        """Linear search with operation counting."""
        self.reset_counter()

        for i, item in enumerate(arr):
            self.count_operation()  # Comparison
            if item == target:
                return i, self.operations_count

        return -1, self.operations_count

    def analyze_binary_search(self, arr, target):
        """Binary search with operation counting."""
        self.reset_counter()
        left, right = 0, len(arr) - 1

        while left <= right:
            self.count_operation()  # Loop condition check
            mid = (left + right) // 2
            self.count_operation()  # Comparison

            if arr[mid] == target:
                return mid, self.operations_count
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1, self.operations_count

    def analyze_list_operations(self, n):
        """Analyze common list operations."""
        results = {}

        # Create list
        lst = list(range(n))

        # O(1) operations
        self.reset_counter()
        _ = lst[0]  # Index access
        results["index_access"] = 1  # O(1)

        self.reset_counter()
        _ = len(lst)  # Length
        results["length"] = 1  # O(1)

        # O(n) operations
        self.reset_counter()
        total = sum(lst)  # Sum all elements
        results["sum_all"] = n  # O(n)

        self.reset_counter()
        found = n // 2 in lst  # Membership test
        results["membership"] = n  # O(n) worst case

        return results

    def analyze_dict_operations(self, n):
        """Analyze common dictionary operations."""
        results = {}

        # Create dictionary
        d = {i: i * 2 for i in range(n)}

        # O(1) average operations
        self.reset_counter()
        _ = d[0]  # Key access
        self.count_operation()
        results["key_access"] = self.operations_count

        self.reset_counter()
        d[n] = n * 2  # Key insertion
        self.count_operation()
        results["key_insert"] = self.operations_count

        self.reset_counter()
        exists = n // 2 in d  # Membership test
        self.count_operation()
        results["membership"] = self.operations_count

        return results


# 5.4 Asymptotic Analysis and Big-O
class BigOAnalyzer:
    """Demonstrate Big-O complexity classes."""

    def constant_time(self, n):
        """O(1) - Constant time."""
        return 42  # Same work regardless of n

    def logarithmic_time(self, n):
        """O(log n) - Logarithmic time."""
        count = 0
        while n > 1:
            n = n // 2
            count += 1
        return count

    def linear_time(self, n):
        """O(n) - Linear time."""
        total = 0
        for i in range(n):
            total += i
        return total

    def quadratic_time(self, n):
        """O(n²) - Quadratic time."""
        total = 0
        for i in range(n):
            for j in range(n):
                total += 1
        return total

    def exponential_time(self, n):
        """O(2ⁿ) - Exponential time (only for small n!)."""
        if n == 0:
            return 1
        return 2 * self.exponential_time(n - 1)

    def measure_complexities(self, sizes):
        """Measure actual runtime for different complexities."""
        results = {}

        for size in sizes:
            # O(1)
            if size >= 1:
                time_const = (
                    timeit.timeit(lambda: self.constant_time(size), number=1000) / 1000
                )
                results.setdefault("O(1)", []).append((size, time_const))

            # O(log n)
            time_log = (
                timeit.timeit(lambda: self.logarithmic_time(size), number=100) / 100
            )
            results.setdefault("O(log n)", []).append((size, time_log))

            # O(n) - use smaller size to avoid slow execution
            n_size = min(size, 10000)
            time_linear = (
                timeit.timeit(lambda: self.linear_time(n_size), number=10) / 10
            )
            results.setdefault("O(n)", []).append((n_size, time_linear))

            # O(n²) - use very small size
            n2_size = min(size, 200)
            time_quad = timeit.timeit(lambda: self.quadratic_time(n2_size), number=1)
            results.setdefault("O(n²)", []).append((n2_size, time_quad))

        return results


# 5.5 Focus on the Worst Case
def worst_case_examples():
    """Demonstrate why we focus on worst case."""

    # Linear search: worst case is when item is not found
    def linear_search_worst_case(arr, target):
        """Always checks every element (worst case)."""
        for item in arr:
            if item == target:
                return True
        return False

    # Quick sort: worst case is already sorted array
    def quicksort_worst_case(arr):
        """O(n²) in worst case, O(n log n) average."""
        if len(arr) <= 1:
            return arr

        pivot = arr[0]  # Bad choice for sorted array
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        return quicksort_worst_case(left) + [pivot] + quicksort_worst_case(right)

    return {
        "linear_search": linear_search_worst_case,
        "quicksort": quicksort_worst_case,
    }


if __name__ == "__main__":
    print("=== Chapter 5: Running Time Analysis ===\n")

    # Timing demonstration
    timing_example()

    # Complexity analyzer
    analyzer = ComplexityAnalyzer()

    # Create test data
    arr = list(range(1000))
    random.shuffle(arr)
    sorted_arr = sorted(arr)

    # Analyze search algorithms
    target = 500

    # Linear search
    index1, ops1 = analyzer.analyze_linear_search(arr, target)
    print(f"Linear search found {target} at index {index1} in {ops1} operations")

    # Binary search (on sorted array)
    sorted_arr = sorted(arr)
    index2, ops2 = analyzer.analyze_binary_search(sorted_arr, target)
    print(f"Binary search found {target} at index {index2} in {ops2} operations")
    print(".1f")
    print()

    # Big-O demonstration
    bigo = BigOAnalyzer()
    sizes = [10, 50, 100, 500, 1000]

    print("Big-O Complexity Demonstration:")
    print("(Measuring actual execution times for different input sizes)")
    print()

    results = bigo.measure_complexities(sizes)

    for complexity, measurements in results.items():
        print(f"{complexity}:")
        for size, time_taken in measurements[:3]:  # Show first 3 sizes
            print("6.2f")
        print()

    # Practical advice
    print("=== Practical Algorithm Selection ===")
    print("For n ≤ 10: Any algorithm works")
    print("For n ≤ 1,000: O(n²) might be acceptable")
    print("For n ≤ 100,000: Prefer O(n log n)")
    print("For n > 100,000: Must use O(n) or better")
    print()
    print("Remember: Choose the right algorithm, not just the right code!")
