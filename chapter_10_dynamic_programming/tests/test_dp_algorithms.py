"""
Tests for Chapter 10: Dynamic Programming - Core Algorithms
"""

import unittest
import sys
import os

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'code'))

from dp_algorithms import DynamicProgramming


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci implementations."""

    def test_fibonacci_naive_base_cases(self):
        """Test naive fibonacci base cases."""
        self.assertEqual(DynamicProgramming.fibonacci_naive(0), 0)
        self.assertEqual(DynamicProgramming.fibonacci_naive(1), 1)

    def test_fibonacci_naive_sequence(self):
        """Test naive fibonacci sequence values."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for n, expected_value in enumerate(expected):
            with self.subTest(n=n):
                self.assertEqual(DynamicProgramming.fibonacci_naive(n), expected_value)

    def test_fibonacci_naive_negative_raises_error(self):
        """Test that naive fibonacci raises error for negative input."""
        with self.assertRaises(ValueError):
            DynamicProgramming.fibonacci_naive(-1)

    def test_fibonacci_memoization_matches_naive(self):
        """Test that memoization matches naive version."""
        for n in range(15):  # Test reasonable values to avoid exponential time
            with self.subTest(n=n):
                naive = DynamicProgramming.fibonacci_naive(n)
                memo = DynamicProgramming.fibonacci_memoization(n)
                self.assertEqual(memo, naive)

    def test_fibonacci_tabulation_matches_memoization(self):
        """Test that tabulation matches memoization."""
        for n in range(20):
            with self.subTest(n=n):
                memo = DynamicProgramming.fibonacci_memoization(n)
                tab = DynamicProgramming.fibonacci_tabulation(n)
                self.assertEqual(tab, memo)

    def test_fibonacci_large_values(self):
        """Test fibonacci with larger values."""
        # These would be slow with naive, but fast with DP
        self.assertEqual(DynamicProgramming.fibonacci_memoization(35), 9227465)
        self.assertEqual(DynamicProgramming.fibonacci_tabulation(35), 9227465)


class TestKnapsack01(unittest.TestCase):
    """Test cases for 0/1 knapsack implementations."""

    def setUp(self):
        """Set up test data."""
        self.weights = [2, 3, 4, 5]
        self.values = [3, 4, 5, 6]
        self.capacity = 5

    def test_knapsack_basic(self):
        """Test basic knapsack functionality."""
        max_val_memo, items_memo = DynamicProgramming.knapsack_01_memoization(
            self.weights, self.values, self.capacity)
        max_val_tab, items_tab = DynamicProgramming.knapsack_01_tabulation(
            self.weights, self.values, self.capacity)

        # Both should give same max value
        self.assertEqual(max_val_memo, 7)
        self.assertEqual(max_val_tab, 7)

        # Both should select same items (though order might differ)
        self.assertEqual(set(items_memo), {0, 1})  # Items 0 (weight 2, value 3) and 1 (weight 3, value 4)
        self.assertEqual(set(items_tab), {0, 1})

    def test_knapsack_edge_cases(self):
        """Test knapsack edge cases."""
        # Empty knapsack
        max_val, items = DynamicProgramming.knapsack_01_tabulation([], [], 10)
        self.assertEqual(max_val, 0)
        self.assertEqual(items, [])

        # Zero capacity
        max_val, items = DynamicProgramming.knapsack_01_tabulation([1, 2], [10, 20], 0)
        self.assertEqual(max_val, 0)
        self.assertEqual(items, [])

        # Single item that fits
        max_val, items = DynamicProgramming.knapsack_01_tabulation([2], [5], 3)
        self.assertEqual(max_val, 5)
        self.assertEqual(items, [0])

        # Single item that doesn't fit
        max_val, items = DynamicProgramming.knapsack_01_tabulation([5], [10], 3)
        self.assertEqual(max_val, 0)
        self.assertEqual(items, [])

    def test_knapsack_complex(self):
        """Test more complex knapsack case."""
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50

        max_val, items = DynamicProgramming.knapsack_01_tabulation(weights, values, capacity)
        self.assertEqual(max_val, 220)  # Items 1 and 2: 100 + 120 = 220
        self.assertEqual(set(items), {1, 2})


