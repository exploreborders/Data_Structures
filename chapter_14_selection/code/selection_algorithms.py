"""
Chapter 14: Selection - Finding Order Statistics

This module implements selection algorithms for finding the k-th smallest element
in an unordered array. The main algorithm is quickselect, which provides O(n)
average-case performance for finding order statistics.
"""

from typing import List, TypeVar, Optional
import random

T = TypeVar("T")


class SelectionAlgorithms:
    """Implementation of selection algorithms for finding order statistics."""

    @staticmethod
    def quickselect(arr: List[T], k: int) -> T:
        """
        Find the k-th smallest element using quickselect algorithm.

        Time: O(n) average case, O(n²) worst case
        Space: O(1) auxiliary space
        Stable: No

        Args:
            arr: List to select from
            k: Index of desired element (0-based, k < len(arr))

        Returns:
            k-th smallest element

        Examples:
            >>> SelectionAlgorithms.quickselect([3, 1, 4, 1, 5], 0)
            1
            >>> SelectionAlgorithms.quickselect([3, 1, 4, 1, 5], 2)
            3
        """
        if not 0 <= k < len(arr):
            raise ValueError(f"k ({k}) must be between 0 and {len(arr) - 1}")

        arr_copy = arr.copy()
        return SelectionAlgorithms._quickselect_helper(
            arr_copy, 0, len(arr_copy) - 1, k
        )

    @staticmethod
    def _quickselect_helper(arr: List[T], low: int, high: int, k: int) -> T:
        """Recursive helper for quickselect."""
        if low == high:
            return arr[low]

        # Choose pivot using median-of-three
        pivot_idx = SelectionAlgorithms._choose_pivot_median_of_three(arr, low, high)
        pivot_idx = SelectionAlgorithms._partition_lomuto(arr, low, high, pivot_idx)

        if pivot_idx == k:
            return arr[pivot_idx]
        elif pivot_idx > k:
            return SelectionAlgorithms._quickselect_helper(arr, low, pivot_idx - 1, k)
        else:
            return SelectionAlgorithms._quickselect_helper(arr, pivot_idx + 1, high, k)

    @staticmethod
    def quickselect_iterative(arr: List[T], k: int) -> T:
        """
        Iterative version of quickselect.

        Args:
            arr: List to select from
            k: Index of desired element (0-based)

        Returns:
            k-th smallest element
        """
        if not 0 <= k < len(arr):
            raise ValueError(f"k ({k}) must be between 0 and {len(arr) - 1}")

        arr_copy = arr.copy()
        left, right = 0, len(arr_copy) - 1

        while left <= right:
            pivot_idx = SelectionAlgorithms._partition_lomuto(
                arr_copy,
                left,
                right,
                SelectionAlgorithms._choose_pivot_median_of_three(
                    arr_copy, left, right
                ),
            )

            if pivot_idx == k:
                return arr_copy[pivot_idx]
            elif pivot_idx > k:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1

        raise ValueError("Selection failed - this should not happen")

    @staticmethod
    def quickselect_random_pivot(arr: List[T], k: int) -> T:
        """
        Quickselect with random pivot selection.

        Args:
            arr: List to select from
            k: Index of desired element

        Returns:
            k-th smallest element
        """
        if not 0 <= k < len(arr):
            raise ValueError(f"k ({k}) must be between 0 and {len(arr) - 1}")

        arr_copy = arr.copy()
        return SelectionAlgorithms._quickselect_random_helper(
            arr_copy, 0, len(arr_copy) - 1, k
        )

    @staticmethod
    def _quickselect_random_helper(arr: List[T], low: int, high: int, k: int) -> T:
        """Helper for random pivot quickselect."""
        if low == high:
            return arr[low]

        # Random pivot
        pivot_idx = random.randint(low, high)
        pivot_idx = SelectionAlgorithms._partition_lomuto(arr, low, high, pivot_idx)

        if pivot_idx == k:
            return arr[pivot_idx]
        elif pivot_idx > k:
            return SelectionAlgorithms._quickselect_random_helper(
                arr, low, pivot_idx - 1, k
            )
        else:
            return SelectionAlgorithms._quickselect_random_helper(
                arr, pivot_idx + 1, high, k
            )

    @staticmethod
    def _partition_lomuto(arr: List[T], low: int, high: int, pivot_idx: int) -> int:
        """
        Lomuto partition scheme.

        Args:
            arr: Array to partition
            low: Start index
            high: End index
            pivot_idx: Index of pivot element

        Returns:
            Final position of pivot
        """
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
    def _partition_hoare(arr: List[T], low: int, high: int) -> int:
        """
        Hoare partition scheme.

        Args:
            arr: Array to partition
            low: Start index
            high: End index

        Returns:
            Partition index
        """
        pivot = arr[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j

            arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _choose_pivot_median_of_three(arr: List[T], low: int, high: int) -> int:
        """
        Choose pivot using median-of-three strategy.

        Args:
            arr: Array
            low: Start index
            high: End index

        Returns:
            Index of chosen pivot
        """
        mid = (low + high) // 2

        # Get values and indices
        candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]

        # Sort by value and return middle element's index
        candidates.sort(key=lambda x: x[0])
        return candidates[1][1]  # Index of median

    @staticmethod
    def _choose_pivot_random(arr: List[T], low: int, high: int) -> int:
        """Choose pivot randomly."""
        return random.randint(low, high)

    @staticmethod
    def find_median(arr: List[T]) -> T:
        """
        Find the median of an array.

        Args:
            arr: Array to find median of

        Returns:
            Median value
        """
        if not arr:
            raise ValueError("Cannot find median of empty array")

        n = len(arr)
        if n % 2 == 1:
            # Odd length - middle element
            return SelectionAlgorithms.quickselect(arr, n // 2)
        else:
            # Even length - average of two middle elements
            mid1 = SelectionAlgorithms.quickselect(arr, n // 2 - 1)
            mid2 = SelectionAlgorithms.quickselect(arr, n // 2)
            # For simplicity, return the lower median
            return mid1

    @staticmethod
    def find_percentile(arr: List[T], percentile: float) -> T:
        """
        Find a percentile of the array.

        Args:
            arr: Array
            percentile: Percentile (0.0 to 100.0)

        Returns:
            Percentile value
        """
        if not 0 <= percentile <= 100:
            raise ValueError("Percentile must be between 0 and 100")

        if not arr:
            raise ValueError("Cannot find percentile of empty array")

        n = len(arr)
        k = int((percentile / 100) * (n - 1))
        return SelectionAlgorithms.quickselect(arr, k)

    @staticmethod
    def select_top_k(arr: List[T], k: int) -> List[T]:
        """
        Find the k smallest elements.

        Args:
            arr: Array
            k: Number of elements to select

        Returns:
            List of k smallest elements (unsorted)
        """
        if k <= 0:
            return []
        if k >= len(arr):
            return arr.copy()

        # Use quickselect to find k-th element
        kth_element = SelectionAlgorithms.quickselect(arr, k - 1)

        # Collect all elements <= k-th element
        result = [x for x in arr if x <= kth_element]

        # If we have more than k elements, we need to trim
        # This is a simplified approach - a full implementation would
        # use more sophisticated selection
        return result[:k]

    @staticmethod
    def is_kth_smallest_correct(arr: List[T], k: int, candidate: T) -> bool:
        """
        Verify that candidate is indeed the k-th smallest element.

        Args:
            arr: Original array
            k: k value
            candidate: Candidate element

        Returns:
            True if candidate is correct
        """
        smaller_or_equal = sum(1 for x in arr if x <= candidate)
        larger = sum(1 for x in arr if x > candidate)

        return smaller_or_equal >= k + 1 and larger == len(arr) - (k + 1)


class SelectionAnalysis:
    """Analysis tools for selection algorithms."""

    @staticmethod
    def benchmark_selection_algorithms(
        arr: List[int], k: int, num_trials: int = 10
    ) -> dict:
        """
        Benchmark different selection algorithms.

        Args:
            arr: Test array
            k: k value for selection
            num_trials: Number of trials to average

        Returns:
            Dictionary with timing results
        """
        import time

        algorithms = [
            ("quickselect", SelectionAlgorithms.quickselect),
            ("quickselect_iterative", SelectionAlgorithms.quickselect_iterative),
            ("quickselect_random", SelectionAlgorithms.quickselect_random_pivot),
        ]

        results = {}

        for name, func in algorithms:
            times = []
            for _ in range(num_trials):
                arr_copy = arr.copy()
                start = time.time()
                result = func(arr_copy, k)
                end = time.time()
                times.append(end - start)

            results[name] = {
                "avg_time": sum(times) / len(times),
                "min_time": min(times),
                "max_time": max(times),
                "result": result,
            }

        return results

    @staticmethod
    def analyze_pivot_quality(arr: List[int], k: int, num_trials: int = 100) -> dict:
        """
        Analyze how pivot selection affects performance.

        Args:
            arr: Test array
            k: k value
            num_trials: Number of trials

        Returns:
            Analysis results
        """
        results = {"random_pivot": [], "median_of_three": []}

        for _ in range(num_trials):
            # Test random pivot
            arr_copy = arr.copy()
            start = time.time()
            SelectionAlgorithms.quickselect_random_pivot(arr_copy, k)
            results["random_pivot"].append(time.time() - start)

            # Test median of three
            arr_copy = arr.copy()
            start = time.time()
            SelectionAlgorithms.quickselect(arr_copy, k)
            results["median_of_three"].append(time.time() - start)

        # Calculate statistics
        for method in results:
            times = results[method]
            results[method] = {
                "avg_time": sum(times) / len(times),
                "min_time": min(times),
                "max_time": max(times),
                "std_dev": (
                    sum((t - sum(times) / len(times)) ** 2 for t in times) / len(times)
                )
                ** 0.5,
            }

        return results

    @staticmethod
    def test_correctness(arr: List[int], k: int) -> bool:
        """
        Test correctness by comparing with sorted array.

        Args:
            arr: Test array
            k: k value

        Returns:
            True if all algorithms give correct results
        """
        expected = sorted(arr)[k]

        algorithms = [
            SelectionAlgorithms.quickselect,
            SelectionAlgorithms.quickselect_iterative,
            SelectionAlgorithms.quickselect_random_pivot,
        ]

        for func in algorithms:
            result = func(arr.copy(), k)
            if result != expected:
                return False

        return True
