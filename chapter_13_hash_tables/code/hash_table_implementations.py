"""
Chapter 13: Hash Tables - Efficient Key-Value Storage

This module implements hash tables with various collision resolution strategies,
hash functions, and performance analysis tools.
"""

from typing import List, Dict, Optional, Tuple, Any, Union
import math


class HashFunction:
    """Collection of hash functions for different use cases."""

    @staticmethod
    def division_hash(key: Any, table_size: int) -> int:
        """Division method: key mod table_size."""
        return hash(key) % table_size

    @staticmethod
    def multiplication_hash(key: Any, table_size: int) -> int:
        """Multiplication method with golden ratio constant."""
        A = 0.6180339887  # (√5 - 1) / 2
        hash_val = hash(key)
        fractional_part = (hash_val * A) % 1
        return int(table_size * fractional_part)

    @staticmethod
    def universal_hash(key: Any, table_size: int, a: int = 31, b: int = 7, p: int = 10**9 + 7) -> int:
        """
        Universal hash function using random coefficients.
        h(k) = ((a * k + b) mod p) mod m
        """
        key_hash = hash(key)
        return ((a * key_hash + b) % p) % table_size

    @staticmethod
    def djb2_hash(key: str) -> int:
        """DJB2 string hash function."""
        hash_val = 5381
        for char in key:
            hash_val = ((hash_val << 5) + hash_val) + ord(char)  # hash * 33 + char
        return hash_val

    @staticmethod
    def fnv1a_hash(key: str) -> int:
        """FNV-1a hash function."""
        hash_val = 14695981039346656037  # FNV offset basis
        fnv_prime = 1099511628211  # FNV prime

        for byte in key.encode('utf-8'):
            hash_val ^= byte
            hash_val *= fnv_prime

        return hash_val


class HashTableEntry:
    """Represents a key-value entry in the hash table."""

    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Entry({self.key}: {self.value})"


