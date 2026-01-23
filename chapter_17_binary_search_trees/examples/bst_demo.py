#!/usr/bin/env python3
"""
Chapter 15: Binary Search Trees - Interactive Examples

This script demonstrates BST operations, traversals, performance analysis,
and comparison with other data structures.
"""

import time
import random
import sys
import os
from typing import List, Tuple, Any

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from bst_implementation import BinarySearchTree, BSTAnalysis


def print_tree_visualization(root, title: str = "BST Structure", max_width: int = 60):
    """Simple text-based BST visualization."""
    print(f"\n{title}:")

    def print_tree_helper(node, prefix: str = "", is_left: bool = True):
        if node:
            # Print right subtree first (for left-to-right layout)
            print_tree_helper(node.right, prefix + ("│   " if is_left else "    "), False)

            # Print current node
            connector = "└── " if is_left else "┌── "
            node_str = f"{node.key}"
            if len(node_str) > 10:
                node_str = node_str[:7] + "..."
            print(f"{prefix}{connector}{node_str}")

            # Print left subtree
            print_tree_helper(node.left, prefix + ("    " if is_left else "│   "), True)

    if root:
        print_tree_helper(root)
    else:
        print("  (empty tree)")


def demonstrate_bst_operations():
    """Demonstrate basic BST operations."""
    print("BASIC BST OPERATIONS")
    print("=" * 50)

    bst = BinarySearchTree()

    print("Inserting values: 8, 3, 10, 1, 6, 14, 4, 7, 13")
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    for i, val in enumerate(values):
        bst.put(val, f"value{val}")
        if i < 5:  # Show first few insertions
            print(f"\nAfter inserting {val}:")
            print_tree_visualization(bst.root)

    print(f"\nFinal BST structure:")
    print_tree_visualization(bst.root)

    print(f"\nBST Properties:")
    print(f"Size: {len(bst)}")
    print(f"Height: {bst.get_height()}")
    print(f"Min key: {bst.min_key()}")
    print(f"Max key: {bst.max_key()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")

    # Demonstrate search
    print(f"\nSearching for key 6: {'Found' if bst.contains(6) else 'Not found'}")
    print(f"Searching for key 9: {'Found' if bst.contains(9) else 'Not found'}")

    # Demonstrate successor/predecessor
    print(f"\nSuccessor of 6: {bst.successor(6)}")
    print(f"Predecessor of 10: {bst.predecessor(10)}")

    # Demonstrate floor/ceiling
    print(f"Floor of 5: {bst.floor(5)}")
    print(f"Ceiling of 9: {bst.ceiling(9)}")


def demonstrate_traversals():
    """Demonstrate different tree traversal algorithms."""
    print("\n\nTREE TRAVERSALS")
    print("=" * 50)

    # Create a sample BST
    bst = BinarySearchTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        bst.put(val, f"value{val}")

    print("Sample BST:")
    print_tree_visualization(bst.root)

    print("\nTraversal Results:")

    # Inorder
    inorder = bst.inorder_traversal()
    print("Inorder (Left-Root-Right - sorted order):")
    print("  Keys:", [key for key, _ in inorder])
    print("  Values:", [val for _, val in inorder])

    # Preorder
    preorder = bst.preorder_traversal()
    print("\nPreorder (Root-Left-Right - copy order):")
    print("  Keys:", [key for key, _ in preorder])

    # Postorder
    postorder = bst.postorder_traversal()
    print("\nPostorder (Left-Right-Root - deletion order):")
    print("  Keys:", [key for key, _ in postorder])

    # Level order
    levelorder = bst.level_order_traversal()
    print("\nLevel-order (breadth-first):")
    print("  Keys:", [key for key, _ in levelorder])


def demonstrate_removal():
    """Demonstrate BST removal operations."""
    print("\n\nBST REMOVAL OPERATIONS")
    print("=" * 50)

    bst = BinarySearchTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for val in values:
        bst.put(val, f"value{val}")

    print("Original BST:")
    print_tree_visualization(bst.root)

    # Remove a leaf node
    print("\nRemoving leaf node 4:")
    bst.remove(4)
    print_tree_visualization(bst.root)
    print(f"Still valid BST: {bst.is_valid_bst()}")

    # Remove a node with one child
    print("\nRemoving node with one child (1):")
    bst.remove(1)
    print_tree_visualization(bst.root)
    print(f"Still valid BST: {bst.is_valid_bst()}")

    # Remove a node with two children
    print("\nRemoving node with two children (3):")
    bst.remove(3)
    print_tree_visualization(bst.root)
    print(f"Still valid BST: {bst.is_valid_bst()}")


