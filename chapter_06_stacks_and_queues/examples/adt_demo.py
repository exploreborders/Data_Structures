#!/usr/bin/env python3
"""
Examples demonstrating Chapter 6 Stack and Queue ADTs.
Run this script to see ADT operations and practical applications.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from chapter_06_stacks_and_queues.code.stack_queue_adts import *


def basic_adt_operations():
    """Demonstrate basic Stack and Queue operations."""
    print("=== Basic ADT Operations ===\n")

    # Stack demonstration
    print("Stack (LIFO - Last In, First Out):")
    stack = Stack()
    items = ["first", "second", "third"]

    print("Pushing items:")
    for item in items:
        stack.push(item)
        print(f"  Push '{item}': {stack}")

    print("Popping items (LIFO order):")
    while not stack.is_empty():
        item = stack.pop()
        print(f"  Pop '{item}': {stack}")
    print()

    # Queue demonstration
    print("Queue (FIFO - First In, First Out):")
    queue = Queue()
    items = ["first", "second", "third"]

    print("Enqueuing items:")
    for item in items:
        queue.enqueue(item)
        print(f"  Enqueue '{item}': {queue}")

    print("Dequeuing items (FIFO order):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Dequeue '{item}': {queue}")
    print()


def error_handling_demo():
    """Demonstrate proper error handling in ADTs."""
    print("=== Error Handling in ADTs ===\n")

    stack = Stack()
    queue = Queue()

    print("Testing empty stack operations:")
    try:
        item = stack.pop()
    except IndexError as e:
        print(f"  ✓ Stack pop error: {e}")

    try:
        item = stack.peek()
    except IndexError as e:
        print(f"  ✓ Stack peek error: {e}")

    print("Testing empty queue operations:")
    try:
        item = queue.dequeue()
    except IndexError as e:
        print(f"  ✓ Queue dequeue error: {e}")

    try:
        item = queue.front()
    except IndexError as e:
        print(f"  ✓ Queue front error: {e}")

    print("Adding items and retrying:")
    stack.push("item")
    queue.enqueue("item")

    print(f"  Stack peek after push: {stack.peek()}")
    print(f"  Queue front after enqueue: {queue.front()}")
    print()


def practical_applications():
    """Demonstrate real-world applications of Stacks and Queues."""
    print("=== Practical Applications ===\n")

    # String reversal with stack
    print("1. String Reversal with Stack:")
    texts = ["hello", "world", "Python"]
    for text in texts:
        reversed_text = reverse_string(text)
        print(f"   '{text}' → '{reversed_text}'")
    print()

    # Balanced parentheses checking
    print("2. Balanced Parentheses Checking:")
    expressions = [
        "(a + b)",  # Balanced
        "(a + b",  # Unbalanced - missing closing
        "((a + b))",  # Balanced - nested
        "(a + b))",  # Unbalanced - extra closing
        "a + b",  # Balanced - no parentheses
        "[a + {b + c}]",  # Balanced - mixed brackets
    ]

    for expr in expressions:
        balanced = is_balanced_parentheses(expr)
        status = "✓ Balanced" if balanced else "✗ Unbalanced"
        print(f"   '{expr}' {status}")
    print()

    # Print queue simulation
    print("3. Print Queue Simulation (FIFO):")
    print_jobs = ["resume.pdf", "photo.jpg", "report.docx", "diagram.png"]
    processed = simulate_print_queue(print_jobs)
    print(f"   Jobs processed in order: {processed}")
    print()


def efficiency_comparison():
    """Compare efficiency of different implementations."""
    print("=== Efficiency Comparison ===\n")

    print("Comparing Queue implementations:")
    print("Note: This demonstrates conceptual differences.")
    print("In practice, EfficientQueue avoids O(n) dequeue operations.\n")

    # Demonstrate with small dataset
    items = list(range(5))

    regular_queue = Queue()
    efficient_queue = EfficientQueue()

    print("Adding items [0, 1, 2, 3, 4]:")
    for item in items:
        regular_queue.enqueue(item)
        efficient_queue.enqueue(item)

    print(f"Regular queue:   {regular_queue}")
    print(f"Efficient queue: {efficient_queue}")

    print("\nRemoving items:")
    while not regular_queue.is_empty():
        reg_item = regular_queue.dequeue()
        eff_item = efficient_queue.dequeue()
        print(f"  Dequeued: {reg_item} (regular), {eff_item} (efficient)")
        print(f"    Regular: {regular_queue}")
        print(f"    Efficient: {efficient_queue}")
    print()


def adt_patterns_and_best_practices():
    """Show common ADT usage patterns and best practices."""
    print("=== ADT Patterns and Best Practices ===\n")

    print("Common Patterns:")
    print("1. Stack for Backtracking:")
    stack = Stack()
    # Simulate function calls
    functions = ["main()", "parse_input()", "validate_data()"]
    for func in functions:
        stack.push(func)
        print(f"   Call: {func} (stack: {[x for x in stack._items]})")

    while not stack.is_empty():
        func = stack.pop()
        print(f"   Return: {func}")
    print()

    print("2. Queue for Task Processing:")
    queue = Queue()
    tasks = ["download_file", "process_data", "send_email", "cleanup"]

    for task in tasks:
        queue.enqueue(task)
        print(f"   Queue task: {task}")

    print("   Processing tasks:")
    while not queue.is_empty():
        task = queue.dequeue()
        print(f"   ✓ Completed: {task}")
    print()

    print("Best Practices:")
    print("• Always check is_empty() before pop/dequeue/front operations")
    print("• Use try-except blocks for robust error handling")
    print("• Consider performance implications of your implementation choice")
    print("• Document ADT contracts (preconditions, postconditions)")
    print("• Test edge cases thoroughly (empty collections, single items)")
    print("• Choose the right ADT for your use case (LIFO vs FIFO)")
    print()


def advanced_adt_usage():
    """Demonstrate more advanced ADT usage patterns."""
    print("=== Advanced ADT Usage ===\n")

    print("Stack-based Expression Evaluation:")

    # Simple postfix notation evaluation
    def evaluate_simple(expression):
        """Evaluate simple postfix expressions with + and *."""
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.push(int(token))
            elif token in ["+", "*"]:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.push(a + b)
                elif token == "*":
                    stack.push(a * b)

        return stack.pop() if not stack.is_empty() else None

    expressions = [
        "3 4 +",  # 3 + 4 = 7
        "5 6 *",  # 5 * 6 = 30
        "2 3 4 * +",  # 2 + (3 * 4) = 14
    ]

    for expr in expressions:
        result = evaluate_simple(expr)
        print(f"   '{expr}' = {result}")
    print()

    print("Queue-based Level-Order Tree Traversal:")

    # Simulate a binary tree using lists
    def level_order_traversal(root):
        """Simulate level-order traversal of a binary tree."""
        if not root:
            return []

        result = []
        queue = Queue()
        queue.enqueue(root)

        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node[0])  # Node value

            # Add children (in real tree, would check for None)
            if len(node) > 1 and node[1]:  # left child
                queue.enqueue(node[1])
            if len(node) > 2 and node[2]:  # right child
                queue.enqueue(node[2])

        return result

    # Tree represented as nested lists: [value, left, right]
    tree = ["A", ["B", ["D"], ["E"]], ["C", ["F"]]]
    traversal = level_order_traversal(tree)
    print(f"   Level-order traversal: {traversal}")
    print()


if __name__ == "__main__":
    print("=== Chapter 6: Stacks and Queues ADT Examples ===\n")

    # Run all demonstrations
    basic_adt_operations()
    error_handling_demo()
    practical_applications()
    efficiency_comparison()
    adt_patterns_and_best_practices()
    advanced_adt_usage()

    print("=== Key Takeaways ===")
    print("• ADTs define behavior, not implementation")
    print("• Stack = LIFO, Queue = FIFO")
    print("• Proper error handling is crucial")
    print("• Choose the right ADT for your problem")
    print("• Consider performance implications")
    print("• Test edge cases thoroughly")
    print(
        "\nStacks and Queues are fundamental building blocks used throughout computer science!"
    )
