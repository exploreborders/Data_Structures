"""
Tests for Chapter 14: Trees - Hierarchical Data Structures
"""

import unittest
from typing import List, Optional

# Add the code directory to the path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from tree_implementations import (
    TreeNode,
    BinaryTree,
    BinarySearchTree,
    AVLTree,
    Heap,
    TreeAnalysis
)


class TestTreeNode(unittest.TestCase):
    """Test cases for TreeNode class."""

    def test_tree_node_creation(self):
        """Test basic TreeNode creation."""
        node = TreeNode(5)
        self.assertEqual(node.value, 5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        self.assertEqual(node.height, 1)

    def test_tree_node_is_leaf(self):
        """Test leaf node detection."""
        leaf = TreeNode(1)
        self.assertTrue(leaf.is_leaf())

        internal = TreeNode(2)
        internal.left = TreeNode(1)
        self.assertFalse(internal.is_leaf())


class TestBinaryTree(unittest.TestCase):
    """Test cases for BinaryTree class."""

    def setUp(self):
        """Set up test tree."""
        # Create a simple tree:
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)

        self.tree = BinaryTree(self.root)

    def test_empty_tree(self):
        """Test empty tree operations."""
        empty_tree = BinaryTree()
        self.assertTrue(empty_tree.is_empty())
        self.assertEqual(empty_tree.get_height(), 0)
        self.assertEqual(empty_tree.inorder_traversal(), [])
        self.assertEqual(empty_tree.level_order_traversal(), [])

    def test_tree_height(self):
        """Test tree height calculation."""
        self.assertEqual(self.tree.get_height(), 2)

        # Single node tree
        single_tree = BinaryTree(TreeNode(1))
        self.assertEqual(single_tree.get_height(), 0)

    def test_traversals(self):
        """Test all tree traversals."""
        # Inorder: Left-Root-Right
        expected_inorder = [4, 2, 5, 1, 3]
        self.assertEqual(self.tree.inorder_traversal(), expected_inorder)

        # Preorder: Root-Left-Right
        expected_preorder = [1, 2, 4, 5, 3]
        self.assertEqual(self.tree.preorder_traversal(), expected_preorder)

        # Postorder: Left-Right-Root
        expected_postorder = [4, 5, 2, 3, 1]
        self.assertEqual(self.tree.postorder_traversal(), expected_postorder)

        # Level order
        expected_level = [1, 2, 3, 4, 5]
        self.assertEqual(self.tree.level_order_traversal(), expected_level)

    def test_iterative_traversals(self):
        """Test iterative traversal implementations."""
        # Inorder iterative
        expected_inorder = [4, 2, 5, 1, 3]
        self.assertEqual(self.tree.inorder_iterative(), expected_inorder)

        # Preorder iterative
        expected_preorder = [1, 2, 4, 5, 3]
        self.assertEqual(self.tree.preorder_iterative(), expected_preorder)

    def test_node_counting(self):
        """Test node counting operations."""
        self.assertEqual(self.tree.count_nodes(), 5)
        self.assertEqual(self.tree.count_leaves(), 3)  # 4, 5, 3 are leaves

    def test_find_max(self):
        """Test finding maximum value."""
        self.assertEqual(self.tree.find_max(), 5)

    def test_mirror(self):
        """Test tree mirroring."""
        original_inorder = self.tree.inorder_traversal()
        self.tree.mirror()

        # After mirroring, the structure changes but inorder should be reversed
        # Actually, inorder of mirrored tree should be the reverse of original inorder
        mirrored_inorder = self.tree.inorder_traversal()
        self.assertEqual(mirrored_inorder, list(reversed(original_inorder)))


