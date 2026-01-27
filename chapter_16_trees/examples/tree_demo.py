#!/usr/bin/env python3
"""
Chapter 14: Trees - Interactive Examples

This script demonstrates tree data structures with interactive visualizations,
traversal demonstrations, and performance comparisons.
"""

import sys
import os
from typing import List, Optional, Any

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from tree_implementations import (
    TreeNode,
    BinaryTree,
    BinarySearchTree,
    AVLTree,
    Heap,
    TreeAnalysis,
)


def print_tree_visualization(
    root: Optional[TreeNode], title: str = "Tree Visualization"
):
    """Simple text-based tree visualization."""
    print(f"\n{title}:")

    def print_tree_helper(
        node: Optional[TreeNode], prefix: str = "", is_left: bool = True
    ):
        if node:
            print_tree_helper(
                node.right, prefix + ("│   " if is_left else "    "), False
            )
            print(f"{prefix}{'└── ' if is_left else '┌── '}{node.value}")
            print_tree_helper(node.left, prefix + ("    " if is_left else "│   "), True)

    if root:
        print_tree_helper(root)
    else:
        print("  (empty tree)")


def demonstrate_tree_traversals():
    """Demonstrate different tree traversal algorithms."""
    print("TREE TRAVERSAL ALGORITHMS")
    print("=" * 50)

    # Create a sample tree:
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    #        /
    #       7

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)

    tree = BinaryTree(root)

    print_tree_visualization(root, "Sample Tree Structure")

    print("\nTraversal Results:")

    print("Inorder (Left-Root-Right):   ", end="")
    print(" ".join(map(str, tree.inorder_traversal())))

    print("Preorder (Root-Left-Right):  ", end="")
    print(" ".join(map(str, tree.preorder_traversal())))

    print("Postorder (Left-Right-Root): ", end="")
    print(" ".join(map(str, tree.postorder_traversal())))

    print("Level-order (BFS):           ", end="")
    print(" ".join(map(str, tree.level_order_traversal())))

    print("\nIterative Traversals:")
    print("Inorder iterative:  ", end="")
    print(" ".join(map(str, tree.inorder_iterative())))

    print("Preorder iterative: ", end="")
    print(" ".join(map(str, tree.preorder_iterative())))


def demonstrate_bst_operations():
    """Demonstrate BST operations with visualization."""
    print("\n\nBINARY SEARCH TREE OPERATIONS")
    print("=" * 50)

    bst = BinarySearchTree()

    print("Building BST by inserting: 8, 3, 10, 1, 6, 14, 4, 7, 13")
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    for val in values:
        bst.insert(val)
        print(f"After inserting {val}:")
        print_tree_visualization(bst.root)

    print("\nBST Properties:")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    print(f"Height: {bst.get_height()}")
    print(f"Min value: {bst.find_min()}")
    print(f"Max value: {bst.find_max()}")

    print(f"\nInorder traversal (should be sorted): {bst.inorder_traversal()}")

    print("\nDeleting node 3 (has two children):")
    bst.delete(3)
    print_tree_visualization(bst.root)
    print(f"Still valid BST: {bst.is_valid_bst()}")


def demonstrate_avl_balance():
    """Demonstrate AVL tree self-balancing."""
    print("\n\nAVL TREE SELF-BALANCING")
    print("=" * 50)

    print("Inserting values that would unbalance a regular BST: 1, 2, 3, 4, 5, 6")
    print("AVL tree automatically performs rotations to maintain balance.")

    avl = AVLTree()

    values = [1, 2, 3, 4, 5, 6]
    for val in values:
        print(f"\nInserting {val}:")
        avl.insert(val)
        print_tree_visualization(avl.root)
        print(
            f"Height: {avl.get_height()}, Balanced: {TreeAnalysis.is_balanced_bst(avl.root)}"
        )

    print(f"\nFinal tree - Height: {avl.get_height()}")
    print(f"Balanced: {TreeAnalysis.is_balanced_bst(avl.root)}")
    print(f"Valid BST: {avl.is_valid_bst()}")


