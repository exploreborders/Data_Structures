#!/usr/bin/env python3
"""
Chapter 13: Hash Tables - Interactive Examples

This script demonstrates hash table concepts with interactive examples,
performance comparisons, and collision visualization.
"""

import time
import random
import sys
import os
from typing import List, Dict, Any

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from hash_table_implementations import (
    HashTableSeparateChaining,
    HashTableOpenAddressing,
    HashTableSet,
    HashTableAnalysis,
    HashFunction
)


def print_hash_table_state(ht, title: str = "Hash Table State"):
    """Print a summary of hash table state."""
    print(f"\n{title}:")
    print(f"  Size: {ht.size}")
    print(f"  Count: {len(ht)}")
    print(".2f")
    if hasattr(ht, 'get_max_chain_length'):
        print(f"  Max chain length: {ht.get_max_chain_length()}")
        print(".2f")
    if hasattr(ht, 'get_avg_probe_length'):
        print(".2f")


def demonstrate_collision_resolution():
    """Demonstrate different collision resolution strategies."""
    print("COLLISION RESOLUTION STRATEGIES")
    print("=" * 50)

    # Create a small hash table to force collisions
    print("Creating small hash tables (size 4) to force collisions...")

    # Separate chaining
    chaining_ht = HashTableSeparateChaining(initial_size=4)
    print("\n1. Separate Chaining:")
    print("   Each slot contains a linked list for collisions")

    items = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
    for key, value in items:
        chaining_ht.put(key, value)
        print(f"   Added ({key}, {value}) - Load factor: {chaining_ht.get_load_factor():.2f}")

    print_hash_table_state(chaining_ht, "Separate Chaining Final State")

    # Open addressing
    addressing_ht = HashTableOpenAddressing(initial_size=4)
    print("\n2. Open Addressing (Linear Probing):")
    print("   Collisions resolved by finding next empty slot")

    for key, value in items:
        addressing_ht.put(key, value)
        print(f"   Added ({key}, {value}) - Load factor: {addressing_ht.get_load_factor():.2f}")

    print_hash_table_state(addressing_ht, "Open Addressing Final State")

    # Test retrieval
    print("\n3. Retrieval Test:")
    test_keys = ["A", "C", "E", "Z"]
    for key in test_keys:
        try:
            val1 = chaining_ht.get(key)
            print(f"   Chaining: {key} → {val1}")
        except KeyError:
            print(f"   Chaining: {key} → Not found")

        try:
            val2 = addressing_ht.get(key)
            print(f"   Addressing: {key} → {val2}")
        except KeyError:
            print(f"   Addressing: {key} → Not found")


def demonstrate_hash_function_quality():
    """Demonstrate hash function quality and distribution."""
    print("\n\nHASH FUNCTION QUALITY ANALYSIS")
    print("=" * 50)

    # Test different hash functions
    keys = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    table_size = 16

    hash_functions = [
        ("Division Hash", HashFunction.division_hash),
        ("Multiplication Hash", HashFunction.multiplication_hash),
    ]

    print(f"Testing {len(keys)} keys on table size {table_size}:")
    print("Keys:", keys)
    print()

    for name, hash_func in hash_functions:
        print(f"{name}:")
        distribution = HashTableAnalysis.test_hash_function_distribution(hash_func, keys, table_size)
        uniformity = HashTableAnalysis.calculate_distribution_uniformity(distribution, table_size)

        print("  Hash distribution:", dict(sorted(distribution.items())))
        print(".4f")
        print(".2f")

        # Visualize distribution
        print("  Distribution visualization:")
        for i in range(table_size):
            count = distribution.get(i, 0)
            bar = "█" * count
            print("2d")

        print()


