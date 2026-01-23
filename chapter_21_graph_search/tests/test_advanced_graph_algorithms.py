"""
Tests for Chapter 21: Advanced Graph Search and Traversal Algorithms

Comprehensive tests covering topological sort, SCCs, MSTs, articulation points,
Eulerian paths, maximum flow, and advanced traversal algorithms.
"""

import pytest
from chapter_21_graph_search.code.advanced_graph_algorithms import (
    AdvancedGraphTraversal,
    TopologicalSort,
    StronglyConnectedComponents,
    MinimumSpanningTrees,
    GraphConnectivity,
    EulerianPaths,
    MaximumFlow,
    GraphSearchAnalysis,
)
from chapter_20_graphs.code.graph_implementations import Graph


class TestAdvancedGraphTraversal:
    """Test advanced traversal algorithms."""

    def test_bidirectional_search_simple(self):
        """Test bidirectional search on simple graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "C")

        path = AdvancedGraphTraversal.bidirectional_search(graph, "A", "C")
        assert path is not None
        assert path[0] == "A"
        assert path[-1] == "C"
        assert len(path) == 3  # A -> B -> C or A -> D -> C

    def test_bidirectional_search_no_path(self):
        """Test bidirectional search when no path exists."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("C", "D")

        path = AdvancedGraphTraversal.bidirectional_search(graph, "A", "D")
        assert path is None

    def test_dfs_with_timestamps(self):
        """Test DFS with discovery and finishing timestamps."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        discovery, finishing, parent = AdvancedGraphTraversal.dfs_with_timestamps(
            graph, "A"
        )

        # All vertices should have timestamps
        assert len(discovery) == 4
        assert len(finishing) == 4

        # Discovery times should be less than finishing times
        for vertex in graph.vertices:
            assert discovery[vertex] < finishing[vertex]

        # Root should have no parent
        assert parent["A"] is None
        assert parent["B"] == "A"
        assert parent["C"] == "A"
        assert parent["D"] == "B"


class TestTopologicalSort:
    """Test topological sorting algorithms."""

    def test_topological_sort_dag(self):
        """Test topological sort on valid DAG."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "D")

        result = TopologicalSort.topological_sort_dfs(graph)
        assert result is not None
        assert len(result) == 4
        assert set(result) == {"A", "B", "C", "D"}

        # A must come before B and C
        a_idx = result.index("A")
        b_idx = result.index("B")
        c_idx = result.index("C")
        d_idx = result.index("D")

        assert a_idx < b_idx
        assert a_idx < c_idx
        assert b_idx < d_idx
        assert c_idx < d_idx

    def test_topological_sort_cycle(self):
        """Test topological sort detects cycles."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Cycle

        result = TopologicalSort.topological_sort_dfs(graph)
        assert result is None

    def test_topological_sort_complex_dag(self):
        """Test topological sort on more complex DAG."""
        graph = Graph(directed=True)
        # Course prerequisites
        graph.add_edge("CS101", "CS201")  # Intro -> Data Structures
        graph.add_edge("CS101", "CS202")  # Intro -> Algorithms
        graph.add_edge("CS201", "CS301")  # Data Structures -> Advanced DS
        graph.add_edge("CS202", "CS301")  # Algorithms -> Advanced DS
        graph.add_edge("CS201", "CS302")  # Data Structures -> Networks
        graph.add_edge("MATH101", "CS202")  # Math -> Algorithms

        result = TopologicalSort.topological_sort_dfs(graph)
        assert result is not None

        # Check ordering constraints
        courses = ["CS101", "MATH101", "CS201", "CS202", "CS301", "CS302"]
        indices = {course: result.index(course) for course in courses}

        assert indices["CS101"] < indices["CS201"]
        assert indices["CS101"] < indices["CS202"]
        assert indices["CS201"] < indices["CS301"]
        assert indices["CS202"] < indices["CS301"]
        assert indices["CS201"] < indices["CS302"]
        assert indices["MATH101"] < indices["CS202"]


class TestStronglyConnectedComponents:
    """Test strongly connected components algorithms."""

    def test_scc_simple(self):
        """Test SCC on simple directed graph."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Cycle: A -> B -> C -> A
        graph.add_edge("C", "D")  # D is separate

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        # Should have 2 SCCs: {A, B, C} and {D}
        assert len(sccs) == 2
        scc_sets = [set(scc) for scc in sccs]

        assert {"A", "B", "C"} in scc_sets
        assert {"D"} in scc_sets

    def test_scc_complex(self):
        """Test SCC on more complex graph."""
        graph = Graph(directed=True)
        # SCC 1: A -> B -> C -> A
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        # SCC 2: D -> E -> D
        graph.add_edge("D", "E")
        graph.add_edge("E", "D")

        # Connection: C -> D
        graph.add_edge("C", "D")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)
        assert len(sccs) == 2

        scc_sets = [set(scc) for scc in sccs]
        assert {"A", "B", "C"} in scc_sets
        assert {"D", "E"} in scc_sets

    def test_scc_single_vertices(self):
        """Test SCC with isolated vertices."""
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)
        assert len(sccs) == 3

        # Each vertex should be its own SCC
        scc_sets = [set(scc) for scc in sccs]
        assert {"A"} in scc_sets
        assert {"B"} in scc_sets
        assert {"C"} in scc_sets


