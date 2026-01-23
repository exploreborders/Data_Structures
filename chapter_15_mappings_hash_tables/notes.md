# Personal Notes for Chapter 13: Hash Tables

## Key Concepts Explained

### The Hash Table Magic
- **O(1) lookup**: From linear search to constant time - that's the revolution
- **Key to index mapping**: Hash functions turn keys into array positions
- **Collision inevitable**: Perfect hashing is impossible in practice
- **Load factor critical**: Too full = performance disaster

### Hash Function: The Heart of It All
- **Deterministic**: Same key, same hash every time
- **Uniform distribution**: Even spread across the table
- **Avalanche effect**: Tiny key change → completely different hash
- **Python's hash()**: Built-in, handles most types, but not cryptographic

### Collision Resolution: When Things Go Wrong
- **Separate chaining**: Linked lists at each slot - simple, flexible
- **Open addressing**: Find another empty slot - cache-friendly, but clustering
- **Linear probing**: Check next slot - primary clustering problem
- **Quadratic probing**: Skip quadratic distances - reduces clustering
- **Double hashing**: Two hash functions - best distribution

## Implementation That Clicked

### Separate Chaining Hash Table
```python
class HashTableChaining:
    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        # Check if key exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update
                return
        # Key not found, append
        self.table[index].append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)
```
- **Simple and robust**: No fancy probing logic
- **Handles collisions gracefully**: Just another item in the list
- **Load factor can exceed 1**: Only limited by memory
- **Cache unfriendly**: Following pointers in linked lists

### Open Addressing with Linear Probing
```python
class HashTableProbing:
    def __init__(self, size=16):
        self.size = size
        self.table = [None] * size  # None means empty
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        if self.count >= self.size * 0.75:  # Load factor > 0.75
            self._resize()

        index = self._hash(key)
        original_index = index

        while self.table[index] is not None and self.table[index][0] != key:
            index = (index + 1) % self.size  # Linear probe
            if index == original_index:  # Full table
                raise Exception("Hash table full")

        if self.table[index] is None:
            self.count += 1
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:  # Searched entire table
                break

        raise KeyError(key)
```
- **Cache friendly**: All data in contiguous array
- **No extra pointers**: Better memory efficiency
- **Clustering problem**: Once a cluster forms, it grows
- **Deletion tricky**: Need tombstones to avoid breaking probe sequences

## Performance Insights That Surprised Me

### Load Factor Effects
- **α < 0.5**: Excellent performance for both strategies
- **α = 0.75**: Still good, but collisions increasing
- **α > 0.9**: Performance degrades significantly
- **Separate chaining**: Can handle α > 1 (but gets slow)
- **Open addressing**: Must keep α < 1

### Hash Function Quality Matters
- **Poor hash**: Clustering kills performance
- **Good hash**: Even distribution, minimal collisions
- **Python's hash()**: Generally excellent for strings and ints
- **Custom objects**: Need good `__hash__` and `__eq__`

### Real-World Performance
- **Separate chaining**: Better for high load factors
- **Open addressing**: Better for cache performance
- **Python dict**: Uses sophisticated open addressing
- **Java HashMap**: Separate chaining with tree conversion

## Real-World Applications I Never Considered

### Database Systems
- **Hash indexes**: O(1) lookup for equality queries
- **Buffer pools**: Fast page lookup by ID
- **Query caches**: Store results by query hash

### Operating Systems
- **Page tables**: Virtual to physical address mapping
- **File system caches**: Fast file metadata access
- **Process tables**: PID to process structure mapping

### Networking
- **Routing tables**: IP address lookups
- **ARP caches**: IP to MAC address mapping
- **DNS caches**: Domain name to IP resolution

### Compilers and Interpreters
- **Symbol tables**: Variable/function name lookups
- **String interning**: Single copy of identical strings
- **Constant pools**: Efficient storage of constants

### Security Systems
- **Password storage**: Salted hash verification
- **Session management**: Session ID to user mapping
- **API key validation**: Fast key lookup and validation

## Common Pitfalls I Keep Making

### 1. **Load Factor Ignorance**
- Letting table get too full without resizing
- Not monitoring performance degradation
- Forgetting different strategies have different optimal load factors

### 2. **Hash Function Assumptions**
- Assuming hash functions are perfect
- Not handling hash collisions properly
- Using poor hash functions for custom objects

### 3. **Key Immutability**
- Modifying keys after insertion (breaks hash)
- Using mutable objects as keys
- Forgetting that list/dict can't be hashed

### 4. **Deletion Problems**
- Breaking probe sequences in open addressing
- Leaving tombstones that slow down searches
- Memory leaks in separate chaining

### 5. **Rehashing Costs**
- Not accounting for rehashing overhead
- Poor resize strategies (too frequent/small)
- Blocking operations during rehashing

## Python Dict Internals
- **Open addressing** with quadratic probing
- **32-bit hashes** for efficiency
- **Automatic resizing** when load factor > 2/3
- **Combined table** for keys and values
- **Hash randomization** for security (dict randomization)

## Advanced Techniques I Want to Explore
- **Cuckoo hashing**: Worst-case O(1) lookup
- **Hopscotch hashing**: Bounded probe distances
- **Perfect hashing**: Zero collisions for static sets
- **Universal hashing**: Provably good performance

## Performance Monitoring
- **Load factor tracking**: Resize before it gets too high
- **Average probe length**: Monitor clustering
- **Resize frequency**: Balance time vs space
- **Cache hit rates**: Memory access patterns

## My Thoughts
- Hash tables are magical - they make the impossible seem trivial
- The collision resolution strategies are beautifully simple yet powerful
- Understanding load factor is crucial - it's the hidden performance killer
- Python's dict is insanely well-optimized - a masterclass in engineering

## Exercises/Thoughts
- Implement different collision resolution strategies and compare performance
- Experiment with different hash functions and their distribution properties
- Build a custom hash table and benchmark against Python's dict
- Think about hash tables in distributed systems (consistent hashing)
- Consider how hash tables are used in modern databases and caches</content>
<parameter name="filePath">chapter_13_hash_tables/notes.md