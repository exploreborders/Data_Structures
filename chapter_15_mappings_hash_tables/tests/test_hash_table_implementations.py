"""
Tests for Chapter 13: Hash Tables - Efficient Key-Value Storage
"""

import unittest
import random
import string
from typing import List

# Add the code directory to the path
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from hash_table_implementations import (
    HashFunction,
    HashTableSeparateChaining,
    HashTableOpenAddressing,
    HashTableSet,
    HashTableAnalysis
)


class TestHashFunctions(unittest.TestCase):
    """Test cases for hash functions."""

    def test_division_hash(self):
        """Test division hash function."""
        table_size = 10

        # Test basic functionality
        self.assertEqual(HashFunction.division_hash("test", table_size), hash("test") % table_size)
        self.assertEqual(HashFunction.division_hash(42, table_size), hash(42) % table_size)

        # Test range
        for key in ["a", "b", "c", 1, 2, 3]:
            hash_val = HashFunction.division_hash(key, table_size)
            self.assertGreaterEqual(hash_val, 0)
            self.assertLess(hash_val, table_size)

    def test_multiplication_hash(self):
        """Test multiplication hash function."""
        table_size = 10

        # Test basic functionality
        hash_val = HashFunction.multiplication_hash("test", table_size)
        self.assertGreaterEqual(hash_val, 0)
        self.assertLess(hash_val, table_size)

        # Test determinism
        hash1 = HashFunction.multiplication_hash("hello", table_size)
        hash2 = HashFunction.multiplication_hash("hello", table_size)
        self.assertEqual(hash1, hash2)

    def test_universal_hash(self):
        """Test universal hash function."""
        table_size = 10

        # Test basic functionality
        hash_val = HashFunction.universal_hash("test", table_size)
        self.assertGreaterEqual(hash_val, 0)
        self.assertLess(hash_val, table_size)

        # Test with different parameters
        hash1 = HashFunction.universal_hash("test", table_size, a=1, b=1)
        hash2 = HashFunction.universal_hash("test", table_size, a=2, b=2)
        # Different parameters should generally give different hashes
        # (though not guaranteed)

    def test_string_hash_functions(self):
        """Test string-specific hash functions."""
        test_string = "hello world"

        # DJB2 hash
        djb2_hash = HashFunction.djb2_hash(test_string)
        self.assertIsInstance(djb2_hash, int)
        self.assertGreater(djb2_hash, 0)

        # FNV-1a hash
        fnv_hash = HashFunction.fnv1a_hash(test_string)
        self.assertIsInstance(fnv_hash, int)
        self.assertGreater(fnv_hash, 0)

        # Test determinism
        self.assertEqual(HashFunction.djb2_hash(test_string), HashFunction.djb2_hash(test_string))
        self.assertEqual(HashFunction.fnv1a_hash(test_string), HashFunction.fnv1a_hash(test_string))


