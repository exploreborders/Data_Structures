import unittest
from chapter_08_doubly_linked_lists.code.concatenation_impl import (
    DoublyNode,
    DoublyLinkedList,
    demonstrate_concatenation_performance,
    create_sample_lists,
)


class TestDoublyNode(unittest.TestCase):
    """Test DoublyNode functionality."""

    def test_node_creation(self):
        """Test node initialization."""
        node = DoublyNode("test")
        self.assertEqual(node.data, "test")
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)
        self.assertEqual(str(node), "DoublyNode(test)")


class TestDoublyLinkedListBasics(unittest.TestCase):
    """Test basic DoublyLinkedList operations."""

    def setUp(self):
        self.list = DoublyLinkedList()

    def test_empty_list(self):
        """Test empty list properties."""
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(len(self.list), 0)
        self.assertEqual(str(self.list), "DoublyLinkedList([])")

    def test_append_single(self):
        """Test appending single element."""
        self.list.append("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")
        self.assertEqual(self.list.tail.data, "first")
        self.assertIsNone(self.list.head.prev)
        self.assertIsNone(self.list.tail.next)

    def test_append_multiple(self):
        """Test appending multiple elements."""
        elements = ["A", "B", "C"]
        for elem in elements:
            self.list.append(elem)

        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list.head.data, "A")
        self.assertEqual(self.list.tail.data, "C")

        # Check forward links
        current = self.list.head
        for expected in elements:
            self.assertEqual(current.data, expected)
            current = current.next

        # Check backward links
        current = self.list.tail
        for expected in reversed(elements):
            self.assertEqual(current.data, expected)
            current = current.prev

    def test_prepend_single(self):
        """Test prepending single element."""
        self.list.prepend("first")
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head.data, "first")
        self.assertEqual(self.list.tail.data, "first")

    def test_prepend_multiple(self):
        """Test prepending multiple elements."""
        self.list.prepend("first")
        self.list.prepend("second")
        self.list.prepend("third")

        self.assertEqual(len(self.list), 3)
        # Should be: third -> second -> first
        self.assertEqual(self.list.head.data, "third")
        self.assertEqual(self.list.tail.data, "first")

    def test_iteration(self):
        """Test list iteration."""
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.list.append(elem)

        collected = list(self.list)
        self.assertEqual(collected, elements)


class TestConcatenationEfficient(unittest.TestCase):
    """Test efficient O(1) concatenation."""

    def setUp(self):
        self.list1 = DoublyLinkedList()
        self.list2 = DoublyLinkedList()

    def test_concatenate_empty_empty(self):
        """Test concatenating two empty lists."""
        result = self.list1.concatenate_efficient(self.list2)
        self.assertEqual(len(result), 0)
        self.assertIsNone(result.head)
        self.assertIsNone(result.tail)

    def test_concatenate_empty_nonempty(self):
        """Test concatenating empty list with non-empty list."""
        self.list2.append("A")
        self.list2.append("B")

        result = self.list1.concatenate_efficient(self.list2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result.head.data, "A")
        self.assertEqual(result.tail.data, "B")
        self.assertEqual(len(self.list2), 0)  # list2 should be empty

    def test_concatenate_nonempty_empty(self):
        """Test concatenating non-empty list with empty list."""
        self.list1.append("X")
        self.list1.append("Y")

        original_len = len(self.list1)
        result = self.list1.concatenate_efficient(self.list2)

        self.assertEqual(len(result), original_len)
        self.assertEqual(result.head.data, "X")
        self.assertEqual(result.tail.data, "Y")

    def test_concatenate_two_nonempty(self):
        """Test concatenating two non-empty lists."""
        # List 1: [1, 2]
        self.list1.append(1)
        self.list1.append(2)

        # List 2: [3, 4, 5]
        self.list2.append(3)
        self.list2.append(4)
        self.list2.append(5)

        result = self.list1.concatenate_efficient(self.list2)

        # Check result
        self.assertEqual(len(result), 5)
        expected = [1, 2, 3, 4, 5]
        current = result.head
        for value in expected:
            self.assertEqual(current.data, value)
            current = current.next

        # Check list2 is empty
        self.assertEqual(len(self.list2), 0)
        self.assertIsNone(self.list2.head)
        self.assertIsNone(self.list2.tail)

    def test_pointer_integrity_after_concatenation(self):
        """Test that all pointers are correctly maintained."""
        self.list1.append("A")
        self.list1.append("B")
        self.list2.append("C")
        self.list2.append("D")

        self.list1.concatenate_efficient(self.list2)

        # Verify forward pointers
        current = self.list1.head
        for expected in ["A", "B", "C", "D"]:
            self.assertEqual(current.data, expected)
            current = current.next

        # Verify backward pointers
        current = self.list1.tail
        for expected in ["D", "C", "B", "A"]:
            self.assertEqual(current.data, expected)
            current = current.prev

        # Verify head and tail pointers
        self.assertEqual(self.list1.head.data, "A")
        self.assertEqual(self.list1.tail.data, "D")
        self.assertIsNone(self.list1.head.prev)
        self.assertIsNone(self.list1.tail.next)

    def test_concatenate_with_self_raises_error(self):
        """Test that concatenating list with itself raises error."""
        self.list1.append("test")
        with self.assertRaises(ValueError):
            self.list1.concatenate_efficient(self.list1)

    def test_concatenate_wrong_type_raises_error(self):
        """Test that concatenating with wrong type raises error."""
        with self.assertRaises(TypeError):
            self.list1.concatenate_efficient("not a list")


