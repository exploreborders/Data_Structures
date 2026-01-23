#!/usr/bin/env python3
"""
Chapter 10: Dynamic Programming - Interactive Examples

This script demonstrates dynamic programming concepts with comparative examples
showing the evolution from naive approaches to optimized DP solutions.
"""

import time
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from dp_algorithms import DynamicProgramming


def time_function(func, *args, **kwargs):
    """Time a function execution and return result and time."""
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start


def demonstrate_fibonacci_evolution():
    """Show the evolution from naive recursion to optimized DP."""
    print("FIBONACCI SEQUENCE EVOLUTION")
    print("=" * 50)

    print("Computing F(35) using different approaches:\n")

    # Naive recursive (only for small n due to exponential time)
    print("1. Naive Recursion:")
    try:
        result, time_taken = time_function(DynamicProgramming.fibonacci_naive, 30)
        print(".6f"    except RecursionError:
        print("   RecursionError - too slow/deep!")

    # Memoization
    print("\n2. Memoization (Top-Down DP):")
    result, time_taken = time_function(DynamicProgramming.fibonacci_memoization, 35)
    print(".6f"
    # Tabulation
    print("\n3. Tabulation (Bottom-Up DP):")
    result, time_taken = time_function(DynamicProgramming.fibonacci_tabulation, 35)
    print(".6f"
    # Larger values
    print("\n4. Tabulation for larger values:")
    result, time_taken = time_function(DynamicProgramming.fibonacci_tabulation, 100)
    print(".6f"    print(f"   Result: {result:,} (that's a {len(str(result))}-digit number!)")

    print("\nKey Insights:")
    print("- Naive recursion: O(2^n) - exponential explosion")
    print("- Memoization: O(n) - cache prevents recomputation")
    print("- Tabulation: O(n) - systematic table filling")
    print("- Space: Memoization O(n), Tabulation O(1) for Fibonacci")


def demonstrate_knapsack_problem():
    """Demonstrate the 0/1 knapsack problem."""
    print("\n\n0/1 KNAPSACK PROBLEM")
    print("=" * 50)

    # Sample problem
    items = [
        ("Laptop", 3, 2000),
        ("Phone", 1, 1500),
        ("Book", 2, 100),
        ("Headphones", 1, 500),
        ("Tablet", 2, 800)
    ]

    weights = [item[1] for item in items]
    values = [item[2] for item in items]
    capacity = 5

    print("Items available:")
    for name, weight, value in items:
        print("15")
    print(f"\nKnapsack capacity: {capacity} kg")
    print("\nSolving with DP...")

    # Tabulation approach
    max_value, selected_indices = DynamicProgramming.knapsack_01_tabulation(
        weights, values, capacity)

    print(f"\nMaximum value: ${max_value}")
    print("Selected items:")
    total_weight = 0
    for idx in selected_indices:
        name, weight, value = items[idx]
        print("15")
        total_weight += weight

    print(f"Total weight: {total_weight}/{capacity} kg")
    print("Space utilization: {:.1f}%".format(total_weight / capacity * 100))


def demonstrate_lcs_problem():
    """Demonstrate longest common subsequence."""
    print("\n\nLONGEST COMMON SUBSEQUENCE")
    print("=" * 50)

    # Example strings
    str1 = "AGGTAB"
    str2 = "GXTXAYB"

    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print()

    length, lcs = DynamicProgramming.longest_common_subsequence(str1, str2)

    print(f"Length of LCS: {length}")
    print(f"Longest Common Subsequence: '{lcs}'")

    # Show alignment
    print("\nAlignment:")
    print(f"String 1: {str1}")
    print(f"LCS:      {'-' * (len(str1) - len(lcs))}{lcs}")

    # More examples
    examples = [
        ("ABCBDAB", "BDCABA"),
        ("XMJYAUZ", "MZJAWXU"),
        ("PROGRAMMING", "ALGORITHMS")
    ]

    print("\nMore examples:")
    for s1, s2 in examples:
        length, lcs = DynamicProgramming.longest_common_subsequence(s1, s2)
        print("12")


def demonstrate_coin_change():
    """Demonstrate coin change problems."""
    print("\n\nCOIN CHANGE PROBLEMS")
    print("=" * 50)

    coins = [1, 2, 5, 10, 25]  # US coins
    amount = 27

    print(f"Available coins: {coins}")
    print(f"Target amount: ${amount}")
    print()

    # Minimum coins
    min_coins = DynamicProgramming.coin_change_minimum(coins, amount)
    print(f"Minimum coins needed: {min_coins}")

    # Number of ways
    ways = DynamicProgramming.coin_change_ways(coins, amount)
    print(f"Number of different ways: {ways}")

    # Show one possible combination
    print("\nExample combination:")
    remaining = amount
    used_coins = []
    for coin in sorted(coins, reverse=True):
        while remaining >= coin:
            used_coins.append(coin)
            remaining -= coin

    print(f"  {used_coins} = ${amount}")

    # Edge case: impossible amount
    impossible_amount = 3
    min_coins = DynamicProgramming.coin_change_minimum([2, 4], impossible_amount)
    print(f"\nImpossible case: Make ${impossible_amount} with [2, 4] coins")
    print(f"  Result: {min_coins} (impossible)")


def demonstrate_edit_distance():
    """Demonstrate edit distance (Levenshtein distance)."""
    print("\n\nEDIT DISTANCE (Levenshtein Distance)")
    print("=" * 50)

    word_pairs = [
        ("kitten", "sitting"),
        ("saturday", "sunday"),
        ("horse", "ros"),
        ("intention", "execution")
    ]

    for word1, word2 in word_pairs:
        distance = DynamicProgramming.edit_distance(word1, word2)
        print("15")

    # Explain operations
    print("\nOperations allowed:")
    print("- Insert a character")
    print("- Delete a character")
    print("- Replace a character")
    print("\nEach operation costs 1 point.")

    # Show transformation for kitten -> sitting
    print("\nExample: kitten -> sitting (distance = 3)")
    print("kitten  -> sitten  (replace k->s)")
    print("sitten  -> sittin  (replace e->i)")
    print("sittin  -> sitting (insert g)")


def demonstrate_subset_sum():
    """Demonstrate subset sum problem."""
    print("\n\nSUBSET SUM PROBLEM")
    print("=" * 50)

    nums = [3, 34, 4, 12, 5, 2]
    targets = [9, 30, 35, 50]

    print(f"Number set: {nums}")
    print()

    for target in targets:
        exists = DynamicProgramming.subset_sum(nums, target)
        status = "✓ EXISTS" if exists else "✗ NO SUBSET"
        print("2")

        if exists:
            # Try to find one possible subset (simplified approach)
            print(f"    One possible subset: ", end="")
            subset = []
            remaining = target
            for num in sorted(nums, reverse=True):
                if num <= remaining and DynamicProgramming.subset_sum(nums, remaining - num):
                    subset.append(num)
                    remaining -= num
                    if remaining == 0:
                        break
            if sum(subset) == target:
                print(f"{subset}")
            else:
                print("Multiple combinations possible")


def demonstrate_performance_comparison():
    """Compare performance of different DP approaches."""
    print("\n\nPERFORMANCE COMPARISON")
    print("=" * 50)

    print("Testing subset sum with different target values:")
    nums = [3, 5, 7, 11, 13, 17, 19, 23]
    targets = [10, 20, 30, 40, 50]

    print("Target | Time (seconds)")
    print("--------|---------------")

    for target in targets:
        start = time.time()
        result = DynamicProgramming.subset_sum(nums, target)
        elapsed = time.time() - start
        print("6.4f")


def main():
    """Run all demonstrations."""
    print("Chapter 10: Dynamic Programming - Interactive Examples")
    print("This script demonstrates DP concepts and performance comparisons.\n")

    demonstrate_fibonacci_evolution()
    demonstrate_knapsack_problem()
    demonstrate_lcs_problem()
    demonstrate_coin_change()
    demonstrate_edit_distance()
    demonstrate_subset_sum()
    demonstrate_performance_comparison()

    print("\n" + "=" * 60)
    print("DP PROBLEM-SOLVING FRAMEWORK:")
    print("=" * 60)
    print("1. Define the subproblem")
    print("2. Write the recurrence relation")
    print("3. Identify base cases")
    print("4. Choose memoization vs tabulation")
    print("5. Optimize space if possible")
    print("6. Test with small inputs first")
    print("\nRemember: DP transforms exponential problems into polynomial ones!")


if __name__ == '__main__':
    main()</content>
<parameter name="filePath">chapter_10_dynamic_programming/examples/dp_demonstrations.py