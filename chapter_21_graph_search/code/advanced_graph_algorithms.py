"""
Chapter 21: Advanced Graph Search and Traversal Algorithms

This module extends chapter 20 with advanced graph algorithms including topological sort,
strongly connected components, articulation points, and maximum flow algorithms.
"""

from typing import List, Dict, Set, Tuple, Optional, Callable, Any
import collections
import heapq
import math
import sys
import os

# Add parent directory to path for imports
sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "..", "chapter_20_graphs", "code")
)
from graph_implementations import Graph


class AdvancedGraphTraversal:
    """Advanced graph traversal algorithms."""

    @staticmethod
    def bidirectional_search(
        graph: Graph[str], start: str, end: str
    ) -> Optional[List[str]]:
        """
        Bidirectional search - search from both start and end simultaneously.

        Args:
            graph: Graph to search
            start: Starting vertex
            end: Target vertex

        Returns:
            Shortest path if found, None otherwise
        """
        if start == end:
            return [start]

        # Forward search
        forward_visited = set([start])
        forward_parent = {start: None}
        forward_queue = collections.deque([start])

        # Backward search
        backward_visited = set([end])
        backward_parent = {end: None}
        backward_queue = collections.deque([end])

        # For backward search, we need reverse edges
        reverse_graph = AdvancedGraphTraversal._build_reverse_graph(graph)

        while forward_queue and backward_queue:
            # Forward step
            if forward_queue:
                current = forward_queue.popleft()
                for neighbor, _ in graph.get_neighbors(current):
                    if neighbor not in forward_visited:
                        forward_visited.add(neighbor)
                        forward_parent[neighbor] = current
                        forward_queue.append(neighbor)

                        # Check if we met backward search
                        if neighbor in backward_visited:
                            return AdvancedGraphTraversal._construct_path(
                                forward_parent, backward_parent, neighbor
                            )

            # Backward step
            if backward_queue:
                current = backward_queue.popleft()
                for neighbor, _ in reverse_graph.get_neighbors(current):
                    if neighbor not in backward_visited:
                        backward_visited.add(neighbor)
                        backward_parent[neighbor] = current
                        backward_queue.append(neighbor)

                        # Check if we met forward search
                        if neighbor in forward_visited:
                            return AdvancedGraphTraversal._construct_path(
                                forward_parent, backward_parent, neighbor
                            )

        return None

    @staticmethod
    def _build_reverse_graph(graph: Graph[str]) -> Graph[str]:
        """Build reverse graph for bidirectional search."""
        reverse = Graph(directed=graph.directed, weighted=graph.weighted)
        for vertex in graph.vertices:
            reverse.add_vertex(vertex)

        for vertex in graph.vertices:
            for neighbor, weight in graph.get_neighbors(vertex):
                reverse.add_edge(neighbor, vertex, weight)

        return reverse

    @staticmethod
    def _construct_path(
        forward_parent: Dict[str, Optional[str]],
        backward_parent: Dict[str, Optional[str]],
        meeting_point: str,
    ) -> List[str]:
        """Construct path from forward and backward parent dictionaries."""
        # Build path from start to meeting point
        path_start_to_meeting = []
        current = meeting_point
        while current is not None:
            path_start_to_meeting.append(current)
            current = forward_parent[current]
        path_start_to_meeting.reverse()

        # Build path from meeting point to end
        path_meeting_to_end = []
        current = backward_parent[meeting_point]
        while current is not None:
            path_meeting_to_end.append(current)
            current = backward_parent[current]

        # Combine paths (remove duplicate meeting point)
        return path_start_to_meeting + path_meeting_to_end

    @staticmethod
    def dfs_with_timestamps(
        graph: Graph[str], start: str
    ) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
        """
        DFS with discovery and finishing timestamps.

        Returns:
            discovery_time, finishing_time, parent relationships
        """
        discovery_time = {}
        finishing_time = {}
        parent = {}
        time = 0

        visited = set()

        def dfs_visit(vertex: str):
            nonlocal time
            visited.add(vertex)
            time += 1
            discovery_time[vertex] = time

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    dfs_visit(neighbor)

            time += 1
            finishing_time[vertex] = time

        # Initialize parents
        for vertex in graph.vertices:
            parent[vertex] = None

        dfs_visit(start)

        # Handle disconnected components
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs_visit(vertex)

        return discovery_time, finishing_time, parent


