"""
Chapter 14: Selection - Quickselect Algorithm

This module implements the quickselect algorithm for finding the k-th smallest
element in an unordered array, achieving average O(n) time complexity.
"""

from typing import List, TypeVar, Optional
import random

T = TypeVar('T')


class QuickSelect:
    """Quickselect algorithm implementations for finding order statistics."""

    @staticmethod
    def quickselect_recursive(arr: List[T], k: int) -> T:
        """
        Find the k-th smallest element using recursive quickselect.

        Time: O(n) average case, O(n²) worst case
        Space: O(log n) average (recursion stack)

        Args:
            arr: List to search
            k: Index of desired element (0-based, k-th smallest)

        Returns:
            k-th smallest element

        Raises:
            ValueError: If k is out of bounds

        Examples:
            >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
            >>> QuickSelect.quickselect_recursive(arr, 0)  # Smallest
            1
            >>> QuickSelect.quickselect_recursive(arr, 4)  # Median
            4
        """
        if not arr:
            raise ValueError("Array is empty")
        if k < 0 or k >= len(arr):
            raise ValueError(f"k ({k}) is out of bounds for array of size {len(arr)}")

        return QuickSelect._quickselect_recursive(arr.copy(), 0, len(arr) - 1, k)

    @staticmethod
    def _quickselect_recursive(arr: List[T], low: int, high: int, k: int) -> T:
        """Recursive quickselect helper."""
        if low == high:
            return arr[low]

        # Choose pivot and partition
        pivot_idx = QuickSelect._choose_pivot_median_of_three(arr, low, high)
        pivot_idx = QuickSelect._partition(arr, low, high, pivot_idx)

        # Check which partition contains the k-th element
        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return QuickSelect._quickselect_recursive(arr, low, pivot_idx - 1, k)
        else:
            return QuickSelect._quickselect_recursive(arr, pivot_idx + 1, high, k)

    @staticmethod
    def quickselect_iterative(arr: List[T], k: int) -> T:
        """
        Find the k-th smallest element using iterative quickselect.

        Time: O(n) average case, O(n²) worst case
        Space: O(1) auxiliary

        Args:
            arr: List to search
            k: Index of desired element (0-based, k-th smallest)

        Returns:
            k-th smallest element

        Examples:
            >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
            >>> QuickSelect.quickselect_iterative(arr, 0)
            1
            >>> QuickSelect.quickselect_iterative(arr, 7)  # Largest
            9
        """
        if not arr:
            raise ValueError("Array is empty")
        if k < 0 or k >= len(arr):
            raise ValueError(f"k ({k}) is out of bounds for array of size {len(arr)}")

        arr_copy = arr.copy()
        left, right = 0, len(arr_copy) - 1

        while left <= right:
            pivot_idx = QuickSelect._choose_pivot_median_of_three(arr_copy, left, right)
            pivot_idx = QuickSelect._partition(arr_copy, left, right, pivot_idx)

            if pivot_idx == k:
                return arr_copy[k]
            elif k < pivot_idx:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

        raise ValueError("k is out of bounds (should not reach here)")

    @staticmethod
    def quickselect_randomized(arr: List[T], k: int) -> T:
        """
        Find the k-th smallest element using randomized quickselect.

        Uses random pivot selection for better average case performance.

        Args:
            arr: List to search
            k: Index of desired element (0-based, k-th smallest)

        Returns:
            k-th smallest element

        Examples:
            >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
            >>> QuickSelect.quickselect_randomized(arr, 2)
            2
        """
        if not arr:
            raise ValueError("Array is empty")
        if k < 0 or k >= len(arr):
            raise ValueError(f"k ({k}) is out of bounds for array of size {len(arr)}")

        arr_copy = arr.copy()
        return QuickSelect._quickselect_randomized(arr_copy, 0, len(arr_copy) - 1, k)

    @staticmethod
    def _quickselect_randomized(arr: List[T], low: int, high: int, k: int) -> T:
        """Randomized quickselect helper."""
        if low == high:
            return arr[low]

        # Choose random pivot
        pivot_idx = random.randint(low, high)
        pivot_idx = QuickSelect._partition(arr, low, high, pivot_idx)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return QuickSelect._quickselect_randomized(arr, low, pivot_idx - 1, k)
        else:
            return QuickSelect._quickselect_randomized(arr, pivot_idx + 1, high, k)

    @staticmethod
    def _choose_pivot_median_of_three(arr: List[T], low: int, high: int) -> int:
        """Choose pivot using median of three elements."""
        mid = (low + high) // 2

        # Find median of arr[low], arr[mid], arr[high]
        candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        candidates.sort(key=lambda x: x[0])

        return candidates[1][1]  # Return index of median

    @staticmethod
    def _partition(arr: List[T], low: int, high: int, pivot_idx: int) -> int:
        """Partition array around pivot using Lomuto scheme."""
        # Move pivot to end
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        pivot = arr[high]

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def find_median(arr: List[T]) -> T:
        """
        Find the median of an array using quickselect.

        Args:
            arr: List to find median of

        Returns:
            Median value

        Examples:
            >>> QuickSelect.find_median([1, 3, 5, 7, 9])
            5
            >>> QuickSelect.find_median([1, 2, 3, 4])
            3
        """
        n = len(arr)
        if n == 0:
            raise ValueError("Cannot find median of empty array")

        if n % 2 == 1:
            # Odd length - return middle element
            return QuickSelect.quickselect_iterative(arr, n // 2)
        else:
            # Even length - return lower median
            return QuickSelect.quickselect_iterative(arr, n // 2 - 1)

    @staticmethod
    def find_kth_largest(arr: List[T], k: int) -> T:
        """
        Find the k-th largest element in an array.

        Args:
            arr: List to search
            k: Position from largest (1-based)

        Returns:
            k-th largest element

        Examples:
            >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
            >>> QuickSelect.find_kth_largest(arr, 1)  # Largest
            9
            >>> QuickSelect.find_kth_largest(arr, 3)  # 3rd largest
            6
        """
        if k < 1 or k > len(arr):
            raise ValueError(f"k ({k}) is out of bounds")

        # k-th largest is equivalent to (n-k)-th smallest
        return QuickSelect.quickselect_iterative(arr, len(arr) - k)

    @staticmethod
    def find_percentile(arr: List[T], percentile: float) -> T:
        """
        Find a percentile value using quickselect.

        Args:
            arr: List to search
            percentile: Percentile (0.0 to 100.0)

        Returns:
            Percentile value

        Examples:
            >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            >>> QuickSelect.find_percentile(arr, 50.0)  # Median
            6
            >>> QuickSelect.find_percentile(arr, 25.0)  # Q1
            3
        """
        if percentile < 0.0 or percentile > 100.0:
            raise ValueError("Percentile must be between 0.0 and 100.0")

        n = len(arr)
        if n == 0:
            raise ValueError("Cannot find percentile of empty array")

        # Calculate index: (percentile/100) * (n-1)
        index = int((percentile / 100.0) * (n - 1))

        return QuickSelect.quickselect_iterative(arr, index)

    @staticmethod
    def select_top_k(arr: List[T], k: int) -> List[T]:
        """
        Find the k smallest elements using quickselect.

        Note: This is not the most efficient way, but demonstrates the concept.

        Args:
            arr: List to search
            k: Number of smallest elements to find

        Returns:
            List of k smallest elements (unsorted)

        Examples:
            >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
            >>> sorted(QuickSelect.select_top_k(arr, 3))
            [1, 1, 2]
        """
        if k < 1 or k > len(arr):
            raise ValueError(f"k ({k}) is out of bounds")

        # Use quickselect to find k-th element as pivot
        kth_element = QuickSelect.quickselect_iterative(arr.copy(), k - 1)

        # Collect all elements <= k-th element
        result = [x for x in arr if x <= kth_element][:k]

        return result


class SelectionAnalysis:
    """Analysis tools for selection algorithms."""

    @staticmethod
    def benchmark_quickselect_implementations(arr: List[int], k_values: List[int]) -> dict:
        """
        Benchmark different quickselect implementations.

        Args:
            arr: Test array
            k_values: List of k values to test

        Returns:
            Dictionary with timing results
        """
        import time

        results = {}

        implementations = [
            ("Recursive", QuickSelect.quickselect_recursive),
            ("Iterative", QuickSelect.quickselect_iterative),
            ("Randomized", QuickSelect.quickselect_randomized),
        ]

        for k in k_values:
            if k >= len(arr):
                continue

            results[k] = {}

            for name, impl in implementations:
                arr_copy = arr.copy()
                start_time = time.time()
                result = impl(arr_copy, k)
                end_time = time.time()

                results[k][name] = {
                    "time": end_time - start_time,
                    "result": result
                }

        return results

    @staticmethod
    def analyze_pivot_strategies(arr: List[int], k: int, num_trials: int = 10) -> dict:
        """
        Analyze performance of different pivot selection strategies.

        Args:
            arr: Test array
            k: k value for selection
            num_trials: Number of trials to run

        Returns:
            Dictionary with performance statistics
        """
        import time
        import statistics

        strategies = [
            ("Median of Three", QuickSelect.quickselect_iterative),
            ("Randomized", QuickSelect.quickselect_randomized),
        ]

        results = {}

        for name, strategy in strategies:
            times = []

            for _ in range(num_trials):
                arr_copy = arr.copy()
                start_time = time.time()
                strategy(arr_copy, k)
                end_time = time.time()
                times.append(end_time - start_time)

            results[name] = {
                "mean_time": statistics.mean(times),
                "median_time": statistics.median(times),
                "min_time": min(times),
                "max_time": max(times)
            }

        return results

    @staticmethod
    def compare_with_sorting(arr: List[int], k_values: List[int]) -> dict:
        """
        Compare quickselect performance with sorting approach.

        Args:
            arr: Test array
            k_values: List of k values to test

        Returns:
            Dictionary comparing approaches
        """
        import time

        results = {}

        for k in k_values:
            if k >= len(arr):
                continue

            # Quickselect approach
            arr_copy = arr.copy()
            start_time = time.time()
            quickselect_result = QuickSelect.quickselect_iterative(arr_copy, k)
            quickselect_time = time.time() - start_time

            # Sorting approach
            arr_copy = arr.copy()
            start_time = time.time()
            sorted_arr = sorted(arr_copy)
            sorting_result = sorted_arr[k]
            sorting_time = time.time() - start_time

            results[k] = {
                "quickselect_time": quickselect_time,
                "sorting_time": sorting_time,
                "speedup": sorting_time / quickselect_time if quickselect_time > 0 else float('inf'),
                "results_match": quickselect_result == sorting_result
            }

        return results