class TestMinimumSpanningTrees:
    """Test MST algorithms."""

    def test_prim_mst_simple(self):
        """Test Prim's MST on simple graph."""
        graph = Graph(weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("B", "C", 1.0)
        graph.add_edge("B", "D", 3.0)
        graph.add_edge("C", "D", 5.0)

        mst = MinimumSpanningTrees.prim_mst(graph)

        # MST should have 3 edges for 4 vertices
        assert len(mst) == 3

        # Calculate total weight
        total_weight = sum(weight for _, _, weight in mst)
        assert total_weight == 6.0  # A-C(2) + C-B(1) + B-D(3)

        # All vertices should be connected
        vertices_in_mst = set()
        for u, v, _ in mst:
            vertices_in_mst.add(u)
            vertices_in_mst.add(v)
        assert vertices_in_mst == {"A", "B", "C", "D"}

    def test_kruskal_mst(self):
        """Test Kruskal's MST implementation."""
        graph = Graph(weighted=True)
        graph.add_edge("A", "B", 4.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("B", "C", 1.0)
        graph.add_edge("B", "D", 3.0)
        graph.add_edge("C", "D", 5.0)

        mst = MinimumSpanningTrees.kruskal_mst(graph)

        assert len(mst) == 3
        total_weight = sum(weight for _, _, weight in mst)
        assert total_weight == 6.0

    def test_mst_errors(self):
        """Test MST error handling."""
        # Directed graph
        directed_graph = Graph(directed=True, weighted=True)
        directed_graph.add_edge("A", "B", 1.0)

        with pytest.raises(ValueError):
            MinimumSpanningTrees.prim_mst(directed_graph)

        # Unweighted graph
        unweighted_graph = Graph(weighted=False)
        unweighted_graph.add_edge("A", "B")

        with pytest.raises(ValueError):
            MinimumSpanningTrees.prim_mst(unweighted_graph)


class TestGraphConnectivity:
    """Test connectivity and articulation points."""

    def test_articulation_points_simple(self):
        """Test articulation points on simple graph."""
        graph = Graph()
        # Create a graph where B is an articulation point
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("B", "D")

        articulation_points = GraphConnectivity.find_articulation_points(graph)

        # B should be an articulation point
        assert "B" in articulation_points

    def test_articulation_points_complex(self):
        """Test articulation points on more complex graph."""
        graph = Graph()
        # Bridge structure with articulation points
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")
        graph.add_edge("B", "F")  # F is only connected through B

        articulation_points = GraphConnectivity.find_articulation_points(graph)

        assert "B" in articulation_points  # Removing B disconnects F
        assert "C" in articulation_points  # Articulation point in path

    def test_bridges_simple(self):
        """Test finding bridges in graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        bridges = GraphConnectivity.find_bridges(graph)

        # All edges are bridges in this linear graph
        assert len(bridges) == 3
        bridge_set = set((min(u, v), max(u, v)) for u, v in bridges)
        expected_bridges = {("A", "B"), ("B", "C"), ("C", "D")}
        assert bridge_set == expected_bridges

    def test_bridges_with_cycle(self):
        """Test bridges in graph with cycles."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")  # Cycle A-B-C
        graph.add_edge("C", "D")  # Bridge to D

        bridges = GraphConnectivity.find_bridges(graph)

        # Only C-D should be a bridge
        assert len(bridges) == 1
        assert ("C", "D") in bridges or ("D", "C") in bridges


class TestEulerianPaths:
    """Test Eulerian path and circuit algorithms."""

    def test_eulerian_circuit_undirected(self):
        """Test Eulerian circuit in undirected graph."""
        # Create Eulerian circuit: all even degrees
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        assert EulerianPaths.has_eulerian_circuit(graph)
        assert EulerianPaths.has_eulerian_path(graph)

    def test_eulerian_path_only_undirected(self):
        """Test Eulerian path (but not circuit) in undirected graph."""
        # Exactly 2 odd-degree vertices
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "D")

        assert not EulerianPaths.has_eulerian_circuit(graph)
        assert EulerianPaths.has_eulerian_path(graph)

    def test_no_eulerian_path_undirected(self):
        """Test graph with no Eulerian path."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("C", "D")
        # Two separate edges, 4 vertices with degree 1

        assert not EulerianPaths.has_eulerian_circuit(graph)
        assert not EulerianPaths.has_eulerian_path(graph)

    def test_eulerian_circuit_directed(self):
        """Test Eulerian circuit in directed graph."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        assert EulerianPaths.has_eulerian_circuit(graph)
        assert EulerianPaths.has_eulerian_path(graph)

    def test_eulerian_path_directed(self):
        """Test Eulerian path in directed graph."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        # A has out=1, in=0; B has out=1, in=1; C has out=0, in=1

        assert not EulerianPaths.has_eulerian_circuit(graph)
        assert EulerianPaths.has_eulerian_path(graph)


class TestMaximumFlow:
    """Test maximum flow algorithms."""

    def test_ford_fulkerson_simple(self):
        """Test Ford-Fulkerson on simple flow network."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("S", "A", 10.0)  # Source to A
        graph.add_edge("S", "B", 5.0)  # Source to B
        graph.add_edge("A", "B", 15.0)  # A to B
        graph.add_edge("A", "T", 10.0)  # A to sink
        graph.add_edge("B", "T", 10.0)  # B to sink

        max_flow = MaximumFlow.ford_fulkerson(graph, "S", "T")
        assert max_flow == 15.0  # Maximum possible flow

    def test_ford_fulkerson_with_capacity(self):
        """Test Ford-Fulkerson with capacity constraints."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("S", "A", 3.0)
        graph.add_edge("S", "B", 2.0)
        graph.add_edge("A", "B", 1.0)
        graph.add_edge("A", "T", 3.0)
        graph.add_edge("B", "T", 2.0)

        max_flow = MaximumFlow.ford_fulkerson(graph, "S", "T")
        assert max_flow == 4.0

    def test_edmonds_karp(self):
        """Test Edmonds-Karp algorithm."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("S", "A", 10.0)
        graph.add_edge("S", "B", 5.0)
        graph.add_edge("A", "B", 15.0)
        graph.add_edge("A", "T", 10.0)
        graph.add_edge("B", "T", 10.0)

        max_flow = MaximumFlow.edmonds_karp(graph, "S", "T")
        assert max_flow == 15.0

    def test_max_flow_errors(self):
        """Test max flow error handling."""
        # Unweighted graph
        unweighted = Graph(directed=True, weighted=False)
        unweighted.add_edge("S", "T")

        with pytest.raises(ValueError):
            MaximumFlow.ford_fulkerson(unweighted, "S", "T")

        # Undirected graph
        undirected = Graph(directed=False, weighted=True)
        undirected.add_edge("S", "T", 1.0)

        with pytest.raises(ValueError):
            MaximumFlow.ford_fulkerson(undirected, "S", "T")


