import sys
import os

# Add root directory to path so imports work
sys.path.insert(0, os.path.join(os.getcwd(), "..", ".."))

from chapter_03_object_oriented_programming.code.oop_concepts import (
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
    """Test Vector class functionality."""
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
    print("✓ test_vector")


def test_vector_invalid_input():
    """Test Vector class with invalid input."""
    v = Vector("invalid", 5)
    assert v.x == 0.0
    assert v.y == 0.0
    print("✓ test_vector_invalid_input")


def test_diary():
    """Test Diary class functionality."""
    diary = Diary("Test Diary")
    assert diary.title == "Test Diary"
    assert diary._entries == []  # accessing private for testing

    diary.add_entry("Entry 1")
    diary.add_entry("Entry 2")
    assert len(diary._entries) == 2
    assert diary._last_entry() == "Entry 2"
    print("✓ test_diary")


def test_triangle():
    """Test Triangle class functionality."""
    t = Triangle([(0, 0), (1, 0), (0, 1)])
    assert t.sides() == 3
    assert str(t) == "I'm a triangle."
    assert t._sides == 3
    print("✓ test_triangle")


def test_square():
    """Test Square class functionality."""
    s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
    assert s.sides() == 4
    assert str(s) == "I'm so square."
    assert s._sides == 4
    print("✓ test_square")


def test_polygon_invalid():
    """Test polygon validation."""
    try:
        Triangle([(0, 0), (1, 0)])  # Wrong number of points
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected exception
    except Exception as e:
        assert False, f"Wrong exception type: {e}"
    print("✓ test_polygon_invalid")


def test_my_limited_list():
    """Test MyLimitedList functionality."""
    lst = MyLimitedList()
    assert len(lst) == 0

    lst.append(1)
    lst.append(2)
    assert len(lst) == 2
    assert lst[0] == 1
    assert lst[1] == 2
    print("✓ test_my_limited_list")


def test_polygon_collection():
    """Test PolygonCollection functionality."""
    collection = PolygonCollection()
    t = Triangle([(0, 0), (1, 0), (0, 1)])
    s = Square([(0, 0), (1, 0), (1, 1), (0, 1)])
    fake = FakeTriangle()

    collection.add(t)
    collection.add(s)
    collection.add(fake)

    assert len(collection._triangles) == 2  # t and fake
    assert len(collection._squares) == 1  # s
    print("✓ test_polygon_collection")


def test_duck_typing():
    """Test duck typing with FakeTriangle."""
    fake = FakeTriangle()
    assert fake.sides() == 3
    assert str(fake) == "Fake triangle (duck typing)"

    # Can be used anywhere a polygon-like object is expected
    collection = PolygonCollection()
    collection.add(fake)
    assert len(collection._triangles) == 1
    print("✓ test_duck_typing")


def run_all_tests():
    """Run all test functions."""
    print("Running Chapter 3 OOP Tests...")
    print("=" * 40)

    test_functions = [
        test_vector,
        test_vector_invalid_input,
        test_diary,
        test_triangle,
        test_square,
        test_polygon_invalid,
        test_my_limited_list,
        test_polygon_collection,
        test_duck_typing,
    ]

    for test_func in test_functions:
        try:
            test_func()
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
            return False

    print("=" * 40)
    print("All tests passed! ✓")
    return True


if __name__ == "__main__":
    run_all_tests()
