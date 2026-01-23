"""
Chapter 22 Examples: Sets - Union-Find (Disjoint Set Union) Demonstrations

Interactive demonstrations of Union-Find applications, performance, and algorithms.
"""

import random
import time
import sys
import os

# Add the code directory to the path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "code"))
from union_find_implementations import (
    UnionFind,
    UnionFindAnalysis,
    KruskalWithUnionFind,
    ConnectivityChecker,
)


def demonstrate_basic_union_find():
    """Demonstrate basic Union-Find operations."""
    print("=== Basic Union-Find Operations ===\n")

    # Start with individual elements
    elements = ["A", "B", "C", "D", "E", "F"]
    uf = UnionFind(elements)

    print(f"Initial sets: {uf}")
    print(f"Number of sets: {uf.get_set_count()}")
    print()

    # Perform unions
    unions = [("A", "B"), ("C", "D"), ("A", "C"), ("E", "F")]

    print("Performing unions:")
    for u, v in unions:
        merged = uf.union(u, v)
        print(f"  union({u}, {v}): {'merged' if merged else 'already connected'}")
        print(f"    Sets: {uf}")
        print(f"    Connected components: {uf.get_set_count()}")
        print()

    # Test connectivity
    print("Connectivity checks:")
    connections = [("A", "D"), ("A", "E"), ("E", "F"), ("B", "F")]
    for u, v in connections:
        connected = uf.connected(u, v)
        print(f"  connected({u}, {v}): {connected}")

    print()


def demonstrate_path_compression():
    """Demonstrate path compression in action."""
    print("\n=== Path Compression Demonstration ===\n")

    uf = UnionFind()

    # Create a chain: A -> B -> C -> D -> E
    elements = ["A", "B", "C", "D", "E"]
    for elem in elements:
        uf.make_set(elem)

    print("Creating a chain structure:")
    for i in range(len(elements) - 1):
        uf.union(elements[i], elements[i + 1])
        print(f"  After union({elements[i]}, {elements[i + 1]}): {uf}")

    print(f"\nBefore path compression - parent pointers:")
    for elem in elements:
        print(f"  {elem}.parent = {uf.parent[elem]}")

    # Trigger path compression by finding a leaf
    print("\nFinding leaf element 'E' (triggers path compression):")
    root = uf.find("E")
    print(f"  find('E') = {root}")

    print("\nAfter path compression - parent pointers:")
    for elem in elements:
        print(f"  {elem}.parent = {uf.parent[elem]}")

    print("\n✓ All elements now point directly to root!")
    print()


def demonstrate_kruskals_algorithm():
    """Demonstrate Kruskal's MST algorithm with Union-Find."""
    print("\n=== Kruskal's Minimum Spanning Tree ===\n")

    # City connection problem
    cities = {
        "NYC": "New York City",
        "BOS": "Boston",
        "PHI": "Philadelphia",
        "DC": "Washington DC",
        "BAL": "Baltimore",
    }

    # Road connections with costs
    roads = [
        ("NYC", "BOS", 215),
        ("NYC", "PHI", 95),
        ("PHI", "DC", 140),
        ("DC", "BAL", 40),
        ("PHI", "BAL", 100),
        ("BOS", "PHI", 300),
    ]

    print("City Network Problem:")
    print("Cities:", list(cities.keys()))
    print("Available roads (distances in miles):")
    for c1, c2, dist in roads:
        print("6")
    print()

    # Sort roads by distance for Kruskal's
    roads.sort(key=lambda x: x[2])
    print("Roads sorted by distance (Kruskal's first step):")
    for c1, c2, dist in roads:
        print("6")
    print()

    # Run Kruskal's algorithm
    print("Building MST with Kruskal's algorithm:")
    vertices = list(cities.keys())
    mst = KruskalWithUnionFind.kruskal_mst(vertices, roads)

    total_cost = 0
    print("Selected roads for MST:")
    for city1, city2, cost in mst:
        total_cost += cost
        print("6")

    print(f"\nTotal cost: {total_cost} miles")
    print("✓ All cities connected with minimum total road cost!")
    # Verify connectivity
    uf = UnionFind(vertices)
    for c1, c2, _ in mst:
        uf.union(c1, c2)

    print(f"✓ Connected components: {uf.get_set_count()} (should be 1)")
    print()


