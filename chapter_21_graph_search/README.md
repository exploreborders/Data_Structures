# Chapter 21: Advanced Graph Search and Traversal

This chapter extends graph theory into advanced algorithms for graph analysis, connectivity, optimization, and network flow. These algorithms solve complex problems in routing, scheduling, network design, and optimization that are essential for modern computing systems.

## Advanced Traversal Techniques

### Bidirectional Search
**Problem**: Find shortest path in unweighted graphs more efficiently.

**Strategy**: Search simultaneously from start and end vertices.

```python
def bidirectional_search(graph, start, end):
    # Forward search from start
    # Backward search from end
    # Meet in the middle for efficiency
```

**Advantages**:
- Often faster than unidirectional BFS
- Reduces search space significantly
- Natural for pathfinding problems

### DFS with Timestamps
**Problem**: Analyze graph structure and properties.

**Strategy**: Track discovery and finishing times during DFS.

```python
def dfs_timestamps(graph, start):
    discovery_time = {}
    finishing_time = {}
    # Use timestamps for classification
```

**Applications**:
- Topological sorting
- Strongly connected components
- Bridge/articulation point detection

## Topological Sorting

### Kahn's Algorithm (BFS-based)
**Problem**: Order vertices in DAG so all edges point forward.

**Strategy**: Process vertices with no incoming edges first.

```python
def kahn_topological_sort(graph):
    in_degree = compute_in_degrees(graph)
    queue = [v for v in graph.vertices if in_degree[v] == 0]

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
```

**Time**: O(V + E)
**Space**: O(V + E)

### DFS-based Topological Sort
**Problem**: Alternative topological sorting approach.

**Strategy**: Post-order DFS gives reverse topological order.

```python
def dfs_topological_sort(graph):
    visited = set()
    result = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(vertex)  # Add after all dependencies

    for vertex in graph.vertices:
        if vertex not in visited:
            dfs(vertex)

    result.reverse()  # Reverse for topological order
```

## Strongly Connected Components

### Kosaraju's Algorithm
**Problem**: Find maximal strongly connected subgraphs.

**Strategy**: Two DFS passes with graph transposition.

```python
def kosaraju_scc(graph):
    # Phase 1: DFS on original graph for finishing times
    finishing_order = dfs_finishing_times(graph)

    # Phase 2: DFS on transposed graph in reverse finishing order
    transpose = build_transpose_graph(graph)
    sccs = dfs_transpose(transpose, finishing_order)

    return sccs
```

**Time**: O(V + E)
**Space**: O(V + E)

### Tarjan's Algorithm
**Problem**: Single-pass SCC finding.

**Strategy**: DFS with stack and low-link values.

**Advantages**: Single DFS pass, more complex but elegant.

## Minimum Spanning Trees

### Prim's Algorithm
**Problem**: Find MST starting from arbitrary vertex.

**Strategy**: Grow tree by adding closest vertex.

```python
def prim_mst(graph, start):
    visited = set([start])
    min_heap = []  # (weight, vertex, parent)

    # Add edges from start vertex
    for neighbor, weight in graph.get_neighbors(start):
        heapq.heappush(min_heap, (weight, neighbor, start))

    mst = []
    while min_heap and len(visited) < len(graph.vertices):
        weight, vertex, parent = heapq.heappop(min_heap)

        if vertex in visited:
            continue

        visited.add(vertex)
        mst.append((parent, vertex, weight))

        # Add new edges
        for neighbor, edge_weight in graph.get_neighbors(vertex):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, vertex))
```

**Time**: O((V + E) log V) with binary heap

### Kruskal's Algorithm
**Problem**: Find MST by sorting all edges.

**Strategy**: Add edges in increasing weight order (no cycles).

```python
def kruskal_mst(graph):
    edges = sorted_edges_by_weight(graph)
    mst = []
    union_find = UnionFind(graph.vertices)

    for weight, u, v in edges:
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            mst.append((u, v, weight))

    return mst
```

**Time**: O(E log E) due to sorting

## Graph Connectivity Analysis

