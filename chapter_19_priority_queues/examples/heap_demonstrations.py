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

    # Event simulation
    print("Event Simulation (earliest first):")
    events = PriorityQueue[tuple]("min")  # Min-heap for time

    event_list = [
        (14, "Meeting ends"),
        (9, "Coffee break"),
        (12, "Lunch time"),
        (8, "Standup meeting"),
        (16, "End of day")
    ]

    for time_val, event in event_list:
        events.insert((time_val, event))

    print("Processing events in chronological order:")
    while not events.is_empty():
        time_val, event = events.remove_top()
        print(f"  {time_val}:00 - {event}")

    print()


def demonstrate_heapsort():
    """Demonstrate heapsort algorithm."""
    print("\n=== Heapsort Algorithm ===\n")

    # Different input types
    test_cases = [
        ("Random array", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
        ("Reverse sorted", list(range(10, 0, -1))),
        ("Already sorted", list(range(1, 11))),
        ("Few unique values", [1, 1, 2, 2, 3, 3, 1, 2, 3]),
    ]

    for name, arr in test_cases:
        print(f"{name}: {arr}")

        heap = BinaryHeap[int]("min")
        sorted_arr = heap.heap_sort(arr.copy())

        print(f"  Sorted: {sorted_arr}")
        print(f"  Correct: {sorted_arr == sorted(arr)}")
        print()

    # Performance comparison
    print("Performance comparison with different array sizes:")
    sizes = [100, 1000, 5000]

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        heap = BinaryHeap[int]("min")
        start_time = time.time()
        sorted_arr = heap.heap_sort(arr.copy())
        sort_time = time.time() - start_time

        correct = sorted_arr == sorted(arr)
        print("6.2f")

    print()


def demonstrate_heap_building():
    """Demonstrate different heap building approaches."""
    print("\n=== Heap Building Methods ===\n")

    arr = [7, 4, 9, 2, 1, 8, 5, 3, 6]
    print(f"Original array: {arr}")

    # Method 1: Insert one by one
    print("\nMethod 1: Insert elements one by one")
    heap1 = BinaryHeap[int]("min")
    for val in arr:
        heap1.insert(val)
        print(f"  After inserting {val}: {heap1.get_heap_array()}")

    # Method 2: Build heap from array
    print("\nMethod 2: Build heap from entire array")
    heap2 = BinaryHeap.from_list(arr.copy(), "min")
    print(f"  Final heap: {heap2.get_heap_array()}")

    # Verify both produce valid heaps
    print(f"\nBoth methods produce valid heaps:")
    print(f"  Method 1 valid: {heap1.is_valid_heap()}")
    print(f"  Method 2 valid: {heap2.is_valid_heap()}")

    # Compare performance for large arrays
    large_arr = list(range(1000, 0, -1))

    # Method 1: Insertions
    start = time.time()
    heap_insert = BinaryHeap[int]("min")
    for val in large_arr:
        heap_insert.insert(val)
    insert_time = time.time() - start

    # Method 2: Build heap
    start = time.time()
    heap_build = BinaryHeap.from_list(large_arr, "min")
    build_time = time.time() - start

    print("
Performance comparison (1000 elements):")
    print(".4f")
    print(".4f")
    print(".1f")
    print()


def demonstrate_heap_analysis():
    """Demonstrate heap analysis tools."""
    print("\n=== Heap Analysis Tools ===\n")

    # Create heaps of different sizes
    sizes = [7, 15, 31, 63]  # Perfect binary tree sizes

    for size in sizes:
        heap = BinaryHeap[int]("min")
        for i in range(size):
            heap.insert(i)

        analysis = HeapAnalysis.analyze_heap_height(heap)

        print(f"Heap with {size} elements:")
        print(f"  Height: {analysis['height']}")
        print(f"  Perfect tree height: {analysis['perfect_height']}")
        print(f"  Is perfect: {analysis['is_perfect']}")
        print(".1f")
        print()

    # Benchmark different operations
    print("Benchmarking heap operations:")
    benchmark_results = HeapAnalysis.benchmark_heap_operations("min", [100, 500])

    for size, results in benchmark_results.items():
        print(f"\nSize {size}:")
        print(".4f")
        print(".4f")
        print(".4f")
        print(f"  Valid heap: {results['is_valid']}")

    print()


def demonstrate_real_world_priority_queue():
    """Demonstrate real-world priority queue applications."""
    print("\n=== Real-World Priority Queue Applications ===\n")

    # Hospital emergency room simulation
    print("1. Hospital Emergency Room Triage:")
    emergency_queue = PriorityQueue[tuple]("min")  # Lower number = higher priority

    patients = [
        (1, "Critical - Heart attack"),
        (3, "Moderate - Broken arm"),
        (2, "Serious - Severe headache"),
        (1, "Critical - Allergic reaction"),
        (4, "Minor - Sprained ankle"),
        (2, "Serious - High fever")
    ]

    print("Patients arriving at emergency room:")
    for priority, condition in patients:
        emergency_queue.insert((priority, condition))
        priority_desc = {1: "Critical", 2: "Serious", 3: "Moderate", 4: "Minor"}[priority]
        print(f"  Priority {priority} ({priority_desc}): {condition}")

    print("
Treating patients in priority order:")
    while not emergency_queue.is_empty():
        priority, condition = emergency_queue.remove_top()
        priority_desc = {1: "Critical", 2: "Serious", 3: "Moderate", 4: "Minor"}[priority]
        print(f"  Treating: {condition} (Priority {priority} - {priority_desc})")

    print()

    # CPU scheduling simulation
    print("2. CPU Process Scheduling:")
    process_queue = PriorityQueue[tuple]("max")  # Higher priority number = more important

    processes = [
        (8, "System process"),
        (3, "User application"),
        (6, "I/O operation"),
        (1, "Background task"),
        (9, "Real-time process"),
        (4, "Network service")
    ]

    print("Processes waiting for CPU time:")
    for priority, name in processes:
        process_queue.insert((priority, name))
        print(f"  Priority {priority}: {name}")

    print("
CPU scheduling processes:")
    while not process_queue.is_empty():
        priority, name = process_queue.remove_top()
        print(f"  Running: {name} (Priority {priority})")

    print()


def demonstrate_heap_visualization():
    """Show heap structure visualization."""
    print("\n=== Heap Structure Visualization ===\n")

    heap = BinaryHeap[int]("min")
    values = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    print("Building heap step by step:")
    print("Values to insert:", values)
    print()

    for i, val in enumerate(values):
        heap.insert(val)
        if (i + 1) % 5 == 0 or i == len(values) - 1:  # Show every 5 insertions or final
            print(f"After {i+1} insertions: {heap.get_heap_array()}")
            print(f"  Height: {HeapAnalysis.analyze_heap_height(heap)['height']}")
            print(f"  Valid: {heap.is_valid_heap()}")
            print()

    print("Final heap structure:")
    heap_array = heap.get_heap_array()
    print(f"Array representation: {heap_array}")

    # Show parent-child relationships
    print("\nParent-child relationships:")
    for i in range(len(heap_array)):
        left = 2 * i + 1
        right = 2 * i + 2
        children = []
        if left < len(heap_array):
            children.append(f"L:{heap_array[left]}")
        if right < len(heap_array):
            children.append(f"R:{heap_array[right]}")

        if children:
            print(f"  {heap_array[i]} -> {', '.join(children)}")
    print()


if __name__ == "__main__":
    demonstrate_heap_operations()
    demonstrate_max_heap_vs_min_heap()
    demonstrate_priority_queue()
    demonstrate_heapsort()
    demonstrate_heap_building()
    demonstrate_heap_analysis()
    demonstrate_real_world_priority_queue()
    demonstrate_heap_visualization()

    print("\n=== Priority Queues Summary ===")
    print("• Binary heaps provide O(log n) priority queue operations")
    print("• Min-heaps vs max-heaps for different priority semantics")
    print("• Heapsort: in-place sorting with heap properties")
    print("• Applications: scheduling, event simulation, data analysis")
    print("• Build heap in O(n) vs O(n log n) insertion approach")
    print("\nChapter 19: Priority queues and heaps mastered! 🎯")