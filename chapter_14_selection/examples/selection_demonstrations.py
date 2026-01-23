"""
Chapter 14 Examples: Selection Algorithms - Finding Order Statistics

Interactive demonstrations of quickselect, pivot strategies, and performance analysis.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from selection_algorithms import SelectionAlgorithms, SelectionAnalysis


def demonstrate_basic_selection():
    """Demonstrate basic selection operations."""
    print("=== Basic Selection Operations ===\n")

    # Sample array
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Array: {arr}")
    print(f"Sorted: {sorted(arr)}\n")

    # Test different k values
    k_values = [0, 2, 5, 7, len(arr) - 1]
    for k in k_values:
        result = SelectionAlgorithms.quickselect(arr, k)
        expected = sorted(arr)[k]
        print(
            f"k={k}: quickselect={result}, expected={expected}, correct={result == expected}"
        )

    print()


def demonstrate_pivot_strategies():
    """Compare different pivot selection strategies."""
    print("\n=== Pivot Selection Strategies ===\n")

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 8, 7]
    k = 5  # Find median

    strategies = [
        ("Median-of-Three", SelectionAlgorithms.quickselect),
        ("Random Pivot", SelectionAlgorithms.quickselect_random_pivot),
    ]

    print(f"Finding {k}-th element in: {arr}")
    print(f"Expected result: {sorted(arr)[k]}\n")

    for name, func in strategies:
        # Run multiple times for random pivot
        results = []
        times = []

        for _ in range(10 if "Random" in name else 1):
            arr_copy = arr.copy()
            start = time.time()
            result = func(arr_copy, k)
            end = time.time()

            results.append(result)
            times.append(end - start)

        avg_time = sum(times) / len(times)
        consistent = len(set(results)) == 1

        print(f"{name}:")
        print(".6f")
        print(f"  Consistent results: {consistent}")
        if not consistent:
            print(f"  Results: {set(results)}")
        print()


def demonstrate_median_and_percentiles():
    """Demonstrate median and percentile finding."""
    print("\n=== Median and Percentile Finding ===\n")

    # Test data sets
    datasets = [
        ("Small array", [3, 1, 4, 1, 5]),
        ("Even length", [1, 2, 3, 4, 5, 6]),
        ("Large range", list(range(1, 101))),
        ("Normal-like", [random.gauss(50, 15) for _ in range(20)]),
    ]

    for name, arr in datasets:
        print(f"{name}: {len(arr)} elements")

        # Find median
        median = SelectionAlgorithms.find_median(arr)
        print(f"  Median: {median}")

        # Find percentiles
        percentiles = [25, 50, 75, 90]
        for p in percentiles:
            try:
                val = SelectionAlgorithms.find_percentile(arr, p)
                print(".1f")
            except Exception as e:
                print(f"  {p}th percentile: Error - {e}")

        # Show sorted for context
        sorted_arr = sorted(arr)
        if len(sorted_arr) <= 10:
            print(f"  Sorted: {sorted_arr}")
        else:
            print(f"  Range: [{sorted_arr[0]:.1f}, {sorted_arr[-1]:.1f}]")
        print()


def demonstrate_performance_comparison():
    """Compare quickselect performance vs sorting."""
    print("\n=== Performance: Quickselect vs Sorting ===\n")

    sizes = [100, 1000, 5000]

    for size in sizes:
        arr = [random.randint(0, 1000000) for _ in range(size)]

        print(f"Array size: {size}")

        # Test different k values
        k_values = [size // 4, size // 2, 3 * size // 4]

        for k in k_values:
            # Quickselect
            arr_copy = arr.copy()
            start = time.time()
            quickselect_result = SelectionAlgorithms.quickselect(arr_copy, k)
            quickselect_time = time.time() - start

            # Sort + index
            arr_copy = arr.copy()
            start = time.time()
            sorted_arr = sorted(arr_copy)
            sort_result = sorted_arr[k]
            sort_time = time.time() - start

            # Verify correctness
            assert quickselect_result == sort_result

            print(f"  k={k} ({k / size:.1%}):")
            print(".6f")
            print(".6f")
            print(".1f")

        print()


def demonstrate_worst_case_scenarios():
    """Show worst-case behavior for different pivot strategies."""
    print("\n=== Worst-Case Scenarios ===\n")

    # Create worst-case array (already sorted)
    arr = list(range(100))
    k = 50

    print(f"Testing with sorted array (worst case for bad pivot selection):")
    print(f"Array: [{arr[0]}, {arr[1]}, ..., {arr[-2]}, {arr[-1]}]")
    print(f"Finding k={k} (median)\n")

    # Test different strategies
    strategies = [
        ("Median-of-Three", SelectionAlgorithms.quickselect),
        ("Random Pivot (avg of 10 runs)", SelectionAlgorithms.quickselect_random_pivot),
    ]

    for name, func in strategies:
        if "Random" in name:
            # Average multiple runs for random pivot
            times = []
            for _ in range(10):
                arr_copy = arr.copy()
                start = time.time()
                result = func(arr_copy, k)
                times.append(time.time() - start)

            avg_time = sum(times) / len(times)
            print(".6f")
        else:
            arr_copy = arr.copy()
            start = time.time()
            result = func(arr_copy, k)
            avg_time = time.time() - start
            print(".6f")

        print(f"  Result: {result} ✓\n")


def demonstrate_top_k_selection():
    """Demonstrate selecting top k elements."""
    print("\n=== Top-K Selection ===\n")

    arr = [random.randint(1, 100) for _ in range(20)]
    sorted_arr = sorted(arr)

    print(f"Array ({len(arr)} elements): {arr}")
    print(f"Sorted: {sorted_arr}\n")

    k_values = [3, 5, 10, 15]

    for k in k_values:
        result = SelectionAlgorithms.select_top_k(arr, k)
        print(f"Top {k} smallest: {sorted(result)}")
        print(
            f"  All ≤ {sorted_arr[k - 1]}: {all(x <= sorted_arr[k - 1] for x in result)}"
        )
        print()


def demonstrate_correctness_verification():
    """Demonstrate correctness verification."""
    print("\n=== Correctness Verification ===\n")

    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = sorted(arr)

    print(f"Array: {arr}")
    print(f"Sorted: {sorted_arr}\n")

    print("Verifying each k-th element:")
    for k in range(len(arr)):
        candidate = SelectionAlgorithms.quickselect(arr, k)
        is_correct = SelectionAlgorithms.is_kth_smallest_correct(arr, k, candidate)
        expected = sorted_arr[k]

        status = "✓" if is_correct and candidate == expected else "✗"
        print(
            f"  k={k}: candidate={candidate}, expected={expected}, verified={is_correct} {status}"
        )

    print()


def demonstrate_algorithm_variants():
    """Compare different quickselect variants."""
    print("\n=== Algorithm Variants Comparison ===\n")

    arr = [random.randint(0, 1000) for _ in range(50)]
    k = 25

    variants = [
        ("Recursive (Median-of-Three)", SelectionAlgorithms.quickselect),
        ("Iterative (Median-of-Three)", SelectionAlgorithms.quickselect_iterative),
        ("Recursive (Random Pivot)", SelectionAlgorithms.quickselect_random_pivot),
    ]

    print(f"Array size: {len(arr)}, finding k={k}")
    print(f"Expected result: {sorted(arr)[k]}\n")

    for name, func in variants:
        arr_copy = arr.copy()
        start = time.time()
        result = func(arr_copy, k)
        elapsed = time.time() - start

        correct = result == sorted(arr)[k]
        print(f"{name}:")
        print(".6f")
        print(f"  Correct: {correct} {'✓' if correct else '✗'}")
        print()


def demonstrate_real_world_applications():
    """Show real-world applications of selection."""
    print("\n=== Real-World Applications ===\n")

    # Tournament winner selection
    print("1. Tournament Selection:")
    scores = [85, 92, 78, 96, 88, 73, 91, 89]
    players = [f"Player{i + 1}" for i in range(len(scores))]

    # Find top 3 scores
    score_player_pairs = list(zip(scores, players))
    top_3_scores = SelectionAlgorithms.select_top_k(
        [s for s, p in score_player_pairs], 3
    )
    top_3_scores_set = set(top_3_scores)

    print(f"  Scores: {scores}")
    print(f"  Top 3 scores: {sorted(top_3_scores, reverse=True)}")

    # Show which players have top scores
    top_players = [
        (score, player)
        for score, player in score_player_pairs
        if score in top_3_scores_set
    ]
    top_players.sort(key=lambda x: x[0], reverse=True)
    print(f"  Top players: {top_players[:3]}")
    print()

    # Statistical analysis
    print("2. Statistical Analysis:")
    data = [random.gauss(100, 15) for _ in range(100)]

    median = SelectionAlgorithms.find_median(data)
    q1 = SelectionAlgorithms.find_percentile(data, 25)
    q3 = SelectionAlgorithms.find_percentile(data, 75)
    p90 = SelectionAlgorithms.find_percentile(data, 90)

    print(f"  Dataset: {len(data)} measurements")
    print(".1f")
    print(".1f")
    print(".1f")
    print(".1f")

    sorted_data = sorted(data)
    print(f"  Range: [{sorted_data[0]:.1f}, {sorted_data[-1]:.1f}]")
    print()

    # Load balancing simulation
    print("3. Load Balancing:")
    server_loads = [random.randint(10, 100) for _ in range(8)]
    print(f"  Server loads: {server_loads}")

    # Find median load (good pivot for balancing)
    median_load = SelectionAlgorithms.find_median(server_loads)
    print(f"  Median load: {median_load}")

    # Servers above median need load reduction
    high_load_servers = [i for i, load in enumerate(server_loads) if load > median_load]
    print(f"  Servers needing load reduction: {high_load_servers}")
    print()


if __name__ == "__main__":
    demonstrate_basic_selection()
    demonstrate_pivot_strategies()
    demonstrate_median_and_percentiles()
    demonstrate_performance_comparison()
    demonstrate_worst_case_scenarios()
    demonstrate_top_k_selection()
    demonstrate_correctness_verification()
    demonstrate_algorithm_variants()
    demonstrate_real_world_applications()

    print("\n=== Selection Algorithms Summary ===")
    print("• Quickselect: O(n) average-case order statistics")
    print("• Pivot selection critical for performance")
    print("• Applications: medians, percentiles, tournaments, statistics")
    print("• Trade-off: precision vs speed for different use cases")
    print("\nChapter 14: Selection algorithms mastered! 🎯")
