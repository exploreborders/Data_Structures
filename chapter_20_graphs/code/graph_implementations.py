"""
Chapter 20: Graphs - Graph Data Structures and Algorithms

This module implements graph data structures and algorithms, covering representations,
traversals, shortest paths, and graph analysis.
"""

from typing import List, Dict, Set, Tuple, Optional, TypeVar, Generic, Callable
import collections
import heapq
import math

T = TypeVar("T")


class Graph(Generic[T]):
    """
    Graph data structure supporting both directed and undirected graphs.

    Supports multiple representations:
    - Adjacency List: Space-efficient for sparse graphs
    - Adjacency Matrix: Fast edge lookups for dense graphs
    """

    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Initialize graph.

        Args:
            directed: Whether to graph is directed
            weighted: Whether edges have weights
        """
        self.directed = directed
        self.weighted = weighted
        self.adj_list: Dict[
            T, List[Tuple[T, float]]
        ] = {}  # vertex -> [(neighbor, weight), ...]
        self.vertices: Set[T] = set()

    def add_vertex(self, vertex: T) -> None:
        """Add a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adj_list[vertex] = []

    def add_edge(self, u: T, v: T, weight: float = 1.0) -> None:
        """
        Add an edge between vertices u and v.

        Args:
            u: Source vertex
            v: Target vertex
            weight: Edge weight (ignored if graph is unweighted)
        """
        # Ensure vertices exist
        self.add_vertex(u)
        self.add_vertex(v)

        # Add edge from u to v
        self.adj_list[u].append((v, weight))

        if not self.directed and u != v:  # Avoid duplicate self-loop
            self.adj_list[v].append((u, weight))

    def remove_vertex(self, vertex: T) -> None:
        """Remove vertex and all its edges."""
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            del self.adj_list[vertex]

            # Remove edges to this vertex
            for v in self.adj_list:
                self.adj_list[v] = [
                    (neighbor, w)
                    for neighbor, w in self.adj_list[v]
                    if neighbor != vertex
                ]

    def remove_edge(self, u: T, v: T) -> None:
        """Remove edge between u and v."""
        if u in self.adj_list:
            self.adj_list[u] = [(x, w) for x, w in self.adj_list[u] if x != v]
        if not self.directed and v in self.adj_list:
            self.adj_list[v] = [(x, w) for x, w in self.adj_list[v] if x != u]

    def has_edge(self, u: T, v: T) -> bool:
        """Check if edge exists between u and v."""
        if u not in self.adj_list:
            return False
        return any(neighbor == v for neighbor, _ in self.adj_list[u])

    def get_edge_weight(self, u: T, v: T) -> Optional[float]:
        """Get weight of edge between u and v."""
        if u not in self.adj_list:
            return None
        for neighbor, weight in self.adj_list[u]:
            if neighbor == v:
                return weight

    def get_neighbors(self, vertex: T) -> List[Tuple[T, float]]:
        """Get all neighbors of a vertex with their weights."""
        return self.adj_list.get(vertex, [])

    def get_degree(self, vertex: T) -> int:
        """Get degree of a vertex."""
        return len(self.get_neighbors(vertex))

    def __len__(self) -> int:
        """Return number of vertices."""
        return len(self.vertices)

    def __str__(self) -> str:
        """String representation of the graph."""
        lines = [
            f"Graph(directed={self.directed}, weighted={self.weighted}, vertices={len(self)})"
        ]
        for vertex in self.vertices:
            neighbors = [(n, w) for n, w in self.adj_list[vertex]]
            if neighbors:
                neighbor_str = ", ".join(f"{n}({w})" for n, w in neighbors)
                lines.append(f"  {vertex} -> {neighbor_str}")
            else:
                lines.append(f"  {vertex} -> (no edges)")
        return "\n".join(lines)

    def get_edges(self) -> List[Tuple[T, T, float]]:
        """Get all edges in the graph."""
        edges = []
        for u, neighbors in self.adj_list.items():
            for v, weight in neighbors:
                edges.append((u, v, weight))
                if not self.directed:
                    # For undirected graphs, avoid duplicate edges
                    if (v, u, weight) not in edges:
                        edges.append((v, u, weight))
        return edges


