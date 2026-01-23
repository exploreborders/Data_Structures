# Personal Notes for Chapter 15: Binary Search Trees

## Key Concepts Explained

### The Ordered Mapping ADT
- **Beyond basic mappings**: Not just put/get, but ordered operations
- **Floor/ceiling**: Find largest ≤ key, smallest ≥ key
- **Successor/predecessor**: Navigate to next/previous in order
- **Range queries**: Everything between low and high
- **Why it matters**: Many real problems need order-based access

### BST Invariants: The Magic Rules
```
Left subtree: all keys < root.key
Right subtree: all keys > root.key
Both subtrees: also BSTs
```
- **Consequence**: Inorder traversal = sorted order
- **Search**: Like binary search, but with tree structure
- **Insert/Delete**: Must maintain the invariant
- **Verification**: Check recursively for each subtree

### Search: The Recursive Beauty
```python
def search(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
```
- **Base cases**: Empty tree or found key
- **Recursive cases**: Go left or right based on comparison
- **Time**: O(h) where h = height
- **Space**: O(h) recursion stack

### Insert: Building the Tree
```python
def insert(root, key, value):
    if not root:
        return BSTNode(key, value)

    if key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    else:
        root.value = value  # Update existing

    return root
```
- **Return the root**: Every call returns subtree root
- **Recursive placement**: Follow search path to insertion point
- **Duplicates**: Convention - update or ignore
- **Height changes**: Tree can become unbalanced

## The Removal Nightmare

### Three Cases - Each Tricky

#### Case 1: Leaf Node (Easy)
```python
# Just remove it - no children
if not node.left and not node.right:
    return None
```

#### Case 2: One Child (Medium)
```python
# Replace with the existing child
if not node.left:
    return node.right
if not node.right:
    return node.left
```

#### Case 3: Two Children (Hard)
```python
# Find inorder successor (min in right subtree)
successor = find_min(node.right)

# Copy successor's key/value to current node
node.key = successor.key
node.value = successor.value

# Remove successor from right subtree
node.right = remove(node.right, successor.key)
```
- **Why successor?**: Maintains BST property
- **Could use predecessor**: Min in left subtree works too
- **Recursive removal**: Remove successor from its position

### Successor/Predecessor: Tree Navigation
- **Successor**: Smallest key > current key
  - If right subtree: min of right subtree
  - Else: Go up until finding node that's a left child
- **Predecessor**: Largest key < current key
  - Symmetric to successor

### Floor/Ceiling: Closest Matches
- **Floor(x)**: Largest key ≤ x
- **Ceiling(x)**: Smallest key ≥ x
- **Algorithm**: Like search, but track closest matches

## Performance: The Height Problem

### Best Case: Perfect Balance
```
Height = log₂n
Operations = O(log n)
Example: Complete BST
```

### Worst Case: Total Imbalance
```
Height = n-1
Operations = O(n)
Example: Inserted in sorted order
```

### Average Case: Hope for Balance
- Random insertions: O(log n) expected
- Real data often not random
- Pathological cases exist

### Balance Factor
```
BF(node) = height(left) - height(right)
```
- AVL trees: |BF| ≤ 1
- Red-Black: Relaxed constraints
- Splay: Amortized balance

## Implementation Patterns I Keep Reusing

### Recursive BST Operations
```python
def operation(root, key, ...):
    if not root:
        # Base case
        return base_result

    if key < root.key:
        # Go left, update left subtree
        root.left = operation(root.left, key, ...)
    elif key > root.key:
        # Go right, update right subtree
        root.right = operation(root.right, key, ...)
    else:
        # Found - handle operation
        # ...

    return root  # Always return root
```

### Iterative BST Operations
```python
def operation(root, key):
    current = root
    parent = None

    while current:
        if key < current.key:
            parent = current
            current = current.left
        elif key > current.key:
            parent = current
            current = current.right
        else:
            # Found
            break

    # Handle operation with current and parent
```

## Common Bugs I Keep Making

### 1. **Forgetting to Return Root**
```python
# Wrong
def insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.key:
        insert(root.left, key)  # BUG: Doesn't update root.left
    # ...

# Right
def insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)  # Correct
    # ...
```

### 2. **Wrong Removal Logic**
- Removing two-child node without finding successor
- Not updating parent pointers
- Breaking BST property

### 3. **Inorder Traversal Mistakes**
- Forgetting left → root → right order
- Modifying tree during traversal
- Not handling empty subtrees

### 4. **Parent Pointer Confusion**
- When to update parent.left vs parent.right
- Handling root node (no parent)
- Null pointer exceptions

## Real-World Applications I Never Considered

### Database Query Optimization
- **Index scans**: Range queries on indexed columns
- **Sort-merge joins**: Ordered access to data
- **Top-k queries**: Find k largest/smallest efficiently

### File System Operations
- **Directory lookups**: Hierarchical path resolution
- **File metadata**: Fast access by modification time
- **Space allocation**: Free block management

### Network Packet Processing
- **IP routing tables**: Longest prefix matching
- **Firewall rules**: Ordered rule evaluation
- **Quality of service**: Priority-based packet scheduling

### Text Processing
- **Concordance**: Word position tracking
- **Spell checkers**: Dictionary lookups with suggestions
- **Compression**: Huffman coding tree maintenance

### Scientific Computing
- **Event simulation**: Timeline management
- **Spatial queries**: Range searches in coordinates
- **Statistical analysis**: Order statistics computation

## Advanced BST Concepts
- **Order statistics**: Find k-th smallest element
- **Range trees**: Multi-dimensional range queries
- **Interval trees**: Overlapping interval queries
- **Treaps**: Randomized BSTs with heap property

## Performance Optimization Tricks
- **Bulk loading**: Build balanced BST from sorted data
- **Lazy deletion**: Mark nodes deleted, clean up later
- **Caching**: Store frequently accessed subtrees
- **Compression**: Reduce memory overhead

## My Thoughts
- BSTs seem simple but maintaining the invariants is surprisingly subtle
- Removal is way harder than insertion - that two-child case is brutal
- The recursive thinking is beautiful but stack overflow is a real concern
- Balance is everything - without it, you're just using a linked list

## Exercises/Thoughts
- Implement all operations both recursively and iteratively
- Build BST from different insertion orders and observe shapes
- Implement AVL rotations to understand self-balancing
- Solve LeetCode BST problems to see patterns
- Think about how BSTs compare to hash tables for ordered vs unordered access</content>
<parameter name="filePath">chapter_15_binary_search_trees/notes.md