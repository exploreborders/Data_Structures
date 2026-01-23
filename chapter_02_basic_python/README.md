# Chapter 2: Basic Python - Programming Fundamentals

This chapter establishes the foundational concepts of Python programming that form the basis for all subsequent chapters. It covers the core building blocks of imperative programming: sequence, selection, and iteration, along with Python's data model and control structures.

## The Three Pillars of Programming

### Sequence: Ordered Execution
**Concept**: Statements execute in the order they appear, like following a recipe step by step.

**Why Important**: Sequential execution is the default behavior of all programs. Understanding sequence helps you predict program flow and debug execution order issues.

**Examples**:
```python
# Simple sequence
x = 5              # Execute first
y = x * 2          # Execute second, uses result from first
result = y + 3     # Execute third, uses result from second
print(result)      # Execute fourth: prints 13
```

**Common Sequence Patterns**:
- Variable initialization before use
- Step-by-step data transformations
- Sequential file operations (open, read, close)

### Selection: Conditional Execution
**Concept**: Choose different execution paths based on conditions, using `if/elif/else` statements.

**Why Important**: Real-world programs must handle different scenarios and make decisions. Selection allows programs to adapt their behavior based on input, state, or external conditions.

**Detailed Examples**:
```python
# Basic conditional
age = 25
if age >= 18:
    status = "adult"
    can_vote = True
else:
    status = "minor"
    can_vote = False

# Multiple conditions with elif
temperature = 75
if temperature > 90:
    activity = "swimming"
elif temperature > 70:
    activity = "hiking"        # This executes
elif temperature > 50:
    activity = "walking"
else:
    activity = "reading"

# Nested conditionals
score = 85
if score >= 60:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"            # This executes
    else:
        grade = "C"
else:
    grade = "F"
```

**Best Practices**:
- Use clear, descriptive condition expressions
- Avoid deeply nested if statements (consider functions or early returns)
- Use elif for mutually exclusive conditions

### Iteration: Repetitive Execution
**Concept**: Execute code repeatedly using loops. Python provides `for` loops for definite iteration and `while` loops for conditional iteration.

**Why Important**: Many programming tasks involve processing collections of data or repeating operations until a condition is met. Iteration allows efficient handling of repetitive tasks.

**For Loops - Definite Iteration**:
```python
# Iterate over a collection
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterate over a range of numbers
for i in range(5):           # 0, 1, 2, 3, 4
    print(f"Count: {i}")

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(f"Number: {i}")

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(f"Even: {i}")

# Iterate with index using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**While Loops - Conditional Iteration**:
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While with complex condition
total = 0
number = 1
while total < 100 and number <= 10:
    total += number
    number += 1
print(f"Sum of first {number-1} numbers: {total}")

# Infinite loop with break
while True:
    user_input = input("Enter a number (or 'quit'): ")
    if user_input.lower() == 'quit':
        break
    try:
        number = float(user_input)
        print(f"Square: {number ** 2}")
    except ValueError:
        print("Please enter a valid number")
```

**Loop Control Statements**:
- `break`: Exit the loop immediately
- `continue`: Skip to the next iteration
- `else`: Execute after loop completes normally (not with break)

## Expressions and Evaluation

### Expression Types
**Arithmetic Expressions**:
```python
# Basic arithmetic
result = 2 + 3 * 4          # 14 (multiplication first)
adjusted = (2 + 3) * 4      # 20 (parentheses override precedence)

# Complex expressions
area = 3.14159 * radius ** 2
discriminant = b**2 - 4*a*c
```

**Comparison Expressions**:
```python
# Return boolean values
is_adult = age >= 18
is_even = number % 2 == 0
is_positive = value > 0
is_in_range = 0 <= score <= 100

# String comparisons
is_python = language == "Python"
starts_with_py = language.startswith("Py")
```

**Logical Expressions**:
```python
# Boolean logic
can_drive = has_license and age >= 16
needs_umbrella = is_raining or is_snowing
is_weekend = not is_weekday

# Short-circuit evaluation
# 'and' stops at first False
# 'or' stops at first True
result = expensive_operation() or default_value
```

### Operator Precedence
Python follows standard mathematical precedence:
1. Parentheses: `()`
2. Exponentiation: `**`
3. Unary operators: `+x`, `-x`
4. Multiplication, division, modulo: `*`, `/`, `//`, `%`
5. Addition, subtraction: `+`, `-`
6. Comparisons: `==`, `!=`, `<`, `<=`, `>`, `>=`
7. Logical NOT: `not`
8. Logical AND: `and`
9. Logical OR: `or`

