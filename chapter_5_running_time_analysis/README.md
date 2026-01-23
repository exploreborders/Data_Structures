# Chapter 5: Running Time Analysis - Understanding Algorithm Efficiency

This chapter introduces the science of analyzing how long programs take to run and how to compare the efficiency of different algorithms. Understanding algorithmic complexity is crucial for writing scalable software that performs well with large inputs.

## Why Algorithm Analysis Matters

### The Problem with Intuition
```python
# Which is faster?
def sum_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

def sum_formula(n):
    return n * (n + 1) // 2

# For small n (100), both are fast
# For large n (1,000,000), the loop is much slower
```

### Real-World Impact
- **Web applications**: Handle thousands of concurrent users
- **Data processing**: Work with millions of records
- **Mobile apps**: Run on limited hardware
- **Scientific computing**: Process massive datasets

Poor algorithm choices can make systems unusable at scale.

## Timing Programs: Measuring Actual Performance

### Basic Timing Techniques
```python
import time

def time_function(func, *args, **kwargs):
    """Time how long a function takes to execute."""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    duration = end_time - start_time
    return result, duration

# Example usage
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

result, time_taken = time_function(slow_sum, 100000)
print(f"Result: {result}, Time: {time_taken:.4f} seconds")
```

### Timing Challenges
- **System variability**: Other programs affect measurements
- **Input size dependency**: Performance changes with problem size
- **Hardware differences**: Code runs differently on different machines
- **Constant factors**: Small differences in fast operations

### Better Timing: `timeit` Module
```python
import timeit

# Time a simple expression
time_taken = timeit.timeit('sum(range(1000))', number=1000)
print(f"Average time per execution: {time_taken/1000:.6f} seconds")

# Time a function
def my_function():
    return sum(range(1000))

time_taken = timeit.timeit(my_function, number=1000)
print(f"Average time: {time_taken/1000:.6f} seconds")
```

## Modeling Running Time: Counting Operations

### Operation Counting
Instead of measuring time, count the number of basic operations.

```python
def count_operations_sum(n):
    """
    Count operations in sum calculation.
    Each iteration: 1 comparison + 1 addition + 1 assignment
    """
    operations = 0

    total = 0  # 1 assignment
    operations += 1

    i = 0  # 1 assignment
    operations += 1

    while i < n:  # n+1 comparisons
        operations += 1

        total += i  # 1 addition + 1 assignment
        operations += 2

        i += 1  # 1 addition + 1 assignment
        operations += 2

    return total, operations

result, ops = count_operations_sum(5)
print(f"Result: {result}, Operations: {ops}")
# Result: 10, Operations: ~20 (exact count depends on implementation)
```

### Common Operation Counts

#### List Operations
```python
# O(1) - Constant time
my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]        # Always 1 operation
last_element = my_list[-1]        # Always 1 operation
list_length = len(my_list)        # Always 1 operation

# O(n) - Linear time
total = sum(my_list)              # n additions
found = 42 in my_list             # Up to n comparisons
max_value = max(my_list)          # n comparisons

# O(n²) - Quadratic time (nested loops)
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if my_list[i] == my_list[j]:
            # Do something
            pass
```

#### Dictionary Operations
```python
# O(1) - Average case constant time
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict['a']              # Usually 1 operation (hash lookup)
my_dict['d'] = 4                  # Usually 1 operation
exists = 'a' in my_dict           # Usually 1 operation

# O(n) - Worst case (hash collisions)
# In rare cases, all operations above become O(n)
```

#### Set Operations
```python
# O(1) - Average case constant time
my_set = {1, 2, 3, 4, 5}
added = my_set.add(6)             # Usually 1 operation
exists = 3 in my_set              # Usually 1 operation

# O(n) - Linear operations
union = my_set | {6, 7, 8}        # n operations
intersection = my_set & {2, 3, 6} # n operations
```

## Asymptotic Analysis: Focusing on Growth Rate

### The Problem with Exact Counting
- **Implementation details**: Different languages/compilers count differently
- **Hardware variations**: Same operations faster/slower on different machines
- **Constant factors**: Don't matter for large inputs

### Big-O Notation: Growth Rate Analysis
Big-O describes how an algorithm's performance grows as input size increases.

**Definition**: f(n) = O(g(n)) means there exist constants c and n₀ such that:
- For all n ≥ n₀, f(n) ≤ c × g(n)

