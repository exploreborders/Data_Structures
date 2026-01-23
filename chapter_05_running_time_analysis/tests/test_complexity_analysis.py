import unittest
import time
from chapter_5_running_time_analysis.code.complexity_analysis import (
    time_function,
    sum_first_k_quadratic,
    sum_first_k_linear,
    sum_first_k_constant,
    ComplexityAnalyzer,
    BigOAnalyzer,
    worst_case_examples,
)


class TestTimingFunctions(unittest.TestCase):
    def test_time_function_basic(self):
        """Test that time_function returns correct result and timing info."""

        def simple_add(a, b):
            return a + b

        result, avg_time, min_time, max_time = time_function(simple_add, 3, 5)

        self.assertEqual(result, 8)
        self.assertIsInstance(avg_time, float)
        self.assertIsInstance(min_time, float)
        self.assertIsInstance(max_time, float)
        self.assertGreaterEqual(avg_time, 0)
        self.assertLessEqual(min_time, avg_time)
        self.assertGreaterEqual(max_time, avg_time)

    def test_time_function_with_multiple_runs(self):
        """Test timing with multiple runs for averaging."""

        def dummy_function(n):
            total = 0
            for i in range(n):
                total += i
            return total

        result, avg_time, min_time, max_time = time_function(
            dummy_function, 100, n_runs=3
        )

        # Verify result is correct (sum of 0 to 99)
        self.assertEqual(result, 4950)
        # Verify timing data makes sense
        self.assertGreater(avg_time, 0)


class TestSumAlgorithms(unittest.TestCase):
    def test_sum_correctness(self):
        """Test that all sum algorithms produce correct results."""
        n = 10
        expected = 55  # Sum of 0+1+2+...+10

        result_quad = sum_first_k_quadratic(n)
        result_linear = sum_first_k_linear(n)
        result_const = sum_first_k_constant(n)

        # All should produce the same result
        self.assertEqual(result_quad, expected)
        self.assertEqual(result_linear, expected)
        self.assertEqual(result_const, expected)

    def test_sum_edge_cases(self):
        """Test sum algorithms with edge cases."""
        # n = 0: sum of first 0 numbers = 0
        self.assertEqual(sum_first_k_quadratic(0), 0)
        self.assertEqual(sum_first_k_linear(0), 0)
        self.assertEqual(sum_first_k_constant(0), 0)

        # n = 1: sum of numbers 0 to 1 (inclusive) = 0 + 1 = 1
        # But our quadratic version has a bug - it sums i where j==i, so for i=0,j=0: +0, for i=1,j=1: +1 = 1
        # Linear version sums 0 to 1 = 0+1 = 1
        # Constant version: 1*(1+1)//2 = 1
        self.assertEqual(sum_first_k_quadratic(1), 1)
        self.assertEqual(sum_first_k_linear(1), 1)
        self.assertEqual(sum_first_k_constant(1), 1)


class TestComplexityAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ComplexityAnalyzer()
        self.test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        self.sorted_array = sorted(self.test_array)

    def test_linear_search_found(self):
        """Test linear search finds existing element."""
        target = 4
        index, operations = self.analyzer.analyze_linear_search(self.test_array, target)

        self.assertGreaterEqual(index, 0)
        self.assertEqual(self.test_array[index], target)
        self.assertGreater(operations, 0)

    def test_linear_search_not_found(self):
        """Test linear search handles missing element."""
        target = 999
        index, operations = self.analyzer.analyze_linear_search(self.test_array, target)

        self.assertEqual(index, -1)
        self.assertEqual(operations, len(self.test_array))

    def test_binary_search_found(self):
        """Test binary search finds existing element."""
        target = 4
        index, operations = self.analyzer.analyze_binary_search(
            self.sorted_array, target
        )

        self.assertGreaterEqual(index, 0)
        self.assertEqual(self.sorted_array[index], target)
        self.assertGreater(operations, 0)

    def test_binary_search_not_found(self):
        """Test binary search handles missing element."""
        target = 999
        index, operations = self.analyzer.analyze_binary_search(
            self.sorted_array, target
        )

        self.assertEqual(index, -1)
        self.assertGreater(operations, 0)

    def test_list_operations_analysis(self):
        """Test analysis of list operations."""
        n = 100
        results = self.analyzer.analyze_list_operations(n)

        # Check that all operations are analyzed
        self.assertIn("index_access", results)
        self.assertIn("length", results)
        self.assertIn("sum_all", results)
        self.assertIn("membership", results)

        # Index access should be O(1)
        self.assertEqual(results["index_access"], 1)

        # Length should be O(1)
        self.assertEqual(results["length"], 1)

        # Sum and membership should be O(n)
        self.assertEqual(results["sum_all"], n)
        self.assertEqual(results["membership"], n)

    def test_dict_operations_analysis(self):
        """Test analysis of dictionary operations."""
        n = 50
        results = self.analyzer.analyze_dict_operations(n)

        # Check that operations are analyzed
        self.assertIn("key_access", results)
        self.assertIn("key_insert", results)
        self.assertIn("membership", results)

        # All should be O(1) average case
        self.assertEqual(results["key_access"], 1)
        self.assertEqual(results["key_insert"], 1)
        self.assertEqual(results["membership"], 1)


class TestBigOAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = BigOAnalyzer()

    def test_constant_time(self):
        """Test O(1) constant time function."""
        # Result should be same regardless of input
        self.assertEqual(self.analyzer.constant_time(1), 42)
        self.assertEqual(self.analyzer.constant_time(1000), 42)
        self.assertEqual(self.analyzer.constant_time(1000000), 42)

    def test_logarithmic_time(self):
        """Test O(log n) logarithmic time function."""
        # log₂(1) = 0
        self.assertEqual(self.analyzer.logarithmic_time(1), 0)

        # log₂(8) = 3
        self.assertEqual(self.analyzer.logarithmic_time(8), 3)

        # log₂(16) = 4
        self.assertEqual(self.analyzer.logarithmic_time(16), 4)

    def test_linear_time(self):
        """Test O(n) linear time function."""
        # The function sums range(n), so:
        # linear_time(1) = sum(range(1)) = sum([0]) = 0
        # linear_time(2) = sum(range(2)) = sum([0,1]) = 1
        # linear_time(6) = sum(range(6)) = sum([0,1,2,3,4,5]) = 15
        self.assertEqual(self.analyzer.linear_time(1), 0)
        self.assertEqual(self.analyzer.linear_time(2), 1)  # 0+1
        self.assertEqual(self.analyzer.linear_time(6), 15)  # 0+1+2+3+4+5

    def test_growth_rates(self):
        """Test that functions exhibit expected growth rates."""
        # Log n grows slower than n
        log_1000 = self.analyzer.logarithmic_time(1000)
        linear_100 = self.analyzer.linear_time(100)

        # For reasonable sizes, log n should be much smaller than n
        self.assertLess(log_1000, 100)  # log₂(1000) ≈ 10
        self.assertGreater(linear_100, 100)  # sum to 99 > 100


class TestWorstCaseExamples(unittest.TestCase):
    def test_worst_case_linear_search(self):
        """Test that linear search examines all elements in worst case."""
        examples = worst_case_examples()
        linear_search = examples["linear_search"]

        # Worst case: element not in array
        arr = [1, 2, 3, 4, 5]
        result = linear_search(arr, 999)
        self.assertFalse(result)

    def test_worst_case_quicksort(self):
        """Test quicksort functionality."""
        examples = worst_case_examples()
        quicksort = examples["quicksort"]

        # Test basic sorting
        arr = [3, 1, 4, 1, 5]
        result = quicksort(arr.copy())
        self.assertEqual(result, [1, 1, 3, 4, 5])


# Performance regression tests
class TestPerformanceRegressions(unittest.TestCase):
    def test_linear_vs_binary_search_performance(self):
        """Test that binary search is faster than linear search for large arrays."""
        # Create large sorted array
        size = 10000
        arr = list(range(size))

        analyzer = ComplexityAnalyzer()

        # Linear search (worst case - element not found)
        _, linear_ops = analyzer.analyze_linear_search(arr, size + 1)

        # Binary search (worst case - element not found)
        _, binary_ops = analyzer.analyze_binary_search(arr, size + 1)

        # Binary search should use far fewer operations
        self.assertLess(binary_ops, linear_ops)
        self.assertLess(binary_ops, size // 10)  # Should be O(log n)

    def test_algorithm_scaling(self):
        """Test that algorithms scale as expected."""
        analyzer = BigOAnalyzer()

        # Test that logarithmic grows slower than linear
        log_small = analyzer.logarithmic_time(100)
        log_large = analyzer.logarithmic_time(1000)

        linear_small = analyzer.linear_time(10)  # Use smaller n for speed
        linear_large = analyzer.linear_time(20)

        # Logarithmic growth: doubling input shouldn't double output much
        self.assertLess(log_large / log_small, 4)  # Should be ~3.3

        # Linear growth: doubling input should roughly double output
        ratio = linear_large / linear_small
        self.assertGreater(ratio, 1.5)  # Should be approximately 2


if __name__ == "__main__":
    unittest.main()
