"""
Tests for Chapter 22: Sets - Union-Find (Disjoint Set Union) Implementation

Comprehensive tests covering Union-Find operations, performance, and applications.
"""

import sys
import os
import time


def run_all_tests():
    """Run all test functions in this module."""
    print("Running Chapter 22 Union-Find Tests...")
    print("=" * 60)
    
    # Collect all test classes
    test_classes = [
        TestUnionFind(),
        TestUnionFindAnalysis(),
        TestKruskalWithUnionFind(),
        TestConnectivityChecker(),
        TestUnionFindPerformance(),
        TestUnionFindEdgeCases(),
    ]
    
    all_passed = True
    
    for test_class in test_classes:
        print(f"\nRunning {test_class.__class__.__name__}:")
        print("-" * 40)
        
        # Get all test methods
        test_methods = [method for method in dir(test_class) if method.startswith("test_")]
        
        for method_name in test_methods:
            try:
                test_method = getattr(test_class, method_name)
                test_method()
                print(f"✓ {method_name}")
            except Exception as e:
                print(f"✗ {method_name}: {e}")
                all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    
    return all_passed

# Add code directory to path for imports (relative to this test file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from union_find_implementations import (
    UnionFind,
    UnionFindAnalysis,
    KruskalWithUnionFind,
    ConnectivityChecker,
)


class TestUnionFind:
    """Test basic Union-Find operations."""

    def test_empty_union_find(self):
        """Test empty Union-Find structure."""
        uf = UnionFind()
        assert len(uf) == 0
        assert uf.get_set_count() == 0

    def test_make_set(self):
        """Test creating sets."""
        uf = UnionFind()

        uf.make_set("A")
        assert len(uf) == 1
        assert uf.get_set_count() == 1
        assert uf.find("A") == "A"
        assert uf.get_set_size("A") == 1

        uf.make_set("B")
        assert len(uf) == 2
        assert uf.get_set_count() == 2

    def test_initialization_with_elements(self):
        """Test initialization with list of elements."""
        elements = ["A", "B", "C", "D"]
        uf = UnionFind(elements)

        assert len(uf) == 4
        assert uf.get_set_count() == 4

        for elem in elements:
            assert uf.find(elem) == elem
            assert uf.get_set_size(elem) == 1

    def test_find_singleton(self):
        """Test find on singleton sets."""
        uf = UnionFind(["A", "B"])

        assert uf.find("A") == "A"
        assert uf.find("B") == "B"
        assert not uf.connected("A", "B")

    def test_union_basic(self):
        """Test basic union operations."""
        uf = UnionFind(["A", "B", "C"])

        # Union A and B
        assert uf.union("A", "B") is True
        assert uf.connected("A", "B")
        assert uf.find("A") == uf.find("B")
        assert uf.get_set_count() == 2

        # Union B and C (connects to A too)
        assert uf.union("B", "C") is True
        assert uf.connected("A", "C")
        assert uf.get_set_count() == 1
        assert uf.get_set_size("A") == 3

    def test_union_already_connected(self):
        """Test union when elements are already connected."""
        uf = UnionFind(["A", "B"])

        uf.union("A", "B")
        assert uf.union("A", "B") is False  # Already connected
        assert uf.union("B", "A") is False  # Same set

    def test_union_by_size(self):
        """Test union by size variant."""
        uf = UnionFind()

        # Create sets of different sizes
        uf.make_set("A")
        uf.make_set("B")
        uf.make_set("C")
        uf.make_set("D")
        uf.make_set("E")

        # Connect to create different sizes
        uf.union("A", "B")  # Size 2
        uf.union("C", "D")  # Size 2
        uf.union("C", "E")  # Size 3

        # Now union by size: smaller (2) should attach to larger (3)
        assert uf.union_by_size("A", "C") is True
        assert uf.get_set_size("A") == 5  # All elements
        assert uf.get_set_count() == 1

    def test_path_compression(self):
        """Test that path compression works."""
        uf = UnionFind()

        # Create a chain: A -> B -> C -> D
        uf.make_set("A")
        uf.make_set("B")
        uf.make_set("C")
        uf.make_set("D")

        uf.union("A", "B")
        uf.union("B", "C")
        uf.union("C", "D")

        # All should have same root
        root = uf.find("A")
        assert uf.find("B") == root
        assert uf.find("C") == root
        assert uf.find("D") == root

        # After path compression, parent pointers should be direct
        assert uf.parent["A"] == root
        assert uf.parent["B"] == root
        assert uf.parent["C"] == root
        assert uf.parent["D"] == root

    def test_get_all_sets(self):
        """Test getting all disjoint sets."""
        uf = UnionFind(["A", "B", "C", "D", "E"])

        uf.union("A", "B")
        uf.union("C", "D")

        sets = uf.get_all_sets()

        assert len(sets) == 3  # Three sets: {A,B}, {C,D}, {E}

        # Check set contents
        set_contents = [set(elements) for elements in sets.values()]
        assert {"A", "B"} in set_contents
        assert {"C", "D"} in set_contents
        assert {"E"} in set_contents

    def test_error_handling(self):
        """Test error handling for invalid operations."""
        uf = UnionFind()

        # Element not found
        try:
            uf.find("A")
            assert False, "Expected ValueError when finding non-existent element"
        except ValueError:
            pass

        try:
            uf.union("A", "B")
            assert False, "Expected ValueError when unioning non-existent elements"
        except ValueError:
            pass

        try:
            uf.connected("A", "B")
            assert False, "Expected ValueError when checking connectivity of non-existent elements"
        except ValueError:
            pass

    def test_string_representations(self):
        """Test string representations."""
        uf = UnionFind(["A", "B", "C"])
        uf.union("A", "B")

        str_repr = str(uf)
        assert "UnionFind" in str_repr
        assert "2 sets" in str_repr

        repr_str = repr(uf)
        assert "UnionFind" in repr_str