class TopologicalSort:
    """Topological sorting algorithms for DAGs."""

    @staticmethod
    def topological_sort_dfs(graph: Graph[str]) -> Optional[List[str]]:
        """
        Topological sort using DFS with finishing times.

        Args:
            graph: Directed acyclic graph

        Returns:
            Topologically sorted vertices, or None if cycle detected
        """
        visited = set()
        visiting = set()  # For cycle detection
        result = []

        def dfs_visit(vertex: str) -> bool:
            visiting.add(vertex)
            visited.add(vertex)

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor in visiting:
                    return False  # Cycle detected
                if neighbor not in visited:
                    if not dfs_visit(neighbor):
                        return False

            visiting.remove(vertex)
            result.append(vertex)  # Add after all dependencies
            return True

        for vertex in graph.vertices:
            if vertex not in visited:
                if not dfs_visit(vertex):
                    return None  # Cycle detected

        result.reverse()  # Reverse to get topological order
        return result

    @staticmethod
    def topological_sort_all(graph: Graph[str]) -> List[List[str]]:
        """
        Find all possible topological orderings.

        Args:
            graph: DAG

        Returns:
            List of all possible topological orderings
        """
        # This is a simplified implementation
        # Full implementation would use backtracking
        order = TopologicalSort.topological_sort_dfs(graph)
        if order is None:
            return []
        return [order]  # Return single ordering for simplicity


class StronglyConnectedComponents:
    """Algorithms for finding strongly connected components."""

    @staticmethod
    def kosaraju_scc(graph: Graph[str]) -> List[List[str]]:
        """
        Kosaraju's algorithm for finding SCCs.

        Args:
            graph: Directed graph

        Returns:
            List of strongly connected components
        """
        # Step 1: DFS on original graph to get finishing times
        finishing_order = []
        visited = set()

        def dfs1(vertex: str):
            visited.add(vertex)
            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs1(neighbor)
            finishing_order.append(vertex)

        for vertex in graph.vertices:
            if vertex not in visited:
                dfs1(vertex)

        # Step 2: Transpose the graph
        transpose = StronglyConnectedComponents._transpose_graph(graph)

        # Step 3: DFS on transposed graph in decreasing finishing time order
        visited.clear()
        sccs = []

        def dfs2(vertex: str, component: List[str]):
            visited.add(vertex)
            component.append(vertex)
            for neighbor, _ in transpose.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs2(neighbor, component)

        while finishing_order:
            vertex = finishing_order.pop()
            if vertex not in visited:
                component = []
                dfs2(vertex, component)
                sccs.append(component)

        return sccs

    @staticmethod
    def tarjan_scc(graph: Graph[str]) -> List[List[str]]:
        """
        Tarjan's algorithm for finding SCCs (simplified implementation).

        Args:
            graph: Directed graph

        Returns:
            List of strongly connected components
        """
        # For educational purposes, we'll use Kosaraju's algorithm
        # Tarjan's algorithm is more complex and requires additional data structures
        return StronglyConnectedComponents.kosaraju_scc(graph)

    @staticmethod
    def _transpose_graph(graph: Graph[str]) -> Graph[str]:
        """Create transpose of directed graph."""
        transpose = Graph(directed=True, weighted=graph.weighted)

        for vertex in graph.vertices:
            transpose.add_vertex(vertex)

        for vertex in graph.vertices:
            for neighbor, weight in graph.get_neighbors(vertex):
                transpose.add_edge(neighbor, vertex, weight)

        return transpose