### Articulation Points (Cut Vertices)
**Problem**: Find vertices whose removal increases connected components.

**Strategy**: DFS with discovery/finishing times and parent tracking.

```python
def find_articulation_points(graph):
    articulation_points = set()
    visited = set()
    discovery_time = {}
    low_time = {}
    parent = {}
    time = 0

    def dfs_ap(vertex):
        nonlocal time
        children = 0
        visited.add(vertex)
        time += 1
        discovery_time[vertex] = time
        low_time[vertex] = time

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                parent[neighbor] = vertex
                children += 1
                dfs_ap(neighbor)

                # Update low time
                low_time[vertex] = min(low_time[vertex], low_time[neighbor])

                # Articulation point conditions
                if parent[vertex] is None and children > 1:
                    articulation_points.add(vertex)
                if parent[vertex] is not None and low_time[neighbor] >= discovery_time[vertex]:
                    articulation_points.add(vertex)
```

### Bridges (Cut Edges)
**Problem**: Find edges whose removal increases connected components.

**Strategy**: Similar to articulation points but for edges.

```python
def find_bridges(graph):
    bridges = []
    visited = set()
    discovery_time = {}
    low_time = {}
    parent = {}
    time = 0

    def dfs_bridge(vertex):
        nonlocal time
        visited.add(vertex)
        time += 1
        discovery_time[vertex] = time
        low_time[vertex] = time

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                parent[neighbor] = vertex
                dfs_bridge(neighbor)

                low_time[vertex] = min(low_time[vertex], low_time[neighbor])

                # Bridge condition
                if low_time[neighbor] > discovery_time[vertex]:
                    bridges.append((vertex, neighbor))
```

## Eulerian Paths and Circuits

### Eulerian Circuit
**Problem**: Find path that traverses each edge exactly once and returns to start.

**Conditions (Undirected)**:
- All vertices have even degree
- Graph is connected (except isolated vertices)

**Conditions (Directed)**:
- All vertices have equal in-degree and out-degree
- Underlying graph is strongly connected

### Eulerian Path
**Problem**: Find path that traverses each edge exactly once.

**Conditions (Undirected)**:
- Exactly 0 or 2 vertices with odd degree
- Graph is connected (ignoring isolated vertices)

**Conditions (Directed)**:
- At most one vertex with out-degree = in-degree + 1 (start)
- At most one vertex with in-degree = out-degree + 1 (end)
- All others have equal in-degree and out-degree

## Maximum Flow Algorithms

### Ford-Fulkerson Method
**Problem**: Find maximum flow in flow network.

**Strategy**: Find augmenting paths until no more exist.

```python
def ford_fulkerson(graph, source, sink):
    residual = build_residual_graph(graph)
    max_flow = 0

    while True:
        # Find augmenting path (BFS in residual graph)
        path = bfs_residual(residual, source, sink)
        if not path:
            break

        # Find bottleneck capacity
        path_flow = min(residual.get_edge_weight(u, v) for u, v in path_edges)

        # Update residual capacities
        for u, v in path_edges:
            # Forward edge
            residual.adj_list[u] = [(n, w - path_flow if n == v else w)
                                  for n, w in residual.adj_list[u]]
            # Backward edge
            residual.adj_list[v] = [(n, w + path_flow if n == u else w)
                                  for n, w in residual.adj_list[v]]

        max_flow += path_flow

    return max_flow
```

### Edmonds-Karp Algorithm
**Problem**: Ford-Fulkerson with BFS for augmenting paths.

**Strategy**: Use BFS instead of DFS for better performance guarantees.

**Time**: O(VE²)
**Advantages**: Polynomial time bound, practical performance

## Algorithm Complexity Summary

| Algorithm | Time Complexity | Space Complexity | Key Insight |
|-----------|----------------|------------------|-------------|
| Bidirectional Search | O(b^{d/2}) | O(b^{d/2}) | Meet in middle |
| Topological Sort | O(V + E) | O(V + E) | Dependency ordering |
| Kosaraju SCC | O(V + E) | O(V + E) | Two DFS passes |
| Prim's MST | O((V+E) log V) | O(V) | Priority queue |
| Kruskal's MST | O(E log E) | O(V) | Union-Find |
| Articulation Points | O(V + E) | O(V) | DFS timestamps |
| Eulerian Path | O(V + E) | O(V + E) | Degree conditions |
| Ford-Fulkerson | O(max_flow × E) | O(V + E) | Augmenting paths |

