import unittest
import sys
import os

# Add root directory to path so imports work
sys.path.insert(0, os.path.join(os.getcwd(), "..", ".."))
from chapter_06_stacks_and_queues.code.stack_queue_adts import (
    Stack,
    Queue,
    EfficientQueue,
    reverse_string,
    is_balanced_parentheses,
    simulate_print_queue,
)


class TestStack(unittest.TestCase):
    """Comprehensive tests for the Stack ADT."""

    def setUp(self):
        """Set up a fresh stack for each test."""
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        """Test that a new stack starts empty."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)

    def test_push_increases_size(self):
        """Test that push increases stack size."""
        self.stack.push("item1")
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

        self.stack.push("item2")
        self.assertEqual(self.stack.size(), 2)

    def test_push_pop_roundtrip(self):
        """Test that push and pop work correctly together."""
        # Push items
        self.stack.push("first")
        self.stack.push("second")
        self.stack.push("third")

        # Verify LIFO behavior
        self.assertEqual(self.stack.pop(), "third")
        self.assertEqual(self.stack.pop(), "second")
        self.assertEqual(self.stack.pop(), "first")
        self.assertTrue(self.stack.is_empty())

    def test_peek_does_not_remove(self):
        """Test that peek returns top item without removing it."""
        self.stack.push("bottom")
        self.stack.push("top")

        # Peek should return top
        self.assertEqual(self.stack.peek(), "top")
        self.assertEqual(self.stack.size(), 2)

        # Pop should still work normally
        self.assertEqual(self.stack.pop(), "top")
        self.assertEqual(self.stack.peek(), "bottom")

    def test_pop_empty_stack_raises_error(self):
        """Test that popping from empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_stack_raises_error(self):
        """Test that peeking at empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_string_representation(self):
        """Test string representation of stack."""
        self.assertEqual(str(self.stack), "Stack([])")

        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(str(self.stack), "Stack([1, 2])")

    def test_large_stack_operations(self):
        """Test stack with many items."""
        # Push many items
        for i in range(1000):
            self.stack.push(i)

        self.assertEqual(self.stack.size(), 1000)

        # Pop in reverse order
        for i in range(999, -1, -1):
            self.assertEqual(self.stack.pop(), i)

        self.assertTrue(self.stack.is_empty())


class TestQueue(unittest.TestCase):
    """Comprehensive tests for the Queue ADT."""

    def setUp(self):
        """Set up a fresh queue for each test."""
        self.queue = Queue()

    def test_new_queue_is_empty(self):
        """Test that a new queue starts empty."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)
        self.assertEqual(len(self.queue), 0)

    def test_enqueue_increases_size(self):
        """Test that enqueue increases queue size."""
        self.queue.enqueue("item1")
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

        self.queue.enqueue("item2")
        self.assertEqual(self.queue.size(), 2)

    def test_enqueue_dequeue_roundtrip(self):
        """Test that enqueue and dequeue work correctly together."""
        # Enqueue items
        self.queue.enqueue("first")
        self.queue.enqueue("second")
        self.queue.enqueue("third")

        # Verify FIFO behavior
        self.assertEqual(self.queue.dequeue(), "first")
        self.assertEqual(self.queue.dequeue(), "second")
        self.assertEqual(self.queue.dequeue(), "third")
        self.assertTrue(self.queue.is_empty())

    def test_front_does_not_remove(self):
        """Test that front returns first item without removing it."""
        self.queue.enqueue("first")
        self.queue.enqueue("second")

        # Front should return first
        self.assertEqual(self.queue.front(), "first")
        self.assertEqual(self.queue.size(), 2)

        # Dequeue should still work normally
        self.assertEqual(self.queue.dequeue(), "first")
        self.assertEqual(self.queue.front(), "second")

    def test_dequeue_empty_queue_raises_error(self):
        """Test that dequeue from empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_front_empty_queue_raises_error(self):
        """Test that front of empty queue raises IndexError."""
        with self.assertRaises(IndexError):
            self.queue.front()

    def test_string_representation(self):
        """Test string representation of queue."""
        self.assertEqual(str(self.queue), "Queue([])")

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "Queue([1, 2])")

    def test_fifo_order_preservation(self):
        """Test that FIFO order is preserved."""
        # Add items in order
        items = ["A", "B", "C", "D"]
        for item in items:
            self.queue.enqueue(item)

        # Remove items should be in same order
        dequeued_items = []
        while not self.queue.is_empty():
            dequeued_items.append(self.queue.dequeue())

        self.assertEqual(dequeued_items, items)


class TestEfficientQueue(unittest.TestCase):
    """Tests for the more efficient queue implementation."""

    def setUp(self):
        self.queue = EfficientQueue()

    def test_efficient_queue_behavior(self):
        """Test that efficient queue behaves like a regular queue."""
        # Test basic operations
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())

    def test_efficient_vs_regular_queue(self):
        """Test that efficient queue produces same results as regular queue."""
        regular_queue = Queue()
        efficient_queue = EfficientQueue()

        # Add same items to both
        items = [1, 2, 3, 4, 5]
        for item in items:
            regular_queue.enqueue(item)
            efficient_queue.enqueue(item)

        # Both should dequeue in same order
        regular_results = []
        efficient_results = []

        while not regular_queue.is_empty():
            regular_results.append(regular_queue.dequeue())

        while not efficient_queue.is_empty():
            efficient_results.append(efficient_queue.dequeue())

        self.assertEqual(regular_results, efficient_results)
        self.assertEqual(regular_results, items)


class TestStackApplications(unittest.TestCase):
    """Tests for stack-based algorithms and applications."""

    def test_reverse_string(self):
        """Test string reversal using stack."""
        test_cases = [
            ("", ""),
            ("a", "a"),
            ("hello", "olleh"),
            ("12345", "54321"),
            ("A man a plan a canal Panama", "amanaP lanac a nalp a nam A"),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = reverse_string(input_str)
                self.assertEqual(result, expected)

    def test_balanced_parentheses(self):
        """Test balanced parentheses checking."""
        test_cases = [
            # Balanced cases
            ("", True),
            ("()", True),
            ("(a + b)", True),
            ("((a + b))", True),
            ("(a + (b + c))", True),
            ("[a + b]", True),
            ("{a + b}", True),
            ("(a) [b] {c}", True),
            # Unbalanced cases
            ("(", False),
            (")", False),
            ("(a + b", False),
            ("a + b)", False),
            ("((a + b)", False),
            ("(a + b))", False),
            ("[a + b)", False),
            ("(a + b]", False),
            ("{a + b)", False),
            ("(a + b}", False),
        ]

        for expression, expected in test_cases:
            with self.subTest(expression=expression):
                result = is_balanced_parentheses(expression)
                self.assertEqual(result, expected)


class TestQueueApplications(unittest.TestCase):
    """Tests for queue-based algorithms and applications."""

    def test_print_queue_simulation(self):
        """Test print queue simulation."""
        jobs = ["doc1.pdf", "photo.jpg", "report.docx", "diagram.png"]

        # Capture printed output (this is a simple test)
        result = simulate_print_queue(jobs)

        # Should process in FIFO order
        self.assertEqual(result, jobs)
        self.assertEqual(len(result), len(jobs))

    def test_empty_job_list(self):
        """Test print queue with empty job list."""
        result = simulate_print_queue([])
        self.assertEqual(result, [])


# Performance comparison tests
class TestPerformanceComparisons(unittest.TestCase):
    """Tests comparing performance characteristics."""

    def test_stack_operations_are_efficient(self):
        """Test that stack operations remain efficient with many items."""
        stack = Stack()

        # Add many items
        n = 10000
        for i in range(n):
            stack.push(i)

        self.assertEqual(stack.size(), n)

        # Operations should still be fast (conceptual test)
        # In real performance testing, you'd measure time
        self.assertEqual(stack.peek(), n - 1)
        self.assertEqual(stack.size(), n)

    def test_queue_performance_characteristics(self):
        """Demonstrate queue performance characteristics."""
        queue = Queue()

        # Enqueue many items (should be fast)
        n = 1000
        for i in range(n):
            queue.enqueue(i)

        self.assertEqual(queue.size(), n)

        # Dequeue operations (would be slow with large n in list-based queue)
        # This test just verifies correctness, not performance
        for i in range(n):
            self.assertEqual(queue.dequeue(), i)

        self.assertTrue(queue.is_empty())


# Edge case and error handling tests
class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases and comprehensive error handling."""

    def test_stack_with_none_values(self):
        """Test stack with None values."""
        stack = Stack()
        stack.push(None)
        self.assertEqual(stack.peek(), None)
        self.assertEqual(stack.pop(), None)
        self.assertTrue(stack.is_empty())

    def test_queue_with_none_values(self):
        """Test queue with None values."""
        queue = Queue()
        queue.enqueue(None)
        self.assertEqual(queue.front(), None)
        self.assertEqual(queue.dequeue(), None)
        self.assertTrue(queue.is_empty())

    def test_mixed_data_types(self):
        """Test ADTs with mixed data types."""
        stack = Stack()
        queue = Queue()

        # Mix of different types
        items = [42, "hello", [1, 2, 3], {"key": "value"}, None]

        for item in items:
            stack.push(item)
            queue.enqueue(item)

        # Should come out in reverse order for stack
        for item in reversed(items):
            self.assertEqual(stack.pop(), item)

        # Should come out in same order for queue
        for item in items:
            self.assertEqual(queue.dequeue(), item)

    def test_large_data_sets(self):
        """Test with larger data sets to ensure stability."""
        stack = Stack()
        queue = Queue()

        # Test with 1000 items
        n = 1000
        for i in range(n):
            stack.push(i)
            queue.enqueue(i)

        self.assertEqual(stack.size(), n)
        self.assertEqual(queue.size(), n)

        # Verify LIFO for stack
        for i in range(n - 1, -1, -1):
            self.assertEqual(stack.pop(), i)

        # Verify FIFO for queue
        for i in range(n):
            self.assertEqual(queue.dequeue(), i)


if __name__ == "__main__":
    unittest.main()
