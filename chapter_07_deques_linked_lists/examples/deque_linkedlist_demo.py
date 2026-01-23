#!/usr/bin/env python3
"""
Examples demonstrating Chapter 7 Deque and Linked List concepts.
Run this script to see ADT operations, wrapper pattern, and practical applications.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from chapter_7_deques_linked_lists.code.deque_linkedlist_impl import *


def basic_linked_list_demo():
    """Demonstrate basic LinkedList operations."""
    print("=== Basic Linked List Operations ===\n")

    linked_list = LinkedList()

    print("Building a linked list:")
    for item in ["first", "second", "third"]:
        linked_list.append(item)
        print(f"  Append '{item}': {linked_list}")

    print("\nPrepending items:")
    linked_list.prepend("zero")
    print(f"  Prepend 'zero': {linked_list}")

    print("\nInserting in middle:")
    linked_list.insert_after("second", "2.5")
    print(f"  Insert '2.5' after 'second': {linked_list}")

    print("\nRemoving items:")
    linked_list.remove("second")
    print(f"  Remove 'second': {linked_list}")

    print("\nIterating through list:")
    for i, item in enumerate(linked_list):
        print(f"  [{i}]: {item}")
    print()


def doubly_linked_list_demo():
    """Demonstrate DoublyLinkedList operations."""
    print("=== Doubly Linked List Operations ===\n")

    doubly_list = DoublyLinkedList()

    print("Appending items (O(1) each):")
    for item in [1, 2, 3]:
        doubly_list.append(item)
        print(f"  Append {item}: {doubly_list}")

    print("\nPrepending items (O(1) each):")
    doubly_list.prepend(0)
    print(f"  Prepend 0: {doubly_list}")

    print("\nRemoving from ends (O(1) each):")
    removed_first = doubly_list.remove_first()
    print(f"  Remove first ({removed_first}): {doubly_list}")

    removed_last = doubly_list.remove_last()
    print(f"  Remove last ({removed_last}): {doubly_list}")
    print()


def deque_operations_demo():
    """Demonstrate Deque ADT operations."""
    print("=== Deque ADT Operations ===\n")

    deque = Deque()

    print("Adding to both ends:")
    deque.add_first("front1")
    print(f"  Add first 'front1': {deque}")

    deque.add_last("back1")
    print(f"  Add last 'back1': {deque}")

    deque.add_first("front2")
    print(f"  Add first 'front2': {deque}")

    deque.add_last("back2")
    print(f"  Add last 'back2': {deque}")

    print("\nAccessing ends (O(1)):")
    print(f"  First: {deque.first()}")
    print(f"  Last: {deque.last()}")

    print("\nRemoving from ends (O(1)):")
    print(f"  Remove first: {deque.remove_first()}")
    print(f"  Deque now: {deque}")

    print(f"  Remove last: {deque.remove_last()}")
    print(f"  Deque now: {deque}")

    print("\nFinal deque:", deque)
    print()


def queue_implementations_comparison():
    """Compare different Queue implementations."""
    print("=== Queue Implementation Comparison ===\n")

    from chapter_6_stacks_and_queues.code.stack_queue_adts import Queue as ListQueue

    # Test data
    items = list(range(10))

    print("Testing with items:", items)
    print()

    # List-based queue (from Chapter 6)
    list_queue = ListQueue()
    for item in items:
        list_queue.enqueue(item)

    print("List-based Queue:")
    print(f"  After enqueuing: {list_queue}")

    dequeued = []
    for _ in range(3):
        dequeued.append(list_queue.dequeue())
    print(f"  Dequeued first 3: {dequeued}")
    print(f"  Queue now: {list_queue}")
    print("  Note: dequeue is O(n) - shifts remaining elements")
    # LinkedList-based queue (Chapter 7)
    linked_queue = LinkedQueue()
    for item in items:
        linked_queue.enqueue(item)

    print("\nLinkedList-based Queue (Wrapper Pattern):")
    print(f"  After enqueuing: {linked_queue}")

    dequeued = []
    for _ in range(3):
        dequeued.append(linked_queue.dequeue())
    print(f"  Dequeued first 3: {dequeued}")
    print(f"  Queue now: {linked_queue}")
    print("  Note: dequeue is O(1) - just update head pointer")
    print()


def wrapper_pattern_explanation():
    """Explain the wrapper pattern with examples."""
    print("=== The Wrapper Pattern ===\n")

    print("Wrapper Pattern: Adapt one interface to another")
    print("LinkedQueue wraps LinkedList to provide Queue interface")
    print()

    # Show the underlying structure
    queue = LinkedQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("Queue operations:")
    print(f"  Enqueue items: {queue}")

    print("Underlying LinkedList structure:")
    print(f"  Internal list: {queue._list}")
    print(f"  Head points to: {queue._list.head.data if queue._list.head else None}")

    # Show wrapping in action
    print("\nWrapper in action:")
    print(f"  Queue front(): {queue.front()} (calls _list.head.data)")
    print(f"  Queue dequeue(): {queue.dequeue()} (removes head, updates _list)")
    print(f"  Queue now: {queue}")
    print()


def practical_applications():
    """Demonstrate practical applications."""
    print("=== Practical Applications ===\n")

    # Palindrome checking
    print("1. Palindrome Checking with Deque:")
    test_words = ["radar", "hello", "racecar", "Able was I ere I saw Elba"]

    for word in test_words:
        is_pal = check_palindrome(word)
        status = "✓ Palindrome" if is_pal else "✗ Not palindrome"
        print(f"   '{word}': {status}")
    print()

    # Sliding window maximum
    print("2. Sliding Window Maximum (O(n) with Deque):")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    maxima = sliding_window_maximum(nums, k)
    print(f"   Array: {nums}")
    print(f"   Window size k={k}")
    print("   Maximum in each window:")

    for i, max_val in enumerate(maxima):
        window = nums[i : i + k]
        print(f"     Window {i + 1} {window}: max = {max_val}")
    print()

    # Browser history simulation
    print("3. Browser History with Deque:")
    history = Deque()

    # Simulate browsing
    pages = ["home", "about", "products", "contact", "blog"]
    for page in pages:
        history.add_last(page)
        print(f"   Visited: {page}")

    print("\nBack button (remove from back):")
    while not history.is_empty():
        current = history.remove_last()
        print(f"   Back to: {current}")
        if history.is_empty():
            print("   No more history!")
            break
    print()


def performance_demonstration():
    """Demonstrate performance differences."""
    print("=== Performance Demonstration ===\n")

    print("Comparing LinkedList vs Python List for end operations:")
    print("(Testing with 10,000 operations)")
    print()

    import time

    # Test data
    n = 10000

    # Python list (dynamic array)
    print("Python List:")
    start = time.time()
    py_list = []
    for i in range(n):
        py_list.append(i)  # O(1) amortized
    append_time = time.time() - start

    start = time.time()
    for _ in range(min(1000, n)):  # Don't dequeue all - too slow
        if py_list:
            py_list.pop(0)  # O(n) - very slow!
    dequeue_time = time.time() - start

    print(".4f")
    print(".4f")

    # LinkedList
    print("\nLinkedList:")
    start = time.time()
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)  # O(1)
    append_time = time.time() - start

    start = time.time()
    for _ in range(min(1000, n)):  # Test reasonable number
        if linked_list.head:
            # Simulate dequeue (remove head)
            linked_list.head = linked_list.head.next
            linked_list._size -= 1
    dequeue_time = time.time() - start

    print(".4f")
    print(".4f")

    print("\nKey Insight:")
    print("- Python list: Fast append, slow remove from front")
    print("- LinkedList: Fast append, fast remove from front")
    print("- Choose based on your access patterns!")
    print()


def data_structure_choice_guide():
    """Guide for choosing data structures."""
    print("=== Data Structure Selection Guide ===\n")

    structures = {
        "Python List": {
            "best_for": "Random access, end operations, simple sequences",
            "operations": "O(1) access, O(1) append, O(n) insert middle",
            "use_when": "You need indexing, sorting, simple iteration",
        },
        "LinkedList": {
            "best_for": "Frequent end insertions/deletions, no random access needed",
            "operations": "O(1) end ops, O(n) access, O(n) search",
            "use_when": "Building stacks, queues, or when memory is fragmented",
        },
        "DoublyLinkedList": {
            "best_for": "Both ends operations, bidirectional traversal",
            "operations": "O(1) all end ops, O(n) middle ops",
            "use_when": "Implementing deques, need both directions",
        },
        "Deque": {
            "best_for": "Double-ended operations, flexible access patterns",
            "operations": "O(1) end ops, no random access",
            "use_when": "Sliding windows, BFS, flexible LIFO/FIFO needs",
        },
    }

    for name, info in structures.items():
        print(f"{name}:")
        print(f"  Best for: {info['best_for']}")
        print(f"  Operations: {info['operations']}")
        print(f"  Use when: {info['use_when']}")
        print()


if __name__ == "__main__":
    print("=== Chapter 7: Deques and Linked Lists Examples ===\n")

    # Run all demonstrations
    basic_linked_list_demo()
    doubly_linked_list_demo()
    deque_operations_demo()
    queue_implementations_comparison()
    wrapper_pattern_explanation()
    practical_applications()
    performance_demonstration()
    data_structure_choice_guide()

    print("=== Key Takeaways ===")
    print("• Linked Lists: No contiguous memory, flexible insertions")
    print("• Doubly Linked: Both ends access, bidirectional traversal")
    print("• Deque: Double-ended operations, very flexible ADT")
    print("• Wrapper Pattern: Adapt interfaces, hide implementations")
    print("• Performance: Choose structures based on access patterns")
    print("• Length Caching: O(1) size queries are crucial for usability")
    print("• ADT Contracts: Clear specifications enable reliable code")
    print("\nMaster these foundations and you'll handle any data structure challenge!")
