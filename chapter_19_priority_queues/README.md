# Chapter 19: Priority Queues

This chapter explores **priority queues**, a fundamental ADT that manages elements with associated priorities. Priority queues enable efficient retrieval of the highest (or lowest) priority element, making them essential for scheduling, event simulation, and optimization algorithms.

## What is a Priority Queue?

A priority queue is an abstract data type that supports the following operations:
- **Insert**: Add an element with a priority
- **Remove Top**: Remove and return the element with highest/lowest priority
- **Peek**: Return the highest/lowest priority element without removing it

Unlike regular queues (FIFO), priority queues serve elements based on their priority rather than arrival order.

### Priority Semantics

- **Min-Priority Queue**: Smallest priority values are served first
- **Max-Priority Queue**: Largest priority values are served first

## Binary Heap Implementation

Priority queues are typically implemented using **binary heaps**, which provide:
- **Insert**: O(log n) time
- **Remove Top**: O(log n) time
- **Peek**: O(1) time
- **Build Heap**: O(n) time

### Heap Properties

A binary heap is a complete binary tree where each node satisfies the **heap property**:
- **Min-heap**: parent ≤ children
- **Max-heap**: parent ≥ children

### Complete Binary Tree Representation

Heaps are efficiently stored in arrays using the following relationships:
```
Parent of node i: (i-1)/2
Left child of node i: 2*i + 1
Right child of node i: 2*i + 2
```

## Core Operations

### Insert Operation
```python
def insert(self, item):
    self.heap.append(item)
    self._bubble_up(len(self.heap) - 1)
```

### Remove Top Operation
```python
def extract_top(self):
    top = self.heap[0]
    last = self.heap.pop()
    if self.heap:
        self.heap[0] = last
        self._sink_down(0)
    return top
```

### Bubble Up (for Insert)
Restores heap property by moving an element up the tree until it finds its correct position.

### Sink Down (for Remove)
Restores heap property by moving the root element down the tree until it finds its correct position.

## Heap Building

### Method 1: Sequential Insertion - O(n log n)
```python
heap = BinaryHeap()
for item in items:
    heap.insert(item)  # O(log n) per insertion
```

### Method 2: Build Heap - O(n)
```python
def build_heap(arr):
    self.heap = arr.copy()
    # Start from last non-leaf node
    for i in range(len(arr)//2 - 1, -1, -1):
        sink_down(i)
```

## Heapsort Algorithm

Heapsort uses heap operations to sort an array in O(n log n) time:

```python
def heapsort(arr):
    # Build max-heap
    build_heap(arr)

    # Extract elements one by one
    for i in range(len(arr)-1, 0, -1):
        # Swap root (largest) with last element
        arr[0], arr[i] = arr[i], arr[0]
        # Restore heap property on reduced heap
        sink_down(arr, 0, i)
```

## Priority Queue Applications

### 1. **CPU Scheduling**
- Operating systems use priority queues to schedule processes
- Higher priority processes get CPU time first

### 2. **Event Simulation**
- Discrete event simulation uses priority queues for event scheduling
- Events are processed in chronological order

### 3. **Graph Algorithms**
- Dijkstra's shortest path algorithm uses priority queues
- Prim's minimum spanning tree algorithm uses priority queues

### 4. **Data Compression**
- Huffman coding uses priority queues to build optimal prefix codes

### 5. **Task Management**
- Task schedulers prioritize urgent tasks
- Print job queues prioritize by deadline or importance

### 6. **Medical Systems**
- Hospital emergency rooms triage patients by severity
- Critical patients seen before less urgent cases

## Implementation Variants

### Min-Heap vs Max-Heap

| Feature | Min-Heap | Max-Heap |
|---------|----------|----------|
| **Top Element** | Smallest | Largest |
| **Use Case** | Min-priority queue | Max-priority queue |
| **Comparison** | `a < b` | `a > b` |

### Array vs Pointer Implementation

- **Array-based**: Simple, cache-friendly, used in most implementations
- **Pointer-based**: More flexible for complex operations

## Performance Analysis

### Time Complexity

| Operation | Binary Heap | Worst Case |
|-----------|-------------|------------|
| Insert | O(log n) | O(log n) |
| Extract Top | O(log n) | O(log n) |
| Peek | O(1) | O(1) |
| Build Heap | O(n) | O(n) |
| Find Arbitrary | O(n) | O(n) |

### Space Complexity
- **Binary Heap**: O(n) for element storage
- **Auxiliary**: O(1) additional space

### Comparison with Other Structures

| Structure | Insert | Extract Top | Find Min/Max |
|-----------|--------|-------------|---------------|
| Unsorted Array | O(1) | O(n) | O(n) |
| Sorted Array | O(n) | O(1) | O(1) |
| Binary Heap | O(log n) | O(log n) | O(1) |
| Balanced BST | O(log n) | O(log n) | O(log n) |

## Heap Variants

### 1. **Binary Heap** (Standard)
- Simple, efficient, widely used
- Array-based implementation
- Good cache performance

### 2. **d-ary Heap**
- Each node has d children instead of 2
- Reduces height for better cache performance
- Trade-off: more comparisons per level

### 3. **Fibonacci Heap**
- Amortized O(1) insert and decrease-key
- Complex implementation
- Used in advanced graph algorithms

### 4. **Binomial Heap**
- Multiple trees with specific structure
- Fast merge operations
- Complex but powerful

## Common Interview Questions

1. **Implement a priority queue using heaps**
2. **Find the k largest/smallest elements in an array**
3. **Merge k sorted arrays**
4. **Implement a stack/queue using priority queues**
5. **Design a system for task scheduling**

## Implementation Considerations

### 1. **Stable Priority Queues**
- Standard heaps are not stable
- May need additional sequence numbers for stability

### 2. **Custom Priorities**
- Support for complex priority schemes
- Comparator functions for custom ordering

### 3. **Concurrent Access**
- Thread-safety considerations
- Lock-free implementations for high performance

### 4. **Memory Management**
- Dynamic resizing strategies
- Memory pool allocation for performance

## Real-World Examples

### Python's heapq Module
```python
import heapq

# Min-heap operations
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heapq.heappop(heap))  # 1
```

### Java's PriorityQueue
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(3);
pq.add(1);
pq.add(4);
System.out.println(pq.poll());  // 1
```

### C++'s priority_queue
```cpp
priority_queue<int> pq;
pq.push(3);
pq.push(1);
pq.push(4);
cout << pq.top() << endl;  // 4 (max-heap)
```

## Advanced Topics

### Decrease/Increase Key Operations
- Modify priority of existing elements
- Important for graph algorithms like Dijkstra

### Merge Operations
- Combine two priority queues efficiently
- Used in certain algorithmic contexts

### Lazy Deletion
- Mark elements as deleted instead of immediate removal
- Useful for concurrent scenarios

## The Priority Queue Mindset

Priority queues teach us to think about **relative importance** rather than **chronological order**. They encourage designing systems where:
- Decisions are made based on current needs
- Resources are allocated to highest-value tasks
- Efficiency comes from focusing on what's most important

This mindset extends beyond computer science to project management, resource allocation, and decision-making in complex systems.

Understanding priority queues is essential for anyone building systems that must make intelligent choices about what to process next.