class TestUnionFindAnalysis:
    """Test Union-Find analysis tools."""

    def test_benchmark_operations(self):
        """Test operation benchmarking."""
        uf = UnionFind(["A", "B", "C", "D"])
        operations = [
            ("union", ("A", "B")),
            ("union", ("C", "D")),
            ("find", ("A",)),
            ("connected", ("A", "B")),
            ("connected", ("A", "C")),
        ]

        results = UnionFindAnalysis.benchmark_operations(uf, operations)

        assert results["total_operations"] == 5
        assert results["union_count"] == 2
        assert results["find_count"] == 1
        assert results["connected_count"] == 2
        assert results["actual_merges"] == 2  # Both unions succeeded
        assert results["time_taken"] >= 0
        assert results["avg_time_per_op"] >= 0

    def test_analyze_structure(self):
        """Test structure analysis."""
        uf = UnionFind(["A", "B", "C", "D", "E"])

        uf.union("A", "B")
        uf.union("C", "D")

        analysis = UnionFindAnalysis.analyze_structure(uf)

        assert analysis["total_elements"] == 5
        assert analysis["total_sets"] == 3
        assert analysis["max_set_size"] == 2
        assert analysis["min_set_size"] == 1
        assert analysis["avg_set_size"] == 5 / 3  # 1.666...

    def test_generate_random_operations(self):
        """Test random operation generation."""
        elements = ["A", "B", "C", "D"]
        operations = UnionFindAnalysis.generate_random_operations(elements, 10)

        assert len(operations) == 10

        for op_type, args in operations:
            assert op_type in ["union", "find", "connected"]
            if op_type == "union":
                assert len(args) == 2
            else:
                assert len(args) == 1 if op_type == "find" else 2

            # All args should be from elements
            for arg in args:
                assert arg in elements

    def test_correctness_testing(self):
        """Test correctness verification."""
        elements = ["A", "B", "C"]
        operations = [
            ("union", ("A", "B")),
            ("find", ("A",)),
            ("connected", ("A", "B")),
        ]

        assert UnionFindAnalysis.test_correctness(elements, operations)

        # Test with invalid operation
        bad_operations = [("invalid_op", ("A",))]
        assert not UnionFindAnalysis.test_correctness(elements, bad_operations)


