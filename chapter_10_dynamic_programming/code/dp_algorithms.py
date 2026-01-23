"""
Chapter 10: Dynamic Programming - Core Algorithms

This module implements fundamental dynamic programming algorithms,
demonstrating both memoization (top-down) and tabulation (bottom-up) approaches.
"""

import sys
from typing import List, Dict, Tuple


class DynamicProgramming:
    """Collection of dynamic programming algorithms."""

    @staticmethod
    def fibonacci_naive(n: int) -> int:
        """
        Naive recursive fibonacci - exponential time O(2^n).

        Args:
            n: Non-negative integer

        Returns:
            nth Fibonacci number

        Examples:
            >>> DynamicProgramming.fibonacci_naive(6)
            8
        """
        if n < 0:
            raise ValueError("Fibonacci not defined for negative numbers")
        if n <= 1:
            return n
        return DynamicProgramming.fibonacci_naive(n-1) + DynamicProgramming.fibonacci_naive(n-2)

    @staticmethod
    def fibonacci_memoization(n: int, memo: Dict[int, int] = None) -> int:
        """
        Fibonacci with memoization - linear time O(n).

        Args:
            n: Non-negative integer
            memo: Dictionary for caching results

        Returns:
            nth Fibonacci number

        Examples:
            >>> DynamicProgramming.fibonacci_memoization(6)
            8
            >>> DynamicProgramming.fibonacci_memoization(50)  # Efficient!
            12586269025
        """
        if memo is None:
            memo = {}

        if n < 0:
            raise ValueError("Fibonacci not defined for negative numbers")

        if n in memo:
            return memo[n]

        if n <= 1:
            return n

        memo[n] = (DynamicProgramming.fibonacci_memoization(n-1, memo) +
                  DynamicProgramming.fibonacci_memoization(n-2, memo))
        return memo[n]

    @staticmethod
    def fibonacci_tabulation(n: int) -> int:
        """
        Fibonacci with tabulation - linear time O(n), constant space O(1).

        Args:
            n: Non-negative integer

        Returns:
            nth Fibonacci number

        Examples:
            >>> DynamicProgramming.fibonacci_tabulation(6)
            8
            >>> DynamicProgramming.fibonacci_tabulation(100)
            354224848179261915075
        """
        if n < 0:
            raise ValueError("Fibonacci not defined for negative numbers")
        if n <= 1:
            return n

        # Use only two variables for space optimization
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def knapsack_01_memoization(weights: List[int], values: List[int],
                               capacity: int) -> Tuple[int, List[int]]:
        """
        0/1 Knapsack problem with memoization.

        Args:
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity

        Returns:
            Tuple of (max_value, selected_items_indices)

        Examples:
            >>> weights = [2, 3, 4, 5]
            >>> values = [3, 4, 5, 6]
            >>> max_val, items = DynamicProgramming.knapsack_01_memoization(weights, values, 5)
            >>> max_val
            7
        """
        n = len(weights)
        memo = {}

        def dp(i: int, w: int) -> int:
            """Recursive helper with memoization."""
            if i >= n or w <= 0:
                return 0

            key = (i, w)
            if key in memo:
                return memo[key]

            # Don't take item i
            result = dp(i + 1, w)

            # Take item i if it fits
            if weights[i] <= w:
                result = max(result, values[i] + dp(i + 1, w - weights[i]))

            memo[key] = result
            return result

        max_value = dp(0, capacity)

        # Reconstruct solution
        selected = []
        w = capacity
        for i in range(n):
            if (i, w) in memo and memo[(i, w)] != dp(i + 1, w):
                selected.append(i)
                w -= weights[i]

        return max_value, selected

    @staticmethod
    def knapsack_01_tabulation(weights: List[int], values: List[int],
                              capacity: int) -> Tuple[int, List[int]]:
        """
        0/1 Knapsack problem with tabulation.

        Args:
            weights: List of item weights
            values: List of item values
            capacity: Maximum weight capacity

        Returns:
            Tuple of (max_value, selected_items_indices)

        Examples:
            >>> weights = [2, 3, 4, 5]
            >>> values = [3, 4, 5, 6]
            >>> max_val, items = DynamicProgramming.knapsack_01_tabulation(weights, values, 5)
            >>> max_val
            7
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # Fill the table
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # Don't take item i
                dp[i][w] = dp[i-1][w]

                # Take item i if it fits
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], values[i-1] + dp[i-1][w - weights[i-1]])

        max_value = dp[n][capacity]

        # Reconstruct solution
        selected = []
        w = capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:  # Item was taken
                selected.append(i-1)
                w -= weights[i-1]

        return max_value, selected[::-1]  # Reverse to get correct order

    @staticmethod
    def longest_common_subsequence(X: str, Y: str) -> Tuple[int, str]:
        """
        Longest Common Subsequence using dynamic programming.

        Args:
            X: First string
            Y: Second string

        Returns:
            Tuple of (length, lcs_string)

        Examples:
            >>> length, lcs = DynamicProgramming.longest_common_subsequence("AGGTAB", "GXTXAYB")
            >>> length
            4
            >>> lcs
            'GTAB'
        """
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Reconstruct LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if X[i-1] == Y[j-1]:
                lcs.append(X[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        return dp[m][n], ''.join(reversed(lcs))

    @staticmethod
    def coin_change_minimum(coins: List[int], amount: int) -> int:
        """
        Minimum number of coins needed to make given amount.

        Args:
            coins: Available coin denominations
            amount: Target amount

        Returns:
            Minimum number of coins, or -1 if impossible

        Examples:
            >>> DynamicProgramming.coin_change_minimum([1, 2, 5], 11)
            3
            >>> DynamicProgramming.coin_change_minimum([2], 3)
            -1
        """
        if amount == 0:
            return 0

        # Initialize dp array
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for amt in range(coin, amount + 1):
                if dp[amt - coin] != sys.maxsize:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        return dp[amount] if dp[amount] != sys.maxsize else -1

    @staticmethod
    def coin_change_ways(coins: List[int], amount: int) -> int:
        """
        Number of ways to make change for given amount.

        Args:
            coins: Available coin denominations
            amount: Target amount

        Returns:
            Number of different ways to make the amount

        Examples:
            >>> DynamicProgramming.coin_change_ways([1, 2, 5], 5)
            4
        """
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make 0: use no coins

        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]

        return dp[amount]

    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """
        Levenshtein distance (edit distance) between two strings.

        Args:
            word1: First string
            word2: Second string

        Returns:
            Minimum number of operations to transform word1 to word2

        Examples:
            >>> DynamicProgramming.edit_distance("kitten", "sitting")
            3
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],      # Delete
                        dp[i][j-1],      # Insert
                        dp[i-1][j-1]     # Replace
                    )

        return dp[m][n]

    @staticmethod
    def subset_sum(nums: List[int], target: int) -> bool:
        """
        Check if there exists a subset that sums to target.

        Args:
            nums: List of positive integers
            target: Target sum

        Returns:
            True if subset exists, False otherwise

        Examples:
            >>> DynamicProgramming.subset_sum([3, 34, 4, 12, 5, 2], 9)
            True
        """
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base case: empty subset sums to 0
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Don't include current element
                dp[i][j] = dp[i-1][j]

                # Include current element if it doesn't exceed target
                if nums[i-1] <= j:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i-1]]

        return dp[n][target]</content>
<parameter name="filePath">chapter_10_dynamic_programming/code/dp_algorithms.py