def demonstrate_range_queries():
    """Demonstrate range query operations."""
    print("\n\nRANGE QUERIES")
    print("=" * 50)

    bst = BinarySearchTree()
    # Insert values 1-20
    for i in range(1, 21):
        bst.put(i, f"value{i}")

    print("BST with keys 1-20")

    test_ranges = [
        (5, 15, "Middle range"),
        (1, 5, "Start range"),
        (15, 20, "End range"),
        (10, 10, "Single value"),
        (25, 30, "Outside range")
    ]

    for low, high, description in test_ranges:
        keys = bst.keys_in_range(low, high)
        values = bst.values_in_range(low, high)
        print(f"\n{description} [{low}, {high}]:")
        print(f"  Keys found: {keys}")
        print(f"  Count: {len(keys)}")


def performance_comparison():
    """Compare BST performance with different insertion orders."""
    print("\n\nPERFORMANCE COMPARISON")
    print("=" * 50)

    sizes = [100, 1000]
    scenarios = [
        ("Worst Case (sorted)", lambda n: list(range(n))),
        ("Best Case (balanced)", lambda n: BSTAnalysis.generate_best_case_bst(n).inorder_traversal()),
        ("Random Case", lambda n: random.sample(range(n), n))
    ]

    print("Size | Scenario       | Build Time | Height | Valid BST")
    print("-----|----------------|------------|--------|----------")

    for size in sizes:
        for scenario_name, key_generator in scenarios:
            # Generate keys
            if "balanced" in scenario_name:
                bst = BSTAnalysis.generate_best_case_bst(size)
                keys = [key for key, _ in bst.inorder_traversal()]
                build_time = 0  # Already built
            else:
                keys = key_generator(size)
                bst = BinarySearchTree()

                # Time the build
                start_time = time.time()
                for key in keys:
                    bst.put(key, f"value{key}")
                build_time = time.time() - start_time

            height = bst.get_height()
            is_valid = bst.is_valid_bst()

            print(".4f")


def demonstrate_bst_shapes():
    """Demonstrate different BST shapes and their properties."""
    print("\n\nBST SHAPES AND PROPERTIES")
    print("=" * 50)

    # Worst case (skewed)
    print("1. Worst Case BST (skewed - inserted in sorted order)")
    worst_bst = BSTAnalysis.generate_worst_case_bst(8)
    print_tree_visualization(worst_bst.root, "Worst Case BST")

    worst_analysis = BSTAnalysis.analyze_bst_shape(worst_bst)
    print("  Properties:")
    print(f"    Height: {worst_analysis['height']}")
    print(f"    Balanced: {worst_analysis['is_balanced']}")
    print(".2f")

    # Best case (balanced)
    print("\n2. Best Case BST (balanced)")
    best_bst = BSTAnalysis.generate_best_case_bst(7)
    print_tree_visualization(best_bst.root, "Best Case BST")

    best_analysis = BSTAnalysis.analyze_bst_shape(best_bst)
    print("  Properties:")
    print(f"    Height: {best_analysis['height']}")
    print(f"    Balanced: {best_analysis['is_balanced']}")
    print(".2f")

    # Random case
    print("\n3. Random Case BST")
    random_bst = BSTAnalysis.generate_random_bst(10, seed=42)
    print_tree_visualization(random_bst.root, "Random BST")

    random_analysis = BSTAnalysis.analyze_bst_shape(random_bst)
    print("  Properties:")
    print(f"    Height: {random_analysis['height']}")
    print(f"    Balanced: {random_analysis['is_balanced']}")
    print(".2f")


def benchmark_vs_other_structures():
    """Compare BST performance with other data structures."""
    print("\n\nCOMPARISON WITH OTHER DATA STRUCTURES")
    print("=" * 50)

    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'chapter_13_hash_tables', 'code'))
    try:
        from hash_table_implementations import HashTableSeparateChaining
        hash_available = True
    except ImportError:
        hash_available = False
        print("Hash table implementation not available for comparison")

    if hash_available:
        operations = 1000
        data = list(range(operations))

        # BST
        bst = BinarySearchTree()
        start_time = time.time()
        for item in data:
            bst.put(item, f"value{item}")
        bst_build_time = time.time() - start_time

        start_time = time.time()
        for item in data:
            bst.contains(item)
        bst_search_time = time.time() - start_time

        # Hash Table
        ht = HashTableSeparateChaining()
        start_time = time.time()
        for item in data:
            ht.put(item, f"value{item}")
        ht_build_time = time.time() - start_time

        start_time = time.time()
        for item in data:
            ht.contains(item)
        ht_search_time = time.time() - start_time

        print("Data Structure | Build Time | Search Time | Height/Load")
        print("---------------|------------|-------------|------------")
        print(".4f")
        print(".4f")

        print("\nKey Insights:")
        print("- Hash tables: O(1) average case, but no ordering")
        print("- BSTs: O(log n) worst case, maintain ordering")
        print("- Choose based on your access pattern needs!")