class TestKruskalWithUnionFind:
    """Test Kruskal's MST using Union-Find."""

    def test_kruskal_simple(self):
        """Test Kruskal's algorithm on simple graph."""
        vertices = ["A", "B", "C", "D"]
        edges = [
            ("A", "B", 1.0),
            ("A", "C", 3.0),
            ("B", "C", 2.0),
            ("B", "D", 4.0),
            ("C", "D", 5.0),
        ]

        mst = KruskalWithUnionFind.kruskal_mst(vertices, edges)

        # Should have 3 edges for 4 vertices
        assert len(mst) == 3

        # Calculate total weight
        total_weight = sum(weight for _, _, weight in mst)
        assert total_weight == 7.0  # 1 + 2 + 4

        # Check that it's a valid tree (connected, no cycles)
        # All vertices should be connected
        uf_test = UnionFind(vertices)
        for u, v, _ in mst:
            uf_test.union(u, v)

        assert uf_test.get_set_count() == 1  # All connected

    def test_kruskal_with_analysis(self):
        """Test Kruskal's with detailed analysis."""
        vertices = ["A", "B", "C"]
        edges = [
            ("A", "B", 1.0),
            ("B", "C", 2.0),
            ("A", "C", 3.0),
        ]

        analysis = KruskalWithUnionFind.kruskal_with_analysis(vertices, edges)

        assert len(analysis["mst"]) == 2
        assert analysis["total_weight"] == 3.0  # 1 + 2
        assert analysis["edges_in_mst"] == 2
        assert analysis["total_edges_considered"] == 3
        assert analysis["final_sets"] == 1  # All connected
        assert analysis["total_time"] >= 0

    def test_kruskal_disconnected(self):
        """Test Kruskal's on disconnected graph."""
        vertices = ["A", "B", "C", "D"]
        edges = [
            ("A", "B", 1.0),
            ("C", "D", 2.0),
            # No edge between {A,B} and {C,D}
        ]

        mst = KruskalWithUnionFind.kruskal_mst(vertices, edges)

        # Should have 2 edges (one for each component)
        assert len(mst) == 2
        assert sum(weight for _, _, weight in mst) == 3.0  # 1 + 2

        # Should result in 2 components
        uf_test = UnionFind(vertices)
        for u, v, _ in mst:
            uf_test.union(u, v)

        assert uf_test.get_set_count() == 2


class TestConnectivityChecker:
    """Test connectivity applications."""

    def test_connected_components(self):
        """Test finding connected components."""
        vertices = ["A", "B", "C", "D", "E"]
        edges = [
            ("A", "B"),
            ("B", "C"),
            ("D", "E"),
            # F is isolated
        ]

        components = ConnectivityChecker.connected_components(vertices, edges)

        assert len(components) == 2  # {A,B,C} and {D,E}

        component_sets = [set(comp) for comp in components]
        assert {"A", "B", "C"} in component_sets
        assert {"D", "E"} in component_sets

    def test_has_cycle_acyclic(self):
        """Test cycle detection on acyclic graph."""
        vertices = ["A", "B", "C", "D"]
        edges = [
            ("A", "B"),
            ("B", "C"),
            ("C", "D"),
        ]

        assert not ConnectivityChecker.has_cycle(vertices, edges)

    def test_has_cycle_cyclic(self):
        """Test cycle detection on cyclic graph."""
        vertices = ["A", "B", "C"]
        edges = [
            ("A", "B"),
            ("B", "C"),
            ("C", "A"),  # Cycle
        ]

        assert ConnectivityChecker.has_cycle(vertices, edges)

    def test_minimum_spanning_forest(self):
        """Test minimum spanning forest."""
        vertices = ["A", "B", "C", "D"]
        edges = [
            ("A", "B", 1.0),
            ("C", "D", 2.0),
            # Disconnected components
        ]

        forest = ConnectivityChecker.minimum_spanning_forest(vertices, edges)

        assert len(forest) == 2  # Two edges for two components
        total_weight = sum(weight for _, _, weight in forest)
        assert total_weight == 3.0  # 1 + 2


class TestUnionFindPerformance:
    """Test Union-Find performance characteristics."""

    def test_large_union_find(self):
        """Test Union-Find with many elements."""
        size = 1000
        elements = list(range(size))
        uf = UnionFind(elements)

        # Perform many unions
        for i in range(0, size - 1, 2):
            uf.union(i, i + 1)

        # Should have size/2 sets
        assert uf.get_set_count() == size // 2

    def test_union_find_amortized_performance(self):
        """Test that operations are effectively constant time."""
        size = 10000
        elements = list(range(size))
        uf = UnionFind(elements)

        # Perform many operations
        operations = UnionFindAnalysis.generate_random_operations(elements, 50000)

        start_time = time.time()
        UnionFindAnalysis.benchmark_operations(uf, operations)
        total_time = time.time() - start_time

        # Should be very fast (near-constant time per operation)
        avg_time_per_op = total_time / len(operations)
        assert avg_time_per_op < 0.001  # Less than 1ms per operation

    def test_path_compression_effectiveness(self):
        """Test that path compression keeps trees flat."""
        uf = UnionFind(list(range(100)))

        # Create a long chain
        for i in range(99):
            uf.union(i, i + 1)

        # After path compression, finds should be very fast
        start_time = time.time()
        for _ in range(1000):
            uf.find(50)  # Find in middle of chain
        find_time = time.time() - start_time

        # Should be extremely fast
        assert find_time < 0.01  # Less than 10ms for 1000 finds

    def test_rank_vs_size_heuristics(self):
        """Compare union by rank vs union by size."""
        # Create two UnionFind instances with same operations
        elements = list(range(100))

        uf_rank = UnionFind(elements.copy())
        uf_size = UnionFind(elements.copy())

        # Perform same unions with different heuristics
        for i in range(0, 99, 2):
            uf_rank.union(i, i + 1)
            uf_size.union_by_size(i, i + 1)

        # Both should give same connectivity
        for i in range(99):
            assert uf_rank.connected(i, i + 1) == uf_size.connected(i, i + 1)

        # But internal structure may differ
        rank_analysis = UnionFindAnalysis.analyze_structure(uf_rank)
        size_analysis = UnionFindAnalysis.analyze_structure(uf_size)

        # Both should be correct
        assert rank_analysis["total_sets"] == size_analysis["total_sets"]


