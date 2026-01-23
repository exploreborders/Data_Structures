"""
Chapter 2: Basic Python - Implementation of key concepts
"""


# 2.1 Sequence, Selection, and Iteration
def demonstrate_sequence_selection_iteration():
    """Demonstrates the three programming constructs."""
    # Sequence: execute in order
    x = 5
    y = x * 2
    # Selection: conditional
    if y > 10:
        result = "big"
    else:
        result = "small"
    # Iteration: loop
    total = 0
    for i in range(5):
        total += i
    return result, total


# 2.2 Expressions and Evaluation
def expressions_example():
    """Shows expression evaluation."""
    a = 2 + 3 * 4  # 14
    b = (2 + 3) * 4  # 20
    c = 5 > 3  # True
    d = len("hello") == 5  # True
    return a, b, c, d


# 2.3 Variables, Types, and State
def variables_types_state():
    """Demonstrates variables and objects."""
    x = 42  # int
    y = 3.14  # float
    z = True  # bool
    s = "hello"  # str

    # Identity, type, value
    print(f"x id: {id(x)}, type: {type(x)}, value: {x}")

    # Assignment
    a = [1, 2, 3]  # mutable
    b = a  # same object
    b.append(4)
    print(f"a: {a}, b: {b}")  # both changed

    # Immutable
    t1 = (1, 2, 3)
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
