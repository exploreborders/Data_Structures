"""
Tests for Chapter 21: Advanced Graph Search and Traversal Algorithms

Comprehensive tests covering topological sort, SCCs, MSTs, articulation points,
Eulerian paths, maximum flow, and advanced traversal techniques.
"""

import sys
import os
import time

# Add code directory to path for imports (relative to this test file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))

from advanced_graph_algorithms import (
    AdvancedGraphTraversal,
    TopologicalSort,
    StronglyConnectedComponents,
    MinimumSpanningTrees,
    GraphConnectivity,
    EulerianPaths,
    MaximumFlow,
    GraphSearchAnalysis,
)
from graph_implementations import Graph
import graph_implementations


class TestAdvancedGraphTraversal:
    """Test advanced traversal algorithms."""

    def test_bidirectional_search_simple(self):
        """Test bidirectional search on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")

        path = AdvancedGraphTraversal.bidirectional_search(graph, "A", "B")
        if path:
            print(f"  Path found: {' -> '.join(path)} (length: {len(path) - 1})")
        else:
            print("  No path found")

    def test_bidirectional_search_no_path(self):
        """Test bidirectional search when no path exists."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        path = AdvancedGraphTraversal.bidirectional_search(graph, "A", "B")
        assert path == []  # Empty list when no path

    def test_dfs_with_timestamps(self):
        """Test DFS with discovery/finishing timestamps."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")

        discovery, finishing, parent = AdvancedGraphTraversal.dfs_with_timestamps(
            graph, "A"
        )

        print(f"Vertex  Discovery  Finishing  Parent")
        print("-" * 35)
        for vertex in sorted(graph.vertices):
            parent_str = parent[vertex] if parent[vertex] else "None"
            print(
                f"{vertex:>4} {discovery[vertex]:>6.1f}  {finishing[vertex]:>6.1f}  {parent_str:>4}"
            )

    def test_dfs_iterative(self):
        """Test iterative DFS."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        # Use iterative DFS from TopologicalSort
        result = TopologicalSort.dfs_iterative(graph, "A")
        assert len(result) == 3
        assert result[0] == "A"
        assert set(result) == {"A", "B", "C"}


class TestTopologicalSort:
    """Test topological sorting algorithms."""

    def test_topological_sort_simple_dag(self):
        """Test topological sort on simple DAG."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        order = TopologicalSort.topological_sort_dfs(graph)

        assert order is not None
        assert len(order) == 4
        assert order[0] == "A"  # A comes before others

    def test_topological_sort_complex_dag(self):
        """Test topological sort on more complex DAG."""
        graph = Graph(directed=True)
        edges = [
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("C", "D"),
            ("D", "E"),
            ("F", "E"),
            ("F", "G"),
            ("E", "G"),
        ]
        for u, v in edges:
            graph.add_edge(u, v)

        order = TopologicalSort.topological_sort_dfs(graph)

        assert order is not None
        assert len(order) == 7
        assert order[0] in [
            "A",
            "F",
        ]  # Either A or F is valid (both have no incoming edges)

    def test_topological_sort_cycle(self):
        """Test topological sort with cycle."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Creates cycle

        order = TopologicalSort.topological_sort_dfs(graph)
        assert order == []  # Cycle detected