class TestUnionFindEdgeCases:
    """Test edge cases and special scenarios."""

    def test_single_element_operations(self):
        """Test operations with single elements."""
        uf = UnionFind(["A"])

        assert uf.find("A") == "A"
        assert uf.connected("A", "A")
        assert uf.get_set_size("A") == 1
        assert uf.get_set_count() == 1

    def test_duplicate_unions(self):
        """Test many duplicate union operations."""
        uf = UnionFind(["A", "B"])

        # Many duplicate unions
        for _ in range(10):
            uf.union("A", "B")

        assert uf.get_set_count() == 1
        assert uf.connected("A", "B")

    def test_union_with_self(self):
        """Test union of element with itself."""
        uf = UnionFind(["A"])

        # Union with self should not change anything
        assert uf.union("A", "A") is False
        assert uf.get_set_count() == 1

    def test_large_number_of_sets(self):
        """Test with many small sets."""
        uf = UnionFind(list(range(1000)))

        # No unions - should have 1000 sets
        assert uf.get_set_count() == 1000

        # Union pairs
        for i in range(0, 1000, 2):
            if i + 1 < 1000:
                uf.union(i, i + 1)

        assert uf.get_set_count() == 500

    def test_deep_nesting_with_path_compression(self):
        """Test path compression with deep trees."""
        uf = UnionFind()

        # Create a deep tree structure
        for i in range(1, 51):  # 1 to 50
            uf.make_set(i)

        # Create a linear chain: 1-2-3-...-50
        for i in range(1, 50):
            uf.union(i, i + 1)

        # Find on leaf should compress entire path
        root = uf.find(50)

        # After path compression, all should point directly to root
        for i in range(1, 51):
            assert uf.parent[i] == root

    def test_mixed_operations(self):
        """Test mix of all operations."""
        uf = UnionFind(list("ABCDEFGHIJ"))

        # Mix of operations
        operations = [
            ("union", ["A", "B"]),
            ("union", ["C", "D"]),
            ("union", ["E", "F"]),
            ("find", ["A"]),
            ("connected", ["A", "B"]),
            ("connected", ["A", "C"]),
            ("union", ["A", "C"]),
            ("find", ["D"]),
            ("union", ["G", "H"]),
            ("union", ["H", "I"]),
            ("connected", ["G", "I"]),
            ("union", ["G", "J"]),  # Union J with G to include it in the set
        ]

        for op, args in operations:
            if op == "union":
                uf.union(args[0], args[1])
            elif op == "find":
                uf.find(args[0])
            elif op == "connected":
                uf.connected(args[0], args[1])

        # Final state checks
        assert uf.connected("A", "D")  # A-B and C-D and A-C
        assert uf.connected("G", "I")  # G-H-I
        assert not uf.connected("A", "G")
        assert uf.get_set_count() == 3  # {A,B,C,D}, {E,F}, {G,H,I,J}

if __name__ == "__main__":
    # Run all test methods
    test_classes = [
        TestUnionFind,
        TestUnionFindAnalysis,
        TestKruskalWithUnionFind,
        TestConnectivityChecker,
        TestUnionFindPerformance,
        TestUnionFindEdgeCases,
    ]

    total_passed = 0
    total_failed = 0

    for testClass in test_classes:
        instance = testClass()
        methods = [method for method in dir(instance) if method.startswith("test_")]

        print(f"\nRunning {testClass.__name__} tests...")
        class_passed = 0
        class_failed = 0

        for method_name in methods:
            try:
                method = getattr(instance, method_name)
                method()
                print(f"  ✓ {method_name}")
                class_passed += 1
            except Exception as e:
                print(f"  ✗ {method_name}: {e}")
                class_failed += 1

        print(f"  Results: {class_passed} passed, {class_failed} failed")
        total_passed += class_passed
        total_failed += class_failed

    print(
        f"\n🎉 Final Results: {total_passed} tests passed, {total_failed} tests failed"
    )

    if total_failed > 0:
        print("Some tests failed - check implementation compatibility")
    else:
        print("🎉 All Chapter 22 sets tests passed successfully!")