```python
# O(1) - Constant time: Performance doesn't change with input size
def get_first_element(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic time: Performance grows slowly
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear time: Performance grows proportionally to input size
def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic time: Performance grows with square of input size
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# O(2ⁿ) - Exponential time: Performance doubles with each input increase
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

### Common Big-O Classes (Ordered by Growth Rate)

| Complexity | Name | Example | Description |
|------------|------|---------|-------------|
| O(1) | Constant | Array access | Same time regardless of input size |
| O(log n) | Logarithmic | Binary search | Time doubles when input size doubles |
| O(n) | Linear | Linear search | Time proportional to input size |
| O(n log n) | Linearithmic | Merge sort | Most efficient comparison sorts |
| O(n²) | Quadratic | Bubble sort | Nested loops over input |
| O(n³) | Cubic | Matrix multiplication | Triple nested loops |
| O(2ⁿ) | Exponential | Subset generation | Time doubles for each additional element |
| O(n!) | Factorial | Traveling salesman | Grows extremely fast |

### Analyzing Complex Algorithms

#### Rule 1: Focus on Dominant Term
Ignore lower-order terms and constants:
- O(n² + 3n + 5) = O(n²)
- O(2n³ + n² + 1000n + 50000) = O(n³)

#### Rule 2: Analyze Loops
- Simple loop: O(n)
- Nested loops: O(n²), O(n³), etc.
- Logarithmic loops: O(log n)

#### Rule 3: Function Calls
Consider the complexity of called functions:
```python
def process_list(items):
    sort_items(items)      # O(n log n)
    for item in items:     # O(n)
        process_item(item) # Assume O(1)
    return items

# Total: O(n log n + n) = O(n log n)
```

### Practical Big-O Analysis

#### Space Complexity
Big-O applies to memory usage too:
```python
# O(1) space
def sum_array(arr):
    total = 0  # Constant space
    for num in arr:
        total += num
    return total

# O(n) space
def duplicate_array(arr):
    result = []  # Grows with input size
    for item in arr:
        result.append(item)
        result.append(item)  # Duplicate each item
    return result
```

#### Best, Average, Worst Case
```python
def linear_search(arr, target):
    """
    Best case: O(1) - target is first element
    Average case: O(n) - target is in middle
    Worst case: O(n) - target not found or is last element
    """
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
```

## Big-O: The Most Important Features

### 1. Comparative Analysis
Big-O helps compare algorithms:
```python
# Algorithm A: O(n²)
# Algorithm B: O(n log n)

# For n=1000:
# A takes ~1,000,000 operations
# B takes ~10,000 operations
# B is 100x faster!

# For n=1,000,000:
# A takes ~1,000,000,000,000 operations
# B takes ~20,000,000 operations
# B is ~50,000x faster!
```

### 2. Scalability Prediction
Predict performance for larger inputs:
```python
# Current system handles 1000 users with O(n²) algorithm
# How many users can it handle with O(n) algorithm?

# O(n²) for 1000 users: 1,000,000 operations
# O(n) needs 1,000,000 operations for: n = 1,000,000 users
# 1000x scalability improvement!
```

### 3. Algorithm Selection Guide
```python
# Problem size considerations
if n <= 10:
    # Any algorithm works
    pass
elif n <= 1000:
    # O(n²) might be acceptable
    pass
elif n <= 100000:
    # Prefer O(n log n)
    pass
else:
    # Must use O(n) or better
    pass
```

## Practical Use of Big-O

### Real-World Algorithm Selection

#### Sorting Algorithms
```python
# Small arrays (n < 50): Insertion sort O(n²) - simple and fast
# Medium arrays (n < 10000): Quicksort O(n log n) - good average case
# Large arrays: Mergesort O(n log n) - guaranteed performance
# Nearly sorted: Timsort O(n log n) - hybrid approach
```

#### Search Algorithms
```python
# Unsorted data: Linear search O(n)
# Sorted data: Binary search O(log n)
# Hash table: Dictionary lookup O(1) average
```

#### Graph Algorithms
```python
# Shortest path: Dijkstra O((V+E) log V)
# Minimum spanning tree: Kruskal O(E log E)
# All pairs shortest paths: Floyd-Warshall O(V³)
```

### Performance Optimization Strategies

#### 1. Algorithm Improvement
```python
# Before: O(n²) nested loops
def has_duplicates_slow(items):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j]:
                return True
    return False

