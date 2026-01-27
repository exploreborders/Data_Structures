import pytest
from chapter_01_overview.code.example import greet, add_numbers


def test_greet():
    assert (
        greet("World") == "Hello, World! Welcome to learning data structures in Python."
    )
    assert (
        greet("Alice") == "Hello, Alice! Welcome to learning data structures in Python."
    )


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
