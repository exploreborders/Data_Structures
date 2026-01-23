# Chapter 13: Hash Tables - Fast Key-Based Access

This chapter explores hash tables, one of the most important data structures for efficient key-based operations. Hash tables provide average O(1) time complexity for insert, delete, and lookup operations, making them fundamental to modern computing systems.

## What is a Hash Table?

A hash table is a data structure that implements an associative array, mapping keys to values using a hash function. The hash function converts keys into array indices, enabling direct access to values without searching.

### Core Components:
1. **Hash Function**: Converts keys to array indices
2. **Array/Table**: Stores key-value pairs
3. **Collision Resolution**: Handles cases where different keys hash to same index

## Hash Function Design

### Properties of Good Hash Functions:
- **Deterministic**: Same key always produces same hash
- **Uniform Distribution**: Evenly distributes keys across table
- **Efficient**: Fast to compute
- **Avalanche Effect**: Small input changes cause large output changes

### Common Hash Functions:

#### 1. **Division Method**
```
h(k) = k mod m
```
- Simple and fast
- Good when table size m is prime
- Sensitive to key patterns

#### 2. **Multiplication Method**
```
h(k) = floor(m × (k × A mod 1))
```
- Where A is a constant (often 0.618...)
- Works well for any table size
- Good distribution properties

#### 3. **Universal Hashing**
- Family of hash functions chosen randomly
- Provably good worst-case performance
- Used in cryptographic applications

## Collision Resolution Strategies

### 1. **Separate Chaining**
- Each table entry is a linked list (or other data structure)
- Colliding keys stored in same list
- Simple to implement
- No limit on number of keys

### 2. **Open Addressing**
- All keys stored in table array
- Collision resolved by probing other positions
- No extra data structures needed

#### Open Addressing Variants:
- **Linear Probing**: Check next consecutive positions
- **Quadratic Probing**: Check positions using quadratic function
- **Double Hashing**: Use second hash function for probe sequence

## Hash Table Operations

### Insert Operation:
1. Compute hash of key: `index = hash(key)`
2. Handle collision using chosen strategy
3. Store key-value pair at final position

### Lookup Operation:
1. Compute hash of key: `index = hash(key)`
2. Search collision chain or probe sequence
3. Return value if key found, None otherwise

### Delete Operation:
- More complex with open addressing (requires tombstones)
- Simple with separate chaining (just remove from list)

## Performance Analysis

### Load Factor (α)
```
α = n / m
```
- n = number of keys
- m = table size
- Critical parameter affecting performance

### Expected Performance:

| Operation | Separate Chaining | Open Addressing |
|-----------|-------------------|-----------------|
| Insert | O(1 + α) | O(1 / (1-α)) |
| Lookup | O(1 + α) | O(1 / (1-α)) |
| Delete | O(1 + α) | O(1 / (1-α)) |

### Rehashing:
- When load factor becomes too high, resize table
- Create new larger table
- Reinsert all existing keys
- Amortized O(1) cost per operation

## Hash Table Variants

### 1. **Hash Map/Dictionary**
- General-purpose key-value storage
- Python's `dict`, Java's `HashMap`

### 2. **Hash Set**
- Stores only keys, no values
- Fast membership testing
- Python's `set`, Java's `HashSet`

### 3. **Concurrent Hash Tables**
- Thread-safe operations
- Used in concurrent programming

### 4. **Cuckoo Hashing**
- Guarantees O(1) worst-case lookup
- Uses multiple hash functions
- More complex but predictable performance

## Implementation Considerations

### Choosing Table Size:
- Prime numbers often preferred
- Powers of 2 can work with good hash functions
- Dynamic resizing as table grows