## Applications

### Topological Sort
- **Task scheduling**: Build systems, project management
- **Course prerequisites**: Academic planning
- **Deadlock prevention**: Resource allocation
- **Makefile dependencies**: Build automation

### Strongly Connected Components
- **Web page ranking**: Link analysis
- **Circuit design**: Component grouping
- **Social network analysis**: Community detection
- **Compiler optimization**: Call graph analysis

### Minimum Spanning Trees
- **Network design**: Cable TV, telephone networks
- **Clustering**: Hierarchical clustering
- **Approximation algorithms**: Traveling salesman
- **Image segmentation**: Computer vision

### Articulation Points & Bridges
- **Network reliability**: Critical node identification
- **Vulnerability analysis**: Infrastructure protection
- **Graph decomposition**: Biconnected components

### Eulerian Paths
- **DNA sequencing**: Genome assembly
- **Route optimization**: Mail delivery, garbage collection
- **Graphics**: Polygon triangulation
- **Game design**: Maze generation

### Maximum Flow
- **Network routing**: Traffic optimization
- **Matching problems**: Bipartite matching
- **Image segmentation**: Min-cut/max-flow
- **Resource allocation**: Transportation problems

## Implementation Considerations

### Graph Representations
- **Adjacency List**: Best for sparse graphs, traversal algorithms
- **Adjacency Matrix**: Better for dense graphs, matrix operations
- **Edge List**: Simple for Kruskal's algorithm

### Union-Find for Kruskal's
```python
class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
```

### Residual Graphs for Flow
- **Forward edges**: Remaining capacity
- **Backward edges**: Flow that can be reduced
- **Augmenting paths**: Found via BFS (Edmonds-Karp)

## Advanced Topics

### Biconnected Components
- **Problem**: Maximal biconnected subgraphs
- **Algorithm**: DFS with stack for edge tracking
- **Applications**: Network reliability analysis

### Network Flow Extensions
- **Min-cost max-flow**: Minimum cost for maximum flow
- **Multi-commodity flow**: Multiple flow types
- **Stochastic flows**: Probabilistic capacities

### Dynamic Graph Algorithms
- **Dynamic MST**: Handle edge insertions/deletions
- **Dynamic connectivity**: Maintain connectivity under updates
- **Fully dynamic graphs**: All operations supported

## Real-World Performance

### Algorithm Selection Guide

| Scenario | Recommended Algorithm | Why |
|----------|----------------------|-----|
| Sparse graph traversal | DFS/BFS | Natural graph structure |
| Dependency ordering | Topological Sort | DAG requirement |
| Web graph analysis | SCC (Kosaraju) | Large directed graphs |
| Network design | MST (Prim's) | Dense graphs |
| Critical infrastructure | Articulation Points | Vulnerability analysis |
| Route optimization | Eulerian Path | Complete coverage |
| Resource allocation | Maximum Flow | Capacity constraints |

### Practical Considerations

- **Graph size**: Affects algorithm choice significantly
- **Density**: Sparse vs dense graph characteristics
- **Updates**: Static vs dynamic graph requirements
- **Memory constraints**: Space-efficient implementations
- **Parallelization**: Which algorithms can be parallelized

## The Advanced Graph Landscape

These advanced algorithms transform graph theory from abstract mathematics into practical tools for solving complex real-world problems. They bridge the gap between theoretical computer science and engineering applications.

Mastering these algorithms means understanding how to:
- **Model complex relationships** as graphs
- **Choose appropriate algorithms** for specific problems
- **Analyze connectivity and flow** in networks
- **Optimize paths and structures** efficiently

The algorithms in this chapter represent the pinnacle of graph theory applications, enabling solutions to problems that would be intractable without these mathematical tools.