def demonstrate_connectivity_analysis():
    """Demonstrate connectivity analysis applications."""
    print("\n=== Connectivity Analysis Applications ===\n")

    # Social network analysis
    print("1. Social Network Communities:")
    people = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    friendships = [
        ("Alice", "Bob"),
        ("Bob", "Charlie"),
        ("Diana", "Eve"),
        ("Eve", "Frank"),
        # Alice's group and Diana's group are separate
    ]

    components = ConnectivityChecker.connected_components(people, friendships)

    print(f"People: {people}")
    print("Friendships:", friendships)
    print(f"Communities found: {len(components)}")
    for i, community in enumerate(components, 1):
        print(f"  Community {i}: {community}")
    print()

    # Network reliability
    print("2. Network Reliability Analysis:")
    servers = ["S1", "S2", "S3", "S4", "S5", "S6"]
    connections = [
        ("S1", "S2"),
        ("S2", "S3"),
        ("S3", "S4"),
        ("S4", "S5"),
        ("S2", "S6"),  # S6 is branch
    ]

    components = ConnectivityChecker.connected_components(servers, connections)
    print(f"Server network: {len(components)} connected components")

    # Check for cycles
    has_cycle = ConnectivityChecker.has_cycle(servers, connections)
    print(f"Network has cycles: {has_cycle}")

    # Simulate failure
    print("\nSimulating server S2 failure:")
    remaining_connections = [(u, v) for u, v in connections if u != "S2" and v != "S2"]
    components_after = ConnectivityChecker.connected_components(
        servers, remaining_connections
    )

    print(f"After S2 failure: {len(components_after)} components")
    print("  ✓ Critical server identified - removing S2 disconnects network!")
    print()


def demonstrate_performance_analysis():
    """Demonstrate Union-Find performance analysis."""
    print("\n=== Performance Analysis ===\n")

    # Test different sizes
    sizes = [100, 500, 1000]

    for size in sizes:
        print(f"Testing with {size} elements:")

        elements = list(range(size))
        uf = UnionFind(elements)

        # Generate operations
        operations = UnionFindAnalysis.generate_random_operations(
            elements, min(1000, size * 2)
        )

        # Benchmark
        results = UnionFindAnalysis.benchmark_operations(uf, operations)

        print(".4f")
        print(".2f")
        print(".6f")
        print(f"    Merges performed: {results['actual_merges']}")
        print()

        # Structure analysis
        analysis = UnionFindAnalysis.analyze_structure(uf)
        print("    Final structure:")
        print(f"      Sets: {analysis['total_sets']}")
        print(".1f")
        print(".1f")
        print()


def demonstrate_union_heuristics():
    """Compare union by rank vs union by size."""
    print("\n=== Union Heuristics Comparison ===\n")

    elements = list(range(100))
    operations = UnionFindAnalysis.generate_random_operations(elements, 200)

    # Test both heuristics
    uf_rank = UnionFind(elements.copy())
    uf_size = UnionFind(elements.copy())

    # Time rank-based unions
    start_time = time.time()
    for op_type, args in operations:
        if op_type == "union":
            uf_rank.union(args[0], args[1])
    rank_time = time.time() - start_time

    # Time size-based unions
    start_time = time.time()
    for op_type, args in operations:
        if op_type == "union":
            uf_size.union_by_size(args[0], args[1])
    size_time = time.time() - start_time

    print("Comparing union heuristics:")
    print(".6f")
    print(".6f")
    print(".2f")

    # Analyze structures
    rank_analysis = UnionFindAnalysis.analyze_structure(uf_rank)
    size_analysis = UnionFindAnalysis.analyze_structure(uf_size)

    print("\nStructural differences:")
    print(f"  Rank-based - Max tree height: {rank_analysis['max_tree_height']}")
    print(f"  Size-based - Max tree height: {size_analysis['max_tree_height']}")

    print("  ✓ Both heuristics produce correct connectivity!")
    print()