class MinimumSpanningTrees:
    """Minimum Spanning Tree algorithms."""

    @staticmethod
    def prim_mst(graph: Graph[str]) -> List[Tuple[str, str, float]]:
        mst = []
        visited = set()
        min_heap = []

        start_vertex = next(iter(graph.vertices))
        visited.add(start_vertex)

        # Add edges from start vertex
        for neighbor, weight in graph.get_neighbors(start_vertex).items():  # <- .items()
            heapq.heappush(min_heap, (weight, neighbor, start_vertex))

        while min_heap and len(visited) < len(graph.vertices):
            weight, vertex, parent = heapq.heappop(min_heap)
            if vertex in visited:
                continue
            visited.add(vertex)
            mst.append((parent, vertex, weight))

            for neighbor, edge_weight in graph.get_neighbors(vertex).items():  # <- .items()
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, vertex))

        return mst


    @staticmethod
    def kruskal_mst(graph: Graph[str]) -> List[Tuple[str, str, float]]:
        """
        Kruskal's algorithm for Minimum Spanning Tree (alternative to chapter 20).

        Args:
            graph: Undirected weighted graph

        Returns:
            List of edges in MST: (u, v, weight)
        """
        if not graph.weighted or graph.directed:
            raise ValueError("Kruskal's algorithm requires undirected weighted graph")

        # Sort all edges by weight
        edges = []
        for u in graph.vertices:
            for v, weight in graph.get_neighbors(u).items():
                if u < v:  # Avoid duplicates
                    edges.append((weight, u, v))


        edges.sort()

        # Union-Find structure
        parent = {vertex: vertex for vertex in graph.vertices}
        rank = {vertex: 0 for vertex in graph.vertices}

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                elif rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1
                return True
            return False

        mst = []
        for weight, u, v in edges:
            if union(u, v):
                mst.append((u, v, weight))

        return mst


class GraphConnectivity:
    """Graph connectivity and articulation points."""

    @staticmethod
    def find_articulation_points(graph: Graph[str]) -> List[str]:
        """
        Find articulation points (cut vertices) in undirected graph.

        Args:
            graph: Undirected graph

        Returns:
            List of articulation points
        """
        if graph.directed:
            raise ValueError("Articulation points require undirected graph")

        articulation_points = []
        visited = set()
        discovery_time = {}
        low_time = {}
        parent = {}
        time = 0

        def dfs_ap(vertex: str) -> int:
            nonlocal time
            children = 0
            visited.add(vertex)
            time += 1
            discovery_time[vertex] = time
            low_time[vertex] = time

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    children += 1
                    dfs_ap(neighbor)

                    # Update low time
                    low_time[vertex] = min(low_time[vertex], low_time[neighbor])

                    # Check articulation point conditions
                    if parent.get(vertex) is None and children > 1:
                        articulation_points.append(vertex)
                    elif (
                        parent.get(vertex) is not None
                        and low_time[neighbor] >= discovery_time[vertex]
                    ):
                        articulation_points.append(vertex)

                elif neighbor != parent.get(vertex):
                    low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])

        # Handle disconnected components
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs_ap(vertex)

        return list(set(articulation_points))  # Remove duplicates

    @staticmethod
    def find_bridges(graph: Graph[str]) -> List[Tuple[str, str]]:
        """
        Find bridges (cut edges) in undirected graph.

        Args:
            graph: Undirected graph

        Returns:
            List of bridge edges: (u, v)
        """
        if graph.directed:
            raise ValueError("Bridges require undirected graph")

        bridges = []
        visited = set()
        discovery_time = {}
        low_time = {}
        parent = {}
        time = 0

        def dfs_bridge(vertex: str):
            nonlocal time
            visited.add(vertex)
            time += 1
            discovery_time[vertex] = time
            low_time[vertex] = time

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    dfs_bridge(neighbor)

                    low_time[vertex] = min(low_time[vertex], low_time[neighbor])

                    # Bridge condition
                    if low_time[neighbor] > discovery_time[vertex]:
                        bridges.append((vertex, neighbor))

                elif neighbor != parent.get(vertex):
                    low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])

        for vertex in graph.vertices:
            if vertex not in visited:
                dfs_bridge(vertex)

        return bridges


