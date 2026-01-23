# Chapter 15: Binary Search Trees - Ordered Data Structures

This chapter explores Binary Search Trees (BSTs), a fundamental data structure that maintains ordered data while providing efficient operations. BSTs combine the hierarchical structure of trees with the ordering properties of sorted arrays, enabling logarithmic-time operations for insertion, deletion, and search.

## The Ordered Mapping ADT

Before diving into BSTs, we need to understand the Ordered Mapping ADT - an extension of the basic Mapping ADT that supports order-based operations.

### Ordered Mapping Operations:
- **Standard Mapping**: `put(key, value)`, `get(key)`, `remove(key)`
- **Ordered Operations**: `floor(key)`, `ceiling(key)`, `predecessor(key)`, `successor(key)`
- **Range Operations**: `keys_in_range(low, high)`, `values_in_range(low, high)`
- **Extremes**: `min_key()`, `max_key()`

### Comparison with Regular Mappings:
| Operation | Unordered Map | Ordered Map |
|-----------|----------------|-------------|
| put/get/remove | O(1) average | O(log n) |
| floor/ceiling | O(n) | O(log n) |
| range queries | O(n) | O(log n) + k |
| min/max | O(n) | O(log n) |

## Binary Search Tree Properties

### BST Invariants:
1. **Left Subtree**: All keys < node's key
2. **Right Subtree**: All keys > node's key
3. **Recursive Property**: Both subtrees are BSTs

### Key Consequences:
- **Inorder Traversal**: Produces sorted order
- **Search Path**: O(h) where h is height
- **Uniqueness**: No duplicate keys (by convention)

## BST Node Structure

```python
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # Optional, but useful for some operations
```

## Core BST Operations

### Search Operation

```python
def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
```

**Time Complexity**: O(h) where h is tree height

### Insert Operation

```python
def insert(root, key, value):
    if root is None:
        return BSTNode(key, value)

    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    else:
        # Key exists - update value
        root.value = value

    return root
```

**Time Complexity**: O(h) for search + O(1) for insertion

## Advanced BST Operations

### Successor and Predecessor

The **successor** of a key is the smallest key greater than the given key.
The **predecessor** is the largest key smaller than the given key.

### Floor and Ceiling

- **Floor(key)**: Largest key ≤ given key
- **Ceiling(key)**: Smallest key ≥ given key

### Range Queries

- **Keys in Range**: Find all keys between low and high
- **Count in Range**: Count keys in a range
- **Sum in Range**: Sum values for keys in a range

## BST Removal - The Complex Case

Removal is the most complex BST operation due to maintaining the BST property.

### Three Removal Cases:

#### 1. **Leaf Node**: No children
```
Before:     5        After:     5
          /   \                /
         3     7              3
        / \   / \              \
       1   4 6   8             4
```
Remove 1: Simply remove the leaf.

#### 2. **One Child**: Node has one subtree
```
Before:     5        After:     7
          /   \                / \
         3     7              3   8
        / \   / \            / \   /
       1   4 6   8         1   4 6
```
Remove 7: Replace with its right child (8), and attach 8's left child (6).

#### 3. **Two Children**: Most complex case
```
Before:     5        After:     6
          /   \                / \
         3     7              3   7
        / \   / \            / \   \
       1   4 6   8         1   4   8
```
Remove 5: Find inorder successor (6), replace 5 with 6, then remove the original 6.

### Inorder Successor Algorithm:
1. If node has right subtree, find minimum in right subtree
2. If no right subtree, go up parents until finding a node that's a left child

## BST Performance Analysis

### Height and Balance

**Best Case**: Complete BST (height = log₂n)
- All operations: O(log n)

**Worst Case**: Skewed BST (height = n-1)
- All operations: O(n)
- Essentially a linked list

### Average Case Analysis
- Random insertions: O(log n) expected height
- Many real-world inputs are not random
- Performance depends on insertion order

### Balance Metrics

#### Balance Factor
```
BF(node) = height(left) - height(right)
```
- AVL trees: |BF| ≤ 1
- Red-Black trees: Relaxed constraints