## Variables, Types, and State

### Python's Object Model
Every value in Python is an object with three fundamental properties:

**Identity**: Unique identifier (`id(object)`) - like a social security number
**Type**: What kind of object it is (`type(object)`) - determines available operations
**Value**: The actual data content

### Variable Assignment
```python
# Variables are labels attached to objects
name = "Alice"      # name labels a string object
age = 30           # age labels an integer object
is_student = True  # is_student labels a boolean object

# Multiple variables can reference the same object
a = [1, 2, 3]
b = a              # b and a refer to the same list
b.append(4)        # Modifies the shared object
print(a)           # [1, 2, 3, 4] - both changed!
```

### Mutable vs Immutable Objects

**Immutable Objects** (cannot be changed after creation):
- **Numbers**: `int`, `float`, `complex`
- **Strings**: `str`
- **Tuples**: `tuple`
- **Frozen sets**: `frozenset`
- **Boolean**: `bool`
- **None**: `NoneType`

**Mutable Objects** (can be modified in place):
- **Lists**: `list`
- **Dictionaries**: `dict`
- **Sets**: `set`
- **Custom objects** (usually)

**Immutability Implications**:
```python
# Immutable: operations create new objects
greeting = "hello"
# greeting[0] = "H"  # TypeError!
new_greeting = "H" + greeting[1:]  # Creates new string

# Mutable: operations modify existing object
numbers = [1, 2, 3]
numbers.append(4)     # Modifies existing list
numbers[1] = 99       # Modifies existing list
```

## Collections: Organizing Related Data

### Strings: Immutable Text Sequences
```python
# String creation
single_quotes = 'Hello'
double_quotes = "World"
multi_line = """This is a
multi-line string"""

# String operations
greeting = "Hello" + " " + "World"    # Concatenation
repeated = "Ha" * 3                   # "HaHaHa"
length = len("Python")                # 6

# String methods
uppercase = "hello".upper()           # "HELLO"
capitalized = "python".capitalize()   # "Python"
contains_h = "h" in "Python"          # True

# String indexing and slicing
text = "Python"
first_char = text[0]      # "P"
last_char = text[-1]      # "n"
substring = text[1:4]     # "yth"
reversed_text = text[::-1] # "nohtyP"
```

### Lists: Mutable Ordered Collections
```python
# List creation
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
nested = [[1, 2], [3, 4]]

# List operations
numbers.append(6)         # [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)      # [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8])    # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# List modification
numbers[1] = 99           # [0, 99, 2, 3, 4, 5, 6, 7, 8]
numbers[2:5] = [20, 30, 40] # [0, 99, 20, 30, 40, 5, 6, 7, 8]

# List removal
removed = numbers.pop()   # Removes and returns last element
numbers.remove(99)        # Removes first occurrence of 99
del numbers[0]            # Removes element at index 0

# List utilities
length = len(numbers)
has_five = 5 in numbers
index_of_five = numbers.index(5)
count_of_twos = numbers.count(2)
```

### Tuples: Immutable Ordered Collections
```python
# Tuple creation
empty_tuple = ()
single_item = (42,)      # Note the comma!
coordinates = (3, 4)
rgb_color = (255, 0, 128)

# Tuple unpacking
x, y = coordinates       # x=3, y=4
r, g, b = rgb_color      # r=255, g=0, b=128

# Tuples are immutable
# coordinates[0] = 5     # TypeError!

# But you can create new tuples
new_coords = (5, coordinates[1])  # (5, 4)
```

### Dictionaries: Key-Value Mappings
```python
# Dictionary creation
empty_dict = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Alternative creation
grades = dict(math=95, english=87, science=92)

# Dictionary operations
person["email"] = "alice@example.com"    # Add new key-value
person["age"] = 31                       # Update existing value
del person["city"]                       # Remove key-value pair

# Dictionary access
name = person["name"]                    # "Alice"
age = person.get("age", 0)              # 31 (with default)
has_email = "email" in person           # True

# Dictionary views
keys = list(person.keys())              # ["name", "age", "email"]
values = list(person.values())          # ["Alice", 31, "alice@example.com"]
items = list(person.items())            # [("name", "Alice"), ("age", 31), ...]

# Dictionary methods
person_copy = person.copy()             # Shallow copy
person.clear()                          # Remove all items
```

