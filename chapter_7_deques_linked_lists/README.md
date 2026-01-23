# Chapter 7: Deques and Linked Lists - Dynamic Data Structures

This chapter explores more sophisticated data structures that overcome limitations of arrays/lists. We'll implement the Deque ADT, build Linked Lists from scratch, demonstrate how to implement Queue using LinkedList (showcasing the Wrapper Pattern), and understand when to choose different implementations.

## The Limitations of Arrays/Lists

### Problems with Dynamic Arrays
Python's `list` uses dynamic arrays that work well for most cases, but have limitations:

1. **Inefficient Insertions/Deletions**: Adding/removing from the middle is O(n)
2. **Memory Overhead**: Pre-allocated space for growth
3. **Contiguous Memory**: Requires large contiguous memory blocks

### When We Need Better Structures
- **Frequent insertions/deletions** at both ends
- **No contiguous memory** requirements
- **Predictable performance** for all operations
- **Memory efficiency** for sparse data

## Linked Lists: Building from Nodes

### Node Structure
```python
class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data    # The actual data
        self.next = None    # Reference to next node
```

### Singly Linked List Implementation
```python
class LinkedList:
    def __init__(self):
        self.head = None    # First node
        self._size = 0      # Track size for O(1) len()

    def append(self, data):
        """Add to end of list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, data):
        """Add to beginning of list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def __len__(self):
        return self._size
```

### Linked List Operations Complexity
- **Access by index**: O(n) - must traverse from head
- **Insertion at head**: O(1) - just update head pointer
- **Insertion at tail**: O(n) - must find last node (unless we track tail)
- **Deletion**: O(n) - must find node to delete

### Doubly Linked List for Better Performance
```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Track both ends
        self._size = 0

    def append(self, data):
        """O(1) append with tail pointer."""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data):
        """O(1) prepend with head pointer."""
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1
```

## The Deque ADT

### Deque Definition
A **Deque** (Double-Ended Queue) allows insertions and deletions at both ends.

**Operations:**
- `add_first(item)`: Add to front
- `add_last(item)`: Add to back  
- `remove_first()`: Remove from front
- `remove_last()`: Remove from back
- `first()`: Look at front item
- `last()`: Look at back item
- `is_empty()`: Check if empty
- `size()`: Get number of items

### Deque vs Stack vs Queue
- **Stack**: Only top operations (LIFO)
- **Queue**: Only front/back operations (FIFO)
- **Deque**: Both ends operations (flexible)

### Deque Implementation with Doubly Linked List
```python
class Deque:
    def __init__(self):
        self._list = DoublyLinkedList()

    def add_first(self, item):
        """Add item to front of deque."""
        self._list.prepend(item)

    def add_last(self, item):
        """Add item to back of deque."""
        self._list.append(item)

    def remove_first(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("remove_first from empty deque")
        item = self._list.head.data
        self._list.head = self._list.head.next
        if self._list.head:
            self._list.head.prev = None
        else:
            self._list.tail = None
        self._list._size -= 1
        return item

    def remove_last(self):
        """Remove and return back item."""
        if self.is_empty():
            raise IndexError("remove_last from empty deque")
        item = self._list.tail.data
        self._list.tail = self._list.tail.prev
        if self._list.tail:
            self._list.tail.next = None
        else:
            self._list.head = None
        self._list._size -= 1
        return item

    def first(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("first of empty deque")
        return self._list.head.data

    def last(self):
        """Return back item without removing."""
        if self.is_empty():
            raise IndexError("last of empty deque")
        return self._list.tail.data

    def is_empty(self):
        return self._list._size == 0

    def size(self):
        return self._list._size
```

## Implementing Queue with LinkedList: The Wrapper Pattern

### The Wrapper Pattern
The **Wrapper Pattern** involves creating a class that "wraps" another class, providing a different interface or additional functionality.

**Why Use Wrappers:**
- **Interface Adaptation**: Make one interface look like another
- **Enhanced Functionality**: Add features to existing classes
- **Implementation Hiding**: Change underlying implementation without affecting users

### Queue Implementation Using LinkedList
```python
class LinkedQueue:
    """
    Queue ADT implemented using a LinkedList.
    Demonstrates the Wrapper Pattern.
    """

    def __init__(self):
        self._list = LinkedList()  # Wrap a LinkedList

    def enqueue(self, item):
        """Add item to back of queue (wrapper for append)."""
        self._list.append(item)

    def dequeue(self):
        """Remove and return front item."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        # Remove from head (front) of linked list
        item = self._list.head.data
        self._list.head = self._list.head.next
        self._list._size -= 1
        return item

    def front(self):
        """Return front item without removing."""
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._list.head.data

    def is_empty(self):
        return self._list._size == 0

    def size(self):
        return self._list._size
```

### Performance Comparison
```python
# List-based Queue (from Chapter 6)
class ListQueue:
    def dequeue(self):      # O(n) - shift all elements
        return self._items.pop(0)

# LinkedList-based Queue
class LinkedQueue:
    def dequeue(self):      # O(1) - just update head pointer
        item = self._list.head.data
        self._list.head = self._list.head.next
        return item
```