def interactive_bst_explorer():
    """Interactive BST exploration."""
    print("\n\nINTERACTIVE BST EXPLORER")
    print("=" * 50)

    bst = BinarySearchTree()

    print("Commands:")
    print("  insert <key> <value>  - Insert key-value pair")
    print("  remove <key>          - Remove key")
    print("  search <key>          - Search for key")
    print("  successor <key>       - Find inorder successor")
    print("  predecessor <key>     - Find inorder predecessor")
    print("  floor <key>           - Find floor of key")
    print("  ceiling <key>         - Find ceiling of key")
    print("  range <low> <high>    - Find keys in range")
    print("  traversals            - Show all traversals")
    print("  visualize             - Show tree structure")
    print("  stats                 - Show tree statistics")
    print("  quit                  - Exit explorer")
    print()

    while True:
        try:
            command = input("Command: ").strip().split()

            if not command:
                continue

            cmd = command[0].lower()

            if cmd == "quit":
                break
            elif cmd == "insert" and len(command) == 3:
                key, value = int(command[1]), command[2]
                bst.put(key, value)
                print(f"Inserted ({key}, {value})")
            elif cmd == "remove" and len(command) == 2:
                key = int(command[1])
                try:
                    value = bst.remove(key)
                    print(f"Removed ({key}, {value})")
                except KeyError:
                    print(f"Key {key} not found")
            elif cmd == "search" and len(command) == 2:
                key = int(command[1])
                found = bst.contains(key)
                if found:
                    value = bst.get(key)
                    print(f"Found: ({key}, {value})")
                else:
                    print(f"Key {key} not found")
            elif cmd == "successor" and len(command) == 2:
                key = int(command[1])
                succ = bst.successor(key)
                print(f"Successor of {key}: {succ}")
            elif cmd == "predecessor" and len(command) == 2:
                key = int(command[1])
                pred = bst.predecessor(key)
                print(f"Predecessor of {key}: {pred}")
            elif cmd == "floor" and len(command) == 2:
                key = int(command[1])
                floor = bst.floor(key)
                print(f"Floor of {key}: {floor}")
            elif cmd == "ceiling" and len(command) == 2:
                key = int(command[1])
                ceiling = bst.ceiling(key)
                print(f"Ceiling of {key}: {ceiling}")
            elif cmd == "range" and len(command) == 3:
                low, high = int(command[1]), int(command[2])
                keys = bst.keys_in_range(low, high)
                values = bst.values_in_range(low, high)
                print(f"Keys in range [{low}, {high}]: {keys}")
                print(f"Values: {values}")
            elif cmd == "traversals":
                print("Inorder:   ", [key for key, _ in bst.inorder_traversal()])
                print("Preorder:  ", [key for key, _ in bst.preorder_traversal()])
                print("Postorder: ", [key for key, _ in bst.postorder_traversal()])
                print("Level:     ", [key for key, _ in bst.level_order_traversal()])
            elif cmd == "visualize":
                print_tree_visualization(bst.root)
            elif cmd == "stats":
                print(f"Size: {len(bst)}")
                print(f"Height: {bst.get_height()}")
                if not bst.is_empty():
                    print(f"Min key: {bst.min_key()}")
                    print(f"Max key: {bst.max_key()}")
                print(f"Valid BST: {bst.is_valid_bst()}")
            else:
                print("Invalid command or not supported.")

        except ValueError:
            print("Please enter valid numbers for keys.")
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Run all demonstrations."""
    print("Chapter 15: Binary Search Trees - Interactive Examples")
    print("This script demonstrates BST operations, traversals, and analysis.\n")

    demonstrate_bst_operations()
    demonstrate_traversals()
    demonstrate_removal()
    demonstrate_range_queries()
    performance_comparison()
    demonstrate_bst_shapes()
    benchmark_vs_other_structures()

    # Interactive demo
    response = input("\nWould you like to explore BSTs interactively? (y/n): ").strip().lower()
    if response == 'y' or response == 'yes':
        interactive_bst_explorer()

    print("\n" + "=" * 60)
    print("BINARY SEARCH TREE KEY INSIGHTS:")
    print("=" * 60)
    print("1. BST invariant: Left < Root < Right enables O(log n) operations")
    print("2. Balance is crucial: Height determines actual performance")
    print("3. Traversals reveal structure: Inorder = sorted, others show tree shape")
    print("4. Removal is complex: Three cases (leaf, one child, two children)")
    print("5. Ordered operations: Successor, predecessor, floor, ceiling")
    print("6. Range queries: Efficient ordered access")
    print("\nBSTs are the foundation of ordered data structures!")


if __name__ == '__main__':
    main()</content>
<parameter name="filePath">chapter_15_binary_search_trees/examples/bst_demo.py