def demonstrate_heap_operations():
    """Demonstrate heap operations."""
    print("\n\nHEAP OPERATIONS")
    print("=" * 50)

    print("Max-Heap Operations:")

    heap = Heap(max_heap=True)
    values = [3, 1, 4, 1, 5, 9, 2, 6]

    print(f"Inserting values: {values}")
    for val in values:
        heap.insert(val)
        print(f"After inserting {val}: heap = {heap.heap}")

    print(f"\nHeap array: {heap.heap}")
    print(f"Size: {heap.size()}")
    print(f"Max element (peek): {heap.peek()}")

    print("\nExtracting elements (in max-first order):")
    while not heap.is_empty():
        extracted = heap.extract_top()
        print(f"Extracted: {extracted}, Remaining: {heap.heap}")

    print("\n" + "=" * 50)
    print("Min-Heap Operations:")

    min_heap = Heap(max_heap=False)
    for val in values:
        min_heap.insert(val)

    print(f"Min-heap array: {min_heap.heap}")
    print(f"Min element (peek): {min_heap.peek()}")

    print("Extracting elements (in min-first order):")
    while not min_heap.is_empty():
        extracted = min_heap.extract_top()
        print(f"Extracted: {extracted}, Remaining: {min_heap.heap}")


def demonstrate_heap_sort():
    """Demonstrate heap sort algorithm."""
    print("\n\nHEAP SORT DEMONSTRATION")
    print("=" * 50)

    arr = [64, 34, 25, 12, 22, 11, 90, 45, 72, 18]
    print(f"Original array: {arr}")

    # Ascending sort
    sorted_asc = Heap.heap_sort(arr.copy(), ascending=True)
    print(f"Ascending sort:  {sorted_asc}")

    # Descending sort
    sorted_desc = Heap.heap_sort(arr.copy(), ascending=False)
    print(f"Descending sort: {sorted_desc}")

    # Compare with Python's built-in sort
    python_sorted = sorted(arr)
    print(f"Python sorted(): {python_sorted}")
    print(f"Matches ascending: {sorted_asc == python_sorted}")


def demonstrate_tree_analysis():
    """Demonstrate tree analysis functions."""
    print("\n\nTREE ANALYSIS FUNCTIONS")
    print("=" * 50)

    # Create a complex tree for analysis
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)

    tree = BinaryTree(root)

    print_tree_visualization(root, "Analysis Tree")

    print("Tree Statistics:")
    print(f"Height: {tree.get_height()}")
    print(f"Total nodes: {tree.count_nodes()}")
    print(f"Leaf nodes: {tree.count_leaves()}")
    print(f"Maximum value: {tree.find_max()}")

    print(f"Diameter (longest path): {TreeAnalysis.tree_diameter(root)}")

    bst = BinarySearchTree()
    for val in [4, 2, 6, 1, 3, 5, 7]:
        bst.insert(val)

    print(f"\nBST Balance Check:")
    print(f"Is balanced: {TreeAnalysis.is_balanced_bst(bst.root)}")

    # Build tree from traversals
    inorder = [4, 2, 5, 1, 3]
    preorder = [1, 2, 4, 5, 3]

    print(f"\nBuilding tree from traversals:")
    print(f"Inorder:  {inorder}")
    print(f"Preorder: {preorder}")

    reconstructed = TreeAnalysis.build_tree_from_traversals(inorder, preorder)
    reconstructed_tree = BinaryTree(reconstructed)

    print(f"Reconstructed inorder:  {reconstructed_tree.inorder_traversal()}")
    print(f"Reconstructed preorder: {reconstructed_tree.preorder_traversal()}")


