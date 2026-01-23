"""
Chapter 3: Object-Oriented Programming - Implementation of key concepts
"""


# 3.1 A simple example - Vector class
class Vector:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except ValueError:
            self.x = 0.0
            self.y = 0.0

    def norm(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx, newy)

    def __str__(self):
        return f"({self.x}, {self.y})"


# 3.2 Encapsulation and the Public Interface
class Diary:
    def __init__(self, title):
        self.title = title  # public
        self._entries = []  # private

    def add_entry(self, entry):
        self._entries.append(entry)

    def _last_entry(self):  # private method
        return self._entries[-1] if self._entries else None


# 3.3 Inheritance and is a relationships
class Polygon:
    def __init__(self, sides, points):
        self._sides = sides
        self._points = list(points)
        if len(self._points) != self._sides:
            raise ValueError("Wrong number of points.")

    def sides(self):
        return self._sides


class Triangle(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)

    def __str__(self):
        return "I'm a triangle."


class Square(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 4, points)

    def __str__(self):
        return "I'm so square."


# 3.5 Composition and "has a" relationships
class MyLimitedList:
    def __init__(self):
        self._L = []

    def append(self, item):
        self._L.append(item)

    def __getitem__(self, index):
        return self._L[index]

    def __len__(self):
        return len(self._L)


# Demonstrating duck typing - any object with sides() method works
class PolygonCollection:
    def __init__(self):
        self._triangles = []
        self._squares = []

    def add(self, polygon):
        if polygon.sides() == 3:
            self._triangles.append(polygon)
        if polygon.sides() == 4:
            self._squares.append(polygon)


# A duck-typed object that works with PolygonCollection
class FakeTriangle:
    def sides(self):
        return 3

    def __str__(self):
        return "Fake triangle (duck typing)"


if __name__ == "__main__":
    # Vector example
    u = Vector(3, 4)
    v = Vector(3, 6)
    print(f"Vector u: {u}, norm: {u.norm()}")
    print(f"u + v = {u + v}")

    # Diary example
    diary = Diary("My Secret Diary")
    diary.add_entry("Had a great day!")
    print(f"Diary title: {diary.title}")
    # print(diary._last_entry())  # Should not access private

    # Inheritance example
    t = Triangle([(0, 0), (1, 0), (0, 1)])
    s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
    print(f"Triangle: {t}, sides: {t.sides()}")
    print(f"Square: {s}, sides: {s.sides()}")

    # Composition example
    mylist = MyLimitedList()
    mylist.append(1)
    mylist.append(2)
    print(f"MyLimitedList[0]: {mylist[0]}, len: {len(mylist)}")

    # Duck typing example
    collection = PolygonCollection()
    collection.add(t)  # real Triangle
    collection.add(s)  # real Square
    fake = FakeTriangle()
    collection.add(fake)  # fake triangle, but has sides() method
    print(f"Triangles in collection: {len(collection._triangles)}")
    print(f"Squares in collection: {len(collection._squares)}")