class EulerianPaths:
    """Eulerian paths and circuits."""

    @staticmethod
    def has_eulerian_path(graph: Graph[str]) -> bool:
        """
        Check if graph has an Eulerian path.

        Args:
            graph: Undirected graph

        Returns:
            True if Eulerian path exists
        """
        if graph.directed:
            return EulerianPaths._has_eulerian_path_directed(graph)
        else:
            return EulerianPaths._has_eulerian_path_undirected(graph)

    @staticmethod
    def has_eulerian_circuit(graph: Graph[str]) -> bool:
        """
        Check if graph has an Eulerian circuit.

        Args:
            graph: Undirected graph

        Returns:
            True if Eulerian circuit exists
        """
        if graph.directed:
            return EulerianPaths._has_eulerian_circuit_directed(graph)
        else:
            return EulerianPaths._has_eulerian_circuit_undirected(graph)

    @staticmethod
    def _has_eulerian_path_undirected(graph: Graph[str]) -> bool:
        """Check Eulerian path for undirected graphs."""
        odd_degree_count = 0
        for vertex in graph.vertices:
            if graph.get_degree(vertex) % 2 == 1:
                odd_degree_count += 1

        return odd_degree_count == 0 or odd_degree_count == 2

    @staticmethod
    def _has_eulerian_circuit_undirected(graph: Graph[str]) -> bool:
        """Check Eulerian circuit for undirected graphs."""
        for vertex in graph.vertices:
            if graph.get_degree(vertex) % 2 == 1:
                return False
        return True

    @staticmethod
    def _has_eulerian_path_directed(graph: Graph[str]) -> bool:
        """Check Eulerian path for directed graphs."""
        in_degrees = {v: 0 for v in graph.vertices}
        out_degrees = {v: 0 for v in graph.vertices}

        for vertex in graph.vertices:
            out_degrees[vertex] = len(graph.get_neighbors(vertex))
            for neighbor, _ in graph.get_neighbors(vertex):
                in_degrees[neighbor] += 1

        start_candidates = sum(
            1 for v in graph.vertices if out_degrees[v] - in_degrees[v] == 1
        )
        end_candidates = sum(
            1 for v in graph.vertices if in_degrees[v] - out_degrees[v] == 1
        )
        balanced = sum(1 for v in graph.vertices if in_degrees[v] == out_degrees[v])

        return (
            start_candidates == 1
            and end_candidates == 1
            and start_candidates + end_candidates + balanced == len(graph.vertices)
        )

    @staticmethod
    def _has_eulerian_circuit_directed(graph: Graph[str]) -> bool:
        """Check Eulerian circuit for directed graphs."""
        in_degrees = {v: 0 for v in graph.vertices}
        out_degrees = {v: 0 for v in graph.vertices}

        for vertex in graph.vertices:
            out_degrees[vertex] = len(graph.get_neighbors(vertex))
            for neighbor, _ in graph.get_neighbors(vertex):
                in_degrees[neighbor] += 1

        return all(in_degrees[v] == out_degrees[v] for v in graph.vertices)


