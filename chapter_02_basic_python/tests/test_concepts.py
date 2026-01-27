import sys
import os

# Add root directory to path so imports work
sys.path.insert(0, os.path.join(os.getcwd(), "..", ".."))

from chapter_02_basic_python.code.concepts import (
    demonstrate_sequence_selection_iteration,
    expressions_example,
    variables_types_state,
    collections_demo,
    common_operations,
    iteration_examples,
    control_flow_demo,
    example_function,
)


def test_sequence_selection_iteration():
    """Test sequence, selection, and iteration concepts."""
    result, total = demonstrate_sequence_selection_iteration()
    assert result == "small"  # x=5, y=10, 10 > 10 is False
    assert total == 10  # 0+1+2+3+4=10
    print("✓ test_sequence_selection_iteration")


def test_expressions():
    """Test expression evaluation."""
    a, b, c, d = expressions_example()
    assert a == 14  # 2 + 3*4
    assert b == 20  # (2+3)*4
    assert c is True
    assert d is True
    print("✓ test_expressions")


def test_variables_types_state():
    """Test variables, types, and state management."""
    # This function prints, but returns values
    x, y, z, s, a, t1 = variables_types_state()
    assert x == 42
    assert isinstance(y, float)
    assert z is True
    assert s == "hello"
    assert a == [1, 2, 3, 4]  # modified in function
    assert t1 == (1, 2, 3)
    print("✓ test_variables_types_state")


def test_collections():
    """Test collection types and operations."""
    s, s_slice, lst, tup, d, st = collections_demo()
    assert s == "Hello World"
    assert s_slice == "World"
    assert lst == [1, 2, 99, 4, 5, 6]
    assert tup == (1, 2, "three", 4.0)
    assert d == {"a": 1, "b": 2, "c": 3, "d": 4}
    assert st == {1, 2, 3}
    print("✓ test_collections")


def test_common_operations():
    """Test common collection operations."""
    length, slice1, slice2, membership = common_operations()
    assert length == 5
    assert slice1 == [20, 30, 40]
    assert slice2 == [50, 40, 30, 20, 10]
    assert membership is True
    print("✓ test_common_operations")


def test_iteration():
    """Test iteration patterns."""
    results = iteration_examples()
    assert results == [2, 4, 6, "a", "b", 0, 1, 2]
    print("✓ test_iteration")


def test_control_flow():
    """Test control flow constructs."""
    status, count, result = control_flow_demo()
    assert status == "big"
    assert count == 3
    assert result == 123
    print("✓ test_control_flow")


def test_example_function():
    """Test function definitions and calls."""
    assert example_function("test") == "test and default"
    assert example_function("hello", "world") == "hello and world"
    print("✓ test_example_function")


def run_all_tests():
    """Run all test functions."""
    print("Running Chapter 2 Tests...")
    print("=" * 40)

    test_functions = [
        test_sequence_selection_iteration,
        test_expressions,
        test_variables_types_state,
        test_collections,
        test_common_operations,
        test_iteration,
        test_control_flow,
        test_example_function,
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
