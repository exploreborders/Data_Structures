# Chapter 2: Basic Python

This chapter covers fundamental Python concepts: sequence, selection, and iteration; expressions and evaluation; variables, types, and state; collections (strings, lists, tuples, dictionaries, sets); common operations; iterating over collections; other control flow; and modules/imports.

## Key Concepts

### Sequence, Selection, Iteration: The Foundation of Programming
- **Sequence**: Executing statements one after another in order. This is the default behavior - Python runs your code line by line.
- **Selection**: Making decisions with conditional statements like `if`. Choose different paths based on conditions.
- **Iteration**: Repeating actions using loops. Process collections of items or repeat until a condition is met.

### Expressions and Evaluation
- **Expressions**: Code that produces a value (like `2 + 3` evaluates to `5`, or `x > 5` evaluates to `True`/`False`).
- **Evaluation**: Python computes expressions following operator precedence rules (multiplication before addition, etc.).
- **Statements**: Code that performs actions but doesn't produce values (like `x = 5` or `print("hello")`).

### Variables, Types, and State
- **Variables**: Named storage locations that hold references to objects. Variables are like labels you attach to boxes (objects).
- **Objects**: The actual data in memory. Every object has three properties:
  - **Identity**: Unique identifier (like a memory address)
  - **Type**: What kind of data it is (int, str, list, etc.)
  - **Value**: The actual data content
- **Mutable vs Immutable**: Mutable objects can be changed after creation (lists, dicts), immutable cannot (strings, tuples, numbers).

### Collections: Organizing Data
- **Strings (str)**: Sequences of characters. Immutable. Used for text data.
- **Lists (list)**: Ordered, mutable sequences. Can contain any types. Great for collections that change.
- **Tuples (tuple)**: Ordered, immutable sequences. Like lists but can't be modified.
- **Dictionaries (dict)**: Key-value mappings. Fast lookups by key. Like real dictionaries.
- **Sets (set)**: Unordered collections of unique items. Good for membership testing and removing duplicates.

### Common Operations on Collections
- **Length**: `len(collection)` - how many items
- **Indexing**: `collection[index]` - access specific items (0-based)
- **Slicing**: `collection[start:end]` - get sub-sequences
- **Membership**: `item in collection` - check if item exists
- **Iteration**: Loop over items with `for item in collection`

### Control Flow
- **if/elif/else**: Conditional execution based on boolean expressions
- **while**: Repeat while condition is true
- **for**: Iterate over sequences or ranges
- **try/except**: Handle errors gracefully
- **Functions**: Reusable code blocks that take inputs and return outputs

### Modules and Imports
- **Modules**: Python files that can be imported and reused
- **Import**: Bring code from other files into your current program
- **Namespaces**: Avoid naming conflicts by organizing code into separate scopes
- **Standard Library**: Built-in modules like `math`, `random`, `datetime`

## Examples with Explanations
- **Basic Expressions**: `2 + 3 * 4` evaluates to 14 (multiplication first)
- **Mutable Objects**: Lists can be modified: `my_list.append(5)`
- **Immutable Objects**: Strings cannot: `s = "hello"; s[0] = "H"` fails
- **List Operations**: `my_list = [1,2,3]; my_list[1] = 99` changes the list
- **Dictionary Usage**: `ages = {"Alice": 25, "Bob": 30}; ages["Alice"]` gets 25
- **Iteration**: `for num in [1,2,3]: print(num)` processes each item
- **Functions**: `def greet(name): return f"Hello {name}"` - reusable greeting
- **Imports**: `import math; math.sqrt(16)` uses external functionality