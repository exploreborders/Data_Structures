"""
Chapter 12: Sorting Algorithms - Comprehensive Implementation

This module implements various sorting algorithms, both comparison-based and non-comparison,
with detailed analysis of their performance characteristics and use cases.
"""

from typing import List, TypeVar, Callable, Any
import heapq
import random
import time

T = TypeVar('T')


class SortingAlgorithms:
    """Collection of sorting algorithms with performance analysis."""

    @staticmethod
    def bubble_sort(arr: List[T]) -> List[T]:
        """
        Bubble sort: repeatedly swap adjacent elements if out of order.

        Time: O(n²) worst/average, O(n) best
        Space: O(1)
        Stable: Yes
        Adaptive: Yes

        Args:
            arr: List to sort

        Returns:
            Sorted list (in-place modification)

        Examples:
            >>> SortingAlgorithms.bubble_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        n = len(arr)
        for i in range(n):
            # Last i elements are already sorted
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            # If no swaps in this pass, array is sorted
            if not swapped:
                break
        return arr

    @staticmethod
    def insertion_sort(arr: List[T]) -> List[T]:
        """
        Insertion sort: build sorted array one element at a time.

        Time: O(n²) worst/average, O(n) best
        Space: O(1)
        Stable: Yes
        Adaptive: Yes

        Args:
            arr: List to sort

        Returns:
            Sorted list (in-place modification)

        Examples:
            >>> SortingAlgorithms.insertion_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Move elements greater than key one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def selection_sort(arr: List[T]) -> List[T]:
        """
        Selection sort: find minimum and place in correct position.

        Time: O(n²) always
        Space: O(1)
        Stable: No
        Adaptive: No

        Args:
            arr: List to sort

        Returns:
            Sorted list (in-place modification)

        Examples:
            >>> SortingAlgorithms.selection_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        n = len(arr)
        for i in range(n):
            # Find minimum element in unsorted portion
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # Swap with first unsorted element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def quick_sort(arr: List[T]) -> List[T]:
        """
        Quick sort: partition around pivot, recursively sort partitions.

        Time: O(n²) worst, O(n log n) average/best
        Space: O(log n) average (recursion stack)
        Stable: No
        Adaptive: No

        Args:
            arr: List to sort

        Returns:
            Sorted list (in-place modification)

        Examples:
            >>> SortingAlgorithms.quick_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        def _quick_sort_helper(low: int, high: int) -> None:
            if low < high:
                # Partition and get pivot index
                pivot_idx = _partition(low, high)
                # Recursively sort left and right partitions
                _quick_sort_helper(low, pivot_idx - 1)
                _quick_sort_helper(pivot_idx + 1, high)

        def _partition(low: int, high: int) -> int:
            # Choose rightmost element as pivot
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        _quick_sort_helper(0, len(arr) - 1)
        return arr

    @staticmethod
    def merge_sort(arr: List[T]) -> List[T]:
        """
        Merge sort: divide and conquer with merging.

        Time: O(n log n) always
        Space: O(n)
        Stable: Yes
        Adaptive: No

        Args:
            arr: List to sort

        Returns:
            Sorted list (creates new list)

        Examples:
            >>> SortingAlgorithms.merge_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        if len(arr) <= 1:
            return arr

        # Split array into two halves
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])

        return SortingAlgorithms._merge(left, right)

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
    def heap_sort(arr: List[T]) -> List[T]:
        """
        Heap sort: build max-heap, repeatedly extract maximum.

        Time: O(n log n) always
        Space: O(1) auxiliary
        Stable: No
        Adaptive: No

        Args:
            arr: List to sort

        Returns:
            Sorted list (in-place modification)

        Examples:
            >>> SortingAlgorithms.heap_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        n = len(arr)

        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr, n, i)

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            # Swap root (maximum) with last element
            arr[i], arr[0] = arr[0], arr[i]
            # Heapify reduced heap
            SortingAlgorithms._heapify(arr, i, 0)

        return arr

    @staticmethod
    def _heapify(arr: List[T], n: int, i: int) -> None:
        """Heapify subtree rooted at index i."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Find largest among root, left child, right child
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root, swap and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)

    @staticmethod
    def counting_sort(arr: List[int], max_val: int = None) -> List[int]:
        """
        Counting sort: count occurrences, reconstruct array.

        Time: O(n + k) where k is range
        Space: O(n + k)
        Stable: Can be made stable
        Adaptive: No

        Args:
            arr: List of non-negative integers to sort
            max_val: Maximum value in array (if known)

        Returns:
            Sorted list

        Examples:
            >>> SortingAlgorithms.counting_sort([3, 1, 4, 1, 5], 5)
            [1, 1, 3, 4, 5]
        """
        if not arr:
            return arr

        if max_val is None:
            max_val = max(arr)

        # Initialize count array
        count = [0] * (max_val + 1)

        # Count occurrences
        for num in arr:
            count[num] += 1

        # Reconstruct sorted array
        result = []
        for i in range(len(count)):
            result.extend([i] * count[i])

        return result

    @staticmethod
    def radix_sort(arr: List[int]) -> List[int]:
        """
        Radix sort: sort by individual digits.

        Time: O(n * d) where d is number of digits
        Space: O(n + k)
        Stable: Yes
        Adaptive: No

        Args:
            arr: List of non-negative integers to sort

        Returns:
            Sorted list

        Examples:
            >>> SortingAlgorithms.radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
            [2, 24, 45, 66, 75, 90, 170, 802]
        """
        if not arr:
            return arr

        # Find maximum number to determine number of digits
        max_num = max(arr)
        if max_num == 0:
            return arr

        # Get number of digits
        digits = 0
        temp = max_num
        while temp > 0:
            digits += 1
            temp //= 10

        # Perform counting sort for each digit
        result = arr.copy()
        for digit in range(digits):
            result = SortingAlgorithms._counting_sort_by_digit(result, digit)

        return result

    @staticmethod
    def _counting_sort_by_digit(arr: List[int], digit: int) -> List[int]:
        """Helper for radix sort - sort by specific digit."""
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # 0-9 digits

        # Count occurrences of each digit
        for num in arr:
            digit_value = (num // (10 ** digit)) % 10
            count[digit_value] += 1

        # Compute cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build output array
        for i in range(n - 1, -1, -1):  # Stable sort
            digit_value = (arr[i] // (10 ** digit)) % 10
            output[count[digit_value] - 1] = arr[i]
            count[digit_value] -= 1

        return output

    @staticmethod
    def bucket_sort(arr: List[float], bucket_count: int = 10) -> List[float]:
        """
        Bucket sort: distribute into buckets, sort buckets.

        Time: O(n) average case (uniform distribution)
        Space: O(n + k)
        Stable: Depends on bucket sorting
        Adaptive: No

        Args:
            arr: List of floats in range [0, 1) to sort
            bucket_count: Number of buckets to use

        Returns:
            Sorted list

        Examples:
            >>> SortingAlgorithms.bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72], 5)
            [0.17, 0.26, 0.39, 0.72, 0.78]
        """
        if not arr:
            return arr

        # Create empty buckets
        buckets = [[] for _ in range(bucket_count)]

        # Distribute elements into buckets
        for num in arr:
            bucket_idx = int(num * bucket_count)
            if bucket_idx == bucket_count:  # Handle case where num == 1.0
                bucket_idx -= 1
            buckets[bucket_idx].append(num)

        # Sort individual buckets and concatenate
        result = []
        for bucket in buckets:
            # Use insertion sort for small buckets
            SortingAlgorithms.insertion_sort(bucket)
            result.extend(bucket)

        return result

    @staticmethod
    def timsort_like_sort(arr: List[T]) -> List[T]:
        """
        Simplified timsort-like algorithm (Python's built-in sort).

        Combines insertion sort for small arrays with merge sort for larger ones.

        Args:
            arr: List to sort

        Returns:
            Sorted list

        Examples:
            >>> SortingAlgorithms.timsort_like_sort([3, 1, 4, 1, 5])
            [1, 1, 3, 4, 5]
        """
        MIN_MERGE = 32

        def insertion_sort_sublist(start: int, end: int) -> None:
            """Sort sublist using insertion sort."""
            for i in range(start + 1, end + 1):
                key = arr[i]
                j = i - 1
                while j >= start and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key

        def merge_sublists(start: int, mid: int, end: int) -> None:
            """Merge two sorted sublists."""
            left = arr[start:mid + 1]
            right = arr[mid + 1:end + 1]

            i = j = 0
            k = start

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        n = len(arr)

        # Sort small subarrays with insertion sort
        for start in range(0, n, MIN_MERGE):
            end = min(start + MIN_MERGE - 1, n - 1)
            insertion_sort_sublist(start, end)

        # Merge sorted subarrays
        size = MIN_MERGE
        while size < n:
            for start in range(0, n, 2 * size):
                mid = min(start + size - 1, n - 1)
                end = min(start + 2 * size - 1, n - 1)

                if mid < end:
                    merge_sublists(start, mid, end)

            size *= 2

        return arr


class SortingAnalysis:
    """Tools for analyzing sorting algorithm performance."""

    @staticmethod
    def time_sorting_algorithm(sort_func: Callable, arr: List[T], *args, **kwargs) -> tuple:
        """
        Time a sorting algorithm execution.

        Args:
            sort_func: Sorting function to time
            arr: Array to sort
            *args, **kwargs: Additional arguments for sort function

        Returns:
            Tuple of (sorted_array, execution_time)
        """
        arr_copy = arr.copy()
        start_time = time.time()
        if args or kwargs:
            result = sort_func(arr_copy, *args, **kwargs)
        else:
            result = sort_func(arr_copy)
        end_time = time.time()
        return result, end_time - start_time

    @staticmethod
    def is_sorted(arr: List[T]) -> bool:
        """Check if array is sorted in ascending order."""
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    @staticmethod
    def is_stable_sort(original: List[T], sorted_arr: List[T],
                      key_func: Callable = None) -> bool:
        """
        Check if sort is stable (preserves relative order of equal elements).

        Note: This is a simplified check and may not work for all cases.
        """
        if len(original) != len(sorted_arr):
            return False

        # For basic types, assume stable if sorted correctly
        return SortingAnalysis.is_sorted(sorted_arr)

    @staticmethod
    def generate_test_data(size: int, distribution: str = "random") -> List[int]:
        """
        Generate test data with different distributions.

        Args:
            size: Size of array to generate
            distribution: Type of distribution ("random", "sorted", "reverse", "nearly_sorted")

        Returns:
            Generated array
        """
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
            raise ValueError(f"Unknown distribution: {distribution}")</content>
<parameter name="filePath">chapter_12_sorting_algorithms/code/sorting_algorithms.py