class TestGraphSearchAnalysis:
    """Test analysis and utility functions."""

    def test_compare_traversal_algorithms(self):
        """Test traversal algorithm comparison."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        results = GraphSearchAnalysis.compare_traversal_algorithms(graph, "A")

        required_algorithms = ["dfs_recursive", "dfs_iterative", "bfs"]
        for algo in required_algorithms:
            assert algo in results
            assert "time" in results[algo]
            assert "vertices_visited" in results[algo]
            assert "order" in results[algo]

            assert results[algo]["vertices_visited"] == 4  # A, B, C, D
            assert results[algo]["time"] >= 0

    def test_analyze_graph_properties(self):
        """Test graph property analysis."""
        graph = Graph(directed=True, weighted=True)
        graph.add_edge("A", "B", 1.0)
        graph.add_edge("A", "C", 2.0)
        graph.add_edge("B", "D", 3.0)

        properties = GraphSearchAnalysis.analyze_graph_properties(graph)

        assert properties["vertices"] == 4
        assert properties["edges"] == 3
        assert properties["directed"] is True
        assert properties["weighted"] is True
        assert properties["avg_degree"] == 1.5  # 6 total degrees / 4 vertices
        assert properties["max_degree"] == 2
        assert properties["min_degree"] == 1

    def test_analyze_undirected_graph(self):
        """Test analysis on undirected graph."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("D", "E")

        properties = GraphSearchAnalysis.analyze_graph_properties(graph)

        assert properties["connected_components"] == 2  # {A,B,C} and {D,E}
        assert "has_cycle" in properties  # Should detect cycle A-B-C

    def test_analyze_dag(self):
        """Test analysis on DAG."""
        graph = Graph(directed=True)
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")

        properties = GraphSearchAnalysis.analyze_graph_properties(graph)

        assert properties["is_dag"] is True
        assert "topological_order" in properties
        assert properties["topological_order"] is not None