class TestHashTableSeparateChaining(unittest.TestCase):
    """Test cases for separate chaining hash table."""

    def setUp(self):
        """Set up test hash table."""
        self.ht = HashTableSeparateChaining(initial_size=16)

    def test_empty_hash_table(self):
        """Test operations on empty hash table."""
        self.assertEqual(len(self.ht), 0)
        self.assertEqual(self.ht.get_load_factor(), 0.0)
        self.assertEqual(self.ht.get_max_chain_length(), 0)

        with self.assertRaises(KeyError):
            self.ht.get("nonexistent")

        with self.assertRaises(KeyError):
            self.ht.remove("nonexistent")

    def test_put_and_get(self):
        """Test basic put and get operations."""
        # Insert some key-value pairs
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")
        self.ht.put(42, "number")
        self.ht.put(("tuple", "key"), "complex_key")

        # Verify they can be retrieved
        self.assertEqual(self.ht.get("key1"), "value1")
        self.assertEqual(self.ht.get("key2"), "value2")
        self.assertEqual(self.ht.get(42), "number")
        self.assertEqual(self.ht.get(("tuple", "key")), "complex_key")

        # Verify count
        self.assertEqual(len(self.ht), 4)

    def test_update_existing_key(self):
        """Test updating existing key."""
        self.ht.put("key1", "value1")
        self.assertEqual(self.ht.get("key1"), "value1")

        # Update the value
        self.ht.put("key1", "updated_value")
        self.assertEqual(self.ht.get("key1"), "updated_value")

        # Count should still be 1
        self.assertEqual(len(self.ht), 1)

    def test_remove(self):
        """Test remove operation."""
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")

        # Remove and verify return value
        removed_value = self.ht.remove("key1")
        self.assertEqual(removed_value, "value1")

        # Key should no longer exist
        with self.assertRaises(KeyError):
            self.ht.get("key1")

        # Count should be reduced
        self.assertEqual(len(self.ht), 1)

    def test_contains(self):
        """Test contains method."""
        self.ht.put("key1", "value1")

        self.assertTrue(self.ht.contains("key1"))
        self.assertFalse(self.ht.contains("nonexistent"))

    def test_keys_values_items(self):
        """Test keys, values, and items methods."""
        test_data = [("a", 1), ("b", 2), ("c", 3)]
        for key, value in test_data:
            self.ht.put(key, value)

        keys = self.ht.keys()
        values = self.ht.values()
        items = self.ht.items()

        # All keys should be present
        for key, _ in test_data:
            self.assertIn(key, keys)

        # All values should be present
        for _, value in test_data:
            self.assertIn(value, values)

        # All items should be present
        for item in test_data:
            self.assertIn(item, items)

    def test_resize(self):
        """Test automatic resizing."""
        initial_size = self.ht.size

        # Add enough items to trigger resize
        for i in range(20):  # More than initial_size * load_factor_threshold
            self.ht.put(f"key{i}", f"value{i}")

        # Size should have increased
        self.assertGreater(self.ht.size, initial_size)

        # All items should still be accessible
        for i in range(20):
            self.assertEqual(self.ht.get(f"key{i}"), f"value{i}")

    def test_collision_handling(self):
        """Test collision handling."""
        # Force collisions by using a small table and similar keys
        small_ht = HashTableSeparateChaining(initial_size=2)

        # These will likely collide
        small_ht.put("a", 1)
        small_ht.put("b", 2)
        small_ht.put("c", 3)

        # All should be retrievable despite collisions
        self.assertEqual(small_ht.get("a"), 1)
        self.assertEqual(small_ht.get("b"), 2)
        self.assertEqual(small_ht.get("c"), 3)

        # Check that chains are being used
        self.assertGreater(small_ht.get_max_chain_length(), 1)

    def test_load_factor_and_chains(self):
        """Test load factor and chain length calculations."""
        # Empty table
        self.assertEqual(self.ht.get_load_factor(), 0.0)
        self.assertEqual(self.ht.get_max_chain_length(), 0)
        self.assertEqual(self.ht.get_avg_chain_length(), 0.0)

        # Add some items
        for i in range(10):
            self.ht.put(f"key{i}", i)

        load_factor = len(self.ht) / self.ht.size
        self.assertEqual(self.ht.get_load_factor(), load_factor)
        self.assertGreaterEqual(self.ht.get_max_chain_length(), 1)


class TestHashTableOpenAddressing(unittest.TestCase):
    """Test cases for open addressing hash table."""

    def setUp(self):
        """Set up test hash table."""
        self.ht = HashTableOpenAddressing(initial_size=16)

    def test_empty_hash_table(self):
        """Test operations on empty hash table."""
        self.assertEqual(len(self.ht), 0)
        self.assertEqual(self.ht.get_load_factor(), 0.0)

        with self.assertRaises(KeyError):
            self.ht.get("nonexistent")

        with self.assertRaises(KeyError):
            self.ht.remove("nonexistent")

    def test_put_and_get(self):
        """Test basic put and get operations."""
        # Insert some key-value pairs
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")
        self.ht.put(42, "number")

        # Verify they can be retrieved
        self.assertEqual(self.ht.get("key1"), "value1")
        self.assertEqual(self.ht.get("key2"), "value2")
        self.assertEqual(self.ht.get(42), "number")

        # Verify count
        self.assertEqual(len(self.ht), 3)

    def test_update_existing_key(self):
        """Test updating existing key."""
        self.ht.put("key1", "value1")
        self.assertEqual(self.ht.get("key1"), "value1")

        # Update the value
        self.ht.put("key1", "updated_value")
        self.assertEqual(self.ht.get("key1"), "updated_value")

        # Count should still be 1
        self.assertEqual(len(self.ht), 1)

    def test_remove(self):
        """Test remove operation."""
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")

        # Remove and verify return value
        removed_value = self.ht.remove("key1")
        self.assertEqual(removed_value, "value1")

        # Key should no longer exist
        with self.assertRaises(KeyError):
            self.ht.get("key1")

        # Count should be reduced
        self.assertEqual(len(self.ht), 1)

    def test_resize(self):
        """Test automatic resizing."""
        initial_size = self.ht.size

        # Add enough items to trigger resize
        for i in range(15):  # More than initial_size * load_factor_threshold
            self.ht.put(f"key{i}", f"value{i}")

        # Size should have increased
        self.assertGreater(self.ht.size, initial_size)

        # All items should still be accessible
        for i in range(15):
            self.assertEqual(self.ht.get(f"key{i}"), f"value{i}")

    def test_collision_handling(self):
        """Test collision handling with linear probing."""
        # Force collisions by using a small table
        small_ht = HashTableOpenAddressing(initial_size=4)

        # Add items that will cause collisions
        small_ht.put("a", 1)
        small_ht.put("b", 2)
        small_ht.put("c", 3)
        small_ht.put("d", 4)

        # All should be retrievable
        self.assertEqual(small_ht.get("a"), 1)
        self.assertEqual(small_ht.get("b"), 2)
        self.assertEqual(small_ht.get("c"), 3)
        self.assertEqual(small_ht.get("d"), 4)

    def test_probe_sequence_analysis(self):
        """Test probe sequence length calculations."""
        # Add some items
        for i in range(5):
            self.ht.put(f"key{i}", i)

        # Test probe sequence length for existing keys
        probe_length = self.ht.get_probe_sequence_length("key1")
        self.assertGreaterEqual(probe_length, 1)

        # Test average probe length
        avg_probe = self.ht.get_avg_probe_length()
        self.assertGreaterEqual(avg_probe, 1.0)


