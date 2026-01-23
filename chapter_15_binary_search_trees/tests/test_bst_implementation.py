"""
Tests for Chapter 15: Binary Search Trees - Ordered Mapping Implementation
"""

import unittest
from typing import List

# Add the code directory to the path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from bst_implementation import BinarySearchTree, BSTNode, BSTAnalysis


class TestBSTNode(unittest.TestCase):
    """Test cases for BSTNode class."""

    def test_node_creation(self):
        """Test basic BSTNode creation."""
        node = BSTNode("key", "value")
        self.assertEqual(node.key, "key")
        self.assertEqual(node.value, "value")
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertIsNone(node.parent)
        self.assertEqual(node.size, 1)

    def test_node_is_leaf(self):
        """Test leaf node detection."""
        leaf = BSTNode(1, "a")
        self.assertTrue(leaf.is_leaf())

        internal = BSTNode(2, "b")
        internal.left = BSTNode(1, "a")
        self.assertFalse(internal.is_leaf())

    def test_node_height(self):
        """Test node height calculation."""
        # Single node
        node = BSTNode(1, "a")
        self.assertEqual(node.get_height(), 0)

        # Node with left child
        node.left = BSTNode(0, "b")
        self.assertEqual(node.get_height(), 1)

        # Node with both children
        node.right = BSTNode(2, "c")
        self.assertEqual(node.get_height(), 1)

        # Deeper tree
        node.left.left = BSTNode(-1, "d")
        self.assertEqual(node.get_height(), 2)


