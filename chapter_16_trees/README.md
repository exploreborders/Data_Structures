# Chapter 14: Trees - Hierarchical Data Structures

This chapter explores tree data structures, fundamental hierarchical organizations that model relationships and enable efficient algorithms. Trees provide logarithmic-time operations for ordered data and serve as the foundation for many advanced data structures and algorithms.

## What is a Tree?

A tree is a hierarchical data structure consisting of nodes connected by edges. Each node has a parent (except the root) and zero or more children. Trees are acyclic, meaning there are no cycles in the structure.

### Tree Terminology:
- **Root**: Topmost node with no parent
- **Leaf**: Node with no children
- **Internal Node**: Node with at least one child
- **Parent/Child**: Relationship between connected nodes
- **Siblings**: Nodes with the same parent
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to node
- **Level**: All nodes at the same depth

## Binary Trees

### Properties:
- Each node has at most two children
- Left child and right child
- Height can range from O(log n) to O(n)

### Complete Binary Tree:
- All levels filled except possibly the last
- Last level filled from left to right
- Can be efficiently represented using arrays

### Full Binary Tree:
- Every node has either 0 or 2 children
- No node has exactly one child

## Binary Search Trees (BST)

### Properties:
- Left subtree contains only nodes with keys < node's key
- Right subtree contains only nodes with keys > node's key
- Both subtrees are also BSTs
- Inorder traversal yields sorted order

### Operations:
- **Search**: O(h) time, h = height
- **Insert**: O(h) time
- **Delete**: O(h) time
- **Find Min/Max**: O(h) time

### BST Performance:
- **Best Case**: Balanced tree, O(log n) operations
- **Worst Case**: Skewed tree (linked list), O(n) operations

## Tree Traversal Algorithms

### Depth-First Traversals:
1. **Inorder**: Left → Root → Right
   - BST: Produces sorted order
   - Expression trees: Infix notation

2. **Preorder**: Root → Left → Right
   - Create copy of tree
   - Expression trees: Prefix notation

3. **Postorder**: Left → Right → Root
   - Delete tree safely
   - Expression trees: Postfix notation

### Breadth-First Traversal:
- **Level Order**: Visit nodes level by level
- Uses queue data structure
- O(n) time, O(w) space (w = max width)

## Balanced Trees

### AVL Trees:
- Self-balancing BST
- Height difference between subtrees ≤ 1
- Rotations maintain balance after operations

### Balance Factor:
```
Balance Factor = Height(right subtree) - Height(left subtree)
```
- Must be in {-1, 0, 1} for AVL trees

### Rotations:
1. **Right Rotation (LL case)**
2. **Left Rotation (RR case)**
3. **Left-Right Rotation (LR case)**
4. **Right-Left Rotation (RL case)**

## Heap Data Structure

### Properties:
- Complete binary tree
- Heap property: Parent ≥ children (max-heap) or Parent ≤ children (min-heap)
- Efficiently implemented using arrays

### Operations:
- **Insert**: O(log n) - bubble up
- **Extract Max/Min**: O(log n) - bubble down
- **Peek**: O(1)
- **Heapify**: O(n) - build heap from array

### Applications:
- Priority queues
- Heap sort
- Finding k largest/smallest elements
- Median maintenance

## Tree Performance Analysis

### Time Complexity:

| Operation | BST (avg) | BST (worst) | Balanced BST | Heap |
|-----------|-----------|-------------|--------------|------|
| Search | O(log n) | O(n) | O(log n) | O(n) |
| Insert | O(log n) | O(n) | O(log n) | O(log n) |
| Delete | O(log n) | O(n) | O(log n) | O(log n) |
| Find Min/Max | O(log n) | O(n) | O(log n) | O(1) |

### Space Complexity:
- **BST**: O(n)
- **AVL Tree**: O(n)
- **Heap**: O(n)

## Tree Representations

### 1. Node-Based (Linked Structure):
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### 2. Array-Based (Complete Trees):
- Root at index 0
- Left child: 2*i + 1
- Right child: 2*i + 2
- Parent: (i-1)//2

## Tree Algorithms

### 1. Tree Construction:
- Build tree from traversals
- Serialize/deserialize tree
- Convert between representations

