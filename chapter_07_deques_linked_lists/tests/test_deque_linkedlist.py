import unittest
from chapter_07_deques_linked_lists.code.deque_linkedlist_impl import (
    Node,
    DoublyNode,
    LinkedList,
    DoublyLinkedList,
    Deque,
    LinkedQueue,
    reverse_with_deque,
    check_palindrome,
    sliding_window_maximum,
)


class TestNodes(unittest.TestCase):
    """Test Node classes."""

    def test_node_creation(self):
        """Test basic node creation."""
        node = Node("data")
        self.assertEqual(node.data, "data")
        self.assertIsNone(node.next)
        self.assertEqual(str(node), "Node(data)")

    def test_doubly_node_creation(self):
        """Test doubly node creation."""
        node = DoublyNode(42)
        self.assertEqual(node.data, 42)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        self.assertEqual(str(node), "DoublyNode(42)")


class TestLinkedList(unittest.TestCase):
    """Comprehensive tests for LinkedList implementation."""

    def setUp(self):
        self.list = LinkedList()

    def test_empty_list(self):
        """Test empty list properties."""
        self.assertIsNone(self.list.head)
        self.assertEqual(len(self.list), 0)
        self.assertEqual(str(self.list), "LinkedList([])")

    def test_append_single_item(self):
        """Test appending to empty list."""
        self.list.append("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")
        self.assertIsNone(self.list.head.next)

    def test_append_multiple_items(self):
        """Test appending multiple items."""
        items = ["first", "second", "third"]
        for item in items:
            self.list.append(item)

        self.assertEqual(len(self.list), 3)

        # Check the chain
        current = self.list.head
        for expected in items:
            self.assertEqual(current.data, expected)
            current = current.next
        self.assertIsNone(current)

    def test_prepend_single_item(self):
        """Test prepending to empty list."""
        self.list.prepend("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")

    def test_prepend_multiple_items(self):
        """Test prepending multiple items (reverse order)."""
        self.list.prepend("first")
        self.list.prepend("second")
        self.list.prepend("third")

        self.assertEqual(len(self.list), 3)
        # Should be: third -> second -> first
        self.assertEqual(self.list.head.data, "third")
        self.assertEqual(self.list.head.next.data, "second")
        self.assertEqual(self.list.head.next.next.data, "first")

    def test_mixed_append_prepend(self):
        """Test mixing append and prepend operations."""
        self.list.append("middle")
        self.list.prepend("start")
        self.list.append("end")

        self.assertEqual(len(self.list), 3)
        # Should be: start -> middle -> end
        current = self.list.head
        self.assertEqual(current.data, "start")
        current = current.next
        self.assertEqual(current.data, "middle")
        current = current.next
        self.assertEqual(current.data, "end")
        self.assertIsNone(current.next)

    def test_insert_after_existing(self):
        """Test inserting after existing item."""
        self.list.append("first")
        self.list.append("third")

        result = self.list.insert_after("first", "second")
        self.assertTrue(result)
        self.assertEqual(len(self.list), 3)

        # Should be: first -> second -> third
        current = self.list.head
        self.assertEqual(current.data, "first")
        current = current.next
        self.assertEqual(current.data, "second")
        current = current.next
        self.assertEqual(current.data, "third")

    def test_insert_after_nonexistent(self):
        """Test inserting after non-existent item."""
        self.list.append("first")
        result = self.list.insert_after("nonexistent", "second")
        self.assertFalse(result)
        self.assertEqual(len(self.list), 1)

    def test_remove_existing(self):
        """Test removing existing item."""
        self.list.append("first")
        self.list.append("second")
        self.list.append("third")

        result = self.list.remove("second")
        self.assertTrue(result)
        self.assertEqual(len(self.list), 2)

        # Should be: first -> third
        current = self.list.head
        self.assertEqual(current.data, "first")
        current = current.next
        self.assertEqual(current.data, "third")

    def test_remove_head(self):
        """Test removing head item."""
        self.list.append("first")
        self.list.append("second")

        result = self.list.remove("first")
        self.assertTrue(result)
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "second")

    def test_remove_nonexistent(self):
        """Test removing non-existent item."""
        self.list.append("first")
        result = self.list.remove("nonexistent")
        self.assertFalse(result)
        self.assertEqual(len(self.list), 1)

    def test_find_existing(self):
        """Test finding existing item."""
        self.list.append("first")
        self.list.append("second")

        node = self.list.find("second")
        self.assertIsNotNone(node)
        self.assertEqual(node.data, "second")

    def test_find_nonexistent(self):
        """Test finding non-existent item."""
        self.list.append("first")
        node = self.list.find("nonexistent")
        self.assertIsNone(node)

    def test_iteration(self):
        """Test list iteration."""
        items = ["a", "b", "c"]
        for item in items:
            self.list.append(item)

        collected = list(self.list)
        self.assertEqual(collected, items)


