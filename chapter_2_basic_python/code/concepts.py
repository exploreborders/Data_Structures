"""
Chapter 2: Basic Python - Implementation of key concepts

This file demonstrates fundamental Python programming concepts:
- Sequence: statements execute one after another
- Selection: conditional execution with if/else
- Iteration: loops that repeat actions
- Expressions: code that evaluates to values
- Variables: names that reference objects
- Collections: data structures for organizing information
- Control flow: directing program execution
"""


# 2.1 Sequence, Selection, and Iteration
def demonstrate_sequence_selection_iteration():
    """
    Demonstrates the three fundamental programming constructs.

    Sequence: Statements execute in order, like following a recipe.
    Selection: Choose different paths based on conditions.
    Iteration: Repeat actions, like counting or processing lists.
    """
    # SEQUENCE: These statements execute one after another
    x = 5  # First: assign 5 to x
    y = x * 2  # Second: multiply x by 2, assign to y (y = 10)

    # SELECTION: Choose what to do based on a condition
    if y > 10:  # Check if y is greater than 10
        result = "big"  # If true: y=10 is not >10, so skip this
    else:
        result = "small"  # If false: execute this (y is not big)

    # ITERATION: Repeat an action multiple times
    total = 0  # Start with total = 0
    for i in range(5):  # Loop 5 times: i = 0,1,2,3,4
        total += i  # Add current i to total: 0+0=0, 0+1=1, 1+2=3, 3+3=6, 6+4=10

    return result, total  # Return both the selection result and iteration total


# 2.2 Expressions and Evaluation
def expressions_example():
    """
    Shows how expressions are evaluated to produce values.

    Expressions are code that computes and returns a result.
    Python follows mathematical order of operations (PEMDAS).
    """
    a = 2 + 3 * 4  # Multiplication before addition: 3*4=12, then 2+12=14
    b = (2 + 3) * 4  # Parentheses force addition first: 2+3=5, then 5*4=20
    c = 5 > 3  # Comparison expression: evaluates to boolean True
    d = len("hello") == 5  # Function call + comparison: len("hello")=5, 5==5=True
    return a, b, c, d  # Return tuple of all expression results


# 2.3 Variables, Types, and State
def variables_types_state():
    """
    Demonstrates variables as references to objects.

    Variables are names that point to objects in memory.
    Objects have identity (unique ID), type (what kind), and value (the data).
    """
    # Create variables pointing to different types of objects
    x = 42  # int: whole numbers
    y = 3.14  # float: decimal numbers
    z = True  # bool: True/False values
    s = "hello"  # str: text/character sequences

    # Every object has three properties:
    print(f"x id: {id(x)}, type: {type(x)}, value: {x}")
    # id: unique identifier (memory address)
    # type: determines what operations are allowed
    # value: the actual data

    # MUTABLE vs IMMUTABLE objects
    a = [1, 2, 3]  # Lists are MUTABLE - can be changed
    b = a  # b points to SAME object as a (not a copy!)
    b.append(4)  # Modify the shared object through b
    print(f"a: {a}, b: {b}")  # Both show the change!

    # Immutable objects
    t1 = (1, 2, 3)  # Tuples are IMMUTABLE - cannot be changed
    # t1[0] = 0  # TypeError

    return x, y, z, s, a, t1


# 2.4 Collections
def collections_demo():
    """Examples of all collection types."""
    # String
    s = "Hello World"
    s_slice = s[6:11]  # "World"

    # List
    lst = [1, 2, 3, 4, 5]
    lst.append(6)
    lst[2] = 99

    # Tuple
    tup = (1, 2, "three", 4.0)

    # Dictionary
    d = {"a": 1, "b": 2, "c": 3}
    d["d"] = 4

    # Set
    st = {1, 2, 3, 3, 2}  # {1, 2, 3}

    return s, s_slice, lst, tup, d, st


# 2.5 Common operations
def common_operations():
    """Len, slicing, membership."""
    lst = [10, 20, 30, 40, 50]
    length = len(lst)  # 5
    slice1 = lst[1:4]  # [20, 30, 40]
    slice2 = lst[::-1]  # reverse
    membership = 30 in lst  # True

    return length, slice1, slice2, membership


# 2.6 Iterating over collections
def iteration_examples():
    """For loops over different collections."""
    results = []
    for item in [1, 2, 3]:
        results.append(item * 2)

    for key in {"a": 1, "b": 2}:
        results.append(key)

    for i in range(3):
        results.append(i)

    return results


# 2.7 Other control flow
def control_flow_demo():
    """If, while, try, functions."""
    # If
    x = 10
    if x > 5:
        status = "big"
    elif x > 0:
        status = "medium"
    else:
        status = "small"

    # While
    count = 0
    while count < 3:
        count += 1

    # Try
    try:
        result = int("123")
    except ValueError:
        result = 0

    return status, count, result


# Function with parameters
def example_function(param1, param2="default"):
    """Example function."""
    return f"{param1} and {param2}"


if __name__ == "__main__":
    print("Chapter 2 demonstrations:")
    print("Sequence/Selection/Iteration:", demonstrate_sequence_selection_iteration())
    print("Expressions:", expressions_example())
    variables_types_state()
    print("Collections:", collections_demo())
    print("Common operations:", common_operations())
    print("Iteration:", iteration_examples())
    print("Control flow:", control_flow_demo())
    print("Function call:", example_function("hello", "world"))
