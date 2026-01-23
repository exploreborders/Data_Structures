"""
Tests for Chapter 19: Priority Queues - Binary Heap Implementation

Comprehensive tests covering heaps, priority queues, heapsort, and analysis tools.
"""

import pytest
import random
from chapter_19_priority_queues.code.heap_implementations import (
    BinaryHeap,
    PriorityQueue,
    HeapAnalysis,
)


class TestBinaryHeap:
    """Test BinaryHeap implementation."""

    def test_min_heap_creation(self):
        """Test min-heap creation."""
        heap = BinaryHeap[int]("min")
        assert len(heap) == 0
        assert heap.is_empty()
        assert heap.heap_type == "min"

    def test_max_heap_creation(self):
        """Test max-heap creation."""
        heap = BinaryHeap[int]("max")
        assert len(heap) == 0
        assert heap.is_empty()
        assert heap.heap_type == "max"

    def test_invalid_heap_type(self):
        """Test invalid heap type raises error."""
        with pytest.raises(ValueError):
            BinaryHeap("invalid")

    def test_min_heap_insert_and_extract(self):
        """Test min-heap insert and extract operations."""
        heap = BinaryHeap[int]("min")

        # Insert elements
        heap.insert(5)
        assert len(heap) == 1
        assert heap.peek() == 5

        heap.insert(3)
        assert len(heap) == 2
        assert heap.peek() == 3  # 3 should be at top

        heap.insert(7)
        assert len(heap) == 3
        assert heap.peek() == 3  # 3 still at top

        # Extract minimum
        assert heap.extract_top() == 3
        assert len(heap) == 2
        assert heap.peek() == 5

        assert heap.extract_top() == 5
        assert len(heap) == 1
        assert heap.peek() == 7

        assert heap.extract_top() == 7
        assert len(heap) == 0
        assert heap.is_empty()

    def test_max_heap_insert_and_extract(self):
        """Test max-heap insert and extract operations."""
        heap = BinaryHeap[int]("max")

        # Insert elements
        heap.insert(5)
        assert heap.peek() == 5

        heap.insert(3)
        assert heap.peek() == 5  # 5 should be at top

        heap.insert(7)
        assert heap.peek() == 7  # 7 should be at top

        # Extract maximum
        assert heap.extract_top() == 7
        assert heap.peek() == 5

        assert heap.extract_top() == 5
        assert heap.peek() == 3

        assert heap.extract_top() == 3
        assert heap.is_empty()

    def test_heap_build_from_list(self):
        """Test building heap from list."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        min_heap = BinaryHeap.from_list(arr, "min")
        assert len(min_heap) == len(arr)
        assert min_heap.is_valid_heap()

        # Should extract in sorted order for min-heap
        sorted_arr = []
        while not min_heap.is_empty():
            sorted_arr.append(min_heap.extract_top())
        assert sorted_arr == sorted(arr)

        max_heap = BinaryHeap.from_list(arr, "max")
        assert len(max_heap) == len(arr)
        assert max_heap.is_valid_heap()

        # Should extract in reverse sorted order for max-heap
        reverse_sorted = []
        while not max_heap.is_empty():
            reverse_sorted.append(max_heap.extract_top())
        assert reverse_sorted == sorted(arr, reverse=True)

    def test_empty_heap_operations(self):
        """Test operations on empty heap."""
        heap = BinaryHeap[int]("min")

        with pytest.raises(IndexError):
            heap.peek()

        with pytest.raises(IndexError):
            heap.extract_top()

    def test_heap_with_duplicates(self):
        """Test heap with duplicate values."""
        heap = BinaryHeap[int]("min")
        values = [3, 1, 4, 1, 5, 1, 9, 2, 6]

        for val in values:
            heap.insert(val)

        assert heap.is_valid_heap()

        # Extract all - should be in sorted order
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        assert extracted == sorted(values)

    def test_heap_with_strings(self):
        """Test heap with string elements."""
        heap = BinaryHeap[str]("min")
        words = ["banana", "apple", "cherry", "date"]

        for word in words:
            heap.insert(word)

        assert heap.is_valid_heap()

        # Extract all
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        assert extracted == sorted(words)

    def test_heap_sort(self):
        """Test heapsort functionality."""
        heap = BinaryHeap[int]("min")
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        sorted_arr = heap.heap_sort(arr)
        assert sorted_arr == sorted(arr)

        # Test sorting heap contents
        heap2 = BinaryHeap.from_list(arr, "min")
        sorted_heap = heap2.heap_sort()
        assert sorted_heap == sorted(arr)

    def test_large_heap(self):
        """Test heap with large number of elements."""
        heap = BinaryHeap[int]("min")
        size = 1000

        # Insert random elements
        elements = [random.randint(0, 10000) for _ in range(size)]
        for elem in elements:
            heap.insert(elem)

        assert len(heap) == size
        assert heap.is_valid_heap()

        # Extract all and verify sorted
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        assert extracted == sorted(elements)

    def test_heap_validity_check(self):
        """Test heap validity checking."""
        heap = BinaryHeap[int]("min")
        assert heap.is_valid_heap()  # Empty heap is valid

        heap.insert(5)
        assert heap.is_valid_heap()

        heap.insert(3)
        assert heap.is_valid_heap()

        heap.insert(7)
        assert heap.is_valid_heap()

        heap.insert(1)
        assert heap.is_valid_heap()


class TestPriorityQueue:
    """Test PriorityQueue implementation."""

    def test_priority_queue_creation(self):
        """Test priority queue creation."""
        pq = PriorityQueue[int]("min")
        assert len(pq) == 0
        assert pq.is_empty()

    def test_min_priority_queue(self):
        """Test min-priority queue."""
        pq = PriorityQueue[int]("min")

        pq.insert(5)
        pq.insert(3)
        pq.insert(7)
        pq.insert(1)

        assert len(pq) == 4
        assert pq.peek() == 1

        assert pq.remove_top() == 1
        assert pq.peek() == 3

        assert pq.remove_top() == 3
        assert pq.peek() == 5

        assert pq.remove_top() == 5
        assert pq.peek() == 7

        assert pq.remove_top() == 7
        assert pq.is_empty()

    def test_max_priority_queue(self):
        """Test max-priority queue."""
        pq = PriorityQueue[int]("max")

        pq.insert(5)
        pq.insert(3)
        pq.insert(7)
        pq.insert(1)

        assert pq.peek() == 7

        assert pq.remove_top() == 7
        assert pq.peek() == 5

        assert pq.remove_top() == 5
        assert pq.peek() == 3

        assert pq.remove_top() == 3
        assert pq.peek() == 1

        assert pq.remove_top() == 1
        assert pq.is_empty()

    def test_empty_priority_queue(self):
        """Test operations on empty priority queue."""
        pq = PriorityQueue[int]("min")

        with pytest.raises(IndexError):
            pq.peek()

        with pytest.raises(IndexError):
            pq.remove_top()


class TestHeapAnalysis:
    """Test heap analysis tools."""

    def test_benchmark_heap_operations(self):
        """Test heap benchmarking."""
        results = HeapAnalysis.benchmark_heap_operations("min", [50, 100])

        assert 50 in results
        assert 100 in results

        for size in [50, 100]:
            assert "build_heap_time" in results[size]
            assert "insert_time" in results[size]
            assert "extract_time" in results[size]
            assert "is_valid" in results[size]
            assert results[size]["is_valid"] is True

    def test_compare_heap_sort(self):
        """Test heapsort comparison."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        results = HeapAnalysis.compare_heap_sort_with_other_sorts(arr)

        assert "heapsort" in results
        assert "timsort" in results

        # All should be correct
        for algo in results:
            assert results[algo]["correct"] is True
            assert results[algo]["time"] >= 0

    def test_heap_height_analysis(self):
        """Test heap height analysis."""
        heap = BinaryHeap[int]("min")

        # Empty heap
        analysis = HeapAnalysis.analyze_heap_height(heap)
        assert analysis["height"] == 0
        assert analysis["size"] == 0

        # Add some elements
        for i in range(7):  # Perfect binary tree
            heap.insert(i)

        analysis = HeapAnalysis.analyze_heap_height(heap)
        assert analysis["size"] == 7
        assert analysis["height"] == 2  # 2^3 - 1 = 7 nodes
        assert analysis["is_perfect"] is True