class TestBinarySearchTree(unittest.TestCase):
    """Test cases for BinarySearchTree class."""

    def setUp(self):
        """Set up test BST."""
        self.bst = BinarySearchTree()

    def test_empty_bst(self):
        """Test empty BST operations."""
        self.assertTrue(self.bst.is_empty())
        self.assertFalse(self.bst.search(5))

        with self.assertRaises(ValueError):
            self.bst.find_min()

        with self.assertRaises(ValueError):
            self.bst.find_max()

    def test_insert_and_search(self):
        """Test insert and search operations."""
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

        for val in values:
            self.bst.insert(val)

        # All values should be searchable
        for val in values:
            self.assertTrue(self.bst.search(val))

        # Non-existing values
        self.assertFalse(self.bst.search(0))
        self.assertFalse(self.bst.search(20))

    def test_bst_properties(self):
        """Test BST ordering properties."""
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        for val in values:
            self.bst.insert(val)

        # Inorder should be sorted
        inorder = self.bst.inorder_traversal()
        self.assertEqual(inorder, sorted(values))

        # BST validation
        self.assertTrue(self.bst.is_valid_bst())

    def test_find_min_max(self):
        """Test finding minimum and maximum values."""
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        for val in values:
            self.bst.insert(val)

        self.assertEqual(self.bst.find_min(), 1)
        self.assertEqual(self.bst.find_max(), 14)

    def test_delete(self):
        """Test delete operations."""
        values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        for val in values:
            self.bst.insert(val)

        original_size = self.bst.count_nodes()

        # Delete leaf node
        self.bst.delete(4)
        self.assertFalse(self.bst.search(4))
        self.assertEqual(self.bst.count_nodes(), original_size - 1)
        self.assertTrue(self.bst.is_valid_bst())

        # Delete node with one child
        self.bst.delete(1)
        self.assertFalse(self.bst.search(1))
        self.assertEqual(self.bst.count_nodes(), original_size - 2)
        self.assertTrue(self.bst.is_valid_bst())

        # Delete node with two children
        self.bst.delete(3)
        self.assertFalse(self.bst.search(3))
        self.assertEqual(self.bst.count_nodes(), original_size - 3)
        self.assertTrue(self.bst.is_valid_bst())

    def test_delete_nonexistent(self):
        """Test deleting non-existent values."""
        self.bst.insert(5)
        self.bst.delete(10)  # Should not crash
        self.assertTrue(self.bst.search(5))


class TestAVLTree(unittest.TestCase):
    """Test cases for AVLTree class."""

    def setUp(self):
        """Set up test AVL tree."""
        self.avl = AVLTree()

    def test_avl_balance(self):
        """Test AVL tree maintains balance."""
        # Insert values that would unbalance a regular BST
        values = [1, 2, 3, 4, 5, 6, 7]  # Would create a skewed BST

        for val in values:
            self.avl.insert(val)

        # Should be balanced
        self.assertTrue(TreeAnalysis.is_balanced_bst(self.avl.root))

        # Height should be O(log n)
        height = self.avl.get_height()
        expected_max_height = 2 * (len(values).bit_length())  # Rough estimate
        self.assertLessEqual(height, expected_max_height)

    def test_avl_rotations(self):
        """Test various rotation scenarios."""
        # Left-Left case
        self.avl.insert(30)
        self.avl.insert(20)
        self.avl.insert(10)  # Should trigger right rotation

        self.assertTrue(TreeAnalysis.is_balanced_bst(self.avl.root))
        self.assertTrue(self.avl.is_valid_bst())

        # Right-Right case
        self.avl.insert(40)
        self.avl.insert(50)  # Should trigger left rotation

        self.assertTrue(TreeAnalysis.is_balanced_bst(self.avl.root))
        self.assertTrue(self.avl.is_valid_bst())

    def test_avl_delete_balance(self):
        """Test that deletion maintains balance."""
        values = [10, 20, 30, 40, 50, 25]
        for val in values:
            self.avl.insert(val)

        # Delete nodes and check balance is maintained
        self.avl.delete(20)
        self.assertTrue(TreeAnalysis.is_balanced_bst(self.avl.root))
        self.assertTrue(self.avl.is_valid_bst())

        self.avl.delete(30)
        self.assertTrue(TreeAnalysis.is_balanced_bst(self.avl.root))
        self.assertTrue(self.avl.is_valid_bst())


