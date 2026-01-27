#!/usr/bin/env python3
"""
Examples demonstrating Chapter 8 Doubly Linked List concatenation.
Run this script to see efficient O(1) list merging operations.
"""
import sys
import os

# Add root directory to path so imports work
sys.path.insert(0, os.path.join(os.getcwd(), "..", ".."))

from chapter_08_doubly_linked_lists.code.concatenation_impl import *


def basic_concatenation_demo():
    """Demonstrate basic concatenation operations."""
    print("=== Basic Concatenation Operations ===\n")

    # Create two sample lists
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    print("Creating sample lists:")
    for item in ["apple", "banana"]:
        list1.append(item)
    for item in ["cherry", "date"]:
        list2.append(item)

    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print()

    # Efficient concatenation
    print("Efficient concatenation (O(1)):")
    list1_copy = list1.clone()
    list2_copy = list2.clone()

    result = list1_copy.concatenate_efficient(list2_copy)
    print(f"Result: {result}")
    print(f"List 2 after concatenation: {list2_copy} (now empty)")
    print()

    # Copy-based concatenation
    print("Copy-based concatenation (O(n+m)):")
    list1_copy2 = list1.clone()
    list2_copy2 = list2.clone()

    result2 = list1_copy2.concatenate_copy(list2_copy2)
    print(f"Result: {result2}")
    print(f"Original lists preserved:")
    print(f"List 1: {list1_copy2}")
    print(f"List 2: {list2_copy2}")
    print()


def multiple_concatenation_demo():
    """Demonstrate concatenating multiple lists."""
    print("=== Multiple List Concatenation ===\n")

    # Create several lists
    lists = []
    data = [
        ["The", "quick"],
        ["brown", "fox"],
        ["jumps", "over"],
        ["the", "lazy", "dog"],
    ]

    print("Creating multiple lists:")
    for i, words in enumerate(data):
        lst = DoublyLinkedList()
        for word in words:
            lst.append(word)
        lists.append(lst)
        print(f"List {i + 1}: {lst}")

    print()

    # Concatenate all at once
    print("Concatenating all lists efficiently:")
    base_list = DoublyLinkedList()
    base_list.concatenate_multiple(*lists)

    print(f"Combined result: {base_list}")
    print(f"Total elements: {len(base_list)}")
    print()

    # Verify source lists are empty
    print("Source lists after concatenation:")
    for i, lst in enumerate(lists):
        print(f"List {i + 1}: {lst} (empty)")
    print()


def split_and_insert_demo():
    """Demonstrate splitting and inserting lists."""
    print("=== List Splitting and Insertion ===\n")

    # Create a list
    original = DoublyLinkedList()
    words = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for word in words:
        original.append(word)

    print(f"Original rainbow: {original}")
    print()

    # Split the list
    print("Splitting at index 3:")
    second_half = original.split_at(3)
    print(f"First half:  {original}")
    print(f"Second half: {second_half}")
    print()

    # Insert a list in the middle
    print("Inserting warm colors between first and second half:")
    warm_colors = DoublyLinkedList()
    warm_colors.append("warm_red")
    warm_colors.append("warm_orange")

    original.insert_list_at(1, warm_colors)
    print(f"After insertion: {original}")
    print(f"Warm colors list: {warm_colors} (now empty)")
    print()

    # Concatenate back together
    print("Final concatenation:")
    original.concatenate_efficient(second_half)
    print(f"Complete rainbow: {original}")
    print()


def edge_cases_demo():
    """Demonstrate edge cases in concatenation."""
    print("=== Edge Cases in Concatenation ===\n")

    # Empty list concatenations
    empty1 = DoublyLinkedList()
    empty2 = DoublyLinkedList()
    filled = DoublyLinkedList()
    filled.append("item")

    print("Empty list cases:")
    print(f"Empty + Empty: {empty1.concatenate_efficient(empty2.clone())}")

    result = DoublyLinkedList()
    result.concatenate_efficient(filled.clone())
    print(f"Empty + Filled: {result}")

    result2 = filled.clone()
    result2.concatenate_efficient(DoublyLinkedList())
    print(f"Filled + Empty: {result2}")
    print()

    # Single element lists
    print("Single element cases:")
    single1 = DoublyLinkedList()
    single1.append("A")
    single2 = DoublyLinkedList()
    single2.append("B")

    single1.concatenate_efficient(single2)
    print(f"Single + Single: {single1}")
    print()

    # Large list concatenation
    print("Large list concatenation:")
    large1 = DoublyLinkedList()
    large2 = DoublyLinkedList()

    for i in range(1000):
        large1.append(f"item_{i}")
        large2.append(f"other_{i}")

    print(f"List 1 size: {len(large1)}")
    print(f"List 2 size: {len(large2)}")

    # Time the concatenation
    import time

    start = time.time()
    large1.concatenate_efficient(large2)
    duration = time.time() - start

    print(f"After concatenation: {len(large1)} total items")
    print(".4f")
    print("Note: O(1) concatenation is fast even for large lists!")
    print()