### Key Requirements:
- Keys must be hashable (implement `__hash__`)
- Keys must be comparable for equality
- Immutable keys preferred (hash shouldn't change)

### Memory Overhead:
- Separate chaining: Pointer overhead
- Open addressing: Wasted space for deleted entries
- Load factor balance between time and space

## Real-World Applications

### 1. **Database Indexing**
- Hash indexes for fast lookups
- In-memory caches
- Database buffer management

### 2. **Caching Systems**
- LRU caches with O(1) access
- Web caches, DNS caches
- CPU caches, TLB

### 3. **Symbol Tables**
- Compilers store identifiers
- Interpreters track variables
- Assemblers manage labels

### 4. **Network Applications**
- Router tables
- Firewall rule matching
- Network address translation

### 5. **File Systems**
- File metadata storage
- Directory structures
- Deduplication systems

### 6. **Cryptography**
- Password storage (with salting)
- Digital signatures
- Blockchain technology

### 7. **Search Engines**
- Inverted indexes
- Query caching
- Result ranking

## Hash Table in Python

### Built-in `dict`:
- Uses open addressing with quadratic probing
- Automatic resizing
- 32-bit hash values
- Highly optimized C implementation

### Custom Hash Table Implementation:
```python
class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        # Handle collision and insertion...

    def get(self, key):
        index = self._hash(key)
        # Handle collision and lookup...
```

## Common Hash Table Issues

### 1. **Hash Collisions**
- Different keys hash to same value
- Handled by collision resolution strategies
- Good hash functions minimize collisions

### 2. **Clustering**
- Open addressing can create clusters
- Quadratic probing reduces primary clustering
- Double hashing reduces secondary clustering

### 3. **Rehashing Cost**
- Expensive operation when table grows
- Done incrementally in production systems
- Amortized analysis shows O(1) average cost

### 4. **Hash Function Quality**
- Poor hash functions cause clustering
- Cryptographic hashes too slow for general use
- Balance speed vs distribution quality

### 5. **Key Distribution**
- Some key types have poor hash distributions
- String keys need good string hashing
- Custom objects need custom `__hash__` methods

## Advanced Hash Table Techniques

### 1. **Perfect Hashing**
- Zero collisions for static key sets
- O(1) worst-case lookup
- Preprocessing intensive

### 2. **Hopscotch Hashing**
- Bounded worst-case probe sequence
- Good cache performance
- Predictable performance

### 3. **Robin Hood Hashing**
- Reduces variance in probe lengths
- Better worst-case performance
- More complex implementation

### 4. **Extendible Hashing**
- Dynamic file structures
- Database applications
- External memory efficiency

## Performance Monitoring

### Key Metrics to Track:
1. **Load factor**: Current table utilization
2. **Average probe length**: Open addressing efficiency
3. **Chain length**: Separate chaining balance
4. **Resize frequency**: Rehashing overhead
5. **Cache hit rates**: Memory access patterns

### Optimization Strategies:
- **Resize thresholds**: When to grow table
- **Hash function selection**: Based on key characteristics
- **Collision resolution**: Based on access patterns
- **Memory layout**: Cache-friendly data structures

## Hash Tables vs Other Data Structures

| Data Structure | Lookup | Insert | Delete | Ordered | Memory |
|----------------|--------|--------|--------|---------|--------|
| Hash Table | O(1) | O(1) | O(1) | No | Moderate |
| Binary Tree | O(log n) | O(log n) | O(log n) | Yes | Low |
| Sorted Array | O(log n) | O(n) | O(n) | Yes | Low |
| Linked List | O(n) | O(1) | O(1) | No | Low |

## The Hash Table Revolution

Hash tables revolutionized computer science by enabling constant-time key-based operations. They power everything from programming language dictionaries to database indexes, from caches to search engines. Understanding hash tables is essential for any programmer working with large-scale data processing.

The beauty of hash tables lies in their simplicity: a clever mathematical trick (hashing) combined with elegant collision resolution creates a data structure that seems almost magical in its efficiency.</content>
<parameter name="filePath">chapter_13_hash_tables/README.md