class TestDoublyLinkedList(unittest.TestCase):
    """Tests for DoublyLinkedList implementation."""

    def setUp(self):
        self.list = DoublyLinkedList()

    def test_empty_list(self):
        """Test empty doubly linked list."""
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(len(self.list), 0)

    def test_append_single(self):
        """Test appending single item."""
        self.list.append("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")
        self.assertEqual(self.list.tail.data, "first")
        self.assertIsNone(self.list.head.prev)
        self.assertIsNone(self.list.tail.next)

    def test_append_multiple(self):
        """Test appending multiple items."""
        items = ["first", "second", "third"]
        for item in items:
            self.list.append(item)

        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.head.data, "first")
        self.assertEqual(self.list.tail.data, "third")

        # Check forward links
        current = self.list.head
        for expected in items:
            self.assertEqual(current.data, expected)
            current = current.next

        # Check backward links
        current = self.list.tail
        for expected in reversed(items):
            self.assertEqual(current.data, expected)
            current = current.prev

    def test_prepend_single(self):
        """Test prepending single item."""
        self.list.prepend("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")
        self.assertEqual(self.list.tail.data, "first")

    def test_prepend_multiple(self):
        """Test prepending multiple items."""
        self.list.prepend("first")
        self.list.prepend("second")
        self.list.prepend("third")

        self.assertEqual(len(self.list), 3)
        # Should be: third -> second -> first
        self.assertEqual(self.list.head.data, "third")
        self.assertEqual(self.list.tail.data, "first")

    def test_mixed_operations(self):
        """Test mixing append and prepend."""
        self.list.append("middle")
        self.list.prepend("start")
        self.list.append("end")

        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.head.data, "start")
        self.assertEqual(self.list.head.next.data, "middle")
        self.assertEqual(self.list.tail.data, "end")

    def test_remove_first_single(self):
        """Test removing first from single-item list."""
        self.list.append("only")
        result = self.list.remove_first()
        self.assertEqual(result, "only")
        self.assertEqual(len(self.list), 0)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_remove_first_multiple(self):
        """Test removing first from multi-item list."""
        self.list.append("first")
        self.list.append("second")
        self.list.append("third")

        result = self.list.remove_first()
        self.assertEqual(result, "first")
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.head.data, "second")
        self.assertIsNone(self.list.head.prev)

    def test_remove_last_single(self):
        """Test removing last from single-item list."""
        self.list.append("only")
        result = self.list.remove_last()
        self.assertEqual(result, "only")
        self.assertEqual(len(self.list), 0)

    def test_remove_last_multiple(self):
        """Test removing last from multi-item list."""
        self.list.append("first")
        self.list.append("second")
        self.list.append("third")

        result = self.list.remove_last()
        self.assertEqual(result, "third")
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.tail.data, "second")
        self.assertIsNone(self.list.tail.next)

    def test_remove_first_empty(self):
        """Test removing first from empty list."""
        with self.assertRaises(IndexError):
            self.list.remove_first()

    def test_remove_last_empty(self):
        """Test removing last from empty list."""
        with self.assertRaises(IndexError):
            self.list.remove_last()


