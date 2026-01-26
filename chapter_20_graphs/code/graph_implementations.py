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
        if self.weighted:
            self.adj_list[u].append((v, weight))
        else:
            self.adj_list[u].append((v, 1.0))

        if not self.directed:
            # For undirected graphs, add reverse edge
            if self.weighted:
                self.adj_list[v].append((u, weight))
            else:
                self.adj_list[v].append((u, 1.0))

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


class GraphTraversal:
    """Graph traversal algorithms: DFS and BFS."""

    @staticmethod
    def dfs(graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None) -> List[T]:
        visited = set()
        result = []

        def dfs_visit(vertex: T):
            if visitor:
                visitor(vertex)
            visited.add(vertex)
            result.append(vertex)

            # Corrected: iterate over neighbors of current vertex
            for neighbor in graph.get_neighbors(vertex).keys():  # <-- use .keys() if dict
                if neighbor not in visited:
                    dfs_visit(neighbor)

        dfs_visit(start)
        return result

    @staticmethod
    def bfs(graph: Graph[T], start: T, visitor: Optional[Callable[[T], None]] = None) -> List[T]:
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
            for neighbor in graph.get_neighbors(vertex).keys():  # <-- use .keys() if dict
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
    ) -> List[T]:
        """
        Reconstruct path from predecessor array.

        Args:
            predecessors: Dictionary from vertex to predecessor
            start: Starting vertex
            end: Target vertex

        Returns:
            List of vertices in path from start to end
        """
        if end not in predecessors or predecessors[end] is None and end != start:
            return []

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]

        path.reverse()
        return path
