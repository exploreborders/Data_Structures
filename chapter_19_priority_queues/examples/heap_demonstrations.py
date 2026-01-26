"""
Chapter 19: Priority Queues - Heap Demonstrations

Interactive demonstrations of heap operations, priority queues, and real-world applications.
"""

import random
import time
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from heap_implementations import BinaryHeap, PriorityQueue, HeapAnalysis


def demonstrate_basic_operations():
    """Demonstrate basic heap operations."""
    print("=== Basic Heap Operations ===\n")

    # Create a max-heap
    heap = BinaryHeap[int]("max")

    print("Building a max-heap with random values:")
    values = [15, 10, 20, 8, 5, 17, 12, 25, 30]
    print(f"Inserting values: {values}")

    for val in values:
        heap.insert(val)
        print(f"  After inserting {val}: {heap.get_heap_array()}")

    print(f"\nFinal heap: {heap.get_heap_array()}")
    print(f"Heap property valid: {heap.is_valid_heap()}")

    print("\nExtract elements:")
    extracted = []
    while not heap.is_empty():
        max_val = heap.remove_top()
        extracted.append(max_val)
        print(f"  Extracted: {max_val}, heap: {heap.get_heap_array()}")

    print(f"Extraction order: {extracted}")
    print(f"Sorted correctly: {extracted == sorted(values, reverse=True)}")


def demonstrate_priority_queue():
    """Demonstrate priority queue usage."""
    print("\n=== Priority Queue Usage ===\n")

    # Task scheduling with max-heap (highest priority first)
    pq = PriorityQueue[tuple]("max")

    tasks = [
        (5, "High priority - System backup"),
        (3, "Medium priority - User requests"),
        (1, "Low priority - Background tasks"),
        (4, "Medium priority - Code review"),
        (2, "Low priority - Documentation"),
    ]

    print("Adding tasks to priority queue:")
    for priority, description in tasks:
        pq.insert((priority, description))
        print(f"  Added: {description} (priority {priority})")

    print("\nProcessing tasks by priority:")
    while not pq.is_empty():
        priority, description = pq.remove_top()
        print(f"  Processing: {description} (priority {priority})")

    print("\nAll tasks processed!")


def demonstrate_performance_analysis():
    """Demonstrate heap performance analysis."""
    print("\n=== Performance Analysis ===\n")

    # Test different heap sizes
    sizes = [1000, 5000, 10000]

    print("Building and testing heaps of different sizes:")
    for size in sizes:
        data = [random.randint(1, 1000) for _ in range(size)]

        # Test sequential insertion
        heap1 = BinaryHeap[int]("max")
        start = time.time()
        for val in data:
            heap1.insert(val)
        insert_time = time.time() - start

        # Test heapify
        heap2 = BinaryHeap[int]("max")
        start = time.time()
        heap2.build_heap(data)
        heapify_time = time.time() - start

        print(
            f"Size {size}: Sequential insert: {insert_time:.4f}s, Heapify: {heapify_time:.4f}s"
        )
        print(f"  Speedup: {insert_time / heapify_time:.1f}x")

    print("\nPerformance insights:")
    print("- Heapify is significantly faster for large datasets")
    print("- Both methods produce valid heaps")
    print("- Choose method based on data access patterns")


def demonstrate_real_world_applications():
    """Demonstrate real-world heap applications."""
    print("\n=== Real-World Applications ===\n")

    # CPU job scheduling
    print("1. CPU Job Scheduling:")
    job_queue = PriorityQueue[tuple]("max")  # Higher priority = more important

    jobs = [
        (10, "Critical system update"),
        (5, "Real-time processing"),
        (8, "User interface response"),
        (3, "Background maintenance"),
        (6, "Data analysis"),
    ]

    print("Adding jobs to scheduler:")
    for priority, job in jobs:
        job_queue.insert((priority, job))
        print(f"  Scheduled: {job} (priority {priority})")

    print("\nExecuting jobs by priority:")
    while not job_queue.is_empty():
        priority, job = job_queue.remove_top()
        print(f"  Running: {job} (priority {priority})")

    # Emergency room triage
    print("\n2. Emergency Room Triage:")
    er_queue = PriorityQueue[tuple]("min")  # Lower number = higher urgency

    patients = [
        (1, "Critical - Heart attack"),
        (2, "Serious - Major trauma"),
        (3, "Moderate - Broken arm"),
        (4, "Low - Minor injury"),
    ]

    print("Adding patients to triage:")
    for priority, condition in patients:
        er_queue.insert((priority, condition))
        print(f"  Triage: {condition} (priority {priority})")

    print("\nProcessing patients by urgency:")
    while not er_queue.is_empty():
        priority, condition = er_queue.remove_top()
        print(f"  Treating: {condition} (priority {priority})")


if __name__ == "__main__":
    print("🏥 Priority Queue Demonstrations")
    print("=====================================")

    demonstrate_basic_operations()
    demonstrate_priority_queue()
    demonstrate_performance_analysis()
    demonstrate_real_world_applications()

    print("\n🎯 Key Takeaways:")
    print("- Binary heaps provide efficient priority-based operations")
    print("- Perfect for scheduling and real-time systems")
    print("- Choose data structure based on access patterns")
    print("- Heap operations maintain optimal O(log n) complexity")