class TestHeapEdgeCases:
    """Test edge cases and special scenarios."""

    def test_single_element_heap(self):
        """Test heap with single element."""
        heap = BinaryHeap[int]("min")
        heap.insert(42)

        assert len(heap) == 1
        assert heap.peek() == 42
        assert heap.extract_top() == 42
        assert heap.is_empty()

    def test_heap_with_negative_numbers(self):
        """Test heap with negative numbers."""
        heap = BinaryHeap[int]("min")
        values = [-5, 3, -1, 0, -10, 8]

        for val in values:
            heap.insert(val)

        assert heap.is_valid_heap()

        # Extract all
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        assert extracted == sorted(values)

    def test_heap_with_floats(self):
        """Test heap with floating point numbers."""
        heap = BinaryHeap[float]("min")
        values = [3.14, 1.41, 2.71, 0.58, -1.5]

        for val in values:
            heap.insert(val)

        assert heap.is_valid_heap()

        # Extract all
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        assert extracted == sorted(values)

    def test_priority_queue_with_custom_objects(self):
        """Test priority queue with custom comparable objects."""

        class Task:
            def __init__(self, priority: int, name: str):
                self.priority = priority
                self.name = name

            def __lt__(self, other):
                return self.priority < other.priority

            def __repr__(self):
                return f"Task({self.priority}, '{self.name}')"

        pq = PriorityQueue[Task]("min")

        tasks = [Task(3, "low"), Task(1, "high"), Task(2, "medium")]

        for task in tasks:
            pq.insert(task)

        # Should extract in priority order
        assert pq.remove_top().name == "high"  # priority 1
        assert pq.remove_top().name == "medium"  # priority 2
        assert pq.remove_top().name == "low"  # priority 3

    def test_heap_sort_stability_test(self):
        """Test heapsort correctness on various inputs."""
        test_cases = [
            [],
            [1],
            [1, 2],
            [2, 1],
            [3, 1, 4, 1, 5, 9, 2, 6],
            list(range(20, 0, -1)),  # Reverse sorted
            list(range(1, 21)),  # Already sorted
            [random.randint(0, 100) for _ in range(50)],  # Random
        ]

        heap = BinaryHeap[int]("min")

        for arr in test_cases:
            sorted_result = heap.heap_sort(arr)
            assert sorted_result == sorted(arr), f"Failed on {arr}"

    def test_heap_string_representation(self):
        """Test string representations of heap."""
        heap = BinaryHeap[int]("min")
        heap.insert(5)
        heap.insert(3)

        str_repr = str(heap)
        assert "MinHeap" in str_repr
        assert "[3, 5]" in str_repr  # Should show heap array

        repr_str = repr(heap)
        assert "BinaryHeap" in repr_str
        assert "heap_type='min'" in repr_str


class TestHeapPerformance:
    """Test heap performance characteristics."""

    def test_heap_vs_naive_priority_queue(self):
        """Compare heap with naive priority queue simulation."""
        # This is more of a conceptual test - in practice we'd use
        # the heap implementation and compare with a list-based approach
        heap = BinaryHeap[int]("min")

        # Insert many elements
        for i in range(100):
            heap.insert(random.randint(0, 1000))

        assert heap.is_valid_heap()

        # Extract all
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        # Should be sorted
        assert extracted == sorted(extracted)

    def test_heap_memory_usage(self):
        """Test that heap operations don't cause excessive memory usage."""
        heap = BinaryHeap[int]("min")

        # Insert many elements
        initial_size = len(heap.get_heap_array())
        for i in range(100):
            heap.insert(i)

        # Heap should grow but not excessively
        final_size = len(heap.get_heap_array())
        assert final_size >= 100  # At least as many as inserted
        assert final_size <= 200  # Not more than 2x (reasonable growth)

        # Extract some elements
        for _ in range(50):
            heap.extract_top()

        # Size should remain the same (we keep the array allocated)
        assert len(heap.get_heap_array()) == final_size
        assert len(heap) == 50
