# Chapter 11: Binary Search - Divide and Conquer Search

This chapter explores binary search, one of the most fundamental and elegant algorithms in computer science. Binary search demonstrates the power of the divide-and-conquer paradigm, achieving logarithmic time complexity by systematically eliminating half the search space at each step.

## What is Binary Search?

Binary search is an efficient algorithm for finding an element in a **sorted array** by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; if greater, it continues in the upper half.

### Core Requirements:
1. **Sorted Array**: Elements must be in ascending order
2. **Random Access**: Array must support O(1) element access
3. **Comparable Elements**: Elements must be comparable

## Basic Binary Search Algorithm

### Iterative Implementation
```python
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found
```

### Recursive Implementation
```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

## Binary Search Variants

### 1. **First Occurrence**
Finds the first occurrence of a duplicate element.

### 2. **Last Occurrence**
Finds the last occurrence of a duplicate element.

### 3. **Lower Bound / Insertion Point**
Finds the position where the target should be inserted to maintain sorted order.

### 4. **Upper Bound**
Finds the first position where elements are greater than the target.

## Applications Beyond Basic Search

### 1. **Square Root Calculation**
Finding the square root of a number using binary search.

### 2. **Peak Finding**
Finding a peak element in an array (element greater than its neighbors).

### 3. **Search in Rotated Sorted Array**
Searching in an array that was rotated at some pivot point.

### 4. **Median of Two Sorted Arrays**
Finding the median efficiently in two sorted arrays.

### 5. **Capacity Problems**
- Maximum capacity that satisfies a condition
- Minimum capacity that satisfies a condition

## Advanced Search Algorithms

### 1. **Exponential Search**
- Also called "galloping search" or "doubling search"
- Finds the range where the element exists, then performs binary search
- Useful when array size is unknown

### 2. **Interpolation Search**
- Uses interpolation formula instead of mid-point calculation
- Performs better when elements are uniformly distributed
- Worst case O(n), best case O(log log n)

### 3. **Ternary Search**
- Divides array into three parts instead of two
- Useful for unimodal functions (functions with single peak)

## Time and Space Complexity

### Time Complexity:
- **Best Case**: O(1) - element found at middle
- **Average Case**: O(log n) - logarithmic time
- **Worst Case**: O(log n) - element not found or at extreme

### Space Complexity:
- **Iterative**: O(1) - constant space
- **Recursive**: O(log n) - recursion stack depth

### Comparison with Other Search Algorithms:
| Algorithm | Time Complexity | Space Complexity | Requirements |
|-----------|----------------|------------------|--------------|
| Linear Search | O(n) | O(1) | None |
| Binary Search | O(log n) | O(1) | Sorted array |
| Interpolation | O(log log n)* | O(1) | Uniform distribution |
| Exponential | O(log n) | O(1) | Sorted array |

*Worst case O(n)

## Implementation Considerations

### Edge Cases to Handle:
1. **Empty array**: Return -1
2. **Single element**: Check if it matches target
3. **Target not in array**: Return -1
4. **Duplicate elements**: Depends on variant needed
5. **Large arrays**: Avoid integer overflow in mid calculation

### Integer Overflow Prevention:
```python
# Instead of: mid = (left + right) // 2
mid = left + (right - left) // 2  # Prevents overflow
```

### Floating Point Arrays:
Binary search works with floating point numbers, but be careful with precision.

## Real-World Applications

### 1. **Database Indexing**
- B-trees and B+ trees use binary search principles
- Database indexes for fast lookups

### 2. **File Systems**
- Directory lookups in file systems
- Binary search in sorted file indexes

### 3. **Compiler Design**
- Symbol table lookups
- Binary search in parse tables

### 4. **Scientific Computing**
- Root finding algorithms
- Optimization problems with unimodal functions

### 5. **Game Development**
- AI pathfinding with binary search variants
- Game state search in decision trees

### 6. **Networking**
- IP address lookups in routing tables
- Binary search in network packet classification

## Binary Search in Other Data Structures

### 1. **Binary Search Trees (BST)**
- Binary search forms the basis of BST operations
- O(log n) search, insert, delete operations

### 2. **Skip Lists**
- Probabilistic data structure using binary search principles

### 3. **Segment Trees**
- Range query data structures using binary search for navigation

## Common Mistakes and Debugging

### 1. **Off-by-One Errors**
```python
# Wrong: mid = (left + right) / 2
mid = left + (right - left) // 2  # Correct

# Wrong: right = mid or left = mid
right = mid - 1  # Correct for left half search
left = mid + 1   # Correct for right half search
```

### 2. **Infinite Loops**
```python
# Wrong: while left < right  (can cause infinite loop)
while left <= right:  # Correct
```

### 3. **Not Handling Duplicates**
- Decide whether to return first, last, or any occurrence
- Consider the problem requirements

### 4. **Array Bounds**
- Always check array bounds before access
- Handle empty arrays and single-element arrays

## Performance Analysis

### When Binary Search Excels:
- **Large sorted datasets**: O(log n) vs O(n) for linear search
- **Frequent searches**: Amortized cost is very low
- **Memory-constrained**: O(1) space complexity
- **Predictable performance**: No worst-case surprises

### Limitations:
- **Requires sorted data**: O(n log n) sort cost may outweigh benefits
- **Not suitable for linked lists**: No random access
- **Insertion/deletion costly**: Maintaining sorted order is expensive

## The Binary Search Mindset

Binary search teaches a fundamental problem-solving approach:
- **Systematic elimination**: Remove half the possibilities each step
- **Invariant maintenance**: Keep the search space valid throughout
- **Precision over brute force**: Smart choices beat exhaustive search

This divide-and-conquer thinking extends far beyond array search, influencing algorithm design across computer science.</content>
<parameter name="filePath">chapter_11_binary_search/README.md