"""
Simple example for Chapter 1: Overview
Demonstrates basic Python concepts as per the book's approach.
"""


def greet(name):
    """A simple function to greet someone."""
    return f"Hello, {name}! Welcome to learning data structures in Python."


def add_numbers(a, b):
    """Basic addition to show expressions and evaluation."""
    return a + b


if __name__ == "__main__":
    print(greet("Learner"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