class MaximumFlow:
    """Maximum flow algorithms."""

    @staticmethod
    def ford_fulkerson(graph: Graph[str], source: str, sink: str) -> float:
        """
        Ford-Fulkerson algorithm for maximum flow.

        Args:
            graph: Flow network (weighted directed graph)
            source: Source vertex
            sink: Sink vertex

        Returns:
            Maximum flow value
        """
        if not graph.weighted or not graph.directed:
            raise ValueError("Ford-Fulkerson requires weighted directed graph")

        # Create residual graph
        residual = MaximumFlow._create_residual_graph(graph)

        max_flow = 0

        while True:
            # Find augmenting path using BFS
            path = MaximumFlow._bfs_residual(residual, source, sink)
            if not path:
                break

            # Find minimum residual capacity
            path_flow = float("inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, residual.get_edge_weight(u, v))

            # Update residual capacities
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                # Forward edge
                current_capacity = residual.get_edge_weight(u, v)
                residual.adj_list[u] = [
                    (n, w if n != v else w - path_flow) for n, w in residual.adj_list[u]
                ]

                # Backward edge
                back_capacity = residual.get_edge_weight(v, u) or 0
                residual.adj_list[v] = [
                    (n, w if n != u else w + path_flow) for n, w in residual.adj_list[v]
                ]
                if back_capacity == 0:
                    residual.add_edge(v, u, path_flow)

            max_flow += path_flow

        return max_flow

    @staticmethod
    def edmonds_karp(graph: Graph[str], source: str, sink: str) -> float:
        """
        Edmonds-Karp algorithm (Ford-Fulkerson with BFS).

        Args:
            graph: Flow network
            source: Source vertex
            sink: Sink vertex

        Returns:
            Maximum flow value
        """
        # Edmonds-Karp is just Ford-Fulkerson with BFS
        return MaximumFlow.ford_fulkerson(graph, source, sink)

    @staticmethod
    def _create_residual_graph(graph: Graph[str]) -> Graph[str]:
        """Create residual graph for flow algorithms."""
        residual = Graph(directed=True, weighted=True)

        for vertex in graph.vertices:
            residual.add_vertex(vertex)

        for vertex in graph.vertices:
            for neighbor, capacity in graph.get_neighbors(vertex):
                residual.add_edge(vertex, neighbor, capacity)
                # Add backward edge with 0 capacity
                if not residual.has_edge(neighbor, vertex):
                    residual.add_edge(neighbor, vertex, 0)

        return residual

    @staticmethod
    def _bfs_residual(
        residual: Graph[str], source: str, sink: str
    ) -> Optional[List[str]]:
        """BFS on residual graph to find augmenting path."""
        visited = set()
        parent = {source: None}
        queue = collections.deque([source])
        visited.add(source)

        found = False
        while queue and not found:
            current = queue.popleft()

            for neighbor, capacity in residual.get_neighbors(current):
                if neighbor not in visited and capacity > 0:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

                    if neighbor == sink:
                        found = True
                        break

        if not found:
            return None

        # Reconstruct path
        path = []
        current = sink
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path


class GraphSearchAnalysis:
    """Analysis tools for graph search algorithms."""

    @staticmethod
    def compare_traversal_algorithms(graph: Graph[str], start: str) -> dict:
        """
        Compare performance of different traversal algorithms.

        Args:
            graph: Graph to traverse
            start: Starting vertex

        Returns:
            Performance comparison results
        """
        import time

        results = {}

        # DFS Recursive
        start_time = time.time()
        dfs_result = []

        def dfs_visitor(v):
            dfs_result.append(v)

        from chapter_20_graphs.code.graph_implementations import GraphTraversal

        GraphTraversal.dfs(graph, start, dfs_visitor)
        dfs_time = time.time() - start_time

        # DFS Iterative
        start_time = time.time()
        dfs_iter_result = GraphTraversal.dfs_iterative(graph, start)
        dfs_iter_time = time.time() - start_time

        # BFS
        start_time = time.time()
        bfs_result = GraphTraversal.bfs(graph, start)
        bfs_time = time.time() - start_time

        results["dfs_recursive"] = {
            "time": dfs_time,
            "vertices_visited": len(dfs_result),
            "order": dfs_result,
        }

        results["dfs_iterative"] = {
            "time": dfs_iter_time,
            "vertices_visited": len(dfs_iter_result),
            "order": dfs_iter_result,
        }

        results["bfs"] = {
            "time": bfs_time,
            "vertices_visited": len(bfs_result),
            "order": bfs_result,
        }

        return results

    @staticmethod
    def analyze_graph_properties(graph: Graph[str]) -> dict:
        """
        Analyze structural properties of a graph.

        Args:
            graph: Graph to analyze

        Returns:
            Analysis results
        """
        properties = {
            "vertices": len(graph),
            "directed": graph.directed,
            "weighted": graph.weighted,
        }

        # Count edges
        edge_count = 0
        for vertex in graph.vertices:
            edge_count += len(graph.get_neighbors(vertex))
        if not graph.directed:
            edge_count //= 2  # Undirected edges counted twice
        properties["edges"] = edge_count

        # Degree analysis
        degrees = [graph.get_degree(v) for v in graph.vertices]
        properties["avg_degree"] = sum(degrees) / len(degrees) if degrees else 0
        properties["max_degree"] = max(degrees) if degrees else 0
        properties["min_degree"] = min(degrees) if degrees else 0

        # Connectivity
        from chapter_20_graphs.code.graph_implementations import GraphAnalysis

        components = GraphAnalysis.connected_components(graph)
        properties["connected_components"] = len(components)

        # Cycles (for undirected graphs)
        if not graph.directed:
            has_cycle = GraphAnalysis.has_cycle(graph)
            properties["has_cycle"] = has_cycle

        # DAG properties (for directed graphs)
        if graph.directed:
            is_dag = GraphAnalysis.is_dag(graph)
            properties["is_dag"] = is_dag

            if is_dag:
                topo_order = GraphAnalysis.topological_sort(graph)
                properties["topological_order"] = topo_order

        return properties
