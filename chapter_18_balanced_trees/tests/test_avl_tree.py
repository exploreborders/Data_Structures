"""
Tests for Chapter 18: Balanced Binary Search Trees - AVL Tree Implementation

Comprehensive tests covering AVL tree operations, balance maintenance, and edge cases.
"""

import pytest
from chapter_18_balanced_trees.code.avl_tree import AVLTree, AVLNode


class TestAVLNode:
    """Test AVLNode functionality."""

    def test_node_creation(self):
        """Test basic node creation."""
        node = AVLNode(5, "five")
        assert node.key == 5
        assert node.value == "five"
        assert node.height == 0
        assert node.left is None
        assert node.right is None

    def test_balance_factor_leaf(self):
        """Test balance factor for leaf node."""
        node = AVLNode(5, "five")
        assert node.get_balance_factor() == 0

    def test_balance_factor_with_children(self):
        """Test balance factor calculation with children."""
        node = AVLNode(5, "five")

        # Add left child
        node.left = AVLNode(3, "three")
        node.update_height()
        assert node.get_balance_factor() == -1

        # Add right child
        node.right = AVLNode(7, "seven")
        node.update_height()
        assert node.get_balance_factor() == 0

        # Make right subtree taller
        node.right.right = AVLNode(9, "nine")
        node.right.update_height()
        node.update_height()
        assert node.get_balance_factor() == 1

    def test_is_leaf(self):
        """Test leaf detection."""
        node = AVLNode(5, "five")
        assert node.is_leaf()

        node.left = AVLNode(3, "three")
        assert not node.is_leaf()

    def test_has_one_child(self):
        """Test single child detection."""
        node = AVLNode(5, "five")

        # No children
        assert not node.has_one_child()

        # One child
        node.left = AVLNode(3, "three")
        assert node.has_one_child()

        # Two children
        node.right = AVLNode(7, "seven")
        assert not node.has_one_child()

    def test_has_two_children(self):
        """Test two children detection."""
        node = AVLNode(5, "five")

        # No children
        assert not node.has_two_children()

        # One child
        node.left = AVLNode(3, "three")
        assert not node.has_two_children()

        # Two children
        node.right = AVLNode(7, "seven")
        assert node.has_two_children()


