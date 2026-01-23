# Personal Notes for Chapter 2

## Key Concepts Explained

### Sequence-Selection-Iteration: Programming Building Blocks
- **Sequence**: The default flow - statements execute one after another. Think of it as following a recipe step by step.
- **Selection**: "If this, then that" decisions. Like choosing different paths at a fork in the road based on conditions.
- **Iteration**: Doing something repeatedly. Like stirring a pot until the sauce thickens - you keep doing the same action until a condition is met.

### Variables and Objects Deep Dive
- **Variables are Labels**: `x = 42` creates a label "x" pointing to the number object 42. The variable doesn't "contain" the value - it references it.
- **Object Properties**:
  - **Identity**: `id(obj)` - unique identifier, like a person's social security number
  - **Type**: `type(obj)` - determines what operations are allowed
  - **Value**: The actual data stored
- **Assignment**: `y = x` makes y point to the same object as x. Changing y might affect x if the object is mutable.

### Mutable vs Immutable: When Things Can/Cannot Change
- **Mutable Objects**: Can be modified after creation
  - Lists: `my_list = [1,2,3]; my_list.append(4)` changes the list
  - Dicts: `my_dict['new_key'] = 'value'` adds to the dictionary
  - Why it matters: Multiple variables can reference the same mutable object
- **Immutable Objects**: Cannot be changed once created
  - Strings: `"hello"[0] = "H"` fails - creates new string instead
  - Tuples: `(1,2,3)[1] = 99` fails
  - Numbers: `x = 5; x += 1` creates new number object, doesn't modify 5

### Collections: Choosing the Right Tool
- **Lists**: When you need ordered data that changes frequently
- **Tuples**: When you need ordered data that shouldn't change (like coordinates)
- **Dictionaries**: When you need fast lookup by name/key (like a phone book)
- **Sets**: When you only care about unique items and membership testing
- **Strings**: For text data - they're sequences of characters

### Control Flow Patterns
- **if/elif/else**: Decision trees - "if condition A, do X; else if condition B, do Y; otherwise do Z"
- **while loops**: Keep going while a condition is true. Be careful of infinite loops!
- **for loops**: Process each item in a collection. Safer than while for most cases.
- **try/except**: "Try this risky operation, and if it fails, do this instead"
- **Functions**: Package code for reuse. Take inputs, return outputs.

### Modules and Code Organization
- **Modules**: Reusable code files. Like having a toolbox of functions you can import.
- **Imports**: `import math` brings in the math module's functions
- **Namespaces**: Prevent naming conflicts. `math.sqrt` vs your own `sqrt`
- **Script Guard**: `if __name__ == '__main__':` ensures code only runs when file is executed directly, not when imported

## Key Takeaways
- **Expressions vs Statements**: Expressions produce values (like `2 + 3`), statements perform actions (like `x = 5`)
- **Slicing Creates Copies**: `new_list = my_list[1:3]` creates a new list. Good for safety, but expensive for huge data.
- **Duck Typing**: Functions accept any object that behaves the right way. A function needing "something with a length" accepts strings, lists, tuples, etc.
- **Import Best Practices**: Use specific imports like `from math import sqrt` instead of `from math import *` to avoid namespace pollution.

## Common Pitfalls
- **Mutable Default Arguments**: `def func(lst=[]):` shares the same list across calls!
- **Modifying While Iterating**: Don't change a list while looping over it
- **String Concatenation in Loops**: Use `''.join()` instead of `+=` for efficiency

## Exercises/Thoughts
- **Object Identity**: Try `x = [1,2,3]; y = x; y.append(4); print(x)` - why does x change?
- **Slicing Practice**: Given `lst = [0,1,2,3,4,5]`, what do these return?
  - `lst[2:5]`, `lst[:3]`, `lst[::2]`, `lst[::-1]`, `lst[-2:]`
- **Duck Typing Experiment**: Write a function that takes "anything with a length" and see what you can pass it
- **Import Exploration**: Create a small module and experiment with different import styles