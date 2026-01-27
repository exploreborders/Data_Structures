import pytest
from chapter_0_basic_python.code.concepts import (
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
    result, total = demonstrate_sequence_selection_iteration()
    assert result == "small"  # x=5, y=10, 10 > 10 is False
    assert total == 10  # 0+1+2+3+4=10


def test_expressions():
    a, b, c, d = expressions_example()
    assert a == 14  # 2 + 3*4
    assert b == 20  # (2+3)*4
    assert c is True
    assert d is True


def test_variables_types_state():
    # This function prints, but returns values
    x, y, z, s, a, t1 = variables_types_state()
    assert x == 42
    assert isinstance(y, float)
    assert z is True
    assert s == "hello"
    assert a == [1, 2, 3, 4]  # modified in function
    assert t1 == (1, 2, 3)


def test_collections():
    s, s_slice, lst, tup, d, st = collections_demo()
    assert s == "Hello World"
    assert s_slice == "World"
    assert lst == [1, 2, 99, 4, 5, 6]
    assert tup == (1, 2, "three", 4.0)
    assert d == {"a": 1, "b": 2, "c": 3, "d": 4}
    assert st == {1, 2, 3}


def test_common_operations():
    length, slice1, slice2, membership = common_operations()
    assert length == 5
    assert slice1 == [20, 30, 40]
    assert slice2 == [50, 40, 30, 20, 10]
    assert membership is True


def test_iteration():
    results = iteration_examples()
    assert results == [2, 4, 6, "a", "b", 0, 1, 2]


def test_control_flow():
    status, count, result = control_flow_demo()
    assert status == "big"
    assert count == 3
    assert result == 123


def test_example_function():
    assert example_function("test") == "test and default"
    assert example_function("hello", "world") == "hello and world"
