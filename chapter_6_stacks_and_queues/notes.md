# Personal Notes for Chapter 6

## Key Concepts Explained

### Abstract Data Types (ADTs)
- **Definition**: Specification of data structure behavior without implementation details
- **Purpose**: Separate interface from implementation for modularity and reusability
- **Benefits**: Can change implementation without affecting users

### Stack ADT
- **LIFO**: Last In, First Out - like a stack of plates
- **Operations**: push, pop, peek, is_empty, size
- **Uses**: Function calls, undo operations, expression evaluation
- **Error Handling**: Cannot pop/peek from empty stack

### Queue ADT
- **FIFO**: First In, First Out - like a line at a store
- **Operations**: enqueue, dequeue, front, is_empty, size
- **Uses**: Task scheduling, breadth-first search, print queues
- **Error Handling**: Cannot dequeue/front from empty queue

## Key Takeaways
- **ADTs define behavior**: What operations do, not how they're implemented
- **Contracts matter**: Preconditions and postconditions must be maintained
- **Error handling**: Proper exceptions for invalid operations
- **Choose right implementation**: Different data structures have different performance
- **Test thoroughly**: Edge cases and error conditions are critical

## Common Patterns
- **Stack for backtracking**: Undo, browser back button
- **Queue for fair scheduling**: Print jobs, CPU tasks
- **Stack for parsing**: Expression evaluation, syntax checking
- **Queue for BFS**: Graph traversal, level-order processing

## Implementation Trade-offs
- **List-based Stack**: Simple, O(1) operations, but may resize
- **List-based Queue**: Simple enqueue, slow dequeue (O(n))
- **Linked implementations**: Consistent O(1), but more memory

## My Understanding
ADTs are the foundation of data structures - they define the "what" while allowing flexibility in the "how". Stacks and queues are fundamental building blocks used everywhere in computing.