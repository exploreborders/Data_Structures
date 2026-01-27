"""
Chapter 11: Binary Search - Efficient Search Algorithms

This module implements various binary search algorithms and their applications,
demonstrating the power of divide-and-conquer search in sorted arrays.
"""

from typing import List, Optional, Tuple
import math


class BinarySearch:
    """Collection of binary search algorithms and variants."""

    @staticmethod
    def binary_search_iterative(arr: List[int], target: int) -> int:
        """
        Standard iterative binary search.

        Args:
            arr: Sorted list of integers
            target: Value to search for

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> BinarySearch.binary_search_iterative([1, 3, 5, 7, 9], 5)
            2
            >>> BinarySearch.binary_search_iterative([1, 3, 5, 7, 9], 6)
            -1
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2  # Prevents integer overflow

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def binary_search_recursive(arr: List[int], target: int,
                               left: int = 0, right: Optional[int] = None) -> int:
        """
        Standard recursive binary search.

        Args:
            arr: Sorted list of integers
            target: Value to search for
            left: Left boundary (internal use)
            right: Right boundary (internal use)

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> BinarySearch.binary_search_recursive([1, 3, 5, 7, 9], 5)
            2
            >>> BinarySearch.binary_search_recursive([1, 3, 5, 7, 9], 6)
            -1
        """
        if right is None:
            right = len(arr) - 1

        if left > right:
            return -1

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BinarySearch.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return BinarySearch.binary_search_recursive(arr, target, left, mid - 1)

    @staticmethod
    def find_first_occurrence(arr: List[int], target: int) -> int:
        """
        Find the first occurrence of target in a sorted array with duplicates.

        Args:
            arr: Sorted list of integers
            target: Value to search for

        Returns:
            Index of first occurrence of target, -1 if not found

        Examples:
            >>> BinarySearch.find_first_occurrence([1, 3, 3, 3, 5], 3)
            1
            >>> BinarySearch.find_first_occurrence([1, 3, 3, 3, 5], 4)
            -1
        """
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left for earlier occurrence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    @staticmethod
    def find_last_occurrence(arr: List[int], target: int) -> int:
        """
        Find the last occurrence of target in a sorted array with duplicates.

        Args:
            arr: Sorted list of integers
            target: Value to search for

        Returns:
            Index of last occurrence of target, -1 if not found

        Examples:
            >>> BinarySearch.find_last_occurrence([1, 3, 3, 3, 5], 3)
            3
            >>> BinarySearch.find_last_occurrence([1, 3, 3, 3, 5], 4)
            -1
        """
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right for later occurrence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    @staticmethod
    def lower_bound(arr: List[int], target: int) -> int:
        """
        Find the first position where target could be inserted to maintain sorted order.
        Also known as the insertion point.

        Args:
            arr: Sorted list of integers
            target: Value to find lower bound for

        Returns:
            Index where target should be inserted

        Examples:
            >>> BinarySearch.lower_bound([1, 3, 5, 7], 4)
            2
            >>> BinarySearch.lower_bound([1, 3, 5, 7], 3)
            1
        """
        left, right = 0, len(arr)

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    @staticmethod
    def upper_bound(arr: List[int], target: int) -> int:
        """
        Find the first position where elements are greater than target.

        Args:
            arr: Sorted list of integers
            target: Value to find upper bound for

        Returns:
            Index of first element greater than target

        Examples:
            >>> BinarySearch.upper_bound([1, 3, 5, 7], 4)
            2
            >>> BinarySearch.upper_bound([1, 3, 5, 7], 3)
            2
        """
        left, right = 0, len(arr)

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    @staticmethod
    def count_occurrences(arr: List[int], target: int) -> int:
        """
        Count the number of occurrences of target in a sorted array.

        Args:
            arr: Sorted list of integers
            target: Value to count

        Returns:
            Number of occurrences of target

        Examples:
            >>> BinarySearch.count_occurrences([1, 3, 3, 3, 5], 3)
            3
            >>> BinarySearch.count_occurrences([1, 3, 3, 3, 5], 4)
            0
        """
        first = BinarySearch.find_first_occurrence(arr, target)
        if first == -1:
            return 0

        last = BinarySearch.find_last_occurrence(arr, target)
        return last - first + 1


class BinarySearchApplications:
    """Applications of binary search beyond basic array search."""

    @staticmethod
    def square_root_binary_search(x: float, precision: float = 1e-6) -> float:
        """
        Calculate square root using binary search.

        Args:
            x: Number to find square root of (x >= 0)
            precision: Desired precision of result

        Returns:
            Square root of x

        Examples:
            >>> abs(BinarySearchApplications.square_root_binary_search(9) - 3) < 1e-6
            True
            >>> abs(BinarySearchApplications.square_root_binary_search(2) - 1.414213562) < 1e-5
            True
        """
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers")
        if x == 0 or x == 1:
            return x

        left, right = 0.0, max(1.0, x)

        while right - left > precision:
            mid = (left + right) / 2
            square = mid * mid

            if abs(square - x) < precision:
                return mid
            elif square < x:
                left = mid
            else:
                right = mid

        return (left + right) / 2

    @staticmethod
    def find_peak_element(arr: List[int]) -> int:
        """
        Find a peak element in an array (element >= neighbors).

        Args:
            arr: List of integers

        Returns:
            Index of a peak element

        Examples:
            >>> BinarySearchApplications.find_peak_element([1, 3, 2, 1])
            1
            >>> BinarySearchApplications.find_peak_element([1, 2, 3, 1])
            2
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check if mid is a peak
            if arr[mid] > arr[mid + 1]:
                right = mid  # Peak is in left half (including mid)
            else:
                left = mid + 1  # Peak is in right half

        return left

    @staticmethod
    def search_rotated_array(arr: List[int], target: int) -> int:
        """
        Search for target in a rotated sorted array.

        Args:
            arr: Rotated sorted array
            target: Value to search for

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> BinarySearchApplications.search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0)
            4
            >>> BinarySearchApplications.search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3)
            -1
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            # Check which half is sorted
            if arr[left] <= arr[mid]:  # Left half is sorted
                if arr[left] <= target < arr[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1   # Search right half
            else:  # Right half is sorted
                if arr[mid] < target <= arr[right]:
                    left = mid + 1   # Search right half
                else:
                    right = mid - 1  # Search left half

        return -1

    @staticmethod
    def find_minimum_in_rotated_array(arr: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array.

        Args:
            arr: Rotated sorted array

        Returns:
            Minimum element

        Examples:
            >>> BinarySearchApplications.find_minimum_in_rotated_array([4, 5, 6, 7, 0, 1, 2])
            0
            >>> BinarySearchApplications.find_minimum_in_rotated_array([1, 2, 3, 4, 5])
            1
        """
        left, right = 0, len(arr) - 1

        # If array is not rotated
        if arr[left] <= arr[right]:
            return arr[left]

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[right]:
                left = mid + 1  # Minimum is in right half
            else:
                right = mid     # Minimum is in left half (including mid)

        return arr[left]


