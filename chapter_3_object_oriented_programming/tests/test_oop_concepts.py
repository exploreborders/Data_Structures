import pytest
from chapter_3_object_oriented_programming.code.oop_concepts import (
    Vector,
    Diary,
    Polygon,
    Triangle,
    Square,
    MyLimitedList,
    PolygonCollection,
    FakeTriangle,
)


def test_vector():
    u = Vector(3, 4)
    assert u.x == 3.0
    assert u.y == 4.0
    assert u.norm() == 5.0

    v = Vector(3, 6)
    w = u + v
    assert isinstance(w, Vector)
    assert w.x == 6.0
    assert w.y == 10.0

    assert str(u) == "(3.0, 4.0)"


def test_vector_invalid_input():
    v = Vector("invalid", 5)
    assert v.x == 0.0
    assert v.y == 0.0


def test_diary():
    diary = Diary("Test Diary")
    assert diary.title == "Test Diary"
    assert diary._entries == []  # accessing private for testing

    diary.add_entry("Entry 1")
    diary.add_entry("Entry 2")
    assert len(diary._entries) == 2
    assert diary._last_entry() == "Entry 2"


def test_triangle():
    t = Triangle([(0, 0), (1, 0), (0, 1)])
    assert t.sides() == 3
    assert str(t) == "I'm a triangle."
    assert t._sides == 3


def test_square():
    s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
    assert s.sides() == 4
    assert str(s) == "I'm so square."
    assert s._sides == 4


def test_polygon_invalid():
    with pytest.raises(ValueError):
        Triangle([(0, 0), (1, 0)])  # Wrong number of points


def test_my_limited_list():
    lst = MyLimitedList()
    assert len(lst) == 0

    lst.append(1)
    lst.append(2)
    assert len(lst) == 2
    assert lst[0] == 1
    assert lst[1] == 2


def test_polygon_collection():
    collection = PolygonCollection()
    t = Triangle([(0, 0), (1, 0), (0, 1)])
    s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
    fake = FakeTriangle()

    collection.add(t)
    collection.add(s)
    collection.add(fake)

    assert len(collection._triangles) == 2  # t and fake
    assert len(collection._squares) == 1  # s


def test_duck_typing():
    fake = FakeTriangle()
    assert fake.sides() == 3
    assert str(fake) == "Fake triangle (duck typing)"

    # Can be used anywhere a polygon-like object is expected
    collection = PolygonCollection()
    collection.add(fake)
    assert len(collection._triangles) == 1
