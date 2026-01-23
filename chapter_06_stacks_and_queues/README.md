# Chapter 6: Stacks and Queues - Abstract Data Types (ADTs)

This chapter introduces Abstract Data Types (ADTs) - specifications for data structures defined by their behavior rather than their implementation. We implement two fundamental ADTs: Stacks and Queues, along with proper error handling for edge cases.

## What is an Abstract Data Type (ADT)?

### ADT Definition
An **Abstract Data Type** is a mathematical model of a data structure that specifies:
- **Operations**: What you can do with the data structure
- **Behavior**: How operations work (contracts/preconditions/postconditions)
- **Constraints**: Rules that must be maintained
- **NOT Implementation**: How it's actually stored in memory

### ADT vs Data Structure
- **ADT**: The "what" and "how it behaves" (interface + contracts)
- **Data Structure**: The "how it's implemented" (concrete code)

**Example**: A Stack ADT specifies push/pop operations and LIFO behavior, regardless of whether it's implemented with arrays, linked lists, or something else.

### Why ADTs Matter
1. **Abstraction**: Hide implementation details from users
2. **Modularity**: Change implementation without affecting users
3. **Correctness**: Define exact behavior expectations
4. **Reusability**: Use the same ADT specification across languages/implementations

## The Stack ADT

### Stack Properties
A Stack is a Last-In-First-Out (LIFO) data structure where:
- **Push**: Add an item to the top
- **Pop**: Remove and return the top item
- **Peek/Top**: Look at the top item without removing it
- **Is Empty**: Check if the stack has no items
- **Size**: Get the number of items in the stack

### Stack Operations Contract
```python
# Stack ADT Interface
class StackADT:
    def push(self, item):
        """Add item to the top of the stack.
        Postcondition: item is now at the top, size increased by 1"""

    def pop(self):
        """Remove and return the top item.
        Precondition: stack is not empty
        Postcondition: top item removed, size decreased by 1"""

    def peek(self):
        """Return the top item without removing it.
        Precondition: stack is not empty"""

    def is_empty(self):
        """Return True if stack has no items."""

    def size(self):
        """Return the number of items in the stack."""
```

### Stack Implementation
```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
```

### Stack Usage Examples
```python
stack = Stack()

# Building a stack
stack.push("first")
stack.push("second")
stack.push("third")

print(stack.size())     # 3
print(stack.peek())     # "third" (top item)

# Using the stack (LIFO)
print(stack.pop())      # "third"
print(stack.pop())      # "second"
print(stack.size())     # 1
```

### Common Stack Applications
1. **Function Call Stack**: Programming languages use stacks to track function calls
2. **Expression Evaluation**: Converting infix to postfix notation
3. **Undo Mechanisms**: Text editors use stacks to track changes
4. **Backtracking**: Solving mazes, parsing expressions
5. **Browser History**: Back button functionality

## The Queue ADT

### Queue Properties
A Queue is a First-In-First-Out (FIFO) data structure where:
- **Enqueue**: Add an item to the back/rear
- **Dequeue**: Remove and return the front item
- **Front/Peek**: Look at the front item without removing it
- **Is Empty**: Check if the queue has no items
- **Size**: Get the number of items in the queue

### Queue Operations Contract
```python
# Queue ADT Interface
class QueueADT:
    def enqueue(self, item):
        """Add item to the back of the queue.
        Postcondition: item is now at the back, size increased by 1"""

    def dequeue(self):
        """Remove and return the front item.
        Precondition: queue is not empty
        Postcondition: front item removed, size decreased by 1"""

    def front(self):
        """Return the front item without removing it.
        Precondition: queue is not empty"""

    def is_empty(self):
        """Return True if queue has no items."""

    def size(self):
        """Return the number of items in the queue."""
```

### Queue Implementation
```python
class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)  # Remove from front

    def front(self):
        if self.is_empty():
            raise IndexError("Front of empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
```

### Queue Usage Examples
```python
queue = Queue()

# Building a queue
queue.enqueue("first")
queue.enqueue("second")
queue.enqueue("third")

print(queue.size())     # 3
print(queue.front())    # "first" (front item)

# Using the queue (FIFO)
print(queue.dequeue())  # "first"
print(queue.dequeue())  # "second"
print(queue.size())     # 1
```

### Common Queue Applications
1. **Task Scheduling**: Operating systems use queues for process scheduling
2. **Print Queues**: Printers process jobs in order received
3. **Breadth-First Search**: Graph traversal algorithm
4. **Customer Service**: Help desk ticket systems
5. **Message Queues**: Asynchronous communication between systems

## Dealing with Errors

### Exception Handling in ADTs
ADTs must handle error conditions gracefully:

```python
class SafeStack:
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at empty stack")
        return self._items[-1]
```

