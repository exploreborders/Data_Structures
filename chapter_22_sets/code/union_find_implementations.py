"""
Chapter 22: Sets - Union-Find (Disjoint Set Union) Implementation

This module implements the Union-Find (Disjoint Set Union - DSU) data structure,
providing efficient operations for managing disjoint sets with near-constant time complexity.
"""

from typing import Dict, List, Set, Tuple, Optional, TypeVar, Generic, Any
import random
import time

T = TypeVar("T")


class UnionFind(Generic[T]):
    """
    Union-Find (Disjoint Set Union) data structure.

    Maintains a partition of a set into disjoint subsets with efficient
    union and find operations.

    Time Complexity: Nearly O(1) amortized per operation
    Space Complexity: O(n) for n elements
    """

    def __init__(self, elements: Optional[List[T]] = None):
        """
        Initialize Union-Find structure.

        Args:
            elements: Initial list of elements (optional)
        """
        self.parent: Dict[T, T] = {}
        self.rank: Dict[T, int] = {}
        self.size: Dict[T, int] = {}

        if elements:
            for element in elements:
                self.make_set(element)

    def make_set(self, element: T) -> None:
        """
        Create a new set containing only the given element.

        Args:
            element: Element to create set for
        """
        if element not in self.parent:
            self.parent[element] = element
            self.rank[element] = 0
            self.size[element] = 1

    def find(self, element: T) -> T:
        """
        Find the representative (root) of the set containing the element.

        Uses path compression for optimization.

        Args:
            element: Element to find set for

        Returns:
            Root element of the set
        """
        if element not in self.parent:
            raise ValueError(f"Element {element} not found in Union-Find structure")

        if self.parent[element] != element:
            # Path compression: make all nodes on path point directly to root
            self.parent[element] = self.find(self.parent[element])

        return self.parent[element]

    def union(self, element1: T, element2: T) -> bool:
        """
        Union the sets containing element1 and element2.

        Uses union by rank for optimization.

        Args:
            element1: First element
            element2: Second element

        Returns:
            True if sets were merged, False if already in same set
        """
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 == root2:
            return False  # Already in same set

        # Union by rank: attach smaller rank tree under larger rank tree
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            # Same rank: choose arbitrarily and increase rank
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            self.rank[root1] += 1

        return True

    def union_by_size(self, element1: T, element2: T) -> bool:
        """
        Union using size-based heuristic instead of rank.

        Args:
            element1: First element
            element2: Second element

        Returns:
            True if sets were merged, False if already in same set
        """
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 == root2:
            return False

        # Union by size: attach smaller size tree under larger size tree
        if self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

        return True

    def connected(self, element1: T, element2: T) -> bool:
        """
        Check if two elements are in the same set.

        Args:
            element1: First element
            element2: Second element

        Returns:
            True if elements are in same set
        """
        return self.find(element1) == self.find(element2)

    def get_set_size(self, element: T) -> int:
        """
        Get the size of the set containing the element.

        Args:
            element: Element to check

        Returns:
            Size of the set
        """
        root = self.find(element)
        return self.size[root]

    def get_all_sets(self) -> Dict[T, List[T]]:
        """
        Get all disjoint sets as a dictionary.

        Returns:
            Dictionary mapping root to list of elements in set
        """
        sets: Dict[T, List[T]] = {}

        for element in self.parent:
            root = self.find(element)
            if root not in sets:
                sets[root] = []
            sets[root].append(element)

        return sets

    def get_set_count(self) -> int:
        """
        Get the number of disjoint sets.

        Returns:
            Number of disjoint sets
        """
        roots = set()
        for element in self.parent:
            roots.add(self.find(element))
        return len(roots)

    def __len__(self) -> int:
        """Return number of elements."""
        return len(self.parent)

    def __str__(self) -> str:
        """String representation."""
        sets = self.get_all_sets()
        set_strs = [
            f"{{{', '.join(map(str, elements))}}}" for elements in sets.values()
        ]
        return (
            f"UnionFind({len(self)} elements, {len(sets)} sets: {' | '.join(set_strs)})"
        )

    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"UnionFind(elements={len(self)}, sets={self.get_set_count()})"