class TestHeap(unittest.TestCase):
    """Test cases for Heap class."""

    def test_empty_heap(self):
        """Test empty heap operations."""
        heap = Heap()
        self.assertTrue(heap.is_empty())
        self.assertEqual(heap.size(), 0)

        with self.assertRaises(IndexError):
            heap.peek()

        with self.assertRaises(IndexError):
            heap.extract_top()

    def test_max_heap_operations(self):
        """Test max-heap operations."""
        heap = Heap(max_heap=True)

        # Insert values
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        for val in values:
            heap.insert(val)

        self.assertEqual(heap.size(), len(values))
        self.assertEqual(heap.peek(), 9)  # Max element

        # Extract elements in descending order
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        self.assertEqual(extracted, [9, 6, 5, 4, 3, 2, 1, 1])

    def test_min_heap_operations(self):
        """Test min-heap operations."""
        heap = Heap(max_heap=False)

        # Insert values
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        for val in values:
            heap.insert(val)

        self.assertEqual(heap.peek(), 1)  # Min element

        # Extract elements in ascending order
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        self.assertEqual(extracted, [1, 1, 2, 3, 4, 5, 6, 9])

    def test_heapify(self):
        """Test heapify operation."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        # Max heap
        max_heap = Heap.heapify(arr, max_heap=True)
        self.assertEqual(max_heap.peek(), 9)
        self.assertEqual(max_heap.size(), len(arr))

        # Min heap
        min_heap = Heap.heapify(arr, max_heap=False)
        self.assertEqual(min_heap.peek(), 1)
        self.assertEqual(min_heap.size(), len(arr))

    def test_heap_sort(self):
        """Test heap sort."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        # Ascending sort (using max-heap)
        sorted_asc = Heap.heap_sort(arr, ascending=True)
        self.assertEqual(sorted_asc, [1, 1, 2, 3, 4, 5, 6, 9])

        # Descending sort (using min-heap)
        sorted_desc = Heap.heap_sort(arr, ascending=False)
        self.assertEqual(sorted_desc, [9, 6, 5, 4, 3, 2, 1, 1])


class TestTreeAnalysis(unittest.TestCase):
    """Test cases for tree analysis functions."""

    def test_is_balanced_bst(self):
        """Test balanced BST detection."""
        # Create balanced BST
        bst = BinarySearchTree()
        values = [4, 2, 6, 1, 3, 5, 7]
        for val in values:
            bst.insert(val)

        self.assertTrue(TreeAnalysis.is_balanced_bst(bst.root))

        # Create unbalanced BST
        skewed_bst = BinarySearchTree()
        for val in [1, 2, 3, 4, 5, 6, 7]:  # Creates skewed tree
            skewed_bst.insert(val)

        self.assertFalse(TreeAnalysis.is_balanced_bst(skewed_bst.root))

    def test_tree_diameter(self):
        """Test tree diameter calculation."""
        # Create test tree:
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
        #    /
        #   6

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(6)

        diameter = TreeAnalysis.tree_diameter(root)
        self.assertEqual(diameter, 5)  # Path 6-5-2-1-3

    def test_build_tree_from_traversals(self):
        """Test building tree from inorder and preorder traversals."""
        inorder = [4, 2, 5, 1, 3]
        preorder = [1, 2, 4, 5, 3]

        root = TreeAnalysis.build_tree_from_traversals(inorder, preorder)

        self.assertEqual(root.value, 1)
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 3)
        self.assertEqual(root.left.left.value, 4)
        self.assertEqual(root.left.right.value, 5)

        # Verify inorder traversal matches
        tree = BinaryTree(root)
        self.assertEqual(tree.inorder_traversal(), inorder)


class TestTreeStress(unittest.TestCase):
    """Stress tests for tree implementations."""

    def test_bst_large_insertions(self):
        """Test BST with many insertions."""
        bst = BinarySearchTree()

        # Insert many values
        num_values = 1000
        values = list(range(num_values))

        for val in values:
            bst.insert(val)

        # Verify all values are present
        for val in values:
            self.assertTrue(bst.search(val))

        # Verify inorder traversal is sorted
        inorder = bst.inorder_traversal()
        self.assertEqual(inorder, values)

    def test_avl_large_insertions(self):
        """Test AVL tree with many insertions."""
        avl = AVLTree()

        # Insert values that would create imbalance
        num_values = 500
        values = list(range(num_values))

        for val in values:
            avl.insert(val)

        # Should remain balanced
        self.assertTrue(TreeAnalysis.is_balanced_bst(avl.root))

        # Should be valid BST
        self.assertTrue(avl.is_valid_bst())

        # Height should be logarithmic
        height = avl.get_height()
        expected_max_height = 2 * (num_values.bit_length())
        self.assertLessEqual(height, expected_max_height)

    def test_heap_large_operations(self):
        """Test heap with many operations."""
        heap = Heap(max_heap=True)

        # Insert many values
        num_values = 1000
        values = list(range(num_values))

        for val in values:
            heap.insert(val)

        self.assertEqual(heap.size(), num_values)

        # Extract all values - should be in descending order
        extracted = []
        while not heap.is_empty():
            extracted.append(heap.extract_top())

        self.assertEqual(extracted, list(range(num_values - 1, -1, -1)))


if __name__ == '__main__':
    unittest.main()</content>
<parameter name="filePath">chapter_14_trees/tests/test_tree_implementations.py