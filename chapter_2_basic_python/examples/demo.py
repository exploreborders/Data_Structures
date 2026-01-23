#!/usr/bin/env python3
"""
Examples demonstrating Chapter 2 concepts interactively.
Run this script to see outputs.
"""

from chapter_2_basic_python.code.concepts import *

print("=== Chapter 2: Basic Python Examples ===\n")

print("1. Sequence, Selection, Iteration:")
print(demonstrate_sequence_selection_iteration())
print()

print("2. Expressions:")
print(expressions_example())
print()

print("3. Variables, Types, State (prints inside function):")
variables_types_state()
print()

print("4. Collections:")
print(collections_demo())
print()

print("5. Common Operations:")
print(common_operations())
print()

print("6. Iteration:")
print(iteration_examples())
print()

print("7. Control Flow:")
print(control_flow_demo())
print()

print("8. Functions:")
print(example_function("Python", "Programming"))
print()

# Additional interactive examples
print("=== Additional Examples ===")

# Mutable vs Immutable
print("Mutable vs Immutable:")
mutable = [1, 2, 3]
immutable = (1, 2, 3)
mutable.append(4)
# immutable.append(4)  # Error
print(f"Mutable: {mutable}")
print(f"Immutable: {immutable}")
print()

# Dict operations
print("Dictionary operations:")
d = {"name": "Alice", "age": 30}
print(f"Original: {d}")
d.update({"city": "NYC"})
print(f"Updated: {d}")
print(f"Keys: {list(d.keys())}")
print(f"Values: {list(d.values())}")
print()

# Set operations
print("Set operations:")
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(f"Union: {s1 | s2}")
print(f"Intersection: {s1 & s2}")
print(f"Difference: {s1 - s2}")
