"""
Chapter 9: Recursion - Basic Recursive Functions

This module demonstrates fundamental recursive algorithms including:
- Factorial calculation
- Fibonacci sequence
- Sum of list elements
- List reversal
- Binary search
"""

def factorial(n):
    """
    Calculate n! using recursion.

    Args:
        n: Non-negative integer

    Returns:
        n! (n factorial)

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n: Non-negative integer

    Returns:
        nth Fibonacci number (F(0)=0, F(1)=1, F(2)=1, F(3)=2, etc.)

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(6)
        8
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoization to optimize performance.

    Args:
        n: Non-negative integer
        memo: Dictionary for caching results (internal use)

    Returns:
        nth Fibonacci number

    Examples:
        >>> fibonacci_memoized(6)
        8
        >>> fibonacci_memoized(50)  # Much faster than naive version
        12586269025
    """
    if memo is None:
        memo = {}

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n in memo:
        return memo[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)

    memo[n] = result
    return result


def sum_list_recursive(numbers):
    """
    Calculate the sum of all elements in a list using recursion.

    Args:
        numbers: List of numbers

    Returns:
        Sum of all elements

    Examples:
        >>> sum_list_recursive([1, 2, 3, 4, 5])
        15
        >>> sum_list_recursive([])
        0
    """
    if not numbers:  # Base case: empty list
        return 0
    else:  # Recursive case: head + sum of tail
        return numbers[0] + sum_list_recursive(numbers[1:])


def reverse_list_recursive(items):
    """
    Reverse a list using recursion.

    Args:
        items: List to reverse

    Returns:
        New list with elements in reverse order

    Examples:
        >>> reverse_list_recursive([1, 2, 3, 4])
        [4, 3, 2, 1]
        >>> reverse_list_recursive([])
        []
    """
    if not items:  # Base case: empty list
        return []
    else:  # Recursive case: last element + reverse of rest
        return [items[-1]] + reverse_list_recursive(items[:-1])


def binary_search_recursive(arr, target, low=0, high=None):
    """
    Perform binary search on a sorted array using recursion.

    Args:
        arr: Sorted list of elements
        target: Element to search for
        low: Lower bound index (internal use)
        high: Upper bound index (internal use)

    Returns:
        Index of target if found, -1 otherwise

    Examples:
        >>> binary_search_recursive([1, 3, 5, 7, 9], 5)
        2
        >>> binary_search_recursive([1, 3, 5, 7, 9], 6)
        -1
    """
    if high is None:
        high = len(arr) - 1

    if low > high:  # Base case: element not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:  # Base case: element found
        return mid
    elif arr[mid] > target:  # Search left half
        return binary_search_recursive(arr, target, low, mid - 1)
    else:  # Search right half
        return binary_search_recursive(arr, target, mid + 1, high)


def power(base, exponent):
    """
    Calculate base^exponent using recursion.

    Args:
        base: Number to raise to power
        exponent: Non-negative integer exponent

    Returns:
        base^exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    if exponent == 0:  # Base case: x^0 = 1
        return 1
    else:  # Recursive case: x^n = x * x^(n-1)
        return base * power(base, exponent - 1)


def gcd(a, b):
    """
    Calculate the greatest common divisor using Euclid's algorithm (recursive).

    Args:
        a, b: Positive integers

    Returns:
        Greatest common divisor of a and b

    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 75)
        25
    """
    if b == 0:  # Base case
        return a
    else:  # Recursive case: gcd(a, b) = gcd(b, a % b)
        return gcd(b, a % b)


def count_elements_recursive(items):
    """
    Count the number of elements in a list using recursion.

    Args:
        items: List to count elements in

    Returns:
        Number of elements in the list

    Examples:
        >>> count_elements_recursive([1, 2, 3, 4])
        4
        >>> count_elements_recursive([])
        0
    """
    if not items:  # Base case: empty list
        return 0
    else:  # Recursive case: 1 + count of rest
        return 1 + count_elements_recursive(items[1:])