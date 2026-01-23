#!/usr/bin/env python3
"""
Chapter 9: Recursion - Interactive Examples

This script demonstrates various recursive concepts with interactive examples.
Run this script to see recursion in action!
"""

import sys
import os
import time

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from recursive_functions import (
    factorial,
    fibonacci,
    fibonacci_memoized,
    sum_list_recursive,
    reverse_list_recursive,
    binary_search_recursive,
    power,
    gcd,
    count_elements_recursive
)


def demonstrate_factorial():
    """Demonstrate factorial calculation with step-by-step explanation."""
    print("\n" + "="*60)
    print("FACTORIAL CALCULATION")
    print("="*60)

    print("Factorial n! = n × (n-1) × (n-2) × ... × 1")
    print("Recursive definition: n! = n × (n-1)!")
    print("Base case: 0! = 1")
    print()

    for n in [0, 1, 2, 3, 4, 5]:
        result = factorial(n)
        print("3d")

    print("\nLet's trace factorial(4):")
    print("factorial(4) = 4 × factorial(3)")
    print("            = 4 × (3 × factorial(2))")
    print("            = 4 × (3 × (2 × factorial(1)))")
    print("            = 4 × (3 × (2 × (1 × factorial(0))))")
    print("            = 4 × (3 × (2 × (1 × 1)))")
    print("            = 4 × (3 × (2 × 1))")
    print("            = 4 × (3 × 2)")
    print("            = 4 × 6")
    print("            = 24")


def demonstrate_fibonacci():
    """Demonstrate Fibonacci sequence and performance comparison."""
    print("\n" + "="*60)
    print("FIBONACCI SEQUENCE")
    print("="*60)

    print("Fibonacci: F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)")
    print("Exponential recursion vs memoized optimization")
    print()

    print("First 10 Fibonacci numbers:")
    for n in range(10):
        fib = fibonacci(n)
        print("3d")

    print("\nPerformance comparison for F(35):")
    print("(This demonstrates why memoization is important!)")

    # Time naive version (only for small n to avoid long wait)
    start = time.time()
    result_naive = fibonacci(30)  # Using smaller n for demo
    naive_time = time.time() - start

    # Time memoized version
    start = time.time()
    result_memo = fibonacci_memoized(35)
    memo_time = time.time() - start

    print(".4f")
    print(".4f")
    print(".1f")


def demonstrate_list_operations():
    """Demonstrate recursive list operations."""
    print("\n" + "="*60)
    print("RECURSIVE LIST OPERATIONS")
    print("="*60)

    # Sum demonstration
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = sum_list_recursive(numbers)
    print(f"Sum of {numbers} = {total}")

    # Count demonstration
    count = count_elements_recursive(numbers)
    print(f"Count of elements in {numbers} = {count}")

    # Reverse demonstration
    original = ['a', 'b', 'c', 'd', 'e']
    reversed_list = reverse_list_recursive(original)
    print(f"Original: {original}")
    print(f"Reversed: {reversed_list}")
    print(f"Original unchanged: {original}")


def demonstrate_binary_search():
    """Demonstrate recursive binary search."""
    print("\n" + "="*60)
    print("RECURSIVE BINARY SEARCH")
    print("="*60)

    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Search array: {arr}")

    test_values = [5, 13, 1, 19, 10, 25]

    for target in test_values:
        index = binary_search_recursive(arr, target)
        if index != -1:
            print(f"Found {target} at index {index}")
        else:
            print(f"{target} not found in array")


def demonstrate_power_and_gcd():
    """Demonstrate power and GCD calculations."""
    print("\n" + "="*60)
    print("POWER AND GCD CALCULATIONS")
    print("="*60)

    # Power demonstration
    print("Power calculations:")
    for base, exp in [(2, 5), (3, 3), (5, 2), (7, 0)]:
        result = power(base, exp)
        print("2d")

    # GCD demonstration
    print("\nGCD (Greatest Common Divisor) calculations:")
    pairs = [(48, 18), (100, 75), (17, 13), (24, 24)]
    for a, b in pairs:
        result = gcd(a, b)
        print(f"GCD({a:2d}, {b:2d}) = {result}")


def demonstrate_call_stack():
    """Demonstrate call stack visualization."""
    print("\n" + "="*60)
    print("CALL STACK VISUALIZATION")
    print("="*60)

    print("Let's trace factorial(3) call stack:")
    print()
    print("Call stack grows:")
    print("factorial(3)")
    print("  ↓")
    print("factorial(3) → 3 × factorial(2)")
    print("  ↓")
    print("factorial(2) → 2 × factorial(1)")
    print("  ↓")
    print("factorial(1) → 1 × factorial(0)")
    print("  ↓")
    print("factorial(0) → 1  ← Base case reached!")
    print()
    print("Call stack unwinds:")
    print("factorial(0) returns 1")
    print("factorial(1) returns 1 × 1 = 1")
    print("factorial(2) returns 2 × 1 = 2")
    print("factorial(3) returns 3 × 2 = 6")
    print()
    print(f"Final result: {factorial(3)}")


def main():
    """Run all demonstrations."""
    print("Chapter 9: Recursion - Interactive Examples")
    print("This script demonstrates recursive algorithms and concepts.")

    demonstrate_factorial()
    demonstrate_fibonacci()
    demonstrate_list_operations()
    demonstrate_binary_search()
    demonstrate_power_and_gcd()
    demonstrate_call_stack()

    print("\n" + "="*60)
    print("EXERCISES FOR YOU:")
    print("="*60)
    print("1. Try implementing iterative versions of these functions")
    print("2. Add memoization to the binary search (though it's not needed)")
    print("3. Implement recursive string reversal")
    print("4. Create a recursive function to check if a string is a palindrome")
    print("5. Implement recursive tree traversal (we'll see this in later chapters)")


if __name__ == '__main__':
    main()</content>
<parameter name="filePath">chapter_9_recursion/examples/recursion_demo.py