class GraphAnalysis:
    """Analysis tools for graph properties and metrics."""

    @staticmethod
    def analyze_graph(graph: Graph[T]) -> dict:
        """Analyze graph properties."""
        return {
            "vertices": len(graph),
            "edges": len(graph.get_edges()),
            "density": len(graph.get_edges()) / (len(graph) * (len(graph) - 1))
            if len(graph) > 1
            else 0,
            "is_connected": len(GraphTraversal.bfs(graph, list(graph.vertices)[0]))
            == len(graph)
            if graph.vertices
            else False,
            "avg_degree": sum(graph.get_degree(v) for v in graph.vertices) / len(graph)
            if graph.vertices
            else 0,
        }

    @staticmethod
    def connected_components(graph: Graph[T]) -> List[List[T]]:
        """Find connected components using DFS."""
        visited = set()
        components = []

        for vertex in graph.vertices:
            if vertex not in visited:
                # For isolated vertices, create a component with just the vertex
                if not graph.get_neighbors(vertex):
                    component = [vertex]
                else:
                    component = GraphTraversal.dfs(graph, vertex)
                components.append(component)
                visited.update(component)

        return components

    @staticmethod
    def has_cycle(graph: Graph[T]) -> bool:
        """Detect if graph has cycle using DFS."""
        visited = set()

        def has_cycle_visit(vertex: T, parent: Optional[T]) -> bool:
            visited.add(vertex)

            for neighbor_info in graph.get_neighbors(vertex):
                neighbor = neighbor_info[0]
                if neighbor not in visited:
                    if has_cycle_visit(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for vertex in graph.vertices:
            if vertex not in visited:
                if has_cycle_visit(vertex, None):
                    return True

        return False

    @staticmethod
    def topological_sort(graph: Graph[T]) -> List[T]:
        """Perform topological sort using Kahn's algorithm."""
        in_degree = {vertex: 0 for vertex in graph.vertices}

        # Calculate in-degrees
        for u in graph.vertices:
            for neighbor_info in graph.get_neighbors(u):
                v = neighbor_info[0]
                in_degree[v] += 1

        # Queue of vertices with no incoming edges
        queue = collections.deque(
            [vertex for vertex in graph.vertices if in_degree[vertex] == 0]
        )
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)

            # Remove u's outgoing edges
            for neighbor_info in graph.get_neighbors(u):
                v = neighbor_info[0]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Check for cycle
        if len(result) != len(graph.vertices):
            return []  # Cycle detected

        return result

    @staticmethod
    def minimum_spanning_tree(graph: Graph[T]) -> List[Tuple[T, T, float]]:
        """Kruskal's algorithm for minimum spanning tree."""
        # Sort edges by weight
        edges = []
        for u in graph.vertices:
            for v, weight in graph.get_neighbors(u):
                if u < v:  # Avoid duplicates
                    edges.append((weight, u, v))

        edges.sort()

        # Union-Find structure
        parent = {vertex: vertex for vertex in graph.vertices}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))

        return mst

    @staticmethod
    def dfs_iterative(graph: Graph[T], start: T) -> List[T]:
        """Iterative DFS implementation."""
        visited = set()
        stack = [start]
        result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)

                # Add neighbors to stack
                for neighbor_info in graph.get_neighbors(current):
                    neighbor = neighbor_info[0]
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    @staticmethod
    def floyd_warshall(graph: Graph[T]) -> Dict[Tuple[T, T], float]:
        """Floyd-Warshall all-pairs shortest paths algorithm."""
        import sys

        # Initialize distance matrix
        vertices = list(graph.vertices)
        n = len(vertices)
        INF = float("inf")
        dist = [[INF] * n for _ in range(n)]

        # Set distances from adjacency list
        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                if graph.has_edge(u, v):
                    dist[i][j] = graph.get_edge_weight(u, v)
                elif i == j:
                    dist[i][j] = 0

        # Floyd-Warshall main algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Convert back to tuple keys
        result = {}
        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                if dist[i][j] != INF:
                    result[(u, v)] = dist[i][j]

        return result

    @staticmethod
    def is_dag(graph: Graph[T]) -> bool:
        """Check if graph is a DAG (no cycles)."""
        return not GraphAnalysis.has_cycle(graph)