def performance_comparison():
    """Compare performance of different hash table implementations."""
    print("PERFORMANCE COMPARISON")
    print("=" * 50)

    sizes = [1000, 5000, 10000]
    operations_per_size = 100

    print("Implementation comparison (operations per second):")
    print("Size     | Chaining Put | Addressing Put | Chaining Get | Addressing Get")
    print("---------|--------------|----------------|--------------|----------------")

    for size in sizes:
        # Generate test data
        keys = [f"key{i}" for i in range(operations_per_size)]
        values = [f"value{i}" for i in range(operations_per_size)]

        # Test separate chaining
        chaining_ht = HashTableSeparateChaining(initial_size=size//10)

        start_time = time.time()
        for key, value in zip(keys, values):
            chaining_ht.put(key, value)
        chaining_put_time = time.time() - start_time

        start_time = time.time()
        for key in keys:
            chaining_ht.get(key)
        chaining_get_time = time.time() - start_time

        # Test open addressing
        addressing_ht = HashTableOpenAddressing(initial_size=size//10)

        start_time = time.time()
        for key, value in zip(keys, values):
            addressing_ht.put(key, value)
        addressing_put_time = time.time() - start_time

        start_time = time.time()
        for key in keys:
            addressing_ht.get(key)
        addressing_get_time = time.time() - start_time

        # Calculate operations per second
        chaining_put_ops = operations_per_size / chaining_put_time if chaining_put_time > 0 else float('inf')
        addressing_put_ops = operations_per_size / addressing_put_time if addressing_put_time > 0 else float('inf')
        chaining_get_ops = operations_per_size / chaining_get_time if chaining_get_time > 0 else float('inf')
        addressing_get_ops = operations_per_size / addressing_get_time if addressing_get_time > 0 else float('inf')

        print("8d")

    print("\nKey Insights:")
    print("- Separate chaining: Better for high load factors, more memory")
    print("- Open addressing: Better cache performance, simpler memory layout")
    print("- Performance depends on load factor and collision patterns")


def demonstrate_load_factor_impact():
    """Demonstrate how load factor affects performance."""
    print("\n\nLOAD FACTOR IMPACT")
    print("=" * 50)

    # Test with different load factors
    load_factors = [0.25, 0.5, 0.75, 0.9]
    table_size = 100
    operations = 50

    print(f"Testing {operations} operations on table size {table_size}:")
    print("Load Factor | Avg Chain Length | Performance (ops/sec)")
    print("------------|------------------|-------------------")

    for target_load in load_factors:
        # Calculate how many items to add
        num_items = int(table_size * target_load)

        # Separate chaining
        ht = HashTableSeparateChaining(initial_size=table_size)

        # Add items
        for i in range(num_items):
            ht.put(f"key{i}", f"value{i}")

        # Measure performance
        start_time = time.time()
        for i in range(operations):
            key = f"key{random.randint(0, num_items-1)}"
            ht.get(key)
        elapsed = time.time() - start_time

        ops_per_sec = operations / elapsed if elapsed > 0 else float('inf')
        avg_chain = ht.get_avg_chain_length()

        print("10.2f")


def demonstrate_hash_table_set():
    """Demonstrate hash table set operations."""
    print("\n\nHASH TABLE SET OPERATIONS")
    print("=" * 50)

    # Create two sets
    set1 = HashTableSet()
    set2 = HashTableSet()

    # Add elements
    elements1 = ["apple", "banana", "cherry", "date"]
    elements2 = ["banana", "date", "elderberry", "fig"]

    print("Set 1:", elements1)
    for item in elements1:
        set1.add(item)

    print("Set 2:", elements2)
    for item in elements2:
        set2.add(item)

    # Demonstrate operations
    print("\nOperations:")

    union_set = set1.union(set2)
    print(f"Union: {sorted(union_set.items())} (size: {union_set.size()})")

    intersect_set = set1.intersection(set2)
    print(f"Intersection: {sorted(intersect_set.items())} (size: {intersect_set.size()})")

    diff_set = set1.difference(set2)
    print(f"Difference (Set1 - Set2): {sorted(diff_set.items())} (size: {diff_set.size()})")

    print(f"\nMembership tests:")
    test_items = ["apple", "banana", "elderberry", "grape"]
    for item in test_items:
        in_set1 = set1.contains(item)
        in_set2 = set2.contains(item)
        print(f"  '{item}': Set1={in_set1}, Set2={in_set2}")


def visualize_hash_table_structure():
    """Visualize hash table internal structure."""
    print("\n\nHASH TABLE STRUCTURE VISUALIZATION")
    print("=" * 50)

    # Create a small hash table and show its structure
    ht = HashTableSeparateChaining(initial_size=6)

    items = [("John", 25), ("Jane", 30), ("Bob", 35), ("Alice", 28)]
    print("Adding items to demonstrate hash table structure:")

    for key, value in items:
        ht.put(key, value)
        hash_index = hash(key) % ht.size
        print(f"  {key} (hash: {hash_index}) → {value}")

    print(f"\nFinal hash table structure (size: {ht.size}):")
    print("Index | Contents")
    print("------|---------")

    for i in range(ht.size):
        bucket = ht.table[i]
        if bucket:
            items_str = ", ".join(f"({entry.key}: {entry.value})" for entry in bucket)
            print("5d")
        else:
            print("5d")

    print_hash_table_state(ht, "\nTable Statistics")


def interactive_hash_table_explorer():
    """Interactive hash table exploration."""
    print("\n\nINTERACTIVE HASH TABLE EXPLORER")
    print("=" * 50)

    ht = HashTableSeparateChaining(initial_size=8)

    print("Commands:")
    print("  put <key> <value>  - Add/update key-value pair")
    print("  get <key>          - Retrieve value for key")
    print("  remove <key>       - Remove key-value pair")
    print("  contains <key>     - Check if key exists")
    print("  keys               - Show all keys")
    print("  values             - Show all values")
    print("  items              - Show all key-value pairs")
    print("  stats              - Show table statistics")
    print("  quit               - Exit explorer")
    print()

    while True:
        try:
            command = input("Command: ").strip().split()

            if not command:
                continue

            cmd = command[0].lower()

            if cmd == "quit":
                break
            elif cmd == "put" and len(command) == 3:
                key, value = command[1], command[2]
                ht.put(key, value)
                print(f"Added ({key}, {value})")
            elif cmd == "get" and len(command) == 2:
                key = command[1]
                try:
                    value = ht.get(key)
                    print(f"{key} → {value}")
                except KeyError:
                    print(f"Key '{key}' not found")
            elif cmd == "remove" and len(command) == 2:
                key = command[1]
                try:
                    value = ht.remove(key)
                    print(f"Removed ({key}, {value})")
                except KeyError:
                    print(f"Key '{key}' not found")
            elif cmd == "contains" and len(command) == 2:
                key = command[1]
                exists = ht.contains(key)
                print(f"Key '{key}' exists: {exists}")
            elif cmd == "keys":
                keys = ht.keys()
                print(f"Keys: {keys}")
            elif cmd == "values":
                values = ht.values()
                print(f"Values: {values}")
            elif cmd == "items":
                items = ht.items()
                print(f"Items: {items}")
            elif cmd == "stats":
                print_hash_table_state(ht)
            else:
                print("Invalid command. Type 'quit' to exit.")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    """Run all demonstrations."""
    print("Chapter 13: Hash Tables - Interactive Examples")
    print("This script demonstrates hash table concepts, performance, and operations.\n")

    demonstrate_collision_resolution()
    demonstrate_hash_function_quality()
    performance_comparison()
    demonstrate_load_factor_impact()
    demonstrate_hash_table_set()
    visualize_hash_table_structure()

    # Interactive demo
    response = input("\nWould you like to explore hash tables interactively? (y/n): ").strip().lower()
    if response == 'y' or response == 'yes':
        interactive_hash_table_explorer()

    print("\n" + "=" * 60)
    print("HASH TABLE KEY INSIGHTS:")
    print("=" * 60)
    print("1. Average O(1) performance: Constant-time operations when load factor is controlled")
    print("2. Collision resolution: Separate chaining vs open addressing trade-offs")
    print("3. Load factor critical: Keep below 0.75-0.8 for good performance")
    print("4. Hash function quality: Uniform distribution prevents clustering")
    print("5. Rehashing cost: Amortized O(1) but can cause latency spikes")
    print("6. Memory vs speed: Separate chaining uses more memory, open addressing is faster")
    print("\nHash tables are the foundation of efficient key-based data access!")


if __name__ == '__main__':
    main()</content>
<parameter name="filePath">chapter_13_hash_tables/examples/hash_table_demo.py