### Sets: Unordered Unique Collections
```python
# Set creation
empty_set = set()       # Not {} - that's an empty dict!
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} - duplicates removed

# Set operations
numbers.add(6)          # {1, 2, 3, 4, 5, 6}
numbers.remove(3)       # {1, 2, 4, 5, 6}
numbers.discard(10)     # No error if item doesn't exist

# Mathematical set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

union = set1 | set2                # {1, 2, 3, 4}
intersection = set1 & set2         # {2, 3}
difference = set1 - set2           # {1}
symmetric_diff = set1 ^ set2       # {1, 4}

# Set comparisons
is_subset = {2, 3} <= set1         # True
is_superset = set1 >= {2, 3}       # True
are_equal = {1, 2, 3} == {3, 2, 1} # True (order doesn't matter)
```

## Control Flow: Exception Handling

### Try-Except Blocks
```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exception types
try:
    number = int("not_a_number")
except ValueError:
    print("Invalid number format")
except TypeError:
    print("Wrong data type")

# Catch-all exception handling
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")

# Finally block (always executes)
file = None
try:
    file = open("data.txt", "r")
    content = file.read()
    # Process content
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()  # Always close the file
```

### Raising Exceptions
```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unreasonably high")

# Usage
try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
```

## Functions: Reusable Code Blocks

### Function Definition and Calling
```python
# Function definition
def greet_person(name, greeting="Hello"):
    """
    Return a personalized greeting.

    Args:
        name: The person's name
        greeting: The greeting to use (default: "Hello")

    Returns:
        A formatted greeting string
    """
    return f"{greeting}, {name}!"

# Function calls
simple_greeting = greet_person("Alice")              # "Hello, Alice!"
custom_greeting = greet_person("Bob", "Hi")          # "Hi, Bob!"
```

### Function Parameters
```python
# Required parameters
def add(a, b):
    return a + b

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# Variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Keyword arguments
def create_person(**info):
    return {
        "name": info.get("name", "Unknown"),
        "age": info.get("age", 0),
        "city": info.get("city", "Unknown")
    }

# Usage
result1 = add(3, 5)                          # 8
result2 = power(3)                            # 9 (3^2)
result3 = power(2, 3)                         # 8 (2^3)
result4 = sum_all(1, 2, 3, 4, 5)             # 15
person = create_person(name="Alice", age=30)  # {"name": "Alice", "age": 30, "city": "Unknown"}
```

### Function Scope and Lifetime
```python
global_variable = "I'm global"

def my_function():
    local_variable = "I'm local"
    print(global_variable)    # Can access global
    print(local_variable)     # Can access local

my_function()
# print(local_var)  # NameError - not accessible here
```

## Modules and Imports

### Module Creation
A module is simply a `.py` file. Create `math_utils.py`:
```python
# math_utils.py
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

def calculate_sphere_volume(radius):
    return 4/3 * 3.14159 * radius ** 3

PI = 3.14159
```

### Import Methods
```python
# Import entire module
import math_utils
area = math_utils.calculate_circle_area(5)

# Import specific items
from math_utils import calculate_circle_area, PI
area = calculate_circle_area(5)

# Import with alias
import math_utils as mu
area = mu.calculate_circle_area(5)

# Import all (generally discouraged)
from math_utils import *
area = calculate_circle_area(5)
```

### Module Search Path
```python
import sys
print(sys.path)  # List of directories Python searches for modules

# Add custom directory to path
sys.path.append('/path/to/my/modules')
```

### Packages: Organizing Modules
```python
# Directory structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#       __init__.py
#       submodule.py

# Import from package
from mypackage import module1
from mypackage.subpackage import submodule
```

### The `__name__` Variable
```python
# my_module.py
def main():
    print("Running as main script")

if __name__ == "__main__":
    main()  # Only runs when file is executed directly
```

## Chapter 2 Best Practices

### Code Style and Readability
- Use descriptive variable and function names
- Add comments for complex logic
- Follow PEP 8 style guidelines
- Use consistent indentation

### Common Patterns
- List comprehensions for simple transformations
- Generator expressions for memory efficiency
- Context managers for resource management
- Duck typing for flexible interfaces

### Debugging Techniques
- Use `print()` statements for simple debugging
- Leverage Python's interactive debugger (`pdb`)
- Add assertions to verify assumptions
- Write tests to isolate and identify issues

This comprehensive foundation in Python basics provides the groundwork for understanding data structures and algorithms in subsequent chapters.