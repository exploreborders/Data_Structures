"""
Chapter 19 Examples: Priority Queues - Binary Heap Demonstrations

Interactive demonstrations of heap operations, priority queues, and heapsort.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'code'))
from heap_implementations import BinaryHeap, PriorityQueue, HeapAnalysis


def demonstrate_heap_operations():
    """Demonstrate basic heap operations."""
    print("=== Basic Heap Operations ===\n")

    # Min-heap demonstration
    print("Min-Heap Operations:")
    min_heap = BinaryHeap[int]("min")

    values = [5, 3, 8, 1, 9, 2, 7]
    print(f"Inserting values: {values}")

    for val in values:
        min_heap.insert(val)
        print(f"  After inserting {val}: heap = {min_heap.get_heap_array()}, valid = {min_heap.is_valid_heap()}")

    print(f"\nFinal heap: {min_heap.get_heap_array()}")
    print(f"Heap property maintained: {min_heap.is_valid_heap()}")
    print(f"Minimum element: {min_heap.peek()}")

    # Extract elements
    print("\nExtracting minimum elements:")
    while not min_heap.is_empty():
        min_val = min_heap.extract_top()
        print(f"  Extracted: {min_val}, remaining: {min_heap.get_heap_array()}")

    print()


def demonstrate_max_heap_vs_min_heap():
    """Compare min-heap and max-heap behavior."""
    print("\n=== Min-Heap vs Max-Heap Comparison ===\n")

    values = [4, 2, 7, 1, 9, 3, 8]

    # Min-heap
    min_heap = BinaryHeap.from_list(values.copy(), "min")
    print(f"Values: {values}")
    print(f"Min-heap top: {min_heap.peek()} (smallest element)")

    min_sorted = []
    while not min_heap.is_empty():
        min_sorted.append(min_heap.extract_top())
    print(f"Min-heap extraction order: {min_sorted}")

    # Max-heap
    max_heap = BinaryHeap.from_list(values.copy(), "max")
    print(f"Max-heap top: {max_heap.peek()} (largest element)")

    max_sorted = []
    while not max_heap.is_empty():
        max_sorted.append(max_heap.extract_top())
    print(f"Max-heap extraction order: {max_sorted}")
    print(f"Reverse of min-heap order: {max_sorted == min_sorted[::-1]}")
    print()


def demonstrate_priority_queue():
    """Demonstrate priority queue usage."""
    print("\n=== Priority Queue Usage ===\n")

    # Task scheduling simulation
    print("Task Scheduling with Priority Queue:")
    pq = PriorityQueue[tuple]("min")  # Min-heap for priority (lower number = higher priority)

    tasks = [
        (3, "Low priority task"),
        (1, "High priority task"),
        (2, "Medium priority task"),
        (1, "Another high priority task"),
        (4, "Very low priority task")
    ]

    print("Adding tasks to priority queue:")
    for priority, description in tasks:
        pq.insert((priority, description))
        print(f"  Added: {description} (priority {priority})")

    print("
Processing tasks in priority order:")
    while not pq.is_empty():
        priority, description = pq.remove_top()
        print(f"  Processing: {description} (priority {priority})")

    print()