class TestDeque(unittest.TestCase):
    """Tests for Deque ADT implementation."""

    def setUp(self):
        self.deque = Deque()

    def test_empty_deque(self):
        """Test empty deque properties."""
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 0)

    def test_add_first_single(self):
        """Test adding first item."""
        self.deque.add_first("first")
        self.assertFalse(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 1)
        self.assertEqual(self.deque.first(), "first")
        self.assertEqual(self.deque.last(), "first")

    def test_add_last_single(self):
        """Test adding last item."""
        self.deque.add_last("last")
        self.assertFalse(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 1)
        self.assertEqual(self.deque.first(), "last")
        self.assertEqual(self.deque.last(), "last")

    def test_add_both_ends(self):
        """Test adding to both ends."""
        self.deque.add_first("first")
        self.deque.add_last("last")
        self.deque.add_first("very_first")

        self.assertEqual(self.deque.size(), 3)
        self.assertEqual(self.deque.first(), "very_first")
        self.assertEqual(self.deque.last(), "last")

    def test_remove_first_single(self):
        """Test removing first from single-item deque."""
        self.deque.add_first("only")
        result = self.deque.remove_first()
        self.assertEqual(result, "only")
        self.assertTrue(self.deque.is_empty())

    def test_remove_last_single(self):
        """Test removing last from single-item deque."""
        self.deque.add_last("only")
        result = self.deque.remove_last()
        self.assertEqual(result, "only")
        self.assertTrue(self.deque.is_empty())

    def test_fifo_like_behavior(self):
        """Test that deque can behave like queue (FIFO)."""
        self.deque.add_last("first")
        self.deque.add_last("second")
        self.deque.add_last("third")

        self.assertEqual(self.deque.remove_first(), "first")
        self.assertEqual(self.deque.remove_first(), "second")
        self.assertEqual(self.deque.remove_first(), "third")
        self.assertTrue(self.deque.is_empty())

    def test_lifo_like_behavior(self):
        """Test that deque can behave like stack (LIFO)."""
        self.deque.add_first("first")
        self.deque.add_first("second")
        self.deque.add_first("third")

        self.assertEqual(self.deque.remove_first(), "third")
        self.assertEqual(self.deque.remove_first(), "second")
        self.assertEqual(self.deque.remove_first(), "first")
        self.assertTrue(self.deque.is_empty())

    def test_remove_first_empty(self):
        """Test removing first from empty deque."""
        with self.assertRaises(IndexError):
            self.deque.remove_first()

    def test_remove_last_empty(self):
        """Test removing last from empty deque."""
        with self.assertRaises(IndexError):
            self.deque.remove_last()

    def test_first_empty(self):
        """Test first() on empty deque."""
        with self.assertRaises(IndexError):
            self.deque.first()

    def test_last_empty(self):
        """Test last() on empty deque."""
        with self.assertRaises(IndexError):
            self.deque.last()

    def test_large_deque(self):
        """Test deque with many items."""
        # Add many items
        for i in range(1000):
            if i % 2 == 0:
                self.deque.add_first(i)
            else:
                self.deque.add_last(i)

        self.assertEqual(self.deque.size(), 1000)

        # Remove half from each end
        for _ in range(250):
            self.deque.remove_first()
            self.deque.remove_last()

        self.assertEqual(self.deque.size(), 500)