### Common Error Patterns
1. **Empty Collection Access**: Popping/peeking empty stack/queue
2. **Invalid Operations**: Operations that violate ADT contracts
3. **Type Errors**: Incorrect data types passed to operations

### Error Handling Strategies
1. **Raise Exceptions**: Clear error messages for programmers
2. **Return Special Values**: `None`, `-1`, etc. (but less clear)
3. **Assert Preconditions**: Fail fast on contract violations

## ADT Implementation Considerations

### Choosing the Right Data Structure
Different implementations have different performance characteristics:

#### Array/List-Based Implementation
```python
# Stack with list (Python list uses dynamic array)
class ListStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)      # O(1) amortized

    def pop(self):
        return self._items.pop()      # O(1)

# Queue with list (inefficient for dequeue)
class ListQueue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)      # O(1)

    def dequeue(self):
        return self._items.pop(0)     # O(n) - shifts all elements!
```

#### Linked Structure Implementation
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        return item
```

### Performance Trade-offs
- **List-based Stack**: O(1) push/pop, but may need resizing
- **List-based Queue**: O(1) enqueue, O(n) dequeue (bad for large queues)
- **Linked Stack**: O(1) push/pop, but extra memory per element
- **Linked Queue**: O(1) enqueue/dequeue, but more complex

## Testing ADTs

### Testing Strategy for ADTs
1. **Interface Testing**: All methods work as specified
2. **Behavior Testing**: Correct LIFO/FIFO behavior
3. **Edge Case Testing**: Empty collections, single items, large collections
4. **Error Condition Testing**: Proper exceptions for invalid operations

### Stack Testing Examples
```python
def test_stack_behavior():
    stack = Stack()

    # Initially empty
    assert stack.is_empty()
    assert stack.size() == 0

    # Push items
    stack.push(1)
    assert not stack.is_empty()
    assert stack.size() == 1
    assert stack.peek() == 1

    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2  # LIFO: last pushed is on top

    # Pop items (LIFO order)
    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.peek() == 1

    assert stack.pop() == 1
    assert stack.is_empty()

def test_stack_error_conditions():
    stack = Stack()

    # Cannot pop from empty stack
    try:
        stack.pop()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass  # Expected

    # Cannot peek at empty stack
    try:
        stack.peek()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass  # Expected
```

### Queue Testing Examples
```python
def test_queue_behavior():
    queue = Queue()

    # Initially empty
    assert queue.is_empty()
    assert queue.size() == 0

    # Enqueue items
    queue.enqueue(1)
    assert not queue.is_empty()
    assert queue.size() == 1
    assert queue.front() == 1

    queue.enqueue(2)
    assert queue.size() == 2
    assert queue.front() == 1  # FIFO: first enqueued is at front

    # Dequeue items (FIFO order)
    assert queue.dequeue() == 1
    assert queue.size() == 1
    assert queue.front() == 2

    assert queue.dequeue() == 2
    assert queue.is_empty()
```

## ADT Design Patterns

### Factory Pattern for ADTs
```python
class ADTFactory:
    @staticmethod
    def create_stack(implementation="list"):
        if implementation == "list":
            return ListStack()
        elif implementation == "linked":
            return LinkedStack()
        else:
            raise ValueError("Unknown stack implementation")

    @staticmethod
    def create_queue(implementation="list"):
        if implementation == "list":
            return ListQueue()
        elif implementation == "linked":
            return LinkedQueue()
        else:
            raise ValueError("Unknown queue implementation")
```

### Adapter Pattern for Existing Classes
```python
# Make a list behave like a stack
class ListAsStack:
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

    def peek(self):
        return self._list[-1]

    def is_empty(self):
        return len(self._list) == 0

    def size(self):
        return len(self._list)
```

## Real-World ADT Usage

### Stack Applications
```python
# Function call simulation
call_stack = Stack()
call_stack.push("main")
call_stack.push("function_a")
call_stack.push("function_b")

print(f"Current function: {call_stack.peek()}")  # "function_b"

# Returning from functions
call_stack.pop()  # back to function_a
call_stack.pop()  # back to main
```

### Queue Applications
```python
# Print job queue
print_queue = Queue()
print_queue.enqueue("document1.pdf")
print_queue.enqueue("document2.pdf")
print_queue.enqueue("document3.pdf")

# Process print jobs in order
while not print_queue.is_empty():
    job = print_queue.dequeue()
    print(f"Printing: {job}")
```

### Complex Data Structures Using ADTs
```python
# Stack-based expression evaluation
def evaluate_postfix(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            # ... other operators

    return stack.pop()
```

This foundation in ADTs provides the basis for understanding more complex data structures and algorithms in subsequent chapters.