class TestConcatenationCopy(unittest.TestCase):
    """Test copy-based concatenation."""

    def setUp(self):
        self.list1 = DoublyLinkedList()
        self.list2 = DoublyLinkedList()

    def test_copy_concatenation_preserves_originals(self):
        """Test that copy concatenation doesn't modify original lists."""
        self.list1.append(1)
        self.list1.append(2)
        self.list2.append(3)
        self.list2.append(4)

        original_len1 = len(self.list1)
        original_len2 = len(self.list2)

        result = self.list1.concatenate_copy(self.list2)

        # Originals unchanged
        self.assertEqual(len(self.list1), original_len1)
        self.assertEqual(len(self.list2), original_len2)

        # Result has combined elements
        self.assertEqual(len(result), original_len1 + original_len2)
        expected = [1, 2, 3, 4]
        current = result.head
        for value in expected:
            self.assertEqual(current.data, value)
            current = current.next

    def test_copy_concatenation_empty_lists(self):
        """Test copy concatenation with empty lists."""
        result = self.list1.concatenate_copy(self.list2)
        self.assertEqual(len(result), 0)

    def test_copy_concatenation_different_types(self):
        """Test copy concatenation preserves different data types."""
        self.list1.append(42)
        self.list1.append("hello")
        self.list2.append([1, 2, 3])
        self.list2.append(True)

        result = self.list1.concatenate_copy(self.list2)
        self.assertEqual(len(result), 4)

        expected = [42, "hello", [1, 2, 3], True]
        collected = list(result)
        self.assertEqual(collected, expected)


class TestMultipleConcatenation(unittest.TestCase):
    """Test concatenating multiple lists."""

    def test_concatenate_multiple_lists(self):
        """Test concatenating three lists at once."""
        lists = []
        for i in range(3):
            lst = DoublyLinkedList()
            lst.append(f"list{i}_item1")
            lst.append(f"list{i}_item2")
            lists.append(lst)

        base_list = DoublyLinkedList()
        base_list.concatenate_multiple(*lists)

        self.assertEqual(len(base_list), 6)
        expected = [
            "list0_item1",
            "list0_item2",
            "list1_item1",
            "list1_item2",
            "list2_item1",
            "list2_item2",
        ]
        collected = list(base_list)
        self.assertEqual(collected, expected)

        # Source lists should be empty
        for lst in lists:
            self.assertEqual(len(lst), 0)

    def test_concatenate_multiple_with_empty_lists(self):
        """Test concatenating with some empty lists."""
        list1 = DoublyLinkedList()
        list1.append("A")

        empty1 = DoublyLinkedList()
        empty2 = DoublyLinkedList()

        list2 = DoublyLinkedList()
        list2.append("B")

        base = DoublyLinkedList()
        base.concatenate_multiple(list1, empty1, list2, empty2)

        self.assertEqual(len(base), 2)
        self.assertEqual(list(base), ["A", "B"])