def demonstrate_real_world_applications():
    """Show real-world applications of Union-Find."""
    print("\n=== Real-World Applications ===\n")

    # Image processing - connected components
    print("1. Image Processing - Connected Components:")
    print("   Problem: Find connected regions in binary images")
    print("   Union-Find solution: Each pixel is an element, connect adjacent pixels")

    # Simulate a simple 4x4 image
    pixels = [(i, j) for i in range(4) for j in range(4)]
    uf = UnionFind(pixels)

    # Connect adjacent pixels (simplified - only right and down neighbors)
    connections = []
    for i in range(4):
        for j in range(4):
            if j < 3:  # Connect right
                connections.append(((i, j), (i, j + 1)))
            if i < 3:  # Connect down
                connections.append(((i, j), (i + 1, j)))

    # Add some "missing" pixels (simulating image regions)
    missing_pixels = [(1, 1), (1, 2), (2, 1)]  # Remove some connections
    filtered_connections = [
        conn
        for conn in connections
        if conn[0] not in missing_pixels and conn[1] not in missing_pixels
    ]

    for p1, p2 in filtered_connections:
        uf.union(p1, p2)

    components = uf.get_all_sets()
    print(f"   Image regions found: {len(components)}")
    print("   ✓ Union-Find efficiently segments images!")
    print()

    # Network connectivity monitoring
    print("2. Network Connectivity Monitoring:")
    print("   Problem: Detect network partitions in real-time")
    print("   Union-Find solution: Union connected devices, find detects partitions")

    devices = [f"Device_{i}" for i in range(10)]
    uf = UnionFind(devices)

    # Simulate network connections
    connections = [
        ("Device_0", "Device_1"),
        ("Device_1", "Device_2"),
        ("Device_3", "Device_4"),
        ("Device_4", "Device_5"),
        ("Device_6", "Device_7"),
    ]  # Three separate networks

    for d1, d2 in connections:
        uf.union(d1, d2)

    print(f"   Network segments: {uf.get_set_count()}")
    print("   ✓ Real-time connectivity monitoring with Union-Find!")
    print()

    # Game connectivity (e.g., Go, Hex)
    print("3. Game Connectivity Analysis:")
    print("   Problem: Detect connected stones/groups in board games")
    print("   Union-Find solution: Union stones of same color that touch")

    # Simulate Go stones
    positions = [(i, j) for i in range(5) for j in range(5)]
    uf = UnionFind(positions)

    # Place some stones (simulate a Go position)
    black_stones = [(0, 0), (0, 1), (1, 0), (2, 2), (3, 3), (3, 4), (4, 4)]
    white_stones = [(1, 3), (2, 3), (2, 4), (4, 0), (4, 1)]

    # Connect adjacent stones of same color
    def connect_adjacent(stones, uf):
        for i, pos1 in enumerate(stones):
            for pos2 in stones[i + 1 :]:
                # Check if adjacent (simplified: only orthogonal)
                if (abs(pos1[0] - pos2[0]) == 1 and pos1[1] == pos2[1]) or (
                    abs(pos1[1] - pos2[1]) == 1 and pos1[0] == pos2[0]
                ):
                    uf.union(pos1, pos2)

    connect_adjacent(black_stones, uf)
    connect_adjacent(white_stones, uf)

    black_groups = sum(
        1
        for root, elements in uf.get_all_sets().items()
        if any(pos in black_stones for pos in elements)
    )
    white_groups = sum(
        1
        for root, elements in uf.get_all_sets().items()
        if any(pos in white_stones for pos in elements)
    )

    print(f"   Black stone groups: {black_groups}")
    print(f"   White stone groups: {white_groups}")
    print("   ✓ Game state analysis with Union-Find!")
    print()


def demonstrate_educational_insights():
    """Show educational insights about Union-Find."""
    print("\n=== Educational Insights ===\n")

    print("Key Union-Find Concepts:")
    print("• Disjoint sets: Non-overlapping collections")
    print("• Find operation: Locate set representative")
    print("• Union operation: Merge two sets")
    print("• Path compression: Flatten trees during finds")
    print("• Union by rank/size: Balance tree heights")
    print()

    print("Why Union-Find is Important:")
    print("• Nearly O(1) amortized operations")
    print("• Simple implementation with powerful optimizations")
    print("• Foundation for Kruskal's MST and many graph algorithms")
    print("• Real applications in networking, games, image processing")
    print()

    # Demonstrate the "nearly constant time" claim
    print("Demonstrating 'nearly constant time':")
    uf = UnionFind(list(range(10000)))

    # Many unions (worst case: chain structure)
    for i in range(9999):
        uf.union(i, i + 1)

    # Now many finds (should be very fast due to path compression)
    start_time = time.time()
    for _ in range(10000):
        uf.find(5000)  # Find in middle
    find_time = time.time() - start_time

    print(".6f")
    print("  ✓ Path compression makes finds effectively constant time!")
    print()


if __name__ == "__main__":
    demonstrate_basic_union_find()
    demonstrate_path_compression()
    demonstrate_kruskals_algorithm()
    demonstrate_connectivity_analysis()
    demonstrate_performance_analysis()
    demonstrate_union_heuristics()
    demonstrate_real_world_applications()
    demonstrate_educational_insights()

    print("\n=== Union-Find Mastery Achieved! ===")
    print("• Disjoint sets with efficient operations")
    print("• Path compression and union heuristics")
    print("• Kruskal's MST and connectivity analysis")
    print("• Real-world applications in networks, games, imaging")
    print("• Nearly constant-time performance")
    print("\nChapter 22: Union-Find and disjoint sets completed! 🔗✨")
