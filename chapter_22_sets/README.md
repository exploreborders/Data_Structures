# Chapter 22: Sets - Union-Find (Disjoint Set Union)

This chapter explores **Union-Find (Disjoint Set Union - DSU)**, a fundamental data structure for efficiently managing disjoint sets. Union-Find provides near-constant time operations for tracking partitions of elements into disjoint subsets, making it essential for algorithms like Kruskal's MST, connected components, and network connectivity analysis.

## What is Union-Find?

Union-Find maintains a **partition** of a set into **disjoint subsets**. Each subset is represented by a **representative element**, and the structure supports two primary operations:

- **Find**: Determine which subset contains a particular element
- **Union**: Merge two subsets into a single subset

### Key Characteristics
- **Nearly O(1) amortized time** per operation
- **Simple implementation** with powerful optimizations
- **No requirement** to know all elements in advance
- **Dynamic structure** that grows as operations are performed

## Core Operations

### Find Operation
```python
def find(self, element: T) -> T:
    if self.parent[element] != element:
        # Path compression
        self.parent[element] = self.find(self.parent[element])
    return self.parent[element]
```

**Path Compression**: During find operations, all nodes on the path to root are made to point directly to the root, flattening the tree structure.

### Union Operation
```python
def union(self, x: T, y: T) -> bool:
    root_x = self.find(x)
    root_y = self.find(y)

    if root_x == root_y:
        return False  # Already in same set

    # Union by rank
    if self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
    elif self.rank[root_x] > self.rank[root_y]:
        self.parent[root_y] = root_x
    else:
        self.parent[root_y] = root_x
        self.rank[root_x] += 1

    return True
```

**Union by Rank**: Attach the shorter tree under the taller tree to maintain balance.

## Optimizations

### Path Compression
- **Effect**: Flattens trees during find operations
- **Benefit**: Reduces future operation times
- **Complexity**: Doesn't change worst-case bounds but improves practical performance

### Union by Rank
- **Effect**: Keeps tree heights small
- **Benefit**: Prevents creation of long chains
- **Alternative**: Union by size (count elements in each set)

### Combined Effect
- **Amortized Time**: Nearly O(1) per operation
- **Inverse Ackermann Function**: α(n), which grows very slowly
- **Practical Performance**: Effectively constant time for all reasonable n

## Union-Find Variants

### Standard Union-Find
- **Union by rank** + **path compression**
- **Best general-purpose** implementation
- **Time**: O(α(n)) amortized

### Union by Size
```python
def union_by_size(self, x, y):
    root_x, root_y = self.find(x), self.find(y)
    if root_x != root_y:
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
```

- **Alternative heuristic** to union by rank
- **Similar performance** characteristics

### Persistent Union-Find
- **Maintains history** of operations
- **Allows rollback** to previous states
- **Higher space complexity** for advanced applications

## Applications

### Kruskal's Minimum Spanning Tree
```python
def kruskal_mst(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(vertices)
    mst = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # Different components
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst
```

- **Cycle Prevention**: Union-Find detects when edges would create cycles
- **Efficiency**: Avoids sorting vertices or maintaining complex data structures

### Connected Components
```python
def connected_components(vertices, edges):
    uf = UnionFind(vertices)
    for u, v in edges:
        uf.union(u, v)
    return uf.get_all_sets()
```

- **Dynamic Connectivity**: Handle streaming edge additions
- **Near-Linear Time**: More efficient than DFS/BFS for dense updates

### Network Connectivity
- **Percolation Theory**: Model fluid flow through porous materials
- **Network Reliability**: Detect network partitions
- **Circuit Design**: Component connectivity analysis

### Image Processing
- **Connected Component Labeling**: Identify distinct regions
- **Blob Detection**: Find connected pixel groups
- **Morphological Operations**: Analyze shape connectivity

### Game Theory
- **Go Groups**: Connected stones of same color
- **Hex Connectivity**: Path finding in hexagonal grids
- **Game State Analysis**: Connected component changes

## Complexity Analysis