class UnionFindAnalysis:
    """Analysis tools for Union-Find operations."""

    @staticmethod
    def benchmark_operations(
        uf: UnionFind[T], operations: List[Tuple[str, Any]]
    ) -> Dict[str, Any]:
        """
        Benchmark Union-Find operations.

        Args:
            uf: Union-Find instance
            operations: List of (operation_type, args) tuples
                      operation_type: "union", "find", "connected"

        Returns:
            Benchmark results
        """
        results = {
            "total_operations": len(operations),
            "union_count": 0,
            "find_count": 0,
            "connected_count": 0,
            "time_taken": 0.0,
            "actual_merges": 0,
        }

        start_time = time.time()

        for op_type, args in operations:
            if op_type == "union":
                merged = uf.union(args[0], args[1])
                results["union_count"] += 1
                if merged:
                    results["actual_merges"] += 1
            elif op_type == "find":
                uf.find(args[0])
                results["find_count"] += 1
            elif op_type == "connected":
                uf.connected(args[0], args[1])
                results["connected_count"] += 1

        results["time_taken"] = time.time() - start_time
        results["avg_time_per_op"] = results["time_taken"] / len(operations)

        return results

    @staticmethod
    def analyze_structure(uf: UnionFind[T]) -> Dict[str, Any]:
        """
        Analyze the internal structure of Union-Find.

        Args:
            uf: Union-Find instance

        Returns:
            Structural analysis
        """
        analysis = {
            "total_elements": len(uf),
            "total_sets": uf.get_set_count(),
            "max_set_size": 0,
            "min_set_size": float("inf"),
            "avg_set_size": 0,
            "tree_heights": {},
            "max_tree_height": 0,
        }

        sets = uf.get_all_sets()
        total_elements = 0

        for root, elements in sets.items():
            set_size = len(elements)
            analysis["max_set_size"] = max(analysis["max_set_size"], set_size)
            analysis["min_set_size"] = min(analysis["min_set_size"], set_size)
            total_elements += set_size

            # Calculate tree height for this set
            height = UnionFindAnalysis._calculate_tree_height(uf, root)
            analysis["tree_heights"][root] = height
            analysis["max_tree_height"] = max(analysis["max_tree_height"], height)

        if sets:
            analysis["avg_set_size"] = total_elements / len(sets)
        else:
            analysis["min_set_size"] = 0

        return analysis

    @staticmethod
    def _calculate_tree_height(uf: UnionFind[T], root: T) -> int:
        """Calculate height of tree rooted at given element."""
        # This is an approximation since path compression flattens trees
        # In practice, trees are very flat due to path compression
        visited = set()
        max_depth = 0

        def dfs_depth(current: T, depth: int) -> int:
            nonlocal max_depth
            if current in visited:
                return depth
            visited.add(current)
            max_depth = max(max_depth, depth)

            # Find children (elements that have this as parent)
            children = [
                elem
                for elem, parent in uf.parent.items()
                if uf.find(parent) == current and elem != current
            ]
            if children:
                for child in children:
                    dfs_depth(child, depth + 1)

            return depth

        dfs_depth(root, 0)
        return max_depth

    @staticmethod
    def generate_random_operations(
        elements: List[T], num_operations: int
    ) -> List[Tuple[str, Any]]:
        """
        Generate random Union-Find operations for testing.

        Args:
            elements: List of elements
            num_operations: Number of operations to generate

        Returns:
            List of (operation_type, args) tuples
        """
        operations = []

        for _ in range(num_operations):
            op_type = random.choice(["union", "find", "connected"])
            elem1 = random.choice(elements)
            elem2 = random.choice(elements)

            if op_type == "union":
                operations.append(("union", (elem1, elem2)))
            elif op_type == "find":
                operations.append(("find", (elem1,)))
            else:  # connected
                operations.append(("connected", (elem1, elem2)))

        return operations

    @staticmethod
    def test_correctness(elements: List[T], operations: List[Tuple[str, Any]]) -> bool:
        """
        Test correctness of Union-Find operations.

        Args:
            elements: List of elements
            operations: List of operations to perform

        Returns:
            True if all operations behave correctly
        """
        uf = UnionFind(elements)

        for op_type, args in operations:
            try:
                if op_type == "union":
                    uf.union(args[0], args[1])
                elif op_type == "find":
                    uf.find(args[0])
                elif op_type == "connected":
                    uf.connected(args[0], args[1])
                else:
                    return False  # Unknown operation
            except Exception:
                return False

        return True