class TestHashTableSet(unittest.TestCase):
    """Test cases for hash set implementation."""

    def setUp(self):
        """Set up test hash set."""
        self.set1 = HashTableSet()
        self.set2 = HashTableSet()

    def test_add_and_contains(self):
        """Test add and contains operations."""
        self.set1.add("apple")
        self.set1.add("banana")
        self.set1.add("cherry")

        self.assertTrue(self.set1.contains("apple"))
        self.assertTrue(self.set1.contains("banana"))
        self.assertTrue(self.set1.contains("cherry"))
        self.assertFalse(self.set1.contains("date"))

    def test_remove(self):
        """Test remove operation."""
        self.set1.add("apple")
        self.assertTrue(self.set1.contains("apple"))

        self.set1.remove("apple")
        self.assertFalse(self.set1.contains("apple"))

        # Removing non-existent item should raise KeyError
        with self.assertRaises(KeyError):
            self.set1.remove("nonexistent")

    def test_size(self):
        """Test size method."""
        self.assertEqual(self.set1.size(), 0)

        self.set1.add("a")
        self.assertEqual(self.set1.size(), 1)

        self.set1.add("b")
        self.assertEqual(self.set1.size(), 2)

        self.set1.remove("a")
        self.assertEqual(self.set1.size(), 1)

    def test_items(self):
        """Test items method."""
        items = ["x", "y", "z"]
        for item in items:
            self.set1.add(item)

        retrieved_items = self.set1.items()
        for item in items:
            self.assertIn(item, retrieved_items)

    def test_set_operations(self):
        """Test set operations."""
        # Set up two sets
        self.set1.add("a")
        self.set1.add("b")
        self.set1.add("c")

        self.set2.add("b")
        self.set2.add("c")
        self.set2.add("d")

        # Union
        union_set = self.set1.union(self.set2)
        self.assertEqual(union_set.size(), 4)  # a, b, c, d
        self.assertTrue(union_set.contains("a"))
        self.assertTrue(union_set.contains("b"))
        self.assertTrue(union_set.contains("c"))
        self.assertTrue(union_set.contains("d"))

        # Intersection
        intersect_set = self.set1.intersection(self.set2)
        self.assertEqual(intersect_set.size(), 2)  # b, c
        self.assertTrue(intersect_set.contains("b"))
        self.assertTrue(intersect_set.contains("c"))
        self.assertFalse(intersect_set.contains("a"))
        self.assertFalse(intersect_set.contains("d"))

        # Difference
        diff_set = self.set1.difference(self.set2)
        self.assertEqual(diff_set.size(), 1)  # a
        self.assertTrue(diff_set.contains("a"))
        self.assertFalse(diff_set.contains("b"))
        self.assertFalse(diff_set.contains("c"))
        self.assertFalse(diff_set.contains("d"))