class HashTableSeparateChaining:
    """Hash table using separate chaining for collision resolution."""

    def __init__(self, initial_size: int = 16, load_factor_threshold: float = 0.75):
        self.size = initial_size
        self.table: List[List[HashTableEntry]] = [[] for _ in range(initial_size)]
        self.count = 0
        self.load_factor_threshold = load_factor_threshold
        self.hash_function = HashFunction.division_hash

    def _hash(self, key: Any) -> int:
        """Compute hash index for a key."""
        return self.hash_function(key, self.size)

    def _resize(self, new_size: int) -> None:
        """Resize the hash table to a new size."""
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0

        # Rehash all entries
        for bucket in old_table:
            for entry in bucket:
                self.put(entry.key, entry.value)

    def put(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair."""
        if self.count / self.size > self.load_factor_threshold:
            self._resize(self.size * 2)

        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        # Key not found, add new entry
        bucket.append(HashTableEntry(key, value))
        self.count += 1

    def get(self, key: Any) -> Any:
        """Retrieve the value for a given key."""
        index = self._hash(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        raise KeyError(f"Key '{key}' not found")

    def remove(self, key: Any) -> Any:
        """Remove and return the value for a given key."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                removed_value = entry.value
                bucket.pop(i)
                self.count -= 1
                return removed_value

        raise KeyError(f"Key '{key}' not found")

    def contains(self, key: Any) -> bool:
        """Check if a key exists in the hash table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self) -> List[Any]:
        """Return all keys in the hash table."""
        result = []
        for bucket in self.table:
            for entry in bucket:
                result.append(entry.key)
        return result

    def values(self) -> List[Any]:
        """Return all values in the hash table."""
        result = []
        for bucket in self.table:
            for entry in bucket:
                result.append(entry.value)
        return result

    def items(self) -> List[Tuple[Any, Any]]:
        """Return all key-value pairs in the hash table."""
        result = []
        for bucket in self.table:
            for entry in bucket:
                result.append((entry.key, entry.value))
        return result

    def get_load_factor(self) -> float:
        """Calculate the current load factor."""
        return self.count / self.size

    def get_max_chain_length(self) -> int:
        """Get the length of the longest chain."""
        return max(len(bucket) for bucket in self.table) if self.table else 0

    def get_avg_chain_length(self) -> float:
        """Get the average chain length."""
        total_chains = sum(len(bucket) for bucket in self.table)
        return total_chains / self.size if self.size > 0 else 0

    def __len__(self) -> int:
        """Return the number of key-value pairs."""
        return self.count

    def __str__(self) -> str:
        """String representation of the hash table."""
        return f"HashTableSeparateChaining(size={self.size}, count={self.count}, load_factor={self.get_load_factor():.2f})"


class HashTableOpenAddressing:
    """Hash table using open addressing for collision resolution."""

    class Entry:
        """Entry that can be a key-value pair, None (empty), or DELETED."""
        def __init__(self, key: Any = None, value: Any = None):
            self.key = key
            self.value = value

        @property
        def is_empty(self) -> bool:
            return self.key is None and self.value is None

        @property
        def is_deleted(self) -> bool:
            return self.key == "__DELETED__"

        def __repr__(self):
            if self.is_empty:
                return "EMPTY"
            elif self.is_deleted:
                return "DELETED"
            else:
                return f"Entry({self.key}: {self.value})"

    def __init__(self, initial_size: int = 16, load_factor_threshold: float = 0.75):
        self.size = initial_size
        self.table: List[HashTableOpenAddressing.Entry] = [
            HashTableOpenAddressing.Entry() for _ in range(initial_size)
        ]
        self.count = 0
        self.deleted_count = 0
        self.load_factor_threshold = load_factor_threshold
        self.hash_function = HashFunction.division_hash

    def _hash(self, key: Any) -> int:
        """Compute primary hash index."""
        return self.hash_function(key, self.size)

    def _probe_linear(self, index: int, attempt: int) -> int:
        """Linear probing: next = (index + attempt) % size."""
        return (index + attempt) % self.size

    def _probe_quadratic(self, index: int, attempt: int) -> int:
        """Quadratic probing: next = (index + attempt²) % size."""
        return (index + attempt * attempt) % self.size

    def _probe_double_hash(self, key: Any, index: int, attempt: int) -> int:
        """Double hashing: uses a second hash function."""
        h2 = HashFunction.multiplication_hash(key, self.size - 1) + 1  # Ensure h2 != 0
        return (index + attempt * h2) % self.size

    def _find_slot(self, key: Any, for_insertion: bool = False) -> Tuple[int, bool]:
        """
        Find the appropriate slot for a key.

        Returns:
            (slot_index, found_existing_key)
        """
        index = self._hash(key)
        deleted_slot = -1

        for attempt in range(self.size):
            slot_idx = self._probe_linear(index, attempt)
            entry = self.table[slot_idx]

            if entry.is_empty:
                # Found empty slot
                return (deleted_slot if deleted_slot != -1 and for_insertion else slot_idx), False
            elif entry.is_deleted:
                # Remember first deleted slot for insertion
                if deleted_slot == -1 and for_insertion:
                    deleted_slot = slot_idx
            elif entry.key == key:
                # Found existing key
                return slot_idx, True

        # Table is full (shouldn't happen if we resize properly)
        raise Exception("Hash table probe sequence exhausted")

    def _resize(self, new_size: int) -> None:
        """Resize the hash table."""
        old_table = self.table
        self.size = new_size
        self.table = [HashTableOpenAddressing.Entry() for _ in range(new_size)]
        self.count = 0
        self.deleted_count = 0

        # Reinsert all non-deleted entries
        for entry in old_table:
            if not entry.is_empty and not entry.is_deleted:
                self.put(entry.key, entry.value)

    def put(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair."""
        if (self.count + self.deleted_count) / self.size > self.load_factor_threshold:
            self._resize(self.size * 2)

        slot_idx, found = self._find_slot(key, for_insertion=True)

        if found:
            # Update existing key
            self.table[slot_idx].value = value
        else:
            # Insert new key
            if self.table[slot_idx].is_deleted:
                self.deleted_count -= 1
            self.table[slot_idx] = HashTableOpenAddressing.Entry(key, value)
            self.count += 1

    def get(self, key: Any) -> Any:
        """Retrieve the value for a given key."""
        slot_idx, found = self._find_slot(key)

        if found:
            return self.table[slot_idx].value
        else:
            raise KeyError(f"Key '{key}' not found")

    def remove(self, key: Any) -> Any:
        """Remove and return the value for a given key."""
        slot_idx, found = self._find_slot(key)

        if found:
            entry = self.table[slot_idx]
            removed_value = entry.value
            entry.key = "__DELETED__"  # Mark as deleted
            entry.value = None
            self.count -= 1
            self.deleted_count += 1
            return removed_value
        else:
            raise KeyError(f"Key '{key}' not found")

    def contains(self, key: Any) -> bool:
        """Check if a key exists in the hash table."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self) -> List[Any]:
        """Return all keys in the hash table."""
        result = []
        for entry in self.table:
            if not entry.is_empty and not entry.is_deleted:
                result.append(entry.key)
        return result

    def values(self) -> List[Any]:
        """Return all values in the hash table."""
        result = []
        for entry in self.table:
            if not entry.is_empty and not entry.is_deleted:
                result.append(entry.value)
        return result

    def items(self) -> List[Tuple[Any, Any]]:
        """Return all key-value pairs."""
        result = []
        for entry in self.table:
            if not entry.is_empty and not entry.is_deleted:
                result.append((entry.key, entry.value))
        return result

    def get_load_factor(self) -> float:
        """Calculate the current load factor."""
        return self.count / self.size

    def get_probe_sequence_length(self, key: Any) -> int:
        """Get the length of the probe sequence for a key."""
        index = self._hash(key)
        probes = 0

        for attempt in range(self.size):
            slot_idx = self._probe_linear(index, attempt)
            entry = self.table[slot_idx]
            probes += 1

            if entry.is_empty:
                return probes
            elif entry.key == key:
                return probes

        return probes

    def get_avg_probe_length(self) -> float:
        """Calculate average probe sequence length."""
        if self.count == 0:
            return 0

        total_probes = 0
        for entry in self.table:
            if not entry.is_empty and not entry.is_deleted:
                total_probes += self.get_probe_sequence_length(entry.key)

        return total_probes / self.count

    def __len__(self) -> int:
        """Return the number of key-value pairs."""
        return self.count

    def __str__(self) -> str:
        """String representation of the hash table."""
        return f"HashTableOpenAddressing(size={self.size}, count={self.count}, load_factor={self.get_load_factor():.2f})"


class HashTableSet:
    """Hash set implementation using hash table for fast membership testing."""

    def __init__(self, initial_size: int = 16):
        self.hash_table = HashTableSeparateChaining(initial_size)

    def add(self, item: Any) -> None:
        """Add an item to the set."""
        self.hash_table.put(item, True)

    def remove(self, item: Any) -> None:
        """Remove an item from the set."""
        self.hash_table.remove(item)

    def contains(self, item: Any) -> bool:
        """Check if item is in the set."""
        return self.hash_table.contains(item)

    def size(self) -> int:
        """Return the number of items in the set."""
        return len(self.hash_table)

    def items(self) -> List[Any]:
        """Return all items in the set."""
        return self.hash_table.keys()

    def union(self, other: 'HashTableSet') -> 'HashTableSet':
        """Return the union of this set with another."""
        result = HashTableSet()
        for item in self.items():
            result.add(item)
        for item in other.items():
            result.add(item)
        return result

    def intersection(self, other: 'HashTableSet') -> 'HashTableSet':
        """Return the intersection of this set with another."""
        result = HashTableSet()
        for item in self.items():
            if other.contains(item):
                result.add(item)
        return result

    def difference(self, other: 'HashTableSet') -> 'HashTableSet':
        """Return the difference of this set with another."""
        result = HashTableSet()
        for item in self.items():
            if not other.contains(item):
                result.add(item)
        return result


class HashTableAnalysis:
    """Tools for analyzing hash table performance."""

    @staticmethod
    def test_hash_function_distribution(hash_func, keys: List[Any], table_size: int) -> Dict[int, int]:
        """
        Test how well a hash function distributes keys.

        Returns:
            Dictionary mapping hash values to count of keys
        """
        distribution = {}
        for key in keys:
            hash_val = hash_func(key, table_size)
            distribution[hash_val] = distribution.get(hash_val, 0) + 1

        return distribution

    @staticmethod
    def calculate_distribution_uniformity(distribution: Dict[int, int], table_size: int) -> float:
        """
        Calculate how uniform a hash distribution is.

        Returns:
            Uniformity score (0 = perfectly uniform, higher = less uniform)
        """
        if not distribution:
            return 0

        expected_count = sum(distribution.values()) / table_size
        variance = sum((count - expected_count) ** 2 for count in distribution.values())
        variance += expected_count ** 2 * (table_size - len(distribution))  # Empty slots

        return variance / table_size

    @staticmethod
    def benchmark_hash_table_operations(hash_table_class, operations: List[Tuple[str, Any, Any]],
                                       initial_size: int = 16) -> Dict[str, float]:
        """
        Benchmark hash table operations.

        operations: List of (operation_type, key, value) tuples
                   operation_type: "put", "get", "remove"
        """
        import time

        ht = hash_table_class(initial_size)
        results = {}

        # Benchmark puts
        puts = [(op, key, val) for op, key, val in operations if op == "put"]
        if puts:
            start_time = time.time()
            for _, key, val in puts:
                ht.put(key, val)
            results["put_time"] = time.time() - start_time

        # Benchmark gets
        gets = [(op, key, val) for op, key, val in operations if op == "get"]
        if gets:
            start_time = time.time()
            for _, key, _ in gets:
                try:
                    ht.get(key)
                except KeyError:
                    pass  # Expected for some tests
            results["get_time"] = time.time() - start_time

        # Benchmark removes
        removes = [(op, key, val) for op, key, val in operations if op == "remove"]
        if removes:
            start_time = time.time()
            for _, key, _ in removes:
                try:
                    ht.remove(key)
                except KeyError:
                    pass  # Expected for some tests
            results["remove_time"] = time.time() - start_time

        results["final_size"] = len(ht)
        results["load_factor"] = ht.get_load_factor()

        return results</content>
<parameter name="filePath">chapter_13_hash_tables/code/hash_table_implementations.py