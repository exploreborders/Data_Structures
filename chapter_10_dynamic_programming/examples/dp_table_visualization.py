#!/usr/bin/env python3
"""
Chapter 10: Dynamic Programming - Top-Down vs Bottom-Up Comparison

This script provides a detailed comparison between memoization (top-down)
and tabulation (bottom-up) approaches with step-by-step visualizations.
"""

import sys
import os
from typing import Dict, List, Tuple

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from dp_algorithms import DynamicProgramming


def print_dp_table(table: List[List[int]], title: str = "DP Table"):
    """Pretty print a 2D DP table."""
    print(f"\n{title}:")
    print("   ", end="")
    for j in range(len(table[0])):
        print(f"{j:3d}", end="")
    print()

    for i, row in enumerate(table):
        print(f"{i:2d}", end="")
        for val in row:
            if val == float("inf") or val == sys.maxsize:
                print(" ∞ ", end="")
            else:
                print(f"{val:3d}", end="")
        print()


def demonstrate_fibonacci_approaches():
    """Compare fibonacci implementations."""
    print("FIBONACCI: Top-Down vs Bottom-Up")
    print("=" * 40)

    n = 8

    print(f"Computing F({n}) using different approaches:\n")

    # Manual memoization demonstration
    print("1. TOP-DOWN (Memoization) - Step by Step:")
    memo = {}

    def fib_memo(n, depth=0):
        indent = "  " * depth
        print(f"{indent}fib({n}) called")

        if n in memo:
            print(f"{indent}  → Using cached value: {memo[n]}")
            return memo[n]

        if n <= 1:
            result = n
            print(f"{indent}  → Base case: {result}")
        else:
            print(f"{indent}  → Computing fib({n - 1}) + fib({n - 2})")
            a = fib_memo(n - 1, depth + 1)
            b = fib_memo(n - 2, depth + 1)
            result = a + b
            print(f"{indent}  → Result: {a} + {b} = {result}")

        memo[n] = result
        print(f"{indent}  → Caching F({n}) = {result}")
        return result

    result = fib_memo(n)
    print(f"\nFinal result: F({n}) = {result}")

    # Tabulation demonstration
    print("\n2. BOTTOM-UP (Tabulation) - Step by Step:")
    dp = [0] * (n + 1)
    print(f"Initial DP array: {dp}")

    dp[0] = 0
    dp[1] = 1
    print(f"Base cases: F(0)={dp[0]}, F(1)={dp[1]}")

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        print(
            f"F({i}) = dp[{i - 1}] + dp[{i - 2}] = {dp[i - 1]} + {dp[i - 2]} = {dp[i]}"
        )

    print(f"\nFinal DP array: {dp}")
    print(f"Result: F({n}) = {dp[n]}")


def demonstrate_knapsack_visualization():
    """Visualize knapsack DP table construction."""
    print("\n\n0/1 KNAPSACK: DP Table Construction")
    print("=" * 50)

    weights = [2, 3, 4]
    values = [1, 2, 5]
    capacity = 5

    print(f"Items: Weights={weights}, Values={values}")
    print(f"Capacity: {capacity}")
    print()

    # Create and fill DP table step by step
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    print_dp_table(dp, "Initial DP Table (all zeros)")

    for i in range(1, n + 1):
        item_idx = i - 1
        item_weight = weights[item_idx]
        item_value = values[item_idx]

        print(f"\nProcessing item {i}: Weight={item_weight}, Value={item_value}")

        for w in range(capacity + 1):
            # Don't take item
            dont_take = dp[i - 1][w]

            # Take item (if possible)
            if item_weight <= w:
                take = item_value + dp[i - 1][w - item_weight]
            else:
                take = float("-inf")  # Impossible

            # Choose maximum
            dp[i][w] = max(dont_take, take)

            if w <= 6:  # Only show first few columns for readability
                choice = (
                    "TAKE" if dp[i][w] == take and take != float("-inf") else "SKIP"
                )
                print(
                    f"  W={w}: Skip={dont_take}, Take={take if take != float('-inf') else 'N/A'} → Choose {choice} → {dp[i][w]}"
                )

        print_dp_table(dp[: i + 1], f"After processing item {i}")

    # Extract solution
    max_value = dp[n][capacity]
    print(f"\nMaximum value: {max_value}")

    # Reconstruct which items were chosen
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Item was taken
            selected.append(i - 1)
            w -= weights[i - 1]

    print(f"Selected items (0-based indices): {selected[::-1]}")