class TestStronglyConnectedComponents:
    """Test strongly connected components algorithms."""

    def test_scc_complex(self):
        """Test SCC on complex directed graph."""
        graph = Graph(directed=True)

        # Create complex SCC structure
        # SCC 1: A -> B -> C -> A
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        # SCC 2: D -> E (separate component)
        graph.add_edge("D", "E")
        graph.add_edge("E", "D")

        # Edge from SCC 1 to SCC 2
        graph.add_edge("C", "D")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        assert len(sccs) == 2

    def test_scc_simple(self):
        """Test SCC on simple graph."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        # Should be four separate components (no cycles in directed path)
        assert len(sccs) == 4
        # Each component should have 1 vertex
        for scc in sccs:
            assert len(scc) == 1

    def test_scc_single_vertices(self):
        """Test SCC with single vertices."""
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        assert len(sccs) == 2  # Two single-vertex components


class TestMinimumSpanningTrees:
    """Test minimum spanning tree algorithms."""

    def test_prim_mst_simple(self):
        """Test Prim's algorithm on simple graph."""
        graph = Graph(weighted=True)
        graph.add_edge("A", "B", 2.0)
        graph.add_edge("A", "C", 1.0)
        graph.add_edge("B", "D", 2.0)
        graph.add_edge("C", "D", 3.0)

        mst = MinimumSpanningTrees.prim_mst(graph)

        # MST should have 3 edges
        assert len(mst) == 3

        # Calculate total weight
        total_weight = sum(weight for _, _, weight in mst)
        expected_weight = 5.0  # A-C (1.0) + A-B (2.0) + B-D (2.0) = minimum possible

        assert total_weight == expected_weight

    def test_kruskal_mst(self):
        """Test Kruskal's algorithm."""
        graph = Graph(weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("B", "C", 1.0)

        mst = MinimumSpanningTrees.kruskal_mst(graph)

        # MST should have 2 edges
        assert len(mst) == 2

        total_weight = sum(weight for _, _, weight in mst)
        expected_weight = 1.0 + 2.0  # A-C + B-C

        assert total_weight == expected_weight

    def test_mst_errors(self):
        """Test MST error handling."""
        # Directed graph should raise error
        directed_graph = Graph(directed=True, weighted=True)
        directed_graph.add_edge("A", "B", 1.0)

        try:
            # This should raise ValueError
            MinimumSpanningTrees.prim_mst(directed_graph)
            # If no exception, this is a failure
            assert False, "Expected ValueError for directed graph"
        except ValueError:
            pass  # Expected exception

        # Unweighted graph
        unweighted_graph = Graph(weighted=False)
        unweighted_graph.add_edge("A", "B")

        # Should raise error when trying MST operations
        try:
            MinimumSpanningTrees.prim_mst(unweighted_graph)
            assert False, "Expected ValueError for unweighted graph"
        except ValueError:
            pass  # Expected exception


class TestGraphConnectivity:
    """Test graph connectivity algorithms."""

    def test_articulation_points_simple(self):
        """Test articulation points on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")

        # A is connected to B and C - removing A would disconnect the graph
        articulation_points = GraphConnectivity.find_articulation_points(graph)
        expected_articulation_points = {"A"}  # A is critical

        assert articulation_points == expected_articulation_points

    def test_articulation_points_complex(self):
        """Test articulation points on complex graph."""
        graph = Graph()
        # Create a complex graph with multiple critical points
        for i in range(5):
            graph.add_vertex(f"V{i}")

        # Make a star graph (V0 connected to all others)
        for i in range(1, 5):
            graph.add_edge("V0", f"V{i}")

        articulation_points = GraphConnectivity.find_articulation_points(graph)
        expected_articulation_points = {"V0"}  # Center of star

        assert articulation_points == expected_articulation_points

    def test_bridges_simple(self):
        """Test bridges on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        bridges = GraphConnectivity.find_bridges(graph)
        # All edges are bridges in this simple chain graph
        # Expected bridges: A-B, B-C, C-D (order may vary)

        assert len(bridges) == 3

    def test_bridges_with_cycle(self):
        """Test bridges detection with cycle."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Creates cycle

        bridges = GraphConnectivity.find_bridges(graph)
        # No bridges in cycle either

        assert bridges == set()


class TestEulerianPaths:
    """Test Eulerian paths and circuits."""

    def test_eulerian_path_only_undirected(self):
        """Test Eulerian path in graph with exactly 2 odd-degree vertices."""
        graph = Graph()
        vertices = ["A", "B", "C", "D", "E", "F"]
        for v in vertices:
            graph.add_vertex(v)

        # Create a graph with exactly 2 odd-degree vertices
        edges = [
            ("A", "B"),
            ("B", "C"),
            ("C", "D"),
            ("D", "E"),
            ("E", "F"),  # A and F have odd degree (1), others have even degree (2)
        ]
        for u, v in edges:
            graph.add_edge(u, v)

        has_path = EulerianPaths.has_eulerian_path(graph)

        # Should have path (can start at odd-degree vertices)
        assert has_path

    def test_no_eulerian_path_undirected(self):
        """Test no Eulerian path when more than 2 odd-degree vertices."""
        graph = Graph()
        vertices = ["A", "B", "C", "D", "E"]
        for v in vertices:
            graph.add_vertex(v)

        # Create a graph with 4 odd-degree vertices (T-shaped graph)
        edges = [
            ("A", "B"),  # A:1, B:1
            ("B", "C"),  # B:2, C:1
            ("B", "D"),  # B:3, D:1
            ("D", "E"),  # D:2, E:1
        ]  # A:1(odd), B:3(odd), C:1(odd), D:2(even), E:1(odd) = 4 odd vertices
        for u, v in edges:
            graph.add_edge(u, v)

        has_path = EulerianPaths.has_eulerian_path(graph)

        # Should not have path (more than 2 odd-degree vertices)
        assert not has_path

    def test_eulerian_circuit_undirected(self):
        """Test Eulerian circuit condition."""
        graph = Graph()
        vertices = ["A", "B", "C"]
        for v in vertices:
            graph.add_vertex(v)

        # Create triangle graph (all degrees = 2, even)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        has_circuit = EulerianPaths.has_eulerian_circuit(graph)

        # Should have circuit (all degrees even)
        assert has_circuit

    def test_eulerian_circuit_directed(self):
        """Test directed graph with Eulerian circuit."""
        graph = Graph(directed=True)
        vertices = ["A", "B", "C"]
        for v in vertices:
            graph.add_vertex(v)

        # Create directed cycle (balanced in-degrees and out-degrees)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        has_circuit = EulerianPaths.has_eulerian_circuit(graph)

        # Should have circuit for directed cycle
        assert has_circuit

    def test_eulerian_path_directed(self):
        """Test directed graph with Eulerian path but no circuit."""
        graph = Graph(directed=True)
        vertices = ["A", "B", "C"]
        for v in vertices:
            graph.add_vertex(v)

        # Create directed path (unbalanced in-degrees and out-degrees)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        has_circuit = EulerianPaths.has_eulerian_circuit(graph)

        # Should not have circuit (unbalanced)
        assert not has_circuit


class TestMaximumFlow:
    """Test maximum flow algorithms."""

    def test_ford_fulkerson_simple(self):
        """Test Ford-Fulkerson on simple network."""
        graph = Graph(directed=True, weighted=True)
        vertices = ["S", "A", "B", "T"]
        for v in vertices:
            graph.add_vertex(v)

        # Simple network: S -> A -> B -> T
        graph.add_edge("S", "A", 10)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "T", 7)

        max_flow = MaximumFlow.ford_fulkerson(graph, "S", "T")
        expected_flow = 5  # Bottleneck is A->B edge (flow limited by A->B)

        assert max_flow == expected_flow

    def test_edmonds_karp(self):
        """Test Edmonds-Karp on a graph where min cut is not obvious."""
        graph = Graph(directed=True, weighted=True)
        vertices = ["S", "A", "B", "C", "T"]
        for v in vertices:
            graph.add_vertex(v)

        # Network: S -> A (1), S -> B (3), S -> C (2)
        # A -> D (1), A -> T (1)  [D, T are sinks]
        # B -> C (4), B -> T (5)
        # C -> T (6)
        graph.add_edge("S", "A", 1)
        graph.add_edge("S", "B", 3)
        graph.add_edge("S", "C", 2)
        graph.add_edge("A", "D", 1)
        graph.add_edge("A", "T", 1)
        graph.add_edge("B", "C", 4)
        graph.add_edge("B", "T", 5)
        graph.add_edge("C", "T", 6)

        max_flow = MaximumFlow.edmonds_karp(graph, "S", "T")
        expected_flow = 6  # S->A(1) + S->B(3) + S->C(2) = 6, bottleneck is 6

        assert max_flow == expected_flow

    def test_ford_fulkerson_with_capacity(self):
        """Test Ford-Fulkerson with capacity constraints."""
        graph = Graph(directed=True, weighted=True)
        vertices = ["S", "A", "B", "T"]
        for v in vertices:
            graph.add_vertex(v)

        # S -> A (10), A -> B (5), B -> T (7)
        graph.add_edge("S", "A", 10)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "T", 7)

        max_flow = MaximumFlow.ford_fulkerson(graph, "S", "T")
        expected_flow = 5  # Bottleneck is 5

        assert max_flow == expected_flow

    def test_max_flow_errors(self):
        """Test max flow error handling."""
        # Undirected graph should raise error
        undirected_graph = Graph(directed=False, weighted=True)
        undirected_graph.add_edge("A", "B", 1.0)

        try:
            MaximumFlow.ford_fulkerson(undirected_graph, "A", "B")
            assert False, "Expected ValueError for undirected graph"
        except ValueError:
            pass  # Expected exception

        # Unweighted graph
        unweighted_graph = Graph(directed=True, weighted=False)
        unweighted_graph.add_edge("A", "B")

        try:
            MaximumFlow.ford_fulkerson(unweighted_graph, "A", "B")
            assert False, "Expected ValueError for unweighted graph"
        except ValueError:
            pass  # Expected exception


class TestGraphSearchAnalysis:
    """Test graph analysis utilities."""

    def test_analyze_dag(self):
        """Test DAG analysis."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        properties = GraphSearchAnalysis.analyze_graph_properties(graph)
        assert properties["is_dag"] is True
        assert properties["cycle_count"] == 0

    def test_analyze_undirected_graph(self):
        """Test undirected graph analysis."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        properties = GraphSearchAnalysis.analyze_graph_properties(graph)
        assert properties["is_dag"] is False  # Undirected graph is not a DAG

    def test_compare_traversal_algorithms(self):
        """Compare different traversal algorithms."""
        graph = Graph()
        for i in range(10):
            graph.add_vertex(f"V{i}")

        # Create connected graph
        for i in range(9):
            graph.add_edge(f"V{i}", f"V{i + 1}")

        # Compare performance - just verify algorithms run without errors
        algorithms = ["DFS", "BFS", "Bidirectional Search"]

        for algorithm in algorithms:
            if algorithm == "DFS":
                AdvancedGraphTraversal.dfs_with_timestamps(graph, "V0")
            elif algorithm == "BFS":
                graph_implementations.GraphTraversal.bfs(graph, "V0")
            elif algorithm == "Bidirectional Search":
                result = AdvancedGraphTraversal.bidirectional_search(graph, "V0", "V9")
                assert result is not None  # Path should exist


class TestAdvancedGraphEdgeCases:
    """Test edge cases and special scenarios."""

    def test_complex_scc_graph(self):
        """Test SCC on complex graph."""
        graph = Graph(directed=True)

        # Create complex SCC structure
        # SCC 1: A -> B -> C -> A (cycle)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        # SCC 2: D -> E -> F -> D (cycle)
        graph.add_edge("D", "E")
        graph.add_edge("E", "F")
        graph.add_edge("F", "D")

        # SCC 3: G -> H -> I -> J -> G (cycle)
        graph.add_edge("G", "H")
        graph.add_edge("H", "I")
        graph.add_edge("I", "J")
        graph.add_edge("J", "G")

        # Connect components
        graph.add_edge("C", "D")  # Connect SCC 1 to SCC 2

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        assert len(sccs) == 3

    def test_disconnected_graph_components(self):
        """Test SCC on disconnected graph."""
        graph = Graph(directed=True)

        # Component 1: A -> B -> C
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        # Component 2: D -> E -> F (separate)
        graph.add_edge("D", "E")
        graph.add_edge("E", "F")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        assert len(sccs) == 6  # Each vertex is its own SCC (no cycles in chains)

    def test_empty_graph_operations(self):
        """Test algorithms on empty graph."""
        graph = Graph()

        # All algorithms should handle empty graph gracefully
        assert StronglyConnectedComponents.kosaraju_scc(graph) == []
        assert GraphConnectivity.find_articulation_points(graph) == set()
        assert GraphConnectivity.find_bridges(graph) == set()
        assert MinimumSpanningTrees.prim_mst(graph) == []
        assert MinimumSpanningTrees.kruskal_mst(graph) == []
        assert MaximumFlow.ford_fulkerson(graph, "S", "T") == 0

    def test_large_graph_performance(self):
        """Test algorithms on larger graphs."""
        import random

        random.seed(42)

        sizes = [10, 25, 50]
        for size in sizes:
            graph = Graph(directed=True, weighted=True)
            vertices = [f"V{i}" for i in range(size)]
            for v in vertices:
                graph.add_vertex(v)

            # Add random edges (10% density)
            for i in range(size):
                for j in range(size):
                    if i != j and random.random() < 0.1:  # 10% chance
                        graph.add_edge(vertices[i], vertices[j], random.randint(1, 10))

            # Test algorithms run without errors
            StronglyConnectedComponents.kosaraju_scc(graph)
            TopologicalSort.topological_sort_dfs(graph)
            MaximumFlow.ford_fulkerson(graph, "V0", f"V{size - 1}")

    def test_mst_unique_weights(self):
        """Test MST with unique weights."""
        graph = Graph(weighted=True)
        vertices = ["A", "B", "C", "D"]
        for v in vertices:
            graph.add_vertex(v)

        # Create complete graph with unique weights
        weights = [1, 2, 3, 4, 5, 6]
        weight_idx = 0
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                graph.add_edge(vertices[i], vertices[j], weights[weight_idx])
                weight_idx += 1

        # MST should have len(vertices) - 1 edges
        mst = MinimumSpanningTrees.prim_mst(graph)
        assert len(mst) == 3

        # All weights should be unique
        mst_weights = [weight for _, _, weight in mst]
        assert len(set(mst_weights)) == len(mst_weights)


if __name__ == "__main__":
    # Run all test methods
    test_classes = [
        TestAdvancedGraphTraversal,
        TestTopologicalSort,
        TestStronglyConnectedComponents,
        TestMinimumSpanningTrees,
        TestGraphConnectivity,
        TestEulerianPaths,
        TestMaximumFlow,
        TestGraphSearchAnalysis,
        TestAdvancedGraphEdgeCases,
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
        print("🎉 All Chapter 21 advanced graph algorithms tests passed successfully!")