class TestAdvancedGraphEdgeCases:
    """Test edge cases for advanced graph algorithms."""

    def test_empty_graph_operations(self):
        """Test operations on empty graphs."""
        graph = Graph()

        # Traversals should handle empty graphs
        dfs_result = AdvancedGraphTraversal.dfs_with_timestamps(graph, "A")
        assert dfs_result == ({}, {}, {})

    def test_single_vertex_graph(self):
        """Test algorithms on single vertex graphs."""
        graph = Graph()
        graph.add_vertex("A")

        # SCC should return single component
        sccs = StronglyConnectedComponents.kosaraju_scc(graph)
        assert len(sccs) == 1
        assert sccs[0] == ["A"]

        # Topological sort should work
        topo = TopologicalSort.topological_sort_dfs(graph)
        assert topo == ["A"]

        # MST should be empty
        mst = MinimumSpanningTrees.prim_mst(graph)
        assert mst == []

    def test_disconnected_graph_components(self):
        """Test algorithms on disconnected graphs."""
        graph = Graph()
        graph.add_edge("A", "B")
        graph.add_edge("C", "D")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)
        assert len(sccs) == 2

        # Both components should be strongly connected
        scc_sets = [set(scc) for scc in sccs]
        assert {"A", "B"} in scc_sets or {"B", "A"} in scc_sets
        assert {"C", "D"} in scc_sets or {"D", "C"} in scc_sets

    def test_large_graph_performance(self):
        """Test algorithms on larger graphs."""
        # Create a larger graph for performance testing
        graph = Graph(directed=True, weighted=True)

        # Add 50 vertices in a linear chain
        for i in range(50):
            graph.add_vertex(str(i))

        for i in range(49):
            graph.add_edge(str(i), str(i + 1), 1.0)

        # Test topological sort
        topo_order = TopologicalSort.topological_sort_dfs(graph)
        assert topo_order is not None
        assert len(topo_order) == 50

        # Verify topological ordering
        indices = {vertex: topo_order.index(vertex) for vertex in topo_order}
        for i in range(49):
            assert indices[str(i)] < indices[str(i + 1)]

    def test_complex_scc_graph(self):
        """Test SCC on complex directed graph."""
        graph = Graph(directed=True)

        # Create multiple SCCs with connections
        # SCC 1: A ↔ B ↔ C
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        # SCC 2: D ↔ E
        graph.add_edge("D", "E")
        graph.add_edge("E", "D")

        # SCC 3: F (single vertex)

        # Connections between SCCs
        graph.add_edge("C", "D")
        graph.add_edge("C", "F")

        sccs = StronglyConnectedComponents.kosaraju_scc(graph)

        # Should have 3 SCCs
        assert len(sccs) == 3
        scc_sets = [set(scc) for scc in sccs]

        assert {"A", "B", "C"} in scc_sets
        assert {"D", "E"} in scc_sets
        assert {"F"} in scc_sets

    def test_mst_unique_weights(self):
        """Test MST with unique edge weights."""
        graph = Graph(weighted=True)

        # Create a complete graph K_4 with unique weights
        vertices = ["A", "B", "C", "D"]
        weights = [1, 2, 3, 4, 5, 6]  # Unique weights for each edge

        idx = 0
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                graph.add_edge(vertices[i], vertices[j], weights[idx])
                idx += 1

        mst_prim = MinimumSpanningTrees.prim_mst(graph)
        mst_kruskal = MinimumSpanningTrees.kruskal_mst(graph)

        # Both should give same total weight
        prim_weight = sum(w for _, _, w in mst_prim)
        kruskal_weight = sum(w for _, _, w in mst_kruskal)

        # For K_4, MST weight should be sum of smallest 3 edges
        expected_weight = sum(sorted(weights)[:3])
        assert prim_weight == expected_weight
        assert kruskal_weight == expected_weight