class TestBinarySearchTree(unittest.TestCase):
    """Test cases for BinarySearchTree class."""

    def setUp(self):
        """Set up test BST."""
        self.bst = BinarySearchTree()

    def test_empty_bst(self):
        """Test operations on empty BST."""
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(len(self.bst), 0)
        self.assertEqual(self.bst.get_height(), 0)

        with self.assertRaises(KeyError):
            self.bst.get(5)

        with self.assertRaises(ValueError):
            self.bst.min_key()

        with self.assertRaises(ValueError):
            self.bst.max_key()

    def test_single_insertion(self):
        """Test inserting single key-value pair."""
        self.bst.put(10, "ten")

        self.assertFalse(self.bst.is_empty())
        self.assertEqual(len(self.bst), 1)
        self.assertEqual(self.bst.get(10), "ten")
        self.assertEqual(self.bst.min_key(), 10)
        self.assertEqual(self.bst.max_key(), 10)

    def test_multiple_insertions(self):
        """Test inserting multiple key-value pairs."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        self.assertEqual(len(self.bst), 6)

        # Test retrieval
        for key, expected_value in values:
            self.assertEqual(self.bst.get(key), expected_value)

        # Test min/max
        self.assertEqual(self.bst.min_key(), 1)
        self.assertEqual(self.bst.max_key(), 14)

    def test_update_existing_key(self):
        """Test updating value for existing key."""
        self.bst.put(5, "five")
        self.assertEqual(self.bst.get(5), "five")

        # Update value
        self.bst.put(5, "updated")
        self.assertEqual(self.bst.get(5), "updated")

        # Size should remain 1
        self.assertEqual(len(self.bst), 1)

    def test_contains(self):
        """Test contains method."""
        self.bst.put(5, "five")

        self.assertTrue(self.bst.contains(5))
        self.assertFalse(self.bst.contains(10))

    def test_removal_leaf_node(self):
        """Test removing a leaf node."""
        # Create BST: 10 with left child 5
        self.bst.put(10, "ten")
        self.bst.put(5, "five")

        self.assertEqual(len(self.bst), 2)
        self.assertEqual(self.bst.remove(5), "five")
        self.assertEqual(len(self.bst), 1)
        self.assertFalse(self.bst.contains(5))
        self.assertTrue(self.bst.is_valid_bst())

    def test_removal_node_with_one_child(self):
        """Test removing a node with one child."""
        # Create BST: 10 with left child 5, 5 has left child 3
        self.bst.put(10, "ten")
        self.bst.put(5, "five")
        self.bst.put(3, "three")

        self.assertEqual(len(self.bst), 3)
        self.assertEqual(self.bst.remove(5), "five")
        self.assertEqual(len(self.bst), 2)
        self.assertFalse(self.bst.contains(5))
        self.assertTrue(self.bst.contains(3))
        self.assertTrue(self.bst.is_valid_bst())

    def test_removal_node_with_two_children(self):
        """Test removing a node with two children."""
        # Create BST with node that has two children
        self.bst.put(10, "ten")
        self.bst.put(5, "five")
        self.bst.put(15, "fifteen")
        self.bst.put(12, "twelve")
        self.bst.put(18, "eighteen")

        self.assertEqual(len(self.bst), 5)
        self.assertEqual(self.bst.remove(15), "fifteen")  # Has two children: 12 and 18
        self.assertEqual(len(self.bst), 4)
        self.assertFalse(self.bst.contains(15))
        self.assertTrue(self.bst.contains(12))
        self.assertTrue(self.bst.contains(18))
        self.assertTrue(self.bst.is_valid_bst())

    def test_remove_nonexistent_key(self):
        """Test removing non-existent key."""
        self.bst.put(5, "five")

        with self.assertRaises(KeyError):
            self.bst.remove(10)

    def test_successor(self):
        """Test successor operation."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        # Test successors
        self.assertEqual(self.bst.successor(1), 3)   # 1 -> 3
        self.assertEqual(self.bst.successor(3), 6)   # 3 -> 6
        self.assertEqual(self.bst.successor(6), 8)   # 6 -> 8
        self.assertEqual(self.bst.successor(8), 10)  # 8 -> 10
        self.assertEqual(self.bst.successor(10), 14) # 10 -> 14
        self.assertIsNone(self.bst.successor(14))    # 14 has no successor

        # Test non-existent key
        self.assertIsNone(self.bst.successor(20))

    def test_predecessor(self):
        """Test predecessor operation."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        # Test predecessors
        self.assertIsNone(self.bst.predecessor(1))   # 1 has no predecessor
        self.assertEqual(self.bst.predecessor(3), 1) # 3 <- 1
        self.assertEqual(self.bst.predecessor(6), 3) # 6 <- 3
        self.assertEqual(self.bst.predecessor(8), 6) # 8 <- 6
        self.assertEqual(self.bst.predecessor(10), 8) # 10 <- 8
        self.assertEqual(self.bst.predecessor(14), 10) # 14 <- 10

        # Test non-existent key
        self.assertIsNone(self.bst.predecessor(0))

    def test_floor(self):
        """Test floor operation."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        # Test floor
        self.assertEqual(self.bst.floor(0), None)    # No key <= 0
        self.assertEqual(self.bst.floor(1), 1)       # 1 <= 1
        self.assertEqual(self.bst.floor(2), 1)       # 1 <= 2
        self.assertEqual(self.bst.floor(4), 3)       # 3 <= 4
        self.assertEqual(self.bst.floor(7), 6)       # 6 <= 7
        self.assertEqual(self.bst.floor(9), 8)       # 8 <= 9
        self.assertEqual(self.bst.floor(11), 10)     # 10 <= 11
        self.assertEqual(self.bst.floor(15), 14)     # 14 <= 15
        self.assertEqual(self.bst.floor(20), 14)     # 14 <= 20

    def test_ceiling(self):
        """Test ceiling operation."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        # Test ceiling
        self.assertEqual(self.bst.ceiling(0), 1)      # 1 >= 0
        self.assertEqual(self.bst.ceiling(1), 1)      # 1 >= 1
        self.assertEqual(self.bst.ceiling(2), 3)      # 3 >= 2
        self.assertEqual(self.bst.ceiling(4), 6)      # 6 >= 4
        self.assertEqual(self.bst.ceiling(7), 8)      # 8 >= 7
        self.assertEqual(self.bst.ceiling(9), 10)     # 10 >= 9
        self.assertEqual(self.bst.ceiling(11), 14)    # 14 >= 11
        self.assertEqual(self.bst.ceiling(15), None)  # No key >= 15

    def test_range_queries(self):
        """Test range query operations."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six"), (14, "fourteen")]
        for key, value in values:
            self.bst.put(key, value)

        # Test keys in range
        self.assertEqual(self.bst.keys_in_range(3, 10), [3, 6, 8, 10])
        self.assertEqual(self.bst.keys_in_range(1, 5), [1, 3])
        self.assertEqual(self.bst.keys_in_range(12, 16), [14])
        self.assertEqual(self.bst.keys_in_range(20, 25), [])

        # Test values in range
        self.assertEqual(self.bst.values_in_range(3, 10), ["three", "six", "eight", "ten"])

    def test_traversals(self):
        """Test tree traversals."""
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six")]
        for key, value in values:
            self.bst.put(key, value)

        # Inorder should be sorted
        inorder = self.bst.inorder_traversal()
        expected_inorder = [(1, "one"), (3, "three"), (6, "six"), (8, "eight"), (10, "ten")]
        self.assertEqual(inorder, expected_inorder)

        # Preorder
        preorder = self.bst.preorder_traversal()
        self.assertEqual(len(preorder), 5)

        # Postorder
        postorder = self.bst.postorder_traversal()
        self.assertEqual(len(postorder), 5)

        # Level order
        level_order = self.bst.level_order_traversal()
        self.assertEqual(len(level_order), 5)

    def test_bst_validity(self):
        """Test BST validity checking."""
        # Valid BST
        values = [(8, "eight"), (3, "three"), (10, "ten"), (1, "one"), (6, "six")]
        for key, value in values:
            self.bst.put(key, value)

        self.assertTrue(self.bst.is_valid_bst())

        # Manually corrupt the BST (swap nodes to break ordering)
        if self.bst.root and self.bst.root.left:
            # Swap root value with left child value
            temp = self.bst.root.key
            self.bst.root.key = self.bst.root.left.key
            self.bst.root.left.key = temp

            self.assertFalse(self.bst.is_valid_bst())

    def test_height_and_balance(self):
        """Test height and balance factor calculations."""
        # Empty tree
        self.assertEqual(self.bst.get_height(), 0)

        # Single node
        self.bst.put(5, "five")
        self.assertEqual(self.bst.get_height(), 0)

        # Add more nodes
        self.bst.put(3, "three")
        self.bst.put(7, "seven")
        self.assertEqual(self.bst.get_height(), 1)

        # Add more to create imbalance
        self.bst.put(2, "two")
        self.bst.put(1, "one")  # Creates left-skewed tree

        # Height should be at least 3
        self.assertGreaterEqual(self.bst.get_height(), 3)


