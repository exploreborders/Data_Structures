"""
Chapter 20 Examples: Graphs - Graph Algorithm Demonstrations

Interactive demonstrations of graph representations, traversals, shortest paths, and analysis.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from graph_implementations import Graph, GraphTraversal, ShortestPaths, GraphAnalysis


def demonstrate_graph_construction():
    """Demonstrate different ways to construct graphs."""
    print("=== Graph Construction Examples ===\n")

    # 1. Undirected unweighted graph
    print("1. Undirected Unweighted Graph:")
    undirected = Graph(directed=False, weighted=False)
    undirected.add_edge("A", "B")
    undirected.add_edge("A", "C")
    undirected.add_edge("B", "D")
    print(undirected)
    print()

    # 2. Directed weighted graph
    print("2. Directed Weighted Graph:")
    directed = Graph(directed=True, weighted=True)
    directed.add_edge("A", "B", 5.0)
    directed.add_edge("A", "C", 3.0)
    directed.add_edge("B", "D", 2.0)
    directed.add_edge("C", "D", 4.0)
    print(directed)
    print()

    # 3. Complete graph (K_4)
    print("3. Complete Graph K_4:")
    complete = Graph()
    vertices = ["A", "B", "C", "D"]
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            complete.add_edge(vertices[i], vertices[j])
    print(complete)
    print()


def demonstrate_graph_traversals():
    """Demonstrate DFS and BFS traversals."""
    print("\n=== Graph Traversal Algorithms ===\n")

    # Create a sample graph
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "G")
    graph.add_edge("E", "G")
    graph.add_edge("F", "G")

    print("Sample Graph:")
    print(graph)
    print()

    # DFS
    print("Depth-First Search (DFS) from A:")
    dfs_result = GraphTraversal.dfs(graph, "A")
    print(f"  Order: {' -> '.join(dfs_result)}")
    print("  DFS explores deeply before backtracking")
    # BFS
    print("\nBreadth-First Search (BFS) from A:")
    bfs_result = GraphTraversal.bfs(graph, "A")
    print(f"  Order: {' -> '.join(bfs_result)}")
    print("  BFS explores level by level")
    # Path finding
    print("\nFinding all paths from A to G:")
    paths = GraphTraversal.dfs_paths(graph, "A", "G")
    for i, path in enumerate(paths, 1):
        print(f"  Path {i}: {' -> '.join(path)}")

    print(f"\nShortest path from A to G (BFS):")
    shortest_path = GraphTraversal.bfs_shortest_path(graph, "A", "G")
    if shortest_path:
        print(
            f"  Path: {' -> '.join(shortest_path)} (length: {len(shortest_path) - 1})"
        )
    print()


def demonstrate_shortest_paths():
    """Demonstrate shortest path algorithms."""
    print("\n=== Shortest Path Algorithms ===\n")

    # Create weighted graph
    graph = Graph(directed=True, weighted=True)
    graph.add_edge("A", "B", 4.0)
    graph.add_edge("A", "C", 2.0)
    graph.add_edge("C", "B", 1.0)
    graph.add_edge("B", "D", 3.0)
    graph.add_edge("C", "D", 5.0)
    graph.add_edge("D", "E", 2.0)

    print("Weighted Graph:")
    print(graph)
    print()

    # Dijkstra
    print("Dijkstra's Algorithm from A:")
    distances, predecessors = ShortestPaths.dijkstra(graph, "A")

    for vertex in sorted(graph.vertices):
        if distances[vertex] == float("inf"):
            print(f"  {vertex}: unreachable")
        else:
            path = ShortestPaths.reconstruct_path(predecessors, "A", vertex)
            path_str = " -> ".join(path) if path else "no path"
            print(".1f")

    print()

    # Bellman-Ford (with negative weights)
    print("Bellman-Ford Algorithm (handles negative weights):")
    neg_graph = Graph(directed=True, weighted=True)
    neg_graph.add_edge("A", "B", 4.0)
    neg_graph.add_edge("A", "C", 2.0)
    neg_graph.add_edge("C", "B", -3.0)  # Negative weight!
    neg_graph.add_edge("B", "D", 3.0)

    distances, predecessors = ShortestPaths.bellman_ford(neg_graph, "A")

    if distances:
        for vertex in sorted(neg_graph.vertices):
            path = ShortestPaths.reconstruct_path(predecessors, "A", vertex)
            path_str = " -> ".join(path) if path else "no path"
            print(".1f")
    else:
        print("  Negative cycle detected!")
    print()


def demonstrate_graph_analysis():
    """Demonstrate graph analysis algorithms."""
    print("\n=== Graph Analysis Algorithms ===\n")

    # Connected components
    print("1. Connected Components:")
    graph1 = Graph()
    # Component 1
    graph1.add_edge("A", "B")
    graph1.add_edge("B", "C")
    # Component 2
    graph1.add_edge("D", "E")
    # Component 3
    graph1.add_vertex("F")

    components = GraphAnalysis.connected_components(graph1)
    print(f"  Graph has {len(components)} connected components:")
    for i, comp in enumerate(components, 1):
        print(f"    Component {i}: {comp}")
    print()

    # Cycle detection
    print("2. Cycle Detection:")
    cyclic_graph = Graph()
    cyclic_graph.add_edge("A", "B")
    cyclic_graph.add_edge("B", "C")
    cyclic_graph.add_edge("C", "A")

    acyclic_graph = Graph()
    acyclic_graph.add_edge("A", "B")
    acyclic_graph.add_edge("A", "C")
    acyclic_graph.add_edge("B", "D")

    print(f"  Cyclic graph has cycle: {GraphAnalysis.has_cycle(cyclic_graph)}")
    print(f"  Acyclic graph has cycle: {GraphAnalysis.has_cycle(acyclic_graph)}")
    print()

    # Topological sort
    print("3. Topological Sort (DAG required):")
    dag = Graph(directed=True)
    dag.add_edge("A", "B")
    dag.add_edge("A", "C")
    dag.add_edge("B", "D")
    dag.add_edge("C", "D")
    dag.add_edge("D", "E")

    topo_order = GraphAnalysis.topological_sort(dag)
    if topo_order:
        print(f"  Topological order: {' -> '.join(topo_order)}")
        print("  This is a valid DAG")
    else:
        print("  Graph contains a cycle!")

    # Try with cyclic graph
    dag.add_edge("E", "A")  # Create cycle
    topo_order = GraphAnalysis.topological_sort(dag)
    if not topo_order:
        print("  After adding E->A: Cycle detected!")
    print()

    # Minimum Spanning Tree
    print("4. Minimum Spanning Tree (Kruskal's algorithm):")
    mst_graph = Graph(weighted=True)
    mst_graph.add_edge("A", "B", 4.0)
    mst_graph.add_edge("A", "C", 2.0)
    mst_graph.add_edge("B", "C", 1.0)
    mst_graph.add_edge("B", "D", 3.0)
    mst_graph.add_edge("C", "D", 5.0)

    mst = GraphAnalysis.minimum_spanning_tree(mst_graph)
    print("  Edges in MST:")
    total_weight = 0
    for u, v, weight in mst:
        print(f"    {u} -- {v} (weight: {weight})")
        total_weight += weight
    print(f"  Total weight: {total_weight}")
    print()


def demonstrate_real_world_applications():
    """Demonstrate real-world graph applications."""
    print("\n=== Real-World Graph Applications ===\n")

    # Social network analysis
    print("1. Social Network (Friendship Graph):")
    social = Graph()

    # Add people
    people = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    for person in people:
        social.add_vertex(person)

    # Add friendships
    friendships = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Charlie"),
        ("Bob", "Diana"),
        ("Charlie", "Diana"),
        ("Diana", "Eve"),
    ]

    for u, v in friendships:
        social.add_edge(u, v)

    print(
        f"  Network: {len(social)} people, {sum(len(social.get_neighbors(p)) for p in social.vertices) // 2} friendships"
    )

    # Find connected components (social circles)
    circles = GraphAnalysis.connected_components(social)
    print(f"  Social circles: {len(circles)}")
    for i, circle in enumerate(circles, 1):
        print(f"    Circle {i}: {circle}")

    # Find shortest path (degrees of separation)
    path = GraphTraversal.bfs_shortest_path(social, "Alice", "Eve")
    if path:
        print(
            f"  Connection Alice -> Eve: {' -> '.join(path)} ({len(path) - 1} degrees)"
        )
    print()

    # Transportation network
    print("2. Transportation Network:")
    transport = Graph(directed=True, weighted=True)

    cities = ["NYC", "Boston", "Philly", "DC", "Baltimore"]
    for city in cities:
        transport.add_vertex(city)

    # Add routes with distances
    routes = [
        ("NYC", "Boston", 215),
        ("NYC", "Philly", 95),
        ("Philly", "DC", 140),
        ("DC", "Baltimore", 40),
        ("Philly", "Baltimore", 100),
        ("Boston", "Philly", 300),
    ]

    for u, v, dist in routes:
        transport.add_edge(u, v, dist)

    print("  Finding shortest routes from NYC:")

    distances, predecessors = ShortestPaths.dijkstra(transport, "NYC")

    for city in ["Boston", "Philly", "DC", "Baltimore"]:
        if distances[city] != float("inf"):
            path = ShortestPaths.reconstruct_path(predecessors, "NYC", city)
            print(
                f"    NYC -> {city}: {' -> '.join(path)} ({int(distances[city])} miles)"
            )
        else:
            print(f"    NYC -> {city}: no route")
    print()

    # Task dependency graph
    print("3. Task Dependency (Project Management):")
    tasks = Graph(directed=True)

    task_list = ["Plan", "Design", "Code", "Test", "Deploy"]
    for task in task_list:
        tasks.add_vertex(task)

    # Add dependencies
    dependencies = [
        ("Plan", "Design"),
        ("Plan", "Code"),
        ("Design", "Code"),
        ("Code", "Test"),
        ("Test", "Deploy"),
    ]

    for before, after in dependencies:
        tasks.add_edge(before, after)

    # Topological sort gives valid execution order
    execution_order = GraphAnalysis.topological_sort(tasks)
    if execution_order:
        print("  Valid execution order: " + " -> ".join(execution_order))
    else:
        print("  Circular dependency detected!")

    print()


def demonstrate_algorithm_performance():
    """Compare algorithm performance on different graph types."""
    print("\n=== Algorithm Performance Comparison ===\n")

    # Create different graph types
    graphs = {
        "Small Graph": create_small_graph(),
        "Sparse Graph": create_sparse_graph(50, 80),
        "Dense Graph": create_dense_graph(20),
    }

    for name, graph in graphs.items():
        print(f"{name} ({len(graph)} vertices):")

        # Test traversals
        start_time = time.time()
        dfs_result = GraphTraversal.dfs(graph, list(graph.vertices)[0])
        dfs_time = time.time() - start_time

        start_time = time.time()
        bfs_result = GraphTraversal.bfs(graph, list(graph.vertices)[0])
        bfs_time = time.time() - start_time

        print(".4f")
        print(".4f")

        # Test shortest paths if weighted
        if graph.weighted and len(graph.vertices) <= 10:
            start_time = time.time()
            distances, _ = ShortestPaths.dijkstra(graph, list(graph.vertices)[0])
            dijkstra_time = time.time() - start_time
            reachable = sum(1 for d in distances.values() if d != float("inf"))
            print(".4f")
        else:
            print("  Dijkstra: N/A (not weighted or too large)")

        print()


def create_small_graph():
    """Create a small test graph."""
    graph = Graph()
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    for u, v in edges:
        graph.add_edge(u, v)
    return graph


def create_sparse_graph(n, m):
    """Create a sparse random graph."""
    graph = Graph()
    vertices = [str(i) for i in range(n)]

    for v in vertices:
        graph.add_vertex(v)

    # Add m random edges
    random.seed(42)
    edges_added = 0
    while edges_added < m:
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v and not graph.has_edge(u, v):
            graph.add_edge(u, v)
            edges_added += 1

    return graph


def create_dense_graph(n):
    """Create a dense graph (almost complete)."""
    graph = Graph()
    vertices = [str(i) for i in range(n)]

    for v in vertices:
        graph.add_vertex(v)

    # Add edges between most pairs
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if random.random() < 0.8:  # 80% chance of edge
                weight = random.uniform(1, 10)
                graph.add_edge(vertices[i], vertices[j], weight)

    return graph


def demonstrate_graph_visualization():
    """Show graph structure and algorithm traces."""
    print("\n=== Graph Structure Visualization ===\n")

    # Create a small graph for visualization
    graph = Graph(directed=True, weighted=True)
    graph.add_edge("A", "B", 2.0)
    graph.add_edge("A", "C", 4.0)
    graph.add_edge("B", "D", 3.0)
    graph.add_edge("C", "D", 1.0)
    graph.add_edge("D", "E", 5.0)

    print("Graph Structure:")
    print(graph)
    print()

    print("Algorithm Traces:")
    print("DFS from A:", " -> ".join(GraphTraversal.dfs(graph, "A")))
    print("BFS from A:", " -> ".join(GraphTraversal.bfs(graph, "A")))
    print()

    print("Shortest Paths from A:")
    distances, predecessors = ShortestPaths.dijkstra(graph, "A")

    for vertex in sorted(graph.vertices):
        if distances[vertex] != float("inf"):
            path = ShortestPaths.reconstruct_path(predecessors, "A", vertex)
            if path:
                path_str = " -> ".join(path)
                print(".1f")
    print()


if __name__ == "__main__":
    demonstrate_graph_construction()
    demonstrate_graph_traversals()
    demonstrate_shortest_paths()
    demonstrate_graph_analysis()
    demonstrate_real_world_applications()
    demonstrate_algorithm_performance()
    demonstrate_graph_visualization()

    print("\n=== Graph Algorithms Summary ===")
    print("• Graph representations: adjacency lists for flexibility")
    print("• Traversal: DFS (depth-first) vs BFS (breadth-first)")
    print("• Shortest paths: Dijkstra (non-negative) vs Bellman-Ford (negative)")
    print("• Analysis: components, cycles, topological sort, MST")
    print("• Applications: social networks, routing, scheduling, dependencies")
    print("\nChapter 20: Graph algorithms mastered! 🕸️")
