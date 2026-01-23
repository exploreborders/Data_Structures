"""
Chapter 18 Examples: Balanced Binary Search Trees - AVL Tree Demonstrations

Interactive examples showing AVL tree balancing, rotations, and performance guarantees.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from avl_tree import AVLTree
import random


def demonstrate_basic_avl_operations():
    """Demonstrate basic AVL tree operations."""
    print("=== Basic AVL Tree Operations ===\n")

    tree = AVLTree()

    print("1. Inserting nodes:")
    insertions = [(5, "five"), (3, "three"), (7, "seven"), (2, "two"), (4, "four")]
    for key, value in insertions:
        tree.put(key, value)
        print(
            f"   After inserting {key}: height={tree.get_height()}, valid={tree.is_valid_avl()}"
        )

    print(f"\nTree structure:\n{tree.visualize_tree()}")

    print(f"\n2. Tree properties:")
    print(f"   Size: {len(tree)}")
    print(f"   Height: {tree.get_height()}")
    print(f"   Min key: {tree.min_key()}")
    print(f"   Max key: {tree.max_key()}")
    print(f"   Balance factors: {tree.get_balance_factor_distribution()}")

    print(f"\n3. Inorder traversal: {[key for key, _ in tree.inorder_traversal()]}")


def demonstrate_rotations():
    """Demonstrate different rotation cases."""
    print("\n=== AVL Tree Rotations ===\n")

    # Right-Right (RR) case
    print("1. Right-Right Case (Left Rotation):")
    tree1 = AVLTree()
    tree1.put(5, "five")
    tree1.put(7, "seven")
    print("   Before imbalance:")
    print(f"   {tree1.visualize_tree()}")

    tree1.put(9, "nine")  # Triggers left rotation
    print("   After inserting 9 (triggers left rotation):")
    print(f"   {tree1.visualize_tree()}")
    print(f"   Balance factors: {tree1.get_balance_factor_distribution()}")

    # Left-Left (LL) case
    print("\n2. Left-Left Case (Right Rotation):")
    tree2 = AVLTree()
    tree2.put(9, "nine")
    tree2.put(7, "seven")
    print("   Before imbalance:")
    print(f"   {tree2.visualize_tree()}")

    tree2.put(5, "five")  # Triggers right rotation
    print("   After inserting 5 (triggers right rotation):")
    print(f"   {tree2.visualize_tree()}")
    print(f"   Balance factors: {tree2.get_balance_factor_distribution()}")

    # Left-Right (LR) case
    print("\n3. Left-Right Case (Right-Left Double Rotation):")
    tree3 = AVLTree()
    tree3.put(9, "nine")
    tree3.put(5, "five")
    print("   Before imbalance:")
    print(f"   {tree3.visualize_tree()}")

    tree3.put(7, "seven")  # Triggers LR rotation (right then left)
    print("   After inserting 7 (triggers LR double rotation):")
    print(f"   {tree3.visualize_tree()}")
    print(f"   Balance factors: {tree3.get_balance_factor_distribution()}")


def demonstrate_balance_maintenance():
    """Show how AVL trees maintain balance during various operations."""
    print("\n=== Balance Maintenance During Operations ===\n")

    tree = AVLTree()

    print("Building tree with 15 nodes (worst-case insertion order):")
    for i in range(15):
        tree.put(i, f"value{i}")
        if i % 5 == 0:  # Show progress
            print(
                f"   After {i + 1} insertions: height={tree.get_height()}, valid={tree.is_valid_avl()}"
            )

    print(f"\nFinal tree height: {tree.get_height()} (theoretical max: ~5)")
    print(f"All balance factors: {tree.get_balance_factor_distribution()}")

    print("\nRemoving nodes to test rebalancing:")
    for i in [7, 8, 9, 10]:  # Remove some nodes
        tree.remove(i)
        print(
            f"   After removing {i}: height={tree.get_height()}, valid={tree.is_valid_avl()}"
        )

    print(f"\nFinal balance factors: {tree.get_balance_factor_distribution()}")


def compare_avl_vs_unbalanced():
    """Compare AVL tree performance vs unbalanced BST."""
    print("\n=== AVL vs Unbalanced BST Performance ===\n")

    # For demonstration, we'll simulate BST behavior
    # In a real implementation, you'd import the BST from chapter 17
    size = 100

    # Create AVL tree
    avl_tree = AVLTree()
    for i in range(size):
        avl_tree.put(i, f"value{i}")

    print(f"Tree size: {size}")
    print(f"AVL tree height: {avl_tree.get_height()}")
    print(".1f")
    print(f"AVL tree valid: {avl_tree.is_valid_avl()}")

    # Test search performance
    import time

    test_keys = list(range(0, size, 10))  # Every 10th key

    # AVL search
    start = time.time()
    for key in test_keys:
        avl_tree.contains(key)
    avl_time = time.time() - start

    print(f"\nSearch performance ({len(test_keys)} operations):")
    print(".6f")


def demonstrate_tree_visualization():
    """Show different tree visualization examples."""
    print("\n=== Tree Visualization Examples ===\n")

    # Empty tree
    empty_tree = AVLTree()
    print("Empty tree:")
    print(empty_tree.visualize_tree())
    print()

    # Single node
    single_tree = AVLTree()
    single_tree.put(5, "five")
    print("Single node:")
    print(single_tree.visualize_tree())
    print()

    # Balanced tree
    balanced_tree = AVLTree()
    balanced_tree.put(5, "five")
    balanced_tree.put(3, "three")
    balanced_tree.put(7, "seven")
    print("Balanced tree:")
    print(balanced_tree.visualize_tree())
    print()

    # After rotation
    rotated_tree = AVLTree()
    rotated_tree.put(5, "five")
    rotated_tree.put(3, "three")
    rotated_tree.put(7, "seven")
    rotated_tree.put(2, "two")
    rotated_tree.put(9, "nine")
    print("After rotation:")
    print(rotated_tree.visualize_tree())
    print()


def demonstrate_edge_cases():
    """Test various edge cases."""
    print("\n=== Edge Cases and Stress Tests ===\n")

    # Large tree test
    print("1. Large tree (1000 nodes):")
    large_tree = AVLTree()
    for i in range(1000):
        large_tree.put(i, f"value{i}")

    print(f"   Size: {len(large_tree)}")
    print(f"   Height: {large_tree.get_height()}")
    print(f"   Valid AVL: {large_tree.is_valid_avl()}")
    print(
        f"   Max balance factor magnitude: {max(abs(bf) for bf in large_tree.get_balance_factor_distribution())}"
    )

    # Random operations
    print("\n2. Random operations test:")
    random_tree = AVLTree()
    operations = []

    for _ in range(50):
        key = random.randint(1, 100)
        if random.random() < 0.7:  # 70% inserts
            random_tree.put(key, f"value{key}")
            operations.append(f"insert {key}")
        elif len(random_tree) > 0:
            try:
                random_tree.remove(key)
                operations.append(f"remove {key}")
            except KeyError:
                operations.append(f"remove {key} (not found)")

    print(f"   Final size: {len(random_tree)}")
    print(f"   Still valid AVL: {random_tree.is_valid_avl()}")
    print(f"   Sample operations: {operations[:10]}...")


if __name__ == "__main__":
    demonstrate_basic_avl_operations()
    demonstrate_rotations()
    demonstrate_balance_maintenance()
    compare_avl_vs_unbalanced()
    demonstrate_tree_visualization()
    demonstrate_edge_cases()

    print("\n=== AVL Tree Demonstration Complete ===")
    print("AVL trees maintain O(log n) performance through automatic balancing!")
    print("Each operation ensures |balance factor| ≤ 1 for all nodes.")