class TestAVLTree:
    """Test AVLTree functionality."""

    def test_empty_tree(self):
        """Test empty tree operations."""
        tree = AVLTree()
        assert len(tree) == 0
        assert tree.is_empty()
        assert tree.get_height() == 0

    def test_single_insertion(self):
        """Test inserting a single node."""
        tree = AVLTree()
        tree.put(5, "five")

        assert len(tree) == 1
        assert not tree.is_empty()
        assert tree.contains(5)
        assert tree.get(5) == "five"
        assert tree.get_height() == 0

    def test_multiple_insertions_balanced(self):
        """Test multiple insertions that stay balanced."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")

        assert len(tree) == 3
        assert tree.get_height() == 1
        assert tree.is_valid_avl()

    def test_left_rotation_rr_case(self):
        """Test right-right case requiring left rotation."""
        tree = AVLTree()

        # Create imbalance that needs left rotation
        tree.put(5, "five")
        tree.put(7, "seven")
        tree.put(9, "nine")  # This should trigger left rotation

        assert tree.is_valid_avl()
        assert tree.get_height() == 1
        assert tree.contains(5)
        assert tree.contains(7)
        assert tree.contains(9)

    def test_right_rotation_ll_case(self):
        """Test left-left case requiring right rotation."""
        tree = AVLTree()

        # Create imbalance that needs right rotation
        tree.put(9, "nine")
        tree.put(7, "seven")
        tree.put(5, "five")  # This should trigger right rotation

        assert tree.is_valid_avl()
        assert tree.get_height() == 1

    def test_left_right_rotation_lr_case(self):
        """Test left-right case requiring double rotation."""
        tree = AVLTree()

        # Create LR imbalance
        tree.put(9, "nine")
        tree.put(5, "five")
        tree.put(7, "seven")  # This creates LR case

        assert tree.is_valid_avl()
        assert tree.get_height() == 1

    def test_right_left_rotation_rl_case(self):
        """Test right-left case requiring double rotation."""
        tree = AVLTree()

        # Create RL imbalance
        tree.put(5, "five")
        tree.put(9, "nine")
        tree.put(7, "seven")  # This creates RL case

        assert tree.is_valid_avl()
        assert tree.get_height() == 1

    def test_update_existing_key(self):
        """Test updating value for existing key."""
        tree = AVLTree()
        tree.put(5, "five")
        assert tree.get(5) == "five"

        tree.put(5, "FIVE")
        assert tree.get(5) == "FIVE"
        assert len(tree) == 1

    def test_removal_leaf_node(self):
        """Test removing a leaf node."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")

        tree.remove(3)
        assert len(tree) == 2
        assert not tree.contains(3)
        assert tree.contains(5)
        assert tree.contains(7)
        assert tree.is_valid_avl()

    def test_removal_node_with_one_child(self):
        """Test removing a node with one child."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(4, "four")  # 3 now has right child

        tree.remove(3)
        assert len(tree) == 2
        assert not tree.contains(3)
        assert tree.contains(4)
        assert tree.is_valid_avl()

    def test_removal_node_with_two_children(self):
        """Test removing a node with two children."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")
        tree.put(2, "two")
        tree.put(4, "four")

        tree.remove(3)  # Should use successor (4)
        assert len(tree) == 4
        assert not tree.contains(3)
        assert tree.contains(4)
        assert tree.is_valid_avl()

    def test_min_max_keys(self):
        """Test finding minimum and maximum keys."""
        tree = AVLTree()
        keys = [5, 3, 7, 2, 4, 6, 8]
        for key in keys:
            tree.put(key, f"value{key}")

        assert tree.min_key() == 2
        assert tree.max_key() == 8

    def test_inorder_traversal(self):
        """Test inorder traversal maintains sorted order."""
        tree = AVLTree()
        keys = [5, 3, 7, 2, 4, 6, 8]
        for key in keys:
            tree.put(key, f"value{key}")

        traversal = tree.inorder_traversal()
        keys_from_traversal = [key for key, value in traversal]

        assert keys_from_traversal == sorted(keys)

    def test_balance_factors_after_operations(self):
        """Test that balance factors stay within AVL bounds."""
        tree = AVLTree()

        # Insert many nodes
        for i in range(20):
            tree.put(i, f"value{i}")

        balance_factors = tree.get_balance_factor_distribution()

        # All balance factors should be between -1 and 1
        assert all(-1 <= bf <= 1 for bf in balance_factors)
        assert tree.is_valid_avl()

    def test_tree_height_bounds(self):
        """Test that AVL tree maintains logarithmic height."""
        import math

        tree = AVLTree()
        n = 100

        for i in range(n):
            tree.put(i, f"value{i}")

        height = tree.get_height()
        theoretical_max = int(1.44 * math.log2(n + 1))

        assert height <= theoretical_max
        assert tree.is_valid_avl()

    def test_worst_case_insertion_order(self):
        """Test that even worst-case insertion order stays balanced."""
        tree = AVLTree()

        # Insert in sorted order (worst case for regular BST)
        for i in range(20):
            tree.put(i, f"value{i}")

        # Should still be balanced
        assert tree.is_valid_avl()
        balance_factors = tree.get_balance_factor_distribution()
        assert all(-1 <= bf <= 1 for bf in balance_factors)

        # Height should be logarithmic
        height = tree.get_height()
        assert height <= 5  # log2(20) * 1.44 ≈ 4.4

    def test_key_error_handling(self):
        """Test proper error handling for missing keys."""
        tree = AVLTree()

        with pytest.raises(KeyError):
            tree.get(5)

        with pytest.raises(KeyError):
            tree.remove(5)

    def test_empty_tree_edge_cases(self):
        """Test edge cases on empty tree."""
        tree = AVLTree()

        with pytest.raises(ValueError):
            tree.min_key()

        with pytest.raises(ValueError):
            tree.max_key()

    def test_visualization(self):
        """Test tree visualization."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")

        visualization = tree.visualize_tree()
        assert "5" in visualization
        assert "3" in visualization
        assert "7" in visualization
        assert "h=" in visualization  # Height information
        assert "bf=" in visualization  # Balance factor information

    def test_tree_integrity_after_many_operations(self):
        """Test tree integrity after many insertions and deletions."""
        tree = AVLTree()

        # Insert many items
        for i in range(50):
            tree.put(i, f"value{i}")

        assert tree.is_valid_avl()

        # Remove half
        for i in range(0, 50, 2):
            tree.remove(i)

        assert tree.is_valid_avl()

        # Insert more
        for i in range(50, 75):
            tree.put(i, f"value{i}")

        assert tree.is_valid_avl()

        # Verify all remaining items are present
        for i in range(1, 75, 2):  # Odd numbers from original + new numbers
            assert tree.contains(i)


class TestAVLAnalysis:
    """Test analysis and utility functions."""

    def test_balance_factor_distribution(self):
        """Test balance factor distribution collection."""
        tree = AVLTree()
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")

        factors = tree.get_balance_factor_distribution()
        assert len(factors) == 3
        assert all(-1 <= bf <= 1 for bf in factors)

    def test_avl_validation(self):
        """Test AVL tree validation."""
        tree = AVLTree()

        # Valid AVL tree
        tree.put(5, "five")
        tree.put(3, "three")
        tree.put(7, "seven")
        assert tree.is_valid_avl()

        # Manually create invalid tree (would be caught by our implementation)
        # But test that valid trees pass validation
        assert tree.is_valid_avl()