class KruskalWithUnionFind:
    """Kruskal's MST algorithm using Union-Find for cycle detection."""

    @staticmethod
    def kruskal_mst(
        vertices: List[T], edges: List[Tuple[T, T, float]]
    ) -> List[Tuple[T, T, float]]:
        """
        Kruskal's Minimum Spanning Tree using Union-Find.

        Args:
            vertices: List of vertices
            edges: List of (u, v, weight) tuples

        Returns:
            List of edges in MST
        """
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Initialize Union-Find
        uf = UnionFind(vertices)
        mst = []

        for u, v, weight in edges:
            # Check if adding this edge would create a cycle
            if not uf.connected(u, v):
                uf.union(u, v)
                mst.append((u, v, weight))

        return mst

    @staticmethod
    def kruskal_with_analysis(
        vertices: List[T], edges: List[Tuple[T, T, float]]
    ) -> Dict[str, Any]:
        """
        Kruskal's algorithm with detailed analysis.

        Args:
            vertices: List of vertices
            edges: List of (u, v, weight) tuples

        Returns:
            Analysis results including MST and performance metrics
        """
        start_time = time.time()

        # Sort edges
        sort_start = time.time()
        edges_sorted = sorted(edges, key=lambda x: x[2])
        sort_time = time.time() - sort_start

        # Run Kruskal's
        uf = UnionFind(vertices)
        mst = []
        union_operations = 0
        find_operations = 0

        kruskal_start = time.time()
        for u, v, weight in edges_sorted:
            find_operations += 2  # Two find operations
            if not uf.connected(u, v):
                union_operations += 1
                uf.union(u, v)
                mst.append((u, v, weight))
        kruskal_time = time.time() - kruskal_start

        total_time = time.time() - start_time

        return {
            "mst": mst,
            "total_weight": sum(weight for _, _, weight in mst),
            "edges_in_mst": len(mst),
            "total_edges_considered": len(edges),
            "sort_time": sort_time,
            "kruskal_time": kruskal_time,
            "total_time": total_time,
            "union_operations": union_operations,
            "find_operations": find_operations,
            "final_sets": uf.get_set_count(),
        }


class ConnectivityChecker:
    """Applications of Union-Find for connectivity problems."""

    @staticmethod
    def connected_components(
        vertices: List[T], edges: List[Tuple[T, T]]
    ) -> List[List[T]]:
        """
        Find connected components using Union-Find.

        Args:
            vertices: List of vertices
            edges: List of (u, v) edge tuples

        Returns:
            List of connected components
        """
        uf = UnionFind(vertices)

        # Union all connected vertices
        for u, v in edges:
            uf.union(u, v)

        # Group elements by their root
        components = {}
        for vertex in vertices:
            root = uf.find(vertex)
            if root not in components:
                components[root] = []
            components[root].append(vertex)

        return list(components.values())

    @staticmethod
    def has_cycle(vertices: List[T], edges: List[Tuple[T, T]]) -> bool:
        """
        Check if undirected graph has cycles using Union-Find.

        Args:
            vertices: List of vertices
            edges: List of (u, v) edge tuples

        Returns:
            True if cycle exists
        """
        uf = UnionFind(vertices)

        for u, v in edges:
            if uf.connected(u, v):
                return True  # Cycle detected
            uf.union(u, v)

        return False

    @staticmethod
    def minimum_spanning_forest(
        vertices: List[T], edges: List[Tuple[T, T, float]]
    ) -> List[Tuple[T, T, float]]:
        """
        Find minimum spanning forest (MST for disconnected graphs).

        Args:
            vertices: List of vertices
            edges: List of (u, v, weight) tuples

        Returns:
            List of edges in minimum spanning forest
        """
        return KruskalWithUnionFind.kruskal_mst(vertices, edges)
