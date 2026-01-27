#!/usr/bin/env python3
"""
Chapter 9: Recursion - Recursion vs Iteration Comparison

This script compares recursive and iterative implementations
to show when each approach is appropriate.
"""

import time


def factorial_iterative(n):
    """Calculate factorial iteratively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_iterative(n):
    """Calculate fibonacci iteratively."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    """Calculate fibonacci recursively."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def sum_list_iterative(numbers):
    """Sum list iteratively."""
    total = 0
    for num in numbers:
        total += num
    return total


def sum_list_recursive(numbers):
    """Sum list recursively."""
    if not numbers:
        return 0
    return numbers[0] + sum_list_recursive(numbers[1:])


def reverse_list_iterative(items):
    """Reverse list iteratively."""
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


def reverse_list_recursive(items):
    """Reverse list recursively."""
    if not items:
        return []
    return [items[-1]] + reverse_list_recursive(items[:-1])


def binary_search_iterative(arr, target):
    """Binary search iteratively."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """Binary search recursively."""
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


def time_function(func, *args, **kwargs):
    """Time a function execution."""
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start


def compare_implementations():
    """Compare recursive vs iterative implementations."""
    print("Recursion vs Iteration Comparison")
    print("=" * 50)

    # Test data
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Factorial comparison
    print("\n1. Factorial Calculation (n=10)")
    fact_iter, time_iter = time_function(factorial_iterative, 10)
    fact_rec, time_rec = time_function(factorial_recursive, 10)
    print(f"  Iterative: {fact_iter} (time: {time_iter:.6f}s)")
    print(f"  Recursive: {fact_rec} (time: {time_rec:.6f}s)")
    print(f"  Same result: {fact_iter == fact_rec}")

    # Fibonacci comparison (small n for recursive due to exponential time)
    print("\n2. Fibonacci Calculation (n=20)")
    fib_iter, time_iter = time_function(fibonacci_iterative, 20)
    fib_rec, time_rec = time_function(fibonacci_recursive, 20)
    print(f"  Iterative: {fib_iter} (time: {time_iter:.6f}s)")
    print(f"  Recursive: {fib_rec} (time: {time_rec:.6f}s)")
    print(f"  Same result: {fib_iter == fib_rec}")

    # List sum comparison
    print("\n3. List Sum")
    sum_iter, time_iter = time_function(sum_list_iterative, test_numbers)
    sum_rec, time_rec = time_function(sum_list_recursive, test_numbers)
    print(f"  Iterative: {sum_iter} (time: {time_iter:.6f}s)")
    print(f"  Recursive: {sum_rec} (time: {time_rec:.6f}s)")
    print(f"  Same result: {sum_iter == sum_rec}")

    # List reverse comparison
    print("\n4. List Reverse")
    rev_iter, time_iter = time_function(reverse_list_iterative, test_numbers)
    rev_rec, time_rec = time_function(reverse_list_recursive, test_numbers)
    print(f"  Iterative: {rev_iter} (time: {time_iter:.6f}s)")
    print(f"  Recursive: {rev_rec} (time: {time_rec:.6f}s)")
    print(f"  Same result: {rev_iter == rev_rec}")

    # Binary search comparison
    print("\n5. Binary Search (target=11)")
    bs_iter, time_iter = time_function(binary_search_iterative, sorted_array, 11)
    bs_rec, time_rec = time_function(binary_search_recursive, sorted_array, 11)
    print(f"  Iterative: {bs_iter} (time: {time_iter:.6f}s)")
    print(f"  Recursive: {bs_rec} (time: {time_rec:.6f}s)")
    print(f"  Same result: {bs_iter == bs_rec}")


def demonstrate_recursion_depth():
    """Demonstrate recursion depth limits."""
    print("\nRecursion Depth Demonstration")
    print("=" * 40)

    print("Python's default recursion limit:")
    import sys
    print(f"  sys.getrecursionlimit() = {sys.getrecursionlimit()}")

    print("\nTrying factorial with increasing n...")

    for n in [10, 50, 100, 500, 1000]:
        try:
            result, exec_time = time_function(factorial_recursive, n)
            print(f"  n={n}: {result} (time: {exec_time:.6f}s)")
        except RecursionError:
            print(f"  n={n}: RecursionError")
            break


def demonstrate_memoization():
    """Demonstrate the power of memoization."""
    print("\nMemoization Demonstration")
    print("=" * 40)

    # Fibonacci without memoization (exponential time)
    print("Fibonacci(35) without memoization:")
    try:
        result, exec_time = time_function(fibonacci_recursive, 35)
        print(f"  Result: {result} (time: {exec_time:.6f}s)")
    except RecursionError:
        print("  RecursionError (too slow/deep)")

    # With memoization
    print("\nFibonacci(35) with memoization:")
    memo = {}
    def fib_memo(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_memo(n-1) + fib_memo(n-2)
        memo[n] = result
        return result

    result, exec_time = time_function(fib_memo, 35)
    print(f"  Result: {result} (time: {exec_time:.6f}s)")
def main():
    """Run all demonstrations."""
    print("Chapter 9: Recursion - Implementation Comparison")

    compare_implementations()
    demonstrate_recursion_depth()
    demonstrate_memoization()

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. For most problems, iteration is faster and safer")
    print("2. Recursion shines when:")
    print("   - Problem has natural recursive structure (trees, graphs)")
    print("   - Code clarity is more important than performance")
    print("   - Working with recursive data structures")
    print("3. Always define base cases clearly")
    print("4. Consider memoization for exponential recursive algorithms")
    print("5. Be aware of recursion depth limits")


if __name__ == '__main__':
    main()
