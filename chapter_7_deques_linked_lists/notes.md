# Personal Notes for Chapter 7

## Key Concepts Explained

### Linked Lists vs Arrays
- **Arrays**: Contiguous memory, O(1) access, O(n) insertions
- **Linked Lists**: Scattered memory, O(n) access, O(1) insertions at ends
- **Trade-offs**: Memory efficiency vs access speed

### Deque ADT
- **Double-ended operations**: Add/remove from both ends
- **Flexibility**: Can be used as stack or queue
- **Implementation**: Doubly linked list for O(1) operations at both ends

### Wrapper Pattern
- **Purpose**: Adapt interfaces or add functionality
- **Queue from LinkedList**: Hide implementation details
- **Benefits**: Implementation hiding, interface adaptation

## Key Takeaways
- **Choose data structures based on access patterns**: Different operations have different costs
- **Linked structures excel at insertions/deletions**: Especially at ends
- **Caching length is crucial**: O(1) length queries are important
- **Wrapper pattern enables reuse**: Adapt existing classes to new interfaces
- **ADT contracts drive testing**: Test behavior, not implementation

## Performance Patterns
- **LinkedList**: O(1) ends, O(n) middle, O(n) access
- **Deque**: O(1) all end operations
- **Wrapper**: Same performance as wrapped object

## Implementation Insights
- **Node references**: next/prev pointers enable traversal
- **Head/tail tracking**: Enables O(1) end operations
- **Size caching**: Avoids O(n) length calculations
- **Error handling**: Consistent with ADT contracts

## My Understanding
Linked structures provide flexibility that arrays can't match, especially for dynamic operations. The wrapper pattern shows how to build complex systems from simpler components while maintaining clean interfaces.