class TestLongestCommonSubsequence(unittest.TestCase):
    """Test cases for longest common subsequence."""

    def test_lcs_basic(self):
        """Test basic LCS functionality."""
        length, lcs = DynamicProgramming.longest_common_subsequence("AGGTAB", "GXTXAYB")
        self.assertEqual(length, 4)
        self.assertEqual(lcs, "GTAB")

    def test_lcs_identical_strings(self):
        """Test LCS with identical strings."""
        length, lcs = DynamicProgramming.longest_common_subsequence("ABC", "ABC")
        self.assertEqual(length, 3)
        self.assertEqual(lcs, "ABC")

    def test_lcs_no_common(self):
        """Test LCS with no common characters."""
        length, lcs = DynamicProgramming.longest_common_subsequence("ABC", "XYZ")
        self.assertEqual(length, 0)
        self.assertEqual(lcs, "")

    def test_lcs_empty_strings(self):
        """Test LCS with empty strings."""
        length, lcs = DynamicProgramming.longest_common_subsequence("", "ABC")
        self.assertEqual(length, 0)
        self.assertEqual(lcs, "")

        length, lcs = DynamicProgramming.longest_common_subsequence("ABC", "")
        self.assertEqual(length, 0)
        self.assertEqual(lcs, "")

        length, lcs = DynamicProgramming.longest_common_subsequence("", "")
        self.assertEqual(length, 0)
        self.assertEqual(lcs, "")

    def test_lcs_complex(self):
        """Test more complex LCS case."""
        X = "ABCDGH"
        Y = "AEDFHR"
        length, lcs = DynamicProgramming.longest_common_subsequence(X, Y)
        self.assertEqual(length, 3)
        self.assertEqual(lcs, "ADH")


class TestCoinChange(unittest.TestCase):
    """Test cases for coin change problems."""

    def test_coin_change_minimum_basic(self):
        """Test minimum coin change basic cases."""
        self.assertEqual(DynamicProgramming.coin_change_minimum([1, 2, 5], 11), 3)  # 5+5+1
        self.assertEqual(DynamicProgramming.coin_change_minimum([2], 3), -1)  # Impossible
        self.assertEqual(DynamicProgramming.coin_change_minimum([1], 0), 0)  # No coins needed

    def test_coin_change_minimum_edge_cases(self):
        """Test minimum coin change edge cases."""
        # Single coin type
        self.assertEqual(DynamicProgramming.coin_change_minimum([5], 10), 2)
        self.assertEqual(DynamicProgramming.coin_change_minimum([5], 7), -1)

        # Multiple coin types
        self.assertEqual(DynamicProgramming.coin_change_minimum([1, 3, 4], 6), 2)  # 3+3

    def test_coin_change_ways_basic(self):
        """Test number of ways coin change."""
        self.assertEqual(DynamicProgramming.coin_change_ways([1, 2, 5], 5), 4)
        # Ways: 5, 2+2+1, 2+1+1+1, 1+1+1+1+1

        self.assertEqual(DynamicProgramming.coin_change_ways([2, 5, 10], 10), 4)
        # Ways: 10, 5+5, 5+2+2+1(wait no), actually: 10, 5+5, 2×5, 10

    def test_coin_change_ways_edge_cases(self):
        """Test number of ways edge cases."""
        self.assertEqual(DynamicProgramming.coin_change_ways([1], 3), 1)  # Only one way
        self.assertEqual(DynamicProgramming.coin_change_ways([2], 3), 0)  # No way
        self.assertEqual(DynamicProgramming.coin_change_ways([], 5), 0)  # No coins


class TestEditDistance(unittest.TestCase):
    """Test cases for edit distance."""

    def test_edit_distance_basic(self):
        """Test basic edit distance cases."""
        self.assertEqual(DynamicProgramming.edit_distance("kitten", "sitting"), 3)
        self.assertEqual(DynamicProgramming.edit_distance("saturday", "sunday"), 3)
        self.assertEqual(DynamicProgramming.edit_distance("horse", "ros"), 3)

    def test_edit_distance_identical(self):
        """Test edit distance with identical strings."""
        self.assertEqual(DynamicProgramming.edit_distance("hello", "hello"), 0)

    def test_edit_distance_empty(self):
        """Test edit distance with empty strings."""
        self.assertEqual(DynamicProgramming.edit_distance("", "abc"), 3)
        self.assertEqual(DynamicProgramming.edit_distance("abc", ""), 3)
        self.assertEqual(DynamicProgramming.edit_distance("", ""), 0)


class TestSubsetSum(unittest.TestCase):
    """Test cases for subset sum problem."""

    def test_subset_sum_basic(self):
        """Test basic subset sum cases."""
        self.assertTrue(DynamicProgramming.subset_sum([3, 34, 4, 12, 5, 2], 9))  # 4+5
        self.assertTrue(DynamicProgramming.subset_sum([3, 34, 4, 12, 5, 2], 30))  # 3+4+12+5+2+4(wait), actually 34+4-12+5-2= wait, let's check: 4+5=9
        self.assertFalse(DynamicProgramming.subset_sum([3, 34, 4, 12, 5, 2], 1))

    def test_subset_sum_edge_cases(self):
        """Test subset sum edge cases."""
        # Empty set
        self.assertTrue(DynamicProgramming.subset_sum([], 0))
        self.assertFalse(DynamicProgramming.subset_sum([], 5))

        # Single element
        self.assertTrue(DynamicProgramming.subset_sum([5], 5))
        self.assertFalse(DynamicProgramming.subset_sum([5], 3))

        # Target zero
        self.assertTrue(DynamicProgramming.subset_sum([1, 2, 3], 0))


if __name__ == '__main__':
    unittest.main()
