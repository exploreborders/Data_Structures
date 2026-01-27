"""
Tests for Chapter 20: Graphs - Graph Data Structures and Algorithms

Comprehensive tests covering graph representations, traversals, shortest paths, and analysis.
"""

import sys
import os

# Add to code directory to path
sys.path.insert(0, os.path.join(os.getcwd(), "..", "code"))

from graph_implementations import (
    Graph,
    GraphTraversal,
    ShortestPaths,
    GraphAnalysis,
)


class TestGraph:
    """Test basic Graph functionality."""

    def test_empty_graph(self):
        """Test empty graph initialization."""
        graph = Graph()
        assert len(graph) == 0
        assert not graph.directed
        assert not graph.weighted

    def test_directed_graph(self):
        """Test directed graph."""
        graph = Graph(directed=True)
        assert graph.directed
        assert not graph.weighted

    def test_weighted_graph(self):
        """Test weighted graph."""
        graph = Graph(weighted=True)
        assert not graph.directed
        assert graph.weighted

    def test_add_vertex(self):
        """Test adding vertices."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        assert len(graph) == 2
        assert "A" in graph.vertices
        assert "B" in graph.vertices

    def test_add_edge_undirected(self):
        """Test adding edges to undirected graph."""
        graph = Graph(directed=False)
        graph.add_edge("A", "B", 5.0)

        assert len(graph) == 2
        assert graph.has_edge("A", "B")
        assert graph.has_edge("B", "A")  # Undirected
        assert graph.get_edge_weight("A", "B") == 5.0
        assert graph.get_edge_weight("B", "A") == 5.0

    def test_add_edge_directed(self):
        """Test adding edges to directed graph."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B", 1.0)

        assert len(graph) == 2
        assert graph.has_edge("A", "B")
        assert not graph.has_edge("B", "A")  # Directed
        assert graph.get_edge_weight("A", "B") == 1.0

    def test_remove_edge(self):
        """Test removing edges."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")

        assert graph.has_edge("A", "B")
        assert graph.has_edge("A", "C")

        graph.remove_edge("A", "B")
        assert not graph.has_edge("A", "B")
        assert not graph.has_edge("B", "A")  # Undirected

    def test_remove_vertex(self):
        """Test removing vertices."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")

        graph.remove_vertex("A")

        assert len(graph) == 2  # B and C remain
        assert "A" not in graph.vertices
        assert not graph.has_edge("B", "A")
        assert not graph.has_edge("C", "A")
        assert graph.has_edge("B", "C")  # This edge should remain

    def test_get_neighbors(self):
        """Test getting neighbors."""
        graph = Graph()
        graph.add_edge("A", "B", 1.0)
        graph.add_edge("A", "C", 2.0)

        neighbors = graph.get_neighbors("A")
        assert len(neighbors) == 2

        # Check neighbors (order may vary) - handle list of tuples format
        neighbors = graph.get_neighbors("A")
        assert len(neighbors) == 2

        # Check that expected neighbors are present (order may vary)
        found_B = False
        found_C = False
        neighbor_B_weight = None
        neighbor_C_weight = None

        for neighbor, weight in neighbors:
            if neighbor == "B":
                found_B = True
                neighbor_B_weight = weight
            elif neighbor == "C":
                found_C = True
                neighbor_C_weight = weight

        assert found_B
        assert found_C
        assert neighbor_B_weight == 1.0
        assert neighbor_C_weight == 2.0

    def test_get_degree(self):
        """Test getting vertex degree."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")

        assert graph.get_degree("A") == 3
        assert graph.get_degree("B") == 1  # Undirected

    def test_graph_string_representation(self):
        """Test string representation of graph."""
        graph = Graph()
        graph.add_edge("A", "B", 1.0)

        str_repr = str(graph)
        assert "Graph" in str_repr
        assert "directed=False" in str_repr
        assert "weighted=False" in str_repr


class TestGraphTraversal:
    """Test graph traversal algorithms."""

    def test_dfs_simple(self):
        """Test DFS on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        result = GraphTraversal.dfs(graph, "A")
        assert len(result) == 4
        assert result[0] == "A"  # Starts with A
        assert set(result) == {"A", "B", "C", "D"}

    def test_dfs_paths(self):
        """Test finding all paths with DFS."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        paths = GraphTraversal.dfs_paths(graph, "A", "D")
        assert len(paths) == 2  # Two paths: A-B-D and A-C-D

        # Check that all paths start with A and end with D
        for path in paths:
            assert path[0] == "A"
            assert path[-1] == "D"
            assert "D" in path

    def test_bfs_simple(self):
        """Test BFS on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        result = GraphTraversal.bfs(graph, "A")
        assert len(result) == 4
        assert result[0] == "A"
        assert result[1] in ["B", "C"]  # Level 1
        assert result[-1] == "D"  # Level 2

    def test_bfs_shortest_path_unweighted(self):
        """Test BFS shortest path on unweighted graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")

        path = GraphTraversal.bfs_shortest_path(graph, "A", "E")
        assert path == ["A", "B", "D", "E"] or path == ["A", "C", "D", "E"]

    def test_bfs_shortest_path_no_path(self):
        """Test BFS when no path exists."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        # No edge between A and B
        path = GraphTraversal.bfs_shortest_path(graph, "A", "B")
        assert path == []  # Empty list when no path

    def test_traversal_visitor(self):
        """Test traversal with visitor function."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")

        visited = []

        def visitor(vertex):
            visited.append(vertex)

        GraphTraversal.dfs(graph, "A", visitor)
        assert len(visited) == 3
        assert "A" in visited


class TestShortestPaths:
    """Test shortest path algorithms."""

    def test_dijkstra_simple(self):
        """Test Dijkstra's algorithm on simple weighted graph."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("C", "B", 1.0)
        graph.add_edge("B", "D", 3.0)
        graph.add_edge("C", "D", 5.0)

        distances, predecessors = ShortestPaths.dijkstra(graph, "A")

        assert distances["A"] == 0
        assert distances["B"] == 3.0  # A->C->B = 2+1 = 3
        assert distances["C"] == 2.0
        assert distances["D"] == 6.0  # A->C->B->D = 2+1+3 = 6

    def test_bellman_ford_negative_weights(self):
        """Test Bellman-Ford with negative weights."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("C", "B", -3.0)  # Negative weight!
        graph.add_edge("B", "D", 3.0)

        distances, predecessors = ShortestPaths.bellman_ford(graph, "A")

        assert distances is not None
        assert distances["A"] == 0
        assert distances["B"] == -1.0  # A->C->B = 2+(-3) = -1
        assert distances["C"] == 2.0

    def test_reconstruct_path(self):
        """Test path reconstruction from predecessors."""
        predecessors = {"A": None, "B": "A", "C": "A", "D": "B"}

        path = ShortestPaths.reconstruct_path(predecessors, "A", "D")
        assert path == ["A", "B", "D"]

        path = ShortestPaths.reconstruct_path(predecessors, "A", "C")
        assert path == ["A", "C"]

        # No path
        path = ShortestPaths.reconstruct_path(predecessors, "D", "A")
        assert path is None


class TestGraphAnalysis:
    """Test graph analysis algorithms."""

    def test_connected_components(self):
        """Test finding connected components."""
        graph = Graph()
        # Component 1: A-B-C
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        # Component 2: D-E
        graph.add_edge("D", "E")
        # Component3: F (isolated)

        components = GraphAnalysis.connected_components(graph)

        assert len(components) == 3
        component_sets = [set(comp) for comp in components]
        assert {"A", "B", "C"} in component_sets
        assert {"D", "E"} in component_sets
        assert {
            "F"
        } in component_sets  # F is isolated vertex, should be in its own component

    def test_has_cycle_acyclic(self):
        """Test cycle detection on acyclic graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        assert not GraphAnalysis.has_cycle(graph)

    def test_has_cycle_cyclic(self):
        """Test cycle detection on cyclic graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        assert GraphAnalysis.has_cycle(graph)

    def test_topological_sort_dag(self):
        """Test topological sort on DAG."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        result = GraphAnalysis.topological_sort(graph)

        assert result is not None
        assert len(result) == 4

        # A must come before B and C
        a_index = result.index("A")
        b_index = result.index("B")
        c_index = result.index("C")
        d_index = result.index("D")

        assert a_index < b_index
        assert a_index < c_index
        assert b_index < d_index
        assert c_index < d_index

    def test_topological_sort_cycle(self):
        """Test topological sort detects cycles."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Cycle

        result = GraphAnalysis.topological_sort(graph)
        assert result == []  # Cycle detected (should return empty list)

    def test_minimum_spanning_tree(self):
        """Test Minimum Spanning Tree."""
        graph = Graph(weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("B", "C", 1.0)
        graph.add_edge("B", "D", 3.0)
        graph.add_edge("C", "D", 5.0)

        mst = GraphAnalysis.minimum_spanning_tree(graph)

        # MST should have 3 edges for 4 vertices
        assert len(mst) == 3

        # Calculate total weight
        total_weight = sum(weight for _, _, weight in mst)
        assert total_weight == 6.0  # A-C(2) + C-B(1) + B-D(3) = 6

        # All vertices should be connected
        vertices_in_mst = set()
        for u, v, _ in mst:
            vertices_in_mst.add(u)
            vertices_in_mst.add(v)
        assert vertices_in_mst == {"A", "B", "C", "D"}


class TestGraphEdgeCases:
    """Test edge cases and special scenarios."""

    def test_single_vertex_graph(self):
        """Test graph with single vertex."""
        graph = Graph()
        graph.add_vertex("A")

        assert len(graph) == 1
        assert GraphTraversal.dfs(graph, "A") == ["A"]
        assert GraphTraversal.bfs(graph, "A") == ["A"]

    def test_disconnected_graph(self):
        """Test operations on disconnected graph."""
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")

        # DFS from A should only visit A
        result = GraphTraversal.dfs(graph, "A")
        assert result == ["A"]

    def test_self_loops(self):
        """Test graphs with self-loops."""
        graph = Graph()
        graph.add_edge("A", "A", 1.0)  # Self-loop

        neighbors = graph.get_neighbors("A")
        assert len(neighbors) == 1
        assert neighbors[0][0] == "A"

    def test_multiple_edges(self):
        """Test multiple edges between same vertices."""
        graph = Graph()
        graph.add_edge("A", "B", 1.0)
        graph.add_edge("A", "B", 2.0)  # Second edge

        neighbors = graph.get_neighbors("A")
        assert len(neighbors) == 2  # Both edges present

    def test_large_graph(self):
        """Test operations on larger graph."""
        graph = Graph()
        # Create a complete graph K_5
        vertices = ["A", "B", "C", "D", "E"]
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                graph.add_edge(vertices[i], vertices[j])

        assert len(graph) == 5
        # Each vertex should have degree 4 in K_5
        for vertex in vertices:
            assert graph.get_degree(vertex) == 4

    def test_weighted_vs_unweighted(self):
        """Test behavior with weighted vs unweighted graphs."""
        # Unweighted
        unweighted = Graph()
        unweighted.add_edge("A", "B")
        assert unweighted.get_edge_weight("A", "B") == 1.0  # Default weight

        # Weighted
        weighted = Graph(weighted=True)
        weighted.add_edge("A", "B", 3.14)
        assert weighted.get_edge_weight("A", "B") == 3.14

    def test_directed_vs_undirected(self):
        """Test directed vs undirected graph behavior."""
        # Undirected
        undirected = Graph(directed=False)
        undirected.add_edge("A", "B")
        assert undirected.has_edge("A", "B")
        assert undirected.has_edge("B", "A")

        # Directed
        directed = Graph(directed=True)
        directed.add_edge("A", "B")
        assert directed.has_edge("A", "B")
        assert not directed.has_edge("B", "A")


class TestGraphPerformance:
    """Test graph performance characteristics."""

    def test_traversal_performance(self):
        """Test traversal performance on larger graphs."""
        graph = Graph()

        # Create a linear graph: 1->2->3->...->100
        for i in range(1, 100):
            graph.add_edge(str(i), str(i + 1))

        # DFS should work
        result = GraphTraversal.dfs(graph, "1")
        assert len(result) == 100
        assert result[0] == "1"
        assert result[-1] == "100"

        # BFS should work
        result = GraphTraversal.bfs(graph, "1")
        assert len(result) == 100

    def test_shortest_path_performance(self):
        """Test shortest path performance."""
        graph = Graph(weighted=True)

        # Create a grid-like graph
        for i in range(10):
            for j in range(10):
                vertex = f"{i},{j}"
                graph.add_vertex(vertex)

                # Add edges to adjacent cells
                if i > 0:
                    graph.add_edge(vertex, f"{i - 1},{j}", 1.0)
                if j > 0:
                    graph.add_edge(vertex, f"{i},{j - 1}", 1.0)

        # Test Dijkstra
        distances, _ = ShortestPaths.dijkstra(graph, "0,0")
        assert distances["0,0"] == 0
        assert distances["9,9"] == 18  # Manhattan distance

    def test_graph_analysis_scalability(self):
        """Test graph analysis on moderately sized graphs."""
        graph = Graph()

        # Create a random graph with 50 vertices
        vertices = [str(i) for i in range(50)]
        for v in vertices:
            graph.add_vertex(v)

        # Add random edges (sparse graph)
        import random

        random.seed(42)
        for _ in range(100):  # 100 edges
            u = random.choice(vertices)
            v = random.choice(vertices)
            if u != v:
                graph.add_edge(u, v)

        # Test connected components
        components = GraphAnalysis.connected_components(graph)
        assert len(components) >= 1  # At least one component

        # Test cycle detection
        has_cycle = GraphAnalysis.has_cycle(graph)
        # Result depends on random edges, but algorithm should run


if __name__ == "__main__":
    # Run all test methods
    test_classes = [
        TestGraph,
        TestGraphTraversal,
        TestShortestPaths,
        TestGraphAnalysis,
        TestGraphEdgeCases,
        TestGraphPerformance,
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
        f"\n🎊 Final Results: {total_passed} tests passed, {total_failed} tests failed"
    )

    if total_failed > 0:
        print("Some tests failed - check implementation compatibility")
    else:
        print("🎉 All tests passed successfully!")