## Storing Length Efficiently

### The Length Caching Problem
```python
# Naive approach: O(n) length
class BadLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # ... append logic
        pass

    def __len__(self):      # O(n) - traverse entire list!
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
```

### The Correct Approach: Cache the Length
```python
class GoodLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0      # Cache the length

    def append(self, data):
        # ... append logic
        self._size += 1     # Update cached length

    def __len__(self):      # O(1) - just return cached value
        return self._size
```

### Why Length Caching Matters
- **Frequent length checks**: `if len(my_list) > 0:` called often
- **Performance**: O(1) vs O(n) for length queries
- **Consistency**: Length always reflects true state
- **Memory vs Speed**: Small memory cost for big performance gain

## Testing Against the ADT Contract

### ADT Contract Testing
Test that implementations satisfy the ADT specifications:

```python
def test_deque_adt_contract():
    """Test that Deque implementation satisfies ADT contract."""

    deque = Deque()

    # Initially empty
    assert deque.is_empty()
    assert deque.size() == 0

    # Test preconditions (should raise errors)
    try:
        deque.remove_first()
        assert False, "Should raise IndexError"
    except IndexError:
        pass

    try:
        deque.first()
        assert False, "Should raise IndexError"
    except IndexError:
        pass

    # Add items and test postconditions
    deque.add_first("first")
    assert not deque.is_empty()
    assert deque.size() == 1
    assert deque.first() == "first"
    assert deque.last() == "first"

    deque.add_last("last")
    assert deque.size() == 2
    assert deque.first() == "first"
    assert deque.last() == "last"

    # Test removals maintain order
    assert deque.remove_first() == "first"
    assert deque.size() == 1
    assert deque.first() == "last"

    assert deque.remove_last() == "last"
    assert deque.is_empty()
```

### Implementation Testing vs ADT Testing
- **Implementation Testing**: Test internal details (may change)
- **ADT Testing**: Test behavior contracts (shouldn't change)

## Design Patterns: The Wrapper Pattern

### Wrapper Pattern Structure
```python
class Wrapper:
    def __init__(self):
        self._wrapped_object = SomeClass()

    def method(self):
        # Delegate to wrapped object, possibly with modifications
        return self._wrapped_object.method()
```

### Real-World Wrapper Examples
```python
# File wrapper with automatic closing
class SafeFile:
    def __init__(self, filename, mode):
        self._file = open(filename, mode)

    def write(self, data):
        return self._file.write(data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

# Usage
with SafeFile("data.txt", "w") as f:
    f.write("Hello")  # Automatically closed

# List wrapper with bounds checking
class SafeList:
    def __init__(self):
        self._list = []

    def get(self, index):
        if index < 0 or index >= len(self._list):
            raise IndexError("Index out of bounds")
        return self._list[index]

    def append(self, item):
        self._list.append(item)
```

### Benefits of the Wrapper Pattern
1. **Interface Adaptation**: Make incompatible interfaces work together
2. **Enhanced Functionality**: Add logging, validation, caching
3. **Implementation Swapping**: Change underlying implementation transparently
4. **Single Responsibility**: Each class has one clear purpose

## Linked List vs Array Performance Comparison

| Operation | Array/List | Singly Linked | Doubly Linked |
|-----------|------------|---------------|---------------|
| Access[i] | O(1) | O(n) | O(n) |
| Insert Head | O(n) | O(1) | O(1) |
| Insert Tail | O(1)* | O(n) | O(1) |
| Insert Middle | O(n) | O(n) | O(n) |
| Delete Head | O(n) | O(1) | O(1) |
| Delete Tail | O(1) | O(n) | O(1) |
| Delete Middle | O(n) | O(n) | O(n) |

*Amortized for dynamic arrays

### When to Use Each Structure
- **Array/List**: Random access, end operations, small datasets
- **Singly Linked**: Head operations, memory efficiency
- **Doubly Linked**: Both end operations, bidirectional traversal

## Practical Applications

### Deque Use Cases
- **Sliding Window Problems**: Maintain window of k elements
- **Palindrome Checking**: Compare from both ends
- **Browser History**: Back/forward with undo
- **Task Scheduling**: Priority-based operations

### Linked List Use Cases
- **Dynamic Memory**: No contiguous allocation needed
- **Frequent Insertions/Deletions**: Better than arrays for middle operations
- **Implementing Other ADTs**: Stacks, queues, graphs
- **Symbol Tables**: Hash tables with chaining

### Wrapper Pattern Use Cases
- **API Adaptation**: Make old APIs work with new code
- **Logging**: Add logging to existing classes
- **Caching**: Add caching to expensive operations
- **Validation**: Add input validation to existing classes

This chapter demonstrates how to build sophisticated data structures from simpler components and adapt them to different use cases through design patterns.