def demonstrate_lcs_visualization():
    """Visualize LCS DP table construction."""
    print("\n\nLONGEST COMMON SUBSEQUENCE: DP Table Construction")
    print("=" * 55)

    X = "AGTA"
    Y = "GXA"

    print(f"String X: '{X}' (length {len(X)})")
    print(f"String Y: '{Y}' (length {len(Y)})")
    print()

    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column with zeros (base cases)
    print("Step 1: Initialize base cases")
    print_dp_table(dp, "DP Table with base cases")

    print("\nStep 2: Fill table using recurrence:")
    print("If X[i-1] == Y[j-1]: dp[i][j] = dp[i-1][j-1] + 1")
    print("Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])")
    print()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                print(
                    f"X[{i - 1}]='{X[i - 1]}' == Y[{j - 1}]='{Y[j - 1]}' → dp[{i}][{j}] = {dp[i - 1][j - 1]} + 1 = {dp[i][j]}"
                )
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                choice = "UP" if dp[i][j] == dp[i - 1][j] else "LEFT"
                print(
                    f"X[{i - 1}]='{X[i - 1]}' != Y[{j - 1}]='{Y[j - 1]}' → dp[{i}][{j}] = max({dp[i - 1][j]}, {dp[i][j - 1]}) = {dp[i][j]} ({choice})"
                )

        print_dp_table(dp, f"After processing X[{i - 1}]='{X[i - 1]}'")

    # Extract LCS
    lcs = []
    i, j = m, n
    print("\nStep 3: Reconstruct LCS by backtracking:")
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            print(f"Match at ({i},{j}): '{X[i - 1]}' - moving diagonally")
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            print(
                f"No match at ({i},{j}) - moving up (from {dp[i][j]} to {dp[i - 1][j]})"
            )
            i -= 1
        else:
            print(
                f"No match at ({i},{j}) - moving left (from {dp[i][j]} to {dp[i][j - 1]})"
            )
            j -= 1

    lcs.reverse()
    print(f"\nFinal LCS: '{''.join(lcs)}' (length {len(lcs)})")


def demonstrate_coin_change_visualization():
    """Visualize coin change DP table."""
    print("\n\nCOIN CHANGE: Minimum Coins DP Table")
    print("=" * 45)

    coins = [1, 2, 5]
    amount = 7

    print(f"Coins: {coins}")
    print(f"Target amount: {amount}")
    print()

    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0  # Base case

    print("Step 1: Initialize DP array")
    print("dp[i] = minimum coins to make amount i")
    print(f"dp[0] = 0 (base case)")
    print(f"Initial dp: {dp[: min(8, len(dp))]}... (showing first 8 values)")

    for coin in coins:
        print(f"\nStep 2: Process coin {coin}")
        for amt in range(coin, amount + 1):
            if dp[amt - coin] != sys.maxsize:
                new_value = dp[amt - coin] + 1
                if new_value < dp[amt]:
                    dp[amt] = new_value
                    print(
                        f"  Amount {amt}: dp[{amt}] = min({dp[amt]}, dp[{amt - coin}] + 1) = {dp[amt]}"
                    )

        print(f"After coin {coin}: dp = {dp}")

    result = dp[amount] if dp[amount] != sys.maxsize else -1
    print(f"\nFinal result: Minimum coins to make {amount} = {result}")


def main():
    """Run all visualizations."""
    print("Chapter 10: Dynamic Programming - Approach Comparison")
    print("This script shows step-by-step DP table construction.\n")

    demonstrate_fibonacci_approaches()
    demonstrate_knapsack_visualization()
    demonstrate_lcs_visualization()
    demonstrate_coin_change_visualization()

    print("\n" + "=" * 60)
    print("KEY INSIGHTS:")
    print("=" * 60)
    print("• Top-Down (Memoization): Natural recursive thinking + caching")
    print("• Bottom-Up (Tabulation): Systematic table filling")
    print("• Both achieve same O(n) time, but tabulation uses less stack space")
    print("• Tables make it easy to see the optimal substructure")
    print("• Backtracking through tables reconstructs the actual solution")


if __name__ == "__main__":
    main()
