"""
Chapter 6: Stacks and Queues - Abstract Data Type Implementations

This module implements the Stack and Queue Abstract Data Types (ADTs)
with proper error handling and comprehensive behavior.
"""


class Stack:
    """
    Stack Abstract Data Type (ADT) implementation.

    A Stack is a Last-In-First-Out (LIFO) data structure.
    Items are added and removed from the "top" of the stack.

    Operations:
    - push(item): Add item to the top
    - pop(): Remove and return the top item
    - peek(): Return the top item without removing it
    - is_empty(): Check if stack has no items
    - size(): Return number of items

    Time Complexity: All operations O(1)
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args:
            item: The item to add (can be any type)

        Postcondition: item is now at the top, size increased by 1
        """
        self._items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The item that was at the top

        Raises:
            IndexError: If the stack is empty

        Precondition: Stack is not empty
        Postcondition: Top item removed, size decreased by 1
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()

    def peek(self):
        """
        Return the top item without removing it.

        Returns:
            The item at the top

        Raises:
            IndexError: If the stack is empty

        Precondition: Stack is not empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        """
        Check if the stack has no items.

        Returns:
            True if stack is empty, False otherwise
        """
        return len(self._items) == 0

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            Integer count of items
        """
        return len(self._items)

    def __str__(self):
        """Return string representation of the stack."""
        return f"Stack({self._items})"

    def __len__(self):
        """Support len(stack) syntax."""
        return self.size()


class Queue:
    """
    Queue Abstract Data Type (ADT) implementation.

    A Queue is a First-In-First-Out (FIFO) data structure.
    Items are added to the "back" and removed from the "front".

    Operations:
    - enqueue(item): Add item to the back
    - dequeue(): Remove and return the front item
    - front(): Return the front item without removing it
    - is_empty(): Check if queue has no items
    - size(): Return number of items

    Note: This implementation uses a Python list, making dequeue O(n).
    In practice, you'd want a more efficient implementation.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self._items = []

    def enqueue(self, item):
        """
        Add an item to the back of the queue.

        Args:
            item: The item to add (can be any type)

        Postcondition: item is now at the back, size increased by 1
        """
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.

        Returns:
            The item that was at the front

        Raises:
            IndexError: If the queue is empty

        Precondition: Queue is not empty
        Postcondition: Front item removed, size decreased by 1
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._items.pop(0)  # Remove from front (inefficient!)

    def front(self):
        """
        Return the front item without removing it.

        Returns:
            The item at the front

        Raises:
            IndexError: If the queue is empty

        Precondition: Queue is not empty
        """
        if self.is_empty():
            raise IndexError("Cannot access front of empty queue")
        return self._items[0]

    def is_empty(self):
        """
        Check if the queue has no items.

        Returns:
            True if queue is empty, False otherwise
        """
        return len(self._items) == 0

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            Integer count of items
        """
        return len(self._items)

    def __str__(self):
        """Return string representation of the queue."""
        return f"Queue({self._items})"

    def __len__(self):
        """Support len(queue) syntax."""
        return self.size()


# Additional ADT implementations for comparison


class EfficientQueue:
    """
    A more efficient Queue implementation using two stacks.

    This avoids the O(n) dequeue operation of the list-based queue.
    enqueue: O(1), dequeue: amortized O(1)
    """

    def __init__(self):
        self._inbox = []  # For enqueue operations
        self._outbox = []  # For dequeue operations

    def enqueue(self, item):
        """Add item to the back (O(1))."""
        self._inbox.append(item)

    def dequeue(self):
        """Remove and return front item (amortized O(1))."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")

        if not self._outbox:
            # Transfer all items from inbox to outbox (reverses order)
            while self._inbox:
                self._outbox.append(self._inbox.pop())

        return self._outbox.pop()

    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot access front of empty queue")

        if not self._outbox:
            # Transfer all items from inbox to outbox (reverses order)
            while self._inbox:
                self._outbox.append(self._inbox.pop())

        return self._outbox[-1]

    def is_empty(self):
        """Check if queue is empty."""
        return not self._inbox and not self._outbox

    def size(self):
        """Return number of items."""
        return len(self._inbox) + len(self._outbox)

    def __str__(self):
        """String representation."""
        # Reconstruct the queue order for display
        items = self._outbox[::-1] + self._inbox
        return f"EfficientQueue({items})"


# Utility functions for ADT demonstrations


def reverse_string(text):
    """
    Reverse a string using a stack.

    Args:
        text: String to reverse

    Returns:
        Reversed string
    """
    stack = Stack()
    for char in text:
        stack.push(char)

    result = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


def is_balanced_parentheses(expression):
    """
    Check if parentheses are balanced using a stack.

    Args:
        expression: String containing parentheses

    Returns:
        True if balanced, False otherwise
    """
    stack = Stack()
    pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


def simulate_print_queue(jobs):
    """
    Simulate a print queue using a queue ADT.

    Args:
        jobs: List of print job names

    Returns:
        List of jobs in processing order
    """
    queue = Queue()
    processed = []

    # Add all jobs to queue
    for job in jobs:
        queue.enqueue(job)

    # Process jobs in FIFO order
    while not queue.is_empty():
        current_job = queue.dequeue()
        processed.append(current_job)
        print(f"Processing: {current_job}")

    return processed


if __name__ == "__main__":
    print("=== Chapter 6: Stacks and Queues Demo ===\n")

    # Stack demonstration
    print("Stack (LIFO) Operations:")
    stack = Stack()
    for item in ["first", "second", "third"]:
        stack.push(item)
        print(f"  Pushed: {item}, Stack: {stack}")

    while not stack.is_empty():
        item = stack.pop()
        print(f"  Popped: {item}, Stack: {stack}")
    print()

    # Queue demonstration
    print("Queue (FIFO) Operations:")
    queue = Queue()
    for item in ["first", "second", "third"]:
        queue.enqueue(item)
        print(f"  Enqueued: {item}, Queue: {queue}")

    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Dequeued: {item}, Queue: {queue}")
    print()

    # Practical applications
    print("Practical Applications:")

    # String reversal with stack
    text = "hello world"
    reversed_text = reverse_string(text)
    print(f"  String reversal: '{text}' -> '{reversed_text}'")

    # Balanced parentheses check
    expressions = ["(a + b)", "(a + b", "((a + b))", "(a + b))"]
    for expr in expressions:
        balanced = is_balanced_parentheses(expr)
        print(f"  '{expr}' balanced: {balanced}")

    print()

    # Print queue simulation
    print("Print Queue Simulation:")
    jobs = ["document1.pdf", "photo.jpg", "report.docx"]
    processed_jobs = simulate_print_queue(jobs)
    print(f"Jobs processed in order: {processed_jobs}")
