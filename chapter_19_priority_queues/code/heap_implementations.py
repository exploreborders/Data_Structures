"""
Chapter 19: Priority Queues - Binary Heap Implementation

This module implements priority queues using binary heaps, providing efficient
O(log n) operations for priority-based element management.
"""

from typing import List, TypeVar, Generic, Optional, Callable
import random

T = TypeVar("T")


class BinaryHeap(Generic[T]):
    """
    Binary Heap implementation supporting both min-heap and max-heap variants.

    A binary heap is a complete binary tree where each node satisfies the heap property:
    - Min-heap: parent ≤ children
    - Max-heap: parent ≥ children

    Time Complexity:
    - insert: O(log n)
    - extract_min/max: O(log n)
    - peek: O(1)
    - build_heap: O(n)
    """

    def __init__(self, heap_type: str = "min", initial_capacity: int = 16):
        """
        Initialize binary heap.

        Args:
            heap_type: "min" for min-heap, "max" for max-heap
            initial_capacity: Initial capacity of the underlying array
        """
        if heap_type not in ["min", "max"]:
            raise ValueError("heap_type must be 'min' or 'max'")

        self.heap_type = heap_type
        self._heap: List[T] = []
        self._size = 0
        self._capacity = initial_capacity

        # Comparison function based on heap type
        self._compare = self._less_than if heap_type == "min" else self._greater_than

    def __len__(self) -> int:
        """Return number of elements in heap."""
        return self._size

    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return self._size == 0

    def _less_than(self, a: T, b: T) -> bool:
        """Compare function for min-heap."""
        return a < b

    def _greater_than(self, a: T, b: T) -> bool:
        """Compare function for max-heap."""
        return a > b

    def _parent(self, index: int) -> int:
        """Get parent index."""
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """Get left child index."""
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """Get right child index."""
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        """Swap elements at indices i and j."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def insert(self, item: T) -> None:
        """
        Insert item into heap.

        Args:
            item: Item to insert
        """
        if self._size >= self._capacity:
            self._capacity *= 2
            # In Python, list automatically resizes, so we don't need explicit capacity management

        self._heap.append(item)
        self._size += 1
        self._bubble_up(self._size - 1)

    def _bubble_up(self, index: int) -> None:
        """Bubble up element at index to maintain heap property."""
        while index > 0:
            parent_idx = self._parent(index)
            if self._compare(self._heap[index], self._heap[parent_idx]):
                self._swap(index, parent_idx)
                index = parent_idx
            else:
                break

    def extract_top(self) -> T:
        """
        Remove and return the top element (min for min-heap, max for max-heap).

        Returns:
            Top element

        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty heap")

        top = self._heap[0]

        # Move last element to root
        last = self._heap[self._size - 1]
        self._heap[0] = last
        self._size -= 1
        self._heap.pop()  # Remove the last element

        if self._size > 0:
            self._sink_down(0)

        return top

    def _sink_down(self, index: int) -> None:
        """Sink down element at index to maintain heap property."""
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest_or_largest = index

            # Find the appropriate child to swap with
            if left < self._size and self._compare(
                self._heap[left], self._heap[smallest_or_largest]
            ):
                smallest_or_largest = left

            if right < self._size and self._compare(
                self._heap[right], self._heap[smallest_or_largest]
            ):
                smallest_or_largest = right

            if smallest_or_largest != index:
                self._swap(index, smallest_or_largest)
                index = smallest_or_largest
            else:
                break

    def peek(self) -> T:
        """
        Return the top element without removing it.

        Returns:
            Top element

        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek into empty heap")
        return self._heap[0]

    def build_heap(self, items: List[T]) -> None:
        """
        Build heap from list of items in O(n) time.

        Args:
            items: List of items to build heap from
        """
        self._heap = items.copy()
        self._size = len(items)

        # Start from the last non-leaf node and sink down
        for i in range(self._size // 2 - 1, -1, -1):
            self._sink_down(i)

    @classmethod
    def from_list(cls, items: List[T], heap_type: str = "min") -> "BinaryHeap[T]":
        """
        Create heap from list of items.

        Args:
            items: List of items
            heap_type: "min" or "max"

        Returns:
            BinaryHeap instance
        """
        heap = cls(heap_type)
        heap.build_heap(items)
        return heap

    def __str__(self) -> str:
        """String representation of heap."""
        return f"{self.heap_type.capitalize()}Heap({self._heap[: self._size]})"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"BinaryHeap(heap_type='{self.heap_type}', size={self._size}, heap={self._heap[: self._size]})"

    def get_heap_array(self) -> List[T]:
        """Get the heap as a list (for debugging/visualization)."""
        return self._heap[: self._size]

    def is_valid_heap(self) -> bool:
        """
        Check if the heap maintains the heap property.

        Returns:
            True if heap property is maintained
        """
        for i in range(self._size):
            left = self._left_child(i)
            right = self._right_child(i)

            if left < self._size and not self._compare(self._heap[i], self._heap[left]):
                return False
            if right < self._size and not self._compare(
                self._heap[i], self._heap[right]
            ):
                return False
        return True

    def heap_sort(self, arr: Optional[List[T]] = None) -> List[T]:
        """
        Sort array using heapsort algorithm.

        Args:
            arr: Array to sort (uses heap contents if None)

        Returns:
            Sorted list
        """
        if arr is None:
            # Sort the heap contents
            result = []
            temp_heap = BinaryHeap(self.heap_type)
            temp_heap._heap = self._heap[: self._size]
            temp_heap._size = self._size

            while not temp_heap.is_empty():
                result.append(temp_heap.extract_top())
            return result
        else:
            # Sort external array
            temp_heap = BinaryHeap(self.heap_type)
            temp_heap.build_heap(arr.copy())

            result = []
            while not temp_heap.is_empty():
                result.append(temp_heap.extract_top())
            return result


class PriorityQueue(Generic[T]):
    """
    Priority Queue ADT implemented using binary heap.

    Supports efficient insertion and removal of highest/lowest priority elements.
    """

    def __init__(self, heap_type: str = "min", initial_capacity: int = 16):
        """
        Initialize priority queue.

        Args:
            heap_type: "min" for min-priority, "max" for max-priority
            initial_capacity: Initial capacity
        """
        self._heap = BinaryHeap[T](heap_type, initial_capacity)

    def __len__(self) -> int:
        """Return number of elements in priority queue."""
        return len(self._heap)

    def is_empty(self) -> bool:
        """Check if priority queue is empty."""
        return self._heap.is_empty()

    def insert(self, item: T) -> None:
        """
        Insert item into priority queue.

        Args:
            item: Item to insert
        """
        self._heap.insert(item)

    def remove_top(self) -> T:
        """
        Remove and return the highest priority element.

        Returns:
            Highest priority element

        Raises:
            IndexError: If queue is empty
        """
        return self._heap.extract_top()

    def peek(self) -> T:
        """
        Return the highest priority element without removing it.

        Returns:
            Highest priority element

        Raises:
            IndexError: If queue is empty
        """
        return self._heap.peek()

    def __str__(self) -> str:
        """String representation."""
        return f"PriorityQueue({self._heap.heap_type}, size={len(self._heap)})"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return (
            f"PriorityQueue(heap_type='{self._heap.heap_type}', size={len(self._heap)})"
        )


class HeapAnalysis:
    """Analysis tools for heap operations and performance."""

    @staticmethod
    def benchmark_heap_operations(
        heap_type: str = "min", sizes: List[int] = None
    ) -> dict:
        """
        Benchmark heap operations for different sizes.

        Args:
            heap_type: "min" or "max"
            sizes: List of heap sizes to test

        Returns:
            Benchmark results
        """
        if sizes is None:
            sizes = [100, 1000, 10000]

        results = {}

        for size in sizes:
            # Generate random data
            data = [random.randint(0, 1000000) for _ in range(size)]

            # Benchmark build_heap
            heap = BinaryHeap[T](heap_type)
            start_time = time.time()
            heap.build_heap(data)
            build_time = time.time() - start_time

            # Benchmark insertions
            heap2 = BinaryHeap[T](heap_type)
            start_time = time.time()
            for item in data:
                heap2.insert(item)
            insert_time = time.time() - start_time

            # Benchmark extractions
            start_time = time.time()
            while not heap.is_empty():
                heap.extract_top()
            extract_time = time.time() - start_time

            results[size] = {
                "build_heap_time": build_time,
                "insert_time": insert_time,
                "extract_time": extract_time,
                "is_valid": heap.is_valid_heap(),
            }

        return results

    @staticmethod
    def compare_heap_sort_with_other_sorts(
        arr: List[int], algorithms: List[str] = None
    ) -> dict:
        """
        Compare heapsort with other sorting algorithms.

        Args:
            arr: Array to sort
            algorithms: List of algorithms to compare

        Returns:
            Comparison results
        """
        if algorithms is None:
            algorithms = ["heapsort", "timsort", "quicksort"]

        results = {}
        arr_copy = arr.copy()

        # Heapsort
        if "heapsort" in algorithms:
            heap = BinaryHeap[int]("min")
            start_time = time.time()
            heap_sorted = heap.heap_sort(arr)
            heap_time = time.time() - start_time
            results["heapsort"] = {
                "time": heap_time,
                "correct": heap_sorted == sorted(arr),
            }

        # Timsort (Python's built-in)
        if "timsort" in algorithms:
            start_time = time.time()
            timsort_result = sorted(arr_copy)
            timsort_time = time.time() - start_time
            results["timsort"] = {
                "time": timsort_time,
                "correct": timsort_result == sorted(arr),
            }

        # Simple quicksort simulation (worst case for sorted input)
        if "quicksort" in algorithms:
            # This is a simplified comparison
            start_time = time.time()
            quicksort_result = sorted(arr_copy, reverse=True)  # Simulate worst case
            quicksort_result.sort()  # Then sort it
            quicksort_time = time.time() - start_time
            results["quicksort"] = {
                "time": quicksort_time,
                "correct": quicksort_result == sorted(arr),
            }

        return results

    @staticmethod
    def analyze_heap_height(heap: BinaryHeap[T]) -> dict:
        """
        Analyze heap height and structure.

        Args:
            heap: Heap to analyze

        Returns:
            Analysis results
        """
        import math

        size = len(heap)
        if size == 0:
            return {"height": 0, "perfect_height": 0, "is_perfect": True}

        # Theoretical height for perfect binary tree
        perfect_height = int(math.log2(size))

        # Actual height (from root to deepest leaf)
        actual_height = 0
        nodes_at_level = 1
        remaining_nodes = size - 1

        while remaining_nodes > 0:
            actual_height += 1
            nodes_at_level *= 2
            remaining_nodes -= min(nodes_at_level, remaining_nodes)

        return {
            "size": size,
            "height": actual_height,
            "perfect_height": perfect_height,
            "is_perfect": size == 2 ** (actual_height + 1) - 1,
            "efficiency": size / (2 ** (actual_height + 1) - 1),
        }


# Import time at module level for analysis functions
import time