### 2. Tree Queries:
- Height, depth, diameter
- Lowest common ancestor (LCA)
- Path sums, subtree sums
- Node counts and properties

### 3. Tree Modifications:
- Insert/delete nodes while maintaining properties
- Balance operations (rotations)
- Tree transformations

## Real-World Applications

### 1. **File Systems**:
- Directory hierarchies
- File organization
- Disk space management

### 2. **Database Systems**:
- B-trees and B+ trees for indexing
- Query optimization trees
- XML/HTML document object models

### 3. **Computer Networks**:
- Routing tables (trie structures)
- Network topologies
- Spanning trees

### 4. **Compilers**:
- Abstract syntax trees (AST)
- Parse trees
- Symbol tables

### 5. **Artificial Intelligence**:
- Game trees (minimax algorithm)
- Decision trees
- Search trees (A* algorithm)

### 6. **Graphics and Games**:
- Scene graphs
- Quadtrees/octree for spatial partitioning
- Animation hierarchies

### 7. **Data Compression**:
- Huffman coding trees
- Tries for dictionary compression

## Implementation Considerations

### Choosing Tree Type:
- **Ordered data with frequent searches**: BST
- **Guaranteed balance needed**: AVL/Red-Black trees
- **Priority-based operations**: Heaps
- **Hierarchical relationships**: General trees

### Memory Management:
- Recursive algorithms may cause stack overflow
- Iterative approaches preferred for deep trees
- Consider memory layout for cache efficiency

### Balance vs Simplicity:
- Unbalanced BSTs: Simple, may degenerate
- Balanced trees: Complex, guaranteed performance
- Trade-off based on use case requirements

## Advanced Tree Concepts

### 1. **Self-Balancing Trees**:
- AVL trees: Strict balance
- Red-Black trees: Relaxed balance, simpler rotations
- Splay trees: Recently accessed nodes moved to root

### 2. **B-Trees**:
- Multi-way search trees
- Used in databases and file systems
- Minimize disk I/O operations

### 3. **Trie (Prefix Tree)**:
- Specialized for string operations
- Efficient prefix searches
- Used in autocomplete, spell checking

### 4. **Segment Trees**:
- Range query optimization
- Efficient updates and queries on ranges
- Used in computational geometry

### 5. **Fenwick Trees (Binary Indexed Trees)**:
- Efficient prefix sum queries
- Space-efficient range updates
- Used in competitive programming

## Tree Traversal Patterns

### Recursive Traversals:
- Natural for tree structures
- Stack space proportional to height
- Simple to implement and understand

### Iterative Traversals:
- Use explicit stacks or queues
- Better for very deep trees
- More complex but memory efficient

### Morris Traversal:
- Inorder traversal without stack or recursion
- O(1) extra space (modifies tree temporarily)
- Complex but space-optimal

## Common Tree Problems

### 1. **Path Problems**:
- Root to leaf paths
- Paths with specific sum
- Diameter of tree
- Maximum path sum

### 2. **Subtree Problems**:
- Identical subtrees
- Largest BST in binary tree
- Subtree with maximum average

### 3. **Tree Construction**:
- Build tree from inorder and preorder
- Build tree from inorder and postorder
- Serialize and deserialize tree

### 4. **Balance and Properties**:
- Check if tree is balanced
- Check if tree is BST
- Convert to balanced BST

## Performance Monitoring

### Key Metrics:
1. **Height**: Should be O(log n) for balanced trees
2. **Balance factor**: Monitor for AVL trees
3. **Operation counts**: Track comparisons and rotations
4. **Memory usage**: Node count and pointer overhead

### Optimization Techniques:
- **Lazy deletion**: Mark nodes as deleted instead of removing
- **Bulk operations**: Process multiple operations together
- **Caching**: Store frequently accessed subtree information
- **Memory pools**: Reduce allocation overhead

## Trees in Modern Systems

Trees are ubiquitous in computer science, appearing in:
- Operating systems (file systems, process hierarchies)
- Databases (B-trees, R-trees)
- Compilers (ASTs, symbol tables)
- Networks (routing trees, spanning trees)
- Graphics (scene graphs, BSP trees)
- AI (game trees, decision trees)

Understanding tree data structures and algorithms is essential for any programmer working with hierarchical data or needing efficient ordered operations.</content>
<parameter name="filePath">chapter_14_trees/README.md