class TestListOperations(unittest.TestCase):
    """Test additional list operations."""

    def test_split_at_beginning(self):
        """Test splitting at index 0."""
        lst = DoublyLinkedList()
        for i in range(5):
            lst.append(i)

        split_list = lst.split_at(0)

        # Original list should be empty
        self.assertEqual(len(lst), 0)
        self.assertIsNone(lst.head)

        # Split list should have all elements
        self.assertEqual(len(split_list), 5)
        self.assertEqual(list(split_list), [0, 1, 2, 3, 4])

    def test_split_at_middle(self):
        """Test splitting in the middle."""
        lst = DoublyLinkedList()
        for i in range(5):
            lst.append(i)

        split_list = lst.split_at(2)

        # Original list should have first 2 elements
        self.assertEqual(len(lst), 2)
        self.assertEqual(list(lst), [0, 1])

        # Split list should have remaining elements
        self.assertEqual(len(split_list), 3)
        self.assertEqual(list(split_list), [2, 3, 4])

    def test_split_at_end(self):
        """Test splitting at the end."""
        lst = DoublyLinkedList()
        for i in range(3):
            lst.append(i)

        split_list = lst.split_at(5)  # Beyond end

        # Original list unchanged
        self.assertEqual(len(lst), 3)
        self.assertEqual(list(lst), [0, 1, 2])

        # Split list empty
        self.assertEqual(len(split_list), 0)

    def test_clone(self):
        """Test list cloning."""
        original = DoublyLinkedList()
        for i in range(3):
            original.append(i)

        cloned = original.clone()

        # Same content
        self.assertEqual(list(original), list(cloned))
        self.assertEqual(len(original), len(cloned))

        # Different objects
        self.assertIsNot(original, cloned)
        self.assertIsNot(original.head, cloned.head)

        # Modifying clone doesn't affect original
        cloned.append(99)
        self.assertEqual(len(original), 3)
        self.assertEqual(len(cloned), 4)


class TestPerformance(unittest.TestCase):
    """Test performance characteristics."""

    def test_concatenation_performance_comparison(self):
        """Test that efficient concatenation is indeed faster."""
        # This test verifies the functions run without error
        # In a real performance test, we'd measure actual times
        try:
            times = demonstrate_concatenation_performance()
            self.assertEqual(len(times), 2)
            self.assertTrue(all(t >= 0 for t in times))
        except Exception as e:
            self.fail(f"Performance demonstration failed: {e}")


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple operations."""

    def test_complex_operations_sequence(self):
        """Test a sequence of complex operations."""
        # Create and populate list
        lst = DoublyLinkedList()
        for i in range(10):
            lst.append(i)

        # Split into two parts
        part2 = lst.split_at(5)

        # Concatenate back with another list
        extra = DoublyLinkedList()
        extra.append(99)
        extra.append(100)

        # Efficient concatenation
        lst.concatenate_efficient(extra)
        # Copy concatenation
        final = lst.concatenate_copy(part2)

        # Verify final result
        expected = [0, 1, 2, 3, 4, 99, 100, 5, 6, 7, 8, 9]
        self.assertEqual(list(final), expected)

    def test_round_trip_operations(self):
        """Test operations that should be reversible."""
        original = DoublyLinkedList()
        data = [1, 2, 3, 4, 5]
        for item in data:
            original.append(item)

        # Clone for testing
        test_list = original.clone()

        # Split and recombine
        part2 = test_list.split_at(3)
        test_list.concatenate_efficient(part2)

        # Should be back to original
        self.assertEqual(list(test_list), data)
        self.assertEqual(len(test_list), len(original))


if __name__ == "__main__":
    unittest.main()