class GraphTraversal:
    """Graph traversal algorithms: DFS and BFS."""

    @staticmethod
    def dfs(
        graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None
    ) -> List[T]:
        visited = set()
        result = []

        def dfs_visit(vertex: T):
            if visitor:
                visitor(vertex)
            visited.add(vertex)
            result.append(vertex)

            # Corrected: iterate over neighbors of current vertex
            for neighbor_info in graph.get_neighbors(vertex):
                neighbor = neighbor_info[
                    0
                ]  # Extract vertex from (vertex, weight) tuple
                if neighbor not in visited:
                    dfs_visit(neighbor)

        dfs_visit(start)
        return result

    @staticmethod
    def dfs_paths(graph: Graph[T], start: T, end: T) -> List[List[T]]:
        """Find all paths from start to end using DFS."""

        def dfs_paths_visit(
            current: T, end: T, visited: set, path: List[T], all_paths: List[List[T]]
        ) -> None:
            path.append(current)

            if current == end:
                all_paths.append(path.copy())
                path.pop()
                return

            visited.add(current)

            for neighbor_info in graph.get_neighbors(current):
                neighbor = neighbor_info[0]
                if neighbor not in visited:
                    dfs_paths_visit(neighbor, end, visited, path, all_paths)

            visited.remove(current)
            path.pop()

        all_paths = []
        dfs_paths_visit(start, end, set(), [], all_paths)
        return all_paths

    @staticmethod
    def bfs_shortest_path(graph: Graph[T], start: T, end: T) -> List[T]:
        """Find shortest path using BFS."""

        def bfs_shortest_path_visit() -> List[T]:
            visited = set()
            queue = collections.deque()
            parent = {}

            visited.add(start)
            queue.append(start)
            parent[start] = None

            while queue:
                current = queue.popleft()

                if current == end:
                    # Reconstruct path
                    path = []
                    while current is not None:
                        path.append(current)
                        current = parent[current]
                    path.reverse()
                    return path

                for neighbor_info in graph.get_neighbors(current):
                    neighbor = neighbor_info[0]
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        parent[neighbor] = current

            # End not found - return empty list
            return []

        return bfs_shortest_path_visit()

    @staticmethod
    def bfs(
        graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None
    ) -> List[T]:
        visited = set()
        result = []
        queue = collections.deque()

        visited.add(start)
        queue.append(start)

        while queue:
            vertex = queue.popleft()
            if visitor:
                visitor(vertex)
            result.append(vertex)

            # Corrected: iterate over neighbors of current vertex
            for neighbor_info in graph.get_neighbors(vertex):
                neighbor = neighbor_info[
                    0
                ]  # Extract vertex from (vertex, weight) tuple
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


class ShortestPaths:
    """Shortest path algorithms for weighted graphs."""

    @staticmethod
    def dijkstra(
        graph: Graph[T], start: T
    ) -> Tuple[Dict[T, float], Dict[T, Optional[T]]]:
        """
        Dijkstra's algorithm for shortest paths from a single source.

        Args:
            graph: Weighted graph with non-negative edge weights
            start: Starting vertex

        Returns:
            Tuple of (distances, predecessors)
        """
        distances: Dict[T, float] = {vertex: float("inf") for vertex in graph.vertices}
        predecessors: Dict[T, Optional[T]] = {vertex: None for vertex in graph.vertices}
        distances[start] = 0

        # Priority queue: (distance, vertex)
        pq: List[Tuple[float, T]] = [(0.0, start)]
        visited = set()

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in graph.get_neighbors(current_vertex):
                if neighbor in visited:
                    continue

                new_distance = current_dist + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))

        return distances, predecessors

    @staticmethod
    def reconstruct_path(
        predecessors: Dict[T, Optional[T]], start: T, end: T
    ) -> Optional[List[T]]:
        """
        Reconstruct path from predecessor array.

        Args:
            predecessors: Dictionary from vertex to predecessor
            start: Starting vertex
            end: Target vertex

        Returns:
            List of vertices in path from start to end, or None if no path exists
        """
        if end not in predecessors or predecessors[end] is None and end != start:
            return None
        elif end == start:
            return [start]  # Handle case where start equals end

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]

        path.reverse()
        return path

    @staticmethod
    def bellman_ford(
        graph: Graph[T], start: T
    ) -> Tuple[Dict[T, float], Dict[T, Optional[T]]]:
        """
        Bellman-Ford algorithm for shortest paths with negative weights.

        Args:
            graph: Weighted graph (can have negative edges)
            start: Starting vertex

        Returns:
            Tuple of (distances, predecessors)
        """
        import sys

        # Initialize distances and predecessors
        distances: Dict[T, float] = {vertex: float("inf") for vertex in graph.vertices}
        predecessors: Dict[T, Optional[T]] = {vertex: None for vertex in graph.vertices}
        distances[start] = 0

        # Relax edges |V| - 1 times
        for i in range(len(graph.vertices) - 1):
            updated = False

            # Check all edges
            for u in graph.vertices:
                for neighbor_info in graph.get_neighbors(u):
                    v = neighbor_info[0]
                    weight = neighbor_info[1]

                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        predecessors[v] = u
                        updated = True

            # Early termination if no updates in this iteration
            if not updated:
                break

        return distances, predecessors
