#!/usr/bin/env python3
"""
Examples demonstrating Chapter 3 OOP concepts.
Run this script to see interactive demonstrations.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from chapter_3_object_oriented_programming.code.oop_concepts import *

print("=== Chapter 3: Object-Oriented Programming Examples ===\n")

print("1. Vector Class (Simple Example):")
u = Vector(3, 4)
v = Vector(1, 2)
print(f"   u = {u}, norm = {u.norm()}")
print(f"   v = {v}, norm = {v.norm()}")
print(f"   u + v = {u + v}")
print()

print("2. Encapsulation (Diary Class):")
diary = Diary("My Learning Journal")
diary.add_entry("Learned about classes today!")
diary.add_entry("OOP is powerful.")
print(f"   Diary title: {diary.title}")
print(f"   Entries added: 2 (using public interface)")
# Note: Not accessing private _entries directly
print()

print("3. Inheritance (Polygon Hierarchy):")
t = Triangle([(0, 0), (1, 0), (0.5, 0.866)])
s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
print(f"   Triangle: {t} with {t.sides()} sides")
print(f"   Square: {s} with {s.sides()} sides")
print(f"   Both inherit from Polygon")
print()

print("4. Composition (MyLimitedList):")
mylist = MyLimitedList()
mylist.append("Python")
mylist.append("OOP")
mylist.append("Great!")
print(f"   List contents: {mylist[0]}, {mylist[1]}, {mylist[2]}")
print(f"   Length: {len(mylist)}")
print()

print("5. Duck Typing (PolygonCollection):")
collection = PolygonCollection()
real_triangle = Triangle([(0, 0), (2, 0), (1, 1.732)])
real_square = Square([(0, 0), (2, 0), (2, 2), (0, 2)])
fake_triangle = FakeTriangle()

collection.add(real_triangle)
collection.add(real_square)
collection.add(fake_triangle)

print(f"   Added real Triangle, real Square, and fake Triangle")
print(f"   Triangles in collection: {len(collection._triangles)}")
print(f"   Squares in collection: {len(collection._squares)}")
print(f"   (Fake triangle works because it has sides() method)")
print()

print("=== Key OOP Principles Demonstrated ===")
print("- Classes encapsulate data and behavior")
print("- Inheritance creates 'is a' relationships")
print("- Composition creates 'has a' relationships")
print("- Duck typing enables polymorphism without inheritance")
print("- Encapsulation protects internal state")