def performance_comparison():
    """Compare performance of different tree operations."""
    print("\n\nPERFORMANCE COMPARISON")
    print("=" * 50)

    import time

    sizes = [1000, 5000]

    for size in sizes:
        print(f"\nTesting with {size} elements:")
        # Generate test data
        if size == 1000:
            # For large sizes, use random data to avoid worst-case recursion
            import random

            values = list(range(size))
            random.shuffle(values)
            search_values = [i * (size // 10) for i in range(10)]  # Every 10th value
        else:
            values = list(range(size))
            search_values = [i * (size // 10) for i in range(10)]  # Every 10th value

        # BST Performance
        bst = BinarySearchTree()
        start_time = time.time()
        try:
            for val in values:
                bst.insert(val)
            bst_insert_time = time.time() - start_time
            start_time = time.time()
            for val in search_values:
                bst.search(val)
                bst_search_time = time.time() - start_time
        except RecursionError:
            print(f"BST insertion failed due to recursion depth limit at size {size}")
            bst_insert_time = None
            bst_search_time = None
        # AVL Performance
        avl = AVLTree()
        start_time = time.time()
        for val in values:
            avl.insert(val)
            avl_insert_time = time.time() - start_time
        start_time = time.time()
        for val in search_values:
            avl.search(val)
            avl_search_time = time.time() - start_time

        print("Implementation | Insert Time | Search Time | Height | Balanced")
        print("---------------|-------------|-------------|--------|----------")
        print(f"AVL provides guaranteed balance (O(log n)) vs BST's average case.")


def interactive_tree_builder():
    """Interactive tree construction and exploration."""
    print("\n\nINTERACTIVE TREE BUILDER")
    print("=" * 50)

    tree_type = input("Choose tree type (bst, avl, binary): ").strip().lower()

    if tree_type == "bst":
        tree = BinarySearchTree()
        tree_name = "Binary Search Tree"
    elif tree_type == "avl":
        tree = AVLTree()
        tree_name = "AVL Tree"
    elif tree_type == "binary":
        tree = BinaryTree()
        tree_name = "Binary Tree"
        # For binary tree, we'll build manually
        root = None
    else:
        print("Invalid choice. Using BST.")
        tree = BinarySearchTree()
        tree_name = "Binary Search Tree"

    print(f"Building a {tree_name}")
    print("Commands:")
    print("  insert <value>     - Insert value (BST/AVL only)")
    print("  delete <value>     - Delete value (BST/AVL only)")
    print("  search <value>     - Search for value (BST/AVL only)")
    print("  traversals         - Show all traversals")
    print("  visualize          - Show tree structure")
    print("  stats              - Show tree statistics")
    print("  quit               - Exit")

    while True:
        try:
            command = input("\nCommand: ").strip().split()
            if not command:
                continue

            cmd = command[0].lower()

            if cmd == "quit":
                break
            elif cmd == "insert" and len(command) == 2 and tree_type in ["bst", "avl"]:
                value = int(command[1])
                tree.insert(value)
                print(f"Inserted {value}")
            elif cmd == "delete" and len(command) == 2 and tree_type in ["bst", "avl"]:
                value = int(command[1])
                tree.delete(value)
                print(f"Deleted {value}")
            elif cmd == "search" and len(command) == 2 and tree_type in ["bst", "avl"]:
                value = int(command[1])
                found = tree.search(value)
                print(f"Value {value} {'found' if found else 'not found'}")
            elif cmd == "traversals":
                print("Inorder:   ", tree.inorder_traversal())
                print("Preorder:  ", tree.preorder_traversal())
                print("Postorder: ", tree.postorder_traversal())
                print("Level:     ", tree.level_order_traversal())
            elif cmd == "visualize":
                print_tree_visualization(tree.root)
            elif cmd == "stats":
                print(f"Height: {tree.get_height()}")
                print(f"Nodes: {tree.count_nodes()}")
                if hasattr(tree, "is_valid_bst"):
                    print(f"Valid BST: {tree.is_valid_bst()}")
                if hasattr(tree, "root") and tree.root:
                    print(f"Balanced: {TreeAnalysis.is_balanced_bst(tree.root)}")
            else:
                print("Invalid command or not supported for this tree type.")

        except ValueError:
            print("Please enter valid numbers for values.")
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Run all demonstrations."""
    print("Chapter 14: Trees - Interactive Examples")
    print("This script demonstrates tree data structures and algorithms.\n")

    demonstrate_tree_traversals()
    demonstrate_bst_operations()
    demonstrate_avl_balance()
    demonstrate_heap_operations()
    demonstrate_heap_sort()
    demonstrate_tree_analysis()
    performance_comparison()

    # Interactive demo
    response = (
        input("\nWould you like to explore tree operations interactively? (y/n): ")
        .strip()
        .lower()
    )
    if response == "y" or response == "yes":
        interactive_tree_builder()

    print("\n" + "=" * 60)
    print("TREE DATA STRUCTURES KEY INSIGHTS:")
    print("=" * 60)
    print("1. Trees represent hierarchical relationships perfectly")
    print("2. BSTs provide O(log n) operations but require balancing")
    print("3. AVL trees guarantee balance through rotations")
    print("4. Heaps enable O(1) access to min/max elements")
    print("5. Traversals reveal different tree perspectives")
    print("6. Balance is crucial for performance guarantees")
    print("\nTrees are fundamental to efficient hierarchical data processing!")


if __name__ == "__main__":
    main()
