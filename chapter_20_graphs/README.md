# Chapter 20: Graphs

This chapter explores **graph theory and algorithms**, one of the most important and versatile areas of computer science. Graphs model relationships and connections between entities, making them essential for representing networks, dependencies, and complex relationships in the real world.

## What is a Graph?

A **graph** G = (V, E) consists of:
- **Vertices** (nodes): Entities being modeled
- **Edges** (links): Relationships between entities

### Graph Terminology

| Concept | Definition | Example |
|---------|------------|---------|
| **Vertex** | Fundamental unit | Person in social network |
| **Edge** | Connection between vertices | Friendship between people |
| **Directed** | Edges have direction | One-way streets |
| **Undirected** | Edges are bidirectional | Mutual friendships |
| **Weighted** | Edges have associated costs | Road distances |
| **Degree** | Number of edges incident to vertex | Number of friends |

### Graph Representations

#### 1. Adjacency List (Most Common)
- **Space**: O(V + E)
- **Pros**: Space-efficient, fast iteration over neighbors
- **Cons**: Slow edge existence checks
- **Best for**: Sparse graphs, traversal algorithms

```python
# Example: adjacency list
graph = {
    "A": [("B", 1.0), ("C", 2.0)],
    "B": [("A", 1.0), ("D", 3.0)],
    "C": [("A", 2.0)],
    "D": [("B", 3.0)]
}
```

#### 2. Adjacency Matrix
- **Space**: O(V²)
- **Pros**: Fast edge existence checks, matrix operations
- **Cons**: Space-intensive for sparse graphs
- **Best for**: Dense graphs, matrix algorithms

```python
# Example: adjacency matrix (4x4)
matrix = [
    [0, 1, 1, 0],  # A -> B, A -> C
    [1, 0, 0, 1],  # B -> A, B -> D
    [1, 0, 0, 0],  # C -> A
    [0, 1, 0, 0]   # D -> B
]
```

## Graph Traversal Algorithms

### Depth-First Search (DFS)
- **Strategy**: Explore deep before wide
- **Implementation**: Stack (recursive or iterative)
- **Time**: O(V + E)
- **Space**: O(V)
- **Applications**: Topological sort, cycle detection, path finding

### Breadth-First Search (BFS)
- **Strategy**: Explore level by level
- **Implementation**: Queue
- **Time**: O(V + E)
- **Space**: O(V)
- **Applications**: Shortest paths (unweighted), level-order traversal

## Shortest Path Algorithms

### Dijkstra's Algorithm
- **Problem**: Single-source shortest paths
- **Constraint**: Non-negative edge weights
- **Strategy**: Greedy, priority queue
- **Time**: O((V + E) log V) with binary heap
- **Applications**: Routing, network optimization

### Bellman-Ford Algorithm
- **Problem**: Single-source shortest paths
- **Constraint**: Handles negative weights
- **Strategy**: Dynamic programming, relaxation
- **Time**: O(V × E)
- **Applications**: Networks with negative costs

### Floyd-Warshall Algorithm
- **Problem**: All-pairs shortest paths
- **Constraint**: Dense graphs
- **Strategy**: Dynamic programming
- **Time**: O(V³)
- **Applications**: Small complete graphs, transitive closure

## Graph Analysis Algorithms

### Connected Components
- **Undirected graphs**: Find connected subgraphs
- **Algorithm**: DFS/BFS from each unvisited vertex
- **Time**: O(V + E)

### Cycle Detection
- **Undirected**: Look for back edges in DFS
- **Directed**: Topological sort or DFS with colors
- **Applications**: Deadlock detection, dependency analysis

### Topological Sort
- **Requirement**: Directed Acyclic Graph (DAG)
- **Algorithm**: Kahn's algorithm or DFS
- **Time**: O(V + E)
- **Applications**: Task scheduling, dependency resolution

### Minimum Spanning Tree (MST)
- **Problem**: Connect all vertices with minimum total edge weight
- **Algorithms**: Kruskal's (edge-based), Prim's (vertex-based)
- **Time**: O(E log E) for Kruskal's
- **Applications**: Network design, clustering

## Special Graph Types

### Trees
- **Properties**: Connected, acyclic, |E| = |V| - 1
- **Special cases**: Binary trees, balanced trees
- **Applications**: Hierarchies, decision trees

### Directed Acyclic Graphs (DAGs)
- **Properties**: No cycles, topological order exists
- **Applications**: Dependencies, scheduling, compilation

### Bipartite Graphs
- **Properties**: Two-colorable, no odd cycles
- **Applications**: Matching problems, resource allocation

### Complete Graphs
- **Properties**: Every pair of vertices connected
- **Notation**: K_n (n vertices)
- **Applications**: Theoretical analysis

## Graph Applications