# After: O(n) with set
def has_duplicates_fast(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False
```

#### 2. Data Structure Selection
```python
# Need fast lookups: Use dict/set O(1) instead of list O(n)
# Need ordered data: Use list O(1) access instead of dict O(1) average
# Need unique items: Use set instead of list with manual checking
```

#### 3. Caching and Memoization
```python
# Cache expensive computations
cache = {}
def expensive_function(n):
    if n in cache:
        return cache[n]  # O(1) lookup
    result = slow_computation(n)  # O(n²) or worse
    cache[n] = result
    return result
```

## Common Functions and Their Complexities

### List Operations
```python
my_list = [1, 2, 3, 4, 5]

# O(1) - Constant time
len(my_list)           # Length lookup
my_list[0]             # Index access
my_list.append(6)      # Add to end

# O(n) - Linear time
sum(my_list)           # Sum all elements
42 in my_list          # Membership test
my_list.insert(0, 0)   # Insert at beginning (shifts elements)

# O(k) - Depends on slice size
my_list[1:4]           # Slicing
```

### Dictionary Operations
```python
my_dict = {'a': 1, 'b': 2}

# O(1) average case - Hash table lookup
my_dict['c'] = 3       # Insert
value = my_dict['a']   # Access
'a' in my_dict         # Membership

# O(n) worst case - Hash collisions
# O(n) for iteration
for key, value in my_dict.items():
    print(key, value)
```

### Set Operations
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# O(1) average case
set1.add(5)            # Add element
4 in set1              # Membership

# O(n) - Linear time
len(set1 | set2)       # Union size
set1 & set2            # Intersection
```

## Logarithms in Algorithm Analysis

### What is a Logarithm?
A logarithm answers: "To what power must I raise this base to get this number?"

- log₂(8) = 3 because 2³ = 8
- log₂(16) = 4 because 2⁴ = 16
- log₁₀(100) = 2 because 10² = 100

### Why Logarithms Matter in Algorithms
Many algorithms divide problems in half each step:
```python
def binary_search(arr, target):
    """
    Each iteration eliminates half the remaining elements
    log₂(n) iterations to find target or determine it's not present
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Base of Logarithm in Big-O
In algorithm analysis, the base doesn't matter because:
log₂(n) = log₁₀(n) / log₁₀(2) ≈ log₁₀(n) × 3.32

So O(log₂ n) = O(log₁₀ n) = O(log n)

**Exception**: When the algorithm depends on the base (rare):
- Binary search tree height: O(log₂ n)
- Base conversion algorithms: Depends on base used

## Practice Examples: Analyzing Real Code

### Example 1: String Processing
```python
def count_vowels(text):
    """Count vowels in a string."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:          # O(n)
        if char in vowels:     # O(1)
            count += 1         # O(1)
    return count

# Total: O(n) - Linear in string length
```

### Example 2: Matrix Operations
```python
def matrix_multiply(A, B):
    """Multiply two matrices."""
    result = []
    for i in range(len(A)):           # O(n)
        row = []
        for j in range(len(B[0])):    # O(p)
            sum = 0
            for k in range(len(A[0])):  # O(m)
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

# Total: O(n × m × p) where n,p are matrix dimensions and m is shared dimension
```

### Example 3: Recursive Algorithms
```python
def fibonacci_recursive(n):
    """Compute nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Time complexity: O(2ⁿ) - Exponential!
# Each call spawns 2 more calls, creating a tree of calls

def fibonacci_memoized(n, memo={}):
    """Compute nth Fibonacci number with memoization."""
    if n in memo:
        return memo[n]    # O(1)
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Time complexity: O(n) - Each value computed only once
```

### Example 4: Sorting Comparison
```python
# O(n²) - Quadratic sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# O(n log n) - Efficient sorting
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# For n=1000 elements:
# Bubble sort: ~1,000,000 operations
# Merge sort: ~10,000 operations
# 100x performance difference!
```

## Summary: Key Takeaways

### Big-O Rules
1. **Ignore constants**: O(2n) = O(n)
2. **Ignore lower terms**: O(n² + n) = O(n²)
3. **Focus on worst case**: Unless specified otherwise
4. **Consider all inputs**: Different inputs may have different complexities

### Practical Guidelines
- **O(1)**: Ideal for frequent operations
- **O(log n)**: Excellent for large datasets
- **O(n)**: Acceptable for most applications
- **O(n log n)**: Good for sorting and similar operations
- **O(n²)**: Sometimes acceptable for small inputs
- **O(2ⁿ)**: Usually too slow except for very small inputs

### Analysis Process
1. **Identify input size**: What is "n"?
2. **Count operations**: For typical case
3. **Find dominant term**: Which operation happens most?
4. **Express in Big-O**: Use simplest accurate classification

This foundation in algorithmic analysis will help you write efficient code and make informed decisions about algorithm and data structure selection.