### Amortized Time Bounds
| Operation | Time Complexity | Notes |
|-----------|----------------|--------|
| Make Set | O(1) | Trivial |
| Find | O(α(n)) | Path compression |
| Union | O(α(n)) | Union by rank |
| Connected | O(α(n)) | Two finds |

### Inverse Ackermann Function α(n)
- **Growth**: Extremely slow, α(n) ≤ 5 for all practical n
- **Intuition**: Effectively constant for computational purposes
- **Practical**: Union-Find operations are faster than most constant factors

### Space Complexity
- **O(n)**: Parent array, rank/size arrays
- **Minimal overhead**: Just a few integers per element
- **Dynamic growth**: Can add elements as needed

## Implementation Considerations

### Initialization
```python
# Lazy initialization
uf = UnionFind()
uf.make_set("element")  # Add as needed

# Bulk initialization
uf = UnionFind(["A", "B", "C", "D"])
```

### Error Handling
- **Missing Elements**: `find()` raises `ValueError` for unknown elements
- **Self-Unions**: `union(x, x)` returns `False` (no change)
- **Connectivity Checks**: `connected(x, y)` returns `False` for different sets

### Performance Tuning
- **Union Heuristic**: Choose rank or size based on access patterns
- **Path Compression**: Always beneficial, minimal overhead
- **Batch Operations**: More efficient when operations are grouped

## Real-World Performance

### Benchmark Results
```
Size: 10,000 elements
Operations: 50,000 random unions/finds
Time: ~0.02 seconds
Avg time per operation: ~0.4 microseconds
```

### Comparison with Alternatives
| Structure | Union | Find | Space | Use Case |
|-----------|-------|------|-------|----------|
| Union-Find | O(α(n)) | O(α(n)) | O(n) | Dynamic connectivity |
| Linked Lists | O(1) | O(n) | O(n) | Simple unions |
| Trees | O(log n) | O(log n) | O(n) | Balanced operations |

## Advanced Topics

### Persistent Union-Find
- **Undo Operations**: Rollback to previous states
- **Version Control**: Maintain operation history
- **Functional Programming**: Immutable data structures

### Weighted Union-Find
- **Size-Based Unions**: Use element counts for heuristics
- **Weighted Heuristics**: Custom weighting schemes
- **Load Balancing**: Distribute work based on set sizes

### Concurrent Union-Find
- **Lock-Free Algorithms**: Non-blocking operations
- **Parallel Unions**: Concurrent set merging
- **Transactional Semantics**: Atomic operation sequences

## Common Interview Questions

1. **Implement Union-Find with path compression and union by rank**
2. **Detect cycles in undirected graphs using Union-Find**
3. **Implement Kruskal's MST algorithm**
4. **Find connected components in a graph**
5. **Compare Union-Find with DFS/BFS for connectivity**

## Implementation in Other Languages

### C++ (with std::vector)
```cpp
class UnionFind {
    std::vector<int> parent, rank;
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    bool unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if(rx == ry) return false;

        if(rank[rx] < rank[ry]) parent[rx] = ry;
        else if(rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }

        return true;
    }
};
```

### Java (with arrays)
```java
public class UnionFind {
    private int[] parent, rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    public int find(int x) {
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public boolean union(int x, int y) {
        int rx = find(x), ry = find(y);
        if(rx == ry) return false;

        if(rank[rx] < rank[ry]) parent[rx] = ry;
        else if(rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }

        return true;
    }
}
```

## The Union-Find Mindset

Union-Find teaches us to think about **connectivity** and **partitions**:

- **Dynamic Sets**: Elements can be added and merged on-the-fly
- **Implicit Representations**: No need to store explicit set contents
- **Lazy Evaluation**: Operations are performed only when needed
- **Optimistic Structures**: Assume good behavior, optimize for it

This mindset extends beyond Union-Find to many algorithmic domains where **incremental computation** and **lazy evaluation** provide elegant solutions.

Understanding Union-Find means understanding how simple data structures with clever optimizations can achieve **theoretical optimality** while maintaining **practical efficiency**.

The combination of path compression and union by rank creates a structure that is not just fast—it's **beautifully efficient**, proving that sometimes the best solutions come from **careful attention to the details of how data is organized and accessed**.