### 1. **Computer Networks**
- **Routing**: Shortest paths between nodes
- **Topology**: Network structure analysis
- **Reliability**: Connected components after failures

### 2. **Social Networks**
- **Communities**: Connected components
- **Influence**: Centrality measures
- **Recommendations**: Path finding

### 3. **Transportation**
- **GPS**: Shortest paths with weights
- **Traffic**: Flow networks
- **Logistics**: Route optimization

### 4. **Software Engineering**
- **Dependencies**: Topological sort
- **Call graphs**: Cycle detection
- **Version control**: Merge analysis

### 5. **Biology**
- **Protein interactions**: Network analysis
- **Genealogy**: Tree structures
- **Epidemiology**: Disease spread modeling

## Implementation Considerations

### Choosing Representations
```python
# Sparse graph (E << V²) → Adjacency List
sparse_graph = Graph()  # Uses adjacency list

# Dense graph (E ≈ V²) → Adjacency Matrix
# (Our implementation uses adjacency list for simplicity)
```

### Algorithm Selection Guide

| Problem | Algorithm | Time | Constraints |
|---------|-----------|------|-------------|
| Single-pair shortest path | BFS/Dijkstra | O(V+E) | Non-negative weights |
| All-pairs shortest paths | Floyd-Warshall | O(V³) | Small graphs |
| Negative weights | Bellman-Ford | O(VE) | No negative cycles |
| MST | Kruskal/Prim | O(E log E) | Connected graph |
| Cycle detection | DFS | O(V+E) | - |
| Topological sort | Kahn's/DFS | O(V+E) | DAG |

## Common Graph Problems

### Path Finding
```python
# All paths between two nodes
paths = GraphTraversal.dfs_paths(graph, start, end)

# Shortest path (unweighted)
path = GraphTraversal.bfs_shortest_path(graph, start, end)

# Shortest path (weighted)
distances, predecessors = ShortestPaths.dijkstra(graph, start)
path = ShortestPaths.reconstruct_path(predecessors, start, end)
```

### Graph Structure Analysis
```python
# Find connected components
components = GraphAnalysis.connected_components(graph)

# Check for cycles
has_cycle = GraphAnalysis.has_cycle(graph)

# Topological ordering
order = GraphAnalysis.topological_sort(dag)
```

## Performance Characteristics

### Time Complexity Summary

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| DFS/BFS | O(V + E) | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |
| Bellman-Ford | O(V × E) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal's MST | O(E log E) | O(V) |
| Connected Components | O(V + E) | O(V) |

### Space Complexity Trade-offs

- **Adjacency List**: O(V + E) - Better for sparse graphs
- **Adjacency Matrix**: O(V²) - Better for dense graphs
- **Edge List**: O(E) - Simple but slow queries

## Graph Theory Concepts

### Graph Invariants
- **Order**: Number of vertices |V|
- **Size**: Number of edges |E|
- **Degree sequence**: Sorted list of vertex degrees

### Graph Metrics
- **Diameter**: Longest shortest path
- **Radius**: Minimum eccentricity
- **Center**: Vertices with minimum eccentricity

### Special Properties
- **Planar**: Can be drawn without edge crossings
- **Eulerian**: Contains Eulerian circuit
- **Hamiltonian**: Contains Hamiltonian path

## Advanced Topics

### Flow Networks
- **Maximum flow**: Ford-Fulkerson, Edmonds-Karp
- **Min-cut max-flow**: Theoretical foundation
- **Applications**: Network reliability, matching

### Graph Coloring
- **Vertex coloring**: NP-complete in general
- **Edge coloring**: Matching problems
- **Applications**: Scheduling, register allocation

### Random Graphs
- **Erdős–Rényi model**: Random edges
- **Properties**: Phase transitions, thresholds
- **Applications**: Network modeling, algorithm analysis

## Real-World Implementations

### Python's networkx
```python
import networkx as nx

G = nx.Graph()
G.add_edge("A", "B", weight=1.0)
nx.shortest_path(G, "A", "B")
```

### JavaScript's graph libraries
```javascript
// Using a graph library
const graph = new Graph();
graph.addEdge("A", "B", 1.0);
graph.dijkstra("A");
```

### Database Graph Processing
- **Neo4j**: Native graph database
- **GraphQL**: Query language for graphs
- **Apache TinkerPop**: Graph computing framework

## The Graph Mindset

Graphs teach us to see the world as **relationships and connections** rather than isolated entities. Every system becomes a network of interacting components, where the structure determines the behavior.

Understanding graphs means recognizing that **connections matter as much as the things they connect**. It's a fundamental shift in how we model and solve problems.

This chapter provides the foundation for understanding complex systems, from social networks to distributed computing, from transportation systems to biological processes. Graphs are everywhere—once you learn to see them.