class TestBSTAnalysis(unittest.TestCase):
    """Test cases for BST analysis tools."""

    def test_generate_worst_case_bst(self):
        """Test generating worst-case BST."""
        bst = BSTAnalysis.generate_worst_case_bst(5)

        # Should have height 4 (n-1 for n=5)
        self.assertEqual(bst.get_height(), 4)
        self.assertEqual(len(bst), 5)
        self.assertTrue(bst.is_valid_bst())

    def test_generate_best_case_bst(self):
        """Test generating best-case BST."""
        bst = BSTAnalysis.generate_best_case_bst(7)

        # Should be relatively balanced
        height = bst.get_height()
        # For 7 nodes, height should be 2 (log₂(7) ≈ 2.8)
        self.assertLessEqual(height, 3)
        self.assertEqual(len(bst), 7)
        self.assertTrue(bst.is_valid_bst())

    def test_generate_random_bst(self):
        """Test generating random BST."""
        bst = BSTAnalysis.generate_random_bst(10)

        self.assertEqual(len(bst), 10)
        self.assertTrue(bst.is_valid_bst())

        # Check that all keys are present
        for i in range(10):
            self.assertTrue(bst.contains(i))

    def test_benchmark_operations(self):
        """Test benchmarking BST operations."""
        bst = BSTAnalysis.generate_random_bst(100)

        results = BSTAnalysis.benchmark_bst_operations(bst, num_operations=50)

        # Check that results contain expected keys
        self.assertIn("search_time", results)
        self.assertIn("insert_time", results)
        self.assertIn("height", results)
        self.assertIn("size", results)
        self.assertIn("balance_factors", results)

        # Check values are reasonable
        self.assertGreaterEqual(results["search_time"], 0)
        self.assertGreaterEqual(results["insert_time"], 0)
        self.assertEqual(results["size"], 100)

    def test_analyze_bst_shape(self):
        """Test BST shape analysis."""
        # Worst case
        worst_bst = BSTAnalysis.generate_worst_case_bst(10)
        analysis = BSTAnalysis.analyze_bst_shape(worst_bst)

        self.assertEqual(analysis["size"], 10)
        self.assertEqual(analysis["height"], 9)  # n-1
        self.assertFalse(analysis["is_balanced"])

        # Best case
        best_bst = BSTAnalysis.generate_best_case_bst(7)
        analysis = BSTAnalysis.analyze_bst_shape(best_bst)

        self.assertEqual(analysis["size"], 7)
        self.assertLessEqual(analysis["height"], 3)
        self.assertTrue(analysis["is_balanced"])


