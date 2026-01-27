"""
Chapter 21 Examples: Advanced Graph Search and Traversal Algorithms

Interactive demonstrations of topological sort, SCCs, MSTs, articulation points,
Eulerian paths, maximum flow, and advanced traversal techniques.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.insert(0, os.path.join(os.getcwd(), "..", "code"))

from advanced_graph_algorithms import (
    AdvancedGraphTraversal,
    TopologicalSort,
    StronglyConnectedComponents,
    MinimumSpanningTrees,
    GraphConnectivity,
    EulerianPaths,
    MaximumFlow,
    GraphSearchAnalysis,
)
from graph_implementations import Graph


def demonstrate_advanced_traversals():
    """Demonstrate advanced traversal techniques."""
    print("=== Advanced Graph Traversal Techniques ===\n")

    # Create a test graph
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("D", "G")
    graph.add_edge("E", "G")
    graph.add_edge("F", "G")

    print("Test Graph:")
    print(graph)
    print()

    # DFS with timestamps
    print("DFS with Discovery/Finishing Timestamps:")
    discovery, finishing, parent = AdvancedGraphTraversal.dfs_with_timestamps(
        graph, "A"
    )

    print("Vertex  Discovery  Finishing  Parent")
    print("-" * 35)
    for vertex in sorted(graph.vertices):
        parent_str = parent[vertex] if parent[vertex] else "None"
        print("4")
    print()

    # Bidirectional search
    print("Bidirectional Search (A to G):")
    path = AdvancedGraphTraversal.bidirectional_search(graph, "A", "G")
    if path:
        print(f"  Path found: {' -> '.join(path)} (length: {len(path) - 1})")
    else:
        print("  No path found")
    print()


def demonstrate_topological_sort():
    """Demonstrate topological sorting algorithms."""
    print("\n=== Topological Sort Algorithms ===\n")

    # Course prerequisite graph
    graph = Graph(directed=True)
    courses = {
        "CS101": "Introduction to Programming",
        "MATH101": "Discrete Mathematics",
        "CS201": "Data Structures",
        "CS202": "Algorithms",
        "CS301": "Advanced Data Structures",
        "CS302": "Computer Networks",
    }

    for course in courses:
        graph.add_vertex(course)

    # Add prerequisites
    prerequisites = [
        ("CS101", "CS201"),  # Intro -> Data Structures
        ("CS101", "CS202"),  # Intro -> Algorithms
        ("MATH101", "CS202"),  # Math -> Algorithms
        ("CS201", "CS301"),  # Data Structures -> Advanced DS
        ("CS202", "CS301"),  # Algorithms -> Advanced DS
        ("CS201", "CS302"),  # Data Structures -> Networks
    ]

    for prereq, course in prerequisites:
        graph.add_edge(prereq, course)

    print("Course Prerequisite Graph:")
    for course, name in courses.items():
        prereqs = [p for p, _ in graph.get_neighbors(course)]
        if prereqs:
            print(f"  {course} ({name}) requires: {', '.join(prereqs)}")
        else:
            print(f"  {course} ({name}) - no prerequisites")
    print()

    # Topological sort
    print("Topological Sort (valid course sequence):")
    topo_order = TopologicalSort.topological_sort_dfs(graph)

    if topo_order:
        print("  Valid course sequence:")
        for i, course in enumerate(topo_order, 1):
            print(f"    {i}. {course} - {courses[course]}")
        print("  ✓ This sequence respects all prerequisites!")
    else:
        print("  ✗ Cycle detected - impossible to satisfy prerequisites!")
    print()

    # Demonstrate cycle detection
    print("Testing Cycle Detection:")
    # Add a cycle
    graph.add_edge("CS302", "CS101")  # Networks requires Intro (creates cycle)

    topo_order_cyclic = TopologicalSort.topological_sort_dfs(graph)
    if topo_order_cyclic is None:
        print("  ✓ Cycle detected after adding CS302 -> CS101!")
        print("    This creates impossible prerequisite requirements.")
    print()


def demonstrate_strongly_connected_components():
    """Demonstrate strongly connected components."""
    print("\n=== Strongly Connected Components ===\n")

    # Create a complex directed graph
    graph = Graph(directed=True)

    # SCC 1: Web browsing cycle
    graph.add_edge("Homepage", "Search")
    graph.add_edge("Search", "Results")
    graph.add_edge("Results", "Homepage")  # Back to browsing

    # SCC 2: Social media cycle
    graph.add_edge("Feed", "Post")
    graph.add_edge("Post", "Comments")
    graph.add_edge("Comments", "Feed")  # Back to feed

    # SCC 3: Single page
    graph.add_vertex("About")

    # Connections between SCCs
    graph.add_edge("Results", "Feed")  # Search results lead to social media
    graph.add_edge("Comments", "About")  # Comments link to about page

    print("Web Navigation Graph:")
    print("• Homepage ↔ Search ↔ Results (browsing cycle)")
    print("• Feed ↔ Post ↔ Comments (social media cycle)")
    print("• About (single page)")
    print("• Cross-links between components")
    print()

    # Find SCCs
    sccs = StronglyConnectedComponents.kosaraju_scc(graph)

    print(f"Strongly Connected Components ({len(sccs)} found):")
    component_names = ["Web Browsing", "Social Media", "About Page"]
    for i, scc in enumerate(sccs):
        name = component_names[i] if i < len(component_names) else f"Component {i + 1}"
        print(f"  {name}: {scc}")

        if len(scc) > 1:
            print("    Users can navigate freely within this component")
        else:
            print("    Single page with no internal navigation")
    print()

    # Demonstrate reachability
    print("Reachability Analysis:")
    print("• Within SCC: Bidirectional navigation possible")
    print("• Between SCCs: May require external links")
    print("• SCCs represent 'strongly connected' regions")
    print()


def demonstrate_minimum_spanning_trees():
    """Demonstrate minimum spanning tree algorithms."""
    print("\n=== Minimum Spanning Trees ===\n")

    # City connection problem
    graph = Graph(weighted=True)
    cities = {
        "NYC": "New York City",
        "BOS": "Boston",
        "PHI": "Philadelphia",
        "DC": "Washington DC",
        "BAL": "Baltimore",
    }

    for city in cities:
        graph.add_vertex(city)

    # Add road connections with distances (miles)
    roads = [
        ("NYC", "BOS", 215),
        ("NYC", "PHI", 95),
        ("PHI", "DC", 140),
        ("DC", "BAL", 40),
        ("PHI", "BAL", 100),
        ("BOS", "PHI", 300),
        ("BOS", "DC", 450),
        ("NYC", "BAL", 190),
    ]

    for city1, city2, distance in roads:
        graph.add_edge(city1, city2, distance)

    print("City Connection Network:")
    print("Cities to connect:", list(cities.keys()))
    print("Available roads:")
    for c1, c2, dist in roads:
        print("6")
    print()

    # Prim's algorithm
    print("Prim's MST (starting from NYC):")
    mst_prim = MinimumSpanningTrees.prim_mst(graph)

    total_cost_prim = 0
    print("  Roads in MST:")
    for city1, city2, cost in mst_prim:
        total_cost_prim += cost
        print("6")
    print(f"  Total cost: {total_cost_prim} miles")
    print()

    # Kruskal's algorithm
    print("Kruskal's MST:")
    mst_kruskal = MinimumSpanningTrees.kruskal_mst(graph)

    total_cost_kruskal = 0
    print("  Roads in MST:")
    for city1, city2, cost in mst_kruskal:
        total_cost_kruskal += cost
        print("6")
    print(f"  Total cost: {total_cost_kruskal} miles")
    print()

    # Verify optimality
    if total_cost_prim == total_cost_kruskal:
        print("✓ Both algorithms found optimal solution!")
        print(f"  Minimum total road length: {total_cost_prim} miles")
    else:
        print("✗ Algorithms gave different results (unexpected)")

    print("✓ All cities connected with minimum total road cost!")
    print()


def demonstrate_articulation_points_and_bridges():
    """Demonstrate articulation points and bridges."""
    print("\n=== Articulation Points and Bridges ===\n")

    # Network infrastructure graph
    graph = Graph()

    # Core network
    servers = ["Server_A", "Server_B", "Server_C", "Server_D", "Server_E"]
    for server in servers:
        graph.add_vertex(server)

    # Network connections
    connections = [
        ("Server_A", "Server_B"),
        ("Server_B", "Server_C"),
        ("Server_C", "Server_D"),
        ("Server_D", "Server_E"),
        ("Server_B", "Server_F"),  # F is only connected through B
        ("Server_C", "Server_G"),  # G is only connected through C
    ]

    for s1, s2 in connections:
        graph.add_edge(s1, s2)
        graph.add_vertex(s2)  # Ensure all servers are added

    print("Network Infrastructure:")
    print("• Server_A - Server_E: Main backbone")
    print("• Server_F: Branch office (only connected via Server_B)")
    print("• Server_G: Remote office (only connected via Server_C)")
    print()

    # Find articulation points
    articulation_points = GraphConnectivity.find_articulation_points(graph)

    print("Articulation Points (critical servers):")
    if articulation_points:
        for server in sorted(articulation_points):
            if server == "Server_B":
                print(
                    f"  • {server}: Critical! Removing it disconnects branch office (Server_F)"
                )
            elif server == "Server_C":
                print(
                    f"  • {server}: Critical! Removing it disconnects remote office (Server_G)"
                )
            else:
                print(f"  • {server}: Critical server in main backbone")
    else:
        print("  No articulation points found")
    print()

    # Find bridges
    bridges = GraphConnectivity.find_bridges(graph)

    print("Bridges (critical connections):")
    if bridges:
        for u, v in bridges:
            if "Server_F" in [u, v]:
                print(
                    f"  • {u} ↔ {v}: Critical! This is the only connection to branch office"
                )
            elif "Server_G" in [u, v]:
                print(
                    f"  • {u} ↔ {v}: Critical! This is the only connection to remote office"
                )
            else:
                print(f"  • {u} ↔ {v}: Bridge in main network")
    else:
        print("  No bridges found")
    print()

    print("Network Reliability Insights:")
    print("• Articulation points represent single points of failure")
    print("• Bridges are critical links that cannot be bypassed")
    print("• Redundant connections improve network resilience")
    print()


def demonstrate_eulerian_paths():
    """Demonstrate Eulerian paths and circuits."""
    print("\n=== Eulerian Paths and Circuits ===\n")

    # Mail carrier problem (undirected)
    print("1. Mail Carrier Problem (Undirected Graph):")
    neighborhood = Graph()

    streets = ["A", "B", "C", "D", "E", "F"]
    for street in streets:
        neighborhood.add_vertex(street)

    # Street connections (undirected)
    routes = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("A", "F"),
        ("B", "E"),
        ("C", "F"),
        ("B", "D"),
    ]

    for s1, s2 in routes:
        neighborhood.add_edge(s1, s2)

    print("  Neighborhood street map:")
    print("  • Streets: A-B-C-D-E-F (connected in various ways)")
    print("  • Mail carrier must traverse each street exactly once")
    has_circuit = EulerianPaths.has_eulerian_circuit(neighborhood)
    has_path = EulerianPaths.has_eulerian_path(neighborhood)

    print(f"  Eulerian circuit possible: {has_circuit}")
    print(f"  Eulerian path possible: {has_path}")

    if has_circuit:
        print("  ✓ Mail carrier can start/end at same location!")
    elif has_path:
        print("  ✓ Mail carrier can traverse all streets (different start/end)!")
    else:
        print("  ✗ Impossible - some streets would be missed!")
    print()

    # Directed route planning
    print("2. Route Planning (Directed Graph):")
    city_graph = Graph(directed=True)

    intersections = ["North", "South", "East", "West", "Center"]
    for intersection in intersections:
        city_graph.add_vertex(intersection)

    # One-way streets
    one_way_streets = [
        ("North", "Center"),
        ("Center", "South"),
        ("East", "Center"),
        ("Center", "West"),
        ("West", "North"),
        ("South", "East"),
    ]

    for start, end in one_way_streets:
        city_graph.add_edge(start, end)

    print("  City one-way street system:")
    print("  • One-way streets create directed routes")
    print("  • Tourist bus must visit each street exactly once")
    has_circuit = EulerianPaths.has_eulerian_circuit(city_graph)
    has_path = EulerianPaths.has_eulerian_path(city_graph)

    print(f"  Eulerian circuit possible: {has_circuit}")
    print(f"  Eulerian path possible: {has_path}")

    if has_circuit:
        print("  ✓ Bus can return to starting point!")
    elif has_path:
        print("  ✓ Bus can visit all streets (but won't return to start)!")
    else:
        print("  ✗ Impossible route - some streets unreachable!")
    print()


def demonstrate_maximum_flow():
    """Demonstrate maximum flow algorithms."""
    print("\n=== Maximum Flow Algorithms ===\n")

    # Transportation network
    network = Graph(directed=True, weighted=True)

    locations = [
        "Factory",
        "Warehouse_A",
        "Warehouse_B",
        "Store_X",
        "Store_Y",
        "Store_Z",
    ]
    for location in locations:
        network.add_vertex(location)

    # Transportation capacities (tons per day)
    capacities = [
        ("Factory", "Warehouse_A", 10),
        ("Factory", "Warehouse_B", 15),
        ("Warehouse_A", "Store_X", 8),
        ("Warehouse_A", "Store_Y", 5),
        ("Warehouse_B", "Store_Y", 10),
        ("Warehouse_B", "Store_Z", 6),
        ("Store_X", "Store_Z", 12),  # Not used in optimal flow
    ]

    for src, dst, capacity in capacities:
        network.add_edge(src, dst, capacity)

    print("Supply Chain Network:")
    print("• Factory produces goods, warehouses distribute to stores")
    print("• Capacities represent tons per day")
    print("• Goal: Maximize flow from Factory to Stores")
    print()

    # Calculate maximum flow
    source = "Factory"
    # We need to create a super-sink for multiple destinations
    # For simplicity, let's measure flow to Store_Y as an example
    sink = "Store_Y"

    print(f"Maximum flow from {source} to {sink}:")
    max_flow = MaximumFlow.ford_fulkerson(network, source, sink)
    print(".1f")
    print()

    # Network interpretation
    print("Flow Analysis:")
    print(".1f")
    print("• This represents maximum goods that can flow through the network")
    print("• Limited by the 'bottleneck' capacities in the path")
    print("• Ford-Fulkerson finds the maximum possible flow")
    print()

    # Multiple sink example (simplified)
    print("Real-World Applications:")
    print("• Oil pipeline networks")
    print("• Internet traffic routing")
    print("• Assembly line optimization")
    print("• Financial transaction networks")
    print()


def demonstrate_algorithm_performance():
    """Compare performance of different algorithms."""
    print("\n=== Algorithm Performance Comparison ===\n")

    # Create test graphs of different sizes
    sizes = [10, 25, 50]

    for size in sizes:
        print(f"Graph with {size} vertices:")

        # Create a random directed graph
        graph = Graph(directed=True)
        vertices = [f"V{i}" for i in range(size)]

        for v in vertices:
            graph.add_vertex(v)

        # Add random edges (sparse graph)
        random.seed(42)
        for i in range(size):
            for j in range(size):
                if i != j and random.random() < 0.1:  # 10% chance
                    graph.add_edge(vertices[i], vertices[j])

        # Test topological sort
        start_time = time.time()
        topo_result = TopologicalSort.topological_sort_dfs(graph)
        topo_time = time.time() - start_time

        # Test SCC
        start_time = time.time()
        scc_result = StronglyConnectedComponents.kosaraju_scc(graph)
        scc_time = time.time() - start_time

        print("8.4f")
        print(f"    SCCs found: {len(scc_result)}")
        print(".4f")

    print()


def demonstrate_real_world_graph_problems():
    """Show how these algorithms solve real problems."""
    print("\n=== Real-World Problem Solving ===\n")

    # Task scheduling with dependencies
    print("1. Software Build System:")
    build_graph = Graph(directed=True)

    components = ["Parser", "Lexer", "AST", "CodeGen", "Linker", "Executable"]
    for comp in components:
        build_graph.add_vertex(comp)

    dependencies = [
        ("Lexer", "Parser"),
        ("Parser", "AST"),
        ("AST", "CodeGen"),
        ("CodeGen", "Linker"),
        ("Linker", "Executable"),
    ]

    for dep, comp in dependencies:
        build_graph.add_edge(dep, comp)

    print("  Build dependencies: Lexer → Parser → AST → CodeGen → Linker → Executable")

    topo_order = TopologicalSort.topological_sort_dfs(build_graph)
    if topo_order:
        print("  ✓ Valid build order: " + " → ".join(topo_order))
        print("  ✓ All dependencies satisfied!")
    print()

    # Flight routing (SCCs)
    print("2. Airline Route Network:")
    flights = Graph(directed=True)

    cities = ["NYC", "London", "Paris", "Tokyo", "Sydney"]
    for city in cities:
        flights.add_vertex(city)

    routes = [
        ("NYC", "London"),
        ("London", "NYC"),  # Bidirectional
        ("London", "Paris"),
        ("Paris", "London"),
        ("Paris", "Tokyo"),
        ("Tokyo", "Sydney"),
        ("Sydney", "NYC"),  # Round-the-world connection
    ]

    for src, dst in routes:
        flights.add_edge(src, dst)

    sccs = StronglyConnectedComponents.kosaraju_scc(flights)
    print(f"  Flight network has {len(sccs)} strongly connected components")

    # Analyze reachability
    print("  Route Analysis:")
    print("  • Within SCC: Round-trip flights possible")
    print("  • Between SCCs: One-way routes only")
    print("  • SCCs show which cities are mutually reachable")
    print()


if __name__ == "__main__":
    demonstrate_advanced_traversals()
    demonstrate_topological_sort()
    demonstrate_strongly_connected_components()
    demonstrate_minimum_spanning_trees()
    demonstrate_articulation_points_and_bridges()
    demonstrate_eulerian_paths()
    demonstrate_maximum_flow()
    demonstrate_algorithm_performance()
    demonstrate_real_world_graph_problems()

    print("\n=== Advanced Graph Algorithms Summary ===")
    print("• Topological Sort: Dependency ordering in DAGs")
    print("• SCCs: Finding strongly connected regions")
    print("• MSTs: Minimum spanning trees (Prim's & Kruskal's)")
    print("• Articulation Points: Critical vertices for connectivity")
    print("• Eulerian Paths: Traversing each edge exactly once")
    print("• Maximum Flow: Network flow optimization")
    print("• Advanced Traversals: Bidirectional search, DFS timestamps")
    print("\nChapter 21: Advanced graph search mastered! 🕸️✨")