class AdvancedSearch:
    """Advanced search algorithms that build on binary search."""

    @staticmethod
    def exponential_search(arr: List[int], target: int) -> int:
        """
        Exponential search: find range, then binary search.

        Args:
            arr: Sorted list of integers
            target: Value to search for

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> AdvancedSearch.exponential_search([1, 3, 5, 7, 9, 11, 13, 15], 7)
            3
            >>> AdvancedSearch.exponential_search([1, 3, 5, 7, 9, 11, 13, 15], 4)
            -1
        """
        if not arr:
            return -1

        if arr[0] == target:
            return 0

        # Find range where element might be
        i = 1
        while i < len(arr) and arr[i] <= target:
            i *= 2

        # Binary search in the found range
        left = i // 2
        right = min(i, len(arr) - 1)

        return BinarySearch.binary_search_iterative(arr[left:right+1], target) + left

    @staticmethod
    def interpolation_search(arr: List[int], target: int) -> int:
        """
        Interpolation search for uniformly distributed arrays.

        Args:
            arr: Sorted list of integers (assumed uniformly distributed)
            target: Value to search for

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> AdvancedSearch.interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
            6
            >>> AdvancedSearch.interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)
            -1
        """
        left, right = 0, len(arr) - 1

        while left <= right and arr[left] <= target <= arr[right]:
            if left == right:
                if arr[left] == target:
                    return left
                return -1

            # Interpolation formula
            pos = left + ((right - left) * (target - arr[left]) //
                         (arr[right] - arr[left]))

            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        return -1

    @staticmethod
    def ternary_search(arr: List[int], target: int) -> int:
        """
        Ternary search: divide array into three parts.

        Args:
            arr: Sorted list of integers
            target: Value to search for

        Returns:
            Index of target if found, -1 otherwise

        Examples:
            >>> AdvancedSearch.ternary_search([1, 3, 5, 7, 9, 11, 13, 15], 7)
            3
            >>> AdvancedSearch.ternary_search([1, 3, 5, 7, 9, 11, 13, 15], 4)
            -1
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            # Divide into three parts
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            if arr[mid1] == target:
                return mid1
            if arr[mid2] == target:
                return mid2

            if target < arr[mid1]:
                right = mid1 - 1
            elif target > arr[mid2]:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1