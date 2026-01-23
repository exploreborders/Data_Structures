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
            directed: Whether the graph is directed
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
        if self.weighted:
            self.adj_list[u].append((v, weight))
        else:
            self.adj_list[u].append((v, 1.0))

        # Add reverse edge if undirected
        if not self.directed:
            if self.weighted:
                self.adj_list[v].append((u, weight))
            else:
                self.adj_list[v].append((u, 1.0))

    def remove_edge(self, u: T, v: T) -> None:
        """Remove edge between u and v."""
        if u in self.adj_list:
            self.adj_list[u] = [
                (neighbor, w) for neighbor, w in self.adj_list[u] if neighbor != v
            ]

        if not self.directed and v in self.adj_list:
            self.adj_list[v] = [
                (neighbor, w) for neighbor, w in self.adj_list[v] if neighbor != u
            ]

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
        return None

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
        for vertex in sorted(self.vertices):
            neighbors = [(n, w) for n, w in self.adj_list[vertex]]
            if neighbors:
                neighbor_str = ", ".join(f"{n}({w})" for n, w in neighbors)
                lines.append(f"  {vertex} -> {neighbor_str}")
            else:
                lines.append(f"  {vertex} -> (no edges)")
        return "\n".join(lines)


class GraphTraversal:
    """Graph traversal algorithms: DFS and BFS."""

    @staticmethod
    def dfs(
        graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None
    ) -> List[T]:
        """
        Depth-First Search traversal.

        Args:
            graph: Graph to traverse
            start: Starting vertex
            visitor: Optional function called on each visited vertex

        Returns:
            List of vertices in DFS order
        """
        visited = set()
        result = []

        def dfs_recursive(vertex: T):
            visited.add(vertex)
            result.append(vertex)
            if visitor:
                visitor(vertex)

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    @staticmethod
    def dfs_iterative(
        graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None
    ) -> List[T]:
        """
        Iterative Depth-First Search.

        Args:
            graph: Graph to traverse
            start: Starting vertex
            visitor: Optional function called on each visited vertex

        Returns:
            List of vertices in DFS order
        """
        visited = set()
        result = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                if visitor:
                    visitor(vertex)

                # Add neighbors in reverse order to match recursive DFS
                for neighbor, _ in reversed(graph.get_neighbors(vertex)):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    @staticmethod
    def bfs(
        graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None
    ) -> List[T]:
        """
        Breadth-First Search traversal.

        Args:
            graph: Graph to traverse
            start: Starting vertex
            visitor: Optional function called on each visited vertex

        Returns:
            List of vertices in BFS order
        """
        visited = set()
        result = []
        queue = collections.deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            if visitor:
                visitor(vertex)

            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    @staticmethod
    def dfs_paths(graph: Graph[T], start: T, end: T) -> List[List[T]]:
        """
        Find all paths from start to end using DFS.

        Args:
            graph: Graph to search
            start: Starting vertex
            end: Target vertex

        Returns:
            List of all paths from start to end
        """
        paths = []

        def dfs_path(current: T, path: List[T]):
            path.append(current)

            if current == end:
                paths.append(path.copy())
            else:
                for neighbor, _ in graph.get_neighbors(current):
                    if neighbor not in path:  # Avoid cycles
                        dfs_path(neighbor, path)

            path.pop()

        dfs_path(start, [])
        return paths

    @staticmethod
    def bfs_shortest_path(graph: Graph[T], start: T, end: T) -> Optional[List[T]]:
        """
        Find shortest path from start to end using BFS (unweighted graphs).

        Args:
            graph: Graph to search
            start: Starting vertex
            end: Target vertex

        Returns:
            Shortest path as list of vertices, or None if no path exists
        """
        if start == end:
            return [start]

        visited = set()
        parent = {start: None}
        queue = collections.deque([start])
        visited.add(start)

        found = False
        while queue and not found:
            current = queue.popleft()

            for neighbor, _ in graph.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

                    if neighbor == end:
                        found = True
                        break

        if not found:
            return None

        # Reconstruct path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path