class TestHashTableAnalysis(unittest.TestCase):
    """Test cases for hash table analysis tools."""

    def test_hash_distribution_analysis(self):
        """Test hash function distribution analysis."""
        keys = ["apple", "banana", "cherry", "date", "elderberry"]
        table_size = 10

        distribution = HashTableAnalysis.test_hash_function_distribution(
            HashFunction.division_hash, keys, table_size)

        # All hash values should be in valid range
        for hash_val in distribution.keys():
            self.assertGreaterEqual(hash_val, 0)
            self.assertLess(hash_val, table_size)

        # Total count should equal number of keys
        total_count = sum(distribution.values())
        self.assertEqual(total_count, len(keys))

    def test_distribution_uniformity(self):
        """Test distribution uniformity calculation."""
        # Perfectly uniform distribution
        perfect_dist = {i: 1 for i in range(10)}
        uniformity = HashTableAnalysis.calculate_distribution_uniformity(perfect_dist, 10)
        self.assertEqual(uniformity, 0.0)

        # Non-uniform distribution
        skewed_dist = {0: 5, 1: 5}  # Only 2 slots used out of 10
        uniformity = HashTableAnalysis.calculate_distribution_uniformity(skewed_dist, 10)
        self.assertGreater(uniformity, 0.0)

    def test_benchmark_operations(self):
        """Test benchmarking functionality."""
        operations = [
            ("put", "key1", "val1"),
            ("put", "key2", "val2"),
            ("get", "key1", None),
            ("get", "key2", None),
            ("remove", "key1", None),
        ]

        results = HashTableAnalysis.benchmark_hash_table_operations(
            HashTableSeparateChaining, operations)

        # Should have timing results
        self.assertIn("put_time", results)
        self.assertIn("get_time", results)
        self.assertIn("remove_time", results)
        self.assertIn("final_size", results)
        self.assertIn("load_factor", results)

        # Times should be non-negative
        self.assertGreaterEqual(results["put_time"], 0)
        self.assertGreaterEqual(results["get_time"], 0)
        self.assertGreaterEqual(results["remove_time"], 0)

        # Final size should be 1 (after removing one item)
        self.assertEqual(results["final_size"], 1)


class TestHashTableStress(unittest.TestCase):
    """Stress tests for hash table implementations."""

    def test_large_dataset_separate_chaining(self):
        """Test separate chaining with larger dataset."""
        ht = HashTableSeparateChaining(initial_size=16)

        # Add many items
        num_items = 1000
        for i in range(num_items):
            ht.put(f"key{i}", f"value{i}")

        # Verify all items are accessible
        for i in range(num_items):
            self.assertEqual(ht.get(f"key{i}"), f"value{i}")

        # Verify size
        self.assertEqual(len(ht), num_items)

        # Test removal
        for i in range(0, num_items, 2):  # Remove even indices
            ht.remove(f"key{i}")

        self.assertEqual(len(ht), num_items // 2)

    def test_large_dataset_open_addressing(self):
        """Test open addressing with larger dataset."""
        ht = HashTableOpenAddressing(initial_size=16)

        # Add many items
        num_items = 500  # Smaller due to load factor limits
        for i in range(num_items):
            ht.put(f"key{i}", f"value{i}")

        # Verify all items are accessible
        for i in range(num_items):
            self.assertEqual(ht.get(f"key{i}"), f"value{i}")

        # Verify size
        self.assertEqual(len(ht), num_items)

    def test_string_keys(self):
        """Test with string keys of various lengths."""
        ht = HashTableSeparateChaining()

        test_strings = [
            "a",
            "hello",
            "world",
            "this_is_a_long_string_key",
            "short",
            "another_string_key"
        ]

        # Add strings
        for i, s in enumerate(test_strings):
            ht.put(s, i)

        # Verify retrieval
        for i, s in enumerate(test_strings):
            self.assertEqual(ht.get(s), i)

    def test_mixed_key_types(self):
        """Test with mixed key types."""
        ht = HashTableSeparateChaining()

        # Add different key types
        ht.put("string", "string_value")
        ht.put(42, "int_value")
        ht.put(3.14, "float_value")
        ht.put(("tuple", "key"), "tuple_value")

        # Verify retrieval
        self.assertEqual(ht.get("string"), "string_value")
        self.assertEqual(ht.get(42), "int_value")
        self.assertEqual(ht.get(3.14), "float_value")
        self.assertEqual(ht.get(("tuple", "key")), "tuple_value")


if __name__ == '__main__':
    unittest.main()</content>
<parameter name="filePath">chapter_13_hash_tables/tests/test_hash_table_implementations.py