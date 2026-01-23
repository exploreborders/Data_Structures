# Chapter 18: Balanced Binary Search Trees

This chapter explores **balanced binary search trees**, focusing on AVL trees. While regular binary search trees can become unbalanced and degenerate into linked lists, balanced trees maintain logarithmic height guarantees through automatic rebalancing.

## Learning Objectives

By the end of this chapter, you'll understand:
- Why tree balance matters for performance
- How AVL trees maintain balance using rotations
- The trade-offs between different balancing strategies
- Implementation of self-balancing tree operations

## The Balance Problem

Regular binary search trees have O(log n) performance on average, but can degrade to O(n) in the worst case:

```
Unbalanced BST:     Balanced BST:
    1                    4
     \                  / \
      2                2   6
       \              / \ / \
        3            1  3 5 7
         \
          4
           \
            5
```

## AVL Trees

**AVL trees** are self-balancing binary search trees named after their inventors Georgy Adelson-Velsky and Evgenii Landis. They maintain balance by ensuring the height difference between left and right subtrees never exceeds 1.

### Balance Factor

Each node stores a **balance factor** (height of right subtree - height of left subtree):
- Balance factor ∈ {-1, 0, 1} for AVL trees
- Balance factor = 0 means perfectly balanced
- Balance factor = 1 means right subtree is taller
- Balance factor = -1 means left subtree is taller

### Rotations

AVL trees use **rotations** to restore balance when insertions or deletions cause imbalance:

#### Right Rotation (LL Case)
```
    y           x
   / \         / \
  x   C  →    A   y
 / \             / \
A   B           B   C
```

#### Left Rotation (RR Case)
```
  x             y
 / \           / \
A   y    →    x   C
   / \       / \
  B   C     A   B
```

#### Left-Right Rotation (LR Case)
```
  x             x           z
 / \           / \         / \
A   y    →    A   z  →    x   y
   / \           / \     / \ / \
  z   D         B   y   A  B C  D
 / \               / \
B   C             C   D
```

## Implementation

Our AVL tree implementation includes:
- Height tracking for each node
- Balance factor calculation
- Four types of rotations (LL, RR, LR, RL)
- Self-balancing insert and delete operations
- All standard BST operations (search, traversal, etc.)

## Performance

AVL trees guarantee O(log n) performance for all operations:
- **Search**: O(log n)
- **Insert**: O(log n) with rotations
- **Delete**: O(log n) with rotations
- **Space**: O(n)

The balancing overhead is minimal compared to the performance guarantees.

## Trade-offs

**Advantages:**
- Guaranteed O(log n) worst-case performance
- Simple balance condition (height difference ≤ 1)
- Efficient for read-heavy workloads

**Disadvantages:**
- More complex implementation than regular BST
- Rotations add overhead to modifications
- Slightly more memory per node (height field)

## Examples

See the `examples/` directory for interactive demonstrations of:
- Tree rotations in action
- Balance factor calculations
- Performance comparisons with unbalanced trees

## Key Concepts

1. **Balance Factor**: Height difference between subtrees
2. **Rotations**: Tree restructuring operations
3. **Self-Balancing**: Automatic maintenance of balance invariants
4. **Height Guarantee**: O(log n) worst-case bounds
5. **AVL Property**: |balance factor| ≤ 1 for all nodes

## Next Steps

After understanding AVL trees, you might explore:
- Red-Black trees (relaxed balance for fewer rotations)
- B-trees (for disk-based storage)
- Splay trees (for locality of reference)

## Exercises

1. Implement a function to check if a BST is height-balanced
2. Compare AVL tree performance with regular BST on sorted input
3. Extend the AVL tree with additional operations (successor, predecessor)
4. Implement a visual tree rotation animator