class TestLinkedQueue(unittest.TestCase):
    """Tests for LinkedQueue (Wrapper Pattern demonstration)."""

    def setUp(self):
        self.queue = LinkedQueue()

    def test_empty_queue(self):
        """Test empty queue properties."""
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_enqueue_single(self):
        """Test enqueuing single item."""
        self.queue.enqueue("first")
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.front(), "first")

    def test_enqueue_multiple(self):
        """Test enqueuing multiple items."""
        items = ["first", "second", "third"]
        for item in items:
            self.queue.enqueue(item)

        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.front(), "first")

    def test_dequeue_single(self):
        """Test dequeuing single item."""
        self.queue.enqueue("only")
        result = self.queue.dequeue()
        self.assertEqual(result, "only")
        self.assertTrue(self.queue.is_empty())

    def test_fifo_order(self):
        """Test FIFO ordering."""
        items = ["A", "B", "C", "D"]
        for item in items:
            self.queue.enqueue(item)

        dequeued = []
        while not self.queue.is_empty():
            dequeued.append(self.queue.dequeue())

        self.assertEqual(dequeued, items)

    def test_front_no_remove(self):
        """Test that front() doesn't remove items."""
        self.queue.enqueue("first")
        self.queue.enqueue("second")

        self.assertEqual(self.queue.front(), "first")
        self.assertEqual(self.queue.size(), 2)

        self.assertEqual(self.queue.dequeue(), "first")
        self.assertEqual(self.queue.front(), "second")

    def test_dequeue_empty(self):
        """Test dequeuing from empty queue."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_front_empty(self):
        """Test front() on empty queue."""
        with self.assertRaises(IndexError):
            self.queue.front()


class TestApplications(unittest.TestCase):
    """Tests for practical applications using the data structures."""

    def test_reverse_with_deque(self):
        """Test string reversal using deque."""
        test_cases = [
            ("", ""),
            ("a", "a"),
            ("hello", "olleh"),
            ("12345", "54321"),
            ("Able was I ere I saw Elba", "ablE was I ere I saw elbA"),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = reverse_with_deque(input_str)
                self.assertEqual(result, expected)

    def test_palindrome_checking(self):
        """Test palindrome detection."""
        test_cases = [
            ("", True),
            ("a", True),
            ("aa", True),
            ("aba", True),
            ("abba", True),
            ("hello", False),
            ("Able was I ere I saw Elba", True),  # Case and spaces ignored
            ("A man a plan a canal Panama", True),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                result = check_palindrome(text)
                self.assertEqual(result, expected)

    def test_sliding_window_maximum(self):
        """Test sliding window maximum algorithm."""
        # Example from the code
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        result = sliding_window_maximum(nums, k)
        expected = [3, 3, 5, 5, 6, 7]  # Maximum in each window of 3
        self.assertEqual(result, expected)

    def test_sliding_window_edge_cases(self):
        """Test sliding window with edge cases."""
        # Empty array
        self.assertEqual(sliding_window_maximum([], 3), [])

        # k = 0 (invalid)
        self.assertEqual(sliding_window_maximum([1, 2, 3], 0), [])

        # k = 1 (each element is its own max)
        self.assertEqual(sliding_window_maximum([1, 3, 2], 1), [1, 3, 2])

        # k larger than array
        self.assertEqual(sliding_window_maximum([1, 2, 3], 5), [])


# Performance comparison tests
class TestPerformanceComparisons(unittest.TestCase):
    """Tests comparing performance characteristics."""

    def test_linked_vs_list_queue_performance(self):
        """Compare LinkedQueue vs list-based Queue performance."""
        from chapter_06_stacks_and_queues.code.stack_queue_adts import Queue as ListQueue

        # Test with moderate size (too large and list-queue is very slow)
        size = 1000

        # Setup both queues
        list_queue = ListQueue()
        linked_queue = LinkedQueue()

        for i in range(size):
            list_queue.enqueue(i)
            linked_queue.enqueue(i)

        # Time dequeue operations
        import timeit

        def list_dequeue_ops():
            result = []
            for _ in range(min(100, size)):
                if not list_queue.is_empty():
                    result.append(list_queue.dequeue())
            return result

        def linked_dequeue_ops():
            result = []
            for _ in range(min(100, size)):
                if not linked_queue.is_empty():
                    result.append(linked_queue.dequeue())
            return result

        list_time = timeit.timeit(list_dequeue_ops, number=1)
        linked_time = timeit.timeit(linked_dequeue_ops, number=1)

        # Both should take some time (not optimized away)
        self.assertGreater(list_time, 0)
        self.assertGreater(linked_time, 0)

        # For small n, list might actually be faster due to lower overhead
        # The real benefit of LinkedQueue shows with large n or frequent dequeues
        # We just verify both implementations work correctly


if __name__ == "__main__":
    unittest.main()