#### Tree Skewness
- Left-heavy vs right-heavy
- Perfect balance vs acceptable imbalance

## BST Variants and Optimizations

### Self-Balancing BSTs
1. **AVL Trees**: Strict balance (height difference ≤ 1)
2. **Red-Black Trees**: Relaxed balance with color invariants
3. **Splay Trees**: Recently accessed nodes moved to root
4. **Treaps**: Random priorities for balance

### BST Optimizations
1. **Parent Pointers**: Enable ancestor queries
2. **Threaded BSTs**: Store inorder successor/predecessor
3. **Cached Statistics**: Store subtree sizes, sums
4. **Bulk Operations**: Handle multiple insertions efficiently

## BST vs Other Ordered Structures

| Structure | Insert | Delete | Search | Range Query | Space |
|-----------|--------|--------|--------|-------------|-------|
| Sorted Array | O(n) | O(n) | O(log n) | O(log n) + k | O(n) |
| BST (avg) | O(log n) | O(log n) | O(log n) | O(log n) + k | O(n) |
| BST (worst) | O(n) | O(n) | O(n) | O(n) | O(n) |
| Balanced BST | O(log n) | O(log n) | O(log n) | O(log n) + k | O(n) |
| Hash Table | O(1) | O(1) | O(1) | O(n) | O(n) |

## Common BST Problems

### 1. **Validation Problems**
- Check if BST property holds
- Verify BST after operations
- Detect corrupted BSTs

### 2. **Traversal Problems**
- Inorder traversal without recursion
- Morris traversal (O(1) space)
- Reverse inorder traversals

### 3. **Structural Problems**
- Convert BST to sorted DLL
- Check if two BSTs are identical
- Find LCA in BST

### 4. **Range and Order Problems**
- Find k-th smallest element
- Count nodes in range
- Find floor/ceiling efficiently

## Implementation Considerations

### Recursive vs Iterative
- **Recursive**: Clean, natural for trees
- **Iterative**: Better for deep trees, avoids stack overflow
- **Hybrid**: Use recursion for simplicity, iteration for safety

### Key Management
- **Immutable Keys**: Prevent key changes after insertion
- **Key Comparison**: Define total ordering
- **Duplicate Handling**: Allow/disallow duplicates

### Memory and Caching
- **Node Overhead**: Store keys, values, pointers
- **Cache Efficiency**: Sequential vs random access patterns
- **Memory Pools**: Reduce allocation overhead

## Real-World Applications

### 1. **Database Indexing**
- B-tree indexes (generalized BSTs)
- Efficient range queries
- Balanced search performance

### 2. **File Systems**
- Directory structures
- File metadata organization
- Fast file lookups

### 3. **Compilers and Interpreters**
- Symbol tables
- Variable scope management
- Function lookup tables

### 4. **Network Routing**
- IP address lookup tables
- Routing table organization
- Network packet classification

### 5. **Text Processing**
- Concordance construction
- Dictionary implementations
- Spell checking data structures

### 6. **Computational Geometry**
- Range trees
- kd-trees (multidimensional BSTs)
- Spatial data structures

## BST Limitations and Solutions

### Problem: Unbalanced Trees
**Solution**: Self-balancing variants (AVL, Red-Black, Splay)

### Problem: No Random Access
**Solution**: Use additional data structures or different representations

### Problem: Range Queries are Slow
**Solution**: Augment with subtree statistics or use different structures

### Problem: Memory Overhead
**Solution**: Compressed BSTs or alternative representations

## The BST Design Philosophy

BSTs represent a fundamental trade-off in data structure design:
- **Ordered access** with logarithmic performance
- **Dynamic insertions/deletions** without full resorting
- **Hierarchical organization** enabling efficient traversals

The BST invariant (left < root < right) creates a powerful abstraction that enables sophisticated algorithms while maintaining intuitive ordering properties. Understanding BSTs is essential for mastering ordered data structures and the algorithms that operate on them.

Modern systems use BST variants extensively, from database indexes to network routing tables, making BST mastery a cornerstone of computer science education.</content>
<parameter name="filePath">chapter_15_binary_search_trees/README.md