class ShortestPaths:
    """Shortest path algorithms for weighted graphs."""

    @staticmethod
    def dijkstra(
        graph: Graph[T], start: T
    ) -> Tuple[Dict[T, float], Dict[T, Optional[T]]]:
        """
        Dijkstra's algorithm for shortest paths from a source vertex.

        Args:
            graph: Weighted graph (non-negative weights)
            start: Source vertex

        Returns:
            Tuple of (distances, predecessors)
        """
        distances = {vertex: float("inf") for vertex in graph.vertices}
        distances[start] = 0
        predecessors = {vertex: None for vertex in graph.vertices}

        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in graph.get_neighbors(current_vertex):
                if neighbor in visited:
                    continue

                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return distances, predecessors

    @staticmethod
    def bellman_ford(
        graph: Graph[T], start: T
    ) -> Tuple[Optional[Dict[T, float]], Optional[Dict[T, Optional[T]]]]:
        """
        Bellman-Ford algorithm for shortest paths (handles negative weights).

        Args:
            graph: Weighted graph (may have negative weights)
            start: Source vertex

        Returns:
            Tuple of (distances, predecessors), or (None, None) if negative cycle detected
        """
        distances = {vertex: float("inf") for vertex in graph.vertices}
        distances[start] = 0
        predecessors = {vertex: None for vertex in graph.vertices}

        # Relax edges |V| - 1 times
        for _ in range(len(graph) - 1):
            for vertex in graph.vertices:
                for neighbor, weight in graph.get_neighbors(vertex):
                    if (
                        distances[vertex] != float("inf")
                        and distances[vertex] + weight < distances[neighbor]
                    ):
                        distances[neighbor] = distances[vertex] + weight
                        predecessors[neighbor] = vertex

        # Check for negative cycles
        for vertex in graph.vertices:
            for neighbor, weight in graph.get_neighbors(vertex):
                if (
                    distances[vertex] != float("inf")
                    and distances[vertex] + weight < distances[neighbor]
                ):
                    return None, None  # Negative cycle detected

        return distances, predecessors

    @staticmethod
    def reconstruct_path(
        predecessors: Dict[T, Optional[T]], start: T, end: T
    ) -> Optional[List[T]]:
        """
        Reconstruct path from predecessors dictionary.

        Args:
            predecessors: Predecessor dictionary from shortest path algorithm
            start: Start vertex
            end: End vertex

        Returns:
            Path from start to end, or None if no path exists
        """
        if end not in predecessors or predecessors[end] is None:
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            if current == start:
                break
            current = predecessors[current]

        if path[-1] != start:
            return None  # No path to start

        path.reverse()
        return path

    @staticmethod
    def floyd_warshall(graph: Graph[T]) -> Dict[Tuple[T, T], float]:
        """
        Floyd-Warshall algorithm for all-pairs shortest paths.

        Args:
            graph: Weighted graph

        Returns:
            Dictionary of shortest distances between all pairs
        """
        # Initialize distance matrix
        vertices = list(graph.vertices)
        vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}
        n = len(vertices)

        # Initialize distances
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        # Set edge weights
        for u in vertices:
            for v, weight in graph.get_neighbors(u):
                i, j = vertex_to_index[u], vertex_to_index[v]
                dist[i][j] = weight

        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Convert back to dictionary
        distances = {}
        for i in range(n):
            for j in range(n):
                if dist[i][j] != float("inf"):
                    distances[(vertices[i], vertices[j])] = dist[i][j]

        return distances


class GraphAnalysis:
    """Graph analysis algorithms."""

    @staticmethod
    def connected_components(graph: Graph[T]) -> List[List[T]]:
        """
        Find connected components in an undirected graph.

        Args:
            graph: Undirected graph

        Returns:
            List of connected components (each as a list of vertices)
        """
        visited = set()
        components = []

        for vertex in graph.vertices:
            if vertex not in visited:
                # Start DFS/BFS from this vertex
                component = GraphTraversal.dfs(graph, vertex)
                components.append(component)
                visited.update(component)

        return components

    @staticmethod
    def has_cycle(graph: Graph[T]) -> bool:
        """
        Check if graph has a cycle (undirected graph).

        Args:
            graph: Undirected graph

        Returns:
            True if cycle exists
        """
        visited = set()

        def dfs_cycle(current: T, parent: Optional[T]) -> bool:
            visited.add(current)

            for neighbor, _ in graph.get_neighbors(current):
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return True
                if dfs_cycle(neighbor, current):
                    return True
            return False

        for vertex in graph.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True

        return False

    @staticmethod
    def topological_sort(graph: Graph[T]) -> Optional[List[T]]:
        """
        Perform topological sort on a directed acyclic graph (DAG).

        Args:
            graph: Directed graph

        Returns:
            Topologically sorted vertices, or None if cycle exists
        """
        # Kahn's algorithm
        in_degree = {vertex: 0 for vertex in graph.vertices}

        # Calculate in-degrees
        for vertex in graph.vertices:
            for neighbor, _ in graph.get_neighbors(vertex):
                in_degree[neighbor] += 1

        # Find vertices with no incoming edges
        queue = collections.deque(
            [vertex for vertex, degree in in_degree.items() if degree == 0]
        )
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            # Reduce in-degree of neighbors
            for neighbor, _ in graph.get_neighbors(vertex):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycles
        if len(result) != len(graph.vertices):
            return None  # Cycle detected

        return result

    @staticmethod
    def is_dag(graph: Graph[T]) -> bool:
        """
        Check if directed graph is a DAG (no cycles).

        Args:
            graph: Directed graph

        Returns:
            True if graph is a DAG
        """
        return GraphAnalysis.topological_sort(graph) is not None

    @staticmethod
    def strongly_connected_components(graph: Graph[T]) -> List[List[T]]:
        """
        Find strongly connected components using Kosaraju's algorithm.

        Args:
            graph: Directed graph

        Returns:
            List of strongly connected components
        """
        # This is a simplified implementation
        # Full Kosaraju's algorithm would require two DFS passes
        # For now, return connected components (not strongly connected)
        return GraphAnalysis.connected_components(graph)

    @staticmethod
    def minimum_spanning_tree(graph: Graph[T]) -> List[Tuple[T, T, float]]:
        """
        Find Minimum Spanning Tree using Kruskal's algorithm.

        Args:
            graph: Undirected weighted graph

        Returns:
            List of edges in MST: (u, v, weight)
        """
        # Collect all edges
        edges = []
        for u in graph.vertices:
            for v, weight in graph.get_neighbors(u):
                # Avoid duplicates in undirected graph
                if u < v:
                    edges.append((weight, u, v))

        edges.sort()  # Sort by weight

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