def pointer_integrity_demo():
    """Demonstrate that pointer integrity is maintained."""
    print("=== Pointer Integrity Demonstration ===\n")

    # Create lists
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    for i in [1, 2, 3]:
        list1.append(i)
    for i in [4, 5, 6]:
        list2.append(i)

    print("Before concatenation:")
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print()

    # Show internal structure
    print("Internal pointer structure:")
    print(f"List 1 head: {list1.head.data if list1.head else None}")
    print(f"List 1 tail: {list1.tail.data if list1.tail else None}")
    print(f"List 2 head: {list2.head.data if list2.head else None}")
    print(f"List 2 tail: {list2.tail.data if list2.tail else None}")
    print()

    # Concatenate
    list1.concatenate_efficient(list2)

    print("After concatenation:")
    print(f"Combined: {list1}")
    print(f"List 2: {list2} (empty)")
    print()

    # Verify pointer integrity
    print("Pointer integrity check:")

    # Forward traversal
    print("Forward traversal:")
    current = list1.head
    while current:
        print(f"  {current.data} -> ", end="")
        current = current.next
    print("None")

    # Backward traversal
    print("Backward traversal:")
    current = list1.tail
    while current:
        print(f"  {current.data} <- ", end="")
        current = current.prev
    print("None")
    print()

    # Verify bidirectional links
    print("Bidirectional link verification:")
    forward = []
    current = list1.head
    while current:
        forward.append(current.data)
        current = current.next

    backward = []
    current = list1.tail
    while current:
        backward.append(current.data)
        current = current.prev

    backward.reverse()  # Reverse to compare with forward

    print(f"Forward:  {forward}")
    print(f"Backward: {backward}")
    print(f"Consistent: {forward == backward}")
    print()


def performance_comparison_demo():
    """Compare performance of different concatenation methods."""
    print("=== Performance Comparison ===\n")

    demonstrate_concatenation_performance()
    print()


def practical_applications():
    """Show real-world applications of list concatenation."""
    print("=== Practical Applications ===\n")

    # Text processing
    print("1. Text Document Assembly:")
    paragraphs = [DoublyLinkedList(), DoublyLinkedList(), DoublyLinkedList()]

    # Simulate paragraphs
    para_texts = [
        ["The", "quick", "brown", "fox"],
        ["jumps", "over"],
        ["the", "lazy", "dog"],
    ]

    for para, words in zip(paragraphs, para_texts):
        for word in words:
            para.append(word)

    # Assemble document
    document = DoublyLinkedList()
    document.concatenate_multiple(*paragraphs)

    print(f"Assembled document: {document}")
    print()

    # Configuration merging
    print("2. Configuration Settings Merge:")
    base_config = DoublyLinkedList()
    user_config = DoublyLinkedList()
    system_config = DoublyLinkedList()

    # Base settings
    for setting in ["theme=default", "language=en"]:
        base_config.append(setting)

    # User overrides
    for setting in ["theme=dark", "font=large"]:
        user_config.append(setting)

    # System settings
    for setting in ["version=1.0"]:
        system_config.append(setting)

    # Merge configurations (user overrides base, system adds)
    final_config = base_config.clone()
    final_config.concatenate_efficient(user_config.clone())
    final_config.concatenate_efficient(system_config.clone())

    print(f"Base config: {base_config}")
    print(f"User config: {user_config}")
    print(f"System config: {system_config}")
    print(f"Final merged config: {final_config}")
    print()

    # Undo/Redo system
    print("3. Undo/Redo Operation History:")
    undo_stack = DoublyLinkedList()
    redo_stack = DoublyLinkedList()

    # Simulate operations
    operations = ["type 'h'", "type 'e'", "type 'l'", "delete", "type 'o'"]
    for op in operations:
        undo_stack.append(op)

    print(f"Operation history: {undo_stack}")

    # Simulate undo (last 2 operations)
    print("Undoing last 2 operations:")
    for _ in range(2):
        if undo_stack.tail:
            operation = undo_stack.remove_last()
            redo_stack.append(operation)
            print(f"  Undid: {operation}")

    print(f"Remaining operations: {undo_stack}")
    print(f"Redo stack: {redo_stack}")
    print()


if __name__ == "__main__":
    print("=== Chapter 8: Concatenating Doubly Linked Lists Examples ===\n")

    # Run all demonstrations
    basic_concatenation_demo()
    multiple_concatenation_demo()
    split_and_insert_demo()
    edge_cases_demo()
    pointer_integrity_demo()
    performance_comparison_demo()
    practical_applications()

    print("=== Key Takeaways ===")
    print("• Efficient concatenation: O(1) pointer updates")
    print("• Copy concatenation: O(n+m) but preserves originals")
    print("• Doubly linked lists enable fast end operations")
    print("• Pointer manipulation is powerful but requires care")
    print("• Multiple concatenation chains operations efficiently")
    print("• Real applications: text processing, configs, undo systems")
    print(
        "\nDoubly linked lists provide elegant solutions for dynamic data management!"
    )
