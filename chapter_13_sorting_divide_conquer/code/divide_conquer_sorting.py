"""
Chapter 13: Sorting with Divide and Conquer - Mergesort and Quicksort

This module implements divide and conquer sorting algorithms: mergesort and quicksort,
demonstrating how these algorithms achieve O(n log n) performance through recursive decomposition.
"""

from typing import List, TypeVar, Callable
import time

T = TypeVar('T')


class DivideConquerSorting:
    """Implementation of divide and conquer sorting algorithms."""

    @staticmethod
    def mergesort(arr: List[T]) -> List[T]:
        """
        Mergesort: Divide and conquer sorting algorithm.

        Time: O(n log n) worst/average/best
        Space: O(n) - requires additional space for merging
        Stable: Yes - preserves relative order of equal elements
        Adaptive: No - same performance regardless of input

        Args:
            arr: List to sort

        Returns:
            New sorted list (original unchanged)

        Examples:
            >>> DivideConquerSorting.mergesort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        if len(arr) <= 1:
            return arr.copy()

        # Divide: Split array into two halves
        mid = len(arr) // 2
        left = DivideConquerSorting.mergesort(arr[:mid])
        right = DivideConquerSorting.mergesort(arr[mid:])

        # Conquer: Merge the sorted halves
        return DivideConquerSorting._merge(left, right)

    @staticmethod
    def _merge(left: List[T], right: List[T]) -> List[T]:
        """Merge two sorted lists into one sorted list."""
        result = []
        i = j = 0

        # Merge while both lists have elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    @staticmethod
    def mergesort_inplace(arr: List[T]) -> None:
        """
        In-place mergesort using indices instead of new arrays.

        Time: O(n log n)
        Space: O(n) - still needs temporary space for merging
        Stable: Yes

        Args:
            arr: List to sort in-place

        Examples:
            >>> arr = [3, 1, 4, 1, 5]
            >>> DivideConquerSorting.mergesort_inplace(arr)
            >>> arr
            [1, 1, 3, 4, 5]
        """
        def _mergesort_helper(start: int, end: int) -> None:
            if end - start <= 1:
                return

            mid = (start + end) // 2
            _mergesort_helper(start, mid)
            _mergesort_helper(mid, end)
            _merge_inplace(start, mid, end)

        def _merge_inplace(start: int, mid: int, end: int) -> None:
            # Create temporary arrays
            left = arr[start:mid]
            right = arr[mid:end]

            i = j = 0
            k = start

            # Merge back into original array
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        _mergesort_helper(0, len(arr))

    @staticmethod
    def quicksort(arr: List[T]) -> List[T]:
        """
        Quicksort: Divide and conquer sorting using partitioning.

        Time: O(n²) worst case, O(n log n) average/best case
        Space: O(log n) average (recursion stack)
        Stable: No - may change relative order of equal elements
        Adaptive: No - same performance regardless of input order

        Args:
            arr: List to sort

        Returns:
            New sorted list (original unchanged)

        Examples:
            >>> DivideConquerSorting.quicksort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        arr_copy = arr.copy()
        DivideConquerSorting._quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    @staticmethod
    def quicksort_inplace(arr: List[T]) -> None:
        """
        In-place quicksort implementation.

        Args:
            arr: List to sort in-place

        Examples:
            >>> arr = [3, 1, 4, 1, 5]
            >>> DivideConquerSorting.quicksort_inplace(arr)
            >>> arr
            [1, 1, 3, 4, 5]
        """
        DivideConquerSorting._quicksort_helper(arr, 0, len(arr) - 1)

    @staticmethod
    def _quicksort_helper(arr: List[T], low: int, high: int) -> None:
        """Recursive quicksort helper."""
        if low < high:
            # Partition and get pivot index
            pivot_idx = DivideConquerSorting._partition(arr, low, high)

            # Recursively sort left and right partitions
            DivideConquerSorting._quicksort_helper(arr, low, pivot_idx - 1)
            DivideConquerSorting._quicksort_helper(arr, pivot_idx + 1, high)

    @staticmethod
    def _partition(arr: List[T], low: int, high: int) -> int:
        """Partition array around pivot using Lomuto scheme."""
        # Choose rightmost element as pivot
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    @staticmethod
    def quicksort_median_pivot(arr: List[T]) -> List[T]:
        """
        Quicksort with median-of-three pivot selection for better performance.

        Args:
            arr: List to sort

        Returns:
            New sorted list

        Examples:
            >>> DivideConquerSorting.quicksort_median_pivot([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        arr_copy = arr.copy()
        DivideConquerSorting._quicksort_median_helper(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    @staticmethod
    def _quicksort_median_helper(arr: List[T], low: int, high: int) -> None:
        """Quicksort with median-of-three pivot selection."""
        if low < high:
            # Choose pivot using median of three
            pivot_idx = DivideConquerSorting._choose_median_pivot(arr, low, high)
            # Swap pivot to end
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

            # Partition
            pivot_idx = DivideConquerSorting._partition(arr, low, high)

            # Recurse
            DivideConquerSorting._quicksort_median_helper(arr, low, pivot_idx - 1)
            DivideConquerSorting._quicksort_median_helper(arr, pivot_idx + 1, high)

    @staticmethod
    def _choose_median_pivot(arr: List[T], low: int, high: int) -> int:
        """Choose pivot using median of three elements."""
        mid = (low + high) // 2

        # Find median of arr[low], arr[mid], arr[high]
        if arr[low] <= arr[mid] <= arr[high] or arr[high] <= arr[mid] <= arr[low]:
            return mid
        elif arr[mid] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[mid]:
            return low
        else:
            return high

    @staticmethod
    def introsort_like(arr: List[T]) -> List[T]:
        """
        Hybrid sorting algorithm inspired by introsort (used in C++ std::sort).

        Uses quicksort with median-of-three, switches to heapsort for worst case,
        and finishes with insertion sort for small arrays.

        Args:
            arr: List to sort

        Returns:
            Sorted list

        Examples:
            >>> DivideConquerSorting.introsort_like([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        arr_copy = arr.copy()
        max_depth = 2 * (len(arr_copy).bit_length() - 1)  # 2 * log2(n)
        DivideConquerSorting._introsort_helper(arr_copy, 0, len(arr_copy) - 1, max_depth)
        return arr_copy

    @staticmethod
    def _introsort_helper(arr: List[T], low: int, high: int, max_depth: int) -> None:
        """Introsort helper with depth limit."""
        if high - low <= 16:  # Small array - use insertion sort
            DivideConquerSorting._insertion_sort_range(arr, low, high)
            return

        if max_depth == 0:  # Recursion too deep - switch to heapsort
            DivideConquerSorting._heapsort_range(arr, low, high)
            return

        # Choose pivot and partition
        pivot_idx = DivideConquerSorting._choose_median_pivot(arr, low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

        pivot_idx = DivideConquerSorting._partition(arr, low, high)

        # Recurse with reduced depth
        DivideConquerSorting._introsort_helper(arr, low, pivot_idx - 1, max_depth - 1)
        DivideConquerSorting._introsort_helper(arr, pivot_idx + 1, high, max_depth - 1)

    @staticmethod
    def _insertion_sort_range(arr: List[T], low: int, high: int) -> None:
        """Insertion sort for a subarray."""
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            while j >= low and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def _heapsort_range(arr: List[T], low: int, high: int) -> None:
        """Heapsort for a subarray."""
        # Build max heap
        for i in range((high - low + 1) // 2 - 1, -1, -1):
            DivideConquerSorting._heapify_range(arr, high - low + 1, i + low, low, high)

        # Extract elements
        for i in range(high, low, -1):
            arr[low], arr[i] = arr[i], arr[low]
            DivideConquerSorting._heapify_range(arr, i - low, low, low, i - 1)

    @staticmethod
    def _heapify_range(arr: List[T], n: int, i: int, low: int, high: int) -> None:
        """Heapify a subtree in a subarray."""
        largest = i
        left = 2 * (i - low) + 1 + low
        right = 2 * (i - low) + 2 + low

        if left <= high and arr[left] > arr[largest]:
            largest = left
        if right <= high and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            DivideConquerSorting._heapify_range(arr, n, largest, low, high)


class SortingAnalysis:
    """Analysis tools for divide and conquer sorting algorithms."""

    @staticmethod
    def benchmark_sorting_algorithms(arr: List[int], algorithms: List[Callable]) -> dict:
        """
        Benchmark multiple sorting algorithms on the same data.

        Args:
            arr: Test array
            algorithms: List of (name, function) tuples

        Returns:
            Dictionary with timing results
        """
        results = {}

        for name, sort_func in algorithms:
            arr_copy = arr.copy()
            start_time = time.time()

            if "inplace" in name.lower():
                sort_func(arr_copy)
                result = arr_copy
            else:
                result = sort_func(arr_copy)

            end_time = time.time()

            results[name] = {
                "time": end_time - start_time,
                "correct": SortingAnalysis.is_sorted(result)
            }

        return results

    @staticmethod
    def is_sorted(arr: List[T]) -> bool:
        """Check if array is sorted in ascending order."""
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    @staticmethod
    def generate_test_data(size: int, distribution: str = "random") -> List[int]:
        """
        Generate test data with different distributions.

        Args:
            size: Size of array
            distribution: "random", "sorted", "reverse", "nearly_sorted"

        Returns:
            Generated array
        """
        import random

        if distribution == "random":
            return [random.randint(0, size * 10) for _ in range(size)]
        elif distribution == "sorted":
            return list(range(size))
        elif distribution == "reverse":
            return list(range(size, 0, -1))
        elif distribution == "nearly_sorted":
            arr = list(range(size))
            # Swap a few elements
            for _ in range(size // 10):
                i, j = random.randint(0, size - 1), random.randint(0, size - 1)
                arr[i], arr[j] = arr[j], arr[i]
            return arr
        else:
            raise ValueError(f"Unknown distribution: {distribution}")

    @staticmethod
    def compare_stability() -> dict:
        """
        Compare stability of different sorting algorithms.

        Returns:
            Dictionary showing stability results
        """
        # Create array with equal elements but different identities
        class Item:
            def __init__(self, value, id):
                self.value = value
                self.id = id

            def __lt__(self, other):
                return self.value < other.value

            def __repr__(self):
                return f"Item({self.value}, {self.id})"

        # Array with duplicate values
        arr = [Item(1, 'a'), Item(2, 'b'), Item(1, 'c'), Item(3, 'd'), Item(1, 'e')]

        results = {}

        # Test mergesort (should be stable)
        merge_result = DivideConquerSorting.mergesort(arr)
        merge_stable = (merge_result[0].id == 'a' and merge_result[2].id == 'c' and
                       merge_result[4].id == 'e')
        results["Mergesort"] = merge_stable

        # Test quicksort (may not be stable)
        quick_result = DivideConquerSorting.quicksort(arr)
        # Quicksort stability depends on implementation
        quick_stable = SortingAnalysis.is_sorted([item.value for item in quick_result])
        results["Quicksort"] = quick_stable

        return results

    @staticmethod
    def analyze_recursion_depth(arr: List[int], algorithm: str = "quicksort") -> int:
        """
        Analyze maximum recursion depth for sorting algorithms.

        Args:
            arr: Array to sort
            algorithm: "quicksort" or "mergesort"

        Returns:
            Maximum recursion depth encountered
        """
        max_depth = 0
        current_depth = 0

        def track_depth(func):
            def wrapper(*args, **kwargs):
                nonlocal current_depth, max_depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)
                try:
                    return func(*args, **kwargs)
                finally:
                    current_depth -= 1
            return wrapper

        if algorithm == "quicksort":
            original_helper = DivideConquerSorting._quicksort_helper
            DivideConquerSorting._quicksort_helper = track_depth(DivideConquerSorting._quicksort_helper)

            try:
                arr_copy = arr.copy()
                DivideConquerSorting._quicksort_helper(arr_copy, 0, len(arr_copy) - 1)
            finally:
                DivideConquerSorting._quicksort_helper = original_helper

        return max_depth</content>
<parameter name="filePath">chapter_13_sorting_divide_conquer/code/divide_conquer_sorting.py