class TestBSTStress(unittest.TestCase):
    """Stress tests for BST implementation."""

    def test_large_bst_operations(self):
        """Test BST with large number of operations."""
        bst = BinarySearchTree()

        # Insert many values
        num_operations = 1000
        for i in range(num_operations):
            bst.put(i, f"value{i}")

        self.assertEqual(len(bst), num_operations)

        # Verify all values are accessible
        for i in range(num_operations):
            self.assertEqual(bst.get(i), f"value{i}")

        # Test range queries
        range_keys = bst.keys_in_range(100, 200)
        self.assertEqual(len(range_keys), 101)  # 100 to 200 inclusive

        # Test removal
        for i in range(0, num_operations, 2):  # Remove even numbers
            bst.remove(i)

        self.assertEqual(len(bst), num_operations // 2)
        self.assertTrue(bst.is_valid_bst())

    def test_bst_with_duplicates_policy(self):
        """Test BST behavior with duplicate keys (updates values)."""
        bst = BinarySearchTree()

        # Insert same key multiple times with different values
        bst.put(5, "first")
        self.assertEqual(bst.get(5), "first")

        bst.put(5, "second")
        self.assertEqual(bst.get(5), "second")
        self.assertEqual(len(bst), 1)  # Size should remain 1

        bst.put(5, "third")
        self.assertEqual(bst.get(5), "third")
        self.assertEqual(len(bst), 1)

    def test_bst_traversal_correctness(self):
        """Test that all traversals visit all nodes exactly once."""
        bst = BinarySearchTree()

        # Insert values that will create a specific structure
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        for val in values:
            bst.put(val, f"val{val}")

        # All traversals should have same length
        inorder = bst.inorder_traversal()
        preorder = bst.preorder_traversal()
        postorder = bst.postorder_traversal()
        levelorder = bst.level_order_traversal()

        expected_length = len(values)
        self.assertEqual(len(inorder), expected_length)
        self.assertEqual(len(preorder), expected_length)
        self.assertEqual(len(postorder), expected_length)
        self.assertEqual(len(levelorder), expected_length)

        # Inorder should be sorted by key
        inorder_keys = [key for key, _ in inorder]
        self.assertEqual(inorder_keys, sorted(values))


if __name__ == '__main__':
    unittest.main()</content>
<parameter name="filePath">chapter_15_binary_search_trees/tests/test_bst_implementation.py