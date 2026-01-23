# Personal Notes for Chapter 11: Binary Search

## Key Concepts Explained

### The Binary Search Paradigm
- **Divide and conquer**: Cut the problem in half each time
- **Logarithmic efficiency**: From linear search's O(n) to O(log n)
- **Sorted prerequisite**: The magic ingredient that makes it all possible
- **Invariant maintenance**: Keep the search space "valid" throughout

### Why Binary Search is Beautiful
- **Predictable performance**: Always O(log n), no worst-case surprises
- **Space efficient**: O(1) space for iterative, O(log n) for recursive
- **Elegant simplicity**: Few lines of code, huge performance gains
- **Teaches precision**: Off-by-one errors are the enemy

### The Core Algorithm (Iterative)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:  # Note: <= not <
        mid = left + (right - left) // 2  # Prevents overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1
```
- **left**: Start of current search range
- **right**: End of current search range
- **mid**: Middle point calculation (careful with overflow!)
- **Loop condition**: `left <= right` ensures we don't miss the last element

### Common Pitfalls I Keep Making
1. **Wrong loop condition**: `while left < right` → infinite loops
2. **Mid calculation**: `mid = (left + right) // 2` → integer overflow
3. **Boundary updates**: `right = mid` vs `right = mid - 1`
4. **Return values**: -1 for not found, but what about insertion points?

### Binary Search Variants
- **First occurrence**: When duplicates exist, find the leftmost match
- **Last occurrence**: Find the rightmost match
- **Lower bound**: First position >= target
- **Upper bound**: First position > target
- **All variants use the same core logic but different termination conditions**

### Real-World Applications That Surprised Me
- **Square root calculation**: Binary search between 0 and x
- **Capacity problems**: "What's the maximum/minimum capacity that works?"
- **Search in rotated arrays**: Find pivot, then search appropriate half
- **Median finding**: Efficiently find median in multiple sorted arrays

## Examples That Clicked

### Square Root with Binary Search
```python
def sqrt_binary_search(x):
    if x < 0: raise ValueError
    if x == 0 or x == 1: return x

    left, right = 0, x
    precision = 1e-6  # For floating point

    while right - left > precision:
        mid = (left + right) / 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid
        else:
            right = mid

    return (left + right) / 2
```
- **Integer overflow prevention**: Use floating point for bounds
- **Precision handling**: Stop when difference is small enough
- **Unimodal function**: Square increases, so binary search works perfectly

### Search in Rotated Sorted Array
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Check which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Search right half
            else:
                right = mid - 1  # Search left half

    return -1
```
- **Rotated array property**: One half is always sorted
- **Pivot detection**: Find which half contains the target
- **Standard binary search with extra logic**

## Performance Insights
- **Theoretical**: O(log n) is unbeatable for search in sorted data
- **Practical**: Binary search is fast even for huge arrays (log₂(1e9) ≈ 30 comparisons)
- **Cache friendly**: Few cache misses due to sequential access patterns
- **Branch prediction**: Modern CPUs predict binary search branches well

## When Binary Search Fails
- **Unsorted data**: Obvious, but sometimes data looks sorted but isn't
- **Linked lists**: No random access → linear search is better
- **Small arrays**: Linear search might be faster due to lower constants
- **Dynamic data**: Insertions/deletions break sorted order

## Advanced Variants I Want to Explore
- **Interpolation search**: For uniformly distributed data
- **Exponential search**: When you don't know the bounds
- **Ternary search**: For 3-way splits (useful for some optimization problems)
- **Binary search on answer**: Solve "maximize/minimize with constraint" problems

## My Thoughts
- Binary search feels like a superpower - you eliminate half the possibilities each time
- The precision required teaches careful thinking about boundaries
- Once you see the pattern, you start applying it to all kinds of problems
- It's a gateway drug to algorithmic thinking

## Exercises/Thoughts
- Implement all the variants (first/last occurrence, bounds)
- Practice on LeetCode binary search problems
- Try implementing square root and other math functions with binary search
- Think about how binary search applies to tree data structures
- Consider: "What problems can be solved by binary search on the answer space?"</content>
<parameter name="filePath">chapter_11_binary_search/notes.md